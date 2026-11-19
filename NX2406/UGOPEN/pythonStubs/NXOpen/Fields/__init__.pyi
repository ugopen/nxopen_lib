from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  This class defines a complex value that is internally 
##         backed up by a  field or two expressions. 
## 
##   <br>  Created in NX11.0.0  <br> 

class ComplexScalarFieldWrapper(NXOpen.NXObject): 
    """ This class defines a complex value that is internally 
        backed up by a  field or two expressions. """


    ##  Returns the indicated implementation if the wrapper is backed up by expressions; 
    ##             NULL otherwise 
    ##  @return expression (@link NXOpen.Expression NXOpen.Expression@endlink):  existing expression or NULL .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetExpression(self) -> NXOpen.Expression:
        """
         Returns the indicated implementation if the wrapper is backed up by expressions; 
                    NULL otherwise 
         @return expression (@link NXOpen.Expression NXOpen.Expression@endlink):  existing expression or NULL .
        """
        pass
    
    ##  Returns the implementation if the wrapper is backed up by a field; 
    ##             NULL otherwise 
    ##  @return field (@link Field NXOpen.Fields.Field@endlink):  existing field or NULL .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetField(self) -> Field:
        """
         Returns the implementation if the wrapper is backed up by a field; 
                    NULL otherwise 
         @return field (@link Field NXOpen.Fields.Field@endlink):  existing field or NULL .
        """
        pass
    
    ##  Returns the indicated implementation if the wrapper is backed up by expressions; 
    ##             NULL otherwise 
    ##  @return expression (@link NXOpen.Expression NXOpen.Expression@endlink):  existing expression or NULL .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetImaginaryExpression(self) -> NXOpen.Expression:
        """
         Returns the indicated implementation if the wrapper is backed up by expressions; 
                    NULL otherwise 
         @return expression (@link NXOpen.Expression NXOpen.Expression@endlink):  existing expression or NULL .
        """
        pass
    
    ##  Sets the implementation of the wrapper to the specified expressions 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2206.0.0.  Use @link NXOpen::Fields::ComplexScalarFieldWrapper::SetExpressions NXOpen::Fields::ComplexScalarFieldWrapper::SetExpressions@endlink , @link NXOpen::Fields::ComplexScalarFieldWrapper::SetRealImaginaryExpressions NXOpen::Fields::ComplexScalarFieldWrapper::SetRealImaginaryExpressions@endlink , or @link NXOpen::Fields::ComplexScalarFieldWrapper::SetMagnitudePhaseExpressions NXOpen::Fields::ComplexScalarFieldWrapper::SetMagnitudePhaseExpressions@endlink  instead.  <br> 

    ## License requirements: None.
    ## 
    ## <param name="expression"> (@link NXOpen.Expression NXOpen.Expression@endlink)  existing expressions that will be this wrapper's value </param>
    def SetExpression(self, expression: NXOpen.Expression) -> None:
        """
         Sets the implementation of the wrapper to the specified expressions 
        """
        pass
    
    ##  Sets the implementation of the wrapper to the specified expressions 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="expressions"> (@link NXOpen.Expression List[NXOpen.Expression]@endlink)  existing expressions that will be this wrapper's value </param>
    def SetExpressions(self, expressions: List[NXOpen.Expression]) -> None:
        """
         Sets the implementation of the wrapper to the specified expressions 
        """
        pass
    
    ##  Sets the implementation of the wrapper to the specified field 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="field"> (@link Field NXOpen.Fields.Field@endlink)  an existing field that will be this wrapper's value </param>
    def SetField(self, field: Field) -> None:
        """
         Sets the implementation of the wrapper to the specified field 
        """
        pass
    
    ##  Sets the implementation of the wrapper to the specified field and scale factor 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="field"> (@link Field NXOpen.Fields.Field@endlink)  an existing field that will be this wrapper's value </param>
    ## <param name="scale_factor"> (float)  the field will be multiplied by this scale factor when being evaluated </param>
    def SetFieldWithScaleFactor(self, field: Field, scale_factor: float) -> None:
        """
         Sets the implementation of the wrapper to the specified field and scale factor 
        """
        pass
    
    ##  Sets the implementation of the wrapper to the specified expressions 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2206.0.0.  Use @link NXOpen::Fields::ComplexScalarFieldWrapper::SetExpressions NXOpen::Fields::ComplexScalarFieldWrapper::SetExpressions@endlink , @link NXOpen::Fields::ComplexScalarFieldWrapper::SetRealImaginaryExpressions NXOpen::Fields::ComplexScalarFieldWrapper::SetRealImaginaryExpressions@endlink , or @link NXOpen::Fields::ComplexScalarFieldWrapper::SetMagnitudePhaseExpressions NXOpen::Fields::ComplexScalarFieldWrapper::SetMagnitudePhaseExpressions@endlink  instead.  <br> 

    ## License requirements: None.
    ## 
    ## <param name="expression"> (@link NXOpen.Expression NXOpen.Expression@endlink)  existing expressions that will be this wrapper's value </param>
    def SetImaginaryExpression(self, expression: NXOpen.Expression) -> None:
        """
         Sets the implementation of the wrapper to the specified expressions 
        """
        pass
    
    ##  Sets the implementation of the wrapper to the specified expressions 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="expressions"> (@link NXOpen.Expression List[NXOpen.Expression]@endlink)  existing expressions that will be this wrapper's value </param>
    def SetMagnitudePhaseExpressions(self, expressions: List[NXOpen.Expression]) -> None:
        """
         Sets the implementation of the wrapper to the specified expressions 
        """
        pass
    
    ##  Sets the implementation of the wrapper to the specified expressions 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="expressions"> (@link NXOpen.Expression List[NXOpen.Expression]@endlink)  existing expressions that will be this wrapper's value </param>
    def SetRealImaginaryExpressions(self, expressions: List[NXOpen.Expression]) -> None:
        """
         Sets the implementation of the wrapper to the specified expressions 
        """
        pass
    
import NXOpen
##  This class defines a complex value that is internally 
##         backed up by a  field or six expressions. 
## 
##   <br>  Created in NX12.0.0  <br> 

class ComplexVectorFieldWrapper(NXOpen.NXObject): 
    """ This class defines a complex value that is internally 
        backed up by a  field or six expressions. """


    ##  Returns the indicated implementation if the wrapper is backed up by expressions; 
    ##             NULL otherwise 
    ##  @return expression (@link NXOpen.Expression NXOpen.Expression@endlink):  existing expression or NULL .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  0, 1 or 2 </param>
    def GetExpressionByIndex(self, index: int) -> NXOpen.Expression:
        """
         Returns the indicated implementation if the wrapper is backed up by expressions; 
                    NULL otherwise 
         @return expression (@link NXOpen.Expression NXOpen.Expression@endlink):  existing expression or NULL .
        """
        pass
    
    ##  Returns the implementation if the wrapper is backed up by a field; 
    ##             NULL otherwise 
    ##  @return field (@link Field NXOpen.Fields.Field@endlink):  existing field or NULL .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    def GetField(self) -> Field:
        """
         Returns the implementation if the wrapper is backed up by a field; 
                    NULL otherwise 
         @return field (@link Field NXOpen.Fields.Field@endlink):  existing field or NULL .
        """
        pass
    
    ##  Returns the indicated implementation if the wrapper is backed up by expressions; 
    ##             NULL otherwise 
    ##  @return expression (@link NXOpen.Expression NXOpen.Expression@endlink):  existing expression or NULL .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  0, 1 or 2 </param>
    def GetImaginaryExpressionByIndex(self, index: int) -> NXOpen.Expression:
        """
         Returns the indicated implementation if the wrapper is backed up by expressions; 
                    NULL otherwise 
         @return expression (@link NXOpen.Expression NXOpen.Expression@endlink):  existing expression or NULL .
        """
        pass
    
    ##  Sets the implementation of the wrapper to the specified expressions 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="expressions"> (@link NXOpen.Expression List[NXOpen.Expression]@endlink)  existing expressions that will be this wrapper's value </param>
    def SetExpressions(self, expressions: List[NXOpen.Expression]) -> None:
        """
         Sets the implementation of the wrapper to the specified expressions 
        """
        pass
    
    ##  Sets the implementation of the wrapper to the specified field 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="field"> (@link Field NXOpen.Fields.Field@endlink)  an existing field that will be this wrapper's value </param>
    ## <param name="scale_factor"> (float)  the field will be multiplied by this scale factor when being evaluated </param>
    def SetField(self, field: Field, scale_factor: float) -> None:
        """
         Sets the implementation of the wrapper to the specified field 
        """
        pass
    
    ##  Sets the implementation of the wrapper to the specified expressions 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="expressions"> (@link NXOpen.Expression List[NXOpen.Expression]@endlink)  existing expressions that will be this wrapper's value </param>
    def SetImaginaryExpressions(self, expressions: List[NXOpen.Expression]) -> None:
        """
         Sets the implementation of the wrapper to the specified expressions 
        """
        pass
    
import NXOpen
##   @brief  Represents a builder class for editing display properties of a @link NXOpen::Fields::Field NXOpen::Fields::Field@endlink   
## 
##  
##      <br> Used to edit a @link NXOpen::Fields::Field NXOpen::Fields::Field@endlink  display properties. <br> 
##      <br> To create a new instance of this class, use @link NXOpen::Fields::FieldManager::CreateDisplayPropertiesBuilder  NXOpen::Fields::FieldManager::CreateDisplayPropertiesBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DepCalcSymblSize </term> <description> 
##  
## 0.1 </description> </item> 
## 
## <item><term> 
##  
## DepDispType </term> <description> 
##  
## Symbol </description> </item> 
## 
## <item><term> 
##  
## DepDomColor </term> <description> 
##  
## Inherit </description> </item> 
## 
## <item><term> 
##  
## DepLabelValues </term> <description> 
##  
## None </description> </item> 
## 
## <item><term> 
##  
## DepRangeMax </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DepRangeMin </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolution </term> <description> 
##  
## Standard </description> </item> 
## 
## <item><term> 
##  
## FaceAnalysis </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## FieldQuantity </term> <description> 
##  
## Type0 </description> </item> 
## 
## <item><term> 
##  
## HeteroTblDispOption </term> <description> 
##  
## ShowAverageValue </description> </item> 
## 
## <item><term> 
##  
## IndepDispType </term> <description> 
##  
## Hide </description> </item> 
## 
## <item><term> 
##  
## Layer </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## LegendPosition </term> <description> 
##  
## Left </description> </item> 
## 
## <item><term> 
##  
## LineFont </term> <description> 
##  
## Solid </description> </item> 
## 
## <item><term> 
##  
## LineWidth </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## PartiallyShaded </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## PrimaryVar.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## Range </term> <description> 
##  
## Auto </description> </item> 
## 
## <item><term> 
##  
## RangeMax </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## RangeMin </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## ShowAxis </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ShowDefaultVal </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ShowDescription </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ShowLabels </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ShowMapTopo </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ShowName </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ShowOverflowValues </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ShowSrcTblVals </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## ShowUndefValues </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ShowUnderflowValues </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## SpectrumLevels </term> <description> 
##  
## 3 </description> </item> 
## 
## <item><term> 
##  
## SurfaceOffset </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## TblDepDispType </term> <description> 
##  
## Symbol </description> </item> 
## 
## <item><term> 
##  
## TblDepPtType (deprecated) </term> <description> 
##  
## Hide </description> </item> 
## 
## <item><term> 
##  
## TblIndepPtType (deprecated) </term> <description> 
##  
## Hide </description> </item> 
## 
## <item><term> 
##  
## TblSurfaceOffset </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## Translucency </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## XMax.Value </term> <description> 
##  
## 0 (millimeters part), 1 (inches part) </description> </item> 
## 
## <item><term> 
##  
## XMin.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## XNum </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## YMax.Value </term> <description> 
##  
## 0 (millimeters part), 1 (inches part) </description> </item> 
## 
## <item><term> 
##  
## YMin.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## YNum </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## ZMax.Value </term> <description> 
##  
## 0 (millimeters part), 1 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ZMin.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ZNum </term> <description> 
##  
## 1 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX6.0.1  <br> 

class DisplayPropertiesBuilder(NXOpen.Builder): 
    """ <summary> Represents a builder class for editing display properties of a <ja_class>NXOpen.Fields.Field</ja_class> </summary>
    <para>Used to edit a <ja_class>NXOpen.Fields.Field</ja_class> display properties.</para>
    """


    ##  Balance Strain Field Type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Xx</term><description> 
    ## </description> </item><item><term> 
    ## Yy</term><description> 
    ## </description> </item><item><term> 
    ## Zz</term><description> 
    ## </description> </item><item><term> 
    ## Xy</term><description> 
    ## </description> </item><item><term> 
    ## Yz</term><description> 
    ## </description> </item><item><term> 
    ## Zx</term><description> 
    ## </description> </item><item><term> 
    ## OffSetXX</term><description> 
    ## </description> </item><item><term> 
    ## OffSetYY</term><description> 
    ## </description> </item><item><term> 
    ## OffSetZZ</term><description> 
    ## </description> </item><item><term> 
    ## OffSetXY</term><description> 
    ## </description> </item><item><term> 
    ## OffSetYZ</term><description> 
    ## </description> </item><item><term> 
    ## OffSetZX</term><description> 
    ## </description> </item></list>
    class BalStrainType(Enum):
        """
        Members Include: <Xx> <Yy> <Zz> <Xy> <Yz> <Zx> <OffSetXX> <OffSetYY> <OffSetZZ> <OffSetXY> <OffSetYZ> <OffSetZX>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.BalStrainType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Complex Scalar Field Type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Mag</term><description> 
    ## </description> </item><item><term> 
    ## Real</term><description> 
    ## </description> </item><item><term> 
    ## Imaginary</term><description> 
    ## </description> </item><item><term> 
    ## Phase</term><description> 
    ## </description> </item></list>
    class ComplexScalarType(Enum):
        """
        Members Include: <Mag> <Real> <Imaginary> <Phase>
        """
        Mag: int
        Real: int
        Imaginary: int
        Phase: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.ComplexScalarType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Complex Vector Field Type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## XReal</term><description> 
    ## </description> </item><item><term> 
    ## YReal</term><description> 
    ## </description> </item><item><term> 
    ## ZReal</term><description> 
    ## </description> </item><item><term> 
    ## XImaginary</term><description> 
    ## </description> </item><item><term> 
    ## YImaginary</term><description> 
    ## </description> </item><item><term> 
    ## ZImaginary</term><description> 
    ## </description> </item></list>
    class ComplexVectorType(Enum):
        """
        Members Include: <XReal> <YReal> <ZReal> <XImaginary> <YImaginary> <ZImaginary>
        """
        XReal: int
        YReal: int
        ZReal: int
        XImaginary: int
        YImaginary: int
        ZImaginary: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.ComplexVectorType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Field Dep Disp Type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Symbol</term><description> 
    ## </description> </item><item><term> 
    ## Surface</term><description> 
    ## </description> </item><item><term> 
    ## SurfaceEdges</term><description> 
    ## </description> </item><item><term> 
    ## Hide</term><description> 
    ## </description> </item></list>
    class DepDispTypeEnum(Enum):
        """
        Members Include: <Symbol> <Surface> <SurfaceEdges> <Hide>
        """
        Symbol: int
        Surface: int
        SurfaceEdges: int
        Hide: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.DepDispTypeEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Field Dep Dom Color 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Inherit</term><description> 
    ## </description> </item><item><term> 
    ## Specified</term><description> 
    ## </description> </item><item><term> 
    ## Spectrum</term><description> 
    ## </description> </item></list>
    class DepDomColorEnum(Enum):
        """
        Members Include: <Inherit> <Specified> <Spectrum>
        """
        Inherit: int
        Specified: int
        Spectrum: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.DepDomColorEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Field Dep Label Value 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ## </description> </item><item><term> 
    ## MinimumMaximum</term><description> 
    ## </description> </item><item><term> 
    ## Maximum</term><description> 
    ## </description> </item><item><term> 
    ## Minimum</term><description> 
    ## </description> </item><item><term> 
    ## All</term><description> 
    ## </description> </item></list>
    class DepLabelValueEnum(Enum):
        """
        Members Include: <NotSet> <MinimumMaximum> <Maximum> <Minimum> <All>
        """
        NotSet: int
        MinimumMaximum: int
        Maximum: int
        Minimum: int
        All: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.DepLabelValueEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Field Disp Resolution 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Coarse</term><description> 
    ## </description> </item><item><term> 
    ## Standard</term><description> 
    ## </description> </item><item><term> 
    ## Fine</term><description> 
    ## </description> </item><item><term> 
    ## ExtraFine</term><description> 
    ## </description> </item><item><term> 
    ## SuperFine</term><description> 
    ## </description> </item><item><term> 
    ## UltraFine</term><description> 
    ## </description> </item><item><term> 
    ## UserSpecified</term><description> 
    ## </description> </item></list>
    class DispResolutionEnum(Enum):
        """
        Members Include: <Coarse> <Standard> <Fine> <ExtraFine> <SuperFine> <UltraFine> <UserSpecified>
        """
        Coarse: int
        Standard: int
        Fine: int
        ExtraFine: int
        SuperFine: int
        UltraFine: int
        UserSpecified: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.DispResolutionEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Field Quanity Type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Type0</term><description> 
    ## </description> </item><item><term> 
    ## Type1</term><description> 
    ## </description> </item><item><term> 
    ## Type2</term><description> 
    ## </description> </item><item><term> 
    ## Type3</term><description> 
    ## </description> </item><item><term> 
    ## Type4</term><description> 
    ## </description> </item><item><term> 
    ## Type5</term><description> 
    ## </description> </item><item><term> 
    ## Type6</term><description> 
    ## </description> </item><item><term> 
    ## Type7</term><description> 
    ## </description> </item><item><term> 
    ## Type8</term><description> 
    ## </description> </item><item><term> 
    ## Type9</term><description> 
    ## </description> </item><item><term> 
    ## Type10</term><description> 
    ## </description> </item><item><term> 
    ## Type11</term><description> 
    ## </description> </item><item><term> 
    ## Type12</term><description> 
    ## </description> </item><item><term> 
    ## Type13</term><description> 
    ## </description> </item><item><term> 
    ## Type14</term><description> 
    ## </description> </item><item><term> 
    ## Type15</term><description> 
    ## </description> </item></list>
    class FieldQuantityType(Enum):
        """
        Members Include: <Type0> <Type1> <Type2> <Type3> <Type4> <Type5> <Type6> <Type7> <Type8> <Type9> <Type10> <Type11> <Type12> <Type13> <Type14> <Type15>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.FieldQuantityType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Field Table Heterogeneous Values Display Option 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ShowAverageValue</term><description> 
    ## </description> </item><item><term> 
    ## PrimaryVarValues</term><description> 
    ## </description> </item><item><term> 
    ## Show1StValue</term><description> 
    ## </description> </item><item><term> 
    ## ShowLastValue</term><description> 
    ## </description> </item><item><term> 
    ## ShowMinimumValue</term><description> 
    ## </description> </item><item><term> 
    ## ShowMaximumValue</term><description> 
    ## </description> </item><item><term> 
    ## Hide</term><description> 
    ## </description> </item></list>
    class HeteroTblDispOptionEnum(Enum):
        """
        Members Include: <ShowAverageValue> <PrimaryVarValues> <Show1StValue> <ShowLastValue> <ShowMinimumValue> <ShowMaximumValue> <Hide>
        """
        ShowAverageValue: int
        PrimaryVarValues: int
        Show1StValue: int
        ShowLastValue: int
        ShowMinimumValue: int
        ShowMaximumValue: int
        Hide: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.HeteroTblDispOptionEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Field Indep Dom Disp 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Point</term><description> 
    ## </description> </item><item><term> 
    ## PlusSign</term><description> 
    ## </description> </item><item><term> 
    ## Asterisk</term><description> 
    ## </description> </item><item><term> 
    ## Circle</term><description> 
    ## </description> </item><item><term> 
    ## PoundSign</term><description> 
    ## </description> </item><item><term> 
    ## Cross</term><description> 
    ## </description> </item><item><term> 
    ## Square</term><description> 
    ## </description> </item><item><term> 
    ## Triangle</term><description> 
    ## </description> </item><item><term> 
    ## Diamond</term><description> 
    ## </description> </item><item><term> 
    ## Centerline</term><description> 
    ## </description> </item><item><term> 
    ## Hide</term><description> 
    ## </description> </item></list>
    class IndepDomDispType(Enum):
        """
        Members Include: <Normal> <Point> <PlusSign> <Asterisk> <Circle> <PoundSign> <Cross> <Square> <Triangle> <Diamond> <Centerline> <Hide>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.IndepDomDispType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Legacy_3D Type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## X</term><description> 
    ## </description> </item><item><term> 
    ## Y</term><description> 
    ## </description> </item><item><term> 
    ## Z</term><description> 
    ## </description> </item></list>
    class Legacy3DType(Enum):
        """
        Members Include: <X> <Y> <Z>
        """
        X: int
        Y: int
        Z: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.Legacy3DType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  legend position 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Hide</term><description> 
    ## </description> </item><item><term> 
    ## Left</term><description> 
    ## </description> </item><item><term> 
    ## Right</term><description> 
    ## </description> </item></list>
    class LegendPos(Enum):
        """
        Members Include: <Hide> <Left> <Right>
        """
        Hide: int
        Left: int
        Right: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.LegendPos:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Field Line Display Fonts 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Solid</term><description> 
    ##  Solid </description> </item><item><term> 
    ## Dashed</term><description> 
    ##  Dashed </description> </item><item><term> 
    ## Phantom</term><description> 
    ##  Phantom </description> </item><item><term> 
    ## Centerline</term><description> 
    ##  Centerline </description> </item><item><term> 
    ## Dotted</term><description> 
    ##  Dotted </description> </item><item><term> 
    ## LongDashed</term><description> 
    ##  LongDashed </description> </item><item><term> 
    ## DottedDashed</term><description> 
    ##  DottedDashed </description> </item><item><term> 
    ## Eight</term><description> 
    ##  LongDashedDoubleDotted</description> </item><item><term> 
    ## Nine</term><description> 
    ##  LongDashedDotted for OOTB Fonts and Undulating for shipbuilding fonts </description> </item><item><term> 
    ## Ten</term><description> 
    ##  LongDashedTriplicateDotted for OOTB fonts and Zigzag for shipbuilding fonts </description> </item><item><term> 
    ## Eleven</term><description> 
    ##  LongDashedDoubleShortDashed for OOTB fonts and Railway for shipbuilding fonts </description> </item></list>
    class LineFontEnum(Enum):
        """
        Members Include: <Solid> <Dashed> <Phantom> <Centerline> <Dotted> <LongDashed> <DottedDashed> <Eight> <Nine> <Ten> <Eleven>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.LineFontEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Field Line Widths 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Thick</term><description> 
    ## </description> </item><item><term> 
    ## Thin</term><description> 
    ## </description> </item><item><term> 
    ## One</term><description> 
    ## </description> </item><item><term> 
    ## Two</term><description> 
    ## </description> </item><item><term> 
    ## Three</term><description> 
    ## </description> </item><item><term> 
    ## Four</term><description> 
    ## </description> </item><item><term> 
    ## Five</term><description> 
    ## </description> </item><item><term> 
    ## Six</term><description> 
    ## </description> </item><item><term> 
    ## Seven</term><description> 
    ## </description> </item><item><term> 
    ## Eight</term><description> 
    ## </description> </item><item><term> 
    ## Nine</term><description> 
    ## </description> </item></list>
    class LineWidthEnum(Enum):
        """
        Members Include: <Normal> <Thick> <Thin> <One> <Two> <Three> <Four> <Five> <Six> <Seven> <Eight> <Nine>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.LineWidthEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Scalar Field Type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Hide</term><description> 
    ## </description> </item><item><term> 
    ## Mag</term><description> 
    ## </description> </item></list>
    class ScalarType(Enum):
        """
        Members Include: <Hide> <Mag>
        """
        Hide: int
        Mag: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.ScalarType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Field Tbl Point Type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Hide</term><description> 
    ## </description> </item><item><term> 
    ## Show</term><description> 
    ## </description> </item></list>
    class TblPointTypeEnum(Enum):
        """
        Members Include: <Hide> <Show>
        """
        Hide: int
        Show: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.TblPointTypeEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Tensor Field Type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Xx</term><description> 
    ## </description> </item><item><term> 
    ## Yy</term><description> 
    ## </description> </item><item><term> 
    ## Zz</term><description> 
    ## </description> </item><item><term> 
    ## Xy</term><description> 
    ## </description> </item><item><term> 
    ## Yz</term><description> 
    ## </description> </item><item><term> 
    ## Zx</term><description> 
    ## </description> </item><item><term> 
    ## Mean</term><description> 
    ## </description> </item><item><term> 
    ## MidPrncpl</term><description> 
    ## </description> </item><item><term> 
    ## MinPrncpl</term><description> 
    ## </description> </item><item><term> 
    ## MaxPrncpl</term><description> 
    ## </description> </item><item><term> 
    ## Octahedral</term><description> 
    ## </description> </item><item><term> 
    ## VonMises</term><description> 
    ## </description> </item></list>
    class TensorType(Enum):
        """
        Members Include: <Xx> <Yy> <Zz> <Xy> <Yz> <Zx> <Mean> <MidPrncpl> <MinPrncpl> <MaxPrncpl> <Octahedral> <VonMises>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.TensorType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  range for contour plots 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Auto</term><description> 
    ## </description> </item><item><term> 
    ## Specified</term><description> 
    ## </description> </item></list>
    class ValueRange(Enum):
        """
        Members Include: <Auto> <Specified>
        """
        Auto: int
        Specified: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.ValueRange:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Field Values 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Hide</term><description> 
    ## </description> </item><item><term> 
    ## Point</term><description> 
    ## </description> </item><item><term> 
    ## PlusSign</term><description> 
    ## </description> </item><item><term> 
    ## Asterisk</term><description> 
    ## </description> </item><item><term> 
    ## Circle</term><description> 
    ## </description> </item><item><term> 
    ## PoundSign</term><description> 
    ## </description> </item><item><term> 
    ## Cross</term><description> 
    ## </description> </item><item><term> 
    ## Square</term><description> 
    ## </description> </item><item><term> 
    ## Triangle</term><description> 
    ## </description> </item><item><term> 
    ## Diamond</term><description> 
    ## </description> </item><item><term> 
    ## Centerline</term><description> 
    ## </description> </item></list>
    class ValuesEnum(Enum):
        """
        Members Include: <Hide> <Point> <PlusSign> <Asterisk> <Circle> <PoundSign> <Cross> <Square> <Triangle> <Diamond> <Centerline>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.ValuesEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Vector Field Type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## X</term><description> 
    ## </description> </item><item><term> 
    ## Y</term><description> 
    ## </description> </item><item><term> 
    ## Z</term><description> 
    ## </description> </item><item><term> 
    ## Mag</term><description> 
    ## </description> </item></list>
    class VectorType(Enum):
        """
        Members Include: <X> <Y> <Z> <Mag>
        """
        X: int
        Y: int
        Z: int
        Mag: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.VectorType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) AxisColor
    ##  Returns the axis color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    ## @return NXOpen.NXColor
    @property
    def AxisColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) AxisColor
         Returns the axis color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) AxisColor

    ##  Returns the axis color   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    @AxisColor.setter
    def AxisColor(self, axisColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) AxisColor
         Returns the axis color   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) BasicColor
    ##  Returns the basic color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    ## @return NXOpen.NXColor
    @property
    def BasicColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) BasicColor
         Returns the basic color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) BasicColor

    ##  Returns the basic color   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    @BasicColor.setter
    def BasicColor(self, basicColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) BasicColor
         Returns the basic color   
            
         
        """
        pass
    
    ## Getter for property: (float) DepCalcSymblSize
    ##  Returns the dep calc symbl size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return float
    @property
    def DepCalcSymblSize(self) -> float:
        """
        Getter for property: (float) DepCalcSymblSize
         Returns the dep calc symbl size   
            
         
        """
        pass
    
    ## Setter for property: (float) DepCalcSymblSize

    ##  Returns the dep calc symbl size   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @DepCalcSymblSize.setter
    def DepCalcSymblSize(self, depCalcSymblSize: float):
        """
        Setter for property: (float) DepCalcSymblSize
         Returns the dep calc symbl size   
            
         
        """
        pass
    
    ## Getter for property: (@link DisplayPropertiesBuilder.DepDispTypeEnum NXOpen.Fields.DisplayPropertiesBuilder.DepDispTypeEnum@endlink) DepDispType
    ##  Returns the dep disp type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    ## @return DisplayPropertiesBuilder.DepDispTypeEnum
    @property
    def DepDispType(self) -> DisplayPropertiesBuilder.DepDispTypeEnum:
        """
        Getter for property: (@link DisplayPropertiesBuilder.DepDispTypeEnum NXOpen.Fields.DisplayPropertiesBuilder.DepDispTypeEnum@endlink) DepDispType
         Returns the dep disp type   
            
         
        """
        pass
    
    ## Setter for property: (@link DisplayPropertiesBuilder.DepDispTypeEnum NXOpen.Fields.DisplayPropertiesBuilder.DepDispTypeEnum@endlink) DepDispType

    ##  Returns the dep disp type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    @DepDispType.setter
    def DepDispType(self, depDispType: DisplayPropertiesBuilder.DepDispTypeEnum):
        """
        Setter for property: (@link DisplayPropertiesBuilder.DepDispTypeEnum NXOpen.Fields.DisplayPropertiesBuilder.DepDispTypeEnum@endlink) DepDispType
         Returns the dep disp type   
            
         
        """
        pass
    
    ## Getter for property: (@link DisplayPropertiesBuilder.DepDomColorEnum NXOpen.Fields.DisplayPropertiesBuilder.DepDomColorEnum@endlink) DepDomColor
    ##  Returns the dep dom color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    ## @return DisplayPropertiesBuilder.DepDomColorEnum
    @property
    def DepDomColor(self) -> DisplayPropertiesBuilder.DepDomColorEnum:
        """
        Getter for property: (@link DisplayPropertiesBuilder.DepDomColorEnum NXOpen.Fields.DisplayPropertiesBuilder.DepDomColorEnum@endlink) DepDomColor
         Returns the dep dom color   
            
         
        """
        pass
    
    ## Setter for property: (@link DisplayPropertiesBuilder.DepDomColorEnum NXOpen.Fields.DisplayPropertiesBuilder.DepDomColorEnum@endlink) DepDomColor

    ##  Returns the dep dom color   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    @DepDomColor.setter
    def DepDomColor(self, depDomColor: DisplayPropertiesBuilder.DepDomColorEnum):
        """
        Setter for property: (@link DisplayPropertiesBuilder.DepDomColorEnum NXOpen.Fields.DisplayPropertiesBuilder.DepDomColorEnum@endlink) DepDomColor
         Returns the dep dom color   
            
         
        """
        pass
    
    ## Getter for property: (@link DisplayPropertiesBuilder.DepLabelValueEnum NXOpen.Fields.DisplayPropertiesBuilder.DepLabelValueEnum@endlink) DepLabelValues
    ##  Returns the dep label values   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    ## @return DisplayPropertiesBuilder.DepLabelValueEnum
    @property
    def DepLabelValues(self) -> DisplayPropertiesBuilder.DepLabelValueEnum:
        """
        Getter for property: (@link DisplayPropertiesBuilder.DepLabelValueEnum NXOpen.Fields.DisplayPropertiesBuilder.DepLabelValueEnum@endlink) DepLabelValues
         Returns the dep label values   
            
         
        """
        pass
    
    ## Setter for property: (@link DisplayPropertiesBuilder.DepLabelValueEnum NXOpen.Fields.DisplayPropertiesBuilder.DepLabelValueEnum@endlink) DepLabelValues

    ##  Returns the dep label values   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    @DepLabelValues.setter
    def DepLabelValues(self, depLabelValues: DisplayPropertiesBuilder.DepLabelValueEnum):
        """
        Setter for property: (@link DisplayPropertiesBuilder.DepLabelValueEnum NXOpen.Fields.DisplayPropertiesBuilder.DepLabelValueEnum@endlink) DepLabelValues
         Returns the dep label values   
            
         
        """
        pass
    
    ## Getter for property: (float) DepRangeMax
    ##  Returns the dep range max   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return float
    @property
    def DepRangeMax(self) -> float:
        """
        Getter for property: (float) DepRangeMax
         Returns the dep range max   
            
         
        """
        pass
    
    ## Setter for property: (float) DepRangeMax

    ##  Returns the dep range max   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @DepRangeMax.setter
    def DepRangeMax(self, depRangeMax: float):
        """
        Setter for property: (float) DepRangeMax
         Returns the dep range max   
            
         
        """
        pass
    
    ## Getter for property: (float) DepRangeMin
    ##  Returns the dependent range min   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return float
    @property
    def DepRangeMin(self) -> float:
        """
        Getter for property: (float) DepRangeMin
         Returns the dependent range min   
            
         
        """
        pass
    
    ## Setter for property: (float) DepRangeMin

    ##  Returns the dependent range min   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @DepRangeMin.setter
    def DepRangeMin(self, depRangeMin: float):
        """
        Setter for property: (float) DepRangeMin
         Returns the dependent range min   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) DepSelColor
    ##  Returns the dep sel color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    ## @return NXOpen.NXColor
    @property
    def DepSelColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) DepSelColor
         Returns the dep sel color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) DepSelColor

    ##  Returns the dep sel color   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    @DepSelColor.setter
    def DepSelColor(self, depSelColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) DepSelColor
         Returns the dep sel color   
            
         
        """
        pass
    
    ## Getter for property: (float) DepSymbolSize
    ##  Returns the dep symbol size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    ## @return float
    @property
    def DepSymbolSize(self) -> float:
        """
        Getter for property: (float) DepSymbolSize
         Returns the dep symbol size   
            
         
        """
        pass
    
    ## Setter for property: (float) DepSymbolSize

    ##  Returns the dep symbol size   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    @DepSymbolSize.setter
    def DepSymbolSize(self, depSymbolSize: float):
        """
        Setter for property: (float) DepSymbolSize
         Returns the dep symbol size   
            
         
        """
        pass
    
    ## Getter for property: (@link DisplayPropertiesBuilder.DispResolutionEnum NXOpen.Fields.DisplayPropertiesBuilder.DispResolutionEnum@endlink) DisplayResolution
    ##  Returns the display resolution   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    ## @return DisplayPropertiesBuilder.DispResolutionEnum
    @property
    def DisplayResolution(self) -> DisplayPropertiesBuilder.DispResolutionEnum:
        """
        Getter for property: (@link DisplayPropertiesBuilder.DispResolutionEnum NXOpen.Fields.DisplayPropertiesBuilder.DispResolutionEnum@endlink) DisplayResolution
         Returns the display resolution   
            
         
        """
        pass
    
    ## Setter for property: (@link DisplayPropertiesBuilder.DispResolutionEnum NXOpen.Fields.DisplayPropertiesBuilder.DispResolutionEnum@endlink) DisplayResolution

    ##  Returns the display resolution   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    @DisplayResolution.setter
    def DisplayResolution(self, displayResolution: DisplayPropertiesBuilder.DispResolutionEnum):
        """
        Setter for property: (@link DisplayPropertiesBuilder.DispResolutionEnum NXOpen.Fields.DisplayPropertiesBuilder.DispResolutionEnum@endlink) DisplayResolution
         Returns the display resolution   
            
         
        """
        pass
    
    ## Getter for property: (float) DummyScale
    ##  Returns the dummy scale   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    ## @return float
    @property
    def DummyScale(self) -> float:
        """
        Getter for property: (float) DummyScale
         Returns the dummy scale   
            
         
        """
        pass
    
    ## Setter for property: (float) DummyScale

    ##  Returns the dummy scale   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    @DummyScale.setter
    def DummyScale(self, dummyScale: float):
        """
        Setter for property: (float) DummyScale
         Returns the dummy scale   
            
         
        """
        pass
    
    ## Getter for property: (bool) FaceAnalysis
    ##  Returns the face analysis   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    ## @return bool
    @property
    def FaceAnalysis(self) -> bool:
        """
        Getter for property: (bool) FaceAnalysis
         Returns the face analysis   
            
         
        """
        pass
    
    ## Setter for property: (bool) FaceAnalysis

    ##  Returns the face analysis   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    @FaceAnalysis.setter
    def FaceAnalysis(self, faceAnalysis: bool):
        """
        Setter for property: (bool) FaceAnalysis
         Returns the face analysis   
            
         
        """
        pass
    
    ## Getter for property: (@link DisplayPropertiesBuilder.FieldQuantityType NXOpen.Fields.DisplayPropertiesBuilder.FieldQuantityType@endlink) FieldQuantity
    ##  Returns the field quantity type  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return DisplayPropertiesBuilder.FieldQuantityType
    @property
    def FieldQuantity(self) -> DisplayPropertiesBuilder.FieldQuantityType:
        """
        Getter for property: (@link DisplayPropertiesBuilder.FieldQuantityType NXOpen.Fields.DisplayPropertiesBuilder.FieldQuantityType@endlink) FieldQuantity
         Returns the field quantity type  
            
         
        """
        pass
    
    ## Setter for property: (@link DisplayPropertiesBuilder.FieldQuantityType NXOpen.Fields.DisplayPropertiesBuilder.FieldQuantityType@endlink) FieldQuantity

    ##  Returns the field quantity type  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @FieldQuantity.setter
    def FieldQuantity(self, fieldQuantity: DisplayPropertiesBuilder.FieldQuantityType):
        """
        Setter for property: (@link DisplayPropertiesBuilder.FieldQuantityType NXOpen.Fields.DisplayPropertiesBuilder.FieldQuantityType@endlink) FieldQuantity
         Returns the field quantity type  
            
         
        """
        pass
    
    ## Getter for property: (@link DisplayPropertiesBuilder.HeteroTblDispOptionEnum NXOpen.Fields.DisplayPropertiesBuilder.HeteroTblDispOptionEnum@endlink) HeteroTblDispOption
    ##  Returns the heterogeneous table values display option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return DisplayPropertiesBuilder.HeteroTblDispOptionEnum
    @property
    def HeteroTblDispOption(self) -> DisplayPropertiesBuilder.HeteroTblDispOptionEnum:
        """
        Getter for property: (@link DisplayPropertiesBuilder.HeteroTblDispOptionEnum NXOpen.Fields.DisplayPropertiesBuilder.HeteroTblDispOptionEnum@endlink) HeteroTblDispOption
         Returns the heterogeneous table values display option   
            
         
        """
        pass
    
    ## Setter for property: (@link DisplayPropertiesBuilder.HeteroTblDispOptionEnum NXOpen.Fields.DisplayPropertiesBuilder.HeteroTblDispOptionEnum@endlink) HeteroTblDispOption

    ##  Returns the heterogeneous table values display option   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @HeteroTblDispOption.setter
    def HeteroTblDispOption(self, hetTblValDispOption: DisplayPropertiesBuilder.HeteroTblDispOptionEnum):
        """
        Setter for property: (@link DisplayPropertiesBuilder.HeteroTblDispOptionEnum NXOpen.Fields.DisplayPropertiesBuilder.HeteroTblDispOptionEnum@endlink) HeteroTblDispOption
         Returns the heterogeneous table values display option   
            
         
        """
        pass
    
    ## Getter for property: (@link DisplayPropertiesBuilder.IndepDomDispType NXOpen.Fields.DisplayPropertiesBuilder.IndepDomDispType@endlink) IndepDispType
    ##  Returns the indep disp type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    ## @return DisplayPropertiesBuilder.IndepDomDispType
    @property
    def IndepDispType(self) -> DisplayPropertiesBuilder.IndepDomDispType:
        """
        Getter for property: (@link DisplayPropertiesBuilder.IndepDomDispType NXOpen.Fields.DisplayPropertiesBuilder.IndepDomDispType@endlink) IndepDispType
         Returns the indep disp type   
            
         
        """
        pass
    
    ## Setter for property: (@link DisplayPropertiesBuilder.IndepDomDispType NXOpen.Fields.DisplayPropertiesBuilder.IndepDomDispType@endlink) IndepDispType

    ##  Returns the indep disp type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    @IndepDispType.setter
    def IndepDispType(self, indepDispType: DisplayPropertiesBuilder.IndepDomDispType):
        """
        Setter for property: (@link DisplayPropertiesBuilder.IndepDomDispType NXOpen.Fields.DisplayPropertiesBuilder.IndepDomDispType@endlink) IndepDispType
         Returns the indep disp type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) LabelColor
    ##  Returns the label color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    ## @return NXOpen.NXColor
    @property
    def LabelColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) LabelColor
         Returns the label color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) LabelColor

    ##  Returns the label color   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    @LabelColor.setter
    def LabelColor(self, labelColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) LabelColor
         Returns the label color   
            
         
        """
        pass
    
    ## Getter for property: (int) Layer
    ##  Returns the layer   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    ## @return int
    @property
    def Layer(self) -> int:
        """
        Getter for property: (int) Layer
         Returns the layer   
            
         
        """
        pass
    
    ## Setter for property: (int) Layer

    ##  Returns the layer   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    @Layer.setter
    def Layer(self, layer: int):
        """
        Setter for property: (int) Layer
         Returns the layer   
            
         
        """
        pass
    
    ## Getter for property: (@link DisplayPropertiesBuilder.LegendPos NXOpen.Fields.DisplayPropertiesBuilder.LegendPos@endlink) LegendPosition
    ##  Returns the legend position   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return DisplayPropertiesBuilder.LegendPos
    @property
    def LegendPosition(self) -> DisplayPropertiesBuilder.LegendPos:
        """
        Getter for property: (@link DisplayPropertiesBuilder.LegendPos NXOpen.Fields.DisplayPropertiesBuilder.LegendPos@endlink) LegendPosition
         Returns the legend position   
            
         
        """
        pass
    
    ## Setter for property: (@link DisplayPropertiesBuilder.LegendPos NXOpen.Fields.DisplayPropertiesBuilder.LegendPos@endlink) LegendPosition

    ##  Returns the legend position   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @LegendPosition.setter
    def LegendPosition(self, legendPosition: DisplayPropertiesBuilder.LegendPos):
        """
        Setter for property: (@link DisplayPropertiesBuilder.LegendPos NXOpen.Fields.DisplayPropertiesBuilder.LegendPos@endlink) LegendPosition
         Returns the legend position   
            
         
        """
        pass
    
    ## Getter for property: (@link DisplayPropertiesBuilder.LineFontEnum NXOpen.Fields.DisplayPropertiesBuilder.LineFontEnum@endlink) LineFont
    ##  Returns the line font   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    ## @return DisplayPropertiesBuilder.LineFontEnum
    @property
    def LineFont(self) -> DisplayPropertiesBuilder.LineFontEnum:
        """
        Getter for property: (@link DisplayPropertiesBuilder.LineFontEnum NXOpen.Fields.DisplayPropertiesBuilder.LineFontEnum@endlink) LineFont
         Returns the line font   
            
         
        """
        pass
    
    ## Setter for property: (@link DisplayPropertiesBuilder.LineFontEnum NXOpen.Fields.DisplayPropertiesBuilder.LineFontEnum@endlink) LineFont

    ##  Returns the line font   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    @LineFont.setter
    def LineFont(self, lineFont: DisplayPropertiesBuilder.LineFontEnum):
        """
        Setter for property: (@link DisplayPropertiesBuilder.LineFontEnum NXOpen.Fields.DisplayPropertiesBuilder.LineFontEnum@endlink) LineFont
         Returns the line font   
            
         
        """
        pass
    
    ## Getter for property: (@link DisplayPropertiesBuilder.LineWidthEnum NXOpen.Fields.DisplayPropertiesBuilder.LineWidthEnum@endlink) LineWidth
    ##  Returns the line width   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    ## @return DisplayPropertiesBuilder.LineWidthEnum
    @property
    def LineWidth(self) -> DisplayPropertiesBuilder.LineWidthEnum:
        """
        Getter for property: (@link DisplayPropertiesBuilder.LineWidthEnum NXOpen.Fields.DisplayPropertiesBuilder.LineWidthEnum@endlink) LineWidth
         Returns the line width   
            
         
        """
        pass
    
    ## Setter for property: (@link DisplayPropertiesBuilder.LineWidthEnum NXOpen.Fields.DisplayPropertiesBuilder.LineWidthEnum@endlink) LineWidth

    ##  Returns the line width   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    @LineWidth.setter
    def LineWidth(self, lineWidth: DisplayPropertiesBuilder.LineWidthEnum):
        """
        Setter for property: (@link DisplayPropertiesBuilder.LineWidthEnum NXOpen.Fields.DisplayPropertiesBuilder.LineWidthEnum@endlink) LineWidth
         Returns the line width   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) OverflowColor
    ##  Returns the overflow color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def OverflowColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) OverflowColor
         Returns the overflow color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) OverflowColor

    ##  Returns the overflow color   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @OverflowColor.setter
    def OverflowColor(self, overflowColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) OverflowColor
         Returns the overflow color   
            
         
        """
        pass
    
    ## Getter for property: (bool) PartiallyShaded
    ##  Returns the partially shaded   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    ## @return bool
    @property
    def PartiallyShaded(self) -> bool:
        """
        Getter for property: (bool) PartiallyShaded
         Returns the partially shaded   
            
         
        """
        pass
    
    ## Setter for property: (bool) PartiallyShaded

    ##  Returns the partially shaded   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    @PartiallyShaded.setter
    def PartiallyShaded(self, partiallyShaded: bool):
        """
        Setter for property: (bool) PartiallyShaded
         Returns the partially shaded   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) PrimaryVar
    ##  Returns the primary var name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def PrimaryVar(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) PrimaryVar
         Returns the primary var name   
            
         
        """
        pass
    
    ## Getter for property: (@link DisplayPropertiesBuilder.ValueRange NXOpen.Fields.DisplayPropertiesBuilder.ValueRange@endlink) Range
    ##  Returns the range   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return DisplayPropertiesBuilder.ValueRange
    @property
    def Range(self) -> DisplayPropertiesBuilder.ValueRange:
        """
        Getter for property: (@link DisplayPropertiesBuilder.ValueRange NXOpen.Fields.DisplayPropertiesBuilder.ValueRange@endlink) Range
         Returns the range   
            
         
        """
        pass
    
    ## Setter for property: (@link DisplayPropertiesBuilder.ValueRange NXOpen.Fields.DisplayPropertiesBuilder.ValueRange@endlink) Range

    ##  Returns the range   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Range.setter
    def Range(self, range: DisplayPropertiesBuilder.ValueRange):
        """
        Setter for property: (@link DisplayPropertiesBuilder.ValueRange NXOpen.Fields.DisplayPropertiesBuilder.ValueRange@endlink) Range
         Returns the range   
            
         
        """
        pass
    
    ## Getter for property: (float) RangeMax
    ##  Returns the legend range max   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return float
    @property
    def RangeMax(self) -> float:
        """
        Getter for property: (float) RangeMax
         Returns the legend range max   
            
         
        """
        pass
    
    ## Setter for property: (float) RangeMax

    ##  Returns the legend range max   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RangeMax.setter
    def RangeMax(self, rangeMax: float):
        """
        Setter for property: (float) RangeMax
         Returns the legend range max   
            
         
        """
        pass
    
    ## Getter for property: (float) RangeMin
    ##  Returns the legend range min   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return float
    @property
    def RangeMin(self) -> float:
        """
        Getter for property: (float) RangeMin
         Returns the legend range min   
            
         
        """
        pass
    
    ## Setter for property: (float) RangeMin

    ##  Returns the legend range min   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RangeMin.setter
    def RangeMin(self, rangeMin: float):
        """
        Setter for property: (float) RangeMin
         Returns the legend range min   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowAxis
    ##  Returns the show axis   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    ## @return bool
    @property
    def ShowAxis(self) -> bool:
        """
        Getter for property: (bool) ShowAxis
         Returns the show axis   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowAxis

    ##  Returns the show axis   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    @ShowAxis.setter
    def ShowAxis(self, showAxis: bool):
        """
        Setter for property: (bool) ShowAxis
         Returns the show axis   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowDefaultVal
    ##  Returns the show default val   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def ShowDefaultVal(self) -> bool:
        """
        Getter for property: (bool) ShowDefaultVal
         Returns the show default val   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowDefaultVal

    ##  Returns the show default val   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ShowDefaultVal.setter
    def ShowDefaultVal(self, showDefaultVal: bool):
        """
        Setter for property: (bool) ShowDefaultVal
         Returns the show default val   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowDescription
    ##  Returns the show description   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def ShowDescription(self) -> bool:
        """
        Getter for property: (bool) ShowDescription
         Returns the show description   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowDescription

    ##  Returns the show description   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ShowDescription.setter
    def ShowDescription(self, showDescription: bool):
        """
        Setter for property: (bool) ShowDescription
         Returns the show description   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowLabels
    ##  Returns the show labels   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    ## @return bool
    @property
    def ShowLabels(self) -> bool:
        """
        Getter for property: (bool) ShowLabels
         Returns the show labels   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowLabels

    ##  Returns the show labels   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    @ShowLabels.setter
    def ShowLabels(self, showLabels: bool):
        """
        Setter for property: (bool) ShowLabels
         Returns the show labels   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowMapTopo
    ##  Returns the show map topo   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    ## @return bool
    @property
    def ShowMapTopo(self) -> bool:
        """
        Getter for property: (bool) ShowMapTopo
         Returns the show map topo   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowMapTopo

    ##  Returns the show map topo   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    @ShowMapTopo.setter
    def ShowMapTopo(self, showMapTopo: bool):
        """
        Setter for property: (bool) ShowMapTopo
         Returns the show map topo   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowName
    ##  Returns the show name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def ShowName(self) -> bool:
        """
        Getter for property: (bool) ShowName
         Returns the show name   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowName

    ##  Returns the show name   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ShowName.setter
    def ShowName(self, showName: bool):
        """
        Setter for property: (bool) ShowName
         Returns the show name   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowOverflowValues
    ##  Returns the show overflow   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def ShowOverflowValues(self) -> bool:
        """
        Getter for property: (bool) ShowOverflowValues
         Returns the show overflow   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowOverflowValues

    ##  Returns the show overflow   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ShowOverflowValues.setter
    def ShowOverflowValues(self, showOverflow: bool):
        """
        Setter for property: (bool) ShowOverflowValues
         Returns the show overflow   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowSrcTblVals
    ##  Returns the show dep src tbl vals   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def ShowSrcTblVals(self) -> bool:
        """
        Getter for property: (bool) ShowSrcTblVals
         Returns the show dep src tbl vals   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowSrcTblVals

    ##  Returns the show dep src tbl vals   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ShowSrcTblVals.setter
    def ShowSrcTblVals(self, showSrcTblVals: bool):
        """
        Setter for property: (bool) ShowSrcTblVals
         Returns the show dep src tbl vals   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowUndefValues
    ##  Returns the show new undefined values   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def ShowUndefValues(self) -> bool:
        """
        Getter for property: (bool) ShowUndefValues
         Returns the show new undefined values   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowUndefValues

    ##  Returns the show new undefined values   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ShowUndefValues.setter
    def ShowUndefValues(self, showUndefValues: bool):
        """
        Setter for property: (bool) ShowUndefValues
         Returns the show new undefined values   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowUnderflowValues
    ##  Returns the show underflow   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def ShowUnderflowValues(self) -> bool:
        """
        Getter for property: (bool) ShowUnderflowValues
         Returns the show underflow   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowUnderflowValues

    ##  Returns the show underflow   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ShowUnderflowValues.setter
    def ShowUnderflowValues(self, showUnderflow: bool):
        """
        Setter for property: (bool) ShowUnderflowValues
         Returns the show underflow   
            
         
        """
        pass
    
    ## Getter for property: (int) SpectrumLevels
    ##  Returns the spectrum levels   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    ## @return int
    @property
    def SpectrumLevels(self) -> int:
        """
        Getter for property: (int) SpectrumLevels
         Returns the spectrum levels   
            
         
        """
        pass
    
    ## Setter for property: (int) SpectrumLevels

    ##  Returns the spectrum levels   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    @SpectrumLevels.setter
    def SpectrumLevels(self, spectrumLevels: int):
        """
        Setter for property: (int) SpectrumLevels
         Returns the spectrum levels   
            
         
        """
        pass
    
    ## Getter for property: (float) SurfaceOffset
    ##  Returns the surface offset   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    ## @return float
    @property
    def SurfaceOffset(self) -> float:
        """
        Getter for property: (float) SurfaceOffset
         Returns the surface offset   
            
         
        """
        pass
    
    ## Setter for property: (float) SurfaceOffset

    ##  Returns the surface offset   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    @SurfaceOffset.setter
    def SurfaceOffset(self, surfaceOffset: float):
        """
        Setter for property: (float) SurfaceOffset
         Returns the surface offset   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) TblDepColor
    ##  Returns the table dependent color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.0.  This function is deprecated, Tbl dependent Color can be obtained using @link NXOpen::Fields::DisplayPropertiesBuilder::DepSelColor NXOpen::Fields::DisplayPropertiesBuilder::DepSelColor@endlink .  <br> 

    ## @return NXOpen.NXColor
    @property
    def TblDepColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) TblDepColor
         Returns the table dependent color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) TblDepColor

    ##  Returns the table dependent color   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.0.  This function is deprecated, Tbl dependent Color can be set using @link NXOpen::Fields::DisplayPropertiesBuilder::DepSelColor NXOpen::Fields::DisplayPropertiesBuilder::DepSelColor@endlink .  <br> 

    @TblDepColor.setter
    def TblDepColor(self, tblDepColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) TblDepColor
         Returns the table dependent color   
            
         
        """
        pass
    
    ## Getter for property: (@link DisplayPropertiesBuilder.DepDispTypeEnum NXOpen.Fields.DisplayPropertiesBuilder.DepDispTypeEnum@endlink) TblDepDispType
    ##  Returns the table dependent display type  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## @return DisplayPropertiesBuilder.DepDispTypeEnum
    @property
    def TblDepDispType(self) -> DisplayPropertiesBuilder.DepDispTypeEnum:
        """
        Getter for property: (@link DisplayPropertiesBuilder.DepDispTypeEnum NXOpen.Fields.DisplayPropertiesBuilder.DepDispTypeEnum@endlink) TblDepDispType
         Returns the table dependent display type  
            
         
        """
        pass
    
    ## Setter for property: (@link DisplayPropertiesBuilder.DepDispTypeEnum NXOpen.Fields.DisplayPropertiesBuilder.DepDispTypeEnum@endlink) TblDepDispType

    ##  Returns the table dependent display type  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    @TblDepDispType.setter
    def TblDepDispType(self, tblDepDispType: DisplayPropertiesBuilder.DepDispTypeEnum):
        """
        Setter for property: (@link DisplayPropertiesBuilder.DepDispTypeEnum NXOpen.Fields.DisplayPropertiesBuilder.DepDispTypeEnum@endlink) TblDepDispType
         Returns the table dependent display type  
            
         
        """
        pass
    
    ## Getter for property: (@link DisplayPropertiesBuilder.DepDomColorEnum NXOpen.Fields.DisplayPropertiesBuilder.DepDomColorEnum@endlink) TblDepDomColor
    ##  Returns the table dependent domain color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.0.  This function is deprecated, Tbl dependent Color can be chosen using @link NXOpen::Fields::DisplayPropertiesBuilder::DepDomColor NXOpen::Fields::DisplayPropertiesBuilder::DepDomColor@endlink .  <br> 

    ## @return DisplayPropertiesBuilder.DepDomColorEnum
    @property
    def TblDepDomColor(self) -> DisplayPropertiesBuilder.DepDomColorEnum:
        """
        Getter for property: (@link DisplayPropertiesBuilder.DepDomColorEnum NXOpen.Fields.DisplayPropertiesBuilder.DepDomColorEnum@endlink) TblDepDomColor
         Returns the table dependent domain color   
            
         
        """
        pass
    
    ## Setter for property: (@link DisplayPropertiesBuilder.DepDomColorEnum NXOpen.Fields.DisplayPropertiesBuilder.DepDomColorEnum@endlink) TblDepDomColor

    ##  Returns the table dependent domain color   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.0.  This function is deprecated, Tbl dependent Color can be chosen using @link NXOpen::Fields::DisplayPropertiesBuilder::DepDomColor NXOpen::Fields::DisplayPropertiesBuilder::DepDomColor@endlink .  <br> 

    @TblDepDomColor.setter
    def TblDepDomColor(self, depDomColor: DisplayPropertiesBuilder.DepDomColorEnum):
        """
        Setter for property: (@link DisplayPropertiesBuilder.DepDomColorEnum NXOpen.Fields.DisplayPropertiesBuilder.DepDomColorEnum@endlink) TblDepDomColor
         Returns the table dependent domain color   
            
         
        """
        pass
    
    ## Getter for property: (@link DisplayPropertiesBuilder.DepLabelValueEnum NXOpen.Fields.DisplayPropertiesBuilder.DepLabelValueEnum@endlink) TblDepLabelValues
    ##  Returns the table dependent label values   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return DisplayPropertiesBuilder.DepLabelValueEnum
    @property
    def TblDepLabelValues(self) -> DisplayPropertiesBuilder.DepLabelValueEnum:
        """
        Getter for property: (@link DisplayPropertiesBuilder.DepLabelValueEnum NXOpen.Fields.DisplayPropertiesBuilder.DepLabelValueEnum@endlink) TblDepLabelValues
         Returns the table dependent label values   
            
         
        """
        pass
    
    ## Setter for property: (@link DisplayPropertiesBuilder.DepLabelValueEnum NXOpen.Fields.DisplayPropertiesBuilder.DepLabelValueEnum@endlink) TblDepLabelValues

    ##  Returns the table dependent label values   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @TblDepLabelValues.setter
    def TblDepLabelValues(self, tblDepLabelValues: DisplayPropertiesBuilder.DepLabelValueEnum):
        """
        Setter for property: (@link DisplayPropertiesBuilder.DepLabelValueEnum NXOpen.Fields.DisplayPropertiesBuilder.DepLabelValueEnum@endlink) TblDepLabelValues
         Returns the table dependent label values   
            
         
        """
        pass
    
    ## Getter for property: (@link DisplayPropertiesBuilder.TblPointTypeEnum NXOpen.Fields.DisplayPropertiesBuilder.TblPointTypeEnum@endlink) TblDepPtType
    ##  Returns the tbl dep pt type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.0.  To show source table dependent values use @link NXOpen::Fields::DisplayPropertiesBuilder::ShowSrcTblVals NXOpen::Fields::DisplayPropertiesBuilder::ShowSrcTblVals@endlink  to show source table values.  <br> 

    ## @return DisplayPropertiesBuilder.TblPointTypeEnum
    @property
    def TblDepPtType(self) -> DisplayPropertiesBuilder.TblPointTypeEnum:
        """
        Getter for property: (@link DisplayPropertiesBuilder.TblPointTypeEnum NXOpen.Fields.DisplayPropertiesBuilder.TblPointTypeEnum@endlink) TblDepPtType
         Returns the tbl dep pt type   
            
         
        """
        pass
    
    ## Setter for property: (@link DisplayPropertiesBuilder.TblPointTypeEnum NXOpen.Fields.DisplayPropertiesBuilder.TblPointTypeEnum@endlink) TblDepPtType

    ##  Returns the tbl dep pt type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.0.  Source table display no longer uses symbols, so this function has no meaning. Table values are only on or off; to show source table values use @link NXOpen::Fields::DisplayPropertiesBuilder::ShowSrcTblVals NXOpen::Fields::DisplayPropertiesBuilder::ShowSrcTblVals@endlink  to show source table values.  <br> 

    @TblDepPtType.setter
    def TblDepPtType(self, tblDepPtType: DisplayPropertiesBuilder.TblPointTypeEnum):
        """
        Setter for property: (@link DisplayPropertiesBuilder.TblPointTypeEnum NXOpen.Fields.DisplayPropertiesBuilder.TblPointTypeEnum@endlink) TblDepPtType
         Returns the tbl dep pt type   
            
         
        """
        pass
    
    ## Getter for property: (float) TblDepSymbolSize
    ##  Returns the table dependent symbol size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return float
    @property
    def TblDepSymbolSize(self) -> float:
        """
        Getter for property: (float) TblDepSymbolSize
         Returns the table dependent symbol size   
            
         
        """
        pass
    
    ## Setter for property: (float) TblDepSymbolSize

    ##  Returns the table dependent symbol size   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @TblDepSymbolSize.setter
    def TblDepSymbolSize(self, tblDepSymbolSize: float):
        """
        Setter for property: (float) TblDepSymbolSize
         Returns the table dependent symbol size   
            
         
        """
        pass
    
    ## Getter for property: (float) TblHetPrimaryValue
    ##  Returns the heterogeneous table value to display   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def TblHetPrimaryValue(self) -> float:
        """
        Getter for property: (float) TblHetPrimaryValue
         Returns the heterogeneous table value to display   
            
         
        """
        pass
    
    ## Setter for property: (float) TblHetPrimaryValue

    ##  Returns the heterogeneous table value to display   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @TblHetPrimaryValue.setter
    def TblHetPrimaryValue(self, hetTblValue: float):
        """
        Setter for property: (float) TblHetPrimaryValue
         Returns the heterogeneous table value to display   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) TblIndepColor
    ##  Returns the tbl indep color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.0.  This function is deprecated. Table independent domain is no longer displayable so this property has no meaning. Dependent domain color can be obtained using @link NXOpen::Fields::DisplayPropertiesBuilder::DepSelColor NXOpen::Fields::DisplayPropertiesBuilder::DepSelColor@endlink .  <br> 

    ## @return NXOpen.NXColor
    @property
    def TblIndepColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) TblIndepColor
         Returns the tbl indep color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) TblIndepColor

    ##  Returns the tbl indep color   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.0.  This function is deprecated. Table independent domain is no longer displayable, so this function has no meaning. Table dependent domain color can be set using @link NXOpen::Fields::DisplayPropertiesBuilder::DepSelColor NXOpen::Fields::DisplayPropertiesBuilder::DepSelColor@endlink .  <br> 

    @TblIndepColor.setter
    def TblIndepColor(self, tblIndepColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) TblIndepColor
         Returns the tbl indep color   
            
         
        """
        pass
    
    ## Getter for property: (@link DisplayPropertiesBuilder.ValuesEnum NXOpen.Fields.DisplayPropertiesBuilder.ValuesEnum@endlink) TblIndepPtType
    ##  Returns the tbl indep pt type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.0.  Table independent domain display no longer modifies the file and is included only to enable old journals to function without modification @link NXOpen::Fields::DisplayPropertiesBuilder::ShowSrcTblVals NXOpen::Fields::DisplayPropertiesBuilder::ShowSrcTblVals@endlink  can be used to control source table values, but independent table values display is deprecated.  <br> 

    ## @return DisplayPropertiesBuilder.ValuesEnum
    @property
    def TblIndepPtType(self) -> DisplayPropertiesBuilder.ValuesEnum:
        """
        Getter for property: (@link DisplayPropertiesBuilder.ValuesEnum NXOpen.Fields.DisplayPropertiesBuilder.ValuesEnum@endlink) TblIndepPtType
         Returns the tbl indep pt type   
            
         
        """
        pass
    
    ## Setter for property: (@link DisplayPropertiesBuilder.ValuesEnum NXOpen.Fields.DisplayPropertiesBuilder.ValuesEnum@endlink) TblIndepPtType

    ##  Returns the tbl indep pt type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.0.  Table Independent variable display no longer modifies the file and is included only to enable old journals to function without modification. @link NXOpen::Fields::DisplayPropertiesBuilder::ShowSrcTblVals NXOpen::Fields::DisplayPropertiesBuilder::ShowSrcTblVals@endlink  can be used to show source table values, but independent table values display is deprecated.  <br> 

    @TblIndepPtType.setter
    def TblIndepPtType(self, tblIndepPtType: DisplayPropertiesBuilder.ValuesEnum):
        """
        Setter for property: (@link DisplayPropertiesBuilder.ValuesEnum NXOpen.Fields.DisplayPropertiesBuilder.ValuesEnum@endlink) TblIndepPtType
         Returns the tbl indep pt type   
            
         
        """
        pass
    
    ## Getter for property: (float) TblSurfaceOffset
    ##  Returns the table dependent surface offset scaling factor  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## @return float
    @property
    def TblSurfaceOffset(self) -> float:
        """
        Getter for property: (float) TblSurfaceOffset
         Returns the table dependent surface offset scaling factor  
            
         
        """
        pass
    
    ## Setter for property: (float) TblSurfaceOffset

    ##  Returns the table dependent surface offset scaling factor  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    @TblSurfaceOffset.setter
    def TblSurfaceOffset(self, tblDepSurfaceOffset: float):
        """
        Setter for property: (float) TblSurfaceOffset
         Returns the table dependent surface offset scaling factor  
            
         
        """
        pass
    
    ## Getter for property: (int) Translucency
    ##  Returns the translucency   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    ## @return int
    @property
    def Translucency(self) -> int:
        """
        Getter for property: (int) Translucency
         Returns the translucency   
            
         
        """
        pass
    
    ## Setter for property: (int) Translucency

    ##  Returns the translucency   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    @Translucency.setter
    def Translucency(self, translucency: int):
        """
        Setter for property: (int) Translucency
         Returns the translucency   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) UndefValueColor
    ##  Returns the undef value color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    ## @return NXOpen.NXColor
    @property
    def UndefValueColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) UndefValueColor
         Returns the undef value color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) UndefValueColor

    ##  Returns the undef value color   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    @UndefValueColor.setter
    def UndefValueColor(self, undefValueColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) UndefValueColor
         Returns the undef value color   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) UnderflowColor
    ##  Returns the underflow color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def UnderflowColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) UnderflowColor
         Returns the underflow color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) UnderflowColor

    ##  Returns the underflow color   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UnderflowColor.setter
    def UnderflowColor(self, underflowColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) UnderflowColor
         Returns the underflow color   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XMax
    ##  Returns the x max   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def XMax(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XMax
         Returns the x max   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XMin
    ##  Returns the x min   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def XMin(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XMin
         Returns the x min   
            
         
        """
        pass
    
    ## Getter for property: (int) XNum
    ##  Returns the x num   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def XNum(self) -> int:
        """
        Getter for property: (int) XNum
         Returns the x num   
            
         
        """
        pass
    
    ## Setter for property: (int) XNum

    ##  Returns the x num   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @XNum.setter
    def XNum(self, xNum: int):
        """
        Setter for property: (int) XNum
         Returns the x num   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YMax
    ##  Returns the y max   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def YMax(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YMax
         Returns the y max   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YMin
    ##  Returns the y min   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def YMin(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YMin
         Returns the y min   
            
         
        """
        pass
    
    ## Getter for property: (int) YNum
    ##  Returns the y num   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def YNum(self) -> int:
        """
        Getter for property: (int) YNum
         Returns the y num   
            
         
        """
        pass
    
    ## Setter for property: (int) YNum

    ##  Returns the y num   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @YNum.setter
    def YNum(self, yNum: int):
        """
        Setter for property: (int) YNum
         Returns the y num   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZMax
    ##  Returns the z max   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ZMax(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZMax
         Returns the z max   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZMin
    ##  Returns the z min   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ZMin(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZMin
         Returns the z min   
            
         
        """
        pass
    
    ## Getter for property: (int) ZNum
    ##  Returns the z num   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def ZNum(self) -> int:
        """
        Getter for property: (int) ZNum
         Returns the z num   
            
         
        """
        pass
    
    ## Setter for property: (int) ZNum

    ##  Returns the z num   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ZNum.setter
    def ZNum(self, zNum: int):
        """
        Setter for property: (int) ZNum
         Returns the z num   
            
         
        """
        pass
    
import NXOpen
##   @brief  Represents data for field export  
## 
##    <br> To create a new instance of this class, use @link NXOpen::Fields::FieldManager::CreateExportData  NXOpen::Fields::FieldManager::CreateExportData @endlink  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class ExportData(NXOpen.TransientObject): 
    """ <summary> Represents data for field export </summary> """


    ##  Add a field 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="field"> (@link Field NXOpen.Fields.Field@endlink)  field to add </param>
    def AddField(self, field: Field) -> None:
        """
         Add a field 
        """
        pass
    
    ##  Add a field 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="fields"> (@link Field List[NXOpen.Fields.Field]@endlink)  fields to add </param>
    def AddFields(self, fields: List[Field]) -> None:
        """
         Add a field 
        """
        pass
    
    ##  Destroys the object 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Destroys the object 
        """
        pass
    
    ##  Gets the fields 
    ##  @return fields (@link Field List[NXOpen.Fields.Field]@endlink):  fields .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def GetFields(self) -> List[Field]:
        """
         Gets the fields 
         @return fields (@link Field List[NXOpen.Fields.Field]@endlink):  fields .
        """
        pass
    
    ##  Get file name 
    ##  @return fileName (str):  file name .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def GetFileName(self) -> str:
        """
         Get file name 
         @return fileName (str):  file name .
        """
        pass
    
    ##  Set file name 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="file_name"> (str)  file name </param>
    def SetFileName(self, file_name: str) -> None:
        """
         Set file name 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##   @brief 
##             Represents a builder class for creating and editing an @link NXOpen::Fields::Field NXOpen::Fields::Field@endlink 
##             that is defined by an external file reference.
##          
## 
##  
##         
##          <br> 
##         This builder allows you to define an @link 
##         NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceCurve 
##         NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceCurve@endlink (2D) or
##        @link NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface@endlink 
##        (3D) profile from the data with an external file.
##        The file must have at least the number of columns of data required for by the dimension of the profile to be created.
##         <br> 
##         <br> 
##         For @link NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceCurve NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceCurve@endlink 
##         you need to specify two columns from the file.
##         <ul>
##          <li><ja_property_both>NXOpen.Fields.ExternalFileProfileBuilder.XColumn</ja_property_both>, the independent value</li>
##          <li><ja_property_both>NXOpen.Fields.ExternalFileProfileBuilder.OrdinateColumn</ja_property_both>, the dependent value</li>
##         </ul>
##         For @link NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface@endlink 
##         you need to specify three columns from the file.
##         <ul>
##          <li><ja_property_both>NXOpen.Fields.ExternalFileProfileBuilder.XColumn</ja_property_both>, the independent value</li>
##          <li><ja_property_both>NXOpen.Fields.ExternalFileProfileBuilder.YColumn</ja_property_both>, the independent value</li>
##          <li><ja_property_both>NXOpen.Fields.ExternalFileProfileBuilder.OrdinateColumn</ja_property_both>, the dependent value</li>
##         </ul>
##         Please refer to documentation for specific details on the file formats supported.
##          <br> 
##         
## 
##   <br>  Created in NX1847.0.0  <br> 

class ExternalFileProfileBuilder(NXOpen.TaggedObject): 
    """ <summary>
            Represents a builder class for creating and editing an <ja_class>NXOpen.Fields.Field</ja_class>
            that is defined by an external file reference.
        </summary>
        <remarks>
        <para>
        This builder allows you to define an <ja_enum_member>
        NXOpen.Fields.ExternalFileProfileBuilder.DimensionChoice.Curve</ja_enum_member>(2D) or
       <ja_enum_member>NXOpen.Fields.ExternalFileProfileBuilder.DimensionChoice.Surface</ja_enum_member>
       (3D) profile from the data with an external file.
       The file must have at least the number of columns of data required for by the dimension of the profile to be created.
       </para>
       <para>
        For <ja_enum_member>NXOpen.Fields.ExternalFileProfileBuilder.DimensionChoice.Curve</ja_enum_member>
        you need to specify two columns from the file.
        <ul>
         <li><ja_property_both>NXOpen.Fields.ExternalFileProfileBuilder.XColumn</ja_property_both>, the independent value</li>
         <li><ja_property_both>NXOpen.Fields.ExternalFileProfileBuilder.OrdinateColumn</ja_property_both>, the dependent value</li>
        </ul>
        For <ja_enum_member>NXOpen.Fields.ExternalFileProfileBuilder.DimensionChoice.Surface</ja_enum_member>
        you need to specify three columns from the file.
        <ul>
         <li><ja_property_both>NXOpen.Fields.ExternalFileProfileBuilder.XColumn</ja_property_both>, the independent value</li>
         <li><ja_property_both>NXOpen.Fields.ExternalFileProfileBuilder.YColumn</ja_property_both>, the independent value</li>
         <li><ja_property_both>NXOpen.Fields.ExternalFileProfileBuilder.OrdinateColumn</ja_property_both>, the dependent value</li>
        </ul>
        Please refer to documentation for specific details on the file formats supported.
        </para>
        </remarks>"""


    ##   @brief 
    ##             Defines if the profile is repeating cyclically in any direction.
    ##          
    ## 
    ##  
    ##         
    ##             This is overriding extrapolation if not set to
    ##             @link NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeNone NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeNone@endlink .
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ##  not cyclic </description> </item><item><term> 
    ## XOnly</term><description> 
    ##  cyclic in x direction </description> </item><item><term> 
    ## YOnly</term><description> 
    ##  cyclic in y direction </description> </item><item><term> 
    ## Both</term><description> 
    ##  cyclic in both x and y direction </description> </item></list>
    class CyclicType(Enum):
        """
        Members Include: <NotSet> <XOnly> <YOnly> <Both>
        """
        NotSet: int
        XOnly: int
        YOnly: int
        Both: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ExternalFileProfileBuilder.CyclicType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##   @brief 
    ##             the dimension of the profile
    ##          
    ## 
    ##   
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Curve</term><description> 
    ##  two dimensional with x axis and ordinate </description> </item><item><term> 
    ## Surface</term><description> 
    ##  three dimensional with x axis, y axis and ordinate </description> </item><item><term> 
    ## Any</term><description> 
    ##  undefined dimension, which an existing profile can never actually have </description> </item></list>
    class DimensionChoice(Enum):
        """
        Members Include: <Curve> <Surface> <Any>
        """
        Curve: int
        Surface: int
        Any: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ExternalFileProfileBuilder.DimensionChoice:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##   @brief 
    ##             the extrapolation method used for the profile
    ##          
    ## 
    ##   
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Linear</term><description> 
    ##  Linear </description> </item><item><term> 
    ## Parabolic</term><description> 
    ##  Parabolic </description> </item><item><term> 
    ## Cubic</term><description> 
    ##  Cubic </description> </item></list>
    class Extrapolation(Enum):
        """
        Members Include: <Linear> <Parabolic> <Cubic>
        """
        Linear: int
        Parabolic: int
        Cubic: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ExternalFileProfileBuilder.Extrapolation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##   @brief 
    ##             the format control method used for the profile
    ##          
    ## 
    ##   
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ComputerRegionalSettings</term><description> 
    ##  Use Computer Regional Settings </description> </item><item><term> 
    ## DotDecimalSeparator</term><description> 
    ##  Use . as decimal separator </description> </item><item><term> 
    ## CommaDecimalSeparator</term><description> 
    ##  Use , as decimal separator </description> </item><item><term> 
    ## DotDecimalSeparatorAndCommaValueDelimiter</term><description> 
    ##  Use . as decimal separator and , as value delimiter</description> </item><item><term> 
    ## CommaDecimalSeparatorAndSemicolonValueDelimiter</term><description> 
    ##  Use , as decimal separator and ; as value delimiter</description> </item></list>
    class FormatOptions(Enum):
        """
        Members Include: <ComputerRegionalSettings> <DotDecimalSeparator> <CommaDecimalSeparator> <DotDecimalSeparatorAndCommaValueDelimiter> <CommaDecimalSeparatorAndSemicolonValueDelimiter>
        """
        ComputerRegionalSettings: int
        DotDecimalSeparator: int
        CommaDecimalSeparator: int
        DotDecimalSeparatorAndCommaValueDelimiter: int
        CommaDecimalSeparatorAndSemicolonValueDelimiter: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ExternalFileProfileBuilder.FormatOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##   @brief 
    ##             the interpolation method used for the profile
    ##          
    ## 
    ##   
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Linear</term><description> 
    ##  Linear </description> </item><item><term> 
    ## Akima</term><description> 
    ##  Akima </description> </item><item><term> 
    ## Akima72</term><description> 
    ##  Akima72 </description> </item><item><term> 
    ## Cubic</term><description> 
    ##  Cubic </description> </item></list>
    class Interpolation(Enum):
        """
        Members Include: <Linear> <Akima> <Akima72> <Cubic>
        """
        Linear: int
        Akima: int
        Akima72: int
        Cubic: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ExternalFileProfileBuilder.Interpolation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link ExternalFileProfileBuilder.CyclicType NXOpen.Fields.ExternalFileProfileBuilder.CyclicType@endlink) Cyclic
    ##  Returns  @brief 
    ##             the cyclic type.  
    ##   
    ##              
    ## 
    ##  
    ##             
    ##             <ul>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeNone NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeNone@endlink </li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeXOnly NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeXOnly@endlink </li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeYOnly NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeYOnly@endlink </li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeBoth NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeBoth@endlink </li>
    ##             </ul>
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link NXOpen::Fields::ProfileSolverOptionsBuilder::Cyclic NXOpen::Fields::ProfileSolverOptionsBuilder::Cyclic@endlink  instead.  <br> 

    ## @return ExternalFileProfileBuilder.CyclicType
    @property
    def Cyclic(self) -> ExternalFileProfileBuilder.CyclicType:
        """
        Getter for property: (@link ExternalFileProfileBuilder.CyclicType NXOpen.Fields.ExternalFileProfileBuilder.CyclicType@endlink) Cyclic
         Returns  @brief 
                    the cyclic type.  
          
                     
        
         
                    
                    <ul>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeNone NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeNone@endlink </li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeXOnly NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeXOnly@endlink </li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeYOnly NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeYOnly@endlink </li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeBoth NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeBoth@endlink </li>
                    </ul>
                      
         
        """
        pass
    
    ## Setter for property: (@link ExternalFileProfileBuilder.CyclicType NXOpen.Fields.ExternalFileProfileBuilder.CyclicType@endlink) Cyclic

    ##  Returns  @brief 
    ##             the cyclic type.  
    ##   
    ##              
    ## 
    ##  
    ##             
    ##             <ul>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeNone NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeNone@endlink </li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeXOnly NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeXOnly@endlink </li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeYOnly NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeYOnly@endlink </li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeBoth NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeBoth@endlink </li>
    ##             </ul>
    ##               
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link NXOpen::Fields::ProfileSolverOptionsBuilder::SetCyclic NXOpen::Fields::ProfileSolverOptionsBuilder::SetCyclic@endlink  instead.  <br> 

    @Cyclic.setter
    def Cyclic(self, cyclicType: ExternalFileProfileBuilder.CyclicType):
        """
        Setter for property: (@link ExternalFileProfileBuilder.CyclicType NXOpen.Fields.ExternalFileProfileBuilder.CyclicType@endlink) Cyclic
         Returns  @brief 
                    the cyclic type.  
          
                     
        
         
                    
                    <ul>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeNone NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeNone@endlink </li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeXOnly NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeXOnly@endlink </li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeYOnly NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeYOnly@endlink </li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeBoth NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeBoth@endlink </li>
                    </ul>
                      
         
        """
        pass
    
    ## Getter for property: (@link ExternalFileProfileBuilder.DimensionChoice NXOpen.Fields.ExternalFileProfileBuilder.DimensionChoice@endlink) Dimension
    ##  Returns  @brief 
    ##             the dimension.  
    ##   
    ##              
    ## 
    ##  
    ##             
    ##             <ul>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceCurve NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceCurve@endlink  2D</li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface@endlink  3D</li>
    ##             </ul>
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return ExternalFileProfileBuilder.DimensionChoice
    @property
    def Dimension(self) -> ExternalFileProfileBuilder.DimensionChoice:
        """
        Getter for property: (@link ExternalFileProfileBuilder.DimensionChoice NXOpen.Fields.ExternalFileProfileBuilder.DimensionChoice@endlink) Dimension
         Returns  @brief 
                    the dimension.  
          
                     
        
         
                    
                    <ul>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceCurve NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceCurve@endlink  2D</li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface@endlink  3D</li>
                    </ul>
                      
         
        """
        pass
    
    ## Setter for property: (@link ExternalFileProfileBuilder.DimensionChoice NXOpen.Fields.ExternalFileProfileBuilder.DimensionChoice@endlink) Dimension

    ##  Returns  @brief 
    ##             the dimension.  
    ##   
    ##              
    ## 
    ##  
    ##             
    ##             <ul>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceCurve NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceCurve@endlink  2D</li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface@endlink  3D</li>
    ##             </ul>
    ##               
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Dimension.setter
    def Dimension(self, dimension: ExternalFileProfileBuilder.DimensionChoice):
        """
        Setter for property: (@link ExternalFileProfileBuilder.DimensionChoice NXOpen.Fields.ExternalFileProfileBuilder.DimensionChoice@endlink) Dimension
         Returns  @brief 
                    the dimension.  
          
                     
        
         
                    
                    <ul>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceCurve NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceCurve@endlink  2D</li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface@endlink  3D</li>
                    </ul>
                      
         
        """
        pass
    
    ## Getter for property: (@link ExternalFileProfileBuilder.FormatOptions NXOpen.Fields.ExternalFileProfileBuilder.FormatOptions@endlink) FormatControlOption
    ##  Returns  @brief 
    ##             the format control of separators 
    ##              
    ##   
    ##   
    ##  
    ##             
    ##             <ul>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsComputerRegionalSettings NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsComputerRegionalSettings@endlink </li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsDotDecimalSeparator NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsDotDecimalSeparator@endlink </li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsCommaDecimalSeparator NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsCommaDecimalSeparator@endlink </li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsDotDecimalSeparatorAndCommaValueDelimiter NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsDotDecimalSeparatorAndCommaValueDelimiter@endlink </li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsCommaDecimalSeparatorAndSemicolonValueDelimiter NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsCommaDecimalSeparatorAndSemicolonValueDelimiter@endlink </li>
    ##             </ul>
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return ExternalFileProfileBuilder.FormatOptions
    @property
    def FormatControlOption(self) -> ExternalFileProfileBuilder.FormatOptions:
        """
        Getter for property: (@link ExternalFileProfileBuilder.FormatOptions NXOpen.Fields.ExternalFileProfileBuilder.FormatOptions@endlink) FormatControlOption
         Returns  @brief 
                    the format control of separators 
                     
          
          
         
                    
                    <ul>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsComputerRegionalSettings NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsComputerRegionalSettings@endlink </li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsDotDecimalSeparator NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsDotDecimalSeparator@endlink </li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsCommaDecimalSeparator NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsCommaDecimalSeparator@endlink </li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsDotDecimalSeparatorAndCommaValueDelimiter NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsDotDecimalSeparatorAndCommaValueDelimiter@endlink </li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsCommaDecimalSeparatorAndSemicolonValueDelimiter NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsCommaDecimalSeparatorAndSemicolonValueDelimiter@endlink </li>
                    </ul>
                      
         
        """
        pass
    
    ## Setter for property: (@link ExternalFileProfileBuilder.FormatOptions NXOpen.Fields.ExternalFileProfileBuilder.FormatOptions@endlink) FormatControlOption

    ##  Returns  @brief 
    ##             the format control of separators 
    ##              
    ##   
    ##   
    ##  
    ##             
    ##             <ul>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsComputerRegionalSettings NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsComputerRegionalSettings@endlink </li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsDotDecimalSeparator NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsDotDecimalSeparator@endlink </li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsCommaDecimalSeparator NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsCommaDecimalSeparator@endlink </li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsDotDecimalSeparatorAndCommaValueDelimiter NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsDotDecimalSeparatorAndCommaValueDelimiter@endlink </li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsCommaDecimalSeparatorAndSemicolonValueDelimiter NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsCommaDecimalSeparatorAndSemicolonValueDelimiter@endlink </li>
    ##             </ul>
    ##               
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @FormatControlOption.setter
    def FormatControlOption(self, formatControlType: ExternalFileProfileBuilder.FormatOptions):
        """
        Setter for property: (@link ExternalFileProfileBuilder.FormatOptions NXOpen.Fields.ExternalFileProfileBuilder.FormatOptions@endlink) FormatControlOption
         Returns  @brief 
                    the format control of separators 
                     
          
          
         
                    
                    <ul>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsComputerRegionalSettings NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsComputerRegionalSettings@endlink </li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsDotDecimalSeparator NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsDotDecimalSeparator@endlink </li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsCommaDecimalSeparator NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsCommaDecimalSeparator@endlink </li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsDotDecimalSeparatorAndCommaValueDelimiter NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsDotDecimalSeparatorAndCommaValueDelimiter@endlink </li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsCommaDecimalSeparatorAndSemicolonValueDelimiter NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsCommaDecimalSeparatorAndSemicolonValueDelimiter@endlink </li>
                    </ul>
                      
         
        """
        pass
    
    ## Getter for property: (int) OrdinateColumn
    ##  Returns  @brief 
    ##             the column number in the external file corresponding to the ordinate axis.  
    ##   
    ##              
    ## 
    ##  
    ##             
    ##             Column A of an excel file corresponds to the number 1.
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def OrdinateColumn(self) -> int:
        """
        Getter for property: (int) OrdinateColumn
         Returns  @brief 
                    the column number in the external file corresponding to the ordinate axis.  
          
                     
        
         
                    
                    Column A of an excel file corresponds to the number 1.
                      
         
        """
        pass
    
    ## Setter for property: (int) OrdinateColumn

    ##  Returns  @brief 
    ##             the column number in the external file corresponding to the ordinate axis.  
    ##   
    ##              
    ## 
    ##  
    ##             
    ##             Column A of an excel file corresponds to the number 1.
    ##               
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @OrdinateColumn.setter
    def OrdinateColumn(self, columnIdx: int):
        """
        Setter for property: (int) OrdinateColumn
         Returns  @brief 
                    the column number in the external file corresponding to the ordinate axis.  
          
                     
        
         
                    
                    Column A of an excel file corresponds to the number 1.
                      
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OrdinateOffset
    ##  Returns  @brief 
    ##             the offset on the ordinate axis.  
    ##   
    ##              
    ## 
    ##  
    ##             
    ##             The unit of the offset has to match the unit defined in the header
    ##             of the @link NXOpen::Fields::ExternalFileProfileBuilder::OrdinateColumn NXOpen::Fields::ExternalFileProfileBuilder::OrdinateColumn@endlink 
    ##             in the file set in @link NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference@endlink .
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def OrdinateOffset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OrdinateOffset
         Returns  @brief 
                    the offset on the ordinate axis.  
          
                     
        
         
                    
                    The unit of the offset has to match the unit defined in the header
                    of the @link NXOpen::Fields::ExternalFileProfileBuilder::OrdinateColumn NXOpen::Fields::ExternalFileProfileBuilder::OrdinateColumn@endlink 
                    in the file set in @link NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference@endlink .
                      
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OrdinateScale
    ##  Returns  @brief 
    ##             the scale on the ordinate axis.  
    ##   
    ##              
    ## 
    ##  
    ##             The scale is unitless.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def OrdinateScale(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OrdinateScale
         Returns  @brief 
                    the scale on the ordinate axis.  
          
                     
        
         
                    The scale is unitless.  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SlopeLeft
    ##  Returns  @brief 
    ##             the left slope.  
    ##   
    ##              
    ## 
    ##  
    ##             
    ##             This is only used when @link NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice@endlink 
    ##             is set to @link NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceCurve NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceCurve@endlink 
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link NXOpen::Fields::ProfileSolverOptionsBuilder::SlopeLeft NXOpen::Fields::ProfileSolverOptionsBuilder::SlopeLeft@endlink  instead.  <br> 

    ## @return NXOpen.Expression
    @property
    def SlopeLeft(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SlopeLeft
         Returns  @brief 
                    the left slope.  
          
                     
        
         
                    
                    This is only used when @link NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice@endlink 
                    is set to @link NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceCurve NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceCurve@endlink 
                      
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SlopeRight
    ##  Returns  @brief 
    ##             the right slope.  
    ##   
    ##              
    ## 
    ##  
    ##             
    ##             This is only used when @link NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice@endlink 
    ##             is set to @link NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceCurve NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceCurve@endlink 
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link NXOpen::Fields::ProfileSolverOptionsBuilder::SlopeRight NXOpen::Fields::ProfileSolverOptionsBuilder::SlopeRight@endlink  instead.  <br> 

    ## @return NXOpen.Expression
    @property
    def SlopeRight(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SlopeRight
         Returns  @brief 
                    the right slope.  
          
                     
        
         
                    
                    This is only used when @link NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice@endlink 
                    is set to @link NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceCurve NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceCurve@endlink 
                      
         
        """
        pass
    
    ## Getter for property: (@link ProfileSolverOptionsBuilder NXOpen.Fields.ProfileSolverOptionsBuilder@endlink) SolverOptions
    ##  Returns  @brief the solver options.  
    ##    
    ## 
    ##    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return ProfileSolverOptionsBuilder
    @property
    def SolverOptions(self) -> ProfileSolverOptionsBuilder:
        """
        Getter for property: (@link ProfileSolverOptionsBuilder NXOpen.Fields.ProfileSolverOptionsBuilder@endlink) SolverOptions
         Returns  @brief the solver options.  
           
        
           
         
        """
        pass
    
    ## Getter for property: (int) XColumn
    ##  Returns  @brief 
    ##             the column number in the external file corresponding to the x axis.  
    ##   
    ##              
    ## 
    ##  
    ##             
    ##             Column A of an excel file corresponds to the number 1.
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def XColumn(self) -> int:
        """
        Getter for property: (int) XColumn
         Returns  @brief 
                    the column number in the external file corresponding to the x axis.  
          
                     
        
         
                    
                    Column A of an excel file corresponds to the number 1.
                      
         
        """
        pass
    
    ## Setter for property: (int) XColumn

    ##  Returns  @brief 
    ##             the column number in the external file corresponding to the x axis.  
    ##   
    ##              
    ## 
    ##  
    ##             
    ##             Column A of an excel file corresponds to the number 1.
    ##               
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @XColumn.setter
    def XColumn(self, columnIdx: int):
        """
        Setter for property: (int) XColumn
         Returns  @brief 
                    the column number in the external file corresponding to the x axis.  
          
                     
        
         
                    
                    Column A of an excel file corresponds to the number 1.
                      
         
        """
        pass
    
    ## Getter for property: (@link ExternalFileProfileBuilder.Extrapolation NXOpen.Fields.ExternalFileProfileBuilder.Extrapolation@endlink) XExtrapolation
    ##  Returns  @brief 
    ##             the extrapolation in x direction.  
    ##   
    ##              
    ## 
    ##  
    ##             
    ##             <ul>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationLinear NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationLinear@endlink </li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationParabolic NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationParabolic@endlink </li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationCubic NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationCubic@endlink </li>
    ##             </ul>
    ##              <br> 
    ##             This is only used when @link NXOpen::Fields::ExternalFileProfileBuilder::SetCyclicType NXOpen::Fields::ExternalFileProfileBuilder::SetCyclicType@endlink 
    ##             is set to @link NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeNone NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeNone@endlink 
    ##             or @link NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeYOnly NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeYOnly@endlink 
    ##              <br> 
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link NXOpen::Fields::ProfileSolverOptionsBuilder::XExtrapolation NXOpen::Fields::ProfileSolverOptionsBuilder::XExtrapolation@endlink  instead.  <br> 

    ## @return ExternalFileProfileBuilder.Extrapolation
    @property
    def XExtrapolation(self) -> ExternalFileProfileBuilder.Extrapolation:
        """
        Getter for property: (@link ExternalFileProfileBuilder.Extrapolation NXOpen.Fields.ExternalFileProfileBuilder.Extrapolation@endlink) XExtrapolation
         Returns  @brief 
                    the extrapolation in x direction.  
          
                     
        
         
                    
                    <ul>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationLinear NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationLinear@endlink </li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationParabolic NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationParabolic@endlink </li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationCubic NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationCubic@endlink </li>
                    </ul>
                     <br> 
                    This is only used when @link NXOpen::Fields::ExternalFileProfileBuilder::SetCyclicType NXOpen::Fields::ExternalFileProfileBuilder::SetCyclicType@endlink 
                    is set to @link NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeNone NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeNone@endlink 
                    or @link NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeYOnly NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeYOnly@endlink 
                     <br> 
                      
         
        """
        pass
    
    ## Setter for property: (@link ExternalFileProfileBuilder.Extrapolation NXOpen.Fields.ExternalFileProfileBuilder.Extrapolation@endlink) XExtrapolation

    ##  Returns  @brief 
    ##             the extrapolation in x direction.  
    ##   
    ##              
    ## 
    ##  
    ##             
    ##             <ul>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationLinear NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationLinear@endlink </li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationParabolic NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationParabolic@endlink </li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationCubic NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationCubic@endlink </li>
    ##             </ul>
    ##              <br> 
    ##             This is only used when @link NXOpen::Fields::ExternalFileProfileBuilder::SetCyclicType NXOpen::Fields::ExternalFileProfileBuilder::SetCyclicType@endlink 
    ##             is set to @link NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeNone NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeNone@endlink 
    ##             or @link NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeYOnly NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeYOnly@endlink 
    ##              <br> 
    ##               
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link NXOpen::Fields::ProfileSolverOptionsBuilder::SetXExtrapolation NXOpen::Fields::ProfileSolverOptionsBuilder::SetXExtrapolation@endlink  instead.  <br> 

    @XExtrapolation.setter
    def XExtrapolation(self, extrapolation: ExternalFileProfileBuilder.Extrapolation):
        """
        Setter for property: (@link ExternalFileProfileBuilder.Extrapolation NXOpen.Fields.ExternalFileProfileBuilder.Extrapolation@endlink) XExtrapolation
         Returns  @brief 
                    the extrapolation in x direction.  
          
                     
        
         
                    
                    <ul>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationLinear NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationLinear@endlink </li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationParabolic NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationParabolic@endlink </li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationCubic NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationCubic@endlink </li>
                    </ul>
                     <br> 
                    This is only used when @link NXOpen::Fields::ExternalFileProfileBuilder::SetCyclicType NXOpen::Fields::ExternalFileProfileBuilder::SetCyclicType@endlink 
                    is set to @link NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeNone NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeNone@endlink 
                    or @link NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeYOnly NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeYOnly@endlink 
                     <br> 
                      
         
        """
        pass
    
    ## Getter for property: (@link ExternalFileProfileBuilder.Interpolation NXOpen.Fields.ExternalFileProfileBuilder.Interpolation@endlink) XInterpolation
    ##  Returns  @brief 
    ##             the interpolation in x direction.  
    ##   
    ##              
    ## 
    ##  
    ##             
    ##             <ul>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::InterpolationLinear NXOpen::Fields::ExternalFileProfileBuilder::InterpolationLinear@endlink </li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima@endlink </li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima72 NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima72@endlink </li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::InterpolationCubic NXOpen::Fields::ExternalFileProfileBuilder::InterpolationCubic@endlink </li>
    ##             </ul>
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link NXOpen::Fields::ProfileSolverOptionsBuilder::XInterpolation NXOpen::Fields::ProfileSolverOptionsBuilder::XInterpolation@endlink  instead.  <br> 

    ## @return ExternalFileProfileBuilder.Interpolation
    @property
    def XInterpolation(self) -> ExternalFileProfileBuilder.Interpolation:
        """
        Getter for property: (@link ExternalFileProfileBuilder.Interpolation NXOpen.Fields.ExternalFileProfileBuilder.Interpolation@endlink) XInterpolation
         Returns  @brief 
                    the interpolation in x direction.  
          
                     
        
         
                    
                    <ul>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::InterpolationLinear NXOpen::Fields::ExternalFileProfileBuilder::InterpolationLinear@endlink </li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima@endlink </li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima72 NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima72@endlink </li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::InterpolationCubic NXOpen::Fields::ExternalFileProfileBuilder::InterpolationCubic@endlink </li>
                    </ul>
                      
         
        """
        pass
    
    ## Setter for property: (@link ExternalFileProfileBuilder.Interpolation NXOpen.Fields.ExternalFileProfileBuilder.Interpolation@endlink) XInterpolation

    ##  Returns  @brief 
    ##             the interpolation in x direction.  
    ##   
    ##              
    ## 
    ##  
    ##             
    ##             <ul>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::InterpolationLinear NXOpen::Fields::ExternalFileProfileBuilder::InterpolationLinear@endlink </li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima@endlink </li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima72 NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima72@endlink </li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::InterpolationCubic NXOpen::Fields::ExternalFileProfileBuilder::InterpolationCubic@endlink </li>
    ##             </ul>
    ##               
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link NXOpen::Fields::ProfileSolverOptionsBuilder::SetXInterpolation NXOpen::Fields::ProfileSolverOptionsBuilder::SetXInterpolation@endlink  instead.  <br> 

    @XInterpolation.setter
    def XInterpolation(self, interpolation: ExternalFileProfileBuilder.Interpolation):
        """
        Setter for property: (@link ExternalFileProfileBuilder.Interpolation NXOpen.Fields.ExternalFileProfileBuilder.Interpolation@endlink) XInterpolation
         Returns  @brief 
                    the interpolation in x direction.  
          
                     
        
         
                    
                    <ul>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::InterpolationLinear NXOpen::Fields::ExternalFileProfileBuilder::InterpolationLinear@endlink </li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima@endlink </li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima72 NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima72@endlink </li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::InterpolationCubic NXOpen::Fields::ExternalFileProfileBuilder::InterpolationCubic@endlink </li>
                    </ul>
                      
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XOffset
    ##  Returns  @brief 
    ##             the offset on the x axis.  
    ##   
    ##              
    ## 
    ##  
    ##             
    ##             The unit of the offset has to match the unit defined in the header
    ##             of the @link NXOpen::Fields::ExternalFileProfileBuilder::XColumn NXOpen::Fields::ExternalFileProfileBuilder::XColumn@endlink 
    ##             in the file set in @link NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference@endlink .
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def XOffset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XOffset
         Returns  @brief 
                    the offset on the x axis.  
          
                     
        
         
                    
                    The unit of the offset has to match the unit defined in the header
                    of the @link NXOpen::Fields::ExternalFileProfileBuilder::XColumn NXOpen::Fields::ExternalFileProfileBuilder::XColumn@endlink 
                    in the file set in @link NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference@endlink .
                      
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XScale
    ##  Returns  @brief 
    ##             the scale on the x axis.  
    ##   
    ##              
    ## 
    ##  
    ##             The scale is unitless.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def XScale(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XScale
         Returns  @brief 
                    the scale on the x axis.  
          
                     
        
         
                    The scale is unitless.  
         
        """
        pass
    
    ## Getter for property: (int) YColumn
    ##  Returns  @brief 
    ##             the column number in the external file corresponding to the y axis.  
    ##   
    ##              
    ## 
    ##  
    ##             
    ##              <br> 
    ##             Column A of an excel file corresponds to the number 1.
    ##              <br> 
    ##              <br> 
    ##             This is only used when @link NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice@endlink 
    ##             is set to @link NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface@endlink .
    ##              <br> 
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def YColumn(self) -> int:
        """
        Getter for property: (int) YColumn
         Returns  @brief 
                    the column number in the external file corresponding to the y axis.  
          
                     
        
         
                    
                     <br> 
                    Column A of an excel file corresponds to the number 1.
                     <br> 
                     <br> 
                    This is only used when @link NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice@endlink 
                    is set to @link NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface@endlink .
                     <br> 
                      
         
        """
        pass
    
    ## Setter for property: (int) YColumn

    ##  Returns  @brief 
    ##             the column number in the external file corresponding to the y axis.  
    ##   
    ##              
    ## 
    ##  
    ##             
    ##              <br> 
    ##             Column A of an excel file corresponds to the number 1.
    ##              <br> 
    ##              <br> 
    ##             This is only used when @link NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice@endlink 
    ##             is set to @link NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface@endlink .
    ##              <br> 
    ##               
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @YColumn.setter
    def YColumn(self, columnIdx: int):
        """
        Setter for property: (int) YColumn
         Returns  @brief 
                    the column number in the external file corresponding to the y axis.  
          
                     
        
         
                    
                     <br> 
                    Column A of an excel file corresponds to the number 1.
                     <br> 
                     <br> 
                    This is only used when @link NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice@endlink 
                    is set to @link NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface@endlink .
                     <br> 
                      
         
        """
        pass
    
    ## Getter for property: (@link ExternalFileProfileBuilder.Extrapolation NXOpen.Fields.ExternalFileProfileBuilder.Extrapolation@endlink) YExtrapolation
    ##  Returns  @brief 
    ##             the extrapolation in y direction.  
    ##   
    ##              
    ## 
    ##  
    ##             
    ##             <ul>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationLinear NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationLinear@endlink </li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationParabolic NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationParabolic@endlink </li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationCubic NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationCubic@endlink </li>
    ##             </ul>
    ##              <br> 
    ##             This is only used when @link NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice@endlink 
    ##             is set to @link NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface@endlink 
    ##             and when @link NXOpen::Fields::ExternalFileProfileBuilder::SetCyclicType NXOpen::Fields::ExternalFileProfileBuilder::SetCyclicType@endlink 
    ##             is set to @link NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeNone NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeNone@endlink 
    ##             or @link NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeXOnly NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeXOnly@endlink 
    ##              <br> 
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link NXOpen::Fields::ProfileSolverOptionsBuilder::YExtrapolation NXOpen::Fields::ProfileSolverOptionsBuilder::YExtrapolation@endlink  instead.  <br> 

    ## @return ExternalFileProfileBuilder.Extrapolation
    @property
    def YExtrapolation(self) -> ExternalFileProfileBuilder.Extrapolation:
        """
        Getter for property: (@link ExternalFileProfileBuilder.Extrapolation NXOpen.Fields.ExternalFileProfileBuilder.Extrapolation@endlink) YExtrapolation
         Returns  @brief 
                    the extrapolation in y direction.  
          
                     
        
         
                    
                    <ul>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationLinear NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationLinear@endlink </li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationParabolic NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationParabolic@endlink </li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationCubic NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationCubic@endlink </li>
                    </ul>
                     <br> 
                    This is only used when @link NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice@endlink 
                    is set to @link NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface@endlink 
                    and when @link NXOpen::Fields::ExternalFileProfileBuilder::SetCyclicType NXOpen::Fields::ExternalFileProfileBuilder::SetCyclicType@endlink 
                    is set to @link NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeNone NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeNone@endlink 
                    or @link NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeXOnly NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeXOnly@endlink 
                     <br> 
                      
         
        """
        pass
    
    ## Setter for property: (@link ExternalFileProfileBuilder.Extrapolation NXOpen.Fields.ExternalFileProfileBuilder.Extrapolation@endlink) YExtrapolation

    ##  Returns  @brief 
    ##             the extrapolation in y direction.  
    ##   
    ##              
    ## 
    ##  
    ##             
    ##             <ul>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationLinear NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationLinear@endlink </li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationParabolic NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationParabolic@endlink </li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationCubic NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationCubic@endlink </li>
    ##             </ul>
    ##              <br> 
    ##             This is only used when @link NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice@endlink 
    ##             is set to @link NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface@endlink 
    ##             and when @link NXOpen::Fields::ExternalFileProfileBuilder::SetCyclicType NXOpen::Fields::ExternalFileProfileBuilder::SetCyclicType@endlink 
    ##             is set to @link NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeNone NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeNone@endlink 
    ##             or @link NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeXOnly NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeXOnly@endlink 
    ##              <br> 
    ##               
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link NXOpen::Fields::ProfileSolverOptionsBuilder::SetYExtrapolation NXOpen::Fields::ProfileSolverOptionsBuilder::SetYExtrapolation@endlink  instead.  <br> 

    @YExtrapolation.setter
    def YExtrapolation(self, extrapolation: ExternalFileProfileBuilder.Extrapolation):
        """
        Setter for property: (@link ExternalFileProfileBuilder.Extrapolation NXOpen.Fields.ExternalFileProfileBuilder.Extrapolation@endlink) YExtrapolation
         Returns  @brief 
                    the extrapolation in y direction.  
          
                     
        
         
                    
                    <ul>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationLinear NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationLinear@endlink </li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationParabolic NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationParabolic@endlink </li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationCubic NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationCubic@endlink </li>
                    </ul>
                     <br> 
                    This is only used when @link NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice@endlink 
                    is set to @link NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface@endlink 
                    and when @link NXOpen::Fields::ExternalFileProfileBuilder::SetCyclicType NXOpen::Fields::ExternalFileProfileBuilder::SetCyclicType@endlink 
                    is set to @link NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeNone NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeNone@endlink 
                    or @link NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeXOnly NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeXOnly@endlink 
                     <br> 
                      
         
        """
        pass
    
    ## Getter for property: (@link ExternalFileProfileBuilder.Interpolation NXOpen.Fields.ExternalFileProfileBuilder.Interpolation@endlink) YInterpolation
    ##  Returns  @brief 
    ##             the interpolation in y direction.  
    ##   
    ##              
    ## 
    ##  
    ##             
    ##             <ul>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::InterpolationLinear NXOpen::Fields::ExternalFileProfileBuilder::InterpolationLinear@endlink </li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima@endlink </li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima72 NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima72@endlink </li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::InterpolationCubic NXOpen::Fields::ExternalFileProfileBuilder::InterpolationCubic@endlink </li>
    ##             </ul>
    ##              <br> 
    ##             This is only used when @link NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice@endlink 
    ##             is set to @link NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface@endlink 
    ##              <br> 
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link NXOpen::Fields::ProfileSolverOptionsBuilder::YInterpolation NXOpen::Fields::ProfileSolverOptionsBuilder::YInterpolation@endlink  instead.  <br> 

    ## @return ExternalFileProfileBuilder.Interpolation
    @property
    def YInterpolation(self) -> ExternalFileProfileBuilder.Interpolation:
        """
        Getter for property: (@link ExternalFileProfileBuilder.Interpolation NXOpen.Fields.ExternalFileProfileBuilder.Interpolation@endlink) YInterpolation
         Returns  @brief 
                    the interpolation in y direction.  
          
                     
        
         
                    
                    <ul>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::InterpolationLinear NXOpen::Fields::ExternalFileProfileBuilder::InterpolationLinear@endlink </li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima@endlink </li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima72 NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima72@endlink </li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::InterpolationCubic NXOpen::Fields::ExternalFileProfileBuilder::InterpolationCubic@endlink </li>
                    </ul>
                     <br> 
                    This is only used when @link NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice@endlink 
                    is set to @link NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface@endlink 
                     <br> 
                      
         
        """
        pass
    
    ## Setter for property: (@link ExternalFileProfileBuilder.Interpolation NXOpen.Fields.ExternalFileProfileBuilder.Interpolation@endlink) YInterpolation

    ##  Returns  @brief 
    ##             the interpolation in y direction.  
    ##   
    ##              
    ## 
    ##  
    ##             
    ##             <ul>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::InterpolationLinear NXOpen::Fields::ExternalFileProfileBuilder::InterpolationLinear@endlink </li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima@endlink </li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima72 NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima72@endlink </li>
    ##               <li>@link NXOpen::Fields::ExternalFileProfileBuilder::InterpolationCubic NXOpen::Fields::ExternalFileProfileBuilder::InterpolationCubic@endlink </li>
    ##             </ul>
    ##              <br> 
    ##             This is only used when @link NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice@endlink 
    ##             is set to @link NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface@endlink 
    ##              <br> 
    ##               
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link NXOpen::Fields::ProfileSolverOptionsBuilder::SetYInterpolation NXOpen::Fields::ProfileSolverOptionsBuilder::SetYInterpolation@endlink  instead.  <br> 

    @YInterpolation.setter
    def YInterpolation(self, interpolation: ExternalFileProfileBuilder.Interpolation):
        """
        Setter for property: (@link ExternalFileProfileBuilder.Interpolation NXOpen.Fields.ExternalFileProfileBuilder.Interpolation@endlink) YInterpolation
         Returns  @brief 
                    the interpolation in y direction.  
          
                     
        
         
                    
                    <ul>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::InterpolationLinear NXOpen::Fields::ExternalFileProfileBuilder::InterpolationLinear@endlink </li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima@endlink </li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima72 NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima72@endlink </li>
                      <li>@link NXOpen::Fields::ExternalFileProfileBuilder::InterpolationCubic NXOpen::Fields::ExternalFileProfileBuilder::InterpolationCubic@endlink </li>
                    </ul>
                     <br> 
                    This is only used when @link NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice@endlink 
                    is set to @link NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface@endlink 
                     <br> 
                      
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YOffset
    ##  Returns  @brief 
    ##             the offset on the y axis.  
    ##   
    ##              
    ## 
    ##  
    ##             
    ##              <br> 
    ##             Please make sure that the unit of the offset matches the unit defined in the header
    ##             of the @link NXOpen::Fields::ExternalFileProfileBuilder::YColumn NXOpen::Fields::ExternalFileProfileBuilder::YColumn@endlink 
    ##             in the file set in @link NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference@endlink .
    ##              <br> 
    ##              <br> 
    ##             This is only used when @link NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice@endlink 
    ##             is set to @link NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface@endlink .
    ##              <br> 
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def YOffset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YOffset
         Returns  @brief 
                    the offset on the y axis.  
          
                     
        
         
                    
                     <br> 
                    Please make sure that the unit of the offset matches the unit defined in the header
                    of the @link NXOpen::Fields::ExternalFileProfileBuilder::YColumn NXOpen::Fields::ExternalFileProfileBuilder::YColumn@endlink 
                    in the file set in @link NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference@endlink .
                     <br> 
                     <br> 
                    This is only used when @link NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice@endlink 
                    is set to @link NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface@endlink .
                     <br> 
                      
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YScale
    ##  Returns  @brief 
    ##             the scale on the y axis.  
    ##   
    ##              
    ## 
    ##  
    ##             The scale is unitless.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def YScale(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YScale
         Returns  @brief 
                    the scale on the y axis.  
          
                     
        
         
                    The scale is unitless.  
         
        """
        pass
    
    ##   @brief 
    ##             Returns the measure of the specified column.
    ##              
    ## 
    ##  
    ##             
    ##             This only works if the file set in @link NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference@endlink 
    ##             is set to a valid file. (Please refer to documentation for specific details on the file formats supported.)<br/>
    ##             If the file was not read already GetColumnMeasureName will read it.
    ##             
    ##  @return measureName (str):  measure name of the specified column .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="columnNumber"> (int)  column number, first column of
    ##             the file set in @link NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference@endlink 
    ##             corresponding to 1 </param>
    def GetColumnMeasureName(self, columnNumber: int) -> str:
        """
          @brief 
                    Returns the measure of the specified column.
                     
        
         
                    
                    This only works if the file set in @link NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference@endlink 
                    is set to a valid file. (Please refer to documentation for specific details on the file formats supported.)<br/>
                    If the file was not read already GetColumnMeasureName will read it.
                    
         @return measureName (str):  measure name of the specified column .
        """
        pass
    
    ##   @brief 
    ##             Returns the title of the specified column.
    ##              
    ## 
    ##  
    ##             
    ##              <br> 
    ##              The title contains the
    ##              <ul>
    ##               <li>column number(s) in file set in @link NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference@endlink  (starting with 1)</li>
    ##               <li>end column for the variable if applicable</li>
    ##               <li>column name and</li>
    ##               <li>localized unit string.</li>
    ##             </ul>
    ##             e.g. "1: X (unitless)" or "2(..4): Y (mm)"
    ##              <br> 
    ##              <br> 
    ##             This only works if file set in @link NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference@endlink 
    ##             is set to a valid file. (Please refer to documentation for specific details on the file formats supported.)<br/>
    ##             If the file was not read already GetColumnTitle will read it.
    ##              <br> 
    ##             
    ##  @return column_title (str):  title of the specified column .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="columnNumber"> (int)  column number, first column of
    ##             the file set in @link NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference@endlink 
    ##             corresponding to 1,<br/>
    ##             if several columns belong together to one variable all those columns will be considered as one common column </param>
    def GetColumnTitle(self, columnNumber: int) -> str:
        """
          @brief 
                    Returns the title of the specified column.
                     
        
         
                    
                     <br> 
                     The title contains the
                     <ul>
                      <li>column number(s) in file set in @link NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference@endlink  (starting with 1)</li>
                      <li>end column for the variable if applicable</li>
                      <li>column name and</li>
                      <li>localized unit string.</li>
                    </ul>
                    e.g. "1: X (unitless)" or "2(..4): Y (mm)"
                     <br> 
                     <br> 
                    This only works if file set in @link NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference@endlink 
                    is set to a valid file. (Please refer to documentation for specific details on the file formats supported.)<br/>
                    If the file was not read already GetColumnTitle will read it.
                     <br> 
                    
         @return column_title (str):  title of the specified column .
        """
        pass
    
    ##   @brief 
    ##             Returns the unit of the specified column.
    ##              
    ## 
    ##  
    ##             
    ##             This only works if the file set in @link NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference@endlink 
    ##             is set to a valid file. (Please refer to documentation for specific details on the file formats supported.)<br/>
    ##             If the file was not read already GetColumnUnit will read it.
    ##             
    ##  @return unit (@link NXOpen.Unit NXOpen.Unit@endlink):  unit of the specified column .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="columnNumber"> (int)  column number, first column of
    ##             the file set in @link NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference@endlink 
    ##             corresponding to 1 </param>
    def GetColumnUnit(self, columnNumber: int) -> NXOpen.Unit:
        """
          @brief 
                    Returns the unit of the specified column.
                     
        
         
                    
                    This only works if the file set in @link NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference@endlink 
                    is set to a valid file. (Please refer to documentation for specific details on the file formats supported.)<br/>
                    If the file was not read already GetColumnUnit will read it.
                    
         @return unit (@link NXOpen.Unit NXOpen.Unit@endlink):  unit of the specified column .
        """
        pass
    
    ##   @brief 
    ##             Gets the number of column titles.
    ##              
    ## 
    ##  
    ##             
    ##              <br> 
    ##             Depending on the format of the file set in @link NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference@endlink 
    ##             several columns in the file can belong together making up one common title.
    ##              <br> 
    ##              <br> 
    ##             This only works if @link NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference@endlink 
    ##             is set to a valid file. (Please refer to documentation for specific details on the file formats supported.)<br/>
    ##             If the file was not read already GetNumberOfColumns will read it.
    ##              <br> 
    ##             
    ##  @return numberColumns (int):  number of column titles .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def GetNumberOfColumns(self) -> int:
        """
          @brief 
                    Gets the number of column titles.
                     
        
         
                    
                     <br> 
                    Depending on the format of the file set in @link NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference@endlink 
                    several columns in the file can belong together making up one common title.
                     <br> 
                     <br> 
                    This only works if @link NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference@endlink 
                    is set to a valid file. (Please refer to documentation for specific details on the file formats supported.)<br/>
                    If the file was not read already GetNumberOfColumns will read it.
                     <br> 
                    
         @return numberColumns (int):  number of column titles .
        """
        pass
    
    ##   @brief 
    ##                 If the measures are marked as fixed and they are changed, the validation at commit will detect an error and fail.
    ##              
    ## 
    ##  
    ##             
    ##                 It is recommended to call this method when editing a profile that is referenced by another object,
    ##                 which depends on specific measures.
    ##             
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="areMeasuresFixed"> (bool)  true, if changed measures should prevent a commit </param>
    def SetMeasuresFixed(self, areMeasuresFixed: bool) -> None:
        """
          @brief 
                        If the measures are marked as fixed and they are changed, the validation at commit will detect an error and fail.
                     
        
         
                    
                        It is recommended to call this method when editing a profile that is referenced by another object,
                        which depends on specific measures.
                    
        """
        pass
    
import NXOpen
##  Represents a collection of Fields  <br> To obtain an instance of this class, refer to @link NXOpen::Fields::FieldManager  NXOpen::Fields::FieldManager @endlink  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class FieldCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Fields """
    pass


import NXOpen
##   @brief  Represents a Field Evaluator which can be used to evaluate a @link NXOpen::Fields::Field NXOpen::Fields::Field@endlink . 
##                         
##          
## 
##    <br> Use @link NXOpen::Fields::Field::GetFieldEvaluator NXOpen::Fields::Field::GetFieldEvaluator@endlink  to obtain an instance of this class  <br> 
## 
##   <br>  Created in NX7.5.2  <br> 

class FieldEvaluator(NXOpen.TaggedObject): 
    """ <summary> Represents a Field Evaluator which can be used to evaluate a <ja_class>NXOpen.Fields.Field</ja_class>. 
                        
        </summary> """


    ##  Options for Delaunay Sliver Detection 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Edgelengthratio</term><description> 
    ##  Default method if not specified, compares ratio of each edge length to the sum of the lengths of the other two sides </description> </item><item><term> 
    ## Aspectratio</term><description> 
    ##  Compares the height from the free edge to the opposite vertex to the length of the free edge </description> </item></list>
    class DelaunaySliverDetectionMethodEnum(Enum):
        """
        Members Include: <Edgelengthratio> <Aspectratio>
        """
        Edgelengthratio: int
        Aspectratio: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FieldEvaluator.DelaunaySliverDetectionMethodEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##   Interpolation type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ##  No interpolation method; table can only be used as a lookup </description> </item><item><term> 
    ## Linear1d</term><description> 
    ##  Standard linear interpolation between bounding points </description> </item><item><term> 
    ## NearestNeighbor1d</term><description> 
    ##  Locates the nearest point and returns its value </description> </item><item><term> 
    ## InverseDistanceWeighting1d</term><description> 
    ##  Sum of the weighted value of all points, based on the inverse of the distance </description> </item><item><term> 
    ## Delaunay2dFast</term><description> 
    ##  Triangulates the independent values and uses the bounding triangle, sacrifices accuracy for speed </description> </item><item><term> 
    ## Delaunay2dMedium</term><description> 
    ##  Triangulates the independent values and uses the bounding triangle, compromise between accuracy and speed </description> </item><item><term> 
    ## Delaunay2dAccurate</term><description> 
    ##  Triangulates the independent values and uses the bounding triangle, sacrifices speed for accuracy </description> </item><item><term> 
    ## NearestNeighbor2d</term><description> 
    ##  Locates the nearest point in a plane and returns its value </description> </item><item><term> 
    ## RenkaShepard2d</term><description> 
    ##  Refined inverse distance weighting in 2D space </description> </item><item><term> 
    ## InverseDistanceWeighting2d</term><description> 
    ##  Sum of the weighted value of all points in 2D space, based on the inverse of the distance </description> </item><item><term> 
    ## Delaunay3dFast</term><description> 
    ##  Creates Tetrahedrals using the independent values and uses the bounding tetrahedron, sacrifices accuracy for speed </description> </item><item><term> 
    ## Delaunay3dMedium</term><description> 
    ##  Creates Tetrahedrals using the independent values and uses the bounding tetrahedron, compromise between accuracy and speed </description> </item><item><term> 
    ## Delaunay3dAccurate</term><description> 
    ##  Creates Tetrahedrals using the independent values and uses the bounding tetrahedron, sacrifices speed for accuracy </description> </item><item><term> 
    ## NearestNeighbor3d</term><description> 
    ##  Locates the nearest point in space and returns its value </description> </item><item><term> 
    ## RenkaShepard3d</term><description> 
    ##  Refined inverse distance weighting in 3D space </description> </item><item><term> 
    ## InverseDistanceWeighting3d</term><description> 
    ##  Sum of the weighted value of all points in 3D space, based on the inverse of the distance </description> </item><item><term> 
    ## NearestNeighborNd</term><description> 
    ##  Locates the nearest point in N dimensional space and returns its value </description> </item><item><term> 
    ## RenkaShepardNd</term><description> 
    ##  Refined inverse distance weighting in N dimensional space </description> </item><item><term> 
    ## InverseDistanceWeightingNd</term><description> 
    ##  Sum of the weighted value of all points in N dimensional, based on the inverse of the distance </description> </item><item><term> 
    ## ApproxNearestNeighbor2d</term><description> 
    ##  Locates the approximate nearest point in a plane and returns its value </description> </item><item><term> 
    ## ApproxNearestNeighbor3d</term><description> 
    ##  Locates the approximate nearest point in space and returns its value </description> </item><item><term> 
    ## ApproxNearestNeighborNd</term><description> 
    ##  Locates the approximate nearest point in N dimensional space and returns its value </description> </item><item><term> 
    ## Akima1d</term><description> 
    ##  akima interpolation </description> </item><item><term> 
    ## Akima721d</term><description> 
    ##  akima72 interpolation </description> </item><item><term> 
    ## Cubic1d</term><description> 
    ##  cubic interpolation </description> </item><item><term> 
    ## Bilinear2d</term><description> 
    ##  linear interpolation in both directions </description> </item><item><term> 
    ## Biakima2d</term><description> 
    ##  akima interpolation in both directions </description> </item><item><term> 
    ## Biakima722d</term><description> 
    ##  akima72 interpolation in both directions </description> </item><item><term> 
    ## Bicubic2d</term><description> 
    ##  cubic interpolation in both directions </description> </item><item><term> 
    ## AkimaLinear2d</term><description> 
    ##  akima interpolation in x direction, linear in y direction </description> </item><item><term> 
    ## Akima72Linear2d</term><description> 
    ##  akima72 interpolation in x direction, linear in y direction </description> </item><item><term> 
    ## CubicLinear2d</term><description> 
    ##  cubic interpolation in x direction, linear in y direction </description> </item><item><term> 
    ## Conservative3d</term><description> 
    ##  conservative interpolation reserved for load mapping workflows </description> </item><item><term> 
    ## Lookupvalues1d</term><description> 
    ##  Lookup values interpolator for 1d integer based id table mapping workflows </description> </item><item><term> 
    ## Lookupvalues2d</term><description> 
    ##  Lookup values interpolator for 2d integer based id table mapping workflows </description> </item><item><term> 
    ## Lookupvalues3d</term><description> 
    ##  Lookup values interpolator for 3d integer based id table mapping workflows </description> </item><item><term> 
    ## LeastSquares1d</term><description> 
    ##  Weighted Least Squares Interpolation for 1d domain </description> </item><item><term> 
    ## LeastSquares2d</term><description> 
    ##  Weighted Least Squares Interpolation for 2d domain </description> </item><item><term> 
    ## LeastSquares3d</term><description> 
    ##  Weighted Least Squares Interpolation for 3d domain </description> </item><item><term> 
    ## Bspline1d</term><description> 
    ##  BSpline Interpolation for 1d domain </description> </item><item><term> 
    ## Bspline2d</term><description> 
    ##  BSpline Interpolation for 2d domain </description> </item><item><term> 
    ## Bspline3d</term><description> 
    ##  BSpline Interpolation for 3d domain </description> </item><item><term> 
    ## LinearLeastSquares1d</term><description> 
    ##  Linear Least Squares Interpolation for 1d domain </description> </item><item><term> 
    ## Spline1d</term><description> 
    ##  Spline Interpolation for 1d domain </description> </item></list>
    class InterpolationEnum(Enum):
        """
        Members Include: <NotSet> <Linear1d> <NearestNeighbor1d> <InverseDistanceWeighting1d> <Delaunay2dFast> <Delaunay2dMedium> <Delaunay2dAccurate> <NearestNeighbor2d> <RenkaShepard2d> <InverseDistanceWeighting2d> <Delaunay3dFast> <Delaunay3dMedium> <Delaunay3dAccurate> <NearestNeighbor3d> <RenkaShepard3d> <InverseDistanceWeighting3d> <NearestNeighborNd> <RenkaShepardNd> <InverseDistanceWeightingNd> <ApproxNearestNeighbor2d> <ApproxNearestNeighbor3d> <ApproxNearestNeighborNd> <Akima1d> <Akima721d> <Cubic1d> <Bilinear2d> <Biakima2d> <Biakima722d> <Bicubic2d> <AkimaLinear2d> <Akima72Linear2d> <CubicLinear2d> <Conservative3d> <Lookupvalues1d> <Lookupvalues2d> <Lookupvalues3d> <LeastSquares1d> <LeastSquares2d> <LeastSquares3d> <Bspline1d> <Bspline2d> <Bspline3d> <LinearLeastSquares1d> <Spline1d>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FieldEvaluator.InterpolationEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Options for IDW (inverse weighted distance) interpolator 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## All</term><description> 
    ##  Sum of the weighted value of all points, based on the inverse of the distance </description> </item><item><term> 
    ## Radius</term><description> 
    ##  Sum of the weighted value of points within a radius (as a fraction of the bounding box diagonal), based on the inverse of the distance </description> </item><item><term> 
    ## NearestPoints</term><description> 
    ##  Sum of the weighted value of N nearest points (as a fraction of the total number of points), based on the inverse of the distance </description> </item><item><term> 
    ## NumNearestPoints</term><description> 
    ##  Sum of the weighted value of N nearest points, based on the inverse of the distance[This option is not supported] </description> </item><item><term> 
    ## MaximumRadiusAndPoints</term><description> 
    ##  Sum of the weighted value of N nearest points and points within a radius, based on the inverse of the distance  </description> </item></list>
    class InverseDistanceWeightingEnum(Enum):
        """
        Members Include: <All> <Radius> <NearestPoints> <NumNearestPoints> <MaximumRadiusAndPoints>
        """
        All: int
        Radius: int
        NearestPoints: int
        NumNearestPoints: int
        MaximumRadiusAndPoints: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FieldEvaluator.InverseDistanceWeightingEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Options for IDW (inverse weighted distance) interpolator power of the distance 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## One</term><description> 
    ##  IDW algorithm will use the distance for its calculation </description> </item><item><term> 
    ## Two</term><description> 
    ##  IDW algorithm will use the squared distance for calculation </description> </item><item><term> 
    ## Three</term><description> 
    ##  IDW algorithm will use the cubed distance for calculation </description> </item></list>
    class InverseDistanceWeightingPowerOfDistanceEnum(Enum):
        """
        Members Include: <One> <Two> <Three>
        """
        One: int
        Two: int
        Three: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FieldEvaluator.InverseDistanceWeightingPowerOfDistanceEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Log Options for Linear interpolator 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## LinearLinear</term><description> 
    ##  Standard linear interpolation. Both Independent variable and Dependent variable scaling are linear </description> </item><item><term> 
    ## LogLinear</term><description> 
    ##  Independent variable scaling is logarithmic (ln), Dependent variable scaling is linear </description> </item><item><term> 
    ## LinearLog</term><description> 
    ##  Independent variable scaling is linear, Dependent variable scaling is logarithmic (ln) </description> </item><item><term> 
    ## LogLog</term><description> 
    ##  Both Independent variable and Dependent variable scaling are logarithmic (ln) </description> </item><item><term> 
    ## ScaleOffset</term><description> 
    ##  Scale/Offset enum selection option under linear interpolation scheme </description> </item></list>
    class LinearLogOptionEnum(Enum):
        """
        Members Include: <LinearLinear> <LogLinear> <LinearLog> <LogLog> <ScaleOffset>
        """
        LinearLinear: int
        LogLinear: int
        LinearLog: int
        LogLog: int
        ScaleOffset: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FieldEvaluator.LinearLogOptionEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Degree Options for Spline interpolator 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ThirdOrder</term><description> 
    ##  Spline interpolation using third degree polynomial </description> </item><item><term> 
    ## FifthOrder</term><description> 
    ##  Spline interpolation using fifth degree polynomial </description> </item></list>
    class SplineDegreeOptionEnum(Enum):
        """
        Members Include: <ThirdOrder> <FifthOrder>
        """
        ThirdOrder: int
        FifthOrder: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FieldEvaluator.SplineDegreeOptionEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Options for outside table values interpolation 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Undefined</term><description> 
    ##  No interpolation result </description> </item><item><term> 
    ## Extrapolate</term><description> 
    ##  Extrapolates from the boundary out into space using the same interpolation method that the interpolator for interior table values uses </description> </item><item><term> 
    ## Constant</term><description> 
    ##  Returns the boundary value as interpolation result </description> </item><item><term> 
    ## Linear</term><description> 
    ##  Extrapolates from the boundary out into space using the linear extrapolation method </description> </item><item><term> 
    ## Parabolic</term><description> 
    ##  Extrapolates from the boundary out into space using the parabolic extrapolation method </description> </item><item><term> 
    ## Cubic</term><description> 
    ##  Extrapolates from the boundary out into space using the cubic extrapolation method </description> </item><item><term> 
    ## Userdefined</term><description> 
    ##  Returns the user specified value as the interpolation result </description> </item></list>
    class ValuesOutsideTableInterpolationEnum(Enum):
        """
        Members Include: <Undefined> <Extrapolate> <Constant> <Linear> <Parabolic> <Cubic> <Userdefined>
        """
        Undefined: int
        Extrapolate: int
        Constant: int
        Linear: int
        Parabolic: int
        Cubic: int
        Userdefined: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FieldEvaluator.ValuesOutsideTableInterpolationEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link FieldEvaluator.InterpolationEnum NXOpen.Fields.FieldEvaluator.InterpolationEnum@endlink) InterpolationMethod
    ##  Returns  
    ##         the interpolation method used when this table data is evaluated.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.2  <br> 

    ## @return FieldEvaluator.InterpolationEnum
    @property
    def InterpolationMethod(self) -> FieldEvaluator.InterpolationEnum:
        """
        Getter for property: (@link FieldEvaluator.InterpolationEnum NXOpen.Fields.FieldEvaluator.InterpolationEnum@endlink) InterpolationMethod
         Returns  
                the interpolation method used when this table data is evaluated.  
          
                  
         
        """
        pass
    
    ## Setter for property: (@link FieldEvaluator.InterpolationEnum NXOpen.Fields.FieldEvaluator.InterpolationEnum@endlink) InterpolationMethod

    ##  Returns  
    ##         the interpolation method used when this table data is evaluated.  
    ##   
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.2  <br> 

    @InterpolationMethod.setter
    def InterpolationMethod(self, interpolation_method: FieldEvaluator.InterpolationEnum):
        """
        Setter for property: (@link FieldEvaluator.InterpolationEnum NXOpen.Fields.FieldEvaluator.InterpolationEnum@endlink) InterpolationMethod
         Returns  
                the interpolation method used when this table data is evaluated.  
          
                  
         
        """
        pass
    
    ##  Delete this field evaluator; destroys the field evaluator and removes all references to it.
    ##         
    ## 
    ##   <br>  Created in NX7.5.2  <br> 

    ## License requirements: None.
    def Delete(self) -> None:
        """
         Delete this field evaluator; destroys the field evaluator and removes all references to it.
                
        """
        pass
    
    ##  Evaluate the Field at the specified independent variable @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink  values and return the values for the specified dependent variable. 
    ##             The number of output values will be the same as number of independent variables specified and these values will be in the same units as the 
    ##             dependent variable @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink .   
    ##         
    ##  @return values (List[float]):  the values evaluated for this dependent variable .
    ## 
    ##   <br>  Created in NX7.5.2  <br> 

    ## License requirements: None.
    ## 
    ## <param name="dependent_variable"> (@link FieldVariable NXOpen.Fields.FieldVariable@endlink)  dependent variable whose values are to be evaluated </param>
    def Evaluate(self, dependent_variable: FieldVariable) -> List[float]:
        """
         Evaluate the Field at the specified independent variable @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink  values and return the values for the specified dependent variable. 
                    The number of output values will be the same as number of independent variables specified and these values will be in the same units as the 
                    dependent variable @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink .   
                
         @return values (List[float]):  the values evaluated for this dependent variable .
        """
        pass
    
    ##  Returns the dependent variables for this @link NXOpen::Fields::FieldEvaluator NXOpen::Fields::FieldEvaluator@endlink   
    ##         
    ##  @return dependent_variables (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink):  dependent variables for this @link NXOpen::Fields::FieldEvaluator NXOpen::Fields::FieldEvaluator@endlink   .
    ## 
    ##   <br>  Created in NX7.5.2  <br> 

    ## License requirements: None.
    def GetDependentVariables(self) -> List[FieldVariable]:
        """
         Returns the dependent variables for this @link NXOpen::Fields::FieldEvaluator NXOpen::Fields::FieldEvaluator@endlink   
                
         @return dependent_variables (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink):  dependent variables for this @link NXOpen::Fields::FieldEvaluator NXOpen::Fields::FieldEvaluator@endlink   .
        """
        pass
    
    ##  Returns the independent variables for this @link NXOpen::Fields::FieldEvaluator NXOpen::Fields::FieldEvaluator@endlink   
    ##         
    ##  @return independent_variables (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink):  independent variables for this @link NXOpen::Fields::FieldEvaluator NXOpen::Fields::FieldEvaluator@endlink   .
    ## 
    ##   <br>  Created in NX7.5.2  <br> 

    ## License requirements: None.
    def GetIndependentVariables(self) -> List[FieldVariable]:
        """
         Returns the independent variables for this @link NXOpen::Fields::FieldEvaluator NXOpen::Fields::FieldEvaluator@endlink   
                
         @return independent_variables (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink):  independent variables for this @link NXOpen::Fields::FieldEvaluator NXOpen::Fields::FieldEvaluator@endlink   .
        """
        pass
    
    ##  Sets values at which the Field will be evaluated for this independent variable @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink . 
    ##             The number of input values mush be the same for independent variables and these values are assumed to be in the same units as the 
    ##             independent variable @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink .   
    ##         
    ## 
    ##   <br>  Created in NX7.5.2  <br> 

    ## License requirements: None.
    ## 
    ## <param name="independent_variable"> (@link FieldVariable NXOpen.Fields.FieldVariable@endlink)  independent variable whose values are being set. </param>
    ## <param name="values"> (List[float])  the values for this independent variable where the field will be evaluated at. </param>
    def SetIndependentVariableValues(self, independent_variable: FieldVariable, values: List[float]) -> None:
        """
         Sets values at which the Field will be evaluated for this independent variable @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink . 
                    The number of input values mush be the same for independent variables and these values are assumed to be in the same units as the 
                    independent variable @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink .   
                
        """
        pass
    
import NXOpen
##   @brief  Represents the Field Expression class. 
## 
##  
##      <br> A field (see @link NXOpen::Fields::Field NXOpen::Fields::Field@endlink ) which has <b><tt>exactly one</tt></b> dependent
##     variable (see @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink ), where the field function defintions
##     is implemented using the NX Expression sub-system @link NXOpen::Expression NXOpen::Expression@endlink . <br>  
## 
##   <br>  Created in NX4.0.0  <br> 

class FieldExpression(Field): 
    """ <summary> Represents the Field Expression class.</summary>
    <para>A field (see <ja_class>NXOpen.Fields.Field</ja_class>) which has <b><tt>exactly one</tt></b> dependent
    variable (see <ja_class>NXOpen.Fields.FieldVariable</ja_class>), where the field function defintions
    is implemented using the NX Expression sub-system <ja_class>NXOpen.Expression</ja_class>.</para> """


    ##  This option specifies how sampling is handled when combining table fields via an expression or an unbounded formula.
    ##             It is not applicable for table fields which have the "Values outside Table" option set to anything other than Constant or Extrapolate, 
    ##             or when other field types are included in the expression. For those cases the Intersection setting will always be used.
    ##             
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Intersection</term><description> 
    ##  The Intersection option will yield only points (e.g.: time points) which are common among the tables. </description> </item><item><term> 
    ## Union</term><description> 
    ##  The Union option will include all points from all tables in the expression. </description> </item></list>
    class CombineTableOption(Enum):
        """
        Members Include: <Intersection> <Union>
        """
        Intersection: int
        Union: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FieldExpression.CombineTableOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link FieldExpression.CombineTableOption NXOpen.Fields.FieldExpression.CombineTableOption@endlink) CombineTable
    ##  Returns the table combine option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return FieldExpression.CombineTableOption
    @property
    def CombineTable(self) -> FieldExpression.CombineTableOption:
        """
        Getter for property: (@link FieldExpression.CombineTableOption NXOpen.Fields.FieldExpression.CombineTableOption@endlink) CombineTable
         Returns the table combine option   
            
         
        """
        pass
    
    ## Setter for property: (@link FieldExpression.CombineTableOption NXOpen.Fields.FieldExpression.CombineTableOption@endlink) CombineTable

    ##  Returns the table combine option   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @CombineTable.setter
    def CombineTable(self, tableOption: FieldExpression.CombineTableOption):
        """
        Setter for property: (@link FieldExpression.CombineTableOption NXOpen.Fields.FieldExpression.CombineTableOption@endlink) CombineTable
         Returns the table combine option   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) FieldExpressionUnits
    ##  Returns the units of the field expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Unit
    @property
    def FieldExpressionUnits(self) -> NXOpen.Unit:
        """
        Getter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) FieldExpressionUnits
         Returns the units of the field expression   
            
         
        """
        pass
    
    ##  Edit the expression field.  Specifies the new expression string and the array of variables used
    ##             in the expression string.  Field expressions are children of
    ##             @link NXOpen::Fields::FieldFormula NXOpen::Fields::FieldFormula@endlink .
    ##          
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="field_exp_string"> (str)  expression string to be associated with the field </param>
    ## <param name="unit_type"> (@link NXOpen.Unit NXOpen.Unit@endlink)  unit of the field </param>
    ## <param name="indep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  independent variables to be associated with the field </param>
    ## <param name="update_flag"> (bool)  update flag </param>
    def EditFieldExpression(self, field_exp_string: str, unit_type: NXOpen.Unit, indep_var_array: List[FieldVariable], update_flag: bool) -> None:
        """
         Edit the expression field.  Specifies the new expression string and the array of variables used
                    in the expression string.  Field expressions are children of
                    @link NXOpen::Fields::FieldFormula NXOpen::Fields::FieldFormula@endlink .
                 
        """
        pass
    
    ##  Gets the expression string of the expression field 
    ##  @return field_exp_string (str):  expression string associated with the field .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetFieldExpressionString(self) -> str:
        """
         Gets the expression string of the expression field 
         @return field_exp_string (str):  expression string associated with the field .
        """
        pass
    
    ##  Sets the new expression string to the expression field 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="field_exp_string"> (str)  expression string to be associated with the field </param>
    ## <param name="updateFlag"> (bool)  update flag </param>
    def SetFieldExpressionString(self, field_exp_string: str, updateFlag: bool) -> None:
        """
         Sets the new expression string to the expression field 
        """
        pass
    
import NXOpen
##   @brief  Provides methods for managing field folders @link NXOpen::Fields::FieldFolder NXOpen::Fields::FieldFolder@endlink   
## 
##    <br> To obtain an instance of this class, refer to @link NXOpen::Fields::FieldManager  NXOpen::Fields::FieldManager @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class FieldFolderCollection(NXOpen.TaggedObjectCollection): 
    """ <summary> Provides methods for managing field folders <ja_class>NXOpen.Fields.FieldFolder</ja_class> </summary> """


    ##  Creates a Field folder with given name, and optional makes it a subfolder if a parent folder is specified. 
    ##          
    ##  @return folder (@link FieldFolder NXOpen.Fields.FieldFolder@endlink):  the created @link NXOpen::Fields::FieldFolder NXOpen::Fields::FieldFolder@endlink  .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="name"> (str)  name of the folder to be created </param>
    ## <param name="parent"> (@link FieldFolder NXOpen.Fields.FieldFolder@endlink)  specify the parent folder @link NXOpen::Fields::FieldFolder NXOpen::Fields::FieldFolder@endlink ,or specify NULL if the folder is root folder.  </param>
    def CreateFolder(self, name: str, parent: FieldFolder) -> FieldFolder:
        """
         Creates a Field folder with given name, and optional makes it a subfolder if a parent folder is specified. 
                 
         @return folder (@link FieldFolder NXOpen.Fields.FieldFolder@endlink):  the created @link NXOpen::Fields::FieldFolder NXOpen::Fields::FieldFolder@endlink  .
        """
        pass
    
    ##  Finds the @link NXOpen::Fields::FieldFolder NXOpen::Fields::FieldFolder@endlink  with the given identifier as recorded in a journal.
    ##         An exception will be thrown if no object can be found with the given journal identifier. 
    ##  @return found (@link FieldFolder NXOpen.Fields.FieldFolder@endlink):  field folder found .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="journalIdentifier"> (str)  Identifier to be found </param>
    def FindObject(self, journalIdentifier: str) -> FieldFolder:
        """
         Finds the @link NXOpen::Fields::FieldFolder NXOpen::Fields::FieldFolder@endlink  with the given identifier as recorded in a journal.
                An exception will be thrown if no object can be found with the given journal identifier. 
         @return found (@link FieldFolder NXOpen.Fields.FieldFolder@endlink):  field folder found .
        """
        pass
    
import NXOpen
import NXOpen.CAE
##   @brief  Represents a folder object in the fields   
## 
##    <br> To create a new instance of this class, use @link NXOpen::Fields::FieldFolderCollection::CreateFolder  NXOpen::Fields::FieldFolderCollection::CreateFolder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class FieldFolder(NXOpen.NXObject): 
    """ <summary> Represents a folder object in the fields  </summary> """


    ## Getter for property: (@link FieldFolder NXOpen.Fields.FieldFolder@endlink) Parent
    ##  Returns the parent folder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return FieldFolder
    @property
    def Parent(self) -> FieldFolder:
        """
        Getter for property: (@link FieldFolder NXOpen.Fields.FieldFolder@endlink) Parent
         Returns the parent folder   
            
         
        """
        pass
    
    ##   Add a child folder 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="field"> (@link Field NXOpen.Fields.Field@endlink)  child object</param>
    def AddField(self, field: Field) -> None:
        """
          Add a child folder 
        """
        pass
    
    ##   Add a child folder 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="subfolder"> (@link FieldFolder NXOpen.Fields.FieldFolder@endlink)  child folder</param>
    def AddSubfolder(self, subfolder: FieldFolder) -> None:
        """
          Add a child folder 
        """
        pass
    
    ##   Remove a child folder 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="field"> (@link Field NXOpen.Fields.Field@endlink)  child object</param>
    def RemoveField(self, field: Field) -> None:
        """
          Remove a child folder 
        """
        pass
    
    ##   Remove a child folder 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="subfolder"> (@link FieldFolder NXOpen.Fields.FieldFolder@endlink)  child folder</param>
    def RemoveSubfolder(self, subfolder: FieldFolder) -> None:
        """
          Remove a child folder 
        """
        pass
    
##   @brief  Represents the Field Formula class. 
## 
##  
##      <br> A field (see @link NXOpen::Fields::Field NXOpen::Fields::Field@endlink ) which has <b><tt>n</tt></b> number of dependent
##     variables, where each dependent variable (see @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink ) is implemented using the NX Expression sub-system.
##     In practical terms, a field formula is implemented using n number of field expressions
##     @link NXOpen::Fields::FieldExpression NXOpen::Fields::FieldExpression@endlink . <br>  
## 
##   <br>  Created in NX6.0.0  <br> 

class FieldFormula(Field): 
    """ <summary> Represents the Field Formula class.</summary>
    <para>A field (see <ja_class>NXOpen.Fields.Field</ja_class>) which has <b><tt>n</tt></b> number of dependent
    variables, where each dependent variable (see <ja_class>NXOpen.Fields.FieldVariable</ja_class>) is implemented using the NX Expression sub-system.
    In practical terms, a field formula is implemented using n number of field expressions
    <ja_class>NXOpen.Fields.FieldExpression</ja_class>.</para> """


    ## Getter for property: (@link FieldExpression.CombineTableOption NXOpen.Fields.FieldExpression.CombineTableOption@endlink) CombineTable
    ##  Returns the table combine option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return FieldExpression.CombineTableOption
    @property
    def CombineTable(self) -> FieldExpression.CombineTableOption:
        """
        Getter for property: (@link FieldExpression.CombineTableOption NXOpen.Fields.FieldExpression.CombineTableOption@endlink) CombineTable
         Returns the table combine option   
            
         
        """
        pass
    
    ## Setter for property: (@link FieldExpression.CombineTableOption NXOpen.Fields.FieldExpression.CombineTableOption@endlink) CombineTable

    ##  Returns the table combine option   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @CombineTable.setter
    def CombineTable(self, tableOption: FieldExpression.CombineTableOption):
        """
        Setter for property: (@link FieldExpression.CombineTableOption NXOpen.Fields.FieldExpression.CombineTableOption@endlink) CombineTable
         Returns the table combine option   
            
         
        """
        pass
    
    ##  Edit the formula field.  Specifies the new expression @link NXOpen::Fields::FieldExpression NXOpen::Fields::FieldExpression@endlink 
    ##             array and the array of @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink s used.
    ##         
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="indep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  independent variables to be associated with the field </param>
    ## <param name="dep_exp_array"> (@link FieldExpression List[NXOpen.Fields.FieldExpression]@endlink)  dependent field expressions to be associated with the field </param>
    def EditFieldFormula(self, indep_var_array: List[FieldVariable], dep_exp_array: List[FieldExpression]) -> None:
        """
         Edit the formula field.  Specifies the new expression @link NXOpen::Fields::FieldExpression NXOpen::Fields::FieldExpression@endlink 
                    array and the array of @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink s used.
                
        """
        pass
    
    ##  Edit the formula field variables.  Specifies the new dependent and independent @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink 
    ##         arrays.  The formula will be updated to reflect the changes (if any) to the variables.  If the dependent variables are changed, the expressions will be changed 
    ##         to 0 if the new variable measure is incompatible with the old variable measure.  If the independent variables change, the expression will be changed
    ##         to 0 if it contains any of the deleted variables.
    ##         
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="indep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  new independent variables to be associated with the field </param>
    ## <param name="dep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  new dependent field variables to be associated with the field </param>
    def EditFieldFormulaVariables(self, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable]) -> None:
        """
         Edit the formula field variables.  Specifies the new dependent and independent @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink 
                arrays.  The formula will be updated to reflect the changes (if any) to the variables.  If the dependent variables are changed, the expressions will be changed 
                to 0 if the new variable measure is incompatible with the old variable measure.  If the independent variables change, the expression will be changed
                to 0 if it contains any of the deleted variables.
                
        """
        pass
    
    ##  Returns the dependent field expressions associated with this formula 
    ##         
    ##  @return dependent_expressions (@link FieldExpression List[NXOpen.Fields.FieldExpression]@endlink):  dependent expressions  .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetDependentExpressions(self) -> List[FieldExpression]:
        """
         Returns the dependent field expressions associated with this formula 
                
         @return dependent_expressions (@link FieldExpression List[NXOpen.Fields.FieldExpression]@endlink):  dependent expressions  .
        """
        pass
    
import NXOpen
##   @brief  Represents the Field LinksTable class. 
## 
##   
##      <br> A field (see @link NXOpen::Fields::Field NXOpen::Fields::Field@endlink ) defined in terms of tabular data involving 
##     one look-up independent column, an equal number of look-up fields and one or more 
##     dependent variables (see @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink ).  This is similar to a table
##     (see @link NXOpen::Fields::FieldTable NXOpen::Fields::FieldTable@endlink ), except instead of the interpolation dependent 
##     values being defined as numerical contants, they are defined by another field. <br>   <br> To obtain a instance of this class use @link NXOpen::Fields::FieldManager NXOpen::Fields::FieldManager@endlink  .  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class FieldLinksTable(Field): 
    """ <summary> Represents the Field LinksTable class.</summary> 
    <para>A field (see <ja_class>NXOpen.Fields.Field</ja_class>) defined in terms of tabular data involving 
    one look-up independent column, an equal number of look-up fields and one or more 
    dependent variables (see <ja_class>NXOpen.Fields.FieldVariable</ja_class>).  This is similar to a table
    (see <ja_class>NXOpen.Fields.FieldTable</ja_class>), except instead of the interpolation dependent 
    values being defined as numerical contants, they are defined by another field.</para> """


    ## Getter for property: (bool) Discontinuities
    ##  Returns a flag specifying if the table has discontinuites   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def Discontinuities(self) -> bool:
        """
        Getter for property: (bool) Discontinuities
         Returns a flag specifying if the table has discontinuites   
            
         
        """
        pass
    
    ## Getter for property: (@link FieldEvaluator.ValuesOutsideTableInterpolationEnum NXOpen.Fields.FieldEvaluator.ValuesOutsideTableInterpolationEnum@endlink) ValuesOutsideTableInterpolation
    ##  Returns the outside table values interpolation method for linear interpolation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return FieldEvaluator.ValuesOutsideTableInterpolationEnum
    @property
    def ValuesOutsideTableInterpolation(self) -> FieldEvaluator.ValuesOutsideTableInterpolationEnum:
        """
        Getter for property: (@link FieldEvaluator.ValuesOutsideTableInterpolationEnum NXOpen.Fields.FieldEvaluator.ValuesOutsideTableInterpolationEnum@endlink) ValuesOutsideTableInterpolation
         Returns the outside table values interpolation method for linear interpolation   
            
         
        """
        pass
    
    ## Setter for property: (@link FieldEvaluator.ValuesOutsideTableInterpolationEnum NXOpen.Fields.FieldEvaluator.ValuesOutsideTableInterpolationEnum@endlink) ValuesOutsideTableInterpolation

    ##  Returns the outside table values interpolation method for linear interpolation   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ValuesOutsideTableInterpolation.setter
    def ValuesOutsideTableInterpolation(self, interpolationMethod: FieldEvaluator.ValuesOutsideTableInterpolationEnum):
        """
        Setter for property: (@link FieldEvaluator.ValuesOutsideTableInterpolationEnum NXOpen.Fields.FieldEvaluator.ValuesOutsideTableInterpolationEnum@endlink) ValuesOutsideTableInterpolation
         Returns the outside table values interpolation method for linear interpolation   
            
         
        """
        pass
    
    ##  Edit the LinksTable field.  Specifies the new array of @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink s 
    ##         for independent and dependent variables, as well as the new double values and linked fields.
    ##         The datapoints and linked fields arrays are row based and number of each must equal the 
    ##         num_rows. The data_points array represents the values for the first independent value.  For example, if 
    ##         the LinksTable has a domain of txyz, the values in this array are all values of t.
    ##         The linked fields array must consist of the fields with independent variables representing the 
    ##         remaining variables in the independent domain of the LinksTable.  For example, if the LinksTable has 
    ##         a domain of txyz, the independent domain of the fields in this array are all xyz.  NULL values are  allowed for 
    ##         linked fields and indicate a discontinuity at the associated value of the first independent  variable.
    ##         The dependent quantities are determined from the linked fields.  The linked fields must have the same 
    ##         dependent variables as the Linkstable.
    ##         
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ## <param name="field_links_table"> (@link FieldLinksTable NXOpen.Fields.FieldLinksTable@endlink) </param>
    ## <param name="indep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  independent variables to be associated with the field </param>
    ## <param name="dep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  dependent variables of this and all linked fields </param>
    ## <param name="datapoints"> (List[float])  row based array of double values representing the first independent variable; the number of points should equal the number of rows. </param>
    ## <param name="link_fields_array"> (@link Field List[NXOpen.Fields.Field]@endlink)  row based array of link field values representing the table; the number of fields should equal the number of rows.</param>
    @overload
    def EditFieldLinksTable(self, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable], datapoints: List[float], link_fields_array: List[Field]) -> None:
        """
         Edit the LinksTable field.  Specifies the new array of @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink s 
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
    
    ##  Edit the LinksTable field.  Specifies the new array of @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink s
    ##        for independent and dependent variables, as well as the new double values and linked fields.
    ##        The datapoints and linked fields arrays are row based and number of each must equal the
    ##        num_rows. The data_points array represents the values for the first independent value.  For example, if
    ##        the LinksTable has a domain of txyz, the values in this array are all values of t.
    ##        The linked fields array must consist of the fields with independent variables representing the
    ##        remaining variables in the independent domain of the LinksTable.  For example, if the LinksTable has
    ##        a domain of txyz, the independent domain of the fields in this array are all xyz.  NULL values are  allowed for
    ##        linked fields and indicate a discontinuity at the associated value of the first independent  variable.
    ##        The dependent quantities are determined from the linked fields.  The linked fields must have the same
    ##        dependent variables as the Linkstable.
    ##        
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="indep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  independent variables to be associated with the field </param>
    ## <param name="dep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  dependent variables of this and all linked fields </param>
    ## <param name="datapoints"> (List[float])  num_points = rows * (1 + numDepVars) </param>
    ## <param name="link_fields_array"> (@link Field List[NXOpen.Fields.Field]@endlink)  row based array of link field values representing the table; the number of fields should equal the number of rows.</param>
    ## <param name="managed_fields_array"> (List[bool])  row based array of logical values indicating the links table field should manage the specified fields .</param>
    def EditFieldLinksTableWithConstants(self, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable], datapoints: List[float], link_fields_array: List[Field], managed_fields_array: List[bool]) -> None:
        """
         Edit the LinksTable field.  Specifies the new array of @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink s
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
    
    ##  Edit the LinksTable field.  Specifies the new array of @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink s 
    ##         for independent and dependent variables, as well as the new double values and linked fields.
    ##         The datapoints, linked fields, and the managed fields arrays are row based and number of each must equal the 
    ##         num_rows. The data_points array represents the values for the first independent value.  For example, if 
    ##         the LinksTable has a domain of txyz, the values in this array are all values of t.
    ##         The linked fields array must consist of the fields with independent variables representing the 
    ##         remaining variables in the independent domain of the LinksTable.  For example, if the LinksTable has 
    ##         a domain of txyz, the independent domain of the fields in this array are all xyz.  NULL values are  allowed for 
    ##         linked fields and indicate a discontinuity at the associated value of the first independent  variable.
    ##         The dependent quantities are determined from the linked fields.  The linked fields must have the same 
    ##         dependent variables as the Linkstable. The managed fields array identifies the fields that should be managed by the links table.
    ##         
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ## <param name="field_links_table"> (@link FieldLinksTable NXOpen.Fields.FieldLinksTable@endlink) </param>
    ## <param name="indep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  independent variables to be associated with the field </param>
    ## <param name="dep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  dependent variables of this and all linked fields </param>
    ## <param name="datapoints"> (List[float])  row based array of double values representing the first independent variable; the number of points should equal the number of rows. </param>
    ## <param name="link_fields_array"> (@link Field List[NXOpen.Fields.Field]@endlink)  row based array of link field values representing the table; the number of fields should equal the number of rows.</param>
    ## <param name="managed_fields_array"> (List[bool])  row based array of logical values indicating the links table field should manage the specified fields .</param>
    @overload
    def EditFieldLinksTable(self, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable], datapoints: List[float], link_fields_array: List[Field], managed_fields_array: List[bool]) -> None:
        """
         Edit the LinksTable field.  Specifies the new array of @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink s 
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
    
    ##  Get the offset value for the primary independent variable 
    ##  @return offset (@link NXOpen.Expression NXOpen.Expression@endlink):  the offset for the primary independent variable .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    def GetPrimaryIndependentVariableOffset(self) -> NXOpen.Expression:
        """
         Get the offset value for the primary independent variable 
         @return offset (@link NXOpen.Expression NXOpen.Expression@endlink):  the offset for the primary independent variable .
        """
        pass
    
    ##  Get the scale factor for the primary independent variable 
    ##  @return scaleFactor (@link NXOpen.Expression NXOpen.Expression@endlink):  the scale factor for the primary independent variable .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    def GetPrimaryIndependentVariableScaleFactor(self) -> NXOpen.Expression:
        """
         Get the scale factor for the primary independent variable 
         @return scaleFactor (@link NXOpen.Expression NXOpen.Expression@endlink):  the scale factor for the primary independent variable .
        """
        pass
    
    ##  Set the offset value for the primary independent variable 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="offset"> (@link NXOpen.Expression NXOpen.Expression@endlink)  the offset for the primary independent variable </param>
    def SetPrimaryIndependentVariableOffset(self, offset: NXOpen.Expression) -> None:
        """
         Set the offset value for the primary independent variable 
        """
        pass
    
    ##  Set the scale factor for the primary independent variable 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="scaleFactor"> (@link NXOpen.Expression NXOpen.Expression@endlink)  the scale factor for the primary independent variable </param>
    def SetPrimaryIndependentVariableScaleFactor(self, scaleFactor: NXOpen.Expression) -> None:
        """
         Set the scale factor for the primary independent variable 
        """
        pass
    
    ##  Set the values outside table interpolation option for sub fields if the sub fields are tables  
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="interpolationMethod"> (@link FieldEvaluator.ValuesOutsideTableInterpolationEnum NXOpen.Fields.FieldEvaluator.ValuesOutsideTableInterpolationEnum@endlink)  the outside table values interpolation method for sub fields</param>
    def SetSecondaryValuesOutsideTableInterpolation(self, interpolationMethod: FieldEvaluator.ValuesOutsideTableInterpolationEnum) -> None:
        """
         Set the values outside table interpolation option for sub fields if the sub fields are tables  
        """
        pass
    
##   @brief  Represents the Field Link class. 
## 
##  
##      <br> A field (see @link Fields::Field Fields::Field@endlink ) which is implemented by another user
##     created field of any type.  This provides the ability to override that field's map with a 
##     localized map. <br>  
## 
##   <br>  Created in NX6.0.0  <br> 

class FieldLink(Field): 
    """ <summary> Represents the Field Link class.</summary>
    <para>A field (see <ja_class>Fields.Field</ja_class>) which is implemented by another user
    created field of any type.  This provides the ability to override that field's map with a 
    localized map.</para> """


    ##  Edit the link field.  Specifies the new @link Fields::Field Fields::Field@endlink 
    ##             to link to.
    ##         
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="fieldToLink"> (@link Field NXOpen.Fields.Field@endlink)  field to link </param>
    def EditFieldLink(self, fieldToLink: Field) -> None:
        """
         Edit the link field.  Specifies the new @link Fields::Field Fields::Field@endlink 
                    to link to.
                
        """
        pass
    
import NXOpen
##   @brief  Represents the manager class of the Fields  
## 
##   
##      <br> This manager class gives access to all the fields @link NXOpen::Fields::Field NXOpen::Fields::Field@endlink  within a part. <br> 
##      <br> It also provides creation methods for the various builders of fields and related classes. <br> 
##     
## 
##   <br>  Created in NX4.0.0  <br> 

class FieldManager(NXOpen.NXObject): 
    """ <summary> Represents the manager class of the Fields </summary> 
    <para>This manager class gives access to all the fields <ja_class>NXOpen.Fields.Field</ja_class> within a part.</para>
    <para>It also provides creation methods for the various builders of fields and related classes.</para>
    """


    ##  Returns a collection of Fields 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @link FieldCollection NXOpen.Fields.FieldCollection@endlink
    @property
    def Fields() -> FieldCollection:
        """
         Returns a collection of Fields 
        """
        pass
    
    ##  Returns the field folder collection 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @link FieldFolderCollection NXOpen.Fields.FieldFolderCollection@endlink
    @property
    def FieldFolders() -> FieldFolderCollection:
        """
         Returns the field folder collection 
        """
        pass
    
    ##   
    ##         Creates and returns a @link NXOpen::Fields::FieldLinksTable NXOpen::Fields::FieldLinksTable@endlink  representation of this table. Deletes the input table and updates all references to point to the links table.
    ##         
    ##  @return linksTable (@link FieldLinksTable NXOpen.Fields.FieldLinksTable@endlink):  table of fields .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="table"> (@link FieldTable NXOpen.Fields.FieldTable@endlink)  Table to be converted </param>
    def ConvertToLinksTable(self, table: FieldTable) -> FieldLinksTable:
        """
          
                Creates and returns a @link NXOpen::Fields::FieldLinksTable NXOpen::Fields::FieldLinksTable@endlink  representation of this table. Deletes the input table and updates all references to point to the links table.
                
         @return linksTable (@link FieldLinksTable NXOpen.Fields.FieldLinksTable@endlink):  table of fields .
        """
        pass
    
    ##  Create a complex scalar field wrapper backed by two scalar expressions 
    ##  @return complexScalarFieldWrapper (@link ComplexScalarFieldWrapper NXOpen.Fields.ComplexScalarFieldWrapper@endlink):  scalar field wrapper created and associated to the expression .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="expressions"> (@link NXOpen.Expression List[NXOpen.Expression]@endlink)  existing expressions that will be this wrapper's value </param>
    def CreateComplexScalarFieldWrapperWithExpressions(self, expressions: List[NXOpen.Expression]) -> ComplexScalarFieldWrapper:
        """
         Create a complex scalar field wrapper backed by two scalar expressions 
         @return complexScalarFieldWrapper (@link ComplexScalarFieldWrapper NXOpen.Fields.ComplexScalarFieldWrapper@endlink):  scalar field wrapper created and associated to the expression .
        """
        pass
    
    ##  Create a complex scalar field wrapper backed up by a complex scalar field 
    ##  @return complexScalarFieldWrapper (@link ComplexScalarFieldWrapper NXOpen.Fields.ComplexScalarFieldWrapper@endlink):  vector field wrapper created and associated to the field .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="field"> (@link Field NXOpen.Fields.Field@endlink)  an existing field that will be this wrapper's value </param>
    def CreateComplexScalarFieldWrapperWithField(self, field: Field) -> ComplexScalarFieldWrapper:
        """
         Create a complex scalar field wrapper backed up by a complex scalar field 
         @return complexScalarFieldWrapper (@link ComplexScalarFieldWrapper NXOpen.Fields.ComplexScalarFieldWrapper@endlink):  vector field wrapper created and associated to the field .
        """
        pass
    
    ##  Create a complex scalar field wrapper backed up by a complex scalar field with scale factor 
    ##  @return complexScalarFieldWrapper (@link ComplexScalarFieldWrapper NXOpen.Fields.ComplexScalarFieldWrapper@endlink):  scalar field wrapper created and associated to the field .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="field"> (@link Field NXOpen.Fields.Field@endlink)  an existing field that will be this wrapper's value </param>
    ## <param name="scaleFactor"> (float)  the field will be multiplied by this scale factor when being evaluated </param>
    def CreateComplexScalarFieldWrapperWithFieldWithScaleFactor(self, field: Field, scaleFactor: float) -> ComplexScalarFieldWrapper:
        """
         Create a complex scalar field wrapper backed up by a complex scalar field with scale factor 
         @return complexScalarFieldWrapper (@link ComplexScalarFieldWrapper NXOpen.Fields.ComplexScalarFieldWrapper@endlink):  scalar field wrapper created and associated to the field .
        """
        pass
    
    ##  Create a complex scalar field wrapper backed by two scalar magnitude/phase expressions 
    ##  @return complexScalarFieldWrapper (@link ComplexScalarFieldWrapper NXOpen.Fields.ComplexScalarFieldWrapper@endlink):  scalar field wrapper created and associated to the expression .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="expressions"> (@link NXOpen.Expression List[NXOpen.Expression]@endlink)  existing expressions that will be this wrapper's value </param>
    def CreateComplexScalarFieldWrapperWithMagnitudePhaseExpressions(self, expressions: List[NXOpen.Expression]) -> ComplexScalarFieldWrapper:
        """
         Create a complex scalar field wrapper backed by two scalar magnitude/phase expressions 
         @return complexScalarFieldWrapper (@link ComplexScalarFieldWrapper NXOpen.Fields.ComplexScalarFieldWrapper@endlink):  scalar field wrapper created and associated to the expression .
        """
        pass
    
    ##  Create a complex scalar field wrapper backed by two scalar real/imaginary expressions 
    ##  @return complexScalarFieldWrapper (@link ComplexScalarFieldWrapper NXOpen.Fields.ComplexScalarFieldWrapper@endlink):  scalar field wrapper created and associated to the expression .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="expressions"> (@link NXOpen.Expression List[NXOpen.Expression]@endlink)  existing expressions that will be this wrapper's value </param>
    def CreateComplexScalarFieldWrapperWithRealImaginaryExpressions(self, expressions: List[NXOpen.Expression]) -> ComplexScalarFieldWrapper:
        """
         Create a complex scalar field wrapper backed by two scalar real/imaginary expressions 
         @return complexScalarFieldWrapper (@link ComplexScalarFieldWrapper NXOpen.Fields.ComplexScalarFieldWrapper@endlink):  scalar field wrapper created and associated to the expression .
        """
        pass
    
    ##  Create a complex vector field wrapper backed by six scalar expressions 
    ##  @return complexVectorFieldWrapper (@link ComplexVectorFieldWrapper NXOpen.Fields.ComplexVectorFieldWrapper@endlink):  scalar field wrapper created and associated to the expression .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="expressions"> (@link NXOpen.Expression List[NXOpen.Expression]@endlink)  existing expressions that will be this wrapper's value </param>
    def CreateComplexVectorFieldWrapperWithExpressions(self, expressions: List[NXOpen.Expression]) -> ComplexVectorFieldWrapper:
        """
         Create a complex vector field wrapper backed by six scalar expressions 
         @return complexVectorFieldWrapper (@link ComplexVectorFieldWrapper NXOpen.Fields.ComplexVectorFieldWrapper@endlink):  scalar field wrapper created and associated to the expression .
        """
        pass
    
    ##  Create a complex vector field wrapper backed up by a complex vector field 
    ##  @return complexVectorFieldWrapper (@link ComplexVectorFieldWrapper NXOpen.Fields.ComplexVectorFieldWrapper@endlink):  vector field wrapper created and associated to the field .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="field"> (@link Field NXOpen.Fields.Field@endlink)  an existing field that will be this wrapper's value </param>
    ## <param name="scaleFactor"> (float)  the field will be multiplied by this scale factor when being evaluated </param>
    def CreateComplexVectorFieldWrapperWithField(self, field: Field, scaleFactor: float) -> ComplexVectorFieldWrapper:
        """
         Create a complex vector field wrapper backed up by a complex vector field 
         @return complexVectorFieldWrapper (@link ComplexVectorFieldWrapper NXOpen.Fields.ComplexVectorFieldWrapper@endlink):  vector field wrapper created and associated to the field .
        """
        pass
    
    ##  Create a dependent variable to be added to the field 
    ##          
    ##  @return dep_var (@link FieldVariable NXOpen.Fields.FieldVariable@endlink):  dependent variable created and associated to the field .
    ## 
    ##   <br>  Created in NX6.0.2  <br> 

    ## License requirements: None.
    ## <param name="field_manager"> (@link FieldManager NXOpen.Fields.FieldManager@endlink) </param>
    ## <param name="owner_field"> (@link Field NXOpen.Fields.Field@endlink)  owner field </param>
    ## <param name="name_variable"> (@link NameVariable NXOpen.Fields.NameVariable@endlink)  existing name variable </param>
    ## <param name="unit_type"> (@link NXOpen.Unit NXOpen.Unit@endlink)  unit of the dependent variable </param>
    @overload
    def CreateDependentVariable(self, owner_field: Field, name_variable: NameVariable, unit_type: NXOpen.Unit) -> FieldVariable:
        """
         Create a dependent variable to be added to the field 
                 
         @return dep_var (@link FieldVariable NXOpen.Fields.FieldVariable@endlink):  dependent variable created and associated to the field .
        """
        pass
    
    ##  Create a dependent variable to be added to the field, specifying the variable value type 
    ##          
    ##  @return dep_var (@link FieldVariable NXOpen.Fields.FieldVariable@endlink):  dependent variable created and associated to the field .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## <param name="field_manager"> (@link FieldManager NXOpen.Fields.FieldManager@endlink) </param>
    ## <param name="owner_field"> (@link Field NXOpen.Fields.Field@endlink)  owner field </param>
    ## <param name="name_variable"> (@link NameVariable NXOpen.Fields.NameVariable@endlink)  existing name variable </param>
    ## <param name="unit_type"> (@link NXOpen.Unit NXOpen.Unit@endlink)  unit of the dependent variable </param>
    ## <param name="type"> (@link FieldVariable.ValueType NXOpen.Fields.FieldVariable.ValueType@endlink)  variable value type </param>
    @overload
    def CreateDependentVariable(self, owner_field: Field, name_variable: NameVariable, unit_type: NXOpen.Unit, type: FieldVariable.ValueType) -> FieldVariable:
        """
         Create a dependent variable to be added to the field, specifying the variable value type 
                 
         @return dep_var (@link FieldVariable NXOpen.Fields.FieldVariable@endlink):  dependent variable created and associated to the field .
        """
        pass
    
    ##  Creates a @link NXOpen::Fields::DisplayPropertiesBuilder NXOpen::Fields::DisplayPropertiesBuilder@endlink  
    ##  @return builder (@link DisplayPropertiesBuilder NXOpen.Fields.DisplayPropertiesBuilder@endlink): .
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="field_array"> (@link Field List[NXOpen.Fields.Field]@endlink)  fields to edit display properties </param>
    def CreateDisplayPropertiesBuilder(self, field_array: List[Field]) -> DisplayPropertiesBuilder:
        """
         Creates a @link NXOpen::Fields::DisplayPropertiesBuilder NXOpen::Fields::DisplayPropertiesBuilder@endlink  
         @return builder (@link DisplayPropertiesBuilder NXOpen.Fields.DisplayPropertiesBuilder@endlink): .
        """
        pass
    
    ##  Creates a Fields.ExportData 
    ##  @return export_data (@link ExportData NXOpen.Fields.ExportData@endlink):  the export data created .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def CreateExportData(self) -> ExportData:
        """
         Creates a Fields.ExportData 
         @return export_data (@link ExportData NXOpen.Fields.ExportData@endlink):  the export data created .
        """
        pass
    
    ##  Creates a system @link NXOpen::Fields::FieldExpression NXOpen::Fields::FieldExpression@endlink  object.  Specifies the new expression 
    ##             string.
    ##          
    ##  @return field_expression (@link FieldExpression NXOpen.Fields.FieldExpression@endlink):  field .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="field_exp_string"> (str)  expression string to be associated with the field </param>
    ## <param name="unit_type"> (@link NXOpen.Unit NXOpen.Unit@endlink)  unit of the field </param>
    def CreateFieldExpression(self, field_exp_string: str, unit_type: NXOpen.Unit) -> FieldExpression:
        """
         Creates a system @link NXOpen::Fields::FieldExpression NXOpen::Fields::FieldExpression@endlink  object.  Specifies the new expression 
                    string.
                 
         @return field_expression (@link FieldExpression NXOpen.Fields.FieldExpression@endlink):  field .
        """
        pass
    
    ##  Creates a @link NXOpen::Fields::FieldFormula NXOpen::Fields::FieldFormula@endlink  object with dependent @link NXOpen::Fields::FieldExpression NXOpen::Fields::FieldExpression@endlink .
    ##          
    ##  @return field_formula (@link FieldFormula NXOpen.Fields.FieldFormula@endlink):  field .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="field_name"> (str)  field name </param>
    ## <param name="indep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  independent variables to be associated with the field </param>
    ## <param name="dep_exp_array"> (@link FieldExpression List[NXOpen.Fields.FieldExpression]@endlink)  dependent expression fields to be associated with the formula field </param>
    def CreateFieldFormula(self, field_name: str, indep_var_array: List[FieldVariable], dep_exp_array: List[FieldExpression]) -> FieldFormula:
        """
         Creates a @link NXOpen::Fields::FieldFormula NXOpen::Fields::FieldFormula@endlink  object with dependent @link NXOpen::Fields::FieldExpression NXOpen::Fields::FieldExpression@endlink .
                 
         @return field_formula (@link FieldFormula NXOpen.Fields.FieldFormula@endlink):  field .
        """
        pass
    
    ##  Creates a @link NXOpen::Fields::FieldLink NXOpen::Fields::FieldLink@endlink .
    ##          
    ##  @return field_link (@link FieldLink NXOpen.Fields.FieldLink@endlink):  field .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="field_name"> (str)  field name </param>
    ## <param name="field_to_link"> (@link Field NXOpen.Fields.Field@endlink)  field to link </param>
    def CreateFieldLink(self, field_name: str, field_to_link: Field) -> FieldLink:
        """
         Creates a @link NXOpen::Fields::FieldLink NXOpen::Fields::FieldLink@endlink .
                 
         @return field_link (@link FieldLink NXOpen.Fields.FieldLink@endlink):  field .
        """
        pass
    
    ##  Creates a @link NXOpen::Fields::FieldLinksTable NXOpen::Fields::FieldLinksTable@endlink  object with dependent and independent variables 
    ##             @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink .
    ##          
    ##  @return field_linkstable (@link FieldLinksTable NXOpen.Fields.FieldLinksTable@endlink):  links table field .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ## <param name="field_manager"> (@link FieldManager NXOpen.Fields.FieldManager@endlink) </param>
    ## <param name="field_name"> (str)  field name </param>
    ## <param name="indep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  independent variables to be associated with the field </param>
    ## <param name="dep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  dependent variables of this and all linked fields </param>
    ## <param name="datapoints"> (List[float])  row based array of double values representing the first independent variable; the number of points should equal the number of rows. </param>
    ## <param name="link_fields_array"> (@link Field List[NXOpen.Fields.Field]@endlink)  row based array of link field values representing the table; the number of fields should equal the number of rows.</param>
    @overload
    def CreateFieldLinksTable(self, field_name: str, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable], datapoints: List[float], link_fields_array: List[Field]) -> FieldLinksTable:
        """
         Creates a @link NXOpen::Fields::FieldLinksTable NXOpen::Fields::FieldLinksTable@endlink  object with dependent and independent variables 
                    @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink .
                 
         @return field_linkstable (@link FieldLinksTable NXOpen.Fields.FieldLinksTable@endlink):  links table field .
        """
        pass
    
    ##  Creates a @link NXOpen::Fields::FieldLinksTable NXOpen::Fields::FieldLinksTable@endlink  object with dependent and independent variables
    ##            with constant value user input @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink .
    ##         
    ##  @return field_linkstable (@link FieldLinksTable NXOpen.Fields.FieldLinksTable@endlink):  links table field .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="field_name"> (str)  field name </param>
    ## <param name="indep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  independent variables to be associated with the field </param>
    ## <param name="dep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  dependent variables of this and all linked fields </param>
    ## <param name="datapoints"> (List[float])  num_points = num_rows * (1 + numDepVars) </param>
    ## <param name="link_fields_array"> (@link Field List[NXOpen.Fields.Field]@endlink)  row based array of link field values representing the table; the number of fields should equal the number of rows.</param>
    ## <param name="managed_fields_array"> (List[bool])  row based array of logical values indicating the links table field should manage the specified fields .</param>
    def CreateFieldLinksTableWithConstants(self, field_name: str, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable], datapoints: List[float], link_fields_array: List[Field], managed_fields_array: List[bool]) -> FieldLinksTable:
        """
         Creates a @link NXOpen::Fields::FieldLinksTable NXOpen::Fields::FieldLinksTable@endlink  object with dependent and independent variables
                   with constant value user input @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink .
                
         @return field_linkstable (@link FieldLinksTable NXOpen.Fields.FieldLinksTable@endlink):  links table field .
        """
        pass
    
    ##  Creates a @link NXOpen::Fields::FieldLinksTable NXOpen::Fields::FieldLinksTable@endlink  object with dependent and independent variables 
    ##             @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink .
    ##          
    ##  @return field_linkstable (@link FieldLinksTable NXOpen.Fields.FieldLinksTable@endlink):  links table field .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## <param name="field_manager"> (@link FieldManager NXOpen.Fields.FieldManager@endlink) </param>
    ## <param name="field_name"> (str)  field name </param>
    ## <param name="indep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  independent variables to be associated with the field </param>
    ## <param name="dep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  dependent variables of this and all linked fields </param>
    ## <param name="datapoints"> (List[float])  row based array of double values representing the first independent variable; the number of points should equal the number of rows. </param>
    ## <param name="link_fields_array"> (@link Field List[NXOpen.Fields.Field]@endlink)  row based array of link field values representing the table; the number of fields should equal the number of rows.</param>
    ## <param name="managed_fields_array"> (List[bool])  row based array of logical values indicating the links table field should manage the specified fields .</param>
    @overload
    def CreateFieldLinksTable(self, field_name: str, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable], datapoints: List[float], link_fields_array: List[Field], managed_fields_array: List[bool]) -> FieldLinksTable:
        """
         Creates a @link NXOpen::Fields::FieldLinksTable NXOpen::Fields::FieldLinksTable@endlink  object with dependent and independent variables 
                    @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink .
                 
         @return field_linkstable (@link FieldLinksTable NXOpen.Fields.FieldLinksTable@endlink):  links table field .
        """
        pass
    
    ##  Creates a @link NXOpen::Fields::FieldTable NXOpen::Fields::FieldTable@endlink  object with dependent and independent variables 
    ##             @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink .
    ##          
    ##  @return field_table (@link FieldTable NXOpen.Fields.FieldTable@endlink):  field .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## <param name="field_manager"> (@link FieldManager NXOpen.Fields.FieldManager@endlink) </param>
    ## <param name="field_name"> (str)  field name </param>
    ## <param name="indep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  independent variables to be associated with the table field </param>
    ## <param name="dep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  dependent variables to be associated with the table field </param>
    ## <param name="datapoints"> (List[float])  row based array of double values representing the table; then number of points should equal the number of independent variables * the number of dependent variables * the number of rows. </param>
    @overload
    def CreateFieldTable(self, field_name: str, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable], datapoints: List[float]) -> FieldTable:
        """
         Creates a @link NXOpen::Fields::FieldTable NXOpen::Fields::FieldTable@endlink  object with dependent and independent variables 
                    @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink .
                 
         @return field_table (@link FieldTable NXOpen.Fields.FieldTable@endlink):  field .
        """
        pass
    
    ##  Creates a @link NXOpen::Fields::FieldTable NXOpen::Fields::FieldTable@endlink  object with dependent and independent variables
    ##             @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink .  This will create a 2 dimensional table, with the option to specify 
    ##             the value type for the dependent variable.
    ##          
    ##  @return field_table (@link FieldTable NXOpen.Fields.FieldTable@endlink):  field .
    ## 
    ##   <br>  Created in NX7.5.2  <br> 

    ## License requirements: None.
    ## 
    ## <param name="field_name_prefix"> (str)  field name prefix; e.g. "AFU Record"; field will have a unique generated name begining with this string </param>
    ## <param name="ivar_unit"> (@link NXOpen.Unit NXOpen.Unit@endlink)  unit of the independent variable </param>
    ## <param name="dvar_unit"> (@link NXOpen.Unit NXOpen.Unit@endlink)  unit of the dependent variable </param>
    ## <param name="dvar_type"> (@link FieldVariable.ValueType NXOpen.Fields.FieldVariable.ValueType@endlink)  dependent variable type (real/imaginary/complex...) </param>
    ## <param name="datapoints"> (List[float])  row based array of double values representing the table; then number of points should equal the number of independent variables * the number of dependent variables * the number of rows. </param>
    def CreateFieldTableFromData(self, field_name_prefix: str, ivar_unit: NXOpen.Unit, dvar_unit: NXOpen.Unit, dvar_type: FieldVariable.ValueType, datapoints: List[float]) -> FieldTable:
        """
         Creates a @link NXOpen::Fields::FieldTable NXOpen::Fields::FieldTable@endlink  object with dependent and independent variables
                    @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink .  This will create a 2 dimensional table, with the option to specify 
                    the value type for the dependent variable.
                 
         @return field_table (@link FieldTable NXOpen.Fields.FieldTable@endlink):  field .
        """
        pass
    
    ##  Creates a @link NXOpen::Fields::FieldTable NXOpen::Fields::FieldTable@endlink  object with dependent and independent variables
    ##             @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink .  This will create a 2 dimensional table, with the option to specify 
    ##             the value type for the dependent variable, and to specify the Name for the Dependent variable. 
    ##             Used when the dependent variable name does not come from the Unit Measure.
    ##          
    ##  @return field_table (@link FieldTable NXOpen.Fields.FieldTable@endlink):  field .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="field_name_prefix"> (str)  field name prefix; e.g. "AFU Record"; field will have a unique generated name begining with this string </param>
    ## <param name="ivar_unit"> (@link NXOpen.Unit NXOpen.Unit@endlink)  unit of the independent variable </param>
    ## <param name="dvar_unit"> (@link NXOpen.Unit NXOpen.Unit@endlink)  unit of the dependent variable </param>
    ## <param name="dvar_type"> (@link FieldVariable.ValueType NXOpen.Fields.FieldVariable.ValueType@endlink)  dependent variable type (real/imaginary/complex...) </param>
    ## <param name="dvar_name"> (str)  Dependent Variable Name.  EG: "PSD Factor"  "CSD Factor" </param>
    ## <param name="datapoints"> (List[float])  row based array of double values representing the table; then number of points should equal the number of independent variables * the number of dependent variables * the number of rows. </param>
    def CreateFieldTableFromDataAndDepVarName(self, field_name_prefix: str, ivar_unit: NXOpen.Unit, dvar_unit: NXOpen.Unit, dvar_type: FieldVariable.ValueType, dvar_name: str, datapoints: List[float]) -> FieldTable:
        """
         Creates a @link NXOpen::Fields::FieldTable NXOpen::Fields::FieldTable@endlink  object with dependent and independent variables
                    @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink .  This will create a 2 dimensional table, with the option to specify 
                    the value type for the dependent variable, and to specify the Name for the Dependent variable. 
                    Used when the dependent variable name does not come from the Unit Measure.
                 
         @return field_table (@link FieldTable NXOpen.Fields.FieldTable@endlink):  field .
        """
        pass
    
    ##  Creates a @link NXOpen::Fields::FieldTable NXOpen::Fields::FieldTable@endlink  object with duplicate value processing option,dependent and independent variables, and
    ##              expression strings.
    ##          
    ##  @return field_table (@link FieldTable NXOpen.Fields.FieldTable@endlink):  field .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## <param name="field_manager"> (@link FieldManager NXOpen.Fields.FieldManager@endlink) </param>
    ## <param name="field_name"> (str)  field name </param>
    ## <param name="indep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  independent variables to be associated with the table field </param>
    ## <param name="dep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  dependent variables to be associated with the table field </param>
    ## <param name="datapoints"> (List[float]) </param>
    ## <param name="dupValueProcessOption"> (@link FieldTable.DuplicateValueOption NXOpen.Fields.FieldTable.DuplicateValueOption@endlink) </param>
    ## <param name="exp_cell_ids"> (List[int]) </param>
    ## <param name="valueStrings"> (List[str])  array of string values </param>
    @overload
    def CreateFieldTableWithExpressions(self, field_name: str, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable], datapoints: List[float], dupValueProcessOption: FieldTable.DuplicateValueOption, exp_cell_ids: List[int], valueStrings: List[str]) -> FieldTable:
        """
         Creates a @link NXOpen::Fields::FieldTable NXOpen::Fields::FieldTable@endlink  object with duplicate value processing option,dependent and independent variables, and
                     expression strings.
                 
         @return field_table (@link FieldTable NXOpen.Fields.FieldTable@endlink):  field .
        """
        pass
    
    ##  Creates a @link NXOpen::Fields::FieldTable NXOpen::Fields::FieldTable@endlink  object with duplicate value processing option,dependent and independent variables, and
    ##              expression strings.
    ##          
    ##  @return field_table (@link FieldTable NXOpen.Fields.FieldTable@endlink):  field .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## <param name="fieldManager"> (@link FieldManager NXOpen.Fields.FieldManager@endlink) </param>
    ## <param name="field_name"> (str)  field name </param>
    ## <param name="indep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  independent variables to be associated with the table field </param>
    ## <param name="dep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  dependent variables to be associated with the table field </param>
    ## <param name="datapoints"> (List[float]) </param>
    ## <param name="dupValueProcessOption"> (@link FieldTable.DuplicateValueOption NXOpen.Fields.FieldTable.DuplicateValueOption@endlink) </param>
    ## <param name="exp_cell_ids"> (List[int]) </param>
    ## <param name="valueStrings"> (List[str])  array of string values </param>
    ## <param name="cellReadOnlys"> (List[bool]) </param>
    @overload
    def CreateFieldTableWithExpressions(self, field_name: str, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable], datapoints: List[float], dupValueProcessOption: FieldTable.DuplicateValueOption, exp_cell_ids: List[int], valueStrings: List[str], cellReadOnlys: List[bool]) -> FieldTable:
        """
         Creates a @link NXOpen::Fields::FieldTable NXOpen::Fields::FieldTable@endlink  object with duplicate value processing option,dependent and independent variables, and
                     expression strings.
                 
         @return field_table (@link FieldTable NXOpen.Fields.FieldTable@endlink):  field .
        """
        pass
    
    ##  Creates a @link NXOpen::Fields::FieldTable NXOpen::Fields::FieldTable@endlink  object with duplicate value processing option,dependent and independent variables, and smart points
    ##         
    ##  @return field_table (@link FieldTable NXOpen.Fields.FieldTable@endlink):  field .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="field_name"> (str)  field name </param>
    ## <param name="indep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  independent variables to be associated with the table field </param>
    ## <param name="dep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  dependent variables to be associated with the table field </param>
    ## <param name="datapoints"> (List[float])  row based array of double values representing the table; then number of points should equal the number of independent variables * the number of dependent variables * the number of rows. </param>
    ## <param name="duplicateValueProcessingOption"> (@link FieldTable.DuplicateValueOption NXOpen.Fields.FieldTable.DuplicateValueOption@endlink) </param>
    ## <param name="point_object_row_ids"> (List[int])  0 based row ID of rows that have associated point objects </param>
    ## <param name="point_objects"> (@link NXOpen.Point List[NXOpen.Point]@endlink)  array of num_point_objects point objects to be associated to rows </param>
    def CreateFieldTableWithPoints(self, field_name: str, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable], datapoints: List[float], duplicateValueProcessingOption: FieldTable.DuplicateValueOption, point_object_row_ids: List[int], point_objects: List[NXOpen.Point]) -> FieldTable:
        """
         Creates a @link NXOpen::Fields::FieldTable NXOpen::Fields::FieldTable@endlink  object with duplicate value processing option,dependent and independent variables, and smart points
                
         @return field_table (@link FieldTable NXOpen.Fields.FieldTable@endlink):  field .
        """
        pass
    
    ##  Creates a @link NXOpen::Fields::FieldTable NXOpen::Fields::FieldTable@endlink  object with duplicate value processing option,dependent and independent variables 
    ##             @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink .
    ##          
    ##  @return field_table (@link FieldTable NXOpen.Fields.FieldTable@endlink):  field .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## <param name="field_manager"> (@link FieldManager NXOpen.Fields.FieldManager@endlink) </param>
    ## <param name="field_name"> (str)  field name </param>
    ## <param name="indep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  independent variables to be associated with the table field </param>
    ## <param name="dep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  dependent variables to be associated with the table field </param>
    ## <param name="datapoints"> (List[float])  row based array of double values representing the table; then number of points should equal the number of independent variables * the number of dependent variables * the number of rows. </param>
    ## <param name="duplicateValueProcessingOption"> (@link FieldTable.DuplicateValueOption NXOpen.Fields.FieldTable.DuplicateValueOption@endlink) </param>
    @overload
    def CreateFieldTable(self, field_name: str, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable], datapoints: List[float], duplicateValueProcessingOption: FieldTable.DuplicateValueOption) -> FieldTable:
        """
         Creates a @link NXOpen::Fields::FieldTable NXOpen::Fields::FieldTable@endlink  object with duplicate value processing option,dependent and independent variables 
                    @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink .
                 
         @return field_table (@link FieldTable NXOpen.Fields.FieldTable@endlink):  field .
        """
        pass
    
    ##  Creates a @link NXOpen::Fields::FieldTable NXOpen::Fields::FieldTable@endlink  object with Table Struct Data ,Duplicate value processing option,dependent and independent variables 
    ##             @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink .
    ##          
    ##  @return field_table (@link FieldTable NXOpen.Fields.FieldTable@endlink):  field .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## <param name="field_manager"> (@link FieldManager NXOpen.Fields.FieldManager@endlink) </param>
    ## <param name="field_name"> (str)  field name </param>
    ## <param name="indep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  independent variables to be associated with the table field </param>
    ## <param name="dep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  dependent variables to be associated with the table field </param>
    ## <param name="datapoints"> (List[float])  row based array of double values representing the table; then number of points should equal the number of independent variables * the number of dependent variables * the number of rows. </param>
    ## <param name="duplicateValueProcessingOption"> (@link FieldTable.DuplicateValueOption NXOpen.Fields.FieldTable.DuplicateValueOption@endlink) </param>
    ## <param name="struct_data_type"> (@link FieldTable.StructDataTableType NXOpen.Fields.FieldTable.StructDataTableType@endlink) </param>
    ## <param name="numStructDataRows"> (int) </param>
    ## <param name="numStructDataColumns"> (int) </param>
    ## <param name="numStructDataPlanes"> (int) </param>
    @overload
    def CreateFieldTable(self, field_name: str, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable], datapoints: List[float], duplicateValueProcessingOption: FieldTable.DuplicateValueOption, struct_data_type: FieldTable.StructDataTableType, numStructDataRows: int, numStructDataColumns: int, numStructDataPlanes: int) -> FieldTable:
        """
         Creates a @link NXOpen::Fields::FieldTable NXOpen::Fields::FieldTable@endlink  object with Table Struct Data ,Duplicate value processing option,dependent and independent variables 
                    @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink .
                 
         @return field_table (@link FieldTable NXOpen.Fields.FieldTable@endlink):  field .
        """
        pass
    
    ##  Create a field wrapper backed up by a field 
    ##  @return fieldWrapper (@link FieldWrapper NXOpen.Fields.FieldWrapper@endlink):  scalar field wrapper created and associated to the field .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="field"> (@link Field NXOpen.Fields.Field@endlink)  an existing field that will be this wrapper's value </param>
    def CreateFieldWrapper(self, field: Field) -> FieldWrapper:
        """
         Create a field wrapper backed up by a field 
         @return fieldWrapper (@link FieldWrapper NXOpen.Fields.FieldWrapper@endlink):  scalar field wrapper created and associated to the field .
        """
        pass
    
    ##  Creates a global @link NXOpen::Fields::SpatialMap NXOpen::Fields::SpatialMap@endlink  
    ##  @return spatialmap (@link SpatialMap NXOpen.Fields.SpatialMap@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    def CreateGlobalSpatialMap(self) -> SpatialMap:
        """
         Creates a global @link NXOpen::Fields::SpatialMap NXOpen::Fields::SpatialMap@endlink  
         @return spatialmap (@link SpatialMap NXOpen.Fields.SpatialMap@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Fields::ImportBuilder NXOpen::Fields::ImportBuilder@endlink  
    ##  @return pBuilder (@link ImportBuilder NXOpen.Fields.ImportBuilder@endlink):  the import builder created .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def CreateImportBuilder(self) -> ImportBuilder:
        """
         Creates a @link NXOpen::Fields::ImportBuilder NXOpen::Fields::ImportBuilder@endlink  
         @return pBuilder (@link ImportBuilder NXOpen.Fields.ImportBuilder@endlink):  the import builder created .
        """
        pass
    
    ##  Creates a @link NXOpen::Fields::ImportTableDataBuilder NXOpen::Fields::ImportTableDataBuilder@endlink  with inputs to create the field on commit
    ##  @return builder (@link ImportTableDataBuilder NXOpen.Fields.ImportTableDataBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="field_name"> (str)  field name </param>
    ## <param name="indep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  independent variables to be associated with the table field </param>
    ## <param name="dep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  dependent variables to be associated with the table field </param>
    def CreateImportTableDataBuilder(self, field_name: str, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable]) -> ImportTableDataBuilder:
        """
         Creates a @link NXOpen::Fields::ImportTableDataBuilder NXOpen::Fields::ImportTableDataBuilder@endlink  with inputs to create the field on commit
         @return builder (@link ImportTableDataBuilder NXOpen.Fields.ImportTableDataBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Fields::ImportTableDataBuilder NXOpen::Fields::ImportTableDataBuilder@endlink  with inputs to create the field on commit
    ##  @return builder (@link ImportTableDataBuilder NXOpen.Fields.ImportTableDataBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="field_table"> (@link FieldTable NXOpen.Fields.FieldTable@endlink)  existing table field to import data to </param>
    def CreateImportTableDataBuilderFromTable(self, field_table: FieldTable) -> ImportTableDataBuilder:
        """
         Creates a @link NXOpen::Fields::ImportTableDataBuilder NXOpen::Fields::ImportTableDataBuilder@endlink  with inputs to create the field on commit
         @return builder (@link ImportTableDataBuilder NXOpen.Fields.ImportTableDataBuilder@endlink): .
        """
        pass
    
    ##  Create an independent variable to be added to the field 
    ##          
    ##  @return indep_var (@link FieldVariable NXOpen.Fields.FieldVariable@endlink):  independent variable created and associated to the field .
    ## 
    ##   <br>  Created in NX6.0.2  <br> 

    ## License requirements: None.
    ## <param name="field_manager"> (@link FieldManager NXOpen.Fields.FieldManager@endlink) </param>
    ## <param name="owner_field"> (@link Field NXOpen.Fields.Field@endlink)  owner field </param>
    ## <param name="name_variable"> (@link NameVariable NXOpen.Fields.NameVariable@endlink)  existing name variable </param>
    ## <param name="unit_type"> (@link NXOpen.Unit NXOpen.Unit@endlink)  unit of the independent variable </param>
    ## <param name="min_value_set"> (bool)  logical value whether minimum value set </param>
    ## <param name="min_value_inclusive"> (bool)  minimum value is itself included in range </param>
    ## <param name="min_value"> (float)  minimum value of the variable range </param>
    ## <param name="max_value_set"> (bool)  logical value whether maximum value set </param>
    ## <param name="max_value_inclusive"> (bool)  maximum value is itself included in range </param>
    ## <param name="max_value"> (float)  maximum value of the variable range </param>
    ## <param name="num_pts_set"> (bool)  logical value whether num_pts set </param>
    ## <param name="num_pts"> (int)  num_pts of the variable range </param>
    ## <param name="default_value_set"> (bool)  logical value whether default value set </param>
    ## <param name="default_value"> (float)  default value of the variable range </param>
    @overload
    def CreateIndependentVariable(self, owner_field: Field, name_variable: NameVariable, unit_type: NXOpen.Unit, min_value_set: bool, min_value_inclusive: bool, min_value: float, max_value_set: bool, max_value_inclusive: bool, max_value: float, num_pts_set: bool, num_pts: int, default_value_set: bool, default_value: float) -> FieldVariable:
        """
         Create an independent variable to be added to the field 
                 
         @return indep_var (@link FieldVariable NXOpen.Fields.FieldVariable@endlink):  independent variable created and associated to the field .
        """
        pass
    
    ##  Create an independent variable to be added to the field, specifying the variable value type
    ##          
    ##  @return indep_var (@link FieldVariable NXOpen.Fields.FieldVariable@endlink):  independent variable created and associated to the field .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## <param name="field_manager"> (@link FieldManager NXOpen.Fields.FieldManager@endlink) </param>
    ## <param name="owner_field"> (@link Field NXOpen.Fields.Field@endlink)  owner field </param>
    ## <param name="name_variable"> (@link NameVariable NXOpen.Fields.NameVariable@endlink)  existing name variable </param>
    ## <param name="unit_type"> (@link NXOpen.Unit NXOpen.Unit@endlink)  unit of the independent variable </param>
    ## <param name="type"> (@link FieldVariable.ValueType NXOpen.Fields.FieldVariable.ValueType@endlink)  variable value type </param>
    ## <param name="min_value_set"> (bool)  logical value whether minimum value set </param>
    ## <param name="min_value_inclusive"> (bool)  minimum value is itself included in range </param>
    ## <param name="min_value"> (float)  minimum value of the variable range </param>
    ## <param name="max_value_set"> (bool)  logical value whether maximum value set </param>
    ## <param name="max_value_inclusive"> (bool)  maximum value is itself included in range </param>
    ## <param name="max_value"> (float)  maximum value of the variable range </param>
    ## <param name="num_pts_set"> (bool)  logical value whether num_pts set </param>
    ## <param name="num_pts"> (int)  num_pts of the variable range </param>
    ## <param name="default_value_set"> (bool)  logical value whether default value set </param>
    ## <param name="default_value"> (float)  default value of the variable range </param>
    @overload
    def CreateIndependentVariable(self, owner_field: Field, name_variable: NameVariable, unit_type: NXOpen.Unit, type: FieldVariable.ValueType, min_value_set: bool, min_value_inclusive: bool, min_value: float, max_value_set: bool, max_value_inclusive: bool, max_value: float, num_pts_set: bool, num_pts: int, default_value_set: bool, default_value: float) -> FieldVariable:
        """
         Create an independent variable to be added to the field, specifying the variable value type
                 
         @return indep_var (@link FieldVariable NXOpen.Fields.FieldVariable@endlink):  independent variable created and associated to the field .
        """
        pass
    
    ##  Create Mesh Size Field @link NXOpen::Fields::Field NXOpen::Fields::Field@endlink  object
    ##          
    ##  @return field_meshsize (@link Field NXOpen.Fields.Field@endlink):  Created Field .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="element_size_type"> (int)  At Centroid of Element Free Face and Elements=0,  At Centroid of Element Free Faces=1, At Centroid of Elements=2 </param>
    ## <param name="mesh_array"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink) </param>
    def CreateMeshSizeFieldData(self, element_size_type: int, mesh_array: List[NXOpen.TaggedObject]) -> Field:
        """
         Create Mesh Size Field @link NXOpen::Fields::Field NXOpen::Fields::Field@endlink  object
                 
         @return field_meshsize (@link Field NXOpen.Fields.Field@endlink):  Created Field .
        """
        pass
    
    ##  Creates a @link NXOpen::Fields::PathObjects NXOpen::Fields::PathObjects@endlink  
    ##  @return pathObjects (@link PathObjects NXOpen.Fields.PathObjects@endlink): .
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    ## License requirements: None.
    def CreatePathObjects(self) -> PathObjects:
        """
         Creates a @link NXOpen::Fields::PathObjects NXOpen::Fields::PathObjects@endlink  
         @return pathObjects (@link PathObjects NXOpen.Fields.PathObjects@endlink): .
        """
        pass
    
    ##  Create a field wrapper backed by a scalar expression 
    ##  @return scalarFieldWrapper (@link ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink):  scalar field wrapper created and associated to the expression .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="expression"> (@link NXOpen.Expression NXOpen.Expression@endlink)  an existing expression that will be this wrapper's value </param>
    def CreateScalarFieldWrapperWithExpression(self, expression: NXOpen.Expression) -> ScalarFieldWrapper:
        """
         Create a field wrapper backed by a scalar expression 
         @return scalarFieldWrapper (@link ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink):  scalar field wrapper created and associated to the expression .
        """
        pass
    
    ##  Create a scalar field wrapper backed up by a scaled scalar field 
    ##  @return scalarFieldWrapper (@link ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink):  scalar field wrapper created and associated to the field .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="field"> (@link Field NXOpen.Fields.Field@endlink)  an existing field that will be this wrapper's value </param>
    ## <param name="scaleFactor"> (float)  the field will be multiplied by this scale factor when being evaluated </param>
    def CreateScalarFieldWrapperWithField(self, field: Field, scaleFactor: float) -> ScalarFieldWrapper:
        """
         Create a scalar field wrapper backed up by a scaled scalar field 
         @return scalarFieldWrapper (@link ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink):  scalar field wrapper created and associated to the field .
        """
        pass
    
    ##  Creates a @link NXOpen::Fields::SpatialMapBuilder NXOpen::Fields::SpatialMapBuilder@endlink  
    ##  @return builder (@link SpatialMapBuilder NXOpen.Fields.SpatialMapBuilder@endlink): .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="spatialmap"> (@link SpatialMap NXOpen.Fields.SpatialMap@endlink)  Existing SpatialMap to edit; NULL to create </param>
    def CreateSpatialMapBuilder(self, spatialmap: SpatialMap) -> SpatialMapBuilder:
        """
         Creates a @link NXOpen::Fields::SpatialMapBuilder NXOpen::Fields::SpatialMapBuilder@endlink  
         @return builder (@link SpatialMapBuilder NXOpen.Fields.SpatialMapBuilder@endlink): .
        """
        pass
    
    ##  Creates a system @link NXOpen::Fields::FieldExpression NXOpen::Fields::FieldExpression@endlink  object with independent variables.
    ##             Specifies the new expression string.
    ##              <br> This method is used to create sub expression fields for a 
    ##             @link NXOpen::Fields::FieldFormula NXOpen::Fields::FieldFormula@endlink . <br> 
    ##          
    ##  @return field_expression (@link FieldExpression NXOpen.Fields.FieldExpression@endlink):  field .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="dep_var"> (@link FieldVariable NXOpen.Fields.FieldVariable@endlink)  dependent variables to be associated with the field </param>
    def CreateSubFieldExpression(self, dep_var: FieldVariable) -> FieldExpression:
        """
         Creates a system @link NXOpen::Fields::FieldExpression NXOpen::Fields::FieldExpression@endlink  object with independent variables.
                    Specifies the new expression string.
                     <br> This method is used to create sub expression fields for a 
                    @link NXOpen::Fields::FieldFormula NXOpen::Fields::FieldFormula@endlink . <br> 
                 
         @return field_expression (@link FieldExpression NXOpen.Fields.FieldExpression@endlink):  field .
        """
        pass
    
    ##  Create a vector field wrapper backed by three scalar expressions 
    ##  @return vectorFieldWrapper (@link VectorFieldWrapper NXOpen.Fields.VectorFieldWrapper@endlink):  scalar field wrapper created and associated to the expression .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="expressions"> (@link NXOpen.Expression List[NXOpen.Expression]@endlink)  existing expressions that will be this wrapper's value </param>
    def CreateVectorFieldWrapperWithExpressions(self, expressions: List[NXOpen.Expression]) -> VectorFieldWrapper:
        """
         Create a vector field wrapper backed by three scalar expressions 
         @return vectorFieldWrapper (@link VectorFieldWrapper NXOpen.Fields.VectorFieldWrapper@endlink):  scalar field wrapper created and associated to the expression .
        """
        pass
    
    ##  Create a vector field wrapper backed up by a scaled vector field 
    ##  @return vectorFieldWrapper (@link VectorFieldWrapper NXOpen.Fields.VectorFieldWrapper@endlink):  vector field wrapper created and associated to the field .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="field"> (@link Field NXOpen.Fields.Field@endlink)  an existing field that will be this wrapper's value </param>
    ## <param name="scaleFactors"> (List[float])  the field will be multiplied by this scale factor when being evaluated </param>
    def CreateVectorFieldWrapperWithField(self, field: Field, scaleFactors: List[float]) -> VectorFieldWrapper:
        """
         Create a vector field wrapper backed up by a scaled vector field 
         @return vectorFieldWrapper (@link VectorFieldWrapper NXOpen.Fields.VectorFieldWrapper@endlink):  vector field wrapper created and associated to the field .
        """
        pass
    
    ##  Deletes the specified @link NXOpen::Fields::Field NXOpen::Fields::Field@endlink  object; if the object cannot be deleted
    ##             it is returned.
    ##          
    ##  @return field_surviving (@link Field NXOpen.Fields.Field@endlink):  If the field cannot be deleted, it is returned; if the field is deleted, this will be NULL .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="field"> (@link Field NXOpen.Fields.Field@endlink)  field to delete </param>
    def DeleteField(self, field: Field) -> Field:
        """
         Deletes the specified @link NXOpen::Fields::Field NXOpen::Fields::Field@endlink  object; if the object cannot be deleted
                    it is returned.
                 
         @return field_surviving (@link Field NXOpen.Fields.Field@endlink):  If the field cannot be deleted, it is returned; if the field is deleted, this will be NULL .
        """
        pass
    
    ##  Deletes the specified collections of @link NXOpen::Fields::Field NXOpen::Fields::Field@endlink  objects;
    ##          
    ##  @return deletionStatus (List[bool]): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="fields"> (@link Field List[NXOpen.Fields.Field]@endlink) </param>
    def DeleteFields(self, fields: List[Field]) -> List[bool]:
        """
         Deletes the specified collections of @link NXOpen::Fields::Field NXOpen::Fields::Field@endlink  objects;
                 
         @return deletionStatus (List[bool]): .
        """
        pass
    
    ##  Deletes the specified @link NXOpen::Fields::FieldFolder NXOpen::Fields::FieldFolder@endlink  folder and its contents.
    ##             Any fields that cannot be deleted will be returned to the root folder.
    ##          
    ##  @return survivingFields (@link Field List[NXOpen.Fields.Field]@endlink):  any fields that could not be deleted .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="folders"> (@link FieldFolder List[NXOpen.Fields.FieldFolder]@endlink)  folders to delete </param>
    def DeleteFolders(self, folders: List[FieldFolder]) -> List[Field]:
        """
         Deletes the specified @link NXOpen::Fields::FieldFolder NXOpen::Fields::FieldFolder@endlink  folder and its contents.
                    Any fields that cannot be deleted will be returned to the root folder.
                 
         @return survivingFields (@link Field List[NXOpen.Fields.Field]@endlink):  any fields that could not be deleted .
        """
        pass
    
    ##  Edit dependent variable 
    ##          
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## <param name="field_manager"> (@link FieldManager NXOpen.Fields.FieldManager@endlink) </param>
    ## <param name="dep_var"> (@link FieldVariable NXOpen.Fields.FieldVariable@endlink)  dep variable to edit </param>
    ## <param name="var_name"> (str)  new name for variable, or NULL to skip updating name </param>
    ## <param name="unit_type"> (@link NXOpen.Unit NXOpen.Unit@endlink)  new unit of the dependent variable </param>
    @overload
    def EditDependentVariable(self, dep_var: FieldVariable, var_name: str, unit_type: NXOpen.Unit) -> None:
        """
         Edit dependent variable 
                 
        """
        pass
    
    ##  Edit dependent variable 
    ##          
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## <param name="field_manager"> (@link FieldManager NXOpen.Fields.FieldManager@endlink) </param>
    ## <param name="dep_var"> (@link FieldVariable NXOpen.Fields.FieldVariable@endlink)  dep variable to edit </param>
    ## <param name="unit_type"> (@link NXOpen.Unit NXOpen.Unit@endlink)  new unit of the dependent variable </param>
    @overload
    def EditDependentVariable(self, dep_var: FieldVariable, unit_type: NXOpen.Unit) -> None:
        """
         Edit dependent variable 
                 
        """
        pass
    
    ##  Edit an independent variable 
    ##          
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## <param name="field_manager"> (@link FieldManager NXOpen.Fields.FieldManager@endlink) </param>
    ## <param name="indep_var"> (@link FieldVariable NXOpen.Fields.FieldVariable@endlink)  indep var to edit </param>
    ## <param name="var_name"> (str)  name of the independent variable to be created </param>
    ## <param name="unit_type"> (@link NXOpen.Unit NXOpen.Unit@endlink)  unit of the independent variable </param>
    ## <param name="min_value_set"> (bool)  logical value whether minimum value set </param>
    ## <param name="min_value_inclusive"> (bool)  minimum value is itself included in range </param>
    ## <param name="min_value"> (float)  minimum value of the variable range </param>
    ## <param name="max_value_set"> (bool)  logical value whether maximum value set </param>
    ## <param name="max_value_inclusive"> (bool)  maximum value is itself included in range </param>
    ## <param name="max_value"> (float)  maximum value of the variable range </param>
    ## <param name="num_pts_set"> (bool)  logical value whether num_pts set </param>
    ## <param name="num_pts"> (int)  num_pts of the variable range </param>
    ## <param name="default_value_set"> (bool)  logical value whether default value set </param>
    ## <param name="default_value"> (float)  default value of the variable range </param>
    @overload
    def EditIndependentVariable(self, indep_var: FieldVariable, var_name: str, unit_type: NXOpen.Unit, min_value_set: bool, min_value_inclusive: bool, min_value: float, max_value_set: bool, max_value_inclusive: bool, max_value: float, num_pts_set: bool, num_pts: int, default_value_set: bool, default_value: float) -> None:
        """
         Edit an independent variable 
                 
        """
        pass
    
    ##  Edit an independent variable 
    ##          
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## <param name="field_manager"> (@link FieldManager NXOpen.Fields.FieldManager@endlink) </param>
    ## <param name="indep_var"> (@link FieldVariable NXOpen.Fields.FieldVariable@endlink)  indep var to edit </param>
    ## <param name="unit_type"> (@link NXOpen.Unit NXOpen.Unit@endlink)  unit of the independent variable </param>
    @overload
    def EditIndependentVariable(self, indep_var: FieldVariable, unit_type: NXOpen.Unit) -> None:
        """
         Edit an independent variable 
                 
        """
        pass
    
    ##  Exports fields to a text file as defined by export_data parameter 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="export_data"> (@link ExportData NXOpen.Fields.ExportData@endlink)  Export data </param>
    def ExportFields(self, export_data: ExportData) -> None:
        """
         Exports fields to a text file as defined by export_data parameter 
        """
        pass
    
    ##  Locate an existing, or create a new @link NXOpen::Fields::NameVariable NXOpen::Fields::NameVariable@endlink  object 
    ##  @return name_variable (@link NameVariable NXOpen.Fields.NameVariable@endlink):  name variable with the specified measure and name .
    ## 
    ##   <br>  Created in NX6.0.2  <br> 

    ## License requirements: None.
    ## 
    ## <param name="variable_name"> (str)  alphanumeric string; if it matches an existing name variable, the measures must also match </param>
    ## <param name="measure_name"> (str)  must match an existing measure name, or "Unitless" </param>
    def GetNameVariable(self, variable_name: str, measure_name: str) -> NameVariable:
        """
         Locate an existing, or create a new @link NXOpen::Fields::NameVariable NXOpen::Fields::NameVariable@endlink  object 
         @return name_variable (@link NameVariable NXOpen.Fields.NameVariable@endlink):  name variable with the specified measure and name .
        """
        pass
    
    ##  Get the next available ID for @link NXOpen::Fields::Field NXOpen::Fields::Field@endlink  object 
    ##  @return valid_id (int):  valid id .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    def GetValidFieldId(self) -> int:
        """
         Get the next available ID for @link NXOpen::Fields::Field NXOpen::Fields::Field@endlink  object 
         @return valid_id (int):  valid id .
        """
        pass
    
    ##  Displays information about specified fields.
    ##          
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="fields"> (@link Field List[NXOpen.Fields.Field]@endlink)  fields to list </param>
    def Information(self, fields: List[Field]) -> None:
        """
         Displays information about specified fields.
                 
        """
        pass
    
    ##  Set the value to be used for un-set variables and plugin functions when evaluating an expression 
    ##         
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="undefinedValue"> (float)  value to be used for un-set variables and plugin functions when evaluating an expression  </param>
    def SetUndefinedVariableValue(self, undefinedValue: float) -> None:
        """
         Set the value to be used for un-set variables and plugin functions when evaluating an expression 
                
        """
        pass
    
##   @brief  Represents an reference field  
## 
##   
##      <br> A Reference Field exposes data inside of an abstract data store.  An abstract data store
##           is provided by an appropriate application data provider, and allows access to the provider
##           data as a @link Fields::Field Fields::Field@endlink  <br> 
##      <br> To obtain a instance of this class use an appropriate application data provider.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class FieldReference(Field): 
    """ <summary> Represents an reference field </summary> 
    <para>A Reference Field exposes data inside of an abstract data store.  An abstract data store
          is provided by an appropriate application data provider, and allows access to the provider
          data as a <ja_class>Fields.Field</ja_class></para>
    """


    ## Getter for property: (@link FieldEvaluator.ValuesOutsideTableInterpolationEnum NXOpen.Fields.FieldEvaluator.ValuesOutsideTableInterpolationEnum@endlink) ValuesOutsideTableInterpolation
    ##  Returns the outside table values interpolation method for linear interpolation.  
    ##   
    ##             If the reference field is heterogeneous, this method gets the outside table values interpolation method for the primary independent doamin and
    ##             use set_secondary_values_outside_table_interpolation method for the secondary independent domain.
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return FieldEvaluator.ValuesOutsideTableInterpolationEnum
    @property
    def ValuesOutsideTableInterpolation(self) -> FieldEvaluator.ValuesOutsideTableInterpolationEnum:
        """
        Getter for property: (@link FieldEvaluator.ValuesOutsideTableInterpolationEnum NXOpen.Fields.FieldEvaluator.ValuesOutsideTableInterpolationEnum@endlink) ValuesOutsideTableInterpolation
         Returns the outside table values interpolation method for linear interpolation.  
          
                    If the reference field is heterogeneous, this method gets the outside table values interpolation method for the primary independent doamin and
                    use set_secondary_values_outside_table_interpolation method for the secondary independent domain.
                      
         
        """
        pass
    
    ## Setter for property: (@link FieldEvaluator.ValuesOutsideTableInterpolationEnum NXOpen.Fields.FieldEvaluator.ValuesOutsideTableInterpolationEnum@endlink) ValuesOutsideTableInterpolation

    ##  Returns the outside table values interpolation method for linear interpolation.  
    ##   
    ##             If the reference field is heterogeneous, this method gets the outside table values interpolation method for the primary independent doamin and
    ##             use set_secondary_values_outside_table_interpolation method for the secondary independent domain.
    ##               
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ValuesOutsideTableInterpolation.setter
    def ValuesOutsideTableInterpolation(self, interpolationMethod: FieldEvaluator.ValuesOutsideTableInterpolationEnum):
        """
        Setter for property: (@link FieldEvaluator.ValuesOutsideTableInterpolationEnum NXOpen.Fields.FieldEvaluator.ValuesOutsideTableInterpolationEnum@endlink) ValuesOutsideTableInterpolation
         Returns the outside table values interpolation method for linear interpolation.  
          
                    If the reference field is heterogeneous, this method gets the outside table values interpolation method for the primary independent doamin and
                    use set_secondary_values_outside_table_interpolation method for the secondary independent domain.
                      
         
        """
        pass
    
    ##  If the reference field is heterogeneous, set the outside table values interpolation method for the secondary independent domain .
    ##             Otherwise, an error will be raised.
    ##             
    ##  @return interpol_method (@link FieldEvaluator.ValuesOutsideTableInterpolationEnum NXOpen.Fields.FieldEvaluator.ValuesOutsideTableInterpolationEnum@endlink):  the outside table values interpolation method for sub fields.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    def GetSecondaryValuesOutsideTableInterpolation(self) -> FieldEvaluator.ValuesOutsideTableInterpolationEnum:
        """
         If the reference field is heterogeneous, set the outside table values interpolation method for the secondary independent domain .
                    Otherwise, an error will be raised.
                    
         @return interpol_method (@link FieldEvaluator.ValuesOutsideTableInterpolationEnum NXOpen.Fields.FieldEvaluator.ValuesOutsideTableInterpolationEnum@endlink):  the outside table values interpolation method for sub fields.
        """
        pass
    
    ##  If the reference field is heterogeneous, set the outside table values interpolation method for the secondary independent domain .
    ##             Otherwise, an error will be raised.
    ##             
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="interpol_method"> (@link FieldEvaluator.ValuesOutsideTableInterpolationEnum NXOpen.Fields.FieldEvaluator.ValuesOutsideTableInterpolationEnum@endlink)  the outside table values interpolation method for sub fields</param>
    def SetSecondaryValuesOutsideTableInterpolation(self, interpol_method: FieldEvaluator.ValuesOutsideTableInterpolationEnum) -> None:
        """
         If the reference field is heterogeneous, set the outside table values interpolation method for the secondary independent domain .
                    Otherwise, an error will be raised.
                    
        """
        pass
    
import NXOpen
import NXOpen.CAE.Xyplot
##   @brief  Represents the Field Table class. 
## 
##   
##      <br> A field (see @link NXOpen::Fields::Field NXOpen::Fields::Field@endlink ) defined in terms of tabular data involving 
##     one or more look-up independent columns and one or more dependent variables (see 
##     @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink ) which depend on the look-up columns. <br>   <br> To obtain a instance of this class use @link NXOpen::Fields::FieldManager NXOpen::Fields::FieldManager@endlink  .  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class FieldTable(Field): 
    """ <summary> Represents the Field Table class.</summary> 
    <para>A field (see <ja_class>NXOpen.Fields.Field</ja_class>) defined in terms of tabular data involving 
    one or more look-up independent columns and one or more dependent variables (see 
    <ja_class>NXOpen.Fields.FieldVariable</ja_class>) which depend on the look-up columns.</para> """


    ##  Options for dB Factors 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## AcousticPowerDefault</term><description> 
    ## </description> </item><item><term> 
    ## AcousticPressureDefault</term><description> 
    ## </description> </item></list>
    class DBFactor(Enum):
        """
        Members Include: <AcousticPowerDefault> <AcousticPressureDefault>
        """
        AcousticPowerDefault: int
        AcousticPressureDefault: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FieldTable.DBFactor:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  duplicate value processing options
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ## </description> </item><item><term> 
    ## Average</term><description> 
    ## </description> </item><item><term> 
    ## Minimum</term><description> 
    ## </description> </item><item><term> 
    ## Maximum</term><description> 
    ## </description> </item><item><term> 
    ## First</term><description> 
    ## </description> </item><item><term> 
    ## Last</term><description> 
    ## </description> </item><item><term> 
    ## Skip</term><description> 
    ## </description> </item></list>
    class DuplicateValueOption(Enum):
        """
        Members Include: <NotSet> <Average> <Minimum> <Maximum> <First> <Last> <Skip>
        """
        NotSet: int
        Average: int
        Minimum: int
        Maximum: int
        First: int
        Last: int
        Skip: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FieldTable.DuplicateValueOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Load file options
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Append</term><description> 
    ##  Append data to the table removing duplicates </description> </item><item><term> 
    ## Replace</term><description> 
    ##  Replace data removing duplicates </description> </item></list>
    class LoadFileOption(Enum):
        """
        Members Include: <Append> <Replace>
        """
        Append: int
        Replace: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FieldTable.LoadFileOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Options for structured table data
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Regular</term><description> 
    ## </description> </item><item><term> 
    ## Strict</term><description> 
    ## </description> </item></list>
    class StructDataTableType(Enum):
        """
        Members Include: <Regular> <Strict>
        """
        Regular: int
        Strict: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FieldTable.StructDataTableType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) AnnTolerance
    ##  Returns
    ##         the approximate nearest neighbor (ANN) interpolation tolerance 
    ##           
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return float
    @property
    def AnnTolerance(self) -> float:
        """
        Getter for property: (float) AnnTolerance
         Returns
                the approximate nearest neighbor (ANN) interpolation tolerance 
                  
            
         
        """
        pass
    
    ## Setter for property: (float) AnnTolerance

    ##  Returns
    ##         the approximate nearest neighbor (ANN) interpolation tolerance 
    ##           
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @AnnTolerance.setter
    def AnnTolerance(self, ann_tolerance: float):
        """
        Setter for property: (float) AnnTolerance
         Returns
                the approximate nearest neighbor (ANN) interpolation tolerance 
                  
            
         
        """
        pass
    
    ## Getter for property: (bool) CreateInterpolatorOnCommit
    ##  Returns 
    ##         a flag specifying if interpolator needs to be created on commit
    ##           
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def CreateInterpolatorOnCommit(self) -> bool:
        """
        Getter for property: (bool) CreateInterpolatorOnCommit
         Returns 
                a flag specifying if interpolator needs to be created on commit
                  
            
         
        """
        pass
    
    ## Setter for property: (bool) CreateInterpolatorOnCommit

    ##  Returns 
    ##         a flag specifying if interpolator needs to be created on commit
    ##           
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @CreateInterpolatorOnCommit.setter
    def CreateInterpolatorOnCommit(self, shouldCreateInterpolOnCommit: bool):
        """
        Setter for property: (bool) CreateInterpolatorOnCommit
         Returns 
                a flag specifying if interpolator needs to be created on commit
                  
            
         
        """
        pass
    
    ## Getter for property: (bool) DelaunayDeleteSlivers
    ##  Returns the option to delete sliver triangles from the resulting 2D Delaunay interpolation mesh.  
    ##     Applies to Delaunay interpolation only.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def DelaunayDeleteSlivers(self) -> bool:
        """
        Getter for property: (bool) DelaunayDeleteSlivers
         Returns the option to delete sliver triangles from the resulting 2D Delaunay interpolation mesh.  
            Applies to Delaunay interpolation only.   
         
        """
        pass
    
    ## Setter for property: (bool) DelaunayDeleteSlivers

    ##  Returns the option to delete sliver triangles from the resulting 2D Delaunay interpolation mesh.  
    ##     Applies to Delaunay interpolation only.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @DelaunayDeleteSlivers.setter
    def DelaunayDeleteSlivers(self, delaunayDeleteSlivers: bool):
        """
        Setter for property: (bool) DelaunayDeleteSlivers
         Returns the option to delete sliver triangles from the resulting 2D Delaunay interpolation mesh.  
            Applies to Delaunay interpolation only.   
         
        """
        pass
    
    ## Getter for property: (float) DelaunayRatioTolerance
    ##  Returns the option for ratio tolerance.  
    ##    Edge Length Tolerance > 1-edgelength(0)/(edgelength(1)+edgelength(2)). Aspect Ratio Tolerance > (height from free edge to opposite vertex)/(length of free edge). Applies to Delaunay interpolation only.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def DelaunayRatioTolerance(self) -> float:
        """
        Getter for property: (float) DelaunayRatioTolerance
         Returns the option for ratio tolerance.  
           Edge Length Tolerance > 1-edgelength(0)/(edgelength(1)+edgelength(2)). Aspect Ratio Tolerance > (height from free edge to opposite vertex)/(length of free edge). Applies to Delaunay interpolation only.   
         
        """
        pass
    
    ## Setter for property: (float) DelaunayRatioTolerance

    ##  Returns the option for ratio tolerance.  
    ##    Edge Length Tolerance > 1-edgelength(0)/(edgelength(1)+edgelength(2)). Aspect Ratio Tolerance > (height from free edge to opposite vertex)/(length of free edge). Applies to Delaunay interpolation only.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @DelaunayRatioTolerance.setter
    def DelaunayRatioTolerance(self, delaunayRatioTolerance: float):
        """
        Setter for property: (float) DelaunayRatioTolerance
         Returns the option for ratio tolerance.  
           Edge Length Tolerance > 1-edgelength(0)/(edgelength(1)+edgelength(2)). Aspect Ratio Tolerance > (height from free edge to opposite vertex)/(length of free edge). Applies to Delaunay interpolation only.   
         
        """
        pass
    
    ## Getter for property: (@link FieldEvaluator.DelaunaySliverDetectionMethodEnum NXOpen.Fields.FieldEvaluator.DelaunaySliverDetectionMethodEnum@endlink) DelaunaySliverDetectionMethod
    ##  Returns the option specifyng the method used to determine if a triangle is a sliver of the 2D Delaunay interpolation mesh.  
    ##     Applies to Delaunay interpolation only.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return FieldEvaluator.DelaunaySliverDetectionMethodEnum
    @property
    def DelaunaySliverDetectionMethod(self) -> FieldEvaluator.DelaunaySliverDetectionMethodEnum:
        """
        Getter for property: (@link FieldEvaluator.DelaunaySliverDetectionMethodEnum NXOpen.Fields.FieldEvaluator.DelaunaySliverDetectionMethodEnum@endlink) DelaunaySliverDetectionMethod
         Returns the option specifyng the method used to determine if a triangle is a sliver of the 2D Delaunay interpolation mesh.  
            Applies to Delaunay interpolation only.   
         
        """
        pass
    
    ## Setter for property: (@link FieldEvaluator.DelaunaySliverDetectionMethodEnum NXOpen.Fields.FieldEvaluator.DelaunaySliverDetectionMethodEnum@endlink) DelaunaySliverDetectionMethod

    ##  Returns the option specifyng the method used to determine if a triangle is a sliver of the 2D Delaunay interpolation mesh.  
    ##     Applies to Delaunay interpolation only.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @DelaunaySliverDetectionMethod.setter
    def DelaunaySliverDetectionMethod(self, delaunaySliverDetectionMethod: FieldEvaluator.DelaunaySliverDetectionMethodEnum):
        """
        Setter for property: (@link FieldEvaluator.DelaunaySliverDetectionMethodEnum NXOpen.Fields.FieldEvaluator.DelaunaySliverDetectionMethodEnum@endlink) DelaunaySliverDetectionMethod
         Returns the option specifyng the method used to determine if a triangle is a sliver of the 2D Delaunay interpolation mesh.  
            Applies to Delaunay interpolation only.   
         
        """
        pass
    
    ## Getter for property: (bool) DelaunaySnapVertices
    ##  Returns the option to snap vertices from deleted sliver triangles to the convex hull of the 2D Delaunay interpolation mesh.  
    ##     Applies to Delaunay interpolation only.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def DelaunaySnapVertices(self) -> bool:
        """
        Getter for property: (bool) DelaunaySnapVertices
         Returns the option to snap vertices from deleted sliver triangles to the convex hull of the 2D Delaunay interpolation mesh.  
            Applies to Delaunay interpolation only.   
         
        """
        pass
    
    ## Setter for property: (bool) DelaunaySnapVertices

    ##  Returns the option to snap vertices from deleted sliver triangles to the convex hull of the 2D Delaunay interpolation mesh.  
    ##     Applies to Delaunay interpolation only.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @DelaunaySnapVertices.setter
    def DelaunaySnapVertices(self, delaunaySnapVertices: bool):
        """
        Setter for property: (bool) DelaunaySnapVertices
         Returns the option to snap vertices from deleted sliver triangles to the convex hull of the 2D Delaunay interpolation mesh.  
            Applies to Delaunay interpolation only.   
         
        """
        pass
    
    ## Getter for property: (bool) DelayedUpdate
    ##  Returns the delayed update flag on the table is returned  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def DelayedUpdate(self) -> bool:
        """
        Getter for property: (bool) DelayedUpdate
         Returns the delayed update flag on the table is returned  
            
         
        """
        pass
    
    ## Setter for property: (bool) DelayedUpdate

    ##  Returns the delayed update flag on the table is returned  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DelayedUpdate.setter
    def DelayedUpdate(self, delayedUpdate: bool):
        """
        Setter for property: (bool) DelayedUpdate
         Returns the delayed update flag on the table is returned  
            
         
        """
        pass
    
    ## Getter for property: (bool) Discontinuities
    ##  Returns a flag specifying if the table has discontinuites   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def Discontinuities(self) -> bool:
        """
        Getter for property: (bool) Discontinuities
         Returns a flag specifying if the table has discontinuites   
            
         
        """
        pass
    
    ## Getter for property: (@link FieldTable.DuplicateValueOption NXOpen.Fields.FieldTable.DuplicateValueOption@endlink) DuplicateValueProcessingOption
    ##  Returns the duplicate value processing option for field independent variable values, the zero value represents no option used/selected   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return FieldTable.DuplicateValueOption
    @property
    def DuplicateValueProcessingOption(self) -> FieldTable.DuplicateValueOption:
        """
        Getter for property: (@link FieldTable.DuplicateValueOption NXOpen.Fields.FieldTable.DuplicateValueOption@endlink) DuplicateValueProcessingOption
         Returns the duplicate value processing option for field independent variable values, the zero value represents no option used/selected   
            
         
        """
        pass
    
    ## Setter for property: (@link FieldTable.DuplicateValueOption NXOpen.Fields.FieldTable.DuplicateValueOption@endlink) DuplicateValueProcessingOption

    ##  Returns the duplicate value processing option for field independent variable values, the zero value represents no option used/selected   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @DuplicateValueProcessingOption.setter
    def DuplicateValueProcessingOption(self, optionIndex: FieldTable.DuplicateValueOption):
        """
        Setter for property: (@link FieldTable.DuplicateValueOption NXOpen.Fields.FieldTable.DuplicateValueOption@endlink) DuplicateValueProcessingOption
         Returns the duplicate value processing option for field independent variable values, the zero value represents no option used/selected   
            
         
        """
        pass
    
    ## Getter for property: (bool) FallbackToDefaultInterpolator
    ##  Returns 
    ##         a flag specifying if interpolator can fallback to a default interpolator, 
    ##         if the creation of the given interpolator fails
    ##           
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def FallbackToDefaultInterpolator(self) -> bool:
        """
        Getter for property: (bool) FallbackToDefaultInterpolator
         Returns 
                a flag specifying if interpolator can fallback to a default interpolator, 
                if the creation of the given interpolator fails
                  
            
         
        """
        pass
    
    ## Setter for property: (bool) FallbackToDefaultInterpolator

    ##  Returns 
    ##         a flag specifying if interpolator can fallback to a default interpolator, 
    ##         if the creation of the given interpolator fails
    ##           
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @FallbackToDefaultInterpolator.setter
    def FallbackToDefaultInterpolator(self, shouldFallbackToDefaultInterpolator: bool):
        """
        Setter for property: (bool) FallbackToDefaultInterpolator
         Returns 
                a flag specifying if interpolator can fallback to a default interpolator, 
                if the creation of the given interpolator fails
                  
            
         
        """
        pass
    
    ## Getter for property: (float) IndependentValueDivisor
    ##  Returns the linear interpolation divisor for field independent value, the zero value represents no divisor used   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def IndependentValueDivisor(self) -> float:
        """
        Getter for property: (float) IndependentValueDivisor
         Returns the linear interpolation divisor for field independent value, the zero value represents no divisor used   
            
         
        """
        pass
    
    ## Setter for property: (float) IndependentValueDivisor

    ##  Returns the linear interpolation divisor for field independent value, the zero value represents no divisor used   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @IndependentValueDivisor.setter
    def IndependentValueDivisor(self, divisor: float):
        """
        Setter for property: (float) IndependentValueDivisor
         Returns the linear interpolation divisor for field independent value, the zero value represents no divisor used   
            
         
        """
        pass
    
    ## Getter for property: (bool) IndependentValueDivisorOption
    ##  Returns a value indicating whether to set the linear interpolation divisor for field independent value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def IndependentValueDivisorOption(self) -> bool:
        """
        Getter for property: (bool) IndependentValueDivisorOption
         Returns a value indicating whether to set the linear interpolation divisor for field independent value   
            
         
        """
        pass
    
    ## Setter for property: (bool) IndependentValueDivisorOption

    ##  Returns a value indicating whether to set the linear interpolation divisor for field independent value   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @IndependentValueDivisorOption.setter
    def IndependentValueDivisorOption(self, divisor_option: bool):
        """
        Setter for property: (bool) IndependentValueDivisorOption
         Returns a value indicating whether to set the linear interpolation divisor for field independent value   
            
         
        """
        pass
    
    ## Getter for property: (float) IndependentValueShift
    ##  Returns the linear interpolation shift for field independent value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def IndependentValueShift(self) -> float:
        """
        Getter for property: (float) IndependentValueShift
         Returns the linear interpolation shift for field independent value   
            
         
        """
        pass
    
    ## Setter for property: (float) IndependentValueShift

    ##  Returns the linear interpolation shift for field independent value   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @IndependentValueShift.setter
    def IndependentValueShift(self, shift: float):
        """
        Setter for property: (float) IndependentValueShift
         Returns the linear interpolation shift for field independent value   
            
         
        """
        pass
    
    ## Getter for property: (bool) IndependentValueShiftOption
    ##  Returns a value indicating whether to set the linear interpolation shift for field independent value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def IndependentValueShiftOption(self) -> bool:
        """
        Getter for property: (bool) IndependentValueShiftOption
         Returns a value indicating whether to set the linear interpolation shift for field independent value   
            
         
        """
        pass
    
    ## Setter for property: (bool) IndependentValueShiftOption

    ##  Returns a value indicating whether to set the linear interpolation shift for field independent value   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @IndependentValueShiftOption.setter
    def IndependentValueShiftOption(self, shift_option: bool):
        """
        Setter for property: (bool) IndependentValueShiftOption
         Returns a value indicating whether to set the linear interpolation shift for field independent value   
            
         
        """
        pass
    
    ## Getter for property: (@link FieldEvaluator.InterpolationEnum NXOpen.Fields.FieldEvaluator.InterpolationEnum@endlink) InterpolationMethod
    ##  Returns  
    ##         the interpolation method used when this table data is evaluated.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.2  <br> 

    ## @return FieldEvaluator.InterpolationEnum
    @property
    def InterpolationMethod(self) -> FieldEvaluator.InterpolationEnum:
        """
        Getter for property: (@link FieldEvaluator.InterpolationEnum NXOpen.Fields.FieldEvaluator.InterpolationEnum@endlink) InterpolationMethod
         Returns  
                the interpolation method used when this table data is evaluated.  
          
                  
         
        """
        pass
    
    ## Setter for property: (@link FieldEvaluator.InterpolationEnum NXOpen.Fields.FieldEvaluator.InterpolationEnum@endlink) InterpolationMethod

    ##  Returns  
    ##         the interpolation method used when this table data is evaluated.  
    ##   
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.2  <br> 

    @InterpolationMethod.setter
    def InterpolationMethod(self, interpolation_method: FieldEvaluator.InterpolationEnum):
        """
        Setter for property: (@link FieldEvaluator.InterpolationEnum NXOpen.Fields.FieldEvaluator.InterpolationEnum@endlink) InterpolationMethod
         Returns  
                the interpolation method used when this table data is evaluated.  
          
                  
         
        """
        pass
    
    ## Getter for property: (@link FieldEvaluator.LinearLogOptionEnum NXOpen.Fields.FieldEvaluator.LinearLogOptionEnum@endlink) LinearLogOption
    ##  Returns  
    ##         the linear/log option used when this table data is evaluated using the linear 1d interpolator.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return FieldEvaluator.LinearLogOptionEnum
    @property
    def LinearLogOption(self) -> FieldEvaluator.LinearLogOptionEnum:
        """
        Getter for property: (@link FieldEvaluator.LinearLogOptionEnum NXOpen.Fields.FieldEvaluator.LinearLogOptionEnum@endlink) LinearLogOption
         Returns  
                the linear/log option used when this table data is evaluated using the linear 1d interpolator.  
          
                  
         
        """
        pass
    
    ## Setter for property: (@link FieldEvaluator.LinearLogOptionEnum NXOpen.Fields.FieldEvaluator.LinearLogOptionEnum@endlink) LinearLogOption

    ##  Returns  
    ##         the linear/log option used when this table data is evaluated using the linear 1d interpolator.  
    ##   
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @LinearLogOption.setter
    def LinearLogOption(self, linear_option: FieldEvaluator.LinearLogOptionEnum):
        """
        Setter for property: (@link FieldEvaluator.LinearLogOptionEnum NXOpen.Fields.FieldEvaluator.LinearLogOptionEnum@endlink) LinearLogOption
         Returns  
                the linear/log option used when this table data is evaluated using the linear 1d interpolator.  
          
                  
         
        """
        pass
    
    ## Getter for property: (bool) ParameterizeIndependentDomain
    ##  Returns the Parameterize Independent Domain option for Table field - toggle switch  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def ParameterizeIndependentDomain(self) -> bool:
        """
        Getter for property: (bool) ParameterizeIndependentDomain
         Returns the Parameterize Independent Domain option for Table field - toggle switch  
            
         
        """
        pass
    
    ## Setter for property: (bool) ParameterizeIndependentDomain

    ##  Returns the Parameterize Independent Domain option for Table field - toggle switch  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ParameterizeIndependentDomain.setter
    def ParameterizeIndependentDomain(self, parameterizeIndependentDomain: bool):
        """
        Setter for property: (bool) ParameterizeIndependentDomain
         Returns the Parameterize Independent Domain option for Table field - toggle switch  
            
         
        """
        pass
    
    ## Getter for property: (bool) PersistentInterpolator
    ##  Returns 
    ##         a flag specifying if interpolator is persistent between session 
    ##           
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def PersistentInterpolator(self) -> bool:
        """
        Getter for property: (bool) PersistentInterpolator
         Returns 
                a flag specifying if interpolator is persistent between session 
                  
            
         
        """
        pass
    
    ## Setter for property: (bool) PersistentInterpolator

    ##  Returns 
    ##         a flag specifying if interpolator is persistent between session 
    ##           
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @PersistentInterpolator.setter
    def PersistentInterpolator(self, persistentInterpolator: bool):
        """
        Setter for property: (bool) PersistentInterpolator
         Returns 
                a flag specifying if interpolator is persistent between session 
                  
            
         
        """
        pass
    
    ## Getter for property: (@link FieldEvaluator.SplineDegreeOptionEnum NXOpen.Fields.FieldEvaluator.SplineDegreeOptionEnum@endlink) SplineDegreeOption
    ##  Returns  
    ##         the degree option used when this table data is evaluated using the spline 1d interpolator.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return FieldEvaluator.SplineDegreeOptionEnum
    @property
    def SplineDegreeOption(self) -> FieldEvaluator.SplineDegreeOptionEnum:
        """
        Getter for property: (@link FieldEvaluator.SplineDegreeOptionEnum NXOpen.Fields.FieldEvaluator.SplineDegreeOptionEnum@endlink) SplineDegreeOption
         Returns  
                the degree option used when this table data is evaluated using the spline 1d interpolator.  
          
                  
         
        """
        pass
    
    ## Setter for property: (@link FieldEvaluator.SplineDegreeOptionEnum NXOpen.Fields.FieldEvaluator.SplineDegreeOptionEnum@endlink) SplineDegreeOption

    ##  Returns  
    ##         the degree option used when this table data is evaluated using the spline 1d interpolator.  
    ##   
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @SplineDegreeOption.setter
    def SplineDegreeOption(self, degree_option: FieldEvaluator.SplineDegreeOptionEnum):
        """
        Setter for property: (@link FieldEvaluator.SplineDegreeOptionEnum NXOpen.Fields.FieldEvaluator.SplineDegreeOptionEnum@endlink) SplineDegreeOption
         Returns  
                the degree option used when this table data is evaluated using the spline 1d interpolator.  
          
                  
         
        """
        pass
    
    ## Getter for property: (float) ValuesOutsideHighTableUserdefinedValue
    ##  Returns the user defined value to return when the lookup value is greater than the highest value for the independent variable.  
    ##     For 1-D independent domains only; 2-D and higher domains, this value is not used and will error out if accessed.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return float
    @property
    def ValuesOutsideHighTableUserdefinedValue(self) -> float:
        """
        Getter for property: (float) ValuesOutsideHighTableUserdefinedValue
         Returns the user defined value to return when the lookup value is greater than the highest value for the independent variable.  
            For 1-D independent domains only; 2-D and higher domains, this value is not used and will error out if accessed.   
         
        """
        pass
    
    ## Setter for property: (float) ValuesOutsideHighTableUserdefinedValue

    ##  Returns the user defined value to return when the lookup value is greater than the highest value for the independent variable.  
    ##     For 1-D independent domains only; 2-D and higher domains, this value is not used and will error out if accessed.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @ValuesOutsideHighTableUserdefinedValue.setter
    def ValuesOutsideHighTableUserdefinedValue(self, userDefinedValueHi: float):
        """
        Setter for property: (float) ValuesOutsideHighTableUserdefinedValue
         Returns the user defined value to return when the lookup value is greater than the highest value for the independent variable.  
            For 1-D independent domains only; 2-D and higher domains, this value is not used and will error out if accessed.   
         
        """
        pass
    
    ## Getter for property: (@link FieldEvaluator.ValuesOutsideTableInterpolationEnum NXOpen.Fields.FieldEvaluator.ValuesOutsideTableInterpolationEnum@endlink) ValuesOutsideTableInterpolation
    ##  Returns the outside table values interpolation method for standard linear interpolation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return FieldEvaluator.ValuesOutsideTableInterpolationEnum
    @property
    def ValuesOutsideTableInterpolation(self) -> FieldEvaluator.ValuesOutsideTableInterpolationEnum:
        """
        Getter for property: (@link FieldEvaluator.ValuesOutsideTableInterpolationEnum NXOpen.Fields.FieldEvaluator.ValuesOutsideTableInterpolationEnum@endlink) ValuesOutsideTableInterpolation
         Returns the outside table values interpolation method for standard linear interpolation   
            
         
        """
        pass
    
    ## Setter for property: (@link FieldEvaluator.ValuesOutsideTableInterpolationEnum NXOpen.Fields.FieldEvaluator.ValuesOutsideTableInterpolationEnum@endlink) ValuesOutsideTableInterpolation

    ##  Returns the outside table values interpolation method for standard linear interpolation   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ValuesOutsideTableInterpolation.setter
    def ValuesOutsideTableInterpolation(self, interpolationMethod: FieldEvaluator.ValuesOutsideTableInterpolationEnum):
        """
        Setter for property: (@link FieldEvaluator.ValuesOutsideTableInterpolationEnum NXOpen.Fields.FieldEvaluator.ValuesOutsideTableInterpolationEnum@endlink) ValuesOutsideTableInterpolation
         Returns the outside table values interpolation method for standard linear interpolation   
            
         
        """
        pass
    
    ## Getter for property: (float) ValuesOutsideTableUserdefinedValue
    ##  Returns the user defined value to return when lookup value is outside.  
    ##    For 1-D domains, this is the value to return when the the lookup value is below the minimum value.  For 2-D and higher domains, this is the only value that can be specified.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return float
    @property
    def ValuesOutsideTableUserdefinedValue(self) -> float:
        """
        Getter for property: (float) ValuesOutsideTableUserdefinedValue
         Returns the user defined value to return when lookup value is outside.  
           For 1-D domains, this is the value to return when the the lookup value is below the minimum value.  For 2-D and higher domains, this is the only value that can be specified.   
         
        """
        pass
    
    ## Setter for property: (float) ValuesOutsideTableUserdefinedValue

    ##  Returns the user defined value to return when lookup value is outside.  
    ##    For 1-D domains, this is the value to return when the the lookup value is below the minimum value.  For 2-D and higher domains, this is the only value that can be specified.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @ValuesOutsideTableUserdefinedValue.setter
    def ValuesOutsideTableUserdefinedValue(self, userDefinedValue: float):
        """
        Setter for property: (float) ValuesOutsideTableUserdefinedValue
         Returns the user defined value to return when lookup value is outside.  
           For 1-D domains, this is the value to return when the the lookup value is below the minimum value.  For 2-D and higher domains, this is the only value that can be specified.   
         
        """
        pass
    
    ##  Create an interpolator 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    def CreateInterpolator(self) -> None:
        """
         Create an interpolator 
        """
        pass
    
    ##  Delete structure data 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    def DeleteStructureData(self) -> None:
        """
         Delete structure data 
        """
        pass
    
    ##  Created a DbScaling object and returns true if successful 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="db_scale_factor"> (float)  db scale factor                                            </param>
    ## <param name="db_ref_value"> (float)  db ref value                                               </param>
    ## <param name="is_db_scaling"> (bool)  db_scaling_object is created if true and if it doesnt exit </param>
    def EditDbScaling(self, db_scale_factor: float, db_ref_value: float, is_db_scaling: bool) -> None:
        """
         Created a DbScaling object and returns true if successful 
        """
        pass
    
    ##  Edit the table field.  Specifies the new array of @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink s for 
    ##         independent and dependent variables, as well as the new double values.
    ##         
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="indep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  independent variables to be associated with the field </param>
    ## <param name="dep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  dependent expression fields to be associated with the formula field </param>
    ## <param name="datapoints"> (List[float])  row based array of double values representing the table; then number of points should equal the number of independent variables * the number of dependent variables * the number of rows. </param>
    def EditFieldTable(self, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable], datapoints: List[float]) -> None:
        """
         Edit the table field.  Specifies the new array of @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink s for 
                independent and dependent variables, as well as the new double values.
                
        """
        pass
    
    ##  Edit the table field complex display.  Specifies the new array of complex display flags for 
    ##         independent and dependent variables.
    ##         
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="indep_var_array_complex_display"> (List[bool])  independent variable complex display flags to be associated with the field </param>
    ## <param name="dep_var_array_complex_display"> (List[bool])  dependent variable complex display flags to be associated with the field </param>
    def EditFieldTableComplexDisplay(self, indep_var_array_complex_display: List[bool], dep_var_array_complex_display: List[bool]) -> None:
        """
         Edit the table field complex display.  Specifies the new array of complex display flags for 
                independent and dependent variables.
                
        """
        pass
    
    ##  Edit the table field complex units array.  
    ##             Specifies the new array of complex phase unit tags for dependent variables.  
    ##             A NULL unit in a given index indicates that the corresponding variable is not complex, or if it is complex, that the value
    ##             is Real/Imaginary, in which both components have the same unit as the variable itself.  
    ##             In the case where the unit is specified, the complex dep variables in magnitude/phase representation.  
    ##             In that case the measure of the specified unit must be angle. 
    ##         
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="dep_var_array_complex_units"> (@link NXOpen.Unit List[NXOpen.Unit]@endlink) </param>
    def EditFieldTableComplexUnits(self, dep_var_array_complex_units: List[NXOpen.Unit]) -> None:
        """
         Edit the table field complex units array.  
                    Specifies the new array of complex phase unit tags for dependent variables.  
                    A NULL unit in a given index indicates that the corresponding variable is not complex, or if it is complex, that the value
                    is Real/Imaginary, in which both components have the same unit as the variable itself.  
                    In the case where the unit is specified, the complex dep variables in magnitude/phase representation.  
                    In that case the measure of the specified unit must be angle. 
                
        """
        pass
    
    ##  Edit the table field with expressions. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## <param name="field_table"> (@link FieldTable NXOpen.Fields.FieldTable@endlink) </param>
    ## <param name="indep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  independent variables to be associated with the field </param>
    ## <param name="dep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  dependent expression fields to be associated with the formula field </param>
    ## <param name="datapoints"> (List[float])  row based array of double values representing the table </param>
    ## <param name="exp_cell_ids"> (List[int])  0 array of expression strings associated to specified cells </param>
    ## <param name="value_strings"> (List[str])  array of num_exp_strings associated to table cells </param>
    @overload
    def EditFieldTableWithExpressions(self, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable], datapoints: List[float], exp_cell_ids: List[int], value_strings: List[str]) -> None:
        """
         Edit the table field with expressions. 
        """
        pass
    
    ##  Edit the table field with expressions. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## <param name="field_table"> (@link FieldTable NXOpen.Fields.FieldTable@endlink) </param>
    ## <param name="indep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  independent variables to be associated with the field </param>
    ## <param name="dep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  dependent expression fields to be associated with the formula field </param>
    ## <param name="datapoints"> (List[float])  row based array of double values representing the table </param>
    ## <param name="exp_cell_ids"> (List[int])  0 array of expression strings associated to specified cells </param>
    ## <param name="value_strings"> (List[str])  array of num_exp_strings associated to table cells </param>
    ## <param name="cellReadOnlys"> (List[bool]) </param>
    @overload
    def EditFieldTableWithExpressions(self, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable], datapoints: List[float], exp_cell_ids: List[int], value_strings: List[str], cellReadOnlys: List[bool]) -> None:
        """
         Edit the table field with expressions. 
        """
        pass
    
    ##  Edit the table field with point objects. 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="indep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  independent variables to be associated with the field </param>
    ## <param name="dep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  dependent expression fields to be associated with the formula field </param>
    ## <param name="datapoints"> (List[float])  row based array of double values representing the table; then number of points should equal the number of independent variables * the number of dependent variables * the number of rows. </param>
    ## <param name="point_object_row_ids"> (List[int])  0 based row ID of rows that have associated point objects </param>
    ## <param name="point_objects"> (@link NXOpen.Point List[NXOpen.Point]@endlink)  array of num_point_objects point objects to be associated to rows </param>
    def EditFieldTableWithPoints(self, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable], datapoints: List[float], point_object_row_ids: List[int], point_objects: List[NXOpen.Point]) -> None:
        """
         Edit the table field with point objects. 
        """
        pass
    
    ##  Edit the lattice table data.  Specifies lattice type,num of lattice rows,columns and planes.
    ##         
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="lattice_type"> (@link FieldTable.StructDataTableType NXOpen.Fields.FieldTable.StructDataTableType@endlink) </param>
    ## <param name="num_lattice_rows"> (int) </param>
    ## <param name="num_lattice_columns"> (int) </param>
    ## <param name="num_lattice_planes"> (int) </param>
    def EditTableLatticeData(self, lattice_type: FieldTable.StructDataTableType, num_lattice_rows: int, num_lattice_columns: int, num_lattice_planes: int) -> None:
        """
         Edit the lattice table data.  Specifies lattice type,num of lattice rows,columns and planes.
                
        """
        pass
    
    ##  Edit the table field dependent variables.  Specifies the new dependent @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink 
    ##         array.  If retain number of rows is specified, the total number of rows will remain the same.  Columns with zeros will be added 
    ##         as necessary, or data will be truncated.  This process will be handled for each set of variables, independent and dependent.
    ##         Thus, if the number of independent columns increases and the dependent columns decrease, a column of zeros will be added for the
    ##         new independent variable, and data will be dropped from the dependent values.
    ##         
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="indep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  independent variables to be associated with the field </param>
    ## <param name="dep_exp_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink)  dependent field variables to be associated with the field </param>
    def EditTableVariables(self, indep_var_array: List[FieldVariable], dep_exp_array: List[FieldVariable]) -> None:
        """
         Edit the table field dependent variables.  Specifies the new dependent @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink 
                array.  If retain number of rows is specified, the total number of rows will remain the same.  Columns with zeros will be added 
                as necessary, or data will be truncated.  This process will be handled for each set of variables, independent and dependent.
                Thus, if the number of independent columns increases and the dependent columns decrease, a column of zeros will be added for the
                new independent variable, and data will be dropped from the dependent values.
                
        """
        pass
    
    ##  Returns the values for the given @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink  in this @link NXOpen::Fields::FieldTable NXOpen::Fields::FieldTable@endlink .  
    ##             The input @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink  should be retrieved from the field using 
    ##             @link NXOpen::Fields::Field::GetIndependentVariables NXOpen::Fields::Field::GetIndependentVariables@endlink  or @link NXOpen::Fields::Field::GetDependentVariables NXOpen::Fields::Field::GetDependentVariables@endlink . 
    ##             The values are in the same @link NXOpen::Unit NXOpen::Unit@endlink  as specified on the @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink .
    ##         
    ##  @return values (List[float]):  the row values for this variable .
    ## 
    ##   <br>  Created in NX7.5.4  <br> 

    ## License requirements: None.
    ## 
    ## <param name="variable"> (@link FieldVariable NXOpen.Fields.FieldVariable@endlink)  variable whose table values are to be returned </param>
    def GetData(self, variable: FieldVariable) -> List[float]:
        """
         Returns the values for the given @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink  in this @link NXOpen::Fields::FieldTable NXOpen::Fields::FieldTable@endlink .  
                    The input @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink  should be retrieved from the field using 
                    @link NXOpen::Fields::Field::GetIndependentVariables NXOpen::Fields::Field::GetIndependentVariables@endlink  or @link NXOpen::Fields::Field::GetDependentVariables NXOpen::Fields::Field::GetDependentVariables@endlink . 
                    The values are in the same @link NXOpen::Unit NXOpen::Unit@endlink  as specified on the @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink .
                
         @return values (List[float]):  the row values for this variable .
        """
        pass
    
    ##  Get the inverse distance weighting (IDW) interpolation options 
    ##  @return A tuple consisting of (nearest_option, nearest_fraction, maximum_radius, number_of_points, power_of_distance). 
    ##  - nearest_option is: @link FieldEvaluator.InverseDistanceWeightingEnum NXOpen.Fields.FieldEvaluator.InverseDistanceWeightingEnum@endlink. nearest option   .
    ##  - nearest_fraction is: float. fraction         .
    ##  - maximum_radius is: float. maximum radius .
    ##  - number_of_points is: int. number of points .
    ##  - power_of_distance is: @link FieldEvaluator.InverseDistanceWeightingPowerOfDistanceEnum NXOpen.Fields.FieldEvaluator.InverseDistanceWeightingPowerOfDistanceEnum@endlink.

    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    def GetIdwOptions(self) -> Tuple[FieldEvaluator.InverseDistanceWeightingEnum, float, float, int, FieldEvaluator.InverseDistanceWeightingPowerOfDistanceEnum]:
        """
         Get the inverse distance weighting (IDW) interpolation options 
         @return A tuple consisting of (nearest_option, nearest_fraction, maximum_radius, number_of_points, power_of_distance). 
         - nearest_option is: @link FieldEvaluator.InverseDistanceWeightingEnum NXOpen.Fields.FieldEvaluator.InverseDistanceWeightingEnum@endlink. nearest option   .
         - nearest_fraction is: float. fraction         .
         - maximum_radius is: float. maximum radius .
         - number_of_points is: int. number of points .
         - power_of_distance is: @link FieldEvaluator.InverseDistanceWeightingPowerOfDistanceEnum NXOpen.Fields.FieldEvaluator.InverseDistanceWeightingPowerOfDistanceEnum@endlink.

        """
        pass
    
    ##  Get point objects associated with table rows. 
    ##  @return A tuple consisting of (point_object_row_ids, point_objects). 
    ##  - point_object_row_ids is: List[int]. 0 based row ID of rows that have associated point objects, in ascending order .
    ##  - point_objects is: @link NXOpen.Point List[NXOpen.Point]@endlink. array of num_point_objects point objects associated to rows .

    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    def GetTablePoints(self) -> Tuple[List[int], List[NXOpen.Point]]:
        """
         Get point objects associated with table rows. 
         @return A tuple consisting of (point_object_row_ids, point_objects). 
         - point_object_row_ids is: List[int]. 0 based row ID of rows that have associated point objects, in ascending order .
         - point_objects is: @link NXOpen.Point List[NXOpen.Point]@endlink. array of num_point_objects point objects associated to rows .

        """
        pass
    
    ##  Get the offset value for the variable 
    ##  @return offset (@link NXOpen.Expression NXOpen.Expression@endlink):  the offset for the variable .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="varType"> (@link FieldVariable.Type NXOpen.Fields.FieldVariable.Type@endlink) </param>
    def GetVariableOffset(self, varType: FieldVariable.Type) -> NXOpen.Expression:
        """
         Get the offset value for the variable 
         @return offset (@link NXOpen.Expression NXOpen.Expression@endlink):  the offset for the variable .
        """
        pass
    
    ##  Get the scale factor for the variable 
    ##  @return scaleFactor (@link NXOpen.Expression NXOpen.Expression@endlink):  the scale factor for the variable .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="varType"> (@link FieldVariable.Type NXOpen.Fields.FieldVariable.Type@endlink) </param>
    def GetVariableScaleFactor(self, varType: FieldVariable.Type) -> NXOpen.Expression:
        """
         Get the scale factor for the variable 
         @return scaleFactor (@link NXOpen.Expression NXOpen.Expression@endlink):  the scale factor for the variable .
        """
        pass
    
    ##  Populate the table from a file replacing or appending data 
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="filename"> (str)  file to read rows from </param>
    ## <param name="load_file_option"> (@link FieldTable.LoadFileOption NXOpen.Fields.FieldTable.LoadFileOption@endlink)  append or replace </param>
    def LoadFromFile(self, filename: str, load_file_option: FieldTable.LoadFileOption) -> None:
        """
         Populate the table from a file replacing or appending data 
        """
        pass
    
    ##  Process pending update 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    def ProcessPendingUpdate(self) -> None:
        """
         Process pending update 
        """
        pass
    
    ##  Set the conservative interpolation options 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2206.0.0.  Use @link NXOpen::Fields::FieldTable::SetConservativeOptionsWithUnits NXOpen::Fields::FieldTable::SetConservativeOptionsWithUnits@endlink  call  <br> 

    ## License requirements: None.
    ## 
    ## <param name="ann_tolerance"> (float)  approximate nearest neighbor (ANN) interpolation tolerance </param>
    ## <param name="maximum_radius"> (float)  maximum radius   </param>
    ## <param name="number_of_points"> (int)  number of points </param>
    def SetConservativeOptions(self, ann_tolerance: float, maximum_radius: float, number_of_points: int) -> None:
        """
         Set the conservative interpolation options 
        """
        pass
    
    ##  Set the conservative interpolation options 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="ann_tolerance"> (float)  approximate nearest neighbor (ANN) interpolation tolerance </param>
    ## <param name="maximum_radius"> (float)  maximum radius   </param>
    ## <param name="maximum_radius_unit"> (@link NXOpen.Unit NXOpen.Unit@endlink)  maximum radius unit </param>
    ## <param name="number_of_points"> (int)  number of points </param>
    def SetConservativeOptionsWithUnits(self, ann_tolerance: float, maximum_radius: float, maximum_radius_unit: NXOpen.Unit, number_of_points: int) -> None:
        """
         Set the conservative interpolation options 
        """
        pass
    
    ##  Set the inverse distance weighting (IDW) interpolation options 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2206.0.0.  Use @link NXOpen::Fields::FieldTable::SetIdwOptionsWithUnits NXOpen::Fields::FieldTable::SetIdwOptionsWithUnits@endlink  call  <br> 

    ## License requirements: None.
    ## 
    ## <param name="nearest_option"> (@link FieldEvaluator.InverseDistanceWeightingEnum NXOpen.Fields.FieldEvaluator.InverseDistanceWeightingEnum@endlink)  nearest option   </param>
    ## <param name="nearest_fraction"> (float)  fraction         </param>
    ## <param name="maximum_radius"> (float)  maximum radius   </param>
    ## <param name="number_of_points"> (int)  number of points </param>
    ## <param name="power_of_distance"> (@link FieldEvaluator.InverseDistanceWeightingPowerOfDistanceEnum NXOpen.Fields.FieldEvaluator.InverseDistanceWeightingPowerOfDistanceEnum@endlink) </param>
    def SetIdwOptions(self, nearest_option: FieldEvaluator.InverseDistanceWeightingEnum, nearest_fraction: float, maximum_radius: float, number_of_points: int, power_of_distance: FieldEvaluator.InverseDistanceWeightingPowerOfDistanceEnum) -> None:
        """
         Set the inverse distance weighting (IDW) interpolation options 
        """
        pass
    
    ##  The idw options are set with units 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="nearest_option"> (@link FieldEvaluator.InverseDistanceWeightingEnum NXOpen.Fields.FieldEvaluator.InverseDistanceWeightingEnum@endlink)  nearest option   </param>
    ## <param name="nearest_fraction"> (float)  fraction         </param>
    ## <param name="maximum_radius"> (float)  maximum radius   </param>
    ## <param name="maximum_radius_unit"> (@link NXOpen.Unit NXOpen.Unit@endlink)  maximum radius unit </param>
    ## <param name="number_of_points"> (int)  number of points </param>
    ## <param name="power_of_distance"> (@link FieldEvaluator.InverseDistanceWeightingPowerOfDistanceEnum NXOpen.Fields.FieldEvaluator.InverseDistanceWeightingPowerOfDistanceEnum@endlink) </param>
    def SetIdwOptionsWithUnits(self, nearest_option: FieldEvaluator.InverseDistanceWeightingEnum, nearest_fraction: float, maximum_radius: float, maximum_radius_unit: NXOpen.Unit, number_of_points: int, power_of_distance: FieldEvaluator.InverseDistanceWeightingPowerOfDistanceEnum) -> None:
        """
         The idw options are set with units 
        """
        pass
    
    ##  Set the offset value for the variable 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="varType"> (@link FieldVariable.Type NXOpen.Fields.FieldVariable.Type@endlink) </param>
    ## <param name="offset"> (@link NXOpen.Expression NXOpen.Expression@endlink)  the offset for the variable </param>
    def SetVariableOffset(self, varType: FieldVariable.Type, offset: NXOpen.Expression) -> None:
        """
         Set the offset value for the variable 
        """
        pass
    
    ##  Set the scale factor for the variable 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="varType"> (@link FieldVariable.Type NXOpen.Fields.FieldVariable.Type@endlink) </param>
    ## <param name="scaleFactor"> (@link NXOpen.Expression NXOpen.Expression@endlink)  the scale factor for the variable </param>
    def SetVariableScaleFactor(self, varType: FieldVariable.Type, scaleFactor: NXOpen.Expression) -> None:
        """
         Set the scale factor for the variable 
        """
        pass
    
    ##  Plots or overlays graphs of the Field's structured data versus the Field's specified y-axis dependent variable ; returns newly created plot object.
    ##             For Tables with 3 independent variables, the structured_data_plane_index parameter must be defined; for tables with 2 independent variables it is ignored.
    ##         
    ##  @return plot (@link NXOpen.CAE.Xyplot.Plot NXOpen.CAE.Xyplot.Plot@endlink):  Created plot(s) .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="x_axis_indep_var"> (@link FieldVariable NXOpen.Fields.FieldVariable@endlink)  the specified x-Axis independent variable for which to create the graph </param>
    ## <param name="z_axis_indep_var"> (@link FieldVariable NXOpen.Fields.FieldVariable@endlink)  the specified z-Axis independent variable for which to create the graph </param>
    ## <param name="y_axis_dep_var"> (@link FieldVariable NXOpen.Fields.FieldVariable@endlink)  the specified y-Axis dependent variable for which to create the graph </param>
    ## <param name="structured_data_plane_index"> (int)  index to which structured data plane to plot for 3 dimensional independent domains with structured data </param>
    ## <param name="window_device"> (int)  greater than 0. the index of display device to show the graph. 1 represents main graphic window</param>
    ## <param name="view_index"> (int)  0 thru 8, viewport number to place the graph in </param>
    ## <param name="overlay"> (bool)  create a new plot or add to existing </param>
    ## <param name="scaleFactor"> (float)  scale dependent variable </param>
    def XYGraph3DStructuredData(self, x_axis_indep_var: FieldVariable, z_axis_indep_var: FieldVariable, y_axis_dep_var: FieldVariable, structured_data_plane_index: int, window_device: int, view_index: int, overlay: bool, scaleFactor: float) -> NXOpen.CAE.Xyplot.Plot:
        """
         Plots or overlays graphs of the Field's structured data versus the Field's specified y-axis dependent variable ; returns newly created plot object.
                    For Tables with 3 independent variables, the structured_data_plane_index parameter must be defined; for tables with 2 independent variables it is ignored.
                
         @return plot (@link NXOpen.CAE.Xyplot.Plot NXOpen.CAE.Xyplot.Plot@endlink):  Created plot(s) .
        """
        pass
    
import NXOpen
##   @brief  Represents the Field Variables  
## 
##  
##      <br> A variable is a symbol on whose value a function, polynomial, etc., depends. For example,
##     the variables in the function <b><tt>f(x,y)</tt></b> are <b><tt>x</tt></b> and <b><tt>y</tt></b>. A
##     function having a single variable is said to be univariate, one having two variables is said to be
##     bivariate, and one having three or more variables is said to be multivariate.  In NX, variables in
##     this sense are specifically referred to as independent variables. <br> 
## 
##      <br> In NX, variables are also used to describe the output of a function; these are referred to
##     as the <b><tt>dependent variables</tt></b>.  In NX, a field with a single dependent variable is
##     called a <b><tt>scalar field</tt></b>, with three variables of the same measure a <b><tt>vector field</tt></b>,
##     all others are simply referred to as fields. <br> 
## 
##      <br> In NX, all variables have a measure and associated unit type specification (see also
##     @link NXOpen::Unit NXOpen::Unit@endlink ). <br> 
##     
## 
##   <br>  Created in NX4.0.0  <br> 

class FieldVariable(NXOpen.NXObject): 
    """ <summary> Represents the Field Variables </summary>
    <para>A variable is a symbol on whose value a function, polynomial, etc., depends. For example,
    the variables in the function <b><tt>f(x,y)</tt></b> are <b><tt>x</tt></b> and <b><tt>y</tt></b>. A
    function having a single variable is said to be univariate, one having two variables is said to be
    bivariate, and one having three or more variables is said to be multivariate.  In NX, variables in
    this sense are specifically referred to as independent variables.</para>

    <para>In NX, variables are also used to describe the output of a function; these are referred to
    as the <b><tt>dependent variables</tt></b>.  In NX, a field with a single dependent variable is
    called a <b><tt>scalar field</tt></b>, with three variables of the same measure a <b><tt>vector field</tt></b>,
    all others are simply referred to as fields.</para>

    <para>In NX, all variables have a measure and associated unit type specification (see also
    <ja_class>NXOpen.Unit</ja_class>).</para>
    """


    ##  Variable Types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Unknown</term><description> 
    ##  </description> </item><item><term> 
    ## Independent</term><description> 
    ##  </description> </item><item><term> 
    ## Dependent</term><description> 
    ##  </description> </item></list>
    class Type(Enum):
        """
        Members Include: <Unknown> <Independent> <Dependent>
        """
        Unknown: int
        Independent: int
        Dependent: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FieldVariable.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Variable value Type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Real</term><description> 
    ##  real </description> </item><item><term> 
    ## Imaginary</term><description> 
    ##  (Legacy) imaginary </description> </item><item><term> 
    ## ComplexRealImaginary</term><description> 
    ##  (Legacy) complex_real_imaginary </description> </item><item><term> 
    ## ComplexMagnitudePhase</term><description> 
    ##  (Legacy) complex_magnitude_phase </description> </item><item><term> 
    ## Complex</term><description> 
    ##  Complex </description> </item><item><term> 
    ## Integer</term><description> 
    ##  Integer </description> </item></list>
    class ValueType(Enum):
        """
        Members Include: <Real> <Imaginary> <ComplexRealImaginary> <ComplexMagnitudePhase> <Complex> <Integer>
        """
        Real: int
        Imaginary: int
        ComplexRealImaginary: int
        ComplexMagnitudePhase: int
        Complex: int
        Integer: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FieldVariable.ValueType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Variable Bounds structure 
    ## @link FieldVariableBounds_Struct NXOpen.Fields.FieldVariableBounds_Struct@endlink is an alias for @link FieldVariable.Bounds NXOpen.Fields.FieldVariable.Bounds@endlink.
    class Bounds:
        """
         Variable Bounds structure 
        @link FieldVariableBounds_Struct NXOpen.Fields.FieldVariableBounds_Struct@endlink is an alias for @link FieldVariable.Bounds NXOpen.Fields.FieldVariable.Bounds@endlink.
        """
        ## Getter for property :(bool) IsMinimumDefined
        ## true if minimum bound is defined
        ## @return bool
        @property
        def IsMinimumDefined(self) -> bool:
            """
            Getter for property IsMinimumDefined
            true if minimum bound is defined

            """
            pass
        
        ## Setter for property :(bool) IsMinimumDefined
        @IsMinimumDefined.setter
        def IsMinimumDefined(self, value: bool):
            """
            Getter for property IsMinimumDefined
            true if minimum bound is defined
            Setter for property IsMinimumDefined
            true if minimum bound is defined

            """
            pass
        
        ## Getter for property :(bool) IsMinimumInclusive
        ## true if minimum bound is inclusive
        ## @return bool
        @property
        def IsMinimumInclusive(self) -> bool:
            """
            Getter for property IsMinimumInclusive
            true if minimum bound is inclusive

            """
            pass
        
        ## Setter for property :(bool) IsMinimumInclusive
        @IsMinimumInclusive.setter
        def IsMinimumInclusive(self, value: bool):
            """
            Getter for property IsMinimumInclusive
            true if minimum bound is inclusive
            Setter for property IsMinimumInclusive
            true if minimum bound is inclusive

            """
            pass
        
        ## Getter for property :(float) MinimumValue
        ## minimum bound value
        ## @return float
        @property
        def MinimumValue(self) -> float:
            """
            Getter for property MinimumValue
            minimum bound value

            """
            pass
        
        ## Setter for property :(float) MinimumValue
        @MinimumValue.setter
        def MinimumValue(self, value: float):
            """
            Getter for property MinimumValue
            minimum bound value
            Setter for property MinimumValue
            minimum bound value

            """
            pass
        
        ## Getter for property :(bool) IsMaximumDefined
        ## true if maximum bound is defined
        ## @return bool
        @property
        def IsMaximumDefined(self) -> bool:
            """
            Getter for property IsMaximumDefined
            true if maximum bound is defined

            """
            pass
        
        ## Setter for property :(bool) IsMaximumDefined
        @IsMaximumDefined.setter
        def IsMaximumDefined(self, value: bool):
            """
            Getter for property IsMaximumDefined
            true if maximum bound is defined
            Setter for property IsMaximumDefined
            true if maximum bound is defined

            """
            pass
        
        ## Getter for property :(bool) IsMaximumInclusive
        ## true if maximum bound is inclusive
        ## @return bool
        @property
        def IsMaximumInclusive(self) -> bool:
            """
            Getter for property IsMaximumInclusive
            true if maximum bound is inclusive

            """
            pass
        
        ## Setter for property :(bool) IsMaximumInclusive
        @IsMaximumInclusive.setter
        def IsMaximumInclusive(self, value: bool):
            """
            Getter for property IsMaximumInclusive
            true if maximum bound is inclusive
            Setter for property IsMaximumInclusive
            true if maximum bound is inclusive

            """
            pass
        
        ## Getter for property :(float) MaximumValue
        ## maximum bound value
        ## @return float
        @property
        def MaximumValue(self) -> float:
            """
            Getter for property MaximumValue
            maximum bound value

            """
            pass
        
        ## Setter for property :(float) MaximumValue
        @MaximumValue.setter
        def MaximumValue(self, value: float):
            """
            Getter for property MaximumValue
            maximum bound value
            Setter for property MaximumValue
            maximum bound value

            """
            pass
        
    
    
    ## Getter for property: (float) DefaultValue
    ##  Returns the variable's default value which is value used when evaluating a field and no value is specified  
    ##           
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.2  <br> 

    ## @return float
    @property
    def DefaultValue(self) -> float:
        """
        Getter for property: (float) DefaultValue
         Returns the variable's default value which is value used when evaluating a field and no value is specified  
                  
            
         
        """
        pass
    
    ## Getter for property: (bool) Logarithmic
    ##  Returns the flag indicating if the units for this variable are stored/retrieved as logarithmic units    
    ##           
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def Logarithmic(self) -> bool:
        """
        Getter for property: (bool) Logarithmic
         Returns the flag indicating if the units for this variable are stored/retrieved as logarithmic units    
                  
            
         
        """
        pass
    
    ## Getter for property: (@link NameVariable NXOpen.Fields.NameVariable@endlink) NameVariable
    ##  Returns the name variable for this variable.  
    ##     
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.2  <br> 

    ## @return NameVariable
    @property
    def NameVariable(self) -> NameVariable:
        """
        Getter for property: (@link NameVariable NXOpen.Fields.NameVariable@endlink) NameVariable
         Returns the name variable for this variable.  
            
                  
         
        """
        pass
    
    ## Getter for property: (int) NumPoints
    ##  Returns the number of points used for this variable when generating a table    
    ##           
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.2  <br> 

    ## @return int
    @property
    def NumPoints(self) -> int:
        """
        Getter for property: (int) NumPoints
         Returns the number of points used for this variable when generating a table    
                  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) Units
    ##  Returns the units for this variable, which can be NULL if the variable is unitless.  
    ##     
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.2  <br> 

    ## @return NXOpen.Unit
    @property
    def Units(self) -> NXOpen.Unit:
        """
        Getter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) Units
         Returns the units for this variable, which can be NULL if the variable is unitless.  
            
                  
         
        """
        pass
    
    ## Getter for property: (@link FieldVariable.Bounds NXOpen.Fields.FieldVariable.Bounds@endlink) VariableBounds
    ##  Returns the variable's minimum and maximum bounds.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.2  <br> 

    ## @return FieldVariable.Bounds
    @property
    def VariableBounds(self) -> FieldVariable.Bounds:
        """
        Getter for property: (@link FieldVariable.Bounds NXOpen.Fields.FieldVariable.Bounds@endlink) VariableBounds
         Returns the variable's minimum and maximum bounds.  
          
                  
         
        """
        pass
    
    ## Getter for property: (@link FieldVariable.Type NXOpen.Fields.FieldVariable.Type@endlink) VariableType
    ##  Returns the type of variable.  
    ##     
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.2  <br> 

    ## @return FieldVariable.Type
    @property
    def VariableType(self) -> FieldVariable.Type:
        """
        Getter for property: (@link FieldVariable.Type NXOpen.Fields.FieldVariable.Type@endlink) VariableType
         Returns the type of variable.  
            
                  
         
        """
        pass
    
import NXOpen
##  This class defines a value that is internally backed up by a field. 
## 
##   <br>  Created in NX6.0.0  <br> 

class FieldWrapper(NXOpen.NXObject): 
    """ This class defines a value that is internally backed up by a field. """


    ##  Returns the implementation 
    ##  @return field (@link Field NXOpen.Fields.Field@endlink):  an existing field .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def GetField(self) -> Field:
        """
         Returns the implementation 
         @return field (@link Field NXOpen.Fields.Field@endlink):  an existing field .
        """
        pass
    
    ##  Sets the implementation of the wrapper to the specified field 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="field"> (@link Field NXOpen.Fields.Field@endlink)  an existing field that will be this wrapper's value </param>
    def SetField(self, field: Field) -> None:
        """
         Sets the implementation of the wrapper to the specified field 
        """
        pass
    
import NXOpen
import NXOpen.CAE.Xyplot
##   @brief Represents an Field abstract class. 
## 
##   
##          <br> Fields represent a way of defining a function for one or more dependent 
##         domains/variables (see @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink ) based on relationships 
##         to one or more independent domains/variables (time, temperature, etc.). <br> 
##          <br> Fields are a generic, reusable concept that crosses many 
##         areas of functionality.  Defined properly, they provide an extendable concept that can 
##         service both simple and complicated needs, for example,  modeling elements, properties, 
##         materials, boundary conditions in CAE/FEM applications. <br>  
## 
##   <br>  Created in NX4.0.0  <br> 

class Field(NXOpen.DisplayableObject): 
    """ <summary>Represents an Field abstract class.</summary> 
        <para>Fields represent a way of defining a function for one or more dependent 
        domains/variables (see <ja_class>NXOpen.Fields.FieldVariable</ja_class>) based on relationships 
        to one or more independent domains/variables (time, temperature, etc.).</para>
        <para>Fields are a generic, reusable concept that crosses many 
        areas of functionality.  Defined properly, they provide an extendable concept that can 
        service both simple and complicated needs, for example,  modeling elements, properties, 
        materials, boundary conditions in CAE/FEM applications.</para> """


    ##  plotting options
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## InterpolatedValues</term><description> 
    ## </description> </item><item><term> 
    ## InterpolatedValuesWithBounds</term><description> 
    ## </description> </item><item><term> 
    ## RawTableValues</term><description> 
    ## </description> </item></list>
    class PlotOption(Enum):
        """
        Members Include: <InterpolatedValues> <InterpolatedValuesWithBounds> <RawTableValues>
        """
        InterpolatedValues: int
        InterpolatedValuesWithBounds: int
        RawTableValues: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Field.PlotOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) IsLocked
    ##  Returns a value that indicates whether this field is locked against edits.  
    ##    
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.2  <br> 

    ## @return bool
    @property
    def IsLocked(self) -> bool:
        """
        Getter for property: (bool) IsLocked
         Returns a value that indicates whether this field is locked against edits.  
           
                  
         
        """
        pass
    
    ## Getter for property: (bool) IsUserField
    ##  Returns a value that indicates whether this field is a user created/managed field.  
    ##   
    ##             Many fields are created automatically by the system for internal uses. The life of these
    ##             fields is managed by the objects that own them and so these fields are 
    ##             not consider user fields. 
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.2  <br> 

    ## @return bool
    @property
    def IsUserField(self) -> bool:
        """
        Getter for property: (bool) IsUserField
         Returns a value that indicates whether this field is a user created/managed field.  
          
                    Many fields are created automatically by the system for internal uses. The life of these
                    fields is managed by the objects that own them and so these fields are 
                    not consider user fields. 
                  
         
        """
        pass
    
    ##  Adds the specified application data object to the field
    ##              
    ##             NOTE: Only one application data object per IApplication can be added
    ##             and the data must be owned by an IApplication with the same Part::Field::Main 
    ##             as the field.  
    ##          
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="appData"> (@link IApplicationData NXOpen.Fields.IApplicationData@endlink) </param>
    def AddApplicationData(self, appData: IApplicationData) -> None:
        """
         Adds the specified application data object to the field
                     
                    NOTE: Only one application data object per IApplication can be added
                    and the data must be owned by an IApplication with the same Part::Field::Main 
                    as the field.  
                 
        """
        pass
    
    ##  Copy the field to the target part.
    ##         
    ##  @return new_field (@link Field NXOpen.Fields.Field@endlink):  newly created field .
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="target_part"> (@link NXOpen.BasePart NXOpen.BasePart@endlink)  target part </param>
    def CreateCopyInPart(self, target_part: NXOpen.BasePart) -> Field:
        """
         Copy the field to the target part.
                
         @return new_field (@link Field NXOpen.Fields.Field@endlink):  newly created field .
        """
        pass
    
    ##  Create a new table field from this field (regardless of type).  Note
    ##         * that the table will be created have the N number of rows, where
    ##         * N is the product of the number of points for each independent variable, 
    ##         * resulting in a grid (or lattice).  The resulting field will be in the
    ##         * same part.
    ##         
    ##  @return new_table (@link FieldTable NXOpen.Fields.FieldTable@endlink):  newly created table .
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="target_part"> (@link NXOpen.BasePart NXOpen.BasePart@endlink)  target part </param>
    def CreateTableInPart(self, target_part: NXOpen.BasePart) -> FieldTable:
        """
         Create a new table field from this field (regardless of type).  Note
                * that the table will be created have the N number of rows, where
                * N is the product of the number of points for each independent variable, 
                * resulting in a grid (or lattice).  The resulting field will be in the
                * same part.
                
         @return new_table (@link FieldTable NXOpen.Fields.FieldTable@endlink):  newly created table .
        """
        pass
    
    ##  Delete this field; destroys the field and removes all references to it.
    ##         
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def Delete(self) -> None:
        """
         Delete this field; destroys the field and removes all references to it.
                
        """
        pass
    
    ##  Retrieves the application data associated with the field for the specified application.
    ##          
    ##  @return appData (@link IApplicationData NXOpen.Fields.IApplicationData@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="applicationName"> (str) </param>
    def GetApplicationData(self, applicationName: str) -> IApplicationData:
        """
         Retrieves the application data associated with the field for the specified application.
                 
         @return appData (@link IApplicationData NXOpen.Fields.IApplicationData@endlink): .
        """
        pass
    
    ##  Returns the dependent variables for this @link NXOpen::Fields::Field NXOpen::Fields::Field@endlink   
    ##         
    ##  @return dependent_variables (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink):  dependent variables for this @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink   .
    ## 
    ##   <br>  Created in NX7.5.2  <br> 

    ## License requirements: None.
    def GetDependentVariables(self) -> List[FieldVariable]:
        """
         Returns the dependent variables for this @link NXOpen::Fields::Field NXOpen::Fields::Field@endlink   
                
         @return dependent_variables (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink):  dependent variables for this @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink   .
        """
        pass
    
    ##  Returns the description of the field.
    ##         
    ##  @return lines (List[str]):  description .
    ## 
    ##   <br>  Created in NX7.5.2  <br> 

    ## License requirements: None.
    def GetDescription(self) -> List[str]:
        """
         Returns the description of the field.
                
         @return lines (List[str]):  description .
        """
        pass
    
    ##  Returns a field evaluator which can be used to evaluate this field.
    ##         
    ##  @return evaluator (@link FieldEvaluator NXOpen.Fields.FieldEvaluator@endlink):  Field Evaluator .
    ## 
    ##   <br>  Created in NX7.5.2  <br> 

    ## License requirements: None.
    def GetFieldEvaluator(self) -> FieldEvaluator:
        """
         Returns a field evaluator which can be used to evaluate this field.
                
         @return evaluator (@link FieldEvaluator NXOpen.Fields.FieldEvaluator@endlink):  Field Evaluator .
        """
        pass
    
    ##  Get the parent folder for this field.  A null folder returned is in the root collection. 
    ##  @return folder (@link FieldFolder NXOpen.Fields.FieldFolder@endlink):  folder .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    def GetFolder(self) -> FieldFolder:
        """
         Get the parent folder for this field.  A null folder returned is in the root collection. 
         @return folder (@link FieldFolder NXOpen.Fields.FieldFolder@endlink):  folder .
        """
        pass
    
    ##  Returns the ID/Label of the field.
    ##         
    ##  @return id_label (int):  ID/Label .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    def GetIdLabel(self) -> int:
        """
         Returns the ID/Label of the field.
                
         @return id_label (int):  ID/Label .
        """
        pass
    
    ##  Returns the independent variables for this @link NXOpen::Fields::Field NXOpen::Fields::Field@endlink   
    ##         
    ##  @return independent_variables (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink):  independent variables for this @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink   .
    ## 
    ##   <br>  Created in NX7.5.2  <br> 

    ## License requirements: None.
    def GetIndependentVariables(self) -> List[FieldVariable]:
        """
         Returns the independent variables for this @link NXOpen::Fields::Field NXOpen::Fields::Field@endlink   
                
         @return independent_variables (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink):  independent variables for this @link NXOpen::Fields::FieldVariable NXOpen::Fields::FieldVariable@endlink   .
        """
        pass
    
    ##  Returns the spatial map for the formula field if one exists.
    ##         
    ##  @return override_map (@link SpatialMap NXOpen.Fields.SpatialMap@endlink):  spatial map  .
    ## 
    ##   <br>  Created in NX7.5.2  <br> 

    ## License requirements: None.
    def GetSpatialMap(self) -> SpatialMap:
        """
         Returns the spatial map for the formula field if one exists.
                
         @return override_map (@link SpatialMap NXOpen.Fields.SpatialMap@endlink):  spatial map  .
        """
        pass
    
    ##  Reloads the field from its data source.  If the data source does not support
    ##         reload functionality or if the field does not have a data source
    ##         the function will do nothing.
    ##         
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def Reload(self) -> None:
        """
         Reloads the field from its data source.  If the data source does not support
                reload functionality or if the field does not have a data source
                the function will do nothing.
                
        """
        pass
    
    ##  Update the name of the field.
    ##         
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="new_name"> (str)  new field name </param>
    def Rename(self, new_name: str) -> None:
        """
         Update the name of the field.
                
        """
        pass
    
    ##  Update the description of the field.
    ##         
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="lines"> (List[str])  new description </param>
    def SetDescription(self, lines: List[str]) -> None:
        """
         Update the description of the field.
                
        """
        pass
    
    ##  Update the ID/Label of the field.
    ##         
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="id_label"> (int)  ID/Label </param>
    def SetIdLabel(self, id_label: int) -> None:
        """
         Update the ID/Label of the field.
                
        """
        pass
    
    ##  Set lock value that indicates whether this field is locked against edits. 
    ##         
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="locked"> (bool)  Lock value of field </param>
    def SetLocked(self, locked: bool) -> None:
        """
         Set lock value that indicates whether this field is locked against edits. 
                
        """
        pass
    
    ##  Set part context.
    ##         
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    def SetPartContext(self) -> None:
        """
         Set part context.
                
        """
        pass
    
    ##  Set the spatial map for the formula field.
    ##         
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="override_map"> (@link SpatialMap NXOpen.Fields.SpatialMap@endlink)  spatial map to set </param>
    def SetSpatialMap(self, override_map: SpatialMap) -> None:
        """
         Set the spatial map for the formula field.
                
        """
        pass
    
    ##  Creates displayed graphs of the Field's specified independent variable
    ##             versus all the Field's dependent variables
    ##          
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## <param name="field"> (@link Field NXOpen.Fields.Field@endlink) </param>
    ## <param name="indep_var"> (@link FieldVariable NXOpen.Fields.FieldVariable@endlink)  the specified independent variable for which to create the graph </param>
    ## <param name="abscissa_minimum"> (float)  the minimum bounds along the abscissa  </param>
    ## <param name="abscissa_maximum"> (float)  the maximum bounds along the abscissa  </param>
    ## <param name="abscissa_point_count"> (int)  the number of points to graph along the abscissa.
    ##                                                                          the number of times to evaluate the graphed independent variable </param>
    ## <param name="constant_indep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink) 
    ##                                                                          independent variables to hold constant 
    ##                                                                          If the field has only 1 independent variable, this parameter is NULL </param>
    ## <param name="constant_indep_var_value_array"> (List[float])  independent variables constant values
    ##                                                                          If the field has only 1 independent variable, this parameter is NULL </param>
    @overload
    def XYGraph(self, indep_var: FieldVariable, abscissa_minimum: float, abscissa_maximum: float, abscissa_point_count: int, constant_indep_var_array: List[FieldVariable], constant_indep_var_value_array: List[float]) -> None:
        """
         Creates displayed graphs of the Field's specified independent variable
                    versus all the Field's dependent variables
                 
        """
        pass
    
    ##  Plots or overlays graphs of the Field's specified x-axis and z-axis independent variables
    ##             versus the Field's specified y-axis dependent variable ; returns newly created plot object.
    ##          
    ##  @return plot (@link NXOpen.CAE.Xyplot.Plot NXOpen.CAE.Xyplot.Plot@endlink):  Created plot(s) .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="x_axis_indep_var"> (@link FieldVariable NXOpen.Fields.FieldVariable@endlink)  the specified x-axis independent variable for which to create the graph </param>
    ## <param name="x_axis_bnds_minimum"> (float)  the minimum bounds along the x-axis  </param>
    ## <param name="x_axis_bnds_maximum"> (float)  the maximum bounds along the x-axis  </param>
    ## <param name="x_axis_bnds_sample_size"> (int)  the sample size to graph along the x-axis.
    ##                                                                       the number of times to evaluate the x-axis independent variable </param>
    ## <param name="z_axis_indep_var"> (@link FieldVariable NXOpen.Fields.FieldVariable@endlink)  the specified z-Axis independent variable for which to create the graph </param>
    ## <param name="z_axis_bnds_minimum"> (float)  the minimum bounds along the z-Axis  </param>
    ## <param name="z_axis_bnds_maximum"> (float)  the maximum bounds along the z-Axis  </param>
    ## <param name="z_axis_bnds_sample_size"> (int)  the sample size to graph along the z-Axis.
    ##                                                                       the number of times to evaluate the z-Axis independent variable </param>
    ## <param name="y_axis_dep_var"> (@link FieldVariable NXOpen.Fields.FieldVariable@endlink)  the specified y-Axis dependent variable for which to create the graph </param>
    ## <param name="constant_indep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink) 
    ##                                                                          independent variables to hold constant 
    ##                                                                          If the field has only 2 independent variables, this parameter is NULL </param>
    ## <param name="constant_indep_var_value_array"> (List[float])  independent variables constant values
    ##                                                                          If the field has only 2 independent variables, this parameter is NULL </param>
    ## <param name="interpolate_table_data"> (bool)  a true value means that the table field data will be interpolated if there are more than 2 independent variables. 
    ##                                                                          a false value means that the data is plotted directly from the table and the constant values will be ignored.
    ##                                                                          this value is only used for table fields with over 2 independent variables.</param>
    ## <param name="window_device"> (int)  greater than 0. the index of display device to show the graph. 1 represents main graphic window</param>
    ## <param name="view_index"> (int)  0 thru 8, viewport number to place the graph in </param>
    ## <param name="overlay"> (bool)  create a new plot or add to existing </param>
    ## <param name="scaleFactor"> (float)  scale dependent variable </param>
    def XYGraph3D(self, x_axis_indep_var: FieldVariable, x_axis_bnds_minimum: float, x_axis_bnds_maximum: float, x_axis_bnds_sample_size: int, z_axis_indep_var: FieldVariable, z_axis_bnds_minimum: float, z_axis_bnds_maximum: float, z_axis_bnds_sample_size: int, y_axis_dep_var: FieldVariable, constant_indep_var_array: List[FieldVariable], constant_indep_var_value_array: List[float], interpolate_table_data: bool, window_device: int, view_index: int, overlay: bool, scaleFactor: float) -> NXOpen.CAE.Xyplot.Plot:
        """
         Plots or overlays graphs of the Field's specified x-axis and z-axis independent variables
                    versus the Field's specified y-axis dependent variable ; returns newly created plot object.
                 
         @return plot (@link NXOpen.CAE.Xyplot.Plot NXOpen.CAE.Xyplot.Plot@endlink):  Created plot(s) .
        """
        pass
    
    ##  Plots the Field's specified independent variable 
    ##             versus all the Field's scaled dependent variables as an Argand graph; returns newly created plot object(s).
    ##          
    ##  @return plots (@link NXOpen.CAE.Xyplot.Plot List[NXOpen.CAE.Xyplot.Plot]@endlink):  Created plot(s) .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="indep_var"> (@link FieldVariable NXOpen.Fields.FieldVariable@endlink)  the specified independent variable for which to create the graph </param>
    ## <param name="abscissa_minimum"> (float)  the minimum bounds along the abscissa  </param>
    ## <param name="abscissa_maximum"> (float)  the maximum bounds along the abscissa  </param>
    ## <param name="abscissa_point_count"> (int)  the number of points to graph along the abscissa.
    ##                                                                          the number of times to evaluate the graphed independent variable </param>
    ## <param name="constant_indep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink) 
    ##                                                                          independent variables to hold constant 
    ##                                                                          If the field has only 1 independent variable, this parameter is NULL </param>
    ## <param name="constant_indep_var_value_array"> (List[float])  independent variables constant values
    ##                                                                          If the field has only 1 independent variable, this parameter is NULL </param>
    ## <param name="window_device"> (int)  great than 0. the index of display device to show the graph. 1 represents main graphic window</param>
    ## <param name="view_index"> (int)  0 thru 8, viewport number to place the graph in </param>
    def XYGraphArgand(self, indep_var: FieldVariable, abscissa_minimum: float, abscissa_maximum: float, abscissa_point_count: int, constant_indep_var_array: List[FieldVariable], constant_indep_var_value_array: List[float], window_device: int, view_index: int) -> List[NXOpen.CAE.Xyplot.Plot]:
        """
         Plots the Field's specified independent variable 
                    versus all the Field's scaled dependent variables as an Argand graph; returns newly created plot object(s).
                 
         @return plots (@link NXOpen.CAE.Xyplot.Plot List[NXOpen.CAE.Xyplot.Plot]@endlink):  Created plot(s) .
        """
        pass
    
    ##  Plots or overlays graphs of the Field's specified independent variable raw data or interpolated data
    ##             versus all the Field's scaled dependent variables; returns newly created plot object(s).
    ##          
    ##  @return plots (@link NXOpen.CAE.Xyplot.Plot List[NXOpen.CAE.Xyplot.Plot]@endlink):  Created plot(s) .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="indep_var"> (@link FieldVariable NXOpen.Fields.FieldVariable@endlink)  the specified independent variable for which to create the graph </param>
    ## <param name="abscissa_minimum"> (float)  the minimum bounds along the abscissa  </param>
    ## <param name="abscissa_maximum"> (float)  the maximum bounds along the abscissa  </param>
    ## <param name="abscissa_point_count"> (int)  the number of points to graph along the abscissa.
    ##                                                                          the number of times to evaluate the graphed independent variable </param>
    ## <param name="constant_indep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink) 
    ##                                                                          independent variables to hold constant 
    ##                                                                          If the field has only 1 independent variable, this parameter is NULL </param>
    ## <param name="constant_indep_var_value_array"> (List[float])  independent variables constant values
    ##                                                                          If the field has only 1 independent variable, this parameter is NULL </param>
    ## <param name="window_device"> (int)  great than 0. the index of display device to show the graph. 1 represents main graphic window</param>
    ## <param name="view_index"> (int)  0 thru 8, viewport number to place the graph in </param>
    ## <param name="overlay"> (bool)  create a new plot or add to existing </param>
    ## <param name="scaleFactor"> (float)  scale dependent variable(s) </param>
    ## <param name="plotOption"> (@link Field.PlotOption NXOpen.Fields.Field.PlotOption@endlink)  whether to plot raw table data or bounded interpolation or default interpolated values </param>
    def XYGraphPlotData(self, indep_var: FieldVariable, abscissa_minimum: float, abscissa_maximum: float, abscissa_point_count: int, constant_indep_var_array: List[FieldVariable], constant_indep_var_value_array: List[float], window_device: int, view_index: int, overlay: bool, scaleFactor: float, plotOption: Field.PlotOption) -> List[NXOpen.CAE.Xyplot.Plot]:
        """
         Plots or overlays graphs of the Field's specified independent variable raw data or interpolated data
                    versus all the Field's scaled dependent variables; returns newly created plot object(s).
                 
         @return plots (@link NXOpen.CAE.Xyplot.Plot List[NXOpen.CAE.Xyplot.Plot]@endlink):  Created plot(s) .
        """
        pass
    
    ##  Plots or overlays graphs of the Field's specified independent variable
    ##             versus all the Field's dependent variables
    ##          
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## <param name="field"> (@link Field NXOpen.Fields.Field@endlink) </param>
    ## <param name="indep_var"> (@link FieldVariable NXOpen.Fields.FieldVariable@endlink)  the specified independent variable for which to create the graph </param>
    ## <param name="abscissa_minimum"> (float)  the minimum bounds along the abscissa  </param>
    ## <param name="abscissa_maximum"> (float)  the maximum bounds along the abscissa  </param>
    ## <param name="abscissa_point_count"> (int)  the number of points to graph along the abscissa.
    ##                                                                          the number of times to evaluate the graphed independent variable </param>
    ## <param name="constant_indep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink) 
    ##                                                                          independent variables to hold constant 
    ##                                                                          If the field has only 1 independent variable, this parameter is NULL </param>
    ## <param name="constant_indep_var_value_array"> (List[float])  independent variables constant values
    ##                                                                          If the field has only 1 independent variable, this parameter is NULL </param>
    ## <param name="view_index"> (int)  0 thru 8, viewport number to place the graph in </param>
    ## <param name="overlay"> (bool)  create a new plot or add to existing </param>
    @overload
    def XYGraph(self, indep_var: FieldVariable, abscissa_minimum: float, abscissa_maximum: float, abscissa_point_count: int, constant_indep_var_array: List[FieldVariable], constant_indep_var_value_array: List[float], view_index: int, overlay: bool) -> None:
        """
         Plots or overlays graphs of the Field's specified independent variable
                    versus all the Field's dependent variables
                 
        """
        pass
    
    ##  Plots or overlays graphs of the Field's specified independent variable
    ##             versus all the Field's dependent variables
    ##          
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ## <param name="field"> (@link Field NXOpen.Fields.Field@endlink) </param>
    ## <param name="indep_var"> (@link FieldVariable NXOpen.Fields.FieldVariable@endlink)  the specified independent variable for which to create the graph </param>
    ## <param name="abscissa_minimum"> (float)  the minimum bounds along the abscissa  </param>
    ## <param name="abscissa_maximum"> (float)  the maximum bounds along the abscissa  </param>
    ## <param name="abscissa_point_count"> (int)  the number of points to graph along the abscissa.
    ##                                                                          the number of times to evaluate the graphed independent variable </param>
    ## <param name="constant_indep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink) 
    ##                                                                          independent variables to hold constant 
    ##                                                                          If the field has only 1 independent variable, this parameter is NULL </param>
    ## <param name="constant_indep_var_value_array"> (List[float])  independent variables constant values
    ##                                                                          If the field has only 1 independent variable, this parameter is NULL </param>
    ## <param name="window_device"> (int)  great than 0. the index of display device to show the graph. 1 represents main graphic window</param>
    ## <param name="view_index"> (int)  0 thru 8, viewport number to place the graph in </param>
    ## <param name="overlay"> (bool)  create a new plot or add to existing </param>
    @overload
    def XYGraph(self, indep_var: FieldVariable, abscissa_minimum: float, abscissa_maximum: float, abscissa_point_count: int, constant_indep_var_array: List[FieldVariable], constant_indep_var_value_array: List[float], window_device: int, view_index: int, overlay: bool) -> None:
        """
         Plots or overlays graphs of the Field's specified independent variable
                    versus all the Field's dependent variables
                 
        """
        pass
    
    ##  Plots or overlays graphs of the Field's specified independent variable
    ##             versus all the Field's dependent variables; returns newly created plot object(s).
    ##          
    ##  @return plots (@link NXOpen.CAE.Xyplot.Plot List[NXOpen.CAE.Xyplot.Plot]@endlink):  Created plot(s) .
    ## 
    ##   <br>  Created in NX9.0.1  <br> 

    ## License requirements: None.
    ## <param name="field"> (@link Field NXOpen.Fields.Field@endlink) </param>
    ## <param name="indep_var"> (@link FieldVariable NXOpen.Fields.FieldVariable@endlink)  the specified independent variable for which to create the graph </param>
    ## <param name="abscissa_minimum"> (float)  the minimum bounds along the abscissa  </param>
    ## <param name="abscissa_maximum"> (float)  the maximum bounds along the abscissa  </param>
    ## <param name="abscissa_point_count"> (int)  the number of points to graph along the abscissa.
    ##                                                                          the number of times to evaluate the graphed independent variable </param>
    ## <param name="constant_indep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink) 
    ##                                                                          independent variables to hold constant 
    ##                                                                          If the field has only 1 independent variable, this parameter is NULL </param>
    ## <param name="constant_indep_var_value_array"> (List[float])  independent variables constant values
    ##                                                                          If the field has only 1 independent variable, this parameter is NULL </param>
    ## <param name="window_device"> (int)  great than 0. the index of display device to show the graph. 1 represents main graphic window</param>
    ## <param name="view_index"> (int)  0 thru 8, viewport number to place the graph in </param>
    ## <param name="overlay"> (bool)  create a new plot or add to existing </param>
    @overload
    def XYGraph(self, indep_var: FieldVariable, abscissa_minimum: float, abscissa_maximum: float, abscissa_point_count: int, constant_indep_var_array: List[FieldVariable], constant_indep_var_value_array: List[float], window_device: int, view_index: int, overlay: bool) -> List[NXOpen.CAE.Xyplot.Plot]:
        """
         Plots or overlays graphs of the Field's specified independent variable
                    versus all the Field's dependent variables; returns newly created plot object(s).
                 
         @return plots (@link NXOpen.CAE.Xyplot.Plot List[NXOpen.CAE.Xyplot.Plot]@endlink):  Created plot(s) .
        """
        pass
    
    ##  Plots or overlays graphs of the Field's specified independent variable 
    ##             versus all the Field's scaled dependent variables; returns newly created plot object(s).
    ##          
    ##  @return plots (@link NXOpen.CAE.Xyplot.Plot List[NXOpen.CAE.Xyplot.Plot]@endlink):  Created plot(s) .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## <param name="field"> (@link Field NXOpen.Fields.Field@endlink) </param>
    ## <param name="indep_var"> (@link FieldVariable NXOpen.Fields.FieldVariable@endlink)  the specified independent variable for which to create the graph </param>
    ## <param name="abscissa_minimum"> (float)  the minimum bounds along the abscissa  </param>
    ## <param name="abscissa_maximum"> (float)  the maximum bounds along the abscissa  </param>
    ## <param name="abscissa_point_count"> (int)  the number of points to graph along the abscissa.
    ##                                                                          the number of times to evaluate the graphed independent variable </param>
    ## <param name="constant_indep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink) 
    ##                                                                          independent variables to hold constant 
    ##                                                                          If the field has only 1 independent variable, this parameter is NULL </param>
    ## <param name="constant_indep_var_value_array"> (List[float])  independent variables constant values
    ##                                                                          If the field has only 1 independent variable, this parameter is NULL </param>
    ## <param name="window_device"> (int)  great than 0. the index of display device to show the graph. 1 represents main graphic window</param>
    ## <param name="view_index"> (int)  0 thru 8, viewport number to place the graph in </param>
    ## <param name="overlay"> (bool)  create a new plot or add to existing </param>
    ## <param name="scaleFactor"> (float)  scale dependent variable(s) </param>
    @overload
    def XYGraph(self, indep_var: FieldVariable, abscissa_minimum: float, abscissa_maximum: float, abscissa_point_count: int, constant_indep_var_array: List[FieldVariable], constant_indep_var_value_array: List[float], window_device: int, view_index: int, overlay: bool, scaleFactor: float) -> List[NXOpen.CAE.Xyplot.Plot]:
        """
         Plots or overlays graphs of the Field's specified independent variable 
                    versus all the Field's scaled dependent variables; returns newly created plot object(s).
                 
         @return plots (@link NXOpen.CAE.Xyplot.Plot List[NXOpen.CAE.Xyplot.Plot]@endlink):  Created plot(s) .
        """
        pass
    
import NXOpen
##   @brief Interface for all application specific data to be registered on fields. Only one 
##     application specific data object per IApplication can be added to a field. 
## 
##  
## 
##   <br>  Created in NX12.0.0  <br> 

class IApplicationData(NXOpen.INXObject): 
    """ <summary>Interface for all application specific data to be registered on fields. Only one 
    application specific data object per IApplication can be added to a field.</summary>"""


    ##  Copy the Application Data object to the specified field 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="field"> (@link Field NXOpen.Fields.Field@endlink)  field to copy to </param>
    @abstractmethod
    def CopyToField(self, field: Field) -> None:
        """
         Copy the Application Data object to the specified field 
        """
        pass
    
    ##  Delete the Application Data object 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @abstractmethod
    def DeleteApplicationData(self) -> None:
        """
         Delete the Application Data object 
        """
        pass
    
    ##  Returns the application associated with this application data object. 
    ##  @return application (@link IApplication NXOpen.Fields.IApplication@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @abstractmethod
    def GetApplication(self) -> IApplication:
        """
         Returns the application associated with this application data object. 
         @return application (@link IApplication NXOpen.Fields.IApplication@endlink): .
        """
        pass
    
import NXOpen
##   @brief Interface for all applications registered with the Field subsystem. Each application
##     type should only be registered once with the Field subsystem. Each application class is identified
##     by its name. 
## 
##   <br> This is an abstract class, and cannot be created.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class IApplication(NXOpen.TaggedObject): 
    """ <summary>Interface for all applications registered with the Field subsystem. Each application
    type should only be registered once with the Field subsystem. Each application class is identified
    by its name.</summary>"""


    ## Getter for property: (str) Name
    ##  Returns the name of the application.  
    ##    This name should be unique for each application class.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name of the application.  
           This name should be unique for each application class.  
         
        """
        pass
    
import NXOpen
##  Represents a builder to import fields from a .fld formatted text file  <br> To create a new instance of this class, use @link NXOpen::Fields::FieldManager::CreateImportBuilder  NXOpen::Fields::FieldManager::CreateImportBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## ConflictResolutionStrategy </term> <description> 
##  
## AppendtoImportedFieldName </description> </item> 
## 
## <item><term> 
##  
## FilterOptions </term> <description> 
##  
## All </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1847.0.0  <br> 

class ImportBuilder(NXOpen.Builder): 
    """ Represents a builder to import fields from a .fld formatted text file """


    ##  Import conflict resolution strategy for a field 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Import</term><description> 
    ## </description> </item><item><term> 
    ## DontImport</term><description> 
    ## </description> </item><item><term> 
    ## ImportAppend</term><description> 
    ## </description> </item><item><term> 
    ## Replace</term><description> 
    ## </description> </item><item><term> 
    ## BackupAndReplace</term><description> 
    ## </description> </item><item><term> 
    ## ImportPrepend</term><description> 
    ## </description> </item></list>
    class ActionType(Enum):
        """
        Members Include: <Import> <DontImport> <ImportAppend> <Replace> <BackupAndReplace> <ImportPrepend>
        """
        Import: int
        DontImport: int
        ImportAppend: int
        Replace: int
        BackupAndReplace: int
        ImportPrepend: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ImportBuilder.ActionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Describes any conflict with imported field and target part.  Since field
    ##             names must be unique, any import fields with the same name as a target field
    ##             is considered to be in potential conflict. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NoConflict</term><description> 
    ## </description> </item><item><term> 
    ## NameOnlyConflict</term><description> 
    ## </description> </item><item><term> 
    ## NameOnlyConflictInUse</term><description> 
    ## </description> </item><item><term> 
    ## CompatibleVariableConflict</term><description> 
    ## </description> </item><item><term> 
    ## CompatibleVariableConflictInUse</term><description> 
    ## </description> </item><item><term> 
    ## IncompatibleVariableConflict</term><description> 
    ## </description> </item><item><term> 
    ## IncompatibleVariableConflictInUse</term><description> 
    ## </description> </item></list>
    class ConflictType(Enum):
        """
        Members Include: <NoConflict> <NameOnlyConflict> <NameOnlyConflictInUse> <CompatibleVariableConflict> <CompatibleVariableConflictInUse> <IncompatibleVariableConflict> <IncompatibleVariableConflictInUse>
        """
        NoConflict: int
        NameOnlyConflict: int
        NameOnlyConflictInUse: int
        CompatibleVariableConflict: int
        CompatibleVariableConflictInUse: int
        IncompatibleVariableConflict: int
        IncompatibleVariableConflictInUse: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ImportBuilder.ConflictType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Import conflict resolution strategy for the file 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## AppendtoImportedFieldName</term><description> 
    ## </description> </item><item><term> 
    ## PrependStringtoImportedFieldName</term><description> 
    ## </description> </item><item><term> 
    ## UserSpecifiedReplaceandorRename</term><description> 
    ## </description> </item></list>
    class ImportConflictStrategy(Enum):
        """
        Members Include: <AppendtoImportedFieldName> <PrependStringtoImportedFieldName> <UserSpecifiedReplaceandorRename>
        """
        AppendtoImportedFieldName: int
        PrependStringtoImportedFieldName: int
        UserSpecifiedReplaceandorRename: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ImportBuilder.ImportConflictStrategy:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Describes import option for a field 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Skip</term><description> 
    ## </description> </item><item><term> 
    ## RenameExisting</term><description> 
    ## </description> </item><item><term> 
    ## RenameImported</term><description> 
    ## </description> </item><item><term> 
    ## Replace</term><description> 
    ## </description> </item><item><term> 
    ## BackupReplace</term><description> 
    ## </description> </item></list>
    class ImportFieldStrategy(Enum):
        """
        Members Include: <Skip> <RenameExisting> <RenameImported> <Replace> <BackupReplace>
        """
        Skip: int
        RenameExisting: int
        RenameImported: int
        Replace: int
        BackupReplace: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ImportBuilder.ImportFieldStrategy:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Describes filter for fields imported from the file 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## All</term><description> 
    ## </description> </item><item><term> 
    ## Formula</term><description> 
    ## </description> </item><item><term> 
    ## Table</term><description> 
    ## </description> </item><item><term> 
    ## LinkedField</term><description> 
    ## </description> </item><item><term> 
    ## TableofFields</term><description> 
    ## </description> </item><item><term> 
    ## FilterbyName</term><description> 
    ## </description> </item><item><term> 
    ## FilterbyDomain</term><description> 
    ## </description> </item><item><term> 
    ## FilterbyDependentVariableName</term><description> 
    ## </description> </item><item><term> 
    ## FilterbyIndependentVariableName</term><description> 
    ## </description> </item></list>
    class ImportFilter(Enum):
        """
        Members Include: <All> <Formula> <Table> <LinkedField> <TableofFields> <FilterbyName> <FilterbyDomain> <FilterbyDependentVariableName> <FilterbyIndependentVariableName>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ImportBuilder.ImportFilter:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link ImportBuilder.ImportConflictStrategy NXOpen.Fields.ImportBuilder.ImportConflictStrategy@endlink) ConflictResolutionStrategy
    ##  Returns the conflict resolution strategy   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return ImportBuilder.ImportConflictStrategy
    @property
    def ConflictResolutionStrategy(self) -> ImportBuilder.ImportConflictStrategy:
        """
        Getter for property: (@link ImportBuilder.ImportConflictStrategy NXOpen.Fields.ImportBuilder.ImportConflictStrategy@endlink) ConflictResolutionStrategy
         Returns the conflict resolution strategy   
            
         
        """
        pass
    
    ## Setter for property: (@link ImportBuilder.ImportConflictStrategy NXOpen.Fields.ImportBuilder.ImportConflictStrategy@endlink) ConflictResolutionStrategy

    ##  Returns the conflict resolution strategy   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ConflictResolutionStrategy.setter
    def ConflictResolutionStrategy(self, conflictResolutionStrategy: ImportBuilder.ImportConflictStrategy):
        """
        Setter for property: (@link ImportBuilder.ImportConflictStrategy NXOpen.Fields.ImportBuilder.ImportConflictStrategy@endlink) ConflictResolutionStrategy
         Returns the conflict resolution strategy   
            
         
        """
        pass
    
    ## Getter for property: (@link ImportBuilder.ImportFilter NXOpen.Fields.ImportBuilder.ImportFilter@endlink) FilterOptions
    ##  Returns the filter options   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return ImportBuilder.ImportFilter
    @property
    def FilterOptions(self) -> ImportBuilder.ImportFilter:
        """
        Getter for property: (@link ImportBuilder.ImportFilter NXOpen.Fields.ImportBuilder.ImportFilter@endlink) FilterOptions
         Returns the filter options   
            
         
        """
        pass
    
    ## Setter for property: (@link ImportBuilder.ImportFilter NXOpen.Fields.ImportBuilder.ImportFilter@endlink) FilterOptions

    ##  Returns the filter options   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @FilterOptions.setter
    def FilterOptions(self, filterOptions: ImportBuilder.ImportFilter):
        """
        Setter for property: (@link ImportBuilder.ImportFilter NXOpen.Fields.ImportBuilder.ImportFilter@endlink) FilterOptions
         Returns the filter options   
            
         
        """
        pass
    
    ## Getter for property: (str) FilterString
    ##  Returns the filter string   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def FilterString(self) -> str:
        """
        Getter for property: (str) FilterString
         Returns the filter string   
            
         
        """
        pass
    
    ## Setter for property: (str) FilterString

    ##  Returns the filter string   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @FilterString.setter
    def FilterString(self, filterString: str):
        """
        Setter for property: (str) FilterString
         Returns the filter string   
            
         
        """
        pass
    
    ## Getter for property: (@link Field NXOpen.Fields.Field@endlink) ImportField
    ##  Returns the imported field   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1980.0.0.  No replacement.  <br> 

    ## @return Field
    @property
    def ImportField(self) -> Field:
        """
        Getter for property: (@link Field NXOpen.Fields.Field@endlink) ImportField
         Returns the imported field   
            
         
        """
        pass
    
    ## Setter for property: (@link Field NXOpen.Fields.Field@endlink) ImportField

    ##  Returns the imported field   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1980.0.0.  No replacement.  <br> 

    @ImportField.setter
    def ImportField(self, import_field: Field):
        """
        Setter for property: (@link Field NXOpen.Fields.Field@endlink) ImportField
         Returns the imported field   
            
         
        """
        pass
    
    ## Getter for property: (str) ImportFile
    ##  Returns the import file   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def ImportFile(self) -> str:
        """
        Getter for property: (str) ImportFile
         Returns the import file   
            
         
        """
        pass
    
    ## Setter for property: (str) ImportFile

    ##  Returns the import file   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ImportFile.setter
    def ImportFile(self, filename: str):
        """
        Setter for property: (str) ImportFile
         Returns the import file   
            
         
        """
        pass
    
    ## Getter for property: (bool) ImportFolders
    ##  Returns the import folders option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def ImportFolders(self) -> bool:
        """
        Getter for property: (bool) ImportFolders
         Returns the import folders option   
            
         
        """
        pass
    
    ## Setter for property: (bool) ImportFolders

    ##  Returns the import folders option   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ImportFolders.setter
    def ImportFolders(self, importFolders: bool):
        """
        Setter for property: (bool) ImportFolders
         Returns the import folders option   
            
         
        """
        pass
    
    ## Getter for property: (str) PrependString
    ##  Returns the prepend string   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def PrependString(self) -> str:
        """
        Getter for property: (str) PrependString
         Returns the prepend string   
            
         
        """
        pass
    
    ## Setter for property: (str) PrependString

    ##  Returns the prepend string   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @PrependString.setter
    def PrependString(self, prependString: str):
        """
        Setter for property: (str) PrependString
         Returns the prepend string   
            
         
        """
        pass
    
    ##  Get the import action 
    ##  @return action (int): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1980.0.0.  Use @link NXOpen::Fields::ImportBuilder::GetNthImportAction NXOpen::Fields::ImportBuilder::GetNthImportAction@endlink  instead.  <br> 

    ## License requirements: None.
    ## 
    ## <param name="nthField"> (int) </param>
    def GetImportAction(self, nthField: int) -> int:
        """
         Get the import action 
         @return action (int): .
        """
        pass
    
    ##  Get the nth field conflict type 
    ##  @return conflict (@link ImportBuilder.ConflictType NXOpen.Fields.ImportBuilder.ConflictType@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="nthField"> (int) </param>
    def GetNthConflictType(self, nthField: int) -> ImportBuilder.ConflictType:
        """
         Get the nth field conflict type 
         @return conflict (@link ImportBuilder.ConflictType NXOpen.Fields.ImportBuilder.ConflictType@endlink): .
        """
        pass
    
    ##  Get the nth field name 
    ##  @return importFieldName (str): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="nthField"> (int) </param>
    def GetNthFieldName(self, nthField: int) -> str:
        """
         Get the nth field name 
         @return importFieldName (str): .
        """
        pass
    
    ##  Get the nth field import action 
    ##  @return action (@link ImportBuilder.ActionType NXOpen.Fields.ImportBuilder.ActionType@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="nthField"> (int) </param>
    def GetNthImportAction(self, nthField: int) -> ImportBuilder.ActionType:
        """
         Get the nth field import action 
         @return action (@link ImportBuilder.ActionType NXOpen.Fields.ImportBuilder.ActionType@endlink): .
        """
        pass
    
    ##  Get the number of fields in import file 
    ##  @return numberOfFields (int): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    def GetNumFields(self) -> int:
        """
         Get the number of fields in import file 
         @return numberOfFields (int): .
        """
        pass
    
    ##  Set the import action 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1980.0.0.  Use @link NXOpen::Fields::ImportBuilder::SetNthImportAction NXOpen::Fields::ImportBuilder::SetNthImportAction@endlink  instead.  <br> 

    ## License requirements: None.
    ## 
    ## <param name="nthField"> (int) </param>
    ## <param name="action"> (int) </param>
    def SetImportAction(self, nthField: int, action: int) -> None:
        """
         Set the import action 
        """
        pass
    
    ##  Set the nth field import action 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="nthField"> (int) </param>
    ## <param name="action"> (@link ImportBuilder.ActionType NXOpen.Fields.ImportBuilder.ActionType@endlink) </param>
    def SetNthImportAction(self, nthField: int, action: ImportBuilder.ActionType) -> None:
        """
         Set the nth field import action 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Fields::ImportTableDataBuilder NXOpen::Fields::ImportTableDataBuilder@endlink  builder 
##     which can be used to import data for @link NXOpen::Fields::FieldTable NXOpen::Fields::FieldTable@endlink   <br> To create a new instance of this class, use @link NXOpen::Fields::FieldManager::CreateImportTableDataBuilderFromTable  NXOpen::Fields::FieldManager::CreateImportTableDataBuilderFromTable @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class ImportTableDataBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Fields.ImportTableDataBuilder</ja_class> builder 
    which can be used to import data for <ja_class>NXOpen.Fields.FieldTable</ja_class> """


    ## Getter for property: (bool) CreateSpatialMap
    ##  Returns the create spatial map value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def CreateSpatialMap(self) -> bool:
        """
        Getter for property: (bool) CreateSpatialMap
         Returns the create spatial map value   
            
         
        """
        pass
    
    ## Setter for property: (bool) CreateSpatialMap

    ##  Returns the create spatial map value   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @CreateSpatialMap.setter
    def CreateSpatialMap(self, createSpatialMap: bool):
        """
        Setter for property: (bool) CreateSpatialMap
         Returns the create spatial map value   
            
         
        """
        pass
    
    ## Getter for property: (@link FieldTable.DuplicateValueOption NXOpen.Fields.FieldTable.DuplicateValueOption@endlink) DuplicateValues
    ##  Returns the duplicate value option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return FieldTable.DuplicateValueOption
    @property
    def DuplicateValues(self) -> FieldTable.DuplicateValueOption:
        """
        Getter for property: (@link FieldTable.DuplicateValueOption NXOpen.Fields.FieldTable.DuplicateValueOption@endlink) DuplicateValues
         Returns the duplicate value option   
            
         
        """
        pass
    
    ## Setter for property: (@link FieldTable.DuplicateValueOption NXOpen.Fields.FieldTable.DuplicateValueOption@endlink) DuplicateValues

    ##  Returns the duplicate value option   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @DuplicateValues.setter
    def DuplicateValues(self, duplicate_value_option: FieldTable.DuplicateValueOption):
        """
        Setter for property: (@link FieldTable.DuplicateValueOption NXOpen.Fields.FieldTable.DuplicateValueOption@endlink) DuplicateValues
         Returns the duplicate value option   
            
         
        """
        pass
    
    ## Getter for property: (str) ImportFile
    ##  Returns the import data file   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def ImportFile(self) -> str:
        """
        Getter for property: (str) ImportFile
         Returns the import data file   
            
         
        """
        pass
    
    ## Setter for property: (str) ImportFile

    ##  Returns the import data file   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ImportFile.setter
    def ImportFile(self, filename: str):
        """
        Setter for property: (str) ImportFile
         Returns the import data file   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsStructDataFormat
    ##  Returns the is structured data value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def IsStructDataFormat(self) -> bool:
        """
        Getter for property: (bool) IsStructDataFormat
         Returns the is structured data value   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsStructDataFormat

    ##  Returns the is structured data value   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @IsStructDataFormat.setter
    def IsStructDataFormat(self, structured_data_format: bool):
        """
        Setter for property: (bool) IsStructDataFormat
         Returns the is structured data value   
            
         
        """
        pass
    
    ## Getter for property: (int) NumStructDataColumns
    ##  Returns the number of structured data columns   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def NumStructDataColumns(self) -> int:
        """
        Getter for property: (int) NumStructDataColumns
         Returns the number of structured data columns   
            
         
        """
        pass
    
    ## Setter for property: (int) NumStructDataColumns

    ##  Returns the number of structured data columns   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @NumStructDataColumns.setter
    def NumStructDataColumns(self, numColumns: int):
        """
        Setter for property: (int) NumStructDataColumns
         Returns the number of structured data columns   
            
         
        """
        pass
    
    ## Getter for property: (int) NumStructDataPlanes
    ##  Returns the number of structured data planes   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def NumStructDataPlanes(self) -> int:
        """
        Getter for property: (int) NumStructDataPlanes
         Returns the number of structured data planes   
            
         
        """
        pass
    
    ## Setter for property: (int) NumStructDataPlanes

    ##  Returns the number of structured data planes   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @NumStructDataPlanes.setter
    def NumStructDataPlanes(self, numPlanes: int):
        """
        Setter for property: (int) NumStructDataPlanes
         Returns the number of structured data planes   
            
         
        """
        pass
    
    ## Getter for property: (int) NumStructDataRows
    ##  Returns the number of structured data rows   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def NumStructDataRows(self) -> int:
        """
        Getter for property: (int) NumStructDataRows
         Returns the number of structured data rows   
            
         
        """
        pass
    
    ## Setter for property: (int) NumStructDataRows

    ##  Returns the number of structured data rows   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @NumStructDataRows.setter
    def NumStructDataRows(self, numRows: int):
        """
        Setter for property: (int) NumStructDataRows
         Returns the number of structured data rows   
            
         
        """
        pass
    
    ##  TODO: fill in a description for this 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def RescanImportFile(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    
    ##  TODO: fill in a description for this 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def SetClearTableOnImport(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##   @brief 
##             Represents a builder class for creating and editing an @link NXOpen::Fields::Field NXOpen::Fields::Field@endlink 
##             that is defined by manual input data.
##          
## 
##  
## 
##   <br>  Created in NX1926.0.0  <br> 

class ManualInputProfileBuilder(NXOpen.TaggedObject): 
    """ <summary>
            Represents a builder class for creating and editing an <ja_class>NXOpen.Fields.Field</ja_class>
            that is defined by manual input data.
        </summary>"""


    ##   @brief 
    ##             Defines if the profile is repeating cyclically in any direction.
    ##          
    ## 
    ##  
    ##         
    ##             This is overriding extrapolation, if not set to
    ##             @link NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeNone NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeNone@endlink .
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ##  not cyclic </description> </item><item><term> 
    ## XOnly</term><description> 
    ##  cyclic in x direction </description> </item></list>
    class CyclicType(Enum):
        """
        Members Include: <NotSet> <XOnly>
        """
        NotSet: int
        XOnly: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ManualInputProfileBuilder.CyclicType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##   @brief 
    ##             the extrapolation method used for the profile
    ##          
    ## 
    ##   
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Linear</term><description> 
    ##  Linear </description> </item><item><term> 
    ## Parabolic</term><description> 
    ##  Parabolic </description> </item></list>
    class Extrapolation(Enum):
        """
        Members Include: <Linear> <Parabolic>
        """
        Linear: int
        Parabolic: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ManualInputProfileBuilder.Extrapolation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##   @brief 
    ##             the interpolation method used for the profile
    ##          
    ## 
    ##   
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Linear</term><description> 
    ##  Linear </description> </item><item><term> 
    ## Akima</term><description> 
    ##  Akima </description> </item><item><term> 
    ## Akima72</term><description> 
    ##  Akima72 </description> </item><item><term> 
    ## Cubic</term><description> 
    ##  Cubic </description> </item></list>
    class Interpolation(Enum):
        """
        Members Include: <Linear> <Akima> <Akima72> <Cubic>
        """
        Linear: int
        Akima: int
        Akima72: int
        Cubic: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ManualInputProfileBuilder.Interpolation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link ManualInputProfileBuilder.CyclicType NXOpen.Fields.ManualInputProfileBuilder.CyclicType@endlink) Cyclic
    ##  Returns  @brief 
    ##             the cyclic type.  
    ##   
    ##          
    ## 
    ##  
    ##         
    ##             <ul>
    ##               <li>@link NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeNone NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeNone@endlink </li>
    ##               <li>@link NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeXOnly NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeXOnly@endlink </li>
    ##             </ul>
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link NXOpen::Fields::ProfileSolverOptionsBuilder::Cyclic NXOpen::Fields::ProfileSolverOptionsBuilder::Cyclic@endlink  instead.  <br> 

    ## @return ManualInputProfileBuilder.CyclicType
    @property
    def Cyclic(self) -> ManualInputProfileBuilder.CyclicType:
        """
        Getter for property: (@link ManualInputProfileBuilder.CyclicType NXOpen.Fields.ManualInputProfileBuilder.CyclicType@endlink) Cyclic
         Returns  @brief 
                    the cyclic type.  
          
                 
        
         
                
                    <ul>
                      <li>@link NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeNone NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeNone@endlink </li>
                      <li>@link NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeXOnly NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeXOnly@endlink </li>
                    </ul>
                  
         
        """
        pass
    
    ## Setter for property: (@link ManualInputProfileBuilder.CyclicType NXOpen.Fields.ManualInputProfileBuilder.CyclicType@endlink) Cyclic

    ##  Returns  @brief 
    ##             the cyclic type.  
    ##   
    ##          
    ## 
    ##  
    ##         
    ##             <ul>
    ##               <li>@link NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeNone NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeNone@endlink </li>
    ##               <li>@link NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeXOnly NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeXOnly@endlink </li>
    ##             </ul>
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link NXOpen::Fields::ProfileSolverOptionsBuilder::SetCyclic NXOpen::Fields::ProfileSolverOptionsBuilder::SetCyclic@endlink  instead.  <br> 

    @Cyclic.setter
    def Cyclic(self, cyclicType: ManualInputProfileBuilder.CyclicType):
        """
        Setter for property: (@link ManualInputProfileBuilder.CyclicType NXOpen.Fields.ManualInputProfileBuilder.CyclicType@endlink) Cyclic
         Returns  @brief 
                    the cyclic type.  
          
                 
        
         
                
                    <ul>
                      <li>@link NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeNone NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeNone@endlink </li>
                      <li>@link NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeXOnly NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeXOnly@endlink </li>
                    </ul>
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OrdinateOffset
    ##  Returns  @brief 
    ##             the offset on the ordinate axis.  
    ##   
    ##          
    ## 
    ##    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def OrdinateOffset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OrdinateOffset
         Returns  @brief 
                    the offset on the ordinate axis.  
          
                 
        
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OrdinateScale
    ##  Returns  @brief 
    ##             the scale on the ordinate axis.  
    ##   
    ##          
    ## 
    ##  
    ##         The scale is unitless.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def OrdinateScale(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OrdinateScale
         Returns  @brief 
                    the scale on the ordinate axis.  
          
                 
        
         
                The scale is unitless.  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) OrdinateUnitType
    ##  Returns  @brief the unit type corresponding to the ordinate axis.  
    ##    
    ## 
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Unit
    @property
    def OrdinateUnitType(self) -> NXOpen.Unit:
        """
        Getter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) OrdinateUnitType
         Returns  @brief the unit type corresponding to the ordinate axis.  
           
        
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) OrdinateUnitType

    ##  Returns  @brief the unit type corresponding to the ordinate axis.  
    ##    
    ## 
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @OrdinateUnitType.setter
    def OrdinateUnitType(self, unitType: NXOpen.Unit):
        """
        Setter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) OrdinateUnitType
         Returns  @brief the unit type corresponding to the ordinate axis.  
           
        
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SlopeLeft
    ##  Returns  @brief 
    ##             the left slope.  
    ##   
    ##          
    ## 
    ##  
    ##         
    ##             This is only used when @link NXOpen::Fields::ManualInputProfileBuilder::CyclicType NXOpen::Fields::ManualInputProfileBuilder::CyclicType@endlink 
    ##             is set to @link NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeNone NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeNone@endlink 
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link NXOpen::Fields::ProfileSolverOptionsBuilder::SlopeLeft NXOpen::Fields::ProfileSolverOptionsBuilder::SlopeLeft@endlink  instead.  <br> 

    ## @return NXOpen.Expression
    @property
    def SlopeLeft(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SlopeLeft
         Returns  @brief 
                    the left slope.  
          
                 
        
         
                
                    This is only used when @link NXOpen::Fields::ManualInputProfileBuilder::CyclicType NXOpen::Fields::ManualInputProfileBuilder::CyclicType@endlink 
                    is set to @link NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeNone NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeNone@endlink 
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SlopeRight
    ##  Returns  @brief 
    ##             the right slope.  
    ##   
    ##          
    ## 
    ##  
    ##         
    ##             This is only used when @link NXOpen::Fields::ManualInputProfileBuilder::CyclicType NXOpen::Fields::ManualInputProfileBuilder::CyclicType@endlink 
    ##             is set to @link NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeNone NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeNone@endlink 
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link NXOpen::Fields::ProfileSolverOptionsBuilder::SlopeRight NXOpen::Fields::ProfileSolverOptionsBuilder::SlopeRight@endlink  instead.  <br> 

    ## @return NXOpen.Expression
    @property
    def SlopeRight(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SlopeRight
         Returns  @brief 
                    the right slope.  
          
                 
        
         
                
                    This is only used when @link NXOpen::Fields::ManualInputProfileBuilder::CyclicType NXOpen::Fields::ManualInputProfileBuilder::CyclicType@endlink 
                    is set to @link NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeNone NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeNone@endlink 
                  
         
        """
        pass
    
    ## Getter for property: (@link ProfileSolverOptionsBuilder NXOpen.Fields.ProfileSolverOptionsBuilder@endlink) SolverOptions
    ##  Returns  @brief the solver options.  
    ##    
    ## 
    ##    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return ProfileSolverOptionsBuilder
    @property
    def SolverOptions(self) -> ProfileSolverOptionsBuilder:
        """
        Getter for property: (@link ProfileSolverOptionsBuilder NXOpen.Fields.ProfileSolverOptionsBuilder@endlink) SolverOptions
         Returns  @brief the solver options.  
           
        
           
         
        """
        pass
    
    ## Getter for property: (@link ManualInputProfileBuilder.Extrapolation NXOpen.Fields.ManualInputProfileBuilder.Extrapolation@endlink) XExtrapolation
    ##  Returns  @brief 
    ##             the extrapolation in x direction.  
    ##   
    ##          
    ## 
    ##  
    ##         
    ##             <ul>
    ##               <li>@link NXOpen::Fields::ManualInputProfileBuilder::ExtrapolationLinear NXOpen::Fields::ManualInputProfileBuilder::ExtrapolationLinear@endlink </li>
    ##               <li>@link NXOpen::Fields::ManualInputProfileBuilder::ExtrapolationParabolic NXOpen::Fields::ManualInputProfileBuilder::ExtrapolationParabolic@endlink </li>
    ##             </ul>
    ##              <br> 
    ##                 This is only used when @link NXOpen::Fields::ManualInputProfileBuilder::CyclicType NXOpen::Fields::ManualInputProfileBuilder::CyclicType@endlink 
    ##                 is set to @link NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeNone NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeNone@endlink 
    ##              <br> 
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link NXOpen::Fields::ProfileSolverOptionsBuilder::XExtrapolation NXOpen::Fields::ProfileSolverOptionsBuilder::XExtrapolation@endlink  instead.  <br> 

    ## @return ManualInputProfileBuilder.Extrapolation
    @property
    def XExtrapolation(self) -> ManualInputProfileBuilder.Extrapolation:
        """
        Getter for property: (@link ManualInputProfileBuilder.Extrapolation NXOpen.Fields.ManualInputProfileBuilder.Extrapolation@endlink) XExtrapolation
         Returns  @brief 
                    the extrapolation in x direction.  
          
                 
        
         
                
                    <ul>
                      <li>@link NXOpen::Fields::ManualInputProfileBuilder::ExtrapolationLinear NXOpen::Fields::ManualInputProfileBuilder::ExtrapolationLinear@endlink </li>
                      <li>@link NXOpen::Fields::ManualInputProfileBuilder::ExtrapolationParabolic NXOpen::Fields::ManualInputProfileBuilder::ExtrapolationParabolic@endlink </li>
                    </ul>
                     <br> 
                        This is only used when @link NXOpen::Fields::ManualInputProfileBuilder::CyclicType NXOpen::Fields::ManualInputProfileBuilder::CyclicType@endlink 
                        is set to @link NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeNone NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeNone@endlink 
                     <br> 
                  
         
        """
        pass
    
    ## Setter for property: (@link ManualInputProfileBuilder.Extrapolation NXOpen.Fields.ManualInputProfileBuilder.Extrapolation@endlink) XExtrapolation

    ##  Returns  @brief 
    ##             the extrapolation in x direction.  
    ##   
    ##          
    ## 
    ##  
    ##         
    ##             <ul>
    ##               <li>@link NXOpen::Fields::ManualInputProfileBuilder::ExtrapolationLinear NXOpen::Fields::ManualInputProfileBuilder::ExtrapolationLinear@endlink </li>
    ##               <li>@link NXOpen::Fields::ManualInputProfileBuilder::ExtrapolationParabolic NXOpen::Fields::ManualInputProfileBuilder::ExtrapolationParabolic@endlink </li>
    ##             </ul>
    ##              <br> 
    ##                 This is only used when @link NXOpen::Fields::ManualInputProfileBuilder::CyclicType NXOpen::Fields::ManualInputProfileBuilder::CyclicType@endlink 
    ##                 is set to @link NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeNone NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeNone@endlink 
    ##              <br> 
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link NXOpen::Fields::ProfileSolverOptionsBuilder::SetXExtrapolation NXOpen::Fields::ProfileSolverOptionsBuilder::SetXExtrapolation@endlink  instead.  <br> 

    @XExtrapolation.setter
    def XExtrapolation(self, extrapolation: ManualInputProfileBuilder.Extrapolation):
        """
        Setter for property: (@link ManualInputProfileBuilder.Extrapolation NXOpen.Fields.ManualInputProfileBuilder.Extrapolation@endlink) XExtrapolation
         Returns  @brief 
                    the extrapolation in x direction.  
          
                 
        
         
                
                    <ul>
                      <li>@link NXOpen::Fields::ManualInputProfileBuilder::ExtrapolationLinear NXOpen::Fields::ManualInputProfileBuilder::ExtrapolationLinear@endlink </li>
                      <li>@link NXOpen::Fields::ManualInputProfileBuilder::ExtrapolationParabolic NXOpen::Fields::ManualInputProfileBuilder::ExtrapolationParabolic@endlink </li>
                    </ul>
                     <br> 
                        This is only used when @link NXOpen::Fields::ManualInputProfileBuilder::CyclicType NXOpen::Fields::ManualInputProfileBuilder::CyclicType@endlink 
                        is set to @link NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeNone NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeNone@endlink 
                     <br> 
                  
         
        """
        pass
    
    ## Getter for property: (@link ManualInputProfileBuilder.Interpolation NXOpen.Fields.ManualInputProfileBuilder.Interpolation@endlink) XInterpolation
    ##  Returns  @brief 
    ##             the interpolation in x direction.  
    ##   
    ##          
    ## 
    ##  
    ##         
    ##             <ul>
    ##               <li>@link NXOpen::Fields::ManualInputProfileBuilder::InterpolationLinear NXOpen::Fields::ManualInputProfileBuilder::InterpolationLinear@endlink </li>
    ##               <li>@link NXOpen::Fields::ManualInputProfileBuilder::InterpolationAkima NXOpen::Fields::ManualInputProfileBuilder::InterpolationAkima@endlink </li>
    ##               <li>@link NXOpen::Fields::ManualInputProfileBuilder::InterpolationAkima72 NXOpen::Fields::ManualInputProfileBuilder::InterpolationAkima72@endlink </li>
    ##               <li>@link NXOpen::Fields::ManualInputProfileBuilder::InterpolationCubic NXOpen::Fields::ManualInputProfileBuilder::InterpolationCubic@endlink </li>
    ##             </ul>
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link NXOpen::Fields::ProfileSolverOptionsBuilder::XInterpolation NXOpen::Fields::ProfileSolverOptionsBuilder::XInterpolation@endlink  instead.  <br> 

    ## @return ManualInputProfileBuilder.Interpolation
    @property
    def XInterpolation(self) -> ManualInputProfileBuilder.Interpolation:
        """
        Getter for property: (@link ManualInputProfileBuilder.Interpolation NXOpen.Fields.ManualInputProfileBuilder.Interpolation@endlink) XInterpolation
         Returns  @brief 
                    the interpolation in x direction.  
          
                 
        
         
                
                    <ul>
                      <li>@link NXOpen::Fields::ManualInputProfileBuilder::InterpolationLinear NXOpen::Fields::ManualInputProfileBuilder::InterpolationLinear@endlink </li>
                      <li>@link NXOpen::Fields::ManualInputProfileBuilder::InterpolationAkima NXOpen::Fields::ManualInputProfileBuilder::InterpolationAkima@endlink </li>
                      <li>@link NXOpen::Fields::ManualInputProfileBuilder::InterpolationAkima72 NXOpen::Fields::ManualInputProfileBuilder::InterpolationAkima72@endlink </li>
                      <li>@link NXOpen::Fields::ManualInputProfileBuilder::InterpolationCubic NXOpen::Fields::ManualInputProfileBuilder::InterpolationCubic@endlink </li>
                    </ul>
                  
         
        """
        pass
    
    ## Setter for property: (@link ManualInputProfileBuilder.Interpolation NXOpen.Fields.ManualInputProfileBuilder.Interpolation@endlink) XInterpolation

    ##  Returns  @brief 
    ##             the interpolation in x direction.  
    ##   
    ##          
    ## 
    ##  
    ##         
    ##             <ul>
    ##               <li>@link NXOpen::Fields::ManualInputProfileBuilder::InterpolationLinear NXOpen::Fields::ManualInputProfileBuilder::InterpolationLinear@endlink </li>
    ##               <li>@link NXOpen::Fields::ManualInputProfileBuilder::InterpolationAkima NXOpen::Fields::ManualInputProfileBuilder::InterpolationAkima@endlink </li>
    ##               <li>@link NXOpen::Fields::ManualInputProfileBuilder::InterpolationAkima72 NXOpen::Fields::ManualInputProfileBuilder::InterpolationAkima72@endlink </li>
    ##               <li>@link NXOpen::Fields::ManualInputProfileBuilder::InterpolationCubic NXOpen::Fields::ManualInputProfileBuilder::InterpolationCubic@endlink </li>
    ##             </ul>
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link NXOpen::Fields::ProfileSolverOptionsBuilder::SetXInterpolation NXOpen::Fields::ProfileSolverOptionsBuilder::SetXInterpolation@endlink  instead.  <br> 

    @XInterpolation.setter
    def XInterpolation(self, interpolation: ManualInputProfileBuilder.Interpolation):
        """
        Setter for property: (@link ManualInputProfileBuilder.Interpolation NXOpen.Fields.ManualInputProfileBuilder.Interpolation@endlink) XInterpolation
         Returns  @brief 
                    the interpolation in x direction.  
          
                 
        
         
                
                    <ul>
                      <li>@link NXOpen::Fields::ManualInputProfileBuilder::InterpolationLinear NXOpen::Fields::ManualInputProfileBuilder::InterpolationLinear@endlink </li>
                      <li>@link NXOpen::Fields::ManualInputProfileBuilder::InterpolationAkima NXOpen::Fields::ManualInputProfileBuilder::InterpolationAkima@endlink </li>
                      <li>@link NXOpen::Fields::ManualInputProfileBuilder::InterpolationAkima72 NXOpen::Fields::ManualInputProfileBuilder::InterpolationAkima72@endlink </li>
                      <li>@link NXOpen::Fields::ManualInputProfileBuilder::InterpolationCubic NXOpen::Fields::ManualInputProfileBuilder::InterpolationCubic@endlink </li>
                    </ul>
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XOffset
    ##  Returns  @brief 
    ##             the offset on the x axis.  
    ##   
    ##          
    ## 
    ##    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def XOffset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XOffset
         Returns  @brief 
                    the offset on the x axis.  
          
                 
        
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XScale
    ##  Returns  @brief 
    ##             the scale on the x axis.  
    ##   
    ##          
    ## 
    ##  
    ##         The scale is unitless.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def XScale(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XScale
         Returns  @brief 
                    the scale on the x axis.  
          
                 
        
         
                The scale is unitless.  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) XUnitType
    ##  Returns  @brief the unit type corresponding to the x axis.  
    ##    
    ## 
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Unit
    @property
    def XUnitType(self) -> NXOpen.Unit:
        """
        Getter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) XUnitType
         Returns  @brief the unit type corresponding to the x axis.  
           
        
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) XUnitType

    ##  Returns  @brief the unit type corresponding to the x axis.  
    ##    
    ## 
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @XUnitType.setter
    def XUnitType(self, unitType: NXOpen.Unit):
        """
        Setter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) XUnitType
         Returns  @brief the unit type corresponding to the x axis.  
           
        
            
         
        """
        pass
    
    ##   @brief 
    ##             Sets the data point expressions.
    ##          
    ## 
    ##  
    ##         
    ##             Some or all data points can be overridden by expressions.
    ##             The cell ids for the cells to be defined by an expression need to be given in the form: row * numColumns + column.
    ##             For 2D curves numColumn = 2.
    ##             The expression is defined in a string. e.g. "1+2" or "3[m]"
    ##         
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="dataPointCellIds"> (List[int]) </param>
    ## <param name="dataPointExpressions"> (List[str]) </param>
    def SetDataPointExpressions(self, dataPointCellIds: List[int], dataPointExpressions: List[str]) -> None:
        """
          @brief 
                    Sets the data point expressions.
                 
        
         
                
                    Some or all data points can be overridden by expressions.
                    The cell ids for the cells to be defined by an expression need to be given in the form: row * numColumns + column.
                    For 2D curves numColumn = 2.
                    The expression is defined in a string. e.g. "1+2" or "3[m]"
                
        """
        pass
    
    ##   @brief 
    ##             Sets the data point values.
    ##          
    ## 
    ##  
    ##         
    ##             The data points are listed as double values row after row.
    ##             e.g. 3 Curve points (1, 3.4), (2.5, 6.7), (4.25, -3.1)
    ##             appear as 1, 3.4, 2.5, 6.7, 4.25, -3.1
    ##         
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="dataPoints"> (List[float]) </param>
    def SetDataPointValues(self, dataPoints: List[float]) -> None:
        """
          @brief 
                    Sets the data point values.
                 
        
         
                
                    The data points are listed as double values row after row.
                    e.g. 3 Curve points (1, 3.4), (2.5, 6.7), (4.25, -3.1)
                    appear as 1, 3.4, 2.5, 6.7, 4.25, -3.1
                
        """
        pass
    
    ##   @brief 
    ##             If the measures are marked as fixed and they are changed, the validation at commit will detect an error and fail.
    ##          
    ## 
    ##  
    ##         
    ##             It is recommended to call this method when editing a profile that is referenced by another object,
    ##             which depends on specific measures.
    ##         
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="areMeasuresFixed"> (bool)  true, if changed measures should prevent a commit </param>
    def SetMeasuresFixed(self, areMeasuresFixed: bool) -> None:
        """
          @brief 
                    If the measures are marked as fixed and they are changed, the validation at commit will detect an error and fail.
                 
        
         
                
                    It is recommended to call this method when editing a profile that is referenced by another object,
                    which depends on specific measures.
                
        """
        pass
    
##   @brief  Represents the Manual Input Profile class. 
## 
##    <br> To obtain an instance of this class use @link NXOpen::Fields::FieldManager NXOpen::Fields::FieldManager@endlink  .  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class ManualInputProfile(FieldTable): 
    """ <summary> Represents the Manual Input Profile class.</summary> """
    pass


import NXOpen
##  This class stores the common name and measure for field variables. 
## 
##   <br>  Created in NX6.0.2  <br> 

class NameVariable(NXOpen.NXObject): 
    """ This class stores the common name and measure for field variables. """


    ## Getter for property: (str) Measure
    ##  Returns the measure of the variable   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.2  <br> 

    ## @return str
    @property
    def Measure(self) -> str:
        """
        Getter for property: (str) Measure
         Returns the measure of the variable   
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the name of the variable   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.2  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name of the variable   
            
         
        """
        pass
    
import NXOpen
##  Represents a list of objects. <br> To create a new instance of this class, use @link NXOpen::Part::CreateObjectList  NXOpen::Part::CreateObjectList @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class PathObjectsList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""


    ## Getter for property: (int) Length
    ##  Returns the length of the list   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    
    ##  Appends a set of objects to the list
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link PathObjectsList NXOpen.Fields.PathObjectsList@endlink) </param>
    ## <param name="objects"> (@link PathObjects List[NXOpen.Fields.PathObjects]@endlink)  items to append </param>
    @overload
    def Append(self, objects: List[PathObjects]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    
    ##  Appends an object to the list
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link PathObjectsList NXOpen.Fields.PathObjectsList@endlink) </param>
    ## <param name="objectValue"> (@link PathObjects NXOpen.Fields.PathObjects@endlink)  item to append </param>
    @overload
    def Append(self, objectValue: PathObjects) -> None:
        """
         Appends an object to the list
            
        """
        pass
    
    ##  Clears the entire list without deleting the objects.  The caller is responsible for 
    ##         accounting for these objects.  If they are not used or deleted by the time the part is 
    ##         closed (in other words, leaked) an error will occur 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link PathObjectsList NXOpen.Fields.PathObjectsList@endlink) </param>
    @overload
    def Clear(self) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    
    ##  Deletes the item at the index specified.  The size of the list does
    ##     *   not change, but the item at this index is set to NULL.
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="delete_idx"> (int)  index of item to be deleted </param>
    def ClearIndex(self, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
            *   not change, but the item at this index is set to NULL.
            
        """
        pass
    
    ##  Clears the entire list 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link PathObjectsList NXOpen.Fields.PathObjectsList@endlink) </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the objects when removing them </param>
    @overload
    def Clear(self, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    
    ##  Erases the object from the list, but does not delete the object.
    ##         The list is shifted so that there isn't a null where the object used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link PathObjectsList NXOpen.Fields.PathObjectsList@endlink) </param>
    ## <param name="index"> (int)  index of item to be removed from the list </param>
    @overload
    def Erase(self, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    
    ##  Erases the object at the given position from the list.
    ##         The list is shifted so that there isn't a null where the object used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link PathObjectsList NXOpen.Fields.PathObjectsList@endlink) </param>
    ## <param name="index"> (int)  index of item to be removed from the list </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the object </param>
    @overload
    def Erase(self, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    
    ##  Erases the object from the list, but does not delete the object.
    ##         The list is shifted so that there isn't a null where the object used to exist. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link PathObjectsList NXOpen.Fields.PathObjectsList@endlink) </param>
    ## <param name="obj"> (@link PathObjects NXOpen.Fields.PathObjects@endlink)  object to be removed from the list </param>
    @overload
    def Erase(self, obj: PathObjects) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    
    ##  Erases the object from the list.
    ##         The list is shifted so that there isn't a null where the object used to exist. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link PathObjectsList NXOpen.Fields.PathObjectsList@endlink) </param>
    ## <param name="obj"> (@link PathObjects NXOpen.Fields.PathObjects@endlink)  object to be removed from the list </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the object </param>
    @overload
    def Erase(self, obj: PathObjects, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    
    ##  Finds the index where the input object appears.  If it does not appear,
    ##     *   -1 is returned.
    ##     
    ##  @return index (int):  index of input object, -1 if not on list .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="obj"> (@link PathObjects NXOpen.Fields.PathObjects@endlink)  Object to find index for </param>
    def FindIndex(self, obj: PathObjects) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
            *   -1 is returned.
            
         @return index (int):  index of input object, -1 if not on list .
        """
        pass
    
    ##  Returns the object at the input index.  May be NULL.
    ##     
    ##  @return obj (@link PathObjects NXOpen.Fields.PathObjects@endlink):  object found at input index .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  index of object to return </param>
    def FindItem(self, index: int) -> PathObjects:
        """
         Returns the object at the input index.  May be NULL.
            
         @return obj (@link PathObjects NXOpen.Fields.PathObjects@endlink):  object found at input index .
        """
        pass
    
    ##  Gets the contents of the entire list 
    ##  @return objects (@link PathObjects List[NXOpen.Fields.PathObjects]@endlink):  The list contents .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetContents(self) -> List[PathObjects]:
        """
         Gets the contents of the entire list 
         @return objects (@link PathObjects List[NXOpen.Fields.PathObjects]@endlink):  The list contents .
        """
        pass
    
    ##  Inserts an object at the specified location 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="location"> (int)  location at which to insert the object </param>
    ## <param name="objectValue"> (@link PathObjects NXOpen.Fields.PathObjects@endlink)  object to be inserted </param>
    def Insert(self, location: int, objectValue: PathObjects) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    
    ##  Move object at the specified location to the bottom of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  location of the item </param>
    def MoveToBottom(self, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    
    ##  Move object at the specified location to the top of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  location of the item </param>
    def MoveToTop(self, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    
    ##  Sets the contents of the entire list. This overwrites the previous contents of this list, 
    ##         but does not delete any objects that were originally on the list.
    ##      
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objects"> (@link PathObjects List[NXOpen.Fields.PathObjects]@endlink)  The list contents </param>
    def SetContents(self, objects: List[PathObjects]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    
    ##  Exchanges the position of two objects inside the list.
    ##         The first object is placed where the second used to be,
    ##         and second object where the first used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link PathObjectsList NXOpen.Fields.PathObjectsList@endlink) </param>
    ## <param name="index1"> (int)  location of the first item </param>
    ## <param name="index2"> (int)  location of the second item </param>
    @overload
    def Swap(self, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
    ##  Exchanges the position of two objects inside the list.
    ##         The first object is placed where the second used to be,
    ##         and second object where the first used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link PathObjectsList NXOpen.Fields.PathObjectsList@endlink) </param>
    ## <param name="object1"> (@link PathObjects NXOpen.Fields.PathObjects@endlink)  first item </param>
    ## <param name="object2"> (@link PathObjects NXOpen.Fields.PathObjects@endlink)  second item </param>
    @overload
    def Swap(self, object1: PathObjects, object2: PathObjects) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
import NXOpen
##   @brief  Contains objects that define a lattice path  
## 
##    <br> Not a KF builder; see Fields.FieldManager methods to create a Fields.PathObjects.  <br> 
## 
##   <br>  Created in NX6.0.1  <br> 

class PathObjects(NXOpen.SelectObjectList): 
    """ <summary> Contains objects that define a lattice path </summary> """


    ##  Check the direction of the lastest selection and reverse it if necessary 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def HandleLatestSelDirection(self) -> None:
        """
         Check the direction of the lastest selection and reverse it if necessary 
        """
        pass
    
    ##  Reverses the order of the objects in the path 
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    ## License requirements: None.
    def ReverseDirection(self) -> None:
        """
         Reverses the order of the objects in the path 
        """
        pass
    
    ##  Reverses the order of the objects in the path 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int) </param>
    def ReverseSectionDirection(self, index: int) -> None:
        """
         Reverses the order of the objects in the path 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##   @brief 
##             Represents a builder class to handle the solver options of an @link NXOpen::Fields::Field NXOpen::Fields::Field@endlink .
##          
## 
##  
## 
##   <br>  Created in NX1953.0.0  <br> 

class ProfileSolverOptionsBuilder(NXOpen.TaggedObject): 
    """ <summary>
            Represents a builder class to handle the solver options of an <ja_class>NXOpen.Fields.Field</ja_class>.
        </summary>"""


    ##   @brief 
    ##             Defines if the profile is repeating cyclically in any direction.
    ##          
    ## 
    ##  
    ##         
    ##             If not set to @link NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone@endlink ,
    ##             this trumps any @link NXOpen::Fields::ProfileSolverOptionsBuilder::Extrapolation NXOpen::Fields::ProfileSolverOptionsBuilder::Extrapolation@endlink  which might have been set.
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ##  not cyclic </description> </item><item><term> 
    ## XOnly</term><description> 
    ##  cyclic in x direction </description> </item><item><term> 
    ## YOnly</term><description> 
    ##  cyclic in y direction </description> </item><item><term> 
    ## Both</term><description> 
    ##  cyclic in both x and y direction </description> </item></list>
    class CyclicType(Enum):
        """
        Members Include: <NotSet> <XOnly> <YOnly> <Both>
        """
        NotSet: int
        XOnly: int
        YOnly: int
        Both: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ProfileSolverOptionsBuilder.CyclicType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##   @brief 
    ##             the extrapolation method used for the profile
    ##          
    ## 
    ##   
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Linear</term><description> 
    ##  Linear </description> </item><item><term> 
    ## Parabolic</term><description> 
    ##  Parabolic </description> </item><item><term> 
    ## Cubic</term><description> 
    ##  Cubic </description> </item></list>
    class Extrapolation(Enum):
        """
        Members Include: <Linear> <Parabolic> <Cubic>
        """
        Linear: int
        Parabolic: int
        Cubic: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ProfileSolverOptionsBuilder.Extrapolation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##   @brief 
    ##             the interpolation method used for the profile
    ##          
    ## 
    ##   
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Linear</term><description> 
    ##  Linear </description> </item><item><term> 
    ## Akima</term><description> 
    ##  Akima </description> </item><item><term> 
    ## Akima72</term><description> 
    ##  Akima72 </description> </item><item><term> 
    ## Cubic</term><description> 
    ##  Cubic </description> </item></list>
    class Interpolation(Enum):
        """
        Members Include: <Linear> <Akima> <Akima72> <Cubic>
        """
        Linear: int
        Akima: int
        Akima72: int
        Cubic: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ProfileSolverOptionsBuilder.Interpolation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link ProfileSolverOptionsBuilder.CyclicType NXOpen.Fields.ProfileSolverOptionsBuilder.CyclicType@endlink) Cyclic
    ##  Returns  @brief 
    ##             the cyclic type.  
    ##   
    ##          
    ## 
    ##  
    ##         
    ##             <ul>
    ##               <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone@endlink </li>
    ##               <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeXOnly NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeXOnly@endlink </li>
    ##             </ul>
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return ProfileSolverOptionsBuilder.CyclicType
    @property
    def Cyclic(self) -> ProfileSolverOptionsBuilder.CyclicType:
        """
        Getter for property: (@link ProfileSolverOptionsBuilder.CyclicType NXOpen.Fields.ProfileSolverOptionsBuilder.CyclicType@endlink) Cyclic
         Returns  @brief 
                    the cyclic type.  
          
                 
        
         
                
                    <ul>
                      <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone@endlink </li>
                      <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeXOnly NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeXOnly@endlink </li>
                    </ul>
                  
         
        """
        pass
    
    ## Setter for property: (@link ProfileSolverOptionsBuilder.CyclicType NXOpen.Fields.ProfileSolverOptionsBuilder.CyclicType@endlink) Cyclic

    ##  Returns  @brief 
    ##             the cyclic type.  
    ##   
    ##          
    ## 
    ##  
    ##         
    ##             <ul>
    ##               <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone@endlink </li>
    ##               <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeXOnly NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeXOnly@endlink </li>
    ##             </ul>
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @Cyclic.setter
    def Cyclic(self, cyclicType: ProfileSolverOptionsBuilder.CyclicType):
        """
        Setter for property: (@link ProfileSolverOptionsBuilder.CyclicType NXOpen.Fields.ProfileSolverOptionsBuilder.CyclicType@endlink) Cyclic
         Returns  @brief 
                    the cyclic type.  
          
                 
        
         
                
                    <ul>
                      <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone@endlink </li>
                      <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeXOnly NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeXOnly@endlink </li>
                    </ul>
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SlopeLeft
    ##  Returns  @brief 
    ##             the left slope.  
    ##   
    ##          
    ## 
    ##  
    ##         
    ##             This is only used when @link NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicType NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicType@endlink 
    ##             is set to @link NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone@endlink 
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SlopeLeft(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SlopeLeft
         Returns  @brief 
                    the left slope.  
          
                 
        
         
                
                    This is only used when @link NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicType NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicType@endlink 
                    is set to @link NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone@endlink 
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SlopeRight
    ##  Returns  @brief 
    ##             the right slope.  
    ##   
    ##          
    ## 
    ##  
    ##         
    ##             This is only used when @link NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicType NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicType@endlink 
    ##             is set to @link NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone@endlink 
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SlopeRight(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SlopeRight
         Returns  @brief 
                    the right slope.  
          
                 
        
         
                
                    This is only used when @link NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicType NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicType@endlink 
                    is set to @link NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone@endlink 
                  
         
        """
        pass
    
    ## Getter for property: (@link ProfileSolverOptionsBuilder.Extrapolation NXOpen.Fields.ProfileSolverOptionsBuilder.Extrapolation@endlink) XExtrapolation
    ##  Returns  @brief 
    ##             the extrapolation in x direction.  
    ##   
    ##          
    ## 
    ##  
    ##         
    ##             <ul>
    ##               <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationLinear NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationLinear@endlink </li>
    ##               <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationParabolic NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationParabolic@endlink </li>
    ##             </ul>
    ##              <br> 
    ##                 This is only used when @link NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicType NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicType@endlink 
    ##                 is set to @link NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone@endlink 
    ##              <br> 
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return ProfileSolverOptionsBuilder.Extrapolation
    @property
    def XExtrapolation(self) -> ProfileSolverOptionsBuilder.Extrapolation:
        """
        Getter for property: (@link ProfileSolverOptionsBuilder.Extrapolation NXOpen.Fields.ProfileSolverOptionsBuilder.Extrapolation@endlink) XExtrapolation
         Returns  @brief 
                    the extrapolation in x direction.  
          
                 
        
         
                
                    <ul>
                      <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationLinear NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationLinear@endlink </li>
                      <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationParabolic NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationParabolic@endlink </li>
                    </ul>
                     <br> 
                        This is only used when @link NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicType NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicType@endlink 
                        is set to @link NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone@endlink 
                     <br> 
                  
         
        """
        pass
    
    ## Setter for property: (@link ProfileSolverOptionsBuilder.Extrapolation NXOpen.Fields.ProfileSolverOptionsBuilder.Extrapolation@endlink) XExtrapolation

    ##  Returns  @brief 
    ##             the extrapolation in x direction.  
    ##   
    ##          
    ## 
    ##  
    ##         
    ##             <ul>
    ##               <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationLinear NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationLinear@endlink </li>
    ##               <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationParabolic NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationParabolic@endlink </li>
    ##             </ul>
    ##              <br> 
    ##                 This is only used when @link NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicType NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicType@endlink 
    ##                 is set to @link NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone@endlink 
    ##              <br> 
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @XExtrapolation.setter
    def XExtrapolation(self, extrapolation: ProfileSolverOptionsBuilder.Extrapolation):
        """
        Setter for property: (@link ProfileSolverOptionsBuilder.Extrapolation NXOpen.Fields.ProfileSolverOptionsBuilder.Extrapolation@endlink) XExtrapolation
         Returns  @brief 
                    the extrapolation in x direction.  
          
                 
        
         
                
                    <ul>
                      <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationLinear NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationLinear@endlink </li>
                      <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationParabolic NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationParabolic@endlink </li>
                    </ul>
                     <br> 
                        This is only used when @link NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicType NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicType@endlink 
                        is set to @link NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone@endlink 
                     <br> 
                  
         
        """
        pass
    
    ## Getter for property: (@link ProfileSolverOptionsBuilder.Interpolation NXOpen.Fields.ProfileSolverOptionsBuilder.Interpolation@endlink) XInterpolation
    ##  Returns  @brief 
    ##             the interpolation in x direction.  
    ##   
    ##          
    ## 
    ##  
    ##         
    ##             <ul>
    ##               <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationLinear NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationLinear@endlink </li>
    ##               <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima@endlink </li>
    ##               <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima72 NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima72@endlink </li>
    ##               <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationCubic NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationCubic@endlink </li>
    ##             </ul>
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return ProfileSolverOptionsBuilder.Interpolation
    @property
    def XInterpolation(self) -> ProfileSolverOptionsBuilder.Interpolation:
        """
        Getter for property: (@link ProfileSolverOptionsBuilder.Interpolation NXOpen.Fields.ProfileSolverOptionsBuilder.Interpolation@endlink) XInterpolation
         Returns  @brief 
                    the interpolation in x direction.  
          
                 
        
         
                
                    <ul>
                      <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationLinear NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationLinear@endlink </li>
                      <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima@endlink </li>
                      <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima72 NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima72@endlink </li>
                      <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationCubic NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationCubic@endlink </li>
                    </ul>
                  
         
        """
        pass
    
    ## Setter for property: (@link ProfileSolverOptionsBuilder.Interpolation NXOpen.Fields.ProfileSolverOptionsBuilder.Interpolation@endlink) XInterpolation

    ##  Returns  @brief 
    ##             the interpolation in x direction.  
    ##   
    ##          
    ## 
    ##  
    ##         
    ##             <ul>
    ##               <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationLinear NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationLinear@endlink </li>
    ##               <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima@endlink </li>
    ##               <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima72 NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima72@endlink </li>
    ##               <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationCubic NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationCubic@endlink </li>
    ##             </ul>
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @XInterpolation.setter
    def XInterpolation(self, interpolation: ProfileSolverOptionsBuilder.Interpolation):
        """
        Setter for property: (@link ProfileSolverOptionsBuilder.Interpolation NXOpen.Fields.ProfileSolverOptionsBuilder.Interpolation@endlink) XInterpolation
         Returns  @brief 
                    the interpolation in x direction.  
          
                 
        
         
                
                    <ul>
                      <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationLinear NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationLinear@endlink </li>
                      <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima@endlink </li>
                      <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima72 NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima72@endlink </li>
                      <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationCubic NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationCubic@endlink </li>
                    </ul>
                  
         
        """
        pass
    
    ## Getter for property: (@link ProfileSolverOptionsBuilder.Extrapolation NXOpen.Fields.ProfileSolverOptionsBuilder.Extrapolation@endlink) YExtrapolation
    ##  Returns  @brief 
    ##             the extrapolation in y direction.  
    ##   
    ##              
    ## 
    ##  
    ##             
    ##             <ul>
    ##               <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationLinear NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationLinear@endlink </li>
    ##               <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationParabolic NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationParabolic@endlink </li>
    ##               <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationCubic NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationCubic@endlink </li>
    ##             </ul>
    ##              <br> 
    ##             This is only used surface profiles
    ##             and when @link NXOpen::Fields::ProfileSolverOptionsBuilder::SetCyclicType NXOpen::Fields::ProfileSolverOptionsBuilder::SetCyclicType@endlink 
    ##             is set to @link NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone@endlink 
    ##             or @link NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeXOnly NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeXOnly@endlink 
    ##              <br> 
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return ProfileSolverOptionsBuilder.Extrapolation
    @property
    def YExtrapolation(self) -> ProfileSolverOptionsBuilder.Extrapolation:
        """
        Getter for property: (@link ProfileSolverOptionsBuilder.Extrapolation NXOpen.Fields.ProfileSolverOptionsBuilder.Extrapolation@endlink) YExtrapolation
         Returns  @brief 
                    the extrapolation in y direction.  
          
                     
        
         
                    
                    <ul>
                      <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationLinear NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationLinear@endlink </li>
                      <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationParabolic NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationParabolic@endlink </li>
                      <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationCubic NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationCubic@endlink </li>
                    </ul>
                     <br> 
                    This is only used surface profiles
                    and when @link NXOpen::Fields::ProfileSolverOptionsBuilder::SetCyclicType NXOpen::Fields::ProfileSolverOptionsBuilder::SetCyclicType@endlink 
                    is set to @link NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone@endlink 
                    or @link NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeXOnly NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeXOnly@endlink 
                     <br> 
                      
         
        """
        pass
    
    ## Setter for property: (@link ProfileSolverOptionsBuilder.Extrapolation NXOpen.Fields.ProfileSolverOptionsBuilder.Extrapolation@endlink) YExtrapolation

    ##  Returns  @brief 
    ##             the extrapolation in y direction.  
    ##   
    ##              
    ## 
    ##  
    ##             
    ##             <ul>
    ##               <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationLinear NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationLinear@endlink </li>
    ##               <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationParabolic NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationParabolic@endlink </li>
    ##               <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationCubic NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationCubic@endlink </li>
    ##             </ul>
    ##              <br> 
    ##             This is only used surface profiles
    ##             and when @link NXOpen::Fields::ProfileSolverOptionsBuilder::SetCyclicType NXOpen::Fields::ProfileSolverOptionsBuilder::SetCyclicType@endlink 
    ##             is set to @link NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone@endlink 
    ##             or @link NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeXOnly NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeXOnly@endlink 
    ##              <br> 
    ##               
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @YExtrapolation.setter
    def YExtrapolation(self, extrapolation: ProfileSolverOptionsBuilder.Extrapolation):
        """
        Setter for property: (@link ProfileSolverOptionsBuilder.Extrapolation NXOpen.Fields.ProfileSolverOptionsBuilder.Extrapolation@endlink) YExtrapolation
         Returns  @brief 
                    the extrapolation in y direction.  
          
                     
        
         
                    
                    <ul>
                      <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationLinear NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationLinear@endlink </li>
                      <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationParabolic NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationParabolic@endlink </li>
                      <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationCubic NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationCubic@endlink </li>
                    </ul>
                     <br> 
                    This is only used surface profiles
                    and when @link NXOpen::Fields::ProfileSolverOptionsBuilder::SetCyclicType NXOpen::Fields::ProfileSolverOptionsBuilder::SetCyclicType@endlink 
                    is set to @link NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone@endlink 
                    or @link NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeXOnly NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeXOnly@endlink 
                     <br> 
                      
         
        """
        pass
    
    ## Getter for property: (@link ProfileSolverOptionsBuilder.Interpolation NXOpen.Fields.ProfileSolverOptionsBuilder.Interpolation@endlink) YInterpolation
    ##  Returns  @brief 
    ##             the interpolation in y direction.  
    ##   
    ##              
    ## 
    ##  
    ##             
    ##             <ul>
    ##               <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationLinear NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationLinear@endlink </li>
    ##               <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima@endlink </li>
    ##               <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima72 NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima72@endlink </li>
    ##               <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationCubic NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationCubic@endlink </li>
    ##             </ul>
    ##              <br> 
    ##             This is only used surface profiles
    ##              <br> 
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return ProfileSolverOptionsBuilder.Interpolation
    @property
    def YInterpolation(self) -> ProfileSolverOptionsBuilder.Interpolation:
        """
        Getter for property: (@link ProfileSolverOptionsBuilder.Interpolation NXOpen.Fields.ProfileSolverOptionsBuilder.Interpolation@endlink) YInterpolation
         Returns  @brief 
                    the interpolation in y direction.  
          
                     
        
         
                    
                    <ul>
                      <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationLinear NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationLinear@endlink </li>
                      <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima@endlink </li>
                      <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima72 NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima72@endlink </li>
                      <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationCubic NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationCubic@endlink </li>
                    </ul>
                     <br> 
                    This is only used surface profiles
                     <br> 
                      
         
        """
        pass
    
    ## Setter for property: (@link ProfileSolverOptionsBuilder.Interpolation NXOpen.Fields.ProfileSolverOptionsBuilder.Interpolation@endlink) YInterpolation

    ##  Returns  @brief 
    ##             the interpolation in y direction.  
    ##   
    ##              
    ## 
    ##  
    ##             
    ##             <ul>
    ##               <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationLinear NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationLinear@endlink </li>
    ##               <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima@endlink </li>
    ##               <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima72 NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima72@endlink </li>
    ##               <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationCubic NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationCubic@endlink </li>
    ##             </ul>
    ##              <br> 
    ##             This is only used surface profiles
    ##              <br> 
    ##               
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @YInterpolation.setter
    def YInterpolation(self, interpolation: ProfileSolverOptionsBuilder.Interpolation):
        """
        Setter for property: (@link ProfileSolverOptionsBuilder.Interpolation NXOpen.Fields.ProfileSolverOptionsBuilder.Interpolation@endlink) YInterpolation
         Returns  @brief 
                    the interpolation in y direction.  
          
                     
        
         
                    
                    <ul>
                      <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationLinear NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationLinear@endlink </li>
                      <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima@endlink </li>
                      <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima72 NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima72@endlink </li>
                      <li>@link NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationCubic NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationCubic@endlink </li>
                    </ul>
                     <br> 
                    This is only used surface profiles
                     <br> 
                      
         
        """
        pass
    
import NXOpen
##  This class defines a scalar value that is internally 
##         backed up by a (optionally scaled) field or an expression. 
## 
##   <br>  Created in NX6.0.0  <br> 

class ScalarFieldWrapper(NXOpen.NXObject): 
    """ This class defines a scalar value that is internally 
        backed up by a (optionally scaled) field or an expression. """


    ##  Returns the implementation if the wrapper is backed up by an expression;
    ##             NULL otherwise 
    ##  @return expression (@link NXOpen.Expression NXOpen.Expression@endlink):  an existing expression or NULL .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def GetExpression(self) -> NXOpen.Expression:
        """
         Returns the implementation if the wrapper is backed up by an expression;
                    NULL otherwise 
         @return expression (@link NXOpen.Expression NXOpen.Expression@endlink):  an existing expression or NULL .
        """
        pass
    
    ##  Returns the implementation if the wrapper is backed up by a field;
    ##             NULL otherwise 
    ##  @return field (@link Field NXOpen.Fields.Field@endlink):  an existing field or NULL .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def GetField(self) -> Field:
        """
         Returns the implementation if the wrapper is backed up by a field;
                    NULL otherwise 
         @return field (@link Field NXOpen.Fields.Field@endlink):  an existing field or NULL .
        """
        pass
    
    ##  Returns the scale factor to be applied to the field, this is only applicable if the wrapper is backed up by a field 
    ##  @return scale_factor (float):  the field will be multiplied by this scale factor when being evaluated .
    ## 
    ##   <br>  Created in NX8.0.3  <br> 

    ## License requirements: None.
    def GetFieldScaleFactor(self) -> float:
        """
         Returns the scale factor to be applied to the field, this is only applicable if the wrapper is backed up by a field 
         @return scale_factor (float):  the field will be multiplied by this scale factor when being evaluated .
        """
        pass
    
    ##  Sets the implementation of the wrapper to the specified expression 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="expression"> (@link NXOpen.Expression NXOpen.Expression@endlink)  an existing expression that will be this wrapper's value </param>
    def SetExpression(self, expression: NXOpen.Expression) -> None:
        """
         Sets the implementation of the wrapper to the specified expression 
        """
        pass
    
    ##  Sets the implementation of the wrapper to the specified field 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="field"> (@link Field NXOpen.Fields.Field@endlink)  an existing field that will be this wrapper's value </param>
    ## <param name="scale_factor"> (float)  the field will be multiplied by this scale factor when being evaluated </param>
    def SetField(self, field: Field, scale_factor: float) -> None:
        """
         Sets the implementation of the wrapper to the specified field 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##   @brief 
##             Represents a builder class for creating and editing an @link NXOpen::Fields::Field NXOpen::Fields::Field@endlink 
##             that is defined by a sketch.
##          
## 
##  
##         
##             It is mandatory to select a valid <ja_property_both>NXOpen.Fields.SketchProfileBuilder.Sketch</ja_property_both>.
##         
##     
## 
##   <br>  Created in NX1847.0.0  <br> 

class SketchProfileBuilder(NXOpen.TaggedObject): 
    """ <summary>
            Represents a builder class for creating and editing an <ja_class>NXOpen.Fields.Field</ja_class>
            that is defined by a sketch.
        </summary>
        <remarks>
            It is mandatory to select a valid <ja_property_both>NXOpen.Fields.SketchProfileBuilder.Sketch</ja_property_both>.
        </remarks>
    """


    ##   @brief interpolation method used for the profile. 
    ## 
    ##   
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Linear</term><description> 
    ##  Linear </description> </item><item><term> 
    ## Akima</term><description> 
    ##  Akima </description> </item><item><term> 
    ## Akima72</term><description> 
    ##  Akima72 </description> </item><item><term> 
    ## Cubic</term><description> 
    ##  Cubic </description> </item></list>
    class InterpolationType(Enum):
        """
        Members Include: <Linear> <Akima> <Akima72> <Cubic>
        """
        Linear: int
        Akima: int
        Akima72: int
        Cubic: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SketchProfileBuilder.InterpolationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##   @brief discrete point type for sketch curve. 
    ## 
    ##   
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ChordalTolerance</term><description> 
    ##  Chordal tolerance type </description> </item><item><term> 
    ## EqualArcLength</term><description> 
    ##  Equal arc length type </description> </item></list>
    class SamplingPointType(Enum):
        """
        Members Include: <ChordalTolerance> <EqualArcLength>
        """
        ChordalTolerance: int
        EqualArcLength: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SketchProfileBuilder.SamplingPointType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ChordalTolerance
    ##  Returns  @brief the chordal tolerance.  
    ##    
    ## 
    ##    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ChordalTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ChordalTolerance
         Returns  @brief the chordal tolerance.  
           
        
           
         
        """
        pass
    
    ## Getter for property: (@link FieldProfileTable.SamplingPointOption NXOpen.Fields.FieldProfileTable.SamplingPointOption@endlink) DiscretePointType
    ##  Returns  @brief the discrete point type.  
    ##    
    ## 
    ##  
    ##             
    ##             <ul>
    ##               <li>@link NXOpen::Fields::FieldProfileTable::SamplingPointOptionChordalTolerance NXOpen::Fields::FieldProfileTable::SamplingPointOptionChordalTolerance@endlink </li>
    ##               <li>@link NXOpen::Fields::FieldProfileTable::SamplingPointOptionEqualArcLength NXOpen::Fields::FieldProfileTable::SamplingPointOptionEqualArcLength@endlink </li>
    ##             </ul>
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1926.0.0.  @link NXOpen::Fields::SketchProfileBuilder::PointSamplingType NXOpen::Fields::SketchProfileBuilder::PointSamplingType@endlink   <br> 

    ## @return FieldProfileTable.SamplingPointOption
    @property
    def DiscretePointType(self) -> FieldProfileTable.SamplingPointOption:
        """
        Getter for property: (@link FieldProfileTable.SamplingPointOption NXOpen.Fields.FieldProfileTable.SamplingPointOption@endlink) DiscretePointType
         Returns  @brief the discrete point type.  
           
        
         
                    
                    <ul>
                      <li>@link NXOpen::Fields::FieldProfileTable::SamplingPointOptionChordalTolerance NXOpen::Fields::FieldProfileTable::SamplingPointOptionChordalTolerance@endlink </li>
                      <li>@link NXOpen::Fields::FieldProfileTable::SamplingPointOptionEqualArcLength NXOpen::Fields::FieldProfileTable::SamplingPointOptionEqualArcLength@endlink </li>
                    </ul>
                      
         
        """
        pass
    
    ## Setter for property: (@link FieldProfileTable.SamplingPointOption NXOpen.Fields.FieldProfileTable.SamplingPointOption@endlink) DiscretePointType

    ##  Returns  @brief the discrete point type.  
    ##    
    ## 
    ##  
    ##             
    ##             <ul>
    ##               <li>@link NXOpen::Fields::FieldProfileTable::SamplingPointOptionChordalTolerance NXOpen::Fields::FieldProfileTable::SamplingPointOptionChordalTolerance@endlink </li>
    ##               <li>@link NXOpen::Fields::FieldProfileTable::SamplingPointOptionEqualArcLength NXOpen::Fields::FieldProfileTable::SamplingPointOptionEqualArcLength@endlink </li>
    ##             </ul>
    ##               
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1926.0.0.  @link NXOpen::Fields::SketchProfileBuilder::SetPointSamplingType NXOpen::Fields::SketchProfileBuilder::SetPointSamplingType@endlink   <br> 

    @DiscretePointType.setter
    def DiscretePointType(self, type: FieldProfileTable.SamplingPointOption):
        """
        Setter for property: (@link FieldProfileTable.SamplingPointOption NXOpen.Fields.FieldProfileTable.SamplingPointOption@endlink) DiscretePointType
         Returns  @brief the discrete point type.  
           
        
         
                    
                    <ul>
                      <li>@link NXOpen::Fields::FieldProfileTable::SamplingPointOptionChordalTolerance NXOpen::Fields::FieldProfileTable::SamplingPointOptionChordalTolerance@endlink </li>
                      <li>@link NXOpen::Fields::FieldProfileTable::SamplingPointOptionEqualArcLength NXOpen::Fields::FieldProfileTable::SamplingPointOptionEqualArcLength@endlink </li>
                    </ul>
                      
         
        """
        pass
    
    ## Getter for property: (@link SketchProfileBuilder.InterpolationType NXOpen.Fields.SketchProfileBuilder.InterpolationType@endlink) Interpolation
    ##  Returns  @brief the interpolation type.  
    ##    
    ## 
    ##  
    ##             
    ##             <ul>
    ##               <li>@link NXOpen::Fields::SketchProfileBuilder::InterpolationTypeLinear NXOpen::Fields::SketchProfileBuilder::InterpolationTypeLinear@endlink </li>
    ##               <li>@link NXOpen::Fields::SketchProfileBuilder::InterpolationTypeAkima NXOpen::Fields::SketchProfileBuilder::InterpolationTypeAkima@endlink </li>
    ##               <li>@link NXOpen::Fields::SketchProfileBuilder::InterpolationTypeAkima72 NXOpen::Fields::SketchProfileBuilder::InterpolationTypeAkima72@endlink </li>
    ##               <li>@link NXOpen::Fields::SketchProfileBuilder::InterpolationTypeCubic NXOpen::Fields::SketchProfileBuilder::InterpolationTypeCubic@endlink </li>
    ##             </ul>
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return SketchProfileBuilder.InterpolationType
    @property
    def Interpolation(self) -> SketchProfileBuilder.InterpolationType:
        """
        Getter for property: (@link SketchProfileBuilder.InterpolationType NXOpen.Fields.SketchProfileBuilder.InterpolationType@endlink) Interpolation
         Returns  @brief the interpolation type.  
           
        
         
                    
                    <ul>
                      <li>@link NXOpen::Fields::SketchProfileBuilder::InterpolationTypeLinear NXOpen::Fields::SketchProfileBuilder::InterpolationTypeLinear@endlink </li>
                      <li>@link NXOpen::Fields::SketchProfileBuilder::InterpolationTypeAkima NXOpen::Fields::SketchProfileBuilder::InterpolationTypeAkima@endlink </li>
                      <li>@link NXOpen::Fields::SketchProfileBuilder::InterpolationTypeAkima72 NXOpen::Fields::SketchProfileBuilder::InterpolationTypeAkima72@endlink </li>
                      <li>@link NXOpen::Fields::SketchProfileBuilder::InterpolationTypeCubic NXOpen::Fields::SketchProfileBuilder::InterpolationTypeCubic@endlink </li>
                    </ul>
                      
         
        """
        pass
    
    ## Setter for property: (@link SketchProfileBuilder.InterpolationType NXOpen.Fields.SketchProfileBuilder.InterpolationType@endlink) Interpolation

    ##  Returns  @brief the interpolation type.  
    ##    
    ## 
    ##  
    ##             
    ##             <ul>
    ##               <li>@link NXOpen::Fields::SketchProfileBuilder::InterpolationTypeLinear NXOpen::Fields::SketchProfileBuilder::InterpolationTypeLinear@endlink </li>
    ##               <li>@link NXOpen::Fields::SketchProfileBuilder::InterpolationTypeAkima NXOpen::Fields::SketchProfileBuilder::InterpolationTypeAkima@endlink </li>
    ##               <li>@link NXOpen::Fields::SketchProfileBuilder::InterpolationTypeAkima72 NXOpen::Fields::SketchProfileBuilder::InterpolationTypeAkima72@endlink </li>
    ##               <li>@link NXOpen::Fields::SketchProfileBuilder::InterpolationTypeCubic NXOpen::Fields::SketchProfileBuilder::InterpolationTypeCubic@endlink </li>
    ##             </ul>
    ##               
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Interpolation.setter
    def Interpolation(self, type: SketchProfileBuilder.InterpolationType):
        """
        Setter for property: (@link SketchProfileBuilder.InterpolationType NXOpen.Fields.SketchProfileBuilder.InterpolationType@endlink) Interpolation
         Returns  @brief the interpolation type.  
           
        
         
                    
                    <ul>
                      <li>@link NXOpen::Fields::SketchProfileBuilder::InterpolationTypeLinear NXOpen::Fields::SketchProfileBuilder::InterpolationTypeLinear@endlink </li>
                      <li>@link NXOpen::Fields::SketchProfileBuilder::InterpolationTypeAkima NXOpen::Fields::SketchProfileBuilder::InterpolationTypeAkima@endlink </li>
                      <li>@link NXOpen::Fields::SketchProfileBuilder::InterpolationTypeAkima72 NXOpen::Fields::SketchProfileBuilder::InterpolationTypeAkima72@endlink </li>
                      <li>@link NXOpen::Fields::SketchProfileBuilder::InterpolationTypeCubic NXOpen::Fields::SketchProfileBuilder::InterpolationTypeCubic@endlink </li>
                    </ul>
                      
         
        """
        pass
    
    ## Getter for property: (int) NumberPoints
    ##  Returns  @brief the number of points.  
    ##    
    ## 
    ##    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def NumberPoints(self) -> int:
        """
        Getter for property: (int) NumberPoints
         Returns  @brief the number of points.  
           
        
           
         
        """
        pass
    
    ## Setter for property: (int) NumberPoints

    ##  Returns  @brief the number of points.  
    ##    
    ## 
    ##    
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @NumberPoints.setter
    def NumberPoints(self, type: int):
        """
        Setter for property: (int) NumberPoints
         Returns  @brief the number of points.  
           
        
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Offset
    ##  Returns  @brief the offset.  
    ##    
    ## 
    ##  
    ##             
    ##             The unit of the offset has to match the
    ##             @link NXOpen::Fields::SketchProfileBuilder::UnitType NXOpen::Fields::SketchProfileBuilder::UnitType@endlink .
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Offset
         Returns  @brief the offset.  
           
        
         
                    
                    The unit of the offset has to match the
                    @link NXOpen::Fields::SketchProfileBuilder::UnitType NXOpen::Fields::SketchProfileBuilder::UnitType@endlink .
                      
         
        """
        pass
    
    ## Getter for property: (@link SketchProfileBuilder.SamplingPointType NXOpen.Fields.SketchProfileBuilder.SamplingPointType@endlink) PointSamplingType
    ##  Returns  @brief the discrete point type.  
    ##    
    ## 
    ##  
    ##             
    ##             <ul>
    ##               <li>@link NXOpen::Fields::SketchProfileBuilder::SamplingPointTypeChordalTolerance NXOpen::Fields::SketchProfileBuilder::SamplingPointTypeChordalTolerance@endlink </li>
    ##               <li>@link NXOpen::Fields::SketchProfileBuilder::SamplingPointTypeEqualArcLength NXOpen::Fields::SketchProfileBuilder::SamplingPointTypeEqualArcLength@endlink </li>
    ##             </ul>
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return SketchProfileBuilder.SamplingPointType
    @property
    def PointSamplingType(self) -> SketchProfileBuilder.SamplingPointType:
        """
        Getter for property: (@link SketchProfileBuilder.SamplingPointType NXOpen.Fields.SketchProfileBuilder.SamplingPointType@endlink) PointSamplingType
         Returns  @brief the discrete point type.  
           
        
         
                    
                    <ul>
                      <li>@link NXOpen::Fields::SketchProfileBuilder::SamplingPointTypeChordalTolerance NXOpen::Fields::SketchProfileBuilder::SamplingPointTypeChordalTolerance@endlink </li>
                      <li>@link NXOpen::Fields::SketchProfileBuilder::SamplingPointTypeEqualArcLength NXOpen::Fields::SketchProfileBuilder::SamplingPointTypeEqualArcLength@endlink </li>
                    </ul>
                      
         
        """
        pass
    
    ## Setter for property: (@link SketchProfileBuilder.SamplingPointType NXOpen.Fields.SketchProfileBuilder.SamplingPointType@endlink) PointSamplingType

    ##  Returns  @brief the discrete point type.  
    ##    
    ## 
    ##  
    ##             
    ##             <ul>
    ##               <li>@link NXOpen::Fields::SketchProfileBuilder::SamplingPointTypeChordalTolerance NXOpen::Fields::SketchProfileBuilder::SamplingPointTypeChordalTolerance@endlink </li>
    ##               <li>@link NXOpen::Fields::SketchProfileBuilder::SamplingPointTypeEqualArcLength NXOpen::Fields::SketchProfileBuilder::SamplingPointTypeEqualArcLength@endlink </li>
    ##             </ul>
    ##               
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @PointSamplingType.setter
    def PointSamplingType(self, type: SketchProfileBuilder.SamplingPointType):
        """
        Setter for property: (@link SketchProfileBuilder.SamplingPointType NXOpen.Fields.SketchProfileBuilder.SamplingPointType@endlink) PointSamplingType
         Returns  @brief the discrete point type.  
           
        
         
                    
                    <ul>
                      <li>@link NXOpen::Fields::SketchProfileBuilder::SamplingPointTypeChordalTolerance NXOpen::Fields::SketchProfileBuilder::SamplingPointTypeChordalTolerance@endlink </li>
                      <li>@link NXOpen::Fields::SketchProfileBuilder::SamplingPointTypeEqualArcLength NXOpen::Fields::SketchProfileBuilder::SamplingPointTypeEqualArcLength@endlink </li>
                    </ul>
                      
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.PointList NXOpen.PointList@endlink) Points
    ##  Returns  @brief the list of points.  
    ##    
    ## 
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.PointList
    @property
    def Points(self) -> NXOpen.PointList:
        """
        Getter for property: (@link NXOpen.PointList NXOpen.PointList@endlink) Points
         Returns  @brief the list of points.  
           
        
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Scale
    ##  Returns  @brief the scale.  
    ##    
    ## 
    ##  
    ##             
    ##             The scale is unitless.
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Scale(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Scale
         Returns  @brief the scale.  
           
        
         
                    
                    The scale is unitless.
                      
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectSketch NXOpen.SelectSketch@endlink) Sketch
    ##  Returns  @brief the sketch.  
    ##    
    ## 
    ##  
    ##             
    ##             For the sketch to be valid
    ##             <ul>
    ##               <li>its start point must be at x=0</li>
    ##               <li>it must be continuous</li>
    ##               <li>it cannot have two y values at the same x value</li>
    ##             </ul>
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.SelectSketch
    @property
    def Sketch(self) -> NXOpen.SelectSketch:
        """
        Getter for property: (@link NXOpen.SelectSketch NXOpen.SelectSketch@endlink) Sketch
         Returns  @brief the sketch.  
           
        
         
                    
                    For the sketch to be valid
                    <ul>
                      <li>its start point must be at x=0</li>
                      <li>it must be continuous</li>
                      <li>it cannot have two y values at the same x value</li>
                    </ul>
                      
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) UnitType
    ##  Returns  @brief the unit type.  
    ##    
    ## 
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Unit
    @property
    def UnitType(self) -> NXOpen.Unit:
        """
        Getter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) UnitType
         Returns  @brief the unit type.  
           
        
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) UnitType

    ##  Returns  @brief the unit type.  
    ##    
    ## 
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @UnitType.setter
    def UnitType(self, unitType: NXOpen.Unit):
        """
        Setter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) UnitType
         Returns  @brief the unit type.  
           
        
            
         
        """
        pass
    
    ##   @brief 
    ##             If the measures are marked as fixed and they are changed, the validation at commit will detect an error and fail.
    ##          
    ## 
    ##  
    ##         
    ##             It is recommended to call this method when editing a profile that is referenced by another object,
    ##             which depends on specific measures.
    ##         
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="areMeasuresFixed"> (bool)  true, if changed measures should prevent a commit </param>
    def SetMeasuresFixed(self, areMeasuresFixed: bool) -> None:
        """
          @brief 
                    If the measures are marked as fixed and they are changed, the validation at commit will detect an error and fail.
                 
        
         
                
                    It is recommended to call this method when editing a profile that is referenced by another object,
                    which depends on specific measures.
                
        """
        pass
    
import NXOpen
##   @brief  Represents a @link NXOpen::Fields::SpatialMap NXOpen::Fields::SpatialMap@endlink  builder  
## 
##  
##      <br> Used to create and or edit a @link NXOpen::Fields::SpatialMap NXOpen::Fields::SpatialMap@endlink . <br> 
##      <br> To create a new instance of this class, use @link NXOpen::Fields::FieldManager::CreateSpatialMapBuilder  NXOpen::Fields::FieldManager::CreateSpatialMapBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## FitSurfaceDirectionOption </term> <description> 
##  
## BestFit </description> </item> 
## 
## <item><term> 
##  
## FitSurfaceUDegree </term> <description> 
##  
## 5 </description> </item> 
## 
## <item><term> 
##  
## FitSurfaceUPatches </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## FitSurfaceVDegree </term> <description> 
##  
## 5 </description> </item> 
## 
## <item><term> 
##  
## FitSurfaceVPatches </term> <description> 
##  
## 1 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX6.0.0  <br> 

class SpatialMapBuilder(NXOpen.Builder): 
    """ <summary> Represents a <ja_class>NXOpen.Fields.SpatialMap</ja_class> builder </summary>
    <para>Used to create and or edit a <ja_class>NXOpen.Fields.SpatialMap</ja_class>.</para>
    """


    ## Direction method provides the ability to specify the projection direction and orientation
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## BestFit</term><description> 
    ## The fit target is sort of rectangular.</description> </item><item><term> 
    ## Vector</term><description> 
    ## Vector will specify the fit direction.</description> </item><item><term> 
    ## Orientation</term><description> 
    ## Orientation will specify the direction and U/V orientation. </description> </item><item><term> 
    ## Csys</term><description> 
    ## CSYS will specify same as orientation but with the need to make it associative with existing geometry. </description> </item></list>
    class FitSurfaceDirectionType(Enum):
        """
        Members Include: <BestFit> <Vector> <Orientation> <Csys>
        """
        BestFit: int
        Vector: int
        Orientation: int
        Csys: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SpatialMapBuilder.FitSurfaceDirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) BoundedObjects
    ##  Returns the bounded objects   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def BoundedObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) BoundedObjects
         Returns the bounded objects   
            
         
        """
        pass
    
    ## Getter for property: (@link SpatialMap.BoundingBoxMapEnum NXOpen.Fields.SpatialMap.BoundingBoxMapEnum@endlink) BoundingBoxMap
    ##  Returns the bounding box map   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return SpatialMap.BoundingBoxMapEnum
    @property
    def BoundingBoxMap(self) -> SpatialMap.BoundingBoxMapEnum:
        """
        Getter for property: (@link SpatialMap.BoundingBoxMapEnum NXOpen.Fields.SpatialMap.BoundingBoxMapEnum@endlink) BoundingBoxMap
         Returns the bounding box map   
            
         
        """
        pass
    
    ## Setter for property: (@link SpatialMap.BoundingBoxMapEnum NXOpen.Fields.SpatialMap.BoundingBoxMapEnum@endlink) BoundingBoxMap

    ##  Returns the bounding box map   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @BoundingBoxMap.setter
    def BoundingBoxMap(self, boundBoxMap: SpatialMap.BoundingBoxMapEnum):
        """
        Setter for property: (@link SpatialMap.BoundingBoxMapEnum NXOpen.Fields.SpatialMap.BoundingBoxMapEnum@endlink) BoundingBoxMap
         Returns the bounding box map   
            
         
        """
        pass
    
    ## Getter for property: (@link PathObjectsList NXOpen.Fields.PathObjectsList@endlink) ConstUObjects
    ##  Returns the list of @link NXOpen::Fields::PathObjects NXOpen::Fields::PathObjects@endlink  objects that define sections of constant u   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    ## @return PathObjectsList
    @property
    def ConstUObjects(self) -> PathObjectsList:
        """
        Getter for property: (@link PathObjectsList NXOpen.Fields.PathObjectsList@endlink) ConstUObjects
         Returns the list of @link NXOpen::Fields::PathObjects NXOpen::Fields::PathObjects@endlink  objects that define sections of constant u   
            
         
        """
        pass
    
    ## Getter for property: (@link PathObjectsList NXOpen.Fields.PathObjectsList@endlink) ConstVObjects
    ##  Returns the list of @link NXOpen::Fields::PathObjects NXOpen::Fields::PathObjects@endlink  objects that define sections of constant v   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    ## @return PathObjectsList
    @property
    def ConstVObjects(self) -> PathObjectsList:
        """
        Getter for property: (@link PathObjectsList NXOpen.Fields.PathObjectsList@endlink) ConstVObjects
         Returns the list of @link NXOpen::Fields::PathObjects NXOpen::Fields::PathObjects@endlink  objects that define sections of constant v   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) CoordSystem
    ##  Returns the csys   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.CoordinateSystem
    @property
    def CoordSystem(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) CoordSystem
         Returns the csys   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) CoordSystem

    ##  Returns the csys   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @CoordSystem.setter
    def CoordSystem(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) CoordSystem
         Returns the csys   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EvaluationTolerance
    ##  Returns the evaluation tolerance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def EvaluationTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EvaluationTolerance
         Returns the evaluation tolerance   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FaceTolerance
    ##  Returns the face tolerance for 3D degenerate surface maps   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.Expression
    @property
    def FaceTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FaceTolerance
         Returns the face tolerance for 3D degenerate surface maps   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) FitSurfaceCoordinateSystem
    ##  Returns the fit surface orientation coordinate system   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.CoordinateSystem
    @property
    def FitSurfaceCoordinateSystem(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) FitSurfaceCoordinateSystem
         Returns the fit surface orientation coordinate system   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) FitSurfaceCoordinateSystem

    ##  Returns the fit surface orientation coordinate system   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @FitSurfaceCoordinateSystem.setter
    def FitSurfaceCoordinateSystem(self, coordSystem: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) FitSurfaceCoordinateSystem
         Returns the fit surface orientation coordinate system   
            
         
        """
        pass
    
    ## Getter for property: (@link SpatialMapBuilder.FitSurfaceDirectionType NXOpen.Fields.SpatialMapBuilder.FitSurfaceDirectionType@endlink) FitSurfaceDirectionOption
    ##  Returns the direction option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return SpatialMapBuilder.FitSurfaceDirectionType
    @property
    def FitSurfaceDirectionOption(self) -> SpatialMapBuilder.FitSurfaceDirectionType:
        """
        Getter for property: (@link SpatialMapBuilder.FitSurfaceDirectionType NXOpen.Fields.SpatialMapBuilder.FitSurfaceDirectionType@endlink) FitSurfaceDirectionOption
         Returns the direction option   
            
         
        """
        pass
    
    ## Setter for property: (@link SpatialMapBuilder.FitSurfaceDirectionType NXOpen.Fields.SpatialMapBuilder.FitSurfaceDirectionType@endlink) FitSurfaceDirectionOption

    ##  Returns the direction option   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @FitSurfaceDirectionOption.setter
    def FitSurfaceDirectionOption(self, directionOption: SpatialMapBuilder.FitSurfaceDirectionType):
        """
        Setter for property: (@link SpatialMapBuilder.FitSurfaceDirectionType NXOpen.Fields.SpatialMapBuilder.FitSurfaceDirectionType@endlink) FitSurfaceDirectionOption
         Returns the direction option   
            
         
        """
        pass
    
    ## Getter for property: (int) FitSurfaceUDegree
    ##  Returns the u degree   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return int
    @property
    def FitSurfaceUDegree(self) -> int:
        """
        Getter for property: (int) FitSurfaceUDegree
         Returns the u degree   
            
         
        """
        pass
    
    ## Setter for property: (int) FitSurfaceUDegree

    ##  Returns the u degree   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @FitSurfaceUDegree.setter
    def FitSurfaceUDegree(self, uDegree: int):
        """
        Setter for property: (int) FitSurfaceUDegree
         Returns the u degree   
            
         
        """
        pass
    
    ## Getter for property: (int) FitSurfaceUPatches
    ##  Returns the u patches   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return int
    @property
    def FitSurfaceUPatches(self) -> int:
        """
        Getter for property: (int) FitSurfaceUPatches
         Returns the u patches   
            
         
        """
        pass
    
    ## Setter for property: (int) FitSurfaceUPatches

    ##  Returns the u patches   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @FitSurfaceUPatches.setter
    def FitSurfaceUPatches(self, uPatches: int):
        """
        Setter for property: (int) FitSurfaceUPatches
         Returns the u patches   
            
         
        """
        pass
    
    ## Getter for property: (int) FitSurfaceVDegree
    ##  Returns the v degree   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return int
    @property
    def FitSurfaceVDegree(self) -> int:
        """
        Getter for property: (int) FitSurfaceVDegree
         Returns the v degree   
            
         
        """
        pass
    
    ## Setter for property: (int) FitSurfaceVDegree

    ##  Returns the v degree   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @FitSurfaceVDegree.setter
    def FitSurfaceVDegree(self, vDegree: int):
        """
        Setter for property: (int) FitSurfaceVDegree
         Returns the v degree   
            
         
        """
        pass
    
    ## Getter for property: (int) FitSurfaceVPatches
    ##  Returns the v patches   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return int
    @property
    def FitSurfaceVPatches(self) -> int:
        """
        Getter for property: (int) FitSurfaceVPatches
         Returns the v patches   
            
         
        """
        pass
    
    ## Setter for property: (int) FitSurfaceVPatches

    ##  Returns the v patches   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @FitSurfaceVPatches.setter
    def FitSurfaceVPatches(self, vPatches: int):
        """
        Setter for property: (int) FitSurfaceVPatches
         Returns the v patches   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) FitSurfaceVector
    ##  Returns the vector specifies the projection direction  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def FitSurfaceVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) FitSurfaceVector
         Returns the vector specifies the projection direction  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) FitSurfaceVector

    ##  Returns the vector specifies the projection direction  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @FitSurfaceVector.setter
    def FitSurfaceVector(self, vector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) FitSurfaceVector
         Returns the vector specifies the projection direction  
            
         
        """
        pass
    
    ## Getter for property: (@link PathObjects NXOpen.Fields.PathObjects@endlink) LatticePath
    ##  Returns the lattice path objects   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    ## @return PathObjects
    @property
    def LatticePath(self) -> PathObjects:
        """
        Getter for property: (@link PathObjects NXOpen.Fields.PathObjects@endlink) LatticePath
         Returns the lattice path objects   
            
         
        """
        pass
    
    ## Getter for property: (@link SpatialMap.SubtypeEnum NXOpen.Fields.SpatialMap.SubtypeEnum@endlink) MapSubtype
    ##  Returns the map subtype   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return SpatialMap.SubtypeEnum
    @property
    def MapSubtype(self) -> SpatialMap.SubtypeEnum:
        """
        Getter for property: (@link SpatialMap.SubtypeEnum NXOpen.Fields.SpatialMap.SubtypeEnum@endlink) MapSubtype
         Returns the map subtype   
            
         
        """
        pass
    
    ## Setter for property: (@link SpatialMap.SubtypeEnum NXOpen.Fields.SpatialMap.SubtypeEnum@endlink) MapSubtype

    ##  Returns the map subtype   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MapSubtype.setter
    def MapSubtype(self, mapSubType: SpatialMap.SubtypeEnum):
        """
        Setter for property: (@link SpatialMap.SubtypeEnum NXOpen.Fields.SpatialMap.SubtypeEnum@endlink) MapSubtype
         Returns the map subtype   
            
         
        """
        pass
    
    ## Getter for property: (@link SpatialMap.SubtypeMappingEnum NXOpen.Fields.SpatialMap.SubtypeMappingEnum@endlink) MapSubtypeMapping
    ##  Returns the subtype mapping   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return SpatialMap.SubtypeMappingEnum
    @property
    def MapSubtypeMapping(self) -> SpatialMap.SubtypeMappingEnum:
        """
        Getter for property: (@link SpatialMap.SubtypeMappingEnum NXOpen.Fields.SpatialMap.SubtypeMappingEnum@endlink) MapSubtypeMapping
         Returns the subtype mapping   
            
         
        """
        pass
    
    ## Setter for property: (@link SpatialMap.SubtypeMappingEnum NXOpen.Fields.SpatialMap.SubtypeMappingEnum@endlink) MapSubtypeMapping

    ##  Returns the subtype mapping   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MapSubtypeMapping.setter
    def MapSubtypeMapping(self, mapSubTypeMapping: SpatialMap.SubtypeMappingEnum):
        """
        Setter for property: (@link SpatialMap.SubtypeMappingEnum NXOpen.Fields.SpatialMap.SubtypeMappingEnum@endlink) MapSubtypeMapping
         Returns the subtype mapping   
            
         
        """
        pass
    
    ## Getter for property: (@link SpatialMap.TypeEnum NXOpen.Fields.SpatialMap.TypeEnum@endlink) MapType
    ##  Returns the map type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return SpatialMap.TypeEnum
    @property
    def MapType(self) -> SpatialMap.TypeEnum:
        """
        Getter for property: (@link SpatialMap.TypeEnum NXOpen.Fields.SpatialMap.TypeEnum@endlink) MapType
         Returns the map type   
            
         
        """
        pass
    
    ## Setter for property: (@link SpatialMap.TypeEnum NXOpen.Fields.SpatialMap.TypeEnum@endlink) MapType

    ##  Returns the map type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @MapType.setter
    def MapType(self, mapType: SpatialMap.TypeEnum):
        """
        Setter for property: (@link SpatialMap.TypeEnum NXOpen.Fields.SpatialMap.TypeEnum@endlink) MapType
         Returns the map type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) MappingFaces
    ##  Returns the faces to be used as mapping objects   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def MappingFaces(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) MappingFaces
         Returns the faces to be used as mapping objects   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) OppositeCorner
    ##  Returns the opposite corner   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def OppositeCorner(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) OppositeCorner
         Returns the opposite corner   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) OppositeCorner

    ##  Returns the opposite corner   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @OppositeCorner.setter
    def OppositeCorner(self, oppositeCorner: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) OppositeCorner
         Returns the opposite corner   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Origin
    ##  Returns the origin   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def Origin(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Origin
         Returns the origin   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Origin

    ##  Returns the origin   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @Origin.setter
    def Origin(self, origin: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Origin
         Returns the origin   
            
         
        """
        pass
    
    ## Getter for property: (@link SpatialMap.ParametricPlaneMapEnum NXOpen.Fields.SpatialMap.ParametricPlaneMapEnum@endlink) ParametricPlaneMap
    ##  Returns the parametric plane map   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return SpatialMap.ParametricPlaneMapEnum
    @property
    def ParametricPlaneMap(self) -> SpatialMap.ParametricPlaneMapEnum:
        """
        Getter for property: (@link SpatialMap.ParametricPlaneMapEnum NXOpen.Fields.SpatialMap.ParametricPlaneMapEnum@endlink) ParametricPlaneMap
         Returns the parametric plane map   
            
         
        """
        pass
    
    ## Setter for property: (@link SpatialMap.ParametricPlaneMapEnum NXOpen.Fields.SpatialMap.ParametricPlaneMapEnum@endlink) ParametricPlaneMap

    ##  Returns the parametric plane map   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @ParametricPlaneMap.setter
    def ParametricPlaneMap(self, parmPlaneMap: SpatialMap.ParametricPlaneMapEnum):
        """
        Setter for property: (@link SpatialMap.ParametricPlaneMapEnum NXOpen.Fields.SpatialMap.ParametricPlaneMapEnum@endlink) ParametricPlaneMap
         Returns the parametric plane map   
            
         
        """
        pass
    
    ##  The method to set the face tolerance to a default value based on the current state of the field 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    def AutoTolerance(self) -> None:
        """
         The method to set the face tolerance to a default value based on the current state of the field 
        """
        pass
    
    ##  Create a lattice spatial map from the input datapoints array.  The number of columns in the datapoints
    ##             array is specified by numOfColumns, and should include the total of all independent and dependent columns.
    ##             Note that the number of dependent columns can be zero.  The independent domain must be x, y, z, xy, xz, yz or xyz and
    ##             the number of columns must be greater than or equal to the count of the independent variables.
    ##             
    ##             The number of rows of data in the datapoints array is calculated by dividing the number of data points by the number of columns.
    ##             
    ##             If number of lattice columns is 1, then a parametric line based map will be created.
    ##             
    ##             Otherwise the lattice will be a M x N u-v grid, where M is the number of lattice columns and N is calculated based 
    ##             on the number of rows in the data points array divded by the number of lattice columns 
    ##  @return A tuple consisting of (latticeMap, parameterizedDatapoints). 
    ##  - latticeMap is: @link SpatialMap NXOpen.Fields.SpatialMap@endlink.
    ##  - parameterizedDatapoints is: List[float].

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="numOfLatticeColumn"> (int) </param>
    ## <param name="numOfColumns"> (int) </param>
    ## <param name="indep_var_array"> (@link FieldVariable List[NXOpen.Fields.FieldVariable]@endlink) </param>
    ## <param name="datapoint"> (List[float]) </param>
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
         @return A tuple consisting of (latticeMap, parameterizedDatapoints). 
         - latticeMap is: @link SpatialMap NXOpen.Fields.SpatialMap@endlink.
         - parameterizedDatapoints is: List[float].

        """
        pass
    
    ##  The get bounding box
    ##  @return boundingbox (List[float]): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    def GetBoundingBox(self) -> List[float]:
        """
         The get bounding box
         @return boundingbox (List[float]): .
        """
        pass
    
    ##  Used to reset map on builder
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="spatialMap"> (@link SpatialMap NXOpen.Fields.SpatialMap@endlink) </param>
    def ResetMap(self, spatialMap: SpatialMap) -> None:
        """
         Used to reset map on builder
        """
        pass
    
    ##  The set bounding box
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="boundingbox"> (List[float]) </param>
    def SetBoundingBox(self, boundingbox: List[float]) -> None:
        """
         The set bounding box
        """
        pass
    
    ##  The Orientation option definition 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="origin"> (@link NXOpen.Point3d NXOpen.Point3d@endlink) </param>
    ## <param name="mtx"> (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) </param>
    def SetFitSurfaceOrientation(self, origin: NXOpen.Point3d, mtx: NXOpen.Matrix3x3) -> None:
        """
         The Orientation option definition 
        """
        pass
    
import NXOpen
##   @brief  Represents the Field Domain Map  
## 
##  
##      <br> A Spatial Map provides a mapping from a field's independent domain into a new domain space.
##     This Particular map type is designed to map into cartesian, cylindrical, spherical or parametric
##     space, allowing the field to be used where these independent domains are required. <br> 
##      <br> To obtain an instance of this class see @link NXOpen::Fields::FieldManager NXOpen::Fields::FieldManager@endlink .  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class SpatialMap(NXOpen.NXObject): 
    """ <summary> Represents the Field Domain Map </summary>
    <para>A Spatial Map provides a mapping from a field's independent domain into a new domain space.
    This Particular map type is designed to map into cartesian, cylindrical, spherical or parametric
    space, allowing the field to be used where these independent domains are required.</para>
    """


    ##  Bounding Box Map  
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## OppositeCorner</term><description> 
    ## </description> </item><item><term> 
    ## Objects</term><description> 
    ## </description> </item></list>
    class BoundingBoxMapEnum(Enum):
        """
        Members Include: <OppositeCorner> <Objects>
        """
        OppositeCorner: int
        Objects: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SpatialMap.BoundingBoxMapEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Parametric Plane Map 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## IsoSections</term><description> 
    ## </description> </item><item><term> 
    ## IsoLines</term><description> 
    ## </description> </item><item><term> 
    ## ImportedIsoLines</term><description> 
    ## </description> </item></list>
    class ParametricPlaneMapEnum(Enum):
        """
        Members Include: <IsoSections> <IsoLines> <ImportedIsoLines>
        """
        IsoSections: int
        IsoLines: int
        ImportedIsoLines: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SpatialMap.ParametricPlaneMapEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Subtype of Spatial Map 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ##  No subtype </description> </item><item><term> 
    ## Surface</term><description> 
    ##  3D degenerate to existing surface </description> </item><item><term> 
    ## FitSurface</term><description> 
    ##  3D degenerate to fit surface </description> </item></list>
    class SubtypeEnum(Enum):
        """
        Members Include: <NotSet> <Surface> <FitSurface>
        """
        NotSet: int
        Surface: int
        FitSurface: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SpatialMap.SubtypeEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Subtype Mapping 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Faces</term><description> 
    ##  Map 3D degenerate data to faces </description> </item><item><term> 
    ## IsoSections</term><description> 
    ##  Map 3D degenerate data using parametric plane using U curves </description> </item><item><term> 
    ## IsoLines</term><description> 
    ##  Map 3D degenerate data using parametric plane using UV curves </description> </item></list>
    class SubtypeMappingEnum(Enum):
        """
        Members Include: <Faces> <IsoSections> <IsoLines>
        """
        Faces: int
        IsoSections: int
        IsoLines: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SpatialMap.SubtypeMappingEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Type of Spatial Map 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ##  No Map </description> </item><item><term> 
    ## Global</term><description> 
    ##  Map to global csys - defaults to cartesian </description> </item><item><term> 
    ## Cartesian</term><description> 
    ##  Map to cartesian csys </description> </item><item><term> 
    ## Cylindrical</term><description> 
    ##  Map to cylindrical csys </description> </item><item><term> 
    ## Spherical</term><description> 
    ##  Map to spherical csys </description> </item><item><term> 
    ## ParametricSpace</term><description> 
    ##  Map to parametric space - see @link NXOpen::Fields::SpatialMap::BoundingBoxMapEnum NXOpen::Fields::SpatialMap::BoundingBoxMapEnum@endlink  </description> </item><item><term> 
    ## ParametricPlane</term><description> 
    ##  Map to parametric plane - see @link NXOpen::Fields::SpatialMap::ParametricPlaneMapEnum NXOpen::Fields::SpatialMap::ParametricPlaneMapEnum@endlink  </description> </item><item><term> 
    ## ParametricLine</term><description> 
    ##  Map to parametric line </description> </item><item><term> 
    ## ImportedParametricLine</term><description> 
    ##  map to imported parametric line </description> </item></list>
    class TypeEnum(Enum):
        """
        Members Include: <NotSet> <Global> <Cartesian> <Cylindrical> <Spherical> <ParametricSpace> <ParametricPlane> <ParametricLine> <ImportedParametricLine>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SpatialMap.TypeEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
import NXOpen
import NXOpen.GeometricUtilities
##   @brief 
##             Represents a builder class for creating and editing an @link NXOpen::Fields::Field NXOpen::Fields::Field@endlink .
##          
## 
##  
##     
## 
##   <br>  Created in NX1847.0.0  <br> 

class TimeSeriesProfileBuilder(NXOpen.TaggedObject): 
    """ <summary>
            Represents a builder class for creating and editing an <ja_class>NXOpen.Fields.Field</ja_class>.
        </summary>
    """


    ##   @brief 
    ##             the interpolation method used for the profile
    ##          
    ## 
    ##   
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Linear</term><description> 
    ##  Linear </description> </item><item><term> 
    ## Akima</term><description> 
    ##  Akima </description> </item><item><term> 
    ## Akima72</term><description> 
    ##  Akima72 </description> </item><item><term> 
    ## Cubic</term><description> 
    ##  Cubic </description> </item></list>
    class InterpolationEnum(Enum):
        """
        Members Include: <Linear> <Akima> <Akima72> <Cubic>
        """
        Linear: int
        Akima: int
        Akima72: int
        Cubic: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TimeSeriesProfileBuilder.InterpolationEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) ChannelHasMeasureUnknown
    ##  Returns  @brief 
    ##              whether or not the profile has unknown measure 
    ##              
    ##   
    ##   
    ##    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def ChannelHasMeasureUnknown(self) -> bool:
        """
        Getter for property: (bool) ChannelHasMeasureUnknown
         Returns  @brief 
                     whether or not the profile has unknown measure 
                     
          
          
           
         
        """
        pass
    
    ## Setter for property: (bool) ChannelHasMeasureUnknown

    ##  Returns  @brief 
    ##              whether or not the profile has unknown measure 
    ##              
    ##   
    ##   
    ##    
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ChannelHasMeasureUnknown.setter
    def ChannelHasMeasureUnknown(self, channelHasUnknownType: bool):
        """
        Setter for property: (bool) ChannelHasMeasureUnknown
         Returns  @brief 
                     whether or not the profile has unknown measure 
                     
          
          
           
         
        """
        pass
    
    ## Getter for property: (str) ChannelName
    ##  Returns  @brief 
    ##             the channel name
    ##              
    ##   
    ##   
    ##    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def ChannelName(self) -> str:
        """
        Getter for property: (str) ChannelName
         Returns  @brief 
                    the channel name
                     
          
          
           
         
        """
        pass
    
    ## Setter for property: (str) ChannelName

    ##  Returns  @brief 
    ##             the channel name
    ##              
    ##   
    ##   
    ##    
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ChannelName.setter
    def ChannelName(self, channelName: str):
        """
        Setter for property: (str) ChannelName
         Returns  @brief 
                    the channel name
                     
          
          
           
         
        """
        pass
    
    ## Getter for property: (str) ExternalFile
    ##  Returns  @brief 
    ##             the external file.  
    ##   
    ##              
    ## 
    ##    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def ExternalFile(self) -> str:
        """
        Getter for property: (str) ExternalFile
         Returns  @brief 
                    the external file.  
          
                     
        
           
         
        """
        pass
    
    ## Setter for property: (str) ExternalFile

    ##  Returns  @brief 
    ##             the external file.  
    ##   
    ##              
    ## 
    ##    
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ExternalFile.setter
    def ExternalFile(self, fileName: str):
        """
        Setter for property: (str) ExternalFile
         Returns  @brief 
                    the external file.  
          
                     
        
           
         
        """
        pass
    
    ## Getter for property: (@link TimeSeriesProfileBuilder.InterpolationEnum NXOpen.Fields.TimeSeriesProfileBuilder.InterpolationEnum@endlink) Interpolation
    ##  Returns  @brief 
    ##             the interpolation 
    ##              
    ##   
    ##   
    ##    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return TimeSeriesProfileBuilder.InterpolationEnum
    @property
    def Interpolation(self) -> TimeSeriesProfileBuilder.InterpolationEnum:
        """
        Getter for property: (@link TimeSeriesProfileBuilder.InterpolationEnum NXOpen.Fields.TimeSeriesProfileBuilder.InterpolationEnum@endlink) Interpolation
         Returns  @brief 
                    the interpolation 
                     
          
          
           
         
        """
        pass
    
    ## Setter for property: (@link TimeSeriesProfileBuilder.InterpolationEnum NXOpen.Fields.TimeSeriesProfileBuilder.InterpolationEnum@endlink) Interpolation

    ##  Returns  @brief 
    ##             the interpolation 
    ##              
    ##   
    ##   
    ##    
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Interpolation.setter
    def Interpolation(self, interpolation: TimeSeriesProfileBuilder.InterpolationEnum):
        """
        Setter for property: (@link TimeSeriesProfileBuilder.InterpolationEnum NXOpen.Fields.TimeSeriesProfileBuilder.InterpolationEnum@endlink) Interpolation
         Returns  @brief 
                    the interpolation 
                     
          
          
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Offset
    ##  Returns  @brief 
    ##             the offset on the x axis.  
    ##   
    ##              
    ## 
    ##    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Offset
         Returns  @brief 
                    the offset on the x axis.  
          
                     
        
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ScaleFactor
    ##  Returns  @brief 
    ##             the scale factor
    ##              
    ##   
    ##   
    ##    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ScaleFactor(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ScaleFactor
         Returns  @brief 
                    the scale factor
                     
          
          
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TimeDelta
    ##  Returns  @brief 
    ##             the time delta
    ##              
    ##   
    ##   
    ##    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def TimeDelta(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TimeDelta
         Returns  @brief 
                    the time delta
                     
          
          
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) UserDefinedUnitType
    ##  Returns  @brief 
    ##             the user defined unit 
    ##              
    ##   
    ##   
    ##    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Unit
    @property
    def UserDefinedUnitType(self) -> NXOpen.Unit:
        """
        Getter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) UserDefinedUnitType
         Returns  @brief 
                    the user defined unit 
                     
          
          
           
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) UserDefinedUnitType

    ##  Returns  @brief 
    ##             the user defined unit 
    ##              
    ##   
    ##   
    ##    
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @UserDefinedUnitType.setter
    def UserDefinedUnitType(self, unitType: NXOpen.Unit):
        """
        Setter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) UserDefinedUnitType
         Returns  @brief 
                    the user defined unit 
                     
          
          
           
         
        """
        pass
    
    ##   @brief 
    ##                 If the measure is marked as fixed and is changed, the validation at commit will detect an error and fail.
    ##              
    ## 
    ##  
    ##             
    ##                 It is recommended to call this method when editing a profile that is referenced by another object,
    ##                 which depends on specific measures.
    ##             
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="isMeasureFixed"> (bool)  true, if changed measures should prevent a commit </param>
    def SetMeasureFixed(self, isMeasureFixed: bool) -> None:
        """
          @brief 
                        If the measure is marked as fixed and is changed, the validation at commit will detect an error and fail.
                     
        
         
                    
                        It is recommended to call this method when editing a profile that is referenced by another object,
                        which depends on specific measures.
                    
        """
        pass
    
import NXOpen
##  This class defines a vector value that is internally 
##         backed up by a (optionally scaled) field or three expressions. 
## 
##   <br>  Created in NX6.0.0  <br> 

class VectorFieldWrapper(NXOpen.NXObject): 
    """ This class defines a vector value that is internally 
        backed up by a (optionally scaled) field or three expressions. """


    ##  Returns the indicated implementation if the wrapper is backed up by expressions; 
    ##             NULL otherwise 
    ##  @return expression (@link NXOpen.Expression NXOpen.Expression@endlink):  existing expression or NULL .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  0, 1 or 2 </param>
    def GetExpressionByIndex(self, index: int) -> NXOpen.Expression:
        """
         Returns the indicated implementation if the wrapper is backed up by expressions; 
                    NULL otherwise 
         @return expression (@link NXOpen.Expression NXOpen.Expression@endlink):  existing expression or NULL .
        """
        pass
    
    ##  Returns the implementation if the wrapper is backed up by a field; 
    ##             NULL otherwise 
    ##  @return field (@link Field NXOpen.Fields.Field@endlink):  existing field or NULL .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def GetField(self) -> Field:
        """
         Returns the implementation if the wrapper is backed up by a field; 
                    NULL otherwise 
         @return field (@link Field NXOpen.Fields.Field@endlink):  existing field or NULL .
        """
        pass
    
    ##  Sets the implementation of the wrapper to the specified expressions 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="expressions"> (@link NXOpen.Expression List[NXOpen.Expression]@endlink)  existing expressions that will be this wrapper's value </param>
    def SetExpressions(self, expressions: List[NXOpen.Expression]) -> None:
        """
         Sets the implementation of the wrapper to the specified expressions 
        """
        pass
    
    ##  Sets the implementation of the wrapper to the specified field 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="field"> (@link Field NXOpen.Fields.Field@endlink)  an existing field that will be this wrapper's value </param>
    ## <param name="scale_factors"> (List[float])  the field will be multiplied by this scale factor when being evaluated </param>
    def SetField(self, field: Field, scale_factors: List[float]) -> None:
        """
         Sets the implementation of the wrapper to the specified field 
        """
        pass
    
## @package NXOpen.Fields
## Classes, Enums and Structs under NXOpen.Fields namespace

##  @link DisplayPropertiesBuilderBalStrainType NXOpen.Fields.DisplayPropertiesBuilderBalStrainType @endlink is an alias for @link DisplayPropertiesBuilder.BalStrainType NXOpen.Fields.DisplayPropertiesBuilder.BalStrainType@endlink
DisplayPropertiesBuilderBalStrainType = DisplayPropertiesBuilder.BalStrainType


##  @link DisplayPropertiesBuilderComplexScalarType NXOpen.Fields.DisplayPropertiesBuilderComplexScalarType @endlink is an alias for @link DisplayPropertiesBuilder.ComplexScalarType NXOpen.Fields.DisplayPropertiesBuilder.ComplexScalarType@endlink
DisplayPropertiesBuilderComplexScalarType = DisplayPropertiesBuilder.ComplexScalarType


##  @link DisplayPropertiesBuilderComplexVectorType NXOpen.Fields.DisplayPropertiesBuilderComplexVectorType @endlink is an alias for @link DisplayPropertiesBuilder.ComplexVectorType NXOpen.Fields.DisplayPropertiesBuilder.ComplexVectorType@endlink
DisplayPropertiesBuilderComplexVectorType = DisplayPropertiesBuilder.ComplexVectorType


##  @link DisplayPropertiesBuilderDepDispTypeEnum NXOpen.Fields.DisplayPropertiesBuilderDepDispTypeEnum @endlink is an alias for @link DisplayPropertiesBuilder.DepDispTypeEnum NXOpen.Fields.DisplayPropertiesBuilder.DepDispTypeEnum@endlink
DisplayPropertiesBuilderDepDispTypeEnum = DisplayPropertiesBuilder.DepDispTypeEnum


##  @link DisplayPropertiesBuilderDepDomColorEnum NXOpen.Fields.DisplayPropertiesBuilderDepDomColorEnum @endlink is an alias for @link DisplayPropertiesBuilder.DepDomColorEnum NXOpen.Fields.DisplayPropertiesBuilder.DepDomColorEnum@endlink
DisplayPropertiesBuilderDepDomColorEnum = DisplayPropertiesBuilder.DepDomColorEnum


##  @link DisplayPropertiesBuilderDepLabelValueEnum NXOpen.Fields.DisplayPropertiesBuilderDepLabelValueEnum @endlink is an alias for @link DisplayPropertiesBuilder.DepLabelValueEnum NXOpen.Fields.DisplayPropertiesBuilder.DepLabelValueEnum@endlink
DisplayPropertiesBuilderDepLabelValueEnum = DisplayPropertiesBuilder.DepLabelValueEnum


##  @link DisplayPropertiesBuilderDispResolutionEnum NXOpen.Fields.DisplayPropertiesBuilderDispResolutionEnum @endlink is an alias for @link DisplayPropertiesBuilder.DispResolutionEnum NXOpen.Fields.DisplayPropertiesBuilder.DispResolutionEnum@endlink
DisplayPropertiesBuilderDispResolutionEnum = DisplayPropertiesBuilder.DispResolutionEnum


##  @link DisplayPropertiesBuilderFieldQuantityType NXOpen.Fields.DisplayPropertiesBuilderFieldQuantityType @endlink is an alias for @link DisplayPropertiesBuilder.FieldQuantityType NXOpen.Fields.DisplayPropertiesBuilder.FieldQuantityType@endlink
DisplayPropertiesBuilderFieldQuantityType = DisplayPropertiesBuilder.FieldQuantityType


##  @link DisplayPropertiesBuilderHeteroTblDispOptionEnum NXOpen.Fields.DisplayPropertiesBuilderHeteroTblDispOptionEnum @endlink is an alias for @link DisplayPropertiesBuilder.HeteroTblDispOptionEnum NXOpen.Fields.DisplayPropertiesBuilder.HeteroTblDispOptionEnum@endlink
DisplayPropertiesBuilderHeteroTblDispOptionEnum = DisplayPropertiesBuilder.HeteroTblDispOptionEnum


##  @link DisplayPropertiesBuilderIndepDomDispType NXOpen.Fields.DisplayPropertiesBuilderIndepDomDispType @endlink is an alias for @link DisplayPropertiesBuilder.IndepDomDispType NXOpen.Fields.DisplayPropertiesBuilder.IndepDomDispType@endlink
DisplayPropertiesBuilderIndepDomDispType = DisplayPropertiesBuilder.IndepDomDispType


##  @link DisplayPropertiesBuilderLegacy3DType NXOpen.Fields.DisplayPropertiesBuilderLegacy3DType @endlink is an alias for @link DisplayPropertiesBuilder.Legacy3DType NXOpen.Fields.DisplayPropertiesBuilder.Legacy3DType@endlink
DisplayPropertiesBuilderLegacy3DType = DisplayPropertiesBuilder.Legacy3DType


##  @link DisplayPropertiesBuilderLegendPos NXOpen.Fields.DisplayPropertiesBuilderLegendPos @endlink is an alias for @link DisplayPropertiesBuilder.LegendPos NXOpen.Fields.DisplayPropertiesBuilder.LegendPos@endlink
DisplayPropertiesBuilderLegendPos = DisplayPropertiesBuilder.LegendPos


##  @link DisplayPropertiesBuilderLineFontEnum NXOpen.Fields.DisplayPropertiesBuilderLineFontEnum @endlink is an alias for @link DisplayPropertiesBuilder.LineFontEnum NXOpen.Fields.DisplayPropertiesBuilder.LineFontEnum@endlink
DisplayPropertiesBuilderLineFontEnum = DisplayPropertiesBuilder.LineFontEnum


##  @link DisplayPropertiesBuilderLineWidthEnum NXOpen.Fields.DisplayPropertiesBuilderLineWidthEnum @endlink is an alias for @link DisplayPropertiesBuilder.LineWidthEnum NXOpen.Fields.DisplayPropertiesBuilder.LineWidthEnum@endlink
DisplayPropertiesBuilderLineWidthEnum = DisplayPropertiesBuilder.LineWidthEnum


##  @link DisplayPropertiesBuilderScalarType NXOpen.Fields.DisplayPropertiesBuilderScalarType @endlink is an alias for @link DisplayPropertiesBuilder.ScalarType NXOpen.Fields.DisplayPropertiesBuilder.ScalarType@endlink
DisplayPropertiesBuilderScalarType = DisplayPropertiesBuilder.ScalarType


##  @link DisplayPropertiesBuilderTblPointTypeEnum NXOpen.Fields.DisplayPropertiesBuilderTblPointTypeEnum @endlink is an alias for @link DisplayPropertiesBuilder.TblPointTypeEnum NXOpen.Fields.DisplayPropertiesBuilder.TblPointTypeEnum@endlink
DisplayPropertiesBuilderTblPointTypeEnum = DisplayPropertiesBuilder.TblPointTypeEnum


##  @link DisplayPropertiesBuilderTensorType NXOpen.Fields.DisplayPropertiesBuilderTensorType @endlink is an alias for @link DisplayPropertiesBuilder.TensorType NXOpen.Fields.DisplayPropertiesBuilder.TensorType@endlink
DisplayPropertiesBuilderTensorType = DisplayPropertiesBuilder.TensorType


##  @link DisplayPropertiesBuilderValueRange NXOpen.Fields.DisplayPropertiesBuilderValueRange @endlink is an alias for @link DisplayPropertiesBuilder.ValueRange NXOpen.Fields.DisplayPropertiesBuilder.ValueRange@endlink
DisplayPropertiesBuilderValueRange = DisplayPropertiesBuilder.ValueRange


##  @link DisplayPropertiesBuilderValuesEnum NXOpen.Fields.DisplayPropertiesBuilderValuesEnum @endlink is an alias for @link DisplayPropertiesBuilder.ValuesEnum NXOpen.Fields.DisplayPropertiesBuilder.ValuesEnum@endlink
DisplayPropertiesBuilderValuesEnum = DisplayPropertiesBuilder.ValuesEnum


##  @link DisplayPropertiesBuilderVectorType NXOpen.Fields.DisplayPropertiesBuilderVectorType @endlink is an alias for @link DisplayPropertiesBuilder.VectorType NXOpen.Fields.DisplayPropertiesBuilder.VectorType@endlink
DisplayPropertiesBuilderVectorType = DisplayPropertiesBuilder.VectorType


##  @link ExternalFileProfileBuilderCyclicType NXOpen.Fields.ExternalFileProfileBuilderCyclicType @endlink is an alias for @link ExternalFileProfileBuilder.CyclicType NXOpen.Fields.ExternalFileProfileBuilder.CyclicType@endlink
ExternalFileProfileBuilderCyclicType = ExternalFileProfileBuilder.CyclicType


##  @link ExternalFileProfileBuilderDimensionChoice NXOpen.Fields.ExternalFileProfileBuilderDimensionChoice @endlink is an alias for @link ExternalFileProfileBuilder.DimensionChoice NXOpen.Fields.ExternalFileProfileBuilder.DimensionChoice@endlink
ExternalFileProfileBuilderDimensionChoice = ExternalFileProfileBuilder.DimensionChoice


##  @link ExternalFileProfileBuilderExtrapolation NXOpen.Fields.ExternalFileProfileBuilderExtrapolation @endlink is an alias for @link ExternalFileProfileBuilder.Extrapolation NXOpen.Fields.ExternalFileProfileBuilder.Extrapolation@endlink
ExternalFileProfileBuilderExtrapolation = ExternalFileProfileBuilder.Extrapolation


##  @link ExternalFileProfileBuilderFormatOptions NXOpen.Fields.ExternalFileProfileBuilderFormatOptions @endlink is an alias for @link ExternalFileProfileBuilder.FormatOptions NXOpen.Fields.ExternalFileProfileBuilder.FormatOptions@endlink
ExternalFileProfileBuilderFormatOptions = ExternalFileProfileBuilder.FormatOptions


##  @link ExternalFileProfileBuilderInterpolation NXOpen.Fields.ExternalFileProfileBuilderInterpolation @endlink is an alias for @link ExternalFileProfileBuilder.Interpolation NXOpen.Fields.ExternalFileProfileBuilder.Interpolation@endlink
ExternalFileProfileBuilderInterpolation = ExternalFileProfileBuilder.Interpolation


##  @link FieldEvaluatorDelaunaySliverDetectionMethodEnum NXOpen.Fields.FieldEvaluatorDelaunaySliverDetectionMethodEnum @endlink is an alias for @link FieldEvaluator.DelaunaySliverDetectionMethodEnum NXOpen.Fields.FieldEvaluator.DelaunaySliverDetectionMethodEnum@endlink
FieldEvaluatorDelaunaySliverDetectionMethodEnum = FieldEvaluator.DelaunaySliverDetectionMethodEnum


##  @link FieldEvaluatorInterpolationEnum NXOpen.Fields.FieldEvaluatorInterpolationEnum @endlink is an alias for @link FieldEvaluator.InterpolationEnum NXOpen.Fields.FieldEvaluator.InterpolationEnum@endlink
FieldEvaluatorInterpolationEnum = FieldEvaluator.InterpolationEnum


##  @link FieldEvaluatorInverseDistanceWeightingEnum NXOpen.Fields.FieldEvaluatorInverseDistanceWeightingEnum @endlink is an alias for @link FieldEvaluator.InverseDistanceWeightingEnum NXOpen.Fields.FieldEvaluator.InverseDistanceWeightingEnum@endlink
FieldEvaluatorInverseDistanceWeightingEnum = FieldEvaluator.InverseDistanceWeightingEnum


##  @link FieldEvaluatorInverseDistanceWeightingPowerOfDistanceEnum NXOpen.Fields.FieldEvaluatorInverseDistanceWeightingPowerOfDistanceEnum @endlink is an alias for @link FieldEvaluator.InverseDistanceWeightingPowerOfDistanceEnum NXOpen.Fields.FieldEvaluator.InverseDistanceWeightingPowerOfDistanceEnum@endlink
FieldEvaluatorInverseDistanceWeightingPowerOfDistanceEnum = FieldEvaluator.InverseDistanceWeightingPowerOfDistanceEnum


##  @link FieldEvaluatorLinearLogOptionEnum NXOpen.Fields.FieldEvaluatorLinearLogOptionEnum @endlink is an alias for @link FieldEvaluator.LinearLogOptionEnum NXOpen.Fields.FieldEvaluator.LinearLogOptionEnum@endlink
FieldEvaluatorLinearLogOptionEnum = FieldEvaluator.LinearLogOptionEnum


##  @link FieldEvaluatorSplineDegreeOptionEnum NXOpen.Fields.FieldEvaluatorSplineDegreeOptionEnum @endlink is an alias for @link FieldEvaluator.SplineDegreeOptionEnum NXOpen.Fields.FieldEvaluator.SplineDegreeOptionEnum@endlink
FieldEvaluatorSplineDegreeOptionEnum = FieldEvaluator.SplineDegreeOptionEnum


##  @link FieldEvaluatorValuesOutsideTableInterpolationEnum NXOpen.Fields.FieldEvaluatorValuesOutsideTableInterpolationEnum @endlink is an alias for @link FieldEvaluator.ValuesOutsideTableInterpolationEnum NXOpen.Fields.FieldEvaluator.ValuesOutsideTableInterpolationEnum@endlink
FieldEvaluatorValuesOutsideTableInterpolationEnum = FieldEvaluator.ValuesOutsideTableInterpolationEnum


##  @link FieldExpressionCombineTableOption NXOpen.Fields.FieldExpressionCombineTableOption @endlink is an alias for @link FieldExpression.CombineTableOption NXOpen.Fields.FieldExpression.CombineTableOption@endlink
FieldExpressionCombineTableOption = FieldExpression.CombineTableOption


##  @link FieldTableDBFactor NXOpen.Fields.FieldTableDBFactor @endlink is an alias for @link FieldTable.DBFactor NXOpen.Fields.FieldTable.DBFactor@endlink
FieldTableDBFactor = FieldTable.DBFactor


##  @link FieldTableDuplicateValueOption NXOpen.Fields.FieldTableDuplicateValueOption @endlink is an alias for @link FieldTable.DuplicateValueOption NXOpen.Fields.FieldTable.DuplicateValueOption@endlink
FieldTableDuplicateValueOption = FieldTable.DuplicateValueOption


##  @link FieldTableLoadFileOption NXOpen.Fields.FieldTableLoadFileOption @endlink is an alias for @link FieldTable.LoadFileOption NXOpen.Fields.FieldTable.LoadFileOption@endlink
FieldTableLoadFileOption = FieldTable.LoadFileOption


##  @link FieldTableStructDataTableType NXOpen.Fields.FieldTableStructDataTableType @endlink is an alias for @link FieldTable.StructDataTableType NXOpen.Fields.FieldTable.StructDataTableType@endlink
FieldTableStructDataTableType = FieldTable.StructDataTableType


## @link FieldVariableBounds_Struct NXOpen.Fields.FieldVariableBounds_Struct@endlink is an alias for @link FieldVariable.Bounds NXOpen.Fields.FieldVariable.Bounds@endlink.
FieldVariableBounds_Struct = FieldVariable.Bounds


##  @link FieldVariableType NXOpen.Fields.FieldVariableType @endlink is an alias for @link FieldVariable.Type NXOpen.Fields.FieldVariable.Type@endlink
FieldVariableType = FieldVariable.Type


##  @link FieldVariableValueType NXOpen.Fields.FieldVariableValueType @endlink is an alias for @link FieldVariable.ValueType NXOpen.Fields.FieldVariable.ValueType@endlink
FieldVariableValueType = FieldVariable.ValueType


##  @link FieldPlotOption NXOpen.Fields.FieldPlotOption @endlink is an alias for @link Field.PlotOption NXOpen.Fields.Field.PlotOption@endlink
FieldPlotOption = Field.PlotOption


##  @link ImportBuilderActionType NXOpen.Fields.ImportBuilderActionType @endlink is an alias for @link ImportBuilder.ActionType NXOpen.Fields.ImportBuilder.ActionType@endlink
ImportBuilderActionType = ImportBuilder.ActionType


##  @link ImportBuilderConflictType NXOpen.Fields.ImportBuilderConflictType @endlink is an alias for @link ImportBuilder.ConflictType NXOpen.Fields.ImportBuilder.ConflictType@endlink
ImportBuilderConflictType = ImportBuilder.ConflictType


##  @link ImportBuilderImportConflictStrategy NXOpen.Fields.ImportBuilderImportConflictStrategy @endlink is an alias for @link ImportBuilder.ImportConflictStrategy NXOpen.Fields.ImportBuilder.ImportConflictStrategy@endlink
ImportBuilderImportConflictStrategy = ImportBuilder.ImportConflictStrategy


##  @link ImportBuilderImportFieldStrategy NXOpen.Fields.ImportBuilderImportFieldStrategy @endlink is an alias for @link ImportBuilder.ImportFieldStrategy NXOpen.Fields.ImportBuilder.ImportFieldStrategy@endlink
ImportBuilderImportFieldStrategy = ImportBuilder.ImportFieldStrategy


##  @link ImportBuilderImportFilter NXOpen.Fields.ImportBuilderImportFilter @endlink is an alias for @link ImportBuilder.ImportFilter NXOpen.Fields.ImportBuilder.ImportFilter@endlink
ImportBuilderImportFilter = ImportBuilder.ImportFilter


##  @link ManualInputProfileBuilderCyclicType NXOpen.Fields.ManualInputProfileBuilderCyclicType @endlink is an alias for @link ManualInputProfileBuilder.CyclicType NXOpen.Fields.ManualInputProfileBuilder.CyclicType@endlink
ManualInputProfileBuilderCyclicType = ManualInputProfileBuilder.CyclicType


##  @link ManualInputProfileBuilderExtrapolation NXOpen.Fields.ManualInputProfileBuilderExtrapolation @endlink is an alias for @link ManualInputProfileBuilder.Extrapolation NXOpen.Fields.ManualInputProfileBuilder.Extrapolation@endlink
ManualInputProfileBuilderExtrapolation = ManualInputProfileBuilder.Extrapolation


##  @link ManualInputProfileBuilderInterpolation NXOpen.Fields.ManualInputProfileBuilderInterpolation @endlink is an alias for @link ManualInputProfileBuilder.Interpolation NXOpen.Fields.ManualInputProfileBuilder.Interpolation@endlink
ManualInputProfileBuilderInterpolation = ManualInputProfileBuilder.Interpolation


##  @link ProfileSolverOptionsBuilderCyclicType NXOpen.Fields.ProfileSolverOptionsBuilderCyclicType @endlink is an alias for @link ProfileSolverOptionsBuilder.CyclicType NXOpen.Fields.ProfileSolverOptionsBuilder.CyclicType@endlink
ProfileSolverOptionsBuilderCyclicType = ProfileSolverOptionsBuilder.CyclicType


##  @link ProfileSolverOptionsBuilderExtrapolation NXOpen.Fields.ProfileSolverOptionsBuilderExtrapolation @endlink is an alias for @link ProfileSolverOptionsBuilder.Extrapolation NXOpen.Fields.ProfileSolverOptionsBuilder.Extrapolation@endlink
ProfileSolverOptionsBuilderExtrapolation = ProfileSolverOptionsBuilder.Extrapolation


##  @link ProfileSolverOptionsBuilderInterpolation NXOpen.Fields.ProfileSolverOptionsBuilderInterpolation @endlink is an alias for @link ProfileSolverOptionsBuilder.Interpolation NXOpen.Fields.ProfileSolverOptionsBuilder.Interpolation@endlink
ProfileSolverOptionsBuilderInterpolation = ProfileSolverOptionsBuilder.Interpolation


##  @link SketchProfileBuilderInterpolationType NXOpen.Fields.SketchProfileBuilderInterpolationType @endlink is an alias for @link SketchProfileBuilder.InterpolationType NXOpen.Fields.SketchProfileBuilder.InterpolationType@endlink
SketchProfileBuilderInterpolationType = SketchProfileBuilder.InterpolationType


##  @link SketchProfileBuilderSamplingPointType NXOpen.Fields.SketchProfileBuilderSamplingPointType @endlink is an alias for @link SketchProfileBuilder.SamplingPointType NXOpen.Fields.SketchProfileBuilder.SamplingPointType@endlink
SketchProfileBuilderSamplingPointType = SketchProfileBuilder.SamplingPointType


##  @link SpatialMapBuilderFitSurfaceDirectionType NXOpen.Fields.SpatialMapBuilderFitSurfaceDirectionType @endlink is an alias for @link SpatialMapBuilder.FitSurfaceDirectionType NXOpen.Fields.SpatialMapBuilder.FitSurfaceDirectionType@endlink
SpatialMapBuilderFitSurfaceDirectionType = SpatialMapBuilder.FitSurfaceDirectionType


##  @link SpatialMapBoundingBoxMapEnum NXOpen.Fields.SpatialMapBoundingBoxMapEnum @endlink is an alias for @link SpatialMap.BoundingBoxMapEnum NXOpen.Fields.SpatialMap.BoundingBoxMapEnum@endlink
SpatialMapBoundingBoxMapEnum = SpatialMap.BoundingBoxMapEnum


##  @link SpatialMapParametricPlaneMapEnum NXOpen.Fields.SpatialMapParametricPlaneMapEnum @endlink is an alias for @link SpatialMap.ParametricPlaneMapEnum NXOpen.Fields.SpatialMap.ParametricPlaneMapEnum@endlink
SpatialMapParametricPlaneMapEnum = SpatialMap.ParametricPlaneMapEnum


##  @link SpatialMapSubtypeEnum NXOpen.Fields.SpatialMapSubtypeEnum @endlink is an alias for @link SpatialMap.SubtypeEnum NXOpen.Fields.SpatialMap.SubtypeEnum@endlink
SpatialMapSubtypeEnum = SpatialMap.SubtypeEnum


##  @link SpatialMapSubtypeMappingEnum NXOpen.Fields.SpatialMapSubtypeMappingEnum @endlink is an alias for @link SpatialMap.SubtypeMappingEnum NXOpen.Fields.SpatialMap.SubtypeMappingEnum@endlink
SpatialMapSubtypeMappingEnum = SpatialMap.SubtypeMappingEnum


##  @link SpatialMapTypeEnum NXOpen.Fields.SpatialMapTypeEnum @endlink is an alias for @link SpatialMap.TypeEnum NXOpen.Fields.SpatialMap.TypeEnum@endlink
SpatialMapTypeEnum = SpatialMap.TypeEnum


##  @link TimeSeriesProfileBuilderInterpolationEnum NXOpen.Fields.TimeSeriesProfileBuilderInterpolationEnum @endlink is an alias for @link TimeSeriesProfileBuilder.InterpolationEnum NXOpen.Fields.TimeSeriesProfileBuilder.InterpolationEnum@endlink
TimeSeriesProfileBuilderInterpolationEnum = TimeSeriesProfileBuilder.InterpolationEnum


