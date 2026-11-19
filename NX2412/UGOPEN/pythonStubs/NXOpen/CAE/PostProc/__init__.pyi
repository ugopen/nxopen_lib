from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class FunctionRecord(NXOpen.TransientObject): 
    """ This class represents a function record. """
    class AbscissaValueType(Enum):
        """
        Members Include: 
         |Double| 
         |Integer| 

        """
        Double: int
        Integer: int
        @staticmethod
        def ValueOf(value: int) -> FunctionRecord.AbscissaValueType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OrdinateValueType(Enum):
        """
        Members Include: 
         |RealOnly| 
         |RealImaginary| 

        """
        RealOnly: int
        RealImaginary: int
        @staticmethod
        def ValueOf(value: int) -> FunctionRecord.OrdinateValueType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AbscissaValueDataType(self) -> FunctionRecord.AbscissaValueType:
        """
        Getter for property: ( FunctionRecord.AbscissaValueType NXOpen.CA) AbscissaValueDataType
         Returns the abscissa value data type   
            
         
        """
        pass
    @property
    def OrdinateValueDataType(self) -> FunctionRecord.OrdinateValueType:
        """
        Getter for property: ( FunctionRecord.OrdinateValueType NXOpen.CA) OrdinateValueDataType
         Returns the ordinate value data type   
            
         
        """
        pass
    @property
    def RecordName(self) -> str:
        """
        Getter for property: (str) RecordName
         Returns the record name   
            
         
        """
        pass
    def Dispose(self) -> None:
        """
         Destroys the object 
        """
        pass
    def GetAbscissaValues(self) -> List[float]:
        """
         Gets abscissa values in case that abscissa value data type is
                        NXOpen.CAE.PostProc.FunctionRecord.AbscissaValueType.Double 
         Returns abscissaValues (List[float]): .
        """
        pass
    def GetIntegerAbscissaValues(self) -> List[int]:
        """
         Gets abscissa values in case that abscissa value data type is
                        NXOpen.CAE.PostProc.FunctionRecord.AbscissaValueType.Integer like Node id, element id etc. 
         Returns abscissaValues (List[int]): .
        """
        pass
    def GetOrdinateValues(self) -> List[float]:
        """
         Gets ordinate values.
                        
                        The values are returned according to the value type.
                        
                        
                        For ordinate value type NXOpen.CAE.PostProc.FunctionRecord.OrdinateValueType.RealOnly,
                        the values are returned as value1, value2...
                        
                        
                        For ordinate value type NXOpen.CAE.PostProc.FunctionRecord.OrdinateValueType.RealImaginary,
                        the values are returned as real1, imaginary1, real2, imaginary2...
                        
                        
                        
         Returns ordinateValues (List[float]): .
        """
        pass
import NXOpen
import NXOpen.CAE
class FunctionResultAccess(NXOpen.TaggedObject): 
    """ Represents a specific result state for a given NXOpen.CAE.Result. 
            The result state is defined by NXOpen.CAE.PostProc.FunctionResultParameters
            Use NXOpen.CAE.ResultManager to create an NXOpen.CAE.PostProc.FunctionResultAccess.
        """
    def GetFunctionRecords(self) -> List[FunctionRecord]:
        """
         Gets function records 
         Returns funcRecords ( FunctionRecord List[NXOpen.): .
        """
        pass
    def GetParameters(self) -> FunctionResultParameters:
        """
          Returns the NXOpen.CAE.PostProc.FunctionResultParameters which defines the current result state.
                          The NXOpen.CAE.PostProc.FunctionResultParameters can be modified but these changes will only take 
                          affect after NXOpen.CAE.PostProc.FunctionResultAccess.SetParameters is called. 
         Returns result_parameters ( FunctionResultParameters NXOpen.CA):  .
        """
        pass
    def GetResult(self) -> NXOpen.CAE.Result:
        """
          Returns the NXOpen.CAE.Result which defines this result Access object
                         The NXOpen.CAE.Result can be queried in order to set result state in
                         NXOpen.CAE.PostProc.FunctionResultParameters 
                     
         Returns result ( NXOpen.CAE.Result): .
        """
        pass
    def SetParameters(self, result_parameters: FunctionResultParameters) -> None:
        """
         SetsNXOpen.CAE.PostProc.FunctionResultParameters. This will validate any inappropiate settings.
                    If the input is not valid it will revert back to previous settings 
        """
        pass
import NXOpen
class FunctionResultParameters(NXOpen.TaggedObject): 
    """ This class is worked as a packet of information that can be either be used to change result state or pass around for information exchange between two  NXOpen.CAE.PostProc.FunctionResultAccess objects.
        Use NXOpen.CAE.ResultManager to create an NXOpen.CAE.PostProc.FunctionResultParameters
        
        You can modifiy these values but validation of correctness will only be perfomed 
        when this object is set to a NXOpen.CAE.PostProc.FunctionResultAccess object
        """
    def AddDoubleValuesFieldToIndependentVariable(self, indepVarName: str, fieldName: str, doubleValues: List[float]) -> None:
        """
         Adds a field of double values to an independent variable. 
        """
        pass
    def AddIntegerValuesFieldToIndependentVariable(self, indepVarName: str, fieldName: str, intValues: List[int]) -> None:
        """
         Adds a field of integer values to an independent variable. 
        """
        pass
    def AddStringValuesFieldToIndependentVariable(self, indepVarName: str, fieldName: str, stringValues: List[str]) -> None:
        """
         Adds a field of string values to an independent variable. 
        """
        pass
    def GetDomainVarAbsSelection(self) -> str:
        """
         Gets the field name which is used to query abscissa values in domain variable with multiple fields. 
         Returns absFieldName (str): .
        """
        pass
    def GetFunctionResultType(self) -> FunctionResultType:
        """
         Gets Function Result type  
         Returns type ( FunctionResultType NXOpen.CA):   .
        """
        pass
    def GetIndependentVariables(self) -> List[IndependentVariable]:
        """
         Gets the independent variables.
         Returns indepVars ( IndependentVariable List[NXOpen.): .
        """
        pass
    def SetDomainIndependentVariable(self, indepVarName: str) -> None:
        """
         Sets domain independent variable which is used to query abscissa values for function record. 
        """
        pass
    def SetDomainVarAbsSelection(self, absFieldName: str) -> None:
        """
         Sets the field name which is used to query abscissa values in domain variable with multiple fields. 
        """
        pass
    def SetFunctionResultType(self, type: FunctionResultType) -> None:
        """
         Sets Function Result type  
        """
        pass
import NXOpen
import NXOpen.CAE.FTK
class FunctionResultService(NXOpen.Object): 
    """ This class provides some services for function results. """
    def CreateRecords2D(tResultParams: List[FunctionResultParameters]) -> List[NXOpen.CAE.FTK.ArrayRecord2D]:
        """
         Creates 2D records which each record represents a set of X-Y values.
                        These records can be used to create 2D plots, stack plots, barchart plots.
         Returns tRecords ( NXOpen.CAE.FTK.ArrayRecord2D Li): .
        """
        pass
    def ListRecordInformationToFile(tResultParams: List[FunctionResultParameters], fileName: str, listData: bool) -> None:
        """
         Lists selected function records information to listing window or a specified output text file.
        """
        pass
import NXOpen
import NXOpen.CAE
class FunctionResultType(NXOpen.CAE.BaseResultType): 
    """ This class represnets a function result type from a result file.
            
            A function result tpye is defined by
            
                NXOpen.CAE.Result.Quantity - It specifies physical quantity of the result like Displacement, Stress etc. 
                Domain variable name - It specifies the function result value domain like time, frequency, etc. 
                Independent varialbes - They specify the independent variables for the function result values. 
            
            
        """
    @property
    def DisplayName(self) -> str:
        """
        Getter for property: (str) DisplayName
         Returns the display name.  
             
         
        """
        pass
    def GetAbscissaUnit(self) -> Tuple[NXOpen.Unit, str, str]:
        """
         Gets the abscissa unit information. 
         Returns A tuple consisting of (unitType, quantityName, localizedQuantityName). 
         - unitType is:  NXOpen.Unit.
         - quantityName is: str.
         - localizedQuantityName is: str.

        """
        pass
    def GetIndependentVariables(self) -> List[IndependentVariable]:
        """
         Gets the all variables of this result type. 
                    
                    
                    The variables are output in order. Primary independent variables always be ahead. and all independent variables are 
                    in the order of navigator hierarchy, this order is intended to make it easier to traverse every independent variable and 
                    its field values.
                    
                    
         Returns indepVars ( IndependentVariable List[NXOpen.): .
        """
        pass
    def GetOrdinateUnit(self) -> Tuple[NXOpen.Unit, str, str]:
        """
         Gets the ordinate unit information. 
         Returns A tuple consisting of (unitType, quantityName, localizedQuantityName). 
         - unitType is:  NXOpen.Unit.
         - quantityName is: str.
         - localizedQuantityName is: str.

        """
        pass
import NXOpen
class Group(NXOpen.TransientObject): 
    """ This class represents a post group. """
    class EntityType(Enum):
        """
        Members Include: 
         |Node|  Groups that contain node only. 
         |Element|  Groups that contain element only. 
         |Mixed|  Groups that contain node and elements. 

        """
        Node: int
        Element: int
        Mixed: int
        @staticmethod
        def ValueOf(value: int) -> Group.EntityType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SourceType(Enum):
        """
        Members Include: 
         |CreateOnLoadedResults|  Groups that are created from loaded results. 
         |ReadFromResultFile|  Groups that are read from result files. Not editable in post processing. 
         |PreModel|  Groups that are created from sim, fem, sim selection recipes, or fem selection recipes

        """
        CreateOnLoadedResults: int
        ReadFromResultFile: int
        PreModel: int
        @staticmethod
        def ValueOf(value: int) -> Group.SourceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def GroupName(self) -> str:
        """
        Getter for property: (str) GroupName
         Returns the group name   
            
         
        """
        pass
    def AskElementIndices(self) -> List[int]:
        """
         Asks element indices in the Group 
         Returns elementIndices (List[int]): .
        """
        pass
    def AskEntityType(self) -> Group.EntityType:
        """
         Ask the group entity type
         Returns groupEntityType ( Group.EntityType NXOpen.CA): .
        """
        pass
    def AskNodeIndices(self) -> List[int]:
        """
         Asks node indices in the Group 
         Returns nodeIndices (List[int]): .
        """
        pass
    def AskSourceType(self) -> Group.SourceType:
        """
         Ask the group source type
         Returns groupSourceType ( Group.SourceType NXOpen.CA): .
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory.  
                        After this method is called, it is illegal to use the object. 
                        In .NET, this method is automatically called when the object is deleted by the garbage collector. 
        """
        pass
import NXOpen
class IndependentVariable(NXOpen.TaggedObject): 
    """  This class represnets an independent variable. 
            
            It can be a field of values or multiple fields of values. One field of values could be
            
            
            String values like load case names, component names, etc.
            
            
            Integer values like node labels, element labels, etc.
            
            
            Double values like time values, frequency values, etc.
            
            
            
        """
    class FieldValueType(Enum):
        """
        Members Include: 
         |String| 
         |Integer| 
         |Double| 

        """
        String: int
        Integer: int
        Double: int
        @staticmethod
        def ValueOf(value: int) -> IndependentVariable.FieldValueType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FieldCount(self) -> int:
        """
        Getter for property: (int) FieldCount
         Returns the field count   
            
         
        """
        pass
    @property
    def IsDomainVariable(self) -> bool:
        """
        Getter for property: (bool) IsDomainVariable
         Returns the option to indicate whether this independent variable is primary independent variable or not   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    def GetDoubleValuesField(self, fieldIndx: int) -> List[float]:
        """
         Gets double values for given field index.
                        
                        The field index starts from 0 and must be smaller than the count by NXOpen.CAE.PostProc.IndependentVariable.FieldCount.
                        The field value type by NXOpen.CAE.PostProc.IndependentVariable.GetFieldValueTypeOption must be NXOpen.CAE.PostProc.IndependentVariable.FieldValueType.Double.
                        
                        If the data of an independent variable and following variable is discontinuous, field values might have duplicate values.
                        
                         
         Returns doubleValues (List[float]): .
        """
        pass
    def GetFieldName(self, fieldIndx: int) -> str:
        """
         Gets the name for given field index.
                        
                        The field index starts from 0 and must be smaller than the count by NXOpen.CAE.PostProc.IndependentVariable.FieldCount.
                         
         Returns fieldName (str): .
        """
        pass
    def GetFieldValueTypeOption(self, fieldIndx: int) -> IndependentVariable.FieldValueType:
        """
         Gets the value type option for given field index.
                        The field index starts from 0 and must be smaller than the count by NXOpen.CAE.PostProc.IndependentVariable.FieldCount.
         Returns valueType ( IndependentVariable.FieldValueType NXOpen.CA): .
        """
        pass
    def GetIntegerValuesField(self, fieldIndx: int) -> List[int]:
        """
         Gets integer values for given field index.
                        
                        The field index starts from 0 and must be smaller than the count by NXOpen.CAE.PostProc.IndependentVariable.FieldCount.
                        The field value type by NXOpen.CAE.PostProc.IndependentVariable.GetFieldValueTypeOption must be NXOpen.CAE.PostProc.IndependentVariable.FieldValueType.Integer.
                        
                        If the data of an independent variable and following variable is discontinuous, field values might have duplicate values.
                        
                         
         Returns intValues (List[int]): .
        """
        pass
    def GetStringValuesField(self, fieldIndx: int) -> List[str]:
        """
         Gets string values for given field index.
                        
                        The field index starts from 0 and must be smaller than the count by NXOpen.CAE.PostProc.IndependentVariable.FieldCount.
                        The field value type by NXOpen.CAE.PostProc.IndependentVariable.GetFieldValueTypeOption must be NXOpen.CAE.PostProc.IndependentVariable.FieldValueType.String.
                        
                        If the data of an independent variable and following variable is discontinuous, field values might have duplicate values.
                        
                         
         Returns stringValues (List[str]): .
        """
        pass
import NXOpen
import NXOpen.CAE
class ModalResult(NXOpen.TransientObject): 
    """ Implementation of ModalResult utility """
    def AskResult(self, modalResultTypes: NXOpen.CAE.Result.ModalResultType) -> Tuple[NXOpen.CAE.Result.ComplexFormat, NXOpen.Unit, List[float], List[float]]:
        """
         Asks the values for given modal result type
                    
                    
                    
                    For NXOpen.CAE.Result.ComplexFormat.RealOnly, only returns values in the complexPart1.
                    
                    
                    For NXOpen.CAE.Result.ComplexFormat.RealImaginary, returns real part values in the complexPart1 and imaginary part values in the complexPart2.
                    
                    
                    For NXOpen.CAE.Result.ComplexFormat.AmplitudePhase, returns amplitude part values in the complexPart1 and phase part values in the complexPart2.
                    
                    
                    NULL_TAG output for the units means unitless units or no such data.
                    
                    
                    
         Returns A tuple consisting of (complexFormat, units, complexPart1, complexPart2). 
         - complexFormat is:  NXOpen.CAE.Result.ComplexFormat.
         - units is:  NXOpen.Unit.
         - complexPart1 is: List[float].
         - complexPart2 is: List[float].

        """
        pass
    def AskResultTypes(self) -> List[NXOpen.CAE.Result.ModalResultType]:
        """
         Asks result types of modal result 
         Returns modalResultTypes ( NXOpen.CAE.Result.ModalResultType Li): .
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory.  
                    After this method is called, it is illegal to use the object.
                    In .NET, this method is automatically called when the object is deleted by the garbage collector. 
        """
        pass
import NXOpen
class ResultModel(NXOpen.TransientObject): 
    """ This class represents the result model. """
    def AskFEGroupByName(self, groupsName: str, groupEntityType: Group.EntityType) -> Group:
        """
         Asks the object of FE Set Group by name 
         Returns groupObjs ( Group NXOpen.CA): .
        """
        pass
    def AskPostGroupByID(self, groupID: int) -> Group:
        """
          Asks the object of Group by ID 
         Returns groupObjs ( Group NXOpen.CA): .
        """
        pass
    def AskPostGroupByName(self, groupsName: str) -> Group:
        """
          Asks the object of Group by name 
         Returns groupObjs ( Group NXOpen.CA): .
        """
        pass
    def AskPostGroups(self) -> List[Group]:
        """
         Asks number and objects of Groups available from the Result Model 
         Returns groupObjs ( Group List[NXOpen.): .
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory.  
                        After this method is called, is illegal to use the object. 
                        In .NET, this method is automatically called when the object is deleted by the garbage collector. 
        """
        pass
    def GetGlobalCyclicCoordinateSystem(self) -> int:
        """
         Gets the global cyclic coordinate system 
         Returns globalCyclicCsys (int): .
        """
        pass
