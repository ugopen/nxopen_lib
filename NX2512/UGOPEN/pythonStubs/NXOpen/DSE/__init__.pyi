from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class ContinuousDesignVariableBuilder(NXOpen.Builder): 
    """ Represents Continuous Design Variable Builder class."""
    @property
    def BaselineValueExpression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BaselineValueExpression
         Returns the baseline value expression  
            
         
        """
        pass
    @property
    def BaselineValueIntExpression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BaselineValueIntExpression
         Returns the int value of baseline value expression   
            
         
        """
        pass
    @property
    def Increment(self) -> float:
        """
        Getter for property: (float) Increment
         Returns the increment   
            
         
        """
        pass
    @Increment.setter
    def Increment(self, increment: float):
        """
        Setter for property: (float) Increment
         Returns the increment   
            
         
        """
        pass
    @property
    def IncrementExpression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) IncrementExpression
         Returns the increment expression  
            
         
        """
        pass
    @property
    def IncrementIntExpression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) IncrementIntExpression
         Returns the int value of increment value expression   
            
         
        """
        pass
    @property
    def LowerLimit(self) -> float:
        """
        Getter for property: (float) LowerLimit
         Returns the lower limit   
            
         
        """
        pass
    @LowerLimit.setter
    def LowerLimit(self, lowerLimit: float):
        """
        Setter for property: (float) LowerLimit
         Returns the lower limit   
            
         
        """
        pass
    @property
    def LowerLimitExpression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LowerLimitExpression
         Returns the lower limit expression  
            
         
        """
        pass
    @property
    def LowerLimitIntExpression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LowerLimitIntExpression
         Returns the int value of lower limit expression   
            
         
        """
        pass
    @property
    def NominalValue(self) -> float:
        """
        Getter for property: (float) NominalValue
         Returns the nominal value   
            
         
        """
        pass
    @NominalValue.setter
    def NominalValue(self, nominalValue: float):
        """
        Setter for property: (float) NominalValue
         Returns the nominal value   
            
         
        """
        pass
    @property
    def UpperLimit(self) -> float:
        """
        Getter for property: (float) UpperLimit
         Returns the upper limit   
            
         
        """
        pass
    @UpperLimit.setter
    def UpperLimit(self, upperLimit: float):
        """
        Setter for property: (float) UpperLimit
         Returns the upper limit   
            
         
        """
        pass
    @property
    def UpperLimitExpression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) UpperLimitExpression
         Returns the upper limit expression  
            
         
        """
        pass
    @property
    def UpperLimitIntExpression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) UpperLimitIntExpression
         Returns the int value of upper limit expression   
            
         
        """
        pass
import NXOpen
class CopyStudyBuilder(NXOpen.Builder): 
    """ Represents Copy Study builder."""
    @property
    def ConstraintsToggle(self) -> bool:
        """
        Getter for property: (bool) ConstraintsToggle
         Returns the constraints toggle to enable copy of design constraints.  
            
         
        """
        pass
    @ConstraintsToggle.setter
    def ConstraintsToggle(self, constraintsToggle: bool):
        """
        Setter for property: (bool) ConstraintsToggle
         Returns the constraints toggle to enable copy of design constraints.  
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name of copied study.  
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name of copied study.  
            
         
        """
        pass
    @property
    def ObjectivesToggle(self) -> bool:
        """
        Getter for property: (bool) ObjectivesToggle
         Returns the objectives toggle to enable copy of design objectives.  
             
         
        """
        pass
    @ObjectivesToggle.setter
    def ObjectivesToggle(self, objectivesToggle: bool):
        """
        Setter for property: (bool) ObjectivesToggle
         Returns the objectives toggle to enable copy of design objectives.  
             
         
        """
        pass
    @property
    def ResponsesToggle(self) -> bool:
        """
        Getter for property: (bool) ResponsesToggle
         Returns the responses toggle to enable copy of design responses.  
            
         
        """
        pass
    @ResponsesToggle.setter
    def ResponsesToggle(self, responsesToggle: bool):
        """
        Setter for property: (bool) ResponsesToggle
         Returns the responses toggle to enable copy of design responses.  
            
         
        """
        pass
    @property
    def VariablesToggle(self) -> bool:
        """
        Getter for property: (bool) VariablesToggle
         Returns the variables toggle to enable copy of design variables.  
             
         
        """
        pass
    @VariablesToggle.setter
    def VariablesToggle(self, variablesToggle: bool):
        """
        Setter for property: (bool) VariablesToggle
         Returns the variables toggle to enable copy of design variables.  
             
         
        """
        pass
import NXOpen
class DesignConstraintBuilder(NXOpen.Builder): 
    """ Represents Design Constraint builder."""
    class NormalizationOption(Enum):
        """
        Members Include: 
         |UseDefault| 
         |Specify| 

        """
        UseDefault: int
        Specify: int
        @staticmethod
        def ValueOf(value: int) -> DesignConstraintBuilder.NormalizationOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TargetType(Enum):
        """
        Members Include: 
         |Equalto| 
         |GreaterthanorEqualto| 
         |LessthanorEqualto| 
         |WithinRange| 

        """
        Equalto: int
        GreaterthanorEqualto: int
        LessthanorEqualto: int
        WithinRange: int
        @staticmethod
        def ValueOf(value: int) -> DesignConstraintBuilder.TargetType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ConstraintLowerLimit(self) -> float:
        """
        Getter for property: (float) ConstraintLowerLimit
         Returns the constraint lower limit available only when target type is range  
            
         
        """
        pass
    @ConstraintLowerLimit.setter
    def ConstraintLowerLimit(self, constraintLowerLimit: float):
        """
        Setter for property: (float) ConstraintLowerLimit
         Returns the constraint lower limit available only when target type is range  
            
         
        """
        pass
    @property
    def ConstraintName(self) -> str:
        """
        Getter for property: (str) ConstraintName
         Returns the constraint name   
            
         
        """
        pass
    @ConstraintName.setter
    def ConstraintName(self, constraintName: str):
        """
        Setter for property: (str) ConstraintName
         Returns the constraint name   
            
         
        """
        pass
    @property
    def ConstraintTargetValue(self) -> float:
        """
        Getter for property: (float) ConstraintTargetValue
         Returns the constraint limit value   
            
         
        """
        pass
    @ConstraintTargetValue.setter
    def ConstraintTargetValue(self, constraintTargetValue: float):
        """
        Setter for property: (float) ConstraintTargetValue
         Returns the constraint limit value   
            
         
        """
        pass
    @property
    def ConstraintType(self) -> DesignConstraintBuilder.TargetType:
        """
        Getter for property: ( DesignConstraintBuilder.TargetType NXOp) ConstraintType
         Returns the constraint type   
            
         
        """
        pass
    @ConstraintType.setter
    def ConstraintType(self, constraintType: DesignConstraintBuilder.TargetType):
        """
        Setter for property: ( DesignConstraintBuilder.TargetType NXOp) ConstraintType
         Returns the constraint type   
            
         
        """
        pass
    @property
    def ConstraintUpperLimit(self) -> float:
        """
        Getter for property: (float) ConstraintUpperLimit
         Returns the constraint upper limit available only when target type is range  
            
         
        """
        pass
    @ConstraintUpperLimit.setter
    def ConstraintUpperLimit(self, constraintUpperLimit: float):
        """
        Setter for property: (float) ConstraintUpperLimit
         Returns the constraint upper limit available only when target type is range  
            
         
        """
        pass
    @property
    def LinearWeight(self) -> int:
        """
        Getter for property: (int) LinearWeight
         Returns the constraint linear weight   
            
         
        """
        pass
    @LinearWeight.setter
    def LinearWeight(self, linearWeight: int):
        """
        Setter for property: (int) LinearWeight
         Returns the constraint linear weight   
            
         
        """
        pass
    @property
    def LowerLimitExpression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LowerLimitExpression
         Returns the lower limit expression  
            
         
        """
        pass
    @property
    def LowerNormalizationFactor(self) -> float:
        """
        Getter for property: (float) LowerNormalizationFactor
         Returns the lower normalization factor available only when target type is range and lower normalization control is opted to specify  
            
         
        """
        pass
    @LowerNormalizationFactor.setter
    def LowerNormalizationFactor(self, lowerNormalizationFactor: float):
        """
        Setter for property: (float) LowerNormalizationFactor
         Returns the lower normalization factor available only when target type is range and lower normalization control is opted to specify  
            
         
        """
        pass
    @property
    def LowerNormalizationType(self) -> DesignConstraintBuilder.NormalizationOption:
        """
        Getter for property: ( DesignConstraintBuilder.NormalizationOption NXOp) LowerNormalizationType
         Returns the lower normalization factor control available only when target type is range  
            
         
        """
        pass
    @LowerNormalizationType.setter
    def LowerNormalizationType(self, lowerNormalizationType: DesignConstraintBuilder.NormalizationOption):
        """
        Setter for property: ( DesignConstraintBuilder.NormalizationOption NXOp) LowerNormalizationType
         Returns the lower normalization factor control available only when target type is range  
            
         
        """
        pass
    @property
    def NormalizationFactor(self) -> float:
        """
        Getter for property: (float) NormalizationFactor
         Returns the normalization factor available only when target type is not range and normalization control is opted to specify  
            
         
        """
        pass
    @NormalizationFactor.setter
    def NormalizationFactor(self, normalizationFactor: float):
        """
        Setter for property: (float) NormalizationFactor
         Returns the normalization factor available only when target type is not range and normalization control is opted to specify  
            
         
        """
        pass
    @property
    def NormalizationType(self) -> DesignConstraintBuilder.NormalizationOption:
        """
        Getter for property: ( DesignConstraintBuilder.NormalizationOption NXOp) NormalizationType
         Returns the normalization factor control available only when target type is not range  
            
         
        """
        pass
    @NormalizationType.setter
    def NormalizationType(self, normalizationType: DesignConstraintBuilder.NormalizationOption):
        """
        Setter for property: ( DesignConstraintBuilder.NormalizationOption NXOp) NormalizationType
         Returns the normalization factor control available only when target type is not range  
            
         
        """
        pass
    @property
    def QuadWeight(self) -> int:
        """
        Getter for property: (int) QuadWeight
         Returns the constraint quad weight   
            
         
        """
        pass
    @QuadWeight.setter
    def QuadWeight(self, quadWeight: int):
        """
        Setter for property: (int) QuadWeight
         Returns the constraint quad weight   
            
         
        """
        pass
    @property
    def TargetValueExpression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TargetValueExpression
         Returns the target value expression  
            
         
        """
        pass
    @property
    def UpperLimitExpression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) UpperLimitExpression
         Returns the upper limit expression  
            
         
        """
        pass
    @property
    def UpperNormalizationFactor(self) -> float:
        """
        Getter for property: (float) UpperNormalizationFactor
         Returns the upper normalization factor available only when target type is range and upper normalization control is opted to specify  
            
         
        """
        pass
    @UpperNormalizationFactor.setter
    def UpperNormalizationFactor(self, upperNormalizationFactor: float):
        """
        Setter for property: (float) UpperNormalizationFactor
         Returns the upper normalization factor available only when target type is range and upper normalization control is opted to specify  
            
         
        """
        pass
    @property
    def UpperNormalizationType(self) -> DesignConstraintBuilder.NormalizationOption:
        """
        Getter for property: ( DesignConstraintBuilder.NormalizationOption NXOp) UpperNormalizationType
         Returns the upper normalization factor control available only when target type is range  
            
         
        """
        pass
    @UpperNormalizationType.setter
    def UpperNormalizationType(self, upperNormalizationType: DesignConstraintBuilder.NormalizationOption):
        """
        Setter for property: ( DesignConstraintBuilder.NormalizationOption NXOp) UpperNormalizationType
         Returns the upper normalization factor control available only when target type is range  
            
         
        """
        pass
    def SetSelectedAppObject(self, appObject: NXOpen.TaggedObject) -> None:
        """
         Set the selected application object 
        """
        pass
    def SetSelectedAppOwnerObjectAndLookupKey(self, appOwnerObject: NXOpen.TaggedObject, appLookupKey: str) -> None:
        """
         Set the selected application owner object and lookup key 
        """
        pass
import NXOpen
class DesignConstraint(NXOpen.NXObject): 
    """ Represents a DSE.DesignConstraint class object."""
    pass
import NXOpen
class DesignFillBuilder(NXOpen.Builder): 
    """ Represents a Design Fill builder class."""
    class StrategyOptionType(Enum):
        """
        Members Include: 
         |UniformVariable| 
         |UniformDesignSpace| 
         |Balanced| 

        """
        UniformVariable: int
        UniformDesignSpace: int
        Balanced: int
        @staticmethod
        def ValueOf(value: int) -> DesignFillBuilder.StrategyOptionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def LimitTimeOption(self) -> bool:
        """
        Getter for property: (bool) LimitTimeOption
         Returns the limit time option   
            
         
        """
        pass
    @LimitTimeOption.setter
    def LimitTimeOption(self, limitTimeOption: bool):
        """
        Setter for property: (bool) LimitTimeOption
         Returns the limit time option   
            
         
        """
        pass
    @property
    def NumberOfDesigns(self) -> int:
        """
        Getter for property: (int) NumberOfDesigns
         Returns the number of designs to fill   
            
         
        """
        pass
    @NumberOfDesigns.setter
    def NumberOfDesigns(self, numberOfDesigns: int):
        """
        Setter for property: (int) NumberOfDesigns
         Returns the number of designs to fill   
            
         
        """
        pass
    @property
    def OutputOption(self) -> DesignSet.AddDesignsOption:
        """
        Getter for property: ( DesignSet.AddDesignsOption NXOp) OutputOption
         Returns the replace   
            
         
        """
        pass
    @OutputOption.setter
    def OutputOption(self, outputOption: DesignSet.AddDesignsOption):
        """
        Setter for property: ( DesignSet.AddDesignsOption NXOp) OutputOption
         Returns the replace   
            
         
        """
        pass
    @property
    def StrategyOption(self) -> DesignFillBuilder.StrategyOptionType:
        """
        Getter for property: ( DesignFillBuilder.StrategyOptionType NXOp) StrategyOption
         Returns the fill strategy option   
            
         
        """
        pass
    @StrategyOption.setter
    def StrategyOption(self, strategyOption: DesignFillBuilder.StrategyOptionType):
        """
        Setter for property: ( DesignFillBuilder.StrategyOptionType NXOp) StrategyOption
         Returns the fill strategy option   
            
         
        """
        pass
    @property
    def TimeLimit(self) -> float:
        """
        Getter for property: (float) TimeLimit
         Returns the time limit for uniform variable strategy   
            
         
        """
        pass
    @TimeLimit.setter
    def TimeLimit(self, timeLimit: float):
        """
        Setter for property: (float) TimeLimit
         Returns the time limit for uniform variable strategy   
            
         
        """
        pass
import NXOpen
class DesignObjectiveBuilder(NXOpen.Builder): 
    """ Represents Design Objective Builder class """
    class NormalizationOption(Enum):
        """
        Members Include: 
         |Baseline| 
         |Specify| 

        """
        Baseline: int
        Specify: int
        @staticmethod
        def ValueOf(value: int) -> DesignObjectiveBuilder.NormalizationOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ObjectiveTypeOption(Enum):
        """
        Members Include: 
         |Maximize| 
         |Minimize| 
         |MaximizeDifference| 
         |MinimizeDifference| 

        """
        Maximize: int
        Minimize: int
        MaximizeDifference: int
        MinimizeDifference: int
        @staticmethod
        def ValueOf(value: int) -> DesignObjectiveBuilder.ObjectiveTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def LinearWeight(self) -> int:
        """
        Getter for property: (int) LinearWeight
         Returns the objective linear weight   
            
         
        """
        pass
    @LinearWeight.setter
    def LinearWeight(self, linearWeight: int):
        """
        Setter for property: (int) LinearWeight
         Returns the objective linear weight   
            
         
        """
        pass
    @property
    def NormalizationFactor(self) -> float:
        """
        Getter for property: (float) NormalizationFactor
         Returns the objective normalization factor   
            
         
        """
        pass
    @NormalizationFactor.setter
    def NormalizationFactor(self, normalizationFactor: float):
        """
        Setter for property: (float) NormalizationFactor
         Returns the objective normalization factor   
            
         
        """
        pass
    @property
    def NormalizationType(self) -> DesignObjectiveBuilder.NormalizationOption:
        """
        Getter for property: ( DesignObjectiveBuilder.NormalizationOption NXOp) NormalizationType
         Returns the normalization factor option   
            
         
        """
        pass
    @NormalizationType.setter
    def NormalizationType(self, normalizationType: DesignObjectiveBuilder.NormalizationOption):
        """
        Setter for property: ( DesignObjectiveBuilder.NormalizationOption NXOp) NormalizationType
         Returns the normalization factor option   
            
         
        """
        pass
    @property
    def ObjectiveName(self) -> str:
        """
        Getter for property: (str) ObjectiveName
         Returns the objective name   
            
         
        """
        pass
    @ObjectiveName.setter
    def ObjectiveName(self, objectiveName: str):
        """
        Setter for property: (str) ObjectiveName
         Returns the objective name   
            
         
        """
        pass
    @property
    def ObjectiveTargetValue(self) -> float:
        """
        Getter for property: (float) ObjectiveTargetValue
         Returns the objective Target value   
            
         
        """
        pass
    @ObjectiveTargetValue.setter
    def ObjectiveTargetValue(self, objectiveTargetValue: float):
        """
        Setter for property: (float) ObjectiveTargetValue
         Returns the objective Target value   
            
         
        """
        pass
    @property
    def ObjectiveType(self) -> DesignObjectiveBuilder.ObjectiveTypeOption:
        """
        Getter for property: ( DesignObjectiveBuilder.ObjectiveTypeOption NXOp) ObjectiveType
         Returns the objective Type   
            
         
        """
        pass
    @ObjectiveType.setter
    def ObjectiveType(self, objectiveType: DesignObjectiveBuilder.ObjectiveTypeOption):
        """
        Setter for property: ( DesignObjectiveBuilder.ObjectiveTypeOption NXOp) ObjectiveType
         Returns the objective Type   
            
         
        """
        pass
    @property
    def QuadWeight(self) -> int:
        """
        Getter for property: (int) QuadWeight
         Returns the objective quad weight   
            
         
        """
        pass
    @QuadWeight.setter
    def QuadWeight(self, quadWeight: int):
        """
        Setter for property: (int) QuadWeight
         Returns the objective quad weight   
            
         
        """
        pass
    @property
    def TargetValueExpression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TargetValueExpression
         Returns the target value expression  
            
         
        """
        pass
    def SetSelectedAppObject(self, appObject: NXOpen.TaggedObject) -> None:
        """
         Set the selected application object 
        """
        pass
    def SetSelectedAppOwnerObjectAndLookupKey(self, appOwnerObject: NXOpen.TaggedObject, appLookupKey: str) -> None:
        """
         Set the selected application owner object and lookup key 
        """
        pass
import NXOpen
class DesignObjective(NXOpen.NXObject): 
    """ Represents a DSE.DesignObjective class object."""
    pass
import NXOpen
class DesignResponseBuilder(NXOpen.Builder): 
    """ Represents Design Response builder."""
    @property
    def ResponseName(self) -> str:
        """
        Getter for property: (str) ResponseName
         Returns the response name   
            
         
        """
        pass
    @ResponseName.setter
    def ResponseName(self, responseName: str):
        """
        Setter for property: (str) ResponseName
         Returns the response name   
            
         
        """
        pass
    def SetSelectedAppObject(self, appObject: NXOpen.TaggedObject) -> None:
        """
         Set the selected application object 
        """
        pass
    def SetSelectedAppOwnerObjectAndLookupKey(self, appOwnerObject: NXOpen.TaggedObject, appLookupKey: str) -> None:
        """
         Set the selected application owner object and lookup key 
        """
        pass
import NXOpen
class DesignResponse(NXOpen.NXObject): 
    """ Represents a DSE.DesignResponse class object."""
    pass
import NXOpen
class DesignSetBuilder(NXOpen.Builder): 
    """
    Builds a NXOpen.DSE.DesignSet object which
    serves to solve a set of designs without optimization.
    """
    class SolveOptionType(Enum):
        """
        Members Include: 
         |All|  All designs will be solved when the set is solved.
         |UserDefined|  Only selected designs will be solved when the set is solved.

        """
        All: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> DesignSetBuilder.SolveOptionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ErrorMessage(self) -> str:
        """
        Getter for property: (str) ErrorMessage
         Returns the design set name.  
             
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the design set name.  
             
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the design set name.  
             
         
        """
        pass
    @property
    def SolveOption(self) -> DesignSetBuilder.SolveOptionType:
        """
        Getter for property: ( DesignSetBuilder.SolveOptionType NXOp) SolveOption
         Returns the design set solve option   
            
         
        """
        pass
    @SolveOption.setter
    def SolveOption(self, solveOption: DesignSetBuilder.SolveOptionType):
        """
        Setter for property: ( DesignSetBuilder.SolveOptionType NXOp) SolveOption
         Returns the design set solve option   
            
         
        """
        pass
    def AddDesign(self, designName: str) -> int:
        """
         Add a design with baseline values of design variables. 
         Returns index (int):  The index of the design that was added .
        """
        pass
    def ClearDesigns(self) -> None:
        """
         Removes all designs except for the baseline design. 
        """
        pass
    def GetDesignFillBuilder(self) -> DesignFillBuilder:
        """
         Get the design fill builder from design set builder. 
         Returns fillBuilder ( DesignFillBuilder NXOp): .
        """
        pass
    def PopulateDesignVariables(self) -> None:
        """
         Adds all design variable of the active study. 
        """
        pass
    def PopulateOutputParameters(self) -> None:
        """
         Adds all design variable of the active study. 
        """
        pass
    def RemoveDesign(self, designName: str) -> None:
        """
         Remove a design. 
        """
        pass
    def RemoveDesignConstraint(self, var: DesignConstraint) -> None:
        """
         Remove a design constraint. 
        """
        pass
    def RemoveDesignObjective(self, var: DesignObjective) -> None:
        """
         Remove a design objective. 
        """
        pass
    def RemoveDesignResponse(self, var: DesignResponse) -> None:
        """
         Remove a design response. 
        """
        pass
    def RemoveDesignVariable(self, var: DesignVariable) -> None:
        """
         Remove a design variable. 
        """
        pass
    def SetComment(self, index: int, comment: str) -> None:
        """
         Set the comment on the design. 
        """
        pass
    def SetDesignConstraintValue(self, index: int, constraint: DesignConstraint, value: str) -> None:
        """
         Set the fixed value of the design for the given design constraint. 
        """
        pass
    def SetDesignName(self, index: int, name: str) -> None:
        """
         Set the name of the design. 
        """
        pass
    def SetDesignObjectiveValue(self, index: int, objective: DesignObjective, value: str) -> None:
        """
         Set the fixed value of the design for the given design objective. 
        """
        pass
    def SetDesignResponseValue(self, index: int, response: DesignResponse, value: str) -> None:
        """
         Set the fixed value of the design for the given design response. 
        """
        pass
    def SetDesignValue(self, index: int, var: DesignVariable, value: str) -> None:
        """
         Set the value of the design for the given design variable. 
        """
        pass
    def SetIsDesignForSolve(self, index: int, isDesignForSolve: bool) -> None:
        """
         Set if a design is going to be applied during solve. 
        """
        pass
    def SetShowOutputParameters(self, showOutputParameters: bool) -> None:
        """
         Set if the output parameters should be displayed in the design set. 
        """
        pass
import NXOpen
class DesignSet(NXOpen.NXObject): 
    """ Represents a DSE.DesignSet object."""
    class AddDesignsOption(Enum):
        """
        Members Include: 
         |Append|  Append to existing designs 
         |Replace|  Remove all existing designs before creating new ones 

        """
        Append: int
        Replace: int
        @staticmethod
        def ValueOf(value: int) -> DesignSet.AddDesignsOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def Rename(self, name: str) -> None:
        """
         Renames the design set 
        """
        pass
import NXOpen
class DesignVariableBuilder(NXOpen.Builder): 
    """ Represents Design Variable Builder class."""
    class EnumType(Enum):
        """
        Members Include: 
         |Continuous| 
         |Discrete| 

        """
        Continuous: int
        Discrete: int
        @staticmethod
        def ValueOf(value: int) -> DesignVariableBuilder.EnumType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def VariableName(self) -> str:
        """
        Getter for property: (str) VariableName
         Returns the variable name   
            
         
        """
        pass
    @VariableName.setter
    def VariableName(self, variableName: str):
        """
        Setter for property: (str) VariableName
         Returns the variable name   
            
         
        """
        pass
    @property
    def VariableType(self) -> DesignVariableBuilder.EnumType:
        """
        Getter for property: ( DesignVariableBuilder.EnumType NXOp) VariableType
         Returns the variable type   
            
         
        """
        pass
    @VariableType.setter
    def VariableType(self, variableType: DesignVariableBuilder.EnumType):
        """
        Setter for property: ( DesignVariableBuilder.EnumType NXOp) VariableType
         Returns the variable type   
            
         
        """
        pass
    def GetContinuousDesignVariableBuilder(self) -> ContinuousDesignVariableBuilder:
        """
         Get continuous design variable builder 
         Returns cdvBuilder ( ContinuousDesignVariableBuilder NXOp): .
        """
        pass
    def GetDiscreteDesignVariableBuilder(self) -> DiscreteDesignVariableBuilder:
        """
         Get discrete design variable builder 
         Returns ddvBuilder ( DiscreteDesignVariableBuilder NXOp): .
        """
        pass
    def SetSelectedAppObject(self, appObject: NXOpen.TaggedObject) -> None:
        """
         Set the selected application object 
        """
        pass
    def SetSelectedAppOwnerObjectAndLookupKey(self, appOwnerObject: NXOpen.TaggedObject, appLookupKey: str) -> None:
        """
         Set the selected application owner object and lookup key 
        """
        pass
import NXOpen
class DesignVariable(NXOpen.NXObject): 
    """ Represents a DSE.DesignVariable class object."""
    pass
import NXOpen
class Design(NXOpen.TaggedObject): 
    """ Represents a DSE.Design object."""
    pass
import NXOpen
import NXOpen.DSEPlatform
class DiscreteDesignVariableBuilder(NXOpen.Builder): 
    """ Represents Discrete Design Variable Builder class."""
    @property
    def ValuesSet(self) -> DiscreteVariableValueBuilderList:
        """
        Getter for property: ( DiscreteVariableValueBuilderList NXOp) ValuesSet
         Returns the values set   
            
         
        """
        pass
    def AddValuesToSet(self, validObjValue: NXOpen.DSEPlatform.ValidObjectValue) -> None:
        """
         Set the object 
        """
        pass
    def GetValidValuesForSelectedObject(self) -> List[NXOpen.DSEPlatform.ValidObjectValue]:
        """
         Get valid values for currently selected application object 
         Returns validObjValues ( NXOpen.DSEPlatform.ValidObjectValue Li): The array of valid values.
        """
        pass
    def RemoveValuesFromSet(self, validObjValue: NXOpen.DSEPlatform.ValidObjectValue) -> None:
        """
         Remove the object 
        """
        pass
import NXOpen
class DiscreteVariableValueBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[DiscreteVariableValueBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: DiscreteVariableValueBuilder) -> None:
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
    def Erase(self, obj: DiscreteVariableValueBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: DiscreteVariableValueBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: DiscreteVariableValueBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> DiscreteVariableValueBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( DiscreteVariableValueBuilder NXOp):  object found at input index .
        """
        pass
    def GetContents(self) -> List[DiscreteVariableValueBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( DiscreteVariableValueBuilder List[NX):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: DiscreteVariableValueBuilder) -> None:
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
    def SetContents(self, objects: List[DiscreteVariableValueBuilder]) -> None:
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
    def Swap(self, object1: DiscreteVariableValueBuilder, object2: DiscreteVariableValueBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class DiscreteVariableValueBuilder(NXOpen.Builder): 
    """ Represents Discrete Design Variable Value Builder class."""
    @property
    def DoubleValue(self) -> float:
        """
        Getter for property: (float) DoubleValue
         Returns the double   
            
         
        """
        pass
    @DoubleValue.setter
    def DoubleValue(self, doubleValue: float):
        """
        Setter for property: (float) DoubleValue
         Returns the double   
            
         
        """
        pass
    @property
    def DoubleValueExpression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DoubleValueExpression
         Returns the double value expression  
            
         
        """
        pass
    @property
    def IntValueExpression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) IntValueExpression
         Returns the int value expression   
            
         
        """
        pass
import NXOpen
class OptimizationStudyBuilder(NXOpen.Builder): 
    """ Represents Optimization Study builder."""
    @property
    def IterationRootString(self) -> str:
        """
        Getter for property: (str) IterationRootString
         Returns the iteration root string for naming iteration parts of Study  
            
         
        """
        pass
    @IterationRootString.setter
    def IterationRootString(self, iterationRootString: str):
        """
        Setter for property: (str) IterationRootString
         Returns the iteration root string for naming iteration parts of Study  
            
         
        """
        pass
    @property
    def ResultStoragePath(self) -> str:
        """
        Getter for property: (str) ResultStoragePath
         Returns the folder location to save parts   
            
         
        """
        pass
    @ResultStoragePath.setter
    def ResultStoragePath(self, foldername: str):
        """
        Setter for property: (str) ResultStoragePath
         Returns the folder location to save parts   
            
         
        """
        pass
    @property
    def StudyName(self) -> str:
        """
        Getter for property: (str) StudyName
         Returns the name of Study  
            
         
        """
        pass
    @StudyName.setter
    def StudyName(self, name: str):
        """
        Setter for property: (str) StudyName
         Returns the name of Study  
            
         
        """
        pass
import NXOpen.DSEPlatform
class OptimizationStudy(NXOpen.DSEPlatform.ExplorationStudy): 
    """ Represents a DSE.OptimizationStudy object."""
    class BaselineDesignOption(Enum):
        """
        Members Include: 
         |Neutral| 
         |Ignore| 
         |Important| 

        """
        Neutral: int
        Ignore: int
        Important: int
        @staticmethod
        def ValueOf(value: int) -> OptimizationStudy.BaselineDesignOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DesignTableOption(Enum):
        """
        Members Include: 
         |DeleteExistingandCreateNew| 
         |UseExisting| 

        """
        DeleteExistingandCreateNew: int
        UseExisting: int
        @staticmethod
        def ValueOf(value: int) -> OptimizationStudy.DesignTableOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ResultStorageOption(Enum):
        """
        Members Include: 
         |Best| 
         |FirstFeasible| 
         |AllFeasible| 
         |All| 
         |NotSet| 

        """
        Best: int
        FirstFeasible: int
        AllFeasible: int
        All: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> OptimizationStudy.ResultStorageOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RunType(Enum):
        """
        Members Include: 
         |Optimization| 
         |EvaluateOnly| 

        """
        Optimization: int
        EvaluateOnly: int
        @staticmethod
        def ValueOf(value: int) -> OptimizationStudy.RunType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SherpaMethodOption(Enum):
        """
        Members Include: 
         |WeightedSumOfAllObjectives| 
         |TradeOffStudy| 

        """
        WeightedSumOfAllObjectives: int
        TradeOffStudy: int
        @staticmethod
        def ValueOf(value: int) -> OptimizationStudy.SherpaMethodOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def AddDesignConstraint(self, desConstraint: DesignConstraint) -> None:
        """
         Set design constraint on optimization study
        """
        pass
    def AddDesignObjective(self, dvObj: DesignObjective) -> None:
        """
         Set design objective on optimization study
        """
        pass
    def AddDesignResponse(self, desResponse: DesignResponse) -> None:
        """
         Set design response on optimization study
        """
        pass
    def AddDesignSet(self, desSet: DesignSet) -> None:
        """
         Set design set on optimization study
        """
        pass
    def AddDesignVariable(self, dvObj: DesignVariable) -> None:
        """
         Set design variable on optimization study
        """
        pass
    def AddWorkflow(self, workflow: NXOpen.DSEPlatform.OptimizationWorkflow) -> None:
        """
         Set design workflow on optimization study
        """
        pass
    def ApplyDesign(self, design: Design) -> None:
        """
         Apply the given design
        """
        pass
    def DeleteDesignConstraint(self, desConstraint: DesignConstraint) -> None:
        """
         Deletes the design constraint
        """
        pass
    def DeleteDesignObjective(self, dvObj: DesignObjective) -> None:
        """
         Deletes the design objective
        """
        pass
    def DeleteDesignResponse(self, desResponse: DesignResponse) -> None:
        """
         Deletes the design response
        """
        pass
    def DeleteDesignSet(self, dvObj: DesignSet) -> None:
        """
         Deletes the design set
        """
        pass
    def DeleteDesignVariable(self, dvObj: DesignVariable) -> None:
        """
         Deletes the design variable
        """
        pass
    def DeleteResult(self, runResultObj: RunResult) -> None:
        """
         Deletes the study result
        """
        pass
    def DeleteStudy(self) -> None:
        """
         Deletes the optimization study
        """
        pass
    def DeleteStudyResults(self) -> None:
        """
         Delete Study Results 
        """
        pass
    def DeleteWorkflow(self, workflow: NXOpen.DSEPlatform.OptimizationWorkflow) -> None:
        """
         Deletes the optimization workflow
        """
        pass
    def GetArchiveSize(self) -> int:
        """
         Get Archive Size 
         Returns archiveSize (int): .
        """
        pass
    def GetBaselineDesignOption(self) -> OptimizationStudy.BaselineDesignOption:
        """
         Get the baseline design option
         Returns baselineDesignOption ( OptimizationStudy.BaselineDesignOption NXOp): .
        """
        pass
    def GetDesignConstraintAtIndex(self, index: int) -> DesignConstraint:
        """
         Get the design constraint at index from the study
         Returns desConstraint ( DesignConstraint NXOp): .
        """
        pass
    def GetDesignObjectiveAtIndex(self, index: int) -> DesignObjective:
        """
         Get the design objective at index from the study
         Returns dvObj ( DesignObjective NXOp): .
        """
        pass
    def GetDesignResponseAtIndex(self, index: int) -> DesignResponse:
        """
         Get the design response at index from the study
         Returns desResponse ( DesignResponse NXOp): .
        """
        pass
    def GetDesignSetAtIndex(self, index: int) -> DesignSet:
        """
         Get the design set at index from the study
         Returns desSet ( DesignSet NXOp): .
        """
        pass
    def GetDesignTableOption(self) -> OptimizationStudy.DesignTableOption:
        """
         Get design table option
         Returns designTableOption ( OptimizationStudy.DesignTableOption NXOp): .
        """
        pass
    def GetDesignVariableAtIndex(self, index: int) -> DesignVariable:
        """
         Get the design variable at index from the study
         Returns dvObj ( DesignVariable NXOp): .
        """
        pass
    def GetDoDisplayUpdate(self) -> bool:
        """
         Get property to update display 
         Returns shouldUpdateDisp (bool): .
        """
        pass
    def GetIteration(self) -> int:
        """
         Get iteration 
         Returns iterations (int): .
        """
        pass
    def GetLatestRunResult(self) -> RunResult:
        """
         Get latest run result
         Returns runResult ( RunResult NXOp): .
        """
        pass
    def GetNumberOfDesignConstraints(self) -> int:
        """
         Get the number of design constraints in the study
         Returns numConstraints (int): .
        """
        pass
    def GetNumberOfDesignObjectives(self) -> int:
        """
         Get the number of design objective in the study
         Returns numVar (int): .
        """
        pass
    def GetNumberOfDesignResponses(self) -> int:
        """
         Get the number of design responses in the study
         Returns numResponses (int): .
        """
        pass
    def GetNumberOfDesignSets(self) -> int:
        """
         Get the number of design sets in the study
         Returns numSets (int): .
        """
        pass
    def GetNumberOfDesignVariables(self) -> int:
        """
         Get the number of design variable in the study
         Returns numVar (int): .
        """
        pass
    def GetNumberOfRunResults(self) -> int:
        """
         Get the number of run results in the study
         Returns numRunResult (int): .
        """
        pass
    def GetNumberOfWorkflows(self) -> int:
        """
         Get the number of workflows in the study
         Returns numWorkflow (int): .
        """
        pass
    def GetRandomSeed(self) -> float:
        """
         Get the random seed 
         Returns randomSeed (float): .
        """
        pass
    def GetResultStorageOption(self) -> OptimizationStudy.ResultStorageOption:
        """
         Get save option
         Returns resultStorageOption ( OptimizationStudy.ResultStorageOption NXOp): .
        """
        pass
    def GetRunResultAtIndex(self, index: int) -> RunResult:
        """
         Get the run result at index from the study
         Returns runResultObj ( RunResult NXOp): .
        """
        pass
    def GetRunResultWithName(self, designTableName: str) -> RunResult:
        """
         Get the run result from the study when name is given
         Returns runResultObj ( RunResult NXOp): .
        """
        pass
    def GetRunType(self) -> OptimizationStudy.RunType:
        """
         Get run type
         Returns runType ( OptimizationStudy.RunType NXOp): .
        """
        pass
    def GetSherpaMethodOption(self) -> OptimizationStudy.SherpaMethodOption:
        """
         Get Sherpa Method Option
         Returns sherpaMethodOption ( OptimizationStudy.SherpaMethodOption NXOp): .
        """
        pass
    def GetWorkflowAtIndex(self, index: int) -> NXOpen.DSEPlatform.OptimizationWorkflow:
        """
         Get the workflow at index from the study
         Returns wfObj ( NXOpen.DSEPlatform.OptimizationWorkflow): .
        """
        pass
    def RunEvaluateOnly(self, designSetsToSolve: List[DesignSet]) -> None:
        """
         Run the evalaute only study 
        """
        pass
    def RunStudy(self) -> None:
        """
         Run the optimization study 
        """
        pass
    def SetArchiveSize(self, iterations: int) -> None:
        """
         Set Archive Size 
        """
        pass
    def SetBaselineDesignOption(self, baselineDesignOption: OptimizationStudy.BaselineDesignOption) -> None:
        """
         Set the baseline design option
        """
        pass
    def SetDesignTableOption(self, designTableOption: OptimizationStudy.DesignTableOption) -> None:
        """
         Set design table option
        """
        pass
    def SetDoDisplayUpdate(self, shouldUpdateDisp: bool) -> None:
        """
         Set property to update display 
        """
        pass
    def SetIteration(self, iterations: int) -> None:
        """
         Set iteration 
        """
        pass
    def SetNewRunName(self, newRunName: str) -> None:
        """
         Set the new run name, this name is cleared after subseqent call to RunStudy
        """
        pass
    def SetRandomSeed(self, randomSeed: float) -> None:
        """
         Set the random seed 
        """
        pass
    def SetResultStorageOption(self, resultStorageOption: OptimizationStudy.ResultStorageOption) -> None:
        """
         Set save option
        """
        pass
    def SetRunResultToAppend(self, runResultObj: RunResult) -> None:
        """
         Set given run result as Appending Design Table 
        """
        pass
    def SetRunType(self, runType: OptimizationStudy.RunType) -> None:
        """
         Set run type
        """
        pass
    def SetSherpaMethodOption(self, sherpaMethodOption: OptimizationStudy.SherpaMethodOption) -> None:
        """
         Set Sherpa Method Option
        """
        pass
import NXOpen
class Plot2DData(NXOpen.Builder): 
    """ Represents Plot2DData class """
    def ClearParameters(self) -> None:
        """
         Clear parameters 
        """
        pass
    def RemoveYParameterColumnIndex(self, columnID: int) -> None:
        """
         Remove the y parameter column index 
        """
        pass
    def SetXParameterColumnIndex(self, columnID: int) -> None:
        """
         Set the x parameter column index 
        """
        pass
    def SetYParameterColumnIndex(self, columnID: int) -> None:
        """
         Set the y parameter column index 
        """
        pass
class Plot2D(Plot): 
    """ Represents a DSE.Plot2D object."""
    pass
import NXOpen
class Plot3DData(NXOpen.Builder): 
    """ Represents Plot3DData class """
    def ClearParameters(self) -> None:
        """
         Clear parameters 
        """
        pass
    def RemoveZParameterColumnIndex(self, columnID: int) -> None:
        """
         Remove the z parameter column index 
        """
        pass
    def SetXParameterColumnIndex(self, columnID: int) -> None:
        """
         Set the x parameter column index 
        """
        pass
    def SetYParameterColumnIndex(self, columnID: int) -> None:
        """
         Set the y parameter column index 
        """
        pass
    def SetZParameterColumnIndex(self, columnID: int) -> None:
        """
         Set the z parameter column index 
        """
        pass
class Plot3D(Plot): 
    """ Represents a DSE.Plot3D object."""
    pass
import NXOpen
class PlotBuilder(NXOpen.Builder): 
    """ Represents Plot Builder class """
    class DesignSetType(Enum):
        """
        Members Include: 
         |All| 
         |Feasible| 
         |Infeasible| 
         |NonError| 
         |Best| 

        """
        All: int
        Feasible: int
        Infeasible: int
        NonError: int
        Best: int
        @staticmethod
        def ValueOf(value: int) -> PlotBuilder.DesignSetType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OutputPlotType(Enum):
        """
        Members Include: 
         |Series| 
         |Individually| 

        """
        Series: int
        Individually: int
        @staticmethod
        def ValueOf(value: int) -> PlotBuilder.OutputPlotType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PlotOption(Enum):
        """
        Members Include: 
         |History| 
         |Relation2D| 
         |Relation3D| 
         |ParetoFront2D| 
         |ParetoFront3D| 
         |ConstraintViolations| 

        """
        History: int
        Relation2D: int
        Relation3D: int
        ParetoFront2D: int
        ParetoFront3D: int
        ConstraintViolations: int
        @staticmethod
        def ValueOf(value: int) -> PlotBuilder.PlotOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ConstraintViolationsData(self) -> Plot2DData:
        """
        Getter for property: ( Plot2DData NXOp) ConstraintViolationsData
         Returns the constraint violations data  
            
         
        """
        pass
    @property
    def DesignSetOption(self) -> PlotBuilder.DesignSetType:
        """
        Getter for property: ( PlotBuilder.DesignSetType NXOp) DesignSetOption
         Returns the design set option   
            
         
        """
        pass
    @DesignSetOption.setter
    def DesignSetOption(self, designSetOption: PlotBuilder.DesignSetType):
        """
        Setter for property: ( PlotBuilder.DesignSetType NXOp) DesignSetOption
         Returns the design set option   
            
         
        """
        pass
    @property
    def HighlightBaselineDesign(self) -> bool:
        """
        Getter for property: (bool) HighlightBaselineDesign
         Returns the option to highlight baseline design   
            
         
        """
        pass
    @HighlightBaselineDesign.setter
    def HighlightBaselineDesign(self, highlightBaselineDesign: bool):
        """
        Setter for property: (bool) HighlightBaselineDesign
         Returns the option to highlight baseline design   
            
         
        """
        pass
    @property
    def HighlightBestDesign(self) -> bool:
        """
        Getter for property: (bool) HighlightBestDesign
         Returns the option to show best design   
            
         
        """
        pass
    @HighlightBestDesign.setter
    def HighlightBestDesign(self, showBestDesign: bool):
        """
        Setter for property: (bool) HighlightBestDesign
         Returns the option to show best design   
            
         
        """
        pass
    @property
    def HistoryData(self) -> Plot2DData:
        """
        Getter for property: ( Plot2DData NXOp) HistoryData
         Returns the history data  
            
         
        """
        pass
    @property
    def OutputPlotOption(self) -> PlotBuilder.OutputPlotType:
        """
        Getter for property: ( PlotBuilder.OutputPlotType NXOp) OutputPlotOption
         Returns the output plot option   
            
         
        """
        pass
    @OutputPlotOption.setter
    def OutputPlotOption(self, outputPlotOption: PlotBuilder.OutputPlotType):
        """
        Setter for property: ( PlotBuilder.OutputPlotType NXOp) OutputPlotOption
         Returns the output plot option   
            
         
        """
        pass
    @property
    def Pareto2DData(self) -> Plot2DData:
        """
        Getter for property: ( Plot2DData NXOp) Pareto2DData
         Returns the 2d pareto data  
            
         
        """
        pass
    @property
    def Pareto3DData(self) -> Plot3DData:
        """
        Getter for property: ( Plot3DData NXOp) Pareto3DData
         Returns the 3d pareto data  
            
         
        """
        pass
    @property
    def Relation2DData(self) -> Plot2DData:
        """
        Getter for property: ( Plot2DData NXOp) Relation2DData
         Returns the 2d relation data  
            
         
        """
        pass
    @property
    def Relation3DData(self) -> Plot3DData:
        """
        Getter for property: ( Plot3DData NXOp) Relation3DData
         Returns the 3d relation data  
            
         
        """
        pass
    @property
    def Type(self) -> PlotBuilder.PlotOption:
        """
        Getter for property: ( PlotBuilder.PlotOption NXOp) Type
         Returns the type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: PlotBuilder.PlotOption):
        """
        Setter for property: ( PlotBuilder.PlotOption NXOp) Type
         Returns the type   
            
         
        """
        pass
    def SetCurrentRunResult(self, runResultObj: RunResult) -> None:
        """
         Set the run result in plot builder 
        """
        pass
    def SetPlotNamePrefix(self, plotNamePrefix: str) -> None:
        """
         Set the plot name prefix 
        """
        pass
import NXOpen
class Plot(NXOpen.NXObject): 
    """ Represents a DSE.Plot object."""
    pass
import NXOpen
class RunResult(NXOpen.TaggedObject): 
    """ Represents a DSE.RunResult object."""
    def DeletePlot(self, plotObj: Plot) -> None:
        """
         Delete the plot from run
        """
        pass
    def GetDesignById(self, designId: int) -> Design:
        """
         Get design by designId
         Returns design ( Design NXOp): .
        """
        pass
    def GetPlotAtIndex(self, index: int) -> Plot:
        """
         Get the plot at index from the run result
         Returns plotObj ( Plot NXOp): .
        """
        pass
import NXOpen
class StudyManager(NXOpen.Object): 
    """ Represents the Design Space Explorer Study Manager class."""
    def CreateCopyStudyBuilder(part: NXOpen.BasePart, sourceStudy: OptimizationStudy) -> CopyStudyBuilder:
        """
         Creates a DSE.CopyStudyBuilder 
         Returns builder ( CopyStudyBuilder NXOp): .
        """
        pass
    def CreateDesignConstraintBuilder(part: NXOpen.BasePart, desConstraint: DesignConstraint) -> DesignConstraintBuilder:
        """
         Creates a DSE.DesignConstraintBuilder 
         Returns builder ( DesignConstraintBuilder NXOp): .
        """
        pass
    def CreateDesignObjectiveBuilder(part: NXOpen.BasePart, designObjectiveObj: DesignObjective) -> DesignObjectiveBuilder:
        """
         Creates a DSE.DesignObjectiveBuilder 
         Returns builder ( DesignObjectiveBuilder NXOp): .
        """
        pass
    def CreateDesignResponseBuilder(part: NXOpen.BasePart, desResponse: DesignResponse) -> DesignResponseBuilder:
        """
         Creates a DSE.DesignResponseBuilder 
         Returns builder ( DesignResponseBuilder NXOp): .
        """
        pass
    def CreateDesignSetBuilder(part: NXOpen.BasePart, study: OptimizationStudy, designSet: DesignSet) -> DesignSetBuilder:
        """
         Creates a DSE.DesignSetBuilder 
         Returns builder ( DesignSetBuilder NXOp): .
        """
        pass
    def CreateDesignVariableBuilder(part: NXOpen.BasePart, dvObj: DesignVariable) -> DesignVariableBuilder:
        """
         Creates a DSE.DesignVariableBuilder 
         Returns builder ( DesignVariableBuilder NXOp): .
        """
        pass
    def CreateDiscreteVariableValueBuilder(part: NXOpen.BasePart, discBuilder: DiscreteDesignVariableBuilder) -> DiscreteVariableValueBuilder:
        """
         Creates a DSE.DiscreteVariableValueBuilder 
         Returns builder ( DiscreteVariableValueBuilder NXOp): .
        """
        pass
    def CreateOptimizationStudyBuilder(part: NXOpen.BasePart, studyObj: OptimizationStudy) -> OptimizationStudyBuilder:
        """
         Creates a DSE.OptimizationStudyBuilder 
         Returns builder ( OptimizationStudyBuilder NXOp): .
        """
        pass
    def CreatePlotBuilder(part: NXOpen.BasePart, plot: Plot) -> PlotBuilder:
        """
         Creates a DSE.PlotBuilder 
         Returns builder ( PlotBuilder NXOp): .
        """
        pass
