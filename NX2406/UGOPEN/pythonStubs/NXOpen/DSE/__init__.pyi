from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents Continuous Design Variable Builder class. <br> To create a new instance of this class, use @link NXOpen::DSE::DesignVariableBuilder::GetContinuousDesignVariableBuilder  NXOpen::DSE::DesignVariableBuilder::GetContinuousDesignVariableBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ContinuousDesignVariableBuilder(NXOpen.Builder): 
    """ Represents Continuous Design Variable Builder class."""


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BaselineValueExpression
    ##  Returns the baseline value expression  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def BaselineValueExpression(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BaselineValueExpression
         Returns the baseline value expression  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BaselineValueIntExpression
    ##  Returns the int value of baseline value expression   
    ##     
    ##  
    ## Getter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def BaselineValueIntExpression(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BaselineValueIntExpression
         Returns the int value of baseline value expression   
            
         
        """
        pass
    
    ## Getter for property: (float) Increment
    ##  Returns the increment   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2212.0.0.  Use @link DSE::ContinuousDesignVariableBuilder::IncrementExpression DSE::ContinuousDesignVariableBuilder::IncrementExpression@endlink  instead.  <br> 

    ## @return float
    @property
    def Increment(self) -> float:
        """
        Getter for property: (float) Increment
         Returns the increment   
            
         
        """
        pass
    
    ## Setter for property: (float) Increment

    ##  Returns the increment   
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2212.0.0.  Use @link DSE::ContinuousDesignVariableBuilder::IncrementExpression DSE::ContinuousDesignVariableBuilder::IncrementExpression@endlink  instead.  <br> 

    @Increment.setter
    def Increment(self, increment: float):
        """
        Setter for property: (float) Increment
         Returns the increment   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) IncrementExpression
    ##  Returns the increment expression  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def IncrementExpression(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) IncrementExpression
         Returns the increment expression  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) IncrementIntExpression
    ##  Returns the int value of increment value expression   
    ##     
    ##  
    ## Getter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def IncrementIntExpression(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) IncrementIntExpression
         Returns the int value of increment value expression   
            
         
        """
        pass
    
    ## Getter for property: (float) LowerLimit
    ##  Returns the lower limit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2212.0.0.  Use @link DSE::ContinuousDesignVariableBuilder::LowerLimitExpression DSE::ContinuousDesignVariableBuilder::LowerLimitExpression@endlink  instead.  <br> 

    ## @return float
    @property
    def LowerLimit(self) -> float:
        """
        Getter for property: (float) LowerLimit
         Returns the lower limit   
            
         
        """
        pass
    
    ## Setter for property: (float) LowerLimit

    ##  Returns the lower limit   
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2212.0.0.  Use @link DSE::ContinuousDesignVariableBuilder::LowerLimitExpression DSE::ContinuousDesignVariableBuilder::LowerLimitExpression@endlink  instead.  <br> 

    @LowerLimit.setter
    def LowerLimit(self, lowerLimit: float):
        """
        Setter for property: (float) LowerLimit
         Returns the lower limit   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LowerLimitExpression
    ##  Returns the lower limit expression  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LowerLimitExpression(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LowerLimitExpression
         Returns the lower limit expression  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LowerLimitIntExpression
    ##  Returns the int value of lower limit expression   
    ##     
    ##  
    ## Getter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LowerLimitIntExpression(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LowerLimitIntExpression
         Returns the int value of lower limit expression   
            
         
        """
        pass
    
    ## Getter for property: (float) NominalValue
    ##  Returns the nominal value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2212.0.0.  Use @link DSE::ContinuousDesignVariableBuilder::BaselineValueExpression DSE::ContinuousDesignVariableBuilder::BaselineValueExpression@endlink  instead.  <br> 

    ## @return float
    @property
    def NominalValue(self) -> float:
        """
        Getter for property: (float) NominalValue
         Returns the nominal value   
            
         
        """
        pass
    
    ## Setter for property: (float) NominalValue

    ##  Returns the nominal value   
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2212.0.0.  Use @link DSE::ContinuousDesignVariableBuilder::BaselineValueExpression DSE::ContinuousDesignVariableBuilder::BaselineValueExpression@endlink  instead.  <br> 

    @NominalValue.setter
    def NominalValue(self, nominalValue: float):
        """
        Setter for property: (float) NominalValue
         Returns the nominal value   
            
         
        """
        pass
    
    ## Getter for property: (float) UpperLimit
    ##  Returns the upper limit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2212.0.0.  Use @link DSE::ContinuousDesignVariableBuilder::UpperLimitExpression DSE::ContinuousDesignVariableBuilder::UpperLimitExpression@endlink  instead.  <br> 

    ## @return float
    @property
    def UpperLimit(self) -> float:
        """
        Getter for property: (float) UpperLimit
         Returns the upper limit   
            
         
        """
        pass
    
    ## Setter for property: (float) UpperLimit

    ##  Returns the upper limit   
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2212.0.0.  Use @link DSE::ContinuousDesignVariableBuilder::UpperLimitExpression DSE::ContinuousDesignVariableBuilder::UpperLimitExpression@endlink  instead.  <br> 

    @UpperLimit.setter
    def UpperLimit(self, upperLimit: float):
        """
        Setter for property: (float) UpperLimit
         Returns the upper limit   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) UpperLimitExpression
    ##  Returns the upper limit expression  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def UpperLimitExpression(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) UpperLimitExpression
         Returns the upper limit expression  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) UpperLimitIntExpression
    ##  Returns the int value of upper limit expression   
    ##     
    ##  
    ## Getter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def UpperLimitIntExpression(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) UpperLimitIntExpression
         Returns the int value of upper limit expression   
            
         
        """
        pass
    
import NXOpen
##  Represents Copy Study builder. <br> To create a new instance of this class, use @link NXOpen::DSE::StudyManager::CreateCopyStudyBuilder  NXOpen::DSE::StudyManager::CreateCopyStudyBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class CopyStudyBuilder(NXOpen.Builder): 
    """ Represents Copy Study builder."""


    ## Getter for property: (bool) ConstraintsToggle
    ##  Returns the constraints toggle to enable copy of design constraints.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def ConstraintsToggle(self) -> bool:
        """
        Getter for property: (bool) ConstraintsToggle
         Returns the constraints toggle to enable copy of design constraints.  
            
         
        """
        pass
    
    ## Setter for property: (bool) ConstraintsToggle

    ##  Returns the constraints toggle to enable copy of design constraints.  
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @ConstraintsToggle.setter
    def ConstraintsToggle(self, constraintsToggle: bool):
        """
        Setter for property: (bool) ConstraintsToggle
         Returns the constraints toggle to enable copy of design constraints.  
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the name of copied study.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name of copied study.  
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the name of copied study.  
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name of copied study.  
            
         
        """
        pass
    
    ## Getter for property: (bool) ObjectivesToggle
    ##  Returns the objectives toggle to enable copy of design objectives.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def ObjectivesToggle(self) -> bool:
        """
        Getter for property: (bool) ObjectivesToggle
         Returns the objectives toggle to enable copy of design objectives.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ObjectivesToggle

    ##  Returns the objectives toggle to enable copy of design objectives.  
    ##      
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @ObjectivesToggle.setter
    def ObjectivesToggle(self, objectivesToggle: bool):
        """
        Setter for property: (bool) ObjectivesToggle
         Returns the objectives toggle to enable copy of design objectives.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ResponsesToggle
    ##  Returns the responses toggle to enable copy of design responses.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return bool
    @property
    def ResponsesToggle(self) -> bool:
        """
        Getter for property: (bool) ResponsesToggle
         Returns the responses toggle to enable copy of design responses.  
            
         
        """
        pass
    
    ## Setter for property: (bool) ResponsesToggle

    ##  Returns the responses toggle to enable copy of design responses.  
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @ResponsesToggle.setter
    def ResponsesToggle(self, responsesToggle: bool):
        """
        Setter for property: (bool) ResponsesToggle
         Returns the responses toggle to enable copy of design responses.  
            
         
        """
        pass
    
    ## Getter for property: (bool) VariablesToggle
    ##  Returns the variables toggle to enable copy of design variables.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def VariablesToggle(self) -> bool:
        """
        Getter for property: (bool) VariablesToggle
         Returns the variables toggle to enable copy of design variables.  
             
         
        """
        pass
    
    ## Setter for property: (bool) VariablesToggle

    ##  Returns the variables toggle to enable copy of design variables.  
    ##      
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @VariablesToggle.setter
    def VariablesToggle(self, variablesToggle: bool):
        """
        Setter for property: (bool) VariablesToggle
         Returns the variables toggle to enable copy of design variables.  
             
         
        """
        pass
    
import NXOpen
##  Represents Design Constraint builder. <br> To create a new instance of this class, use @link NXOpen::DSE::StudyManager::CreateDesignConstraintBuilder  NXOpen::DSE::StudyManager::CreateDesignConstraintBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class DesignConstraintBuilder(NXOpen.Builder): 
    """ Represents Design Constraint builder."""


    ##  Represents normalization controls to define default normalisation factor or to specify.
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## UseDefault</term><description> 
    ## </description> </item><item><term> 
    ## Specify</term><description> 
    ## </description> </item></list>
    class NormalizationOption(Enum):
        """
        Members Include: <UseDefault> <Specify>
        """
        UseDefault: int
        Specify: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DesignConstraintBuilder.NormalizationOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents different target type options to compare for Constraint.
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Equalto</term><description> 
    ## </description> </item><item><term> 
    ## GreaterthanorEqualto</term><description> 
    ## </description> </item><item><term> 
    ## LessthanorEqualto</term><description> 
    ## </description> </item><item><term> 
    ## WithinRange</term><description> 
    ## </description> </item></list>
    class TargetType(Enum):
        """
        Members Include: <Equalto> <GreaterthanorEqualto> <LessthanorEqualto> <WithinRange>
        """
        Equalto: int
        GreaterthanorEqualto: int
        LessthanorEqualto: int
        WithinRange: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DesignConstraintBuilder.TargetType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) ConstraintLowerLimit
    ##  Returns the constraint lower limit available only when target type is range  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2212.0.0.  Use @link DSE::DesignConstraintBuilder::LowerLimitExpression DSE::DesignConstraintBuilder::LowerLimitExpression@endlink  instead.  <br> 

    ## @return float
    @property
    def ConstraintLowerLimit(self) -> float:
        """
        Getter for property: (float) ConstraintLowerLimit
         Returns the constraint lower limit available only when target type is range  
            
         
        """
        pass
    
    ## Setter for property: (float) ConstraintLowerLimit

    ##  Returns the constraint lower limit available only when target type is range  
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2212.0.0.  Use @link DSE::DesignConstraintBuilder::LowerLimitExpression DSE::DesignConstraintBuilder::LowerLimitExpression@endlink  instead.  <br> 

    @ConstraintLowerLimit.setter
    def ConstraintLowerLimit(self, constraintLowerLimit: float):
        """
        Setter for property: (float) ConstraintLowerLimit
         Returns the constraint lower limit available only when target type is range  
            
         
        """
        pass
    
    ## Getter for property: (str) ConstraintName
    ##  Returns the constraint name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return str
    @property
    def ConstraintName(self) -> str:
        """
        Getter for property: (str) ConstraintName
         Returns the constraint name   
            
         
        """
        pass
    
    ## Setter for property: (str) ConstraintName

    ##  Returns the constraint name   
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ConstraintName.setter
    def ConstraintName(self, constraintName: str):
        """
        Setter for property: (str) ConstraintName
         Returns the constraint name   
            
         
        """
        pass
    
    ## Getter for property: (float) ConstraintTargetValue
    ##  Returns the constraint limit value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2212.0.0.  Use @link DSE::DesignConstraintBuilder::TargetValueExpression DSE::DesignConstraintBuilder::TargetValueExpression@endlink  instead.  <br> 

    ## @return float
    @property
    def ConstraintTargetValue(self) -> float:
        """
        Getter for property: (float) ConstraintTargetValue
         Returns the constraint limit value   
            
         
        """
        pass
    
    ## Setter for property: (float) ConstraintTargetValue

    ##  Returns the constraint limit value   
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2212.0.0.  Use @link DSE::DesignConstraintBuilder::TargetValueExpression DSE::DesignConstraintBuilder::TargetValueExpression@endlink  instead.  <br> 

    @ConstraintTargetValue.setter
    def ConstraintTargetValue(self, constraintTargetValue: float):
        """
        Setter for property: (float) ConstraintTargetValue
         Returns the constraint limit value   
            
         
        """
        pass
    
    ## Getter for property: (@link DesignConstraintBuilder.TargetType NXOpen.DSE.DesignConstraintBuilder.TargetType@endlink) ConstraintType
    ##  Returns the constraint type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return DesignConstraintBuilder.TargetType
    @property
    def ConstraintType(self) -> DesignConstraintBuilder.TargetType:
        """
        Getter for property: (@link DesignConstraintBuilder.TargetType NXOpen.DSE.DesignConstraintBuilder.TargetType@endlink) ConstraintType
         Returns the constraint type   
            
         
        """
        pass
    
    ## Setter for property: (@link DesignConstraintBuilder.TargetType NXOpen.DSE.DesignConstraintBuilder.TargetType@endlink) ConstraintType

    ##  Returns the constraint type   
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ConstraintType.setter
    def ConstraintType(self, constraintType: DesignConstraintBuilder.TargetType):
        """
        Setter for property: (@link DesignConstraintBuilder.TargetType NXOpen.DSE.DesignConstraintBuilder.TargetType@endlink) ConstraintType
         Returns the constraint type   
            
         
        """
        pass
    
    ## Getter for property: (float) ConstraintUpperLimit
    ##  Returns the constraint upper limit available only when target type is range  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2212.0.0.  Use @link DSE::DesignConstraintBuilder::UpperLimitExpression DSE::DesignConstraintBuilder::UpperLimitExpression@endlink  instead.  <br> 

    ## @return float
    @property
    def ConstraintUpperLimit(self) -> float:
        """
        Getter for property: (float) ConstraintUpperLimit
         Returns the constraint upper limit available only when target type is range  
            
         
        """
        pass
    
    ## Setter for property: (float) ConstraintUpperLimit

    ##  Returns the constraint upper limit available only when target type is range  
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2212.0.0.  Use @link DSE::DesignConstraintBuilder::UpperLimitExpression DSE::DesignConstraintBuilder::UpperLimitExpression@endlink  instead.  <br> 

    @ConstraintUpperLimit.setter
    def ConstraintUpperLimit(self, constraintUpperLimit: float):
        """
        Setter for property: (float) ConstraintUpperLimit
         Returns the constraint upper limit available only when target type is range  
            
         
        """
        pass
    
    ## Getter for property: (int) LinearWeight
    ##  Returns the constraint linear weight   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return int
    @property
    def LinearWeight(self) -> int:
        """
        Getter for property: (int) LinearWeight
         Returns the constraint linear weight   
            
         
        """
        pass
    
    ## Setter for property: (int) LinearWeight

    ##  Returns the constraint linear weight   
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @LinearWeight.setter
    def LinearWeight(self, linearWeight: int):
        """
        Setter for property: (int) LinearWeight
         Returns the constraint linear weight   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LowerLimitExpression
    ##  Returns the lower limit expression  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LowerLimitExpression(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LowerLimitExpression
         Returns the lower limit expression  
            
         
        """
        pass
    
    ## Getter for property: (float) LowerNormalizationFactor
    ##  Returns the lower normalization factor available only when target type is range and lower normalization control is opted to specify  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return float
    @property
    def LowerNormalizationFactor(self) -> float:
        """
        Getter for property: (float) LowerNormalizationFactor
         Returns the lower normalization factor available only when target type is range and lower normalization control is opted to specify  
            
         
        """
        pass
    
    ## Setter for property: (float) LowerNormalizationFactor

    ##  Returns the lower normalization factor available only when target type is range and lower normalization control is opted to specify  
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @LowerNormalizationFactor.setter
    def LowerNormalizationFactor(self, lowerNormalizationFactor: float):
        """
        Setter for property: (float) LowerNormalizationFactor
         Returns the lower normalization factor available only when target type is range and lower normalization control is opted to specify  
            
         
        """
        pass
    
    ## Getter for property: (@link DesignConstraintBuilder.NormalizationOption NXOpen.DSE.DesignConstraintBuilder.NormalizationOption@endlink) LowerNormalizationType
    ##  Returns the lower normalization factor control available only when target type is range  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return DesignConstraintBuilder.NormalizationOption
    @property
    def LowerNormalizationType(self) -> DesignConstraintBuilder.NormalizationOption:
        """
        Getter for property: (@link DesignConstraintBuilder.NormalizationOption NXOpen.DSE.DesignConstraintBuilder.NormalizationOption@endlink) LowerNormalizationType
         Returns the lower normalization factor control available only when target type is range  
            
         
        """
        pass
    
    ## Setter for property: (@link DesignConstraintBuilder.NormalizationOption NXOpen.DSE.DesignConstraintBuilder.NormalizationOption@endlink) LowerNormalizationType

    ##  Returns the lower normalization factor control available only when target type is range  
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @LowerNormalizationType.setter
    def LowerNormalizationType(self, lowerNormalizationType: DesignConstraintBuilder.NormalizationOption):
        """
        Setter for property: (@link DesignConstraintBuilder.NormalizationOption NXOpen.DSE.DesignConstraintBuilder.NormalizationOption@endlink) LowerNormalizationType
         Returns the lower normalization factor control available only when target type is range  
            
         
        """
        pass
    
    ## Getter for property: (float) NormalizationFactor
    ##  Returns the normalization factor available only when target type is not range and normalization control is opted to specify  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return float
    @property
    def NormalizationFactor(self) -> float:
        """
        Getter for property: (float) NormalizationFactor
         Returns the normalization factor available only when target type is not range and normalization control is opted to specify  
            
         
        """
        pass
    
    ## Setter for property: (float) NormalizationFactor

    ##  Returns the normalization factor available only when target type is not range and normalization control is opted to specify  
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @NormalizationFactor.setter
    def NormalizationFactor(self, normalizationFactor: float):
        """
        Setter for property: (float) NormalizationFactor
         Returns the normalization factor available only when target type is not range and normalization control is opted to specify  
            
         
        """
        pass
    
    ## Getter for property: (@link DesignConstraintBuilder.NormalizationOption NXOpen.DSE.DesignConstraintBuilder.NormalizationOption@endlink) NormalizationType
    ##  Returns the normalization factor control available only when target type is not range  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return DesignConstraintBuilder.NormalizationOption
    @property
    def NormalizationType(self) -> DesignConstraintBuilder.NormalizationOption:
        """
        Getter for property: (@link DesignConstraintBuilder.NormalizationOption NXOpen.DSE.DesignConstraintBuilder.NormalizationOption@endlink) NormalizationType
         Returns the normalization factor control available only when target type is not range  
            
         
        """
        pass
    
    ## Setter for property: (@link DesignConstraintBuilder.NormalizationOption NXOpen.DSE.DesignConstraintBuilder.NormalizationOption@endlink) NormalizationType

    ##  Returns the normalization factor control available only when target type is not range  
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @NormalizationType.setter
    def NormalizationType(self, normalizationType: DesignConstraintBuilder.NormalizationOption):
        """
        Setter for property: (@link DesignConstraintBuilder.NormalizationOption NXOpen.DSE.DesignConstraintBuilder.NormalizationOption@endlink) NormalizationType
         Returns the normalization factor control available only when target type is not range  
            
         
        """
        pass
    
    ## Getter for property: (int) QuadWeight
    ##  Returns the constraint quad weight   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return int
    @property
    def QuadWeight(self) -> int:
        """
        Getter for property: (int) QuadWeight
         Returns the constraint quad weight   
            
         
        """
        pass
    
    ## Setter for property: (int) QuadWeight

    ##  Returns the constraint quad weight   
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @QuadWeight.setter
    def QuadWeight(self, quadWeight: int):
        """
        Setter for property: (int) QuadWeight
         Returns the constraint quad weight   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TargetValueExpression
    ##  Returns the target value expression  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def TargetValueExpression(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TargetValueExpression
         Returns the target value expression  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) UpperLimitExpression
    ##  Returns the upper limit expression  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def UpperLimitExpression(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) UpperLimitExpression
         Returns the upper limit expression  
            
         
        """
        pass
    
    ## Getter for property: (float) UpperNormalizationFactor
    ##  Returns the upper normalization factor available only when target type is range and upper normalization control is opted to specify  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return float
    @property
    def UpperNormalizationFactor(self) -> float:
        """
        Getter for property: (float) UpperNormalizationFactor
         Returns the upper normalization factor available only when target type is range and upper normalization control is opted to specify  
            
         
        """
        pass
    
    ## Setter for property: (float) UpperNormalizationFactor

    ##  Returns the upper normalization factor available only when target type is range and upper normalization control is opted to specify  
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @UpperNormalizationFactor.setter
    def UpperNormalizationFactor(self, upperNormalizationFactor: float):
        """
        Setter for property: (float) UpperNormalizationFactor
         Returns the upper normalization factor available only when target type is range and upper normalization control is opted to specify  
            
         
        """
        pass
    
    ## Getter for property: (@link DesignConstraintBuilder.NormalizationOption NXOpen.DSE.DesignConstraintBuilder.NormalizationOption@endlink) UpperNormalizationType
    ##  Returns the upper normalization factor control available only when target type is range  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return DesignConstraintBuilder.NormalizationOption
    @property
    def UpperNormalizationType(self) -> DesignConstraintBuilder.NormalizationOption:
        """
        Getter for property: (@link DesignConstraintBuilder.NormalizationOption NXOpen.DSE.DesignConstraintBuilder.NormalizationOption@endlink) UpperNormalizationType
         Returns the upper normalization factor control available only when target type is range  
            
         
        """
        pass
    
    ## Setter for property: (@link DesignConstraintBuilder.NormalizationOption NXOpen.DSE.DesignConstraintBuilder.NormalizationOption@endlink) UpperNormalizationType

    ##  Returns the upper normalization factor control available only when target type is range  
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @UpperNormalizationType.setter
    def UpperNormalizationType(self, upperNormalizationType: DesignConstraintBuilder.NormalizationOption):
        """
        Setter for property: (@link DesignConstraintBuilder.NormalizationOption NXOpen.DSE.DesignConstraintBuilder.NormalizationOption@endlink) UpperNormalizationType
         Returns the upper normalization factor control available only when target type is range  
            
         
        """
        pass
    
    ##  Set the selected application object 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="appObject"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def SetSelectedAppObject(self, appObject: NXOpen.TaggedObject) -> None:
        """
         Set the selected application object 
        """
        pass
    
    ##  Set the selected application owner object and lookup key 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="appOwnerObject"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    ## <param name="appLookupKey"> (str) </param>
    def SetSelectedAppOwnerObjectAndLookupKey(self, appOwnerObject: NXOpen.TaggedObject, appLookupKey: str) -> None:
        """
         Set the selected application owner object and lookup key 
        """
        pass
    
import NXOpen
##  Represents a @link DSE::DesignConstraint DSE::DesignConstraint@endlink  class object. <br> To create or edit an instance of this class, use @link NXOpen::DSE::DesignConstraintBuilder  NXOpen::DSE::DesignConstraintBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class DesignConstraint(NXOpen.NXObject): 
    """ Represents a <ja_class>DSE.DesignConstraint</ja_class> class object."""
    pass


import NXOpen
##  Represents Design Objective Builder class  <br> To create a new instance of this class, use @link NXOpen::DSE::StudyManager::CreateDesignObjectiveBuilder  NXOpen::DSE::StudyManager::CreateDesignObjectiveBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class DesignObjectiveBuilder(NXOpen.Builder): 
    """ Represents Design Objective Builder class """


    ##  Represents normalization option to define default normalisation factor or to specify.
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Baseline</term><description> 
    ## </description> </item><item><term> 
    ## Specify</term><description> 
    ## </description> </item></list>
    class NormalizationOption(Enum):
        """
        Members Include: <Baseline> <Specify>
        """
        Baseline: int
        Specify: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DesignObjectiveBuilder.NormalizationOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents Design objective enum type.
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Maximize</term><description> 
    ## </description> </item><item><term> 
    ## Minimize</term><description> 
    ## </description> </item><item><term> 
    ## MaximizeDifference</term><description> 
    ## </description> </item><item><term> 
    ## MinimizeDifference</term><description> 
    ## </description> </item></list>
    class ObjectiveTypeOption(Enum):
        """
        Members Include: <Maximize> <Minimize> <MaximizeDifference> <MinimizeDifference>
        """
        Maximize: int
        Minimize: int
        MaximizeDifference: int
        MinimizeDifference: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DesignObjectiveBuilder.ObjectiveTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (int) LinearWeight
    ##  Returns the objective linear weight   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return int
    @property
    def LinearWeight(self) -> int:
        """
        Getter for property: (int) LinearWeight
         Returns the objective linear weight   
            
         
        """
        pass
    
    ## Setter for property: (int) LinearWeight

    ##  Returns the objective linear weight   
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @LinearWeight.setter
    def LinearWeight(self, linearWeight: int):
        """
        Setter for property: (int) LinearWeight
         Returns the objective linear weight   
            
         
        """
        pass
    
    ## Getter for property: (float) NormalizationFactor
    ##  Returns the objective normalization factor   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return float
    @property
    def NormalizationFactor(self) -> float:
        """
        Getter for property: (float) NormalizationFactor
         Returns the objective normalization factor   
            
         
        """
        pass
    
    ## Setter for property: (float) NormalizationFactor

    ##  Returns the objective normalization factor   
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @NormalizationFactor.setter
    def NormalizationFactor(self, normalizationFactor: float):
        """
        Setter for property: (float) NormalizationFactor
         Returns the objective normalization factor   
            
         
        """
        pass
    
    ## Getter for property: (@link DesignObjectiveBuilder.NormalizationOption NXOpen.DSE.DesignObjectiveBuilder.NormalizationOption@endlink) NormalizationType
    ##  Returns the normalization factor option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return DesignObjectiveBuilder.NormalizationOption
    @property
    def NormalizationType(self) -> DesignObjectiveBuilder.NormalizationOption:
        """
        Getter for property: (@link DesignObjectiveBuilder.NormalizationOption NXOpen.DSE.DesignObjectiveBuilder.NormalizationOption@endlink) NormalizationType
         Returns the normalization factor option   
            
         
        """
        pass
    
    ## Setter for property: (@link DesignObjectiveBuilder.NormalizationOption NXOpen.DSE.DesignObjectiveBuilder.NormalizationOption@endlink) NormalizationType

    ##  Returns the normalization factor option   
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @NormalizationType.setter
    def NormalizationType(self, normalizationType: DesignObjectiveBuilder.NormalizationOption):
        """
        Setter for property: (@link DesignObjectiveBuilder.NormalizationOption NXOpen.DSE.DesignObjectiveBuilder.NormalizationOption@endlink) NormalizationType
         Returns the normalization factor option   
            
         
        """
        pass
    
    ## Getter for property: (str) ObjectiveName
    ##  Returns the objective name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return str
    @property
    def ObjectiveName(self) -> str:
        """
        Getter for property: (str) ObjectiveName
         Returns the objective name   
            
         
        """
        pass
    
    ## Setter for property: (str) ObjectiveName

    ##  Returns the objective name   
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ObjectiveName.setter
    def ObjectiveName(self, objectiveName: str):
        """
        Setter for property: (str) ObjectiveName
         Returns the objective name   
            
         
        """
        pass
    
    ## Getter for property: (float) ObjectiveTargetValue
    ##  Returns the objective Target value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2212.0.0.  Use @link DSE::DesignObjectiveBuilder::TargetValueExpression DSE::DesignObjectiveBuilder::TargetValueExpression@endlink  instead.  <br> 

    ## @return float
    @property
    def ObjectiveTargetValue(self) -> float:
        """
        Getter for property: (float) ObjectiveTargetValue
         Returns the objective Target value   
            
         
        """
        pass
    
    ## Setter for property: (float) ObjectiveTargetValue

    ##  Returns the objective Target value   
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2212.0.0.  Use @link DSE::DesignObjectiveBuilder::TargetValueExpression DSE::DesignObjectiveBuilder::TargetValueExpression@endlink  instead.  <br> 

    @ObjectiveTargetValue.setter
    def ObjectiveTargetValue(self, objectiveTargetValue: float):
        """
        Setter for property: (float) ObjectiveTargetValue
         Returns the objective Target value   
            
         
        """
        pass
    
    ## Getter for property: (@link DesignObjectiveBuilder.ObjectiveTypeOption NXOpen.DSE.DesignObjectiveBuilder.ObjectiveTypeOption@endlink) ObjectiveType
    ##  Returns the objective Type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return DesignObjectiveBuilder.ObjectiveTypeOption
    @property
    def ObjectiveType(self) -> DesignObjectiveBuilder.ObjectiveTypeOption:
        """
        Getter for property: (@link DesignObjectiveBuilder.ObjectiveTypeOption NXOpen.DSE.DesignObjectiveBuilder.ObjectiveTypeOption@endlink) ObjectiveType
         Returns the objective Type   
            
         
        """
        pass
    
    ## Setter for property: (@link DesignObjectiveBuilder.ObjectiveTypeOption NXOpen.DSE.DesignObjectiveBuilder.ObjectiveTypeOption@endlink) ObjectiveType

    ##  Returns the objective Type   
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ObjectiveType.setter
    def ObjectiveType(self, objectiveType: DesignObjectiveBuilder.ObjectiveTypeOption):
        """
        Setter for property: (@link DesignObjectiveBuilder.ObjectiveTypeOption NXOpen.DSE.DesignObjectiveBuilder.ObjectiveTypeOption@endlink) ObjectiveType
         Returns the objective Type   
            
         
        """
        pass
    
    ## Getter for property: (int) QuadWeight
    ##  Returns the objective quad weight   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return int
    @property
    def QuadWeight(self) -> int:
        """
        Getter for property: (int) QuadWeight
         Returns the objective quad weight   
            
         
        """
        pass
    
    ## Setter for property: (int) QuadWeight

    ##  Returns the objective quad weight   
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @QuadWeight.setter
    def QuadWeight(self, quadWeight: int):
        """
        Setter for property: (int) QuadWeight
         Returns the objective quad weight   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TargetValueExpression
    ##  Returns the target value expression  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def TargetValueExpression(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TargetValueExpression
         Returns the target value expression  
            
         
        """
        pass
    
    ##  Set the selected application object 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="appObject"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def SetSelectedAppObject(self, appObject: NXOpen.TaggedObject) -> None:
        """
         Set the selected application object 
        """
        pass
    
    ##  Set the selected application owner object and lookup key 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="appOwnerObject"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    ## <param name="appLookupKey"> (str) </param>
    def SetSelectedAppOwnerObjectAndLookupKey(self, appOwnerObject: NXOpen.TaggedObject, appLookupKey: str) -> None:
        """
         Set the selected application owner object and lookup key 
        """
        pass
    
import NXOpen
##  Represents a @link DSE::DesignObjective DSE::DesignObjective@endlink  class object. <br> To create or edit an instance of this class, use @link NXOpen::DSE::DesignObjectiveBuilder  NXOpen::DSE::DesignObjectiveBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class DesignObjective(NXOpen.NXObject): 
    """ Represents a <ja_class>DSE.DesignObjective</ja_class> class object."""
    pass


import NXOpen
##  Represents Design Response builder. <br> To create a new instance of this class, use @link NXOpen::DSE::StudyManager::CreateDesignResponseBuilder  NXOpen::DSE::StudyManager::CreateDesignResponseBuilder @endlink  <br> 
## 
##   <br>  Created in NX2406.0.0  <br> 

class DesignResponseBuilder(NXOpen.Builder): 
    """ Represents Design Response builder."""


    ## Getter for property: (str) ResponseName
    ##  Returns the response name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return str
    @property
    def ResponseName(self) -> str:
        """
        Getter for property: (str) ResponseName
         Returns the response name   
            
         
        """
        pass
    
    ## Setter for property: (str) ResponseName

    ##  Returns the response name   
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @ResponseName.setter
    def ResponseName(self, responseName: str):
        """
        Setter for property: (str) ResponseName
         Returns the response name   
            
         
        """
        pass
    
    ##  Set the selected application object 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="appObject"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def SetSelectedAppObject(self, appObject: NXOpen.TaggedObject) -> None:
        """
         Set the selected application object 
        """
        pass
    
    ##  Set the selected application owner object and lookup key 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="appOwnerObject"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    ## <param name="appLookupKey"> (str) </param>
    def SetSelectedAppOwnerObjectAndLookupKey(self, appOwnerObject: NXOpen.TaggedObject, appLookupKey: str) -> None:
        """
         Set the selected application owner object and lookup key 
        """
        pass
    
import NXOpen
##  Represents a @link DSE::DesignResponse DSE::DesignResponse@endlink  class object. <br> To create or edit an instance of this class, use @link NXOpen::DSE::DesignResponseBuilder  NXOpen::DSE::DesignResponseBuilder @endlink  <br> 
## 
##   <br>  Created in NX2406.0.0  <br> 

class DesignResponse(NXOpen.NXObject): 
    """ Represents a <ja_class>DSE.DesignResponse</ja_class> class object."""
    pass


import NXOpen
## 
##     Builds a @link NXOpen::DSE::DesignSet NXOpen::DSE::DesignSet@endlink  object which
##     serves to solve a set of designs without optimization.
##      <br> To create a new instance of this class, use @link NXOpen::DSE::StudyManager::CreateDesignSetBuilder  NXOpen::DSE::StudyManager::CreateDesignSetBuilder @endlink  <br> 
## 
##   <br>  Created in NX2406.0.0  <br> 

class DesignSetBuilder(NXOpen.Builder): 
    """
    Builds a <ja_class>NXOpen.DSE.DesignSet</ja_class> object which
    serves to solve a set of designs without optimization.
    """


    ## Getter for property: (str) ErrorMessage
    ##  Returns the design set name.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return str
    @property
    def ErrorMessage(self) -> str:
        """
        Getter for property: (str) ErrorMessage
         Returns the design set name.  
             
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the design set name.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the design set name.  
             
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the design set name.  
    ##      
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the design set name.  
             
         
        """
        pass
    
    ##  Add a design. 
    ##  @return index (int):  The index of the design that was added .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="designName"> (str)  The new unique name of the design to add </param>
    def AddDesign(self, designName: str) -> int:
        """
         Add a design. 
         @return index (int):  The index of the design that was added .
        """
        pass
    
    ##  Removes all designs except for the baseline design. 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    def ClearDesigns(self) -> None:
        """
         Removes all designs except for the baseline design. 
        """
        pass
    
    ##  Adds all design variable of the active study. 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    def PopulateDesignVariables(self) -> None:
        """
         Adds all design variable of the active study. 
        """
        pass
    
    ##  Adds all design variable of the active study. 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    def PopulateOutputParameters(self) -> None:
        """
         Adds all design variable of the active study. 
        """
        pass
    
    ##  Remove a design. 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="designName"> (str)  The name of the design to remove </param>
    def RemoveDesign(self, designName: str) -> None:
        """
         Remove a design. 
        """
        pass
    
    ##  Remove a design constraint. 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="var"> (@link DesignConstraint NXOpen.DSE.DesignConstraint@endlink)  The design constraint to remove </param>
    def RemoveDesignConstraint(self, var: DesignConstraint) -> None:
        """
         Remove a design constraint. 
        """
        pass
    
    ##  Remove a design objective. 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="var"> (@link DesignObjective NXOpen.DSE.DesignObjective@endlink)  The design objective to remove </param>
    def RemoveDesignObjective(self, var: DesignObjective) -> None:
        """
         Remove a design objective. 
        """
        pass
    
    ##  Remove a design response. 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="var"> (@link DesignResponse NXOpen.DSE.DesignResponse@endlink)  The design response to remove </param>
    def RemoveDesignResponse(self, var: DesignResponse) -> None:
        """
         Remove a design response. 
        """
        pass
    
    ##  Remove a design variable. 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="var"> (@link DesignVariable NXOpen.DSE.DesignVariable@endlink)  The design variable to remove </param>
    def RemoveDesignVariable(self, var: DesignVariable) -> None:
        """
         Remove a design variable. 
        """
        pass
    
    ##  Set the comment on the design. 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="index"> (int)  The index of the design to update </param>
    ## <param name="comment"> (str)  The new comment on the design </param>
    def SetComment(self, index: int, comment: str) -> None:
        """
         Set the comment on the design. 
        """
        pass
    
    ##  Set the fixed value of the design for the given design constraint. 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="index"> (int)  The index of the constraint to update </param>
    ## <param name="constraint"> (@link DesignConstraint NXOpen.DSE.DesignConstraint@endlink)  The design constraint whose value to fix </param>
    ## <param name="value"> (str)  The new value of the design </param>
    def SetDesignConstraintValue(self, index: int, constraint: DesignConstraint, value: str) -> None:
        """
         Set the fixed value of the design for the given design constraint. 
        """
        pass
    
    ##  Set the name of the design. 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="index"> (int)  The index of the design to update </param>
    ## <param name="name"> (str)  The new unique name of the design </param>
    def SetDesignName(self, index: int, name: str) -> None:
        """
         Set the name of the design. 
        """
        pass
    
    ##  Set the fixed value of the design for the given design objective. 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="index"> (int)  The index of the objective to update </param>
    ## <param name="objective"> (@link DesignObjective NXOpen.DSE.DesignObjective@endlink)  The design objective whose value to fix </param>
    ## <param name="value"> (str)  The new value of the design </param>
    def SetDesignObjectiveValue(self, index: int, objective: DesignObjective, value: str) -> None:
        """
         Set the fixed value of the design for the given design objective. 
        """
        pass
    
    ##  Set the fixed value of the design for the given design response. 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="index"> (int)  The index of the response to update </param>
    ## <param name="response"> (@link DesignResponse NXOpen.DSE.DesignResponse@endlink)  The design response whose value to fix </param>
    ## <param name="value"> (str)  The new value of the design </param>
    def SetDesignResponseValue(self, index: int, response: DesignResponse, value: str) -> None:
        """
         Set the fixed value of the design for the given design response. 
        """
        pass
    
    ##  Set the value of the design for the given design_variable. 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="index"> (int)  The index of the design to update </param>
    ## <param name="var"> (@link DesignVariable NXOpen.DSE.DesignVariable@endlink)  The design_variable whose design value to update </param>
    ## <param name="value"> (str)  The new value of the design </param>
    def SetDesignValue(self, index: int, var: DesignVariable, value: str) -> None:
        """
         Set the value of the design for the given design_variable. 
        """
        pass
    
    ##  Set if a design is going to be applied during solve. 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="index"> (int)  The index of the design to add or remove from solve </param>
    ## <param name="isDesignForSolve"> (bool)  weather the design is to be applied during solve or not </param>
    def SetIsDesignForSolve(self, index: int, isDesignForSolve: bool) -> None:
        """
         Set if a design is going to be applied during solve. 
        """
        pass
    
    ##  Set if the output parameters should be displayed in the design set. 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="showOutputParameters"> (bool)  weather the output parameters should be displayed in the design set </param>
    def SetShowOutputParameters(self, showOutputParameters: bool) -> None:
        """
         Set if the output parameters should be displayed in the design set. 
        """
        pass
    
import NXOpen
##  Represents a @link DSE::DesignSet DSE::DesignSet@endlink  object. <br> To create or edit an instance of this class, use @link NXOpen::DSE::DesignSetBuilder  NXOpen::DSE::DesignSetBuilder @endlink  <br> 
## 
##   <br>  Created in NX2406.0.0  <br> 

class DesignSet(NXOpen.NXObject): 
    """ Represents a <ja_class>DSE.DesignSet</ja_class> object."""


    ##  Renames the design set 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="name"> (str)  design set name </param>
    def Rename(self, name: str) -> None:
        """
         Renames the design set 
        """
        pass
    
import NXOpen
##  Represents Design Variable Builder class. <br> To create a new instance of this class, use @link NXOpen::DSE::StudyManager::CreateDesignVariableBuilder  NXOpen::DSE::StudyManager::CreateDesignVariableBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class DesignVariableBuilder(NXOpen.Builder): 
    """ Represents Design Variable Builder class."""


    ##  Represents Continuous and Discrete varibale enum type.
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Continuous</term><description> 
    ## </description> </item><item><term> 
    ## Discrete</term><description> 
    ## </description> </item></list>
    class EnumType(Enum):
        """
        Members Include: <Continuous> <Discrete>
        """
        Continuous: int
        Discrete: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DesignVariableBuilder.EnumType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) VariableName
    ##  Returns the variable name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return str
    @property
    def VariableName(self) -> str:
        """
        Getter for property: (str) VariableName
         Returns the variable name   
            
         
        """
        pass
    
    ## Setter for property: (str) VariableName

    ##  Returns the variable name   
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @VariableName.setter
    def VariableName(self, variableName: str):
        """
        Setter for property: (str) VariableName
         Returns the variable name   
            
         
        """
        pass
    
    ## Getter for property: (@link DesignVariableBuilder.EnumType NXOpen.DSE.DesignVariableBuilder.EnumType@endlink) VariableType
    ##  Returns the variable type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return DesignVariableBuilder.EnumType
    @property
    def VariableType(self) -> DesignVariableBuilder.EnumType:
        """
        Getter for property: (@link DesignVariableBuilder.EnumType NXOpen.DSE.DesignVariableBuilder.EnumType@endlink) VariableType
         Returns the variable type   
            
         
        """
        pass
    
    ## Setter for property: (@link DesignVariableBuilder.EnumType NXOpen.DSE.DesignVariableBuilder.EnumType@endlink) VariableType

    ##  Returns the variable type   
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @VariableType.setter
    def VariableType(self, variableType: DesignVariableBuilder.EnumType):
        """
        Setter for property: (@link DesignVariableBuilder.EnumType NXOpen.DSE.DesignVariableBuilder.EnumType@endlink) VariableType
         Returns the variable type   
            
         
        """
        pass
    
    ##  Get continuous design variable builder 
    ##  @return cdvBuilder (@link ContinuousDesignVariableBuilder NXOpen.DSE.ContinuousDesignVariableBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    def GetContinuousDesignVariableBuilder(self) -> ContinuousDesignVariableBuilder:
        """
         Get continuous design variable builder 
         @return cdvBuilder (@link ContinuousDesignVariableBuilder NXOpen.DSE.ContinuousDesignVariableBuilder@endlink): .
        """
        pass
    
    ##  Get discrete design variable builder 
    ##  @return ddvBuilder (@link DiscreteDesignVariableBuilder NXOpen.DSE.DiscreteDesignVariableBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    def GetDiscreteDesignVariableBuilder(self) -> DiscreteDesignVariableBuilder:
        """
         Get discrete design variable builder 
         @return ddvBuilder (@link DiscreteDesignVariableBuilder NXOpen.DSE.DiscreteDesignVariableBuilder@endlink): .
        """
        pass
    
    ##  Set the selected application object 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="appObject"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def SetSelectedAppObject(self, appObject: NXOpen.TaggedObject) -> None:
        """
         Set the selected application object 
        """
        pass
    
    ##  Set the selected application owner object and lookup key 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="appOwnerObject"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    ## <param name="appLookupKey"> (str) </param>
    def SetSelectedAppOwnerObjectAndLookupKey(self, appOwnerObject: NXOpen.TaggedObject, appLookupKey: str) -> None:
        """
         Set the selected application owner object and lookup key 
        """
        pass
    
import NXOpen
##  Represents a @link DSE::DesignVariable DSE::DesignVariable@endlink  class object. <br> To create or edit an instance of this class, use @link NXOpen::DSE::DesignVariableBuilder  NXOpen::DSE::DesignVariableBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class DesignVariable(NXOpen.NXObject): 
    """ Represents a <ja_class>DSE.DesignVariable</ja_class> class object."""
    pass


import NXOpen
##  Represents a @link DSE::Design DSE::Design@endlink  object. <br> This object cannot be created  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class Design(NXOpen.TaggedObject): 
    """ Represents a <ja_class>DSE.Design</ja_class> object."""
    pass


import NXOpen
import NXOpen.DSEPlatform
##  Represents Discrete Design Variable Builder class. <br> To create a new instance of this class, use @link NXOpen::DSE::DesignVariableBuilder::GetDiscreteDesignVariableBuilder  NXOpen::DSE::DesignVariableBuilder::GetDiscreteDesignVariableBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class DiscreteDesignVariableBuilder(NXOpen.Builder): 
    """ Represents Discrete Design Variable Builder class."""


    ## Getter for property: (@link DiscreteVariableValueBuilderList NXOpen.DSE.DiscreteVariableValueBuilderList@endlink) ValuesSet
    ##  Returns the values set   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return DiscreteVariableValueBuilderList
    @property
    def ValuesSet(self) -> DiscreteVariableValueBuilderList:
        """
        Getter for property: (@link DiscreteVariableValueBuilderList NXOpen.DSE.DiscreteVariableValueBuilderList@endlink) ValuesSet
         Returns the values set   
            
         
        """
        pass
    
    ##  Set the object 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="validObjValue"> (@link NXOpen.DSEPlatform.ValidObjectValue NXOpen.DSEPlatform.ValidObjectValue@endlink) </param>
    def AddValuesToSet(self, validObjValue: NXOpen.DSEPlatform.ValidObjectValue) -> None:
        """
         Set the object 
        """
        pass
    
    ##  Get valid values for currently selected application object 
    ##  @return validObjValues (@link NXOpen.DSEPlatform.ValidObjectValue List[NXOpen.DSEPlatform.ValidObjectValue]@endlink): The array of valid values.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    def GetValidValuesForSelectedObject(self) -> List[NXOpen.DSEPlatform.ValidObjectValue]:
        """
         Get valid values for currently selected application object 
         @return validObjValues (@link NXOpen.DSEPlatform.ValidObjectValue List[NXOpen.DSEPlatform.ValidObjectValue]@endlink): The array of valid values.
        """
        pass
    
    ##  Remove the object 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="validObjValue"> (@link NXOpen.DSEPlatform.ValidObjectValue NXOpen.DSEPlatform.ValidObjectValue@endlink) </param>
    def RemoveValuesFromSet(self, validObjValue: NXOpen.DSEPlatform.ValidObjectValue) -> None:
        """
         Remove the object 
        """
        pass
    
import NXOpen
##  Represents a list of objects. <br> To create a new instance of this class, use @link NXOpen::Part::CreateObjectList  NXOpen::Part::CreateObjectList @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class DiscreteVariableValueBuilderList(NXOpen.TaggedObject): 
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
    ## <param name="object_list"> (@link DiscreteVariableValueBuilderList NXOpen.DSE.DiscreteVariableValueBuilderList@endlink) </param>
    ## <param name="objects"> (@link DiscreteVariableValueBuilder List[NXOpen.DSE.DiscreteVariableValueBuilder]@endlink)  items to append </param>
    @overload
    def Append(self, objects: List[DiscreteVariableValueBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    
    ##  Appends an object to the list
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link DiscreteVariableValueBuilderList NXOpen.DSE.DiscreteVariableValueBuilderList@endlink) </param>
    ## <param name="objectValue"> (@link DiscreteVariableValueBuilder NXOpen.DSE.DiscreteVariableValueBuilder@endlink)  item to append </param>
    @overload
    def Append(self, objectValue: DiscreteVariableValueBuilder) -> None:
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
    ## <param name="object_list"> (@link DiscreteVariableValueBuilderList NXOpen.DSE.DiscreteVariableValueBuilderList@endlink) </param>
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
    ## <param name="object_list"> (@link DiscreteVariableValueBuilderList NXOpen.DSE.DiscreteVariableValueBuilderList@endlink) </param>
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
    ## <param name="object_list"> (@link DiscreteVariableValueBuilderList NXOpen.DSE.DiscreteVariableValueBuilderList@endlink) </param>
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
    ## <param name="object_list"> (@link DiscreteVariableValueBuilderList NXOpen.DSE.DiscreteVariableValueBuilderList@endlink) </param>
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
    ## <param name="object_list"> (@link DiscreteVariableValueBuilderList NXOpen.DSE.DiscreteVariableValueBuilderList@endlink) </param>
    ## <param name="obj"> (@link DiscreteVariableValueBuilder NXOpen.DSE.DiscreteVariableValueBuilder@endlink)  object to be removed from the list </param>
    @overload
    def Erase(self, obj: DiscreteVariableValueBuilder) -> None:
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
    ## <param name="object_list"> (@link DiscreteVariableValueBuilderList NXOpen.DSE.DiscreteVariableValueBuilderList@endlink) </param>
    ## <param name="obj"> (@link DiscreteVariableValueBuilder NXOpen.DSE.DiscreteVariableValueBuilder@endlink)  object to be removed from the list </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the object </param>
    @overload
    def Erase(self, obj: DiscreteVariableValueBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    ## <param name="obj"> (@link DiscreteVariableValueBuilder NXOpen.DSE.DiscreteVariableValueBuilder@endlink)  Object to find index for </param>
    def FindIndex(self, obj: DiscreteVariableValueBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
            *   -1 is returned.
            
         @return index (int):  index of input object, -1 if not on list .
        """
        pass
    
    ##  Returns the object at the input index.  May be NULL.
    ##     
    ##  @return obj (@link DiscreteVariableValueBuilder NXOpen.DSE.DiscreteVariableValueBuilder@endlink):  object found at input index .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  index of object to return </param>
    def FindItem(self, index: int) -> DiscreteVariableValueBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         @return obj (@link DiscreteVariableValueBuilder NXOpen.DSE.DiscreteVariableValueBuilder@endlink):  object found at input index .
        """
        pass
    
    ##  Gets the contents of the entire list 
    ##  @return objects (@link DiscreteVariableValueBuilder List[NXOpen.DSE.DiscreteVariableValueBuilder]@endlink):  The list contents .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetContents(self) -> List[DiscreteVariableValueBuilder]:
        """
         Gets the contents of the entire list 
         @return objects (@link DiscreteVariableValueBuilder List[NXOpen.DSE.DiscreteVariableValueBuilder]@endlink):  The list contents .
        """
        pass
    
    ##  Inserts an object at the specified location 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="location"> (int)  location at which to insert the object </param>
    ## <param name="objectValue"> (@link DiscreteVariableValueBuilder NXOpen.DSE.DiscreteVariableValueBuilder@endlink)  object to be inserted </param>
    def Insert(self, location: int, objectValue: DiscreteVariableValueBuilder) -> None:
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
    ## <param name="objects"> (@link DiscreteVariableValueBuilder List[NXOpen.DSE.DiscreteVariableValueBuilder]@endlink)  The list contents </param>
    def SetContents(self, objects: List[DiscreteVariableValueBuilder]) -> None:
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
    ## <param name="object_list"> (@link DiscreteVariableValueBuilderList NXOpen.DSE.DiscreteVariableValueBuilderList@endlink) </param>
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
    ## <param name="object_list"> (@link DiscreteVariableValueBuilderList NXOpen.DSE.DiscreteVariableValueBuilderList@endlink) </param>
    ## <param name="object1"> (@link DiscreteVariableValueBuilder NXOpen.DSE.DiscreteVariableValueBuilder@endlink)  first item </param>
    ## <param name="object2"> (@link DiscreteVariableValueBuilder NXOpen.DSE.DiscreteVariableValueBuilder@endlink)  second item </param>
    @overload
    def Swap(self, object1: DiscreteVariableValueBuilder, object2: DiscreteVariableValueBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
import NXOpen
##  Represents Discrete Design Variable Value Builder class. <br> To create a new instance of this class, use @link NXOpen::DSE::StudyManager::CreateDiscreteVariableValueBuilder  NXOpen::DSE::StudyManager::CreateDiscreteVariableValueBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class DiscreteVariableValueBuilder(NXOpen.Builder): 
    """ Represents Discrete Design Variable Value Builder class."""


    ## Getter for property: (float) DoubleValue
    ##  Returns the double   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2212.0.0.  Use @link DSE::DiscreteVariableValueBuilder::DoubleValueExpression DSE::DiscreteVariableValueBuilder::DoubleValueExpression@endlink  instead.  <br> 

    ## @return float
    @property
    def DoubleValue(self) -> float:
        """
        Getter for property: (float) DoubleValue
         Returns the double   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleValue

    ##  Returns the double   
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2212.0.0.  Use @link DSE::DiscreteVariableValueBuilder::DoubleValueExpression DSE::DiscreteVariableValueBuilder::DoubleValueExpression@endlink  instead.  <br> 

    @DoubleValue.setter
    def DoubleValue(self, doubleValue: float):
        """
        Setter for property: (float) DoubleValue
         Returns the double   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DoubleValueExpression
    ##  Returns the double value expression  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DoubleValueExpression(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DoubleValueExpression
         Returns the double value expression  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) IntValueExpression
    ##  Returns the int value expression   
    ##     
    ##  
    ## Getter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def IntValueExpression(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) IntValueExpression
         Returns the int value expression   
            
         
        """
        pass
    
import NXOpen
##  Represents Optimization Study builder. <br> To create a new instance of this class, use @link NXOpen::DSE::StudyManager::CreateOptimizationStudyBuilder  NXOpen::DSE::StudyManager::CreateOptimizationStudyBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class OptimizationStudyBuilder(NXOpen.Builder): 
    """ Represents Optimization Study builder."""


    ## Getter for property: (str) IterationRootString
    ##  Returns the iteration root string for naming iteration parts of Study  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return str
    @property
    def IterationRootString(self) -> str:
        """
        Getter for property: (str) IterationRootString
         Returns the iteration root string for naming iteration parts of Study  
            
         
        """
        pass
    
    ## Setter for property: (str) IterationRootString

    ##  Returns the iteration root string for naming iteration parts of Study  
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @IterationRootString.setter
    def IterationRootString(self, iterationRootString: str):
        """
        Setter for property: (str) IterationRootString
         Returns the iteration root string for naming iteration parts of Study  
            
         
        """
        pass
    
    ## Getter for property: (str) ResultStoragePath
    ##  Returns the folder location to save parts   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return str
    @property
    def ResultStoragePath(self) -> str:
        """
        Getter for property: (str) ResultStoragePath
         Returns the folder location to save parts   
            
         
        """
        pass
    
    ## Setter for property: (str) ResultStoragePath

    ##  Returns the folder location to save parts   
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ResultStoragePath.setter
    def ResultStoragePath(self, foldername: str):
        """
        Setter for property: (str) ResultStoragePath
         Returns the folder location to save parts   
            
         
        """
        pass
    
    ## Getter for property: (str) StudyName
    ##  Returns the name of Study  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return str
    @property
    def StudyName(self) -> str:
        """
        Getter for property: (str) StudyName
         Returns the name of Study  
            
         
        """
        pass
    
    ## Setter for property: (str) StudyName

    ##  Returns the name of Study  
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @StudyName.setter
    def StudyName(self, name: str):
        """
        Setter for property: (str) StudyName
         Returns the name of Study  
            
         
        """
        pass
    
import NXOpen.DSEPlatform
##  Represents a @link DSE::OptimizationStudy DSE::OptimizationStudy@endlink  object. <br> To create or edit an instance of this class, use @link NXOpen::DSE::OptimizationStudyBuilder  NXOpen::DSE::OptimizationStudyBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class OptimizationStudy(NXOpen.DSEPlatform.ExplorationStudy): 
    """ Represents a <ja_class>DSE.OptimizationStudy</ja_class> object."""


    ##  Defines how to treat the baseline design 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Neutral</term><description> 
    ## </description> </item><item><term> 
    ## Ignore</term><description> 
    ## </description> </item><item><term> 
    ## Important</term><description> 
    ## </description> </item></list>
    class BaselineDesignOption(Enum):
        """
        Members Include: <Neutral> <Ignore> <Important>
        """
        Neutral: int
        Ignore: int
        Important: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OptimizationStudy.BaselineDesignOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents different design table usage options 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## DeleteExistingandCreateNew</term><description> 
    ## </description> </item><item><term> 
    ## UseExisting</term><description> 
    ## </description> </item></list>
    class DesignTableOption(Enum):
        """
        Members Include: <DeleteExistingandCreateNew> <UseExisting>
        """
        DeleteExistingandCreateNew: int
        UseExisting: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OptimizationStudy.DesignTableOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents different result storage options.
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Best</term><description> 
    ## </description> </item><item><term> 
    ## FirstFeasible</term><description> 
    ## </description> </item><item><term> 
    ## AllFeasible</term><description> 
    ## </description> </item><item><term> 
    ## All</term><description> 
    ## </description> </item><item><term> 
    ## NotSet</term><description> 
    ## </description> </item></list>
    class ResultStorageOption(Enum):
        """
        Members Include: <Best> <FirstFeasible> <AllFeasible> <All> <NotSet>
        """
        Best: int
        FirstFeasible: int
        AllFeasible: int
        All: int
        NotSet: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OptimizationStudy.ResultStorageOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines type for the run 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Optimization</term><description> 
    ## </description> </item><item><term> 
    ## EvaluateOnly</term><description> 
    ## </description> </item></list>
    class RunType(Enum):
        """
        Members Include: <Optimization> <EvaluateOnly>
        """
        Optimization: int
        EvaluateOnly: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OptimizationStudy.RunType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines type for the sherpa method 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## WeightedSumOfAllObjectives</term><description> 
    ## </description> </item><item><term> 
    ## TradeOffStudy</term><description> 
    ## </description> </item></list>
    class SherpaMethodOption(Enum):
        """
        Members Include: <WeightedSumOfAllObjectives> <TradeOffStudy>
        """
        WeightedSumOfAllObjectives: int
        TradeOffStudy: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OptimizationStudy.SherpaMethodOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Set design constraint on optimization study
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="desConstraint"> (@link DesignConstraint NXOpen.DSE.DesignConstraint@endlink) </param>
    def AddDesignConstraint(self, desConstraint: DesignConstraint) -> None:
        """
         Set design constraint on optimization study
        """
        pass
    
    ##  Set design objective on optimization study
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="dvObj"> (@link DesignObjective NXOpen.DSE.DesignObjective@endlink) </param>
    def AddDesignObjective(self, dvObj: DesignObjective) -> None:
        """
         Set design objective on optimization study
        """
        pass
    
    ##  Set design response on optimization study
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="desResponse"> (@link DesignResponse NXOpen.DSE.DesignResponse@endlink) </param>
    def AddDesignResponse(self, desResponse: DesignResponse) -> None:
        """
         Set design response on optimization study
        """
        pass
    
    ##  Set design set on optimization study
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="desSet"> (@link DesignSet NXOpen.DSE.DesignSet@endlink) </param>
    def AddDesignSet(self, desSet: DesignSet) -> None:
        """
         Set design set on optimization study
        """
        pass
    
    ##  Set design variable on optimization study
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="dvObj"> (@link DesignVariable NXOpen.DSE.DesignVariable@endlink) </param>
    def AddDesignVariable(self, dvObj: DesignVariable) -> None:
        """
         Set design variable on optimization study
        """
        pass
    
    ##  Set design workflow on optimization study
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="workflow"> (@link NXOpen.DSEPlatform.OptimizationWorkflow NXOpen.DSEPlatform.OptimizationWorkflow@endlink) </param>
    def AddWorkflow(self, workflow: NXOpen.DSEPlatform.OptimizationWorkflow) -> None:
        """
         Set design workflow on optimization study
        """
        pass
    
    ##  Apply the given design
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="design"> (@link Design NXOpen.DSE.Design@endlink) </param>
    def ApplyDesign(self, design: Design) -> None:
        """
         Apply the given design
        """
        pass
    
    ##  Deletes the design constraint
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="desConstraint"> (@link DesignConstraint NXOpen.DSE.DesignConstraint@endlink) </param>
    def DeleteDesignConstraint(self, desConstraint: DesignConstraint) -> None:
        """
         Deletes the design constraint
        """
        pass
    
    ##  Deletes the design objective
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="dvObj"> (@link DesignObjective NXOpen.DSE.DesignObjective@endlink) </param>
    def DeleteDesignObjective(self, dvObj: DesignObjective) -> None:
        """
         Deletes the design objective
        """
        pass
    
    ##  Deletes the design response
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="desResponse"> (@link DesignResponse NXOpen.DSE.DesignResponse@endlink) </param>
    def DeleteDesignResponse(self, desResponse: DesignResponse) -> None:
        """
         Deletes the design response
        """
        pass
    
    ##  Deletes the design set
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="dvObj"> (@link DesignSet NXOpen.DSE.DesignSet@endlink) </param>
    def DeleteDesignSet(self, dvObj: DesignSet) -> None:
        """
         Deletes the design set
        """
        pass
    
    ##  Deletes the design variable
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="dvObj"> (@link DesignVariable NXOpen.DSE.DesignVariable@endlink) </param>
    def DeleteDesignVariable(self, dvObj: DesignVariable) -> None:
        """
         Deletes the design variable
        """
        pass
    
    ##  Deletes the study result
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="runResultObj"> (@link RunResult NXOpen.DSE.RunResult@endlink) </param>
    def DeleteResult(self, runResultObj: RunResult) -> None:
        """
         Deletes the study result
        """
        pass
    
    ##  Deletes the optimization study
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    def DeleteStudy(self) -> None:
        """
         Deletes the optimization study
        """
        pass
    
    ##  Delete Study Results 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    def DeleteStudyResults(self) -> None:
        """
         Delete Study Results 
        """
        pass
    
    ##  Deletes the optimization workflow
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="workflow"> (@link NXOpen.DSEPlatform.OptimizationWorkflow NXOpen.DSEPlatform.OptimizationWorkflow@endlink) </param>
    def DeleteWorkflow(self, workflow: NXOpen.DSEPlatform.OptimizationWorkflow) -> None:
        """
         Deletes the optimization workflow
        """
        pass
    
    ##  Get Archive Size 
    ##  @return archiveSize (int): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    def GetArchiveSize(self) -> int:
        """
         Get Archive Size 
         @return archiveSize (int): .
        """
        pass
    
    ##  Get the baseline design option
    ##  @return baselineDesignOption (@link OptimizationStudy.BaselineDesignOption NXOpen.DSE.OptimizationStudy.BaselineDesignOption@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    def GetBaselineDesignOption(self) -> OptimizationStudy.BaselineDesignOption:
        """
         Get the baseline design option
         @return baselineDesignOption (@link OptimizationStudy.BaselineDesignOption NXOpen.DSE.OptimizationStudy.BaselineDesignOption@endlink): .
        """
        pass
    
    ##  Get the design constraint at index from the study
    ##  @return desConstraint (@link DesignConstraint NXOpen.DSE.DesignConstraint@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int) </param>
    def GetDesignConstraintAtIndex(self, index: int) -> DesignConstraint:
        """
         Get the design constraint at index from the study
         @return desConstraint (@link DesignConstraint NXOpen.DSE.DesignConstraint@endlink): .
        """
        pass
    
    ##  Get the design objective at index from the study
    ##  @return dvObj (@link DesignObjective NXOpen.DSE.DesignObjective@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int) </param>
    def GetDesignObjectiveAtIndex(self, index: int) -> DesignObjective:
        """
         Get the design objective at index from the study
         @return dvObj (@link DesignObjective NXOpen.DSE.DesignObjective@endlink): .
        """
        pass
    
    ##  Get the design response at index from the study
    ##  @return desResponse (@link DesignResponse NXOpen.DSE.DesignResponse@endlink): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int) </param>
    def GetDesignResponseAtIndex(self, index: int) -> DesignResponse:
        """
         Get the design response at index from the study
         @return desResponse (@link DesignResponse NXOpen.DSE.DesignResponse@endlink): .
        """
        pass
    
    ##  Get the design set at index from the study
    ##  @return desSet (@link DesignSet NXOpen.DSE.DesignSet@endlink): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int) </param>
    def GetDesignSetAtIndex(self, index: int) -> DesignSet:
        """
         Get the design set at index from the study
         @return desSet (@link DesignSet NXOpen.DSE.DesignSet@endlink): .
        """
        pass
    
    ##  Get design table option
    ##  @return designTableOption (@link OptimizationStudy.DesignTableOption NXOpen.DSE.OptimizationStudy.DesignTableOption@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    def GetDesignTableOption(self) -> OptimizationStudy.DesignTableOption:
        """
         Get design table option
         @return designTableOption (@link OptimizationStudy.DesignTableOption NXOpen.DSE.OptimizationStudy.DesignTableOption@endlink): .
        """
        pass
    
    ##  Get the design variable at index from the study
    ##  @return dvObj (@link DesignVariable NXOpen.DSE.DesignVariable@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int) </param>
    def GetDesignVariableAtIndex(self, index: int) -> DesignVariable:
        """
         Get the design variable at index from the study
         @return dvObj (@link DesignVariable NXOpen.DSE.DesignVariable@endlink): .
        """
        pass
    
    ##  Get property to update display 
    ##  @return shouldUpdateDisp (bool): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    def GetDoDisplayUpdate(self) -> bool:
        """
         Get property to update display 
         @return shouldUpdateDisp (bool): .
        """
        pass
    
    ##  Get iteration 
    ##  @return iterations (int): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    def GetIteration(self) -> int:
        """
         Get iteration 
         @return iterations (int): .
        """
        pass
    
    ##  Get latest run result
    ##  @return runResult (@link RunResult NXOpen.DSE.RunResult@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    def GetLatestRunResult(self) -> RunResult:
        """
         Get latest run result
         @return runResult (@link RunResult NXOpen.DSE.RunResult@endlink): .
        """
        pass
    
    ##  Get the number of design constraints in the study
    ##  @return numConstraints (int): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    def GetNumberOfDesignConstraints(self) -> int:
        """
         Get the number of design constraints in the study
         @return numConstraints (int): .
        """
        pass
    
    ##  Get the number of design objective in the study
    ##  @return numVar (int): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    def GetNumberOfDesignObjectives(self) -> int:
        """
         Get the number of design objective in the study
         @return numVar (int): .
        """
        pass
    
    ##  Get the number of design responses in the study
    ##  @return numResponses (int): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    def GetNumberOfDesignResponses(self) -> int:
        """
         Get the number of design responses in the study
         @return numResponses (int): .
        """
        pass
    
    ##  Get the number of design sets in the study
    ##  @return numSets (int): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    def GetNumberOfDesignSets(self) -> int:
        """
         Get the number of design sets in the study
         @return numSets (int): .
        """
        pass
    
    ##  Get the number of design variable in the study
    ##  @return numVar (int): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    def GetNumberOfDesignVariables(self) -> int:
        """
         Get the number of design variable in the study
         @return numVar (int): .
        """
        pass
    
    ##  Get the number of run results in the study
    ##  @return numRunResult (int): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    def GetNumberOfRunResults(self) -> int:
        """
         Get the number of run results in the study
         @return numRunResult (int): .
        """
        pass
    
    ##  Get the number of workflows in the study
    ##  @return numWorkflow (int): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    def GetNumberOfWorkflows(self) -> int:
        """
         Get the number of workflows in the study
         @return numWorkflow (int): .
        """
        pass
    
    ##  Get the random seed 
    ##  @return randomSeed (float): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    def GetRandomSeed(self) -> float:
        """
         Get the random seed 
         @return randomSeed (float): .
        """
        pass
    
    ##  Get save option
    ##  @return resultStorageOption (@link OptimizationStudy.ResultStorageOption NXOpen.DSE.OptimizationStudy.ResultStorageOption@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    def GetResultStorageOption(self) -> OptimizationStudy.ResultStorageOption:
        """
         Get save option
         @return resultStorageOption (@link OptimizationStudy.ResultStorageOption NXOpen.DSE.OptimizationStudy.ResultStorageOption@endlink): .
        """
        pass
    
    ##  Get the run result at index from the study
    ##  @return runResultObj (@link RunResult NXOpen.DSE.RunResult@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int) </param>
    def GetRunResultAtIndex(self, index: int) -> RunResult:
        """
         Get the run result at index from the study
         @return runResultObj (@link RunResult NXOpen.DSE.RunResult@endlink): .
        """
        pass
    
    ##  Get the run result from the study when name is given
    ##  @return runResultObj (@link RunResult NXOpen.DSE.RunResult@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="designTableName"> (str) </param>
    def GetRunResultWithName(self, designTableName: str) -> RunResult:
        """
         Get the run result from the study when name is given
         @return runResultObj (@link RunResult NXOpen.DSE.RunResult@endlink): .
        """
        pass
    
    ##  Get run type
    ##  @return runType (@link OptimizationStudy.RunType NXOpen.DSE.OptimizationStudy.RunType@endlink): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    def GetRunType(self) -> OptimizationStudy.RunType:
        """
         Get run type
         @return runType (@link OptimizationStudy.RunType NXOpen.DSE.OptimizationStudy.RunType@endlink): .
        """
        pass
    
    ##  Get Sherpa Method Option
    ##  @return sherpaMethodOption (@link OptimizationStudy.SherpaMethodOption NXOpen.DSE.OptimizationStudy.SherpaMethodOption@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    def GetSherpaMethodOption(self) -> OptimizationStudy.SherpaMethodOption:
        """
         Get Sherpa Method Option
         @return sherpaMethodOption (@link OptimizationStudy.SherpaMethodOption NXOpen.DSE.OptimizationStudy.SherpaMethodOption@endlink): .
        """
        pass
    
    ##  Get the workflow at index from the study
    ##  @return wfObj (@link NXOpen.DSEPlatform.OptimizationWorkflow NXOpen.DSEPlatform.OptimizationWorkflow@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int) </param>
    def GetWorkflowAtIndex(self, index: int) -> NXOpen.DSEPlatform.OptimizationWorkflow:
        """
         Get the workflow at index from the study
         @return wfObj (@link NXOpen.DSEPlatform.OptimizationWorkflow NXOpen.DSEPlatform.OptimizationWorkflow@endlink): .
        """
        pass
    
    ##  Run the evalaute only study 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="designSetsToSolve"> (@link DesignSet List[NXOpen.DSE.DesignSet]@endlink) </param>
    def RunEvaluateOnly(self, designSetsToSolve: List[DesignSet]) -> None:
        """
         Run the evalaute only study 
        """
        pass
    
    ##  Run the optimization study 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_design_explorer (" NX Design Space Exploration")
    def RunStudy(self) -> None:
        """
         Run the optimization study 
        """
        pass
    
    ##  Set Archive Size 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="iterations"> (int) </param>
    def SetArchiveSize(self, iterations: int) -> None:
        """
         Set Archive Size 
        """
        pass
    
    ##  Set the baseline design option
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="baselineDesignOption"> (@link OptimizationStudy.BaselineDesignOption NXOpen.DSE.OptimizationStudy.BaselineDesignOption@endlink) </param>
    def SetBaselineDesignOption(self, baselineDesignOption: OptimizationStudy.BaselineDesignOption) -> None:
        """
         Set the baseline design option
        """
        pass
    
    ##  Set design table option
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="designTableOption"> (@link OptimizationStudy.DesignTableOption NXOpen.DSE.OptimizationStudy.DesignTableOption@endlink) </param>
    def SetDesignTableOption(self, designTableOption: OptimizationStudy.DesignTableOption) -> None:
        """
         Set design table option
        """
        pass
    
    ##  Set property to update display 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="shouldUpdateDisp"> (bool) </param>
    def SetDoDisplayUpdate(self, shouldUpdateDisp: bool) -> None:
        """
         Set property to update display 
        """
        pass
    
    ##  Set iteration 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="iterations"> (int) </param>
    def SetIteration(self, iterations: int) -> None:
        """
         Set iteration 
        """
        pass
    
    ##  Set the new run name, this name is cleared after subseqent call to RunStudy
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="newRunName"> (str) </param>
    def SetNewRunName(self, newRunName: str) -> None:
        """
         Set the new run name, this name is cleared after subseqent call to RunStudy
        """
        pass
    
    ##  Set the random seed 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="randomSeed"> (float) </param>
    def SetRandomSeed(self, randomSeed: float) -> None:
        """
         Set the random seed 
        """
        pass
    
    ##  Set save option
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="resultStorageOption"> (@link OptimizationStudy.ResultStorageOption NXOpen.DSE.OptimizationStudy.ResultStorageOption@endlink) </param>
    def SetResultStorageOption(self, resultStorageOption: OptimizationStudy.ResultStorageOption) -> None:
        """
         Set save option
        """
        pass
    
    ##  Set given run result as Appending Design Table 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="runResultObj"> (@link RunResult NXOpen.DSE.RunResult@endlink) </param>
    def SetRunResultToAppend(self, runResultObj: RunResult) -> None:
        """
         Set given run result as Appending Design Table 
        """
        pass
    
    ##  Set run type
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="runType"> (@link OptimizationStudy.RunType NXOpen.DSE.OptimizationStudy.RunType@endlink) </param>
    def SetRunType(self, runType: OptimizationStudy.RunType) -> None:
        """
         Set run type
        """
        pass
    
    ##  Set Sherpa Method Option
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="sherpaMethodOption"> (@link OptimizationStudy.SherpaMethodOption NXOpen.DSE.OptimizationStudy.SherpaMethodOption@endlink) </param>
    def SetSherpaMethodOption(self, sherpaMethodOption: OptimizationStudy.SherpaMethodOption) -> None:
        """
         Set Sherpa Method Option
        """
        pass
    
import NXOpen
##  Represents Plot2DData class  <br> This class is created by PlotBuilder create method  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class Plot2DData(NXOpen.Builder): 
    """ Represents Plot2DData class """


    ##  Clear parameters 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    def ClearParameters(self) -> None:
        """
         Clear parameters 
        """
        pass
    
    ##  Remove the y parameter column index 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="columnID"> (int) </param>
    def RemoveYParameterColumnIndex(self, columnID: int) -> None:
        """
         Remove the y parameter column index 
        """
        pass
    
    ##  Set the x parameter column index 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="columnID"> (int) </param>
    def SetXParameterColumnIndex(self, columnID: int) -> None:
        """
         Set the x parameter column index 
        """
        pass
    
    ##  Set the y parameter column index 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="columnID"> (int) </param>
    def SetYParameterColumnIndex(self, columnID: int) -> None:
        """
         Set the y parameter column index 
        """
        pass
    
##  Represents a @link DSE::Plot2D DSE::Plot2D@endlink  object. <br> This object cannot be created  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class Plot2D(Plot): 
    """ Represents a <ja_class>DSE.Plot2D</ja_class> object."""
    pass


import NXOpen
##  Represents Plot3DData class  <br> This class is created by PlotBuilder create method  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class Plot3DData(NXOpen.Builder): 
    """ Represents Plot3DData class """


    ##  Clear parameters 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    def ClearParameters(self) -> None:
        """
         Clear parameters 
        """
        pass
    
    ##  Remove the z parameter column index 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="columnID"> (int) </param>
    def RemoveZParameterColumnIndex(self, columnID: int) -> None:
        """
         Remove the z parameter column index 
        """
        pass
    
    ##  Set the x parameter column index 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="columnID"> (int) </param>
    def SetXParameterColumnIndex(self, columnID: int) -> None:
        """
         Set the x parameter column index 
        """
        pass
    
    ##  Set the y parameter column index 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="columnID"> (int) </param>
    def SetYParameterColumnIndex(self, columnID: int) -> None:
        """
         Set the y parameter column index 
        """
        pass
    
    ##  Set the z parameter column index 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="columnID"> (int) </param>
    def SetZParameterColumnIndex(self, columnID: int) -> None:
        """
         Set the z parameter column index 
        """
        pass
    
##  Represents a @link DSE::Plot3D DSE::Plot3D@endlink  object. <br> This object cannot be created  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class Plot3D(Plot): 
    """ Represents a <ja_class>DSE.Plot3D</ja_class> object."""
    pass


import NXOpen
##  Represents Plot Builder class  <br> To create a new instance of this class, use @link NXOpen::DSE::StudyManager::CreatePlotBuilder  NXOpen::DSE::StudyManager::CreatePlotBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class PlotBuilder(NXOpen.Builder): 
    """ Represents Plot Builder class """


    ##  Represents design set option to create plot.
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## All</term><description> 
    ## </description> </item><item><term> 
    ## Feasible</term><description> 
    ## </description> </item><item><term> 
    ## Infeasible</term><description> 
    ## </description> </item><item><term> 
    ## NonError</term><description> 
    ## </description> </item><item><term> 
    ## Best</term><description> 
    ## </description> </item></list>
    class DesignSetType(Enum):
        """
        Members Include: <All> <Feasible> <Infeasible> <NonError> <Best>
        """
        All: int
        Feasible: int
        Infeasible: int
        NonError: int
        Best: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PlotBuilder.DesignSetType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents output plot option to create plot.
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Series</term><description> 
    ## </description> </item><item><term> 
    ## Individually</term><description> 
    ## </description> </item></list>
    class OutputPlotType(Enum):
        """
        Members Include: <Series> <Individually>
        """
        Series: int
        Individually: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PlotBuilder.OutputPlotType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents plot enum type.
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## History</term><description> 
    ## </description> </item><item><term> 
    ## Relation2D</term><description> 
    ## </description> </item><item><term> 
    ## Relation3D</term><description> 
    ## </description> </item><item><term> 
    ## ParetoFront2D</term><description> 
    ## </description> </item><item><term> 
    ## ParetoFront3D</term><description> 
    ## </description> </item><item><term> 
    ## ConstraintViolations</term><description> 
    ## </description> </item></list>
    class PlotOption(Enum):
        """
        Members Include: <History> <Relation2D> <Relation3D> <ParetoFront2D> <ParetoFront3D> <ConstraintViolations>
        """
        History: int
        Relation2D: int
        Relation3D: int
        ParetoFront2D: int
        ParetoFront3D: int
        ConstraintViolations: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PlotBuilder.PlotOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link Plot2DData NXOpen.DSE.Plot2DData@endlink) ConstraintViolationsData
    ##  Returns the constraint violations data  
    ##     
    ##  
    ## Getter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return Plot2DData
    @property
    def ConstraintViolationsData(self) -> Plot2DData:
        """
        Getter for property: (@link Plot2DData NXOpen.DSE.Plot2DData@endlink) ConstraintViolationsData
         Returns the constraint violations data  
            
         
        """
        pass
    
    ## Getter for property: (@link PlotBuilder.DesignSetType NXOpen.DSE.PlotBuilder.DesignSetType@endlink) DesignSetOption
    ##  Returns the design set option   
    ##     
    ##  
    ## Getter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return PlotBuilder.DesignSetType
    @property
    def DesignSetOption(self) -> PlotBuilder.DesignSetType:
        """
        Getter for property: (@link PlotBuilder.DesignSetType NXOpen.DSE.PlotBuilder.DesignSetType@endlink) DesignSetOption
         Returns the design set option   
            
         
        """
        pass
    
    ## Setter for property: (@link PlotBuilder.DesignSetType NXOpen.DSE.PlotBuilder.DesignSetType@endlink) DesignSetOption

    ##  Returns the design set option   
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @DesignSetOption.setter
    def DesignSetOption(self, designSetOption: PlotBuilder.DesignSetType):
        """
        Setter for property: (@link PlotBuilder.DesignSetType NXOpen.DSE.PlotBuilder.DesignSetType@endlink) DesignSetOption
         Returns the design set option   
            
         
        """
        pass
    
    ## Getter for property: (bool) HighlightBaselineDesign
    ##  Returns the option to highlight baseline design   
    ##     
    ##  
    ## Getter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def HighlightBaselineDesign(self) -> bool:
        """
        Getter for property: (bool) HighlightBaselineDesign
         Returns the option to highlight baseline design   
            
         
        """
        pass
    
    ## Setter for property: (bool) HighlightBaselineDesign

    ##  Returns the option to highlight baseline design   
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @HighlightBaselineDesign.setter
    def HighlightBaselineDesign(self, highlightBaselineDesign: bool):
        """
        Setter for property: (bool) HighlightBaselineDesign
         Returns the option to highlight baseline design   
            
         
        """
        pass
    
    ## Getter for property: (bool) HighlightBestDesign
    ##  Returns the option to show best design   
    ##     
    ##  
    ## Getter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def HighlightBestDesign(self) -> bool:
        """
        Getter for property: (bool) HighlightBestDesign
         Returns the option to show best design   
            
         
        """
        pass
    
    ## Setter for property: (bool) HighlightBestDesign

    ##  Returns the option to show best design   
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @HighlightBestDesign.setter
    def HighlightBestDesign(self, showBestDesign: bool):
        """
        Setter for property: (bool) HighlightBestDesign
         Returns the option to show best design   
            
         
        """
        pass
    
    ## Getter for property: (@link Plot2DData NXOpen.DSE.Plot2DData@endlink) HistoryData
    ##  Returns the history data  
    ##     
    ##  
    ## Getter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return Plot2DData
    @property
    def HistoryData(self) -> Plot2DData:
        """
        Getter for property: (@link Plot2DData NXOpen.DSE.Plot2DData@endlink) HistoryData
         Returns the history data  
            
         
        """
        pass
    
    ## Getter for property: (@link PlotBuilder.OutputPlotType NXOpen.DSE.PlotBuilder.OutputPlotType@endlink) OutputPlotOption
    ##  Returns the output plot option   
    ##     
    ##  
    ## Getter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return PlotBuilder.OutputPlotType
    @property
    def OutputPlotOption(self) -> PlotBuilder.OutputPlotType:
        """
        Getter for property: (@link PlotBuilder.OutputPlotType NXOpen.DSE.PlotBuilder.OutputPlotType@endlink) OutputPlotOption
         Returns the output plot option   
            
         
        """
        pass
    
    ## Setter for property: (@link PlotBuilder.OutputPlotType NXOpen.DSE.PlotBuilder.OutputPlotType@endlink) OutputPlotOption

    ##  Returns the output plot option   
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @OutputPlotOption.setter
    def OutputPlotOption(self, outputPlotOption: PlotBuilder.OutputPlotType):
        """
        Setter for property: (@link PlotBuilder.OutputPlotType NXOpen.DSE.PlotBuilder.OutputPlotType@endlink) OutputPlotOption
         Returns the output plot option   
            
         
        """
        pass
    
    ## Getter for property: (@link Plot2DData NXOpen.DSE.Plot2DData@endlink) Pareto2DData
    ##  Returns the 2d pareto data  
    ##     
    ##  
    ## Getter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return Plot2DData
    @property
    def Pareto2DData(self) -> Plot2DData:
        """
        Getter for property: (@link Plot2DData NXOpen.DSE.Plot2DData@endlink) Pareto2DData
         Returns the 2d pareto data  
            
         
        """
        pass
    
    ## Getter for property: (@link Plot3DData NXOpen.DSE.Plot3DData@endlink) Pareto3DData
    ##  Returns the 3d pareto data  
    ##     
    ##  
    ## Getter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return Plot3DData
    @property
    def Pareto3DData(self) -> Plot3DData:
        """
        Getter for property: (@link Plot3DData NXOpen.DSE.Plot3DData@endlink) Pareto3DData
         Returns the 3d pareto data  
            
         
        """
        pass
    
    ## Getter for property: (@link Plot2DData NXOpen.DSE.Plot2DData@endlink) Relation2DData
    ##  Returns the 2d relation data  
    ##     
    ##  
    ## Getter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return Plot2DData
    @property
    def Relation2DData(self) -> Plot2DData:
        """
        Getter for property: (@link Plot2DData NXOpen.DSE.Plot2DData@endlink) Relation2DData
         Returns the 2d relation data  
            
         
        """
        pass
    
    ## Getter for property: (@link Plot3DData NXOpen.DSE.Plot3DData@endlink) Relation3DData
    ##  Returns the 3d relation data  
    ##     
    ##  
    ## Getter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return Plot3DData
    @property
    def Relation3DData(self) -> Plot3DData:
        """
        Getter for property: (@link Plot3DData NXOpen.DSE.Plot3DData@endlink) Relation3DData
         Returns the 3d relation data  
            
         
        """
        pass
    
    ## Getter for property: (@link PlotBuilder.PlotOption NXOpen.DSE.PlotBuilder.PlotOption@endlink) Type
    ##  Returns the type   
    ##     
    ##  
    ## Getter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return PlotBuilder.PlotOption
    @property
    def Type(self) -> PlotBuilder.PlotOption:
        """
        Getter for property: (@link PlotBuilder.PlotOption NXOpen.DSE.PlotBuilder.PlotOption@endlink) Type
         Returns the type   
            
         
        """
        pass
    
    ## Setter for property: (@link PlotBuilder.PlotOption NXOpen.DSE.PlotBuilder.PlotOption@endlink) Type

    ##  Returns the type   
    ##     
    ##  
    ## Setter License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Type.setter
    def Type(self, type: PlotBuilder.PlotOption):
        """
        Setter for property: (@link PlotBuilder.PlotOption NXOpen.DSE.PlotBuilder.PlotOption@endlink) Type
         Returns the type   
            
         
        """
        pass
    
    ##  Set the run result in plot builder 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="runResultObj"> (@link RunResult NXOpen.DSE.RunResult@endlink) </param>
    def SetCurrentRunResult(self, runResultObj: RunResult) -> None:
        """
         Set the run result in plot builder 
        """
        pass
    
    ##  Set the plot name prefix 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="plotNamePrefix"> (str) </param>
    def SetPlotNamePrefix(self, plotNamePrefix: str) -> None:
        """
         Set the plot name prefix 
        """
        pass
    
import NXOpen
##  Represents a @link DSE::Plot DSE::Plot@endlink  object. <br> To create or edit an instance of this class, use @link NXOpen::DSE::PlotBuilder  NXOpen::DSE::PlotBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class Plot(NXOpen.NXObject): 
    """ Represents a <ja_class>DSE.Plot</ja_class> object."""
    pass


import NXOpen
##  Represents a @link DSE::RunResult DSE::RunResult@endlink  object. <br> This object cannot be created  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class RunResult(NXOpen.TaggedObject): 
    """ Represents a <ja_class>DSE.RunResult</ja_class> object."""


    ##  Delete the plot from run
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="plotObj"> (@link Plot NXOpen.DSE.Plot@endlink) </param>
    def DeletePlot(self, plotObj: Plot) -> None:
        """
         Delete the plot from run
        """
        pass
    
    ##  Get design by designId
    ##  @return design (@link Design NXOpen.DSE.Design@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="designId"> (int) </param>
    def GetDesignById(self, designId: int) -> Design:
        """
         Get design by designId
         @return design (@link Design NXOpen.DSE.Design@endlink): .
        """
        pass
    
    ##  Get the plot at index from the run result
    ##  @return plotObj (@link Plot NXOpen.DSE.Plot@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="index"> (int) </param>
    def GetPlotAtIndex(self, index: int) -> Plot:
        """
         Get the plot at index from the run result
         @return plotObj (@link Plot NXOpen.DSE.Plot@endlink): .
        """
        pass
    
import NXOpen
##  Represents the Design Space Explorer Study Manager class. <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class StudyManager(NXOpen.Object): 
    """ Represents the Design Space Explorer Study Manager class."""


    ##  Creates a @link DSE::CopyStudyBuilder DSE::CopyStudyBuilder@endlink  
    ##  @return builder (@link CopyStudyBuilder NXOpen.DSE.CopyStudyBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## <param name="part"> (@link NXOpen.BasePart NXOpen.BasePart@endlink) </param>
    ## <param name="sourceStudy"> (@link OptimizationStudy NXOpen.DSE.OptimizationStudy@endlink) </param>
    def CreateCopyStudyBuilder(part: NXOpen.BasePart, sourceStudy: OptimizationStudy) -> CopyStudyBuilder:
        """
         Creates a @link DSE::CopyStudyBuilder DSE::CopyStudyBuilder@endlink  
         @return builder (@link CopyStudyBuilder NXOpen.DSE.CopyStudyBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link DSE::DesignConstraintBuilder DSE::DesignConstraintBuilder@endlink  
    ##  @return builder (@link DesignConstraintBuilder NXOpen.DSE.DesignConstraintBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## <param name="part"> (@link NXOpen.BasePart NXOpen.BasePart@endlink) </param>
    ## <param name="desConstraint"> (@link DesignConstraint NXOpen.DSE.DesignConstraint@endlink) </param>
    def CreateDesignConstraintBuilder(part: NXOpen.BasePart, desConstraint: DesignConstraint) -> DesignConstraintBuilder:
        """
         Creates a @link DSE::DesignConstraintBuilder DSE::DesignConstraintBuilder@endlink  
         @return builder (@link DesignConstraintBuilder NXOpen.DSE.DesignConstraintBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link DSE::DesignObjectiveBuilder DSE::DesignObjectiveBuilder@endlink  
    ##  @return builder (@link DesignObjectiveBuilder NXOpen.DSE.DesignObjectiveBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## <param name="part"> (@link NXOpen.BasePart NXOpen.BasePart@endlink) </param>
    ## <param name="designObjectiveObj"> (@link DesignObjective NXOpen.DSE.DesignObjective@endlink) </param>
    def CreateDesignObjectiveBuilder(part: NXOpen.BasePart, designObjectiveObj: DesignObjective) -> DesignObjectiveBuilder:
        """
         Creates a @link DSE::DesignObjectiveBuilder DSE::DesignObjectiveBuilder@endlink  
         @return builder (@link DesignObjectiveBuilder NXOpen.DSE.DesignObjectiveBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link DSE::DesignResponseBuilder DSE::DesignResponseBuilder@endlink  
    ##  @return builder (@link DesignResponseBuilder NXOpen.DSE.DesignResponseBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## <param name="part"> (@link NXOpen.BasePart NXOpen.BasePart@endlink) </param>
    ## <param name="desResponse"> (@link DesignResponse NXOpen.DSE.DesignResponse@endlink) </param>
    def CreateDesignResponseBuilder(part: NXOpen.BasePart, desResponse: DesignResponse) -> DesignResponseBuilder:
        """
         Creates a @link DSE::DesignResponseBuilder DSE::DesignResponseBuilder@endlink  
         @return builder (@link DesignResponseBuilder NXOpen.DSE.DesignResponseBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link DSE::DesignSetBuilder DSE::DesignSetBuilder@endlink  
    ##  @return builder (@link DesignSetBuilder NXOpen.DSE.DesignSetBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## <param name="part"> (@link NXOpen.BasePart NXOpen.BasePart@endlink) </param>
    ## <param name="study"> (@link OptimizationStudy NXOpen.DSE.OptimizationStudy@endlink) </param>
    ## <param name="designSet"> (@link DesignSet NXOpen.DSE.DesignSet@endlink) </param>
    def CreateDesignSetBuilder(part: NXOpen.BasePart, study: OptimizationStudy, designSet: DesignSet) -> DesignSetBuilder:
        """
         Creates a @link DSE::DesignSetBuilder DSE::DesignSetBuilder@endlink  
         @return builder (@link DesignSetBuilder NXOpen.DSE.DesignSetBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link DSE::DesignVariableBuilder DSE::DesignVariableBuilder@endlink  
    ##  @return builder (@link DesignVariableBuilder NXOpen.DSE.DesignVariableBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## <param name="part"> (@link NXOpen.BasePart NXOpen.BasePart@endlink) </param>
    ## <param name="dvObj"> (@link DesignVariable NXOpen.DSE.DesignVariable@endlink) </param>
    def CreateDesignVariableBuilder(part: NXOpen.BasePart, dvObj: DesignVariable) -> DesignVariableBuilder:
        """
         Creates a @link DSE::DesignVariableBuilder DSE::DesignVariableBuilder@endlink  
         @return builder (@link DesignVariableBuilder NXOpen.DSE.DesignVariableBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link DSE::DiscreteVariableValueBuilder DSE::DiscreteVariableValueBuilder@endlink  
    ##  @return builder (@link DiscreteVariableValueBuilder NXOpen.DSE.DiscreteVariableValueBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## <param name="part"> (@link NXOpen.BasePart NXOpen.BasePart@endlink) </param>
    ## <param name="discBuilder"> (@link DiscreteDesignVariableBuilder NXOpen.DSE.DiscreteDesignVariableBuilder@endlink) </param>
    def CreateDiscreteVariableValueBuilder(part: NXOpen.BasePart, discBuilder: DiscreteDesignVariableBuilder) -> DiscreteVariableValueBuilder:
        """
         Creates a @link DSE::DiscreteVariableValueBuilder DSE::DiscreteVariableValueBuilder@endlink  
         @return builder (@link DiscreteVariableValueBuilder NXOpen.DSE.DiscreteVariableValueBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link DSE::OptimizationStudyBuilder DSE::OptimizationStudyBuilder@endlink  
    ##  @return builder (@link OptimizationStudyBuilder NXOpen.DSE.OptimizationStudyBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## <param name="part"> (@link NXOpen.BasePart NXOpen.BasePart@endlink) </param>
    ## <param name="studyObj"> (@link OptimizationStudy NXOpen.DSE.OptimizationStudy@endlink) </param>
    def CreateOptimizationStudyBuilder(part: NXOpen.BasePart, studyObj: OptimizationStudy) -> OptimizationStudyBuilder:
        """
         Creates a @link DSE::OptimizationStudyBuilder DSE::OptimizationStudyBuilder@endlink  
         @return builder (@link OptimizationStudyBuilder NXOpen.DSE.OptimizationStudyBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link DSE::PlotBuilder DSE::PlotBuilder@endlink  
    ##  @return builder (@link PlotBuilder NXOpen.DSE.PlotBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_design_explr_eval (" NX Design Space Exploration Evaluation Only") OR nx_perf_predictor (" Performance Predictor")
    ## <param name="part"> (@link NXOpen.BasePart NXOpen.BasePart@endlink) </param>
    ## <param name="plot"> (@link Plot NXOpen.DSE.Plot@endlink) </param>
    def CreatePlotBuilder(part: NXOpen.BasePart, plot: Plot) -> PlotBuilder:
        """
         Creates a @link DSE::PlotBuilder DSE::PlotBuilder@endlink  
         @return builder (@link PlotBuilder NXOpen.DSE.PlotBuilder@endlink): .
        """
        pass
    
## @package NXOpen.DSE
## Classes, Enums and Structs under NXOpen.DSE namespace

##  @link DesignConstraintBuilderNormalizationOption NXOpen.DSE.DesignConstraintBuilderNormalizationOption @endlink is an alias for @link DesignConstraintBuilder.NormalizationOption NXOpen.DSE.DesignConstraintBuilder.NormalizationOption@endlink
DesignConstraintBuilderNormalizationOption = DesignConstraintBuilder.NormalizationOption


##  @link DesignConstraintBuilderTargetType NXOpen.DSE.DesignConstraintBuilderTargetType @endlink is an alias for @link DesignConstraintBuilder.TargetType NXOpen.DSE.DesignConstraintBuilder.TargetType@endlink
DesignConstraintBuilderTargetType = DesignConstraintBuilder.TargetType


##  @link DesignObjectiveBuilderNormalizationOption NXOpen.DSE.DesignObjectiveBuilderNormalizationOption @endlink is an alias for @link DesignObjectiveBuilder.NormalizationOption NXOpen.DSE.DesignObjectiveBuilder.NormalizationOption@endlink
DesignObjectiveBuilderNormalizationOption = DesignObjectiveBuilder.NormalizationOption


##  @link DesignObjectiveBuilderObjectiveTypeOption NXOpen.DSE.DesignObjectiveBuilderObjectiveTypeOption @endlink is an alias for @link DesignObjectiveBuilder.ObjectiveTypeOption NXOpen.DSE.DesignObjectiveBuilder.ObjectiveTypeOption@endlink
DesignObjectiveBuilderObjectiveTypeOption = DesignObjectiveBuilder.ObjectiveTypeOption


##  @link DesignVariableBuilderEnumType NXOpen.DSE.DesignVariableBuilderEnumType @endlink is an alias for @link DesignVariableBuilder.EnumType NXOpen.DSE.DesignVariableBuilder.EnumType@endlink
DesignVariableBuilderEnumType = DesignVariableBuilder.EnumType


##  @link OptimizationStudyBaselineDesignOption NXOpen.DSE.OptimizationStudyBaselineDesignOption @endlink is an alias for @link OptimizationStudy.BaselineDesignOption NXOpen.DSE.OptimizationStudy.BaselineDesignOption@endlink
OptimizationStudyBaselineDesignOption = OptimizationStudy.BaselineDesignOption


##  @link OptimizationStudyDesignTableOption NXOpen.DSE.OptimizationStudyDesignTableOption @endlink is an alias for @link OptimizationStudy.DesignTableOption NXOpen.DSE.OptimizationStudy.DesignTableOption@endlink
OptimizationStudyDesignTableOption = OptimizationStudy.DesignTableOption


##  @link OptimizationStudyResultStorageOption NXOpen.DSE.OptimizationStudyResultStorageOption @endlink is an alias for @link OptimizationStudy.ResultStorageOption NXOpen.DSE.OptimizationStudy.ResultStorageOption@endlink
OptimizationStudyResultStorageOption = OptimizationStudy.ResultStorageOption


##  @link OptimizationStudyRunType NXOpen.DSE.OptimizationStudyRunType @endlink is an alias for @link OptimizationStudy.RunType NXOpen.DSE.OptimizationStudy.RunType@endlink
OptimizationStudyRunType = OptimizationStudy.RunType


##  @link OptimizationStudySherpaMethodOption NXOpen.DSE.OptimizationStudySherpaMethodOption @endlink is an alias for @link OptimizationStudy.SherpaMethodOption NXOpen.DSE.OptimizationStudy.SherpaMethodOption@endlink
OptimizationStudySherpaMethodOption = OptimizationStudy.SherpaMethodOption


##  @link PlotBuilderDesignSetType NXOpen.DSE.PlotBuilderDesignSetType @endlink is an alias for @link PlotBuilder.DesignSetType NXOpen.DSE.PlotBuilder.DesignSetType@endlink
PlotBuilderDesignSetType = PlotBuilder.DesignSetType


##  @link PlotBuilderOutputPlotType NXOpen.DSE.PlotBuilderOutputPlotType @endlink is an alias for @link PlotBuilder.OutputPlotType NXOpen.DSE.PlotBuilder.OutputPlotType@endlink
PlotBuilderOutputPlotType = PlotBuilder.OutputPlotType


##  @link PlotBuilderPlotOption NXOpen.DSE.PlotBuilderPlotOption @endlink is an alias for @link PlotBuilder.PlotOption NXOpen.DSE.PlotBuilder.PlotOption@endlink
PlotBuilderPlotOption = PlotBuilder.PlotOption


