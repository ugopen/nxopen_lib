from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
class AeroStructuresAnnotDataS:
    ## Getter for property :(@link AeroStructuresAnnotdirectionoption NXOpen.CAE.AeroStructures.AeroStructuresAnnotdirectionoption@endlink) Direction@return @link AeroStructuresAnnotdirectionoption NXOpen.CAE.AeroStructures.AeroStructuresAnnotdirectionoption@endlink
    @property
    def Direction(self) -> AeroStructuresAnnotdirectionoption:
        """
        Getter for property Direction
        """
        pass
    
    ## Setter for property :(@link AeroStructuresAnnotdirectionoption NXOpen.CAE.AeroStructures.AeroStructuresAnnotdirectionoption@endlink) Direction
    @Direction.setter
    def Direction(self, value: AeroStructuresAnnotdirectionoption):
        """
        Getter for property DirectionSetter for property Direction
        """
        pass
    
    ## Getter for property :(bool) IsReversed@return bool
    @property
    def IsReversed(self) -> bool:
        """
        Getter for property IsReversed
        """
        pass
    
    ## Setter for property :(bool) IsReversed
    @IsReversed.setter
    def IsReversed(self, value: bool):
        """
        Getter for property IsReversedSetter for property IsReversed
        """
        pass
    
    ## Getter for property :(float) LeaderLength
    ## scale value in the range [-1,1] from smallest to largest, 0 gives default
    ## @return float
    @property
    def LeaderLength(self) -> float:
        """
        Getter for property LeaderLength
        scale value in the range [-1,1] from smallest to largest, 0 gives default

        """
        pass
    
    ## Setter for property :(float) LeaderLength
    @LeaderLength.setter
    def LeaderLength(self, value: float):
        """
        Getter for property LeaderLength
        scale value in the range [-1,1] from smallest to largest, 0 gives default
        Setter for property LeaderLength
        scale value in the range [-1,1] from smallest to largest, 0 gives default

        """
        pass
    
    ## Getter for property :(float) TextSize
    ## scale value in the range [-1,1] from shortest to longest, 0 gives default
    ## @return float
    @property
    def TextSize(self) -> float:
        """
        Getter for property TextSize
        scale value in the range [-1,1] from shortest to longest, 0 gives default

        """
        pass
    
    ## Setter for property :(float) TextSize
    @TextSize.setter
    def TextSize(self, value: float):
        """
        Getter for property TextSize
        scale value in the range [-1,1] from shortest to longest, 0 gives default
        Setter for property TextSize
        scale value in the range [-1,1] from shortest to longest, 0 gives default

        """
        pass
    


##  the Annotation direction option 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Normal</term><description> 
## </description> </item><item><term> 
## Xc</term><description> 
## </description> </item><item><term> 
## Yc</term><description> 
## </description> </item><item><term> 
## Zc</term><description> 
## </description> </item><item><term> 
## Unknown</term><description> 
## </description> </item></list>
class AeroStructuresAnnotdirectionoption(Enum):
    """
    Members Include: <Normal> <Xc> <Yc> <Zc> <Unknown>
    """
    Normal: int
    Xc: int
    Yc: int
    Zc: int
    Unknown: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> AeroStructuresAnnotdirectionoption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
import NXOpen.Annotations
import NXOpen.CAE
##   @brief  This is the  @link CAE::AeroStructures::BaseCalculation CAE::AeroStructures::BaseCalculation@endlink  
## 
##   
## 
##   <br>  Created in NX1926.0.0  <br> 

class BaseCalculation(NXOpen.NXObject): 
    """ <summary> This is the  <ja_class>CAE.AeroStructures.BaseCalculation</ja_class></summary> """


    ##  the Status type 
    ##  has not run 
    class CalculationStatus(Enum):
        """
        Members Include: <NotRun> <Error> <Success> <PreparationFailed>
        """
        NotRun: int
        Error: int
        Success: int
        PreparationFailed: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> BaseCalculation.CalculationStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Annotations.NoteBase NXOpen.Annotations.NoteBase@endlink) Annotation
    ##   the Annotation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Annotations.NoteBase
    @property
    def Annotation(self) -> NXOpen.Annotations.NoteBase:
        """
        Getter for property: (@link NXOpen.Annotations.NoteBase NXOpen.Annotations.NoteBase@endlink) Annotation
          the Annotation   
            
         
        """
        pass
    
    ## Getter for property: (str) Description
    ##   the description   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
          the description   
            
         
        """
        pass
    
    ## Getter for property: (@link ExtractionSourceSet NXOpen.CAE.AeroStructures.ExtractionSourceSet@endlink) ExtractionSourceSet
    ##   the ExtractionSourceSet for the calculation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return ExtractionSourceSet
    @property
    def ExtractionSourceSet(self) -> ExtractionSourceSet:
        """
        Getter for property: (@link ExtractionSourceSet NXOpen.CAE.AeroStructures.ExtractionSourceSet@endlink) ExtractionSourceSet
          the ExtractionSourceSet for the calculation   
            
         
        """
        pass
    
    ## Setter for property: (@link ExtractionSourceSet NXOpen.CAE.AeroStructures.ExtractionSourceSet@endlink) ExtractionSourceSet

    ##   the ExtractionSourceSet for the calculation   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ExtractionSourceSet.setter
    def ExtractionSourceSet(self, extractionSourceSet: ExtractionSourceSet):
        """
        Setter for property: (@link ExtractionSourceSet NXOpen.CAE.AeroStructures.ExtractionSourceSet@endlink) ExtractionSourceSet
          the ExtractionSourceSet for the calculation   
            
         
        """
        pass
    
    ## Getter for property: (@link LoadCaseSet NXOpen.CAE.AeroStructures.LoadCaseSet@endlink) LoadCaseSet
    ##   the LoadCaseSet used by the calculation  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return LoadCaseSet
    @property
    def LoadCaseSet(self) -> LoadCaseSet:
        """
        Getter for property: (@link LoadCaseSet NXOpen.CAE.AeroStructures.LoadCaseSet@endlink) LoadCaseSet
          the LoadCaseSet used by the calculation  
            
         
        """
        pass
    
    ## Setter for property: (@link LoadCaseSet NXOpen.CAE.AeroStructures.LoadCaseSet@endlink) LoadCaseSet

    ##   the LoadCaseSet used by the calculation  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @LoadCaseSet.setter
    def LoadCaseSet(self, loadCaseSet: LoadCaseSet):
        """
        Setter for property: (@link LoadCaseSet NXOpen.CAE.AeroStructures.LoadCaseSet@endlink) LoadCaseSet
          the LoadCaseSet used by the calculation  
            
         
        """
        pass
    
    ## Getter for property: (@link MethodDescriptor NXOpen.CAE.AeroStructures.MethodDescriptor@endlink) MethodDescriptor
    ##   the method descriptor   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return MethodDescriptor
    @property
    def MethodDescriptor(self) -> MethodDescriptor:
        """
        Getter for property: (@link MethodDescriptor NXOpen.CAE.AeroStructures.MethodDescriptor@endlink) MethodDescriptor
          the method descriptor   
            
         
        """
        pass
    
    ## Getter for property: (@link PropTable NXOpen.CAE.AeroStructures.PropTable@endlink) PropertyTable
    ##   the Property Table   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return PropTable
    @property
    def PropertyTable(self) -> PropTable:
        """
        Getter for property: (@link PropTable NXOpen.CAE.AeroStructures.PropTable@endlink) PropertyTable
          the Property Table   
            
         
        """
        pass
    
    ## Getter for property: (@link BaseCalculation.CalculationStatus NXOpen.CAE.AeroStructures.BaseCalculation.CalculationStatus@endlink) Status
    ##   the calculation status   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return BaseCalculation.CalculationStatus
    @property
    def Status(self) -> BaseCalculation.CalculationStatus:
        """
        Getter for property: (@link BaseCalculation.CalculationStatus NXOpen.CAE.AeroStructures.BaseCalculation.CalculationStatus@endlink) Status
          the calculation status   
            
         
        """
        pass
    
    ##  Create a template from the calculation 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ##  The file path to save template as 
    def CreateTemplate(calc: BaseCalculation, filePath: str) -> None:
        """
         Create a template from the calculation 
        """
        pass
    
    ##  Returns a boolean value that indicates whether the calculation has computed results 
    ##  @return hasResult (bool): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetHasResult(context: BaseCalculation) -> bool:
        """
         Returns a boolean value that indicates whether the calculation has computed results 
         @return hasResult (bool): .
        """
        pass
    
    ##  Get the value of a boolean input parameter 
    ##  @return value (bool): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetInputBooleanValue(context: BaseCalculation, parameterName: str) -> bool:
        """
         Get the value of a boolean input parameter 
         @return value (bool): .
        """
        pass
    
    ##  Returns the user comment for an input 
    ##  @return comment (str): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="inputName"> (str) </param>
    def GetInputComment(context: BaseCalculation, inputName: str) -> str:
        """
         Returns the user comment for an input 
         @return comment (str): .
        """
        pass
    
    ##  Get the value of an expanded file input parameter 
    ##  @return value (str): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetInputFileValue(context: BaseCalculation, parameterName: str) -> str:
        """
         Get the value of an expanded file input parameter 
         @return value (str): .
        """
        pass
    
    ##  Get the value of an integer input parameter 
    ##  @return value (int): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetInputIntegerValue(context: BaseCalculation, parameterName: str) -> int:
        """
         Get the value of an integer input parameter 
         @return value (int): .
        """
        pass
    
    ##  Get the value of a laminate input parameter 
    ##  @return value (@link Laminate NXOpen.CAE.AeroStructures.Laminate@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetInputLaminateValue(context: BaseCalculation, parameterName: str) -> Laminate:
        """
         Get the value of a laminate input parameter 
         @return value (@link Laminate NXOpen.CAE.AeroStructures.Laminate@endlink): .
        """
        pass
    
    ##  Get the elements where the loads are extracted from 
    ##  @return elementArray (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink):  the list of support elements, if available .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetInputLoadElements(context: BaseCalculation, parameterName: str) -> List[NXOpen.CAE.FEElement]:
        """
         Get the elements where the loads are extracted from 
         @return elementArray (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink):  the list of support elements, if available .
        """
        pass
    
    ##  Get the location (element or node) from where the loads are extracted  
    ##  @return location (@link NXOpen.CAE.Result.Location NXOpen.CAE.Result.Location@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetInputLoadLocation(context: BaseCalculation, parameterName: str) -> NXOpen.CAE.Result.Location:
        """
         Get the location (element or node) from where the loads are extracted  
         @return location (@link NXOpen.CAE.Result.Location NXOpen.CAE.Result.Location@endlink): .
        """
        pass
    
    ##  Get the nodes where the loads are extracted from 
    ##  @return nodeArray (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink):  the list of support nodes, if available .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetInputLoadNodes(context: BaseCalculation, parameterName: str) -> List[NXOpen.CAE.FENode]:
        """
         Get the nodes where the loads are extracted from 
         @return nodeArray (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink):  the list of support nodes, if available .
        """
        pass
    
    ##  Get the unit type of a load input parameter.
    ##               * Returns null if the parameter is unitless
    ##               
    ##  @return unit_type (@link NXOpen.Unit NXOpen.Unit@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetInputLoadUnit(context: BaseCalculation, parameterName: str) -> NXOpen.Unit:
        """
         Get the unit type of a load input parameter.
                      * Returns null if the parameter is unitless
                      
         @return unit_type (@link NXOpen.Unit NXOpen.Unit@endlink): .
        """
        pass
    
    ##  Get the aggregated or non-aggregated load values of an input parameter for this row.
    ##                 If the load values were aggregated, the output will be an array with only one value.
    ##                 If the values were not aggregated, the output will be an array with one value per element or node. 
    ##  @return values (List[float]): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterName"> (str) </param>
    ## <param name="loadCaseName"> (str) </param>
    def GetInputLoadValues(context: BaseCalculation, parameterName: str, loadCaseName: str) -> List[float]:
        """
         Get the aggregated or non-aggregated load values of an input parameter for this row.
                        If the load values were aggregated, the output will be an array with only one value.
                        If the values were not aggregated, the output will be an array with one value per element or node. 
         @return values (List[float]): .
        """
        pass
    
    ##  Get the aggregated or non-aggregated all load values of an input parameter
    ##                 The output will be a general scalar table, one load by row.
    ##                 If the load values were aggregated, the row will contain one column.
    ##                 If the values were not aggregated, the row will contain one value per element or node per column. 
    ##  @return loads (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetInputLoadValuesAll(context: BaseCalculation, parameterName: str) -> NXOpen.GeneralScalarTable:
        """
         Get the aggregated or non-aggregated all load values of an input parameter
                        The output will be a general scalar table, one load by row.
                        If the load values were aggregated, the row will contain one column.
                        If the values were not aggregated, the row will contain one value per element or node per column. 
         @return loads (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink): .
        """
        pass
    
    ##  Returns a list of all the current input names 
    ##  @return inputNames (List[str]): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetInputNames(context: BaseCalculation) -> List[str]:
        """
         Returns a list of all the current input names 
         @return inputNames (List[str]): .
        """
        pass
    
    ##  Get the unit type of a scalar input parameter 
    ##               * Returns null if the parameter is unitless
    ##               
    ##  @return unit_type (@link NXOpen.Unit NXOpen.Unit@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetInputScalarUnit(context: BaseCalculation, parameterName: str) -> NXOpen.Unit:
        """
         Get the unit type of a scalar input parameter 
                      * Returns null if the parameter is unitless
                      
         @return unit_type (@link NXOpen.Unit NXOpen.Unit@endlink): .
        """
        pass
    
    ##  Get the value of a scalar input parameter 
    ##  @return value (float): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetInputScalarValue(context: BaseCalculation, parameterName: str) -> float:
        """
         Get the value of a scalar input parameter 
         @return value (float): .
        """
        pass
    
    ##  Get the value of a size input parameter 
    ##  @return value (int): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetInputSizeValue(context: BaseCalculation, parameterName: str) -> int:
        """
         Get the value of a size input parameter 
         @return value (int): .
        """
        pass
    
    ##  Get the value of a string input parameter 
    ##  @return value (str): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetInputStringValue(context: BaseCalculation, parameterName: str) -> str:
        """
         Get the value of a string input parameter 
         @return value (str): .
        """
        pass
    
    ##  Get the value of a table input parameter 
    ##  @return value (@link TableParameter NXOpen.CAE.AeroStructures.TableParameter@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetInputTableValue(context: BaseCalculation, parameterName: str) -> TableParameter:
        """
         Get the value of a table input parameter 
         @return value (@link TableParameter NXOpen.CAE.AeroStructures.TableParameter@endlink): .
        """
        pass
    
    ##  Returns the laminate query manager 
    ##  @return mgr (@link LaminateQueryManager NXOpen.CAE.AeroStructures.LaminateQueryManager@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetLaminateQueryManager(context: BaseCalculation) -> LaminateQueryManager:
        """
         Returns the laminate query manager 
         @return mgr (@link LaminateQueryManager NXOpen.CAE.AeroStructures.LaminateQueryManager@endlink): .
        """
        pass
    
    ##  Return the list of log entries 
    ##  @return logsEntries (@link CalculationLogLine List[NXOpen.CAE.AeroStructures.CalculationLogLine]@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetLog(context: BaseCalculation) -> List[CalculationLogLine]:
        """
         Return the list of log entries 
         @return logsEntries (@link CalculationLogLine List[NXOpen.CAE.AeroStructures.CalculationLogLine]@endlink): .
        """
        pass
    
    ##  Returns a list of all the current output names 
    ##  @return outputNames (List[str]): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetOutputNames(context: BaseCalculation) -> List[str]:
        """
         Returns a list of all the current output names 
         @return outputNames (List[str]): .
        """
        pass
    
    ##  Returns the parameter type for a current input or output 
    ##  @return type (@link ParameterDescriptor.ParameterType NXOpen.CAE.AeroStructures.ParameterDescriptor.ParameterType@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetParameterType(context: BaseCalculation, parameterName: str) -> ParameterDescriptor.ParameterType:
        """
         Returns the parameter type for a current input or output 
         @return type (@link ParameterDescriptor.ParameterType NXOpen.CAE.AeroStructures.ParameterDescriptor.ParameterType@endlink): .
        """
        pass
    
    ##  Returns the failMode names from the last computed result
    ##  @return failModeIds (List[str]): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetResultFailModeNames(context: BaseCalculation) -> List[str]:
        """
         Returns the failMode names from the last computed result
         @return failModeIds (List[str]): .
        """
        pass
    
    ##  Get the value of a boolean input parameter for the last computed result 
    ##  @return value (bool): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetResultInputBooleanValue(context: BaseCalculation, parameterName: str) -> bool:
        """
         Get the value of a boolean input parameter for the last computed result 
         @return value (bool): .
        """
        pass
    
    ##  Returns the user comment about an input in the last computed result 
    ##  @return comment (str): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="inputName"> (str) </param>
    def GetResultInputComment(context: BaseCalculation, inputName: str) -> str:
        """
         Returns the user comment about an input in the last computed result 
         @return comment (str): .
        """
        pass
    
    ##  Get the value of a file input parameter 
    ##  @return value (str): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetResultInputFileValue(context: BaseCalculation, parameterName: str) -> str:
        """
         Get the value of a file input parameter 
         @return value (str): .
        """
        pass
    
    ##  Get the value of an integer input parameter for the last computed result 
    ##  @return value (int): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetResultInputIntegerValue(context: BaseCalculation, parameterName: str) -> int:
        """
         Get the value of an integer input parameter for the last computed result 
         @return value (int): .
        """
        pass
    
    ##  Get the shorthand notation of a laminate input parameter for the last computed result 
    ##  @return value (str): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetResultInputLaminateShorthandNotation(context: BaseCalculation, parameterName: str) -> str:
        """
         Get the shorthand notation of a laminate input parameter for the last computed result 
         @return value (str): .
        """
        pass
    
    ##  Get the unit type of a scalar input parameter for the last computed result 
    ##  @return unit_type (@link NXOpen.Unit NXOpen.Unit@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetResultInputLoadUnit(context: BaseCalculation, parameterName: str) -> NXOpen.Unit:
        """
         Get the unit type of a scalar input parameter for the last computed result 
         @return unit_type (@link NXOpen.Unit NXOpen.Unit@endlink): .
        """
        pass
    
    ##  Get the aggregated or non-aggregated load values of an input parameter for this row.
    ##                 If the load values were aggregated, the output will be an array with only one value.
    ##                 If the values were not aggregated, the output will be an array with one value per element or node. 
    ##  @return values (List[float]): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterName"> (str) </param>
    ## <param name="loadCaseName"> (str) </param>
    def GetResultInputLoadValues(context: BaseCalculation, parameterName: str, loadCaseName: str) -> List[float]:
        """
         Get the aggregated or non-aggregated load values of an input parameter for this row.
                        If the load values were aggregated, the output will be an array with only one value.
                        If the values were not aggregated, the output will be an array with one value per element or node. 
         @return values (List[float]): .
        """
        pass
    
    ##  Returns a list of all the input names used in the last computed result 
    ##  @return inputNames (List[str]): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetResultInputNames(context: BaseCalculation) -> List[str]:
        """
         Returns a list of all the input names used in the last computed result 
         @return inputNames (List[str]): .
        """
        pass
    
    ##  Get the unit type of a scalar input parameter for the last computed result 
    ##  @return unit_type (@link NXOpen.Unit NXOpen.Unit@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetResultInputScalarUnit(context: BaseCalculation, parameterName: str) -> NXOpen.Unit:
        """
         Get the unit type of a scalar input parameter for the last computed result 
         @return unit_type (@link NXOpen.Unit NXOpen.Unit@endlink): .
        """
        pass
    
    ##  Get the value of a scalar input parameter for the last computed result 
    ##  @return value (float): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetResultInputScalarValue(context: BaseCalculation, parameterName: str) -> float:
        """
         Get the value of a scalar input parameter for the last computed result 
         @return value (float): .
        """
        pass
    
    ##  Get the value of a string input parameter for the last computed result 
    ##  @return value (str): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetResultInputStringValue(context: BaseCalculation, parameterName: str) -> str:
        """
         Get the value of a string input parameter for the last computed result 
         @return value (str): .
        """
        pass
    
    ##  Returns the loadCase names used in the last computed result
    ##  @return loadCaseNames (List[str]): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetResultLoadCaseNames(context: BaseCalculation) -> List[str]:
        """
         Returns the loadCase names used in the last computed result
         @return loadCaseNames (List[str]): .
        """
        pass
    
    ##  Get the value of a boolean output parameter for the last computed result 
    ##  @return value (bool): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterName"> (str) </param>
    ## <param name="failureModeName"> (str) </param>
    ## <param name="loadCaseName"> (str) </param>
    def GetResultOutputBooleanValue(context: BaseCalculation, parameterName: str, failureModeName: str, loadCaseName: str) -> bool:
        """
         Get the value of a boolean output parameter for the last computed result 
         @return value (bool): .
        """
        pass
    
    ##  Get the value of a file output parameter 
    ##  @return value (str): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetResultOutputFileValue(context: BaseCalculation, parameterName: str) -> str:
        """
         Get the value of a file output parameter 
         @return value (str): .
        """
        pass
    
    ##  Get the value of an integer output parameter for the last computed result 
    ##  @return value (int): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterName"> (str) </param>
    ## <param name="failureModeName"> (str) </param>
    ## <param name="loadCaseName"> (str) </param>
    def GetResultOutputIntegerValue(context: BaseCalculation, parameterName: str, failureModeName: str, loadCaseName: str) -> int:
        """
         Get the value of an integer output parameter for the last computed result 
         @return value (int): .
        """
        pass
    
    ##  Returns a list of all the output names used in the last computed result
    ##  @return outputNames (List[str]): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetResultOutputNames(context: BaseCalculation) -> List[str]:
        """
         Returns a list of all the output names used in the last computed result
         @return outputNames (List[str]): .
        """
        pass
    
    ##  Get the unit type of a scalar output parameter for the last computed result 
    ##  @return unit_type (@link NXOpen.Unit NXOpen.Unit@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetResultOutputScalarUnit(context: BaseCalculation, parameterName: str) -> NXOpen.Unit:
        """
         Get the unit type of a scalar output parameter for the last computed result 
         @return unit_type (@link NXOpen.Unit NXOpen.Unit@endlink): .
        """
        pass
    
    ##  Get the value of a scalar output parameter for the last computed result 
    ##  @return value (float): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterName"> (str) </param>
    ## <param name="failureModeName"> (str) </param>
    ## <param name="loadCaseName"> (str) </param>
    def GetResultOutputScalarValue(context: BaseCalculation, parameterName: str, failureModeName: str, loadCaseName: str) -> float:
        """
         Get the value of a scalar output parameter for the last computed result 
         @return value (float): .
        """
        pass
    
    ##  Get the value of a string output parameter for the last computed result 
    ##  @return value (str): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterName"> (str) </param>
    ## <param name="failureModeName"> (str) </param>
    ## <param name="loadCaseName"> (str) </param>
    def GetResultOutputStringValue(context: BaseCalculation, parameterName: str, failureModeName: str, loadCaseName: str) -> str:
        """
         Get the value of a string output parameter for the last computed result 
         @return value (str): .
        """
        pass
    
    ##  Returns the unit type for an output in the last computed result 
    ##  @return unit_type (@link NXOpen.Unit NXOpen.Unit@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="outputName"> (str) </param>
    def GetResultOutputUnit(context: BaseCalculation, outputName: str) -> NXOpen.Unit:
        """
         Returns the unit type for an output in the last computed result 
         @return unit_type (@link NXOpen.Unit NXOpen.Unit@endlink): .
        """
        pass
    
    ##  Returns the parameter type for an input or output in the last computed result 
    ##  @return type (@link ParameterDescriptor.ParameterType NXOpen.CAE.AeroStructures.ParameterDescriptor.ParameterType@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetResultParameterType(context: BaseCalculation, parameterName: str) -> ParameterDescriptor.ParameterType:
        """
         Returns the parameter type for an input or output in the last computed result 
         @return type (@link ParameterDescriptor.ParameterType NXOpen.CAE.AeroStructures.ParameterDescriptor.ParameterType@endlink): .
        """
        pass
    
    ##  Cause scalar expressions to be updated 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def UpdateScalarExpressions(calc: BaseCalculation) -> None:
        """
         Cause scalar expressions to be updated 
        """
        pass
    
import NXOpen
##  Base abstract class for extraction source.  <br> No support for KF  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class BaseExtractionSource(NXOpen.NXObject): 
    """ Base abstract class for extraction source. """


    ##  the ExtractionSite type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Unknown</term><description> 
    ## </description> </item><item><term> 
    ## PolygonFace</term><description> 
    ## </description> </item><item><term> 
    ## PolygonEdge</term><description> 
    ## </description> </item><item><term> 
    ## PolygonBody</term><description> 
    ## </description> </item><item><term> 
    ## SelectionRecipe</term><description> 
    ## </description> </item><item><term> 
    ## Element1D</term><description> 
    ## </description> </item><item><term> 
    ## Element2D</term><description> 
    ## </description> </item><item><term> 
    ## Element3D</term><description> 
    ## </description> </item><item><term> 
    ## Node</term><description> 
    ## </description> </item><item><term> 
    ## Group</term><description> 
    ## </description> </item><item><term> 
    ## PhysicalProperty</term><description> 
    ## </description> </item><item><term> 
    ## Collector2D</term><description> 
    ## </description> </item><item><term> 
    ## Material</term><description> 
    ## </description> </item><item><term> 
    ## Section</term><description> 
    ## </description> </item><item><term> 
    ## Mesh1D</term><description> 
    ## </description> </item><item><term> 
    ## Mesh2D</term><description> 
    ## </description> </item><item><term> 
    ## LaminatePhysicalProperty</term><description> 
    ## </description> </item></list>
    class TypeEnum(Enum):
        """
        Members Include: <Unknown> <PolygonFace> <PolygonEdge> <PolygonBody> <SelectionRecipe> <Element1D> <Element2D> <Element3D> <Node> <Group> <PhysicalProperty> <Collector2D> <Material> <Section> <Mesh1D> <Mesh2D> <LaminatePhysicalProperty>
        """
        Unknown: int
        PolygonFace: int
        PolygonEdge: int
        PolygonBody: int
        SelectionRecipe: int
        Element1D: int
        Element2D: int
        Element3D: int
        Node: int
        Group: int
        PhysicalProperty: int
        Collector2D: int
        Material: int
        Section: int
        Mesh1D: int
        Mesh2D: int
        LaminatePhysicalProperty: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> BaseExtractionSource.TypeEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) BaseDefaultName
    ##   the base default name   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def BaseDefaultName(self) -> str:
        """
        Getter for property: (str) BaseDefaultName
          the base default name   
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##   the name   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
          the name   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfEntities
    ##   the number of entities in the group   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return int
    @property
    def NumberOfEntities(self) -> int:
        """
        Getter for property: (int) NumberOfEntities
          the number of entities in the group   
            
         
        """
        pass
    
    ## Getter for property: (@link BaseExtractionSource.TypeEnum NXOpen.CAE.AeroStructures.BaseExtractionSource.TypeEnum@endlink) Type
    ##   the extraction source type   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return BaseExtractionSource.TypeEnum
    @property
    def Type(self) -> BaseExtractionSource.TypeEnum:
        """
        Getter for property: (@link BaseExtractionSource.TypeEnum NXOpen.CAE.AeroStructures.BaseExtractionSource.TypeEnum@endlink) Type
          the extraction source type   
            
         
        """
        pass
    
    ##  Get the entities of this source 
    ##  @return entities (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink):  .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetEntities(source: BaseExtractionSource) -> List[NXOpen.TaggedObject]:
        """
         Get the entities of this source 
         @return entities (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink):  .
        """
        pass
    
import NXOpen
import NXOpen.CAE
##  Base journaling class for Aerostruct solutions.  <br> No support for KF  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class BaseSolution(NXOpen.NXObject): 
    """ Base journaling class for Aerostruct solutions. """


    ## Getter for property: (str) Description
    ##   the solution description   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
          the solution description   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.SimSolution NXOpen.CAE.SimSolution@endlink) ReferenceSolution
    ##   the referenced FE-Solution of the AeroStructure solution   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.CAE.SimSolution
    @property
    def ReferenceSolution(self) -> NXOpen.CAE.SimSolution:
        """
        Getter for property: (@link NXOpen.CAE.SimSolution NXOpen.CAE.SimSolution@endlink) ReferenceSolution
          the referenced FE-Solution of the AeroStructure solution   
            
         
        """
        pass
    
    ##  Returns the @link NXOpen::CAE::AeroStructures::LoadCaseCollection NXOpen::CAE::AeroStructures::LoadCaseCollection@endlink  belonging to this 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @link LoadCaseCollection NXOpen.CAE.AeroStructures.LoadCaseCollection@endlink
    @property
    def LoadCaseCollection() -> LoadCaseCollection:
        """
         Returns the @link NXOpen::CAE::AeroStructures::LoadCaseCollection NXOpen::CAE::AeroStructures::LoadCaseCollection@endlink  belonging to this 
        """
        pass
    
    ##  Returns the @link NXOpen::CAE::AeroStructures::LoadCaseSetCollection NXOpen::CAE::AeroStructures::LoadCaseSetCollection@endlink  belonging to this 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @link LoadCaseSetCollection NXOpen.CAE.AeroStructures.LoadCaseSetCollection@endlink
    @property
    def LoadCaseSetCollection() -> LoadCaseSetCollection:
        """
         Returns the @link NXOpen::CAE::AeroStructures::LoadCaseSetCollection NXOpen::CAE::AeroStructures::LoadCaseSetCollection@endlink  belonging to this 
        """
        pass
    
    ##  Access to the solve options for this session 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @link SolveOptions NXOpen.CAE.AeroStructures.SolveOptions@endlink
    @property
    def SolveOptions() -> SolveOptions:
        """
         Access to the solve options for this session 
        """
        pass
    
    ##  Renames the solution
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="name"> (str) </param>
    def Rename(solution: BaseSolution, name: str) -> None:
        """
         Renames the solution
        """
        pass
    
    ##  Solve the calculations passed in the argument belonging to this solution 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  The list of calculations from the solution to solve 
    def Solve(solution: BaseSolution, calculations: List[BaseCalculation]) -> None:
        """
         Solve the calculations passed in the argument belonging to this solution 
        """
        pass
    
    ##  Solve all the calculations in the solution 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def SolveAll(solution: BaseSolution) -> None:
        """
         Solve all the calculations in the solution 
        """
        pass
    
import NXOpen
##   @brief  This is the Calculation log line  
## 
##   
## 
##   <br>  Created in NX12.0.1  <br> 

class CalculationLogLine(NXOpen.TransientObject): 
    """ <summary> This is the Calculation log line </summary> """


    ##  Calculation logger message type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Info</term><description> 
    ## </description> </item><item><term> 
    ## Warning</term><description> 
    ## </description> </item><item><term> 
    ## Error</term><description> 
    ## </description> </item><item><term> 
    ## Unknown</term><description> 
    ## </description> </item></list>
    class MessageType(Enum):
        """
        Members Include: <Info> <Warning> <Error> <Unknown>
        """
        Info: int
        Warning: int
        Error: int
        Unknown: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CalculationLogLine.MessageType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) Failmode
    ##   the failMode   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return str
    @property
    def Failmode(self) -> str:
        """
        Getter for property: (str) Failmode
          the failMode   
            
         
        """
        pass
    
    ## Getter for property: (str) Loadcase
    ##   the loadcase name   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return str
    @property
    def Loadcase(self) -> str:
        """
        Getter for property: (str) Loadcase
          the loadcase name   
            
         
        """
        pass
    
    ## Getter for property: (str) Message
    ##   the log message   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return str
    @property
    def Message(self) -> str:
        """
        Getter for property: (str) Message
          the log message   
            
         
        """
        pass
    
    ## Getter for property: (@link CalculationLogLine.MessageType NXOpen.CAE.AeroStructures.CalculationLogLine.MessageType@endlink) MsgType
    ##   the message type   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return CalculationLogLine.MessageType
    @property
    def MsgType(self) -> CalculationLogLine.MessageType:
        """
        Getter for property: (@link CalculationLogLine.MessageType NXOpen.CAE.AeroStructures.CalculationLogLine.MessageType@endlink) MsgType
          the message type   
            
         
        """
        pass
    
    ## Getter for property: (str) Source
    ##   the source   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return str
    @property
    def Source(self) -> str:
        """
        Getter for property: (str) Source
          the source   
            
         
        """
        pass
    
    ## Getter for property: (str) Timestamp
    ##   the timestamp   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return str
    @property
    def Timestamp(self) -> str:
        """
        Getter for property: (str) Timestamp
          the timestamp   
            
         
        """
        pass
    
    ##  Dispose 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(data: CalculationLogLine) -> None:
        """
         Dispose 
        """
        pass
    
    ##  Return structure as a string line 
    ##  @return result (str): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def ToStringLine(line: CalculationLogLine) -> str:
        """
         Return structure as a string line 
         @return result (str): .
        """
        pass
    
import NXOpen
##   @brief  Represents a description value  
## 
##    <br> No support for KF  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class DescriptionValue(NXOpen.NXObject): 
    """ <summary> Represents a description value </summary> """


    ## Getter for property: (bool) AutomaticTextPropertyValue
    ##   the automatic_text_property   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def AutomaticTextPropertyValue(self) -> bool:
        """
        Getter for property: (bool) AutomaticTextPropertyValue
          the automatic_text_property   
            
         
        """
        pass
    
    ## Setter for property: (bool) AutomaticTextPropertyValue

    ##   the automatic_text_property   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @AutomaticTextPropertyValue.setter
    def AutomaticTextPropertyValue(self, property_value: bool):
        """
        Setter for property: (bool) AutomaticTextPropertyValue
          the automatic_text_property   
            
         
        """
        pass
    
##  Represents a @link NXOpen::CAE::AeroStructures::DynamicLoadCaseSet NXOpen::CAE::AeroStructures::DynamicLoadCaseSet@endlink . 
## 
##   <br>  Created in NX2206.0.0  <br> 

class DynamicLoadCaseSet(LoadCaseSet): 
    """ Represents a <ja_class>NXOpen.CAE.AeroStructures.DynamicLoadCaseSet</ja_class>. """
    pass


import NXOpen
##  Represents a collection of  @link CAE::AeroStructures::Expression CAE::AeroStructures::Expression@endlink .  <br> Use @link NXOpen::CAE::AeroStructures::ExpressionCollection NXOpen::CAE::AeroStructures::ExpressionCollection@endlink  to get the instance of this class.  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class ExpressionCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of  <ja_class>CAE.AeroStructures.Expression</ja_class>. """


    ##  Removes the expression from the solution 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  @link NXOpen::CAE::AeroStructures::Expression NXOpen::CAE::AeroStructures::Expression@endlink  to be deleted 
    @overload
    def DeleteExpression(self, solution: ExpressionCollection, expression: Expression) -> None:
        """
         Removes the expression from the solution 
        """
        pass
    
    ##  Removes the expressions from the solution .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## List of expressions to delete 
    @overload
    def DeleteExpression(self, solution: ExpressionCollection, expressionsTags: List[Expression]) -> None:
        """
         Removes the expressions from the solution .
        """
        pass
    
    ##  Finds the @link NXOpen::CAE::AeroStructures::Expression NXOpen::CAE::AeroStructures::Expression@endlink  object with the given name. 
    ##  @return found (@link Expression NXOpen.CAE.AeroStructures.Expression@endlink):  @link NXOpen::CAE::AeroStructures::Expression NXOpen::CAE::AeroStructures::Expression@endlink  object with this name. .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Name of the Expression  
    def FindObject(marginsolution: ExpressionCollection, name: str) -> Expression:
        """
         Finds the @link NXOpen::CAE::AeroStructures::Expression NXOpen::CAE::AeroStructures::Expression@endlink  object with the given name. 
         @return found (@link Expression NXOpen.CAE.AeroStructures.Expression@endlink):  @link NXOpen::CAE::AeroStructures::Expression NXOpen::CAE::AeroStructures::Expression@endlink  object with this name. .
        """
        pass
    
    ##  Renames expression.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Base name of the expressions, will be suffixed by number if not unique  
    @overload
    def RenameExpression(self, solution: ExpressionCollection, name: str, expression: Expression) -> None:
        """
         Renames expression.
        """
        pass
    
    ##  Renames expression.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Base name of the expressions, will be suffixed by number if not unique  
    @overload
    def RenameExpression(self, solution: ExpressionCollection, name: str, expressionsTags: List[Expression]) -> None:
        """
         Renames expression.
        """
        pass
    
##  Represents a @link NXOpen::CAE::AeroStructures::ExpressionResult NXOpen::CAE::AeroStructures::ExpressionResult@endlink .  <br> No support for KF  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class ExpressionResult(Expression): 
    """ Represents a <ja_class>NXOpen.CAE.AeroStructures.ExpressionResult</ja_class>. """


    ##  Enumeration defining the type of expression. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## CriticalMS</term><description> 
    ## </description> </item></list>
    class Type(Enum):
        """
        Members Include: <CriticalMS>
        """
        CriticalMS: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ExpressionResult.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Sets the calculations. 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  The list of calculations from the solution to consider 
    def SetCalculations(expression: ExpressionResult, marginCalculations: List[MarginCalculation]) -> None:
        """
         Sets the calculations. 
        """
        pass
    
    ##  Update the expression. 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def Update(expression: ExpressionResult) -> None:
        """
         Update the expression. 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::CAE::AeroStructures::Expression NXOpen::CAE::AeroStructures::Expression@endlink .  <br> No support for KF  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class Expression(NXOpen.NXObject): 
    """ Represents a <ja_class>NXOpen.CAE.AeroStructures.Expression</ja_class>. """
    pass


import NXOpen
##  Class for set of named extraction sources.  <br> No support for KF  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class ExtractionSourceSet(NXOpen.NXObject): 
    """ Class for set of named extraction sources. """


    ##  Add a single @link NXOpen::CAE::AeroStructures::BaseExtractionSource NXOpen::CAE::AeroStructures::BaseExtractionSource@endlink  item to the extraction source set.   
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  source to be added - will be renamed if necessary 
    def AddExtractionSource(sourceSet: ExtractionSourceSet, source: BaseExtractionSource) -> None:
        """
         Add a single @link NXOpen::CAE::AeroStructures::BaseExtractionSource NXOpen::CAE::AeroStructures::BaseExtractionSource@endlink  item to the extraction source set.   
        """
        pass
    
    ##  Creates a
    ##                 @link NXOpen::CAE::AeroStructures::GeometricalExtractionSource NXOpen::CAE::AeroStructures::GeometricalExtractionSource@endlink 
    ##                 If the type is not supported or the entities do not match the entity type,
    ##                 an empty extraction source is returned with type 'Unknown'.
    ##              
    ##  @return source (@link GeometricalExtractionSource NXOpen.CAE.AeroStructures.GeometricalExtractionSource@endlink):  geometrical extraction source object.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="type"> (@link BaseExtractionSource.TypeEnum NXOpen.CAE.AeroStructures.BaseExtractionSource.TypeEnum@endlink) </param>
    ## <param name="source_name"> (str) </param>
    ## <param name="entities_array"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink) </param>
    def CreateGeometricalExtractionSource(sourceSet: ExtractionSourceSet, type: BaseExtractionSource.TypeEnum, source_name: str, entities_array: List[NXOpen.TaggedObject]) -> GeometricalExtractionSource:
        """
         Creates a
                        @link NXOpen::CAE::AeroStructures::GeometricalExtractionSource NXOpen::CAE::AeroStructures::GeometricalExtractionSource@endlink 
                        If the type is not supported or the entities do not match the entity type,
                        an empty extraction source is returned with type 'Unknown'.
                     
         @return source (@link GeometricalExtractionSource NXOpen.CAE.AeroStructures.GeometricalExtractionSource@endlink):  geometrical extraction source object.
        """
        pass
    
    ##  Creates a
    ##                 @link NXOpen::CAE::AeroStructures::GeometricalExtractionSource NXOpen::CAE::AeroStructures::GeometricalExtractionSource@endlink 
    ##                 with the source type defined by the specified entity.  The
    ##                 entity is added to the source.  If the entity is not of a supported type
    ##                 an empty extraction source is returned with type 'Unknown'.
    ##              
    ##  @return source (@link GeometricalExtractionSource NXOpen.CAE.AeroStructures.GeometricalExtractionSource@endlink):  geometrical extraction source object.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="source_name"> (str) </param>
    ## <param name="entity"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def CreateGeometricalExtractionSourceFromEntity(sourceSet: ExtractionSourceSet, source_name: str, entity: NXOpen.TaggedObject) -> GeometricalExtractionSource:
        """
         Creates a
                        @link NXOpen::CAE::AeroStructures::GeometricalExtractionSource NXOpen::CAE::AeroStructures::GeometricalExtractionSource@endlink 
                        with the source type defined by the specified entity.  The
                        entity is added to the source.  If the entity is not of a supported type
                        an empty extraction source is returned with type 'Unknown'.
                     
         @return source (@link GeometricalExtractionSource NXOpen.CAE.AeroStructures.GeometricalExtractionSource@endlink):  geometrical extraction source object.
        """
        pass
    
    ##  Creates a @link NXOpen::CAE::AeroStructures::MaterialSource NXOpen::CAE::AeroStructures::MaterialSource@endlink  
    ##  @return source (@link MaterialSource NXOpen.CAE.AeroStructures.MaterialSource@endlink):  material source object.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="source_name"> (str) </param>
    ## <param name="entity"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def CreateMaterialSource(sourceSet: ExtractionSourceSet, source_name: str, entity: NXOpen.TaggedObject) -> MaterialSource:
        """
         Creates a @link NXOpen::CAE::AeroStructures::MaterialSource NXOpen::CAE::AeroStructures::MaterialSource@endlink  
         @return source (@link MaterialSource NXOpen.CAE.AeroStructures.MaterialSource@endlink):  material source object.
        """
        pass
    
    ##  Creates a @link NXOpen::CAE::AeroStructures::PhysicalPropertySource NXOpen::CAE::AeroStructures::PhysicalPropertySource@endlink  
    ##  @return source (@link PhysicalPropertySource NXOpen.CAE.AeroStructures.PhysicalPropertySource@endlink):  physical property source object.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="type"> (@link BaseExtractionSource.TypeEnum NXOpen.CAE.AeroStructures.BaseExtractionSource.TypeEnum@endlink) </param>
    ## <param name="source_name"> (str) </param>
    ## <param name="entity"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def CreatePhysicalPropertySource(sourceSet: ExtractionSourceSet, type: BaseExtractionSource.TypeEnum, source_name: str, entity: NXOpen.TaggedObject) -> PhysicalPropertySource:
        """
         Creates a @link NXOpen::CAE::AeroStructures::PhysicalPropertySource NXOpen::CAE::AeroStructures::PhysicalPropertySource@endlink  
         @return source (@link PhysicalPropertySource NXOpen.CAE.AeroStructures.PhysicalPropertySource@endlink):  physical property source object.
        """
        pass
    
    ##  Creates a @link NXOpen::CAE::AeroStructures::SectionSource NXOpen::CAE::AeroStructures::SectionSource@endlink  
    ##  @return source (@link SectionSource NXOpen.CAE.AeroStructures.SectionSource@endlink):  section source object.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="source_name"> (str) </param>
    ## <param name="entity"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def CreateSectionSource(sourceSet: ExtractionSourceSet, source_name: str, entity: NXOpen.TaggedObject) -> SectionSource:
        """
         Creates a @link NXOpen::CAE::AeroStructures::SectionSource NXOpen::CAE::AeroStructures::SectionSource@endlink  
         @return source (@link SectionSource NXOpen.CAE.AeroStructures.SectionSource@endlink):  section source object.
        """
        pass
    
    ##  Get the array of  @link NXOpen::CAE::AeroStructures::BaseExtractionSource NXOpen::CAE::AeroStructures::BaseExtractionSource@endlink  
    ##  @return source (@link BaseExtractionSource List[NXOpen.CAE.AeroStructures.BaseExtractionSource]@endlink):  extraction source objects.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetExtractionSources(sourceSet: ExtractionSourceSet) -> List[BaseExtractionSource]:
        """
         Get the array of  @link NXOpen::CAE::AeroStructures::BaseExtractionSource NXOpen::CAE::AeroStructures::BaseExtractionSource@endlink  
         @return source (@link BaseExtractionSource List[NXOpen.CAE.AeroStructures.BaseExtractionSource]@endlink):  extraction source objects.
        """
        pass
    
    ##  Return the next available default source name for a given type 
    ##  @return name (str): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="type"> (@link BaseExtractionSource.TypeEnum NXOpen.CAE.AeroStructures.BaseExtractionSource.TypeEnum@endlink) </param>
    def GetNextAvailableDefaultSourceName(sourceSet: ExtractionSourceSet, type: BaseExtractionSource.TypeEnum) -> str:
        """
         Return the next available default source name for a given type 
         @return name (str): .
        """
        pass
    
    ##  Set the array of  @link NXOpen::CAE::AeroStructures::BaseExtractionSource NXOpen::CAE::AeroStructures::BaseExtractionSource@endlink  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  extraction source objects
    def SetExtractionSources(sourceSet: ExtractionSourceSet, source: List[BaseExtractionSource]) -> None:
        """
         Set the array of  @link NXOpen::CAE::AeroStructures::BaseExtractionSource NXOpen::CAE::AeroStructures::BaseExtractionSource@endlink  
        """
        pass
    
import NXOpen
##   @brief  This is the Failure Mode  
## 
##   
## 
##   <br>  Created in NX12.0.1  <br> 

class FailureMode(NXOpen.TransientObject): 
    """ <summary> This is the Failure Mode </summary> """


    ## Getter for property: (str) Id
    ##   the id   
    ##     
    ##  
    ## Getter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return str
    @property
    def Id(self) -> str:
        """
        Getter for property: (str) Id
          the id   
            
         
        """
        pass
    
    ## Getter for property: (str) UiName
    ##   the UI name   
    ##     
    ##  
    ## Getter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return str
    @property
    def UiName(self) -> str:
        """
        Getter for property: (str) UiName
          the UI name   
            
         
        """
        pass
    
    ##  Dispose 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(data: FailureMode) -> None:
        """
         Dispose 
        """
        pass
    
import NXOpen.CAE
##   @brief  This is the FreeBody LoadExtraction class  
## 
##    <br> No support for KF  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class FreeBodyLoadExtraction(LoadExtractionStrategy): 
    """ <summary> This is the FreeBody LoadExtraction class </summary> """


    ##  Type of Component 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ## </description> </item><item><term> 
    ## X</term><description> 
    ## </description> </item><item><term> 
    ## Y</term><description> 
    ## </description> </item><item><term> 
    ## Z</term><description> 
    ## </description> </item><item><term> 
    ## PlanarMagnitudeXY</term><description> 
    ## </description> </item><item><term> 
    ## PlanarMagnitudeXZ</term><description> 
    ## </description> </item><item><term> 
    ## PlanarMagnitudeZY</term><description> 
    ## </description> </item><item><term> 
    ## Magnitude</term><description> 
    ## </description> </item></list>
    class Component(Enum):
        """
        Members Include: <NotSet> <X> <Y> <Z> <PlanarMagnitudeXY> <PlanarMagnitudeXZ> <PlanarMagnitudeZY> <Magnitude>
        """
        NotSet: int
        X: int
        Y: int
        Z: int
        PlanarMagnitudeXY: int
        PlanarMagnitudeXZ: int
        PlanarMagnitudeZY: int
        Magnitude: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FreeBodyLoadExtraction.Component:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Type of Result
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ## </description> </item><item><term> 
    ## Force</term><description> 
    ## </description> </item><item><term> 
    ## Moment</term><description> 
    ## </description> </item></list>
    class Result(Enum):
        """
        Members Include: <NotSet> <Force> <Moment>
        """
        NotSet: int
        Force: int
        Moment: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FreeBodyLoadExtraction.Result:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Get Component Type 
    ##  @return component (@link FreeBodyLoadExtraction.Component NXOpen.CAE.AeroStructures.FreeBodyLoadExtraction.Component@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetComponent(loadExt: FreeBodyLoadExtraction) -> FreeBodyLoadExtraction.Component:
        """
         Get Component Type 
         @return component (@link FreeBodyLoadExtraction.Component NXOpen.CAE.AeroStructures.FreeBodyLoadExtraction.Component@endlink): .
        """
        pass
    
    ##  Get Free Body 
    ##  @return freeBody (@link NXOpen.CAE.NodalForceReport NXOpen.CAE.NodalForceReport@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetFreeBody(loadExt: FreeBodyLoadExtraction) -> NXOpen.CAE.NodalForceReport:
        """
         Get Free Body 
         @return freeBody (@link NXOpen.CAE.NodalForceReport NXOpen.CAE.NodalForceReport@endlink): .
        """
        pass
    
    ##  Get Matrix Manip 
    ##  @return manip (@link MatrixManip NXOpen.CAE.AeroStructures.MatrixManip@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetMatrixManip(loadExt: FreeBodyLoadExtraction) -> MatrixManip:
        """
         Get Matrix Manip 
         @return manip (@link MatrixManip NXOpen.CAE.AeroStructures.MatrixManip@endlink): .
        """
        pass
    
    ##  Get Result Type 
    ##  @return result (@link FreeBodyLoadExtraction.Result NXOpen.CAE.AeroStructures.FreeBodyLoadExtraction.Result@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetResult(loadExt: FreeBodyLoadExtraction) -> FreeBodyLoadExtraction.Result:
        """
         Get Result Type 
         @return result (@link FreeBodyLoadExtraction.Result NXOpen.CAE.AeroStructures.FreeBodyLoadExtraction.Result@endlink): .
        """
        pass
    
    ##  Set Component Type 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="component"> (@link FreeBodyLoadExtraction.Component NXOpen.CAE.AeroStructures.FreeBodyLoadExtraction.Component@endlink) </param>
    def SetComponent(loadExt: FreeBodyLoadExtraction, component: FreeBodyLoadExtraction.Component) -> None:
        """
         Set Component Type 
        """
        pass
    
    ##  Set Free Body 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="freeBody"> (@link NXOpen.CAE.NodalForceReport NXOpen.CAE.NodalForceReport@endlink) </param>
    def SetFreeBody(loadExt: FreeBodyLoadExtraction, freeBody: NXOpen.CAE.NodalForceReport) -> None:
        """
         Set Free Body 
        """
        pass
    
    ##  Set Matrix Manip 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="manip"> (@link MatrixManip NXOpen.CAE.AeroStructures.MatrixManip@endlink) </param>
    def SetMatrixManip(loadExt: FreeBodyLoadExtraction, manip: MatrixManip) -> None:
        """
         Set Matrix Manip 
        """
        pass
    
    ##  Set Result Type 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="result"> (@link FreeBodyLoadExtraction.Result NXOpen.CAE.AeroStructures.FreeBodyLoadExtraction.Result@endlink) </param>
    def SetResult(loadExt: FreeBodyLoadExtraction, result: FreeBodyLoadExtraction.Result) -> None:
        """
         Set Result Type 
        """
        pass
    
##  Geometrical extraction source class.  <br> To create a new instance of this class, use @link NXOpen::CAE::AeroStructures::ExtractionSourceSet::CreateGeometricalExtractionSource  NXOpen::CAE::AeroStructures::ExtractionSourceSet::CreateGeometricalExtractionSource @endlink  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class GeometricalExtractionSource(BaseExtractionSource): 
    """ Geometrical extraction source class. """
    pass


import NXOpen
##  This is a manager to the @link CAE::AeroStructures::GraphicalReport CAE::AeroStructures::GraphicalReport@endlink  class.
##     Object of type @link CAE::AeroStructures::GraphicalReport CAE::AeroStructures::GraphicalReport@endlink  can be
##     created and edited only through this class
##      <br> To create a new instance of this class, use @link NXOpen::CAE::AeroStructures::GraphicalReportCollection::CreateGraphicalReportBuilder  NXOpen::CAE::AeroStructures::GraphicalReportCollection::CreateGraphicalReportBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class GraphicalReportBuilder(NXOpen.Builder): 
    """ This is a manager to the <ja_class>CAE.AeroStructures.GraphicalReport</ja_class> class.
    Object of type <ja_class>CAE.AeroStructures.GraphicalReport</ja_class> can be
    created and edited only through this class
    """


    ## Getter for property: (str) Description
    ##   the graphical report description   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
          the graphical report description   
            
         
        """
        pass
    
    ## Setter for property: (str) Description

    ##   the graphical report description   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @Description.setter
    def Description(self, title: str):
        """
        Setter for property: (str) Description
          the graphical report description   
            
         
        """
        pass
    
    ## Getter for property: (str) Title
    ##   the graphical report title  
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def Title(self) -> str:
        """
        Getter for property: (str) Title
          the graphical report title  
            
         
        """
        pass
    
    ## Setter for property: (str) Title

    ##   the graphical report title  
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @Title.setter
    def Title(self, title: str):
        """
        Setter for property: (str) Title
          the graphical report title  
            
         
        """
        pass
    
import NXOpen
##  Represents a collection of AeroStruct GraphicalReport  <br> Use @link CAE::AeroStructures::MarginSolution::GraphicalReportCollection CAE::AeroStructures::MarginSolution::GraphicalReportCollection@endlink  to get the instance of this class.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class GraphicalReportCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of AeroStruct GraphicalReport """


    ##  Creates a @link NXOpen::CAE::AeroStructures::GraphicalReportBuilder NXOpen::CAE::AeroStructures::GraphicalReportBuilder@endlink  
    ##  @return builder (@link GraphicalReportBuilder NXOpen.CAE.AeroStructures.GraphicalReportBuilder@endlink):  Builder object.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  @link NXOpen::CAE::AeroStructures::GraphicalReport NXOpen::CAE::AeroStructures::GraphicalReport@endlink  
    def CreateGraphicalReportBuilder(marginSolution: GraphicalReportCollection, graphicalReport: GraphicalReport) -> GraphicalReportBuilder:
        """
         Creates a @link NXOpen::CAE::AeroStructures::GraphicalReportBuilder NXOpen::CAE::AeroStructures::GraphicalReportBuilder@endlink  
         @return builder (@link GraphicalReportBuilder NXOpen.CAE.AeroStructures.GraphicalReportBuilder@endlink):  Builder object.
        """
        pass
    
    ##  Delete an AeroStruct graphical report. 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  @link NXOpen::CAE::AeroStructures::GraphicalReport NXOpen::CAE::AeroStructures::GraphicalReport@endlink  
    def DeleteGraphicalReport(marginSolution: GraphicalReportCollection, graphicalReport: GraphicalReport) -> None:
        """
         Delete an AeroStruct graphical report. 
        """
        pass
    
    ##  Finds the @link NXOpen::CAE::AeroStructures::GraphicalReport NXOpen::CAE::AeroStructures::GraphicalReport@endlink  object with the given name. 
    ##  @return found (@link GraphicalReport NXOpen.CAE.AeroStructures.GraphicalReport@endlink):  @link NXOpen::CAE::AeroStructures::GraphicalReport NXOpen::CAE::AeroStructures::GraphicalReport@endlink  object with this name. .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  GraphicalReport title  
    def FindObject(margin_solution: GraphicalReportCollection, title: str) -> GraphicalReport:
        """
         Finds the @link NXOpen::CAE::AeroStructures::GraphicalReport NXOpen::CAE::AeroStructures::GraphicalReport@endlink  object with the given name. 
         @return found (@link GraphicalReport NXOpen.CAE.AeroStructures.GraphicalReport@endlink):  @link NXOpen::CAE::AeroStructures::GraphicalReport NXOpen::CAE::AeroStructures::GraphicalReport@endlink  object with this name. .
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::CAE::AeroStructures::GraphicalReport NXOpen::CAE::AeroStructures::GraphicalReport@endlink .  <br> To create or edit an instance of this class, use @link NXOpen::CAE::AeroStructures::GraphicalReportBuilder  NXOpen::CAE::AeroStructures::GraphicalReportBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class GraphicalReport(NXOpen.NXObject): 
    """ Represents a <ja_class>NXOpen.CAE.AeroStructures.GraphicalReport</ja_class>. """


    ## Getter for property: (str) Description
    ##   the description   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
          the description   
            
         
        """
        pass
    
    ## Getter for property: (str) FilePath
    ##   the file path   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def FilePath(self) -> str:
        """
        Getter for property: (str) FilePath
          the file path   
            
         
        """
        pass
    
    ## Getter for property: (str) Title
    ##   the title   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def Title(self) -> str:
        """
        Getter for property: (str) Title
          the title   
            
         
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::CAE::AeroStructures::LaminateHelper NXOpen::CAE::AeroStructures::LaminateHelper@endlink  object.  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LaminateHelper(NXOpen.Object): 
    """ Represents a <ja_class>NXOpen.CAE.AeroStructures.LaminateHelper</ja_class> object. """


    ##  Create an empty local laminate 
    ##  @return local (@link LocalLaminate NXOpen.CAE.AeroStructures.LocalLaminate@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def NewLocalLaminate() -> LocalLaminate:
        """
         Create an empty local laminate 
         @return local (@link LocalLaminate NXOpen.CAE.AeroStructures.LocalLaminate@endlink): .
        """
        pass
    
import NXOpen
##   @brief  Represents a laminate manager  
## 
##    <br> No support for KF  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LaminateQueryManager(NXOpen.NXObject): 
    """ <summary> Represents a laminate manager </summary> """


    ##  Adds a laminate query object to the manager 
    ##  @return status (bool): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="query"> (@link LaminateQuery NXOpen.CAE.AeroStructures.LaminateQuery@endlink) </param>
    def AddLaminateQuery(manager: LaminateQueryManager, query: LaminateQuery) -> bool:
        """
         Adds a laminate query object to the manager 
         @return status (bool): .
        """
        pass
    
    ##  Create a laminate query object 
    ##  @return query (@link LaminateQuery NXOpen.CAE.AeroStructures.LaminateQuery@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="laminateBaseName"> (str) </param>
    ## <param name="laminateQueryOwner"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="isManagedQuery"> (bool) </param>
    def CreateLaminateQuery(manager: LaminateQueryManager, laminateBaseName: str, laminateQueryOwner: NXOpen.NXObject, isManagedQuery: bool) -> LaminateQuery:
        """
         Create a laminate query object 
         @return query (@link LaminateQuery NXOpen.CAE.AeroStructures.LaminateQuery@endlink): .
        """
        pass
    
    ##  Create a managed copy of the laminate query object 
    ##  @return query (@link LaminateQuery NXOpen.CAE.AeroStructures.LaminateQuery@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="laminateBaseName"> (str) </param>
    ## <param name="laminateQueryOwner"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="baseLaminateObject"> (@link LaminateQuery NXOpen.CAE.AeroStructures.LaminateQuery@endlink) </param>
    def CreateLaminateQueryCopy(manager: LaminateQueryManager, laminateBaseName: str, laminateQueryOwner: NXOpen.NXObject, baseLaminateObject: LaminateQuery) -> LaminateQuery:
        """
         Create a managed copy of the laminate query object 
         @return query (@link LaminateQuery NXOpen.CAE.AeroStructures.LaminateQuery@endlink): .
        """
        pass
    
    ##  Returns the list of available laminate queries 
    ##  @return A tuple consisting of (laminateQueryNames, laminateQueryTags). 
    ##  - laminateQueryNames is: List[str].
    ##  - laminateQueryTags is: @link NXOpen.NXObject List[NXOpen.NXObject]@endlink.

    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetLaminateQueries(manager: LaminateQueryManager) -> Tuple[List[str], List[NXOpen.NXObject]]:
        """
         Returns the list of available laminate queries 
         @return A tuple consisting of (laminateQueryNames, laminateQueryTags). 
         - laminateQueryNames is: List[str].
         - laminateQueryTags is: @link NXOpen.NXObject List[NXOpen.NXObject]@endlink.

        """
        pass
    
    ##  Find a laminate query object by name
    ##  @return query (@link LaminateQuery NXOpen.CAE.AeroStructures.LaminateQuery@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="laminateBaseName"> (str) </param>
    def GetLaminateQuery(manager: LaminateQueryManager, laminateBaseName: str) -> LaminateQuery:
        """
         Find a laminate query object by name
         @return query (@link LaminateQuery NXOpen.CAE.AeroStructures.LaminateQuery@endlink): .
        """
        pass
    
    ##  Removes a laminate query from the manager 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="query"> (@link LaminateQuery NXOpen.CAE.AeroStructures.LaminateQuery@endlink) </param>
    def RemoveLaminateQuery(manager: LaminateQueryManager, query: LaminateQuery) -> None:
        """
         Removes a laminate query from the manager 
        """
        pass
    
import NXOpen
##   @brief  Represents a laminate query  
## 
##    <br> No support for KF  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LaminateQuery(NXOpen.NXObject): 
    """ <summary> Represents a laminate query </summary> """


    ##  Enumeration defining the manner in which the laminate properties
    ##              * are to be extracted. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## MaterialAngle</term><description> 
    ## </description> </item><item><term> 
    ## Angle</term><description> 
    ## </description> </item><item><term> 
    ## Vector</term><description> 
    ## </description> </item></list>
    class AngleDefinitionTypeEnum(Enum):
        """
        Members Include: <MaterialAngle> <Angle> <Vector>
        """
        MaterialAngle: int
        Angle: int
        Vector: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> LaminateQuery.AngleDefinitionTypeEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Enumeration for reference entity types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ExistingLaminate</term><description> 
    ## </description> </item><item><term> 
    ## LaminatePhysicalProperty</term><description> 
    ## </description> </item><item><term> 
    ## Element2D</term><description> 
    ## </description> </item><item><term> 
    ## PolygonFace</term><description> 
    ## </description> </item><item><term> 
    ## Mesh</term><description> 
    ## </description> </item><item><term> 
    ## Collector2D</term><description> 
    ## </description> </item><item><term> 
    ## Group</term><description> 
    ## </description> </item><item><term> 
    ## SelectionRecipe</term><description> 
    ## </description> </item><item><term> 
    ## Unknown</term><description> 
    ## </description> </item><item><term> 
    ## ExtractionSource</term><description> 
    ## </description> </item></list>
    class ReferenceEntityTypeEnum(Enum):
        """
        Members Include: <ExistingLaminate> <LaminatePhysicalProperty> <Element2D> <PolygonFace> <Mesh> <Collector2D> <Group> <SelectionRecipe> <Unknown> <ExtractionSource>
        """
        ExistingLaminate: int
        LaminatePhysicalProperty: int
        Element2D: int
        PolygonFace: int
        Mesh: int
        Collector2D: int
        Group: int
        SelectionRecipe: int
        Unknown: int
        ExtractionSource: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> LaminateQuery.ReferenceEntityTypeEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link LaminateQuery.AngleDefinitionTypeEnum NXOpen.CAE.AeroStructures.LaminateQuery.AngleDefinitionTypeEnum@endlink) AngleDefinitionType
    ##   the current angle definition type   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return LaminateQuery.AngleDefinitionTypeEnum
    @property
    def AngleDefinitionType(self) -> LaminateQuery.AngleDefinitionTypeEnum:
        """
        Getter for property: (@link LaminateQuery.AngleDefinitionTypeEnum NXOpen.CAE.AeroStructures.LaminateQuery.AngleDefinitionTypeEnum@endlink) AngleDefinitionType
          the current angle definition type   
            
         
        """
        pass
    
    ## Getter for property: (bool) ExtractionInvertNormal
    ##   the laminate extraction normal flag.  
    ##      
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def ExtractionInvertNormal(self) -> bool:
        """
        Getter for property: (bool) ExtractionInvertNormal
          the laminate extraction normal flag.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ExtractionReversePlies
    ##   the laminate extraction reverse ply order flag.  
    ##      
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def ExtractionReversePlies(self) -> bool:
        """
        Getter for property: (bool) ExtractionReversePlies
          the laminate extraction reverse ply order flag.  
             
         
        """
        pass
    
    ## Getter for property: (str) ExtractionSourceName
    ##   the extraction source name  
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def ExtractionSourceName(self) -> str:
        """
        Getter for property: (str) ExtractionSourceName
          the extraction source name  
            
         
        """
        pass
    
    ## Setter for property: (str) ExtractionSourceName

    ##   the extraction source name  
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @ExtractionSourceName.setter
    def ExtractionSourceName(self, name: str):
        """
        Setter for property: (str) ExtractionSourceName
          the extraction source name  
            
         
        """
        pass
    
    ## Getter for property: (str) LaminateBaseName
    ##   the laminate base name   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def LaminateBaseName(self) -> str:
        """
        Getter for property: (str) LaminateBaseName
          the laminate base name   
            
         
        """
        pass
    
    ## Setter for property: (str) LaminateBaseName

    ##   the laminate base name   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @LaminateBaseName.setter
    def LaminateBaseName(self, laminateBaseName: str):
        """
        Setter for property: (str) LaminateBaseName
          the laminate base name   
            
         
        """
        pass
    
    ## Getter for property: (str) LaminateName
    ##   the laminate name   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def LaminateName(self) -> str:
        """
        Getter for property: (str) LaminateName
          the laminate name   
            
         
        """
        pass
    
    ## Setter for property: (str) LaminateName

    ##   the laminate name   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @LaminateName.setter
    def LaminateName(self, laminateName: str):
        """
        Setter for property: (str) LaminateName
          the laminate name   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ReferenceEntity
    ##   the selected entity tag   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def ReferenceEntity(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ReferenceEntity
          the selected entity tag   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ReferenceEntity

    ##   the selected entity tag   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ReferenceEntity.setter
    def ReferenceEntity(self, referenceEntity: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ReferenceEntity
          the selected entity tag   
            
         
        """
        pass
    
    ## Getter for property: (@link LaminateQuery.ReferenceEntityTypeEnum NXOpen.CAE.AeroStructures.LaminateQuery.ReferenceEntityTypeEnum@endlink) ReferenceEntityType
    ##   the current reference entity type   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return LaminateQuery.ReferenceEntityTypeEnum
    @property
    def ReferenceEntityType(self) -> LaminateQuery.ReferenceEntityTypeEnum:
        """
        Getter for property: (@link LaminateQuery.ReferenceEntityTypeEnum NXOpen.CAE.AeroStructures.LaminateQuery.ReferenceEntityTypeEnum@endlink) ReferenceEntityType
          the current reference entity type   
            
         
        """
        pass
    
    ## Setter for property: (@link LaminateQuery.ReferenceEntityTypeEnum NXOpen.CAE.AeroStructures.LaminateQuery.ReferenceEntityTypeEnum@endlink) ReferenceEntityType

    ##   the current reference entity type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ReferenceEntityType.setter
    def ReferenceEntityType(self, referenceEntityType: LaminateQuery.ReferenceEntityTypeEnum):
        """
        Setter for property: (@link LaminateQuery.ReferenceEntityTypeEnum NXOpen.CAE.AeroStructures.LaminateQuery.ReferenceEntityTypeEnum@endlink) ReferenceEntityType
          the current reference entity type   
            
         
        """
        pass
    
    ##  Gets the laminate extraction angle. 
    ##  @return laminateAngle (float): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetExtractionAngle(query: LaminateQuery) -> float:
        """
         Gets the laminate extraction angle. 
         @return laminateAngle (float): .
        """
        pass
    
    ##  Gets the laminate extraction angle tolerance. 
    ##  @return angleTolerance (float): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Unit for the angle value, if NULL returns the value in radians 
    def GetExtractionAngleTolerance(query: LaminateQuery, angleUnit: NXOpen.Unit) -> float:
        """
         Gets the laminate extraction angle tolerance. 
         @return angleTolerance (float): .
        """
        pass
    
    ##  Gets the laminate extraction direction. 
    ##  @return direction (@link NXOpen.Vector3d NXOpen.Vector3d@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetExtractionDirection(query: LaminateQuery) -> NXOpen.Vector3d:
        """
         Gets the laminate extraction direction. 
         @return direction (@link NXOpen.Vector3d NXOpen.Vector3d@endlink): .
        """
        pass
    
    ##  Get the extraction source 
    ##  @return source (@link BaseExtractionSource NXOpen.CAE.AeroStructures.BaseExtractionSource@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetExtractionSource(query: LaminateQuery) -> BaseExtractionSource:
        """
         Get the extraction source 
         @return source (@link BaseExtractionSource NXOpen.CAE.AeroStructures.BaseExtractionSource@endlink): .
        """
        pass
    
    ##  Finds the available physical properties of type laminate 
    ##  @return A tuple consisting of (physicalPropertyNames, physicalPropertyLaminates). 
    ##  - physicalPropertyNames is: List[str].
    ##  - physicalPropertyLaminates is: @link NXOpen.NXObject List[NXOpen.NXObject]@endlink.

    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetLaminatePhysicalProperties(query: LaminateQuery) -> Tuple[List[str], List[NXOpen.NXObject]]:
        """
         Finds the available physical properties of type laminate 
         @return A tuple consisting of (physicalPropertyNames, physicalPropertyLaminates). 
         - physicalPropertyNames is: List[str].
         - physicalPropertyLaminates is: @link NXOpen.NXObject List[NXOpen.NXObject]@endlink.

        """
        pass
    
    ##  Returns the list of available laminate queries 
    ##  @return A tuple consisting of (laminateQueryNames, laminateQueryTags). 
    ##  - laminateQueryNames is: List[str].
    ##  - laminateQueryTags is: @link NXOpen.NXObject List[NXOpen.NXObject]@endlink.

    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetLaminateQueries(query: LaminateQuery) -> Tuple[List[str], List[NXOpen.NXObject]]:
        """
         Returns the list of available laminate queries 
         @return A tuple consisting of (laminateQueryNames, laminateQueryTags). 
         - laminateQueryNames is: List[str].
         - laminateQueryTags is: @link NXOpen.NXObject List[NXOpen.NXObject]@endlink.

        """
        pass
    
    ##  Returns the renference entity type name 
    ##  @return referenceEntityTypeName (str):  The reference entity name .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="referenceEntityType"> (@link LaminateQuery.ReferenceEntityTypeEnum NXOpen.CAE.AeroStructures.LaminateQuery.ReferenceEntityTypeEnum@endlink) </param>
    def GetReferenceEntityTypeName(query: LaminateQuery, referenceEntityType: LaminateQuery.ReferenceEntityTypeEnum) -> str:
        """
         Returns the renference entity type name 
         @return referenceEntityTypeName (str):  The reference entity name .
        """
        pass
    
    ##  Returns the renference entity type names 
    ##  @return referenceEntityTypeNames (List[str]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetReferenceEntityTypeNames(query: LaminateQuery) -> List[str]:
        """
         Returns the renference entity type names 
         @return referenceEntityTypeNames (List[str]): .
        """
        pass
    
    ##  Returns the renference entity type names 
    ##  @return A tuple consisting of (referenceEntityIndexes, referenceEntityTypeNames). 
    ##  - referenceEntityIndexes is: List[int].
    ##  - referenceEntityTypeNames is: List[str].

    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetReferenceEntityTypesAndNames(query: LaminateQuery) -> Tuple[List[int], List[str]]:
        """
         Returns the renference entity type names 
         @return A tuple consisting of (referenceEntityIndexes, referenceEntityTypeNames). 
         - referenceEntityIndexes is: List[int].
         - referenceEntityTypeNames is: List[str].

        """
        pass
    
    ##  Sets the laminate extraction angle. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  laminate angle in radians 
    def SetExtractionAngle(query: LaminateQuery, laminateAngle: float) -> None:
        """
         Sets the laminate extraction angle. 
        """
        pass
    
    ##  Sets the laminate extraction direction. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  
    def SetExtractionDirection(query: LaminateQuery, direction: NXOpen.Vector3d) -> None:
        """
         Sets the laminate extraction direction. 
        """
        pass
    
    ##  Sets the internal values of the query  (with entity) 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## <param name="query"> (@link LaminateQuery NXOpen.CAE.AeroStructures.LaminateQuery@endlink) </param>
    ## <param name="laminateBaseName"> (str) </param>
    ## <param name="laminateName"> (str) </param>
    ## <param name="referenceEntityType"> (@link LaminateQuery.ReferenceEntityTypeEnum NXOpen.CAE.AeroStructures.LaminateQuery.ReferenceEntityTypeEnum@endlink) </param>
    ## <param name="referenceEntity"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    ## <param name="extractionAngleInRadians"> (float) </param>
    ## <param name="extractionDirection"> (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) </param>
    ## <param name="extractionType"> (@link LaminateQuery.AngleDefinitionTypeEnum NXOpen.CAE.AeroStructures.LaminateQuery.AngleDefinitionTypeEnum@endlink) </param>
    ## <param name="extractionAngleToleranceInRadians"> (float) </param>
    ## <param name="invertNormals"> (bool) </param>
    ## <param name="reverseOrder"> (bool) </param>
    @overload
    def SetValues(self, query: LaminateQuery, laminateBaseName: str, laminateName: str, referenceEntityType: LaminateQuery.ReferenceEntityTypeEnum, referenceEntity: NXOpen.TaggedObject, extractionAngleInRadians: float, extractionDirection: NXOpen.Vector3d, extractionType: LaminateQuery.AngleDefinitionTypeEnum, extractionAngleToleranceInRadians: float, invertNormals: bool, reverseOrder: bool) -> None:
        """
         Sets the internal values of the query  (with entity) 
        """
        pass
    
    ##  Sets the internal values of the query  (with extraction source) 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## <param name="query"> (@link LaminateQuery NXOpen.CAE.AeroStructures.LaminateQuery@endlink) </param>
    ## <param name="laminateBaseName"> (str) </param>
    ## <param name="laminateName"> (str) </param>
    ## <param name="sourceName"> (str) </param>
    ## <param name="extractionAngleInRadians"> (float) </param>
    ## <param name="extractionDirection"> (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) </param>
    ## <param name="extractionType"> (@link LaminateQuery.AngleDefinitionTypeEnum NXOpen.CAE.AeroStructures.LaminateQuery.AngleDefinitionTypeEnum@endlink) </param>
    ## <param name="extractionAngleToleranceInRadians"> (float) </param>
    ## <param name="invertNormals"> (bool) </param>
    ## <param name="reverseOrder"> (bool) </param>
    @overload
    def SetValues(self, query: LaminateQuery, laminateBaseName: str, laminateName: str, sourceName: str, extractionAngleInRadians: float, extractionDirection: NXOpen.Vector3d, extractionType: LaminateQuery.AngleDefinitionTypeEnum, extractionAngleToleranceInRadians: float, invertNormals: bool, reverseOrder: bool) -> None:
        """
         Sets the internal values of the query  (with extraction source) 
        """
        pass
    
import NXOpen
##   @brief  Represents a laminate value  
## 
##    <br> No support for KF  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LaminateValue(NXOpen.NXObject): 
    """ <summary> Represents a laminate value </summary> """


    ## Getter for property: (@link LaminateQuery NXOpen.CAE.AeroStructures.LaminateQuery@endlink) LaminateQuery
    ##   the active Query   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return LaminateQuery
    @property
    def LaminateQuery(self) -> LaminateQuery:
        """
        Getter for property: (@link LaminateQuery NXOpen.CAE.AeroStructures.LaminateQuery@endlink) LaminateQuery
          the active Query   
            
         
        """
        pass
    
    ## Setter for property: (@link LaminateQuery NXOpen.CAE.AeroStructures.LaminateQuery@endlink) LaminateQuery

    ##   the active Query   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @LaminateQuery.setter
    def LaminateQuery(self, query: LaminateQuery):
        """
        Setter for property: (@link LaminateQuery NXOpen.CAE.AeroStructures.LaminateQuery@endlink) LaminateQuery
          the active Query   
            
         
        """
        pass
    
import NXOpen
import NXOpen.CAE.AeroStructures.Author
##  Represents a @link NXOpen::CAE::AeroStructures::Laminate NXOpen::CAE::AeroStructures::Laminate@endlink  object.  <br> No support for KF  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class Laminate(NXOpen.TransientObject): 
    """ Represents a <ja_class>NXOpen.CAE.AeroStructures.Laminate</ja_class> object. """


    ##  Represents the laminate reference location 
    ##  
    class LamRefLoc(Enum):
        """
        Members Include: <Top> <Middle> <Bottom> <Specify>
        """
        Top: int
        Middle: int
        Bottom: int
        Specify: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Laminate.LamRefLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) IsBalanced
    ##   the laminate is balanced   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def IsBalanced(self) -> bool:
        """
        Getter for property: (bool) IsBalanced
          the laminate is balanced   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsSymmetric
    ##   the laminate is symmetric   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def IsSymmetric(self) -> bool:
        """
        Getter for property: (bool) IsSymmetric
          the laminate is symmetric   
            
         
        """
        pass
    
    ## Getter for property: (float) MassDensity
    ##   the mass density   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def MassDensity(self) -> float:
        """
        Getter for property: (float) MassDensity
          the mass density   
            
         
        """
        pass
    
    ## Getter for property: (float) MassPerUnitArea
    ##   the mass per unit area   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def MassPerUnitArea(self) -> float:
        """
        Getter for property: (float) MassPerUnitArea
          the mass per unit area   
            
         
        """
        pass
    
    ## Getter for property: (int) NumMaterials
    ##   the number of distinct materials used   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def NumMaterials(self) -> int:
        """
        Getter for property: (int) NumMaterials
          the number of distinct materials used   
            
         
        """
        pass
    
    ## Getter for property: (int) NumPlies
    ##   the number of plies   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def NumPlies(self) -> int:
        """
        Getter for property: (int) NumPlies
          the number of plies   
            
         
        """
        pass
    
    ## Getter for property: (str) PhysPropName
    ##   the name of the laminate physical property.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def PhysPropName(self) -> str:
        """
        Getter for property: (str) PhysPropName
          the name of the laminate physical property.  
             
         
        """
        pass
    
    ## Getter for property: (float) TotalThickness
    ##   the total thickness of the composite   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def TotalThickness(self) -> float:
        """
        Getter for property: (float) TotalThickness
          the total thickness of the composite   
            
         
        """
        pass
    
    ##  Create an editable copy of the laminate 
    ##  @return local (@link LocalLaminate NXOpen.CAE.AeroStructures.LocalLaminate@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def CreateLocalLaminateByCopy(param: Laminate) -> LocalLaminate:
        """
         Create an editable copy of the laminate 
         @return local (@link LocalLaminate NXOpen.CAE.AeroStructures.LocalLaminate@endlink): .
        """
        pass
    
    ##  Frees the object from memory.  After this method is called, it is
    ##             illegal to use the object. In .NET, this method is automatically
    ##             called when the object is deleted by the garbage collector. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(param: Laminate) -> None:
        """
         Frees the object from memory.  After this method is called, it is
                    illegal to use the object. In .NET, this method is automatically
                    called when the object is deleted by the garbage collector. 
        """
        pass
    
    ##  The ABD matrix 
    ##  @return matrix (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetABD(param: Laminate) -> NXOpen.GeneralScalarTable:
        """
         The ABD matrix 
         @return matrix (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink): .
        """
        pass
    
    ##  Bending Shear Modulus 
    ##  @return value (float): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBendingShearModulus(param: Laminate) -> float:
        """
         Bending Shear Modulus 
         @return value (float): .
        """
        pass
    
    ##  Bending Youngs Modulus 
    ##  @return matrix (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBendingYoungsModulus(param: Laminate) -> NXOpen.GeneralScalarTable:
        """
         Bending Youngs Modulus 
         @return matrix (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink): .
        """
        pass
    
    ##  Fetch the bottom fiber distance 
    ##  @return distance (float): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBottomFiberDistance(param: Laminate) -> float:
        """
         Fetch the bottom fiber distance 
         @return distance (float): .
        """
        pass
    
    ##  Obtain interlaminar values per ply per LC (stress_yz, stress_zx)
    ##             
    ##  @return A tuple consisting of (stress_yz, stress_zx). 
    ##  - stress_yz is: @link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink. num_load_cases rows  and num_plies columns .
    ##  - stress_zx is: @link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink.

    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  true for ply coordinates, false for laminate coordinates 
    @staticmethod
    def GetInterlaminarShearStress(param: Laminate, use_ply_coordinates: bool, op_temp: List[float], nxx: List[float], nyy: List[float], nxy: List[float], mxx: List[float], myy: List[float], mxy: List[float], tsx: List[float], tsy: List[float]) -> Tuple[NXOpen.GeneralScalarTable, NXOpen.GeneralScalarTable]:
        """
         Obtain interlaminar values per ply per LC (stress_yz, stress_zx)
                    
         @return A tuple consisting of (stress_yz, stress_zx). 
         - stress_yz is: @link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink. num_load_cases rows  and num_plies columns .
         - stress_zx is: @link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink.

        """
        pass
    
    ##  Fetch the laminate angle in radians 
    ##  @return radians (float): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetLaminateAngle(param: Laminate) -> float:
        """
         Fetch the laminate angle in radians 
         @return radians (float): .
        """
        pass
    
    ##  The list of material names 
    ##  @return material_names (List[str]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetMaterialNames(param: Laminate) -> List[str]:
        """
         The list of material names 
         @return material_names (List[str]): .
        """
        pass
    
    ##  Number of plies per orientation using given material (index) 
    ##  @return plies (List[int]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="material_index"> (int) </param>
    def GetMaterialPlyCount(param: Laminate, material_index: int) -> List[int]:
        """
         Number of plies per orientation using given material (index) 
         @return plies (List[int]): .
        """
        pass
    
    ##  Thickness of plies per orientation using given material (index) 
    ##  @return thicknesses (List[float]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="material_index"> (int) </param>
    def GetMaterialThickness(param: Laminate, material_index: int) -> List[float]:
        """
         Thickness of plies per orientation using given material (index) 
         @return thicknesses (List[float]): .
        """
        pass
    
    ##  Mid1 
    ##  @return matrix (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetMid1(param: Laminate) -> NXOpen.GeneralScalarTable:
        """
         Mid1 
         @return matrix (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink): .
        """
        pass
    
    ##  Mid2 
    ##  @return matrix (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetMid2(param: Laminate) -> NXOpen.GeneralScalarTable:
        """
         Mid2 
         @return matrix (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink): .
        """
        pass
    
    ##  Mid3 
    ##  @return matrix (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetMid3(param: Laminate) -> NXOpen.GeneralScalarTable:
        """
         Mid3 
         @return matrix (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink): .
        """
        pass
    
    ##  Mid4 
    ##  @return matrix (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetMid4(param: Laminate) -> NXOpen.GeneralScalarTable:
        """
         Mid4 
         @return matrix (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink): .
        """
        pass
    
    ##  The list of orientations used 
    ##  @return orientations (List[float]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetOrientations(param: Laminate) -> List[float]:
        """
         The list of orientations used 
         @return orientations (List[float]): .
        """
        pass
    
    ##  Ply angle 
    ##  @return value (float): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="ply_index"> (int) </param>
    def GetPlyAngle(param: Laminate, ply_index: int) -> float:
        """
         Ply angle 
         @return value (float): .
        """
        pass
    
    ##  Ply angles 
    ##  @return values (List[float]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPlyAngles(param: Laminate) -> List[float]:
        """
         Ply angles 
         @return values (List[float]): .
        """
        pass
    
    ##  Ply Id 
    ##  @return id (int): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="ply_index"> (int) </param>
    def GetPlyId(param: Laminate, ply_index: int) -> int:
        """
         Ply Id 
         @return id (int): .
        """
        pass
    
    ##  Ply Ids 
    ##  @return ids (List[int]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPlyIds(param: Laminate) -> List[int]:
        """
         Ply Ids 
         @return ids (List[int]): .
        """
        pass
    
    ##  Ply material 
    ##  @return material (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="ply_index"> (int) </param>
    def GetPlyMaterial(param: Laminate, ply_index: int) -> NXOpen.PhysicalMaterial:
        """
         Ply material 
         @return material (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink): .
        """
        pass
    
    ##  Ply material name 
    ##  @return name (str): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="ply_index"> (int) </param>
    def GetPlyMaterialName(param: Laminate, ply_index: int) -> str:
        """
         Ply material name 
         @return name (str): .
        """
        pass
    
    ##  Ply material names 
    ##  @return names (List[str]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPlyMaterialNames(param: Laminate) -> List[str]:
        """
         Ply material names 
         @return names (List[str]): .
        """
        pass
    
    ##  Ply materials 
    ##  @return materials (@link NXOpen.PhysicalMaterial List[NXOpen.PhysicalMaterial]@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPlyMaterials(param: Laminate) -> List[NXOpen.PhysicalMaterial]:
        """
         Ply materials 
         @return materials (@link NXOpen.PhysicalMaterial List[NXOpen.PhysicalMaterial]@endlink): .
        """
        pass
    
    ##  Ply thickness 
    ##  @return value (float): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="ply_index"> (int) </param>
    def GetPlyThickness(param: Laminate, ply_index: int) -> float:
        """
         Ply thickness 
         @return value (float): .
        """
        pass
    
    ##  Ply thicknesses 
    ##  @return values (List[float]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPlyThicknesses(param: Laminate) -> List[float]:
        """
         Ply thicknesses 
         @return values (List[float]): .
        """
        pass
    
    ##  Poissons Ratio 
    ##  @return matrix (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPoissonsRatio(param: Laminate) -> NXOpen.GeneralScalarTable:
        """
         Poissons Ratio 
         @return matrix (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink): .
        """
        pass
    
    ##  Top|Middle|Bottom|Specify 
    ##  @return plane (@link Laminate.LamRefLoc NXOpen.CAE.AeroStructures.Laminate.LamRefLoc@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetReferencePlane(param: Laminate) -> Laminate.LamRefLoc:
        """
         Top|Middle|Bottom|Specify 
         @return plane (@link Laminate.LamRefLoc NXOpen.CAE.AeroStructures.Laminate.LamRefLoc@endlink): .
        """
        pass
    
    ##  Fetch the reference temperature 
    ##  @return temp (float): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetReferenceTemperature(param: Laminate) -> float:
        """
         Fetch the reference temperature 
         @return temp (float): .
        """
        pass
    
    ##  Shear Modulus 
    ##  @return matrix (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetShearModulus(param: Laminate) -> NXOpen.GeneralScalarTable:
        """
         Shear Modulus 
         @return matrix (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink): .
        """
        pass
    
    ##  Specific Heat 
    ##  @return value (float): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSpecificHeat(param: Laminate) -> float:
        """
         Specific Heat 
         @return value (float): .
        """
        pass
    
    ##  The A section of the ABD matrix 
    ##  @return matrix (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStiffnessA(param: Laminate) -> NXOpen.GeneralScalarTable:
        """
         The A section of the ABD matrix 
         @return matrix (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink): .
        """
        pass
    
    ##  The B section of the ABD matrix 
    ##  @return matrix (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStiffnessB(param: Laminate) -> NXOpen.GeneralScalarTable:
        """
         The B section of the ABD matrix 
         @return matrix (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink): .
        """
        pass
    
    ##  The D section of the ABD matrix 
    ##  @return matrix (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStiffnessD(param: Laminate) -> NXOpen.GeneralScalarTable:
        """
         The D section of the ABD matrix 
         @return matrix (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink): .
        """
        pass
    
    ##  Obtain strain values per ply per LC 
    ##  @return A tuple consisting of (xx_strain, yy_strain, xy_strain). 
    ##  - xx_strain is: @link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink. num_load_cases rows  and num_plies columns .
    ##  - yy_strain is: @link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink.
    ##  - xy_strain is: @link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink.

    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  true for ply coordinates, false for laminate coordinates 
    @staticmethod
    def GetStrainPerPly(param: Laminate, use_ply_coordinates: bool, op_temp: List[float], nxx: List[float], nyy: List[float], nxy: List[float], mxx: List[float], myy: List[float], mxy: List[float]) -> Tuple[NXOpen.GeneralScalarTable, NXOpen.GeneralScalarTable, NXOpen.GeneralScalarTable]:
        """
         Obtain strain values per ply per LC 
         @return A tuple consisting of (xx_strain, yy_strain, xy_strain). 
         - xx_strain is: @link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink. num_load_cases rows  and num_plies columns .
         - yy_strain is: @link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink.
         - xy_strain is: @link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink.

        """
        pass
    
    ##  Obtain stress values per ply per LC 
    ##  @return A tuple consisting of (xx_stress, yy_stress, xy_stress). 
    ##  - xx_stress is: @link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink. num_load_cases rows  and num_plies columns .
    ##  - yy_stress is: @link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink.
    ##  - xy_stress is: @link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink.

    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  true for ply coordinates, false for laminate coordinates 
    @staticmethod
    def GetStressPerPly(param: Laminate, use_ply_coordinates: bool, op_temp: List[float], nxx: List[float], nyy: List[float], nxy: List[float], mxx: List[float], myy: List[float], mxy: List[float]) -> Tuple[NXOpen.GeneralScalarTable, NXOpen.GeneralScalarTable, NXOpen.GeneralScalarTable]:
        """
         Obtain stress values per ply per LC 
         @return A tuple consisting of (xx_stress, yy_stress, xy_stress). 
         - xx_stress is: @link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink. num_load_cases rows  and num_plies columns .
         - yy_stress is: @link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink.
         - xy_stress is: @link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink.

        """
        pass
    
    ##  Thermal Conductivity Coefficient 
    ##  @return matrix (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetThermalConductivityCoeff(param: Laminate) -> NXOpen.GeneralScalarTable:
        """
         Thermal Conductivity Coefficient 
         @return matrix (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink): .
        """
        pass
    
    ##  Thermal Expansion Coefficient 
    ##  @return matrix (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetThermalExpansionCoeff(param: Laminate) -> NXOpen.GeneralScalarTable:
        """
         Thermal Expansion Coefficient 
         @return matrix (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink): .
        """
        pass
    
    ##  The transverse shear matrix 
    ##  @return matrix (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetTransverseShear(param: Laminate) -> NXOpen.GeneralScalarTable:
        """
         The transverse shear matrix 
         @return matrix (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink): .
        """
        pass
    
    ##  Unit system 
    ##  @return unitSystem (@link NXOpen.CAE.AeroStructures.Author.CalculationContext.UnitSystem NXOpen.CAE.AeroStructures.Author.CalculationContext.UnitSystem@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetUnitSystem(param: Laminate) -> NXOpen.CAE.AeroStructures.Author.CalculationContext.UnitSystem:
        """
         Unit system 
         @return unitSystem (@link NXOpen.CAE.AeroStructures.Author.CalculationContext.UnitSystem NXOpen.CAE.AeroStructures.Author.CalculationContext.UnitSystem@endlink): .
        """
        pass
    
    ##  Youngs Modulus 
    ##  @return matrix (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetYoungsModulus(param: Laminate) -> NXOpen.GeneralScalarTable:
        """
         Youngs Modulus 
         @return matrix (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink): .
        """
        pass
    
    ##  Ask if the ply signs are inverted 
    ##  @return inverted (bool): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def IsInverted(param: Laminate) -> bool:
        """
         Ask if the ply signs are inverted 
         @return inverted (bool): .
        """
        pass
    
    ##  Ask if the ply order is reversed 
    ##  @return reversed (bool): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def IsReversed(param: Laminate) -> bool:
        """
         Ask if the ply order is reversed 
         @return reversed (bool): .
        """
        pass
    
    ##  If this ply uses a ply material 
    ##  @return is_ply_material (bool): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="ply_index"> (int) </param>
    def IsUsingPlyMaterial(param: Laminate, ply_index: int) -> bool:
        """
         If this ply uses a ply material 
         @return is_ply_material (bool): .
        """
        pass
    
    ##  If plies use ply materials 
    ##  @return using_ply_materials (List[bool]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def IsUsingPlyMaterials(param: Laminate) -> List[bool]:
        """
         If plies use ply materials 
         @return using_ply_materials (List[bool]): .
        """
        pass
    
    ##  Write out laminate information 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="plies"> (bool) </param>
    ## <param name="props"> (bool) </param>
    ## <param name="mats"> (bool) </param>
    def PrintLaminateInfo(param: Laminate, plies: bool, props: bool, mats: bool) -> None:
        """
         Write out laminate information 
        """
        pass
    
    ##  Unit system 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="unitSystem"> (@link NXOpen.CAE.AeroStructures.Author.CalculationContext.UnitSystem NXOpen.CAE.AeroStructures.Author.CalculationContext.UnitSystem@endlink) </param>
    def SetUnitSystem(param: Laminate, unitSystem: NXOpen.CAE.AeroStructures.Author.CalculationContext.UnitSystem) -> None:
        """
         Unit system 
        """
        pass
    
    ##  Laminate shorthand notation 
    ##  @return shorthand_notation (str): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def ToShorthandNotation(param: Laminate) -> str:
        """
         Laminate shorthand notation 
         @return shorthand_notation (str): .
        """
        pass
    
import NXOpen
##  Represents a collection of AeroStruct LoadCases  <br> Use @link CAE::AeroStructures::BaseSolution::LoadCaseCollection CAE::AeroStructures::BaseSolution::LoadCaseCollection@endlink  to get the instance of this class.  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class LoadCaseCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of AeroStruct LoadCases """


    ##  Creates a @link NXOpen::CAE::AeroStructures::LoadCaseListBuilder NXOpen::CAE::AeroStructures::LoadCaseListBuilder@endlink  
    ##  @return builder (@link LoadCaseListBuilder NXOpen.CAE.AeroStructures.LoadCaseListBuilder@endlink):   Builder object.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    def CreateLoadCaseListBuilder(basesolution: LoadCaseCollection) -> LoadCaseListBuilder:
        """
         Creates a @link NXOpen::CAE::AeroStructures::LoadCaseListBuilder NXOpen::CAE::AeroStructures::LoadCaseListBuilder@endlink  
         @return builder (@link LoadCaseListBuilder NXOpen.CAE.AeroStructures.LoadCaseListBuilder@endlink):   Builder object.
        """
        pass
    
    ##  Deletes a @link NXOpen::CAE::AeroStructures::LoadCase NXOpen::CAE::AeroStructures::LoadCase@endlink . 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  @link NXOpen::CAE::AeroStructures::LoadCase NXOpen::CAE::AeroStructures::LoadCase@endlink  
    def DeleteLoadCase(basesolution: LoadCaseCollection, loadcase: LoadCase) -> None:
        """
         Deletes a @link NXOpen::CAE::AeroStructures::LoadCase NXOpen::CAE::AeroStructures::LoadCase@endlink . 
        """
        pass
    
    ##  Finds the @link NXOpen::CAE::AeroStructures::LoadCase NXOpen::CAE::AeroStructures::LoadCase@endlink  object with the given name. 
    ##  @return found (@link LoadCase NXOpen.CAE.AeroStructures.LoadCase@endlink):  @link NXOpen::CAE::AeroStructures::LoadCase NXOpen::CAE::AeroStructures::LoadCase@endlink  object with this name. .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  Name of the LocalDefinition  
    def FindObject(solution: LoadCaseCollection, name: str) -> LoadCase:
        """
         Finds the @link NXOpen::CAE::AeroStructures::LoadCase NXOpen::CAE::AeroStructures::LoadCase@endlink  object with the given name. 
         @return found (@link LoadCase NXOpen.CAE.AeroStructures.LoadCase@endlink):  @link NXOpen::CAE::AeroStructures::LoadCase NXOpen::CAE::AeroStructures::LoadCase@endlink  object with this name. .
        """
        pass
    
import NXOpen
##  This is a manager to the loadcases of @link CAE::AeroStructures::BaseSolution CAE::AeroStructures::BaseSolution@endlink  class.
##      <br> To create a new instance of this class, use @link NXOpen::CAE::AeroStructures::LoadCaseCollection::CreateLoadCaseListBuilder  NXOpen::CAE::AeroStructures::LoadCaseCollection::CreateLoadCaseListBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class LoadCaseListBuilder(NXOpen.Builder): 
    """ This is a manager to the loadcases of <ja_class>CAE.AeroStructures.BaseSolution</ja_class> class.
    """


    ##  Register the removable of orphaned load cases 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def RegisterCleanup(load_case_list_builder: LoadCaseListBuilder) -> None:
        """
         Register the removable of orphaned load cases 
        """
        pass
    
import NXOpen
##  This is a manager to the @link CAE::AeroStructures::LoadCaseSet CAE::AeroStructures::LoadCaseSet@endlink  class.
##     Object of type @link CAE::AeroStructures::LoadCaseSet CAE::AeroStructures::LoadCaseSet@endlink  can be
##     created and edited only through this class
##      <br> To create a new instance of this class, use @link NXOpen::CAE::AeroStructures::LoadCaseSetCollection::CreateLoadCaseSetBuilder  NXOpen::CAE::AeroStructures::LoadCaseSetCollection::CreateLoadCaseSetBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class LoadCaseSetBuilder(NXOpen.Builder): 
    """ This is a manager to the <ja_class>CAE.AeroStructures.LoadCaseSet</ja_class> class.
    Object of type <ja_class>CAE.AeroStructures.LoadCaseSet</ja_class> can be
    created and edited only through this class
    """


    ## Getter for property: (str) Description
    ##   the load case set description   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return str
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
          the load case set description   
            
         
        """
        pass
    
    ## Setter for property: (str) Description

    ##   the load case set description   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @Description.setter
    def Description(self, title: str):
        """
        Setter for property: (str) Description
          the load case set description   
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##   the load case set name  
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
          the load case set name  
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##   the load case set name  
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Name.setter
    def Name(self, title: str):
        """
        Setter for property: (str) Name
          the load case set name  
            
         
        """
        pass
    
    ##  Insert a loadcase to the load case set builder 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="loadcase"> (@link LoadCase NXOpen.CAE.AeroStructures.LoadCase@endlink) </param>
    def AddLoadCase(load_case_set_builder: LoadCaseSetBuilder, loadcase: LoadCase) -> None:
        """
         Insert a loadcase to the load case set builder 
        """
        pass
    
    ##  Remove a loadcase from the load case set builder 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="loadcase"> (@link LoadCase NXOpen.CAE.AeroStructures.LoadCase@endlink) </param>
    def RemoveLoadCase(load_case_set_builder: LoadCaseSetBuilder, loadcase: LoadCase) -> None:
        """
         Remove a loadcase from the load case set builder 
        """
        pass
    
import NXOpen
##  Represents a collection of AeroStruct LoadCases  <br> Use @link CAE::AeroStructures::BaseSolution::LoadCaseSetCollection CAE::AeroStructures::BaseSolution::LoadCaseSetCollection@endlink  to get the instance of this class.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class LoadCaseSetCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of AeroStruct LoadCases """


    ##  Create a AeroStruct loadcase set. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  @link NXOpen::CAE::AeroStructures::LoadCaseSet NXOpen::CAE::AeroStructures::LoadCaseSet@endlink  
    def CloneLoadCaseSet(basesolution: LoadCaseSetCollection, loadcaseset: LoadCaseSet) -> None:
        """
         Create a AeroStruct loadcase set. 
        """
        pass
    
    ##  Create a AeroStruct loadcase set. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  @link NXOpen::CAE::AeroStructures::LoadCaseSetBuilder NXOpen::CAE::AeroStructures::LoadCaseSetBuilder@endlink  
    def CreateLoadCaseSet(basesolution: LoadCaseSetCollection, builder: LoadCaseSetBuilder) -> None:
        """
         Create a AeroStruct loadcase set. 
        """
        pass
    
    ##  Creates a @link NXOpen::CAE::AeroStructures::LoadCaseSetBuilder NXOpen::CAE::AeroStructures::LoadCaseSetBuilder@endlink  
    ##  @return builder (@link LoadCaseSetBuilder NXOpen.CAE.AeroStructures.LoadCaseSetBuilder@endlink):  Builder object.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  @link NXOpen::CAE::AeroStructures::LoadCase NXOpen::CAE::AeroStructures::LoadCase@endlink  to be edited 
    def CreateLoadCaseSetBuilder(basesolution: LoadCaseSetCollection, loadcaeset: LoadCaseSet) -> LoadCaseSetBuilder:
        """
         Creates a @link NXOpen::CAE::AeroStructures::LoadCaseSetBuilder NXOpen::CAE::AeroStructures::LoadCaseSetBuilder@endlink  
         @return builder (@link LoadCaseSetBuilder NXOpen.CAE.AeroStructures.LoadCaseSetBuilder@endlink):  Builder object.
        """
        pass
    
    ##  Delete a AeroStruct loadcase set. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  @link NXOpen::CAE::AeroStructures::LoadCaseSet NXOpen::CAE::AeroStructures::LoadCaseSet@endlink  
    def DeleteLoadCaseSet(basesolution: LoadCaseSetCollection, loadcaseset: LoadCaseSet) -> None:
        """
         Delete a AeroStruct loadcase set. 
        """
        pass
    
    ##  Finds the @link NXOpen::CAE::AeroStructures::LoadCaseSet NXOpen::CAE::AeroStructures::LoadCaseSet@endlink  object with the given name. 
    ##             The name must be in the format {SolutionName}/{LoadCaseName} where {SolutionName} is the name of
    ##             the referenced FE solution, and {LoadCaseName} is the name of the load case to find.  
    ##             {SolutionName}/{LoadCaseName} is the value returned by @link NXOpen::CAE::AeroStructures::LoadCase NXOpen::CAE::AeroStructures::LoadCase@endlink .Name.
    ##          
    ##  @return found (@link LoadCaseSet NXOpen.CAE.AeroStructures.LoadCaseSet@endlink):  @link NXOpen::CAE::AeroStructures::LoadCaseSet NXOpen::CAE::AeroStructures::LoadCaseSet@endlink  object with this name. .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  LoadCaseSet Name  
    def FindObject(margin_solution: LoadCaseSetCollection, name: str) -> LoadCaseSet:
        """
         Finds the @link NXOpen::CAE::AeroStructures::LoadCaseSet NXOpen::CAE::AeroStructures::LoadCaseSet@endlink  object with the given name. 
                    The name must be in the format {SolutionName}/{LoadCaseName} where {SolutionName} is the name of
                    the referenced FE solution, and {LoadCaseName} is the name of the load case to find.  
                    {SolutionName}/{LoadCaseName} is the value returned by @link NXOpen::CAE::AeroStructures::LoadCase NXOpen::CAE::AeroStructures::LoadCase@endlink .Name.
                 
         @return found (@link LoadCaseSet NXOpen.CAE.AeroStructures.LoadCaseSet@endlink):  @link NXOpen::CAE::AeroStructures::LoadCaseSet NXOpen::CAE::AeroStructures::LoadCaseSet@endlink  object with this name. .
        """
        pass
    
    ##  Import Load Case Set from file 
    ##  @return A tuple consisting of (loadcaseset, errorMsg, warningMsg). 
    ##  - loadcaseset is: @link LoadCaseSet NXOpen.CAE.AeroStructures.LoadCaseSet@endlink. @link NXOpen::CAE::AeroStructures::LoadCaseSet NXOpen::CAE::AeroStructures::LoadCaseSet@endlink  .
    ##  - errorMsg is: str.
    ##  - warningMsg is: List[str].

    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="fileName"> (str) </param>
    @staticmethod
    def ImportLoadCaseSetFromFile(basesolution: LoadCaseSetCollection, fileName: str) -> Tuple[LoadCaseSet, str, List[str]]:
        """
         Import Load Case Set from file 
         @return A tuple consisting of (loadcaseset, errorMsg, warningMsg). 
         - loadcaseset is: @link LoadCaseSet NXOpen.CAE.AeroStructures.LoadCaseSet@endlink. @link NXOpen::CAE::AeroStructures::LoadCaseSet NXOpen::CAE::AeroStructures::LoadCaseSet@endlink  .
         - errorMsg is: str.
         - warningMsg is: List[str].

        """
        pass
    
import NXOpen
##  Represents a collection of AeroStruct LoadCases  <br> Use @link CAE::AeroStructures::LoadCaseSet::LoadCaseCollection CAE::AeroStructures::LoadCaseSet::LoadCaseCollection@endlink  to get the instance of this class.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class LoadCaseSetLoadCaseCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of AeroStruct LoadCases """


    ##  Finds the @link NXOpen::CAE::AeroStructures::LoadCase NXOpen::CAE::AeroStructures::LoadCase@endlink  object with the given name. 
    ##  @return found (@link LoadCase NXOpen.CAE.AeroStructures.LoadCase@endlink):  @link NXOpen::CAE::AeroStructures::LoadCase NXOpen::CAE::AeroStructures::LoadCase@endlink  object with this name. .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  Name of the LocalDefinition  
    def FindObject(loadCaseSetTag: LoadCaseSetLoadCaseCollection, name: str) -> LoadCase:
        """
         Finds the @link NXOpen::CAE::AeroStructures::LoadCase NXOpen::CAE::AeroStructures::LoadCase@endlink  object with the given name. 
         @return found (@link LoadCase NXOpen.CAE.AeroStructures.LoadCase@endlink):  @link NXOpen::CAE::AeroStructures::LoadCase NXOpen::CAE::AeroStructures::LoadCase@endlink  object with this name. .
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::CAE::AeroStructures::LoadCaseSet NXOpen::CAE::AeroStructures::LoadCaseSet@endlink .  <br> To create or edit an instance of this class, use @link NXOpen::CAE::AeroStructures::LoadCaseSetBuilder  NXOpen::CAE::AeroStructures::LoadCaseSetBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class LoadCaseSet(NXOpen.NXObject): 
    """ Represents a <ja_class>NXOpen.CAE.AeroStructures.LoadCaseSet</ja_class>. """


    ##  Returns the @link NXOpen::CAE::AeroStructures::LoadCaseSetLoadCaseCollection NXOpen::CAE::AeroStructures::LoadCaseSetLoadCaseCollection@endlink  belonging to this 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @link LoadCaseSetLoadCaseCollection NXOpen.CAE.AeroStructures.LoadCaseSetLoadCaseCollection@endlink
    @property
    def LoadCaseCollection() -> LoadCaseSetLoadCaseCollection:
        """
         Returns the @link NXOpen::CAE::AeroStructures::LoadCaseSetLoadCaseCollection NXOpen::CAE::AeroStructures::LoadCaseSetLoadCaseCollection@endlink  belonging to this 
        """
        pass
    
    ##  Export @link NXOpen::CAE::AeroStructures::LoadCaseSet NXOpen::CAE::AeroStructures::LoadCaseSet@endlink  to given file 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="fullPathName"> (str) </param>
    def Export(lcs: LoadCaseSet, fullPathName: str) -> None:
        """
         Export @link NXOpen::CAE::AeroStructures::LoadCaseSet NXOpen::CAE::AeroStructures::LoadCaseSet@endlink  to given file 
        """
        pass
    
import NXOpen
import NXOpen.CAE
##  Represents a @link NXOpen::CAE::AeroStructures::LoadCase NXOpen::CAE::AeroStructures::LoadCase@endlink . 
## 
##   <br>  Created in NX12.0.0  <br> 

class LoadCase(NXOpen.NXObject): 
    """ Represents a <ja_class>NXOpen.CAE.AeroStructures.LoadCase</ja_class>. """


    ##  the Loadcase type 
    ##  Unitary loadcase 
    class LoadCaseType(Enum):
        """
        Members Include: <Unitary> <Combined>
        """
        Unitary: int
        Combined: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> LoadCase.LoadCaseType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.CAE.BaseLoadcase NXOpen.CAE.BaseLoadcase@endlink) BaseLoadCase
    ##   the associated CAE::BaseLoadCase   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.CAE.BaseLoadcase
    @property
    def BaseLoadCase(self) -> NXOpen.CAE.BaseLoadcase:
        """
        Getter for property: (@link NXOpen.CAE.BaseLoadcase NXOpen.CAE.BaseLoadcase@endlink) BaseLoadCase
          the associated CAE::BaseLoadCase   
            
         
        """
        pass
    
    ## Getter for property: (str) StrengthRequirement
    ##   the strength requirement   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def StrengthRequirement(self) -> str:
        """
        Getter for property: (str) StrengthRequirement
          the strength requirement   
            
         
        """
        pass
    
import NXOpen
##   @brief  Represents a proper load extraction strategy  
## 
##    <br> No support for KF  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class LoadExtractionStrategy(NXOpen.NXObject): 
    """ <summary> Represents a proper load extraction strategy </summary> """
    pass


import NXOpen
##   @brief  Represents a proper load extraction value  
## 
##    <br> No support for KF  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class LoadExtractionValue(NXOpen.NXObject): 
    """ <summary> Represents a proper load extraction value </summary> """


    ##  Map Operations 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ## </description> </item><item><term> 
    ## User</term><description> 
    ## </description> </item><item><term> 
    ## Manual</term><description> 
    ## </description> </item><item><term> 
    ## FreeBody</term><description> 
    ## </description> </item></list>
    class ActiveStrategy(Enum):
        """
        Members Include: <NotSet> <User> <Manual> <FreeBody>
        """
        NotSet: int
        User: int
        Manual: int
        FreeBody: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> LoadExtractionValue.ActiveStrategy:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link LoadExtractionStrategy NXOpen.CAE.AeroStructures.LoadExtractionStrategy@endlink) Strategy
    ##   the active strategy   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return LoadExtractionStrategy
    @property
    def Strategy(self) -> LoadExtractionStrategy:
        """
        Getter for property: (@link LoadExtractionStrategy NXOpen.CAE.AeroStructures.LoadExtractionStrategy@endlink) Strategy
          the active strategy   
            
         
        """
        pass
    
    ## Setter for property: (@link LoadExtractionStrategy NXOpen.CAE.AeroStructures.LoadExtractionStrategy@endlink) Strategy

    ##   the active strategy   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Strategy.setter
    def Strategy(self, strat: LoadExtractionStrategy):
        """
        Setter for property: (@link LoadExtractionStrategy NXOpen.CAE.AeroStructures.LoadExtractionStrategy@endlink) Strategy
          the active strategy   
            
         
        """
        pass
    
    ## Getter for property: (@link LoadExtractionValue.ActiveStrategy NXOpen.CAE.AeroStructures.LoadExtractionValue.ActiveStrategy@endlink) StrategyType
    ##   the active strategy type   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return LoadExtractionValue.ActiveStrategy
    @property
    def StrategyType(self) -> LoadExtractionValue.ActiveStrategy:
        """
        Getter for property: (@link LoadExtractionValue.ActiveStrategy NXOpen.CAE.AeroStructures.LoadExtractionValue.ActiveStrategy@endlink) StrategyType
          the active strategy type   
            
         
        """
        pass
    
    ## Setter for property: (@link LoadExtractionValue.ActiveStrategy NXOpen.CAE.AeroStructures.LoadExtractionValue.ActiveStrategy@endlink) StrategyType

    ##   the active strategy type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @StrategyType.setter
    def StrategyType(self, stratType: LoadExtractionValue.ActiveStrategy):
        """
        Setter for property: (@link LoadExtractionValue.ActiveStrategy NXOpen.CAE.AeroStructures.LoadExtractionValue.ActiveStrategy@endlink) StrategyType
          the active strategy type   
            
         
        """
        pass
    
import NXOpen
import NXOpen.Annotations
##  Represents a @link NXOpen::CAE::AeroStructures::LoadFilteringCalculation NXOpen::CAE::AeroStructures::LoadFilteringCalculation@endlink  builder.  <br> No support for KF  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class LoadFilteringCalculationBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.CAE.AeroStructures.LoadFilteringCalculation</ja_class> builder. """


    ## Getter for property: (@link NXOpen.Annotations.NoteBase NXOpen.Annotations.NoteBase@endlink) Annotation
    ##   the Annotation   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Annotations.NoteBase
    @property
    def Annotation(self) -> NXOpen.Annotations.NoteBase:
        """
        Getter for property: (@link NXOpen.Annotations.NoteBase NXOpen.Annotations.NoteBase@endlink) Annotation
          the Annotation   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Annotations.NoteBase NXOpen.Annotations.NoteBase@endlink) Annotation

    ##   the Annotation   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Annotation.setter
    def Annotation(self, annotation: NXOpen.Annotations.NoteBase):
        """
        Setter for property: (@link NXOpen.Annotations.NoteBase NXOpen.Annotations.NoteBase@endlink) Annotation
          the Annotation   
            
         
        """
        pass
    
    ## Getter for property: (str) Description
    ##   the description.  
    ##      
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
          the description.  
             
         
        """
        pass
    
    ## Setter for property: (str) Description

    ##   the description.  
    ##      
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
          the description.  
             
         
        """
        pass
    
    ## Getter for property: (@link ExtractionSourceSet NXOpen.CAE.AeroStructures.ExtractionSourceSet@endlink) ExtractionSourceSet
    ##   the Extraction sources   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return ExtractionSourceSet
    @property
    def ExtractionSourceSet(self) -> ExtractionSourceSet:
        """
        Getter for property: (@link ExtractionSourceSet NXOpen.CAE.AeroStructures.ExtractionSourceSet@endlink) ExtractionSourceSet
          the Extraction sources   
            
         
        """
        pass
    
    ## Getter for property: (@link LoadCaseSet NXOpen.CAE.AeroStructures.LoadCaseSet@endlink) LoadCaseSet
    ##   the LoadCaseSet used by the calculation  
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return LoadCaseSet
    @property
    def LoadCaseSet(self) -> LoadCaseSet:
        """
        Getter for property: (@link LoadCaseSet NXOpen.CAE.AeroStructures.LoadCaseSet@endlink) LoadCaseSet
          the LoadCaseSet used by the calculation  
            
         
        """
        pass
    
    ## Setter for property: (@link LoadCaseSet NXOpen.CAE.AeroStructures.LoadCaseSet@endlink) LoadCaseSet

    ##   the LoadCaseSet used by the calculation  
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @LoadCaseSet.setter
    def LoadCaseSet(self, lcset: LoadCaseSet):
        """
        Setter for property: (@link LoadCaseSet NXOpen.CAE.AeroStructures.LoadCaseSet@endlink) LoadCaseSet
          the LoadCaseSet used by the calculation  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) LocationCoordinateSystem
    ##   the calculation location with direction as a coordinate system.  
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.CoordinateSystem
    @property
    def LocationCoordinateSystem(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) LocationCoordinateSystem
          the calculation location with direction as a coordinate system.  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) LocationCoordinateSystem

    ##   the calculation location with direction as a coordinate system.  
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @LocationCoordinateSystem.setter
    def LocationCoordinateSystem(self, location: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) LocationCoordinateSystem
          the calculation location with direction as a coordinate system.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) LocationPoint
    ##   the calculation location as a single point.  
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def LocationPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) LocationPoint
          the calculation location as a single point.  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) LocationPoint

    ##   the calculation location as a single point.  
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @LocationPoint.setter
    def LocationPoint(self, location: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) LocationPoint
          the calculation location as a single point.  
            
         
        """
        pass
    
    ## Getter for property: (str) MethodKey
    ##   the MethodKey.  
    ##    (This text contains non-printable ASCII characters.)   
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def MethodKey(self) -> str:
        """
        Getter for property: (str) MethodKey
          the MethodKey.  
           (This text contains non-printable ASCII characters.)   
         
        """
        pass
    
    ## Setter for property: (str) MethodKey

    ##   the MethodKey.  
    ##    (This text contains non-printable ASCII characters.)   
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @MethodKey.setter
    def MethodKey(self, methodkey: str):
        """
        Setter for property: (str) MethodKey
          the MethodKey.  
           (This text contains non-printable ASCII characters.)   
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##   the name.  
    ##      
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
          the name.  
             
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##   the name.  
    ##      
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
          the name.  
             
         
        """
        pass
    
    ## Getter for property: (@link PropTable NXOpen.CAE.AeroStructures.PropTable@endlink) PropertyTable
    ##   the Property Table   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return PropTable
    @property
    def PropertyTable(self) -> PropTable:
        """
        Getter for property: (@link PropTable NXOpen.CAE.AeroStructures.PropTable@endlink) PropertyTable
          the Property Table   
            
         
        """
        pass
    
    ##  Clear annotation data (no annotation will be generated)
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def ClearAnnotationData(builder: LoadFilteringCalculationBuilder) -> None:
        """
         Clear annotation data (no annotation will be generated)
        """
        pass
    
    ##  Replace the current edited calculation by a copy 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def DuplicateCalculation(builder: LoadFilteringCalculationBuilder) -> None:
        """
         Replace the current edited calculation by a copy 
        """
        pass
    
    ##  Initialize calculation from a template file 
    ##  @return errors (List[str]):  list of errors .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="templateFile"> (str) </param>
    def InitFromTemplate(builder: LoadFilteringCalculationBuilder, templateFile: str) -> List[str]:
        """
         Initialize calculation from a template file 
         @return errors (List[str]):  list of errors .
        """
        pass
    
    ##  Initialize calculation from a template file 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2306.0.0.  InitFromTemplate  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="templateFile"> (str) </param>
    def InitializeFromTemplate(builder: LoadFilteringCalculationBuilder, templateFile: str) -> None:
        """
         Initialize calculation from a template file 
        """
        pass
    
    ##  Set annotation data 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="annotData"> (@link AeroStructuresAnnotDataS NXOpen.CAE.AeroStructures.AeroStructuresAnnotDataS@endlink) </param>
    def SetAnnotationData(builder: LoadFilteringCalculationBuilder, annotData: AeroStructuresAnnotDataS) -> None:
        """
         Set annotation data 
        """
        pass
    
import NXOpen
##  Represents a collection of  @link CAE::AeroStructures::LoadFilteringCalculation CAE::AeroStructures::LoadFilteringCalculation@endlink .  <br> Use @link NXOpen::CAE::AeroStructures::LoadFilteringCalculationCollection NXOpen::CAE::AeroStructures::LoadFilteringCalculationCollection@endlink  to get the instance of this class.  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class LoadFilteringCalculationCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of  <ja_class>CAE.AeroStructures.LoadFilteringCalculation</ja_class>. """


    ##  Makes a copy of the calculation and adds it to the solution, adjusting the given name if it is a duplicate 
    ##  @return clonedCalculation (@link LoadFilteringCalculation NXOpen.CAE.AeroStructures.LoadFilteringCalculation@endlink): The resulting cloned @link NXOpen::CAE::AeroStructures::LoadFilteringCalculation NXOpen::CAE::AeroStructures::LoadFilteringCalculation@endlink  .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Tentative name of the cloned LoadFilteringCalculation, will be changed if not unique  
    def CloneCalculation(solution: LoadFilteringCalculationCollection, name: str, sourceCalculation: LoadFilteringCalculation) -> LoadFilteringCalculation:
        """
         Makes a copy of the calculation and adds it to the solution, adjusting the given name if it is a duplicate 
         @return clonedCalculation (@link LoadFilteringCalculation NXOpen.CAE.AeroStructures.LoadFilteringCalculation@endlink): The resulting cloned @link NXOpen::CAE::AeroStructures::LoadFilteringCalculation NXOpen::CAE::AeroStructures::LoadFilteringCalculation@endlink  .
        """
        pass
    
    ##  Clones calculations in bulk.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## List of calculations to clone 
    def CloneCalculations(solution: LoadFilteringCalculationCollection, calculations: List[LoadFilteringCalculation]) -> None:
        """
         Clones calculations in bulk.
        """
        pass
    
    ##  Create annotations in bulk 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="calculations"> (@link LoadFilteringCalculation List[NXOpen.CAE.AeroStructures.LoadFilteringCalculation]@endlink) </param>
    ## <param name="annotData"> (@link AeroStructuresAnnotDataS NXOpen.CAE.AeroStructures.AeroStructuresAnnotDataS@endlink) </param>
    def CreateAnnotations(solution: LoadFilteringCalculationCollection, calculations: List[LoadFilteringCalculation], annotData: AeroStructuresAnnotDataS) -> None:
        """
         Create annotations in bulk 
        """
        pass
    
    ##  Creates a @link CAE::AeroStructures::LoadFilteringCalculationBuilder CAE::AeroStructures::LoadFilteringCalculationBuilder@endlink  
    ##  @return builder (@link LoadFilteringCalculationBuilder NXOpen.CAE.AeroStructures.LoadFilteringCalculationBuilder@endlink):  Builder object.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##   
    def CreateLoadFilteringCalculationBuilder(solution: LoadFilteringCalculationCollection, calculation: LoadFilteringCalculation) -> LoadFilteringCalculationBuilder:
        """
         Creates a @link CAE::AeroStructures::LoadFilteringCalculationBuilder CAE::AeroStructures::LoadFilteringCalculationBuilder@endlink  
         @return builder (@link LoadFilteringCalculationBuilder NXOpen.CAE.AeroStructures.LoadFilteringCalculationBuilder@endlink):  Builder object.
        """
        pass
    
    ##  Creates a @link CAE::AeroStructures::LoadFilteringCalculationBuilder CAE::AeroStructures::LoadFilteringCalculationBuilder@endlink  for duplication
    ##  @return builder (@link LoadFilteringCalculationBuilder NXOpen.CAE.AeroStructures.LoadFilteringCalculationBuilder@endlink):  Builder object.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##   the calculation to duplicate 
    def CreateLoadFilteringCalculationBuilderForDuplication(solution: LoadFilteringCalculationCollection, calculation: LoadFilteringCalculation) -> LoadFilteringCalculationBuilder:
        """
         Creates a @link CAE::AeroStructures::LoadFilteringCalculationBuilder CAE::AeroStructures::LoadFilteringCalculationBuilder@endlink  for duplication
         @return builder (@link LoadFilteringCalculationBuilder NXOpen.CAE.AeroStructures.LoadFilteringCalculationBuilder@endlink):  Builder object.
        """
        pass
    
    ##  Removes the calculation from the solution 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  @link NXOpen::CAE::AeroStructures::LoadFilteringCalculation NXOpen::CAE::AeroStructures::LoadFilteringCalculation@endlink  to be deleted 
    def DeleteCalculation(solution: LoadFilteringCalculationCollection, calculation: LoadFilteringCalculation) -> None:
        """
         Removes the calculation from the solution 
        """
        pass
    
    ##  Deletes calculations in bulk.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## List of calculations to delete 
    def DeleteCalculations(solution: LoadFilteringCalculationCollection, calculations: List[LoadFilteringCalculation]) -> None:
        """
         Deletes calculations in bulk.
        """
        pass
    
    ##  Finds the @link NXOpen::CAE::AeroStructures::LoadFilteringCalculation NXOpen::CAE::AeroStructures::LoadFilteringCalculation@endlink  object with the given name. 
    ##  @return calculation (@link LoadFilteringCalculation NXOpen.CAE.AeroStructures.LoadFilteringCalculation@endlink):  @link NXOpen::CAE::AeroStructures::LoadFilteringCalculation NXOpen::CAE::AeroStructures::LoadFilteringCalculation@endlink  object with this name. .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Name of the LoadFilteringCalculation  
    def FindObject(solution: LoadFilteringCalculationCollection, name: str) -> LoadFilteringCalculation:
        """
         Finds the @link NXOpen::CAE::AeroStructures::LoadFilteringCalculation NXOpen::CAE::AeroStructures::LoadFilteringCalculation@endlink  object with the given name. 
         @return calculation (@link LoadFilteringCalculation NXOpen.CAE.AeroStructures.LoadFilteringCalculation@endlink):  @link NXOpen::CAE::AeroStructures::LoadFilteringCalculation NXOpen::CAE::AeroStructures::LoadFilteringCalculation@endlink  object with this name. .
        """
        pass
    
    ##  Renames calculations in bulk.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Base name of the calculations, will be suffixed by index if not unique  
    def RenameCalculations(solution: LoadFilteringCalculationCollection, name: str, calculations: List[LoadFilteringCalculation]) -> None:
        """
         Renames calculations in bulk.
        """
        pass
    
import NXOpen
##   @brief  This is the LoadFilteringCalculation  
## 
##   
## 
##   <br>  Created in NX1926.0.0  <br> 

class LoadFilteringCalculation(BaseCalculation): 
    """ <summary> This is the LoadFilteringCalculation </summary> """


    ##  Get the list of selected load case names in the last computed result 
    ##  @return loadCaseNames (List[str]): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetResultSelectedLoadCaseNames(context: LoadFilteringCalculation) -> List[str]:
        """
         Get the list of selected load case names in the last computed result 
         @return loadCaseNames (List[str]): .
        """
        pass
    
    ##  Get the expression of a scalar field input parameter 
    ##  @return exp (@link NXOpen.Expression NXOpen.Expression@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="inputName"> (str) </param>
    def GetScalarFieldExpression(context: LoadFilteringCalculation, inputName: str) -> NXOpen.Expression:
        """
         Get the expression of a scalar field input parameter 
         @return exp (@link NXOpen.Expression NXOpen.Expression@endlink): .
        """
        pass
    
    ##  Replace the expression of a scalar field input parameter
    ##                 and removes old expression from the expression manager. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="inputName"> (str) </param>
    ## <param name="exp"> (@link NXOpen.Expression NXOpen.Expression@endlink) </param>
    def ReplaceScalarFieldExpression(context: LoadFilteringCalculation, inputName: str, exp: NXOpen.Expression) -> None:
        """
         Replace the expression of a scalar field input parameter
                        and removes old expression from the expression manager. 
        """
        pass
    
import NXOpen
import NXOpen.CAE
##  This is a manager to the @link CAE::AeroStructures::LoadFilteringSolution CAE::AeroStructures::LoadFilteringSolution@endlink  class.
##     Object of type @link CAE::AeroStructures::LoadFilteringSolution CAE::AeroStructures::LoadFilteringSolution@endlink  can be
##     created and edited only through this class
##      <br> To create a new instance of this class, use @link NXOpen::CAE::AeroStructures::LoadFilteringSolutionCollection::CreateLoadFilteringSolutionBuilder  NXOpen::CAE::AeroStructures::LoadFilteringSolutionCollection::CreateLoadFilteringSolutionBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class LoadFilteringSolutionBuilder(NXOpen.Builder): 
    """ This is a manager to the <ja_class>CAE.AeroStructures.LoadFilteringSolution</ja_class> class.
    Object of type <ja_class>CAE.AeroStructures.LoadFilteringSolution</ja_class> can be
    created and edited only through this class
    """


    ## Getter for property: (str) Description
    ##    a Get the metasolution description  
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
           a Get the metasolution description  
            
         
        """
        pass
    
    ## Setter for property: (str) Description

    ##    a Get the metasolution description  
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Description.setter
    def Description(self, title: str):
        """
        Setter for property: (str) Description
           a Get the metasolution description  
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##   the metasolution name  
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
          the metasolution name  
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##   the metasolution name  
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Name.setter
    def Name(self, title: str):
        """
        Setter for property: (str) Name
          the metasolution name  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.SimSolution NXOpen.CAE.SimSolution@endlink) ReferenceSolution
    ##   the referenced FE-Solution of the AeroStructure solution   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.CAE.SimSolution
    @property
    def ReferenceSolution(self) -> NXOpen.CAE.SimSolution:
        """
        Getter for property: (@link NXOpen.CAE.SimSolution NXOpen.CAE.SimSolution@endlink) ReferenceSolution
          the referenced FE-Solution of the AeroStructure solution   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.SimSolution NXOpen.CAE.SimSolution@endlink) ReferenceSolution

    ##   the referenced FE-Solution of the AeroStructure solution   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ReferenceSolution.setter
    def ReferenceSolution(self, referenceSolution: NXOpen.CAE.SimSolution):
        """
        Setter for property: (@link NXOpen.CAE.SimSolution NXOpen.CAE.SimSolution@endlink) ReferenceSolution
          the referenced FE-Solution of the AeroStructure solution   
            
         
        """
        pass
    
    ## Getter for property: (str) UnitSystem
    ##   the unit system of the load filtering solution  
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def UnitSystem(self) -> str:
        """
        Getter for property: (str) UnitSystem
          the unit system of the load filtering solution  
            
         
        """
        pass
    
    ## Setter for property: (str) UnitSystem

    ##   the unit system of the load filtering solution  
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @UnitSystem.setter
    def UnitSystem(self, unit_system: str):
        """
        Setter for property: (str) UnitSystem
          the unit system of the load filtering solution  
            
         
        """
        pass
    
import NXOpen
##  Represents a collection of load filtering solution.  <br> To obtain an instance of this class, refer to @link NXOpen::CAE::AeroStructManager  NXOpen::CAE::AeroStructManager @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class LoadFilteringSolutionCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of load filtering solution. """


    ##  Clones a AeroStruct load filtering solution. 
    ##  @return copy (@link LoadFilteringSolution NXOpen.CAE.AeroStructures.LoadFilteringSolution@endlink):  Cloned load filtering solution .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Source load filtering solution 
    def CloneSolution(sim: LoadFilteringSolutionCollection, source: LoadFilteringSolution) -> LoadFilteringSolution:
        """
         Clones a AeroStruct load filtering solution. 
         @return copy (@link LoadFilteringSolution NXOpen.CAE.AeroStructures.LoadFilteringSolution@endlink):  Cloned load filtering solution .
        """
        pass
    
    ##  Creates the builder object of AeroStruct load filtering solution. 
    ##  @return builder (@link LoadFilteringSolutionBuilder NXOpen.CAE.AeroStructures.LoadFilteringSolutionBuilder@endlink):   .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##   
    def CreateLoadFilteringSolutionBuilder(sim: LoadFilteringSolutionCollection, loadFilteringSol: LoadFilteringSolution) -> LoadFilteringSolutionBuilder:
        """
         Creates the builder object of AeroStruct load filtering solution. 
         @return builder (@link LoadFilteringSolutionBuilder NXOpen.CAE.AeroStructures.LoadFilteringSolutionBuilder@endlink):   .
        """
        pass
    
    ##  Delete a AeroStruct load filtering solution. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  The AeroStruct load filtering solution to be deleted 
    def DeleteSolution(sim: LoadFilteringSolutionCollection, metasolution: LoadFilteringSolution) -> None:
        """
         Delete a AeroStruct load filtering solution. 
        """
        pass
    
    ##  Finds a AeroStruct load filtering solution with a specified name. 
    ##  @return found (@link LoadFilteringSolution NXOpen.CAE.AeroStructures.LoadFilteringSolution@endlink):  The AeroStruct load filtering solution .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  name of the AeroStruct load filtering solution  
    def FindObject(sim: LoadFilteringSolutionCollection, name: str) -> LoadFilteringSolution:
        """
         Finds a AeroStruct load filtering solution with a specified name. 
         @return found (@link LoadFilteringSolution NXOpen.CAE.AeroStructures.LoadFilteringSolution@endlink):  The AeroStruct load filtering solution .
        """
        pass
    
    ##  Returns the load filtering calculation. 
    ##  @return activeCalculation (@link LoadFilteringCalculation NXOpen.CAE.AeroStructures.LoadFilteringCalculation@endlink):  The active Load Filtering calculation .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetActiveLoadfilteringcalculation(simulation: LoadFilteringSolutionCollection) -> LoadFilteringCalculation:
        """
         Returns the load filtering calculation. 
         @return activeCalculation (@link LoadFilteringCalculation NXOpen.CAE.AeroStructures.LoadFilteringCalculation@endlink):  The active Load Filtering calculation .
        """
        pass
    
    ##  Returns the active load filtering solution. 
    ##  @return activeSolution (@link LoadFilteringSolution NXOpen.CAE.AeroStructures.LoadFilteringSolution@endlink):  The active load filtering solution .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetActiveSolution(sim: LoadFilteringSolutionCollection) -> LoadFilteringSolution:
        """
         Returns the active load filtering solution. 
         @return activeSolution (@link LoadFilteringSolution NXOpen.CAE.AeroStructures.LoadFilteringSolution@endlink):  The active load filtering solution .
        """
        pass
    
    ##  Sets the active load filtering calculation. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  The Load Filtering calculation to activate
    def SetActiveLoadfilteringcalculation(simulation: LoadFilteringSolutionCollection, activeCalculation: LoadFilteringCalculation) -> None:
        """
         Sets the active load filtering calculation. 
        """
        pass
    
    ##  Activates the load filtering solution. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  The load filtering solution to activate
    def SetActiveSolution(sim: LoadFilteringSolutionCollection, source: LoadFilteringSolution) -> None:
        """
         Activates the load filtering solution. 
        """
        pass
    
import NXOpen.CAE
##  Represent a @link NXOpen::CAE::AeroStructures::LoadFilteringSolution NXOpen::CAE::AeroStructures::LoadFilteringSolution@endlink .  <br> To create or edit an instance of this class, use @link NXOpen::CAE::AeroStructures::LoadFilteringSolutionBuilder  NXOpen::CAE::AeroStructures::LoadFilteringSolutionBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class LoadFilteringSolution(BaseSolution): 
    """ Represent a <ja_class>NXOpen.CAE.AeroStructures.LoadFilteringSolution</ja_class>. """


    ##  Returns the @link NXOpen::CAE::AeroStructures::LoadFilteringCalculationCollection NXOpen::CAE::AeroStructures::LoadFilteringCalculationCollection@endlink  belonging to this 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @link LoadFilteringCalculationCollection NXOpen.CAE.AeroStructures.LoadFilteringCalculationCollection@endlink
    @property
    def LoadFilteringCalculationCollection() -> LoadFilteringCalculationCollection:
        """
         Returns the @link NXOpen::CAE::AeroStructures::LoadFilteringCalculationCollection NXOpen::CAE::AeroStructures::LoadFilteringCalculationCollection@endlink  belonging to this 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::CAE::AeroStructures::LocalLaminate NXOpen::CAE::AeroStructures::LocalLaminate@endlink  object.  <br> To obtain an instance of this class use CAE.AeroStructures.LaminateHelper  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LocalLaminate(Laminate): 
    """ Represents a <ja_class>NXOpen.CAE.AeroStructures.LocalLaminate</ja_class> object. """


    ##  Add a ply to the laminate. Always added to the end of the original
    ##             stack. 
    ##  @return plyIndex (int): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Unit for the thickness value, if NULL use default 
    def AddPly(param: LocalLaminate, material: NXOpen.PhysicalMaterial, thickness: float, thicknessUnit: NXOpen.Unit, angle: float, angleUnit: NXOpen.Unit) -> int:
        """
         Add a ply to the laminate. Always added to the end of the original
                    stack. 
         @return plyIndex (int): .
        """
        pass
    
    ##  Add a ply to the laminate using a material name. Always added to
    ##             the end of the original stack. 
    ##  @return plyIndex (int): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Unit for the thickness value, if NULL use default 
    def AddPlyByMaterialName(param: LocalLaminate, materialName: str, thickness: float, thicknessUnit: NXOpen.Unit, angle: float, angleUnit: NXOpen.Unit) -> int:
        """
         Add a ply to the laminate using a material name. Always added to
                    the end of the original stack. 
         @return plyIndex (int): .
        """
        pass
    
    ##  Frees the object from memory.  After this method is called, it is
    ##             illegal to use the object. In .NET, this method is automatically
    ##             called when the object is deleted by the garbage collector. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(param: LocalLaminate) -> None:
        """
         Frees the object from memory.  After this method is called, it is
                    illegal to use the object. In .NET, this method is automatically
                    called when the object is deleted by the garbage collector. 
        """
        pass
    
    ##  Set bottom fiber distance 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Unit for the distance value, if NULL use default 
    def SetBottomFiberDistance(param: LocalLaminate, distance: float, distanceUnit: NXOpen.Unit) -> None:
        """
         Set bottom fiber distance 
        """
        pass
    
    ##  Invert ply angles 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="inverted"> (bool) </param>
    def SetInverted(param: LocalLaminate, inverted: bool) -> None:
        """
         Invert ply angles 
        """
        pass
    
    ##  Set laminate angle 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Unit for the angle value, if NULL use default 
    def SetLaminateAngle(param: LocalLaminate, angle: float, angleUnit: NXOpen.Unit) -> None:
        """
         Set laminate angle 
        """
        pass
    
    ##  Set the angle for the ply 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Unit for the angle value, if NULL use default 
    def SetPlyAngle(param: LocalLaminate, plyIndex: int, angle: float, angleUnit: NXOpen.Unit) -> None:
        """
         Set the angle for the ply 
        """
        pass
    
    ##  Set the Physical Material for the ply 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="plyIndex"> (int) </param>
    ## <param name="material"> (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) </param>
    def SetPlyMaterial(param: LocalLaminate, plyIndex: int, material: NXOpen.PhysicalMaterial) -> None:
        """
         Set the Physical Material for the ply 
        """
        pass
    
    ##  Set the Material for the ply by name 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="plyIndex"> (int) </param>
    ## <param name="materialName"> (str) </param>
    def SetPlyMaterialByName(param: LocalLaminate, plyIndex: int, materialName: str) -> None:
        """
         Set the Material for the ply by name 
        """
        pass
    
    ##  Set the thickness for the ply 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Unit for the thickness value, if NULL use default 
    def SetPlyThickness(param: LocalLaminate, plyIndex: int, thickness: float, thicknessUnit: NXOpen.Unit) -> None:
        """
         Set the thickness for the ply 
        """
        pass
    
    ##  Top|Middle|Bottom|Specify 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="location"> (@link Laminate.LamRefLoc NXOpen.CAE.AeroStructures.Laminate.LamRefLoc@endlink) </param>
    def SetReferencePlane(param: LocalLaminate, location: Laminate.LamRefLoc) -> None:
        """
         Top|Middle|Bottom|Specify 
        """
        pass
    
    ##  Set reference temperature 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Unit for the temperature value, if NULL use default 
    def SetReferenceTemperature(param: LocalLaminate, temperature: float, temperatureUnit: NXOpen.Unit) -> None:
        """
         Set reference temperature 
        """
        pass
    
    ##  Reverse ply order 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="reversed"> (bool) </param>
    def SetReversed(param: LocalLaminate, reversed: bool) -> None:
        """
         Reverse ply order 
        """
        pass
    
import NXOpen
##   @brief  This is the Manual LoadExtraction class  
## 
##   
## 
##   <br>  Created in NX12.0.0  <br> 

class ManualLoadExtraction(LoadExtractionStrategy): 
    """ <summary> This is the Manual LoadExtraction class </summary> """


    ##  Get values in given units 
    ##  @return A tuple consisting of (keys, values). 
    ##  - keys is: List[str]. list of keys (loadcase names) .
    ##  - values is: List[float]. list of values .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  unit in which values are expected. 
    @staticmethod
    def GetValues(loadExt: ManualLoadExtraction, unit: NXOpen.Unit) -> Tuple[List[str], List[float]]:
        """
         Get values in given units 
         @return A tuple consisting of (keys, values). 
         - keys is: List[str]. list of keys (loadcase names) .
         - values is: List[float]. list of values .

        """
        pass
    
    ##  Set values in given units 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  unit in which values are specified. 
    def SetValues(loadExt: ManualLoadExtraction, unit: NXOpen.Unit, keys: List[str], values: List[float]) -> None:
        """
         Set values in given units 
        """
        pass
    
import NXOpen.CAE
##  Represents a Margin annotation builder class  <br> To create a new instance of this class, use @link NXOpen::CAE::AeroStructures::MarginAnnotCollection::CreateMarginAnnotBuilder  NXOpen::CAE::AeroStructures::MarginAnnotCollection::CreateMarginAnnotBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class MarginAnnotBuilder(NXOpen.CAE.CaeNoteBuilder): 
    """ Represents a Margin annotation builder class """
    pass


import NXOpen
import NXOpen.Annotations
##  Represents a collection of Margin annotation  <br> To obtain an instance of this class, refer to @link NXOpen::CAE::CaePart  NXOpen::CAE::CaePart @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class MarginAnnotCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Margin annotation """


    ##  Creates a Margin Annotation 
    ##  @return annotation (@link MarginAnnot NXOpen.CAE.AeroStructures.MarginAnnot@endlink):  New Margin annotation .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Annotation data 
    def CreateMarginAnnot(part: MarginAnnotCollection, label_data: NXOpen.Annotations.LabelData) -> MarginAnnot:
        """
         Creates a Margin Annotation 
         @return annotation (@link MarginAnnot NXOpen.CAE.AeroStructures.MarginAnnot@endlink):  New Margin annotation .
        """
        pass
    
    ##  Creates a builder for Margin annotation 
    ##  @return builder (@link MarginAnnotBuilder NXOpen.CAE.AeroStructures.MarginAnnotBuilder@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  @link NXOpen::Annotations::SimpleDraftingAid NXOpen::Annotations::SimpleDraftingAid@endlink  to be edited 
    def CreateMarginAnnotBuilder(part: MarginAnnotCollection, annotation: NXOpen.Annotations.SimpleDraftingAid) -> MarginAnnotBuilder:
        """
         Creates a builder for Margin annotation 
         @return builder (@link MarginAnnotBuilder NXOpen.CAE.AeroStructures.MarginAnnotBuilder@endlink): .
        """
        pass
    
    ##  Finds a margin annotation with a specified name. 
    ##  @return found (@link MarginAnnot NXOpen.CAE.AeroStructures.MarginAnnot@endlink):  The margin annot .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  name of the margin annot 
    def FindObject(sim: MarginAnnotCollection, name: str) -> MarginAnnot:
        """
         Finds a margin annotation with a specified name. 
         @return found (@link MarginAnnot NXOpen.CAE.AeroStructures.MarginAnnot@endlink):  The margin annot .
        """
        pass
    
    ##  Hide Annotation 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="annot_array"> (@link MarginAnnot List[NXOpen.CAE.AeroStructures.MarginAnnot]@endlink) </param>
    def HideAnnotations(part: MarginAnnotCollection, annot_array: List[MarginAnnot]) -> None:
        """
         Hide Annotation 
        """
        pass
    
    ##  Relocate Margin annotations in bulk 
    ##  @return relocated (bool):  returns true if the annotation(s) is truly relocated  .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="annot_array"> (@link MarginAnnot List[NXOpen.CAE.AeroStructures.MarginAnnot]@endlink) </param>
    def RelocateAnnotations(part: MarginAnnotCollection, annot_array: List[MarginAnnot]) -> bool:
        """
         Relocate Margin annotations in bulk 
         @return relocated (bool):  returns true if the annotation(s) is truly relocated  .
        """
        pass
    
    ##  Reverse Margin annotation leaders 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="annot_array"> (@link MarginAnnot List[NXOpen.CAE.AeroStructures.MarginAnnot]@endlink) </param>
    def ReverseLeaders(part: MarginAnnotCollection, annot_array: List[MarginAnnot]) -> None:
        """
         Reverse Margin annotation leaders 
        """
        pass
    
    ##  Scale Margin annotation text size 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  non-negative scale value 
    def ScaleTextSize(part: MarginAnnotCollection, annot_array: List[MarginAnnot], scale: float) -> None:
        """
         Scale Margin annotation text size 
        """
        pass
    
    ##  Show Annotation 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="annot_array"> (@link MarginAnnot List[NXOpen.CAE.AeroStructures.MarginAnnot]@endlink) </param>
    def ShowAnnotations(part: MarginAnnotCollection, annot_array: List[MarginAnnot]) -> None:
        """
         Show Annotation 
        """
        pass
    
    ##  Update Margin annotations preference 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="annot_array"> (@link MarginAnnot List[NXOpen.CAE.AeroStructures.MarginAnnot]@endlink) </param>
    ## <param name="annotData"> (@link AeroStructuresAnnotDataS NXOpen.CAE.AeroStructures.AeroStructuresAnnotDataS@endlink) </param>
    def UpdateAnnotations(part: MarginAnnotCollection, annot_array: List[MarginAnnot], annotData: AeroStructuresAnnotDataS) -> None:
        """
         Update Margin annotations preference 
        """
        pass
    
import NXOpen.CAE
##  Represents an object that manages annotation for CAE  <br> To obtain an instance of this object use on of the creator in @link NXOpen::CAE::AeroStructures::MarginAnnotCollection NXOpen::CAE::AeroStructures::MarginAnnotCollection@endlink .  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class MarginAnnot(NXOpen.CAE.CaeLabel): 
    """ Represents an object that manages annotation for CAE """
    pass


import NXOpen
import NXOpen.Annotations
##  Represents a @link NXOpen::CAE::AeroStructures::MarginCalculation NXOpen::CAE::AeroStructures::MarginCalculation@endlink  builder.  <br> No support for KF  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class MarginCalculationBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.CAE.AeroStructures.MarginCalculation</ja_class> builder. """


    ## Getter for property: (@link NXOpen.Annotations.NoteBase NXOpen.Annotations.NoteBase@endlink) Annotation
    ##   the Annotation   
    ##     
    ##  
    ## Getter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Annotations.NoteBase
    @property
    def Annotation(self) -> NXOpen.Annotations.NoteBase:
        """
        Getter for property: (@link NXOpen.Annotations.NoteBase NXOpen.Annotations.NoteBase@endlink) Annotation
          the Annotation   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Annotations.NoteBase NXOpen.Annotations.NoteBase@endlink) Annotation

    ##   the Annotation   
    ##     
    ##  
    ## Setter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Annotation.setter
    def Annotation(self, annotation: NXOpen.Annotations.NoteBase):
        """
        Setter for property: (@link NXOpen.Annotations.NoteBase NXOpen.Annotations.NoteBase@endlink) Annotation
          the Annotation   
            
         
        """
        pass
    
    ## Getter for property: (str) Description
    ##   the description.  
    ##      
    ##  
    ## Getter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
          the description.  
             
         
        """
        pass
    
    ## Setter for property: (str) Description

    ##   the description.  
    ##      
    ##  
    ## Setter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
          the description.  
             
         
        """
        pass
    
    ## Getter for property: (@link ExtractionSourceSet NXOpen.CAE.AeroStructures.ExtractionSourceSet@endlink) ExtractionSourceSet
    ##   the Extraction sources   
    ##     
    ##  
    ## Getter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return ExtractionSourceSet
    @property
    def ExtractionSourceSet(self) -> ExtractionSourceSet:
        """
        Getter for property: (@link ExtractionSourceSet NXOpen.CAE.AeroStructures.ExtractionSourceSet@endlink) ExtractionSourceSet
          the Extraction sources   
            
         
        """
        pass
    
    ## Getter for property: (@link LoadCaseSet NXOpen.CAE.AeroStructures.LoadCaseSet@endlink) LoadCaseSet
    ##   the LoadCaseSet used by the calculation  
    ##     
    ##  
    ## Getter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return LoadCaseSet
    @property
    def LoadCaseSet(self) -> LoadCaseSet:
        """
        Getter for property: (@link LoadCaseSet NXOpen.CAE.AeroStructures.LoadCaseSet@endlink) LoadCaseSet
          the LoadCaseSet used by the calculation  
            
         
        """
        pass
    
    ## Setter for property: (@link LoadCaseSet NXOpen.CAE.AeroStructures.LoadCaseSet@endlink) LoadCaseSet

    ##   the LoadCaseSet used by the calculation  
    ##     
    ##  
    ## Setter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @LoadCaseSet.setter
    def LoadCaseSet(self, lcset: LoadCaseSet):
        """
        Setter for property: (@link LoadCaseSet NXOpen.CAE.AeroStructures.LoadCaseSet@endlink) LoadCaseSet
          the LoadCaseSet used by the calculation  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) LocationCoordinateSystem
    ##   the calculation location with direction as a coordinate system.  
    ##     
    ##  
    ## Getter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.CoordinateSystem
    @property
    def LocationCoordinateSystem(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) LocationCoordinateSystem
          the calculation location with direction as a coordinate system.  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) LocationCoordinateSystem

    ##   the calculation location with direction as a coordinate system.  
    ##     
    ##  
    ## Setter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @LocationCoordinateSystem.setter
    def LocationCoordinateSystem(self, location: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) LocationCoordinateSystem
          the calculation location with direction as a coordinate system.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) LocationPoint
    ##   the calculation location as a single point.  
    ##     
    ##  
    ## Getter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def LocationPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) LocationPoint
          the calculation location as a single point.  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) LocationPoint

    ##   the calculation location as a single point.  
    ##     
    ##  
    ## Setter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @LocationPoint.setter
    def LocationPoint(self, location: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) LocationPoint
          the calculation location as a single point.  
            
         
        """
        pass
    
    ## Getter for property: (str) MethodKey
    ##   the MethodKey.  
    ##    (This text contains non-printable ASCII characters.)   
    ##  
    ## Getter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def MethodKey(self) -> str:
        """
        Getter for property: (str) MethodKey
          the MethodKey.  
           (This text contains non-printable ASCII characters.)   
         
        """
        pass
    
    ## Setter for property: (str) MethodKey

    ##   the MethodKey.  
    ##    (This text contains non-printable ASCII characters.)   
    ##  
    ## Setter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @MethodKey.setter
    def MethodKey(self, methodkey: str):
        """
        Setter for property: (str) MethodKey
          the MethodKey.  
           (This text contains non-printable ASCII characters.)   
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##   the name.  
    ##      
    ##  
    ## Getter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
          the name.  
             
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##   the name.  
    ##      
    ##  
    ## Setter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
          the name.  
             
         
        """
        pass
    
    ## Getter for property: (@link PropTable NXOpen.CAE.AeroStructures.PropTable@endlink) PropertyTable
    ##   the Property Table   
    ##     
    ##  
    ## Getter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return PropTable
    @property
    def PropertyTable(self) -> PropTable:
        """
        Getter for property: (@link PropTable NXOpen.CAE.AeroStructures.PropTable@endlink) PropertyTable
          the Property Table   
            
         
        """
        pass
    
    ##  Clear annotation data (no annotation will be generated)
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    @staticmethod
    def ClearAnnotationData(builder: MarginCalculationBuilder) -> None:
        """
         Clear annotation data (no annotation will be generated)
        """
        pass
    
    ##  Creates a PropertyTable 
    ##  @return propertytable (@link PropTable NXOpen.CAE.AeroStructures.PropTable@endlink):  the property table.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    def CreatePropertyTable(builder: MarginCalculationBuilder) -> PropTable:
        """
         Creates a PropertyTable 
         @return propertytable (@link PropTable NXOpen.CAE.AeroStructures.PropTable@endlink):  the property table.
        """
        pass
    
    ##  Replace the current edited calculation by a copy 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    @staticmethod
    def DuplicateCalculation(builder: MarginCalculationBuilder) -> None:
        """
         Replace the current edited calculation by a copy 
        """
        pass
    
    ##  Initialize calculation from a template file 
    ##  @return errors (List[str]):  list of errors .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ## <param name="templateFile"> (str) </param>
    def InitFromTemplate(builder: MarginCalculationBuilder, templateFile: str) -> List[str]:
        """
         Initialize calculation from a template file 
         @return errors (List[str]):  list of errors .
        """
        pass
    
    ##  Initialize calculation from a template file 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2306.0.0.  InitFromTemplate  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ## <param name="templateFile"> (str) </param>
    def InitializeFromTemplate(builder: MarginCalculationBuilder, templateFile: str) -> None:
        """
         Initialize calculation from a template file 
        """
        pass
    
    ##  Set annotation data 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ## <param name="annotData"> (@link AeroStructuresAnnotDataS NXOpen.CAE.AeroStructures.AeroStructuresAnnotDataS@endlink) </param>
    def SetAnnotationData(builder: MarginCalculationBuilder, annotData: AeroStructuresAnnotDataS) -> None:
        """
         Set annotation data 
        """
        pass
    
import NXOpen
##  Represents a collection of  @link CAE::AeroStructures::MarginCalculation CAE::AeroStructures::MarginCalculation@endlink .  <br> Use @link NXOpen::CAE::AeroStructures::MarginCalculationCollection NXOpen::CAE::AeroStructures::MarginCalculationCollection@endlink  to get the instance of this class.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class MarginCalculationCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of  <ja_class>CAE.AeroStructures.MarginCalculation</ja_class>. """


    ##  Makes a copy of the calculation and adds it to the margin solution, adjusting the given name if it is a duplicate 
    ##  @return clonedmargincalculation (@link MarginCalculation NXOpen.CAE.AeroStructures.MarginCalculation@endlink): The resulting cloned @link NXOpen::CAE::AeroStructures::MarginCalculation NXOpen::CAE::AeroStructures::MarginCalculation@endlink  .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  Tentative name of the cloned MarginCalculation, will be changed if not unique  
    def CloneCalculation(solution: MarginCalculationCollection, name: str, sourcemargincalculation: MarginCalculation) -> MarginCalculation:
        """
         Makes a copy of the calculation and adds it to the margin solution, adjusting the given name if it is a duplicate 
         @return clonedmargincalculation (@link MarginCalculation NXOpen.CAE.AeroStructures.MarginCalculation@endlink): The resulting cloned @link NXOpen::CAE::AeroStructures::MarginCalculation NXOpen::CAE::AeroStructures::MarginCalculation@endlink  .
        """
        pass
    
    ##  Clones calculations in bulk.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## List of calculations to clone 
    def CloneCalculations(solution: MarginCalculationCollection, calculations: List[MarginCalculation]) -> None:
        """
         Clones calculations in bulk.
        """
        pass
    
    ##  Create annotations in bulk 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ## <param name="marginCalculations"> (@link MarginCalculation List[NXOpen.CAE.AeroStructures.MarginCalculation]@endlink) </param>
    ## <param name="annotData"> (@link AeroStructuresAnnotDataS NXOpen.CAE.AeroStructures.AeroStructuresAnnotDataS@endlink) </param>
    def CreateAnnotations(solution: MarginCalculationCollection, marginCalculations: List[MarginCalculation], annotData: AeroStructuresAnnotDataS) -> None:
        """
         Create annotations in bulk 
        """
        pass
    
    ##  Creates a @link CAE::AeroStructures::MarginCalculationBuilder CAE::AeroStructures::MarginCalculationBuilder@endlink  
    ##  @return builder (@link MarginCalculationBuilder NXOpen.CAE.AeroStructures.MarginCalculationBuilder@endlink):  Builder object.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##   
    def CreateMarginCalculationBuilder(solution: MarginCalculationCollection, margincalculation: MarginCalculation) -> MarginCalculationBuilder:
        """
         Creates a @link CAE::AeroStructures::MarginCalculationBuilder CAE::AeroStructures::MarginCalculationBuilder@endlink  
         @return builder (@link MarginCalculationBuilder NXOpen.CAE.AeroStructures.MarginCalculationBuilder@endlink):  Builder object.
        """
        pass
    
    ##  Creates a @link CAE::AeroStructures::MarginCalculationBuilder CAE::AeroStructures::MarginCalculationBuilder@endlink  for duplication
    ##  @return builder (@link MarginCalculationBuilder NXOpen.CAE.AeroStructures.MarginCalculationBuilder@endlink):  Builder object.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##   the calculation to duplicate 
    def CreateMarginCalculationBuilderForDuplication(solution: MarginCalculationCollection, margincalculation: MarginCalculation) -> MarginCalculationBuilder:
        """
         Creates a @link CAE::AeroStructures::MarginCalculationBuilder CAE::AeroStructures::MarginCalculationBuilder@endlink  for duplication
         @return builder (@link MarginCalculationBuilder NXOpen.CAE.AeroStructures.MarginCalculationBuilder@endlink):  Builder object.
        """
        pass
    
    ##  Creates a @link CAE::AeroStructures::MultiMarginCalculationBuilder CAE::AeroStructures::MultiMarginCalculationBuilder@endlink  
    ##  @return builder (@link MultiMarginCalculationBuilder NXOpen.CAE.AeroStructures.MultiMarginCalculationBuilder@endlink):  Builder object.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##   
    def CreateMultiMarginCalculationBuilder(solution: MarginCalculationCollection, margincalculation: MarginCalculation) -> MultiMarginCalculationBuilder:
        """
         Creates a @link CAE::AeroStructures::MultiMarginCalculationBuilder CAE::AeroStructures::MultiMarginCalculationBuilder@endlink  
         @return builder (@link MultiMarginCalculationBuilder NXOpen.CAE.AeroStructures.MultiMarginCalculationBuilder@endlink):  Builder object.
        """
        pass
    
    ##  Removes the calculation from the solution 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  @link NXOpen::CAE::AeroStructures::MarginCalculation NXOpen::CAE::AeroStructures::MarginCalculation@endlink  to be deleted 
    def DeleteCalculation(solution: MarginCalculationCollection, margincalculation: MarginCalculation) -> None:
        """
         Removes the calculation from the solution 
        """
        pass
    
    ##  Deletes calculations in bulk.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## List of calculations to delete 
    def DeleteCalculations(solution: MarginCalculationCollection, calculations: List[MarginCalculation]) -> None:
        """
         Deletes calculations in bulk.
        """
        pass
    
    ##  Finds the @link NXOpen::CAE::AeroStructures::MarginCalculation NXOpen::CAE::AeroStructures::MarginCalculation@endlink  object with the given name. 
    ##  @return found (@link MarginCalculation NXOpen.CAE.AeroStructures.MarginCalculation@endlink):  @link NXOpen::CAE::AeroStructures::MarginCalculation NXOpen::CAE::AeroStructures::MarginCalculation@endlink  object with this name. .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  Name of the MarginCalculation  
    def FindObject(marginsolution: MarginCalculationCollection, name: str) -> MarginCalculation:
        """
         Finds the @link NXOpen::CAE::AeroStructures::MarginCalculation NXOpen::CAE::AeroStructures::MarginCalculation@endlink  object with the given name. 
         @return found (@link MarginCalculation NXOpen.CAE.AeroStructures.MarginCalculation@endlink):  @link NXOpen::CAE::AeroStructures::MarginCalculation NXOpen::CAE::AeroStructures::MarginCalculation@endlink  object with this name. .
        """
        pass
    
    ##  Renames calculations in bulk.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  Base name of the calculations, will be suffixed by index if not unique  
    def RenameCalculations(solution: MarginCalculationCollection, name: str, calculations: List[MarginCalculation]) -> None:
        """
         Renames calculations in bulk.
        """
        pass
    
import NXOpen
##   @brief  This is the MarginCalculation  
## 
##   
## 
##   <br>  Created in NX12.0.0  <br> 

class MarginCalculation(BaseCalculation): 
    """ <summary> This is the MarginCalculation </summary> """


    ##  Get an MS value in the last computed result 
    ##  @return value (float): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ## <param name="failureModeName"> (str) </param>
    ## <param name="loadCaseName"> (str) </param>
    def GetResultMsValue(context: MarginCalculation, failureModeName: str, loadCaseName: str) -> float:
        """
         Get an MS value in the last computed result 
         @return value (float): .
        """
        pass
    
    ##  Get the expression of a scalar field input parameter 
    ##  @return exp (@link NXOpen.Expression NXOpen.Expression@endlink): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ## <param name="inputName"> (str) </param>
    def GetScalarFieldExpression(context: MarginCalculation, inputName: str) -> NXOpen.Expression:
        """
         Get the expression of a scalar field input parameter 
         @return exp (@link NXOpen.Expression NXOpen.Expression@endlink): .
        """
        pass
    
    ##  Replace the expression of a scalar field input parameter
    ##                 and removes old expression from the expression manager. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ## <param name="inputName"> (str) </param>
    ## <param name="exp"> (@link NXOpen.Expression NXOpen.Expression@endlink) </param>
    def ReplaceScalarFieldExpression(context: MarginCalculation, inputName: str, exp: NXOpen.Expression) -> None:
        """
         Replace the expression of a scalar field input parameter
                        and removes old expression from the expression manager. 
        """
        pass
    
import NXOpen
##   @brief  Iterate over the solutions of a query.
##         Each solution is a @link CAE::AeroStructures::MarginResultTableRow CAE::AeroStructures::MarginResultTableRow@endlink .
##         @link CAE::AeroStructures::MarginResultIterator::Next CAE::AeroStructures::MarginResultIterator::Next@endlink  advances to the next row. 
##         @link CAE::AeroStructures::MarginResultIterator::GetCurrentRow CAE::AeroStructures::MarginResultIterator::GetCurrentRow@endlink  retreives the current row.
##          
## 
##   
## 
##   <br>  Created in NX12.0.0  <br> 

class MarginResultIterator(NXOpen.NXObject): 
    """ <summary> Iterate over the solutions of a query.
        Each solution is a <ja_class>CAE.AeroStructures.MarginResultTableRow</ja_class>.
        <ja_method>CAE.AeroStructures.MarginResultIterator.Next</ja_method> advances to the next row. 
        <ja_method>CAE.AeroStructures.MarginResultIterator.GetCurrentRow</ja_method> retreives the current row.
        </summary> """


    ##  Returns the current @link CAE::AeroStructures::MarginResultTableRow CAE::AeroStructures::MarginResultTableRow@endlink 
    ##  @return row (@link MarginResultTableRow NXOpen.CAE.AeroStructures.MarginResultTableRow@endlink):  the current @link CAE::AeroStructures::MarginResultTableRow CAE::AeroStructures::MarginResultTableRow@endlink  .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    @staticmethod
    def GetCurrentRow(context: MarginResultIterator) -> MarginResultTableRow:
        """
         Returns the current @link CAE::AeroStructures::MarginResultTableRow CAE::AeroStructures::MarginResultTableRow@endlink 
         @return row (@link MarginResultTableRow NXOpen.CAE.AeroStructures.MarginResultTableRow@endlink):  the current @link CAE::AeroStructures::MarginResultTableRow CAE::AeroStructures::MarginResultTableRow@endlink  .
        """
        pass
    
    ##  Increments the iterator to the next row. Returns false if the iterator was already positioned at the last row. 
    ##                 If successful, calling @link CAE::AeroStructures::MarginResultIterator::GetCurrentRow CAE::AeroStructures::MarginResultIterator::GetCurrentRow@endlink  will return the subsequent row.
    ##  @return success (bool): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    @staticmethod
    def Next(context: MarginResultIterator) -> bool:
        """
         Increments the iterator to the next row. Returns false if the iterator was already positioned at the last row. 
                        If successful, calling @link CAE::AeroStructures::MarginResultIterator::GetCurrentRow CAE::AeroStructures::MarginResultIterator::GetCurrentRow@endlink  will return the subsequent row.
         @return success (bool): .
        """
        pass
    
import NXOpen
##   @brief  @link CAE::AeroStructures::MarginResultQuery CAE::AeroStructures::MarginResultQuery@endlink  defines a query on all, or a subset, of the available margin results.
##                       Depending on the chosen constructor it is possible to pre-filter the results before the rank calculation takes place.
##                       It is also possible to specify a filter that acts after the rank calculation has taken place.
##                       Post filters offer more flexibility in terms of constraints than pre filters.
##                       An instance of this class can be created using the following methods:
##                       @link CAE::AeroStructures::MarginSolution::CreateMarginResultQuery CAE::AeroStructures::MarginSolution::CreateMarginResultQuery@endlink   or
##                       @link CAE::AeroStructures::MarginResultTableDataProvider::CreateQuery  CAE::AeroStructures::MarginResultTableDataProvider::CreateQuery @endlink 
##                   
##                       In order to use the query, request an iterator and use that to obtain one row at a time.
##          
## 
##    <br> To create a new instance of this class, use @link NXOpen::CAE::AeroStructures::MarginSolution::CreateMarginResultQuery  NXOpen::CAE::AeroStructures::MarginSolution::CreateMarginResultQuery @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class MarginResultQuery(NXOpen.NXObject): 
    """ <summary> <ja_class>CAE.AeroStructures.MarginResultQuery</ja_class> defines a query on all, or a subset, of the available margin results.
                      Depending on the chosen constructor it is possible to pre-filter the results before the rank calculation takes place.
                      It is also possible to specify a filter that acts after the rank calculation has taken place.
                      Post filters offer more flexibility in terms of constraints than pre filters.
                      An instance of this class can be created using the following methods:
                      <ja_method>CAE.AeroStructures.MarginSolution.CreateMarginResultQuery</ja_method>  or
                      <ja_method>CAE.AeroStructures.MarginResultTableDataProvider.CreateQuery </ja_method>
                  
                      In order to use the query, request an iterator and use that to obtain one row at a time.
        </summary> """


    ##  Creates a new iterator 
    ##  @return iterator (@link MarginResultIterator NXOpen.CAE.AeroStructures.MarginResultIterator@endlink):  output iterator .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    def CreateIterator(context: MarginResultQuery) -> MarginResultIterator:
        """
         Creates a new iterator 
         @return iterator (@link MarginResultIterator NXOpen.CAE.AeroStructures.MarginResultIterator@endlink):  output iterator .
        """
        pass
    
    ##  Get the maximum row count resulting from this query. 
    ##                 The actual count could be lower and can be retrieved by the method @link CAE::AeroStructures::MarginResultQuery::GetRowCount  CAE::AeroStructures::MarginResultQuery::GetRowCount @endlink  
    ##                 but this might require more time to compute if the query includes a filter
    ##  @return count (int): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    @staticmethod
    def GetMaximumRowCount(context: MarginResultQuery) -> int:
        """
         Get the maximum row count resulting from this query. 
                        The actual count could be lower and can be retrieved by the method @link CAE::AeroStructures::MarginResultQuery::GetRowCount  CAE::AeroStructures::MarginResultQuery::GetRowCount @endlink  
                        but this might require more time to compute if the query includes a filter
         @return count (int): .
        """
        pass
    
    ##  Get the row count resulting from this query. 
    ##                 If the query contains filtering this method takes more time than @link CAE::AeroStructures::MarginResultQuery::GetMaximumRowCount  CAE::AeroStructures::MarginResultQuery::GetMaximumRowCount @endlink  
    ##                 
    ##  @return count (int): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    @staticmethod
    def GetRowCount(context: MarginResultQuery) -> int:
        """
         Get the row count resulting from this query. 
                        If the query contains filtering this method takes more time than @link CAE::AeroStructures::MarginResultQuery::GetMaximumRowCount  CAE::AeroStructures::MarginResultQuery::GetMaximumRowCount @endlink  
                        
         @return count (int): .
        """
        pass
    
import NXOpen
##   @brief  @link CAE::AeroStructures::MarginResultTableDataProvider CAE::AeroStructures::MarginResultTableDataProvider@endlink  is used by the global results editor.
##                       It provides a table view of the results of a subset of the calculations in a margin solution.
##                       The columns can be configured using @link CAE::AeroStructures::MarginResultTableDataProvider::RegisterColumn CAE::AeroStructures::MarginResultTableDataProvider::RegisterColumn@endlink .
##                       @link CAE::AeroStructures::MarginResultTableDataProvider CAE::AeroStructures::MarginResultTableDataProvider@endlink  is also a data provider for @link CAE::AeroStructures::MarginResultQuery CAE::AeroStructures::MarginResultQuery@endlink  object.
##                       The method @link CAE::AeroStructures::MarginResultTableDataProvider::RegisterColumn CAE::AeroStructures::MarginResultTableDataProvider::RegisterColumn@endlink  creates a @link CAE::AeroStructures::MarginResultQuery CAE::AeroStructures::MarginResultQuery@endlink  that 
##                       represents the result data present in this table provider. 
##                         
## 
##    <br> To create a new instance of this class, use @link NXOpen::CAE::AeroStructures::MarginSolution::CreateMarginResultTableDataProvider  NXOpen::CAE::AeroStructures::MarginSolution::CreateMarginResultTableDataProvider @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class MarginResultTableDataProvider(NXOpen.NXObject): 
    """ <summary> <ja_class>CAE.AeroStructures.MarginResultTableDataProvider</ja_class> is used by the global results editor.
                      It provides a table view of the results of a subset of the calculations in a margin solution.
                      The columns can be configured using <ja_method>CAE.AeroStructures.MarginResultTableDataProvider.RegisterColumn</ja_method>.
                      <ja_class>CAE.AeroStructures.MarginResultTableDataProvider</ja_class> is also a data provider for <ja_class>CAE.AeroStructures.MarginResultQuery</ja_class> object.
                      The method <ja_method>CAE.AeroStructures.MarginResultTableDataProvider.RegisterColumn</ja_method> creates a <ja_class>CAE.AeroStructures.MarginResultQuery</ja_class> that 
                      represents the result data present in this table provider. 
                       </summary> """


    ##  The column type enumerates the available builtin column types that can be registered.
    ##                 The last one (sentinel) is not a real column type but is used internally as an end of enumeration marker
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Calculation</term><description> 
    ## </description> </item><item><term> 
    ## FailureMode</term><description> 
    ## </description> </item><item><term> 
    ## LoadCase</term><description> 
    ## </description> </item><item><term> 
    ## MarginOfSafety</term><description> 
    ## </description> </item><item><term> 
    ## GlobalRank</term><description> 
    ## </description> </item><item><term> 
    ## RankByCalculation</term><description> 
    ## </description> </item><item><term> 
    ## RankByFailureMode</term><description> 
    ## </description> </item><item><term> 
    ## RankByLoadCase</term><description> 
    ## </description> </item><item><term> 
    ## Method</term><description> 
    ## </description> </item><item><term> 
    ## FemSolution</term><description> 
    ## </description> </item><item><term> 
    ## SelectedLoadCaseCount</term><description> 
    ## </description> </item><item><term> 
    ## LoadCaseCount</term><description> 
    ## </description> </item><item><term> 
    ## LoadCaseSet</term><description> 
    ## </description> </item><item><term> 
    ## ReserveFactor</term><description> 
    ## </description> </item><item><term> 
    ## Sentinel</term><description> 
    ## </description> </item></list>
    class ColumnType(Enum):
        """
        Members Include: <Calculation> <FailureMode> <LoadCase> <MarginOfSafety> <GlobalRank> <RankByCalculation> <RankByFailureMode> <RankByLoadCase> <Method> <FemSolution> <SelectedLoadCaseCount> <LoadCaseCount> <LoadCaseSet> <ReserveFactor> <Sentinel>
        """
        Calculation: int
        FailureMode: int
        LoadCase: int
        MarginOfSafety: int
        GlobalRank: int
        RankByCalculation: int
        RankByFailureMode: int
        RankByLoadCase: int
        Method: int
        FemSolution: int
        SelectedLoadCaseCount: int
        LoadCaseCount: int
        LoadCaseSet: int
        ReserveFactor: int
        Sentinel: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MarginResultTableDataProvider.ColumnType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Creates a query based on this table data provider. For this query to be useful the appropriate columns must be registered.
    ##  @return query (@link MarginResultQuery NXOpen.CAE.AeroStructures.MarginResultQuery@endlink):  output query.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    def CreateQuery(context: MarginResultTableDataProvider) -> MarginResultQuery:
        """
         Creates a query based on this table data provider. For this query to be useful the appropriate columns must be registered.
         @return query (@link MarginResultQuery NXOpen.CAE.AeroStructures.MarginResultQuery@endlink):  output query.
        """
        pass
    
    ##  Register all columns listed in the ColumnType enumeration (except for the sentinel value)  
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    @staticmethod
    def RegisterAllColumns(context: MarginResultTableDataProvider) -> None:
        """
         Register all columns listed in the ColumnType enumeration (except for the sentinel value)  
        """
        pass
    
    ##  Register a new column 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  the column index which must correspond to the number of currently registered columns otherwise the method fails 
    def RegisterColumn(context: MarginResultTableDataProvider, columnIdx: int, columnType: MarginResultTableDataProvider.ColumnType) -> None:
        """
         Register a new column 
        """
        pass
    
import NXOpen
##   @brief  A MarginResultTableRowFilter holds conditions which can be applied to a MarginResultTableRow.
##             The filter is used to create a MarginResultTableFilterQuery which is used to filter out rows from a 
##             result table or from another input query.      
## 
##    <br> To create a new instance of this class, use @link NXOpen::CAE::AeroStructures::MarginSolution::CreateMarginResultTableRowFilter  NXOpen::CAE::AeroStructures::MarginSolution::CreateMarginResultTableRowFilter @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class MarginResultTableRowFilter(NXOpen.TransientObject): 
    """ <summary> A MarginResultTableRowFilter holds conditions which can be applied to a MarginResultTableRow.
            The filter is used to create a MarginResultTableFilterQuery which is used to filter out rows from a 
            result table or from another input query.     </summary> """


    ##  Numeric comparison operator
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
    ## LessOrEqual</term><description> 
    ## </description> </item><item><term> 
    ## GreaterThan</term><description> 
    ## </description> </item><item><term> 
    ## GreaterOrEqual</term><description> 
    ## </description> </item></list>
    class NumericComparisonOperator(Enum):
        """
        Members Include: <Equal> <NotEqual> <LessThan> <LessOrEqual> <GreaterThan> <GreaterOrEqual>
        """
        Equal: int
        NotEqual: int
        LessThan: int
        LessOrEqual: int
        GreaterThan: int
        GreaterOrEqual: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MarginResultTableRowFilter.NumericComparisonOperator:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  String comparison operator
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
    ## LessOrEqual</term><description> 
    ## </description> </item><item><term> 
    ## GreaterThan</term><description> 
    ## </description> </item><item><term> 
    ## GreaterOrEqual</term><description> 
    ## </description> </item><item><term> 
    ## StartsWith</term><description> 
    ## </description> </item><item><term> 
    ## EndsWith</term><description> 
    ## </description> </item><item><term> 
    ## Contains</term><description> 
    ## </description> </item></list>
    class StringComparisonOperator(Enum):
        """
        Members Include: <Equal> <NotEqual> <LessThan> <LessOrEqual> <GreaterThan> <GreaterOrEqual> <StartsWith> <EndsWith> <Contains>
        """
        Equal: int
        NotEqual: int
        LessThan: int
        LessOrEqual: int
        GreaterThan: int
        GreaterOrEqual: int
        StartsWith: int
        EndsWith: int
        Contains: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MarginResultTableRowFilter.StringComparisonOperator:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Add a new case-insensitive condition on a string column 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  the registered column type 
    def AddCiCondition(filter: MarginResultTableRowFilter, columnType: MarginResultTableDataProvider.ColumnType, op: MarginResultTableRowFilter.StringComparisonOperator, value: str) -> None:
        """
         Add a new case-insensitive condition on a string column 
        """
        pass
    
    ##  Add a new condition on an integer column 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  the registered column type 
    @overload
    def AddCondition(self, filter: MarginResultTableRowFilter, columnType: MarginResultTableDataProvider.ColumnType, op: MarginResultTableRowFilter.NumericComparisonOperator, value: int) -> None:
        """
         Add a new condition on an integer column 
        """
        pass
    
    ##  Add a new condition on a numeric column 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  the registered column type 
    @overload
    def AddCondition(self, filter: MarginResultTableRowFilter, columnType: MarginResultTableDataProvider.ColumnType, op: MarginResultTableRowFilter.NumericComparisonOperator, value: float) -> None:
        """
         Add a new condition on a numeric column 
        """
        pass
    
    ##  Add a new condition on a string column 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  the registered column type 
    @overload
    def AddCondition(self, filter: MarginResultTableRowFilter, columnType: MarginResultTableDataProvider.ColumnType, op: MarginResultTableRowFilter.StringComparisonOperator, value: str) -> None:
        """
         Add a new condition on a string column 
        """
        pass
    
    ##  Adds another filter to the conditions of the current filter
    ##                  if the current filter is a conjunction the new filter is logically AND-ed 
    ##                  if the current filter is a disjunction the new filter is logically OR-ed
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## <param name="filter"> (@link MarginResultTableRowFilter NXOpen.CAE.AeroStructures.MarginResultTableRowFilter@endlink) </param>
    ## <param name="otherFilter"> (@link MarginResultTableRowFilter NXOpen.CAE.AeroStructures.MarginResultTableRowFilter@endlink) </param>
    @overload
    def AddCondition(self, filter: MarginResultTableRowFilter, otherFilter: MarginResultTableRowFilter) -> None:
        """
         Adds another filter to the conditions of the current filter
                         if the current filter is a conjunction the new filter is logically AND-ed 
                         if the current filter is a disjunction the new filter is logically OR-ed
        """
        pass
    
    ##  Logically AND with the current filter 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ## <param name="otherFilter"> (@link MarginResultTableRowFilter NXOpen.CAE.AeroStructures.MarginResultTableRowFilter@endlink) </param>
    def AndWith(filter: MarginResultTableRowFilter, otherFilter: MarginResultTableRowFilter) -> None:
        """
         Logically AND with the current filter 
        """
        pass
    
    ##  Dispose 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(filter: MarginResultTableRowFilter) -> None:
        """
         Dispose 
        """
        pass
    
    ##  Logically OR with the current filter 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ## <param name="otherFilter"> (@link MarginResultTableRowFilter NXOpen.CAE.AeroStructures.MarginResultTableRowFilter@endlink) </param>
    def OrWith(filter: MarginResultTableRowFilter, otherFilter: MarginResultTableRowFilter) -> None:
        """
         Logically OR with the current filter 
        """
        pass
    
import NXOpen
##   @brief  MarginResultTableRow represents one row in a result table and is returned by a query iterator  
## 
##   
## 
##   <br>  Created in NX12.0.0  <br> 

class MarginResultTableRow(NXOpen.TransientObject): 
    """ <summary> MarginResultTableRow represents one row in a result table and is returned by a query iterator </summary> """


    ## Getter for property: (@link MarginCalculation NXOpen.CAE.AeroStructures.MarginCalculation@endlink) Calculation
    ##   the calculation object for this row   
    ##     
    ##  
    ## Getter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return MarginCalculation
    @property
    def Calculation(self) -> MarginCalculation:
        """
        Getter for property: (@link MarginCalculation NXOpen.CAE.AeroStructures.MarginCalculation@endlink) Calculation
          the calculation object for this row   
            
         
        """
        pass
    
    ## Getter for property: (str) CalculationName
    ##   the calculation name for this row   
    ##     
    ##  
    ## Getter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def CalculationName(self) -> str:
        """
        Getter for property: (str) CalculationName
          the calculation name for this row   
            
         
        """
        pass
    
    ## Getter for property: (str) FailureModeName
    ##   the failure mode name for this row   
    ##     
    ##  
    ## Getter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def FailureModeName(self) -> str:
        """
        Getter for property: (str) FailureModeName
          the failure mode name for this row   
            
         
        """
        pass
    
    ## Getter for property: (str) FemSolutionName
    ##   the fem solution name for this row   
    ##     
    ##  
    ## Getter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def FemSolutionName(self) -> str:
        """
        Getter for property: (str) FemSolutionName
          the fem solution name for this row   
            
         
        """
        pass
    
    ## Getter for property: (int) GlobalRank
    ##   the global rank for this row   
    ##     
    ##  
    ## Getter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def GlobalRank(self) -> int:
        """
        Getter for property: (int) GlobalRank
          the global rank for this row   
            
         
        """
        pass
    
    ## Getter for property: (str) LoadCaseName
    ##   the load case name for this row   
    ##     
    ##  
    ## Getter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def LoadCaseName(self) -> str:
        """
        Getter for property: (str) LoadCaseName
          the load case name for this row   
            
         
        """
        pass
    
    ## Getter for property: (float) MarginOfSafety
    ##   the margin of safety for this row   
    ##     
    ##  
    ## Getter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return float
    @property
    def MarginOfSafety(self) -> float:
        """
        Getter for property: (float) MarginOfSafety
          the margin of safety for this row   
            
         
        """
        pass
    
    ## Getter for property: (str) MethodName
    ##   the method name implementing the calculation for this row   
    ##     
    ##  
    ## Getter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def MethodName(self) -> str:
        """
        Getter for property: (str) MethodName
          the method name implementing the calculation for this row   
            
         
        """
        pass
    
    ## Getter for property: (int) RankByCalculation
    ##   the rank by calculation for this row   
    ##     
    ##  
    ## Getter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def RankByCalculation(self) -> int:
        """
        Getter for property: (int) RankByCalculation
          the rank by calculation for this row   
            
         
        """
        pass
    
    ## Getter for property: (int) RankByFailureMode
    ##   the rank by failure_mode for this row   
    ##     
    ##  
    ## Getter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def RankByFailureMode(self) -> int:
        """
        Getter for property: (int) RankByFailureMode
          the rank by failure_mode for this row   
            
         
        """
        pass
    
    ## Getter for property: (int) RankByLoadCase
    ##   the rank by load case for this row   
    ##     
    ##  
    ## Getter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def RankByLoadCase(self) -> int:
        """
        Getter for property: (int) RankByLoadCase
          the rank by load case for this row   
            
         
        """
        pass
    
    ## Getter for property: (float) ReserveFactor
    ##   the reserve factor for this row   
    ##     
    ##  
    ## Getter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return float
    @property
    def ReserveFactor(self) -> float:
        """
        Getter for property: (float) ReserveFactor
          the reserve factor for this row   
            
         
        """
        pass
    
    ##  Dispose 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(row: MarginResultTableRow) -> None:
        """
         Dispose 
        """
        pass
    
    ##  Get the value of a boolean input parameter for this row 
    ##  @return value (bool): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetInputBooleanValue(row: MarginResultTableRow, parameterName: str) -> bool:
        """
         Get the value of a boolean input parameter for this row 
         @return value (bool): .
        """
        pass
    
    ##  Get the value of an integer input parameter for this row 
    ##  @return value (int): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetInputIntegerValue(row: MarginResultTableRow, parameterName: str) -> int:
        """
         Get the value of an integer input parameter for this row 
         @return value (int): .
        """
        pass
    
    ##  Get the aggregated or non aggregated load values of an input parameter for this row.
    ##                     If the load values were aggregated, the output will be an array with only one value.
    ##                     If the values were not aggregated, the output will be an array with one value per element or node. 
    ##  @return values (List[float]): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetInputLoad(row: MarginResultTableRow, parameterName: str) -> List[float]:
        """
         Get the aggregated or non aggregated load values of an input parameter for this row.
                            If the load values were aggregated, the output will be an array with only one value.
                            If the values were not aggregated, the output will be an array with one value per element or node. 
         @return values (List[float]): .
        """
        pass
    
    ##  Get the measure of a scalar input parameter for this row. 
    ##  @return measure (str): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetInputScalarMeasure(row: MarginResultTableRow, parameterName: str) -> str:
        """
         Get the measure of a scalar input parameter for this row. 
         @return measure (str): .
        """
        pass
    
    ##  Get the unit of a scalar input parameter for this row 
    ##  @return unit_type (@link NXOpen.Unit NXOpen.Unit@endlink):  the unit of the value returned by @link CAE::AeroStructures::MarginResultTableRow::GetInputScalarValue CAE::AeroStructures::MarginResultTableRow::GetInputScalarValue@endlink .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetInputScalarUnit(row: MarginResultTableRow, parameterName: str) -> NXOpen.Unit:
        """
         Get the unit of a scalar input parameter for this row 
         @return unit_type (@link NXOpen.Unit NXOpen.Unit@endlink):  the unit of the value returned by @link CAE::AeroStructures::MarginResultTableRow::GetInputScalarValue CAE::AeroStructures::MarginResultTableRow::GetInputScalarValue@endlink .
        """
        pass
    
    ##  Get the value of a scalar input parameter for this row 
    ##  @return value (float): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetInputScalarValue(row: MarginResultTableRow, parameterName: str) -> float:
        """
         Get the value of a scalar input parameter for this row 
         @return value (float): .
        """
        pass
    
    ##  Get the value of a string input parameter for this row 
    ##  @return value (str): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetInputStringValue(row: MarginResultTableRow, parameterName: str) -> str:
        """
         Get the value of a string input parameter for this row 
         @return value (str): .
        """
        pass
    
    ##  Get the value of a boolean output parameter for this row 
    ##  @return value (bool): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetOutputBooleanValue(row: MarginResultTableRow, parameterName: str) -> bool:
        """
         Get the value of a boolean output parameter for this row 
         @return value (bool): .
        """
        pass
    
    ##  Get the value of an integer output parameter for this row 
    ##  @return value (int): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetOutputIntegerValue(row: MarginResultTableRow, parameterName: str) -> int:
        """
         Get the value of an integer output parameter for this row 
         @return value (int): .
        """
        pass
    
    ##  Get the measure of a scalar output parameter for this row. 
    ##  @return measure (str): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetOutputScalarMeasure(row: MarginResultTableRow, parameterName: str) -> str:
        """
         Get the measure of a scalar output parameter for this row. 
         @return measure (str): .
        """
        pass
    
    ##  Get the unit of a scalar output parameter for this row.
    ##                 An exception(code "3520027") will be thrown if no unit can be found with the given parameter.
    ##                 An exception(code "3520046") will be thrown if the unit measure of the given parameter is Unitless,
    ##                 this API returns NULL as well.
    ##                 
    ##  @return unit_type (@link NXOpen.Unit NXOpen.Unit@endlink):  the unit of the value returned by @link CAE::AeroStructures::MarginResultTableRow::GetOutputScalarValue CAE::AeroStructures::MarginResultTableRow::GetOutputScalarValue@endlink .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetOutputScalarUnit(row: MarginResultTableRow, parameterName: str) -> NXOpen.Unit:
        """
         Get the unit of a scalar output parameter for this row.
                        An exception(code "3520027") will be thrown if no unit can be found with the given parameter.
                        An exception(code "3520046") will be thrown if the unit measure of the given parameter is Unitless,
                        this API returns NULL as well.
                        
         @return unit_type (@link NXOpen.Unit NXOpen.Unit@endlink):  the unit of the value returned by @link CAE::AeroStructures::MarginResultTableRow::GetOutputScalarValue CAE::AeroStructures::MarginResultTableRow::GetOutputScalarValue@endlink .
        """
        pass
    
    ##  Get the value of a scalar output parameter for this row 
    ##  @return value (float): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetOutputScalarValue(row: MarginResultTableRow, parameterName: str) -> float:
        """
         Get the value of a scalar output parameter for this row 
         @return value (float): .
        """
        pass
    
    ##  Get the value of a string output parameter for this row 
    ##  @return value (str): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ## <param name="parameterName"> (str) </param>
    def GetOutputStringValue(row: MarginResultTableRow, parameterName: str) -> str:
        """
         Get the value of a string output parameter for this row 
         @return value (str): .
        """
        pass
    
import NXOpen
import NXOpen.CAE
##  This is a manager to the @link CAE::AeroStructures::MarginSolution CAE::AeroStructures::MarginSolution@endlink  class.
##     Object of type @link CAE::AeroStructures::MarginSolution CAE::AeroStructures::MarginSolution@endlink  can be
##     created and edited only through this class
##      <br> To create a new instance of this class, use @link NXOpen::CAE::AeroStructures::MarginSolutionCollection::CreateMarginSolutionBuilder  NXOpen::CAE::AeroStructures::MarginSolutionCollection::CreateMarginSolutionBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class MarginSolutionBuilder(NXOpen.Builder): 
    """ This is a manager to the <ja_class>CAE.AeroStructures.MarginSolution</ja_class> class.
    Object of type <ja_class>CAE.AeroStructures.MarginSolution</ja_class> can be
    created and edited only through this class
    """


    ## Getter for property: (str) Description
    ##    a Get the metasolution description  
    ##     
    ##  
    ## Getter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
           a Get the metasolution description  
            
         
        """
        pass
    
    ## Setter for property: (str) Description

    ##    a Get the metasolution description  
    ##     
    ##  
    ## Setter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Description.setter
    def Description(self, title: str):
        """
        Setter for property: (str) Description
           a Get the metasolution description  
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##   the metasolution name  
    ##     
    ##  
    ## Getter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
          the metasolution name  
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##   the metasolution name  
    ##     
    ##  
    ## Setter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Name.setter
    def Name(self, title: str):
        """
        Setter for property: (str) Name
          the metasolution name  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.SimSolution NXOpen.CAE.SimSolution@endlink) ReferenceSolution
    ##   the referenced FE-Solution of the AeroStructure solution   
    ##     
    ##  
    ## Getter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.CAE.SimSolution
    @property
    def ReferenceSolution(self) -> NXOpen.CAE.SimSolution:
        """
        Getter for property: (@link NXOpen.CAE.SimSolution NXOpen.CAE.SimSolution@endlink) ReferenceSolution
          the referenced FE-Solution of the AeroStructure solution   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.SimSolution NXOpen.CAE.SimSolution@endlink) ReferenceSolution

    ##   the referenced FE-Solution of the AeroStructure solution   
    ##     
    ##  
    ## Setter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ReferenceSolution.setter
    def ReferenceSolution(self, referenceSolution: NXOpen.CAE.SimSolution):
        """
        Setter for property: (@link NXOpen.CAE.SimSolution NXOpen.CAE.SimSolution@endlink) ReferenceSolution
          the referenced FE-Solution of the AeroStructure solution   
            
         
        """
        pass
    
    ## Getter for property: (str) UnitSystem
    ##   the unit system of the margin solution  
    ##     
    ##  
    ## Getter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def UnitSystem(self) -> str:
        """
        Getter for property: (str) UnitSystem
          the unit system of the margin solution  
            
         
        """
        pass
    
    ## Setter for property: (str) UnitSystem

    ##   the unit system of the margin solution  
    ##     
    ##  
    ## Setter License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @UnitSystem.setter
    def UnitSystem(self, unit_system: str):
        """
        Setter for property: (str) UnitSystem
          the unit system of the margin solution  
            
         
        """
        pass
    
import NXOpen
##  Represents a collection of  margin solution.  <br> To obtain an instance of this class, refer to @link NXOpen::CAE::AeroStructManager  NXOpen::CAE::AeroStructManager @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class MarginSolutionCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of  margin solution. """


    ##  Clones a AeroStruct marginsolution. 
    ##  @return copy (@link MarginSolution NXOpen.CAE.AeroStructures.MarginSolution@endlink):  Cloned metasolution .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  Source metasolution 
    def CloneMarginSolution(sim: MarginSolutionCollection, source: MarginSolution) -> MarginSolution:
        """
         Clones a AeroStruct marginsolution. 
         @return copy (@link MarginSolution NXOpen.CAE.AeroStructures.MarginSolution@endlink):  Cloned metasolution .
        """
        pass
    
    ##  Creates the builder object of AeroStruct meta solution. 
    ##  @return builder (@link MarginSolutionBuilder NXOpen.CAE.AeroStructures.MarginSolutionBuilder@endlink):   .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##   
    def CreateMarginSolutionBuilder(sim: MarginSolutionCollection, metasolution: MarginSolution) -> MarginSolutionBuilder:
        """
         Creates the builder object of AeroStruct meta solution. 
         @return builder (@link MarginSolutionBuilder NXOpen.CAE.AeroStructures.MarginSolutionBuilder@endlink):   .
        """
        pass
    
    ##  Delete a AeroStruct metasolution. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The AeroStruct margin_solution to be deleted 
    def DeleteMarginSolution(sim: MarginSolutionCollection, metasolution: MarginSolution) -> None:
        """
         Delete a AeroStruct metasolution. 
        """
        pass
    
    ##  Finds a AeroStruct margin solution with a specified name. 
    ##  @return found (@link MarginSolution NXOpen.CAE.AeroStructures.MarginSolution@endlink):  The AeroStruct margin solution .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  name of the AeroStruct margin  
    def FindObject(sim: MarginSolutionCollection, name: str) -> MarginSolution:
        """
         Finds a AeroStruct margin solution with a specified name. 
         @return found (@link MarginSolution NXOpen.CAE.AeroStructures.MarginSolution@endlink):  The AeroStruct margin solution .
        """
        pass
    
    ##  Returns the active margincalculation. 
    ##  @return activeCalculation (@link MarginCalculation NXOpen.CAE.AeroStructures.MarginCalculation@endlink):  The active margincalculation .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    @staticmethod
    def GetActiveMargincalculation(simulation: MarginSolutionCollection) -> MarginCalculation:
        """
         Returns the active margincalculation. 
         @return activeCalculation (@link MarginCalculation NXOpen.CAE.AeroStructures.MarginCalculation@endlink):  The active margincalculation .
        """
        pass
    
    ##  Returns the active marginsolution. 
    ##  @return activeSolution (@link MarginSolution NXOpen.CAE.AeroStructures.MarginSolution@endlink):  The active metasolution .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    @staticmethod
    def GetActiveMarginsolution(sim: MarginSolutionCollection) -> MarginSolution:
        """
         Returns the active marginsolution. 
         @return activeSolution (@link MarginSolution NXOpen.CAE.AeroStructures.MarginSolution@endlink):  The active metasolution .
        """
        pass
    
    ##  Sets the active margin calculation. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The margincalculation to activate
    def SetActiveMargincalculation(simulation: MarginSolutionCollection, activeCalculation: MarginCalculation) -> None:
        """
         Sets the active margin calculation. 
        """
        pass
    
    ##  Activates the marginsolution. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The metasolution to activate
    def SetActiveMarginsolution(sim: MarginSolutionCollection, source: MarginSolution) -> None:
        """
         Activates the marginsolution. 
        """
        pass
    
import NXOpen.Report
##  Represents a @link NXOpen::CAE::AeroStructures::MarginSolution NXOpen::CAE::AeroStructures::MarginSolution@endlink .  <br> To create or edit an instance of this class, use @link NXOpen::CAE::AeroStructures::MarginSolutionBuilder  NXOpen::CAE::AeroStructures::MarginSolutionBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class MarginSolution(BaseSolution): 
    """ Represents a <ja_class>NXOpen.CAE.AeroStructures.MarginSolution</ja_class>. """


    ##  Returns the @link NXOpen::CAE::AeroStructures::MarginCalculationCollection NXOpen::CAE::AeroStructures::MarginCalculationCollection@endlink  belonging to this 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @link MarginCalculationCollection NXOpen.CAE.AeroStructures.MarginCalculationCollection@endlink
    @property
    def MarginCalculationCollection() -> MarginCalculationCollection:
        """
         Returns the @link NXOpen::CAE::AeroStructures::MarginCalculationCollection NXOpen::CAE::AeroStructures::MarginCalculationCollection@endlink  belonging to this 
        """
        pass
    
    ##  Returns the @link NXOpen::CAE::AeroStructures::ExpressionCollection NXOpen::CAE::AeroStructures::ExpressionCollection@endlink  belonging to this 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @link ExpressionCollection NXOpen.CAE.AeroStructures.ExpressionCollection@endlink
    @property
    def ExpressionCollection() -> ExpressionCollection:
        """
         Returns the @link NXOpen::CAE::AeroStructures::ExpressionCollection NXOpen::CAE::AeroStructures::ExpressionCollection@endlink  belonging to this 
        """
        pass
    
    ##  Returns the @link NXOpen::CAE::AeroStructures::GraphicalReportCollection NXOpen::CAE::AeroStructures::GraphicalReportCollection@endlink  belonging to this 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @link GraphicalReportCollection NXOpen.CAE.AeroStructures.GraphicalReportCollection@endlink
    @property
    def GraphicalReportCollection() -> GraphicalReportCollection:
        """
         Returns the @link NXOpen::CAE::AeroStructures::GraphicalReportCollection NXOpen::CAE::AeroStructures::GraphicalReportCollection@endlink  belonging to this 
        """
        pass
    
    ##  Create critical MS expression 
    ##  @return expression (@link ExpressionResult NXOpen.CAE.AeroStructures.ExpressionResult@endlink):  The critical MS expression .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The list of calculations from the solution to consider 
    def CreateCriticalMs(margin: MarginSolution, name: str, marginCalculations: List[MarginCalculation]) -> ExpressionResult:
        """
         Create critical MS expression 
         @return expression (@link ExpressionResult NXOpen.CAE.AeroStructures.ExpressionResult@endlink):  The critical MS expression .
        """
        pass
    
    ##  Creates a @link NXOpen::CAE::AeroStructures::MarginResultQuery NXOpen::CAE::AeroStructures::MarginResultQuery@endlink  
    ##              containing all the results of every calculation that has been solved and belongs to this solution
    ##              If a non-null @link CAE::AeroStructures::MarginResultTableRowFilter CAE::AeroStructures::MarginResultTableRowFilter@endlink  is passed as argument
    ##              the results are further post-filtered (after the rank calculation has taken place) according to that filter
    ##             
    ##  @return query (@link MarginResultQuery NXOpen.CAE.AeroStructures.MarginResultQuery@endlink):  output query .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  additional post filter (may be null)
    @overload
    def CreateMarginResultQuery(self, marginSolution: MarginSolution, filter: MarginResultTableRowFilter) -> MarginResultQuery:
        """
         Creates a @link NXOpen::CAE::AeroStructures::MarginResultQuery NXOpen::CAE::AeroStructures::MarginResultQuery@endlink  
                     containing all the results of every calculation that has been solved and belongs to this solution
                     If a non-null @link CAE::AeroStructures::MarginResultTableRowFilter CAE::AeroStructures::MarginResultTableRowFilter@endlink  is passed as argument
                     the results are further post-filtered (after the rank calculation has taken place) according to that filter
                    
         @return query (@link MarginResultQuery NXOpen.CAE.AeroStructures.MarginResultQuery@endlink):  output query .
        """
        pass
    
    ##  Creates a @link NXOpen::CAE::AeroStructures::MarginResultQuery NXOpen::CAE::AeroStructures::MarginResultQuery@endlink  
    ##              containing all the results of every calculation passed in the argument 
    ##              that has been solved and belongs to this solution
    ##              If a non-null @link CAE::AeroStructures::MarginResultTableRowFilter CAE::AeroStructures::MarginResultTableRowFilter@endlink  is passed as argument
    ##              the results are further post-filtered (after the rank calculation has taken place) according to that filter
    ##             
    ##  @return query (@link MarginResultQuery NXOpen.CAE.AeroStructures.MarginResultQuery@endlink):   output query .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  The list of calculations from the solution to consider, only the ones with results are taken into account 
    @overload
    def CreateMarginResultQuery(self, marginSolution: MarginSolution, marginCalculations: List[MarginCalculation], filter: MarginResultTableRowFilter) -> MarginResultQuery:
        """
         Creates a @link NXOpen::CAE::AeroStructures::MarginResultQuery NXOpen::CAE::AeroStructures::MarginResultQuery@endlink  
                     containing all the results of every calculation passed in the argument 
                     that has been solved and belongs to this solution
                     If a non-null @link CAE::AeroStructures::MarginResultTableRowFilter CAE::AeroStructures::MarginResultTableRowFilter@endlink  is passed as argument
                     the results are further post-filtered (after the rank calculation has taken place) according to that filter
                    
         @return query (@link MarginResultQuery NXOpen.CAE.AeroStructures.MarginResultQuery@endlink):   output query .
        """
        pass
    
    ##  Creates a @link NXOpen::CAE::AeroStructures::MarginResultQuery NXOpen::CAE::AeroStructures::MarginResultQuery@endlink  
    ##             containing all the results of every calculation belonging to this solution that has been solved and 
    ##             that satisfies the following pre-conditions:
    ##             - the margin of safety is less than or equal to the maxMS specified in the argument
    ##             - the global rank is less than or equal to the maxRank specified in the argument
    ##             Results that do not satisfy these conditions are ignored and do not participate in the
    ##             computation of the other ranks.
    ##             If a non-null @link CAE::AeroStructures::MarginResultTableRowFilter CAE::AeroStructures::MarginResultTableRowFilter@endlink  is passed as argument
    ##             the results are further post-filtered (after the rank calculation has taken place) according to that filter
    ##             
    ##  @return query (@link MarginResultQuery NXOpen.CAE.AeroStructures.MarginResultQuery@endlink):   margin result table data provider object.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  the global maximum rank permitted, effectively restricting the number of possible rows in the table 
    @overload
    def CreateMarginResultQuery(self, marginSolution: MarginSolution, maxRank: int, maxMS: float, filter: MarginResultTableRowFilter) -> MarginResultQuery:
        """
         Creates a @link NXOpen::CAE::AeroStructures::MarginResultQuery NXOpen::CAE::AeroStructures::MarginResultQuery@endlink  
                    containing all the results of every calculation belonging to this solution that has been solved and 
                    that satisfies the following pre-conditions:
                    - the margin of safety is less than or equal to the maxMS specified in the argument
                    - the global rank is less than or equal to the maxRank specified in the argument
                    Results that do not satisfy these conditions are ignored and do not participate in the
                    computation of the other ranks.
                    If a non-null @link CAE::AeroStructures::MarginResultTableRowFilter CAE::AeroStructures::MarginResultTableRowFilter@endlink  is passed as argument
                    the results are further post-filtered (after the rank calculation has taken place) according to that filter
                    
         @return query (@link MarginResultQuery NXOpen.CAE.AeroStructures.MarginResultQuery@endlink):   margin result table data provider object.
        """
        pass
    
    ##  Creates a @link NXOpen::CAE::AeroStructures::MarginResultQuery NXOpen::CAE::AeroStructures::MarginResultQuery@endlink  
    ##             containing the results of the calculations passed in the argument belonging to this solution that have been solved and 
    ##             that satisfy the following pre-conditions:
    ##             - the margin of safety is less than or equal to the maxMS specified in the argument
    ##             - the global rank is less than or equal to the maxRank specified in the argument
    ##             Results that do not satisfy these conditions are ignored and do not participate in the
    ##             computation of the other ranks.
    ##             If a non-null @link CAE::AeroStructures::MarginResultTableRowFilter CAE::AeroStructures::MarginResultTableRowFilter@endlink  is passed as argument
    ##             the results are further post-filtered (after the rank calculation has taken place) according to that filter
    ##             
    ##  @return query (@link MarginResultQuery NXOpen.CAE.AeroStructures.MarginResultQuery@endlink):   margin result table data provider object.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  The list of calculations from the solution to consider, only the ones with results are taken into account 
    @overload
    def CreateMarginResultQuery(self, marginSolution: MarginSolution, marginCalculations: List[MarginCalculation], maxRank: int, maxMS: float, filter: MarginResultTableRowFilter) -> MarginResultQuery:
        """
         Creates a @link NXOpen::CAE::AeroStructures::MarginResultQuery NXOpen::CAE::AeroStructures::MarginResultQuery@endlink  
                    containing the results of the calculations passed in the argument belonging to this solution that have been solved and 
                    that satisfy the following pre-conditions:
                    - the margin of safety is less than or equal to the maxMS specified in the argument
                    - the global rank is less than or equal to the maxRank specified in the argument
                    Results that do not satisfy these conditions are ignored and do not participate in the
                    computation of the other ranks.
                    If a non-null @link CAE::AeroStructures::MarginResultTableRowFilter CAE::AeroStructures::MarginResultTableRowFilter@endlink  is passed as argument
                    the results are further post-filtered (after the rank calculation has taken place) according to that filter
                    
         @return query (@link MarginResultQuery NXOpen.CAE.AeroStructures.MarginResultQuery@endlink):   margin result table data provider object.
        """
        pass
    
    ##  Creates a @link NXOpen::CAE::AeroStructures::MarginResultTableDataProvider NXOpen::CAE::AeroStructures::MarginResultTableDataProvider@endlink  
    ##             which will be based on every calculation of this solution that has results
    ##         
    ##             Note: no column is registered by default. 
    ##                   Methods @link  CAE::AeroStructures::MarginResultTableDataProvider::RegisterAllColumns  CAE::AeroStructures::MarginResultTableDataProvider::RegisterAllColumns@endlink  or
    ##                   Methods @link  CAE::AeroStructures::MarginResultTableDataProvider::RegisterColumn  CAE::AeroStructures::MarginResultTableDataProvider::RegisterColumn@endlink 
    ##                   should be called after calling this creator
    ##         
    ##  @return tableDataProvider (@link MarginResultTableDataProvider NXOpen.CAE.AeroStructures.MarginResultTableDataProvider@endlink):   margin result table data provider object.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## <param name="marginSolution"> (@link MarginSolution NXOpen.CAE.AeroStructures.MarginSolution@endlink) </param>
    @overload
    def CreateMarginResultTableDataProvider(self, marginSolution: MarginSolution) -> MarginResultTableDataProvider:
        """
         Creates a @link NXOpen::CAE::AeroStructures::MarginResultTableDataProvider NXOpen::CAE::AeroStructures::MarginResultTableDataProvider@endlink  
                    which will be based on every calculation of this solution that has results
                
                    Note: no column is registered by default. 
                          Methods @link  CAE::AeroStructures::MarginResultTableDataProvider::RegisterAllColumns  CAE::AeroStructures::MarginResultTableDataProvider::RegisterAllColumns@endlink  or
                          Methods @link  CAE::AeroStructures::MarginResultTableDataProvider::RegisterColumn  CAE::AeroStructures::MarginResultTableDataProvider::RegisterColumn@endlink 
                          should be called after calling this creator
                
         @return tableDataProvider (@link MarginResultTableDataProvider NXOpen.CAE.AeroStructures.MarginResultTableDataProvider@endlink):   margin result table data provider object.
        """
        pass
    
    ##  Creates a @link NXOpen::CAE::AeroStructures::MarginResultTableDataProvider NXOpen::CAE::AeroStructures::MarginResultTableDataProvider@endlink  
    ##             Only the subset of calculations given in the argument which have results are taken into account
    ##         
    ##             Note: no column is registered by default. 
    ##                   Methods @link  CAE::AeroStructures::MarginResultTableDataProvider::RegisterAllColumns  CAE::AeroStructures::MarginResultTableDataProvider::RegisterAllColumns@endlink  or
    ##                   Methods @link  CAE::AeroStructures::MarginResultTableDataProvider::RegisterColumn  CAE::AeroStructures::MarginResultTableDataProvider::RegisterColumn@endlink 
    ##                   should be called after calling this creator
    ##          
    ##  @return tableDataProvider (@link MarginResultTableDataProvider NXOpen.CAE.AeroStructures.MarginResultTableDataProvider@endlink):   margin result table data provider object.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  The list of calculations from the solution to consider, only the ones with results are taken into account 
    @overload
    def CreateMarginResultTableDataProvider(self, marginSolution: MarginSolution, marginCalculations: List[MarginCalculation]) -> MarginResultTableDataProvider:
        """
         Creates a @link NXOpen::CAE::AeroStructures::MarginResultTableDataProvider NXOpen::CAE::AeroStructures::MarginResultTableDataProvider@endlink  
                    Only the subset of calculations given in the argument which have results are taken into account
                
                    Note: no column is registered by default. 
                          Methods @link  CAE::AeroStructures::MarginResultTableDataProvider::RegisterAllColumns  CAE::AeroStructures::MarginResultTableDataProvider::RegisterAllColumns@endlink  or
                          Methods @link  CAE::AeroStructures::MarginResultTableDataProvider::RegisterColumn  CAE::AeroStructures::MarginResultTableDataProvider::RegisterColumn@endlink 
                          should be called after calling this creator
                 
         @return tableDataProvider (@link MarginResultTableDataProvider NXOpen.CAE.AeroStructures.MarginResultTableDataProvider@endlink):   margin result table data provider object.
        """
        pass
    
    ##  Creates a @link NXOpen::CAE::AeroStructures::MarginResultTableDataProvider NXOpen::CAE::AeroStructures::MarginResultTableDataProvider@endlink  
    ##             which will be based on every calculation of this solution that has results 
    ##             and satisfies the following conditions:
    ##             - the margin of safety is less than or equal to the maxMS specified in argument
    ##             - the global rank is less than or equal to the maxRank specified in argument
    ##             Results that do not satisfy these conditions are ignored and do not participate in the
    ##             computation of the other ranks.
    ##             
    ##             Note: no column is registered by default. 
    ##                   Methods @link  CAE::AeroStructures::MarginResultTableDataProvider::RegisterAllColumns  CAE::AeroStructures::MarginResultTableDataProvider::RegisterAllColumns@endlink  or
    ##                   Methods @link  CAE::AeroStructures::MarginResultTableDataProvider::RegisterColumn  CAE::AeroStructures::MarginResultTableDataProvider::RegisterColumn@endlink 
    ##                   should be called after calling this creator
    ##           
    ##  @return tableDataProvider (@link MarginResultTableDataProvider NXOpen.CAE.AeroStructures.MarginResultTableDataProvider@endlink):   margin result table data provider object.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  the global maximum rank permitted, effectively restricting the number of possible rows in the table 
    @overload
    def CreateMarginResultTableDataProvider(self, marginSolution: MarginSolution, maxRank: int, maxMS: float) -> MarginResultTableDataProvider:
        """
         Creates a @link NXOpen::CAE::AeroStructures::MarginResultTableDataProvider NXOpen::CAE::AeroStructures::MarginResultTableDataProvider@endlink  
                    which will be based on every calculation of this solution that has results 
                    and satisfies the following conditions:
                    - the margin of safety is less than or equal to the maxMS specified in argument
                    - the global rank is less than or equal to the maxRank specified in argument
                    Results that do not satisfy these conditions are ignored and do not participate in the
                    computation of the other ranks.
                    
                    Note: no column is registered by default. 
                          Methods @link  CAE::AeroStructures::MarginResultTableDataProvider::RegisterAllColumns  CAE::AeroStructures::MarginResultTableDataProvider::RegisterAllColumns@endlink  or
                          Methods @link  CAE::AeroStructures::MarginResultTableDataProvider::RegisterColumn  CAE::AeroStructures::MarginResultTableDataProvider::RegisterColumn@endlink 
                          should be called after calling this creator
                  
         @return tableDataProvider (@link MarginResultTableDataProvider NXOpen.CAE.AeroStructures.MarginResultTableDataProvider@endlink):   margin result table data provider object.
        """
        pass
    
    ##  Creates a @link NXOpen::CAE::AeroStructures::MarginResultTableDataProvider NXOpen::CAE::AeroStructures::MarginResultTableDataProvider@endlink  
    ##             Only the subset of calculations given in the argument which have results are taken into account
    ##             Additionally only results that satisfy the following conditions are taken into account:
    ##             - the margin of safety is less than or equal to the maxMS specified in argument
    ##             - the global rank is less than or equal to the maxRank specified in argument
    ##             Results that do not satisfy these conditions are ignored and do not participate in the
    ##             computation of the other ranks.
    ##             
    ##             Note: no column is registered by default. 
    ##                   Methods @link  CAE::AeroStructures::MarginResultTableDataProvider::RegisterAllColumns  CAE::AeroStructures::MarginResultTableDataProvider::RegisterAllColumns@endlink  or
    ##                   Methods @link  CAE::AeroStructures::MarginResultTableDataProvider::RegisterColumn  CAE::AeroStructures::MarginResultTableDataProvider::RegisterColumn@endlink 
    ##                   should be called after calling this creator
    ##         
    ##  @return tableDataProvider (@link MarginResultTableDataProvider NXOpen.CAE.AeroStructures.MarginResultTableDataProvider@endlink):   margin result table data provider object.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  The list of calculations from the solution to consider, only the ones with results are taken into account 
    @overload
    def CreateMarginResultTableDataProvider(self, marginSolution: MarginSolution, marginCalculations: List[MarginCalculation], maxRank: int, maxMS: float) -> MarginResultTableDataProvider:
        """
         Creates a @link NXOpen::CAE::AeroStructures::MarginResultTableDataProvider NXOpen::CAE::AeroStructures::MarginResultTableDataProvider@endlink  
                    Only the subset of calculations given in the argument which have results are taken into account
                    Additionally only results that satisfy the following conditions are taken into account:
                    - the margin of safety is less than or equal to the maxMS specified in argument
                    - the global rank is less than or equal to the maxRank specified in argument
                    Results that do not satisfy these conditions are ignored and do not participate in the
                    computation of the other ranks.
                    
                    Note: no column is registered by default. 
                          Methods @link  CAE::AeroStructures::MarginResultTableDataProvider::RegisterAllColumns  CAE::AeroStructures::MarginResultTableDataProvider::RegisterAllColumns@endlink  or
                          Methods @link  CAE::AeroStructures::MarginResultTableDataProvider::RegisterColumn  CAE::AeroStructures::MarginResultTableDataProvider::RegisterColumn@endlink 
                          should be called after calling this creator
                
         @return tableDataProvider (@link MarginResultTableDataProvider NXOpen.CAE.AeroStructures.MarginResultTableDataProvider@endlink):   margin result table data provider object.
        """
        pass
    
    ##  Creates an empty @link NXOpen::CAE::AeroStructures::MarginResultTableRowFilter NXOpen::CAE::AeroStructures::MarginResultTableRowFilter@endlink  
    ##             By default it is a conjunction, meaning that successive conditions added to this filter
    ##             using AddCondition will be the terms of a conjunction (cond1 AND cond2 AND ...)
    ##  @return filter (@link MarginResultTableRowFilter NXOpen.CAE.AeroStructures.MarginResultTableRowFilter@endlink):   margin result table row filter object.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## <param name="marginSolution"> (@link MarginSolution NXOpen.CAE.AeroStructures.MarginSolution@endlink) </param>
    @overload
    def CreateMarginResultTableRowFilter(self, marginSolution: MarginSolution) -> MarginResultTableRowFilter:
        """
         Creates an empty @link NXOpen::CAE::AeroStructures::MarginResultTableRowFilter NXOpen::CAE::AeroStructures::MarginResultTableRowFilter@endlink  
                    By default it is a conjunction, meaning that successive conditions added to this filter
                    using AddCondition will be the terms of a conjunction (cond1 AND cond2 AND ...)
         @return filter (@link MarginResultTableRowFilter NXOpen.CAE.AeroStructures.MarginResultTableRowFilter@endlink):   margin result table row filter object.
        """
        pass
    
    ##  Creates an empty @link NXOpen::CAE::AeroStructures::MarginResultTableRowFilter NXOpen::CAE::AeroStructures::MarginResultTableRowFilter@endlink  
    ##             Specifying if it is a conjunction or a disjunction and if it is negated or not.
    ##             This means that successive conditions added to this filter using AddCondition will be the terms of either 
    ##             a conjunction (cond1 AND cond2 AND ...) or
    ##             a disjunction (cond1 OR cond2 OR ...)
    ##             Additionally if isNegated is true the whole conjunction or disjunction is negated:
    ##             NOT(cond1 AND cond2 AND ...) or
    ##             NOT(cond1 OR cond2 OR ...)
    ##             
    ##  @return filter (@link MarginResultTableRowFilter NXOpen.CAE.AeroStructures.MarginResultTableRowFilter@endlink):   margin result table row filter object.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  If true the filter is a disjunction otherwise it is a conjunction 
    @overload
    def CreateMarginResultTableRowFilter(self, marginSolution: MarginSolution, isDisjunction: bool, isNegated: bool) -> MarginResultTableRowFilter:
        """
         Creates an empty @link NXOpen::CAE::AeroStructures::MarginResultTableRowFilter NXOpen::CAE::AeroStructures::MarginResultTableRowFilter@endlink  
                    Specifying if it is a conjunction or a disjunction and if it is negated or not.
                    This means that successive conditions added to this filter using AddCondition will be the terms of either 
                    a conjunction (cond1 AND cond2 AND ...) or
                    a disjunction (cond1 OR cond2 OR ...)
                    Additionally if isNegated is true the whole conjunction or disjunction is negated:
                    NOT(cond1 AND cond2 AND ...) or
                    NOT(cond1 OR cond2 OR ...)
                    
         @return filter (@link MarginResultTableRowFilter NXOpen.CAE.AeroStructures.MarginResultTableRowFilter@endlink):   margin result table row filter object.
        """
        pass
    
    ##  Post processing of the calculations passed in the argument belonging to this solution 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  The list of calculations from the solution to be post-processed 
    def PostProcessing(marginSolution: MarginSolution, marginCalculations: List[MarginCalculation]) -> None:
        """
         Post processing of the calculations passed in the argument belonging to this solution 
        """
        pass
    
##  Material source class.  <br> To create a new instance of this class, use @link NXOpen::CAE::AeroStructures::ExtractionSourceSet::CreateMaterialSource  NXOpen::CAE::AeroStructures::ExtractionSourceSet::CreateMaterialSource @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class MaterialSource(BaseExtractionSource): 
    """ Material source class. """
    pass


import NXOpen
##   @brief  This is the User LoadExtraction class  
## 
##    <br> No support for KF  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class MatrixManip(NXOpen.NXObject): 
    """ <summary> This is the User LoadExtraction class </summary> """


    ##  Filter Operations 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Positive</term><description> 
    ## </description> </item><item><term> 
    ## Negative</term><description> 
    ## </description> </item><item><term> 
    ## Range</term><description> 
    ## </description> </item><item><term> 
    ## NotSet</term><description> 
    ## </description> </item></list>
    class FilterOperations(Enum):
        """
        Members Include: <Positive> <Negative> <Range> <NotSet>
        """
        Positive: int
        Negative: int
        Range: int
        NotSet: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MatrixManip.FilterOperations:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Map Operations 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Absolute</term><description> 
    ## </description> </item><item><term> 
    ## NotSet</term><description> 
    ## </description> </item></list>
    class MapOperations(Enum):
        """
        Members Include: <Absolute> <NotSet>
        """
        Absolute: int
        NotSet: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MatrixManip.MapOperations:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Reduce Operations 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Max</term><description> 
    ## </description> </item><item><term> 
    ## Min</term><description> 
    ## </description> </item><item><term> 
    ## Average</term><description> 
    ## </description> </item><item><term> 
    ## Sum</term><description> 
    ## </description> </item><item><term> 
    ## NotSet</term><description> 
    ## </description> </item><item><term> 
    ## SignedAbsoluteExtremum</term><description> 
    ## </description> </item></list>
    class ReduceOperations(Enum):
        """
        Members Include: <Max> <Min> <Average> <Sum> <NotSet> <SignedAbsoluteExtremum>
        """
        Max: int
        Min: int
        Average: int
        Sum: int
        NotSet: int
        SignedAbsoluteExtremum: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MatrixManip.ReduceOperations:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Get end Measure
    ##  @return measure (str): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetEndMeasure(manip: MatrixManip) -> str:
        """
         Get end Measure
         @return measure (str): .
        """
        pass
    
    ##  Get Factor Value
    ##  @return factor (float): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetFactor(manip: MatrixManip) -> float:
        """
         Get Factor Value
         @return factor (float): .
        """
        pass
    
    ##  Get Conversion Factor Value 
    ##  @return factor (float): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetFactorConversion(manip: MatrixManip) -> float:
        """
         Get Conversion Factor Value 
         @return factor (float): .
        """
        pass
    
    ##  Get Conversion Factor expression 
    ##  @return exp (@link NXOpen.Expression NXOpen.Expression@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetFactorConversionExpression(manip: MatrixManip) -> NXOpen.Expression:
        """
         Get Conversion Factor expression 
         @return exp (@link NXOpen.Expression NXOpen.Expression@endlink): .
        """
        pass
    
    ##  Get Factor expression
    ##  @return exp (@link NXOpen.Expression NXOpen.Expression@endlink): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetFactorExpression(manip: MatrixManip) -> NXOpen.Expression:
        """
         Get Factor expression
         @return exp (@link NXOpen.Expression NXOpen.Expression@endlink): .
        """
        pass
    
    ##  Get filter lower bound
    ##  @return lowerBound (float): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetFilterLowerBound(manip: MatrixManip) -> float:
        """
         Get filter lower bound
         @return lowerBound (float): .
        """
        pass
    
    ##  Get filter lower bound expression
    ##  @return exp (@link NXOpen.Expression NXOpen.Expression@endlink): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetFilterLowerBoundExpression(manip: MatrixManip) -> NXOpen.Expression:
        """
         Get filter lower bound expression
         @return exp (@link NXOpen.Expression NXOpen.Expression@endlink): .
        """
        pass
    
    ##  Get Filter Operation 
    ##  @return filterOp (@link MatrixManip.FilterOperations NXOpen.CAE.AeroStructures.MatrixManip.FilterOperations@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetFilterOperation(manip: MatrixManip) -> MatrixManip.FilterOperations:
        """
         Get Filter Operation 
         @return filterOp (@link MatrixManip.FilterOperations NXOpen.CAE.AeroStructures.MatrixManip.FilterOperations@endlink): .
        """
        pass
    
    ##  Get filter upper bound
    ##  @return upperBound (float): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetFilterUpperBound(manip: MatrixManip) -> float:
        """
         Get filter upper bound
         @return upperBound (float): .
        """
        pass
    
    ##  Get filter upper bound expression
    ##  @return exp (@link NXOpen.Expression NXOpen.Expression@endlink): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetFilterUpperBoundExpression(manip: MatrixManip) -> NXOpen.Expression:
        """
         Get filter upper bound expression
         @return exp (@link NXOpen.Expression NXOpen.Expression@endlink): .
        """
        pass
    
    ##  Get Map Operation 
    ##  @return mapOp (@link MatrixManip.MapOperations NXOpen.CAE.AeroStructures.MatrixManip.MapOperations@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetMapOperation(manip: MatrixManip) -> MatrixManip.MapOperations:
        """
         Get Map Operation 
         @return mapOp (@link MatrixManip.MapOperations NXOpen.CAE.AeroStructures.MatrixManip.MapOperations@endlink): .
        """
        pass
    
    ##  Get Reduce Operation 
    ##  @return reduceOp (@link MatrixManip.ReduceOperations NXOpen.CAE.AeroStructures.MatrixManip.ReduceOperations@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetReduceOperation(manip: MatrixManip) -> MatrixManip.ReduceOperations:
        """
         Get Reduce Operation 
         @return reduceOp (@link MatrixManip.ReduceOperations NXOpen.CAE.AeroStructures.MatrixManip.ReduceOperations@endlink): .
        """
        pass
    
    ##  Get start Measure
    ##  @return measure (str): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetStartMeasure(manip: MatrixManip) -> str:
        """
         Get start Measure
         @return measure (str): .
        """
        pass
    
    ##  Set end Measure
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="measure"> (str) </param>
    def SetEndMeasure(manip: MatrixManip, measure: str) -> None:
        """
         Set end Measure
        """
        pass
    
    ##  Set Factor Value
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="factor"> (float) </param>
    def SetFactor(manip: MatrixManip, factor: float) -> None:
        """
         Set Factor Value
        """
        pass
    
    ##  Set Conversion Factor Value 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="factor"> (float) </param>
    def SetFactorConversion(manip: MatrixManip, factor: float) -> None:
        """
         Set Conversion Factor Value 
        """
        pass
    
    ##  Set Conversion Factor expression 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="exp"> (@link NXOpen.Expression NXOpen.Expression@endlink) </param>
    def SetFactorConversionExpression(manip: MatrixManip, exp: NXOpen.Expression) -> None:
        """
         Set Conversion Factor expression 
        """
        pass
    
    ##  Set Factor expression
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="exp"> (@link NXOpen.Expression NXOpen.Expression@endlink) </param>
    def SetFactorExpression(manip: MatrixManip, exp: NXOpen.Expression) -> None:
        """
         Set Factor expression
        """
        pass
    
    ##  Set filter lower bound
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="lowerBound"> (float) </param>
    def SetFilterLowerBound(manip: MatrixManip, lowerBound: float) -> None:
        """
         Set filter lower bound
        """
        pass
    
    ##  Set filter lower bound expression
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="exp"> (@link NXOpen.Expression NXOpen.Expression@endlink) </param>
    def SetFilterLowerBoundExpression(manip: MatrixManip, exp: NXOpen.Expression) -> None:
        """
         Set filter lower bound expression
        """
        pass
    
    ##  Set Filter Operation 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="filterOp"> (@link MatrixManip.FilterOperations NXOpen.CAE.AeroStructures.MatrixManip.FilterOperations@endlink) </param>
    def SetFilterOperation(manip: MatrixManip, filterOp: MatrixManip.FilterOperations) -> None:
        """
         Set Filter Operation 
        """
        pass
    
    ##  Set filter upper bound
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="upperBound"> (float) </param>
    def SetFilterUpperBound(manip: MatrixManip, upperBound: float) -> None:
        """
         Set filter upper bound
        """
        pass
    
    ##  Set filter upper bound expression
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="exp"> (@link NXOpen.Expression NXOpen.Expression@endlink) </param>
    def SetFilterUpperBoundExpression(manip: MatrixManip, exp: NXOpen.Expression) -> None:
        """
         Set filter upper bound expression
        """
        pass
    
    ##  Set Map Operation 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="mapOp"> (@link MatrixManip.MapOperations NXOpen.CAE.AeroStructures.MatrixManip.MapOperations@endlink) </param>
    def SetMapOperation(manip: MatrixManip, mapOp: MatrixManip.MapOperations) -> None:
        """
         Set Map Operation 
        """
        pass
    
    ##  Set Reduce Operation 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="reduceOp"> (@link MatrixManip.ReduceOperations NXOpen.CAE.AeroStructures.MatrixManip.ReduceOperations@endlink) </param>
    def SetReduceOperation(manip: MatrixManip, reduceOp: MatrixManip.ReduceOperations) -> None:
        """
         Set Reduce Operation 
        """
        pass
    
    ##  Set start Measure
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="measure"> (str) </param>
    def SetStartMeasure(manip: MatrixManip, measure: str) -> None:
        """
         Set start Measure
        """
        pass
    
import NXOpen
##   @brief  This is the MethodDescriptor.  
## 
##   
## 
##   <br>  Created in NX12.0.1  <br> 

class MethodDescriptor(NXOpen.TransientObject): 
    """ <summary> This is the MethodDescriptor. </summary> """


    ## Getter for property: (str) Author
    ##   the author   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return str
    @property
    def Author(self) -> str:
        """
        Getter for property: (str) Author
          the author   
            
         
        """
        pass
    
    ## Getter for property: (str) Category
    ##   the category   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return str
    @property
    def Category(self) -> str:
        """
        Getter for property: (str) Category
          the category   
            
         
        """
        pass
    
    ## Getter for property: (str) Description
    ##   the description   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return str
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
          the description   
            
         
        """
        pass
    
    ## Getter for property: (str) Id
    ##   the id   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return str
    @property
    def Id(self) -> str:
        """
        Getter for property: (str) Id
          the id   
            
         
        """
        pass
    
    ## Getter for property: (str) UiName
    ##   the ui name   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return str
    @property
    def UiName(self) -> str:
        """
        Getter for property: (str) UiName
          the ui name   
            
         
        """
        pass
    
    ## Getter for property: (int) Version
    ##   the version   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return int
    @property
    def Version(self) -> int:
        """
        Getter for property: (int) Version
          the version   
            
         
        """
        pass
    
    ##  Dispose the MethodDescriptor object 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(data: MethodDescriptor) -> None:
        """
         Dispose the MethodDescriptor object 
        """
        pass
    
    ##  Returns the diagram url as given in the method descriptor file 
    ##  @return diagram (str): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetDiagramUrl(data: MethodDescriptor) -> str:
        """
         Returns the diagram url as given in the method descriptor file 
         @return diagram (str): .
        """
        pass
    
    ##  Returns the absolute diagram url with any embedded variables expanded 
    ##  @return diagram (str): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetDiagramUrlExpanded(data: MethodDescriptor) -> str:
        """
         Returns the absolute diagram url with any embedded variables expanded 
         @return diagram (str): .
        """
        pass
    
    ##  Returns the doc url as given in the method descriptor file 
    ##  @return doc (str): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetDocUrl(data: MethodDescriptor) -> str:
        """
         Returns the doc url as given in the method descriptor file 
         @return doc (str): .
        """
        pass
    
    ##  Returns the absolute doc url with any embedded variables expanded 
    ##  @return doc (str): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetDocUrlExpanded(data: MethodDescriptor) -> str:
        """
         Returns the absolute doc url with any embedded variables expanded 
         @return doc (str): .
        """
        pass
    
    ##  Returns an array of all the failure mode ids 
    ##  @return fmArray (@link FailureMode List[NXOpen.CAE.AeroStructures.FailureMode]@endlink): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetFailureModeArray(data: MethodDescriptor) -> List[FailureMode]:
        """
         Returns an array of all the failure mode ids 
         @return fmArray (@link FailureMode List[NXOpen.CAE.AeroStructures.FailureMode]@endlink): .
        """
        pass
    
    ##  Returns the input descriptor 
    ##  @return input (@link ParameterDescriptor NXOpen.CAE.AeroStructures.ParameterDescriptor@endlink): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="id"> (str) </param>
    def GetInput(data: MethodDescriptor, id: str) -> ParameterDescriptor:
        """
         Returns the input descriptor 
         @return input (@link ParameterDescriptor NXOpen.CAE.AeroStructures.ParameterDescriptor@endlink): .
        """
        pass
    
    ##  Returns an array of all the input descriptors 
    ##  @return inputArray (@link ParameterDescriptor List[NXOpen.CAE.AeroStructures.ParameterDescriptor]@endlink): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetInputArray(data: MethodDescriptor) -> List[ParameterDescriptor]:
        """
         Returns an array of all the input descriptors 
         @return inputArray (@link ParameterDescriptor List[NXOpen.CAE.AeroStructures.ParameterDescriptor]@endlink): .
        """
        pass
    
    ##  Returns the number of failure modes 
    ##  @return number (int): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetNumFailureModes(data: MethodDescriptor) -> int:
        """
         Returns the number of failure modes 
         @return number (int): .
        """
        pass
    
    ##  Returns the number of inputs 
    ##  @return number (int): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetNumInputs(data: MethodDescriptor) -> int:
        """
         Returns the number of inputs 
         @return number (int): .
        """
        pass
    
    ##  Returns the number of outputs 
    ##  @return number (int): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetNumOutputs(data: MethodDescriptor) -> int:
        """
         Returns the number of outputs 
         @return number (int): .
        """
        pass
    
    ##  Returns the output descriptor 
    ##  @return output (@link ParameterDescriptor NXOpen.CAE.AeroStructures.ParameterDescriptor@endlink): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="id"> (str) </param>
    def GetOutput(data: MethodDescriptor, id: str) -> ParameterDescriptor:
        """
         Returns the output descriptor 
         @return output (@link ParameterDescriptor NXOpen.CAE.AeroStructures.ParameterDescriptor@endlink): .
        """
        pass
    
    ##  Returns an array of all the output descriptors 
    ##  @return outputArray (@link ParameterDescriptor List[NXOpen.CAE.AeroStructures.ParameterDescriptor]@endlink): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetOutputArray(data: MethodDescriptor) -> List[ParameterDescriptor]:
        """
         Returns an array of all the output descriptors 
         @return outputArray (@link ParameterDescriptor List[NXOpen.CAE.AeroStructures.ParameterDescriptor]@endlink): .
        """
        pass
    
    ##  Returns if the given failure mode is present 
    ##  @return present (bool): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="id"> (str) </param>
    def HasFailureMode(data: MethodDescriptor, id: str) -> bool:
        """
         Returns if the given failure mode is present 
         @return present (bool): .
        """
        pass
    
    ##  Returns if the given input is present 
    ##  @return present (bool): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="id"> (str) </param>
    def HasInput(data: MethodDescriptor, id: str) -> bool:
        """
         Returns if the given input is present 
         @return present (bool): .
        """
        pass
    
    ##  Returns if the given output is present 
    ##  @return present (bool): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="id"> (str) </param>
    def HasOutput(data: MethodDescriptor, id: str) -> bool:
        """
         Returns if the given output is present 
         @return present (bool): .
        """
        pass
    
import NXOpen
##  Represents a builder for creating multi @link NXOpen::CAE::AeroStructures::MarginCalculation NXOpen::CAE::AeroStructures::MarginCalculation@endlink .  <br> No support for KF  <br> 
## 
##   <br>  Created in NX1872.0.0  <br> 

class MultiMarginCalculationBuilder(MarginCalculationBuilder): 
    """ Represents a builder for creating multi <ja_class>NXOpen.CAE.AeroStructures.MarginCalculation</ja_class>. """


    ##  the ExtractionSite type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## PolygonFace</term><description> 
    ## </description> </item><item><term> 
    ## Group</term><description> 
    ## </description> </item><item><term> 
    ## Element</term><description> 
    ## </description> </item><item><term> 
    ## Node</term><description> 
    ## </description> </item><item><term> 
    ## Edge</term><description> 
    ## </description> </item><item><term> 
    ## Body</term><description> 
    ## </description> </item><item><term> 
    ## NotSet</term><description> 
    ## </description> </item><item><term> 
    ## Multiple</term><description> 
    ## </description> </item></list>
    class ExtractionSiteType(Enum):
        """
        Members Include: <PolygonFace> <Group> <Element> <Node> <Edge> <Body> <NotSet> <Multiple>
        """
        PolygonFace: int
        Group: int
        Element: int
        Node: int
        Edge: int
        Body: int
        NotSet: int
        Multiple: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MultiMarginCalculationBuilder.ExtractionSiteType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Set the list of extraction sites 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  Provide list of extraction sites over which the calculation will be propagated 
    def SetExtractionSites(builder: MultiMarginCalculationBuilder, extractionSiteType: MultiMarginCalculationBuilder.ExtractionSiteType, extractionSites: List[NXOpen.TaggedObject]) -> None:
        """
         Set the list of extraction sites 
        """
        pass
    
    ##  Set the list of sources for propagation 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  Provide list of sources over which the calculation will be propagated 
    def SetExtractionSources(builder: MultiMarginCalculationBuilder, sourceName: str, sourceType: BaseExtractionSource.TypeEnum, extractionSources: List[NXOpen.TaggedObject]) -> None:
        """
         Set the list of sources for propagation 
        """
        pass
    
import NXOpen
##   @brief  This is the Parameter Descriptor  
## 
##   
## 
##   <br>  Created in NX12.0.1  <br> 

class ParameterDescriptor(NXOpen.TransientObject): 
    """ <summary> This is the Parameter Descriptor </summary> """


    ##  the Dimensionality 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ## </description> </item><item><term> 
    ## Failuremode</term><description> 
    ## </description> </item><item><term> 
    ## Loadcase</term><description> 
    ## </description> </item><item><term> 
    ## FmLc</term><description> 
    ## </description> </item></list>
    class DimensionalityType(Enum):
        """
        Members Include: <NotSet> <Failuremode> <Loadcase> <FmLc>
        """
        NotSet: int
        Failuremode: int
        Loadcase: int
        FmLc: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ParameterDescriptor.DimensionalityType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the Parameter Type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Boolean</term><description> 
    ## </description> </item><item><term> 
    ## Integer</term><description> 
    ## </description> </item><item><term> 
    ## Scalar</term><description> 
    ## </description> </item><item><term> 
    ## Text</term><description> 
    ## </description> </item><item><term> 
    ## Load</term><description> 
    ## </description> </item><item><term> 
    ## Table</term><description> 
    ## </description> </item><item><term> 
    ## Size</term><description> 
    ## </description> </item><item><term> 
    ## Laminate</term><description> 
    ## </description> </item><item><term> 
    ## File</term><description> 
    ## </description> </item><item><term> 
    ## Unknown</term><description> 
    ## </description> </item></list>
    class ParameterType(Enum):
        """
        Members Include: <Boolean> <Integer> <Scalar> <Text> <Load> <Table> <Size> <Laminate> <File> <Unknown>
        """
        Boolean: int
        Integer: int
        Scalar: int
        Text: int
        Load: int
        Table: int
        Size: int
        Laminate: int
        File: int
        Unknown: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ParameterDescriptor.ParameterType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link ParameterDescriptor.DimensionalityType NXOpen.CAE.AeroStructures.ParameterDescriptor.DimensionalityType@endlink) Dimensionality
    ##   the Dimensionality   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return ParameterDescriptor.DimensionalityType
    @property
    def Dimensionality(self) -> ParameterDescriptor.DimensionalityType:
        """
        Getter for property: (@link ParameterDescriptor.DimensionalityType NXOpen.CAE.AeroStructures.ParameterDescriptor.DimensionalityType@endlink) Dimensionality
          the Dimensionality   
            
         
        """
        pass
    
    ## Getter for property: (str) Id
    ##   the id   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return str
    @property
    def Id(self) -> str:
        """
        Getter for property: (str) Id
          the id   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsOptional
    ##   the IsOptional   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return bool
    @property
    def IsOptional(self) -> bool:
        """
        Getter for property: (bool) IsOptional
          the IsOptional   
            
         
        """
        pass
    
    ## Getter for property: (@link ParameterDescriptor.ParameterType NXOpen.CAE.AeroStructures.ParameterDescriptor.ParameterType@endlink) ParamType
    ##   the ParameterType   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return ParameterDescriptor.ParameterType
    @property
    def ParamType(self) -> ParameterDescriptor.ParameterType:
        """
        Getter for property: (@link ParameterDescriptor.ParameterType NXOpen.CAE.AeroStructures.ParameterDescriptor.ParameterType@endlink) ParamType
          the ParameterType   
            
         
        """
        pass
    
    ## Getter for property: (str) UiName
    ##   the UI name   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return str
    @property
    def UiName(self) -> str:
        """
        Getter for property: (str) UiName
          the UI name   
            
         
        """
        pass
    
    ##  Dispose 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(data: ParameterDescriptor) -> None:
        """
         Dispose 
        """
        pass
    
##  Physical property source class.  <br> To create a new instance of this class, use @link NXOpen::CAE::AeroStructures::ExtractionSourceSet::CreatePhysicalPropertySource  NXOpen::CAE::AeroStructures::ExtractionSourceSet::CreatePhysicalPropertySource @endlink  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class PhysicalPropertySource(BaseExtractionSource): 
    """ Physical property source class. """
    pass


import NXOpen.CAE
##   @brief  Represents a property table  
## 
##    <br> This is a sub object  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class PropTable(NXOpen.CAE.PropertyTable): 
    """ <summary> Represents a property table </summary> """


    ##  Property Types 
    ##  BASE_PROPERTY_TABLE_margin_property_type_unknown               
    class MarginPropertyType(Enum):
        """
        Members Include: <Unknown> <String> <Boolean> <Integer> <Double> <FieldWrapper> <ScalarFieldWrapper> <CoordinateSystem> <DoubleArray> <IntegerArray> <PhysicalMaterial> <Matrix> <ScalarTable> <Text> <FieldExpression> <VectorFieldWrapper> <Vector> <Reference> <Point> <DateTime> <NamedPropertyTableArray> <SetManager> <NamedPropertyTable> <Axis> <CaeSection> <SectionOrientation> <SectionOffset> <ReferenceArray> <StringArray> <Loadextraction> <Laminate> <Description> <Table>
        """
        Unknown: int
        String: int
        Boolean: int
        Integer: int
        Double: int
        FieldWrapper: int
        ScalarFieldWrapper: int
        CoordinateSystem: int
        DoubleArray: int
        IntegerArray: int
        PhysicalMaterial: int
        Matrix: int
        ScalarTable: int
        Text: int
        FieldExpression: int
        VectorFieldWrapper: int
        Vector: int
        Reference: int
        Point: int
        DateTime: int
        NamedPropertyTableArray: int
        SetManager: int
        NamedPropertyTable: int
        Axis: int
        CaeSection: int
        SectionOrientation: int
        SectionOffset: int
        ReferenceArray: int
        StringArray: int
        Loadextraction: int
        Laminate: int
        Description: int
        Table: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PropTable.MarginPropertyType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Returns the description property 
    ##  @return property_value (@link DescriptionValue NXOpen.CAE.AeroStructures.DescriptionValue@endlink):  value of the property .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  name of the property 
    def GetDescriptionPropertyValue(property_table: PropTable, property_name: str) -> DescriptionValue:
        """
         Returns the description property 
         @return property_value (@link DescriptionValue NXOpen.CAE.AeroStructures.DescriptionValue@endlink):  value of the property .
        """
        pass
    
    ##  Returns the load laminate property 
    ##  @return property_value (@link LaminateValue NXOpen.CAE.AeroStructures.LaminateValue@endlink):  value of the property .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  name of the property 
    def GetLaminatePropertyValue(property_table: PropTable, property_name: str) -> LaminateValue:
        """
         Returns the load laminate property 
         @return property_value (@link LaminateValue NXOpen.CAE.AeroStructures.LaminateValue@endlink):  value of the property .
        """
        pass
    
    ##  Returns the load extraction property 
    ##  @return property_value (@link LoadExtractionValue NXOpen.CAE.AeroStructures.LoadExtractionValue@endlink):  value of the property .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  name of the property 
    def GetLoadExtractionPropertyValue(property_table: PropTable, property_name: str) -> LoadExtractionValue:
        """
         Returns the load extraction property 
         @return property_value (@link LoadExtractionValue NXOpen.CAE.AeroStructures.LoadExtractionValue@endlink):  value of the property .
        """
        pass
    
    ##  Returns the type of the property 
    ##  @return property_type (@link PropTable.MarginPropertyType NXOpen.CAE.AeroStructures.PropTable.MarginPropertyType@endlink):  type of the property .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  name of the property 
    def GetMarginPropertyType(property_table: PropTable, property_name: str) -> PropTable.MarginPropertyType:
        """
         Returns the type of the property 
         @return property_type (@link PropTable.MarginPropertyType NXOpen.CAE.AeroStructures.PropTable.MarginPropertyType@endlink):  type of the property .
        """
        pass
    
    ##  Returns the table parameter value 
    ##  @return property_value (@link TableParamValue NXOpen.CAE.AeroStructures.TableParamValue@endlink):  value of the property .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  name of the property 
    def GetTableParamPropertyValue(property_table: PropTable, property_name: str) -> TableParamValue:
        """
         Returns the table parameter value 
         @return property_value (@link TableParamValue NXOpen.CAE.AeroStructures.TableParamValue@endlink):  value of the property .
        """
        pass
    
    ##  Used to set a description value
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  name of the property 
    def SetDescriptionPropertyValue(property_table: PropTable, property_name: str, property_value: DescriptionValue) -> None:
        """
         Used to set a description value
        """
        pass
    
    ##  Sets the file reference value of the property
    ##             
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    ##  name of the property 
    def SetFilePropertyValue(property_table: PropTable, property_name: str, property_value: str) -> None:
        """
         Sets the file reference value of the property
                    
        """
        pass
    
    ##  Used to set a laminate value
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  name of the property 
    def SetLaminatePropertyValue(property_table: PropTable, property_name: str, property_value: LaminateValue) -> None:
        """
         Used to set a laminate value
        """
        pass
    
    ##  Used to set a load extraction value
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  name of the property 
    def SetLoadExtractionPropertyValue(property_table: PropTable, property_name: str, property_value: LoadExtractionValue) -> None:
        """
         Used to set a load extraction value
        """
        pass
    
    ##  Used to set a table parameter value
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  name of the property 
    def SetTableParamPropertyValue(property_table: PropTable, property_name: str, property_value: TableParamValue) -> None:
        """
         Used to set a table parameter value
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::CAE::AeroStructures::ScriptCallbackData NXOpen::CAE::AeroStructures::ScriptCallbackData@endlink .  <br> No support for KF  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class ScriptCallbackData(NXOpen.NXObject): 
    """ Represents a <ja_class>NXOpen.CAE.AeroStructures.ScriptCallbackData</ja_class>. """


    ##  Returns the method ID. 
    ##  @return methodID (str):  .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetMethodId(context: ScriptCallbackData) -> str:
        """
         Returns the method ID. 
         @return methodID (str):  .
        """
        pass
    
    ##  Returns the module path. 
    ##  @return modulePath (str):  .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetModulePath(context: ScriptCallbackData) -> str:
        """
         Returns the module path. 
         @return modulePath (str):  .
        """
        pass
    
    ##  Returns the tagged object used by the script callback.
    ##  @return taggedObject (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink):  .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetObject(context: ScriptCallbackData) -> NXOpen.TaggedObject:
        """
         Returns the tagged object used by the script callback.
         @return taggedObject (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink):  .
        """
        pass
    
    ##  Returns the script method name. 
    ##  @return scriptMethodName (str):  .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetScriptMethodName(context: ScriptCallbackData) -> str:
        """
         Returns the script method name. 
         @return scriptMethodName (str):  .
        """
        pass
    
    ##  Set the success of the script callback execution. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetSuccess(context: ScriptCallbackData, success: bool) -> None:
        """
         Set the success of the script callback execution. 
        """
        pass
    
##  Section source class.  <br> To create a new instance of this class, use @link NXOpen::CAE::AeroStructures::ExtractionSourceSet::CreateSectionSource  NXOpen::CAE::AeroStructures::ExtractionSourceSet::CreateSectionSource @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class SectionSource(BaseExtractionSource): 
    """ Section source class. """
    pass


import NXOpen
##  Represents options for solve  <br> Use @link CAE::AeroStructures::BaseSolution::SolveOptions CAE::AeroStructures::BaseSolution::SolveOptions@endlink  to get the instance of this class.  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class SolveOptions(NXOpen.Object): 
    """ Represents options for solve """


    ## Getter for property: (bool) StoreLoadCaseInfo
    ##   the option for load case specific outputs in the log (default is on)   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def StoreLoadCaseInfo(self) -> bool:
        """
        Getter for property: (bool) StoreLoadCaseInfo
          the option for load case specific outputs in the log (default is on)   
            
         
        """
        pass
    
    ## Setter for property: (bool) StoreLoadCaseInfo

    ##   the option for load case specific outputs in the log (default is on)   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @StoreLoadCaseInfo.setter
    def StoreLoadCaseInfo(self, store: bool):
        """
        Setter for property: (bool) StoreLoadCaseInfo
          the option for load case specific outputs in the log (default is on)   
            
         
        """
        pass
    
import NXOpen
##   @brief  This is the TableParameter  
## 
##    <br> No support for KF  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class TableParameter(NXOpen.NXObject): 
    """ <summary> This is the TableParameter </summary> """


    ## Getter for property: (int) Size
    ##   the size of the table   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def Size(self) -> int:
        """
        Getter for property: (int) Size
          the size of the table   
            
         
        """
        pass
    
    ## Getter for property: (int) SizeOffset
    ##   the size offset   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def SizeOffset(self) -> int:
        """
        Getter for property: (int) SizeOffset
          the size offset   
            
         
        """
        pass
    
    ## Getter for property: (str) SizeParameter
    ##   the size parameter   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def SizeParameter(self) -> str:
        """
        Getter for property: (str) SizeParameter
          the size parameter   
            
         
        """
        pass
    
    ##  Get the values of a Boolean column 
    ##  @return value (List[bool]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="columnId"> (str) </param>
    def GetBooleanValues(context: TableParameter, columnId: str) -> List[bool]:
        """
         Get the values of a Boolean column 
         @return value (List[bool]): .
        """
        pass
    
    ##  Returns a list of all column IDs 
    ##  @return columnIds (List[str]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetColumnNames(context: TableParameter) -> List[str]:
        """
         Returns a list of all column IDs 
         @return columnIds (List[str]): .
        """
        pass
    
    ##  Returns the parameter type for a column 
    ##  @return type (@link ParameterDescriptor.ParameterType NXOpen.CAE.AeroStructures.ParameterDescriptor.ParameterType@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="columnName"> (str) </param>
    def GetColumnType(context: TableParameter, columnName: str) -> ParameterDescriptor.ParameterType:
        """
         Returns the parameter type for a column 
         @return type (@link ParameterDescriptor.ParameterType NXOpen.CAE.AeroStructures.ParameterDescriptor.ParameterType@endlink): .
        """
        pass
    
    ##  Returns the UI names for a given list of column ids, in the same order 
    ##  @return columnUiNames (List[str]): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="columnIds"> (List[str]) </param>
    def GetColumnUiNames(context: TableParameter, columnIds: List[str]) -> List[str]:
        """
         Returns the UI names for a given list of column ids, in the same order 
         @return columnUiNames (List[str]): .
        """
        pass
    
    ##  Get the values of an integer column 
    ##  @return value (List[int]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="columnId"> (str) </param>
    def GetIntegerValues(context: TableParameter, columnId: str) -> List[int]:
        """
         Get the values of an integer column 
         @return value (List[int]): .
        """
        pass
    
    ##  Get the values of a laminate column 
    ##  @return value (@link Laminate List[NXOpen.CAE.AeroStructures.Laminate]@endlink):  .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="columnId"> (str) </param>
    def GetLaminateValues(context: TableParameter, columnId: str) -> List[Laminate]:
        """
         Get the values of a laminate column 
         @return value (@link Laminate List[NXOpen.CAE.AeroStructures.Laminate]@endlink):  .
        """
        pass
    
    ##  Get the measure name of a scalar column
    ##                 Returns "Unitless" for unitless case
    ##               
    ##  @return measure (str): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="columnId"> (str) </param>
    def GetMeasure(context: TableParameter, columnId: str) -> str:
        """
         Get the measure name of a scalar column
                        Returns "Unitless" for unitless case
                      
         @return measure (str): .
        """
        pass
    
    ##  Get the values of a scalar column ("Not a number" values are returned as system NAN)
    ## These values are expressed in default unit type that can be retrieved by calling @link CAE::AeroStructures::TableParameter::GetUnitType CAE::AeroStructures::TableParameter::GetUnitType@endlink  
    ##  @return value (List[float]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## <param name="context"> (@link TableParameter NXOpen.CAE.AeroStructures.TableParameter@endlink) </param>
    ## <param name="columnId"> (str) </param>
    @overload
    def GetScalarValues(self, context: TableParameter, columnId: str) -> List[float]:
        """
         Get the values of a scalar column ("Not a number" values are returned as system NAN)
        These values are expressed in default unit type that can be retrieved by calling @link CAE::AeroStructures::TableParameter::GetUnitType CAE::AeroStructures::TableParameter::GetUnitType@endlink  
         @return value (List[float]): .
        """
        pass
    
    ##  Get the values of a scalar column converted in a specified unit ("Not a number" values are returned as system NAN)
    ##  @return value (List[float]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## <param name="context"> (@link TableParameter NXOpen.CAE.AeroStructures.TableParameter@endlink) </param>
    ## <param name="columnId"> (str) </param>
    ## <param name="unit_type"> (@link NXOpen.Unit NXOpen.Unit@endlink) </param>
    @overload
    def GetScalarValues(self, context: TableParameter, columnId: str, unit_type: NXOpen.Unit) -> List[float]:
        """
         Get the values of a scalar column converted in a specified unit ("Not a number" values are returned as system NAN)
         @return value (List[float]): .
        """
        pass
    
    ##  Get the values of a string column 
    ##  @return value (List[str]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="columnId"> (str) </param>
    def GetStringValues(context: TableParameter, columnId: str) -> List[str]:
        """
         Get the values of a string column 
         @return value (List[str]): .
        """
        pass
    
    ##  Get the unit type of a scalar column
    ##               * Returns null if the column is unitless
    ##               
    ##  @return unit_type (@link NXOpen.Unit NXOpen.Unit@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="columnId"> (str) </param>
    def GetUnitType(context: TableParameter, columnId: str) -> NXOpen.Unit:
        """
         Get the unit type of a scalar column
                      * Returns null if the column is unitless
                      
         @return unit_type (@link NXOpen.Unit NXOpen.Unit@endlink): .
        """
        pass
    
import NXOpen
##   @brief  Represents a proper table parameter value  
## 
##    <br> No support for KF  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class TableParamValue(NXOpen.NXObject): 
    """ <summary> Represents a proper table parameter value </summary> """


    ##  Changes the length of the columns
    ##             
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="rowId"> (int) </param>
    def ChangeColumnsLength(value: TableParamValue, rowId: int) -> None:
        """
         Changes the length of the columns
                    
        """
        pass
    
    ##  Gets the expression from expression column at a certain row 
    ##  @return expression (@link NXOpen.Expression NXOpen.Expression@endlink):  the expression at columnId,rowId.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="columnId"> (str) </param>
    ## <param name="rowId"> (int) </param>
    def GetExpression(value: TableParamValue, columnId: str, rowId: int) -> NXOpen.Expression:
        """
         Gets the expression from expression column at a certain row 
         @return expression (@link NXOpen.Expression NXOpen.Expression@endlink):  the expression at columnId,rowId.
        """
        pass
    
    ##  Gets the laminate query from a laminate column at a certain row 
    ##                 If no laminate exists for that row or the row is outside the current table size a new laminate is created and returned.
    ##                 This new laminate is registered with the laminate query manager of margin calculation owning the property table
    ##                 It is inteded to be stored in a laminate column using @link TableParamValue::UpdateLaminateColumnValue TableParamValue::UpdateLaminateColumnValue@endlink 
    ##             
    ##  @return laminateQuery (@link LaminateQuery NXOpen.CAE.AeroStructures.LaminateQuery@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  property table required to create laminate query object 
    def GetLaminate(value: TableParamValue, columnId: str, rowId: int, propTable: NXOpen.TaggedObject) -> LaminateQuery:
        """
         Gets the laminate query from a laminate column at a certain row 
                        If no laminate exists for that row or the row is outside the current table size a new laminate is created and returned.
                        This new laminate is registered with the laminate query manager of margin calculation owning the property table
                        It is inteded to be stored in a laminate column using @link TableParamValue::UpdateLaminateColumnValue TableParamValue::UpdateLaminateColumnValue@endlink 
                    
         @return laminateQuery (@link LaminateQuery NXOpen.CAE.AeroStructures.LaminateQuery@endlink): .
        """
        pass
    
    ##  Sets a bool column value list 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  the list of column values 
    def SetBoolColumnValue(value: TableParamValue, columnId: str, columnValues: List[bool]) -> None:
        """
         Sets a bool column value list 
        """
        pass
    
    ##  Sets a int column value list 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  the list of column values 
    def SetIntColumnValue(value: TableParamValue, columnId: str, columnValues: List[int]) -> None:
        """
         Sets a int column value list 
        """
        pass
    
    ##  Sets the validated status 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="isValidated"> (bool) </param>
    def SetIsValidated(value: TableParamValue, isValidated: bool) -> None:
        """
         Sets the validated status 
        """
        pass
    
    ##  Sets a scalar column value list 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Unit in which the column values are expressed. 
    def SetScalarColumnValue(value: TableParamValue, columnId: str, unit: NXOpen.Unit, columnValues: List[float]) -> None:
        """
         Sets a scalar column value list 
        """
        pass
    
    ##  Sets a string column value list 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  the list of column values 
    def SetStringColumnValue(value: TableParamValue, columnId: str, columnValues: List[str]) -> None:
        """
         Sets a string column value list 
        """
        pass
    
    ##  Update an expression column value list with the expression array passed as input
    ##                 Adjust its length and delete previous expressions if necessary 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Unit of the expressions. 
    def UpdateExpressionColumnValue(value: TableParamValue, columnId: str, unit: NXOpen.Unit, columnValues: List[NXOpen.Expression]) -> None:
        """
         Update an expression column value list with the expression array passed as input
                        Adjust its length and delete previous expressions if necessary 
        """
        pass
    
    ##  Update a laminate column value list with the laminate array passed as input
    ##                 Adjust its length and delete previous laminates if necessary 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  the list of column values 
    def UpdateLaminateColumnValue(value: TableParamValue, columnId: str, columnValues: List[LaminateQuery]) -> None:
        """
         Update a laminate column value list with the laminate array passed as input
                        Adjust its length and delete previous laminates if necessary 
        """
        pass
    
import NXOpen
import NXOpen.CAE
##   @brief  This is the User LoadExtraction class  
## 
##    <br> No support for KF  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class UserLoadExtraction(LoadExtractionStrategy): 
    """ <summary> This is the User LoadExtraction class </summary> """


    ##  Type of Selection
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Model</term><description> 
    ## </description> </item><item><term> 
    ## Group</term><description> 
    ## </description> </item><item><term> 
    ## ExtractionSource</term><description> 
    ## </description> </item></list>
    class PickMethod(Enum):
        """
        Members Include: <Model> <Group> <ExtractionSource>
        """
        Model: int
        Group: int
        ExtractionSource: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> UserLoadExtraction.PickMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Target Entity type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## EntireModel</term><description> 
    ## </description> </item><item><term> 
    ## Nodes</term><description> 
    ## </description> </item><item><term> 
    ## Elements</term><description> 
    ## </description> </item><item><term> 
    ## Points</term><description> 
    ## </description> </item><item><term> 
    ## Edges</term><description> 
    ## </description> </item><item><term> 
    ## Faces</term><description> 
    ## </description> </item><item><term> 
    ## Bodies</term><description> 
    ## </description> </item><item><term> 
    ## NotSet</term><description> 
    ## </description> </item></list>
    class TargetEntity(Enum):
        """
        Members Include: <EntireModel> <Nodes> <Elements> <Points> <Edges> <Faces> <Bodies> <NotSet>
        """
        EntireModel: int
        Nodes: int
        Elements: int
        Points: int
        Edges: int
        Faces: int
        Bodies: int
        NotSet: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> UserLoadExtraction.TargetEntity:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) ExtractionSourceName
    ##   the extraction source name  
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def ExtractionSourceName(self) -> str:
        """
        Getter for property: (str) ExtractionSourceName
          the extraction source name  
            
         
        """
        pass
    
    ## Setter for property: (str) ExtractionSourceName

    ##   the extraction source name  
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @ExtractionSourceName.setter
    def ExtractionSourceName(self, name: str):
        """
        Setter for property: (str) ExtractionSourceName
          the extraction source name  
            
         
        """
        pass
    
    ##  Get Coordinate System 
    ##  @return csys (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetCoordinateSystem(loadExt: UserLoadExtraction) -> NXOpen.CoordinateSystem:
        """
         Get Coordinate System 
         @return csys (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink): .
        """
        pass
    
    ##  Get External Group 
    ##  @return group (@link NXOpen.CAE.CaeGroup NXOpen.CAE.CaeGroup@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetExternalGroup(loadExt: UserLoadExtraction) -> NXOpen.CAE.CaeGroup:
        """
         Get External Group 
         @return group (@link NXOpen.CAE.CaeGroup NXOpen.CAE.CaeGroup@endlink): .
        """
        pass
    
    ##  Get the extraction source 
    ##  @return source (@link BaseExtractionSource NXOpen.CAE.AeroStructures.BaseExtractionSource@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetExtractionSource(loadExt: UserLoadExtraction) -> BaseExtractionSource:
        """
         Get the extraction source 
         @return source (@link BaseExtractionSource NXOpen.CAE.AeroStructures.BaseExtractionSource@endlink): .
        """
        pass
    
    ##  Get Matrix Manip 
    ##  @return manip (@link MatrixManip NXOpen.CAE.AeroStructures.MatrixManip@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetMatrixManip(loadExt: UserLoadExtraction) -> MatrixManip:
        """
         Get Matrix Manip 
         @return manip (@link MatrixManip NXOpen.CAE.AeroStructures.MatrixManip@endlink): .
        """
        pass
    
    ##  Get Pick Method 
    ##  @return pickMethod (@link UserLoadExtraction.PickMethod NXOpen.CAE.AeroStructures.UserLoadExtraction.PickMethod@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetPickMethod(loadExt: UserLoadExtraction) -> UserLoadExtraction.PickMethod:
        """
         Get Pick Method 
         @return pickMethod (@link UserLoadExtraction.PickMethod NXOpen.CAE.AeroStructures.UserLoadExtraction.PickMethod@endlink): .
        """
        pass
    
    ##  Get Result Parameters 
    ##  @return parameters (@link NXOpen.CAE.ResultParameters NXOpen.CAE.ResultParameters@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetResultParameters(loadExt: UserLoadExtraction) -> NXOpen.CAE.ResultParameters:
        """
         Get Result Parameters 
         @return parameters (@link NXOpen.CAE.ResultParameters NXOpen.CAE.ResultParameters@endlink): .
        """
        pass
    
    ##  Get Selected Entities 
    ##  @return entities (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink):  .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetSelectedEntities(loadExt: UserLoadExtraction) -> List[NXOpen.TaggedObject]:
        """
         Get Selected Entities 
         @return entities (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink):  .
        """
        pass
    
    ##  Get Entities Type 
    ##  @return target (@link UserLoadExtraction.TargetEntity NXOpen.CAE.AeroStructures.UserLoadExtraction.TargetEntity@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetTargetEntity(loadExt: UserLoadExtraction) -> UserLoadExtraction.TargetEntity:
        """
         Get Entities Type 
         @return target (@link UserLoadExtraction.TargetEntity NXOpen.CAE.AeroStructures.UserLoadExtraction.TargetEntity@endlink): .
        """
        pass
    
    ##  Set Coordinate System 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="csys"> (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) </param>
    def SetCoordinateSystem(loadExt: UserLoadExtraction, csys: NXOpen.CoordinateSystem) -> None:
        """
         Set Coordinate System 
        """
        pass
    
    ##  Set External Group 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="group"> (@link NXOpen.CAE.CaeGroup NXOpen.CAE.CaeGroup@endlink) </param>
    def SetExternalGroup(loadExt: UserLoadExtraction, group: NXOpen.CAE.CaeGroup) -> None:
        """
         Set External Group 
        """
        pass
    
    ##  Set Matrix Manip 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="manip"> (@link MatrixManip NXOpen.CAE.AeroStructures.MatrixManip@endlink) </param>
    def SetMatrixManip(loadExt: UserLoadExtraction, manip: MatrixManip) -> None:
        """
         Set Matrix Manip 
        """
        pass
    
    ##  Set Pick Method 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="pickMethod"> (@link UserLoadExtraction.PickMethod NXOpen.CAE.AeroStructures.UserLoadExtraction.PickMethod@endlink) </param>
    def SetPickMethod(loadExt: UserLoadExtraction, pickMethod: UserLoadExtraction.PickMethod) -> None:
        """
         Set Pick Method 
        """
        pass
    
    ##  Set Result Parameters 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="parameters"> (@link NXOpen.CAE.ResultParameters NXOpen.CAE.ResultParameters@endlink) </param>
    def SetResultParameters(loadExt: UserLoadExtraction, parameters: NXOpen.CAE.ResultParameters) -> None:
        """
         Set Result Parameters 
        """
        pass
    
    ##  Set Selected Entities 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  
    def SetSelectedEntities(loadExt: UserLoadExtraction, entities: List[NXOpen.TaggedObject]) -> None:
        """
         Set Selected Entities 
        """
        pass
    
    ##  Set Entities Type 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="target"> (@link UserLoadExtraction.TargetEntity NXOpen.CAE.AeroStructures.UserLoadExtraction.TargetEntity@endlink) </param>
    def SetTargetEntity(loadExt: UserLoadExtraction, target: UserLoadExtraction.TargetEntity) -> None:
        """
         Set Entities Type 
        """
        pass
    
import NXOpen
##  Contains universal aerostructure utility methods  <br> To obtain an instance use @link NXOpen::CAE::AeroStructures::Utils NXOpen::CAE::AeroStructures::Utils@endlink .  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class Utils(NXOpen.Object): 
    """ Contains universal aerostructure utility methods """


    ##  Returns template paths from the repository regarding a template name 
    ##  @return paths (List[str]): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ##  The template name without ext 
    @staticmethod
    def GetTemplatePaths(templateName: str) -> List[str]:
        """
         Returns template paths from the repository regarding a template name 
         @return paths (List[str]): .
        """
        pass
    
## @package NXOpen.CAE.AeroStructures
## Classes, Enums and Structs under NXOpen.CAE.AeroStructures namespace

##  @link BaseCalculationCalculationStatus NXOpen.CAE.AeroStructures.BaseCalculationCalculationStatus @endlink is an alias for @link BaseCalculation.CalculationStatus NXOpen.CAE.AeroStructures.BaseCalculation.CalculationStatus@endlink
BaseCalculationCalculationStatus = BaseCalculation.CalculationStatus


##  @link BaseExtractionSourceTypeEnum NXOpen.CAE.AeroStructures.BaseExtractionSourceTypeEnum @endlink is an alias for @link BaseExtractionSource.TypeEnum NXOpen.CAE.AeroStructures.BaseExtractionSource.TypeEnum@endlink
BaseExtractionSourceTypeEnum = BaseExtractionSource.TypeEnum


##  @link CalculationLogLineMessageType NXOpen.CAE.AeroStructures.CalculationLogLineMessageType @endlink is an alias for @link CalculationLogLine.MessageType NXOpen.CAE.AeroStructures.CalculationLogLine.MessageType@endlink
CalculationLogLineMessageType = CalculationLogLine.MessageType


##  @link ExpressionResultType NXOpen.CAE.AeroStructures.ExpressionResultType @endlink is an alias for @link ExpressionResult.Type NXOpen.CAE.AeroStructures.ExpressionResult.Type@endlink
ExpressionResultType = ExpressionResult.Type


##  @link FreeBodyLoadExtractionComponent NXOpen.CAE.AeroStructures.FreeBodyLoadExtractionComponent @endlink is an alias for @link FreeBodyLoadExtraction.Component NXOpen.CAE.AeroStructures.FreeBodyLoadExtraction.Component@endlink
FreeBodyLoadExtractionComponent = FreeBodyLoadExtraction.Component


##  @link FreeBodyLoadExtractionResult NXOpen.CAE.AeroStructures.FreeBodyLoadExtractionResult @endlink is an alias for @link FreeBodyLoadExtraction.Result NXOpen.CAE.AeroStructures.FreeBodyLoadExtraction.Result@endlink
FreeBodyLoadExtractionResult = FreeBodyLoadExtraction.Result


##  @link LaminateQueryAngleDefinitionTypeEnum NXOpen.CAE.AeroStructures.LaminateQueryAngleDefinitionTypeEnum @endlink is an alias for @link LaminateQuery.AngleDefinitionTypeEnum NXOpen.CAE.AeroStructures.LaminateQuery.AngleDefinitionTypeEnum@endlink
LaminateQueryAngleDefinitionTypeEnum = LaminateQuery.AngleDefinitionTypeEnum


##  @link LaminateQueryReferenceEntityTypeEnum NXOpen.CAE.AeroStructures.LaminateQueryReferenceEntityTypeEnum @endlink is an alias for @link LaminateQuery.ReferenceEntityTypeEnum NXOpen.CAE.AeroStructures.LaminateQuery.ReferenceEntityTypeEnum@endlink
LaminateQueryReferenceEntityTypeEnum = LaminateQuery.ReferenceEntityTypeEnum


##  @link LaminateLamRefLoc NXOpen.CAE.AeroStructures.LaminateLamRefLoc @endlink is an alias for @link Laminate.LamRefLoc NXOpen.CAE.AeroStructures.Laminate.LamRefLoc@endlink
LaminateLamRefLoc = Laminate.LamRefLoc


##  @link LoadCaseLoadCaseType NXOpen.CAE.AeroStructures.LoadCaseLoadCaseType @endlink is an alias for @link LoadCase.LoadCaseType NXOpen.CAE.AeroStructures.LoadCase.LoadCaseType@endlink
LoadCaseLoadCaseType = LoadCase.LoadCaseType


##  @link LoadExtractionValueActiveStrategy NXOpen.CAE.AeroStructures.LoadExtractionValueActiveStrategy @endlink is an alias for @link LoadExtractionValue.ActiveStrategy NXOpen.CAE.AeroStructures.LoadExtractionValue.ActiveStrategy@endlink
LoadExtractionValueActiveStrategy = LoadExtractionValue.ActiveStrategy


##  @link MarginResultTableDataProviderColumnType NXOpen.CAE.AeroStructures.MarginResultTableDataProviderColumnType @endlink is an alias for @link MarginResultTableDataProvider.ColumnType NXOpen.CAE.AeroStructures.MarginResultTableDataProvider.ColumnType@endlink
MarginResultTableDataProviderColumnType = MarginResultTableDataProvider.ColumnType


##  @link MarginResultTableRowFilterNumericComparisonOperator NXOpen.CAE.AeroStructures.MarginResultTableRowFilterNumericComparisonOperator @endlink is an alias for @link MarginResultTableRowFilter.NumericComparisonOperator NXOpen.CAE.AeroStructures.MarginResultTableRowFilter.NumericComparisonOperator@endlink
MarginResultTableRowFilterNumericComparisonOperator = MarginResultTableRowFilter.NumericComparisonOperator


##  @link MarginResultTableRowFilterStringComparisonOperator NXOpen.CAE.AeroStructures.MarginResultTableRowFilterStringComparisonOperator @endlink is an alias for @link MarginResultTableRowFilter.StringComparisonOperator NXOpen.CAE.AeroStructures.MarginResultTableRowFilter.StringComparisonOperator@endlink
MarginResultTableRowFilterStringComparisonOperator = MarginResultTableRowFilter.StringComparisonOperator


##  @link MatrixManipFilterOperations NXOpen.CAE.AeroStructures.MatrixManipFilterOperations @endlink is an alias for @link MatrixManip.FilterOperations NXOpen.CAE.AeroStructures.MatrixManip.FilterOperations@endlink
MatrixManipFilterOperations = MatrixManip.FilterOperations


##  @link MatrixManipMapOperations NXOpen.CAE.AeroStructures.MatrixManipMapOperations @endlink is an alias for @link MatrixManip.MapOperations NXOpen.CAE.AeroStructures.MatrixManip.MapOperations@endlink
MatrixManipMapOperations = MatrixManip.MapOperations


##  @link MatrixManipReduceOperations NXOpen.CAE.AeroStructures.MatrixManipReduceOperations @endlink is an alias for @link MatrixManip.ReduceOperations NXOpen.CAE.AeroStructures.MatrixManip.ReduceOperations@endlink
MatrixManipReduceOperations = MatrixManip.ReduceOperations


##  @link MultiMarginCalculationBuilderExtractionSiteType NXOpen.CAE.AeroStructures.MultiMarginCalculationBuilderExtractionSiteType @endlink is an alias for @link MultiMarginCalculationBuilder.ExtractionSiteType NXOpen.CAE.AeroStructures.MultiMarginCalculationBuilder.ExtractionSiteType@endlink
MultiMarginCalculationBuilderExtractionSiteType = MultiMarginCalculationBuilder.ExtractionSiteType


##  @link ParameterDescriptorDimensionalityType NXOpen.CAE.AeroStructures.ParameterDescriptorDimensionalityType @endlink is an alias for @link ParameterDescriptor.DimensionalityType NXOpen.CAE.AeroStructures.ParameterDescriptor.DimensionalityType@endlink
ParameterDescriptorDimensionalityType = ParameterDescriptor.DimensionalityType


##  @link ParameterDescriptorParameterType NXOpen.CAE.AeroStructures.ParameterDescriptorParameterType @endlink is an alias for @link ParameterDescriptor.ParameterType NXOpen.CAE.AeroStructures.ParameterDescriptor.ParameterType@endlink
ParameterDescriptorParameterType = ParameterDescriptor.ParameterType


##  @link PropTableMarginPropertyType NXOpen.CAE.AeroStructures.PropTableMarginPropertyType @endlink is an alias for @link PropTable.MarginPropertyType NXOpen.CAE.AeroStructures.PropTable.MarginPropertyType@endlink
PropTableMarginPropertyType = PropTable.MarginPropertyType


##  @link UserLoadExtractionPickMethod NXOpen.CAE.AeroStructures.UserLoadExtractionPickMethod @endlink is an alias for @link UserLoadExtraction.PickMethod NXOpen.CAE.AeroStructures.UserLoadExtraction.PickMethod@endlink
UserLoadExtractionPickMethod = UserLoadExtraction.PickMethod


##  @link UserLoadExtractionTargetEntity NXOpen.CAE.AeroStructures.UserLoadExtractionTargetEntity @endlink is an alias for @link UserLoadExtraction.TargetEntity NXOpen.CAE.AeroStructures.UserLoadExtraction.TargetEntity@endlink
UserLoadExtractionTargetEntity = UserLoadExtraction.TargetEntity


