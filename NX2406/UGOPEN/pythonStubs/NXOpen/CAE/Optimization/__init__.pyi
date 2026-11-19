from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
##  Represents the category type 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## OneDimension</term><description> 
##  1D constraints </description> </item><item><term> 
## TwoDimension</term><description> 
##  2D constraints </description> </item><item><term> 
## ThreeDimension</term><description> 
##  3D constraints </description> </item><item><term> 
## All</term><description> 
##  Model constraints </description> </item></list>
class Category(Enum):
    """
    Members Include: <OneDimension> <TwoDimension> <ThreeDimension> <All>
    """
    OneDimension: int
    TwoDimension: int
    ThreeDimension: int
    All: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> Category:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
import NXOpen.CAE
##  Represents a @link NXOpen::CAE::Optimization::DAOConstraintBuilder NXOpen::CAE::Optimization::DAOConstraintBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::CAE::Optimization::DAOSolution::CreateConstraintBuilder  NXOpen::CAE::Optimization::DAOSolution::CreateConstraintBuilder @endlink  <br> 
## 
##   <br>  Created in NX8.0.0  <br> 

class DAOConstraintBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.CAE.Optimization.DAOConstraintBuilder</ja_class>. """


    ## Getter for property: (@link Category NXOpen.CAE.Optimization.Category@endlink) CategoryType
    ##  Returns the category type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return Category
    @property
    def CategoryType(self) -> Category:
        """
        Getter for property: (@link Category NXOpen.CAE.Optimization.Category@endlink) CategoryType
         Returns the category type   
            
         
        """
        pass
    
    ## Setter for property: (@link Category NXOpen.CAE.Optimization.Category@endlink) CategoryType

    ##  Returns the category type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @CategoryType.setter
    def CategoryType(self, category_type: Category):
        """
        Setter for property: (@link Category NXOpen.CAE.Optimization.Category@endlink) CategoryType
         Returns the category type   
            
         
        """
        pass
    
    ## Getter for property: (@link Geometry NXOpen.CAE.Optimization.Geometry@endlink) GeometryType
    ##  Returns the geometry type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return Geometry
    @property
    def GeometryType(self) -> Geometry:
        """
        Getter for property: (@link Geometry NXOpen.CAE.Optimization.Geometry@endlink) GeometryType
         Returns the geometry type   
            
         
        """
        pass
    
    ## Setter for property: (@link Geometry NXOpen.CAE.Optimization.Geometry@endlink) GeometryType

    ##  Returns the geometry type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @GeometryType.setter
    def GeometryType(self, geometry_type: Geometry):
        """
        Setter for property: (@link Geometry NXOpen.CAE.Optimization.Geometry@endlink) GeometryType
         Returns the geometry type   
            
         
        """
        pass
    
    ## Getter for property: (@link Limit NXOpen.CAE.Optimization.Limit@endlink) LimitType
    ##  Returns the limit type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return Limit
    @property
    def LimitType(self) -> Limit:
        """
        Getter for property: (@link Limit NXOpen.CAE.Optimization.Limit@endlink) LimitType
         Returns the limit type   
            
         
        """
        pass
    
    ## Setter for property: (@link Limit NXOpen.CAE.Optimization.Limit@endlink) LimitType

    ##  Returns the limit type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @LimitType.setter
    def LimitType(self, limit_type: Limit):
        """
        Setter for property: (@link Limit NXOpen.CAE.Optimization.Limit@endlink) LimitType
         Returns the limit type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) LimitUnit
    ##  Returns the limit unit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return NXOpen.Unit
    @property
    def LimitUnit(self) -> NXOpen.Unit:
        """
        Getter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) LimitUnit
         Returns the limit unit   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) LimitUnit

    ##  Returns the limit unit   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @LimitUnit.setter
    def LimitUnit(self, target_unit: NXOpen.Unit):
        """
        Setter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) LimitUnit
         Returns the limit unit   
            
         
        """
        pass
    
    ## Getter for property: (float) LimitValue
    ##  Returns the limit value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return float
    @property
    def LimitValue(self) -> float:
        """
        Getter for property: (float) LimitValue
         Returns the limit value   
            
         
        """
        pass
    
    ## Setter for property: (float) LimitValue

    ##  Returns the limit value   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @LimitValue.setter
    def LimitValue(self, limit_value: float):
        """
        Setter for property: (float) LimitValue
         Returns the limit value   
            
         
        """
        pass
    
    ## Getter for property: (int) LoadCase
    ##  Returns the frequency load case index   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def LoadCase(self) -> int:
        """
        Getter for property: (int) LoadCase
         Returns the frequency load case index   
            
         
        """
        pass
    
    ## Setter for property: (int) LoadCase

    ##  Returns the frequency load case index   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @LoadCase.setter
    def LoadCase(self, loadcase: int):
        """
        Setter for property: (int) LoadCase
         Returns the frequency load case index   
            
         
        """
        pass
    
    ## Getter for property: (int) ModeNumber
    ##  Returns the frequency mode number   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return int
    @property
    def ModeNumber(self) -> int:
        """
        Getter for property: (int) ModeNumber
         Returns the frequency mode number   
            
         
        """
        pass
    
    ## Setter for property: (int) ModeNumber

    ##  Returns the frequency mode number   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @ModeNumber.setter
    def ModeNumber(self, mode_number: int):
        """
        Setter for property: (int) ModeNumber
         Returns the frequency mode number   
            
         
        """
        pass
    
    ## Getter for property: (@link Response NXOpen.CAE.Optimization.Response@endlink) Response
    ##  Returns the constraint response   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return Response
    @property
    def Response(self) -> Response:
        """
        Getter for property: (@link Response NXOpen.CAE.Optimization.Response@endlink) Response
         Returns the constraint response   
            
         
        """
        pass
    
    ## Setter for property: (@link Response NXOpen.CAE.Optimization.Response@endlink) Response

    ##  Returns the constraint response   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @Response.setter
    def Response(self, constraint_response: Response):
        """
        Setter for property: (@link Response NXOpen.CAE.Optimization.Response@endlink) Response
         Returns the constraint response   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.ResultMeasure NXOpen.CAE.ResultMeasure@endlink) ResultMeasure
    ##  Returns the result measure   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.CAE.ResultMeasure
    @property
    def ResultMeasure(self) -> NXOpen.CAE.ResultMeasure:
        """
        Getter for property: (@link NXOpen.CAE.ResultMeasure NXOpen.CAE.ResultMeasure@endlink) ResultMeasure
         Returns the result measure   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.ResultMeasure NXOpen.CAE.ResultMeasure@endlink) ResultMeasure

    ##  Returns the result measure   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ResultMeasure.setter
    def ResultMeasure(self, resMeas: NXOpen.CAE.ResultMeasure):
        """
        Setter for property: (@link NXOpen.CAE.ResultMeasure NXOpen.CAE.ResultMeasure@endlink) ResultMeasure
         Returns the result measure   
            
         
        """
        pass
    
    ##  Gets the target geometry 
    ##  @return geometry (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink):  Target geometry .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    def GetGeometry(self) -> List[NXOpen.DisplayableObject]:
        """
         Gets the target geometry 
         @return geometry (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink):  Target geometry .
        """
        pass
    
    ##  Sets the target geometry 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="geometry"> (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink)  Target geometry </param>
    def SetGeometry(self, geometry: List[NXOpen.DisplayableObject]) -> None:
        """
         Sets the target geometry 
        """
        pass
    
import NXOpen
##  Represents the collection of optimization solution design constraint  <br> To obtain an instance of this class, refer to @link NXOpen::CAE::Optimization::DAOSolution  NXOpen::CAE::Optimization::DAOSolution @endlink  <br> 
## 
##   <br>  Created in NX8.0.0  <br> 

class DAOConstraintCollection(NXOpen.TaggedObjectCollection): 
    """ Represents the collection of optimization solution design constraint """


    ##  Finds an optimization solution design constraint with a specified name 
    ##  @return design_constraint (@link DAOConstraint NXOpen.CAE.Optimization.DAOConstraint@endlink):  Design constraint .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="design_constraint_name"> (str)  Design constraint name </param>
    def FindObject(self, design_constraint_name: str) -> DAOConstraint:
        """
         Finds an optimization solution design constraint with a specified name 
         @return design_constraint (@link DAOConstraint NXOpen.CAE.Optimization.DAOConstraint@endlink):  Design constraint .
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::CAE::Optimization::DAOConstraint NXOpen::CAE::Optimization::DAOConstraint@endlink .  <br> To create or edit an instance of this class, use @link NXOpen::CAE::Optimization::DAOConstraintBuilder  NXOpen::CAE::Optimization::DAOConstraintBuilder @endlink  <br> 
## 
##   <br>  Created in NX8.0.0  <br> 

class DAOConstraint(NXOpen.NXObject): 
    """ Represents a <ja_class>NXOpen.CAE.Optimization.DAOConstraint</ja_class>. """


    ##  Gets the constraint result group number 
    ##  @return group_number (int):  Result group number .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    def GetNumberResultGroup(self) -> int:
        """
         Gets the constraint result group number 
         @return group_number (int):  Result group number .
        """
        pass
    
    ##  Gets the constraint results 
    ##  @return results (List[float]):  Constraint optimization results .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="result_group_index"> (int)  Result group index </param>
    def GetResults(self, result_group_index: int) -> List[float]:
        """
         Gets the constraint results 
         @return results (List[float]):  Constraint optimization results .
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::CAE::Optimization::DAODesignVariableBuilder NXOpen::CAE::Optimization::DAODesignVariableBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::CAE::Optimization::DAOSolution::CreateDesignVariableBuilder  NXOpen::CAE::Optimization::DAOSolution::CreateDesignVariableBuilder @endlink  <br> 
## 
##   <br>  Created in NX8.0.0  <br> 

class DAODesignVariableBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.CAE.Optimization.DAODesignVariableBuilder</ja_class>. """


    ##  Represents the design variable type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## SectionProperty</term><description> 
    ##  Section property variables </description> </item><item><term> 
    ## ShellProperty</term><description> 
    ##  Shell property variables </description> </item><item><term> 
    ## FeatureDimension</term><description> 
    ##  Feature dimension variables </description> </item><item><term> 
    ## SketchDimension</term><description> 
    ##  Sketch dimension variables </description> </item><item><term> 
    ## AllExpressions</term><description> 
    ##  Variables from FEM, SIM and master part </description> </item><item><term> 
    ## Count</term><description> 
    ##  Variable type count </description> </item></list>
    class Variable(Enum):
        """
        Members Include: <SectionProperty> <ShellProperty> <FeatureDimension> <SketchDimension> <AllExpressions> <Count>
        """
        SectionProperty: int
        ShellProperty: int
        FeatureDimension: int
        SketchDimension: int
        AllExpressions: int
        Count: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DAODesignVariableBuilder.Variable:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) GlobalSensitivityFlag
    ##  Returns the flag if mark current design variable as global sensitivity design variable, only effective for global sensitivity optimization type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return bool
    @property
    def GlobalSensitivityFlag(self) -> bool:
        """
        Getter for property: (bool) GlobalSensitivityFlag
         Returns the flag if mark current design variable as global sensitivity design variable, only effective for global sensitivity optimization type   
            
         
        """
        pass
    
    ## Setter for property: (bool) GlobalSensitivityFlag

    ##  Returns the flag if mark current design variable as global sensitivity design variable, only effective for global sensitivity optimization type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @GlobalSensitivityFlag.setter
    def GlobalSensitivityFlag(self, global_sensitivity_flag: bool):
        """
        Setter for property: (bool) GlobalSensitivityFlag
         Returns the flag if mark current design variable as global sensitivity design variable, only effective for global sensitivity optimization type   
            
         
        """
        pass
    
    ## Getter for property: (float) LowerLimit
    ##  Returns the lower limit value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return float
    @property
    def LowerLimit(self) -> float:
        """
        Getter for property: (float) LowerLimit
         Returns the lower limit value   
            
         
        """
        pass
    
    ## Setter for property: (float) LowerLimit

    ##  Returns the lower limit value   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @LowerLimit.setter
    def LowerLimit(self, lower_limit: float):
        """
        Setter for property: (float) LowerLimit
         Returns the lower limit value   
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the design variable name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the design variable name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the design variable name   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @Name.setter
    def Name(self, design_variable_name: str):
        """
        Setter for property: (str) Name
         Returns the design variable name   
            
         
        """
        pass
    
    ## Getter for property: (float) UpperLimit
    ##  Returns the upper limit value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return float
    @property
    def UpperLimit(self) -> float:
        """
        Getter for property: (float) UpperLimit
         Returns the upper limit value   
            
         
        """
        pass
    
    ## Setter for property: (float) UpperLimit

    ##  Returns the upper limit value   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @UpperLimit.setter
    def UpperLimit(self, upper_limit: float):
        """
        Setter for property: (float) UpperLimit
         Returns the upper limit value   
            
         
        """
        pass
    
    ##  Gets the design variable 
    ##  @return A tuple consisting of (variable_type, variable_expression). 
    ##  - variable_type is: @link DAODesignVariableBuilder.Variable NXOpen.CAE.Optimization.DAODesignVariableBuilder.Variable@endlink. Variable type .
    ##  - variable_expression is: @link NXOpen.Expression NXOpen.Expression@endlink. Variable expression .

    ## 
    ##   <br>  Created in NX8.0.1  <br> 

    ## License requirements: None.
    def GetVariable(self) -> Tuple[DAODesignVariableBuilder.Variable, NXOpen.Expression]:
        """
         Gets the design variable 
         @return A tuple consisting of (variable_type, variable_expression). 
         - variable_type is: @link DAODesignVariableBuilder.Variable NXOpen.CAE.Optimization.DAODesignVariableBuilder.Variable@endlink. Variable type .
         - variable_expression is: @link NXOpen.Expression NXOpen.Expression@endlink. Variable expression .

        """
        pass
    
    ##  Sets the design variable 
    ## 
    ##   <br>  Created in NX8.0.1  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="variable_type"> (@link DAODesignVariableBuilder.Variable NXOpen.CAE.Optimization.DAODesignVariableBuilder.Variable@endlink)  Variable type </param>
    ## <param name="variable_expression"> (@link NXOpen.Expression NXOpen.Expression@endlink)  Variable Expression </param>
    def SetVariable(self, variable_type: DAODesignVariableBuilder.Variable, variable_expression: NXOpen.Expression) -> None:
        """
         Sets the design variable 
        """
        pass
    
import NXOpen
##  Represents the collection of optimization solution design variable  <br> To obtain an instance of this class, refer to @link NXOpen::CAE::Optimization::DAOSolution  NXOpen::CAE::Optimization::DAOSolution @endlink  <br> 
## 
##   <br>  Created in NX8.0.0  <br> 

class DAODesignVariableCollection(NXOpen.TaggedObjectCollection): 
    """ Represents the collection of optimization solution design variable """


    ##  Finds an optimization solution design variable with a specified name 
    ##  @return design_variable (@link DAODesignVariable NXOpen.CAE.Optimization.DAODesignVariable@endlink):  Design variable .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="design_variable_name"> (str)  Design variable name </param>
    def FindObject(self, design_variable_name: str) -> DAODesignVariable:
        """
         Finds an optimization solution design variable with a specified name 
         @return design_variable (@link DAODesignVariable NXOpen.CAE.Optimization.DAODesignVariable@endlink):  Design variable .
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::CAE::Optimization::DAODesignVariable NXOpen::CAE::Optimization::DAODesignVariable@endlink .  <br> To create or edit an instance of this class, use @link NXOpen::CAE::Optimization::DAODesignVariableBuilder  NXOpen::CAE::Optimization::DAODesignVariableBuilder @endlink  <br> 
## 
##   <br>  Created in NX8.0.0  <br> 

class DAODesignVariable(NXOpen.NXObject): 
    """ Represents a <ja_class>NXOpen.CAE.Optimization.DAODesignVariable</ja_class>. """


    ##  Gets the design variable results 
    ##  @return results (List[float]):  Design variable optimization results .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    def GetResults(self) -> List[float]:
        """
         Gets the design variable results 
         @return results (List[float]):  Design variable optimization results .
        """
        pass
    
import NXOpen
import NXOpen.CAE
##  Represents a @link NXOpen::CAE::Optimization::DAOObjective NXOpen::CAE::Optimization::DAOObjective@endlink . 
## 
##   <br>  Created in NX8.0.0  <br> 

class DAOObjective(NXOpen.NXObject): 
    """ Represents a <ja_class>NXOpen.CAE.Optimization.DAOObjective</ja_class>. """


    ## Getter for property: (@link Category NXOpen.CAE.Optimization.Category@endlink) CategoryType
    ##  Returns the category type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return Category
    @property
    def CategoryType(self) -> Category:
        """
        Getter for property: (@link Category NXOpen.CAE.Optimization.Category@endlink) CategoryType
         Returns the category type   
            
         
        """
        pass
    
    ## Setter for property: (@link Category NXOpen.CAE.Optimization.Category@endlink) CategoryType

    ##  Returns the category type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @CategoryType.setter
    def CategoryType(self, category_type: Category):
        """
        Setter for property: (@link Category NXOpen.CAE.Optimization.Category@endlink) CategoryType
         Returns the category type   
            
         
        """
        pass
    
    ## Getter for property: (@link Geometry NXOpen.CAE.Optimization.Geometry@endlink) GeometryType
    ##  Returns the geometry type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return Geometry
    @property
    def GeometryType(self) -> Geometry:
        """
        Getter for property: (@link Geometry NXOpen.CAE.Optimization.Geometry@endlink) GeometryType
         Returns the geometry type   
            
         
        """
        pass
    
    ## Setter for property: (@link Geometry NXOpen.CAE.Optimization.Geometry@endlink) GeometryType

    ##  Returns the geometry type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @GeometryType.setter
    def GeometryType(self, geometry_type: Geometry):
        """
        Setter for property: (@link Geometry NXOpen.CAE.Optimization.Geometry@endlink) GeometryType
         Returns the geometry type   
            
         
        """
        pass
    
    ## Getter for property: (int) LoadCase
    ##  Returns the frequency load case index   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def LoadCase(self) -> int:
        """
        Getter for property: (int) LoadCase
         Returns the frequency load case index   
            
         
        """
        pass
    
    ## Setter for property: (int) LoadCase

    ##  Returns the frequency load case index   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @LoadCase.setter
    def LoadCase(self, loadcase: int):
        """
        Setter for property: (int) LoadCase
         Returns the frequency load case index   
            
         
        """
        pass
    
    ## Getter for property: (int) ModeNumber
    ##  Returns the frequency mode number   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def ModeNumber(self) -> int:
        """
        Getter for property: (int) ModeNumber
         Returns the frequency mode number   
            
         
        """
        pass
    
    ## Setter for property: (int) ModeNumber

    ##  Returns the frequency mode number   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ModeNumber.setter
    def ModeNumber(self, mode_number: int):
        """
        Setter for property: (int) ModeNumber
         Returns the frequency mode number   
            
         
        """
        pass
    
    ## Getter for property: (@link Goal NXOpen.CAE.Optimization.Goal@endlink) ObjectiveGoal
    ##  Returns the objective goal   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return Goal
    @property
    def ObjectiveGoal(self) -> Goal:
        """
        Getter for property: (@link Goal NXOpen.CAE.Optimization.Goal@endlink) ObjectiveGoal
         Returns the objective goal   
            
         
        """
        pass
    
    ## Setter for property: (@link Goal NXOpen.CAE.Optimization.Goal@endlink) ObjectiveGoal

    ##  Returns the objective goal   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @ObjectiveGoal.setter
    def ObjectiveGoal(self, objective_goal: Goal):
        """
        Setter for property: (@link Goal NXOpen.CAE.Optimization.Goal@endlink) ObjectiveGoal
         Returns the objective goal   
            
         
        """
        pass
    
    ## Getter for property: (@link Response NXOpen.CAE.Optimization.Response@endlink) Response
    ##  Returns the objective response   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return Response
    @property
    def Response(self) -> Response:
        """
        Getter for property: (@link Response NXOpen.CAE.Optimization.Response@endlink) Response
         Returns the objective response   
            
         
        """
        pass
    
    ## Setter for property: (@link Response NXOpen.CAE.Optimization.Response@endlink) Response

    ##  Returns the objective response   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @Response.setter
    def Response(self, objective_response: Response):
        """
        Setter for property: (@link Response NXOpen.CAE.Optimization.Response@endlink) Response
         Returns the objective response   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.ResultMeasure NXOpen.CAE.ResultMeasure@endlink) ResultMeasure
    ##  Returns the result measure   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.CAE.ResultMeasure
    @property
    def ResultMeasure(self) -> NXOpen.CAE.ResultMeasure:
        """
        Getter for property: (@link NXOpen.CAE.ResultMeasure NXOpen.CAE.ResultMeasure@endlink) ResultMeasure
         Returns the result measure   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.ResultMeasure NXOpen.CAE.ResultMeasure@endlink) ResultMeasure

    ##  Returns the result measure   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ResultMeasure.setter
    def ResultMeasure(self, resMeas: NXOpen.CAE.ResultMeasure):
        """
        Setter for property: (@link NXOpen.CAE.ResultMeasure NXOpen.CAE.ResultMeasure@endlink) ResultMeasure
         Returns the result measure   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) TargetUnit
    ##  Returns the target unit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return NXOpen.Unit
    @property
    def TargetUnit(self) -> NXOpen.Unit:
        """
        Getter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) TargetUnit
         Returns the target unit   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) TargetUnit

    ##  Returns the target unit   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @TargetUnit.setter
    def TargetUnit(self, target_unit: NXOpen.Unit):
        """
        Setter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) TargetUnit
         Returns the target unit   
            
         
        """
        pass
    
    ## Getter for property: (float) TargetValue
    ##  Returns the target value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return float
    @property
    def TargetValue(self) -> float:
        """
        Getter for property: (float) TargetValue
         Returns the target value   
            
         
        """
        pass
    
    ## Setter for property: (float) TargetValue

    ##  Returns the target value   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @TargetValue.setter
    def TargetValue(self, target_value: float):
        """
        Setter for property: (float) TargetValue
         Returns the target value   
            
         
        """
        pass
    
    ##  Gets the target geometry 
    ##  @return geometry (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink):  Target geometry .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    def GetGeometry(self) -> List[NXOpen.DisplayableObject]:
        """
         Gets the target geometry 
         @return geometry (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink):  Target geometry .
        """
        pass
    
    ##  Gets the objective result group number 
    ##  @return group_number (int):  Result group number .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    def GetNumberResultGroup(self) -> int:
        """
         Gets the objective result group number 
         @return group_number (int):  Result group number .
        """
        pass
    
    ##  Gets the objective results 
    ##  @return results (List[float]):  Objective optimization results .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="result_group_index"> (int)  Result group index </param>
    def GetResults(self, result_group_index: int) -> List[float]:
        """
         Gets the objective results 
         @return results (List[float]):  Objective optimization results .
        """
        pass
    
    ##  Sets the target geometry 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="geometry"> (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink)  Target geometry </param>
    def SetGeometry(self, geometry: List[NXOpen.DisplayableObject]) -> None:
        """
         Sets the target geometry 
        """
        pass
    
import NXOpen
##  Represents the Design and Analysis optimization manager that contains all optimization objects.  <br> To obtain an instance of this class, refer to @link NXOpen::CAE::SimSimulation  NXOpen::CAE::SimSimulation @endlink  <br> 
## 
##   <br>  Created in NX8.0.0  <br> 

class DAOOptimizationManager(NXOpen.Object): 
    """ Represents the Design and Analysis optimization manager that contains all optimization objects. """


    ##  Returns the optimization solution collection belonging to this sim part. 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @link DAOSolutionCollection NXOpen.CAE.Optimization.DAOSolutionCollection@endlink
    @property
    def OptimizationSolution() -> DAOSolutionCollection:
        """
         Returns the optimization solution collection belonging to this sim part. 
        """
        pass
    
import NXOpen
import NXOpen.CAE
##  Represents a @link NXOpen::CAE::Optimization::DAOSolutionBuilder NXOpen::CAE::Optimization::DAOSolutionBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::CAE::Optimization::DAOSolutionCollection::CreateOptimizationBuilder  NXOpen::CAE::Optimization::DAOSolutionCollection::CreateOptimizationBuilder @endlink  <br> 
## 
##   <br>  Created in NX8.0.0  <br> 

class DAOSolutionBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.CAE.Optimization.DAOSolutionBuilder</ja_class>. """


    ## Getter for property: (@link NXOpen.CAE.SimSolution NXOpen.CAE.SimSolution@endlink) AnalysisSolution
    ##  Returns the optimization solution analysis solution   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return NXOpen.CAE.SimSolution
    @property
    def AnalysisSolution(self) -> NXOpen.CAE.SimSolution:
        """
        Getter for property: (@link NXOpen.CAE.SimSolution NXOpen.CAE.SimSolution@endlink) AnalysisSolution
         Returns the optimization solution analysis solution   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.SimSolution NXOpen.CAE.SimSolution@endlink) AnalysisSolution

    ##  Returns the optimization solution analysis solution   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @AnalysisSolution.setter
    def AnalysisSolution(self, analysis_solution: NXOpen.CAE.SimSolution):
        """
        Setter for property: (@link NXOpen.CAE.SimSolution NXOpen.CAE.SimSolution@endlink) AnalysisSolution
         Returns the optimization solution analysis solution   
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the optimization solution name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the optimization solution name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the optimization solution name   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @Name.setter
    def Name(self, solution_name: str):
        """
        Setter for property: (str) Name
         Returns the optimization solution name   
            
         
        """
        pass
    
    ## Getter for property: (@link Solver NXOpen.CAE.Optimization.Solver@endlink) SolverType
    ##  Returns the optimization solution solver type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return Solver
    @property
    def SolverType(self) -> Solver:
        """
        Getter for property: (@link Solver NXOpen.CAE.Optimization.Solver@endlink) SolverType
         Returns the optimization solution solver type   
            
         
        """
        pass
    
    ## Setter for property: (@link Solver NXOpen.CAE.Optimization.Solver@endlink) SolverType

    ##  Returns the optimization solution solver type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @SolverType.setter
    def SolverType(self, solver_type: Solver):
        """
        Setter for property: (@link Solver NXOpen.CAE.Optimization.Solver@endlink) SolverType
         Returns the optimization solution solver type   
            
         
        """
        pass
    
import NXOpen
##  Represents the collection of optimization solution  <br> To obtain an instance of this class, refer to @link NXOpen::CAE::Optimization::DAOOptimizationManager  NXOpen::CAE::Optimization::DAOOptimizationManager @endlink  <br> 
## 
##   <br>  Created in NX8.0.0  <br> 

class DAOSolutionCollection(NXOpen.TaggedObjectCollection): 
    """ Represents the collection of optimization solution """


    ##  Creates the builder object of optimization solution design constraint 
    ##  @return builder (@link DAOConstraintBuilder NXOpen.CAE.Optimization.DAOConstraintBuilder@endlink):  Design constraint builder .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX9.0.0.  Use @link NXOpen::CAE::Optimization::DAOSolution::CreateConstraintBuilder NXOpen::CAE::Optimization::DAOSolution::CreateConstraintBuilder@endlink  instead.  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="design_constraint"> (@link DAOConstraint NXOpen.CAE.Optimization.DAOConstraint@endlink)  Design constraint </param>
    def CreateConstraintBuilder(self, design_constraint: DAOConstraint) -> DAOConstraintBuilder:
        """
         Creates the builder object of optimization solution design constraint 
         @return builder (@link DAOConstraintBuilder NXOpen.CAE.Optimization.DAOConstraintBuilder@endlink):  Design constraint builder .
        """
        pass
    
    ##  Creates the builder object of optimization solution design variable 
    ##  @return builder (@link DAODesignVariableBuilder NXOpen.CAE.Optimization.DAODesignVariableBuilder@endlink):  Design variable builder .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX9.0.0.  Use @link NXOpen::CAE::Optimization::DAOSolution::CreateDesignVariableBuilder NXOpen::CAE::Optimization::DAOSolution::CreateDesignVariableBuilder@endlink  instead.  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="design_variable"> (@link DAODesignVariable NXOpen.CAE.Optimization.DAODesignVariable@endlink)  Design variable </param>
    def CreateDesignVariableBuilder(self, design_variable: DAODesignVariable) -> DAODesignVariableBuilder:
        """
         Creates the builder object of optimization solution design variable 
         @return builder (@link DAODesignVariableBuilder NXOpen.CAE.Optimization.DAODesignVariableBuilder@endlink):  Design variable builder .
        """
        pass
    
    ##  Creates the builder object of optimization solution 
    ##  @return builder (@link DAOSolutionBuilder NXOpen.CAE.Optimization.DAOSolutionBuilder@endlink):  Optimization solution builder .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="optimization_solution"> (@link DAOSolution NXOpen.CAE.Optimization.DAOSolution@endlink)  Optimization solution </param>
    def CreateOptimizationBuilder(self, optimization_solution: DAOSolution) -> DAOSolutionBuilder:
        """
         Creates the builder object of optimization solution 
         @return builder (@link DAOSolutionBuilder NXOpen.CAE.Optimization.DAOSolutionBuilder@endlink):  Optimization solution builder .
        """
        pass
    
    ##  Finds an optimization solution with a specified name 
    ##  @return optimization_solution (@link DAOSolution NXOpen.CAE.Optimization.DAOSolution@endlink):  Optimization solution .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="solution_name"> (str)  Optimization solution name </param>
    def FindObject(self, solution_name: str) -> DAOSolution:
        """
         Finds an optimization solution with a specified name 
         @return optimization_solution (@link DAOSolution NXOpen.CAE.Optimization.DAOSolution@endlink):  Optimization solution .
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::CAE::Optimization::DAOSolution NXOpen::CAE::Optimization::DAOSolution@endlink .  <br> To create or edit an instance of this class, use @link NXOpen::CAE::Optimization::DAOSolutionBuilder  NXOpen::CAE::Optimization::DAOSolutionBuilder @endlink  <br> 
## 
##   <br>  Created in NX8.0.0  <br> 

class DAOSolution(NXOpen.NXObject): 
    """ Represents a <ja_class>NXOpen.CAE.Optimization.DAOSolution</ja_class>. """


    ## Getter for property: (str) Name
    ##  Returns the optimization solution name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the optimization solution name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the optimization solution name   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @Name.setter
    def Name(self, solution_name: str):
        """
        Setter for property: (str) Name
         Returns the optimization solution name   
            
         
        """
        pass
    
    ## Getter for property: (@link DAOStopCondition NXOpen.CAE.Optimization.DAOStopCondition@endlink) OptimizerControl
    ##  Returns the optimization solution optimizer control   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX9.0.0.  Not a valid method. Use @link NXOpen::CAE::Optimization::DAOSolution::GetSolutionControls NXOpen::CAE::Optimization::DAOSolution::GetSolutionControls@endlink  instead.  <br> 

    ## @return DAOStopCondition
    @property
    def OptimizerControl(self) -> DAOStopCondition:
        """
        Getter for property: (@link DAOStopCondition NXOpen.CAE.Optimization.DAOStopCondition@endlink) OptimizerControl
         Returns the optimization solution optimizer control   
            
         
        """
        pass
    
    ## Setter for property: (@link DAOStopCondition NXOpen.CAE.Optimization.DAOStopCondition@endlink) OptimizerControl

    ##  Returns the optimization solution optimizer control   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX9.0.0.  Not a valid method. Use @link NXOpen::CAE::Optimization::DAOSolution::GetSolutionControls NXOpen::CAE::Optimization::DAOSolution::GetSolutionControls@endlink  instead.  <br> 

    @OptimizerControl.setter
    def OptimizerControl(self, optimizer_control: DAOStopCondition):
        """
        Setter for property: (@link DAOStopCondition NXOpen.CAE.Optimization.DAOStopCondition@endlink) OptimizerControl
         Returns the optimization solution optimizer control   
            
         
        """
        pass
    
    ## Getter for property: (@link Solver NXOpen.CAE.Optimization.Solver@endlink) SolverType
    ##  Returns the optimization solution solver type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return Solver
    @property
    def SolverType(self) -> Solver:
        """
        Getter for property: (@link Solver NXOpen.CAE.Optimization.Solver@endlink) SolverType
         Returns the optimization solution solver type   
            
         
        """
        pass
    
    ## Setter for property: (@link Solver NXOpen.CAE.Optimization.Solver@endlink) SolverType

    ##  Returns the optimization solution solver type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @SolverType.setter
    def SolverType(self, solver_type: Solver):
        """
        Setter for property: (@link Solver NXOpen.CAE.Optimization.Solver@endlink) SolverType
         Returns the optimization solution solver type   
            
         
        """
        pass
    
    ##  Returns the optimization design constraint collection. 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @link DAOConstraintCollection NXOpen.CAE.Optimization.DAOConstraintCollection@endlink
    @property
    def DesignConstraint() -> DAOConstraintCollection:
        """
         Returns the optimization design constraint collection. 
        """
        pass
    
    ##  Returns the optimization design variable collection. 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @link DAODesignVariableCollection NXOpen.CAE.Optimization.DAODesignVariableCollection@endlink
    @property
    def DesignVariable() -> DAODesignVariableCollection:
        """
         Returns the optimization design variable collection. 
        """
        pass
    
    ##  Activates the optimization solution setup 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    def ActivateSolution(self) -> None:
        """
         Activates the optimization solution setup 
        """
        pass
    
    ##  Creates the builder object of optimization solution design constraint 
    ##  @return builder (@link DAOConstraintBuilder NXOpen.CAE.Optimization.DAOConstraintBuilder@endlink):  Design constraint builder .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="optimization_constraint"> (@link DAOConstraint NXOpen.CAE.Optimization.DAOConstraint@endlink)  Design constraint </param>
    def CreateConstraintBuilder(self, optimization_constraint: DAOConstraint) -> DAOConstraintBuilder:
        """
         Creates the builder object of optimization solution design constraint 
         @return builder (@link DAOConstraintBuilder NXOpen.CAE.Optimization.DAOConstraintBuilder@endlink):  Design constraint builder .
        """
        pass
    
    ##  Creates the builder object of optimization solution design variable 
    ##  @return builder (@link DAODesignVariableBuilder NXOpen.CAE.Optimization.DAODesignVariableBuilder@endlink):  Design variable builder .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="optimization_desvar"> (@link DAODesignVariable NXOpen.CAE.Optimization.DAODesignVariable@endlink)  Design variable </param>
    def CreateDesignVariableBuilder(self, optimization_desvar: DAODesignVariable) -> DAODesignVariableBuilder:
        """
         Creates the builder object of optimization solution design variable 
         @return builder (@link DAODesignVariableBuilder NXOpen.CAE.Optimization.DAODesignVariableBuilder@endlink):  Design variable builder .
        """
        pass
    
    ##  Deletes the optimization solution 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    def DeleteSolution(self) -> None:
        """
         Deletes the optimization solution 
        """
        pass
    
    ##  Gets the optimization solution design constraints 
    ##  @return design_constraints (@link DAOConstraint List[NXOpen.CAE.Optimization.DAOConstraint]@endlink):  Design constraints .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    def GetDesignConstraints(self) -> List[DAOConstraint]:
        """
         Gets the optimization solution design constraints 
         @return design_constraints (@link DAOConstraint List[NXOpen.CAE.Optimization.DAOConstraint]@endlink):  Design constraints .
        """
        pass
    
    ##  Gets the optimization solution design objective 
    ##  @return design_objective (@link DAOObjective NXOpen.CAE.Optimization.DAOObjective@endlink):  Design objective .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    def GetDesignObjective(self) -> DAOObjective:
        """
         Gets the optimization solution design objective 
         @return design_objective (@link DAOObjective NXOpen.CAE.Optimization.DAOObjective@endlink):  Design objective .
        """
        pass
    
    ##  Gets the optimization solution design variables for global sensitivity optimization type 
    ##  @return design_variables (@link DAODesignVariable List[NXOpen.CAE.Optimization.DAODesignVariable]@endlink):  Design variables .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    def GetGlobalSensitivityDesignVariables(self) -> List[DAODesignVariable]:
        """
         Gets the optimization solution design variables for global sensitivity optimization type 
         @return design_variables (@link DAODesignVariable List[NXOpen.CAE.Optimization.DAODesignVariable]@endlink):  Design variables .
        """
        pass
    
    ##  Gets the optimization solution design variables for general optimization type 
    ##  @return design_variables (@link DAODesignVariable List[NXOpen.CAE.Optimization.DAODesignVariable]@endlink):  Design variables .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    def GetOptimizationDesignVariables(self) -> List[DAODesignVariable]:
        """
         Gets the optimization solution design variables for general optimization type 
         @return design_variables (@link DAODesignVariable List[NXOpen.CAE.Optimization.DAODesignVariable]@endlink):  Design variables .
        """
        pass
    
    ##  Gets the optimization solution optimizer control 
    ##  @return optimizer_control (@link DAOStopCondition NXOpen.CAE.Optimization.DAOStopCondition@endlink):  Optimizer control .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    def GetSolutionControls(self) -> DAOStopCondition:
        """
         Gets the optimization solution optimizer control 
         @return optimizer_control (@link DAOStopCondition NXOpen.CAE.Optimization.DAOStopCondition@endlink):  Optimizer control .
        """
        pass
    
    ##  Sets the optimization solution design variables for global sensitivity optimization type 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="design_variables"> (@link DAODesignVariable List[NXOpen.CAE.Optimization.DAODesignVariable]@endlink)  Design variables </param>
    def SetGlobalSensitivityDesignVariables(self, design_variables: List[DAODesignVariable]) -> None:
        """
         Sets the optimization solution design variables for global sensitivity optimization type 
        """
        pass
    
    ##  Solves the optimization solution 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    def Solve(self) -> None:
        """
         Solves the optimization solution 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::CAE::Optimization::DAOStopCondition NXOpen::CAE::Optimization::DAOStopCondition@endlink . 
## 
##   <br>  Created in NX8.0.0  <br> 

class DAOStopCondition(NXOpen.NXObject): 
    """ Represents a <ja_class>NXOpen.CAE.Optimization.DAOStopCondition</ja_class>. """


    ## Getter for property: (float) AbsoluteConvergence
    ##  Returns the absolute convergence   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return float
    @property
    def AbsoluteConvergence(self) -> float:
        """
        Getter for property: (float) AbsoluteConvergence
         Returns the absolute convergence   
            
         
        """
        pass
    
    ## Setter for property: (float) AbsoluteConvergence

    ##  Returns the absolute convergence   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @AbsoluteConvergence.setter
    def AbsoluteConvergence(self, absolute_convergence: float):
        """
        Setter for property: (float) AbsoluteConvergence
         Returns the absolute convergence   
            
         
        """
        pass
    
    ## Getter for property: (bool) ConstraintChecking
    ##  Returns the constraint checking flag, only effective for global sensitivity optimization type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return bool
    @property
    def ConstraintChecking(self) -> bool:
        """
        Getter for property: (bool) ConstraintChecking
         Returns the constraint checking flag, only effective for global sensitivity optimization type   
            
         
        """
        pass
    
    ## Setter for property: (bool) ConstraintChecking

    ##  Returns the constraint checking flag, only effective for global sensitivity optimization type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @ConstraintChecking.setter
    def ConstraintChecking(self, constraint_checking: bool):
        """
        Setter for property: (bool) ConstraintChecking
         Returns the constraint checking flag, only effective for global sensitivity optimization type   
            
         
        """
        pass
    
    ## Getter for property: (float) MaxConstraintViolation
    ##  Returns the maximum constraint violation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return float
    @property
    def MaxConstraintViolation(self) -> float:
        """
        Getter for property: (float) MaxConstraintViolation
         Returns the maximum constraint violation   
            
         
        """
        pass
    
    ## Setter for property: (float) MaxConstraintViolation

    ##  Returns the maximum constraint violation   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @MaxConstraintViolation.setter
    def MaxConstraintViolation(self, constraint_violation: float):
        """
        Setter for property: (float) MaxConstraintViolation
         Returns the maximum constraint violation   
            
         
        """
        pass
    
    ## Getter for property: (int) MaxIterations
    ##  Returns the maximum iteration number   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return int
    @property
    def MaxIterations(self) -> int:
        """
        Getter for property: (int) MaxIterations
         Returns the maximum iteration number   
            
         
        """
        pass
    
    ## Setter for property: (int) MaxIterations

    ##  Returns the maximum iteration number   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @MaxIterations.setter
    def MaxIterations(self, step_number: int):
        """
        Setter for property: (int) MaxIterations
         Returns the maximum iteration number   
            
         
        """
        pass
    
    ## Getter for property: (float) PerturbationFraction
    ##  Returns the perturbation fraction   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return float
    @property
    def PerturbationFraction(self) -> float:
        """
        Getter for property: (float) PerturbationFraction
         Returns the perturbation fraction   
            
         
        """
        pass
    
    ## Setter for property: (float) PerturbationFraction

    ##  Returns the perturbation fraction   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @PerturbationFraction.setter
    def PerturbationFraction(self, perturbation_fraction: float):
        """
        Setter for property: (float) PerturbationFraction
         Returns the perturbation fraction   
            
         
        """
        pass
    
    ## Getter for property: (float) RelativeConvergence
    ##  Returns the relative convergence   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return float
    @property
    def RelativeConvergence(self) -> float:
        """
        Getter for property: (float) RelativeConvergence
         Returns the relative convergence   
            
         
        """
        pass
    
    ## Setter for property: (float) RelativeConvergence

    ##  Returns the relative convergence   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @RelativeConvergence.setter
    def RelativeConvergence(self, relative_convergence: float):
        """
        Setter for property: (float) RelativeConvergence
         Returns the relative convergence   
            
         
        """
        pass
    
    ## Getter for property: (bool) SaveAllIterationResults
    ##  Returns the save all interation results flag   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return bool
    @property
    def SaveAllIterationResults(self) -> bool:
        """
        Getter for property: (bool) SaveAllIterationResults
         Returns the save all interation results flag   
            
         
        """
        pass
    
    ## Setter for property: (bool) SaveAllIterationResults

    ##  Returns the save all interation results flag   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @SaveAllIterationResults.setter
    def SaveAllIterationResults(self, save_results: bool):
        """
        Setter for property: (bool) SaveAllIterationResults
         Returns the save all interation results flag   
            
         
        """
        pass
    
##  Represents the geometry type 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Body</term><description> 
##  Body </description> </item><item><term> 
## Face</term><description> 
##  Face </description> </item><item><term> 
## Edge</term><description> 
##  Edge </description> </item><item><term> 
## Point</term><description> 
##  Point </description> </item><item><term> 
## Curve</term><description> 
##  Curve </description> </item></list>
class Geometry(Enum):
    """
    Members Include: <Body> <Face> <Edge> <Point> <Curve>
    """
    Body: int
    Face: int
    Edge: int
    Point: int
    Curve: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> Geometry:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the goal type 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Minimum</term><description> 
##  Minimum value </description> </item><item><term> 
## Maximum</term><description> 
##  Maximum value </description> </item><item><term> 
## Target</term><description> 
##  Target value </description> </item></list>
class Goal(Enum):
    """
    Members Include: <Minimum> <Maximum> <Target>
    """
    Minimum: int
    Maximum: int
    Target: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> Goal:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the limit type 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Upper</term><description> 
##  Upper </description> </item><item><term> 
## Lower</term><description> 
##  Lower </description> </item></list>
class Limit(Enum):
    """
    Members Include: <Upper> <Lower>
    """
    Upper: int
    Lower: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> Limit:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the specific variable 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## NotSet</term><description> 
##   </description> </item><item><term> 
## Weight</term><description> 
##   </description> </item><item><term> 
## Volume</term><description> 
##   </description> </item><item><term> 
## Frequency</term><description> 
##   </description> </item><item><term> 
## Temperature</term><description> 
##   </description> </item><item><term> 
## StressVonMises</term><description> 
##   </description> </item><item><term> 
## StrainVonMises</term><description> 
##   </description> </item><item><term> 
## TranslationX</term><description> 
##   </description> </item><item><term> 
## TranslationY</term><description> 
##   </description> </item><item><term> 
## TranslationZ</term><description> 
##   </description> </item><item><term> 
## RotationX</term><description> 
##   </description> </item><item><term> 
## RotationY</term><description> 
##   </description> </item><item><term> 
## RotationZ</term><description> 
##   </description> </item><item><term> 
## Stress2DMaximumShear</term><description> 
##   </description> </item><item><term> 
## Stress2DMajorPrincipal</term><description> 
##   </description> </item><item><term> 
## Stress2DMinorPrincipal</term><description> 
##   </description> </item><item><term> 
## Stress2DVonMises</term><description> 
##   </description> </item><item><term> 
## Stress2DMaximumShearBottom</term><description> 
##   </description> </item><item><term> 
## Stress2DMajorPrincipalBottom</term><description> 
##   </description> </item><item><term> 
## Stress2DMinorPrincipalBottom</term><description> 
##   </description> </item><item><term> 
## Stress2DVonMisesBottom</term><description> 
##   </description> </item><item><term> 
## Strain2DMaximumShear</term><description> 
##   </description> </item><item><term> 
## Strain2DMajorPrincipal</term><description> 
##   </description> </item><item><term> 
## Strain2DMinorPrincipal</term><description> 
##   </description> </item><item><term> 
## Strain2DVonMises</term><description> 
##   </description> </item><item><term> 
## Strain2DMaximumShearBottom</term><description> 
##   </description> </item><item><term> 
## Strain2DMajorPrincipalBottom</term><description> 
##   </description> </item><item><term> 
## Strain2DMinorPrincipalBottom</term><description> 
##   </description> </item><item><term> 
## Strain2DVonMisesBottom</term><description> 
##   </description> </item><item><term> 
## Stress1DVonMisesStressRecoveryPointC</term><description> 
##   </description> </item><item><term> 
## Stress1DVonMisesStressRecoveryPointD</term><description> 
##   </description> </item><item><term> 
## Stress1DVonMisesStressRecoveryPointE</term><description> 
##   </description> </item><item><term> 
## Stress1DVonMisesStressRecoveryPointF</term><description> 
##   </description> </item><item><term> 
## Stress1DVonMisesMaximum</term><description> 
##   </description> </item><item><term> 
## Stress1DVonMisesMinimum</term><description> 
##   </description> </item><item><term> 
## Strain1DVonMisesStressRecoveryPointC</term><description> 
##   </description> </item><item><term> 
## Strain1DVonMisesStressRecoveryPointD</term><description> 
##   </description> </item><item><term> 
## Strain1DVonMisesStressRecoveryPointE</term><description> 
##   </description> </item><item><term> 
## Strain1DVonMisesStressRecoveryPointF</term><description> 
##   </description> </item><item><term> 
## Strain1DVonMisesMaximum</term><description> 
##   </description> </item><item><term> 
## Strain1DVonMisesMinimum</term><description> 
##   </description> </item><item><term> 
## Stress3DFirstPrincipal</term><description> 
##   </description> </item><item><term> 
## Stress3DSecondPrincipal</term><description> 
##   </description> </item><item><term> 
## Stress3DThirdPrincipal</term><description> 
##   </description> </item><item><term> 
## Stress3DVonMises</term><description> 
##   </description> </item><item><term> 
## Strain3DFirstPrincipal</term><description> 
##   </description> </item><item><term> 
## Strain3DSecondPrincipal</term><description> 
##   </description> </item><item><term> 
## Strain3DThirdPrincipal</term><description> 
##   </description> </item><item><term> 
## Strain3DVonMises</term><description> 
##   </description> </item><item><term> 
## ResultMeasure</term><description> 
##  Response type is a result measure </description> </item></list>
class Response(Enum):
    """
    Members Include: <NotSet> <Weight> <Volume> <Frequency> <Temperature> <StressVonMises> <StrainVonMises> <TranslationX> <TranslationY> <TranslationZ> <RotationX> <RotationY> <RotationZ> <Stress2DMaximumShear> <Stress2DMajorPrincipal> <Stress2DMinorPrincipal> <Stress2DVonMises> <Stress2DMaximumShearBottom> <Stress2DMajorPrincipalBottom> <Stress2DMinorPrincipalBottom> <Stress2DVonMisesBottom> <Strain2DMaximumShear> <Strain2DMajorPrincipal> <Strain2DMinorPrincipal> <Strain2DVonMises> <Strain2DMaximumShearBottom> <Strain2DMajorPrincipalBottom> <Strain2DMinorPrincipalBottom> <Strain2DVonMisesBottom> <Stress1DVonMisesStressRecoveryPointC> <Stress1DVonMisesStressRecoveryPointD> <Stress1DVonMisesStressRecoveryPointE> <Stress1DVonMisesStressRecoveryPointF> <Stress1DVonMisesMaximum> <Stress1DVonMisesMinimum> <Strain1DVonMisesStressRecoveryPointC> <Strain1DVonMisesStressRecoveryPointD> <Strain1DVonMisesStressRecoveryPointE> <Strain1DVonMisesStressRecoveryPointF> <Strain1DVonMisesMaximum> <Strain1DVonMisesMinimum> <Stress3DFirstPrincipal> <Stress3DSecondPrincipal> <Stress3DThirdPrincipal> <Stress3DVonMises> <Strain3DFirstPrincipal> <Strain3DSecondPrincipal> <Strain3DThirdPrincipal> <Strain3DVonMises> <ResultMeasure>
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
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> Response:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the optimization solution solver type 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Optimization</term><description> 
##  Optimization </description> </item><item><term> 
## GlobalSensitivity</term><description> 
##  Global sensitivity </description> </item><item><term> 
## AltairHyperOpt</term><description> 
##  Altair HyperOpt: Deprecated in NX10 </description> </item></list>
class Solver(Enum):
    """
    Members Include: <Optimization> <GlobalSensitivity> <AltairHyperOpt>
    """
    Optimization: int
    GlobalSensitivity: int
    AltairHyperOpt: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> Solver:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


## @package NXOpen.CAE.Optimization
## Classes, Enums and Structs under NXOpen.CAE.Optimization namespace

##  @link DAODesignVariableBuilderVariable NXOpen.CAE.Optimization.DAODesignVariableBuilderVariable @endlink is an alias for @link DAODesignVariableBuilder.Variable NXOpen.CAE.Optimization.DAODesignVariableBuilder.Variable@endlink
DAODesignVariableBuilderVariable = DAODesignVariableBuilder.Variable


