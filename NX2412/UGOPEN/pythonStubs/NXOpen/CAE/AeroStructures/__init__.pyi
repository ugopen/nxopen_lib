from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
class AeroStructuresAnnotDataS:
    @property
    def Direction(self) -> AeroStructuresAnnotdirectionoption:
        """
        Getter for property Direction
        """
        pass
    @Direction.setter
    def Direction(self, value: AeroStructuresAnnotdirectionoption):
        """
        Getter for property DirectionSetter for property Direction
        """
        pass
    @property
    def IsReversed(self) -> bool:
        """
        Getter for property IsReversed
        """
        pass
    @IsReversed.setter
    def IsReversed(self, value: bool):
        """
        Getter for property IsReversedSetter for property IsReversed
        """
        pass
    @property
    def LeaderLength(self) -> float:
        """
        Getter for property LeaderLength
        scale value in the range [-1,1] from smallest to largest, 0 gives default

        """
        pass
    @LeaderLength.setter
    def LeaderLength(self, value: float):
        """
        Getter for property LeaderLength
        scale value in the range [-1,1] from smallest to largest, 0 gives default
        Setter for property LeaderLength
        scale value in the range [-1,1] from smallest to largest, 0 gives default

        """
        pass
    @property
    def TextSize(self) -> float:
        """
        Getter for property TextSize
        scale value in the range [-1,1] from shortest to longest, 0 gives default

        """
        pass
    @TextSize.setter
    def TextSize(self, value: float):
        """
        Getter for property TextSize
        scale value in the range [-1,1] from shortest to longest, 0 gives default
        Setter for property TextSize
        scale value in the range [-1,1] from shortest to longest, 0 gives default

        """
        pass
class AeroStructuresAnnotdirectionoption(Enum):
    """
    Members Include: 
     |Normal| 
     |Xc| 
     |Yc| 
     |Zc| 
     |Unknown| 

    """
    Normal: int
    Xc: int
    Yc: int
    Zc: int
    Unknown: int
    @staticmethod
    def ValueOf(value: int) -> AeroStructuresAnnotdirectionoption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.Annotations
import NXOpen.CAE
class BaseCalculation(NXOpen.NXObject): 
    """  This is the  CAE.AeroStructures.BaseCalculation """
    class CalculationStatus(Enum):
        """
        Members Include: 
         |NotRun|  has not run 
         |Error|  error 
         |Success|  success 
         |PreparationFailed|  inputs arewere not coherent 

        """
        NotRun: int
        Error: int
        Success: int
        PreparationFailed: int
        @staticmethod
        def ValueOf(value: int) -> BaseCalculation.CalculationStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Annotation(self) -> NXOpen.Annotations.NoteBase:
        """
        Getter for property: ( NXOpen.Annotations.NoteBase) Annotation
         Returns the Annotation   
            
         
        """
        pass
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the description   
            
         
        """
        pass
    @property
    def ExtractionSourceSet(self) -> ExtractionSourceSet:
        """
        Getter for property: ( ExtractionSourceSet NXOpen.CAE.A) ExtractionSourceSet
         Returns the ExtractionSourceSet for the calculation   
            
         
        """
        pass
    @ExtractionSourceSet.setter
    def ExtractionSourceSet(self, extractionSourceSet: ExtractionSourceSet):
        """
        Setter for property: ( ExtractionSourceSet NXOpen.CAE.A) ExtractionSourceSet
         Returns the ExtractionSourceSet for the calculation   
            
         
        """
        pass
    @property
    def LoadCaseSet(self) -> LoadCaseSet:
        """
        Getter for property: ( LoadCaseSet NXOpen.CAE.A) LoadCaseSet
         Returns the LoadCaseSet used by the calculation  
            
         
        """
        pass
    @LoadCaseSet.setter
    def LoadCaseSet(self, loadCaseSet: LoadCaseSet):
        """
        Setter for property: ( LoadCaseSet NXOpen.CAE.A) LoadCaseSet
         Returns the LoadCaseSet used by the calculation  
            
         
        """
        pass
    @property
    def MethodDescriptor(self) -> MethodDescriptor:
        """
        Getter for property: ( MethodDescriptor NXOpen.CAE.A) MethodDescriptor
         Returns the method descriptor   
            
         
        """
        pass
    @property
    def PropertyTable(self) -> PropTable:
        """
        Getter for property: ( PropTable NXOpen.CAE.A) PropertyTable
         Returns the Property Table   
            
         
        """
        pass
    @property
    def Status(self) -> BaseCalculation.CalculationStatus:
        """
        Getter for property: ( BaseCalculation.CalculationStatus NXOpen.CAE.A) Status
         Returns the calculation status   
            
         
        """
        pass
    def CreateTemplate(self, filePath: str) -> None:
        """
         Create a template from the calculation 
        """
        pass
    def GetHasResult(self) -> bool:
        """
         Returns a boolean value that indicates whether the calculation has computed results 
         Returns hasResult (bool): .
        """
        pass
    def GetInputBooleanValue(self, parameterName: str) -> bool:
        """
         Get the value of a boolean input parameter 
         Returns value (bool): .
        """
        pass
    def GetInputComment(self, inputName: str) -> str:
        """
         Returns the user comment for an input 
         Returns comment (str): .
        """
        pass
    def GetInputFileValue(self, parameterName: str) -> str:
        """
         Get the value of an expanded file input parameter 
         Returns value (str): .
        """
        pass
    def GetInputIntegerValue(self, parameterName: str) -> int:
        """
         Get the value of an integer input parameter 
         Returns value (int): .
        """
        pass
    def GetInputLaminateValue(self, parameterName: str) -> Laminate:
        """
         Get the value of a laminate input parameter 
         Returns value ( Laminate NXOpen.CAE.A): .
        """
        pass
    def GetInputLoadElements(self, parameterName: str) -> List[NXOpen.CAE.FEElement]:
        """
         Get the elements where the loads are extracted from 
         Returns elementArray ( NXOpen.CAE.FEElement Li):  the list of support elements, if available .
        """
        pass
    def GetInputLoadLocation(self, parameterName: str) -> NXOpen.CAE.Result.Location:
        """
         Get the location (element or node) from where the loads are extracted  
         Returns location ( NXOpen.CAE.Result.Location): .
        """
        pass
    def GetInputLoadNodes(self, parameterName: str) -> List[NXOpen.CAE.FENode]:
        """
         Get the nodes where the loads are extracted from 
         Returns nodeArray ( NXOpen.CAE.FENode Li):  the list of support nodes, if available .
        """
        pass
    def GetInputLoadUnit(self, parameterName: str) -> NXOpen.Unit:
        """
         Get the unit type of a load input parameter.
                       Returns null if the parameter is unitless
                      
         Returns unit_type ( NXOpen.Unit): .
        """
        pass
    def GetInputLoadValues(self, parameterName: str, loadCaseName: str) -> List[float]:
        """
         Get the aggregated or non-aggregated load values of an input parameter for this row.
                        If the load values were aggregated, the output will be an array with only one value.
                        If the values were not aggregated, the output will be an array with one value per element or node.
                        This call is not available when the solution refers to Attached Results.
                        Both the load case's Name and JournalIdentifier are supported. 
         Returns values (List[float]): .
        """
        pass
    def GetInputLoadValuesAll(self, parameterName: str) -> NXOpen.GeneralScalarTable:
        """
         Get the aggregated or non-aggregated all load values of an input parameter
                        The output will be a general scalar table, one load by row.
                        If the load values were aggregated, the row will contain one column.
                        If the values were not aggregated, the row will contain one value per element or node per column. 
                        This call is not available when the solution refers to Attached Results. 
         Returns loads ( NXOpen.GeneralScalarTable): .
        """
        pass
    def GetInputNames(self) -> List[str]:
        """
         Returns a list of all the current input names 
         Returns inputNames (List[str]): .
        """
        pass
    def GetInputScalarUnit(self, parameterName: str) -> NXOpen.Unit:
        """
         Get the unit type of a scalar input parameter 
                       Returns null if the parameter is unitless
                      
         Returns unit_type ( NXOpen.Unit): .
        """
        pass
    def GetInputScalarValue(self, parameterName: str) -> float:
        """
         Get the value of a scalar input parameter 
         Returns value (float): .
        """
        pass
    def GetInputSizeValue(self, parameterName: str) -> int:
        """
         Get the value of a size input parameter 
         Returns value (int): .
        """
        pass
    def GetInputStringValue(self, parameterName: str) -> str:
        """
         Get the value of a string input parameter 
         Returns value (str): .
        """
        pass
    def GetInputTableValue(self, parameterName: str) -> TableParameter:
        """
         Get the value of a table input parameter 
         Returns value ( TableParameter NXOpen.CAE.A): .
        """
        pass
    def GetLaminateQueryManager(self) -> LaminateQueryManager:
        """
         Returns the laminate query manager 
         Returns mgr ( LaminateQueryManager NXOpen.CAE.A): .
        """
        pass
    def GetLog(self) -> List[CalculationLogLine]:
        """
         Return the list of log entries 
         Returns logsEntries ( CalculationLogLine List[NXOpen.CAE): .
        """
        pass
    def GetOutputNames(self) -> List[str]:
        """
         Returns a list of all the current output names 
         Returns outputNames (List[str]): .
        """
        pass
    def GetParameterType(self, parameterName: str) -> ParameterDescriptor.ParameterType:
        """
         Returns the parameter type for a current input or output 
         Returns type ( ParameterDescriptor.ParameterType NXOpen.CAE.A): .
        """
        pass
    def GetResultFailModeNames(self) -> List[str]:
        """
         Returns the failMode names from the last computed result
         Returns failModeIds (List[str]): .
        """
        pass
    def GetResultInputBooleanValue(self, parameterName: str) -> bool:
        """
         Get the value of a boolean input parameter for the last computed result 
         Returns value (bool): .
        """
        pass
    def GetResultInputComment(self, inputName: str) -> str:
        """
         Returns the user comment about an input in the last computed result 
         Returns comment (str): .
        """
        pass
    def GetResultInputFileValue(self, parameterName: str) -> str:
        """
         Get the value of a file input parameter 
         Returns value (str): .
        """
        pass
    def GetResultInputIntegerValue(self, parameterName: str) -> int:
        """
         Get the value of an integer input parameter for the last computed result 
         Returns value (int): .
        """
        pass
    def GetResultInputLaminateShorthandNotation(self, parameterName: str) -> str:
        """
         Get the shorthand notation of a laminate input parameter for the last computed result 
         Returns value (str): .
        """
        pass
    def GetResultInputLoadUnit(self, parameterName: str) -> NXOpen.Unit:
        """
         Get the unit type of a scalar input parameter for the last computed result 
         Returns unit_type ( NXOpen.Unit): .
        """
        pass
    def GetResultInputLoadValues(self, parameterName: str, loadCaseName: str) -> List[float]:
        """
         Get the aggregated or non-aggregated load values of an input parameter for this row.
                        If the load values were aggregated, the output will be an array with only one value.
                        If the values were not aggregated, the output will be an array with one value per element or node.
                        Both the load case's Name and JournalIdentifier are supported. 
         Returns values (List[float]): .
        """
        pass
    def GetResultInputNames(self) -> List[str]:
        """
         Returns a list of all the input names used in the last computed result 
         Returns inputNames (List[str]): .
        """
        pass
    def GetResultInputScalarUnit(self, parameterName: str) -> NXOpen.Unit:
        """
         Get the unit type of a scalar input parameter for the last computed result 
         Returns unit_type ( NXOpen.Unit): .
        """
        pass
    def GetResultInputScalarValue(self, parameterName: str) -> float:
        """
         Get the value of a scalar input parameter for the last computed result 
         Returns value (float): .
        """
        pass
    def GetResultInputStringValue(self, parameterName: str) -> str:
        """
         Get the value of a string input parameter for the last computed result 
         Returns value (str): .
        """
        pass
    def GetResultLoadCaseNames(self) -> List[str]:
        """
         Returns the loadCase names used in the last computed result
         Returns loadCaseNames (List[str]): .
        """
        pass
    def GetResultOutputBooleanValue(self, parameterName: str, failureModeName: str, loadCaseName: str) -> bool:
        """
         Get the value of a boolean output parameter for the last computed result.
                        Both the load case's Name and JournalIdentifier are supported. 
         Returns value (bool): .
        """
        pass
    def GetResultOutputFileValue(self, parameterName: str) -> str:
        """
         Get the value of a file output parameter 
         Returns value (str): .
        """
        pass
    def GetResultOutputIntegerValue(self, parameterName: str, failureModeName: str, loadCaseName: str) -> int:
        """
         Get the value of an integer output parameter for the last computed result.
                        Both the load case's Name and JournalIdentifier are supported. 
         Returns value (int): .
        """
        pass
    def GetResultOutputNames(self) -> List[str]:
        """
         Returns a list of all the output names used in the last computed result
         Returns outputNames (List[str]): .
        """
        pass
    def GetResultOutputScalarUnit(self, parameterName: str) -> NXOpen.Unit:
        """
         Get the unit type of a scalar output parameter for the last computed result 
         Returns unit_type ( NXOpen.Unit): .
        """
        pass
    def GetResultOutputScalarValue(self, parameterName: str, failureModeName: str, loadCaseName: str) -> float:
        """
         Get the value of a scalar output parameter for the last computed result.
                        Both the load case's Name and JournalIdentifier are supported. 
         Returns value (float): .
        """
        pass
    def GetResultOutputStringValue(self, parameterName: str, failureModeName: str, loadCaseName: str) -> str:
        """
         Get the value of a string output parameter for the last computed result.
                        Both the load case's Name and JournalIdentifier are supported. 
         Returns value (str): .
        """
        pass
    def GetResultOutputUnit(self, outputName: str) -> NXOpen.Unit:
        """
         Returns the unit type for an output in the last computed result 
         Returns unit_type ( NXOpen.Unit): .
        """
        pass
    def GetResultParameterType(self, parameterName: str) -> ParameterDescriptor.ParameterType:
        """
         Returns the parameter type for an input or output in the last computed result 
         Returns type ( ParameterDescriptor.ParameterType NXOpen.CAE.A): .
        """
        pass
    def UpdateScalarExpressions(self) -> None:
        """
         Cause scalar expressions to be updated 
        """
        pass
import NXOpen
class BaseExtractionSource(NXOpen.NXObject): 
    """ Base abstract class for extraction source. """
    class TypeEnum(Enum):
        """
        Members Include: 
         |Unknown| 
         |PolygonFace| 
         |PolygonEdge| 
         |PolygonBody| 
         |SelectionRecipe| 
         |Element1D| 
         |Element2D| 
         |Element3D| 
         |Node| 
         |Group| 
         |PhysicalProperty| 
         |Collector2D| 
         |Material| 
         |Section| 
         |Mesh1D| 
         |Mesh2D| 
         |LaminatePhysicalProperty| 

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
        @staticmethod
        def ValueOf(value: int) -> BaseExtractionSource.TypeEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BaseDefaultName(self) -> str:
        """
        Getter for property: (str) BaseDefaultName
         Returns the base default name   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    @property
    def NumberOfEntities(self) -> int:
        """
        Getter for property: (int) NumberOfEntities
         Returns the number of entities in the group   
            
         
        """
        pass
    @property
    def Type(self) -> BaseExtractionSource.TypeEnum:
        """
        Getter for property: ( BaseExtractionSource.TypeEnum NXOpen.CAE.A) Type
         Returns the extraction source type   
            
         
        """
        pass
    def GetEntities(self) -> List[NXOpen.TaggedObject]:
        """
         Get the entities of this source 
         Returns entities ( NXOpen.TaggedObject Li):  .
        """
        pass
import NXOpen
import NXOpen.CAE
class BaseSolution(NXOpen.NXObject): 
    """ Base journaling class for Aerostruct solutions. """
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the solution description   
            
         
        """
        pass
    @property
    def IsUsingAttachedResults(self) -> bool:
        """
        Getter for property: (bool) IsUsingAttachedResults
         Returns a value indicating whether the reference solution refers to attached results   
            
         
        """
        pass
    @property
    def ReferenceSolution(self) -> NXOpen.CAE.SimSolution:
        """
        Getter for property: ( NXOpen.CAE.SimSolution) ReferenceSolution
         Returns the referenced FE-Solution of the AeroStructure solution   
            
         
        """
        pass
    @property
    def LoadCaseCollection() -> LoadCaseCollection:
        """
         Returns the  NXOpen::CAE::AeroStructures::LoadCaseCollection  belonging to this 
        """
        pass
    @property
    def LoadCaseSetCollection() -> LoadCaseSetCollection:
        """
         Returns the  NXOpen::CAE::AeroStructures::LoadCaseSetCollection  belonging to this 
        """
        pass
    @property
    def SolveOptions() -> SolveOptions:
        """
         Access to the solve options for this session 
        """
        pass
    def Rename(self, name: str) -> None:
        """
         Renames the solution
        """
        pass
    def Solve(self, calculations: List[BaseCalculation]) -> None:
        """
         Solve the calculations passed in the argument belonging to this solution 
        """
        pass
    def SolveAll(self) -> None:
        """
         Solve all the calculations in the solution 
        """
        pass
import NXOpen
class CalculationLogLine(NXOpen.TransientObject): 
    """  This is the Calculation log line  """
    class MessageType(Enum):
        """
        Members Include: 
         |Info| 
         |Warning| 
         |Error| 
         |Unknown| 

        """
        Info: int
        Warning: int
        Error: int
        Unknown: int
        @staticmethod
        def ValueOf(value: int) -> CalculationLogLine.MessageType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Failmode(self) -> str:
        """
        Getter for property: (str) Failmode
         Returns the failMode   
            
         
        """
        pass
    @property
    def Loadcase(self) -> str:
        """
        Getter for property: (str) Loadcase
         Returns the loadcase name   
            
         
        """
        pass
    @property
    def Message(self) -> str:
        """
        Getter for property: (str) Message
         Returns the log message   
            
         
        """
        pass
    @property
    def MsgType(self) -> CalculationLogLine.MessageType:
        """
        Getter for property: ( CalculationLogLine.MessageType NXOpen.CAE.A) MsgType
         Returns the message type   
            
         
        """
        pass
    @property
    def Source(self) -> str:
        """
        Getter for property: (str) Source
         Returns the source   
            
         
        """
        pass
    @property
    def Timestamp(self) -> str:
        """
        Getter for property: (str) Timestamp
         Returns the timestamp   
            
         
        """
        pass
    def Dispose(self) -> None:
        """
         Dispose 
        """
        pass
    def ToStringLine(self) -> str:
        """
         Return structure as a string line 
         Returns result (str): .
        """
        pass
import NXOpen
class DescriptionValue(NXOpen.NXObject): 
    """  Represents a description value  """
    @property
    def AutomaticTextPropertyValue(self) -> bool:
        """
        Getter for property: (bool) AutomaticTextPropertyValue
         Returns the automatic_text_property   
            
         
        """
        pass
    @AutomaticTextPropertyValue.setter
    def AutomaticTextPropertyValue(self, property_value: bool):
        """
        Setter for property: (bool) AutomaticTextPropertyValue
         Returns the automatic_text_property   
            
         
        """
        pass
class DynamicLoadCaseSet(LoadCaseSet): 
    """ Represents a NXOpen.CAE.AeroStructures.DynamicLoadCaseSet. """
    pass
import NXOpen
class ExpressionCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of  CAE.AeroStructures.Expression. """
    @overload
    def DeleteExpression(self, expression: Expression) -> None:
        """
         Removes the expression from the solution 
        """
        pass
    @overload
    def DeleteExpression(self, expressionsTags: List[Expression]) -> None:
        """
         Removes the expressions from the solution .
        """
        pass
    def FindObject(self, name: str) -> Expression:
        """
         Finds the NXOpen.CAE.AeroStructures.Expression object with the given name. 
         Returns found ( Expression NXOpen.CAE.A):  NXOpen.CAE.AeroStructures.Expression object with this name. .
        """
        pass
    @overload
    def RenameExpression(self, name: str, expression: Expression) -> None:
        """
         Renames expression.
        """
        pass
    @overload
    def RenameExpression(self, name: str, expressionsTags: List[Expression]) -> None:
        """
         Renames expression.
        """
        pass
class ExpressionResult(Expression): 
    """ Represents a NXOpen.CAE.AeroStructures.ExpressionResult. """
    class Type(Enum):
        """
        Members Include: 
         |CriticalMS| 

        """
        CriticalMS: int
        @staticmethod
        def ValueOf(value: int) -> ExpressionResult.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def SetCalculations(self, marginCalculations: List[MarginCalculation]) -> None:
        """
         Sets the calculations. 
        """
        pass
    def Update(self) -> None:
        """
         Update the expression. 
        """
        pass
import NXOpen
class Expression(NXOpen.NXObject): 
    """ Represents a NXOpen.CAE.AeroStructures.Expression. """
    pass
import NXOpen
class ExtractionSourceSet(NXOpen.NXObject): 
    """ Class for set of named extraction sources. """
    def AddExtractionSource(self, source: BaseExtractionSource) -> None:
        """
         Add a single NXOpen.CAE.AeroStructures.BaseExtractionSource item to the extraction source set.   
        """
        pass
    def CreateGeometricalExtractionSource(self, type: BaseExtractionSource.TypeEnum, source_name: str, entities_array: List[NXOpen.TaggedObject]) -> GeometricalExtractionSource:
        """
         Creates a
                        NXOpen.CAE.AeroStructures.GeometricalExtractionSource
                        If the type is not supported or the entities do not match the entity type,
                        an empty extraction source is returned with type 'Unknown'.
                     
         Returns source ( GeometricalExtractionSource NXOpen.CAE.A):  geometrical extraction source object.
        """
        pass
    def CreateGeometricalExtractionSourceFromEntity(self, source_name: str, entity: NXOpen.TaggedObject) -> GeometricalExtractionSource:
        """
         Creates a
                        NXOpen.CAE.AeroStructures.GeometricalExtractionSource
                        with the source type defined by the specified entity.  The
                        entity is added to the source.  If the entity is not of a supported type
                        an empty extraction source is returned with type 'Unknown'.
                     
         Returns source ( GeometricalExtractionSource NXOpen.CAE.A):  geometrical extraction source object.
        """
        pass
    def CreateMaterialSource(self, source_name: str, entity: NXOpen.TaggedObject) -> MaterialSource:
        """
         Creates a NXOpen.CAE.AeroStructures.MaterialSource 
         Returns source ( MaterialSource NXOpen.CAE.A):  material source object.
        """
        pass
    def CreatePhysicalPropertySource(self, type: BaseExtractionSource.TypeEnum, source_name: str, entity: NXOpen.TaggedObject) -> PhysicalPropertySource:
        """
         Creates a NXOpen.CAE.AeroStructures.PhysicalPropertySource 
         Returns source ( PhysicalPropertySource NXOpen.CAE.A):  physical property source object.
        """
        pass
    def CreateSectionSource(self, source_name: str, entity: NXOpen.TaggedObject) -> SectionSource:
        """
         Creates a NXOpen.CAE.AeroStructures.SectionSource 
         Returns source ( SectionSource NXOpen.CAE.A):  section source object.
        """
        pass
    def GetExtractionSources(self) -> List[BaseExtractionSource]:
        """
         Get the array of  NXOpen.CAE.AeroStructures.BaseExtractionSource 
         Returns source ( BaseExtractionSource List[NXOpen.CAE):  extraction source objects.
        """
        pass
    def GetNextAvailableDefaultSourceName(self, type: BaseExtractionSource.TypeEnum) -> str:
        """
         Return the next available default source name for a given type 
         Returns name (str): .
        """
        pass
    def SetExtractionSources(self, source: List[BaseExtractionSource]) -> None:
        """
         Set the array of  NXOpen.CAE.AeroStructures.BaseExtractionSource 
        """
        pass
import NXOpen
class FailureMode(NXOpen.TransientObject): 
    """  This is the Failure Mode  """
    @property
    def Id(self) -> str:
        """
        Getter for property: (str) Id
         Returns the id   
            
         
        """
        pass
    @property
    def UiName(self) -> str:
        """
        Getter for property: (str) UiName
         Returns the UI name   
            
         
        """
        pass
    def Dispose(self) -> None:
        """
         Dispose 
        """
        pass
import NXOpen.CAE
class FreeBodyLoadExtraction(LoadExtractionStrategy): 
    """  This is the FreeBody LoadExtraction class  """
    class Component(Enum):
        """
        Members Include: 
         |NotSet| 
         |X| 
         |Y| 
         |Z| 
         |PlanarMagnitudeXY| 
         |PlanarMagnitudeXZ| 
         |PlanarMagnitudeZY| 
         |Magnitude| 

        """
        NotSet: int
        X: int
        Y: int
        Z: int
        PlanarMagnitudeXY: int
        PlanarMagnitudeXZ: int
        PlanarMagnitudeZY: int
        Magnitude: int
        @staticmethod
        def ValueOf(value: int) -> FreeBodyLoadExtraction.Component:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Result(Enum):
        """
        Members Include: 
         |NotSet| 
         |Force| 
         |Moment| 

        """
        NotSet: int
        Force: int
        Moment: int
        @staticmethod
        def ValueOf(value: int) -> FreeBodyLoadExtraction.Result:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetComponent(self) -> FreeBodyLoadExtraction.Component:
        """
         Get Component Type 
         Returns component ( FreeBodyLoadExtraction.Component NXOpen.CAE.A): .
        """
        pass
    def GetFreeBody(self) -> NXOpen.CAE.NodalForceReport:
        """
         Get Free Body 
         Returns freeBody ( NXOpen.CAE.NodalForceReport): .
        """
        pass
    def GetMatrixManip(self) -> MatrixManip:
        """
         Get Matrix Manip 
         Returns manip ( MatrixManip NXOpen.CAE.A): .
        """
        pass
    def GetResult(self) -> FreeBodyLoadExtraction.Result:
        """
         Get Result Type 
         Returns result ( FreeBodyLoadExtraction.Result NXOpen.CAE.A): .
        """
        pass
    def SetComponent(self, component: FreeBodyLoadExtraction.Component) -> None:
        """
         Set Component Type 
        """
        pass
    def SetFreeBody(self, freeBody: NXOpen.CAE.NodalForceReport) -> None:
        """
         Set Free Body 
        """
        pass
    def SetMatrixManip(self, manip: MatrixManip) -> None:
        """
         Set Matrix Manip 
        """
        pass
    def SetResult(self, result: FreeBodyLoadExtraction.Result) -> None:
        """
         Set Result Type 
        """
        pass
class GeometricalExtractionSource(BaseExtractionSource): 
    """ Geometrical extraction source class. """
    pass
import NXOpen
class GraphicalReportBuilder(NXOpen.Builder): 
    """ This is a manager to the CAE.AeroStructures.GraphicalReport class.
    Object of type CAE.AeroStructures.GraphicalReport can be
    created and edited only through this class
    """
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the graphical report description   
            
         
        """
        pass
    @Description.setter
    def Description(self, title: str):
        """
        Setter for property: (str) Description
         Returns the graphical report description   
            
         
        """
        pass
    @property
    def Title(self) -> str:
        """
        Getter for property: (str) Title
         Returns the graphical report title  
            
         
        """
        pass
    @Title.setter
    def Title(self, title: str):
        """
        Setter for property: (str) Title
         Returns the graphical report title  
            
         
        """
        pass
import NXOpen
class GraphicalReportCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of AeroStruct GraphicalReport """
    def CreateGraphicalReportBuilder(self, graphicalReport: GraphicalReport) -> GraphicalReportBuilder:
        """
         Creates a NXOpen.CAE.AeroStructures.GraphicalReportBuilder 
         Returns builder ( GraphicalReportBuilder NXOpen.CAE.A):  Builder object.
        """
        pass
    def DeleteGraphicalReport(self, graphicalReport: GraphicalReport) -> None:
        """
         Delete an AeroStruct graphical report. 
        """
        pass
    def FindObject(self, title: str) -> GraphicalReport:
        """
         Finds the NXOpen.CAE.AeroStructures.GraphicalReport object with the given name. 
         Returns found ( GraphicalReport NXOpen.CAE.A):  NXOpen.CAE.AeroStructures.GraphicalReport object with this name. .
        """
        pass
import NXOpen
class GraphicalReport(NXOpen.NXObject): 
    """ Represents a NXOpen.CAE.AeroStructures.GraphicalReport. """
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the description   
            
         
        """
        pass
    @property
    def FilePath(self) -> str:
        """
        Getter for property: (str) FilePath
         Returns the file path   
            
         
        """
        pass
    @property
    def Title(self) -> str:
        """
        Getter for property: (str) Title
         Returns the title   
            
         
        """
        pass
import NXOpen
class LaminateHelper(NXOpen.Object): 
    """ Represents a NXOpen.CAE.AeroStructures.LaminateHelper object. """
    def NewLocalLaminate() -> LocalLaminate:
        """
         Create an empty local laminate 
         Returns local ( LocalLaminate NXOpen.CAE.A): .
        """
        pass
import NXOpen
class LaminateQueryManager(NXOpen.NXObject): 
    """  Represents a laminate manager  """
    def AddLaminateQuery(self, query: LaminateQuery) -> bool:
        """
         Adds a laminate query object to the manager 
         Returns status (bool): .
        """
        pass
    def CreateLaminateQuery(self, laminateBaseName: str, laminateQueryOwner: NXOpen.NXObject, isManagedQuery: bool) -> LaminateQuery:
        """
         Create a laminate query object 
         Returns query ( LaminateQuery NXOpen.CAE.A): .
        """
        pass
    def CreateLaminateQueryCopy(self, laminateBaseName: str, laminateQueryOwner: NXOpen.NXObject, baseLaminateObject: LaminateQuery) -> LaminateQuery:
        """
         Create a managed copy of the laminate query object 
         Returns query ( LaminateQuery NXOpen.CAE.A): .
        """
        pass
    def GetLaminateQueries(self) -> Tuple[List[str], List[NXOpen.NXObject]]:
        """
         Returns the list of available laminate queries 
         Returns A tuple consisting of (laminateQueryNames, laminateQueryTags). 
         - laminateQueryNames is: List[str].
         - laminateQueryTags is:  NXOpen.NXObject Li.

        """
        pass
    def GetLaminateQuery(self, laminateBaseName: str) -> LaminateQuery:
        """
         Find a laminate query object by name
         Returns query ( LaminateQuery NXOpen.CAE.A): .
        """
        pass
    def RemoveLaminateQuery(self, query: LaminateQuery) -> None:
        """
         Removes a laminate query from the manager 
        """
        pass
import NXOpen
class LaminateQuery(NXOpen.NXObject): 
    """  Represents a laminate query  """
    class AngleDefinitionTypeEnum(Enum):
        """
        Members Include: 
         |MaterialAngle| 
         |Angle| 
         |Vector| 

        """
        MaterialAngle: int
        Angle: int
        Vector: int
        @staticmethod
        def ValueOf(value: int) -> LaminateQuery.AngleDefinitionTypeEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ReferenceEntityTypeEnum(Enum):
        """
        Members Include: 
         |ExistingLaminate| 
         |LaminatePhysicalProperty| 
         |Element2D| 
         |PolygonFace| 
         |Mesh| 
         |Collector2D| 
         |Group| 
         |SelectionRecipe| 
         |Unknown| 
         |ExtractionSource| 

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
        @staticmethod
        def ValueOf(value: int) -> LaminateQuery.ReferenceEntityTypeEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AngleDefinitionType(self) -> LaminateQuery.AngleDefinitionTypeEnum:
        """
        Getter for property: ( LaminateQuery.AngleDefinitionTypeEnum NXOpen.CAE.A) AngleDefinitionType
         Returns the current angle definition type   
            
         
        """
        pass
    @property
    def ExtractionInvertNormal(self) -> bool:
        """
        Getter for property: (bool) ExtractionInvertNormal
         Returns the laminate extraction normal flag.  
             
         
        """
        pass
    @property
    def ExtractionReversePlies(self) -> bool:
        """
        Getter for property: (bool) ExtractionReversePlies
         Returns the laminate extraction reverse ply order flag.  
             
         
        """
        pass
    @property
    def ExtractionSourceName(self) -> str:
        """
        Getter for property: (str) ExtractionSourceName
         Returns the extraction source name  
            
         
        """
        pass
    @ExtractionSourceName.setter
    def ExtractionSourceName(self, name: str):
        """
        Setter for property: (str) ExtractionSourceName
         Returns the extraction source name  
            
         
        """
        pass
    @property
    def LaminateBaseName(self) -> str:
        """
        Getter for property: (str) LaminateBaseName
         Returns the laminate base name   
            
         
        """
        pass
    @LaminateBaseName.setter
    def LaminateBaseName(self, laminateBaseName: str):
        """
        Setter for property: (str) LaminateBaseName
         Returns the laminate base name   
            
         
        """
        pass
    @property
    def LaminateName(self) -> str:
        """
        Getter for property: (str) LaminateName
         Returns the laminate name   
            
         
        """
        pass
    @LaminateName.setter
    def LaminateName(self, laminateName: str):
        """
        Setter for property: (str) LaminateName
         Returns the laminate name   
            
         
        """
        pass
    @property
    def ReferenceEntity(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) ReferenceEntity
         Returns the selected entity tag   
            
         
        """
        pass
    @ReferenceEntity.setter
    def ReferenceEntity(self, referenceEntity: NXOpen.TaggedObject):
        """
        Setter for property: ( NXOpen.TaggedObject) ReferenceEntity
         Returns the selected entity tag   
            
         
        """
        pass
    @property
    def ReferenceEntityType(self) -> LaminateQuery.ReferenceEntityTypeEnum:
        """
        Getter for property: ( LaminateQuery.ReferenceEntityTypeEnum NXOpen.CAE.A) ReferenceEntityType
         Returns the current reference entity type   
            
         
        """
        pass
    @ReferenceEntityType.setter
    def ReferenceEntityType(self, referenceEntityType: LaminateQuery.ReferenceEntityTypeEnum):
        """
        Setter for property: ( LaminateQuery.ReferenceEntityTypeEnum NXOpen.CAE.A) ReferenceEntityType
         Returns the current reference entity type   
            
         
        """
        pass
    def GetExtractionAngle(self) -> float:
        """
         Gets the laminate extraction angle. 
         Returns laminateAngle (float): .
        """
        pass
    def GetExtractionAngleTolerance(self, angleUnit: NXOpen.Unit) -> float:
        """
         Gets the laminate extraction angle tolerance. 
         Returns angleTolerance (float): .
        """
        pass
    def GetExtractionDirection(self) -> NXOpen.Vector3d:
        """
         Gets the laminate extraction direction. 
         Returns direction ( NXOpen.Vector3d): .
        """
        pass
    def GetExtractionSource(self) -> BaseExtractionSource:
        """
         Get the extraction source 
         Returns source ( BaseExtractionSource NXOpen.CAE.A): .
        """
        pass
    def GetLaminatePhysicalProperties(self) -> Tuple[List[str], List[NXOpen.NXObject]]:
        """
         Finds the available physical properties of type laminate 
         Returns A tuple consisting of (physicalPropertyNames, physicalPropertyLaminates). 
         - physicalPropertyNames is: List[str].
         - physicalPropertyLaminates is:  NXOpen.NXObject Li.

        """
        pass
    def GetLaminateQueries(self) -> Tuple[List[str], List[NXOpen.NXObject]]:
        """
         Returns the list of available laminate queries 
         Returns A tuple consisting of (laminateQueryNames, laminateQueryTags). 
         - laminateQueryNames is: List[str].
         - laminateQueryTags is:  NXOpen.NXObject Li.

        """
        pass
    def GetReferenceEntityTypeName(self, referenceEntityType: LaminateQuery.ReferenceEntityTypeEnum) -> str:
        """
         Returns the renference entity type name 
         Returns referenceEntityTypeName (str):  The reference entity name .
        """
        pass
    def GetReferenceEntityTypeNames(self) -> List[str]:
        """
         Returns the renference entity type names 
         Returns referenceEntityTypeNames (List[str]): .
        """
        pass
    def GetReferenceEntityTypesAndNames(self) -> Tuple[List[int], List[str]]:
        """
         Returns the renference entity type names 
         Returns A tuple consisting of (referenceEntityIndexes, referenceEntityTypeNames). 
         - referenceEntityIndexes is: List[int].
         - referenceEntityTypeNames is: List[str].

        """
        pass
    def SetExtractionAngle(self, laminateAngle: float) -> None:
        """
         Sets the laminate extraction angle. 
        """
        pass
    def SetExtractionDirection(self, direction: NXOpen.Vector3d) -> None:
        """
         Sets the laminate extraction direction. 
        """
        pass
    @overload
    def SetValues(self, laminateBaseName: str, laminateName: str, referenceEntityType: LaminateQuery.ReferenceEntityTypeEnum, referenceEntity: NXOpen.TaggedObject, extractionAngleInRadians: float, extractionDirection: NXOpen.Vector3d, extractionType: LaminateQuery.AngleDefinitionTypeEnum, extractionAngleToleranceInRadians: float, invertNormals: bool, reverseOrder: bool) -> None:
        """
         Sets the internal values of the query  (with entity) 
        """
        pass
    @overload
    def SetValues(self, laminateBaseName: str, laminateName: str, sourceName: str, extractionAngleInRadians: float, extractionDirection: NXOpen.Vector3d, extractionType: LaminateQuery.AngleDefinitionTypeEnum, extractionAngleToleranceInRadians: float, invertNormals: bool, reverseOrder: bool) -> None:
        """
         Sets the internal values of the query  (with extraction source) 
        """
        pass
import NXOpen
class LaminateValue(NXOpen.NXObject): 
    """  Represents a laminate value  """
    @property
    def LaminateQuery(self) -> LaminateQuery:
        """
        Getter for property: ( LaminateQuery NXOpen.CAE.A) LaminateQuery
         Returns the active Query   
            
         
        """
        pass
    @LaminateQuery.setter
    def LaminateQuery(self, query: LaminateQuery):
        """
        Setter for property: ( LaminateQuery NXOpen.CAE.A) LaminateQuery
         Returns the active Query   
            
         
        """
        pass
import NXOpen
import NXOpen.CAE.AeroStructures.Author
class Laminate(NXOpen.TransientObject): 
    """ Represents a NXOpen.CAE.AeroStructures.Laminate object. """
    class LamRefLoc(Enum):
        """
        Members Include: 
         |Top|  
         |Middle|  
         |Bottom|  
         |Specify|  

        """
        Top: int
        Middle: int
        Bottom: int
        Specify: int
        @staticmethod
        def ValueOf(value: int) -> Laminate.LamRefLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def IsBalanced(self) -> bool:
        """
        Getter for property: (bool) IsBalanced
         Returns the laminate is balanced   
            
         
        """
        pass
    @property
    def IsSymmetric(self) -> bool:
        """
        Getter for property: (bool) IsSymmetric
         Returns the laminate is symmetric   
            
         
        """
        pass
    @property
    def MassDensity(self) -> float:
        """
        Getter for property: (float) MassDensity
         Returns the mass density   
            
         
        """
        pass
    @property
    def MassPerUnitArea(self) -> float:
        """
        Getter for property: (float) MassPerUnitArea
         Returns the mass per unit area   
            
         
        """
        pass
    @property
    def NumMaterials(self) -> int:
        """
        Getter for property: (int) NumMaterials
         Returns the number of distinct materials used   
            
         
        """
        pass
    @property
    def NumPlies(self) -> int:
        """
        Getter for property: (int) NumPlies
         Returns the number of plies   
            
         
        """
        pass
    @property
    def PhysPropName(self) -> str:
        """
        Getter for property: (str) PhysPropName
         Returns the name of the laminate physical property.  
             
         
        """
        pass
    @property
    def TotalThickness(self) -> float:
        """
        Getter for property: (float) TotalThickness
         Returns the total thickness of the composite   
            
         
        """
        pass
    def CreateLocalLaminateByCopy(self) -> LocalLaminate:
        """
         Create an editable copy of the laminate 
         Returns local ( LocalLaminate NXOpen.CAE.A): .
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called, it is
                    illegal to use the object. In .NET, this method is automatically
                    called when the object is deleted by the garbage collector. 
        """
        pass
    def GetABD(self) -> NXOpen.GeneralScalarTable:
        """
         The ABD matrix 
         Returns matrix ( NXOpen.GeneralScalarTable): .
        """
        pass
    def GetBendingShearModulus(self) -> float:
        """
         Bending Shear Modulus 
         Returns value (float): .
        """
        pass
    def GetBendingYoungsModulus(self) -> NXOpen.GeneralScalarTable:
        """
         Bending Youngs Modulus 
         Returns matrix ( NXOpen.GeneralScalarTable): .
        """
        pass
    def GetBottomFiberDistance(self) -> float:
        """
         Fetch the bottom fiber distance 
         Returns distance (float): .
        """
        pass
    def GetInterlaminarShearStress(self, use_ply_coordinates: bool, op_temp: List[float], nxx: List[float], nyy: List[float], nxy: List[float], mxx: List[float], myy: List[float], mxy: List[float], tsx: List[float], tsy: List[float]) -> Tuple[NXOpen.GeneralScalarTable, NXOpen.GeneralScalarTable]:
        """
         Obtain interlaminar values per ply per LC (stress_yz, stress_zx)
                    
         Returns A tuple consisting of (stress_yz, stress_zx). 
         - stress_yz is:  NXOpen.GeneralScalarTable. num_load_cases rows  and num_plies columns .
         - stress_zx is:  NXOpen.GeneralScalarTable.

        """
        pass
    def GetLaminateAngle(self) -> float:
        """
         Fetch the laminate angle in radians 
         Returns radians (float): .
        """
        pass
    def GetMaterialNames(self) -> List[str]:
        """
         The list of material names 
         Returns material_names (List[str]): .
        """
        pass
    def GetMaterialPlyCount(self, material_index: int) -> List[int]:
        """
         Number of plies per orientation using given material (index) 
         Returns plies (List[int]): .
        """
        pass
    def GetMaterialThickness(self, material_index: int) -> List[float]:
        """
         Thickness of plies per orientation using given material (index) 
         Returns thicknesses (List[float]): .
        """
        pass
    def GetMid1(self) -> NXOpen.GeneralScalarTable:
        """
         Mid1 
         Returns matrix ( NXOpen.GeneralScalarTable): .
        """
        pass
    def GetMid2(self) -> NXOpen.GeneralScalarTable:
        """
         Mid2 
         Returns matrix ( NXOpen.GeneralScalarTable): .
        """
        pass
    def GetMid3(self) -> NXOpen.GeneralScalarTable:
        """
         Mid3 
         Returns matrix ( NXOpen.GeneralScalarTable): .
        """
        pass
    def GetMid4(self) -> NXOpen.GeneralScalarTable:
        """
         Mid4 
         Returns matrix ( NXOpen.GeneralScalarTable): .
        """
        pass
    def GetOrientations(self) -> List[float]:
        """
         The list of orientations used 
         Returns orientations (List[float]): .
        """
        pass
    def GetPlyAngle(self, ply_index: int) -> float:
        """
         Ply angle 
         Returns value (float): .
        """
        pass
    def GetPlyAngles(self) -> List[float]:
        """
         Ply angles 
         Returns values (List[float]): .
        """
        pass
    def GetPlyId(self, ply_index: int) -> int:
        """
         Ply Id 
         Returns id (int): .
        """
        pass
    def GetPlyIds(self) -> List[int]:
        """
         Ply Ids 
         Returns ids (List[int]): .
        """
        pass
    def GetPlyMaterial(self, ply_index: int) -> NXOpen.PhysicalMaterial:
        """
         Ply material 
         Returns material ( NXOpen.PhysicalMaterial): .
        """
        pass
    def GetPlyMaterialName(self, ply_index: int) -> str:
        """
         Ply material name 
         Returns name (str): .
        """
        pass
    def GetPlyMaterialNames(self) -> List[str]:
        """
         Ply material names 
         Returns names (List[str]): .
        """
        pass
    def GetPlyMaterials(self) -> List[NXOpen.PhysicalMaterial]:
        """
         Ply materials 
         Returns materials ( NXOpen.PhysicalMaterial Li): .
        """
        pass
    def GetPlyThickness(self, ply_index: int) -> float:
        """
         Ply thickness 
         Returns value (float): .
        """
        pass
    def GetPlyThicknesses(self) -> List[float]:
        """
         Ply thicknesses 
         Returns values (List[float]): .
        """
        pass
    def GetPoissonsRatio(self) -> NXOpen.GeneralScalarTable:
        """
         Poissons Ratio 
         Returns matrix ( NXOpen.GeneralScalarTable): .
        """
        pass
    def GetReferencePlane(self) -> Laminate.LamRefLoc:
        """
         Top|Middle|Bottom|Specify 
         Returns plane ( Laminate.LamRefLoc NXOpen.CAE.A): .
        """
        pass
    def GetReferenceTemperature(self) -> float:
        """
         Fetch the reference temperature 
         Returns temp (float): .
        """
        pass
    def GetShearModulus(self) -> NXOpen.GeneralScalarTable:
        """
         Shear Modulus 
         Returns matrix ( NXOpen.GeneralScalarTable): .
        """
        pass
    def GetSpecificHeat(self) -> float:
        """
         Specific Heat 
         Returns value (float): .
        """
        pass
    def GetStiffnessA(self) -> NXOpen.GeneralScalarTable:
        """
         The A section of the ABD matrix 
         Returns matrix ( NXOpen.GeneralScalarTable): .
        """
        pass
    def GetStiffnessB(self) -> NXOpen.GeneralScalarTable:
        """
         The B section of the ABD matrix 
         Returns matrix ( NXOpen.GeneralScalarTable): .
        """
        pass
    def GetStiffnessD(self) -> NXOpen.GeneralScalarTable:
        """
         The D section of the ABD matrix 
         Returns matrix ( NXOpen.GeneralScalarTable): .
        """
        pass
    def GetStrainPerPly(self, use_ply_coordinates: bool, op_temp: List[float], nxx: List[float], nyy: List[float], nxy: List[float], mxx: List[float], myy: List[float], mxy: List[float]) -> Tuple[NXOpen.GeneralScalarTable, NXOpen.GeneralScalarTable, NXOpen.GeneralScalarTable]:
        """
         Obtain strain values per ply per LC 
         Returns A tuple consisting of (xx_strain, yy_strain, xy_strain). 
         - xx_strain is:  NXOpen.GeneralScalarTable. num_load_cases rows  and num_plies columns .
         - yy_strain is:  NXOpen.GeneralScalarTable.
         - xy_strain is:  NXOpen.GeneralScalarTable.

        """
        pass
    def GetStressPerPly(self, use_ply_coordinates: bool, op_temp: List[float], nxx: List[float], nyy: List[float], nxy: List[float], mxx: List[float], myy: List[float], mxy: List[float]) -> Tuple[NXOpen.GeneralScalarTable, NXOpen.GeneralScalarTable, NXOpen.GeneralScalarTable]:
        """
         Obtain stress values per ply per LC 
         Returns A tuple consisting of (xx_stress, yy_stress, xy_stress). 
         - xx_stress is:  NXOpen.GeneralScalarTable. num_load_cases rows  and num_plies columns .
         - yy_stress is:  NXOpen.GeneralScalarTable.
         - xy_stress is:  NXOpen.GeneralScalarTable.

        """
        pass
    def GetThermalConductivityCoeff(self) -> NXOpen.GeneralScalarTable:
        """
         Thermal Conductivity Coefficient 
         Returns matrix ( NXOpen.GeneralScalarTable): .
        """
        pass
    def GetThermalExpansionCoeff(self) -> NXOpen.GeneralScalarTable:
        """
         Thermal Expansion Coefficient 
         Returns matrix ( NXOpen.GeneralScalarTable): .
        """
        pass
    def GetTransverseShear(self) -> NXOpen.GeneralScalarTable:
        """
         The transverse shear matrix 
         Returns matrix ( NXOpen.GeneralScalarTable): .
        """
        pass
    def GetUnitSystem(self) -> NXOpen.CAE.AeroStructures.Author.CalculationContext.UnitSystem:
        """
         Unit system 
         Returns unitSystem ( NXOpen.CAE.AeroStructures.Author.CalculationContext.UnitSystem): .
        """
        pass
    def GetYoungsModulus(self) -> NXOpen.GeneralScalarTable:
        """
         Youngs Modulus 
         Returns matrix ( NXOpen.GeneralScalarTable): .
        """
        pass
    def IsInverted(self) -> bool:
        """
         Ask if the ply signs are inverted 
         Returns inverted (bool): .
        """
        pass
    def IsReversed(self) -> bool:
        """
         Ask if the ply order is reversed 
         Returns reversed (bool): .
        """
        pass
    def IsUsingPlyMaterial(self, ply_index: int) -> bool:
        """
         If this ply uses a ply material 
         Returns is_ply_material (bool): .
        """
        pass
    def IsUsingPlyMaterials(self) -> List[bool]:
        """
         If plies use ply materials 
         Returns using_ply_materials (List[bool]): .
        """
        pass
    def PrintLaminateInfo(self, plies: bool, props: bool, mats: bool) -> None:
        """
         Write out laminate information 
        """
        pass
    def SetUnitSystem(self, unitSystem: NXOpen.CAE.AeroStructures.Author.CalculationContext.UnitSystem) -> None:
        """
         Unit system 
        """
        pass
    def ToShorthandNotation(self) -> str:
        """
         Laminate shorthand notation 
         Returns shorthand_notation (str): .
        """
        pass
import NXOpen
class LoadCaseCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of AeroStruct LoadCases """
    def CreateLoadCaseListBuilder(self) -> LoadCaseListBuilder:
        """
         Creates a NXOpen.CAE.AeroStructures.LoadCaseListBuilder 
         Returns builder ( LoadCaseListBuilder NXOpen.CAE.A):   Builder object.
        """
        pass
    def DeleteLoadCase(self, loadcase: LoadCase) -> None:
        """
         Deletes a NXOpen.CAE.AeroStructures.LoadCase. 
        """
        pass
    def FindObject(self, name: str) -> LoadCase:
        """
         Finds the NXOpen.CAE.AeroStructures.LoadCase object with the given name. 
         Returns found ( LoadCase NXOpen.CAE.A):  NXOpen.CAE.AeroStructures.LoadCase object with this name. .
        """
        pass
import NXOpen
class LoadCaseListBuilder(NXOpen.Builder): 
    """ This is a manager to the loadcases of CAE.AeroStructures.BaseSolution class.
    """
    def RegisterCleanup(self) -> None:
        """
         Register the removable of orphaned load cases 
        """
        pass
import NXOpen
class LoadCaseSetBuilder(NXOpen.Builder): 
    """ This is a manager to the CAE.AeroStructures.LoadCaseSet class.
    Object of type CAE.AeroStructures.LoadCaseSet can be
    created and edited only through this class
    """
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the load case set description   
            
         
        """
        pass
    @Description.setter
    def Description(self, title: str):
        """
        Setter for property: (str) Description
         Returns the load case set description   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the load case set name  
            
         
        """
        pass
    @Name.setter
    def Name(self, title: str):
        """
        Setter for property: (str) Name
         Returns the load case set name  
            
         
        """
        pass
    def AddLoadCase(self, loadcase: LoadCase) -> None:
        """
         Insert a loadcase to the load case set builder 
        """
        pass
    def RemoveLoadCase(self, loadcase: LoadCase) -> None:
        """
         Remove a loadcase from the load case set builder 
        """
        pass
import NXOpen
class LoadCaseSetCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of AeroStruct LoadCases """
    def CloneLoadCaseSet(self, loadcaseset: LoadCaseSet) -> None:
        """
         Create a AeroStruct loadcase set. 
        """
        pass
    def CreateLoadCaseSet(self, builder: LoadCaseSetBuilder) -> None:
        """
         Create a AeroStruct loadcase set. 
        """
        pass
    def CreateLoadCaseSetBuilder(self, loadcaeset: LoadCaseSet) -> LoadCaseSetBuilder:
        """
         Creates a NXOpen.CAE.AeroStructures.LoadCaseSetBuilder 
         Returns builder ( LoadCaseSetBuilder NXOpen.CAE.A):  Builder object.
        """
        pass
    def DeleteLoadCaseSet(self, loadcaseset: LoadCaseSet) -> None:
        """
         Delete a AeroStruct loadcase set. 
        """
        pass
    def FindObject(self, name: str) -> LoadCaseSet:
        """
         Finds the NXOpen.CAE.AeroStructures.LoadCaseSet object with the given name. 
                    The name must be in the format {SolutionName}{LoadCaseName} where {SolutionName} is the name of
                    the referenced FE solution, and {LoadCaseName} is the name of the load case to find.  
                    {SolutionName}{LoadCaseName} is the value returned by NXOpen.CAE.AeroStructures.LoadCase.Name.
                 
         Returns found ( LoadCaseSet NXOpen.CAE.A):  NXOpen.CAE.AeroStructures.LoadCaseSet object with this name. .
        """
        pass
    def ImportLoadCaseSetFromFile(self, fileName: str) -> Tuple[LoadCaseSet, str, List[str]]:
        """
         Import Load Case Set from file 
         Returns A tuple consisting of (loadcaseset, errorMsg, warningMsg). 
         - loadcaseset is:  LoadCaseSet NXOpen.CAE.A. NXOpen.CAE.AeroStructures.LoadCaseSet .
         - errorMsg is: str.
         - warningMsg is: List[str].

        """
        pass
import NXOpen
class LoadCaseSetLoadCaseCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of AeroStruct LoadCases """
    def FindObject(self, name: str) -> LoadCase:
        """
         Finds the NXOpen.CAE.AeroStructures.LoadCase object with the given name. 
         Returns found ( LoadCase NXOpen.CAE.A):  NXOpen.CAE.AeroStructures.LoadCase object with this name. .
        """
        pass
import NXOpen
import NXOpen.CAE
class LoadCaseSet(NXOpen.NXObject): 
    """ Represents a NXOpen.CAE.AeroStructures.LoadCaseSet. """
    @property
    def LoadCaseCollection() -> LoadCaseSetLoadCaseCollection:
        """
         Returns the  NXOpen::CAE::AeroStructures::LoadCaseSetLoadCaseCollection  belonging to this 
                        When the base sim solution refers to Attached Results this collection is empty,
                        consider using  NXOpen::CAE::AeroStructures::LoadCaseSet::GetLoadcaseIterations  instead.
                        
        """
        pass
    def Export(self, fullPathName: str) -> None:
        """
         Export NXOpen.CAE.AeroStructures.LoadCaseSet to given file 
        """
        pass
    def GetLoadcaseIterations(self) -> List[NXOpen.CAE.LoadcaseIteration]:
        """
         Get a list of loadcase iterations in this set of the Attached Results
                        This method fails if the base solution does not refer to Attached Results. 
         Returns loadcaseIterations ( NXOpen.CAE.LoadcaseIteration Li): .
        """
        pass
import NXOpen
import NXOpen.CAE
class LoadCase(NXOpen.NXObject): 
    """ Represents a NXOpen.CAE.AeroStructures.LoadCase. """
    class LoadCaseType(Enum):
        """
        Members Include: 
         |Unitary|  Unitary loadcase 
         |Combined|  Combined loadcase 

        """
        Unitary: int
        Combined: int
        @staticmethod
        def ValueOf(value: int) -> LoadCase.LoadCaseType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BaseLoadCase(self) -> NXOpen.CAE.BaseLoadcase:
        """
        Getter for property: ( NXOpen.CAE.BaseLoadcase) BaseLoadCase
         Returns the associated CAE::BaseLoadCase   
            
         
        """
        pass
    @property
    def StrengthRequirement(self) -> str:
        """
        Getter for property: (str) StrengthRequirement
         Returns the strength requirement   
            
         
        """
        pass
import NXOpen
class LoadExtractionStrategy(NXOpen.NXObject): 
    """  Represents a proper load extraction strategy  """
    pass
import NXOpen
class LoadExtractionValue(NXOpen.NXObject): 
    """  Represents a proper load extraction value  """
    class ActiveStrategy(Enum):
        """
        Members Include: 
         |NotSet| 
         |User| 
         |Manual| 
         |FreeBody| 

        """
        NotSet: int
        User: int
        Manual: int
        FreeBody: int
        @staticmethod
        def ValueOf(value: int) -> LoadExtractionValue.ActiveStrategy:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Strategy(self) -> LoadExtractionStrategy:
        """
        Getter for property: ( LoadExtractionStrategy NXOpen.CAE.A) Strategy
         Returns the active strategy   
            
         
        """
        pass
    @Strategy.setter
    def Strategy(self, strat: LoadExtractionStrategy):
        """
        Setter for property: ( LoadExtractionStrategy NXOpen.CAE.A) Strategy
         Returns the active strategy   
            
         
        """
        pass
    @property
    def StrategyType(self) -> LoadExtractionValue.ActiveStrategy:
        """
        Getter for property: ( LoadExtractionValue.ActiveStrategy NXOpen.CAE.A) StrategyType
         Returns the active strategy type   
            
         
        """
        pass
    @StrategyType.setter
    def StrategyType(self, stratType: LoadExtractionValue.ActiveStrategy):
        """
        Setter for property: ( LoadExtractionValue.ActiveStrategy NXOpen.CAE.A) StrategyType
         Returns the active strategy type   
            
         
        """
        pass
import NXOpen
import NXOpen.Annotations
class LoadFilteringCalculationBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.CAE.AeroStructures.LoadFilteringCalculation builder. """
    @property
    def Annotation(self) -> NXOpen.Annotations.NoteBase:
        """
        Getter for property: ( NXOpen.Annotations.NoteBase) Annotation
         Returns the Annotation   
            
         
        """
        pass
    @Annotation.setter
    def Annotation(self, annotation: NXOpen.Annotations.NoteBase):
        """
        Setter for property: ( NXOpen.Annotations.NoteBase) Annotation
         Returns the Annotation   
            
         
        """
        pass
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the description.  
             
         
        """
        pass
    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
         Returns the description.  
             
         
        """
        pass
    @property
    def ExtractionSourceSet(self) -> ExtractionSourceSet:
        """
        Getter for property: ( ExtractionSourceSet NXOpen.CAE.A) ExtractionSourceSet
         Returns the Extraction sources   
            
         
        """
        pass
    @property
    def LoadCaseSet(self) -> LoadCaseSet:
        """
        Getter for property: ( LoadCaseSet NXOpen.CAE.A) LoadCaseSet
         Returns the LoadCaseSet used by the calculation  
            
         
        """
        pass
    @LoadCaseSet.setter
    def LoadCaseSet(self, lcset: LoadCaseSet):
        """
        Setter for property: ( LoadCaseSet NXOpen.CAE.A) LoadCaseSet
         Returns the LoadCaseSet used by the calculation  
            
         
        """
        pass
    @property
    def LocationCoordinateSystem(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) LocationCoordinateSystem
         Returns the calculation location with direction as a coordinate system.  
            
         
        """
        pass
    @LocationCoordinateSystem.setter
    def LocationCoordinateSystem(self, location: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) LocationCoordinateSystem
         Returns the calculation location with direction as a coordinate system.  
            
         
        """
        pass
    @property
    def LocationPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) LocationPoint
         Returns the calculation location as a single point.  
            
         
        """
        pass
    @LocationPoint.setter
    def LocationPoint(self, location: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) LocationPoint
         Returns the calculation location as a single point.  
            
         
        """
        pass
    @property
    def MethodKey(self) -> str:
        """
        Getter for property: (str) MethodKey
         Returns the MethodKey.  
           (This text contains non-printable ASCII characters.)   
         
        """
        pass
    @MethodKey.setter
    def MethodKey(self, methodkey: str):
        """
        Setter for property: (str) MethodKey
         Returns the MethodKey.  
           (This text contains non-printable ASCII characters.)   
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    @property
    def PropertyTable(self) -> PropTable:
        """
        Getter for property: ( PropTable NXOpen.CAE.A) PropertyTable
         Returns the Property Table   
            
         
        """
        pass
    def ClearAnnotationData(self) -> None:
        """
         Clear annotation data (no annotation will be generated)
        """
        pass
    def DuplicateCalculation(self) -> None:
        """
         Replace the current edited calculation by a copy 
        """
        pass
    def InitFromTemplate(self, templateFile: str) -> List[str]:
        """
         Initialize calculation from a template file 
         Returns errors (List[str]):  list of errors .
        """
        pass
    def InitializeFromTemplate(self, templateFile: str) -> None:
        """
         Initialize calculation from a template file 
        """
        pass
    def SetAnnotationData(self, annotData: AeroStructuresAnnotDataS) -> None:
        """
         Set annotation data 
        """
        pass
import NXOpen
class LoadFilteringCalculationCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of  CAE.AeroStructures.LoadFilteringCalculation. """
    def CloneCalculation(self, name: str, sourceCalculation: LoadFilteringCalculation) -> LoadFilteringCalculation:
        """
         Makes a copy of the calculation and adds it to the solution, adjusting the given name if it is a duplicate 
         Returns clonedCalculation ( LoadFilteringCalculation NXOpen.CAE.A): The resulting cloned NXOpen.CAE.AeroStructures.LoadFilteringCalculation .
        """
        pass
    def CloneCalculations(self, calculations: List[LoadFilteringCalculation]) -> None:
        """
         Clones calculations in bulk.
        """
        pass
    def CreateAnnotations(self, calculations: List[LoadFilteringCalculation], annotData: AeroStructuresAnnotDataS) -> None:
        """
         Create annotations in bulk 
        """
        pass
    def CreateLoadFilteringCalculationBuilder(self, calculation: LoadFilteringCalculation) -> LoadFilteringCalculationBuilder:
        """
         Creates a CAE.AeroStructures.LoadFilteringCalculationBuilder 
         Returns builder ( LoadFilteringCalculationBuilder NXOpen.CAE.A):  Builder object.
        """
        pass
    def CreateLoadFilteringCalculationBuilderForDuplication(self, calculation: LoadFilteringCalculation) -> LoadFilteringCalculationBuilder:
        """
         Creates a CAE.AeroStructures.LoadFilteringCalculationBuilder for duplication
         Returns builder ( LoadFilteringCalculationBuilder NXOpen.CAE.A):  Builder object.
        """
        pass
    def DeleteCalculation(self, calculation: LoadFilteringCalculation) -> None:
        """
         Removes the calculation from the solution 
        """
        pass
    def DeleteCalculations(self, calculations: List[LoadFilteringCalculation]) -> None:
        """
         Deletes calculations in bulk.
        """
        pass
    def FindObject(self, name: str) -> LoadFilteringCalculation:
        """
         Finds the NXOpen.CAE.AeroStructures.LoadFilteringCalculation object with the given name. 
         Returns calculation ( LoadFilteringCalculation NXOpen.CAE.A):  NXOpen.CAE.AeroStructures.LoadFilteringCalculation object with this name. .
        """
        pass
    def RenameCalculations(self, name: str, calculations: List[LoadFilteringCalculation]) -> None:
        """
         Renames calculations in bulk.
        """
        pass
import NXOpen
class LoadFilteringCalculation(BaseCalculation): 
    """  This is the LoadFilteringCalculation  """
    def GetResultSelectedLoadCaseNames(self) -> List[str]:
        """
         Get the list of selected load case names in the last computed result 
         Returns loadCaseNames (List[str]): .
        """
        pass
    def GetScalarFieldExpression(self, inputName: str) -> NXOpen.Expression:
        """
         Get the expression of a scalar field input parameter 
         Returns exp ( NXOpen.Expression): .
        """
        pass
    def ReplaceScalarFieldExpression(self, inputName: str, exp: NXOpen.Expression) -> None:
        """
         Replace the expression of a scalar field input parameter
                        and removes old expression from the expression manager. 
        """
        pass
import NXOpen
import NXOpen.CAE
class LoadFilteringSolutionBuilder(NXOpen.Builder): 
    """ This is a manager to the CAE.AeroStructures.LoadFilteringSolution class.
    Object of type CAE.AeroStructures.LoadFilteringSolution can be
    created and edited only through this class
    """
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns  a Get the metasolution description  
            
         
        """
        pass
    @Description.setter
    def Description(self, title: str):
        """
        Setter for property: (str) Description
         Returns  a Get the metasolution description  
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the metasolution name  
            
         
        """
        pass
    @Name.setter
    def Name(self, title: str):
        """
        Setter for property: (str) Name
         Returns the metasolution name  
            
         
        """
        pass
    @property
    def ReferenceSolution(self) -> NXOpen.CAE.SimSolution:
        """
        Getter for property: ( NXOpen.CAE.SimSolution) ReferenceSolution
         Returns the referenced FE-Solution of the AeroStructure solution   
            
         
        """
        pass
    @ReferenceSolution.setter
    def ReferenceSolution(self, referenceSolution: NXOpen.CAE.SimSolution):
        """
        Setter for property: ( NXOpen.CAE.SimSolution) ReferenceSolution
         Returns the referenced FE-Solution of the AeroStructure solution   
            
         
        """
        pass
    @property
    def UnitSystem(self) -> str:
        """
        Getter for property: (str) UnitSystem
         Returns the unit system of the load filtering solution  
            
         
        """
        pass
    @UnitSystem.setter
    def UnitSystem(self, unit_system: str):
        """
        Setter for property: (str) UnitSystem
         Returns the unit system of the load filtering solution  
            
         
        """
        pass
import NXOpen
class LoadFilteringSolutionCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of load filtering solution. """
    def CloneSolution(self, source: LoadFilteringSolution) -> LoadFilteringSolution:
        """
         Clones a AeroStruct load filtering solution. 
         Returns copy ( LoadFilteringSolution NXOpen.CAE.A):  Cloned load filtering solution .
        """
        pass
    def CreateLoadFilteringSolutionBuilder(self, loadFilteringSol: LoadFilteringSolution) -> LoadFilteringSolutionBuilder:
        """
         Creates the builder object of AeroStruct load filtering solution. 
         Returns builder ( LoadFilteringSolutionBuilder NXOpen.CAE.A):   .
        """
        pass
    def DeleteSolution(self, metasolution: LoadFilteringSolution) -> None:
        """
         Delete a AeroStruct load filtering solution. 
        """
        pass
    def FindObject(self, name: str) -> LoadFilteringSolution:
        """
         Finds a AeroStruct load filtering solution with a specified name. 
         Returns found ( LoadFilteringSolution NXOpen.CAE.A):  The AeroStruct load filtering solution .
        """
        pass
    def GetActiveLoadfilteringcalculation(self) -> LoadFilteringCalculation:
        """
         Returns the load filtering calculation. 
         Returns activeCalculation ( LoadFilteringCalculation NXOpen.CAE.A):  The active Load Filtering calculation .
        """
        pass
    def GetActiveSolution(self) -> LoadFilteringSolution:
        """
         Returns the active load filtering solution. 
         Returns activeSolution ( LoadFilteringSolution NXOpen.CAE.A):  The active load filtering solution .
        """
        pass
    def SetActiveLoadfilteringcalculation(self, activeCalculation: LoadFilteringCalculation) -> None:
        """
         Sets the active load filtering calculation. 
        """
        pass
    def SetActiveSolution(self, source: LoadFilteringSolution) -> None:
        """
         Activates the load filtering solution. 
        """
        pass
import NXOpen.CAE
class LoadFilteringSolution(BaseSolution): 
    """ Represent a NXOpen.CAE.AeroStructures.LoadFilteringSolution. """
    @property
    def LoadFilteringCalculationCollection() -> LoadFilteringCalculationCollection:
        """
         Returns the  NXOpen::CAE::AeroStructures::LoadFilteringCalculationCollection  belonging to this 
        """
        pass
import NXOpen
class LocalLaminate(Laminate): 
    """ Represents a NXOpen.CAE.AeroStructures.LocalLaminate object. """
    def AddPly(self, material: NXOpen.PhysicalMaterial, thickness: float, thicknessUnit: NXOpen.Unit, angle: float, angleUnit: NXOpen.Unit) -> int:
        """
         Add a ply to the laminate. Always added to the end of the original
                    stack. 
         Returns plyIndex (int): .
        """
        pass
    def AddPlyByMaterialName(self, materialName: str, thickness: float, thicknessUnit: NXOpen.Unit, angle: float, angleUnit: NXOpen.Unit) -> int:
        """
         Add a ply to the laminate using a material name. Always added to
                    the end of the original stack. 
         Returns plyIndex (int): .
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called, it is
                    illegal to use the object. In .NET, this method is automatically
                    called when the object is deleted by the garbage collector. 
        """
        pass
    def SetBottomFiberDistance(self, distance: float, distanceUnit: NXOpen.Unit) -> None:
        """
         Set bottom fiber distance 
        """
        pass
    def SetInverted(self, inverted: bool) -> None:
        """
         Invert ply angles 
        """
        pass
    def SetLaminateAngle(self, angle: float, angleUnit: NXOpen.Unit) -> None:
        """
         Set laminate angle 
        """
        pass
    def SetPlyAngle(self, plyIndex: int, angle: float, angleUnit: NXOpen.Unit) -> None:
        """
         Set the angle for the ply 
        """
        pass
    def SetPlyMaterial(self, plyIndex: int, material: NXOpen.PhysicalMaterial) -> None:
        """
         Set the Physical Material for the ply 
        """
        pass
    def SetPlyMaterialByName(self, plyIndex: int, materialName: str) -> None:
        """
         Set the Material for the ply by name 
        """
        pass
    def SetPlyThickness(self, plyIndex: int, thickness: float, thicknessUnit: NXOpen.Unit) -> None:
        """
         Set the thickness for the ply 
        """
        pass
    def SetReferencePlane(self, location: Laminate.LamRefLoc) -> None:
        """
         Top|Middle|Bottom|Specify 
        """
        pass
    def SetReferenceTemperature(self, temperature: float, temperatureUnit: NXOpen.Unit) -> None:
        """
         Set reference temperature 
        """
        pass
    def SetReversed(self, reversed: bool) -> None:
        """
         Reverse ply order 
        """
        pass
import NXOpen
class ManualLoadExtraction(LoadExtractionStrategy): 
    """  This is the Manual LoadExtraction class  """
    def GetValues(self, unit: NXOpen.Unit) -> Tuple[List[str], List[float]]:
        """
         Get values in given units 
         Returns A tuple consisting of (keys, values). 
         - keys is: List[str]. list of keys (loadcase names) .
         - values is: List[float]. list of values .

        """
        pass
    def SetValues(self, unit: NXOpen.Unit, keys: List[str], values: List[float]) -> None:
        """
         Set values in given units 
        """
        pass
import NXOpen.CAE
class MarginAnnotBuilder(NXOpen.CAE.CaeNoteBuilder): 
    """ Represents a Margin annotation builder class """
    pass
import NXOpen
import NXOpen.Annotations
class MarginAnnotCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Margin annotation """
    def CreateMarginAnnot(self, label_data: NXOpen.Annotations.LabelData) -> MarginAnnot:
        """
         Creates a Margin Annotation 
         Returns annotation ( MarginAnnot NXOpen.CAE.A):  New Margin annotation .
        """
        pass
    def CreateMarginAnnotBuilder(self, annotation: NXOpen.Annotations.SimpleDraftingAid) -> MarginAnnotBuilder:
        """
         Creates a builder for Margin annotation 
         Returns builder ( MarginAnnotBuilder NXOpen.CAE.A): .
        """
        pass
    def FindObject(self, name: str) -> MarginAnnot:
        """
         Finds a margin annotation with a specified name. 
         Returns found ( MarginAnnot NXOpen.CAE.A):  The margin annot .
        """
        pass
    def HideAnnotations(self, annot_array: List[MarginAnnot]) -> None:
        """
         Hide Annotation 
        """
        pass
    def RelocateAnnotations(self, annot_array: List[MarginAnnot]) -> bool:
        """
         Relocate Margin annotations in bulk 
         Returns relocated (bool):  returns true if the annotation(s) is truly relocated  .
        """
        pass
    def ReverseLeaders(self, annot_array: List[MarginAnnot]) -> None:
        """
         Reverse Margin annotation leaders 
        """
        pass
    def ScaleTextSize(self, annot_array: List[MarginAnnot], scale: float) -> None:
        """
         Scale Margin annotation text size 
        """
        pass
    def ShowAnnotations(self, annot_array: List[MarginAnnot]) -> None:
        """
         Show Annotation 
        """
        pass
    def UpdateAnnotations(self, annot_array: List[MarginAnnot], annotData: AeroStructuresAnnotDataS) -> None:
        """
         Update Margin annotations preference 
        """
        pass
import NXOpen.CAE
class MarginAnnot(NXOpen.CAE.CaeLabel): 
    """ Represents an object that manages annotation for CAE """
    pass
import NXOpen
import NXOpen.Annotations
class MarginCalculationBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.CAE.AeroStructures.MarginCalculation builder. """
    @property
    def Annotation(self) -> NXOpen.Annotations.NoteBase:
        """
        Getter for property: ( NXOpen.Annotations.NoteBase) Annotation
         Returns the Annotation   
            
         
        """
        pass
    @Annotation.setter
    def Annotation(self, annotation: NXOpen.Annotations.NoteBase):
        """
        Setter for property: ( NXOpen.Annotations.NoteBase) Annotation
         Returns the Annotation   
            
         
        """
        pass
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the description.  
             
         
        """
        pass
    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
         Returns the description.  
             
         
        """
        pass
    @property
    def ExtractionSourceSet(self) -> ExtractionSourceSet:
        """
        Getter for property: ( ExtractionSourceSet NXOpen.CAE.A) ExtractionSourceSet
         Returns the Extraction sources   
            
         
        """
        pass
    @property
    def LoadCaseSet(self) -> LoadCaseSet:
        """
        Getter for property: ( LoadCaseSet NXOpen.CAE.A) LoadCaseSet
         Returns the LoadCaseSet used by the calculation  
            
         
        """
        pass
    @LoadCaseSet.setter
    def LoadCaseSet(self, lcset: LoadCaseSet):
        """
        Setter for property: ( LoadCaseSet NXOpen.CAE.A) LoadCaseSet
         Returns the LoadCaseSet used by the calculation  
            
         
        """
        pass
    @property
    def LocationCoordinateSystem(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) LocationCoordinateSystem
         Returns the calculation location with direction as a coordinate system.  
            
         
        """
        pass
    @LocationCoordinateSystem.setter
    def LocationCoordinateSystem(self, location: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) LocationCoordinateSystem
         Returns the calculation location with direction as a coordinate system.  
            
         
        """
        pass
    @property
    def LocationPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) LocationPoint
         Returns the calculation location as a single point.  
            
         
        """
        pass
    @LocationPoint.setter
    def LocationPoint(self, location: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) LocationPoint
         Returns the calculation location as a single point.  
            
         
        """
        pass
    @property
    def MethodKey(self) -> str:
        """
        Getter for property: (str) MethodKey
         Returns the MethodKey.  
           (This text contains non-printable ASCII characters.)   
         
        """
        pass
    @MethodKey.setter
    def MethodKey(self, methodkey: str):
        """
        Setter for property: (str) MethodKey
         Returns the MethodKey.  
           (This text contains non-printable ASCII characters.)   
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    @property
    def PropertyTable(self) -> PropTable:
        """
        Getter for property: ( PropTable NXOpen.CAE.A) PropertyTable
         Returns the Property Table   
            
         
        """
        pass
    def ClearAnnotationData(self) -> None:
        """
         Clear annotation data (no annotation will be generated)
        """
        pass
    def CreatePropertyTable(self) -> PropTable:
        """
         Creates a PropertyTable 
         Returns propertytable ( PropTable NXOpen.CAE.A):  the property table.
        """
        pass
    def DuplicateCalculation(self) -> None:
        """
         Replace the current edited calculation by a copy 
        """
        pass
    def InitFromTemplate(self, templateFile: str) -> List[str]:
        """
         Initialize calculation from a template file 
         Returns errors (List[str]):  list of errors .
        """
        pass
    def InitializeFromTemplate(self, templateFile: str) -> None:
        """
         Initialize calculation from a template file 
        """
        pass
    def SetAnnotationData(self, annotData: AeroStructuresAnnotDataS) -> None:
        """
         Set annotation data 
        """
        pass
import NXOpen
class MarginCalculationCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of  CAE.AeroStructures.MarginCalculation. """
    def CloneCalculation(self, name: str, sourcemargincalculation: MarginCalculation) -> MarginCalculation:
        """
         Makes a copy of the calculation and adds it to the margin solution, adjusting the given name if it is a duplicate 
         Returns clonedmargincalculation ( MarginCalculation NXOpen.CAE.A): The resulting cloned NXOpen.CAE.AeroStructures.MarginCalculation .
        """
        pass
    def CloneCalculations(self, calculations: List[MarginCalculation]) -> None:
        """
         Clones calculations in bulk.
        """
        pass
    def CreateAnnotations(self, marginCalculations: List[MarginCalculation], annotData: AeroStructuresAnnotDataS) -> None:
        """
         Create annotations in bulk 
        """
        pass
    def CreateMarginCalculationBuilder(self, margincalculation: MarginCalculation) -> MarginCalculationBuilder:
        """
         Creates a CAE.AeroStructures.MarginCalculationBuilder 
         Returns builder ( MarginCalculationBuilder NXOpen.CAE.A):  Builder object.
        """
        pass
    def CreateMarginCalculationBuilderForDuplication(self, margincalculation: MarginCalculation) -> MarginCalculationBuilder:
        """
         Creates a CAE.AeroStructures.MarginCalculationBuilder for duplication
         Returns builder ( MarginCalculationBuilder NXOpen.CAE.A):  Builder object.
        """
        pass
    def CreateMultiMarginCalculationBuilder(self, margincalculation: MarginCalculation) -> MultiMarginCalculationBuilder:
        """
         Creates a CAE.AeroStructures.MultiMarginCalculationBuilder 
         Returns builder ( MultiMarginCalculationBuilder NXOpen.CAE.A):  Builder object.
        """
        pass
    def DeleteCalculation(self, margincalculation: MarginCalculation) -> None:
        """
         Removes the calculation from the solution 
        """
        pass
    def DeleteCalculations(self, calculations: List[MarginCalculation]) -> None:
        """
         Deletes calculations in bulk.
        """
        pass
    def FindObject(self, name: str) -> MarginCalculation:
        """
         Finds the NXOpen.CAE.AeroStructures.MarginCalculation object with the given name. 
         Returns found ( MarginCalculation NXOpen.CAE.A):  NXOpen.CAE.AeroStructures.MarginCalculation object with this name. .
        """
        pass
    def RenameCalculations(self, name: str, calculations: List[MarginCalculation]) -> None:
        """
         Renames calculations in bulk.
        """
        pass
import NXOpen
class MarginCalculation(BaseCalculation): 
    """  This is the MarginCalculation  """
    def GetResultMsValue(self, failureModeName: str, loadCaseName: str) -> float:
        """
         Get an MS value in the last computed result.
                        Both the load case's Name and JournalIdentifier are supported. 
         Returns value (float): .
        """
        pass
    def GetScalarFieldExpression(self, inputName: str) -> NXOpen.Expression:
        """
         Get the expression of a scalar field input parameter 
         Returns exp ( NXOpen.Expression): .
        """
        pass
    def ReplaceScalarFieldExpression(self, inputName: str, exp: NXOpen.Expression) -> None:
        """
         Replace the expression of a scalar field input parameter
                        and removes old expression from the expression manager. 
        """
        pass
import NXOpen
class MarginResultIterator(NXOpen.NXObject): 
    """  Iterate over the solutions of a query.
        Each solution is a CAE.AeroStructures.MarginResultTableRow.
        CAE.AeroStructures.MarginResultIterator.Next advances to the next row. 
        CAE.AeroStructures.MarginResultIterator.GetCurrentRow retreives the current row.
         """
    def GetCurrentRow(self) -> MarginResultTableRow:
        """
         Returns the current CAE.AeroStructures.MarginResultTableRow
         Returns row ( MarginResultTableRow NXOpen.CAE.A):  the current CAE.AeroStructures.MarginResultTableRow .
        """
        pass
    def Next(self) -> bool:
        """
         Increments the iterator to the next row. Returns false if the iterator was already positioned at the last row. 
                        If successful, calling CAE.AeroStructures.MarginResultIterator.GetCurrentRow will return the subsequent row.
         Returns success (bool): .
        """
        pass
import NXOpen
class MarginResultQuery(NXOpen.NXObject): 
    """  CAE.AeroStructures.MarginResultQuery defines a query on all, or a subset, of the available margin results.
                      Depending on the chosen constructor it is possible to pre-filter the results before the rank calculation takes place.
                      It is also possible to specify a filter that acts after the rank calculation has taken place.
                      Post filters offer more flexibility in terms of constraints than pre filters.
                      An instance of this class can be created using the following methods:
                      CAE.AeroStructures.MarginSolution.CreateMarginResultQuery  or
                      CAE.AeroStructures.MarginResultTableDataProvider.CreateQuery 
                  
                      In order to use the query, request an iterator and use that to obtain one row at a time.
         """
    def CreateIterator(self) -> MarginResultIterator:
        """
         Creates a new iterator 
         Returns iterator ( MarginResultIterator NXOpen.CAE.A):  output iterator .
        """
        pass
    def GetMaximumRowCount(self) -> int:
        """
         Get the maximum row count resulting from this query. 
                        The actual count could be lower and can be retrieved by the method CAE.AeroStructures.MarginResultQuery.GetRowCount  
                        but this might require more time to compute if the query includes a filter
         Returns count (int): .
        """
        pass
    def GetRowCount(self) -> int:
        """
         Get the row count resulting from this query. 
                        If the query contains filtering this method takes more time than CAE.AeroStructures.MarginResultQuery.GetMaximumRowCount  
                        
         Returns count (int): .
        """
        pass
import NXOpen
class MarginResultTableDataProvider(NXOpen.NXObject): 
    """  CAE.AeroStructures.MarginResultTableDataProvider is used by the global results editor.
                      It provides a table view of the results of a subset of the calculations in a margin solution.
                      The columns can be configured using CAE.AeroStructures.MarginResultTableDataProvider.RegisterColumn.
                      CAE.AeroStructures.MarginResultTableDataProvider is also a data provider for CAE.AeroStructures.MarginResultQuery object.
                      The method CAE.AeroStructures.MarginResultTableDataProvider.RegisterColumn creates a CAE.AeroStructures.MarginResultQuery that 
                      represents the result data present in this table provider. 
                        """
    class ColumnType(Enum):
        """
        Members Include: 
         |Calculation| 
         |FailureMode| 
         |LoadCase| 
         |MarginOfSafety| 
         |GlobalRank| 
         |RankByCalculation| 
         |RankByFailureMode| 
         |RankByLoadCase| 
         |Method| 
         |FemSolution| 
         |SelectedLoadCaseCount| 
         |LoadCaseCount| 
         |LoadCaseSet| 
         |ReserveFactor| 
         |Sentinel| 

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
        @staticmethod
        def ValueOf(value: int) -> MarginResultTableDataProvider.ColumnType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def CreateQuery(self) -> MarginResultQuery:
        """
         Creates a query based on this table data provider. For this query to be useful the appropriate columns must be registered.
         Returns query ( MarginResultQuery NXOpen.CAE.A):  output query.
        """
        pass
    def RegisterAllColumns(self) -> None:
        """
         Register all columns listed in the ColumnType enumeration (except for the sentinel value)  
        """
        pass
    def RegisterColumn(self, columnIdx: int, columnType: MarginResultTableDataProvider.ColumnType) -> None:
        """
         Register a new column 
        """
        pass
import NXOpen
class MarginResultTableRowFilter(NXOpen.TransientObject): 
    """  A MarginResultTableRowFilter holds conditions which can be applied to a MarginResultTableRow.
            The filter is used to create a MarginResultTableFilterQuery which is used to filter out rows from a 
            result table or from another input query.      """
    class NumericComparisonOperator(Enum):
        """
        Members Include: 
         |Equal| 
         |NotEqual| 
         |LessThan| 
         |LessOrEqual| 
         |GreaterThan| 
         |GreaterOrEqual| 

        """
        Equal: int
        NotEqual: int
        LessThan: int
        LessOrEqual: int
        GreaterThan: int
        GreaterOrEqual: int
        @staticmethod
        def ValueOf(value: int) -> MarginResultTableRowFilter.NumericComparisonOperator:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class StringComparisonOperator(Enum):
        """
        Members Include: 
         |Equal| 
         |NotEqual| 
         |LessThan| 
         |LessOrEqual| 
         |GreaterThan| 
         |GreaterOrEqual| 
         |StartsWith| 
         |EndsWith| 
         |Contains| 

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
        @staticmethod
        def ValueOf(value: int) -> MarginResultTableRowFilter.StringComparisonOperator:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def AddCiCondition(self, columnType: MarginResultTableDataProvider.ColumnType, op: MarginResultTableRowFilter.StringComparisonOperator, value: str) -> None:
        """
         Add a new case-insensitive condition on a string column 
        """
        pass
    @overload
    def AddCondition(self, columnType: MarginResultTableDataProvider.ColumnType, op: MarginResultTableRowFilter.NumericComparisonOperator, value: int) -> None:
        """
         Add a new condition on an integer column 
        """
        pass
    @overload
    def AddCondition(self, columnType: MarginResultTableDataProvider.ColumnType, op: MarginResultTableRowFilter.NumericComparisonOperator, value: float) -> None:
        """
         Add a new condition on a numeric column 
        """
        pass
    @overload
    def AddCondition(self, columnType: MarginResultTableDataProvider.ColumnType, op: MarginResultTableRowFilter.StringComparisonOperator, value: str) -> None:
        """
         Add a new condition on a string column 
        """
        pass
    @overload
    def AddCondition(self, otherFilter: MarginResultTableRowFilter) -> None:
        """
         Adds another filter to the conditions of the current filter
                         if the current filter is a conjunction the new filter is logically AND-ed 
                         if the current filter is a disjunction the new filter is logically OR-ed
        """
        pass
    def AndWith(self, otherFilter: MarginResultTableRowFilter) -> None:
        """
         Logically AND with the current filter 
        """
        pass
    def Dispose(self) -> None:
        """
         Dispose 
        """
        pass
    def OrWith(self, otherFilter: MarginResultTableRowFilter) -> None:
        """
         Logically OR with the current filter 
        """
        pass
import NXOpen
class MarginResultTableRow(NXOpen.TransientObject): 
    """  MarginResultTableRow represents one row in a result table and is returned by a query iterator  """
    @property
    def Calculation(self) -> MarginCalculation:
        """
        Getter for property: ( MarginCalculation NXOpen.CAE.A) Calculation
         Returns the calculation object for this row   
            
         
        """
        pass
    @property
    def CalculationName(self) -> str:
        """
        Getter for property: (str) CalculationName
         Returns the calculation name for this row   
            
         
        """
        pass
    @property
    def FailureModeName(self) -> str:
        """
        Getter for property: (str) FailureModeName
         Returns the failure mode name for this row   
            
         
        """
        pass
    @property
    def FemSolutionName(self) -> str:
        """
        Getter for property: (str) FemSolutionName
         Returns the fem solution name for this row   
            
         
        """
        pass
    @property
    def GlobalRank(self) -> int:
        """
        Getter for property: (int) GlobalRank
         Returns the global rank for this row   
            
         
        """
        pass
    @property
    def LoadCaseName(self) -> str:
        """
        Getter for property: (str) LoadCaseName
         Returns the load case name for this row   
            
         
        """
        pass
    @property
    def MarginOfSafety(self) -> float:
        """
        Getter for property: (float) MarginOfSafety
         Returns the margin of safety for this row   
            
         
        """
        pass
    @property
    def MethodName(self) -> str:
        """
        Getter for property: (str) MethodName
         Returns the method name implementing the calculation for this row   
            
         
        """
        pass
    @property
    def RankByCalculation(self) -> int:
        """
        Getter for property: (int) RankByCalculation
         Returns the rank by calculation for this row   
            
         
        """
        pass
    @property
    def RankByFailureMode(self) -> int:
        """
        Getter for property: (int) RankByFailureMode
         Returns the rank by failure_mode for this row   
            
         
        """
        pass
    @property
    def RankByLoadCase(self) -> int:
        """
        Getter for property: (int) RankByLoadCase
         Returns the rank by load case for this row   
            
         
        """
        pass
    @property
    def ReserveFactor(self) -> float:
        """
        Getter for property: (float) ReserveFactor
         Returns the reserve factor for this row   
            
         
        """
        pass
    def Dispose(self) -> None:
        """
         Dispose 
        """
        pass
    def GetInputBooleanValue(self, parameterName: str) -> bool:
        """
         Get the value of a boolean input parameter for this row 
         Returns value (bool): .
        """
        pass
    def GetInputIntegerValue(self, parameterName: str) -> int:
        """
         Get the value of an integer input parameter for this row 
         Returns value (int): .
        """
        pass
    def GetInputLoad(self, parameterName: str) -> List[float]:
        """
         Get the aggregated or non aggregated load values of an input parameter for this row.
                            If the load values were aggregated, the output will be an array with only one value.
                            If the values were not aggregated, the output will be an array with one value per element or node. 
         Returns values (List[float]): .
        """
        pass
    def GetInputScalarMeasure(self, parameterName: str) -> str:
        """
         Get the measure of a scalar input parameter for this row. 
         Returns measure (str): .
        """
        pass
    def GetInputScalarUnit(self, parameterName: str) -> NXOpen.Unit:
        """
         Get the unit of a scalar input parameter for this row 
         Returns unit_type ( NXOpen.Unit):  the unit of the value returned by CAE.AeroStructures.MarginResultTableRow.GetInputScalarValue.
        """
        pass
    def GetInputScalarValue(self, parameterName: str) -> float:
        """
         Get the value of a scalar input parameter for this row 
         Returns value (float): .
        """
        pass
    def GetInputStringValue(self, parameterName: str) -> str:
        """
         Get the value of a string input parameter for this row 
         Returns value (str): .
        """
        pass
    def GetOutputBooleanValue(self, parameterName: str) -> bool:
        """
         Get the value of a boolean output parameter for this row 
         Returns value (bool): .
        """
        pass
    def GetOutputIntegerValue(self, parameterName: str) -> int:
        """
         Get the value of an integer output parameter for this row 
         Returns value (int): .
        """
        pass
    def GetOutputScalarMeasure(self, parameterName: str) -> str:
        """
         Get the measure of a scalar output parameter for this row. 
         Returns measure (str): .
        """
        pass
    def GetOutputScalarUnit(self, parameterName: str) -> NXOpen.Unit:
        """
         Get the unit of a scalar output parameter for this row.
                        An exception(code "3520027") will be thrown if no unit can be found with the given parameter.
                        An exception(code "3520046") will be thrown if the unit measure of the given parameter is Unitless,
                        this API returns NULL as well.
                        
         Returns unit_type ( NXOpen.Unit):  the unit of the value returned by CAE.AeroStructures.MarginResultTableRow.GetOutputScalarValue.
        """
        pass
    def GetOutputScalarValue(self, parameterName: str) -> float:
        """
         Get the value of a scalar output parameter for this row 
         Returns value (float): .
        """
        pass
    def GetOutputStringValue(self, parameterName: str) -> str:
        """
         Get the value of a string output parameter for this row 
         Returns value (str): .
        """
        pass
import NXOpen
import NXOpen.CAE
class MarginSolutionBuilder(NXOpen.Builder): 
    """ This is a manager to the CAE.AeroStructures.MarginSolution class.
    Object of type CAE.AeroStructures.MarginSolution can be
    created and edited only through this class
    """
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns  a Get the metasolution description  
            
         
        """
        pass
    @Description.setter
    def Description(self, title: str):
        """
        Setter for property: (str) Description
         Returns  a Get the metasolution description  
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the metasolution name  
            
         
        """
        pass
    @Name.setter
    def Name(self, title: str):
        """
        Setter for property: (str) Name
         Returns the metasolution name  
            
         
        """
        pass
    @property
    def ReferenceSolution(self) -> NXOpen.CAE.SimSolution:
        """
        Getter for property: ( NXOpen.CAE.SimSolution) ReferenceSolution
         Returns the referenced FE-Solution of the AeroStructure solution   
            
         
        """
        pass
    @ReferenceSolution.setter
    def ReferenceSolution(self, referenceSolution: NXOpen.CAE.SimSolution):
        """
        Setter for property: ( NXOpen.CAE.SimSolution) ReferenceSolution
         Returns the referenced FE-Solution of the AeroStructure solution   
            
         
        """
        pass
    @property
    def UnitSystem(self) -> str:
        """
        Getter for property: (str) UnitSystem
         Returns the unit system of the margin solution  
            
         
        """
        pass
    @UnitSystem.setter
    def UnitSystem(self, unit_system: str):
        """
        Setter for property: (str) UnitSystem
         Returns the unit system of the margin solution  
            
         
        """
        pass
import NXOpen
class MarginSolutionCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of  margin solution. """
    def CloneMarginSolution(self, source: MarginSolution) -> MarginSolution:
        """
         Clones a AeroStruct marginsolution. 
         Returns copy ( MarginSolution NXOpen.CAE.A):  Cloned metasolution .
        """
        pass
    def CreateMarginSolutionBuilder(self, metasolution: MarginSolution) -> MarginSolutionBuilder:
        """
         Creates the builder object of AeroStruct meta solution. 
         Returns builder ( MarginSolutionBuilder NXOpen.CAE.A):   .
        """
        pass
    def DeleteMarginSolution(self, metasolution: MarginSolution) -> None:
        """
         Delete a AeroStruct metasolution. 
        """
        pass
    def FindObject(self, name: str) -> MarginSolution:
        """
         Finds a AeroStruct margin solution with a specified name. 
         Returns found ( MarginSolution NXOpen.CAE.A):  The AeroStruct margin solution .
        """
        pass
    def GetActiveMargincalculation(self) -> MarginCalculation:
        """
         Returns the active margincalculation. 
         Returns activeCalculation ( MarginCalculation NXOpen.CAE.A):  The active margincalculation .
        """
        pass
    def GetActiveMarginsolution(self) -> MarginSolution:
        """
         Returns the active marginsolution. 
         Returns activeSolution ( MarginSolution NXOpen.CAE.A):  The active metasolution .
        """
        pass
    def SetActiveMargincalculation(self, activeCalculation: MarginCalculation) -> None:
        """
         Sets the active margin calculation. 
        """
        pass
    def SetActiveMarginsolution(self, source: MarginSolution) -> None:
        """
         Activates the marginsolution. 
        """
        pass
import NXOpen.Report
class MarginSolution(BaseSolution): 
    """ Represents a NXOpen.CAE.AeroStructures.MarginSolution. """
    @property
    def MarginCalculationCollection() -> MarginCalculationCollection:
        """
         Returns the  NXOpen::CAE::AeroStructures::MarginCalculationCollection  belonging to this 
        """
        pass
    @property
    def ExpressionCollection() -> ExpressionCollection:
        """
         Returns the  NXOpen::CAE::AeroStructures::ExpressionCollection  belonging to this 
        """
        pass
    @property
    def GraphicalReportCollection() -> GraphicalReportCollection:
        """
         Returns the  NXOpen::CAE::AeroStructures::GraphicalReportCollection  belonging to this 
        """
        pass
    def CreateCriticalMs(self, name: str, marginCalculations: List[MarginCalculation]) -> ExpressionResult:
        """
         Create critical MS expression 
         Returns expression ( ExpressionResult NXOpen.CAE.A):  The critical MS expression .
        """
        pass
    @overload
    def CreateMarginResultQuery(self, filter: MarginResultTableRowFilter) -> MarginResultQuery:
        """
         Creates a NXOpen.CAE.AeroStructures.MarginResultQuery 
                     containing all the results of every calculation that has been solved and belongs to this solution
                     If a non-null CAE.AeroStructures.MarginResultTableRowFilter is passed as argument
                     the results are further post-filtered (after the rank calculation has taken place) according to that filter
                    
         Returns query ( MarginResultQuery NXOpen.CAE.A):  output query .
        """
        pass
    @overload
    def CreateMarginResultQuery(self, marginCalculations: List[MarginCalculation], filter: MarginResultTableRowFilter) -> MarginResultQuery:
        """
         Creates a NXOpen.CAE.AeroStructures.MarginResultQuery 
                     containing all the results of every calculation passed in the argument 
                     that has been solved and belongs to this solution
                     If a non-null CAE.AeroStructures.MarginResultTableRowFilter is passed as argument
                     the results are further post-filtered (after the rank calculation has taken place) according to that filter
                    
         Returns query ( MarginResultQuery NXOpen.CAE.A):   output query .
        """
        pass
    @overload
    def CreateMarginResultQuery(self, maxRank: int, maxMS: float, filter: MarginResultTableRowFilter) -> MarginResultQuery:
        """
         Creates a NXOpen.CAE.AeroStructures.MarginResultQuery 
                    containing all the results of every calculation belonging to this solution that has been solved and 
                    that satisfies the following pre-conditions:
                    - the margin of safety is less than or equal to the maxMS specified in the argument
                    - the global rank is less than or equal to the maxRank specified in the argument
                    Results that do not satisfy these conditions are ignored and do not participate in the
                    computation of the other ranks.
                    If a non-null CAE.AeroStructures.MarginResultTableRowFilter is passed as argument
                    the results are further post-filtered (after the rank calculation has taken place) according to that filter
                    
         Returns query ( MarginResultQuery NXOpen.CAE.A):   margin result table data provider object.
        """
        pass
    @overload
    def CreateMarginResultQuery(self, marginCalculations: List[MarginCalculation], maxRank: int, maxMS: float, filter: MarginResultTableRowFilter) -> MarginResultQuery:
        """
         Creates a NXOpen.CAE.AeroStructures.MarginResultQuery 
                    containing the results of the calculations passed in the argument belonging to this solution that have been solved and 
                    that satisfy the following pre-conditions:
                    - the margin of safety is less than or equal to the maxMS specified in the argument
                    - the global rank is less than or equal to the maxRank specified in the argument
                    Results that do not satisfy these conditions are ignored and do not participate in the
                    computation of the other ranks.
                    If a non-null CAE.AeroStructures.MarginResultTableRowFilter is passed as argument
                    the results are further post-filtered (after the rank calculation has taken place) according to that filter
                    
         Returns query ( MarginResultQuery NXOpen.CAE.A):   margin result table data provider object.
        """
        pass
    @overload
    def CreateMarginResultTableDataProvider(self) -> MarginResultTableDataProvider:
        """
         Creates a NXOpen.CAE.AeroStructures.MarginResultTableDataProvider 
                    which will be based on every calculation of this solution that has results
                
                    Note: no column is registered by default. 
                          Methods  CAE.AeroStructures.MarginResultTableDataProvider.RegisterAllColumns or
                          Methods  CAE.AeroStructures.MarginResultTableDataProvider.RegisterColumn
                          should be called after calling this creator
                
         Returns tableDataProvider ( MarginResultTableDataProvider NXOpen.CAE.A):   margin result table data provider object.
        """
        pass
    @overload
    def CreateMarginResultTableDataProvider(self, marginCalculations: List[MarginCalculation]) -> MarginResultTableDataProvider:
        """
         Creates a NXOpen.CAE.AeroStructures.MarginResultTableDataProvider 
                    Only the subset of calculations given in the argument which have results are taken into account
                
                    Note: no column is registered by default. 
                          Methods  CAE.AeroStructures.MarginResultTableDataProvider.RegisterAllColumns or
                          Methods  CAE.AeroStructures.MarginResultTableDataProvider.RegisterColumn
                          should be called after calling this creator
                 
         Returns tableDataProvider ( MarginResultTableDataProvider NXOpen.CAE.A):   margin result table data provider object.
        """
        pass
    @overload
    def CreateMarginResultTableDataProvider(self, maxRank: int, maxMS: float) -> MarginResultTableDataProvider:
        """
         Creates a NXOpen.CAE.AeroStructures.MarginResultTableDataProvider 
                    which will be based on every calculation of this solution that has results 
                    and satisfies the following conditions:
                    - the margin of safety is less than or equal to the maxMS specified in argument
                    - the global rank is less than or equal to the maxRank specified in argument
                    Results that do not satisfy these conditions are ignored and do not participate in the
                    computation of the other ranks.
                    
                    Note: no column is registered by default. 
                          Methods  CAE.AeroStructures.MarginResultTableDataProvider.RegisterAllColumns or
                          Methods  CAE.AeroStructures.MarginResultTableDataProvider.RegisterColumn
                          should be called after calling this creator
                  
         Returns tableDataProvider ( MarginResultTableDataProvider NXOpen.CAE.A):   margin result table data provider object.
        """
        pass
    @overload
    def CreateMarginResultTableDataProvider(self, marginCalculations: List[MarginCalculation], maxRank: int, maxMS: float) -> MarginResultTableDataProvider:
        """
         Creates a NXOpen.CAE.AeroStructures.MarginResultTableDataProvider 
                    Only the subset of calculations given in the argument which have results are taken into account
                    Additionally only results that satisfy the following conditions are taken into account:
                    - the margin of safety is less than or equal to the maxMS specified in argument
                    - the global rank is less than or equal to the maxRank specified in argument
                    Results that do not satisfy these conditions are ignored and do not participate in the
                    computation of the other ranks.
                    
                    Note: no column is registered by default. 
                          Methods  CAE.AeroStructures.MarginResultTableDataProvider.RegisterAllColumns or
                          Methods  CAE.AeroStructures.MarginResultTableDataProvider.RegisterColumn
                          should be called after calling this creator
                
         Returns tableDataProvider ( MarginResultTableDataProvider NXOpen.CAE.A):   margin result table data provider object.
        """
        pass
    @overload
    def CreateMarginResultTableRowFilter(self) -> MarginResultTableRowFilter:
        """
         Creates an empty NXOpen.CAE.AeroStructures.MarginResultTableRowFilter 
                    By default it is a conjunction, meaning that successive conditions added to this filter
                    using AddCondition will be the terms of a conjunction (cond1 AND cond2 AND ...)
         Returns filter ( MarginResultTableRowFilter NXOpen.CAE.A):   margin result table row filter object.
        """
        pass
    @overload
    def CreateMarginResultTableRowFilter(self, isDisjunction: bool, isNegated: bool) -> MarginResultTableRowFilter:
        """
         Creates an empty NXOpen.CAE.AeroStructures.MarginResultTableRowFilter 
                    Specifying if it is a conjunction or a disjunction and if it is negated or not.
                    This means that successive conditions added to this filter using AddCondition will be the terms of either 
                    a conjunction (cond1 AND cond2 AND ...) or
                    a disjunction (cond1 OR cond2 OR ...)
                    Additionally if isNegated is true the whole conjunction or disjunction is negated:
                    NOT(cond1 AND cond2 AND ...) or
                    NOT(cond1 OR cond2 OR ...)
                    
         Returns filter ( MarginResultTableRowFilter NXOpen.CAE.A):   margin result table row filter object.
        """
        pass
    def PostProcessing(self, marginCalculations: List[MarginCalculation]) -> None:
        """
         Post processing of the calculations passed in the argument belonging to this solution 
        """
        pass
class MaterialSource(BaseExtractionSource): 
    """ Material source class. """
    pass
import NXOpen
class MatrixManip(NXOpen.NXObject): 
    """  This is the User LoadExtraction class  """
    class FilterOperations(Enum):
        """
        Members Include: 
         |Positive| 
         |Negative| 
         |Range| 
         |NotSet| 

        """
        Positive: int
        Negative: int
        Range: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> MatrixManip.FilterOperations:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MapOperations(Enum):
        """
        Members Include: 
         |Absolute| 
         |NotSet| 

        """
        Absolute: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> MatrixManip.MapOperations:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ReduceOperations(Enum):
        """
        Members Include: 
         |Max| 
         |Min| 
         |Average| 
         |Sum| 
         |NotSet| 
         |SignedAbsoluteExtremum| 

        """
        Max: int
        Min: int
        Average: int
        Sum: int
        NotSet: int
        SignedAbsoluteExtremum: int
        @staticmethod
        def ValueOf(value: int) -> MatrixManip.ReduceOperations:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetEndMeasure(self) -> str:
        """
         Get end Measure
         Returns measure (str): .
        """
        pass
    def GetFactor(self) -> float:
        """
         Get Factor Value
         Returns factor (float): .
        """
        pass
    def GetFactorConversion(self) -> float:
        """
         Get Conversion Factor Value 
         Returns factor (float): .
        """
        pass
    def GetFactorConversionExpression(self) -> NXOpen.Expression:
        """
         Get Conversion Factor expression 
         Returns exp ( NXOpen.Expression): .
        """
        pass
    def GetFactorExpression(self) -> NXOpen.Expression:
        """
         Get Factor expression
         Returns exp ( NXOpen.Expression): .
        """
        pass
    def GetFilterLowerBound(self) -> float:
        """
         Get filter lower bound
         Returns lowerBound (float): .
        """
        pass
    def GetFilterLowerBoundExpression(self) -> NXOpen.Expression:
        """
         Get filter lower bound expression
         Returns exp ( NXOpen.Expression): .
        """
        pass
    def GetFilterOperation(self) -> MatrixManip.FilterOperations:
        """
         Get Filter Operation 
         Returns filterOp ( MatrixManip.FilterOperations NXOpen.CAE.A): .
        """
        pass
    def GetFilterUpperBound(self) -> float:
        """
         Get filter upper bound
         Returns upperBound (float): .
        """
        pass
    def GetFilterUpperBoundExpression(self) -> NXOpen.Expression:
        """
         Get filter upper bound expression
         Returns exp ( NXOpen.Expression): .
        """
        pass
    def GetMapOperation(self) -> MatrixManip.MapOperations:
        """
         Get Map Operation 
         Returns mapOp ( MatrixManip.MapOperations NXOpen.CAE.A): .
        """
        pass
    def GetReduceOperation(self) -> MatrixManip.ReduceOperations:
        """
         Get Reduce Operation 
         Returns reduceOp ( MatrixManip.ReduceOperations NXOpen.CAE.A): .
        """
        pass
    def GetStartMeasure(self) -> str:
        """
         Get start Measure
         Returns measure (str): .
        """
        pass
    def SetEndMeasure(self, measure: str) -> None:
        """
         Set end Measure
        """
        pass
    def SetFactor(self, factor: float) -> None:
        """
         Set Factor Value
        """
        pass
    def SetFactorConversion(self, factor: float) -> None:
        """
         Set Conversion Factor Value 
        """
        pass
    def SetFactorConversionExpression(self, exp: NXOpen.Expression) -> None:
        """
         Set Conversion Factor expression 
        """
        pass
    def SetFactorExpression(self, exp: NXOpen.Expression) -> None:
        """
         Set Factor expression
        """
        pass
    def SetFilterLowerBound(self, lowerBound: float) -> None:
        """
         Set filter lower bound
        """
        pass
    def SetFilterLowerBoundExpression(self, exp: NXOpen.Expression) -> None:
        """
         Set filter lower bound expression
        """
        pass
    def SetFilterOperation(self, filterOp: MatrixManip.FilterOperations) -> None:
        """
         Set Filter Operation 
        """
        pass
    def SetFilterUpperBound(self, upperBound: float) -> None:
        """
         Set filter upper bound
        """
        pass
    def SetFilterUpperBoundExpression(self, exp: NXOpen.Expression) -> None:
        """
         Set filter upper bound expression
        """
        pass
    def SetMapOperation(self, mapOp: MatrixManip.MapOperations) -> None:
        """
         Set Map Operation 
        """
        pass
    def SetReduceOperation(self, reduceOp: MatrixManip.ReduceOperations) -> None:
        """
         Set Reduce Operation 
        """
        pass
    def SetStartMeasure(self, measure: str) -> None:
        """
         Set start Measure
        """
        pass
import NXOpen
class MethodDescriptor(NXOpen.TransientObject): 
    """  This is the MethodDescriptor.  """
    @property
    def Author(self) -> str:
        """
        Getter for property: (str) Author
         Returns the author   
            
         
        """
        pass
    @property
    def Category(self) -> str:
        """
        Getter for property: (str) Category
         Returns the category   
            
         
        """
        pass
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the description   
            
         
        """
        pass
    @property
    def Id(self) -> str:
        """
        Getter for property: (str) Id
         Returns the id   
            
         
        """
        pass
    @property
    def UiName(self) -> str:
        """
        Getter for property: (str) UiName
         Returns the ui name   
            
         
        """
        pass
    @property
    def Version(self) -> int:
        """
        Getter for property: (int) Version
         Returns the version   
            
         
        """
        pass
    def Dispose(self) -> None:
        """
         Dispose the MethodDescriptor object 
        """
        pass
    def GetDiagramUrl(self) -> str:
        """
         Returns the diagram url as given in the method descriptor file 
         Returns diagram (str): .
        """
        pass
    def GetDiagramUrlExpanded(self) -> str:
        """
         Returns the absolute diagram url with any embedded variables expanded 
         Returns diagram (str): .
        """
        pass
    def GetDocUrl(self) -> str:
        """
         Returns the doc url as given in the method descriptor file 
         Returns doc (str): .
        """
        pass
    def GetDocUrlExpanded(self) -> str:
        """
         Returns the absolute doc url with any embedded variables expanded 
         Returns doc (str): .
        """
        pass
    def GetFailureModeArray(self) -> List[FailureMode]:
        """
         Returns an array of all the failure mode ids 
         Returns fmArray ( FailureMode List[NXOpen.CAE): .
        """
        pass
    def GetInput(self, id: str) -> ParameterDescriptor:
        """
         Returns the input descriptor 
         Returns input ( ParameterDescriptor NXOpen.CAE.A): .
        """
        pass
    def GetInputArray(self) -> List[ParameterDescriptor]:
        """
         Returns an array of all the input descriptors 
         Returns inputArray ( ParameterDescriptor List[NXOpen.CAE): .
        """
        pass
    def GetNumFailureModes(self) -> int:
        """
         Returns the number of failure modes 
         Returns number (int): .
        """
        pass
    def GetNumInputs(self) -> int:
        """
         Returns the number of inputs 
         Returns number (int): .
        """
        pass
    def GetNumOutputs(self) -> int:
        """
         Returns the number of outputs 
         Returns number (int): .
        """
        pass
    def GetOutput(self, id: str) -> ParameterDescriptor:
        """
         Returns the output descriptor 
         Returns output ( ParameterDescriptor NXOpen.CAE.A): .
        """
        pass
    def GetOutputArray(self) -> List[ParameterDescriptor]:
        """
         Returns an array of all the output descriptors 
         Returns outputArray ( ParameterDescriptor List[NXOpen.CAE): .
        """
        pass
    def HasFailureMode(self, id: str) -> bool:
        """
         Returns if the given failure mode is present 
         Returns present (bool): .
        """
        pass
    def HasInput(self, id: str) -> bool:
        """
         Returns if the given input is present 
         Returns present (bool): .
        """
        pass
    def HasOutput(self, id: str) -> bool:
        """
         Returns if the given output is present 
         Returns present (bool): .
        """
        pass
import NXOpen
class MultiMarginCalculationBuilder(MarginCalculationBuilder): 
    """ Represents a builder for creating multi NXOpen.CAE.AeroStructures.MarginCalculation. """
    class ExtractionSiteType(Enum):
        """
        Members Include: 
         |PolygonFace| 
         |Group| 
         |Element| 
         |Node| 
         |Edge| 
         |Body| 
         |NotSet| 
         |Multiple| 

        """
        PolygonFace: int
        Group: int
        Element: int
        Node: int
        Edge: int
        Body: int
        NotSet: int
        Multiple: int
        @staticmethod
        def ValueOf(value: int) -> MultiMarginCalculationBuilder.ExtractionSiteType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def SetExtractionSites(self, extractionSiteType: MultiMarginCalculationBuilder.ExtractionSiteType, extractionSites: List[NXOpen.TaggedObject]) -> None:
        """
         Set the list of extraction sites 
        """
        pass
    def SetExtractionSources(self, sourceName: str, sourceType: BaseExtractionSource.TypeEnum, extractionSources: List[NXOpen.TaggedObject]) -> None:
        """
         Set the list of sources for propagation 
        """
        pass
import NXOpen
class ParameterDescriptor(NXOpen.TransientObject): 
    """  This is the Parameter Descriptor  """
    class DimensionalityType(Enum):
        """
        Members Include: 
         |NotSet| 
         |Failuremode| 
         |Loadcase| 
         |FmLc| 

        """
        NotSet: int
        Failuremode: int
        Loadcase: int
        FmLc: int
        @staticmethod
        def ValueOf(value: int) -> ParameterDescriptor.DimensionalityType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ParameterType(Enum):
        """
        Members Include: 
         |Boolean| 
         |Integer| 
         |Scalar| 
         |Text| 
         |Load| 
         |Table| 
         |Size| 
         |Laminate| 
         |File| 
         |Unknown| 

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
        @staticmethod
        def ValueOf(value: int) -> ParameterDescriptor.ParameterType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Dimensionality(self) -> ParameterDescriptor.DimensionalityType:
        """
        Getter for property: ( ParameterDescriptor.DimensionalityType NXOpen.CAE.A) Dimensionality
         Returns the Dimensionality   
            
         
        """
        pass
    @property
    def Id(self) -> str:
        """
        Getter for property: (str) Id
         Returns the id   
            
         
        """
        pass
    @property
    def IsOptional(self) -> bool:
        """
        Getter for property: (bool) IsOptional
         Returns the IsOptional   
            
         
        """
        pass
    @property
    def ParamType(self) -> ParameterDescriptor.ParameterType:
        """
        Getter for property: ( ParameterDescriptor.ParameterType NXOpen.CAE.A) ParamType
         Returns the ParameterType   
            
         
        """
        pass
    @property
    def UiName(self) -> str:
        """
        Getter for property: (str) UiName
         Returns the UI name   
            
         
        """
        pass
    def Dispose(self) -> None:
        """
         Dispose 
        """
        pass
class PhysicalPropertySource(BaseExtractionSource): 
    """ Physical property source class. """
    pass
import NXOpen.CAE
class PropTable(NXOpen.CAE.PropertyTable): 
    """  Represents a property table  """
    class MarginPropertyType(Enum):
        """
        Members Include: 
         |Unknown|  BASE_PROPERTY_TABLE_margin_property_type_unknown               
         |String|  BASE_PROPERTY_TABLE_margin_property_type_string                
         |Boolean|  BASE_PROPERTY_TABLE_margin_property_type_boolean               
         |Integer|  BASE_PROPERTY_TABLE_margin_property_type_integer               
         |Double|  BASE_PROPERTY_TABLE_margin_property_type_double                
         |FieldWrapper|  BASE_PROPERTY_TABLE_margin_property_type_field_wrapper         
         |ScalarFieldWrapper|  BASE_PROPERTY_TABLE_margin_property_type_scalar_field_wrapper  
         |CoordinateSystem|  BASE_PROPERTY_TABLE_margin_property_type_coordinate_system     
         |DoubleArray|  BASE_PROPERTY_TABLE_margin_property_type_double_array          
         |IntegerArray|  BASE_PROPERTY_TABLE_margin_property_type_integer_array         
         |PhysicalMaterial|  BASE_PROPERTY_TABLE_margin_property_type_physical_material     
         |Matrix|  BASE_PROPERTY_TABLE_margin_property_type_matrix                
         |ScalarTable|  BASE_PROPERTY_TABLE_margin_property_type_scalar_table          
         |Text|  
         |FieldExpression|  
         |VectorFieldWrapper|  
         |Vector|  
         |Reference|  
         |Point|  
         |DateTime|  
         |NamedPropertyTableArray|  
         |SetManager|  
         |NamedPropertyTable|  
         |Axis|  
         |CaeSection|  
         |SectionOrientation|  
         |SectionOffset|  
         |ReferenceArray|  
         |StringArray|  
         |Loadextraction|  
         |Laminate|  
         |Description|  
         |Table|  

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
        @staticmethod
        def ValueOf(value: int) -> PropTable.MarginPropertyType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetDescriptionPropertyValue(self, property_name: str) -> DescriptionValue:
        """
         Returns the description property 
         Returns property_value ( DescriptionValue NXOpen.CAE.A):  value of the property .
        """
        pass
    def GetLaminatePropertyValue(self, property_name: str) -> LaminateValue:
        """
         Returns the load laminate property 
         Returns property_value ( LaminateValue NXOpen.CAE.A):  value of the property .
        """
        pass
    def GetLoadExtractionPropertyValue(self, property_name: str) -> LoadExtractionValue:
        """
         Returns the load extraction property 
         Returns property_value ( LoadExtractionValue NXOpen.CAE.A):  value of the property .
        """
        pass
    def GetMarginPropertyType(self, property_name: str) -> PropTable.MarginPropertyType:
        """
         Returns the type of the property 
         Returns property_type ( PropTable.MarginPropertyType NXOpen.CAE.A):  type of the property .
        """
        pass
    def GetTableParamPropertyValue(self, property_name: str) -> TableParamValue:
        """
         Returns the table parameter value 
         Returns property_value ( TableParamValue NXOpen.CAE.A):  value of the property .
        """
        pass
    def SetDescriptionPropertyValue(self, property_name: str, property_value: DescriptionValue) -> None:
        """
         Used to set a description value
        """
        pass
    def SetFilePropertyValue(self, property_name: str, property_value: str) -> None:
        """
         Sets the file reference value of the property
                    
        """
        pass
    def SetLaminatePropertyValue(self, property_name: str, property_value: LaminateValue) -> None:
        """
         Used to set a laminate value
        """
        pass
    def SetLoadExtractionPropertyValue(self, property_name: str, property_value: LoadExtractionValue) -> None:
        """
         Used to set a load extraction value
        """
        pass
    def SetTableParamPropertyValue(self, property_name: str, property_value: TableParamValue) -> None:
        """
         Used to set a table parameter value
        """
        pass
import NXOpen
class ResultParams(NXOpen.NXObject): 
    """  This is the Aerostructure ResultParams class  """
    @property
    def ResultTypeName(self) -> str:
        """
        Getter for property: (str) ResultTypeName
         Returnsthe result type name   
            
         
        """
        pass
    @ResultTypeName.setter
    def ResultTypeName(self, name: str):
        """
        Setter for property: (str) ResultTypeName
         Returnsthe result type name   
            
         
        """
        pass
import NXOpen
class ScriptCallbackData(NXOpen.NXObject): 
    """ Represents a NXOpen.CAE.AeroStructures.ScriptCallbackData. """
    def GetMethodId(self) -> str:
        """
         Returns the method ID. 
         Returns methodID (str):  .
        """
        pass
    def GetModulePath(self) -> str:
        """
         Returns the module path. 
         Returns modulePath (str):  .
        """
        pass
    def GetObject(self) -> NXOpen.TaggedObject:
        """
         Returns the tagged object used by the script callback.
         Returns taggedObject ( NXOpen.TaggedObject):  .
        """
        pass
    def GetScriptMethodName(self) -> str:
        """
         Returns the script method name. 
         Returns scriptMethodName (str):  .
        """
        pass
    def SetSuccess(self, success: bool) -> None:
        """
         Set the success of the script callback execution. 
        """
        pass
class SectionSource(BaseExtractionSource): 
    """ Section source class. """
    pass
import NXOpen
class SolveOptions(NXOpen.Object): 
    """ Represents options for solve """
    @property
    def StoreLoadCaseInfo(self) -> bool:
        """
        Getter for property: (bool) StoreLoadCaseInfo
         Returns the option for load case specific outputs in the log (default is on)   
            
         
        """
        pass
    @StoreLoadCaseInfo.setter
    def StoreLoadCaseInfo(self, store: bool):
        """
        Setter for property: (bool) StoreLoadCaseInfo
         Returns the option for load case specific outputs in the log (default is on)   
            
         
        """
        pass
import NXOpen
class TableParameter(NXOpen.NXObject): 
    """  This is the TableParameter  """
    @property
    def Size(self) -> int:
        """
        Getter for property: (int) Size
         Returns the size of the table   
            
         
        """
        pass
    @property
    def SizeOffset(self) -> int:
        """
        Getter for property: (int) SizeOffset
         Returns the size offset   
            
         
        """
        pass
    @property
    def SizeParameter(self) -> str:
        """
        Getter for property: (str) SizeParameter
         Returns the size parameter   
            
         
        """
        pass
    def GetBooleanValues(self, columnId: str) -> List[bool]:
        """
         Get the values of a Boolean column 
         Returns value (List[bool]): .
        """
        pass
    def GetColumnNames(self) -> List[str]:
        """
         Returns a list of all column IDs 
         Returns columnIds (List[str]): .
        """
        pass
    def GetColumnType(self, columnName: str) -> ParameterDescriptor.ParameterType:
        """
         Returns the parameter type for a column 
         Returns type ( ParameterDescriptor.ParameterType NXOpen.CAE.A): .
        """
        pass
    def GetColumnUiNames(self, columnIds: List[str]) -> List[str]:
        """
         Returns the UI names for a given list of column ids, in the same order 
         Returns columnUiNames (List[str]): .
        """
        pass
    def GetIntegerValues(self, columnId: str) -> List[int]:
        """
         Get the values of an integer column 
         Returns value (List[int]): .
        """
        pass
    def GetLaminateValues(self, columnId: str) -> List[Laminate]:
        """
         Get the values of a laminate column 
         Returns value ( Laminate List[NXOpen.CAE):  .
        """
        pass
    def GetMeasure(self, columnId: str) -> str:
        """
         Get the measure name of a scalar column
                        Returns "Unitless" for unitless case
                      
         Returns measure (str): .
        """
        pass
    @overload
    def GetScalarValues(self, columnId: str) -> List[float]:
        """
         Get the values of a scalar column ("Not a number" values are returned as system NAN)
        These values are expressed in default unit type that can be retrieved by calling CAE.AeroStructures.TableParameter.GetUnitType 
         Returns value (List[float]): .
        """
        pass
    @overload
    def GetScalarValues(self, columnId: str, unit_type: NXOpen.Unit) -> List[float]:
        """
         Get the values of a scalar column converted in a specified unit ("Not a number" values are returned as system NAN)
         Returns value (List[float]): .
        """
        pass
    def GetStringValues(self, columnId: str) -> List[str]:
        """
         Get the values of a string column 
         Returns value (List[str]): .
        """
        pass
    def GetUnitType(self, columnId: str) -> NXOpen.Unit:
        """
         Get the unit type of a scalar column
                       Returns null if the column is unitless
                      
         Returns unit_type ( NXOpen.Unit): .
        """
        pass
import NXOpen
class TableParamValue(NXOpen.NXObject): 
    """  Represents a proper table parameter value  """
    def ChangeColumnsLength(self, rowId: int) -> None:
        """
         Changes the length of the columns
                    
        """
        pass
    def GetExpression(self, columnId: str, rowId: int) -> NXOpen.Expression:
        """
         Gets the expression from expression column at a certain row 
         Returns expression ( NXOpen.Expression):  the expression at columnId,rowId.
        """
        pass
    def GetLaminate(self, columnId: str, rowId: int, propTable: NXOpen.TaggedObject) -> LaminateQuery:
        """
         Gets the laminate query from a laminate column at a certain row 
                        If no laminate exists for that row or the row is outside the current table size a new laminate is created and returned.
                        This new laminate is registered with the laminate query manager of margin calculation owning the property table
                        It is inteded to be stored in a laminate column using TableParamValue.UpdateLaminateColumnValue
                    
         Returns laminateQuery ( LaminateQuery NXOpen.CAE.A): .
        """
        pass
    def SetBoolColumnValue(self, columnId: str, columnValues: List[bool]) -> None:
        """
         Sets a bool column value list 
        """
        pass
    def SetIntColumnValue(self, columnId: str, columnValues: List[int]) -> None:
        """
         Sets a int column value list 
        """
        pass
    def SetIsValidated(self, isValidated: bool) -> None:
        """
         Sets the validated status 
        """
        pass
    def SetScalarColumnValue(self, columnId: str, unit: NXOpen.Unit, columnValues: List[float]) -> None:
        """
         Sets a scalar column value list 
        """
        pass
    def SetStringColumnValue(self, columnId: str, columnValues: List[str]) -> None:
        """
         Sets a string column value list 
        """
        pass
    def UpdateExpressionColumnValue(self, columnId: str, unit: NXOpen.Unit, columnValues: List[NXOpen.Expression]) -> None:
        """
         Update an expression column value list with the expression array passed as input
                        Adjust its length and delete previous expressions if necessary 
        """
        pass
    def UpdateLaminateColumnValue(self, columnId: str, columnValues: List[LaminateQuery]) -> None:
        """
         Update a laminate column value list with the laminate array passed as input
                        Adjust its length and delete previous laminates if necessary 
        """
        pass
import NXOpen
import NXOpen.CAE
class UserLoadExtraction(LoadExtractionStrategy): 
    """  This is the User LoadExtraction class  """
    class PickMethod(Enum):
        """
        Members Include: 
         |Model| 
         |Group| 
         |ExtractionSource| 

        """
        Model: int
        Group: int
        ExtractionSource: int
        @staticmethod
        def ValueOf(value: int) -> UserLoadExtraction.PickMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TargetEntity(Enum):
        """
        Members Include: 
         |EntireModel| 
         |Nodes| 
         |Elements| 
         |Points| 
         |Edges| 
         |Faces| 
         |Bodies| 
         |NotSet| 

        """
        EntireModel: int
        Nodes: int
        Elements: int
        Points: int
        Edges: int
        Faces: int
        Bodies: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> UserLoadExtraction.TargetEntity:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ExtractionSourceName(self) -> str:
        """
        Getter for property: (str) ExtractionSourceName
         Returns the extraction source name  
            
         
        """
        pass
    @ExtractionSourceName.setter
    def ExtractionSourceName(self, name: str):
        """
        Setter for property: (str) ExtractionSourceName
         Returns the extraction source name  
            
         
        """
        pass
    @property
    def ResultParams(self) -> ResultParams:
        """
        Getter for property: ( ResultParams NXOpen.CAE.A) ResultParams
         Returns the aerostructure result params.  
             
         
        """
        pass
    def GetCoordinateSystem(self) -> NXOpen.CoordinateSystem:
        """
         Get Coordinate System 
         Returns csys ( NXOpen.CoordinateSystem): .
        """
        pass
    def GetExternalGroup(self) -> NXOpen.CAE.CaeGroup:
        """
         Get External Group 
         Returns group ( NXOpen.CAE.CaeGroup): .
        """
        pass
    def GetExtractionSource(self) -> BaseExtractionSource:
        """
         Get the extraction source 
         Returns source ( BaseExtractionSource NXOpen.CAE.A): .
        """
        pass
    def GetMatrixManip(self) -> MatrixManip:
        """
         Get Matrix Manip 
         Returns manip ( MatrixManip NXOpen.CAE.A): .
        """
        pass
    def GetPickMethod(self) -> UserLoadExtraction.PickMethod:
        """
         Get Pick Method 
         Returns pickMethod ( UserLoadExtraction.PickMethod NXOpen.CAE.A): .
        """
        pass
    def GetResultParameters(self) -> NXOpen.CAE.ResultParameters:
        """
         Get Result Parameters 
         Returns parameters ( NXOpen.CAE.ResultParameters): .
        """
        pass
    def GetSelectedEntities(self) -> List[NXOpen.TaggedObject]:
        """
         Get Selected Entities 
         Returns entities ( NXOpen.TaggedObject Li):  .
        """
        pass
    def GetTargetEntity(self) -> UserLoadExtraction.TargetEntity:
        """
         Get Entities Type 
         Returns target ( UserLoadExtraction.TargetEntity NXOpen.CAE.A): .
        """
        pass
    def SetCoordinateSystem(self, csys: NXOpen.CoordinateSystem) -> None:
        """
         Set Coordinate System 
        """
        pass
    def SetExternalGroup(self, group: NXOpen.CAE.CaeGroup) -> None:
        """
         Set External Group 
        """
        pass
    def SetMatrixManip(self, manip: MatrixManip) -> None:
        """
         Set Matrix Manip 
        """
        pass
    def SetPickMethod(self, pickMethod: UserLoadExtraction.PickMethod) -> None:
        """
         Set Pick Method 
        """
        pass
    def SetResultParameters(self, parameters: NXOpen.CAE.ResultParameters) -> None:
        """
         Set Result Parameters 
        """
        pass
    def SetSelectedEntities(self, entities: List[NXOpen.TaggedObject]) -> None:
        """
         Set Selected Entities 
        """
        pass
    def SetTargetEntity(self, target: UserLoadExtraction.TargetEntity) -> None:
        """
         Set Entities Type 
        """
        pass
import NXOpen
class Utils(NXOpen.Object): 
    """ Contains universal aerostructure utility methods """
    def GetTemplatePaths(templateName: str) -> List[str]:
        """
         Returns template paths from the repository regarding a template name 
         Returns paths (List[str]): .
        """
        pass
    def ReloadMethodsAndTemplates() -> None:
        """
         Reloads the methods and templates for Aerostructures 
        """
        pass
