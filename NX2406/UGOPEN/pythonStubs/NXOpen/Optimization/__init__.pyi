from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents a @link NXOpen::Optimization::DesignStudyAttributeBuilder NXOpen::Optimization::DesignStudyAttributeBuilder@endlink   <br> To create a new instance of this class, use @link NXOpen::Optimization::DesignStudyCollection::CreateDesignStudyAttributeBuilder  NXOpen::Optimization::DesignStudyCollection::CreateDesignStudyAttributeBuilder @endlink  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class DesignStudyAttributeBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Optimization.DesignStudyAttributeBuilder</ja_class> """


    ##  Adopt object 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objectValue"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  Object to adopt </param>
    def AdoptObject(self, objectValue: NXOpen.NXObject) -> None:
        """
         Adopt object 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Optimization::DesignStudyBuilder NXOpen::Optimization::DesignStudyBuilder@endlink   <br> To create a new instance of this class, use @link NXOpen::Optimization::DesignStudyCollection::CreateDesignStudyBuilder  NXOpen::Optimization::DesignStudyCollection::CreateDesignStudyBuilder @endlink  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class DesignStudyBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Optimization.DesignStudyBuilder</ja_class> """


    ##  Attribute type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Expression</term><description> 
    ##  Expression type </description> </item><item><term> 
    ## KFAttribute</term><description> 
    ##  KF attribute type </description> </item><item><term> 
    ## GeometryParameter</term><description> 
    ##  Geometry parameter type </description> </item></list>
    class DesignStudyAttributeType(Enum):
        """
        Members Include: <Expression> <KFAttribute> <GeometryParameter>
        """
        Expression: int
        KFAttribute: int
        GeometryParameter: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DesignStudyBuilder.DesignStudyAttributeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Constraint limit type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Upper</term><description> 
    ##  Upper limit type </description> </item><item><term> 
    ## Lower</term><description> 
    ##  Lower limit type </description> </item></list>
    class DesignStudyConstraintLimitType(Enum):
        """
        Members Include: <Upper> <Lower>
        """
        Upper: int
        Lower: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DesignStudyBuilder.DesignStudyConstraintLimitType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Distribution type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Uniform</term><description> 
    ##  Uniform distribution type </description> </item><item><term> 
    ## Normal</term><description> 
    ##  Normal distribution type </description> </item><item><term> 
    ## Gamma</term><description> 
    ##  Gamma distribution type </description> </item></list>
    class DesignStudyDistributeType(Enum):
        """
        Members Include: <Uniform> <Normal> <Gamma>
        """
        Uniform: int
        Normal: int
        Gamma: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DesignStudyBuilder.DesignStudyDistributeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defined Objective Structure 
    ## @link DesignStudyBuilderDesignStudyObjective_Struct NXOpen.Optimization.DesignStudyBuilderDesignStudyObjective_Struct@endlink is an alias for @link DesignStudyBuilder.DesignStudyObjective NXOpen.Optimization.DesignStudyBuilder.DesignStudyObjective@endlink.
    class DesignStudyObjective:
        """
         Defined Objective Structure 
        @link DesignStudyBuilderDesignStudyObjective_Struct NXOpen.Optimization.DesignStudyBuilderDesignStudyObjective_Struct@endlink is an alias for @link DesignStudyBuilder.DesignStudyObjective NXOpen.Optimization.DesignStudyBuilder.DesignStudyObjective@endlink.
        """
        ## Getter for property :(str) AttributeName
        ## Attribute name
        ## @return str
        @property
        def AttributeName(self) -> str:
            """
            Getter for property AttributeName
            Attribute name

            """
            pass
        
        ## Setter for property :(str) AttributeName
        @AttributeName.setter
        def AttributeName(self, value: str):
            """
            Getter for property AttributeName
            Attribute name
            Setter for property AttributeName
            Attribute name

            """
            pass
        
        ## Getter for property :(@link NXOpen.NXObject NXOpen.NXObject@endlink) AttributeObject
        ## Object which the attribute belongs to, it makes sense with geometry design variable type
        ## @return @link NXOpen.NXObject NXOpen.NXObject@endlink
        @property
        def AttributeObject(self) -> NXOpen.NXObject:
            """
            Getter for property AttributeObject
            Object which the attribute belongs to, it makes sense with geometry design variable type

            """
            pass
        
        ## Setter for property :(@link NXOpen.NXObject NXOpen.NXObject@endlink) AttributeObject
        @AttributeObject.setter
        def AttributeObject(self, value: NXOpen.NXObject):
            """
            Getter for property AttributeObject
            Object which the attribute belongs to, it makes sense with geometry design variable type
            Setter for property AttributeObject
            Object which the attribute belongs to, it makes sense with geometry design variable type

            """
            pass
        
        ## Getter for property :(@link DesignStudyBuilder.DesignStudyAttributeType NXOpen.Optimization.DesignStudyBuilder.DesignStudyAttributeType@endlink) ObjectiveType
        ## Objectibe type
        ## @return @link DesignStudyBuilder.DesignStudyAttributeType NXOpen.Optimization.DesignStudyBuilder.DesignStudyAttributeType@endlink
        @property
        def ObjectiveType(self) -> DesignStudyBuilder.DesignStudyAttributeType:
            """
            Getter for property ObjectiveType
            Objectibe type

            """
            pass
        
        ## Setter for property :(@link DesignStudyBuilder.DesignStudyAttributeType NXOpen.Optimization.DesignStudyBuilder.DesignStudyAttributeType@endlink) ObjectiveType
        @ObjectiveType.setter
        def ObjectiveType(self, value: DesignStudyBuilder.DesignStudyAttributeType):
            """
            Getter for property ObjectiveType
            Objectibe type
            Setter for property ObjectiveType
            Objectibe type

            """
            pass
        
        ## Getter for property :(float) WarningLowerLimit
        ## Warning lower limit
        ## @return float
        @property
        def WarningLowerLimit(self) -> float:
            """
            Getter for property WarningLowerLimit
            Warning lower limit

            """
            pass
        
        ## Setter for property :(float) WarningLowerLimit
        @WarningLowerLimit.setter
        def WarningLowerLimit(self, value: float):
            """
            Getter for property WarningLowerLimit
            Warning lower limit
            Setter for property WarningLowerLimit
            Warning lower limit

            """
            pass
        
        ## Getter for property :(float) WarningUpperLimit
        ## Warning Upper limit
        ## @return float
        @property
        def WarningUpperLimit(self) -> float:
            """
            Getter for property WarningUpperLimit
            Warning Upper limit

            """
            pass
        
        ## Setter for property :(float) WarningUpperLimit
        @WarningUpperLimit.setter
        def WarningUpperLimit(self, value: float):
            """
            Getter for property WarningUpperLimit
            Warning Upper limit
            Setter for property WarningUpperLimit
            Warning Upper limit

            """
            pass
        
        ## Getter for property :(float) FailureLowerLimit
        ## Failure Lower limit
        ## @return float
        @property
        def FailureLowerLimit(self) -> float:
            """
            Getter for property FailureLowerLimit
            Failure Lower limit

            """
            pass
        
        ## Setter for property :(float) FailureLowerLimit
        @FailureLowerLimit.setter
        def FailureLowerLimit(self, value: float):
            """
            Getter for property FailureLowerLimit
            Failure Lower limit
            Setter for property FailureLowerLimit
            Failure Lower limit

            """
            pass
        
        ## Getter for property :(float) FailureUpperLimit
        ## Failure Upper limit
        ## @return float
        @property
        def FailureUpperLimit(self) -> float:
            """
            Getter for property FailureUpperLimit
            Failure Upper limit

            """
            pass
        
        ## Setter for property :(float) FailureUpperLimit
        @FailureUpperLimit.setter
        def FailureUpperLimit(self, value: float):
            """
            Getter for property FailureUpperLimit
            Failure Upper limit
            Setter for property FailureUpperLimit
            Failure Upper limit

            """
            pass
        
    
    
    ##  Defined variable structure 
    ## @link DesignStudyBuilderDesignStudyVariable_Struct NXOpen.Optimization.DesignStudyBuilderDesignStudyVariable_Struct@endlink is an alias for @link DesignStudyBuilder.DesignStudyVariable NXOpen.Optimization.DesignStudyBuilder.DesignStudyVariable@endlink.
    class DesignStudyVariable:
        """
         Defined variable structure 
        @link DesignStudyBuilderDesignStudyVariable_Struct NXOpen.Optimization.DesignStudyBuilderDesignStudyVariable_Struct@endlink is an alias for @link DesignStudyBuilder.DesignStudyVariable NXOpen.Optimization.DesignStudyBuilder.DesignStudyVariable@endlink.
        """
        ## Getter for property :(str) AttributeName
        ## Attribute name
        ## @return str
        @property
        def AttributeName(self) -> str:
            """
            Getter for property AttributeName
            Attribute name

            """
            pass
        
        ## Setter for property :(str) AttributeName
        @AttributeName.setter
        def AttributeName(self, value: str):
            """
            Getter for property AttributeName
            Attribute name
            Setter for property AttributeName
            Attribute name

            """
            pass
        
        ## Getter for property :(@link NXOpen.NXObject NXOpen.NXObject@endlink) AttributeObject
        ## Object which the attribute belongs to, it makes sense with geometry design variable type
        ## @return @link NXOpen.NXObject NXOpen.NXObject@endlink
        @property
        def AttributeObject(self) -> NXOpen.NXObject:
            """
            Getter for property AttributeObject
            Object which the attribute belongs to, it makes sense with geometry design variable type

            """
            pass
        
        ## Setter for property :(@link NXOpen.NXObject NXOpen.NXObject@endlink) AttributeObject
        @AttributeObject.setter
        def AttributeObject(self, value: NXOpen.NXObject):
            """
            Getter for property AttributeObject
            Object which the attribute belongs to, it makes sense with geometry design variable type
            Setter for property AttributeObject
            Object which the attribute belongs to, it makes sense with geometry design variable type

            """
            pass
        
        ## Getter for property :(@link DesignStudyBuilder.DesignStudyAttributeType NXOpen.Optimization.DesignStudyBuilder.DesignStudyAttributeType@endlink) VariableType
        ## Variable type
        ## @return @link DesignStudyBuilder.DesignStudyAttributeType NXOpen.Optimization.DesignStudyBuilder.DesignStudyAttributeType@endlink
        @property
        def VariableType(self) -> DesignStudyBuilder.DesignStudyAttributeType:
            """
            Getter for property VariableType
            Variable type

            """
            pass
        
        ## Setter for property :(@link DesignStudyBuilder.DesignStudyAttributeType NXOpen.Optimization.DesignStudyBuilder.DesignStudyAttributeType@endlink) VariableType
        @VariableType.setter
        def VariableType(self, value: DesignStudyBuilder.DesignStudyAttributeType):
            """
            Getter for property VariableType
            Variable type
            Setter for property VariableType
            Variable type

            """
            pass
        
        ## Getter for property :(float) VariableLowerLimitValue
        ## Lower limit value
        ## @return float
        @property
        def VariableLowerLimitValue(self) -> float:
            """
            Getter for property VariableLowerLimitValue
            Lower limit value

            """
            pass
        
        ## Setter for property :(float) VariableLowerLimitValue
        @VariableLowerLimitValue.setter
        def VariableLowerLimitValue(self, value: float):
            """
            Getter for property VariableLowerLimitValue
            Lower limit value
            Setter for property VariableLowerLimitValue
            Lower limit value

            """
            pass
        
        ## Getter for property :(float) VariableUpperLimitValue
        ## Upper limit value
        ## @return float
        @property
        def VariableUpperLimitValue(self) -> float:
            """
            Getter for property VariableUpperLimitValue
            Upper limit value

            """
            pass
        
        ## Setter for property :(float) VariableUpperLimitValue
        @VariableUpperLimitValue.setter
        def VariableUpperLimitValue(self, value: float):
            """
            Getter for property VariableUpperLimitValue
            Upper limit value
            Setter for property VariableUpperLimitValue
            Upper limit value

            """
            pass
        
        ## Getter for property :(@link DesignStudyBuilder.DesignStudyDistributeType NXOpen.Optimization.DesignStudyBuilder.DesignStudyDistributeType@endlink) DistributeType
        ## Distribute type
        ## @return @link DesignStudyBuilder.DesignStudyDistributeType NXOpen.Optimization.DesignStudyBuilder.DesignStudyDistributeType@endlink
        @property
        def DistributeType(self) -> DesignStudyBuilder.DesignStudyDistributeType:
            """
            Getter for property DistributeType
            Distribute type

            """
            pass
        
        ## Setter for property :(@link DesignStudyBuilder.DesignStudyDistributeType NXOpen.Optimization.DesignStudyBuilder.DesignStudyDistributeType@endlink) DistributeType
        @DistributeType.setter
        def DistributeType(self, value: DesignStudyBuilder.DesignStudyDistributeType):
            """
            Getter for property DistributeType
            Distribute type
            Setter for property DistributeType
            Distribute type

            """
            pass
        
        ## Getter for property :(float) LocationParameter
        ## Location parameter
        ## @return float
        @property
        def LocationParameter(self) -> float:
            """
            Getter for property LocationParameter
            Location parameter

            """
            pass
        
        ## Setter for property :(float) LocationParameter
        @LocationParameter.setter
        def LocationParameter(self, value: float):
            """
            Getter for property LocationParameter
            Location parameter
            Setter for property LocationParameter
            Location parameter

            """
            pass
        
        ## Getter for property :(float) ScaleParameter
        ## Scale parameter
        ## @return float
        @property
        def ScaleParameter(self) -> float:
            """
            Getter for property ScaleParameter
            Scale parameter

            """
            pass
        
        ## Setter for property :(float) ScaleParameter
        @ScaleParameter.setter
        def ScaleParameter(self, value: float):
            """
            Getter for property ScaleParameter
            Scale parameter
            Setter for property ScaleParameter
            Scale parameter

            """
            pass
        
        ## Getter for property :(float) ShapeParameter
        ## Shape parameter
        ## @return float
        @property
        def ShapeParameter(self) -> float:
            """
            Getter for property ShapeParameter
            Shape parameter

            """
            pass
        
        ## Setter for property :(float) ShapeParameter
        @ShapeParameter.setter
        def ShapeParameter(self, value: float):
            """
            Getter for property ShapeParameter
            Shape parameter
            Setter for property ShapeParameter
            Shape parameter

            """
            pass
        
        ## Getter for property :(int) ValuesCount
        ## Values count
        ## @return int
        @property
        def ValuesCount(self) -> int:
            """
            Getter for property ValuesCount
            Values count

            """
            pass
        
        ## Setter for property :(int) ValuesCount
        @ValuesCount.setter
        def ValuesCount(self, value: int):
            """
            Getter for property ValuesCount
            Values count
            Setter for property ValuesCount
            Values count

            """
            pass
        
    
    
    ## Getter for property: (bool) IsShowGraph
    ##  Returns the property - is show graph   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def IsShowGraph(self) -> bool:
        """
        Getter for property: (bool) IsShowGraph
         Returns the property - is show graph   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsShowGraph

    ##  Returns the property - is show graph   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @IsShowGraph.setter
    def IsShowGraph(self, isShowGraph: bool):
        """
        Setter for property: (bool) IsShowGraph
         Returns the property - is show graph   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsUpdateDisp
    ##  Returns the property - is update display   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def IsUpdateDisp(self) -> bool:
        """
        Getter for property: (bool) IsUpdateDisp
         Returns the property - is update display   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsUpdateDisp

    ##  Returns the property - is update display   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @IsUpdateDisp.setter
    def IsUpdateDisp(self, isUpdateDisp: bool):
        """
        Setter for property: (bool) IsUpdateDisp
         Returns the property - is update display   
            
         
        """
        pass
    
    ## Getter for property: (str) StudyName
    ##  Returns the study name which is unique in one part   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return str
    @property
    def StudyName(self) -> str:
        """
        Getter for property: (str) StudyName
         Returns the study name which is unique in one part   
            
         
        """
        pass
    
    ## Setter for property: (str) StudyName

    ##  Returns the study name which is unique in one part   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @StudyName.setter
    def StudyName(self, studyName: str):
        """
        Setter for property: (str) StudyName
         Returns the study name which is unique in one part   
            
         
        """
        pass
    
    ##  Build all the objectives 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def BuildAllObjectives(self) -> None:
        """
         Build all the objectives 
        """
        pass
    
    ##  Build all the variables 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def BuildAllVariables(self) -> None:
        """
         Build all the variables 
        """
        pass
    
    ##  Returns the objectives 
    ##  @return objectives (@link DesignStudyBuilder.DesignStudyObjective List[NXOpen.Optimization.DesignStudyBuilder.DesignStudyObjective]@endlink):  Objectives .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def GetDesignStudyObjectives(self) -> List[DesignStudyBuilder.DesignStudyObjective]:
        """
         Returns the objectives 
         @return objectives (@link DesignStudyBuilder.DesignStudyObjective List[NXOpen.Optimization.DesignStudyBuilder.DesignStudyObjective]@endlink):  Objectives .
        """
        pass
    
    ##  Returns the variables 
    ##  @return variables (@link DesignStudyBuilder.DesignStudyVariable List[NXOpen.Optimization.DesignStudyBuilder.DesignStudyVariable]@endlink):  Variables .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def GetDesignStudyVariables(self) -> List[DesignStudyBuilder.DesignStudyVariable]:
        """
         Returns the variables 
         @return variables (@link DesignStudyBuilder.DesignStudyVariable List[NXOpen.Optimization.DesignStudyBuilder.DesignStudyVariable]@endlink):  Variables .
        """
        pass
    
    ##  Remove all the objectives 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def RemoveAllObjectives(self) -> None:
        """
         Remove all the objectives 
        """
        pass
    
    ##  Remove all the variables 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def RemoveAllVariables(self) -> None:
        """
         Remove all the variables 
        """
        pass
    
    ##  Run design study process 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def RunDesignStudy(self) -> None:
        """
         Run design study process 
        """
        pass
    
    ##  Sets the objectives 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="attributeNames"> (List[str])  Objective attribute name array </param>
    ## <param name="attributeObjects"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  Objective attribute object array </param>
    ## <param name="objectiveTypes"> (@link DesignStudyBuilder.DesignStudyAttributeType List[NXOpen.Optimization.DesignStudyBuilder.DesignStudyAttributeType]@endlink)  Objective attribute type array </param>
    ## <param name="warningLowerLimit"> (List[float])  Warning lower limit </param>
    ## <param name="warningUpperLimit"> (List[float])  Warning upper limit </param>
    ## <param name="failureLowerLimit"> (List[float])  Failure lower limit </param>
    ## <param name="failureUpperLimit"> (List[float])  Failure upper limit </param>
    def SetDesignStudyObjectives(self, attributeNames: List[str], attributeObjects: List[NXOpen.NXObject], objectiveTypes: List[DesignStudyBuilder.DesignStudyAttributeType], warningLowerLimit: List[float], warningUpperLimit: List[float], failureLowerLimit: List[float], failureUpperLimit: List[float]) -> None:
        """
         Sets the objectives 
        """
        pass
    
    ##  Sets the variables 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="attributeNames"> (List[str])  Variable attribute name array </param>
    ## <param name="attributeObjects"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  Variable attribute object array </param>
    ## <param name="variableTypes"> (@link DesignStudyBuilder.DesignStudyAttributeType List[NXOpen.Optimization.DesignStudyBuilder.DesignStudyAttributeType]@endlink)  Variable attribute type array </param>
    ## <param name="variableLowerLimitValue"> (List[float])  Variable lower limit value array </param>
    ## <param name="variableUpperLimitValue"> (List[float])  Variable upper limit value array </param>
    ## <param name="distributeType"> (@link DesignStudyBuilder.DesignStudyDistributeType List[NXOpen.Optimization.DesignStudyBuilder.DesignStudyDistributeType]@endlink)  Distribute type </param>
    ## <param name="locationParameter"> (List[float])  Location parameter </param>
    ## <param name="scaleParameter"> (List[float])  Scale parameter </param>
    ## <param name="shapeParameter"> (List[float])  Shape parameter </param>
    ## <param name="valuesCount"> (List[int])  Values count </param>
    def SetDesignStudyVariables(self, attributeNames: List[str], attributeObjects: List[NXOpen.NXObject], variableTypes: List[DesignStudyBuilder.DesignStudyAttributeType], variableLowerLimitValue: List[float], variableUpperLimitValue: List[float], distributeType: List[DesignStudyBuilder.DesignStudyDistributeType], locationParameter: List[float], scaleParameter: List[float], shapeParameter: List[float], valuesCount: List[int]) -> None:
        """
         Sets the variables 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Optimization::DesignStudyCollection NXOpen::Optimization::DesignStudyCollection@endlink   <br> To obtain an instance of this class, refer to @link NXOpen::BasePart  NXOpen::BasePart @endlink  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class DesignStudyCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a <ja_class>NXOpen.Optimization.DesignStudyCollection</ja_class> """


    ##  Create builder for DesignStudyAttribute class 
    ##  @return builder (@link DesignStudyAttributeBuilder NXOpen.Optimization.DesignStudyAttributeBuilder@endlink): .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def CreateDesignStudyAttributeBuilder(self) -> DesignStudyAttributeBuilder:
        """
         Create builder for DesignStudyAttribute class 
         @return builder (@link DesignStudyAttributeBuilder NXOpen.Optimization.DesignStudyAttributeBuilder@endlink): .
        """
        pass
    
    ##  Create builder for design study class 
    ##  @return builder (@link DesignStudyBuilder NXOpen.Optimization.DesignStudyBuilder@endlink): .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def CreateDesignStudyBuilder(self) -> DesignStudyBuilder:
        """
         Create builder for design study class 
         @return builder (@link DesignStudyBuilder NXOpen.Optimization.DesignStudyBuilder@endlink): .
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Optimization::MapleExpBuilder NXOpen::Optimization::MapleExpBuilder@endlink   <br> To create a new instance of this class, use @link NXOpen::Optimization::OptimizationCollection::CreateMapleExpBuilder  NXOpen::Optimization::OptimizationCollection::CreateMapleExpBuilder @endlink  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 
## 
##   <br>  @deprecated Deprecated in NX12.0.0.  Use @link NXOpen::Optimization::MathIntegrationExpBuilder NXOpen::Optimization::MathIntegrationExpBuilder@endlink  instead.  <br> 

class MapleExpBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Optimization.MapleExpBuilder</ja_class> """
    pass


import NXOpen
##  Represents a @link NXOpen::Optimization::MathIntegrationExpBuilder NXOpen::Optimization::MathIntegrationExpBuilder@endlink   <br> To create a new instance of this class, use @link NXOpen::Optimization::OptimizationCollection::CreateMathIntegrationExpBuilder  NXOpen::Optimization::OptimizationCollection::CreateMathIntegrationExpBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class MathIntegrationExpBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Optimization.MathIntegrationExpBuilder</ja_class> """
    pass


import NXOpen
##  Represents a @link NXOpen::Optimization::OptimizationAttributeBuilder NXOpen::Optimization::OptimizationAttributeBuilder@endlink   <br> To create a new instance of this class, use @link NXOpen::Optimization::OptimizationCollection::CreateOptimizationAttributeBuilder  NXOpen::Optimization::OptimizationCollection::CreateOptimizationAttributeBuilder @endlink  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class OptimizationAttributeBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Optimization.OptimizationAttributeBuilder</ja_class> """


    ##  Adopt object 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objectValue"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  Object to adopt </param>
    def AdoptObject(self, objectValue: NXOpen.NXObject) -> None:
        """
         Adopt object 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Optimization::OptimizationBuilder NXOpen::Optimization::OptimizationBuilder@endlink   <br> To create a new instance of this class, use @link NXOpen::Optimization::OptimizationCollection::CreateOptimizationBuilder  NXOpen::Optimization::OptimizationCollection::CreateOptimizationBuilder @endlink  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class OptimizationBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Optimization.OptimizationBuilder</ja_class> """


    ##  Algorithm type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## SimulatedAnnealing</term><description> 
    ##  Simulated annealing </description> </item><item><term> 
    ## GlobalSimplex</term><description> 
    ##  Global simplex </description> </item><item><term> 
    ## Powell</term><description> 
    ##  Powell </description> </item><item><term> 
    ## ConjugateGradient</term><description> 
    ##  Conjugate gradient </description> </item><item><term> 
    ## Lexicographic</term><description> 
    ##  Lexicographic </description> </item><item><term> 
    ## PatternSwarm</term><description> 
    ##  Pattern swarm </description> </item></list>
    class OptimizationAlgorithmType(Enum):
        """
        Members Include: <SimulatedAnnealing> <GlobalSimplex> <Powell> <ConjugateGradient> <Lexicographic> <PatternSwarm>
        """
        SimulatedAnnealing: int
        GlobalSimplex: int
        Powell: int
        ConjugateGradient: int
        Lexicographic: int
        PatternSwarm: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OptimizationBuilder.OptimizationAlgorithmType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Attribute type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Expression</term><description> 
    ##  Expression attribute </description> </item><item><term> 
    ## KFAttribute</term><description> 
    ##  KF attribute </description> </item><item><term> 
    ## GeometryParameter</term><description> 
    ##  Geometry/feature parameter attribute</description> </item></list>
    class OptimizationAttributeType(Enum):
        """
        Members Include: <Expression> <KFAttribute> <GeometryParameter>
        """
        Expression: int
        KFAttribute: int
        GeometryParameter: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OptimizationBuilder.OptimizationAttributeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Constraint limit type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Upper</term><description> 
    ##  Upper limit </description> </item><item><term> 
    ## Lower</term><description> 
    ##  Lower limit </description> </item></list>
    class OptimizationConstraintLimitType(Enum):
        """
        Members Include: <Upper> <Lower>
        """
        Upper: int
        Lower: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OptimizationBuilder.OptimizationConstraintLimitType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Convergence speed type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Slow</term><description> 
    ##  Slow convergence speed </description> </item><item><term> 
    ## Medium</term><description> 
    ##  Medium convergence speed</description> </item><item><term> 
    ## Fast</term><description> 
    ##  Fast convergence speed</description> </item><item><term> 
    ## Infinite</term><description> 
    ##  Infinite convergence speed</description> </item></list>
    class OptimizationConvergenceSpeedType(Enum):
        """
        Members Include: <Slow> <Medium> <Fast> <Infinite>
        """
        Slow: int
        Medium: int
        Fast: int
        Infinite: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OptimizationBuilder.OptimizationConvergenceSpeedType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Optimization type for objective 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Minimum</term><description> 
    ##  Target is minimum value of design objective </description> </item><item><term> 
    ## Maximum</term><description> 
    ##  Target is maximum value of design objective </description> </item><item><term> 
    ## Target</term><description> 
    ##  Target is specified value of design objective </description> </item></list>
    class OptimizationTargetType(Enum):
        """
        Members Include: <Minimum> <Maximum> <Target>
        """
        Minimum: int
        Maximum: int
        Target: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OptimizationBuilder.OptimizationTargetType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defined constraint structure 
    ## @link OptimizationBuilderOptimizationConstraint_Struct NXOpen.Optimization.OptimizationBuilderOptimizationConstraint_Struct@endlink is an alias for @link OptimizationBuilder.OptimizationConstraint NXOpen.Optimization.OptimizationBuilder.OptimizationConstraint@endlink.
    class OptimizationConstraint:
        """
         Defined constraint structure 
        @link OptimizationBuilderOptimizationConstraint_Struct NXOpen.Optimization.OptimizationBuilderOptimizationConstraint_Struct@endlink is an alias for @link OptimizationBuilder.OptimizationConstraint NXOpen.Optimization.OptimizationBuilder.OptimizationConstraint@endlink.
        """
        ## Getter for property :(str) AttributeName
        ## Attribute name
        ## @return str
        @property
        def AttributeName(self) -> str:
            """
            Getter for property AttributeName
            Attribute name

            """
            pass
        
        ## Setter for property :(str) AttributeName
        @AttributeName.setter
        def AttributeName(self, value: str):
            """
            Getter for property AttributeName
            Attribute name
            Setter for property AttributeName
            Attribute name

            """
            pass
        
        ## Getter for property :(@link NXOpen.NXObject NXOpen.NXObject@endlink) AttributeObject
        ## Object which the attribute belongs to, it makes sense with geometry design variable type
        ## @return @link NXOpen.NXObject NXOpen.NXObject@endlink
        @property
        def AttributeObject(self) -> NXOpen.NXObject:
            """
            Getter for property AttributeObject
            Object which the attribute belongs to, it makes sense with geometry design variable type

            """
            pass
        
        ## Setter for property :(@link NXOpen.NXObject NXOpen.NXObject@endlink) AttributeObject
        @AttributeObject.setter
        def AttributeObject(self, value: NXOpen.NXObject):
            """
            Getter for property AttributeObject
            Object which the attribute belongs to, it makes sense with geometry design variable type
            Setter for property AttributeObject
            Object which the attribute belongs to, it makes sense with geometry design variable type

            """
            pass
        
        ## Getter for property :(@link OptimizationBuilder.OptimizationAttributeType NXOpen.Optimization.OptimizationBuilder.OptimizationAttributeType@endlink) ConstraintType
        ## Constraint type
        ## @return @link OptimizationBuilder.OptimizationAttributeType NXOpen.Optimization.OptimizationBuilder.OptimizationAttributeType@endlink
        @property
        def ConstraintType(self) -> OptimizationBuilder.OptimizationAttributeType:
            """
            Getter for property ConstraintType
            Constraint type

            """
            pass
        
        ## Setter for property :(@link OptimizationBuilder.OptimizationAttributeType NXOpen.Optimization.OptimizationBuilder.OptimizationAttributeType@endlink) ConstraintType
        @ConstraintType.setter
        def ConstraintType(self, value: OptimizationBuilder.OptimizationAttributeType):
            """
            Getter for property ConstraintType
            Constraint type
            Setter for property ConstraintType
            Constraint type

            """
            pass
        
        ## Getter for property :(float) ConstraintLowerLimitValue
        ## Lower limit value
        ## @return float
        @property
        def ConstraintLowerLimitValue(self) -> float:
            """
            Getter for property ConstraintLowerLimitValue
            Lower limit value

            """
            pass
        
        ## Setter for property :(float) ConstraintLowerLimitValue
        @ConstraintLowerLimitValue.setter
        def ConstraintLowerLimitValue(self, value: float):
            """
            Getter for property ConstraintLowerLimitValue
            Lower limit value
            Setter for property ConstraintLowerLimitValue
            Lower limit value

            """
            pass
        
        ## Getter for property :(float) ConstraintUpperLimitValue
        ## Upper limit value
        ## @return float
        @property
        def ConstraintUpperLimitValue(self) -> float:
            """
            Getter for property ConstraintUpperLimitValue
            Upper limit value

            """
            pass
        
        ## Setter for property :(float) ConstraintUpperLimitValue
        @ConstraintUpperLimitValue.setter
        def ConstraintUpperLimitValue(self, value: float):
            """
            Getter for property ConstraintUpperLimitValue
            Upper limit value
            Setter for property ConstraintUpperLimitValue
            Upper limit value

            """
            pass
        
        ## Getter for property :(@link OptimizationBuilder.OptimizationConstraintLimitType NXOpen.Optimization.OptimizationBuilder.OptimizationConstraintLimitType@endlink) ConstraintLimitType
        ## constraint limit type, lower type or upper type
        ## @return @link OptimizationBuilder.OptimizationConstraintLimitType NXOpen.Optimization.OptimizationBuilder.OptimizationConstraintLimitType@endlink
        @property
        def ConstraintLimitType(self) -> OptimizationBuilder.OptimizationConstraintLimitType:
            """
            Getter for property ConstraintLimitType
            constraint limit type, lower type or upper type

            """
            pass
        
        ## Setter for property :(@link OptimizationBuilder.OptimizationConstraintLimitType NXOpen.Optimization.OptimizationBuilder.OptimizationConstraintLimitType@endlink) ConstraintLimitType
        @ConstraintLimitType.setter
        def ConstraintLimitType(self, value: OptimizationBuilder.OptimizationConstraintLimitType):
            """
            Getter for property ConstraintLimitType
            constraint limit type, lower type or upper type
            Setter for property ConstraintLimitType
            constraint limit type, lower type or upper type

            """
            pass
        
    
    
    ##  Defined Objective Structure 
    ## @link OptimizationBuilderOptimizationObjective_Struct NXOpen.Optimization.OptimizationBuilderOptimizationObjective_Struct@endlink is an alias for @link OptimizationBuilder.OptimizationObjective NXOpen.Optimization.OptimizationBuilder.OptimizationObjective@endlink.
    class OptimizationObjective:
        """
         Defined Objective Structure 
        @link OptimizationBuilderOptimizationObjective_Struct NXOpen.Optimization.OptimizationBuilderOptimizationObjective_Struct@endlink is an alias for @link OptimizationBuilder.OptimizationObjective NXOpen.Optimization.OptimizationBuilder.OptimizationObjective@endlink.
        """
        ## Getter for property :(str) AttributeName
        ## Attribute name
        ## @return str
        @property
        def AttributeName(self) -> str:
            """
            Getter for property AttributeName
            Attribute name

            """
            pass
        
        ## Setter for property :(str) AttributeName
        @AttributeName.setter
        def AttributeName(self, value: str):
            """
            Getter for property AttributeName
            Attribute name
            Setter for property AttributeName
            Attribute name

            """
            pass
        
        ## Getter for property :(@link NXOpen.NXObject NXOpen.NXObject@endlink) AttributeObject
        ## Object which the attribute belongs to, it makes sense with geometry design variable type
        ## @return @link NXOpen.NXObject NXOpen.NXObject@endlink
        @property
        def AttributeObject(self) -> NXOpen.NXObject:
            """
            Getter for property AttributeObject
            Object which the attribute belongs to, it makes sense with geometry design variable type

            """
            pass
        
        ## Setter for property :(@link NXOpen.NXObject NXOpen.NXObject@endlink) AttributeObject
        @AttributeObject.setter
        def AttributeObject(self, value: NXOpen.NXObject):
            """
            Getter for property AttributeObject
            Object which the attribute belongs to, it makes sense with geometry design variable type
            Setter for property AttributeObject
            Object which the attribute belongs to, it makes sense with geometry design variable type

            """
            pass
        
        ## Getter for property :(@link OptimizationBuilder.OptimizationAttributeType NXOpen.Optimization.OptimizationBuilder.OptimizationAttributeType@endlink) ObjectiveType
        ## Objectibe type
        ## @return @link OptimizationBuilder.OptimizationAttributeType NXOpen.Optimization.OptimizationBuilder.OptimizationAttributeType@endlink
        @property
        def ObjectiveType(self) -> OptimizationBuilder.OptimizationAttributeType:
            """
            Getter for property ObjectiveType
            Objectibe type

            """
            pass
        
        ## Setter for property :(@link OptimizationBuilder.OptimizationAttributeType NXOpen.Optimization.OptimizationBuilder.OptimizationAttributeType@endlink) ObjectiveType
        @ObjectiveType.setter
        def ObjectiveType(self, value: OptimizationBuilder.OptimizationAttributeType):
            """
            Getter for property ObjectiveType
            Objectibe type
            Setter for property ObjectiveType
            Objectibe type

            """
            pass
        
        ## Getter for property :(float) ObjectiveTargetValue
        ## Value of objective target
        ## @return float
        @property
        def ObjectiveTargetValue(self) -> float:
            """
            Getter for property ObjectiveTargetValue
            Value of objective target

            """
            pass
        
        ## Setter for property :(float) ObjectiveTargetValue
        @ObjectiveTargetValue.setter
        def ObjectiveTargetValue(self, value: float):
            """
            Getter for property ObjectiveTargetValue
            Value of objective target
            Setter for property ObjectiveTargetValue
            Value of objective target

            """
            pass
        
    
    
    ##  Defined variable structure 
    ## @link OptimizationBuilderOptimizationVariable_Struct NXOpen.Optimization.OptimizationBuilderOptimizationVariable_Struct@endlink is an alias for @link OptimizationBuilder.OptimizationVariable NXOpen.Optimization.OptimizationBuilder.OptimizationVariable@endlink.
    class OptimizationVariable:
        """
         Defined variable structure 
        @link OptimizationBuilderOptimizationVariable_Struct NXOpen.Optimization.OptimizationBuilderOptimizationVariable_Struct@endlink is an alias for @link OptimizationBuilder.OptimizationVariable NXOpen.Optimization.OptimizationBuilder.OptimizationVariable@endlink.
        """
        ## Getter for property :(str) AttributeName
        ## Attribute name
        ## @return str
        @property
        def AttributeName(self) -> str:
            """
            Getter for property AttributeName
            Attribute name

            """
            pass
        
        ## Setter for property :(str) AttributeName
        @AttributeName.setter
        def AttributeName(self, value: str):
            """
            Getter for property AttributeName
            Attribute name
            Setter for property AttributeName
            Attribute name

            """
            pass
        
        ## Getter for property :(@link NXOpen.NXObject NXOpen.NXObject@endlink) AttributeObject
        ## Object which the attribute belongs to, it makes sense with geometry design variable type
        ## @return @link NXOpen.NXObject NXOpen.NXObject@endlink
        @property
        def AttributeObject(self) -> NXOpen.NXObject:
            """
            Getter for property AttributeObject
            Object which the attribute belongs to, it makes sense with geometry design variable type

            """
            pass
        
        ## Setter for property :(@link NXOpen.NXObject NXOpen.NXObject@endlink) AttributeObject
        @AttributeObject.setter
        def AttributeObject(self, value: NXOpen.NXObject):
            """
            Getter for property AttributeObject
            Object which the attribute belongs to, it makes sense with geometry design variable type
            Setter for property AttributeObject
            Object which the attribute belongs to, it makes sense with geometry design variable type

            """
            pass
        
        ## Getter for property :(@link OptimizationBuilder.OptimizationAttributeType NXOpen.Optimization.OptimizationBuilder.OptimizationAttributeType@endlink) VariableType
        ## Variable type
        ## @return @link OptimizationBuilder.OptimizationAttributeType NXOpen.Optimization.OptimizationBuilder.OptimizationAttributeType@endlink
        @property
        def VariableType(self) -> OptimizationBuilder.OptimizationAttributeType:
            """
            Getter for property VariableType
            Variable type

            """
            pass
        
        ## Setter for property :(@link OptimizationBuilder.OptimizationAttributeType NXOpen.Optimization.OptimizationBuilder.OptimizationAttributeType@endlink) VariableType
        @VariableType.setter
        def VariableType(self, value: OptimizationBuilder.OptimizationAttributeType):
            """
            Getter for property VariableType
            Variable type
            Setter for property VariableType
            Variable type

            """
            pass
        
        ## Getter for property :(float) VariableLowerLimitValue
        ## Lower limit value
        ## @return float
        @property
        def VariableLowerLimitValue(self) -> float:
            """
            Getter for property VariableLowerLimitValue
            Lower limit value

            """
            pass
        
        ## Setter for property :(float) VariableLowerLimitValue
        @VariableLowerLimitValue.setter
        def VariableLowerLimitValue(self, value: float):
            """
            Getter for property VariableLowerLimitValue
            Lower limit value
            Setter for property VariableLowerLimitValue
            Lower limit value

            """
            pass
        
        ## Getter for property :(float) VariableUpperLimitValue
        ## Upper limit value
        ## @return float
        @property
        def VariableUpperLimitValue(self) -> float:
            """
            Getter for property VariableUpperLimitValue
            Upper limit value

            """
            pass
        
        ## Setter for property :(float) VariableUpperLimitValue
        @VariableUpperLimitValue.setter
        def VariableUpperLimitValue(self, value: float):
            """
            Getter for property VariableUpperLimitValue
            Upper limit value
            Setter for property VariableUpperLimitValue
            Upper limit value

            """
            pass
        
    
    
    ## Getter for property: (float) AbsoluteConvergenceCriteria
    ##  Returns the absolute criteria for optimizer to determine convergence.  
    ##    This value is
    ##             multiplied by the first objective result,and if the difference in last two 
    ##             objective results is less than this, then it is converged   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return float
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
    
    ## Setter for property: (float) AbsoluteConvergenceCriteria

    ##  Returns the absolute criteria for optimizer to determine convergence.  
    ##    This value is
    ##             multiplied by the first objective result,and if the difference in last two 
    ##             objective results is less than this, then it is converged   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

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
    
    ## Getter for property: (@link OptimizationBuilder.OptimizationAlgorithmType NXOpen.Optimization.OptimizationBuilder.OptimizationAlgorithmType@endlink) AlgorithmType
    ##  Returns the algorithm type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return OptimizationBuilder.OptimizationAlgorithmType
    @property
    def AlgorithmType(self) -> OptimizationBuilder.OptimizationAlgorithmType:
        """
        Getter for property: (@link OptimizationBuilder.OptimizationAlgorithmType NXOpen.Optimization.OptimizationBuilder.OptimizationAlgorithmType@endlink) AlgorithmType
         Returns the algorithm type   
            
         
        """
        pass
    
    ## Setter for property: (@link OptimizationBuilder.OptimizationAlgorithmType NXOpen.Optimization.OptimizationBuilder.OptimizationAlgorithmType@endlink) AlgorithmType

    ##  Returns the algorithm type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @AlgorithmType.setter
    def AlgorithmType(self, algorithmType: OptimizationBuilder.OptimizationAlgorithmType):
        """
        Setter for property: (@link OptimizationBuilder.OptimizationAlgorithmType NXOpen.Optimization.OptimizationBuilder.OptimizationAlgorithmType@endlink) AlgorithmType
         Returns the algorithm type   
            
         
        """
        pass
    
    ## Getter for property: (@link OptimizationBuilder.OptimizationConvergenceSpeedType NXOpen.Optimization.OptimizationBuilder.OptimizationConvergenceSpeedType@endlink) ConvergenceSpeedType
    ##  Returns the convergence speed type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return OptimizationBuilder.OptimizationConvergenceSpeedType
    @property
    def ConvergenceSpeedType(self) -> OptimizationBuilder.OptimizationConvergenceSpeedType:
        """
        Getter for property: (@link OptimizationBuilder.OptimizationConvergenceSpeedType NXOpen.Optimization.OptimizationBuilder.OptimizationConvergenceSpeedType@endlink) ConvergenceSpeedType
         Returns the convergence speed type   
            
         
        """
        pass
    
    ## Setter for property: (@link OptimizationBuilder.OptimizationConvergenceSpeedType NXOpen.Optimization.OptimizationBuilder.OptimizationConvergenceSpeedType@endlink) ConvergenceSpeedType

    ##  Returns the convergence speed type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @ConvergenceSpeedType.setter
    def ConvergenceSpeedType(self, convergenceSpeedType: OptimizationBuilder.OptimizationConvergenceSpeedType):
        """
        Setter for property: (@link OptimizationBuilder.OptimizationConvergenceSpeedType NXOpen.Optimization.OptimizationBuilder.OptimizationConvergenceSpeedType@endlink) ConvergenceSpeedType
         Returns the convergence speed type   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsShowGraph
    ##  Returns the property - is show graph   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def IsShowGraph(self) -> bool:
        """
        Getter for property: (bool) IsShowGraph
         Returns the property - is show graph   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsShowGraph

    ##  Returns the property - is show graph   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @IsShowGraph.setter
    def IsShowGraph(self, isShowGraph: bool):
        """
        Setter for property: (bool) IsShowGraph
         Returns the property - is show graph   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsUpdateDisp
    ##  Returns the property - is update display   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def IsUpdateDisp(self) -> bool:
        """
        Getter for property: (bool) IsUpdateDisp
         Returns the property - is update display   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsUpdateDisp

    ##  Returns the property - is update display   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @IsUpdateDisp.setter
    def IsUpdateDisp(self, isUpdateDisp: bool):
        """
        Setter for property: (bool) IsUpdateDisp
         Returns the property - is update display   
            
         
        """
        pass
    
    ## Getter for property: (int) MaxNumberIteration
    ##  Returns the maximum number of updates allowed without converging to a solutionthe maximum iterations time  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return int
    @property
    def MaxNumberIteration(self) -> int:
        """
        Getter for property: (int) MaxNumberIteration
         Returns the maximum number of updates allowed without converging to a solutionthe maximum iterations time  
            
         
        """
        pass
    
    ## Setter for property: (int) MaxNumberIteration

    ##  Returns the maximum number of updates allowed without converging to a solutionthe maximum iterations time  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @MaxNumberIteration.setter
    def MaxNumberIteration(self, integerMaxNumIter: int):
        """
        Setter for property: (int) MaxNumberIteration
         Returns the maximum number of updates allowed without converging to a solutionthe maximum iterations time  
            
         
        """
        pass
    
    ## Getter for property: (int) MaxTime
    ##  Returns the maximum time allowed for this run in seconds   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return int
    @property
    def MaxTime(self) -> int:
        """
        Getter for property: (int) MaxTime
         Returns the maximum time allowed for this run in seconds   
            
         
        """
        pass
    
    ## Setter for property: (int) MaxTime

    ##  Returns the maximum time allowed for this run in seconds   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @MaxTime.setter
    def MaxTime(self, maxTime: int):
        """
        Setter for property: (int) MaxTime
         Returns the maximum time allowed for this run in seconds   
            
         
        """
        pass
    
    ## Getter for property: (@link OptimizationBuilder.OptimizationTargetType NXOpen.Optimization.OptimizationBuilder.OptimizationTargetType@endlink) OptimizationType
    ##  Returns the optimization type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return OptimizationBuilder.OptimizationTargetType
    @property
    def OptimizationType(self) -> OptimizationBuilder.OptimizationTargetType:
        """
        Getter for property: (@link OptimizationBuilder.OptimizationTargetType NXOpen.Optimization.OptimizationBuilder.OptimizationTargetType@endlink) OptimizationType
         Returns the optimization type   
            
         
        """
        pass
    
    ## Setter for property: (@link OptimizationBuilder.OptimizationTargetType NXOpen.Optimization.OptimizationBuilder.OptimizationTargetType@endlink) OptimizationType

    ##  Returns the optimization type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @OptimizationType.setter
    def OptimizationType(self, optimizationType: OptimizationBuilder.OptimizationTargetType):
        """
        Setter for property: (@link OptimizationBuilder.OptimizationTargetType NXOpen.Optimization.OptimizationBuilder.OptimizationTargetType@endlink) OptimizationType
         Returns the optimization type   
            
         
        """
        pass
    
    ## Getter for property: (float) RelativeConvergenceCriteria
    ##  Returns the relative criteria for optimizer
    ##             to determine convergence.  
    ##     If one minus
    ##             the ratio of the last two iterations is
    ##             less than this value, the solution is converged   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return float
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
    
    ## Setter for property: (float) RelativeConvergenceCriteria

    ##  Returns the relative criteria for optimizer
    ##             to determine convergence.  
    ##     If one minus
    ##             the ratio of the last two iterations is
    ##             less than this value, the solution is converged   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

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
    
    ## Getter for property: (str) StudyName
    ##  Returns the study name which is unique in one part   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return str
    @property
    def StudyName(self) -> str:
        """
        Getter for property: (str) StudyName
         Returns the study name which is unique in one part   
            
         
        """
        pass
    
    ## Setter for property: (str) StudyName

    ##  Returns the study name which is unique in one part   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @StudyName.setter
    def StudyName(self, studyName: str):
        """
        Setter for property: (str) StudyName
         Returns the study name which is unique in one part   
            
         
        """
        pass
    
    ##  Build all the constraints 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def BuildAllConstraints(self) -> None:
        """
         Build all the constraints 
        """
        pass
    
    ##  Build all the objectives 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def BuildAllObjectives(self) -> None:
        """
         Build all the objectives 
        """
        pass
    
    ##  Build all the variables 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def BuildAllVariables(self) -> None:
        """
         Build all the variables 
        """
        pass
    
    ##  Returns the constraints 
    ##  @return constraints (@link OptimizationBuilder.OptimizationConstraint List[NXOpen.Optimization.OptimizationBuilder.OptimizationConstraint]@endlink):  Constraints .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def GetOptimizationConstraints(self) -> List[OptimizationBuilder.OptimizationConstraint]:
        """
         Returns the constraints 
         @return constraints (@link OptimizationBuilder.OptimizationConstraint List[NXOpen.Optimization.OptimizationBuilder.OptimizationConstraint]@endlink):  Constraints .
        """
        pass
    
    ##  Returns the objectives 
    ##  @return objectives (@link OptimizationBuilder.OptimizationObjective List[NXOpen.Optimization.OptimizationBuilder.OptimizationObjective]@endlink):  Objectives .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def GetOptimizationObjectives(self) -> List[OptimizationBuilder.OptimizationObjective]:
        """
         Returns the objectives 
         @return objectives (@link OptimizationBuilder.OptimizationObjective List[NXOpen.Optimization.OptimizationBuilder.OptimizationObjective]@endlink):  Objectives .
        """
        pass
    
    ##  Returns the variables 
    ##  @return variables (@link OptimizationBuilder.OptimizationVariable List[NXOpen.Optimization.OptimizationBuilder.OptimizationVariable]@endlink):  Variables .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def GetOptimizationVariables(self) -> List[OptimizationBuilder.OptimizationVariable]:
        """
         Returns the variables 
         @return variables (@link OptimizationBuilder.OptimizationVariable List[NXOpen.Optimization.OptimizationBuilder.OptimizationVariable]@endlink):  Variables .
        """
        pass
    
    ##  Remove all the constraints 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def RemoveAllConstraints(self) -> None:
        """
         Remove all the constraints 
        """
        pass
    
    ##  Remove all the objectives 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def RemoveAllObjectives(self) -> None:
        """
         Remove all the objectives 
        """
        pass
    
    ##  Remove all the variables 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def RemoveAllVariables(self) -> None:
        """
         Remove all the variables 
        """
        pass
    
    ##  Run optimization process 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def RunOptimization(self) -> None:
        """
         Run optimization process 
        """
        pass
    
    ##  Sets the constraints 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="attributeNames"> (List[str])  Constraint attribute name array </param>
    ## <param name="attributeObjects"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  Constraint attribute type array </param>
    ## <param name="constraintTypes"> (@link OptimizationBuilder.OptimizationAttributeType List[NXOpen.Optimization.OptimizationBuilder.OptimizationAttributeType]@endlink)  Constraint attribute type array </param>
    ## <param name="constraintLowerLimitValue"> (List[float])  Constraint lower limit value array </param>
    ## <param name="constraintUpperLimitValue"> (List[float])  Constraint upper limit value array </param>
    ## <param name="constraintLimitType"> (@link OptimizationBuilder.OptimizationConstraintLimitType List[NXOpen.Optimization.OptimizationBuilder.OptimizationConstraintLimitType]@endlink)  Constraint atribute limit type array </param>
    def SetOptimizationConstraints(self, attributeNames: List[str], attributeObjects: List[NXOpen.NXObject], constraintTypes: List[OptimizationBuilder.OptimizationAttributeType], constraintLowerLimitValue: List[float], constraintUpperLimitValue: List[float], constraintLimitType: List[OptimizationBuilder.OptimizationConstraintLimitType]) -> None:
        """
         Sets the constraints 
        """
        pass
    
    ##  Sets the objectives 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="attributeNames"> (List[str])  Objective attribute name array </param>
    ## <param name="attributeObjects"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  Objective attribute object array </param>
    ## <param name="objectiveTypes"> (@link OptimizationBuilder.OptimizationAttributeType List[NXOpen.Optimization.OptimizationBuilder.OptimizationAttributeType]@endlink)  Objective attribute type array </param>
    ## <param name="objectiveTargetValues"> (List[float])  Objective target value array </param>
    def SetOptimizationObjectives(self, attributeNames: List[str], attributeObjects: List[NXOpen.NXObject], objectiveTypes: List[OptimizationBuilder.OptimizationAttributeType], objectiveTargetValues: List[float]) -> None:
        """
         Sets the objectives 
        """
        pass
    
    ##  Sets the variables 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="attributeNames"> (List[str])  Variable attribute name array </param>
    ## <param name="attributeObjects"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  Variable attribute object array </param>
    ## <param name="variableTypes"> (@link OptimizationBuilder.OptimizationAttributeType List[NXOpen.Optimization.OptimizationBuilder.OptimizationAttributeType]@endlink)  Variable attribute type array </param>
    ## <param name="variableLowerLimitValue"> (List[float])  Variable lower limit value array </param>
    ## <param name="variableUpperLimitValue"> (List[float])  Variable upper limit value array </param>
    def SetOptimizationVariables(self, attributeNames: List[str], attributeObjects: List[NXOpen.NXObject], variableTypes: List[OptimizationBuilder.OptimizationAttributeType], variableLowerLimitValue: List[float], variableUpperLimitValue: List[float]) -> None:
        """
         Sets the variables 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Optimization::OptimizationCollection NXOpen::Optimization::OptimizationCollection@endlink   <br> To obtain an instance of this class, refer to @link NXOpen::BasePart  NXOpen::BasePart @endlink  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class OptimizationCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a <ja_class>NXOpen.Optimization.OptimizationCollection</ja_class> """


    ##  Create builder for MapleExpBuilder class 
    ##  @return builder (@link MapleExpBuilder NXOpen.Optimization.MapleExpBuilder@endlink): .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.0.  Use @link NXOpen::Optimization::OptimizationCollection::CreateMathIntegrationExpBuilder NXOpen::Optimization::OptimizationCollection::CreateMathIntegrationExpBuilder@endlink  instead.  <br> 

    ## License requirements: None.
    def CreateMapleExpBuilder(self) -> MapleExpBuilder:
        """
         Create builder for MapleExpBuilder class 
         @return builder (@link MapleExpBuilder NXOpen.Optimization.MapleExpBuilder@endlink): .
        """
        pass
    
    ##  Create builder for MathIntegrationExpBuilder class 
    ##  @return builder (@link MathIntegrationExpBuilder NXOpen.Optimization.MathIntegrationExpBuilder@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    def CreateMathIntegrationExpBuilder(self) -> MathIntegrationExpBuilder:
        """
         Create builder for MathIntegrationExpBuilder class 
         @return builder (@link MathIntegrationExpBuilder NXOpen.Optimization.MathIntegrationExpBuilder@endlink): .
        """
        pass
    
    ##  Create builder for OptimizationAttribute class 
    ##  @return builder (@link OptimizationAttributeBuilder NXOpen.Optimization.OptimizationAttributeBuilder@endlink): .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def CreateOptimizationAttributeBuilder(self) -> OptimizationAttributeBuilder:
        """
         Create builder for OptimizationAttribute class 
         @return builder (@link OptimizationAttributeBuilder NXOpen.Optimization.OptimizationAttributeBuilder@endlink): .
        """
        pass
    
    ##  Create builder for optimization class 
    ##  @return builder (@link OptimizationBuilder NXOpen.Optimization.OptimizationBuilder@endlink): .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def CreateOptimizationBuilder(self) -> OptimizationBuilder:
        """
         Create builder for optimization class 
         @return builder (@link OptimizationBuilder NXOpen.Optimization.OptimizationBuilder@endlink): .
        """
        pass
    
## @package NXOpen.Optimization
## Classes, Enums and Structs under NXOpen.Optimization namespace

##  @link DesignStudyBuilderDesignStudyAttributeType NXOpen.Optimization.DesignStudyBuilderDesignStudyAttributeType @endlink is an alias for @link DesignStudyBuilder.DesignStudyAttributeType NXOpen.Optimization.DesignStudyBuilder.DesignStudyAttributeType@endlink
DesignStudyBuilderDesignStudyAttributeType = DesignStudyBuilder.DesignStudyAttributeType


##  @link DesignStudyBuilderDesignStudyConstraintLimitType NXOpen.Optimization.DesignStudyBuilderDesignStudyConstraintLimitType @endlink is an alias for @link DesignStudyBuilder.DesignStudyConstraintLimitType NXOpen.Optimization.DesignStudyBuilder.DesignStudyConstraintLimitType@endlink
DesignStudyBuilderDesignStudyConstraintLimitType = DesignStudyBuilder.DesignStudyConstraintLimitType


##  @link DesignStudyBuilderDesignStudyDistributeType NXOpen.Optimization.DesignStudyBuilderDesignStudyDistributeType @endlink is an alias for @link DesignStudyBuilder.DesignStudyDistributeType NXOpen.Optimization.DesignStudyBuilder.DesignStudyDistributeType@endlink
DesignStudyBuilderDesignStudyDistributeType = DesignStudyBuilder.DesignStudyDistributeType


## @link DesignStudyBuilderDesignStudyObjective_Struct NXOpen.Optimization.DesignStudyBuilderDesignStudyObjective_Struct@endlink is an alias for @link DesignStudyBuilder.DesignStudyObjective NXOpen.Optimization.DesignStudyBuilder.DesignStudyObjective@endlink.
DesignStudyBuilderDesignStudyObjective_Struct = DesignStudyBuilder.DesignStudyObjective


## @link DesignStudyBuilderDesignStudyVariable_Struct NXOpen.Optimization.DesignStudyBuilderDesignStudyVariable_Struct@endlink is an alias for @link DesignStudyBuilder.DesignStudyVariable NXOpen.Optimization.DesignStudyBuilder.DesignStudyVariable@endlink.
DesignStudyBuilderDesignStudyVariable_Struct = DesignStudyBuilder.DesignStudyVariable


##  @link OptimizationBuilderOptimizationAlgorithmType NXOpen.Optimization.OptimizationBuilderOptimizationAlgorithmType @endlink is an alias for @link OptimizationBuilder.OptimizationAlgorithmType NXOpen.Optimization.OptimizationBuilder.OptimizationAlgorithmType@endlink
OptimizationBuilderOptimizationAlgorithmType = OptimizationBuilder.OptimizationAlgorithmType


##  @link OptimizationBuilderOptimizationAttributeType NXOpen.Optimization.OptimizationBuilderOptimizationAttributeType @endlink is an alias for @link OptimizationBuilder.OptimizationAttributeType NXOpen.Optimization.OptimizationBuilder.OptimizationAttributeType@endlink
OptimizationBuilderOptimizationAttributeType = OptimizationBuilder.OptimizationAttributeType


##  @link OptimizationBuilderOptimizationConstraintLimitType NXOpen.Optimization.OptimizationBuilderOptimizationConstraintLimitType @endlink is an alias for @link OptimizationBuilder.OptimizationConstraintLimitType NXOpen.Optimization.OptimizationBuilder.OptimizationConstraintLimitType@endlink
OptimizationBuilderOptimizationConstraintLimitType = OptimizationBuilder.OptimizationConstraintLimitType


## @link OptimizationBuilderOptimizationConstraint_Struct NXOpen.Optimization.OptimizationBuilderOptimizationConstraint_Struct@endlink is an alias for @link OptimizationBuilder.OptimizationConstraint NXOpen.Optimization.OptimizationBuilder.OptimizationConstraint@endlink.
OptimizationBuilderOptimizationConstraint_Struct = OptimizationBuilder.OptimizationConstraint


##  @link OptimizationBuilderOptimizationConvergenceSpeedType NXOpen.Optimization.OptimizationBuilderOptimizationConvergenceSpeedType @endlink is an alias for @link OptimizationBuilder.OptimizationConvergenceSpeedType NXOpen.Optimization.OptimizationBuilder.OptimizationConvergenceSpeedType@endlink
OptimizationBuilderOptimizationConvergenceSpeedType = OptimizationBuilder.OptimizationConvergenceSpeedType


## @link OptimizationBuilderOptimizationObjective_Struct NXOpen.Optimization.OptimizationBuilderOptimizationObjective_Struct@endlink is an alias for @link OptimizationBuilder.OptimizationObjective NXOpen.Optimization.OptimizationBuilder.OptimizationObjective@endlink.
OptimizationBuilderOptimizationObjective_Struct = OptimizationBuilder.OptimizationObjective


##  @link OptimizationBuilderOptimizationTargetType NXOpen.Optimization.OptimizationBuilderOptimizationTargetType @endlink is an alias for @link OptimizationBuilder.OptimizationTargetType NXOpen.Optimization.OptimizationBuilder.OptimizationTargetType@endlink
OptimizationBuilderOptimizationTargetType = OptimizationBuilder.OptimizationTargetType


## @link OptimizationBuilderOptimizationVariable_Struct NXOpen.Optimization.OptimizationBuilderOptimizationVariable_Struct@endlink is an alias for @link OptimizationBuilder.OptimizationVariable NXOpen.Optimization.OptimizationBuilder.OptimizationVariable@endlink.
OptimizationBuilderOptimizationVariable_Struct = OptimizationBuilder.OptimizationVariable


