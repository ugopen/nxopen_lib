from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class DesignStudyAttributeBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Optimization.DesignStudyAttributeBuilder """
    def AdoptObject(self, objectValue: NXOpen.NXObject) -> None:
        """
         Adopt object 
        """
        pass
import NXOpen
class DesignStudyBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Optimization.DesignStudyBuilder """
    class DesignStudyAttributeType(Enum):
        """
        Members Include: 
         |Expression|  Expression type 
         |KFAttribute|  KF attribute type 
         |GeometryParameter|  Geometry parameter type 

        """
        Expression: int
        KFAttribute: int
        GeometryParameter: int
        @staticmethod
        def ValueOf(value: int) -> DesignStudyBuilder.DesignStudyAttributeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DesignStudyConstraintLimitType(Enum):
        """
        Members Include: 
         |Upper|  Upper limit type 
         |Lower|  Lower limit type 

        """
        Upper: int
        Lower: int
        @staticmethod
        def ValueOf(value: int) -> DesignStudyBuilder.DesignStudyConstraintLimitType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DesignStudyDistributeType(Enum):
        """
        Members Include: 
         |Uniform|  Uniform distribution type 
         |Normal|  Normal distribution type 
         |Gamma|  Gamma distribution type 

        """
        Uniform: int
        Normal: int
        Gamma: int
        @staticmethod
        def ValueOf(value: int) -> DesignStudyBuilder.DesignStudyDistributeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DesignStudyObjective:
        """
         Defined Objective Structure 
         DesignStudyBuilderDesignStudyObjective_Struct NXOpen.Op is an alias for  DesignStudyBuilder.DesignStudyObjective NXOpen.Op.
        """
        @property
        def AttributeName(self) -> str:
            """
            Getter for property AttributeName
            Attribute name

            """
            pass
        @AttributeName.setter
        def AttributeName(self, value: str):
            """
            Getter for property AttributeName
            Attribute name
            Setter for property AttributeName
            Attribute name

            """
            pass
        @property
        def AttributeObject(self) -> NXOpen.NXObject:
            """
            Getter for property AttributeObject
            Object which the attribute belongs to, it makes sense with geometry design variable type

            """
            pass
        @AttributeObject.setter
        def AttributeObject(self, value: NXOpen.NXObject):
            """
            Getter for property AttributeObject
            Object which the attribute belongs to, it makes sense with geometry design variable type
            Setter for property AttributeObject
            Object which the attribute belongs to, it makes sense with geometry design variable type

            """
            pass
        @property
        def ObjectiveType(self) -> DesignStudyBuilder.DesignStudyAttributeType:
            """
            Getter for property ObjectiveType
            Objectibe type

            """
            pass
        @ObjectiveType.setter
        def ObjectiveType(self, value: DesignStudyBuilder.DesignStudyAttributeType):
            """
            Getter for property ObjectiveType
            Objectibe type
            Setter for property ObjectiveType
            Objectibe type

            """
            pass
        @property
        def WarningLowerLimit(self) -> float:
            """
            Getter for property WarningLowerLimit
            Warning lower limit

            """
            pass
        @WarningLowerLimit.setter
        def WarningLowerLimit(self, value: float):
            """
            Getter for property WarningLowerLimit
            Warning lower limit
            Setter for property WarningLowerLimit
            Warning lower limit

            """
            pass
        @property
        def WarningUpperLimit(self) -> float:
            """
            Getter for property WarningUpperLimit
            Warning Upper limit

            """
            pass
        @WarningUpperLimit.setter
        def WarningUpperLimit(self, value: float):
            """
            Getter for property WarningUpperLimit
            Warning Upper limit
            Setter for property WarningUpperLimit
            Warning Upper limit

            """
            pass
        @property
        def FailureLowerLimit(self) -> float:
            """
            Getter for property FailureLowerLimit
            Failure Lower limit

            """
            pass
        @FailureLowerLimit.setter
        def FailureLowerLimit(self, value: float):
            """
            Getter for property FailureLowerLimit
            Failure Lower limit
            Setter for property FailureLowerLimit
            Failure Lower limit

            """
            pass
        @property
        def FailureUpperLimit(self) -> float:
            """
            Getter for property FailureUpperLimit
            Failure Upper limit

            """
            pass
        @FailureUpperLimit.setter
        def FailureUpperLimit(self, value: float):
            """
            Getter for property FailureUpperLimit
            Failure Upper limit
            Setter for property FailureUpperLimit
            Failure Upper limit

            """
            pass
    class DesignStudyVariable:
        """
         Defined variable structure 
         DesignStudyBuilderDesignStudyVariable_Struct NXOpen.Op is an alias for  DesignStudyBuilder.DesignStudyVariable NXOpen.Op.
        """
        @property
        def AttributeName(self) -> str:
            """
            Getter for property AttributeName
            Attribute name

            """
            pass
        @AttributeName.setter
        def AttributeName(self, value: str):
            """
            Getter for property AttributeName
            Attribute name
            Setter for property AttributeName
            Attribute name

            """
            pass
        @property
        def AttributeObject(self) -> NXOpen.NXObject:
            """
            Getter for property AttributeObject
            Object which the attribute belongs to, it makes sense with geometry design variable type

            """
            pass
        @AttributeObject.setter
        def AttributeObject(self, value: NXOpen.NXObject):
            """
            Getter for property AttributeObject
            Object which the attribute belongs to, it makes sense with geometry design variable type
            Setter for property AttributeObject
            Object which the attribute belongs to, it makes sense with geometry design variable type

            """
            pass
        @property
        def VariableType(self) -> DesignStudyBuilder.DesignStudyAttributeType:
            """
            Getter for property VariableType
            Variable type

            """
            pass
        @VariableType.setter
        def VariableType(self, value: DesignStudyBuilder.DesignStudyAttributeType):
            """
            Getter for property VariableType
            Variable type
            Setter for property VariableType
            Variable type

            """
            pass
        @property
        def VariableLowerLimitValue(self) -> float:
            """
            Getter for property VariableLowerLimitValue
            Lower limit value

            """
            pass
        @VariableLowerLimitValue.setter
        def VariableLowerLimitValue(self, value: float):
            """
            Getter for property VariableLowerLimitValue
            Lower limit value
            Setter for property VariableLowerLimitValue
            Lower limit value

            """
            pass
        @property
        def VariableUpperLimitValue(self) -> float:
            """
            Getter for property VariableUpperLimitValue
            Upper limit value

            """
            pass
        @VariableUpperLimitValue.setter
        def VariableUpperLimitValue(self, value: float):
            """
            Getter for property VariableUpperLimitValue
            Upper limit value
            Setter for property VariableUpperLimitValue
            Upper limit value

            """
            pass
        @property
        def DistributeType(self) -> DesignStudyBuilder.DesignStudyDistributeType:
            """
            Getter for property DistributeType
            Distribute type

            """
            pass
        @DistributeType.setter
        def DistributeType(self, value: DesignStudyBuilder.DesignStudyDistributeType):
            """
            Getter for property DistributeType
            Distribute type
            Setter for property DistributeType
            Distribute type

            """
            pass
        @property
        def LocationParameter(self) -> float:
            """
            Getter for property LocationParameter
            Location parameter

            """
            pass
        @LocationParameter.setter
        def LocationParameter(self, value: float):
            """
            Getter for property LocationParameter
            Location parameter
            Setter for property LocationParameter
            Location parameter

            """
            pass
        @property
        def ScaleParameter(self) -> float:
            """
            Getter for property ScaleParameter
            Scale parameter

            """
            pass
        @ScaleParameter.setter
        def ScaleParameter(self, value: float):
            """
            Getter for property ScaleParameter
            Scale parameter
            Setter for property ScaleParameter
            Scale parameter

            """
            pass
        @property
        def ShapeParameter(self) -> float:
            """
            Getter for property ShapeParameter
            Shape parameter

            """
            pass
        @ShapeParameter.setter
        def ShapeParameter(self, value: float):
            """
            Getter for property ShapeParameter
            Shape parameter
            Setter for property ShapeParameter
            Shape parameter

            """
            pass
        @property
        def ValuesCount(self) -> int:
            """
            Getter for property ValuesCount
            Values count

            """
            pass
        @ValuesCount.setter
        def ValuesCount(self, value: int):
            """
            Getter for property ValuesCount
            Values count
            Setter for property ValuesCount
            Values count

            """
            pass
    @property
    def IsShowGraph(self) -> bool:
        """
        Getter for property: (bool) IsShowGraph
         Returns the property - is show graph   
            
         
        """
        pass
    @IsShowGraph.setter
    def IsShowGraph(self, isShowGraph: bool):
        """
        Setter for property: (bool) IsShowGraph
         Returns the property - is show graph   
            
         
        """
        pass
    @property
    def IsUpdateDisp(self) -> bool:
        """
        Getter for property: (bool) IsUpdateDisp
         Returns the property - is update display   
            
         
        """
        pass
    @IsUpdateDisp.setter
    def IsUpdateDisp(self, isUpdateDisp: bool):
        """
        Setter for property: (bool) IsUpdateDisp
         Returns the property - is update display   
            
         
        """
        pass
    @property
    def StudyName(self) -> str:
        """
        Getter for property: (str) StudyName
         Returns the study name which is unique in one part   
            
         
        """
        pass
    @StudyName.setter
    def StudyName(self, studyName: str):
        """
        Setter for property: (str) StudyName
         Returns the study name which is unique in one part   
            
         
        """
        pass
    def BuildAllObjectives(self) -> None:
        """
         Build all the objectives 
        """
        pass
    def BuildAllVariables(self) -> None:
        """
         Build all the variables 
        """
        pass
    def GetDesignStudyObjectives(self) -> List[DesignStudyBuilder.DesignStudyObjective]:
        """
         Returns the objectives 
         Returns objectives ( DesignStudyBuilder.DesignStudyObjective List[NXOpen.):  Objectives .
        """
        pass
    def GetDesignStudyVariables(self) -> List[DesignStudyBuilder.DesignStudyVariable]:
        """
         Returns the variables 
         Returns variables ( DesignStudyBuilder.DesignStudyVariable List[NXOpen.):  Variables .
        """
        pass
    def RemoveAllObjectives(self) -> None:
        """
         Remove all the objectives 
        """
        pass
    def RemoveAllVariables(self) -> None:
        """
         Remove all the variables 
        """
        pass
    def RunDesignStudy(self) -> None:
        """
         Run design study process 
        """
        pass
    def SetDesignStudyObjectives(self, attributeNames: List[str], attributeObjects: List[NXOpen.NXObject], objectiveTypes: List[DesignStudyBuilder.DesignStudyAttributeType], warningLowerLimit: List[float], warningUpperLimit: List[float], failureLowerLimit: List[float], failureUpperLimit: List[float]) -> None:
        """
         Sets the objectives 
        """
        pass
    def SetDesignStudyVariables(self, attributeNames: List[str], attributeObjects: List[NXOpen.NXObject], variableTypes: List[DesignStudyBuilder.DesignStudyAttributeType], variableLowerLimitValue: List[float], variableUpperLimitValue: List[float], distributeType: List[DesignStudyBuilder.DesignStudyDistributeType], locationParameter: List[float], scaleParameter: List[float], shapeParameter: List[float], valuesCount: List[int]) -> None:
        """
         Sets the variables 
        """
        pass
import NXOpen
class DesignStudyCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a NXOpen.Optimization.DesignStudyCollection """
    def CreateDesignStudyAttributeBuilder(self) -> DesignStudyAttributeBuilder:
        """
         Create builder for DesignStudyAttribute class 
         Returns builder ( DesignStudyAttributeBuilder NXOpen.Op): .
        """
        pass
    def CreateDesignStudyBuilder(self) -> DesignStudyBuilder:
        """
         Create builder for design study class 
         Returns builder ( DesignStudyBuilder NXOpen.Op): .
        """
        pass
import NXOpen
class MapleExpBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Optimization.MapleExpBuilder """
    pass
import NXOpen
class MathIntegrationExpBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Optimization.MathIntegrationExpBuilder """
    pass
import NXOpen
class OptimizationAttributeBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Optimization.OptimizationAttributeBuilder """
    def AdoptObject(self, objectValue: NXOpen.NXObject) -> None:
        """
         Adopt object 
        """
        pass
import NXOpen
class OptimizationBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Optimization.OptimizationBuilder """
    class OptimizationAlgorithmType(Enum):
        """
        Members Include: 
         |SimulatedAnnealing|  Simulated annealing 
         |GlobalSimplex|  Global simplex 
         |Powell|  Powell 
         |ConjugateGradient|  Conjugate gradient 
         |Lexicographic|  Lexicographic 
         |PatternSwarm|  Pattern swarm 

        """
        SimulatedAnnealing: int
        GlobalSimplex: int
        Powell: int
        ConjugateGradient: int
        Lexicographic: int
        PatternSwarm: int
        @staticmethod
        def ValueOf(value: int) -> OptimizationBuilder.OptimizationAlgorithmType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OptimizationAttributeType(Enum):
        """
        Members Include: 
         |Expression|  Expression attribute 
         |KFAttribute|  KF attribute 
         |GeometryParameter|  Geometryfeature parameter attribute

        """
        Expression: int
        KFAttribute: int
        GeometryParameter: int
        @staticmethod
        def ValueOf(value: int) -> OptimizationBuilder.OptimizationAttributeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OptimizationConstraintLimitType(Enum):
        """
        Members Include: 
         |Upper|  Upper limit 
         |Lower|  Lower limit 

        """
        Upper: int
        Lower: int
        @staticmethod
        def ValueOf(value: int) -> OptimizationBuilder.OptimizationConstraintLimitType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OptimizationConvergenceSpeedType(Enum):
        """
        Members Include: 
         |Slow|  Slow convergence speed 
         |Medium|  Medium convergence speed
         |Fast|  Fast convergence speed
         |Infinite|  Infinite convergence speed

        """
        Slow: int
        Medium: int
        Fast: int
        Infinite: int
        @staticmethod
        def ValueOf(value: int) -> OptimizationBuilder.OptimizationConvergenceSpeedType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OptimizationTargetType(Enum):
        """
        Members Include: 
         |Minimum|  Target is minimum value of design objective 
         |Maximum|  Target is maximum value of design objective 
         |Target|  Target is specified value of design objective 

        """
        Minimum: int
        Maximum: int
        Target: int
        @staticmethod
        def ValueOf(value: int) -> OptimizationBuilder.OptimizationTargetType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OptimizationConstraint:
        """
         Defined constraint structure 
         OptimizationBuilderOptimizationConstraint_Struct NXOpen.Op is an alias for  OptimizationBuilder.OptimizationConstraint NXOpen.Op.
        """
        @property
        def AttributeName(self) -> str:
            """
            Getter for property AttributeName
            Attribute name

            """
            pass
        @AttributeName.setter
        def AttributeName(self, value: str):
            """
            Getter for property AttributeName
            Attribute name
            Setter for property AttributeName
            Attribute name

            """
            pass
        @property
        def AttributeObject(self) -> NXOpen.NXObject:
            """
            Getter for property AttributeObject
            Object which the attribute belongs to, it makes sense with geometry design variable type

            """
            pass
        @AttributeObject.setter
        def AttributeObject(self, value: NXOpen.NXObject):
            """
            Getter for property AttributeObject
            Object which the attribute belongs to, it makes sense with geometry design variable type
            Setter for property AttributeObject
            Object which the attribute belongs to, it makes sense with geometry design variable type

            """
            pass
        @property
        def ConstraintType(self) -> OptimizationBuilder.OptimizationAttributeType:
            """
            Getter for property ConstraintType
            Constraint type

            """
            pass
        @ConstraintType.setter
        def ConstraintType(self, value: OptimizationBuilder.OptimizationAttributeType):
            """
            Getter for property ConstraintType
            Constraint type
            Setter for property ConstraintType
            Constraint type

            """
            pass
        @property
        def ConstraintLowerLimitValue(self) -> float:
            """
            Getter for property ConstraintLowerLimitValue
            Lower limit value

            """
            pass
        @ConstraintLowerLimitValue.setter
        def ConstraintLowerLimitValue(self, value: float):
            """
            Getter for property ConstraintLowerLimitValue
            Lower limit value
            Setter for property ConstraintLowerLimitValue
            Lower limit value

            """
            pass
        @property
        def ConstraintUpperLimitValue(self) -> float:
            """
            Getter for property ConstraintUpperLimitValue
            Upper limit value

            """
            pass
        @ConstraintUpperLimitValue.setter
        def ConstraintUpperLimitValue(self, value: float):
            """
            Getter for property ConstraintUpperLimitValue
            Upper limit value
            Setter for property ConstraintUpperLimitValue
            Upper limit value

            """
            pass
        @property
        def ConstraintLimitType(self) -> OptimizationBuilder.OptimizationConstraintLimitType:
            """
            Getter for property ConstraintLimitType
            constraint limit type, lower type or upper type

            """
            pass
        @ConstraintLimitType.setter
        def ConstraintLimitType(self, value: OptimizationBuilder.OptimizationConstraintLimitType):
            """
            Getter for property ConstraintLimitType
            constraint limit type, lower type or upper type
            Setter for property ConstraintLimitType
            constraint limit type, lower type or upper type

            """
            pass
    class OptimizationObjective:
        """
         Defined Objective Structure 
         OptimizationBuilderOptimizationObjective_Struct NXOpen.Op is an alias for  OptimizationBuilder.OptimizationObjective NXOpen.Op.
        """
        @property
        def AttributeName(self) -> str:
            """
            Getter for property AttributeName
            Attribute name

            """
            pass
        @AttributeName.setter
        def AttributeName(self, value: str):
            """
            Getter for property AttributeName
            Attribute name
            Setter for property AttributeName
            Attribute name

            """
            pass
        @property
        def AttributeObject(self) -> NXOpen.NXObject:
            """
            Getter for property AttributeObject
            Object which the attribute belongs to, it makes sense with geometry design variable type

            """
            pass
        @AttributeObject.setter
        def AttributeObject(self, value: NXOpen.NXObject):
            """
            Getter for property AttributeObject
            Object which the attribute belongs to, it makes sense with geometry design variable type
            Setter for property AttributeObject
            Object which the attribute belongs to, it makes sense with geometry design variable type

            """
            pass
        @property
        def ObjectiveType(self) -> OptimizationBuilder.OptimizationAttributeType:
            """
            Getter for property ObjectiveType
            Objectibe type

            """
            pass
        @ObjectiveType.setter
        def ObjectiveType(self, value: OptimizationBuilder.OptimizationAttributeType):
            """
            Getter for property ObjectiveType
            Objectibe type
            Setter for property ObjectiveType
            Objectibe type

            """
            pass
        @property
        def ObjectiveTargetValue(self) -> float:
            """
            Getter for property ObjectiveTargetValue
            Value of objective target

            """
            pass
        @ObjectiveTargetValue.setter
        def ObjectiveTargetValue(self, value: float):
            """
            Getter for property ObjectiveTargetValue
            Value of objective target
            Setter for property ObjectiveTargetValue
            Value of objective target

            """
            pass
    class OptimizationVariable:
        """
         Defined variable structure 
         OptimizationBuilderOptimizationVariable_Struct NXOpen.Op is an alias for  OptimizationBuilder.OptimizationVariable NXOpen.Op.
        """
        @property
        def AttributeName(self) -> str:
            """
            Getter for property AttributeName
            Attribute name

            """
            pass
        @AttributeName.setter
        def AttributeName(self, value: str):
            """
            Getter for property AttributeName
            Attribute name
            Setter for property AttributeName
            Attribute name

            """
            pass
        @property
        def AttributeObject(self) -> NXOpen.NXObject:
            """
            Getter for property AttributeObject
            Object which the attribute belongs to, it makes sense with geometry design variable type

            """
            pass
        @AttributeObject.setter
        def AttributeObject(self, value: NXOpen.NXObject):
            """
            Getter for property AttributeObject
            Object which the attribute belongs to, it makes sense with geometry design variable type
            Setter for property AttributeObject
            Object which the attribute belongs to, it makes sense with geometry design variable type

            """
            pass
        @property
        def VariableType(self) -> OptimizationBuilder.OptimizationAttributeType:
            """
            Getter for property VariableType
            Variable type

            """
            pass
        @VariableType.setter
        def VariableType(self, value: OptimizationBuilder.OptimizationAttributeType):
            """
            Getter for property VariableType
            Variable type
            Setter for property VariableType
            Variable type

            """
            pass
        @property
        def VariableLowerLimitValue(self) -> float:
            """
            Getter for property VariableLowerLimitValue
            Lower limit value

            """
            pass
        @VariableLowerLimitValue.setter
        def VariableLowerLimitValue(self, value: float):
            """
            Getter for property VariableLowerLimitValue
            Lower limit value
            Setter for property VariableLowerLimitValue
            Lower limit value

            """
            pass
        @property
        def VariableUpperLimitValue(self) -> float:
            """
            Getter for property VariableUpperLimitValue
            Upper limit value

            """
            pass
        @VariableUpperLimitValue.setter
        def VariableUpperLimitValue(self, value: float):
            """
            Getter for property VariableUpperLimitValue
            Upper limit value
            Setter for property VariableUpperLimitValue
            Upper limit value

            """
            pass
    @property
    def AbsoluteConvergenceCriteria(self) -> float:
        """
        Getter for property: (float) AbsoluteConvergenceCriteria
         Returns the absolute criteria for optimizer to determine convergence.  
           This value is
                    multiplied by the first objective result,and if the difference in last two 
                    objective results is less than this, then it is converged   
         
        """
        pass
    @AbsoluteConvergenceCriteria.setter
    def AbsoluteConvergenceCriteria(self, absoluteConvergenceCriteria: float):
        """
        Setter for property: (float) AbsoluteConvergenceCriteria
         Returns the absolute criteria for optimizer to determine convergence.  
           This value is
                    multiplied by the first objective result,and if the difference in last two 
                    objective results is less than this, then it is converged   
         
        """
        pass
    @property
    def AlgorithmType(self) -> OptimizationBuilder.OptimizationAlgorithmType:
        """
        Getter for property: ( OptimizationBuilder.OptimizationAlgorithmType NXOpen.Op) AlgorithmType
         Returns the algorithm type   
            
         
        """
        pass
    @AlgorithmType.setter
    def AlgorithmType(self, algorithmType: OptimizationBuilder.OptimizationAlgorithmType):
        """
        Setter for property: ( OptimizationBuilder.OptimizationAlgorithmType NXOpen.Op) AlgorithmType
         Returns the algorithm type   
            
         
        """
        pass
    @property
    def ConvergenceSpeedType(self) -> OptimizationBuilder.OptimizationConvergenceSpeedType:
        """
        Getter for property: ( OptimizationBuilder.OptimizationConvergenceSpeedType NXOpen.Op) ConvergenceSpeedType
         Returns the convergence speed type   
            
         
        """
        pass
    @ConvergenceSpeedType.setter
    def ConvergenceSpeedType(self, convergenceSpeedType: OptimizationBuilder.OptimizationConvergenceSpeedType):
        """
        Setter for property: ( OptimizationBuilder.OptimizationConvergenceSpeedType NXOpen.Op) ConvergenceSpeedType
         Returns the convergence speed type   
            
         
        """
        pass
    @property
    def IsShowGraph(self) -> bool:
        """
        Getter for property: (bool) IsShowGraph
         Returns the property - is show graph   
            
         
        """
        pass
    @IsShowGraph.setter
    def IsShowGraph(self, isShowGraph: bool):
        """
        Setter for property: (bool) IsShowGraph
         Returns the property - is show graph   
            
         
        """
        pass
    @property
    def IsUpdateDisp(self) -> bool:
        """
        Getter for property: (bool) IsUpdateDisp
         Returns the property - is update display   
            
         
        """
        pass
    @IsUpdateDisp.setter
    def IsUpdateDisp(self, isUpdateDisp: bool):
        """
        Setter for property: (bool) IsUpdateDisp
         Returns the property - is update display   
            
         
        """
        pass
    @property
    def MaxNumberIteration(self) -> int:
        """
        Getter for property: (int) MaxNumberIteration
         Returns the maximum number of updates allowed without converging to a solutionthe maximum iterations time  
            
         
        """
        pass
    @MaxNumberIteration.setter
    def MaxNumberIteration(self, integerMaxNumIter: int):
        """
        Setter for property: (int) MaxNumberIteration
         Returns the maximum number of updates allowed without converging to a solutionthe maximum iterations time  
            
         
        """
        pass
    @property
    def MaxTime(self) -> int:
        """
        Getter for property: (int) MaxTime
         Returns the maximum time allowed for this run in seconds   
            
         
        """
        pass
    @MaxTime.setter
    def MaxTime(self, maxTime: int):
        """
        Setter for property: (int) MaxTime
         Returns the maximum time allowed for this run in seconds   
            
         
        """
        pass
    @property
    def OptimizationType(self) -> OptimizationBuilder.OptimizationTargetType:
        """
        Getter for property: ( OptimizationBuilder.OptimizationTargetType NXOpen.Op) OptimizationType
         Returns the optimization type   
            
         
        """
        pass
    @OptimizationType.setter
    def OptimizationType(self, optimizationType: OptimizationBuilder.OptimizationTargetType):
        """
        Setter for property: ( OptimizationBuilder.OptimizationTargetType NXOpen.Op) OptimizationType
         Returns the optimization type   
            
         
        """
        pass
    @property
    def RelativeConvergenceCriteria(self) -> float:
        """
        Getter for property: (float) RelativeConvergenceCriteria
         Returns the relative criteria for optimizer
                    to determine convergence.  
            If one minus
                    the ratio of the last two iterations is
                    less than this value, the solution is converged   
         
        """
        pass
    @RelativeConvergenceCriteria.setter
    def RelativeConvergenceCriteria(self, relativeConverCriteria: float):
        """
        Setter for property: (float) RelativeConvergenceCriteria
         Returns the relative criteria for optimizer
                    to determine convergence.  
            If one minus
                    the ratio of the last two iterations is
                    less than this value, the solution is converged   
         
        """
        pass
    @property
    def StudyName(self) -> str:
        """
        Getter for property: (str) StudyName
         Returns the study name which is unique in one part   
            
         
        """
        pass
    @StudyName.setter
    def StudyName(self, studyName: str):
        """
        Setter for property: (str) StudyName
         Returns the study name which is unique in one part   
            
         
        """
        pass
    def BuildAllConstraints(self) -> None:
        """
         Build all the constraints 
        """
        pass
    def BuildAllObjectives(self) -> None:
        """
         Build all the objectives 
        """
        pass
    def BuildAllVariables(self) -> None:
        """
         Build all the variables 
        """
        pass
    def GetOptimizationConstraints(self) -> List[OptimizationBuilder.OptimizationConstraint]:
        """
         Returns the constraints 
         Returns constraints ( OptimizationBuilder.OptimizationConstraint List[NXOpen.):  Constraints .
        """
        pass
    def GetOptimizationObjectives(self) -> List[OptimizationBuilder.OptimizationObjective]:
        """
         Returns the objectives 
         Returns objectives ( OptimizationBuilder.OptimizationObjective List[NXOpen.):  Objectives .
        """
        pass
    def GetOptimizationVariables(self) -> List[OptimizationBuilder.OptimizationVariable]:
        """
         Returns the variables 
         Returns variables ( OptimizationBuilder.OptimizationVariable List[NXOpen.):  Variables .
        """
        pass
    def RemoveAllConstraints(self) -> None:
        """
         Remove all the constraints 
        """
        pass
    def RemoveAllObjectives(self) -> None:
        """
         Remove all the objectives 
        """
        pass
    def RemoveAllVariables(self) -> None:
        """
         Remove all the variables 
        """
        pass
    def RunOptimization(self) -> None:
        """
         Run optimization process 
        """
        pass
    def SetOptimizationConstraints(self, attributeNames: List[str], attributeObjects: List[NXOpen.NXObject], constraintTypes: List[OptimizationBuilder.OptimizationAttributeType], constraintLowerLimitValue: List[float], constraintUpperLimitValue: List[float], constraintLimitType: List[OptimizationBuilder.OptimizationConstraintLimitType]) -> None:
        """
         Sets the constraints 
        """
        pass
    def SetOptimizationObjectives(self, attributeNames: List[str], attributeObjects: List[NXOpen.NXObject], objectiveTypes: List[OptimizationBuilder.OptimizationAttributeType], objectiveTargetValues: List[float]) -> None:
        """
         Sets the objectives 
        """
        pass
    def SetOptimizationVariables(self, attributeNames: List[str], attributeObjects: List[NXOpen.NXObject], variableTypes: List[OptimizationBuilder.OptimizationAttributeType], variableLowerLimitValue: List[float], variableUpperLimitValue: List[float]) -> None:
        """
         Sets the variables 
        """
        pass
import NXOpen
class OptimizationCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a NXOpen.Optimization.OptimizationCollection """
    def CreateMapleExpBuilder(self) -> MapleExpBuilder:
        """
         Create builder for MapleExpBuilder class 
         Returns builder ( MapleExpBuilder NXOpen.Op): .
        """
        pass
    def CreateMathIntegrationExpBuilder(self) -> MathIntegrationExpBuilder:
        """
         Create builder for MathIntegrationExpBuilder class 
         Returns builder ( MathIntegrationExpBuilder NXOpen.Op): .
        """
        pass
    def CreateOptimizationAttributeBuilder(self) -> OptimizationAttributeBuilder:
        """
         Create builder for OptimizationAttribute class 
         Returns builder ( OptimizationAttributeBuilder NXOpen.Op): .
        """
        pass
    def CreateOptimizationBuilder(self) -> OptimizationBuilder:
        """
         Create builder for optimization class 
         Returns builder ( OptimizationBuilder NXOpen.Op): .
        """
        pass
