from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  This class represents a function record.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class FunctionRecord(NXOpen.TransientObject): 
    """ This class represents a function record. """


    ##  the abscissa value type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Double</term><description> 
    ## </description> </item><item><term> 
    ## Integer</term><description> 
    ## </description> </item></list>
    class AbscissaValueType(Enum):
        """
        Members Include: <Double> <Integer>
        """
        Double: int
        Integer: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FunctionRecord.AbscissaValueType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the ordinate value type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## RealOnly</term><description> 
    ## </description> </item><item><term> 
    ## RealImaginary</term><description> 
    ## </description> </item></list>
    class OrdinateValueType(Enum):
        """
        Members Include: <RealOnly> <RealImaginary>
        """
        RealOnly: int
        RealImaginary: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FunctionRecord.OrdinateValueType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link FunctionRecord.AbscissaValueType NXOpen.CAE.PostProc.FunctionRecord.AbscissaValueType@endlink) AbscissaValueDataType
    ##   the abscissa value data type   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return FunctionRecord.AbscissaValueType
    @property
    def AbscissaValueDataType(self) -> FunctionRecord.AbscissaValueType:
        """
        Getter for property: (@link FunctionRecord.AbscissaValueType NXOpen.CAE.PostProc.FunctionRecord.AbscissaValueType@endlink) AbscissaValueDataType
          the abscissa value data type   
            
         
        """
        pass
    
    ## Getter for property: (@link FunctionRecord.OrdinateValueType NXOpen.CAE.PostProc.FunctionRecord.OrdinateValueType@endlink) OrdinateValueDataType
    ##   the ordinate value data type   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return FunctionRecord.OrdinateValueType
    @property
    def OrdinateValueDataType(self) -> FunctionRecord.OrdinateValueType:
        """
        Getter for property: (@link FunctionRecord.OrdinateValueType NXOpen.CAE.PostProc.FunctionRecord.OrdinateValueType@endlink) OrdinateValueDataType
          the ordinate value data type   
            
         
        """
        pass
    
    ## Getter for property: (str) RecordName
    ##   the record name   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def RecordName(self) -> str:
        """
        Getter for property: (str) RecordName
          the record name   
            
         
        """
        pass
    
    ##  Destroys the object 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(pFuncRecord: FunctionRecord) -> None:
        """
         Destroys the object 
        """
        pass
    
    ##  Gets abscissa values in case that abscissa value data type is
    ##                 @link NXOpen::CAE::PostProc::FunctionRecord::AbscissaValueType::Double NXOpen::CAE::PostProc::FunctionRecord::AbscissaValueType::Double@endlink  
    ##  @return abscissaValues (List[float]): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer")
    @staticmethod
    def GetAbscissaValues(pFuncRecord: FunctionRecord) -> List[float]:
        """
         Gets abscissa values in case that abscissa value data type is
                        @link NXOpen::CAE::PostProc::FunctionRecord::AbscissaValueType::Double NXOpen::CAE::PostProc::FunctionRecord::AbscissaValueType::Double@endlink  
         @return abscissaValues (List[float]): .
        """
        pass
    
    ##  Gets abscissa values in case that abscissa value data type is
    ##                 @link NXOpen::CAE::PostProc::FunctionRecord::AbscissaValueType::Integer NXOpen::CAE::PostProc::FunctionRecord::AbscissaValueType::Integer@endlink  like Node id, element id etc. 
    ##  @return abscissaValues (List[int]): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer")
    @staticmethod
    def GetIntegerAbscissaValues(pFuncRecord: FunctionRecord) -> List[int]:
        """
         Gets abscissa values in case that abscissa value data type is
                        @link NXOpen::CAE::PostProc::FunctionRecord::AbscissaValueType::Integer NXOpen::CAE::PostProc::FunctionRecord::AbscissaValueType::Integer@endlink  like Node id, element id etc. 
         @return abscissaValues (List[int]): .
        """
        pass
    
    ##  Gets ordinate values.
    ##                 <remark>
    ##                 The values are returned according to the value type.
    ##                 <ol>
    ##                 <li>
    ##                 For ordinate value type @link NXOpen::CAE::PostProc::FunctionRecord::OrdinateValueType::RealOnly NXOpen::CAE::PostProc::FunctionRecord::OrdinateValueType::RealOnly@endlink ,
    ##                 the values are returned as value1, value2...
    ##                 </li>
    ##                 <li>
    ##                 For ordinate value type @link NXOpen::CAE::PostProc::FunctionRecord::OrdinateValueType::RealImaginary NXOpen::CAE::PostProc::FunctionRecord::OrdinateValueType::RealImaginary@endlink ,
    ##                 the values are returned as real1, imaginary1, real2, imaginary2...
    ##                 </li>
    ##                 </ol>
    ##                 </remark>
    ##  @return ordinateValues (List[float]): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer")
    @staticmethod
    def GetOrdinateValues(pFuncRecord: FunctionRecord) -> List[float]:
        """
         Gets ordinate values.
                        <remark>
                        The values are returned according to the value type.
                        <ol>
                        <li>
                        For ordinate value type @link NXOpen::CAE::PostProc::FunctionRecord::OrdinateValueType::RealOnly NXOpen::CAE::PostProc::FunctionRecord::OrdinateValueType::RealOnly@endlink ,
                        the values are returned as value1, value2...
                        </li>
                        <li>
                        For ordinate value type @link NXOpen::CAE::PostProc::FunctionRecord::OrdinateValueType::RealImaginary NXOpen::CAE::PostProc::FunctionRecord::OrdinateValueType::RealImaginary@endlink ,
                        the values are returned as real1, imaginary1, real2, imaginary2...
                        </li>
                        </ol>
                        </remark>
         @return ordinateValues (List[float]): .
        """
        pass
    
import NXOpen
import NXOpen.CAE
##  Represents a specific result state for a given @link NXOpen::CAE::Result NXOpen::CAE::Result@endlink . 
##             <br/>The result state is defined by @link NXOpen::CAE::PostProc::FunctionResultParameters NXOpen::CAE::PostProc::FunctionResultParameters@endlink 
##             <br/>Use @link NXOpen::CAE::ResultManager NXOpen::CAE::ResultManager@endlink  to create an @link NXOpen::CAE::PostProc::FunctionResultAccess NXOpen::CAE::PostProc::FunctionResultAccess@endlink .
##          <br> An instance of this class can not be obtained  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class FunctionResultAccess(NXOpen.TaggedObject): 
    """ Represents a specific result state for a given <ja_class>NXOpen.CAE.Result</ja_class>. 
            <br/>The result state is defined by <ja_class>NXOpen.CAE.PostProc.FunctionResultParameters</ja_class>
            <br/>Use <ja_class>NXOpen.CAE.ResultManager</ja_class> to create an <ja_class>NXOpen.CAE.PostProc.FunctionResultAccess</ja_class>.
        """


    ##  Gets function records 
    ##  @return funcRecords (@link FunctionRecord List[NXOpen.CAE.PostProc.FunctionRecord]@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer")
    @staticmethod
    def GetFunctionRecords(tResultAccess: FunctionResultAccess) -> List[FunctionRecord]:
        """
         Gets function records 
         @return funcRecords (@link FunctionRecord List[NXOpen.CAE.PostProc.FunctionRecord]@endlink): .
        """
        pass
    
    ##   Returns the @link NXOpen::CAE::PostProc::FunctionResultParameters NXOpen::CAE::PostProc::FunctionResultParameters@endlink  which defines the current result state.
    ##                   <br/>The @link NXOpen::CAE::PostProc::FunctionResultParameters NXOpen::CAE::PostProc::FunctionResultParameters@endlink  can be modified but these changes will only take 
    ##                   affect after @link NXOpen::CAE::PostProc::FunctionResultAccess::SetParameters NXOpen::CAE::PostProc::FunctionResultAccess::SetParameters@endlink  is called. 
    ##  @return result_parameters (@link FunctionResultParameters NXOpen.CAE.PostProc.FunctionResultParameters@endlink):  .
    ## 
    ##   <br>  Created in NX6.0.2  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer")
    @staticmethod
    def GetParameters(result_access: FunctionResultAccess) -> FunctionResultParameters:
        """
          Returns the @link NXOpen::CAE::PostProc::FunctionResultParameters NXOpen::CAE::PostProc::FunctionResultParameters@endlink  which defines the current result state.
                          <br/>The @link NXOpen::CAE::PostProc::FunctionResultParameters NXOpen::CAE::PostProc::FunctionResultParameters@endlink  can be modified but these changes will only take 
                          affect after @link NXOpen::CAE::PostProc::FunctionResultAccess::SetParameters NXOpen::CAE::PostProc::FunctionResultAccess::SetParameters@endlink  is called. 
         @return result_parameters (@link FunctionResultParameters NXOpen.CAE.PostProc.FunctionResultParameters@endlink):  .
        """
        pass
    
    ##   Returns the @link NXOpen::CAE::Result NXOpen::CAE::Result@endlink  which defines this result Access object
    ##                  The @link NXOpen::CAE::Result NXOpen::CAE::Result@endlink  can be queried in order to set result state in
    ##                  @link NXOpen::CAE::PostProc::FunctionResultParameters NXOpen::CAE::PostProc::FunctionResultParameters@endlink  
    ##              
    ##  @return result (@link NXOpen.CAE.Result NXOpen.CAE.Result@endlink): .
    ## 
    ##   <br>  Created in NX6.0.2  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer")
    @staticmethod
    def GetResult(result_access: FunctionResultAccess) -> NXOpen.CAE.Result:
        """
          Returns the @link NXOpen::CAE::Result NXOpen::CAE::Result@endlink  which defines this result Access object
                         The @link NXOpen::CAE::Result NXOpen::CAE::Result@endlink  can be queried in order to set result state in
                         @link NXOpen::CAE::PostProc::FunctionResultParameters NXOpen::CAE::PostProc::FunctionResultParameters@endlink  
                     
         @return result (@link NXOpen.CAE.Result NXOpen.CAE.Result@endlink): .
        """
        pass
    
    ##  Sets@link NXOpen::CAE::PostProc::FunctionResultParameters NXOpen::CAE::PostProc::FunctionResultParameters@endlink . This will validate any inappropiate settings.
    ##             If the input is not valid it will revert back to previous settings 
    ## 
    ##   <br>  Created in NX6.0.2  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer")
    ##  
    def SetParameters(result_access: FunctionResultAccess, result_parameters: FunctionResultParameters) -> None:
        """
         Sets@link NXOpen::CAE::PostProc::FunctionResultParameters NXOpen::CAE::PostProc::FunctionResultParameters@endlink . This will validate any inappropiate settings.
                    If the input is not valid it will revert back to previous settings 
        """
        pass
    
import NXOpen
##  This class is worked as a packet of information that can be either be used to change result state or pass around for information exchange between two  @link NXOpen::CAE::PostProc::FunctionResultAccess NXOpen::CAE::PostProc::FunctionResultAccess@endlink  objects.
##         <br/>Use @link NXOpen::CAE::ResultManager NXOpen::CAE::ResultManager@endlink  to create an @link NXOpen::CAE::PostProc::FunctionResultParameters NXOpen::CAE::PostProc::FunctionResultParameters@endlink 
##         
##         <br/>You can modifiy these values but validation of correctness will only be perfomed 
##         when this object is set to a @link NXOpen::CAE::PostProc::FunctionResultAccess NXOpen::CAE::PostProc::FunctionResultAccess@endlink  object
##          <br> To obtain an instance of this class use @link NXOpen::Session::ResultManager NXOpen::Session::ResultManager@endlink .  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class FunctionResultParameters(NXOpen.TaggedObject): 
    """ This class is worked as a packet of information that can be either be used to change result state or pass around for information exchange between two  <ja_class>NXOpen.CAE.PostProc.FunctionResultAccess</ja_class> objects.
        <br/>Use <ja_class>NXOpen.CAE.ResultManager</ja_class> to create an <ja_class>NXOpen.CAE.PostProc.FunctionResultParameters</ja_class>
        
        <br/>You can modifiy these values but validation of correctness will only be perfomed 
        when this object is set to a <ja_class>NXOpen.CAE.PostProc.FunctionResultAccess</ja_class> object
        """


    ##  Adds a field of double values to an independent variable. 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer")
    ## 
    ## <param name="indepVarName"> (str) </param>
    ## <param name="fieldName"> (str) </param>
    ## <param name="doubleValues"> (List[float]) </param>
    def AddDoubleValuesFieldToIndependentVariable(tParamerters: FunctionResultParameters, indepVarName: str, fieldName: str, doubleValues: List[float]) -> None:
        """
         Adds a field of double values to an independent variable. 
        """
        pass
    
    ##  Adds a field of integer values to an independent variable. 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer")
    ## 
    ## <param name="indepVarName"> (str) </param>
    ## <param name="fieldName"> (str) </param>
    ## <param name="intValues"> (List[int]) </param>
    def AddIntegerValuesFieldToIndependentVariable(tParamerters: FunctionResultParameters, indepVarName: str, fieldName: str, intValues: List[int]) -> None:
        """
         Adds a field of integer values to an independent variable. 
        """
        pass
    
    ##  Adds a field of string values to an independent variable. 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer")
    ## 
    ## <param name="indepVarName"> (str) </param>
    ## <param name="fieldName"> (str) </param>
    ## <param name="stringValues"> (List[str]) </param>
    def AddStringValuesFieldToIndependentVariable(tParamerters: FunctionResultParameters, indepVarName: str, fieldName: str, stringValues: List[str]) -> None:
        """
         Adds a field of string values to an independent variable. 
        """
        pass
    
    ##  Ask Function Result type  
    ##  @return type (@link FunctionResultType NXOpen.CAE.PostProc.FunctionResultType@endlink):   .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer")
    @staticmethod
    def GetFunctionResultType(parameter: FunctionResultParameters) -> FunctionResultType:
        """
         Ask Function Result type  
         @return type (@link FunctionResultType NXOpen.CAE.PostProc.FunctionResultType@endlink):   .
        """
        pass
    
    ##  Gets the independent variables.
    ##  @return indepVars (@link IndependentVariable List[NXOpen.CAE.PostProc.IndependentVariable]@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer")
    @staticmethod
    def GetIndependentVariables(tParamerters: FunctionResultParameters) -> List[IndependentVariable]:
        """
         Gets the independent variables.
         @return indepVars (@link IndependentVariable List[NXOpen.CAE.PostProc.IndependentVariable]@endlink): .
        """
        pass
    
    ##  Sets domain independent variable which is used to query abscissa values for function record. 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer")
    ## 
    ## <param name="indepVarName"> (str) </param>
    def SetDomainIndependentVariable(tParamerters: FunctionResultParameters, indepVarName: str) -> None:
        """
         Sets domain independent variable which is used to query abscissa values for function record. 
        """
        pass
    
    ##  Set Function Result type  
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer")
    ##   
    def SetFunctionResultType(parameter: FunctionResultParameters, type: FunctionResultType) -> None:
        """
         Set Function Result type  
        """
        pass
    
import NXOpen
import NXOpen.CAE.FTK
##  This class provides some services for function results.  <br> To obtain an instance of this class use @link NXOpen::CAE::ResultManager::FunctionResultService NXOpen::CAE::ResultManager::FunctionResultService@endlink .  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class FunctionResultService(NXOpen.Object): 
    """ This class provides some services for function results. """


    ##  Creates 2D records which each record represents a set of X-Y values.
    ##                 <remark>These records can be used to create 2D plots, stack plots, barchart plots.</remark>
    ##  @return tRecords (@link NXOpen.CAE.FTK.ArrayRecord2D List[NXOpen.CAE.FTK.ArrayRecord2D]@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer")
    ## <param name="tResultParams"> (@link FunctionResultParameters List[NXOpen.CAE.PostProc.FunctionResultParameters]@endlink) </param>
    def CreateRecords2D(tResultParams: List[FunctionResultParameters]) -> List[NXOpen.CAE.FTK.ArrayRecord2D]:
        """
         Creates 2D records which each record represents a set of X-Y values.
                        <remark>These records can be used to create 2D plots, stack plots, barchart plots.</remark>
         @return tRecords (@link NXOpen.CAE.FTK.ArrayRecord2D List[NXOpen.CAE.FTK.ArrayRecord2D]@endlink): .
        """
        pass
    
    ##  Lists selected function records information to listing window or a specified output text file.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer")
    ##  if fileName is empty, print information to listing information window. Otherwise write information to the file 
    def ListRecordInformationToFile(tResultParams: List[FunctionResultParameters], fileName: str, listData: bool) -> None:
        """
         Lists selected function records information to listing window or a specified output text file.
        """
        pass
    
import NXOpen
import NXOpen.CAE
##  This class represnets a function result type from a result file.
##              <br> 
##             A function result tpye is defined by
##             <ol>
##                 <li>@link NXOpen::CAE::Result::Quantity NXOpen::CAE::Result::Quantity@endlink  - It specifies physical quantity of the result like Displacement, Stress etc. </li>
##                 <li>Domain variable name - It specifies the function result value domain like time, frequency, etc. </li>
##                 <li>Independent varialbes - They specify the independent variables for the function result values. </li>
##             </ol>
##              <br> 
##          <br> Not support KF.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class FunctionResultType(NXOpen.CAE.BaseResultType): 
    """ This class represnets a function result type from a result file.
            <para>
            A function result tpye is defined by
            <ol>
                <li><ja_enum>NXOpen.CAE.Result.Quantity</ja_enum> - It specifies physical quantity of the result like Displacement, Stress etc. </li>
                <li>Domain variable name - It specifies the function result value domain like time, frequency, etc. </li>
                <li>Independent varialbes - They specify the independent variables for the function result values. </li>
            </ol>
            </para>
        """


    ## Getter for property: (str) DisplayName
    ##   the display name.  
    ##      
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def DisplayName(self) -> str:
        """
        Getter for property: (str) DisplayName
          the display name.  
             
         
        """
        pass
    
    ##  Gets the abscissa unit information. 
    ##  @return A tuple consisting of (unitType, quantityName, localizedQuantityName). 
    ##  - unitType is: @link NXOpen.Unit NXOpen.Unit@endlink.
    ##  - quantityName is: str.
    ##  - localizedQuantityName is: str.

    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer")
    @staticmethod
    def GetAbscissaUnit(pFuncResultType: FunctionResultType) -> Tuple[NXOpen.Unit, str, str]:
        """
         Gets the abscissa unit information. 
         @return A tuple consisting of (unitType, quantityName, localizedQuantityName). 
         - unitType is: @link NXOpen.Unit NXOpen.Unit@endlink.
         - quantityName is: str.
         - localizedQuantityName is: str.

        """
        pass
    
    ##  Gets the independent variables. 
    ##  @return indepVars (@link IndependentVariable List[NXOpen.CAE.PostProc.IndependentVariable]@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer")
    @staticmethod
    def GetIndependentVariables(pFuncResultType: FunctionResultType) -> List[IndependentVariable]:
        """
         Gets the independent variables. 
         @return indepVars (@link IndependentVariable List[NXOpen.CAE.PostProc.IndependentVariable]@endlink): .
        """
        pass
    
    ##  Gets the ordinate unit information. 
    ##  @return A tuple consisting of (unitType, quantityName, localizedQuantityName). 
    ##  - unitType is: @link NXOpen.Unit NXOpen.Unit@endlink.
    ##  - quantityName is: str.
    ##  - localizedQuantityName is: str.

    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer")
    @staticmethod
    def GetOrdinateUnit(pFuncResultType: FunctionResultType) -> Tuple[NXOpen.Unit, str, str]:
        """
         Gets the ordinate unit information. 
         @return A tuple consisting of (unitType, quantityName, localizedQuantityName). 
         - unitType is: @link NXOpen.Unit NXOpen.Unit@endlink.
         - quantityName is: str.
         - localizedQuantityName is: str.

        """
        pass
    
import NXOpen
##   @brief  This class represnets an independent variable.  
## 
##  
##             
##             It can be a field of values or multiple fields of values. One field of values could be
##             <ol>
##             <li>
##             String values like load case names, component names, etc.
##             </li>
##             <li>
##             Integer values like node labels, element labels, etc.
##             </li>
##             <li>
##             Double values like time values, frequency values, etc.
##             </li>
##             </ol>
##             
##          <br> Not support KF.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class IndependentVariable(NXOpen.TaggedObject): 
    """ <summary> This class represnets an independent variable. </summary>
            <remarks>
            It can be a field of values or multiple fields of values. One field of values could be
            <ol>
            <li>
            String values like load case names, component names, etc.
            </li>
            <li>
            Integer values like node labels, element labels, etc.
            </li>
            <li>
            Double values like time values, frequency values, etc.
            </li>
            </ol>
            </remarks>
        """


    ##  the value type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## String</term><description> 
    ## </description> </item><item><term> 
    ## Integer</term><description> 
    ## </description> </item><item><term> 
    ## Double</term><description> 
    ## </description> </item></list>
    class FieldValueType(Enum):
        """
        Members Include: <String> <Integer> <Double>
        """
        String: int
        Integer: int
        Double: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> IndependentVariable.FieldValueType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (int) FieldCount
    ##   the field count   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return int
    @property
    def FieldCount(self) -> int:
        """
        Getter for property: (int) FieldCount
          the field count   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsDomainVariable
    ##   the option to indicate whether this independent variable is domain variable or not   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def IsDomainVariable(self) -> bool:
        """
        Getter for property: (bool) IsDomainVariable
          the option to indicate whether this independent variable is domain variable or not   
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##   the name.  
    ##      
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
          the name.  
             
         
        """
        pass
    
    ##  Gets double values for given field index.
    ##                 <remark>
    ##                 The field index starts from 0 and must be smaller than the count by @link NXOpen::CAE::PostProc::IndependentVariable::FieldCount NXOpen::CAE::PostProc::IndependentVariable::FieldCount@endlink .
    ##                 The field value type by @link NXOpen::CAE::PostProc::IndependentVariable::GetFieldValueTypeOption NXOpen::CAE::PostProc::IndependentVariable::GetFieldValueTypeOption@endlink  must be @link NXOpen::CAE::PostProc::IndependentVariable::FieldValueType::Double NXOpen::CAE::PostProc::IndependentVariable::FieldValueType::Double@endlink .
    ##                 </remark> 
    ##  @return doubleValues (List[float]): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer")
    ## 
    ## <param name="fieldIndx"> (int) </param>
    def GetDoubleValuesField(pIndepVar: IndependentVariable, fieldIndx: int) -> List[float]:
        """
         Gets double values for given field index.
                        <remark>
                        The field index starts from 0 and must be smaller than the count by @link NXOpen::CAE::PostProc::IndependentVariable::FieldCount NXOpen::CAE::PostProc::IndependentVariable::FieldCount@endlink .
                        The field value type by @link NXOpen::CAE::PostProc::IndependentVariable::GetFieldValueTypeOption NXOpen::CAE::PostProc::IndependentVariable::GetFieldValueTypeOption@endlink  must be @link NXOpen::CAE::PostProc::IndependentVariable::FieldValueType::Double NXOpen::CAE::PostProc::IndependentVariable::FieldValueType::Double@endlink .
                        </remark> 
         @return doubleValues (List[float]): .
        """
        pass
    
    ##  Gets the name for given field index.
    ##                 <remark>
    ##                 The field index starts from 0 and must be smaller than the count by @link NXOpen::CAE::PostProc::IndependentVariable::FieldCount NXOpen::CAE::PostProc::IndependentVariable::FieldCount@endlink .
    ##                 </remark> 
    ##  @return fieldName (str): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer")
    ## 
    ## <param name="fieldIndx"> (int) </param>
    def GetFieldName(pIndepVar: IndependentVariable, fieldIndx: int) -> str:
        """
         Gets the name for given field index.
                        <remark>
                        The field index starts from 0 and must be smaller than the count by @link NXOpen::CAE::PostProc::IndependentVariable::FieldCount NXOpen::CAE::PostProc::IndependentVariable::FieldCount@endlink .
                        </remark> 
         @return fieldName (str): .
        """
        pass
    
    ##  Gets the value type option for given field index.
    ##                 <remark>The field index starts from 0 and must be smaller than the count by @link NXOpen::CAE::PostProc::IndependentVariable::FieldCount NXOpen::CAE::PostProc::IndependentVariable::FieldCount@endlink .</remark>
    ##  @return valueType (@link IndependentVariable.FieldValueType NXOpen.CAE.PostProc.IndependentVariable.FieldValueType@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer")
    ## 
    ## <param name="fieldIndx"> (int) </param>
    def GetFieldValueTypeOption(pIndepVar: IndependentVariable, fieldIndx: int) -> IndependentVariable.FieldValueType:
        """
         Gets the value type option for given field index.
                        <remark>The field index starts from 0 and must be smaller than the count by @link NXOpen::CAE::PostProc::IndependentVariable::FieldCount NXOpen::CAE::PostProc::IndependentVariable::FieldCount@endlink .</remark>
         @return valueType (@link IndependentVariable.FieldValueType NXOpen.CAE.PostProc.IndependentVariable.FieldValueType@endlink): .
        """
        pass
    
    ##  Gets integer values for given field index.
    ##                 <remark>
    ##                 The field index starts from 0 and must be smaller than the count by @link NXOpen::CAE::PostProc::IndependentVariable::FieldCount NXOpen::CAE::PostProc::IndependentVariable::FieldCount@endlink .
    ##                 The field value type by @link NXOpen::CAE::PostProc::IndependentVariable::GetFieldValueTypeOption NXOpen::CAE::PostProc::IndependentVariable::GetFieldValueTypeOption@endlink  must be @link NXOpen::CAE::PostProc::IndependentVariable::FieldValueType::Integer NXOpen::CAE::PostProc::IndependentVariable::FieldValueType::Integer@endlink .
    ##                 </remark> 
    ##  @return intValues (List[int]): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer")
    ## 
    ## <param name="fieldIndx"> (int) </param>
    def GetIntegerValuesField(pIndepVar: IndependentVariable, fieldIndx: int) -> List[int]:
        """
         Gets integer values for given field index.
                        <remark>
                        The field index starts from 0 and must be smaller than the count by @link NXOpen::CAE::PostProc::IndependentVariable::FieldCount NXOpen::CAE::PostProc::IndependentVariable::FieldCount@endlink .
                        The field value type by @link NXOpen::CAE::PostProc::IndependentVariable::GetFieldValueTypeOption NXOpen::CAE::PostProc::IndependentVariable::GetFieldValueTypeOption@endlink  must be @link NXOpen::CAE::PostProc::IndependentVariable::FieldValueType::Integer NXOpen::CAE::PostProc::IndependentVariable::FieldValueType::Integer@endlink .
                        </remark> 
         @return intValues (List[int]): .
        """
        pass
    
    ##  Gets string values for given field index.
    ##                 <remark>
    ##                 The field index starts from 0 and must be smaller than the count by @link NXOpen::CAE::PostProc::IndependentVariable::FieldCount NXOpen::CAE::PostProc::IndependentVariable::FieldCount@endlink .
    ##                 The field value type by @link NXOpen::CAE::PostProc::IndependentVariable::GetFieldValueTypeOption NXOpen::CAE::PostProc::IndependentVariable::GetFieldValueTypeOption@endlink  must be @link NXOpen::CAE::PostProc::IndependentVariable::FieldValueType::String NXOpen::CAE::PostProc::IndependentVariable::FieldValueType::String@endlink .
    ##                 </remark> 
    ##  @return stringValues (List[str]): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer")
    ## 
    ## <param name="fieldIndx"> (int) </param>
    def GetStringValuesField(pIndepVar: IndependentVariable, fieldIndx: int) -> List[str]:
        """
         Gets string values for given field index.
                        <remark>
                        The field index starts from 0 and must be smaller than the count by @link NXOpen::CAE::PostProc::IndependentVariable::FieldCount NXOpen::CAE::PostProc::IndependentVariable::FieldCount@endlink .
                        The field value type by @link NXOpen::CAE::PostProc::IndependentVariable::GetFieldValueTypeOption NXOpen::CAE::PostProc::IndependentVariable::GetFieldValueTypeOption@endlink  must be @link NXOpen::CAE::PostProc::IndependentVariable::FieldValueType::String NXOpen::CAE::PostProc::IndependentVariable::FieldValueType::String@endlink .
                        </remark> 
         @return stringValues (List[str]): .
        """
        pass
    
## @package NXOpen.CAE.PostProc
## Classes, Enums and Structs under NXOpen.CAE.PostProc namespace

##  @link FunctionRecordAbscissaValueType NXOpen.CAE.PostProc.FunctionRecordAbscissaValueType @endlink is an alias for @link FunctionRecord.AbscissaValueType NXOpen.CAE.PostProc.FunctionRecord.AbscissaValueType@endlink
FunctionRecordAbscissaValueType = FunctionRecord.AbscissaValueType


##  @link FunctionRecordOrdinateValueType NXOpen.CAE.PostProc.FunctionRecordOrdinateValueType @endlink is an alias for @link FunctionRecord.OrdinateValueType NXOpen.CAE.PostProc.FunctionRecord.OrdinateValueType@endlink
FunctionRecordOrdinateValueType = FunctionRecord.OrdinateValueType


##  @link IndependentVariableFieldValueType NXOpen.CAE.PostProc.IndependentVariableFieldValueType @endlink is an alias for @link IndependentVariable.FieldValueType NXOpen.CAE.PostProc.IndependentVariable.FieldValueType@endlink
IndependentVariableFieldValueType = IndependentVariable.FieldValueType


