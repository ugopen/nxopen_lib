from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
class Category(Enum):
    """
    Members Include: 
     |OneDimension|  1D constraints 
     |TwoDimension|  2D constraints 
     |ThreeDimension|  3D constraints 
     |All|  Model constraints 

    """
    OneDimension: int
    TwoDimension: int
    ThreeDimension: int
    All: int
    @staticmethod
    def ValueOf(value: int) -> Category:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.CAE
class DAOConstraintBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.CAE.Optimization.DAOConstraintBuilder. """
    @property
    def CategoryType(self) -> Category:
        """
        Getter for property: ( Category NXOpen.CAE.) CategoryType
         Returns the category type   
            
         
        """
        pass
    @CategoryType.setter
    def CategoryType(self, category_type: Category):
        """
        Setter for property: ( Category NXOpen.CAE.) CategoryType
         Returns the category type   
            
         
        """
        pass
    @property
    def GeometryType(self) -> Geometry:
        """
        Getter for property: ( Geometry NXOpen.CAE.) GeometryType
         Returns the geometry type   
            
         
        """
        pass
    @GeometryType.setter
    def GeometryType(self, geometry_type: Geometry):
        """
        Setter for property: ( Geometry NXOpen.CAE.) GeometryType
         Returns the geometry type   
            
         
        """
        pass
    @property
    def LimitType(self) -> Limit:
        """
        Getter for property: ( Limit NXOpen.CAE.) LimitType
         Returns the limit type   
            
         
        """
        pass
    @LimitType.setter
    def LimitType(self, limit_type: Limit):
        """
        Setter for property: ( Limit NXOpen.CAE.) LimitType
         Returns the limit type   
            
         
        """
        pass
    @property
    def LimitUnit(self) -> NXOpen.Unit:
        """
        Getter for property: ( NXOpen.Unit) LimitUnit
         Returns the limit unit   
            
         
        """
        pass
    @LimitUnit.setter
    def LimitUnit(self, target_unit: NXOpen.Unit):
        """
        Setter for property: ( NXOpen.Unit) LimitUnit
         Returns the limit unit   
            
         
        """
        pass
    @property
    def LimitValue(self) -> float:
        """
        Getter for property: (float) LimitValue
         Returns the limit value   
            
         
        """
        pass
    @LimitValue.setter
    def LimitValue(self, limit_value: float):
        """
        Setter for property: (float) LimitValue
         Returns the limit value   
            
         
        """
        pass
    @property
    def LoadCase(self) -> int:
        """
        Getter for property: (int) LoadCase
         Returns the frequency load case index   
            
         
        """
        pass
    @LoadCase.setter
    def LoadCase(self, loadcase: int):
        """
        Setter for property: (int) LoadCase
         Returns the frequency load case index   
            
         
        """
        pass
    @property
    def ModeNumber(self) -> int:
        """
        Getter for property: (int) ModeNumber
         Returns the frequency mode number   
            
         
        """
        pass
    @ModeNumber.setter
    def ModeNumber(self, mode_number: int):
        """
        Setter for property: (int) ModeNumber
         Returns the frequency mode number   
            
         
        """
        pass
    @property
    def Response(self) -> Response:
        """
        Getter for property: ( Response NXOpen.CAE.) Response
         Returns the constraint response   
            
         
        """
        pass
    @Response.setter
    def Response(self, constraint_response: Response):
        """
        Setter for property: ( Response NXOpen.CAE.) Response
         Returns the constraint response   
            
         
        """
        pass
    @property
    def ResultMeasure(self) -> NXOpen.CAE.ResultMeasure:
        """
        Getter for property: ( NXOpen.CAE.ResultMeasure) ResultMeasure
         Returns the result measure   
            
         
        """
        pass
    @ResultMeasure.setter
    def ResultMeasure(self, resMeas: NXOpen.CAE.ResultMeasure):
        """
        Setter for property: ( NXOpen.CAE.ResultMeasure) ResultMeasure
         Returns the result measure   
            
         
        """
        pass
    def GetGeometry(self) -> List[NXOpen.DisplayableObject]:
        """
         Gets the target geometry 
         Returns geometry ( NXOpen.DisplayableObject Li):  Target geometry .
        """
        pass
    def SetGeometry(self, geometry: List[NXOpen.DisplayableObject]) -> None:
        """
         Sets the target geometry 
        """
        pass
import NXOpen
class DAOConstraintCollection(NXOpen.TaggedObjectCollection): 
    """ Represents the collection of optimization solution design constraint """
    def FindObject(self, design_constraint_name: str) -> DAOConstraint:
        """
         Finds an optimization solution design constraint with a specified name 
         Returns design_constraint ( DAOConstraint NXOpen.CAE.):  Design constraint .
        """
        pass
import NXOpen
class DAOConstraint(NXOpen.NXObject): 
    """ Represents a NXOpen.CAE.Optimization.DAOConstraint. """
    def GetNumberResultGroup(self) -> int:
        """
         Gets the constraint result group number 
         Returns group_number (int):  Result group number .
        """
        pass
    def GetResults(self, result_group_index: int) -> List[float]:
        """
         Gets the constraint results 
         Returns results (List[float]):  Constraint optimization results .
        """
        pass
import NXOpen
class DAODesignVariableBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.CAE.Optimization.DAODesignVariableBuilder. """
    class Variable(Enum):
        """
        Members Include: 
         |SectionProperty|  Section property variables 
         |ShellProperty|  Shell property variables 
         |FeatureDimension|  Feature dimension variables 
         |SketchDimension|  Sketch dimension variables 
         |AllExpressions|  Variables from FEM, SIM and master part 
         |Count|  Variable type count 

        """
        SectionProperty: int
        ShellProperty: int
        FeatureDimension: int
        SketchDimension: int
        AllExpressions: int
        Count: int
        @staticmethod
        def ValueOf(value: int) -> DAODesignVariableBuilder.Variable:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def GlobalSensitivityFlag(self) -> bool:
        """
        Getter for property: (bool) GlobalSensitivityFlag
         Returns the flag if mark current design variable as global sensitivity design variable, only effective for global sensitivity optimization type   
            
         
        """
        pass
    @GlobalSensitivityFlag.setter
    def GlobalSensitivityFlag(self, global_sensitivity_flag: bool):
        """
        Setter for property: (bool) GlobalSensitivityFlag
         Returns the flag if mark current design variable as global sensitivity design variable, only effective for global sensitivity optimization type   
            
         
        """
        pass
    @property
    def LowerLimit(self) -> float:
        """
        Getter for property: (float) LowerLimit
         Returns the lower limit value   
            
         
        """
        pass
    @LowerLimit.setter
    def LowerLimit(self, lower_limit: float):
        """
        Setter for property: (float) LowerLimit
         Returns the lower limit value   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the design variable name   
            
         
        """
        pass
    @Name.setter
    def Name(self, design_variable_name: str):
        """
        Setter for property: (str) Name
         Returns the design variable name   
            
         
        """
        pass
    @property
    def UpperLimit(self) -> float:
        """
        Getter for property: (float) UpperLimit
         Returns the upper limit value   
            
         
        """
        pass
    @UpperLimit.setter
    def UpperLimit(self, upper_limit: float):
        """
        Setter for property: (float) UpperLimit
         Returns the upper limit value   
            
         
        """
        pass
    def GetVariable(self) -> Tuple[DAODesignVariableBuilder.Variable, NXOpen.Expression]:
        """
         Gets the design variable 
         Returns A tuple consisting of (variable_type, variable_expression). 
         - variable_type is:  DAODesignVariableBuilder.Variable NXOpen.CAE.. Variable type .
         - variable_expression is:  NXOpen.Expression. Variable expression .

        """
        pass
    def SetVariable(self, variable_type: DAODesignVariableBuilder.Variable, variable_expression: NXOpen.Expression) -> None:
        """
         Sets the design variable 
        """
        pass
import NXOpen
class DAODesignVariableCollection(NXOpen.TaggedObjectCollection): 
    """ Represents the collection of optimization solution design variable """
    def FindObject(self, design_variable_name: str) -> DAODesignVariable:
        """
         Finds an optimization solution design variable with a specified name 
         Returns design_variable ( DAODesignVariable NXOpen.CAE.):  Design variable .
        """
        pass
import NXOpen
class DAODesignVariable(NXOpen.NXObject): 
    """ Represents a NXOpen.CAE.Optimization.DAODesignVariable. """
    def GetResults(self) -> List[float]:
        """
         Gets the design variable results 
         Returns results (List[float]):  Design variable optimization results .
        """
        pass
import NXOpen
import NXOpen.CAE
class DAOObjective(NXOpen.NXObject): 
    """ Represents a NXOpen.CAE.Optimization.DAOObjective. """
    @property
    def CategoryType(self) -> Category:
        """
        Getter for property: ( Category NXOpen.CAE.) CategoryType
         Returns the category type   
            
         
        """
        pass
    @CategoryType.setter
    def CategoryType(self, category_type: Category):
        """
        Setter for property: ( Category NXOpen.CAE.) CategoryType
         Returns the category type   
            
         
        """
        pass
    @property
    def GeometryType(self) -> Geometry:
        """
        Getter for property: ( Geometry NXOpen.CAE.) GeometryType
         Returns the geometry type   
            
         
        """
        pass
    @GeometryType.setter
    def GeometryType(self, geometry_type: Geometry):
        """
        Setter for property: ( Geometry NXOpen.CAE.) GeometryType
         Returns the geometry type   
            
         
        """
        pass
    @property
    def LoadCase(self) -> int:
        """
        Getter for property: (int) LoadCase
         Returns the frequency load case index   
            
         
        """
        pass
    @LoadCase.setter
    def LoadCase(self, loadcase: int):
        """
        Setter for property: (int) LoadCase
         Returns the frequency load case index   
            
         
        """
        pass
    @property
    def ModeNumber(self) -> int:
        """
        Getter for property: (int) ModeNumber
         Returns the frequency mode number   
            
         
        """
        pass
    @ModeNumber.setter
    def ModeNumber(self, mode_number: int):
        """
        Setter for property: (int) ModeNumber
         Returns the frequency mode number   
            
         
        """
        pass
    @property
    def ObjectiveGoal(self) -> Goal:
        """
        Getter for property: ( Goal NXOpen.CAE.) ObjectiveGoal
         Returns the objective goal   
            
         
        """
        pass
    @ObjectiveGoal.setter
    def ObjectiveGoal(self, objective_goal: Goal):
        """
        Setter for property: ( Goal NXOpen.CAE.) ObjectiveGoal
         Returns the objective goal   
            
         
        """
        pass
    @property
    def Response(self) -> Response:
        """
        Getter for property: ( Response NXOpen.CAE.) Response
         Returns the objective response   
            
         
        """
        pass
    @Response.setter
    def Response(self, objective_response: Response):
        """
        Setter for property: ( Response NXOpen.CAE.) Response
         Returns the objective response   
            
         
        """
        pass
    @property
    def ResultMeasure(self) -> NXOpen.CAE.ResultMeasure:
        """
        Getter for property: ( NXOpen.CAE.ResultMeasure) ResultMeasure
         Returns the result measure   
            
         
        """
        pass
    @ResultMeasure.setter
    def ResultMeasure(self, resMeas: NXOpen.CAE.ResultMeasure):
        """
        Setter for property: ( NXOpen.CAE.ResultMeasure) ResultMeasure
         Returns the result measure   
            
         
        """
        pass
    @property
    def TargetUnit(self) -> NXOpen.Unit:
        """
        Getter for property: ( NXOpen.Unit) TargetUnit
         Returns the target unit   
            
         
        """
        pass
    @TargetUnit.setter
    def TargetUnit(self, target_unit: NXOpen.Unit):
        """
        Setter for property: ( NXOpen.Unit) TargetUnit
         Returns the target unit   
            
         
        """
        pass
    @property
    def TargetValue(self) -> float:
        """
        Getter for property: (float) TargetValue
         Returns the target value   
            
         
        """
        pass
    @TargetValue.setter
    def TargetValue(self, target_value: float):
        """
        Setter for property: (float) TargetValue
         Returns the target value   
            
         
        """
        pass
    def GetGeometry(self) -> List[NXOpen.DisplayableObject]:
        """
         Gets the target geometry 
         Returns geometry ( NXOpen.DisplayableObject Li):  Target geometry .
        """
        pass
    def GetNumberResultGroup(self) -> int:
        """
         Gets the objective result group number 
         Returns group_number (int):  Result group number .
        """
        pass
    def GetResults(self, result_group_index: int) -> List[float]:
        """
         Gets the objective results 
         Returns results (List[float]):  Objective optimization results .
        """
        pass
    def SetGeometry(self, geometry: List[NXOpen.DisplayableObject]) -> None:
        """
         Sets the target geometry 
        """
        pass
import NXOpen
class DAOOptimizationManager(NXOpen.Object): 
    """ Represents the Design and Analysis optimization manager that contains all optimization objects. """
    @property
    def OptimizationSolution() -> DAOSolutionCollection:
        """
         Returns the optimization solution collection belonging to this sim part. 
        """
        pass
import NXOpen
import NXOpen.CAE
class DAOSolutionBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.CAE.Optimization.DAOSolutionBuilder. """
    @property
    def AnalysisSolution(self) -> NXOpen.CAE.SimSolution:
        """
        Getter for property: ( NXOpen.CAE.SimSolution) AnalysisSolution
         Returns the optimization solution analysis solution   
            
         
        """
        pass
    @AnalysisSolution.setter
    def AnalysisSolution(self, analysis_solution: NXOpen.CAE.SimSolution):
        """
        Setter for property: ( NXOpen.CAE.SimSolution) AnalysisSolution
         Returns the optimization solution analysis solution   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the optimization solution name   
            
         
        """
        pass
    @Name.setter
    def Name(self, solution_name: str):
        """
        Setter for property: (str) Name
         Returns the optimization solution name   
            
         
        """
        pass
    @property
    def SolverType(self) -> Solver:
        """
        Getter for property: ( Solver NXOpen.CAE.) SolverType
         Returns the optimization solution solver type   
            
         
        """
        pass
    @SolverType.setter
    def SolverType(self, solver_type: Solver):
        """
        Setter for property: ( Solver NXOpen.CAE.) SolverType
         Returns the optimization solution solver type   
            
         
        """
        pass
import NXOpen
class DAOSolutionCollection(NXOpen.TaggedObjectCollection): 
    """ Represents the collection of optimization solution """
    def CreateConstraintBuilder(self, design_constraint: DAOConstraint) -> DAOConstraintBuilder:
        """
         Creates the builder object of optimization solution design constraint 
         Returns builder ( DAOConstraintBuilder NXOpen.CAE.):  Design constraint builder .
        """
        pass
    def CreateDesignVariableBuilder(self, design_variable: DAODesignVariable) -> DAODesignVariableBuilder:
        """
         Creates the builder object of optimization solution design variable 
         Returns builder ( DAODesignVariableBuilder NXOpen.CAE.):  Design variable builder .
        """
        pass
    def CreateOptimizationBuilder(self, optimization_solution: DAOSolution) -> DAOSolutionBuilder:
        """
         Creates the builder object of optimization solution 
         Returns builder ( DAOSolutionBuilder NXOpen.CAE.):  Optimization solution builder .
        """
        pass
    def FindObject(self, solution_name: str) -> DAOSolution:
        """
         Finds an optimization solution with a specified name 
         Returns optimization_solution ( DAOSolution NXOpen.CAE.):  Optimization solution .
        """
        pass
import NXOpen
class DAOSolution(NXOpen.NXObject): 
    """ Represents a NXOpen.CAE.Optimization.DAOSolution. """
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the optimization solution name   
            
         
        """
        pass
    @Name.setter
    def Name(self, solution_name: str):
        """
        Setter for property: (str) Name
         Returns the optimization solution name   
            
         
        """
        pass
    @property
    def OptimizerControl(self) -> DAOStopCondition:
        """
        Getter for property: ( DAOStopCondition NXOpen.CAE.) OptimizerControl
         Returns the optimization solution optimizer control   
            
         
        """
        pass
    @OptimizerControl.setter
    def OptimizerControl(self, optimizer_control: DAOStopCondition):
        """
        Setter for property: ( DAOStopCondition NXOpen.CAE.) OptimizerControl
         Returns the optimization solution optimizer control   
            
         
        """
        pass
    @property
    def SolverType(self) -> Solver:
        """
        Getter for property: ( Solver NXOpen.CAE.) SolverType
         Returns the optimization solution solver type   
            
         
        """
        pass
    @SolverType.setter
    def SolverType(self, solver_type: Solver):
        """
        Setter for property: ( Solver NXOpen.CAE.) SolverType
         Returns the optimization solution solver type   
            
         
        """
        pass
    @property
    def DesignConstraint() -> DAOConstraintCollection:
        """
         Returns the optimization design constraint collection. 
        """
        pass
    @property
    def DesignVariable() -> DAODesignVariableCollection:
        """
         Returns the optimization design variable collection. 
        """
        pass
    def ActivateSolution(self) -> None:
        """
         Activates the optimization solution setup 
        """
        pass
    def CreateConstraintBuilder(self, optimization_constraint: DAOConstraint) -> DAOConstraintBuilder:
        """
         Creates the builder object of optimization solution design constraint 
         Returns builder ( DAOConstraintBuilder NXOpen.CAE.):  Design constraint builder .
        """
        pass
    def CreateDesignVariableBuilder(self, optimization_desvar: DAODesignVariable) -> DAODesignVariableBuilder:
        """
         Creates the builder object of optimization solution design variable 
         Returns builder ( DAODesignVariableBuilder NXOpen.CAE.):  Design variable builder .
        """
        pass
    def DeleteSolution(self) -> None:
        """
         Deletes the optimization solution 
        """
        pass
    def GetDesignConstraints(self) -> List[DAOConstraint]:
        """
         Gets the optimization solution design constraints 
         Returns design_constraints ( DAOConstraint List[NXOpen.CA):  Design constraints .
        """
        pass
    def GetDesignObjective(self) -> DAOObjective:
        """
         Gets the optimization solution design objective 
         Returns design_objective ( DAOObjective NXOpen.CAE.):  Design objective .
        """
        pass
    def GetGlobalSensitivityDesignVariables(self) -> List[DAODesignVariable]:
        """
         Gets the optimization solution design variables for global sensitivity optimization type 
         Returns design_variables ( DAODesignVariable List[NXOpen.CA):  Design variables .
        """
        pass
    def GetOptimizationDesignVariables(self) -> List[DAODesignVariable]:
        """
         Gets the optimization solution design variables for general optimization type 
         Returns design_variables ( DAODesignVariable List[NXOpen.CA):  Design variables .
        """
        pass
    def GetSolutionControls(self) -> DAOStopCondition:
        """
         Gets the optimization solution optimizer control 
         Returns optimizer_control ( DAOStopCondition NXOpen.CAE.):  Optimizer control .
        """
        pass
    def SetGlobalSensitivityDesignVariables(self, design_variables: List[DAODesignVariable]) -> None:
        """
         Sets the optimization solution design variables for global sensitivity optimization type 
        """
        pass
    def Solve(self) -> None:
        """
         Solves the optimization solution 
        """
        pass
import NXOpen
class DAOStopCondition(NXOpen.NXObject): 
    """ Represents a NXOpen.CAE.Optimization.DAOStopCondition. """
    @property
    def AbsoluteConvergence(self) -> float:
        """
        Getter for property: (float) AbsoluteConvergence
         Returns the absolute convergence   
            
         
        """
        pass
    @AbsoluteConvergence.setter
    def AbsoluteConvergence(self, absolute_convergence: float):
        """
        Setter for property: (float) AbsoluteConvergence
         Returns the absolute convergence   
            
         
        """
        pass
    @property
    def ConstraintChecking(self) -> bool:
        """
        Getter for property: (bool) ConstraintChecking
         Returns the constraint checking flag, only effective for global sensitivity optimization type   
            
         
        """
        pass
    @ConstraintChecking.setter
    def ConstraintChecking(self, constraint_checking: bool):
        """
        Setter for property: (bool) ConstraintChecking
         Returns the constraint checking flag, only effective for global sensitivity optimization type   
            
         
        """
        pass
    @property
    def MaxConstraintViolation(self) -> float:
        """
        Getter for property: (float) MaxConstraintViolation
         Returns the maximum constraint violation   
            
         
        """
        pass
    @MaxConstraintViolation.setter
    def MaxConstraintViolation(self, constraint_violation: float):
        """
        Setter for property: (float) MaxConstraintViolation
         Returns the maximum constraint violation   
            
         
        """
        pass
    @property
    def MaxIterations(self) -> int:
        """
        Getter for property: (int) MaxIterations
         Returns the maximum iteration number   
            
         
        """
        pass
    @MaxIterations.setter
    def MaxIterations(self, step_number: int):
        """
        Setter for property: (int) MaxIterations
         Returns the maximum iteration number   
            
         
        """
        pass
    @property
    def PerturbationFraction(self) -> float:
        """
        Getter for property: (float) PerturbationFraction
         Returns the perturbation fraction   
            
         
        """
        pass
    @PerturbationFraction.setter
    def PerturbationFraction(self, perturbation_fraction: float):
        """
        Setter for property: (float) PerturbationFraction
         Returns the perturbation fraction   
            
         
        """
        pass
    @property
    def RelativeConvergence(self) -> float:
        """
        Getter for property: (float) RelativeConvergence
         Returns the relative convergence   
            
         
        """
        pass
    @RelativeConvergence.setter
    def RelativeConvergence(self, relative_convergence: float):
        """
        Setter for property: (float) RelativeConvergence
         Returns the relative convergence   
            
         
        """
        pass
    @property
    def SaveAllIterationResults(self) -> bool:
        """
        Getter for property: (bool) SaveAllIterationResults
         Returns the save all interation results flag   
            
         
        """
        pass
    @SaveAllIterationResults.setter
    def SaveAllIterationResults(self, save_results: bool):
        """
        Setter for property: (bool) SaveAllIterationResults
         Returns the save all interation results flag   
            
         
        """
        pass
class Geometry(Enum):
    """
    Members Include: 
     |Body|  Body 
     |Face|  Face 
     |Edge|  Edge 
     |Point|  Point 
     |Curve|  Curve 

    """
    Body: int
    Face: int
    Edge: int
    Point: int
    Curve: int
    @staticmethod
    def ValueOf(value: int) -> Geometry:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class Goal(Enum):
    """
    Members Include: 
     |Minimum|  Minimum value 
     |Maximum|  Maximum value 
     |Target|  Target value 

    """
    Minimum: int
    Maximum: int
    Target: int
    @staticmethod
    def ValueOf(value: int) -> Goal:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class Limit(Enum):
    """
    Members Include: 
     |Upper|  Upper 
     |Lower|  Lower 

    """
    Upper: int
    Lower: int
    @staticmethod
    def ValueOf(value: int) -> Limit:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class Response(Enum):
    """
    Members Include: 
     |NotSet|   
     |Weight|   
     |Volume|   
     |Frequency|   
     |Temperature|   
     |StressVonMises|   
     |StrainVonMises|   
     |TranslationX|   
     |TranslationY|   
     |TranslationZ|   
     |RotationX|   
     |RotationY|   
     |RotationZ|   
     |Stress2DMaximumShear|   
     |Stress2DMajorPrincipal|   
     |Stress2DMinorPrincipal|   
     |Stress2DVonMises|   
     |Stress2DMaximumShearBottom|   
     |Stress2DMajorPrincipalBottom|   
     |Stress2DMinorPrincipalBottom|   
     |Stress2DVonMisesBottom|   
     |Strain2DMaximumShear|   
     |Strain2DMajorPrincipal|   
     |Strain2DMinorPrincipal|   
     |Strain2DVonMises|   
     |Strain2DMaximumShearBottom|   
     |Strain2DMajorPrincipalBottom|   
     |Strain2DMinorPrincipalBottom|   
     |Strain2DVonMisesBottom|   
     |Stress1DVonMisesStressRecoveryPointC|   
     |Stress1DVonMisesStressRecoveryPointD|   
     |Stress1DVonMisesStressRecoveryPointE|   
     |Stress1DVonMisesStressRecoveryPointF|   
     |Stress1DVonMisesMaximum|   
     |Stress1DVonMisesMinimum|   
     |Strain1DVonMisesStressRecoveryPointC|   
     |Strain1DVonMisesStressRecoveryPointD|   
     |Strain1DVonMisesStressRecoveryPointE|   
     |Strain1DVonMisesStressRecoveryPointF|   
     |Strain1DVonMisesMaximum|   
     |Strain1DVonMisesMinimum|   
     |Stress3DFirstPrincipal|   
     |Stress3DSecondPrincipal|   
     |Stress3DThirdPrincipal|   
     |Stress3DVonMises|   
     |Strain3DFirstPrincipal|   
     |Strain3DSecondPrincipal|   
     |Strain3DThirdPrincipal|   
     |Strain3DVonMises|   
     |ResultMeasure|  Response type is a result measure 

    """
    NotSet: int
    Weight: int
    Volume: int
    Frequency: int
    Temperature: int
    StressVonMises: int
    StrainVonMises: int
    TranslationX: int
    TranslationY: int
    TranslationZ: int
    RotationX: int
    RotationY: int
    RotationZ: int
    Stress2DMaximumShear: int
    Stress2DMajorPrincipal: int
    Stress2DMinorPrincipal: int
    Stress2DVonMises: int
    Stress2DMaximumShearBottom: int
    Stress2DMajorPrincipalBottom: int
    Stress2DMinorPrincipalBottom: int
    Stress2DVonMisesBottom: int
    Strain2DMaximumShear: int
    Strain2DMajorPrincipal: int
    Strain2DMinorPrincipal: int
    Strain2DVonMises: int
    Strain2DMaximumShearBottom: int
    Strain2DMajorPrincipalBottom: int
    Strain2DMinorPrincipalBottom: int
    Strain2DVonMisesBottom: int
    Stress1DVonMisesStressRecoveryPointC: int
    Stress1DVonMisesStressRecoveryPointD: int
    Stress1DVonMisesStressRecoveryPointE: int
    Stress1DVonMisesStressRecoveryPointF: int
    Stress1DVonMisesMaximum: int
    Stress1DVonMisesMinimum: int
    Strain1DVonMisesStressRecoveryPointC: int
    Strain1DVonMisesStressRecoveryPointD: int
    Strain1DVonMisesStressRecoveryPointE: int
    Strain1DVonMisesStressRecoveryPointF: int
    Strain1DVonMisesMaximum: int
    Strain1DVonMisesMinimum: int
    Stress3DFirstPrincipal: int
    Stress3DSecondPrincipal: int
    Stress3DThirdPrincipal: int
    Stress3DVonMises: int
    Strain3DFirstPrincipal: int
    Strain3DSecondPrincipal: int
    Strain3DThirdPrincipal: int
    Strain3DVonMises: int
    ResultMeasure: int
    @staticmethod
    def ValueOf(value: int) -> Response:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class Solver(Enum):
    """
    Members Include: 
     |Optimization|  Optimization 
     |GlobalSensitivity|  Global sensitivity 
     |AltairHyperOpt|  Altair HyperOpt: Deprecated in NX10 

    """
    Optimization: int
    GlobalSensitivity: int
    AltairHyperOpt: int
    @staticmethod
    def ValueOf(value: int) -> Solver:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
