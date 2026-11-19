from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  A Classifier within a @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
##     
## 
##   <br>  Created in NX8.0.0  <br> 

class Classifier(NXOpen.NXObject): 
    """ A Classifier within a <ja_class>NXOpen.VisualReporting.Rule</ja_class>.
    """


    ##  Represents the possible date grouping method options.
    ##             for a @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink .
    ##         
    ##  The date grouping by day will be used 
    class DateGroupMethodOption(Enum):
        """
        Members Include: <Day> <Week> <Month> <Year>
        """
        Day: int
        Week: int
        Month: int
        Year: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Classifier.DateGroupMethodOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the possible grouping method options.
    ##             for a @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink .
    ##         
    ##  Grouping is manual 
    class GroupingMethodOption(Enum):
        """
        Members Include: <Manual> <Automatic> <SemiAutomatic>
        """
        Manual: int
        Automatic: int
        SemiAutomatic: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Classifier.GroupingMethodOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the possible range method options.
    ##             for a @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink .
    ##         
    ##  A numeric range will be used 
    class RangeMethodOption(Enum):
        """
        Members Include: <Number> <Percentage>
        """
        Number: int
        Percentage: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Classifier.RangeMethodOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the possible type options.
    ##              for a @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink .
    ##         
    ##  Simple classifier type 
    class TypeOption(Enum):
        """
        Members Include: <Simple> <Value> <Range>
        """
        Simple: int
        Value: int
        Range: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Classifier.TypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
import NXOpen
##  A Condition within a @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
##     
## 
##   <br>  Created in NX7.0.0  <br> 

class Condition(NXOpen.NXObject): 
    """ A Condition within a <ja_class>NXOpen.VisualReporting.Rule</ja_class>.
    """


    ##  Represents the possible operator type options.
    ##            for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .
    ##         
    ##   
    class OperatorOption(Enum):
        """
        Members Include: <EqualOperator> <LessThanOperator> <NotLessThanOperator> <GreaterThanOperator> <NotGreaterThanOperator> <NotEqualOperator> <RegularExpressionOperator> <ContainsOperator> <DoesNotContainOperator> <OnOrBeforeOperator> <OnOrAfterOperator>
        """
        EqualOperator: int
        LessThanOperator: int
        NotLessThanOperator: int
        GreaterThanOperator: int
        NotGreaterThanOperator: int
        NotEqualOperator: int
        RegularExpressionOperator: int
        ContainsOperator: int
        DoesNotContainOperator: int
        OnOrBeforeOperator: int
        OnOrAfterOperator: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Condition.OperatorOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the possible type options
    ##            for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink . If the type is a
    ##            @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
    ##            the type of value can be found from @link NXOpen::VisualReporting::Condition::Datatype NXOpen::VisualReporting::Condition::Datatype@endlink .
    ##         
    ##   
    class TypeOption(Enum):
        """
        Members Include: <AndCondition> <OrCondition> <NotCondition> <ValueCondition>
        """
        AndCondition: int
        OrCondition: int
        NotCondition: int
        ValueCondition: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Condition.TypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link Property.DatatypeOption NXOpen.VisualReporting.Property.DatatypeOption@endlink) Datatype
    ##   the @link NXOpen::VisualReporting::Property::DatatypeOption NXOpen::VisualReporting::Property::DatatypeOption@endlink  of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .  
    ##   
    ## 
    ##             The returned data type will never be
    ##             @link NXOpen::VisualReporting::Property::DatatypeOptionUnknown NXOpen::VisualReporting::Property::DatatypeOptionUnknown@endlink .
    ##         
    ##             Note that this @link NXOpen::VisualReporting::Condition::Datatype NXOpen::VisualReporting::Condition::Datatype@endlink  cannot be modified. 
    ##             Instead it is specified when creating this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  by using the appropriate function:
    ##              - @link NXOpen::VisualReporting::VisualReportBuilder::CreateStringCondition NXOpen::VisualReporting::VisualReportBuilder::CreateStringCondition@endlink 
    ##              - @link NXOpen::VisualReporting::VisualReportBuilder::CreateIntegerCondition NXOpen::VisualReporting::VisualReportBuilder::CreateIntegerCondition@endlink 
    ##              - @link NXOpen::VisualReporting::VisualReportBuilder::CreateRealCondition NXOpen::VisualReporting::VisualReportBuilder::CreateRealCondition@endlink 
    ##              - @link NXOpen::VisualReporting::VisualReportBuilder::CreateBooleanCondition NXOpen::VisualReporting::VisualReportBuilder::CreateBooleanCondition@endlink 
    ## 
    ##             Note that the @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink s created using the following functions do not
    ##             have @link NXOpen::VisualReporting::Property::DatatypeOption NXOpen::VisualReporting::Property::DatatypeOption@endlink s and calling this function will cause an error for these:
    ##              - @link NXOpen::VisualReporting::VisualReportBuilder::CreateAndCondition NXOpen::VisualReporting::VisualReportBuilder::CreateAndCondition@endlink 
    ##              - @link NXOpen::VisualReporting::VisualReportBuilder::CreateOrCondition NXOpen::VisualReporting::VisualReportBuilder::CreateOrCondition@endlink 
    ##              - @link NXOpen::VisualReporting::VisualReportBuilder::CreateNotCondition NXOpen::VisualReporting::VisualReportBuilder::CreateNotCondition@endlink 
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return Property.DatatypeOption
    @property
    def Datatype(self) -> Property.DatatypeOption:
        """
        Getter for property: (@link Property.DatatypeOption NXOpen.VisualReporting.Property.DatatypeOption@endlink) Datatype
          the @link NXOpen::VisualReporting::Property::DatatypeOption NXOpen::VisualReporting::Property::DatatypeOption@endlink  of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .  
          
        
                    The returned data type will never be
                    @link NXOpen::VisualReporting::Property::DatatypeOptionUnknown NXOpen::VisualReporting::Property::DatatypeOptionUnknown@endlink .
                
                    Note that this @link NXOpen::VisualReporting::Condition::Datatype NXOpen::VisualReporting::Condition::Datatype@endlink  cannot be modified. 
                    Instead it is specified when creating this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  by using the appropriate function:
                     - @link NXOpen::VisualReporting::VisualReportBuilder::CreateStringCondition NXOpen::VisualReporting::VisualReportBuilder::CreateStringCondition@endlink 
                     - @link NXOpen::VisualReporting::VisualReportBuilder::CreateIntegerCondition NXOpen::VisualReporting::VisualReportBuilder::CreateIntegerCondition@endlink 
                     - @link NXOpen::VisualReporting::VisualReportBuilder::CreateRealCondition NXOpen::VisualReporting::VisualReportBuilder::CreateRealCondition@endlink 
                     - @link NXOpen::VisualReporting::VisualReportBuilder::CreateBooleanCondition NXOpen::VisualReporting::VisualReportBuilder::CreateBooleanCondition@endlink 
        
                    Note that the @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink s created using the following functions do not
                    have @link NXOpen::VisualReporting::Property::DatatypeOption NXOpen::VisualReporting::Property::DatatypeOption@endlink s and calling this function will cause an error for these:
                     - @link NXOpen::VisualReporting::VisualReportBuilder::CreateAndCondition NXOpen::VisualReporting::VisualReportBuilder::CreateAndCondition@endlink 
                     - @link NXOpen::VisualReporting::VisualReportBuilder::CreateOrCondition NXOpen::VisualReporting::VisualReportBuilder::CreateOrCondition@endlink 
                     - @link NXOpen::VisualReporting::VisualReportBuilder::CreateNotCondition NXOpen::VisualReporting::VisualReportBuilder::CreateNotCondition@endlink 
                  
         
        """
        pass
    
    ## Getter for property: (str) Description
    ##   the description for this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .  
    ##   
    ##             Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
    ##             @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return str
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
          the description for this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .  
          
                    Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                    @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                  
         
        """
        pass
    
    ## Setter for property: (str) Description

    ##   the description for this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .  
    ##   
    ##             Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
    ##             @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
    ##           
    ##  
    ## Setter License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
          the description for this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .  
          
                    Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                    @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                  
         
        """
        pass
    
    ## Getter for property: (bool) HasUserSpecifiedValue
    ##   whether this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  requires user input.  
    ##   
    ##             Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
    ##             @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return bool
    @property
    def HasUserSpecifiedValue(self) -> bool:
        """
        Getter for property: (bool) HasUserSpecifiedValue
          whether this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  requires user input.  
          
                    Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                    @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                  
         
        """
        pass
    
    ## Setter for property: (bool) HasUserSpecifiedValue

    ##   whether this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  requires user input.  
    ##   
    ##             Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
    ##             @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
    ##           
    ##  
    ## Setter License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @HasUserSpecifiedValue.setter
    def HasUserSpecifiedValue(self, isUserSpecified: bool):
        """
        Setter for property: (bool) HasUserSpecifiedValue
          whether this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  requires user input.  
          
                    Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                    @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                  
         
        """
        pass
    
    ## Getter for property: (@link Condition.OperatorOption NXOpen.VisualReporting.Condition.OperatorOption@endlink) OperatorType
    ##   the @link NXOpen::VisualReporting::Condition::OperatorOption NXOpen::VisualReporting::Condition::OperatorOption@endlink  of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .  
    ##    
    ##             Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
    ##             @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return Condition.OperatorOption
    @property
    def OperatorType(self) -> Condition.OperatorOption:
        """
        Getter for property: (@link Condition.OperatorOption NXOpen.VisualReporting.Condition.OperatorOption@endlink) OperatorType
          the @link NXOpen::VisualReporting::Condition::OperatorOption NXOpen::VisualReporting::Condition::OperatorOption@endlink  of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .  
           
                    Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                    @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                  
         
        """
        pass
    
    ## Setter for property: (@link Condition.OperatorOption NXOpen.VisualReporting.Condition.OperatorOption@endlink) OperatorType

    ##   the @link NXOpen::VisualReporting::Condition::OperatorOption NXOpen::VisualReporting::Condition::OperatorOption@endlink  of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .  
    ##    
    ##             Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
    ##             @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
    ##           
    ##  
    ## Setter License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @OperatorType.setter
    def OperatorType(self, operatorType: Condition.OperatorOption):
        """
        Setter for property: (@link Condition.OperatorOption NXOpen.VisualReporting.Condition.OperatorOption@endlink) OperatorType
          the @link NXOpen::VisualReporting::Condition::OperatorOption NXOpen::VisualReporting::Condition::OperatorOption@endlink  of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .  
           
                    Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                    @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                  
         
        """
        pass
    
    ## Getter for property: (@link Condition NXOpen.VisualReporting.Condition@endlink) ParentCondition
    ##   the parent condition of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .  
    ##    If this
    ##             condition has no parent or if the parent isn't a condition
    ##             then this returns NULL.
    ## 
    ##             Note that this @link NXOpen::VisualReporting::Condition::ParentCondition NXOpen::VisualReporting::Condition::ParentCondition@endlink  cannot be modified. 
    ##             Instead it is determined when inserting this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  in the @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink 
    ##             by using the appropriate function:
    ##              - @link NXOpen::VisualReporting::VisualReportBuilder::SetFilterConditionOfRule NXOpen::VisualReporting::VisualReportBuilder::SetFilterConditionOfRule@endlink 
    ##              - @link NXOpen::VisualReporting::VisualReportBuilder::AddChildToCondition NXOpen::VisualReporting::VisualReportBuilder::AddChildToCondition@endlink 
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return Condition
    @property
    def ParentCondition(self) -> Condition:
        """
        Getter for property: (@link Condition NXOpen.VisualReporting.Condition@endlink) ParentCondition
          the parent condition of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .  
           If this
                    condition has no parent or if the parent isn't a condition
                    then this returns NULL.
        
                    Note that this @link NXOpen::VisualReporting::Condition::ParentCondition NXOpen::VisualReporting::Condition::ParentCondition@endlink  cannot be modified. 
                    Instead it is determined when inserting this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  in the @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink 
                    by using the appropriate function:
                     - @link NXOpen::VisualReporting::VisualReportBuilder::SetFilterConditionOfRule NXOpen::VisualReporting::VisualReportBuilder::SetFilterConditionOfRule@endlink 
                     - @link NXOpen::VisualReporting::VisualReportBuilder::AddChildToCondition NXOpen::VisualReporting::VisualReportBuilder::AddChildToCondition@endlink 
                  
         
        """
        pass
    
    ## Getter for property: (@link Property NXOpen.VisualReporting.Property@endlink) Property
    ##   the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .  
    ##    If the
    ##             @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  is set to NULL, then it is
    ##             deleted.
    ##             Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
    ##             @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return Property
    @property
    def Property(self) -> Property:
        """
        Getter for property: (@link Property NXOpen.VisualReporting.Property@endlink) Property
          the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .  
           If the
                    @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  is set to NULL, then it is
                    deleted.
                    Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                    @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                  
         
        """
        pass
    
    ## Setter for property: (@link Property NXOpen.VisualReporting.Property@endlink) Property

    ##   the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .  
    ##    If the
    ##             @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  is set to NULL, then it is
    ##             deleted.
    ##             Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
    ##             @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
    ##           
    ##  
    ## Setter License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @Property.setter
    def Property(self, property: Property):
        """
        Setter for property: (@link Property NXOpen.VisualReporting.Property@endlink) Property
          the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .  
           If the
                    @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  is set to NULL, then it is
                    deleted.
                    Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                    @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                  
         
        """
        pass
    
    ## Getter for property: (@link Condition.TypeOption NXOpen.VisualReporting.Condition.TypeOption@endlink) Type
    ##   the @link NXOpen::VisualReporting::Condition::TypeOption NXOpen::VisualReporting::Condition::TypeOption@endlink  of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink 
    ##   
    ##   
    ##             Note that this @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  cannot be modified. 
    ##             Instead it is determined when creating this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  by using the appropriate function:
    ##              - @link NXOpen::VisualReporting::VisualReportBuilder::CreateStringCondition NXOpen::VisualReporting::VisualReportBuilder::CreateStringCondition@endlink 
    ##              - @link NXOpen::VisualReporting::VisualReportBuilder::CreateIntegerCondition NXOpen::VisualReporting::VisualReportBuilder::CreateIntegerCondition@endlink 
    ##              - @link NXOpen::VisualReporting::VisualReportBuilder::CreateRealCondition NXOpen::VisualReporting::VisualReportBuilder::CreateRealCondition@endlink 
    ##              - @link NXOpen::VisualReporting::VisualReportBuilder::CreateBooleanCondition NXOpen::VisualReporting::VisualReportBuilder::CreateBooleanCondition@endlink 
    ##              - @link NXOpen::VisualReporting::VisualReportBuilder::CreateAndCondition NXOpen::VisualReporting::VisualReportBuilder::CreateAndCondition@endlink 
    ##              - @link NXOpen::VisualReporting::VisualReportBuilder::CreateOrCondition NXOpen::VisualReporting::VisualReportBuilder::CreateOrCondition@endlink 
    ##              - @link NXOpen::VisualReporting::VisualReportBuilder::CreateNotCondition NXOpen::VisualReporting::VisualReportBuilder::CreateNotCondition@endlink 
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return Condition.TypeOption
    @property
    def Type(self) -> Condition.TypeOption:
        """
        Getter for property: (@link Condition.TypeOption NXOpen.VisualReporting.Condition.TypeOption@endlink) Type
          the @link NXOpen::VisualReporting::Condition::TypeOption NXOpen::VisualReporting::Condition::TypeOption@endlink  of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink 
          
          
                    Note that this @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  cannot be modified. 
                    Instead it is determined when creating this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  by using the appropriate function:
                     - @link NXOpen::VisualReporting::VisualReportBuilder::CreateStringCondition NXOpen::VisualReporting::VisualReportBuilder::CreateStringCondition@endlink 
                     - @link NXOpen::VisualReporting::VisualReportBuilder::CreateIntegerCondition NXOpen::VisualReporting::VisualReportBuilder::CreateIntegerCondition@endlink 
                     - @link NXOpen::VisualReporting::VisualReportBuilder::CreateRealCondition NXOpen::VisualReporting::VisualReportBuilder::CreateRealCondition@endlink 
                     - @link NXOpen::VisualReporting::VisualReportBuilder::CreateBooleanCondition NXOpen::VisualReporting::VisualReportBuilder::CreateBooleanCondition@endlink 
                     - @link NXOpen::VisualReporting::VisualReportBuilder::CreateAndCondition NXOpen::VisualReporting::VisualReportBuilder::CreateAndCondition@endlink 
                     - @link NXOpen::VisualReporting::VisualReportBuilder::CreateOrCondition NXOpen::VisualReporting::VisualReportBuilder::CreateOrCondition@endlink 
                     - @link NXOpen::VisualReporting::VisualReportBuilder::CreateNotCondition NXOpen::VisualReporting::VisualReportBuilder::CreateNotCondition@endlink 
                  
         
        """
        pass
    
    ## Getter for property: (str) UserPrompt
    ##   the user prompt for this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .  
    ##    Only useful for a condition where
    ##             @link NXOpen::VisualReporting::Condition::HasUserSpecifiedValue NXOpen::VisualReporting::Condition::HasUserSpecifiedValue@endlink  is true.
    ##             Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
    ##             @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return str
    @property
    def UserPrompt(self) -> str:
        """
        Getter for property: (str) UserPrompt
          the user prompt for this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .  
           Only useful for a condition where
                    @link NXOpen::VisualReporting::Condition::HasUserSpecifiedValue NXOpen::VisualReporting::Condition::HasUserSpecifiedValue@endlink  is true.
                    Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                    @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                  
         
        """
        pass
    
    ## Setter for property: (str) UserPrompt

    ##   the user prompt for this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .  
    ##    Only useful for a condition where
    ##             @link NXOpen::VisualReporting::Condition::HasUserSpecifiedValue NXOpen::VisualReporting::Condition::HasUserSpecifiedValue@endlink  is true.
    ##             Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
    ##             @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
    ##           
    ##  
    ## Setter License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @UserPrompt.setter
    def UserPrompt(self, userPrompt: str):
        """
        Setter for property: (str) UserPrompt
          the user prompt for this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .  
           Only useful for a condition where
                    @link NXOpen::VisualReporting::Condition::HasUserSpecifiedValue NXOpen::VisualReporting::Condition::HasUserSpecifiedValue@endlink  is true.
                    Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                    @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                  
         
        """
        pass
    
    ## Getter for property: (str) Value
    ##   the value of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .  
    ##    
    ##             Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
    ##             @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def Value(self) -> str:
        """
        Getter for property: (str) Value
          the value of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .  
           
                    Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                    @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                  
         
        """
        pass
    
    ## Setter for property: (str) Value

    ##   the value of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .  
    ##    
    ##             Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
    ##             @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
    ##           
    ##  
    ## Setter License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @Value.setter
    def Value(self, conditionValue: str):
        """
        Setter for property: (str) Value
          the value of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .  
           
                    Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                    @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                  
         
        """
        pass
    
    ##  Return the specified child Condition from this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink 
    ##         
    ##  @return childCondition (@link Condition NXOpen.VisualReporting.Condition@endlink): .
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    ##  The index of the returned Condition. 
    def GetChildCondition(condition: Condition, index: int) -> Condition:
        """
         Return the specified child Condition from this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink 
                
         @return childCondition (@link Condition NXOpen.VisualReporting.Condition@endlink): .
        """
        pass
    
    ##  Returns all the child Conditions in this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink 
    ##         
    ##  @return childConditions (@link Condition List[NXOpen.VisualReporting.Condition]@endlink): .
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetChildConditions(condition: Condition) -> List[Condition]:
        """
         Returns all the child Conditions in this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink 
                
         @return childConditions (@link Condition List[NXOpen.VisualReporting.Condition]@endlink): .
        """
        pass
    
    ##  Returns whether the given @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  is an immediate child of this condition
    ##         
    ##  @return isChild (bool): .
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    ##  The possible child Condition 
    def IsChildCondition(condition: Condition, childCondition: Condition) -> bool:
        """
         Returns whether the given @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  is an immediate child of this condition
                
         @return isChild (bool): .
        """
        pass
    
import NXOpen
## 
##         A group label corresponds to a group of objects in the results of an applied 
##         @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
##     
## 
##   <br>  Created in NX7.0.0  <br> 

class GroupLabel(NXOpen.NXObject): 
    """
        A group label corresponds to a group of objects in the results of an applied 
        <ja_class>NXOpen.VisualReporting.VisualReport</ja_class>.
    """


    ##  Represents the possible display style options
    ##             for a @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
    ##         
    ##  Matching objects will be de-emphasized 
    class DisplayStyleOption(Enum):
        """
        Members Include: <DeEmphasis> <SpecifiedColor> <OriginalColor> <AutomaticColor>
        """
        DeEmphasis: int
        SpecifiedColor: int
        OriginalColor: int
        AutomaticColor: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> GroupLabel.DisplayStyleOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the possible priority options
    ##             for a @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
    ##         
    ##  Low priority 
    class TagPriorityOption(Enum):
        """
        Members Include: <Low> <Medium> <High>
        """
        Low: int
        Medium: int
        High: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> GroupLabel.TagPriorityOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) BitmapName
    ##   the bitmap name of this @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def BitmapName(self) -> str:
        """
        Getter for property: (str) BitmapName
          the bitmap name of this @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .  
          
                  
         
        """
        pass
    
    ## Setter for property: (str) BitmapName

    ##   the bitmap name of this @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .  
    ##   
    ##           
    ##  
    ## Setter License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @BitmapName.setter
    def BitmapName(self, bitmapName: str):
        """
        Setter for property: (str) BitmapName
          the bitmap name of this @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .  
          
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor.Rgb NXOpen.NXColor.Rgb@endlink) Color
    ##   the color of the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return NXOpen.NXColor.Rgb
    @property
    def Color(self) -> NXOpen.NXColor.Rgb:
        """
        Getter for property: (@link NXOpen.NXColor.Rgb NXOpen.NXColor.Rgb@endlink) Color
          the color of the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink    
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor.Rgb NXOpen.NXColor.Rgb@endlink) Color

    ##   the color of the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink    
    ##     
    ##  
    ## Setter License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @Color.setter
    def Color(self, color: NXOpen.NXColor.Rgb):
        """
        Setter for property: (@link NXOpen.NXColor.Rgb NXOpen.NXColor.Rgb@endlink) Color
          the color of the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink    
            
         
        """
        pass
    
    ## Getter for property: (str) CustomMessage
    ##   the custom message of this @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def CustomMessage(self) -> str:
        """
        Getter for property: (str) CustomMessage
          the custom message of this @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .  
          
                  
         
        """
        pass
    
    ## Setter for property: (str) CustomMessage

    ##   the custom message of this @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .  
    ##   
    ##           
    ##  
    ## Setter License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @CustomMessage.setter
    def CustomMessage(self, customMessage: str):
        """
        Setter for property: (str) CustomMessage
          the custom message of this @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .  
          
                  
         
        """
        pass
    
    ## Getter for property: (@link GroupLabel.DisplayStyleOption NXOpen.VisualReporting.GroupLabel.DisplayStyleOption@endlink) DisplayStyle
    ##   the @link NXOpen::VisualReporting::GroupLabel::DisplayStyleOption NXOpen::VisualReporting::GroupLabel::DisplayStyleOption@endlink  of the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return GroupLabel.DisplayStyleOption
    @property
    def DisplayStyle(self) -> GroupLabel.DisplayStyleOption:
        """
        Getter for property: (@link GroupLabel.DisplayStyleOption NXOpen.VisualReporting.GroupLabel.DisplayStyleOption@endlink) DisplayStyle
          the @link NXOpen::VisualReporting::GroupLabel::DisplayStyleOption NXOpen::VisualReporting::GroupLabel::DisplayStyleOption@endlink  of the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink    
            
         
        """
        pass
    
    ## Setter for property: (@link GroupLabel.DisplayStyleOption NXOpen.VisualReporting.GroupLabel.DisplayStyleOption@endlink) DisplayStyle

    ##   the @link NXOpen::VisualReporting::GroupLabel::DisplayStyleOption NXOpen::VisualReporting::GroupLabel::DisplayStyleOption@endlink  of the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink    
    ##     
    ##  
    ## Setter License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @DisplayStyle.setter
    def DisplayStyle(self, displayStyle: GroupLabel.DisplayStyleOption):
        """
        Setter for property: (@link GroupLabel.DisplayStyleOption NXOpen.VisualReporting.GroupLabel.DisplayStyleOption@endlink) DisplayStyle
          the @link NXOpen::VisualReporting::GroupLabel::DisplayStyleOption NXOpen::VisualReporting::GroupLabel::DisplayStyleOption@endlink  of the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Validation.Result NXOpen.Validation.Result@endlink) ErrorLevel
    ##   the Error Level of this @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return NXOpen.Validation.Result
    @property
    def ErrorLevel(self) -> NXOpen.Validation.Result:
        """
        Getter for property: (@link NXOpen.Validation.Result NXOpen.Validation.Result@endlink) ErrorLevel
          the Error Level of this @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Validation.Result NXOpen.Validation.Result@endlink) ErrorLevel

    ##   the Error Level of this @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .  
    ##      
    ##  
    ## Setter License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @ErrorLevel.setter
    def ErrorLevel(self, errorLevel: NXOpen.Validation.Result):
        """
        Setter for property: (@link NXOpen.Validation.Result NXOpen.Validation.Result@endlink) ErrorLevel
          the Error Level of this @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .  
             
         
        """
        pass
    
    ## Getter for property: (bool) IsManual
    ##   whether the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  is manual.  
    ##    It is manual if it either has a user-specified
    ##             @link NXOpen::NXObject::Name NXOpen::NXObject::Name@endlink  or if its @link NXOpen::VisualReporting::GroupLabel::DisplayStyle NXOpen::VisualReporting::GroupLabel::DisplayStyle@endlink  is
    ##             not @link NXOpen::VisualReporting::GroupLabel::DisplayStyleOptionAutomaticColor NXOpen::VisualReporting::GroupLabel::DisplayStyleOptionAutomaticColor@endlink .
    ##             You can change a @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  from automatic to manual, but you cannot 
    ##             change @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  from manual to automatic.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return bool
    @property
    def IsManual(self) -> bool:
        """
        Getter for property: (bool) IsManual
          whether the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  is manual.  
           It is manual if it either has a user-specified
                    @link NXOpen::NXObject::Name NXOpen::NXObject::Name@endlink  or if its @link NXOpen::VisualReporting::GroupLabel::DisplayStyle NXOpen::VisualReporting::GroupLabel::DisplayStyle@endlink  is
                    not @link NXOpen::VisualReporting::GroupLabel::DisplayStyleOptionAutomaticColor NXOpen::VisualReporting::GroupLabel::DisplayStyleOptionAutomaticColor@endlink .
                    You can change a @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  from automatic to manual, but you cannot 
                    change @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  from manual to automatic.
                  
         
        """
        pass
    
    ## Setter for property: (bool) IsManual

    ##   whether the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  is manual.  
    ##    It is manual if it either has a user-specified
    ##             @link NXOpen::NXObject::Name NXOpen::NXObject::Name@endlink  or if its @link NXOpen::VisualReporting::GroupLabel::DisplayStyle NXOpen::VisualReporting::GroupLabel::DisplayStyle@endlink  is
    ##             not @link NXOpen::VisualReporting::GroupLabel::DisplayStyleOptionAutomaticColor NXOpen::VisualReporting::GroupLabel::DisplayStyleOptionAutomaticColor@endlink .
    ##             You can change a @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  from automatic to manual, but you cannot 
    ##             change @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  from manual to automatic.
    ##           
    ##  
    ## Setter License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @IsManual.setter
    def IsManual(self, isManual: bool):
        """
        Setter for property: (bool) IsManual
          whether the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  is manual.  
           It is manual if it either has a user-specified
                    @link NXOpen::NXObject::Name NXOpen::NXObject::Name@endlink  or if its @link NXOpen::VisualReporting::GroupLabel::DisplayStyle NXOpen::VisualReporting::GroupLabel::DisplayStyle@endlink  is
                    not @link NXOpen::VisualReporting::GroupLabel::DisplayStyleOptionAutomaticColor NXOpen::VisualReporting::GroupLabel::DisplayStyleOptionAutomaticColor@endlink .
                    You can change a @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  from automatic to manual, but you cannot 
                    change @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  from manual to automatic.
                  
         
        """
        pass
    
    ## Getter for property: (bool) IsNameUserSpecified
    ##   whether the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  has a user-specified @link NXOpen::NXObject::Name NXOpen::NXObject::Name@endlink .  
    ##    If it isn't
    ##             user-specified, then the system will generate its name automatically.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return bool
    @property
    def IsNameUserSpecified(self) -> bool:
        """
        Getter for property: (bool) IsNameUserSpecified
          whether the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  has a user-specified @link NXOpen::NXObject::Name NXOpen::NXObject::Name@endlink .  
           If it isn't
                    user-specified, then the system will generate its name automatically.
                  
         
        """
        pass
    
    ## Setter for property: (bool) IsNameUserSpecified

    ##   whether the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  has a user-specified @link NXOpen::NXObject::Name NXOpen::NXObject::Name@endlink .  
    ##    If it isn't
    ##             user-specified, then the system will generate its name automatically.
    ##           
    ##  
    ## Setter License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @IsNameUserSpecified.setter
    def IsNameUserSpecified(self, isNameUserSpecified: bool):
        """
        Setter for property: (bool) IsNameUserSpecified
          whether the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  has a user-specified @link NXOpen::NXObject::Name NXOpen::NXObject::Name@endlink .  
           If it isn't
                    user-specified, then the system will generate its name automatically.
                  
         
        """
        pass
    
    ## Getter for property: (str) LowerBound
    ##   the lower bound value of the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  (if it is being grouped by range)   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def LowerBound(self) -> str:
        """
        Getter for property: (str) LowerBound
          the lower bound value of the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  (if it is being grouped by range)   
            
         
        """
        pass
    
    ## Setter for property: (str) LowerBound

    ##   the lower bound value of the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  (if it is being grouped by range)   
    ##     
    ##  
    ## Setter License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @LowerBound.setter
    def LowerBound(self, fromValue: str):
        """
        Setter for property: (str) LowerBound
          the lower bound value of the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  (if it is being grouped by range)   
            
         
        """
        pass
    
    ## Getter for property: (@link GroupLabel.TagPriorityOption NXOpen.VisualReporting.GroupLabel.TagPriorityOption@endlink) TagPriority
    ##   the Tag Priority of this @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return GroupLabel.TagPriorityOption
    @property
    def TagPriority(self) -> GroupLabel.TagPriorityOption:
        """
        Getter for property: (@link GroupLabel.TagPriorityOption NXOpen.VisualReporting.GroupLabel.TagPriorityOption@endlink) TagPriority
          the Tag Priority of this @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .  
             
         
        """
        pass
    
    ## Setter for property: (@link GroupLabel.TagPriorityOption NXOpen.VisualReporting.GroupLabel.TagPriorityOption@endlink) TagPriority

    ##   the Tag Priority of this @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .  
    ##      
    ##  
    ## Setter License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @TagPriority.setter
    def TagPriority(self, tagPriority: GroupLabel.TagPriorityOption):
        """
        Setter for property: (@link GroupLabel.TagPriorityOption NXOpen.VisualReporting.GroupLabel.TagPriorityOption@endlink) TagPriority
          the Tag Priority of this @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .  
             
         
        """
        pass
    
    ## Getter for property: (str) UpperBound
    ##   the upper bound value of the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  (if it is being grouped by range)   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def UpperBound(self) -> str:
        """
        Getter for property: (str) UpperBound
          the upper bound value of the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  (if it is being grouped by range)   
            
         
        """
        pass
    
    ## Setter for property: (str) UpperBound

    ##   the upper bound value of the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  (if it is being grouped by range)   
    ##     
    ##  
    ## Setter License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @UpperBound.setter
    def UpperBound(self, upperBound: str):
        """
        Setter for property: (str) UpperBound
          the upper bound value of the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  (if it is being grouped by range)   
            
         
        """
        pass
    
    ## Getter for property: (str) Value
    ##   the value of the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  (if it is being grouped by value)   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return str
    @property
    def Value(self) -> str:
        """
        Getter for property: (str) Value
          the value of the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  (if it is being grouped by value)   
            
         
        """
        pass
    
    ## Setter for property: (str) Value

    ##   the value of the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  (if it is being grouped by value)   
    ##     
    ##  
    ## Setter License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @Value.setter
    def Value(self, groupLabelValue: str):
        """
        Setter for property: (str) Value
          the value of the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  (if it is being grouped by value)   
            
         
        """
        pass
    
import NXOpen
##  A property within either a @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink  or a
##         @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink , or used as referenced property 
##         information for the report.
##     
## 
##   <br>  Created in NX7.0.0  <br> 

class Property(NXOpen.NXObject): 
    """ A property within either a <ja_class>NXOpen.VisualReporting.Rule</ja_class> or a
        <ja_class>NXOpen.VisualReporting.Condition</ja_class>, or used as referenced property 
        information for the report.
    """


    ##  Represents the possible @link NXOpen::VisualReporting::Property::SystemDatatype NXOpen::VisualReporting::Property::SystemDatatype@endlink  options
    ##             for a property.
    ##         
    ##  String data type 
    class DatatypeOption(Enum):
        """
        Members Include: <String> <Integer> <Real> <Boolean> <Unknown> <Null> <Date>
        """
        String: int
        Integer: int
        Real: int
        Boolean: int
        Unknown: int
        Null: int
        Date: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Property.DatatypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the possible @link NXOpen::VisualReporting::Property::PropertyType NXOpen::VisualReporting::Property::PropertyType@endlink  options
    ##             for a property
    ##         
    ##  Arrangement specific positioning 
    class TypeOption(Enum):
        """
        Members Include: <ArrangementSpecificPositionProperty> <AttributeProperty> <ComponentGroupProperty> <ComponentNameProperty> <DescriptivePartNameProperty> <LoadStateProperty> <MassKgProperty> <MassLbProperty> <ModifiedProperty> <MultiCadProperty> <PartNameProperty> <PartUnitsProperty> <PiecePartProperty> <PositionProperty> <PositionControlProperty> <ReadOnlyProperty> <ReferenceSetProperty> <RootPartProperty> <SuppressionControlProperty> <WeightStatusProperty> <TeamcenterProperty> <ServerProperty> <DegreesOfFreedomProperty> <RuleEvaluationResultProperty> <CheckMateResultProperty> <LastModifiedDateProperty> <RequirementsValidationStatusProperty> <RepresentationProperty> <LastModifiedUserProperty> <ComponentProperty> <MassGmProperty> <PartFamilyMemberProperty> <LinkedPartProperty> <ProductTemplateProperty> <BodyDensityProperty> <BodyMassProperty> <BodyRadiusGyrationProperty> <BodySurfaceAreaProperty> <BodyTypeProperty> <BodyVolumeProperty> <BodyWeightProperty> <FaceAreaProperty> <FaceTypeProperty> <FaceMinRadiusProperty> <FacePerimeterProperty> <FacePMIFCFProperty> <FacePMIFCFCharacteristicsProperty> <FacePMIFCFCharFormTolProperty> <FacePMIFCFCharLocationTolProperty> <FacePMIFCFCharOrientationTolProperty> <FacePMIFCFCharProfileTolProperty> <FacePMIFCFCharRunoutTolProperty> <FacePMIDatumFeatureProperty> <FacePMIDatumTargetProperty> <ObjectAttributeProperty> <ObjectCreatedByUserProperty> <ObjectCreatedDateProperty> <ObjectCreatedVersionProperty> <ObjectRefByWaveLinkProperty> <ObjectWaveLinkedProperty> <ObjectModifiedByUserProperty> <ObjectModifiedDateProperty> <ObjectModifiedVersionProperty> <PartitionMembershipProperty> <ComponentAddedDateProperty> <TeamcenterObjectProperty> <ComponentPatternTypeProperty> <ObjectNameProperty> <NXOpenProperty> <SheetMetalBendAngleProperty> <SheetMetalBendRadiusProperty> <SheetMetalFaceTypeAllProperty> <SheetMetalFaceTypeBendProperty> <SheetMetalFaceTypeDeformProperty> <SheetMetalFaceTypeWebProperty> <SheetMetalNeutralFactorProperty> <SheetMetalBodyTypeProperty> <FeatureFailureProperty> <MassIssueProperty> <MassUpdateToggleStatusProperty> <LastSavedVersionProperty> <FlexiblePrintedCircuitDesignFaceTypeTopAndBottomProperty> <MassReferenceSetProperty> <BodyReferenceSetNamesProperty> <EnvironmentalMaterialProperty>
        """
        ArrangementSpecificPositionProperty: int
        AttributeProperty: int
        ComponentGroupProperty: int
        ComponentNameProperty: int
        DescriptivePartNameProperty: int
        LoadStateProperty: int
        MassKgProperty: int
        MassLbProperty: int
        ModifiedProperty: int
        MultiCadProperty: int
        PartNameProperty: int
        PartUnitsProperty: int
        PiecePartProperty: int
        PositionProperty: int
        PositionControlProperty: int
        ReadOnlyProperty: int
        ReferenceSetProperty: int
        RootPartProperty: int
        SuppressionControlProperty: int
        WeightStatusProperty: int
        TeamcenterProperty: int
        ServerProperty: int
        DegreesOfFreedomProperty: int
        RuleEvaluationResultProperty: int
        CheckMateResultProperty: int
        LastModifiedDateProperty: int
        RequirementsValidationStatusProperty: int
        RepresentationProperty: int
        LastModifiedUserProperty: int
        ComponentProperty: int
        MassGmProperty: int
        PartFamilyMemberProperty: int
        LinkedPartProperty: int
        ProductTemplateProperty: int
        BodyDensityProperty: int
        BodyMassProperty: int
        BodyRadiusGyrationProperty: int
        BodySurfaceAreaProperty: int
        BodyTypeProperty: int
        BodyVolumeProperty: int
        BodyWeightProperty: int
        FaceAreaProperty: int
        FaceTypeProperty: int
        FaceMinRadiusProperty: int
        FacePerimeterProperty: int
        FacePMIFCFProperty: int
        FacePMIFCFCharacteristicsProperty: int
        FacePMIFCFCharFormTolProperty: int
        FacePMIFCFCharLocationTolProperty: int
        FacePMIFCFCharOrientationTolProperty: int
        FacePMIFCFCharProfileTolProperty: int
        FacePMIFCFCharRunoutTolProperty: int
        FacePMIDatumFeatureProperty: int
        FacePMIDatumTargetProperty: int
        ObjectAttributeProperty: int
        ObjectCreatedByUserProperty: int
        ObjectCreatedDateProperty: int
        ObjectCreatedVersionProperty: int
        ObjectRefByWaveLinkProperty: int
        ObjectWaveLinkedProperty: int
        ObjectModifiedByUserProperty: int
        ObjectModifiedDateProperty: int
        ObjectModifiedVersionProperty: int
        PartitionMembershipProperty: int
        ComponentAddedDateProperty: int
        TeamcenterObjectProperty: int
        ComponentPatternTypeProperty: int
        ObjectNameProperty: int
        NXOpenProperty: int
        SheetMetalBendAngleProperty: int
        SheetMetalBendRadiusProperty: int
        SheetMetalFaceTypeAllProperty: int
        SheetMetalFaceTypeBendProperty: int
        SheetMetalFaceTypeDeformProperty: int
        SheetMetalFaceTypeWebProperty: int
        SheetMetalNeutralFactorProperty: int
        SheetMetalBodyTypeProperty: int
        FeatureFailureProperty: int
        MassIssueProperty: int
        MassUpdateToggleStatusProperty: int
        LastSavedVersionProperty: int
        FlexiblePrintedCircuitDesignFaceTypeTopAndBottomProperty: int
        MassReferenceSetProperty: int
        BodyReferenceSetNamesProperty: int
        EnvironmentalMaterialProperty: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Property.TypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) BitmapName
    ##   the bitmap name of this property.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def BitmapName(self) -> str:
        """
        Getter for property: (str) BitmapName
          the bitmap name of this property.  
          
                  
         
        """
        pass
    
    ## Setter for property: (str) BitmapName

    ##   the bitmap name of this property.  
    ##   
    ##           
    ##  
    ## Setter License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @BitmapName.setter
    def BitmapName(self, bitmapName: str):
        """
        Setter for property: (str) BitmapName
          the bitmap name of this property.  
          
                  
         
        """
        pass
    
    ## Getter for property: (str) CustomMessage
    ##   the custom message of this property.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def CustomMessage(self) -> str:
        """
        Getter for property: (str) CustomMessage
          the custom message of this property.  
          
                  
         
        """
        pass
    
    ## Setter for property: (str) CustomMessage

    ##   the custom message of this property.  
    ##   
    ##           
    ##  
    ## Setter License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @CustomMessage.setter
    def CustomMessage(self, customMessage: str):
        """
        Setter for property: (str) CustomMessage
          the custom message of this property.  
          
                  
         
        """
        pass
    
    ## Getter for property: (@link Property.TypeOption NXOpen.VisualReporting.Property.TypeOption@endlink) PropertyType
    ##   the @link NXOpen::VisualReporting::Property::TypeOption NXOpen::VisualReporting::Property::TypeOption@endlink  of this @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink .  
    ##   
    ## 
    ##             Note that this @link NXOpen::VisualReporting::Property::PropertyType NXOpen::VisualReporting::Property::PropertyType@endlink  cannot be modified. 
    ##             Instead it is specified when creating this @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  by using the appropriate function:
    ##              - @link NXOpen::VisualReporting::VisualReportBuilder::CreateProperty NXOpen::VisualReporting::VisualReportBuilder::CreateProperty@endlink 
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return Property.TypeOption
    @property
    def PropertyType(self) -> Property.TypeOption:
        """
        Getter for property: (@link Property.TypeOption NXOpen.VisualReporting.Property.TypeOption@endlink) PropertyType
          the @link NXOpen::VisualReporting::Property::TypeOption NXOpen::VisualReporting::Property::TypeOption@endlink  of this @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink .  
          
        
                    Note that this @link NXOpen::VisualReporting::Property::PropertyType NXOpen::VisualReporting::Property::PropertyType@endlink  cannot be modified. 
                    Instead it is specified when creating this @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  by using the appropriate function:
                     - @link NXOpen::VisualReporting::VisualReportBuilder::CreateProperty NXOpen::VisualReporting::VisualReportBuilder::CreateProperty@endlink 
                  
         
        """
        pass
    
    ## Getter for property: (@link Property.DatatypeOption NXOpen.VisualReporting.Property.DatatypeOption@endlink) SystemDatatype
    ##   the preferred @link NXOpen::VisualReporting::Property::DatatypeOption NXOpen::VisualReporting::Property::DatatypeOption@endlink  that should be used for the
    ##             owning @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  or @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink .  
    ##   
    ## 
    ##             This function will return a data type of 
    ##             @link NXOpen::VisualReporting::Property::DatatypeOptionUnknown NXOpen::VisualReporting::Property::DatatypeOptionUnknown@endlink 
    ##             for properties whose @link NXOpen::VisualReporting::Property::PropertyType NXOpen::VisualReporting::Property::PropertyType@endlink  is
    ##             @link NXOpen::VisualReporting::Property::TypeOptionTeamcenterProperty NXOpen::VisualReporting::Property::TypeOptionTeamcenterProperty@endlink , 
    ##             @link NXOpen::VisualReporting::Property::TypeOptionServerProperty NXOpen::VisualReporting::Property::TypeOptionServerProperty@endlink , 
    ##             or @link NXOpen::VisualReporting::Property::TypeOptionAttributeProperty NXOpen::VisualReporting::Property::TypeOptionAttributeProperty@endlink 
    ##             where the preferred data type cannot be determined.
    ## 
    ##             Note that this @link NXOpen::VisualReporting::Property::SystemDatatype NXOpen::VisualReporting::Property::SystemDatatype@endlink  cannot be modified. 
    ##             Instead it is determined when creating this @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  by using the appropriate function:
    ##              - @link NXOpen::VisualReporting::VisualReportBuilder::CreateProperty NXOpen::VisualReporting::VisualReportBuilder::CreateProperty@endlink 
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return Property.DatatypeOption
    @property
    def SystemDatatype(self) -> Property.DatatypeOption:
        """
        Getter for property: (@link Property.DatatypeOption NXOpen.VisualReporting.Property.DatatypeOption@endlink) SystemDatatype
          the preferred @link NXOpen::VisualReporting::Property::DatatypeOption NXOpen::VisualReporting::Property::DatatypeOption@endlink  that should be used for the
                    owning @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  or @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink .  
          
        
                    This function will return a data type of 
                    @link NXOpen::VisualReporting::Property::DatatypeOptionUnknown NXOpen::VisualReporting::Property::DatatypeOptionUnknown@endlink 
                    for properties whose @link NXOpen::VisualReporting::Property::PropertyType NXOpen::VisualReporting::Property::PropertyType@endlink  is
                    @link NXOpen::VisualReporting::Property::TypeOptionTeamcenterProperty NXOpen::VisualReporting::Property::TypeOptionTeamcenterProperty@endlink , 
                    @link NXOpen::VisualReporting::Property::TypeOptionServerProperty NXOpen::VisualReporting::Property::TypeOptionServerProperty@endlink , 
                    or @link NXOpen::VisualReporting::Property::TypeOptionAttributeProperty NXOpen::VisualReporting::Property::TypeOptionAttributeProperty@endlink 
                    where the preferred data type cannot be determined.
        
                    Note that this @link NXOpen::VisualReporting::Property::SystemDatatype NXOpen::VisualReporting::Property::SystemDatatype@endlink  cannot be modified. 
                    Instead it is determined when creating this @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  by using the appropriate function:
                     - @link NXOpen::VisualReporting::VisualReportBuilder::CreateProperty NXOpen::VisualReporting::VisualReportBuilder::CreateProperty@endlink 
                  
         
        """
        pass
    
import NXOpen
##  A result category within a @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
##     
## 
##   <br>  Created in NX8.0.0  <br> 

class ResultCategory(NXOpen.NXObject): 
    """ A result category within a <ja_class>NXOpen.VisualReporting.VisualReport</ja_class>.
    """


    ## Getter for property: (str) BitmapName
    ##   the bitmap name of this @link NXOpen::VisualReporting::ResultCategory NXOpen::VisualReporting::ResultCategory@endlink .  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def BitmapName(self) -> str:
        """
        Getter for property: (str) BitmapName
          the bitmap name of this @link NXOpen::VisualReporting::ResultCategory NXOpen::VisualReporting::ResultCategory@endlink .  
          
                  
         
        """
        pass
    
    ## Setter for property: (str) BitmapName

    ##   the bitmap name of this @link NXOpen::VisualReporting::ResultCategory NXOpen::VisualReporting::ResultCategory@endlink .  
    ##   
    ##           
    ##  
    ## Setter License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @BitmapName.setter
    def BitmapName(self, bitmapName: str):
        """
        Setter for property: (str) BitmapName
          the bitmap name of this @link NXOpen::VisualReporting::ResultCategory NXOpen::VisualReporting::ResultCategory@endlink .  
          
                  
         
        """
        pass
    
    ## Getter for property: (str) CustomMessage
    ##   the custom message of this @link NXOpen::VisualReporting::ResultCategory NXOpen::VisualReporting::ResultCategory@endlink .  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def CustomMessage(self) -> str:
        """
        Getter for property: (str) CustomMessage
          the custom message of this @link NXOpen::VisualReporting::ResultCategory NXOpen::VisualReporting::ResultCategory@endlink .  
          
                  
         
        """
        pass
    
    ## Setter for property: (str) CustomMessage

    ##   the custom message of this @link NXOpen::VisualReporting::ResultCategory NXOpen::VisualReporting::ResultCategory@endlink .  
    ##   
    ##           
    ##  
    ## Setter License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @CustomMessage.setter
    def CustomMessage(self, customMessage: str):
        """
        Setter for property: (str) CustomMessage
          the custom message of this @link NXOpen::VisualReporting::ResultCategory NXOpen::VisualReporting::ResultCategory@endlink .  
          
                  
         
        """
        pass
    
import NXOpen
##  A rule within a @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
##     
## 
##   <br>  Created in NX7.0.0  <br> 

class Rule(NXOpen.NXObject): 
    """ A rule within a <ja_class>NXOpen.VisualReporting.VisualReport</ja_class>.
    """


    ## Getter for property: (@link Classifier NXOpen.VisualReporting.Classifier@endlink) ActiveClassifier
    ##   the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink 
    ##             for a multiple properties report.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return Classifier
    @property
    def ActiveClassifier(self) -> Classifier:
        """
        Getter for property: (@link Classifier NXOpen.VisualReporting.Classifier@endlink) ActiveClassifier
          the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink 
                    for a multiple properties report.  
          
                  
         
        """
        pass
    
    ## Setter for property: (@link Classifier NXOpen.VisualReporting.Classifier@endlink) ActiveClassifier

    ##   the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink 
    ##             for a multiple properties report.  
    ##   
    ##           
    ##  
    ## Setter License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @ActiveClassifier.setter
    def ActiveClassifier(self, activeClassifier: Classifier):
        """
        Setter for property: (@link Classifier NXOpen.VisualReporting.Classifier@endlink) ActiveClassifier
          the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink 
                    for a multiple properties report.  
          
                  
         
        """
        pass
    
    ## Getter for property: (@link Condition NXOpen.VisualReporting.Condition@endlink) FilterCondition
    ##   the filter @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  from this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .  
    ##    
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return Condition
    @property
    def FilterCondition(self) -> Condition:
        """
        Getter for property: (@link Condition NXOpen.VisualReporting.Condition@endlink) FilterCondition
          the filter @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  from this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .  
           
                  
         
        """
        pass
    
    ## Setter for property: (@link Condition NXOpen.VisualReporting.Condition@endlink) FilterCondition

    ##   the filter @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  from this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .  
    ##    
    ##           
    ##  
    ## Setter License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @FilterCondition.setter
    def FilterCondition(self, filterCondition: Condition):
        """
        Setter for property: (@link Condition NXOpen.VisualReporting.Condition@endlink) FilterCondition
          the filter @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  from this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .  
           
                  
         
        """
        pass
    
    ##  Returns the @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink s associated with this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
    ##         
    ##  @return classifiers (@link Classifier List[NXOpen.VisualReporting.Classifier]@endlink): .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetClassifiers(rule: Rule) -> List[Classifier]:
        """
         Returns the @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink s associated with this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
                
         @return classifiers (@link Classifier List[NXOpen.VisualReporting.Classifier]@endlink): .
        """
        pass
    
    ##  The @link NXOpen::VisualReporting::Classifier::DateGroupMethodOption NXOpen::VisualReporting::Classifier::DateGroupMethodOption@endlink  in this @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  
    ##             in the @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink  will be determined by the overall date range of all reported objects.
    ##             
    ##             For example, if the date range spans over 18 monthes, group by year will be used, otherwise if it is over 3 months, group by month will be used.
    ##             If the date range is small, within 2 weeks, group by day will be used. 
    ## 
    ##             Only valid for a @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  whose @link NXOpen::VisualReporting::Classifier::GroupingMethodOption NXOpen::VisualReporting::Classifier::GroupingMethodOption@endlink 
    ##             is @link NXOpen::VisualReporting::Classifier::GroupingMethodOptionAutomatic NXOpen::VisualReporting::Classifier::GroupingMethodOptionAutomatic@endlink  or
    ##             @link NXOpen::VisualReporting::Classifier::GroupingMethodOptionSemiAutomatic NXOpen::VisualReporting::Classifier::GroupingMethodOptionSemiAutomatic@endlink  and the
    ##             @link NXOpen::VisualReporting::Property::DatatypeOption NXOpen::VisualReporting::Property::DatatypeOption@endlink  on the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink 
    ##             is @link NXOpen::VisualReporting::Property::DatatypeOptionDate NXOpen::VisualReporting::Property::DatatypeOptionDate@endlink .
    ##         
    ##  @return isSmartGroupDateEnabled (bool): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="classifier"> (@link Classifier NXOpen.VisualReporting.Classifier@endlink) </param>
    def GetIsSmartGroupDateEnabled(rule: Rule, classifier: Classifier) -> bool:
        """
         The @link NXOpen::VisualReporting::Classifier::DateGroupMethodOption NXOpen::VisualReporting::Classifier::DateGroupMethodOption@endlink  in this @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  
                    in the @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink  will be determined by the overall date range of all reported objects.
                    
                    For example, if the date range spans over 18 monthes, group by year will be used, otherwise if it is over 3 months, group by month will be used.
                    If the date range is small, within 2 weeks, group by day will be used. 
        
                    Only valid for a @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  whose @link NXOpen::VisualReporting::Classifier::GroupingMethodOption NXOpen::VisualReporting::Classifier::GroupingMethodOption@endlink 
                    is @link NXOpen::VisualReporting::Classifier::GroupingMethodOptionAutomatic NXOpen::VisualReporting::Classifier::GroupingMethodOptionAutomatic@endlink  or
                    @link NXOpen::VisualReporting::Classifier::GroupingMethodOptionSemiAutomatic NXOpen::VisualReporting::Classifier::GroupingMethodOptionSemiAutomatic@endlink  and the
                    @link NXOpen::VisualReporting::Property::DatatypeOption NXOpen::VisualReporting::Property::DatatypeOption@endlink  on the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink 
                    is @link NXOpen::VisualReporting::Property::DatatypeOptionDate NXOpen::VisualReporting::Property::DatatypeOptionDate@endlink .
                
         @return isSmartGroupDateEnabled (bool): .
        """
        pass
    
    ##  The @link NXOpen::VisualReporting::Classifier::DateGroupMethodOption NXOpen::VisualReporting::Classifier::DateGroupMethodOption@endlink  in this @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  
    ##             in the @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink  will be determined by the overall date range of all reported objects.
    ##         
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ## <param name="classifier"> (@link Classifier NXOpen.VisualReporting.Classifier@endlink) </param>
    ## <param name="isSmartGroupDateEnabled"> (bool) </param>
    def SetIsSmartGroupDateEnabled(rule: Rule, classifier: Classifier, isSmartGroupDateEnabled: bool) -> None:
        """
         The @link NXOpen::VisualReporting::Classifier::DateGroupMethodOption NXOpen::VisualReporting::Classifier::DateGroupMethodOption@endlink  in this @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  
                    in the @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink  will be determined by the overall date range of all reported objects.
                
        """
        pass
    
import NXOpen
##  Represents a Specify Date Builder <br> To create a new instance of this class, use @link NXOpen::VisualReporting::VisualReportManager::CreateSpecifyDateBuilder  NXOpen::VisualReporting::VisualReportManager::CreateSpecifyDateBuilder @endlink  <br> 
## 
##   <br>  Created in NX8.0.0  <br> 

class SpecifyDateBuilder(NXOpen.Builder): 
    """ Represents a Specify Date Builder"""


    ## Getter for property: (@link NXOpen.DateBuilder NXOpen.DateBuilder@endlink) Date
    ##   the date   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return NXOpen.DateBuilder
    @property
    def Date(self) -> NXOpen.DateBuilder:
        """
        Getter for property: (@link NXOpen.DateBuilder NXOpen.DateBuilder@endlink) Date
          the date   
            
         
        """
        pass
    
    ## Getter for property: (str) DateString
    ##   the current date as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def DateString(self) -> str:
        """
        Getter for property: (str) DateString
          the current date as string  
            
         
        """
        pass
    
    ## Getter for property: (str) RelativeDateString
    ##   the current relative date string   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def RelativeDateString(self) -> str:
        """
        Getter for property: (str) RelativeDateString
          the current relative date string   
            
         
        """
        pass
    
    ## Setter for property: (str) RelativeDateString

    ##   the current relative date string   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @RelativeDateString.setter
    def RelativeDateString(self, date_string: str):
        """
        Setter for property: (str) RelativeDateString
          the current relative date string   
            
         
        """
        pass
    
import NXOpen
##  An unmatched result category within a @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
##     
## 
##   <br>  Created in NX8.0.0  <br> 

class UnmatchedResultCategory(NXOpen.NXObject): 
    """ An unmatched result category within a <ja_class>NXOpen.VisualReporting.VisualReport</ja_class>.
    """
    pass


import NXOpen
##  A Builder for creating and editing @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink s.
##      <br> To create a new instance of this class, use @link NXOpen::VisualReporting::VisualReportManager::CreateVisualReportBuilder  NXOpen::VisualReporting::VisualReportManager::CreateVisualReportBuilder @endlink  <br> 
## 
##   <br>  Created in NX7.0.0  <br> 

class VisualReportBuilder(NXOpen.Builder): 
    """ A Builder for creating and editing <ja_class>NXOpen.VisualReporting.VisualReport</ja_class>s.
    """


    ##  Represents the usage option of reference @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink 
    ##         
    ## The property is used in tooltip only
    class PropertyUsageOption(Enum):
        """
        Members Include: <Tooltip> <InfoView> <TooltipAndInfoView>
        """
        Tooltip: int
        InfoView: int
        TooltipAndInfoView: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> VisualReportBuilder.PropertyUsageOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) BitmapNameOfReport
    ##   the bitmap name of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def BitmapNameOfReport(self) -> str:
        """
        Getter for property: (str) BitmapNameOfReport
          the bitmap name of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
          
                  
         
        """
        pass
    
    ## Setter for property: (str) BitmapNameOfReport

    ##   the bitmap name of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
    ##   
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @BitmapNameOfReport.setter
    def BitmapNameOfReport(self, bitmapName: str):
        """
        Setter for property: (str) BitmapNameOfReport
          the bitmap name of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
          
                  
         
        """
        pass
    
    ## Getter for property: (str) BitmapNameOfReportingProperty
    ##   the bitmap name of the reporting @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  in the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink .  
    ##    
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def BitmapNameOfReportingProperty(self) -> str:
        """
        Getter for property: (str) BitmapNameOfReportingProperty
          the bitmap name of the reporting @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  in the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink .  
           
                  
         
        """
        pass
    
    ## Setter for property: (str) BitmapNameOfReportingProperty

    ##   the bitmap name of the reporting @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  in the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink .  
    ##    
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @BitmapNameOfReportingProperty.setter
    def BitmapNameOfReportingProperty(self, bitmapName: str):
        """
        Setter for property: (str) BitmapNameOfReportingProperty
          the bitmap name of the reporting @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  in the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink .  
           
                  
         
        """
        pass
    
    ## Getter for property: (str) CustomMessageOfReport
    ##  the custom message of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
    ##    
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def CustomMessageOfReport(self) -> str:
        """
        Getter for property: (str) CustomMessageOfReport
         the custom message of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
           
                  
         
        """
        pass
    
    ## Setter for property: (str) CustomMessageOfReport

    ##  the custom message of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
    ##    
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @CustomMessageOfReport.setter
    def CustomMessageOfReport(self, customMessage: str):
        """
        Setter for property: (str) CustomMessageOfReport
         the custom message of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
           
                  
         
        """
        pass
    
    ## Getter for property: (str) CustomMessageOfReportingProperty
    ##  the custom message of the reporting @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  in the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink .  
    ##    
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def CustomMessageOfReportingProperty(self) -> str:
        """
        Getter for property: (str) CustomMessageOfReportingProperty
         the custom message of the reporting @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  in the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink .  
           
                  
         
        """
        pass
    
    ## Setter for property: (str) CustomMessageOfReportingProperty

    ##  the custom message of the reporting @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  in the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink .  
    ##    
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @CustomMessageOfReportingProperty.setter
    def CustomMessageOfReportingProperty(self, customMessage: str):
        """
        Setter for property: (str) CustomMessageOfReportingProperty
         the custom message of the reporting @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  in the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink .  
           
                  
         
        """
        pass
    
    ## Getter for property: (str) DescriptionOfVisualReport
    ##   the description of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this
    ##             builder.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def DescriptionOfVisualReport(self) -> str:
        """
        Getter for property: (str) DescriptionOfVisualReport
          the description of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this
                    builder.  
          
                  
         
        """
        pass
    
    ## Setter for property: (str) DescriptionOfVisualReport

    ##   the description of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this
    ##             builder.  
    ##   
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @DescriptionOfVisualReport.setter
    def DescriptionOfVisualReport(self, description: str):
        """
        Setter for property: (str) DescriptionOfVisualReport
          the description of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this
                    builder.  
          
                  
         
        """
        pass
    
    ## Getter for property: (str) DescriptiveCategoryOfVisualReport
    ##   the descriptive category of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink 
    ##             being built by this builder.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def DescriptiveCategoryOfVisualReport(self) -> str:
        """
        Getter for property: (str) DescriptiveCategoryOfVisualReport
          the descriptive category of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink 
                    being built by this builder.  
          
                  
         
        """
        pass
    
    ## Setter for property: (str) DescriptiveCategoryOfVisualReport

    ##   the descriptive category of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink 
    ##             being built by this builder.  
    ##   
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @DescriptiveCategoryOfVisualReport.setter
    def DescriptiveCategoryOfVisualReport(self, category: str):
        """
        Setter for property: (str) DescriptiveCategoryOfVisualReport
          the descriptive category of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink 
                    being built by this builder.  
          
                  
         
        """
        pass
    
    ## Getter for property: (str) DestinationTeamcenterFolder
    ##   the destination Teamcenter folder for saving the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this
    ##             builder to Teamcenter database.  
    ##   
    ## 
    ##             Note that this property is only needed when NX is connected to Teamcenter and report is saved as a copy to Teamcenter database.
    ##             This @link NXOpen::VisualReporting::VisualReport::DestinationTeamcenterFolder NXOpen::VisualReporting::VisualReport::DestinationTeamcenterFolder@endlink  may return NULL if you haven't 
    ##             set a folder name on this property.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def DestinationTeamcenterFolder(self) -> str:
        """
        Getter for property: (str) DestinationTeamcenterFolder
          the destination Teamcenter folder for saving the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this
                    builder to Teamcenter database.  
          
        
                    Note that this property is only needed when NX is connected to Teamcenter and report is saved as a copy to Teamcenter database.
                    This @link NXOpen::VisualReporting::VisualReport::DestinationTeamcenterFolder NXOpen::VisualReporting::VisualReport::DestinationTeamcenterFolder@endlink  may return NULL if you haven't 
                    set a folder name on this property.
                  
         
        """
        pass
    
    ## Setter for property: (str) DestinationTeamcenterFolder

    ##   the destination Teamcenter folder for saving the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this
    ##             builder to Teamcenter database.  
    ##   
    ## 
    ##             Note that this property is only needed when NX is connected to Teamcenter and report is saved as a copy to Teamcenter database.
    ##             This @link NXOpen::VisualReporting::VisualReport::DestinationTeamcenterFolder NXOpen::VisualReporting::VisualReport::DestinationTeamcenterFolder@endlink  may return NULL if you haven't 
    ##             set a folder name on this property.
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @DestinationTeamcenterFolder.setter
    def DestinationTeamcenterFolder(self, foldername: str):
        """
        Setter for property: (str) DestinationTeamcenterFolder
          the destination Teamcenter folder for saving the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this
                    builder to Teamcenter database.  
          
        
                    Note that this property is only needed when NX is connected to Teamcenter and report is saved as a copy to Teamcenter database.
                    This @link NXOpen::VisualReporting::VisualReport::DestinationTeamcenterFolder NXOpen::VisualReporting::VisualReport::DestinationTeamcenterFolder@endlink  may return NULL if you haven't 
                    set a folder name on this property.
                  
         
        """
        pass
    
    ## Getter for property: (str) FilenameOfVisualReport
    ##   the file name of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this
    ##             builder.  
    ##   
    ## 
    ##             Note that when NX is connected to Teamcenter, this property is the report dataset identifier from Teamcenter database. 
    ##             If it is a new report, it will be the report dataset name. When the report is save by @link NXOpen::VisualReporting::VisualReportBuilder::Save NXOpen::VisualReporting::VisualReportBuilder::Save@endlink , 
    ##             the report dataset identifier will be saved in this property.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def FilenameOfVisualReport(self) -> str:
        """
        Getter for property: (str) FilenameOfVisualReport
          the file name of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this
                    builder.  
          
        
                    Note that when NX is connected to Teamcenter, this property is the report dataset identifier from Teamcenter database. 
                    If it is a new report, it will be the report dataset name. When the report is save by @link NXOpen::VisualReporting::VisualReportBuilder::Save NXOpen::VisualReporting::VisualReportBuilder::Save@endlink , 
                    the report dataset identifier will be saved in this property.
                  
         
        """
        pass
    
    ## Setter for property: (str) FilenameOfVisualReport

    ##   the file name of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this
    ##             builder.  
    ##   
    ## 
    ##             Note that when NX is connected to Teamcenter, this property is the report dataset identifier from Teamcenter database. 
    ##             If it is a new report, it will be the report dataset name. When the report is save by @link NXOpen::VisualReporting::VisualReportBuilder::Save NXOpen::VisualReporting::VisualReportBuilder::Save@endlink , 
    ##             the report dataset identifier will be saved in this property.
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @FilenameOfVisualReport.setter
    def FilenameOfVisualReport(self, filename: str):
        """
        Setter for property: (str) FilenameOfVisualReport
          the file name of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this
                    builder.  
          
        
                    Note that when NX is connected to Teamcenter, this property is the report dataset identifier from Teamcenter database. 
                    If it is a new report, it will be the report dataset name. When the report is save by @link NXOpen::VisualReporting::VisualReportBuilder::Save NXOpen::VisualReporting::VisualReportBuilder::Save@endlink , 
                    the report dataset identifier will be saved in this property.
                  
         
        """
        pass
    
    ## Getter for property: (str) KeywordsOfVisualReport
    ##   the keywords of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this
    ##             builder.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def KeywordsOfVisualReport(self) -> str:
        """
        Getter for property: (str) KeywordsOfVisualReport
          the keywords of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this
                    builder.  
          
                  
         
        """
        pass
    
    ## Setter for property: (str) KeywordsOfVisualReport

    ##   the keywords of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this
    ##             builder.  
    ##   
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @KeywordsOfVisualReport.setter
    def KeywordsOfVisualReport(self, keywords: str):
        """
        Setter for property: (str) KeywordsOfVisualReport
          the keywords of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this
                    builder.  
          
                  
         
        """
        pass
    
    ## Getter for property: (@link VisualReport.ReportContextOption NXOpen.VisualReporting.VisualReport.ReportContextOption@endlink) ReportContextOfVisualReport
    ##   the @link NXOpen::VisualReporting::VisualReport::ReportContextOption NXOpen::VisualReporting::VisualReport::ReportContextOption@endlink  of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this builder.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX9.0.3.  Use @link NXOpen::VisualReporting::VisualReport::ReportContext NXOpen::VisualReporting::VisualReport::ReportContext@endlink  instead.  <br> 

    ## @return VisualReport.ReportContextOption
    @property
    def ReportContextOfVisualReport(self) -> VisualReport.ReportContextOption:
        """
        Getter for property: (@link VisualReport.ReportContextOption NXOpen.VisualReporting.VisualReport.ReportContextOption@endlink) ReportContextOfVisualReport
          the @link NXOpen::VisualReporting::VisualReport::ReportContextOption NXOpen::VisualReporting::VisualReport::ReportContextOption@endlink  of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this builder.  
          
                  
         
        """
        pass
    
    ## Setter for property: (@link VisualReport.ReportContextOption NXOpen.VisualReporting.VisualReport.ReportContextOption@endlink) ReportContextOfVisualReport

    ##   the @link NXOpen::VisualReporting::VisualReport::ReportContextOption NXOpen::VisualReporting::VisualReport::ReportContextOption@endlink  of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this builder.  
    ##   
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX9.0.3.  Use @link NXOpen::VisualReporting::VisualReport::SetReportContext NXOpen::VisualReporting::VisualReport::SetReportContext@endlink  instead.  <br> 

    @ReportContextOfVisualReport.setter
    def ReportContextOfVisualReport(self, reportContext: VisualReport.ReportContextOption):
        """
        Setter for property: (@link VisualReport.ReportContextOption NXOpen.VisualReporting.VisualReport.ReportContextOption@endlink) ReportContextOfVisualReport
          the @link NXOpen::VisualReporting::VisualReport::ReportContextOption NXOpen::VisualReporting::VisualReport::ReportContextOption@endlink  of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this builder.  
          
                  
         
        """
        pass
    
    ## Getter for property: (str) ReportNameOfVisualReport
    ##   the name of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this builder.  
    ##    
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def ReportNameOfVisualReport(self) -> str:
        """
        Getter for property: (str) ReportNameOfVisualReport
          the name of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this builder.  
           
                  
         
        """
        pass
    
    ## Setter for property: (str) ReportNameOfVisualReport

    ##   the name of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this builder.  
    ##    
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @ReportNameOfVisualReport.setter
    def ReportNameOfVisualReport(self, reportName: str):
        """
        Setter for property: (str) ReportNameOfVisualReport
          the name of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this builder.  
           
                  
         
        """
        pass
    
    ## Getter for property: (@link VisualReport.ReportingObjectTypeOption NXOpen.VisualReporting.VisualReport.ReportingObjectTypeOption@endlink) ReportingObjectTypeOfVisualReport
    ##   the reporting object type of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this builder.  
    ##   
    ##             Only valid if the @link NXOpen::VisualReporting::VisualReport::ScopeType NXOpen::VisualReporting::VisualReport::ScopeType@endlink  of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink 
    ##             is @link NXOpen::VisualReporting::VisualReport::ScopeTypeOptionComponent NXOpen::VisualReporting::VisualReport::ScopeTypeOptionComponent@endlink  type.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return VisualReport.ReportingObjectTypeOption
    @property
    def ReportingObjectTypeOfVisualReport(self) -> VisualReport.ReportingObjectTypeOption:
        """
        Getter for property: (@link VisualReport.ReportingObjectTypeOption NXOpen.VisualReporting.VisualReport.ReportingObjectTypeOption@endlink) ReportingObjectTypeOfVisualReport
          the reporting object type of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this builder.  
          
                    Only valid if the @link NXOpen::VisualReporting::VisualReport::ScopeType NXOpen::VisualReporting::VisualReport::ScopeType@endlink  of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink 
                    is @link NXOpen::VisualReporting::VisualReport::ScopeTypeOptionComponent NXOpen::VisualReporting::VisualReport::ScopeTypeOptionComponent@endlink  type.
                  
         
        """
        pass
    
    ## Setter for property: (@link VisualReport.ReportingObjectTypeOption NXOpen.VisualReporting.VisualReport.ReportingObjectTypeOption@endlink) ReportingObjectTypeOfVisualReport

    ##   the reporting object type of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this builder.  
    ##   
    ##             Only valid if the @link NXOpen::VisualReporting::VisualReport::ScopeType NXOpen::VisualReporting::VisualReport::ScopeType@endlink  of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink 
    ##             is @link NXOpen::VisualReporting::VisualReport::ScopeTypeOptionComponent NXOpen::VisualReporting::VisualReport::ScopeTypeOptionComponent@endlink  type.
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @ReportingObjectTypeOfVisualReport.setter
    def ReportingObjectTypeOfVisualReport(self, reportingObjectType: VisualReport.ReportingObjectTypeOption):
        """
        Setter for property: (@link VisualReport.ReportingObjectTypeOption NXOpen.VisualReporting.VisualReport.ReportingObjectTypeOption@endlink) ReportingObjectTypeOfVisualReport
          the reporting object type of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this builder.  
          
                    Only valid if the @link NXOpen::VisualReporting::VisualReport::ScopeType NXOpen::VisualReporting::VisualReport::ScopeType@endlink  of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink 
                    is @link NXOpen::VisualReporting::VisualReport::ScopeTypeOptionComponent NXOpen::VisualReporting::VisualReport::ScopeTypeOptionComponent@endlink  type.
                  
         
        """
        pass
    
    ## Getter for property: (@link VisualReport.ReportingStyleOption NXOpen.VisualReporting.VisualReport.ReportingStyleOption@endlink) ReportingStyleOfVisualReport
    ##   the reporting style of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this builder.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return VisualReport.ReportingStyleOption
    @property
    def ReportingStyleOfVisualReport(self) -> VisualReport.ReportingStyleOption:
        """
        Getter for property: (@link VisualReport.ReportingStyleOption NXOpen.VisualReporting.VisualReport.ReportingStyleOption@endlink) ReportingStyleOfVisualReport
          the reporting style of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this builder.  
          
                  
         
        """
        pass
    
    ## Setter for property: (@link VisualReport.ReportingStyleOption NXOpen.VisualReporting.VisualReport.ReportingStyleOption@endlink) ReportingStyleOfVisualReport

    ##   the reporting style of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this builder.  
    ##   
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @ReportingStyleOfVisualReport.setter
    def ReportingStyleOfVisualReport(self, reportingStyle: VisualReport.ReportingStyleOption):
        """
        Setter for property: (@link VisualReport.ReportingStyleOption NXOpen.VisualReporting.VisualReport.ReportingStyleOption@endlink) ReportingStyleOfVisualReport
          the reporting style of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this builder.  
          
                  
         
        """
        pass
    
    ## Getter for property: (@link VisualReport.SaveDestinationOption NXOpen.VisualReporting.VisualReport.SaveDestinationOption@endlink) SaveDestination
    ##   the @link NXOpen::VisualReporting::VisualReport::SaveDestinationOption NXOpen::VisualReporting::VisualReport::SaveDestinationOption@endlink  of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this
    ##             builder.  
    ##   
    ##             Note that this property will always be @link NXOpen::VisualReporting::VisualReport::SaveDestinationOptionLocal NXOpen::VisualReporting::VisualReport::SaveDestinationOptionLocal@endlink  when NX is not connected to Teamcenter.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return VisualReport.SaveDestinationOption
    @property
    def SaveDestination(self) -> VisualReport.SaveDestinationOption:
        """
        Getter for property: (@link VisualReport.SaveDestinationOption NXOpen.VisualReporting.VisualReport.SaveDestinationOption@endlink) SaveDestination
          the @link NXOpen::VisualReporting::VisualReport::SaveDestinationOption NXOpen::VisualReporting::VisualReport::SaveDestinationOption@endlink  of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this
                    builder.  
          
                    Note that this property will always be @link NXOpen::VisualReporting::VisualReport::SaveDestinationOptionLocal NXOpen::VisualReporting::VisualReport::SaveDestinationOptionLocal@endlink  when NX is not connected to Teamcenter.
                  
         
        """
        pass
    
    ## Setter for property: (@link VisualReport.SaveDestinationOption NXOpen.VisualReporting.VisualReport.SaveDestinationOption@endlink) SaveDestination

    ##   the @link NXOpen::VisualReporting::VisualReport::SaveDestinationOption NXOpen::VisualReporting::VisualReport::SaveDestinationOption@endlink  of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this
    ##             builder.  
    ##   
    ##             Note that this property will always be @link NXOpen::VisualReporting::VisualReport::SaveDestinationOptionLocal NXOpen::VisualReporting::VisualReport::SaveDestinationOptionLocal@endlink  when NX is not connected to Teamcenter.
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @SaveDestination.setter
    def SaveDestination(self, destinationOption: VisualReport.SaveDestinationOption):
        """
        Setter for property: (@link VisualReport.SaveDestinationOption NXOpen.VisualReporting.VisualReport.SaveDestinationOption@endlink) SaveDestination
          the @link NXOpen::VisualReporting::VisualReport::SaveDestinationOption NXOpen::VisualReporting::VisualReport::SaveDestinationOption@endlink  of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this
                    builder.  
          
                    Note that this property will always be @link NXOpen::VisualReporting::VisualReport::SaveDestinationOptionLocal NXOpen::VisualReporting::VisualReport::SaveDestinationOptionLocal@endlink  when NX is not connected to Teamcenter.
                  
         
        """
        pass
    
    ## Getter for property: (str) ScopeNameOfVisualReport
    ##   the scope name of visual report.  
    ##   
    ## 
    ##             when set the scope name of visual report, the object type of this scope is also setted, so caller no need to call 
    ##             @link NXOpen::VisualReporting::VisualReportBuilder::SetScopeTypeOfVisualReport NXOpen::VisualReporting::VisualReportBuilder::SetScopeTypeOfVisualReport@endlink .
    ##             but if the scope is @link NXOpen::VisualReporting::VisualReport::ScopeTypeOptionSubPart NXOpen::VisualReporting::VisualReport::ScopeTypeOptionSubPart@endlink , the caller should also call
    ##             @link NXOpen::VisualReporting::VisualReportBuilder::SetObjectTypesOfVisualReport NXOpen::VisualReporting::VisualReportBuilder::SetObjectTypesOfVisualReport@endlink  after setting scope name.
    ##             note that during setting the scope name of visual report, the @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink  of this report will be deleted and initilized, so the caller should 
    ##             get rule again.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def ScopeNameOfVisualReport(self) -> str:
        """
        Getter for property: (str) ScopeNameOfVisualReport
          the scope name of visual report.  
          
        
                    when set the scope name of visual report, the object type of this scope is also setted, so caller no need to call 
                    @link NXOpen::VisualReporting::VisualReportBuilder::SetScopeTypeOfVisualReport NXOpen::VisualReporting::VisualReportBuilder::SetScopeTypeOfVisualReport@endlink .
                    but if the scope is @link NXOpen::VisualReporting::VisualReport::ScopeTypeOptionSubPart NXOpen::VisualReporting::VisualReport::ScopeTypeOptionSubPart@endlink , the caller should also call
                    @link NXOpen::VisualReporting::VisualReportBuilder::SetObjectTypesOfVisualReport NXOpen::VisualReporting::VisualReportBuilder::SetObjectTypesOfVisualReport@endlink  after setting scope name.
                    note that during setting the scope name of visual report, the @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink  of this report will be deleted and initilized, so the caller should 
                    get rule again.
                  
         
        """
        pass
    
    ## Setter for property: (str) ScopeNameOfVisualReport

    ##   the scope name of visual report.  
    ##   
    ## 
    ##             when set the scope name of visual report, the object type of this scope is also setted, so caller no need to call 
    ##             @link NXOpen::VisualReporting::VisualReportBuilder::SetScopeTypeOfVisualReport NXOpen::VisualReporting::VisualReportBuilder::SetScopeTypeOfVisualReport@endlink .
    ##             but if the scope is @link NXOpen::VisualReporting::VisualReport::ScopeTypeOptionSubPart NXOpen::VisualReporting::VisualReport::ScopeTypeOptionSubPart@endlink , the caller should also call
    ##             @link NXOpen::VisualReporting::VisualReportBuilder::SetObjectTypesOfVisualReport NXOpen::VisualReporting::VisualReportBuilder::SetObjectTypesOfVisualReport@endlink  after setting scope name.
    ##             note that during setting the scope name of visual report, the @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink  of this report will be deleted and initilized, so the caller should 
    ##             get rule again.
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ScopeNameOfVisualReport.setter
    def ScopeNameOfVisualReport(self, scopeName: str):
        """
        Setter for property: (str) ScopeNameOfVisualReport
          the scope name of visual report.  
          
        
                    when set the scope name of visual report, the object type of this scope is also setted, so caller no need to call 
                    @link NXOpen::VisualReporting::VisualReportBuilder::SetScopeTypeOfVisualReport NXOpen::VisualReporting::VisualReportBuilder::SetScopeTypeOfVisualReport@endlink .
                    but if the scope is @link NXOpen::VisualReporting::VisualReport::ScopeTypeOptionSubPart NXOpen::VisualReporting::VisualReport::ScopeTypeOptionSubPart@endlink , the caller should also call
                    @link NXOpen::VisualReporting::VisualReportBuilder::SetObjectTypesOfVisualReport NXOpen::VisualReporting::VisualReportBuilder::SetObjectTypesOfVisualReport@endlink  after setting scope name.
                    note that during setting the scope name of visual report, the @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink  of this report will be deleted and initilized, so the caller should 
                    get rule again.
                  
         
        """
        pass
    
    ## Getter for property: (@link VisualReport.ScopeTypeOption NXOpen.VisualReporting.VisualReport.ScopeTypeOption@endlink) ScopeTypeOfVisualReport
    ##   the @link NXOpen::VisualReporting::VisualReport::ScopeTypeOption NXOpen::VisualReporting::VisualReport::ScopeTypeOption@endlink  of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this builder.  
    ##   
    ##             note that during setting scope type of visual report, the @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink  of this report will be deleted and initilized, so the caller should 
    ##             get rule again.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return VisualReport.ScopeTypeOption
    @property
    def ScopeTypeOfVisualReport(self) -> VisualReport.ScopeTypeOption:
        """
        Getter for property: (@link VisualReport.ScopeTypeOption NXOpen.VisualReporting.VisualReport.ScopeTypeOption@endlink) ScopeTypeOfVisualReport
          the @link NXOpen::VisualReporting::VisualReport::ScopeTypeOption NXOpen::VisualReporting::VisualReport::ScopeTypeOption@endlink  of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this builder.  
          
                    note that during setting scope type of visual report, the @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink  of this report will be deleted and initilized, so the caller should 
                    get rule again.
                  
         
        """
        pass
    
    ## Setter for property: (@link VisualReport.ScopeTypeOption NXOpen.VisualReporting.VisualReport.ScopeTypeOption@endlink) ScopeTypeOfVisualReport

    ##   the @link NXOpen::VisualReporting::VisualReport::ScopeTypeOption NXOpen::VisualReporting::VisualReport::ScopeTypeOption@endlink  of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this builder.  
    ##   
    ##             note that during setting scope type of visual report, the @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink  of this report will be deleted and initilized, so the caller should 
    ##             get rule again.
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ScopeTypeOfVisualReport.setter
    def ScopeTypeOfVisualReport(self, scopeType: VisualReport.ScopeTypeOption):
        """
        Setter for property: (@link VisualReport.ScopeTypeOption NXOpen.VisualReporting.VisualReport.ScopeTypeOption@endlink) ScopeTypeOfVisualReport
          the @link NXOpen::VisualReporting::VisualReport::ScopeTypeOption NXOpen::VisualReporting::VisualReport::ScopeTypeOption@endlink  of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this builder.  
          
                    note that during setting scope type of visual report, the @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink  of this report will be deleted and initilized, so the caller should 
                    get rule again.
                  
         
        """
        pass
    
    ##  Add a new child @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  to this condition. If the child is already a
    ##             child of another @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  or @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink , then it is
    ##             removed from that other object. The new child must have been created in the same
    ##             @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  as this parent condition. If this is a
    ##             @link NXOpen::VisualReporting::Condition::TypeOptionNotCondition NXOpen::VisualReporting::Condition::TypeOptionNotCondition@endlink  then
    ##             this replaces the existing child, and the existing child is deleted.
    ##         
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    ##  The condition 
    def AddChildToCondition(builder: VisualReportBuilder, condition: Condition, childCondition: Condition) -> None:
        """
         Add a new child @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  to this condition. If the child is already a
                    child of another @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  or @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink , then it is
                    removed from that other object. The new child must have been created in the same
                    @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  as this parent condition. If this is a
                    @link NXOpen::VisualReporting::Condition::TypeOptionNotCondition NXOpen::VisualReporting::Condition::TypeOptionNotCondition@endlink  then
                    this replaces the existing child, and the existing child is deleted.
                
        """
        pass
    
    ##  When @link Builder::Commit Builder::Commit@endlink  is called on this builder, it will
    ##             delete the original @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  whose copy the builder is editing and install the copied
    ##             @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  to the @link NXOpen::VisualReporting::VisualReportManager NXOpen::VisualReporting::VisualReportManager@endlink .
    ##             
    ##             If it is required not to delete the original @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink ,
    ##             then @link CommitAsCopy CommitAsCopy@endlink  can be called instead. This behaves
    ##             just like @link Builder::Commit Builder::Commit@endlink  except it does not delete the
    ##             original @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
    ##         
    ##  @return newVisualReport (@link VisualReport NXOpen.VisualReporting.VisualReport@endlink):   .
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def CommitAsCopy(builder: VisualReportBuilder) -> VisualReport:
        """
         When @link Builder::Commit Builder::Commit@endlink  is called on this builder, it will
                    delete the original @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  whose copy the builder is editing and install the copied
                    @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  to the @link NXOpen::VisualReporting::VisualReportManager NXOpen::VisualReporting::VisualReportManager@endlink .
                    
                    If it is required not to delete the original @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink ,
                    then @link CommitAsCopy CommitAsCopy@endlink  can be called instead. This behaves
                    just like @link Builder::Commit Builder::Commit@endlink  except it does not delete the
                    original @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
                
         @return newVisualReport (@link VisualReport NXOpen.VisualReporting.VisualReport@endlink):   .
        """
        pass
    
    ##  Creates a new empty @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink , but does not add it to a
    ##             @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
    ##         
    ##  @return condition (@link Condition NXOpen.VisualReporting.Condition@endlink):  The created condition .
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    def CreateAndCondition(builder: VisualReportBuilder) -> Condition:
        """
         Creates a new empty @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink , but does not add it to a
                    @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
                
         @return condition (@link Condition NXOpen.VisualReporting.Condition@endlink):  The created condition .
        """
        pass
    
    ##  Creates a new empty @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
    ##             @link NXOpen::VisualReporting::Condition::Datatype NXOpen::VisualReporting::Condition::Datatype@endlink  is
    ##             @link NXOpen::VisualReporting::Property::DatatypeOptionBoolean NXOpen::VisualReporting::Property::DatatypeOptionBoolean@endlink ,
    ##             but does not add it to a @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
    ##         
    ##  @return condition (@link Condition NXOpen.VisualReporting.Condition@endlink):  The created condition .
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    ##  The @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  to which this condition will be applied 
    def CreateBooleanCondition(builder: VisualReportBuilder, property: Property, value: bool, operatorType: Condition.OperatorOption) -> Condition:
        """
         Creates a new empty @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                    @link NXOpen::VisualReporting::Condition::Datatype NXOpen::VisualReporting::Condition::Datatype@endlink  is
                    @link NXOpen::VisualReporting::Property::DatatypeOptionBoolean NXOpen::VisualReporting::Property::DatatypeOptionBoolean@endlink ,
                    but does not add it to a @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
                
         @return condition (@link Condition NXOpen.VisualReporting.Condition@endlink):  The created condition .
        """
        pass
    
    ##  Creates a new empty @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
    ##             @link NXOpen::VisualReporting::Condition::Datatype NXOpen::VisualReporting::Condition::Datatype@endlink  is
    ##             @link NXOpen::VisualReporting::Property::DatatypeOptionDate NXOpen::VisualReporting::Property::DatatypeOptionDate@endlink ,
    ##             but does not add it to a @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
    ##         
    ##  @return condition (@link Condition NXOpen.VisualReporting.Condition@endlink):  The created condition .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  to which this condition will be applied 
    def CreateDateCondition(builder: VisualReportBuilder, property: Property, value: str, operatorType: Condition.OperatorOption) -> Condition:
        """
         Creates a new empty @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                    @link NXOpen::VisualReporting::Condition::Datatype NXOpen::VisualReporting::Condition::Datatype@endlink  is
                    @link NXOpen::VisualReporting::Property::DatatypeOptionDate NXOpen::VisualReporting::Property::DatatypeOptionDate@endlink ,
                    but does not add it to a @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
                
         @return condition (@link Condition NXOpen.VisualReporting.Condition@endlink):  The created condition .
        """
        pass
    
    ##  Creates a new empty @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink , and adds it to the given
    ##             @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink . This can only be called if the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  
    ##             in this rule is using @link NXOpen::VisualReporting::Classifier::GroupingMethodOptionManual NXOpen::VisualReporting::Classifier::GroupingMethodOptionManual@endlink  grouping.
    ##         
    ##  @return groupLabel (@link GroupLabel NXOpen.VisualReporting.GroupLabel@endlink):  The created group label .
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    ##  The initial name. If this name is empty then a system-generated name will be
    ##                                                                                                                     assigned when the owning @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  is next activated 
    def CreateGroupLabel(builder: VisualReportBuilder, name: str, rule: Rule, afterGroupLabel: GroupLabel) -> GroupLabel:
        """
         Creates a new empty @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink , and adds it to the given
                    @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink . This can only be called if the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  
                    in this rule is using @link NXOpen::VisualReporting::Classifier::GroupingMethodOptionManual NXOpen::VisualReporting::Classifier::GroupingMethodOptionManual@endlink  grouping.
                
         @return groupLabel (@link GroupLabel NXOpen.VisualReporting.GroupLabel@endlink):  The created group label .
        """
        pass
    
    ##  Creates a new empty @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
    ##             @link NXOpen::VisualReporting::Condition::Datatype NXOpen::VisualReporting::Condition::Datatype@endlink  is
    ##             @link NXOpen::VisualReporting::Property::DatatypeOptionInteger NXOpen::VisualReporting::Property::DatatypeOptionInteger@endlink ,
    ##             but does not add it to a @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
    ##         
    ##  @return condition (@link Condition NXOpen.VisualReporting.Condition@endlink):  The created condition .
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    ##  The @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  to which this condition will be applied 
    def CreateIntegerCondition(builder: VisualReportBuilder, property: Property, value: int, operatorType: Condition.OperatorOption) -> Condition:
        """
         Creates a new empty @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                    @link NXOpen::VisualReporting::Condition::Datatype NXOpen::VisualReporting::Condition::Datatype@endlink  is
                    @link NXOpen::VisualReporting::Property::DatatypeOptionInteger NXOpen::VisualReporting::Property::DatatypeOptionInteger@endlink ,
                    but does not add it to a @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
                
         @return condition (@link Condition NXOpen.VisualReporting.Condition@endlink):  The created condition .
        """
        pass
    
    ##  Creates a new empty @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink , but does not add it to a
    ##             @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
    ##         
    ##  @return condition (@link Condition NXOpen.VisualReporting.Condition@endlink):  The created condition .
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    def CreateNotCondition(builder: VisualReportBuilder) -> Condition:
        """
         Creates a new empty @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink , but does not add it to a
                    @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
                
         @return condition (@link Condition NXOpen.VisualReporting.Condition@endlink):  The created condition .
        """
        pass
    
    ##  Creates a new empty @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
    ##             @link NXOpen::VisualReporting::Condition::Datatype NXOpen::VisualReporting::Condition::Datatype@endlink  is
    ##             @link NXOpen::VisualReporting::Property::DatatypeOptionNull NXOpen::VisualReporting::Property::DatatypeOptionNull@endlink ,
    ##             but does not add it to a @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
    ##         
    ##  @return condition (@link Condition NXOpen.VisualReporting.Condition@endlink):  The created condition .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  to which this condition will be applied 
    def CreateNullCondition(builder: VisualReportBuilder, property: Property, value: bool, operatorType: Condition.OperatorOption) -> Condition:
        """
         Creates a new empty @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                    @link NXOpen::VisualReporting::Condition::Datatype NXOpen::VisualReporting::Condition::Datatype@endlink  is
                    @link NXOpen::VisualReporting::Property::DatatypeOptionNull NXOpen::VisualReporting::Property::DatatypeOptionNull@endlink ,
                    but does not add it to a @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
                
         @return condition (@link Condition NXOpen.VisualReporting.Condition@endlink):  The created condition .
        """
        pass
    
    ##  Creates a new empty @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink , but does not add it to a
    ##             @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
    ##         
    ##  @return condition (@link Condition NXOpen.VisualReporting.Condition@endlink):  The created condition .
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    def CreateOrCondition(builder: VisualReportBuilder) -> Condition:
        """
         Creates a new empty @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink , but does not add it to a
                    @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
                
         @return condition (@link Condition NXOpen.VisualReporting.Condition@endlink):  The created condition .
        """
        pass
    
    ##  Creates a new empty @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink , but does not add it to a
    ##             @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
    ##         
    ##  @return property (@link Property NXOpen.VisualReporting.Property@endlink):  The created property .
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    ##  Property Type of the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  being created 
    @overload
    def CreateProperty(self, builder: VisualReportBuilder, propertyType: Property.TypeOption) -> Property:
        """
         Creates a new empty @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink , but does not add it to a
                    @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
                
         @return property (@link Property NXOpen.VisualReporting.Property@endlink):  The created property .
        """
        pass
    
    ##  Creates a new empty @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink , but does not add it to a
    ##             @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
    ##         
    ##  @return createdProperty (@link Property NXOpen.VisualReporting.Property@endlink):  The created property .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  Property Identifier of the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  being created 
    @overload
    def CreateProperty(self, builder: VisualReportBuilder, propertyId: str) -> Property:
        """
         Creates a new empty @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink , but does not add it to a
                    @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
                
         @return createdProperty (@link Property NXOpen.VisualReporting.Property@endlink):  The created property .
        """
        pass
    
    ##  Creates a new empty @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
    ##             @link NXOpen::VisualReporting::Condition::Datatype NXOpen::VisualReporting::Condition::Datatype@endlink  is
    ##             @link NXOpen::VisualReporting::Property::DatatypeOptionReal NXOpen::VisualReporting::Property::DatatypeOptionReal@endlink ,
    ##             but does not add it to a @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
    ##         
    ##  @return condition (@link Condition NXOpen.VisualReporting.Condition@endlink):  The created condition .
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    ##  The @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  to which this condition will be applied 
    def CreateRealCondition(builder: VisualReportBuilder, property: Property, value: float, operatorType: Condition.OperatorOption, tolerance: float) -> Condition:
        """
         Creates a new empty @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                    @link NXOpen::VisualReporting::Condition::Datatype NXOpen::VisualReporting::Condition::Datatype@endlink  is
                    @link NXOpen::VisualReporting::Property::DatatypeOptionReal NXOpen::VisualReporting::Property::DatatypeOptionReal@endlink ,
                    but does not add it to a @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
                
         @return condition (@link Condition NXOpen.VisualReporting.Condition@endlink):  The created condition .
        """
        pass
    
    ##  Creates a new empty @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
    ##             @link NXOpen::VisualReporting::Condition::Datatype NXOpen::VisualReporting::Condition::Datatype@endlink  is
    ##             @link NXOpen::VisualReporting::Property::DatatypeOptionString NXOpen::VisualReporting::Property::DatatypeOptionString@endlink ,
    ##             but does not add it to a @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
    ##         
    ##  @return condition (@link Condition NXOpen.VisualReporting.Condition@endlink):  The created condition .
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    ##  The @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  to which this condition will be applied 
    def CreateStringCondition(builder: VisualReportBuilder, property: Property, value: str, operatorType: Condition.OperatorOption) -> Condition:
        """
         Creates a new empty @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                    @link NXOpen::VisualReporting::Condition::Datatype NXOpen::VisualReporting::Condition::Datatype@endlink  is
                    @link NXOpen::VisualReporting::Property::DatatypeOptionString NXOpen::VisualReporting::Property::DatatypeOptionString@endlink ,
                    but does not add it to a @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
                
         @return condition (@link Condition NXOpen.VisualReporting.Condition@endlink):  The created condition .
        """
        pass
    
    ##  Creates a new empty @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  and starts editing it.
    ##             The created @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  will not be added to the
    ##             @link NXOpen::VisualReporting::VisualReportManager NXOpen::VisualReporting::VisualReportManager@endlink  until @link Builder::Commit Builder::Commit@endlink 
    ##             or @link NXOpen::VisualReporting::VisualReportBuilder::CommitAsCopy NXOpen::VisualReporting::VisualReportBuilder::CommitAsCopy@endlink  is called on this builder.
    ##         
    ##  @return visualReport (@link VisualReport NXOpen.VisualReporting.VisualReport@endlink): .
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    def CreateVisualReport(builder: VisualReportBuilder) -> VisualReport:
        """
         Creates a new empty @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  and starts editing it.
                    The created @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  will not be added to the
                    @link NXOpen::VisualReporting::VisualReportManager NXOpen::VisualReporting::VisualReportManager@endlink  until @link Builder::Commit Builder::Commit@endlink 
                    or @link NXOpen::VisualReporting::VisualReportBuilder::CommitAsCopy NXOpen::VisualReporting::VisualReportBuilder::CommitAsCopy@endlink  is called on this builder.
                
         @return visualReport (@link VisualReport NXOpen.VisualReporting.VisualReport@endlink): .
        """
        pass
    
    ##  Deletes a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  from its parent condition.
    ##             If there are @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink s associated with this condition, these properties will be deleted.
    ##             If there are child conditions associated with this condtion, these child conditions will be deleted too. 
    ##         
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The condition 
    def DeleteChildCondition(builder: VisualReportBuilder, condition: Condition, childCondition: Condition) -> None:
        """
         Deletes a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  from its parent condition.
                    If there are @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink s associated with this condition, these properties will be deleted.
                    If there are child conditions associated with this condtion, these child conditions will be deleted too. 
                
        """
        pass
    
    ##  Deletes the given @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  from the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  
    ##             in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
    ##         
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    ##  The rule containing the group label 
    def DeleteGroupLabel(builder: VisualReportBuilder, rule: Rule, groupLabel: GroupLabel) -> None:
        """
         Deletes the given @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  from the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  
                    in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
                
        """
        pass
    
    ##  Delete @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  which has no owner. Before call this function,
    ##             User must be sure there is no reference to this object
    ##         
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    ##  The property to be deleted
    def DeleteProperty(builder: VisualReportBuilder, property: Property) -> None:
        """
         Delete @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  which has no owner. Before call this function,
                    User must be sure there is no reference to this object
                
        """
        pass
    
    ##  Starts editing a @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink . The builder will create a
    ##             copy of the given VisualReport and all edits will be applied to that copy. When
    ##             @link Builder::Commit Builder::Commit@endlink  is called on this builder, the supplied
    ##             VisualReport will be deleted and replaced with the new one. Alternatively if
    ##             @link NXOpen::VisualReporting::VisualReportBuilder::CommitAsCopy NXOpen::VisualReporting::VisualReportBuilder::CommitAsCopy@endlink  is called, the copied @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink 
    ##             will be added to the @link NXOpen::VisualReporting::VisualReportManager NXOpen::VisualReporting::VisualReportManager@endlink  without deleting the one given in this function.
    ## 
    ##             Any current @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  which this builder is currently
    ##             building will be deleted when this function is called.
    ##         
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    ##  The visual report 
    def EditVisualReport(builder: VisualReportBuilder, visualReport: VisualReport) -> None:
        """
         Starts editing a @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink . The builder will create a
                    copy of the given VisualReport and all edits will be applied to that copy. When
                    @link Builder::Commit Builder::Commit@endlink  is called on this builder, the supplied
                    VisualReport will be deleted and replaced with the new one. Alternatively if
                    @link NXOpen::VisualReporting::VisualReportBuilder::CommitAsCopy NXOpen::VisualReporting::VisualReportBuilder::CommitAsCopy@endlink  is called, the copied @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink 
                    will be added to the @link NXOpen::VisualReporting::VisualReportManager NXOpen::VisualReporting::VisualReportManager@endlink  without deleting the one given in this function.
        
                    Any current @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  which this builder is currently
                    building will be deleted when this function is called.
                
        """
        pass
    
    ##  Sets whether use of @link NXOpen::VisualReporting::VisualReport::UnmatchedGroupLabel NXOpen::VisualReporting::VisualReport::UnmatchedGroupLabel@endlink 
    ##             is enabled for the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this builder.
    ##         
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    ##  Whether the unmatched group is enabled 
    def EnableUnmatchedGroupOfVisualReport(builder: VisualReportBuilder, enableUnmatchedGroup: bool) -> None:
        """
         Sets whether use of @link NXOpen::VisualReporting::VisualReport::UnmatchedGroupLabel NXOpen::VisualReporting::VisualReport::UnmatchedGroupLabel@endlink 
                    is enabled for the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this builder.
                
        """
        pass
    
    ##  Gets the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink 
    ##             for a multiple properties report.
    ##         
    ##  @return activeClassifier (@link Classifier NXOpen.VisualReporting.Classifier@endlink): .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="rule"> (@link Rule NXOpen.VisualReporting.Rule@endlink) </param>
    def GetActiveClassifierOfRule(builder: VisualReportBuilder, rule: Rule) -> Classifier:
        """
         Gets the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink 
                    for a multiple properties report.
                
         @return activeClassifier (@link Classifier NXOpen.VisualReporting.Classifier@endlink): .
        """
        pass
    
    ##  Returns the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink s associated with the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  
    ##             in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
    ##         
    ##  @return groupLabels (@link GroupLabel List[NXOpen.VisualReporting.GroupLabel]@endlink):  The manually defined groups .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The rule 
    def GetAllGroupLabelsOfRule(builder: VisualReportBuilder, rule: Rule) -> List[GroupLabel]:
        """
         Returns the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink s associated with the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  
                    in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
                
         @return groupLabels (@link GroupLabel List[NXOpen.VisualReporting.GroupLabel]@endlink):  The manually defined groups .
        """
        pass
    
    ##  Gets the bitmap of the given @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
    ##         
    ##  @return bitmapName (str):  The bitmap name .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The group label 
    def GetBitmapNameOfGroupLabel(builder: VisualReportBuilder, groupLabel: GroupLabel) -> str:
        """
         Gets the bitmap of the given @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
                
         @return bitmapName (str):  The bitmap name .
        """
        pass
    
    ##  Returns the specified child @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  from this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink 
    ##         
    ##  @return childCondition (@link Condition NXOpen.VisualReporting.Condition@endlink): .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The index of the returned Condition. 
    def GetChildCondition(builder: VisualReportBuilder, condition: Condition, index: int) -> Condition:
        """
         Returns the specified child @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  from this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink 
                
         @return childCondition (@link Condition NXOpen.VisualReporting.Condition@endlink): .
        """
        pass
    
    ##  Returns all the child @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink s in this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink 
    ##         
    ##  @return childConditions (@link Condition List[NXOpen.VisualReporting.Condition]@endlink): .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="condition"> (@link Condition NXOpen.VisualReporting.Condition@endlink) </param>
    def GetChildConditions(builder: VisualReportBuilder, condition: Condition) -> List[Condition]:
        """
         Returns all the child @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink s in this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink 
                
         @return childConditions (@link Condition List[NXOpen.VisualReporting.Condition]@endlink): .
        """
        pass
    
    ##  Gets the reporting @link NXOpen::VisualReporting::Classifier::TypeOption NXOpen::VisualReporting::Classifier::TypeOption@endlink  for the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink 
    ##             in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
    ##         
    ##  @return classifierType (@link Classifier.TypeOption NXOpen.VisualReporting.Classifier.TypeOption@endlink):  The classifier type .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The rule 
    def GetClassifierTypeOfRule(builder: VisualReportBuilder, rule: Rule) -> Classifier.TypeOption:
        """
         Gets the reporting @link NXOpen::VisualReporting::Classifier::TypeOption NXOpen::VisualReporting::Classifier::TypeOption@endlink  for the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink 
                    in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
                
         @return classifierType (@link Classifier.TypeOption NXOpen.VisualReporting.Classifier.TypeOption@endlink):  The classifier type .
        """
        pass
    
    ##  Returns the @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink s associated with this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
    ##         
    ##  @return classifiers (@link Classifier List[NXOpen.VisualReporting.Classifier]@endlink): .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="rule"> (@link Rule NXOpen.VisualReporting.Rule@endlink) </param>
    def GetClassifiersOfRule(builder: VisualReportBuilder, rule: Rule) -> List[Classifier]:
        """
         Returns the @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink s associated with this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
                
         @return classifiers (@link Classifier List[NXOpen.VisualReporting.Classifier]@endlink): .
        """
        pass
    
    ##  Gets the @link NXOpen::VisualReporting::GroupLabel::Color NXOpen::VisualReporting::GroupLabel::Color@endlink 
    ##             of the given @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink . 
    ##         
    ##  @return color (@link NXOpen.NXColor.Rgb NXOpen.NXColor.Rgb@endlink):  The color .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The group label 
    def GetColorOfGroupLabel(builder: VisualReportBuilder, groupLabel: GroupLabel) -> NXOpen.NXColor.Rgb:
        """
         Gets the @link NXOpen::VisualReporting::GroupLabel::Color NXOpen::VisualReporting::GroupLabel::Color@endlink 
                    of the given @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink . 
                
         @return color (@link NXOpen.NXColor.Rgb NXOpen.NXColor.Rgb@endlink):  The color .
        """
        pass
    
    ##  Gets the custom message of the given@link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
    ##         
    ##  @return customMessage (str):  The bitmap name .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The group label 
    def GetCustomMessageOfGroupLabel(builder: VisualReportBuilder, groupLabel: GroupLabel) -> str:
        """
         Gets the custom message of the given@link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
                
         @return customMessage (str):  The bitmap name .
        """
        pass
    
    ##  Gets the @link NXOpen::VisualReporting::Classifier::DateGroupMethodOption NXOpen::VisualReporting::Classifier::DateGroupMethodOption@endlink  of the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  
    ##             in the given @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink . 
    ##             
    ##             Only valid if the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  in the rule 
    ##             is @link NXOpen::VisualReporting::Classifier::TypeOptionRange NXOpen::VisualReporting::Classifier::TypeOptionRange@endlink  type.
    ##         
    ##  @return dateGroupMethod (@link Classifier.DateGroupMethodOption NXOpen.VisualReporting.Classifier.DateGroupMethodOption@endlink):  The range method .
    ## 
    ##   <br>  Created in NX8.0.1  <br> 

    ## License requirements: None.
    ##  The rule 
    def GetDateGroupMethodOfRule(builder: VisualReportBuilder, rule: Rule) -> Classifier.DateGroupMethodOption:
        """
         Gets the @link NXOpen::VisualReporting::Classifier::DateGroupMethodOption NXOpen::VisualReporting::Classifier::DateGroupMethodOption@endlink  of the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  
                    in the given @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink . 
                    
                    Only valid if the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  in the rule 
                    is @link NXOpen::VisualReporting::Classifier::TypeOptionRange NXOpen::VisualReporting::Classifier::TypeOptionRange@endlink  type.
                
         @return dateGroupMethod (@link Classifier.DateGroupMethodOption NXOpen.VisualReporting.Classifier.DateGroupMethodOption@endlink):  The range method .
        """
        pass
    
    ##  Gets the @link NXOpen::VisualReporting::Condition::Description NXOpen::VisualReporting::Condition::Description@endlink  of the
    ##             specified @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .
    ##             Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
    ##             @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
    ##         
    ##  @return description (str):  The description .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The condition 
    def GetDescriptionOfCondition(builder: VisualReportBuilder, condition: Condition) -> str:
        """
         Gets the @link NXOpen::VisualReporting::Condition::Description NXOpen::VisualReporting::Condition::Description@endlink  of the
                    specified @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .
                    Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                    @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                
         @return description (str):  The description .
        """
        pass
    
    ##  Gets the @link NXOpen::VisualReporting::GroupLabel::DisplayStyleOption NXOpen::VisualReporting::GroupLabel::DisplayStyleOption@endlink  
    ##             of the given @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  
    ##         
    ##  @return displayStyle (@link GroupLabel.DisplayStyleOption NXOpen.VisualReporting.GroupLabel.DisplayStyleOption@endlink):  The display style .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The group label 
    def GetDisplayStyleForGroupLabel(builder: VisualReportBuilder, groupLabel: GroupLabel) -> GroupLabel.DisplayStyleOption:
        """
         Gets the @link NXOpen::VisualReporting::GroupLabel::DisplayStyleOption NXOpen::VisualReporting::GroupLabel::DisplayStyleOption@endlink  
                    of the given @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  
                
         @return displayStyle (@link GroupLabel.DisplayStyleOption NXOpen.VisualReporting.GroupLabel.DisplayStyleOption@endlink):  The display style .
        """
        pass
    
    ##  Gets the error level of the given@link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
    ##         
    ##  @return errorLevel (@link NXOpen.Validation.Result NXOpen.Validation.Result@endlink):  The error level .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  The group label 
    def GetErrorLevelOfGroupLabel(builder: VisualReportBuilder, groupLabel: GroupLabel) -> NXOpen.Validation.Result:
        """
         Gets the error level of the given@link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
                
         @return errorLevel (@link NXOpen.Validation.Result NXOpen.Validation.Result@endlink):  The error level .
        """
        pass
    
    ##  Gets the filter @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  from this rule. 
    ##         
    ##  @return filterCondition (@link Condition NXOpen.VisualReporting.Condition@endlink):  The filter condition .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The rule 
    def GetFilterConditionOfRule(builder: VisualReportBuilder, rule: Rule) -> Condition:
        """
         Gets the filter @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  from this rule. 
                
         @return filterCondition (@link Condition NXOpen.VisualReporting.Condition@endlink):  The filter condition .
        """
        pass
    
    ##  Gets the @link NXOpen::VisualReporting::Classifier::GroupingMethodOption NXOpen::VisualReporting::Classifier::GroupingMethodOption@endlink  of the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink 
    ##             in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
    ##         
    ##  @return groupingMethod (@link Classifier.GroupingMethodOption NXOpen.VisualReporting.Classifier.GroupingMethodOption@endlink):  The grouping method .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The rule 
    def GetGroupingMethodOfRule(builder: VisualReportBuilder, rule: Rule) -> Classifier.GroupingMethodOption:
        """
         Gets the @link NXOpen::VisualReporting::Classifier::GroupingMethodOption NXOpen::VisualReporting::Classifier::GroupingMethodOption@endlink  of the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink 
                    in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
                
         @return groupingMethod (@link Classifier.GroupingMethodOption NXOpen.VisualReporting.Classifier.GroupingMethodOption@endlink):  The grouping method .
        """
        pass
    
    ##  Gets @link NXOpen::VisualReporting::Condition::HasUserSpecifiedValue NXOpen::VisualReporting::Condition::HasUserSpecifiedValue@endlink  on the
    ##             specified @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .
    ##             Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
    ##             @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
    ##         
    ##  @return isUserSpecified (bool):  Whether the condition's value should be user-specified .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The condition 
    def GetHasUserSpecifiedValueForCondition(builder: VisualReportBuilder, condition: Condition) -> bool:
        """
         Gets @link NXOpen::VisualReporting::Condition::HasUserSpecifiedValue NXOpen::VisualReporting::Condition::HasUserSpecifiedValue@endlink  on the
                    specified @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .
                    Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                    @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                
         @return isUserSpecified (bool):  Whether the condition's value should be user-specified .
        """
        pass
    
    ##  Gets the @link NXOpen::VisualReporting::GroupLabel::LowerBound NXOpen::VisualReporting::GroupLabel::LowerBound@endlink 
    ##             of the given @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
    ##         
    ##  @return lowerBound (str):  The lower bound .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The group label 
    def GetLowerBoundOfGroupLabel(builder: VisualReportBuilder, groupLabel: GroupLabel) -> str:
        """
         Gets the @link NXOpen::VisualReporting::GroupLabel::LowerBound NXOpen::VisualReporting::GroupLabel::LowerBound@endlink 
                    of the given @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
                
         @return lowerBound (str):  The lower bound .
        """
        pass
    
    ##  Returns the specified @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink s associated with the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  
    ##             in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink  which are manually defined.
    ##         
    ##  @return groupLabel (@link GroupLabel NXOpen.VisualReporting.GroupLabel@endlink):  The specified manually defined group .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The rule 
    def GetManualGroupLabelOfRule(builder: VisualReportBuilder, rule: Rule, index: int) -> GroupLabel:
        """
         Returns the specified @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink s associated with the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  
                    in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink  which are manually defined.
                
         @return groupLabel (@link GroupLabel NXOpen.VisualReporting.GroupLabel@endlink):  The specified manually defined group .
        """
        pass
    
    ##  Returns the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink s associated with the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  
    ##             in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink  which are manually defined.
    ##         
    ##  @return groupLabels (@link GroupLabel List[NXOpen.VisualReporting.GroupLabel]@endlink):  The manually defined groups .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The rule 
    def GetManualGroupLabelsOfRule(builder: VisualReportBuilder, rule: Rule) -> List[GroupLabel]:
        """
         Returns the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink s associated with the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  
                    in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink  which are manually defined.
                
         @return groupLabels (@link GroupLabel List[NXOpen.VisualReporting.GroupLabel]@endlink):  The manually defined groups .
        """
        pass
    
    ##  Gets whether the @link NXOpen::VisualReporting::Classifier::GroupingMethodOption NXOpen::VisualReporting::Classifier::GroupingMethodOption@endlink  of the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink 
    ##             in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink  is @link NXOpen::VisualReporting::Classifier::GroupingMethodOptionManual NXOpen::VisualReporting::Classifier::GroupingMethodOptionManual@endlink . 
    ##         
    ##  @return isManualGrouping (bool):  Whether manual grouping should be used .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The rule 
    def GetManualGroupingForRule(builder: VisualReportBuilder, rule: Rule) -> bool:
        """
         Gets whether the @link NXOpen::VisualReporting::Classifier::GroupingMethodOption NXOpen::VisualReporting::Classifier::GroupingMethodOption@endlink  of the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink 
                    in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink  is @link NXOpen::VisualReporting::Classifier::GroupingMethodOptionManual NXOpen::VisualReporting::Classifier::GroupingMethodOptionManual@endlink . 
                
         @return isManualGrouping (bool):  Whether manual grouping should be used .
        """
        pass
    
    ##  Gets the @link NXOpen::VisualReporting::VisualReport::ObjectTypeOption NXOpen::VisualReporting::VisualReport::ObjectTypeOption@endlink s of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this builder.
    ##             Only valid if the @link NXOpen::VisualReporting::VisualReport::ScopeType NXOpen::VisualReporting::VisualReport::ScopeType@endlink  of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink 
    ##             is @link NXOpen::VisualReporting::VisualReport::ScopeTypeOptionSubPart NXOpen::VisualReporting::VisualReport::ScopeTypeOptionSubPart@endlink  type.
    ##         
    ##  @return objectTypes (@link VisualReport.ObjectTypeOption List[NXOpen.VisualReporting.VisualReport.ObjectTypeOption]@endlink):  The object types .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetObjectTypesOfVisualReport(builder: VisualReportBuilder) -> List[VisualReport.ObjectTypeOption]:
        """
         Gets the @link NXOpen::VisualReporting::VisualReport::ObjectTypeOption NXOpen::VisualReporting::VisualReport::ObjectTypeOption@endlink s of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this builder.
                    Only valid if the @link NXOpen::VisualReporting::VisualReport::ScopeType NXOpen::VisualReporting::VisualReport::ScopeType@endlink  of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink 
                    is @link NXOpen::VisualReporting::VisualReport::ScopeTypeOptionSubPart NXOpen::VisualReporting::VisualReport::ScopeTypeOptionSubPart@endlink  type.
                
         @return objectTypes (@link VisualReport.ObjectTypeOption List[NXOpen.VisualReporting.VisualReport.ObjectTypeOption]@endlink):  The object types .
        """
        pass
    
    ##  Gets the @link NXOpen::VisualReporting::Condition::OperatorOption NXOpen::VisualReporting::Condition::OperatorOption@endlink  of this condition. Only valid if
    ##             @link NXOpen::VisualReporting::Condition::TypeOption NXOpen::VisualReporting::Condition::TypeOption@endlink  is
    ##             @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
    ##         
    ##  @return operatorType (@link Condition.OperatorOption NXOpen.VisualReporting.Condition.OperatorOption@endlink):  The operator type being set .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The condition 
    def GetOperatorTypeOfCondition(builder: VisualReportBuilder, condition: Condition) -> Condition.OperatorOption:
        """
         Gets the @link NXOpen::VisualReporting::Condition::OperatorOption NXOpen::VisualReporting::Condition::OperatorOption@endlink  of this condition. Only valid if
                    @link NXOpen::VisualReporting::Condition::TypeOption NXOpen::VisualReporting::Condition::TypeOption@endlink  is
                    @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                
         @return operatorType (@link Condition.OperatorOption NXOpen.VisualReporting.Condition.OperatorOption@endlink):  The operator type being set .
        """
        pass
    
    ##  Gets the parent condition of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink . If this
    ##             condition has no parent or if the parent isn't a condition
    ##             then this returns NULL.
    ##         
    ##  @return parentCondition (@link Condition NXOpen.VisualReporting.Condition@endlink): .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="condition"> (@link Condition NXOpen.VisualReporting.Condition@endlink) </param>
    def GetParentCondition(builder: VisualReportBuilder, condition: Condition) -> Condition:
        """
         Gets the parent condition of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink . If this
                    condition has no parent or if the parent isn't a condition
                    then this returns NULL.
                
         @return parentCondition (@link Condition NXOpen.VisualReporting.Condition@endlink): .
        """
        pass
    
    ##  Gets the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  in the value for comparison of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink . 
    ##         
    ##  @return property (@link Property NXOpen.VisualReporting.Property@endlink):  The property .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The condition 
    def GetPropertyForComparison(builder: VisualReportBuilder, condition: Condition) -> Property:
        """
         Gets the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  in the value for comparison of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink . 
                
         @return property (@link Property NXOpen.VisualReporting.Property@endlink):  The property .
        """
        pass
    
    ##  Gets the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  of this condition. 
    ##             Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
    ##             @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
    ##         
    ##  @return property (@link Property NXOpen.VisualReporting.Property@endlink):  The property .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The condition 
    def GetPropertyOfCondition(builder: VisualReportBuilder, condition: Condition) -> Property:
        """
         Gets the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  of this condition. 
                    Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                    @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                
         @return property (@link Property NXOpen.VisualReporting.Property@endlink):  The property .
        """
        pass
    
    ##  Gets the property specification of the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  being built by this builder.
    ##         
    ##  @return A tuple consisting of (propertyType, key, name). 
    ##  - propertyType is: @link Property.TypeOption NXOpen.VisualReporting.Property.TypeOption@endlink. Property Type of the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  .
    ##  - key is: str. property key .
    ##  - name is: str. property name .

    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The property being ask 
    @staticmethod
    def GetPropertySpecification(builder: VisualReportBuilder, property: Property) -> Tuple[Property.TypeOption, str, str]:
        """
         Gets the property specification of the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  being built by this builder.
                
         @return A tuple consisting of (propertyType, key, name). 
         - propertyType is: @link Property.TypeOption NXOpen.VisualReporting.Property.TypeOption@endlink. Property Type of the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  .
         - key is: str. property key .
         - name is: str. property name .

        """
        pass
    
    ##  Gets the @link NXOpen::VisualReporting::Classifier::RangeMethodOption NXOpen::VisualReporting::Classifier::RangeMethodOption@endlink  of the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  
    ##             in the given @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink . 
    ##             
    ##             Only valid if the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  in the rule 
    ##             is @link NXOpen::VisualReporting::Classifier::TypeOptionRange NXOpen::VisualReporting::Classifier::TypeOptionRange@endlink  type.
    ##         
    ##  @return rangeMethod (@link Classifier.RangeMethodOption NXOpen.VisualReporting.Classifier.RangeMethodOption@endlink):  The range method .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The rule 
    def GetRangeMethodOfRule(builder: VisualReportBuilder, rule: Rule) -> Classifier.RangeMethodOption:
        """
         Gets the @link NXOpen::VisualReporting::Classifier::RangeMethodOption NXOpen::VisualReporting::Classifier::RangeMethodOption@endlink  of the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  
                    in the given @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink . 
                    
                    Only valid if the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  in the rule 
                    is @link NXOpen::VisualReporting::Classifier::TypeOptionRange NXOpen::VisualReporting::Classifier::TypeOptionRange@endlink  type.
                
         @return rangeMethod (@link Classifier.RangeMethodOption NXOpen.VisualReporting.Classifier.RangeMethodOption@endlink):  The range method .
        """
        pass
    
    ## Gets the message @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink   list of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink . 
    ##         
    ##  @return A tuple consisting of (properties, usages, notUsed). 
    ##  - properties is: @link Property List[NXOpen.VisualReporting.Property]@endlink. The reference properties of report.
    ##  - usages is: @link VisualReportBuilder.PropertyUsageOption List[NXOpen.VisualReporting.VisualReportBuilder.PropertyUsageOption]@endlink. The usages of report.
    ##  - notUsed is: int.

    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetReferencePropertiesOfReport(builder: VisualReportBuilder) -> Tuple[List[Property], List[VisualReportBuilder.PropertyUsageOption], int]:
        """
        Gets the message @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink   list of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink . 
                
         @return A tuple consisting of (properties, usages, notUsed). 
         - properties is: @link Property List[NXOpen.VisualReporting.Property]@endlink. The reference properties of report.
         - usages is: @link VisualReportBuilder.PropertyUsageOption List[NXOpen.VisualReporting.VisualReportBuilder.PropertyUsageOption]@endlink. The usages of report.
         - notUsed is: int.

        """
        pass
    
    ##  Gets the message @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink   list of the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink 
    ##             in the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink . 
    ##         
    ##  @return A tuple consisting of (properties, usages). 
    ##  - properties is: @link Property List[NXOpen.VisualReporting.Property]@endlink. The reference properties of property.
    ##  - usages is: @link VisualReportBuilder.PropertyUsageOption List[NXOpen.VisualReporting.VisualReportBuilder.PropertyUsageOption]@endlink. The usages .

    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetReferencePropertiesOfReportingProperty(builder: VisualReportBuilder) -> Tuple[List[Property], List[VisualReportBuilder.PropertyUsageOption]]:
        """
         Gets the message @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink   list of the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink 
                    in the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink . 
                
         @return A tuple consisting of (properties, usages). 
         - properties is: @link Property List[NXOpen.VisualReporting.Property]@endlink. The reference properties of property.
         - usages is: @link VisualReportBuilder.PropertyUsageOption List[NXOpen.VisualReporting.VisualReportBuilder.PropertyUsageOption]@endlink. The usages .

        """
        pass
    
    ##  Gets the @link NXOpen::VisualReporting::Property::DatatypeOption NXOpen::VisualReporting::Property::DatatypeOption@endlink  of the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink 's reporting @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink 
    ##             in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
    ##         
    ##  @return datatype (@link Property.DatatypeOption NXOpen.VisualReporting.Property.DatatypeOption@endlink):  The datatype.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The rule 
    def GetReportingDatatypeOfRule(builder: VisualReportBuilder, rule: Rule) -> Property.DatatypeOption:
        """
         Gets the @link NXOpen::VisualReporting::Property::DatatypeOption NXOpen::VisualReporting::Property::DatatypeOption@endlink  of the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink 's reporting @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink 
                    in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
                
         @return datatype (@link Property.DatatypeOption NXOpen.VisualReporting.Property.DatatypeOption@endlink):  The datatype.
        """
        pass
    
    ##  Gets the reporting @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  for the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink 
    ##             in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
    ##         
    ##  @return reportingProperty (@link Property NXOpen.VisualReporting.Property@endlink):  The property .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The rule 
    def GetReportingPropertyOfRule(builder: VisualReportBuilder, rule: Rule) -> Property:
        """
         Gets the reporting @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  for the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink 
                    in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
                
         @return reportingProperty (@link Property NXOpen.VisualReporting.Property@endlink):  The property .
        """
        pass
    
    ##  Return the specified @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink  from the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink 
    ##             being built by this builder.
    ##         
    ##  @return rule (@link Rule NXOpen.VisualReporting.Rule@endlink): .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The index of the returned @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink . 
    def GetRule(builder: VisualReportBuilder, index: int) -> Rule:
        """
         Return the specified @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink  from the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink 
                    being built by this builder.
                
         @return rule (@link Rule NXOpen.VisualReporting.Rule@endlink): .
        """
        pass
    
    ##  Returns all the @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink s in the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  
    ##             being built by this builder.
    ##         
    ##  @return rules (@link Rule List[NXOpen.VisualReporting.Rule]@endlink): .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetRules(builder: VisualReportBuilder) -> List[Rule]:
        """
         Returns all the @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink s in the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  
                    being built by this builder.
                
         @return rules (@link Rule List[NXOpen.VisualReporting.Rule]@endlink): .
        """
        pass
    
    ##  Gets the priority of the given@link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
    ##         
    ##  @return tagPriority (@link GroupLabel.TagPriorityOption NXOpen.VisualReporting.GroupLabel.TagPriorityOption@endlink):  The priority .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The group label 
    def GetTagPriorityOfGroupLabel(builder: VisualReportBuilder, groupLabel: GroupLabel) -> GroupLabel.TagPriorityOption:
        """
         Gets the priority of the given@link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
                
         @return tagPriority (@link GroupLabel.TagPriorityOption NXOpen.VisualReporting.GroupLabel.TagPriorityOption@endlink):  The priority .
        """
        pass
    
    ##  Gets the tolerance of the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  in the given @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink 
    ## 
    ##             Only valid if the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  in the rule 
    ##             is @link NXOpen::VisualReporting::Classifier::TypeOptionValue NXOpen::VisualReporting::Classifier::TypeOptionValue@endlink  type.
    ##         
    ##  @return tolerance (float):  The tolerance value .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  The rule 
    def GetToleranceOfRule(builder: VisualReportBuilder, rule: Rule) -> float:
        """
         Gets the tolerance of the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  in the given @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink 
        
                    Only valid if the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  in the rule 
                    is @link NXOpen::VisualReporting::Classifier::TypeOptionValue NXOpen::VisualReporting::Classifier::TypeOptionValue@endlink  type.
                
         @return tolerance (float):  The tolerance value .
        """
        pass
    
    ##  Gets the @link NXOpen::VisualReporting::GroupLabel::UpperBound NXOpen::VisualReporting::GroupLabel::UpperBound@endlink 
    ##             of the given @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
    ##         
    ##  @return upperBound (str):  The upper bound .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The group label 
    def GetUpperBoundOfGroupLabel(builder: VisualReportBuilder, groupLabel: GroupLabel) -> str:
        """
         Gets the @link NXOpen::VisualReporting::GroupLabel::UpperBound NXOpen::VisualReporting::GroupLabel::UpperBound@endlink 
                    of the given @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
                
         @return upperBound (str):  The upper bound .
        """
        pass
    
    ##  Gets the @link NXOpen::NXObject::Name NXOpen::NXObject::Name@endlink 
    ##             of the given @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink . 
    ##         
    ##  @return name (str):  The name .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The group label 
    def GetUserNameOfGroupLabel(builder: VisualReportBuilder, groupLabel: GroupLabel) -> str:
        """
         Gets the @link NXOpen::NXObject::Name NXOpen::NXObject::Name@endlink 
                    of the given @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink . 
                
         @return name (str):  The name .
        """
        pass
    
    ##  Gets the @link NXOpen::VisualReporting::Condition::UserPrompt NXOpen::VisualReporting::Condition::UserPrompt@endlink  of the
    ##             specified @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .
    ##             Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
    ##             @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
    ##         
    ##  @return userPrompt (str):  The user-prompt  .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The condition 
    def GetUserPromptOfCondition(builder: VisualReportBuilder, condition: Condition) -> str:
        """
         Gets the @link NXOpen::VisualReporting::Condition::UserPrompt NXOpen::VisualReporting::Condition::UserPrompt@endlink  of the
                    specified @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .
                    Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                    @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                
         @return userPrompt (str):  The user-prompt  .
        """
        pass
    
    ##  Gets the value of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink . 
    ##             Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
    ##             @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
    ##         
    ##  @return value (str): .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="condition"> (@link Condition NXOpen.VisualReporting.Condition@endlink) </param>
    def GetValueOfCondition(builder: VisualReportBuilder, condition: Condition) -> str:
        """
         Gets the value of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink . 
                    Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                    @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                
         @return value (str): .
        """
        pass
    
    ##  Gets the @link NXOpen::VisualReporting::GroupLabel::Value NXOpen::VisualReporting::GroupLabel::Value@endlink 
    ##             of the given @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
    ##         
    ##  @return value (str):  The value .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The group label 
    def GetValueOfGroupLabel(builder: VisualReportBuilder, groupLabel: GroupLabel) -> str:
        """
         Gets the @link NXOpen::VisualReporting::GroupLabel::Value NXOpen::VisualReporting::GroupLabel::Value@endlink 
                    of the given @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
                
         @return value (str):  The value .
        """
        pass
    
    ##  Returns whether the given @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  is an immediate child of this condition
    ##         
    ##  @return isChild (bool): .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The possible child Condition 
    def IsChildCondition(builder: VisualReportBuilder, condition: Condition, childCondition: Condition) -> bool:
        """
         Returns whether the given @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  is an immediate child of this condition
                
         @return isChild (bool): .
        """
        pass
    
    ##  Removes a condition from its parent condition. If the condition has an associated @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink 
    ##             that will be deleted too. If the condition has any child conditions, those will all
    ##             be deleted too.
    ##         
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    ##  The condition 
    def RemoveChildFromCondition(builder: VisualReportBuilder, condition: Condition, childCondition: Condition) -> None:
        """
         Removes a condition from its parent condition. If the condition has an associated @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink 
                    that will be deleted too. If the condition has any child conditions, those will all
                    be deleted too.
                
        """
        pass
    
    ##  Removes any existing filter @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  from this rule. This will not delete
    ##             the condition.
    ##         
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    ##  The rule 
    def RemoveFilterConditionFromRule(builder: VisualReportBuilder, rule: Rule) -> None:
        """
         Removes any existing filter @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  from this rule. This will not delete
                    the condition.
                
        """
        pass
    
    ##  Removes the current @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  from this condition
    ##             without deleting it.
    ##         
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    ##  The condition 
    def RemovePropertyFromCondition(builder: VisualReportBuilder, condition: Condition) -> None:
        """
         Removes the current @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  from this condition
                    without deleting it.
                
        """
        pass
    
    ##  Saves the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  to its current @link NXOpen::VisualReporting::VisualReportBuilder::FilenameOfVisualReport NXOpen::VisualReporting::VisualReportBuilder::FilenameOfVisualReport@endlink  .
    ## 
    ##             Note that when NX is connected to Teamcenter, the @link NXOpen::VisualReporting::VisualReportBuilder::FilenameOfVisualReport NXOpen::VisualReporting::VisualReportBuilder::FilenameOfVisualReport@endlink  will be 
    ##             updated to the report dataset identifier after the report is saved to Teamcenter database.
    ##         
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Save(builder: VisualReportBuilder) -> None:
        """
         Saves the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  to its current @link NXOpen::VisualReporting::VisualReportBuilder::FilenameOfVisualReport NXOpen::VisualReporting::VisualReportBuilder::FilenameOfVisualReport@endlink  .
        
                    Note that when NX is connected to Teamcenter, the @link NXOpen::VisualReporting::VisualReportBuilder::FilenameOfVisualReport NXOpen::VisualReporting::VisualReportBuilder::FilenameOfVisualReport@endlink  will be 
                    updated to the report dataset identifier after the report is saved to Teamcenter database.
                
        """
        pass
    
    ##  Sets the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink 
    ##             for a multiple properties report.
    ##         
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="rule"> (@link Rule NXOpen.VisualReporting.Rule@endlink) </param>
    ## <param name="activeClassifier"> (@link Classifier NXOpen.VisualReporting.Classifier@endlink) </param>
    def SetActiveClassifierOfRule(builder: VisualReportBuilder, rule: Rule, activeClassifier: Classifier) -> None:
        """
         Sets the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink 
                    for a multiple properties report.
                
        """
        pass
    
    ##  Sets the bitmap of the given @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
    ##         
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The group label 
    def SetBitmapNameOfGroupLabel(builder: VisualReportBuilder, groupLabel: GroupLabel, bitmapName: str) -> None:
        """
         Sets the bitmap of the given @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
                
        """
        pass
    
    ##  Sets the reporting @link NXOpen::VisualReporting::Classifier::TypeOption NXOpen::VisualReporting::Classifier::TypeOption@endlink  for the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink 
    ##             in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
    ## 
    ##             Note that the old @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink  will be deleted 
    ##             and a new @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  will be created and set as the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink 
    ##             in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
    ##         
    ##  @return newClassifier (@link Classifier NXOpen.VisualReporting.Classifier@endlink):  The new active classifier .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The rule 
    def SetClassifierTypeOfRule(builder: VisualReportBuilder, rule: Rule, classifierType: Classifier.TypeOption) -> Classifier:
        """
         Sets the reporting @link NXOpen::VisualReporting::Classifier::TypeOption NXOpen::VisualReporting::Classifier::TypeOption@endlink  for the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink 
                    in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
        
                    Note that the old @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink  will be deleted 
                    and a new @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  will be created and set as the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink 
                    in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
                
         @return newClassifier (@link Classifier NXOpen.VisualReporting.Classifier@endlink):  The new active classifier .
        """
        pass
    
    ##  Sets the @link NXOpen::VisualReporting::GroupLabel::Color NXOpen::VisualReporting::GroupLabel::Color@endlink 
    ##             of the given @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink . This also changes
    ##             @link NXOpen::VisualReporting::GroupLabel::DisplayStyle NXOpen::VisualReporting::GroupLabel::DisplayStyle@endlink 
    ##             to @link NXOpen::VisualReporting::GroupLabel::DisplayStyleOptionSpecifiedColor NXOpen::VisualReporting::GroupLabel::DisplayStyleOptionSpecifiedColor@endlink .
    ##         
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    ##  The group label 
    def SetColorOfGroupLabel(builder: VisualReportBuilder, groupLabel: GroupLabel, color: NXOpen.NXColor.Rgb) -> None:
        """
         Sets the @link NXOpen::VisualReporting::GroupLabel::Color NXOpen::VisualReporting::GroupLabel::Color@endlink 
                    of the given @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink . This also changes
                    @link NXOpen::VisualReporting::GroupLabel::DisplayStyle NXOpen::VisualReporting::GroupLabel::DisplayStyle@endlink 
                    to @link NXOpen::VisualReporting::GroupLabel::DisplayStyleOptionSpecifiedColor NXOpen::VisualReporting::GroupLabel::DisplayStyleOptionSpecifiedColor@endlink .
                
        """
        pass
    
    ##  Sets the custom message of the given @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
    ##         
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The group label 
    def SetCustomMessageOfGroupLabel(builder: VisualReportBuilder, groupLabel: GroupLabel, customMessage: str) -> None:
        """
         Sets the custom message of the given @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
                
        """
        pass
    
    ##  Sets the @link NXOpen::VisualReporting::Classifier::DateGroupMethodOption NXOpen::VisualReporting::Classifier::DateGroupMethodOption@endlink  of the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  
    ##             in the given @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink . 
    ##             
    ##             Only valid if the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  in the rule 
    ##             is @link NXOpen::VisualReporting::Classifier::TypeOptionRange NXOpen::VisualReporting::Classifier::TypeOptionRange@endlink  type.
    ##         
    ## 
    ##   <br>  Created in NX8.0.1  <br> 

    ## License requirements: None.
    ##  The rule 
    def SetDateGroupMethodOfRule(builder: VisualReportBuilder, rule: Rule, dateGroupMethod: Classifier.DateGroupMethodOption) -> None:
        """
         Sets the @link NXOpen::VisualReporting::Classifier::DateGroupMethodOption NXOpen::VisualReporting::Classifier::DateGroupMethodOption@endlink  of the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  
                    in the given @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink . 
                    
                    Only valid if the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  in the rule 
                    is @link NXOpen::VisualReporting::Classifier::TypeOptionRange NXOpen::VisualReporting::Classifier::TypeOptionRange@endlink  type.
                
        """
        pass
    
    ##  Sets the @link NXOpen::VisualReporting::Condition::Description NXOpen::VisualReporting::Condition::Description@endlink  of the
    ##             specified @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .
    ##             Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
    ##             @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
    ##         
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    ##  The condition 
    def SetDescriptionOfCondition(builder: VisualReportBuilder, condition: Condition, description: str) -> None:
        """
         Sets the @link NXOpen::VisualReporting::Condition::Description NXOpen::VisualReporting::Condition::Description@endlink  of the
                    specified @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .
                    Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                    @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                
        """
        pass
    
    ##  Sets the @link NXOpen::VisualReporting::GroupLabel::DisplayStyleOption NXOpen::VisualReporting::GroupLabel::DisplayStyleOption@endlink  
    ##             of the given @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  
    ##         
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The group label 
    def SetDisplayStyleForGroupLabel(builder: VisualReportBuilder, groupLabel: GroupLabel, displayStyle: GroupLabel.DisplayStyleOption) -> None:
        """
         Sets the @link NXOpen::VisualReporting::GroupLabel::DisplayStyleOption NXOpen::VisualReporting::GroupLabel::DisplayStyleOption@endlink  
                    of the given @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  
                
        """
        pass
    
    ##  Sets the priority of the given@link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
    ##         
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  The group label 
    def SetErrorLevelOfGroupLabel(builder: VisualReportBuilder, groupLabel: GroupLabel, errorLevel: NXOpen.Validation.Result) -> None:
        """
         Sets the priority of the given@link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
                
        """
        pass
    
    ##  Sets the filter @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  from this rule. Setting this will delete
    ##             any existing @link NXOpen::VisualReporting::Rule::FilterCondition NXOpen::VisualReporting::Rule::FilterCondition@endlink  and all of its children
    ##             (except it won't delete the replacement @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  being set
    ##             by this call).
    ##         
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    ##  The rule 
    def SetFilterConditionOfRule(builder: VisualReportBuilder, rule: Rule, filterCondition: Condition) -> None:
        """
         Sets the filter @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  from this rule. Setting this will delete
                    any existing @link NXOpen::VisualReporting::Rule::FilterCondition NXOpen::VisualReporting::Rule::FilterCondition@endlink  and all of its children
                    (except it won't delete the replacement @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  being set
                    by this call).
                
        """
        pass
    
    ##  Sets the @link NXOpen::VisualReporting::Classifier::GroupingMethodOption NXOpen::VisualReporting::Classifier::GroupingMethodOption@endlink  of the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  
    ##             in the given @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
    ##             If the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  uses manual grouping then no @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink s 
    ##             will be automatically generated, and they should instead be added using @link NXOpen::VisualReporting::VisualReportBuilder::CreateGroupLabel NXOpen::VisualReporting::VisualReportBuilder::CreateGroupLabel@endlink .
    ##         
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The rule 
    def SetGroupingMethodOfRule(builder: VisualReportBuilder, rule: Rule, groupingMethod: Classifier.GroupingMethodOption) -> None:
        """
         Sets the @link NXOpen::VisualReporting::Classifier::GroupingMethodOption NXOpen::VisualReporting::Classifier::GroupingMethodOption@endlink  of the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  
                    in the given @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
                    If the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  uses manual grouping then no @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink s 
                    will be automatically generated, and they should instead be added using @link NXOpen::VisualReporting::VisualReportBuilder::CreateGroupLabel NXOpen::VisualReporting::VisualReportBuilder::CreateGroupLabel@endlink .
                
        """
        pass
    
    ##  Sets @link NXOpen::VisualReporting::Condition::HasUserSpecifiedValue NXOpen::VisualReporting::Condition::HasUserSpecifiedValue@endlink  on the
    ##             specified @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .
    ##             Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
    ##             @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
    ##         
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    ##  The condition 
    def SetHasUserSpecifiedValueForCondition(builder: VisualReportBuilder, condition: Condition, isUserSpecified: bool) -> None:
        """
         Sets @link NXOpen::VisualReporting::Condition::HasUserSpecifiedValue NXOpen::VisualReporting::Condition::HasUserSpecifiedValue@endlink  on the
                    specified @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .
                    Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                    @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                
        """
        pass
    
    ##  Sets the @link NXOpen::VisualReporting::GroupLabel::LowerBound NXOpen::VisualReporting::GroupLabel::LowerBound@endlink 
    ##             of the given @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
    ##         
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The group label 
    def SetLowerBoundOfGroupLabel(builder: VisualReportBuilder, groupLabel: GroupLabel, lowerBound: str) -> None:
        """
         Sets the @link NXOpen::VisualReporting::GroupLabel::LowerBound NXOpen::VisualReporting::GroupLabel::LowerBound@endlink 
                    of the given @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
                
        """
        pass
    
    ##  Sets whether the @link NXOpen::VisualReporting::Classifier::GroupingMethodOption NXOpen::VisualReporting::Classifier::GroupingMethodOption@endlink  of the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink 
    ##             in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink  is @link NXOpen::VisualReporting::Classifier::GroupingMethodOptionManual NXOpen::VisualReporting::Classifier::GroupingMethodOptionManual@endlink . 
    ##             If it uses @link NXOpen::VisualReporting::Classifier::GroupingMethodOptionManual NXOpen::VisualReporting::Classifier::GroupingMethodOptionManual@endlink , then no
    ##             @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink s will be automatically generated, and they should
    ##             instead be added manually as required using @link NXOpen::VisualReporting::VisualReportBuilder::CreateGroupLabel NXOpen::VisualReporting::VisualReportBuilder::CreateGroupLabel@endlink .
    ##         
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    ##  The rule 
    def SetManualGroupingForRule(builder: VisualReportBuilder, rule: Rule, isManualGrouping: bool) -> None:
        """
         Sets whether the @link NXOpen::VisualReporting::Classifier::GroupingMethodOption NXOpen::VisualReporting::Classifier::GroupingMethodOption@endlink  of the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink 
                    in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink  is @link NXOpen::VisualReporting::Classifier::GroupingMethodOptionManual NXOpen::VisualReporting::Classifier::GroupingMethodOptionManual@endlink . 
                    If it uses @link NXOpen::VisualReporting::Classifier::GroupingMethodOptionManual NXOpen::VisualReporting::Classifier::GroupingMethodOptionManual@endlink , then no
                    @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink s will be automatically generated, and they should
                    instead be added manually as required using @link NXOpen::VisualReporting::VisualReportBuilder::CreateGroupLabel NXOpen::VisualReporting::VisualReportBuilder::CreateGroupLabel@endlink .
                
        """
        pass
    
    ##  Sets the @link NXOpen::VisualReporting::VisualReport::ObjectTypeOption NXOpen::VisualReporting::VisualReport::ObjectTypeOption@endlink s of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this builder.
    ##             Only valid if the @link NXOpen::VisualReporting::VisualReport::ScopeType NXOpen::VisualReporting::VisualReport::ScopeType@endlink  of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink 
    ##             is @link NXOpen::VisualReporting::VisualReport::ScopeTypeOptionSubPart NXOpen::VisualReporting::VisualReport::ScopeTypeOptionSubPart@endlink  type.
    ##             note that during setting object type of visual report, the @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink  of this report will be deleted and initilized, so the caller should 
    ##             get rule again.
    ##         
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ##  The object types being set 
    def SetObjectTypesOfVisualReport(builder: VisualReportBuilder, objectTypes: List[VisualReport.ObjectTypeOption]) -> None:
        """
         Sets the @link NXOpen::VisualReporting::VisualReport::ObjectTypeOption NXOpen::VisualReporting::VisualReport::ObjectTypeOption@endlink s of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  being built by this builder.
                    Only valid if the @link NXOpen::VisualReporting::VisualReport::ScopeType NXOpen::VisualReporting::VisualReport::ScopeType@endlink  of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink 
                    is @link NXOpen::VisualReporting::VisualReport::ScopeTypeOptionSubPart NXOpen::VisualReporting::VisualReport::ScopeTypeOptionSubPart@endlink  type.
                    note that during setting object type of visual report, the @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink  of this report will be deleted and initilized, so the caller should 
                    get rule again.
                
        """
        pass
    
    ##  Sets the @link NXOpen::VisualReporting::Condition::OperatorOption NXOpen::VisualReporting::Condition::OperatorOption@endlink  of this condition. Only valid if
    ##             @link NXOpen::VisualReporting::Condition::TypeOption NXOpen::VisualReporting::Condition::TypeOption@endlink  is
    ##             @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
    ##         
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    ##  The condition 
    def SetOperatorTypeOfCondition(builder: VisualReportBuilder, condition: Condition, operatorType: Condition.OperatorOption) -> None:
        """
         Sets the @link NXOpen::VisualReporting::Condition::OperatorOption NXOpen::VisualReporting::Condition::OperatorOption@endlink  of this condition. Only valid if
                    @link NXOpen::VisualReporting::Condition::TypeOption NXOpen::VisualReporting::Condition::TypeOption@endlink  is
                    @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                
        """
        pass
    
    ##  Sets the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  in the value for comparison of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink . If the
    ##             @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  is set to NULL, then it is
    ##             deleted.
    ##         
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The condition 
    def SetPropertyForComparison(builder: VisualReportBuilder, condition: Condition, property: Property) -> None:
        """
         Sets the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  in the value for comparison of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink . If the
                    @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  is set to NULL, then it is
                    deleted.
                
        """
        pass
    
    ##  Sets the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  of this condition. If the
    ##             @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  is set to NULL, then it is
    ##             deleted.
    ##             Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
    ##             @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
    ##         
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    ##  The condition 
    def SetPropertyOfCondition(builder: VisualReportBuilder, condition: Condition, property: Property) -> None:
        """
         Sets the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  of this condition. If the
                    @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  is set to NULL, then it is
                    deleted.
                    Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                    @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                
        """
        pass
    
    ##  Sets the property specification of the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  being built by this builder.
    ##         
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The property being set 
    @overload
    def SetPropertySpecification(self, builder: VisualReportBuilder, property: Property, key: str) -> None:
        """
         Sets the property specification of the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  being built by this builder.
                
        """
        pass
    
    ##  Sets the property specification of the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  being built by this builder.
    ##         
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The property being set 
    @overload
    def SetPropertySpecification(self, builder: VisualReportBuilder, property: Property, key: str, name: str) -> None:
        """
         Sets the property specification of the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  being built by this builder.
                
        """
        pass
    
    ##  Sets the @link NXOpen::VisualReporting::Classifier::RangeMethodOption NXOpen::VisualReporting::Classifier::RangeMethodOption@endlink  of the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  
    ##             in the given @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink . 
    ##             
    ##             Only valid if the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  in the rule 
    ##             is @link NXOpen::VisualReporting::Classifier::TypeOptionRange NXOpen::VisualReporting::Classifier::TypeOptionRange@endlink  type.
    ##         
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The rule 
    def SetRangeMethodOfRule(builder: VisualReportBuilder, rule: Rule, rangeMethod: Classifier.RangeMethodOption) -> None:
        """
         Sets the @link NXOpen::VisualReporting::Classifier::RangeMethodOption NXOpen::VisualReporting::Classifier::RangeMethodOption@endlink  of the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  
                    in the given @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink . 
                    
                    Only valid if the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  in the rule 
                    is @link NXOpen::VisualReporting::Classifier::TypeOptionRange NXOpen::VisualReporting::Classifier::TypeOptionRange@endlink  type.
                
        """
        pass
    
    ## Sets the message @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  list of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
    ##         
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The reference properties of report
    def SetReferencePropertiesOfReport(builder: VisualReportBuilder, properties: List[Property], usages: List[VisualReportBuilder.PropertyUsageOption]) -> None:
        """
        Sets the message @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  list of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
                
        """
        pass
    
    ##  Sets the message @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  list of the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink 
    ##             in the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink .
    ##         
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The reference properties of property
    def SetReferencePropertiesOfReportingProperty(builder: VisualReportBuilder, properties: List[Property], usages: List[VisualReportBuilder.PropertyUsageOption]) -> None:
        """
         Sets the message @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  list of the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink 
                    in the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink .
                
        """
        pass
    
    ##  Sets the @link NXOpen::VisualReporting::Property::DatatypeOption NXOpen::VisualReporting::Property::DatatypeOption@endlink  of the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink 's reporting @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink 
    ##             in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
    ## 
    ##             However datatype must not be @link NXOpen::VisualReporting::Property::DatatypeOptionUnknown NXOpen::VisualReporting::Property::DatatypeOptionUnknown@endlink .
    ##         
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    ##  The rule 
    def SetReportingDatatypeOfRule(builder: VisualReportBuilder, rule: Rule, datatype: Property.DatatypeOption) -> None:
        """
         Sets the @link NXOpen::VisualReporting::Property::DatatypeOption NXOpen::VisualReporting::Property::DatatypeOption@endlink  of the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink 's reporting @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink 
                    in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
        
                    However datatype must not be @link NXOpen::VisualReporting::Property::DatatypeOptionUnknown NXOpen::VisualReporting::Property::DatatypeOptionUnknown@endlink .
                
        """
        pass
    
    ##  Sets the reporting @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  for the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink 
    ##             in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
    ##             If the reporting @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  of the rule is set to NULL, then it is deleted.
    ## 
    ##             Only valid for a @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink  whose
    ##             @link NXOpen::VisualReporting::Classifier::TypeOption NXOpen::VisualReporting::Classifier::TypeOption@endlink  is @link NXOpen::VisualReporting::Classifier::TypeOptionValue NXOpen::VisualReporting::Classifier::TypeOptionValue@endlink 
    ##             or @link NXOpen::VisualReporting::Classifier::TypeOptionRange NXOpen::VisualReporting::Classifier::TypeOptionRange@endlink .
    ##         
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    ##  The rule 
    def SetReportingPropertyOfRule(builder: VisualReportBuilder, rule: Rule, reportingProperty: Property) -> None:
        """
         Sets the reporting @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  for the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink 
                    in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink .
                    If the reporting @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink  of the rule is set to NULL, then it is deleted.
        
                    Only valid for a @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  in this @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink  whose
                    @link NXOpen::VisualReporting::Classifier::TypeOption NXOpen::VisualReporting::Classifier::TypeOption@endlink  is @link NXOpen::VisualReporting::Classifier::TypeOptionValue NXOpen::VisualReporting::Classifier::TypeOptionValue@endlink 
                    or @link NXOpen::VisualReporting::Classifier::TypeOptionRange NXOpen::VisualReporting::Classifier::TypeOptionRange@endlink .
                
        """
        pass
    
    ##  Sets the priority of the given@link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
    ##         
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The group label 
    def SetTagPriorityOfGroupLabel(builder: VisualReportBuilder, groupLabel: GroupLabel, tagPriority: GroupLabel.TagPriorityOption) -> None:
        """
         Sets the priority of the given@link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
                
        """
        pass
    
    ##  Sets the tolerance of the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  in the given @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink 
    ## 
    ##             Only valid if the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  in the rule 
    ##             is @link NXOpen::VisualReporting::Classifier::TypeOptionValue NXOpen::VisualReporting::Classifier::TypeOptionValue@endlink  type.
    ##         
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  The rule 
    def SetToleranceOfRule(builder: VisualReportBuilder, rule: Rule, tolerance: float) -> None:
        """
         Sets the tolerance of the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  in the given @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink 
        
                    Only valid if the active @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  in the rule 
                    is @link NXOpen::VisualReporting::Classifier::TypeOptionValue NXOpen::VisualReporting::Classifier::TypeOptionValue@endlink  type.
                
        """
        pass
    
    ##  Sets the @link NXOpen::VisualReporting::GroupLabel::UpperBound NXOpen::VisualReporting::GroupLabel::UpperBound@endlink 
    ##             of the given @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
    ##         
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The group label 
    def SetUpperBoundOfGroupLabel(builder: VisualReportBuilder, groupLabel: GroupLabel, upperBound: str) -> None:
        """
         Sets the @link NXOpen::VisualReporting::GroupLabel::UpperBound NXOpen::VisualReporting::GroupLabel::UpperBound@endlink 
                    of the given @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
                
        """
        pass
    
    ##  Sets the @link NXOpen::NXObject::Name NXOpen::NXObject::Name@endlink 
    ##             of the given @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink . Calling this function
    ##             will cause @link NXOpen::VisualReporting::GroupLabel::IsNameUserSpecified NXOpen::VisualReporting::GroupLabel::IsNameUserSpecified@endlink 
    ##             to return true.
    ##         
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    ##  The group label 
    def SetUserNameOfGroupLabel(builder: VisualReportBuilder, groupLabel: GroupLabel, name: str) -> None:
        """
         Sets the @link NXOpen::NXObject::Name NXOpen::NXObject::Name@endlink 
                    of the given @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink . Calling this function
                    will cause @link NXOpen::VisualReporting::GroupLabel::IsNameUserSpecified NXOpen::VisualReporting::GroupLabel::IsNameUserSpecified@endlink 
                    to return true.
                
        """
        pass
    
    ##  Sets the @link NXOpen::VisualReporting::Condition::UserPrompt NXOpen::VisualReporting::Condition::UserPrompt@endlink  of the
    ##             specified @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .
    ##             Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
    ##             @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
    ##         
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    ##  The condition 
    def SetUserPromptOfCondition(builder: VisualReportBuilder, condition: Condition, userPrompt: str) -> None:
        """
         Sets the @link NXOpen::VisualReporting::Condition::UserPrompt NXOpen::VisualReporting::Condition::UserPrompt@endlink  of the
                    specified @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink .
                    Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                    @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                
        """
        pass
    
    ##  Sets the value of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink . 
    ##             Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
    ##             @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
    ##         
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="condition"> (@link Condition NXOpen.VisualReporting.Condition@endlink) </param>
    ## <param name="value"> (str) </param>
    def SetValueOfCondition(builder: VisualReportBuilder, condition: Condition, value: str) -> None:
        """
         Sets the value of this @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink . 
                    Only valid for a @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink  whose
                    @link NXOpen::VisualReporting::Condition::Type NXOpen::VisualReporting::Condition::Type@endlink  is @link NXOpen::VisualReporting::Condition::TypeOptionValueCondition NXOpen::VisualReporting::Condition::TypeOptionValueCondition@endlink 
                
        """
        pass
    
    ##  Sets the @link NXOpen::VisualReporting::GroupLabel::Value NXOpen::VisualReporting::GroupLabel::Value@endlink 
    ##             of the given @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
    ##         
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    ##  The group label 
    def SetValueOfGroupLabel(builder: VisualReportBuilder, groupLabel: GroupLabel, value: str) -> None:
        """
         Sets the @link NXOpen::VisualReporting::GroupLabel::Value NXOpen::VisualReporting::GroupLabel::Value@endlink 
                    of the given @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
                
        """
        pass
    
    ##  Resets the @link NXOpen::VisualReporting::GroupLabel::IsNameUserSpecified NXOpen::VisualReporting::GroupLabel::IsNameUserSpecified@endlink 
    ##             status of the given @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  so that the name is now
    ##             system-generated.
    ##         
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    ##  The group label 
    def UnsetUserNameOfGroupLabel(builder: VisualReportBuilder, groupLabel: GroupLabel) -> None:
        """
         Resets the @link NXOpen::VisualReporting::GroupLabel::IsNameUserSpecified NXOpen::VisualReporting::GroupLabel::IsNameUserSpecified@endlink 
                    status of the given @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  so that the name is now
                    system-generated.
                
        """
        pass
    
import NXOpen
## 
##         A collection of visual reports.
##      <br> To obtain an instance of this class, refer to @link NXOpen::VisualReporting::VisualReportManager  NXOpen::VisualReporting::VisualReportManager @endlink  <br> 
## 
##   <br>  Created in NX7.0.0  <br> 

class VisualReportCollection(NXOpen.TaggedObjectCollection): 
    """
        A collection of visual reports.
    """


    ##  Finds the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  with the given identifier as recorded in a journal. 
    ##         An object may not return the same value as its JournalIdentifier in different versions of 
    ##         the software. However newer versions of the software should find the same object when 
    ##         FindObject is passed older versions of its journal identifier. In general, this method 
    ##         should not be used in handwritten code and exists to support record and playback of journals.
    ##     
    ##         An exception will be thrown if no object can be found with the given journal identifier. 
    ##  @return visualReport (@link VisualReport NXOpen.VisualReporting.VisualReport@endlink):  Visual report found, or null if no such visual report exists.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    ##  Filename of the visual report to be found 
    def FindObject(manager: VisualReportCollection, journalIdentifier: str) -> VisualReport:
        """
         Finds the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  with the given identifier as recorded in a journal. 
                An object may not return the same value as its JournalIdentifier in different versions of 
                the software. However newer versions of the software should find the same object when 
                FindObject is passed older versions of its journal identifier. In general, this method 
                should not be used in handwritten code and exists to support record and playback of journals.
            
                An exception will be thrown if no object can be found with the given journal identifier. 
         @return visualReport (@link VisualReport NXOpen.VisualReporting.VisualReport@endlink):  Visual report found, or null if no such visual report exists.
        """
        pass
    
import NXOpen
## 
##         The Explorer of the results of a visual report.
##         The Visual Report Explorer enables a report to focus on specified objects
##         or on a particular group in the visual report.
##      <br> To obtain an instance of this class, refer to @link NXOpen::VisualReporting::VisualReportManager  NXOpen::VisualReporting::VisualReportManager @endlink  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class VisualReportExplorer(NXOpen.Object): 
    """
        The Explorer of the results of a visual report.
        The Visual Report Explorer enables a report to focus on specified objects
        or on a particular group in the visual report.
    """


    ##  Represents whether Explore Report mode is on or off.
    ##         
    ##  Explore Visual Report results is off 
    class ExploreReportOption(Enum):
        """
        Members Include: <Off> <On>
        """
        Off: int
        On: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> VisualReportExplorer.ExploreReportOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Status reported by @link NXOpen::VisualReporting::VisualReportExplorer::ReportDown NXOpen::VisualReporting::VisualReportExplorer::ReportDown@endlink .
    ##         
    ##  There are no objects of interest below the specified objects 
    class ReportDownStatus(Enum):
        """
        Members Include: <NotSet> <End> <More>
        """
        NotSet: int
        End: int
        More: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> VisualReportExplorer.ReportDownStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  When the set of objects to report upon is changed, should the 
    ##             contents of the set be replaced or extended.
    ##         
    ##  Replace the existing set of objects 
    class ReportOnObjectsOption(Enum):
        """
        Members Include: <Replace> <Add>
        """
        Replace: int
        Add: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> VisualReportExplorer.ReportOnObjectsOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link VisualReportExplorer.ExploreReportOption NXOpen.VisualReporting.VisualReportExplorer.ExploreReportOption@endlink) ExploreReport
    ##   the Explore Report setting
    ##           
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return VisualReportExplorer.ExploreReportOption
    @property
    def ExploreReport(self) -> VisualReportExplorer.ExploreReportOption:
        """
        Getter for property: (@link VisualReportExplorer.ExploreReportOption NXOpen.VisualReporting.VisualReportExplorer.ExploreReportOption@endlink) ExploreReport
          the Explore Report setting
                  
            
         
        """
        pass
    
    ## Setter for property: (@link VisualReportExplorer.ExploreReportOption NXOpen.VisualReporting.VisualReportExplorer.ExploreReportOption@endlink) ExploreReport

    ##   the Explore Report setting
    ##           
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @ExploreReport.setter
    def ExploreReport(self, exploreReportOption: VisualReportExplorer.ExploreReportOption):
        """
        Setter for property: (@link VisualReportExplorer.ExploreReportOption NXOpen.VisualReporting.VisualReportExplorer.ExploreReportOption@endlink) ExploreReport
          the Explore Report setting
                  
            
         
        """
        pass
    
    ##  Remove all objects from the visual report.
    ##         
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def ClearReportObjects() -> None:
        """
         Remove all objects from the visual report.
                
        """
        pass
    
    ##  Gets the exploring @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink 
    ##         
    ##  @return groupLabel (@link GroupLabel NXOpen.VisualReporting.GroupLabel@endlink):  The exploring group .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetExploringGroup() -> GroupLabel:
        """
         Gets the exploring @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink 
                
         @return groupLabel (@link GroupLabel NXOpen.VisualReporting.GroupLabel@endlink):  The exploring group .
        """
        pass
    
    ##  Remove objects from report.
    ##         
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Objects to remove from report 
    @staticmethod
    def RemoveReportObjects(nxObjects: List[NXOpen.NXObject]) -> None:
        """
         Remove objects from report.
                
        """
        pass
    
    ##  Report down the assembly, starting from the @link NXOpen::Assemblies::ComponentAssembly::RootComponent NXOpen::Assemblies::ComponentAssembly::RootComponent@endlink .
    ##             A group to explore should have been specified for this method to         
    ##             have any effect.
    ##             The first time this method is called the operation will start from
    ##             @link NXOpen::Assemblies::ComponentAssembly::RootComponent NXOpen::Assemblies::ComponentAssembly::RootComponent@endlink .
    ##             On subsequent calls, the set of objects currently reported upon 
    ##             will be used as the starting point.
    ##         
    ##  @return reportDownStatus (@link VisualReportExplorer.ReportDownStatus NXOpen.VisualReporting.VisualReportExplorer.ReportDownStatus@endlink):  Status from the report down operation .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Add to or replace objects in report 
    @staticmethod
    @overload
    def ReportDown(self, reportOnObjectsOption: VisualReportExplorer.ReportOnObjectsOption) -> VisualReportExplorer.ReportDownStatus:
        """
         Report down the assembly, starting from the @link NXOpen::Assemblies::ComponentAssembly::RootComponent NXOpen::Assemblies::ComponentAssembly::RootComponent@endlink .
                    A group to explore should have been specified for this method to         
                    have any effect.
                    The first time this method is called the operation will start from
                    @link NXOpen::Assemblies::ComponentAssembly::RootComponent NXOpen::Assemblies::ComponentAssembly::RootComponent@endlink .
                    On subsequent calls, the set of objects currently reported upon 
                    will be used as the starting point.
                
         @return reportDownStatus (@link VisualReportExplorer.ReportDownStatus NXOpen.VisualReporting.VisualReportExplorer.ReportDownStatus@endlink):  Status from the report down operation .
        """
        pass
    
    ##  Report down from a starting array of objects.
    ##             A group to explore should have been specified for this method to
    ##             have any effect.
    ##             On subsequent calls to @link NXOpen::VisualReporting::VisualReportExplorer::ReportDown NXOpen::VisualReporting::VisualReportExplorer::ReportDown@endlink , with no nxObjects
    ##             array, the set of objects currently reported upon will be used as the 
    ##             starting point.
    ##         
    ##  @return reportDownStatus (@link VisualReportExplorer.ReportDownStatus NXOpen.VisualReporting.VisualReportExplorer.ReportDownStatus@endlink):  Status from the report down operation .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Objects from which to start report down operation 
    @overload
    def ReportDown(self, nxObjects: List[NXOpen.NXObject], reportOnObjectsOption: VisualReportExplorer.ReportOnObjectsOption) -> VisualReportExplorer.ReportDownStatus:
        """
         Report down from a starting array of objects.
                    A group to explore should have been specified for this method to
                    have any effect.
                    On subsequent calls to @link NXOpen::VisualReporting::VisualReportExplorer::ReportDown NXOpen::VisualReporting::VisualReportExplorer::ReportDown@endlink , with no nxObjects
                    array, the set of objects currently reported upon will be used as the 
                    starting point.
                
         @return reportDownStatus (@link VisualReportExplorer.ReportDownStatus NXOpen.VisualReporting.VisualReportExplorer.ReportDownStatus@endlink):  Status from the report down operation .
        """
        pass
    
    ##  Report on the children of nxObjects.
    ##             The children will either replace the existing contents of the report
    ##             or be added to the report.
    ##             This operation is intended for @link NXOpen::Assemblies::Component NXOpen::Assemblies::Component@endlink s
    ##             and will report on direct children of the components.
    ##             If an object is not an instance of @link NXOpen::Assemblies::Component NXOpen::Assemblies::Component@endlink 
    ##             or if it has no children then nothing will be changed.
    ##         
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Objects whose children will be reported upon 
    def ReportOnChildren(nxObjects: List[NXOpen.NXObject], reportOnObjectsOption: VisualReportExplorer.ReportOnObjectsOption) -> None:
        """
         Report on the children of nxObjects.
                    The children will either replace the existing contents of the report
                    or be added to the report.
                    This operation is intended for @link NXOpen::Assemblies::Component NXOpen::Assemblies::Component@endlink s
                    and will report on direct children of the components.
                    If an object is not an instance of @link NXOpen::Assemblies::Component NXOpen::Assemblies::Component@endlink 
                    or if it has no children then nothing will be changed.
                
        """
        pass
    
    ##  Set objects to report upon.
    ##         
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Objects to report upon 
    def ReportOnObjects(nxObjects: List[NXOpen.NXObject], reportOnObjectsOption: VisualReportExplorer.ReportOnObjectsOption) -> None:
        """
         Set objects to report upon.
                
        """
        pass
    
    ##  Report on the parents of the nxObjects.
    ##             The parents will either replace the existing contents of the report
    ##             or be added to the report.
    ##             This operation is intended for @link NXOpen::Assemblies::Component NXOpen::Assemblies::Component@endlink s
    ##             and will report on the parent of the component.
    ##             If the object is not an instance of @link NXOpen::Assemblies::Component NXOpen::Assemblies::Component@endlink 
    ##             or if it has no parent then nothing will be changed.
    ##         
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Objects whose parents will be reported upon 
    def ReportOnParents(nxObjects: List[NXOpen.NXObject], reportOnObjectsOption: VisualReportExplorer.ReportOnObjectsOption) -> None:
        """
         Report on the parents of the nxObjects.
                    The parents will either replace the existing contents of the report
                    or be added to the report.
                    This operation is intended for @link NXOpen::Assemblies::Component NXOpen::Assemblies::Component@endlink s
                    and will report on the parent of the component.
                    If the object is not an instance of @link NXOpen::Assemblies::Component NXOpen::Assemblies::Component@endlink 
                    or if it has no parent then nothing will be changed.
                
        """
        pass
    
    ##  Resets the objects to report upon.
    ##             If there is no group to explore set, then all leaf nodes of the 
    ##             assembly will be included in the report.
    ##             If a group to explore is set, then elements of that group
    ##             will be reported upon.  Where there are two elements of the group
    ##             on the same branch of the assembly, the lowest will be reported upon.
    ##         
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def ResetReportObjects() -> None:
        """
         Resets the objects to report upon.
                    If there is no group to explore set, then all leaf nodes of the 
                    assembly will be included in the report.
                    If a group to explore is set, then elements of that group
                    will be reported upon.  Where there are two elements of the group
                    on the same branch of the assembly, the lowest will be reported upon.
                
        """
        pass
    
    ##  Sets the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  to explore.
    ##             The @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  to explore can be set to NULL.
    ##             If there is no active visual report, then nothing will happen.
    ##             Note that the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  should belong to the active visual report
    ##             otherwise the call will fail.
    ##             This method will also cause the objects reported upon to be reset in the
    ##             same way as a call to @link ResetReportObjects ResetReportObjects@endlink .
    ##         
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  The group to explore 
    @staticmethod
    def SetGroupToExplore(groupLabel: GroupLabel) -> None:
        """
         Sets the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  to explore.
                    The @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  to explore can be set to NULL.
                    If there is no active visual report, then nothing will happen.
                    Note that the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  should belong to the active visual report
                    otherwise the call will fail.
                    This method will also cause the objects reported upon to be reset in the
                    same way as a call to @link ResetReportObjects ResetReportObjects@endlink .
                
        """
        pass
    
import NXOpen
## 
##         A manager for load, creation and activation of visual reports.
##      <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX7.0.0  <br> 

class VisualReportManager(NXOpen.Object): 
    """
        A manager for load, creation and activation of visual reports.
    """


    ## Getter for property: (@link VisualReport NXOpen.VisualReporting.VisualReport@endlink) Current
    ##   
    ##             the current @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return VisualReport
    @property
    def Current(self) -> VisualReport:
        """
        Getter for property: (@link VisualReport NXOpen.VisualReporting.VisualReport@endlink) Current
          
                    the current @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
          
                  
         
        """
        pass
    
    ## Setter for property: (@link VisualReport NXOpen.VisualReporting.VisualReport@endlink) Current

    ##   
    ##             the current @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
    ##   
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @Current.setter
    def Current(self, visualReport: VisualReport):
        """
        Setter for property: (@link VisualReport NXOpen.VisualReporting.VisualReport@endlink) Current
          
                    the current @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
          
                  
         
        """
        pass
    
    ##  Returns the @link NXOpen::VisualReporting::VisualReportCollection NXOpen::VisualReporting::VisualReportCollection@endlink  belonging to this visual report manager 
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @link VisualReportCollection NXOpen.VisualReporting.VisualReportCollection@endlink
    @property
    def VisualReports() -> VisualReportCollection:
        """
         Returns the @link NXOpen::VisualReporting::VisualReportCollection NXOpen::VisualReporting::VisualReportCollection@endlink  belonging to this visual report manager 
        """
        pass
    
    ##  Returns the @link NXOpen::VisualReporting::VisualReportExplorer NXOpen::VisualReporting::VisualReportExplorer@endlink  belonging to this visual report manager 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @link VisualReportExplorer NXOpen.VisualReporting.VisualReportExplorer@endlink
    @property
    def VisualReportExplorer() -> VisualReportExplorer:
        """
         Returns the @link NXOpen::VisualReporting::VisualReportExplorer NXOpen::VisualReporting::VisualReportExplorer@endlink  belonging to this visual report manager 
        """
        pass
    
    ##   Activates the @link NXOpen::VisualReporting::VisualReportManager::Current NXOpen::VisualReporting::VisualReportManager::Current@endlink  visual report. 
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def ActivateCurrentVisualReport() -> None:
        """
          Activates the @link NXOpen::VisualReporting::VisualReportManager::Current NXOpen::VisualReporting::VisualReportManager::Current@endlink  visual report. 
        """
        pass
    
    ##  Creates a @link NXOpen::VisualReporting::SpecifyDateBuilder NXOpen::VisualReporting::SpecifyDateBuilder@endlink .
    ##         
    ##  @return specifyDateBuilder (@link SpecifyDateBuilder NXOpen.VisualReporting.SpecifyDateBuilder@endlink):  The created builder .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    def CreateSpecifyDateBuilder() -> SpecifyDateBuilder:
        """
         Creates a @link NXOpen::VisualReporting::SpecifyDateBuilder NXOpen::VisualReporting::SpecifyDateBuilder@endlink .
                
         @return specifyDateBuilder (@link SpecifyDateBuilder NXOpen.VisualReporting.SpecifyDateBuilder@endlink):  The created builder .
        """
        pass
    
    ##  Creates a @link NXOpen::VisualReporting::VisualReportBuilder NXOpen::VisualReporting::VisualReportBuilder@endlink  and starts
    ##             editing a copy of the given @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
    ##         
    ##  @return visualReportBuilder (@link VisualReportBuilder NXOpen.VisualReporting.VisualReportBuilder@endlink):  The created builder .
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: nx_visual_reporting ("Visual Reporting")
    ##  The VisualReport for which this builder is being created. Can be NULL 
    def CreateVisualReportBuilder(visualReport: VisualReport) -> VisualReportBuilder:
        """
         Creates a @link NXOpen::VisualReporting::VisualReportBuilder NXOpen::VisualReporting::VisualReportBuilder@endlink  and starts
                    editing a copy of the given @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
                
         @return visualReportBuilder (@link VisualReportBuilder NXOpen.VisualReporting.VisualReportBuilder@endlink):  The created builder .
        """
        pass
    
    ##   Deactivates the @link NXOpen::VisualReporting::VisualReportManager::Current NXOpen::VisualReporting::VisualReportManager::Current@endlink  visual report. 
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def DeactivateCurrentVisualReport() -> None:
        """
          Deactivates the @link NXOpen::VisualReporting::VisualReportManager::Current NXOpen::VisualReporting::VisualReportManager::Current@endlink  visual report. 
        """
        pass
    
    ##  User defined method that is called when ask an boolean property value. 
    ## A callback definition with the following input arguments: 
    ##  - @link NXOpen.NXObject NXOpen.NXObject@endlink
    ##  and no return type
    GetBooleanTypePropertyValue = Callable[[NXOpen.NXObject], None]
    
    
    ##  User defined method that is called when ask an date property value. 
    ## A callback definition with the following input arguments: 
    ##  - @link NXOpen.NXObject NXOpen.NXObject@endlink
    ##  and no return type
    GetDateTypePropertyValue = Callable[[NXOpen.NXObject], None]
    
    
    ##  User defined method that is called when ask an integer type property value. 
    ## A callback definition with the following input arguments: 
    ##  - @link NXOpen.NXObject NXOpen.NXObject@endlink
    ##  and no return type
    GetIntegerTypePropertyValue = Callable[[NXOpen.NXObject], None]
    
    
    ##  User defined method that is called when ask an double type property value. 
    ## A callback definition with the following input arguments: 
    ##  - @link NXOpen.NXObject NXOpen.NXObject@endlink
    ##  and no return type
    GetRealTypePropertyValue = Callable[[NXOpen.NXObject], None]
    
    
    ##  User defined method that is called when ask an string type property value. 
    ## A callback definition with the following input arguments: 
    ##  - @link NXOpen.NXObject NXOpen.NXObject@endlink
    ##  and no return type
    GetStringTypePropertyValue = Callable[[NXOpen.NXObject], None]
    
    
    ##  Merges multiple existing @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  into one @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink , but does not set them to be the 
    ##             @link NXOpen::VisualReporting::VisualReportManager::Current NXOpen::VisualReporting::VisualReportManager::Current@endlink  visual report or activate them, and does not save the merged @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
    ##         
    ##  @return mergedReport (@link VisualReport NXOpen.VisualReporting.VisualReport@endlink):  merged report .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: nx_visual_reporting ("Visual Reporting")
    ##  array of existing reports 
    def MergeReports(visualReports: List[VisualReport], mergedReportName: str, mergedReportDescription: str) -> VisualReport:
        """
         Merges multiple existing @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  into one @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink , but does not set them to be the 
                    @link NXOpen::VisualReporting::VisualReportManager::Current NXOpen::VisualReporting::VisualReportManager::Current@endlink  visual report or activate them, and does not save the merged @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
                
         @return mergedReport (@link VisualReport NXOpen.VisualReporting.VisualReport@endlink):  merged report .
        """
        pass
    
    ##  Opens an existing @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink , but does not set it to be the 
    ##             @link NXOpen::VisualReporting::VisualReportManager::Current NXOpen::VisualReporting::VisualReportManager::Current@endlink  visual report or activate it.
    ##             If the visual report file cannot be opened, or if there is a problem parsing the file,
    ##             then an exception will be raised.
    ## 
    ##             If opening a managed report then it is recommended to use @link NXOpen::VisualReporting::VisualReportManager::OpenReports NXOpen::VisualReporting::VisualReportManager::OpenReports@endlink 
    ##             which can take a container path and list of dataset names
    ##         
    ##  @return visualReport (@link VisualReport NXOpen.VisualReporting.VisualReport@endlink):  .
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: nx_visual_reporting ("Visual Reporting")
    ##  The filename of the visual report to open 
    @staticmethod
    def Open(filename: str) -> VisualReport:
        """
         Opens an existing @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink , but does not set it to be the 
                    @link NXOpen::VisualReporting::VisualReportManager::Current NXOpen::VisualReporting::VisualReportManager::Current@endlink  visual report or activate it.
                    If the visual report file cannot be opened, or if there is a problem parsing the file,
                    then an exception will be raised.
        
                    If opening a managed report then it is recommended to use @link NXOpen::VisualReporting::VisualReportManager::OpenReports NXOpen::VisualReporting::VisualReportManager::OpenReports@endlink 
                    which can take a container path and list of dataset names
                
         @return visualReport (@link VisualReport NXOpen.VisualReporting.VisualReport@endlink):  .
        """
        pass
    
    ##  Opens existing @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink , but does not set them to be the 
    ##             @link NXOpen::VisualReporting::VisualReportManager::Current NXOpen::VisualReporting::VisualReportManager::Current@endlink  visual report or activate them.
    ##             If the visual report file cannot be opened, or if there is a problem parsing the file,
    ##             then an exception will be raised.
    ## 
    ##             This can be used in native mode by sending in a folder path and filenames, or in
    ##             managed mode using a container path and dataset names.
    ##         
    ##  @return visualReports (@link VisualReport List[NXOpen.VisualReporting.VisualReport]@endlink):  array of opened reports .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: nx_visual_reporting ("Visual Reporting")
    ##  array of folders to be searched 
    def OpenReports(folders: List[str], names: List[str]) -> List[VisualReport]:
        """
         Opens existing @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink , but does not set them to be the 
                    @link NXOpen::VisualReporting::VisualReportManager::Current NXOpen::VisualReporting::VisualReportManager::Current@endlink  visual report or activate them.
                    If the visual report file cannot be opened, or if there is a problem parsing the file,
                    then an exception will be raised.
        
                    This can be used in native mode by sending in a folder path and filenames, or in
                    managed mode using a container path and dataset names.
                
         @return visualReports (@link VisualReport List[NXOpen.VisualReporting.VisualReport]@endlink):  array of opened reports .
        """
        pass
    
    ##  Registers a string type property.
    ##         
    ##             The property key and property name should be unique in current session.
    ##             Parameters 'isValidInNative' and 'isValidInTeamcenter' shouldn't be 'false' at the same time.
    ##         
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_visual_reporting ("Visual Reporting")
    ##  property key 
    @overload
    def RegisterProperty(self, propertyKey: str, propertyName: str, scopeType: VisualReport.ScopeTypeOption, objectTypes: List[VisualReport.ObjectTypeOption], dataType: Property.DatatypeOption, isValidInNative: bool, isValidInTeamcenter: bool, getStringTypePropertyValue: VisualReportManager.GetStringTypePropertyValue) -> None:
        """
         Registers a string type property.
                
                    The property key and property name should be unique in current session.
                    Parameters 'isValidInNative' and 'isValidInTeamcenter' shouldn't be 'false' at the same time.
                
        """
        pass
    
    ##  Registers an integer type property.
    ##         
    ##             The property key and property name should be unique in current session.
    ##             Parameters 'isValidInNative' and 'isValidInTeamcenter' shouldn't be 'false' at the same time.
    ##         
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_visual_reporting ("Visual Reporting")
    ##  property key 
    @overload
    def RegisterProperty(self, propertyKey: str, propertyName: str, scopeType: VisualReport.ScopeTypeOption, objectTypes: List[VisualReport.ObjectTypeOption], dataType: Property.DatatypeOption, isValidInNative: bool, isValidInTeamcenter: bool, getIntegerTypePropertyValue: VisualReportManager.GetIntegerTypePropertyValue) -> None:
        """
         Registers an integer type property.
                
                    The property key and property name should be unique in current session.
                    Parameters 'isValidInNative' and 'isValidInTeamcenter' shouldn't be 'false' at the same time.
                
        """
        pass
    
    ##  Registers a double type property.
    ##         
    ##             The property key and property name should be unique in current session.
    ##             Parameters 'isValidInNative' and 'isValidInTeamcenter' shouldn't be 'false' at the same time.
    ##         
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_visual_reporting ("Visual Reporting")
    ##  property key 
    @overload
    def RegisterProperty(self, propertyKey: str, propertyName: str, scopeType: VisualReport.ScopeTypeOption, objectTypes: List[VisualReport.ObjectTypeOption], dataType: Property.DatatypeOption, isValidInNative: bool, isValidInTeamcenter: bool, getRealTypePropertyValue: VisualReportManager.GetRealTypePropertyValue) -> None:
        """
         Registers a double type property.
                
                    The property key and property name should be unique in current session.
                    Parameters 'isValidInNative' and 'isValidInTeamcenter' shouldn't be 'false' at the same time.
                
        """
        pass
    
    ##  Registers a boolean type property.
    ##         
    ##             The property key and property name should be unique in current session.
    ##             Parameters 'isValidInNative' and 'isValidInTeamcenter' shouldn't be 'false' at the same time.
    ##         
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_visual_reporting ("Visual Reporting")
    ##  property key 
    @overload
    def RegisterProperty(self, propertyKey: str, propertyName: str, scopeType: VisualReport.ScopeTypeOption, objectTypes: List[VisualReport.ObjectTypeOption], dataType: Property.DatatypeOption, isValidInNative: bool, isValidInTeamcenter: bool, getBooleanTypePropertyValue: VisualReportManager.GetBooleanTypePropertyValue) -> None:
        """
         Registers a boolean type property.
                
                    The property key and property name should be unique in current session.
                    Parameters 'isValidInNative' and 'isValidInTeamcenter' shouldn't be 'false' at the same time.
                
        """
        pass
    
    ##  Registers a @link NXOpen::NXObject::ComputationalTime NXOpen::NXObject::ComputationalTime@endlink  type property.
    ##         
    ##             The property key and property name should be unique in current session.
    ##             Parameters 'isValidInNative' and 'isValidInTeamcenter' shouldn't be 'false' at the same time.
    ##         
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_visual_reporting ("Visual Reporting")
    ##  property key 
    @overload
    def RegisterProperty(self, propertyKey: str, propertyName: str, scopeType: VisualReport.ScopeTypeOption, objectTypes: List[VisualReport.ObjectTypeOption], dataType: Property.DatatypeOption, isValidInNative: bool, isValidInTeamcenter: bool, getDateTypePropertyValue: VisualReportManager.GetDateTypePropertyValue) -> None:
        """
         Registers a @link NXOpen::NXObject::ComputationalTime NXOpen::NXObject::ComputationalTime@endlink  type property.
                
                    The property key and property name should be unique in current session.
                    Parameters 'isValidInNative' and 'isValidInTeamcenter' shouldn't be 'false' at the same time.
                
        """
        pass
    
    ##  Unloads an opened  @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
    ##         
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: nx_visual_reporting ("Visual Reporting")
    ## <param name="visualReport"> (@link VisualReport NXOpen.VisualReporting.VisualReport@endlink) </param>
    @staticmethod
    def Unload(visualReport: VisualReport) -> None:
        """
         Unloads an opened  @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
                
        """
        pass
    
    ##  Unregisters a property.
    ##         
    ##             When the library which the property resides in is unloaded from NX session, this method should be called to unregister the property.
    ##         
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_visual_reporting ("Visual Reporting")
    ##  property key 
    @staticmethod
    def UnregisterProperty(propertyKey: str) -> None:
        """
         Unregisters a property.
                
                    When the library which the property resides in is unloaded from NX session, this method should be called to unregister the property.
                
        """
        pass
    
import NXOpen
## 
##         A visual report can be activated by the @link NXOpen::VisualReporting::VisualReportManager NXOpen::VisualReporting::VisualReportManager@endlink  to 
##         apply colors to objects in the graphics window.
##         An active visual report groups objects according to filtering conditions and classification 
##         rules.  The contents of the groups can be accessed via @link NXOpen::VisualReporting::VisualReport::GetGroupLabels NXOpen::VisualReporting::VisualReport::GetGroupLabels@endlink 
##         and @link NXOpen::VisualReporting::VisualReport::GetObjectsInGroup NXOpen::VisualReporting::VisualReport::GetObjectsInGroup@endlink .
##     
## 
##   <br>  Created in NX7.0.0  <br> 

class VisualReport(NXOpen.NXObject): 
    """
        A visual report can be activated by the <ja_class>NXOpen.VisualReporting.VisualReportManager</ja_class> to 
        apply colors to objects in the graphics window.
        An active visual report groups objects according to filtering conditions and classification 
        rules.  The contents of the groups can be accessed via <ja_method>NXOpen.VisualReporting.VisualReport.GetGroupLabels</ja_method>
        and <ja_method>NXOpen.VisualReporting.VisualReport.GetObjectsInGroup</ja_method>.
    """


    ##  Represents the possible report object type options
    ##            for a @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
    ##            Only valid if the @link NXOpen::VisualReporting::VisualReport::ScopeType NXOpen::VisualReporting::VisualReport::ScopeType@endlink  of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink 
    ##            is @link NXOpen::VisualReporting::VisualReport::ScopeTypeOptionSubPart NXOpen::VisualReporting::VisualReport::ScopeTypeOptionSubPart@endlink  type.
    ##         
    ##  The report objects are bodies 
    class ObjectTypeOption(Enum):
        """
        Members Include: <Body> <Face>
        """
        Body: int
        Face: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> VisualReport.ObjectTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the possible @link NXOpen::VisualReporting::VisualReport::ReportContext NXOpen::VisualReporting::VisualReport::ReportContext@endlink  options
    ##            for a @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
    ##         
    ##  Collect objects from entire assembly 
    class ReportContextOption(Enum):
        """
        Members Include: <Assembly> <WorkPart>
        """
        Assembly: int
        WorkPart: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> VisualReport.ReportContextOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the possible @link NXOpen::VisualReporting::VisualReport::ReportingObjectType NXOpen::VisualReporting::VisualReport::ReportingObjectType@endlink 
    ##            for a @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
    ##            Only valid if the @link NXOpen::VisualReporting::VisualReport::ScopeType NXOpen::VisualReporting::VisualReport::ScopeType@endlink  of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink 
    ##            is @link NXOpen::VisualReporting::VisualReport::ScopeTypeOptionComponent NXOpen::VisualReporting::VisualReport::ScopeTypeOptionComponent@endlink  type.
    ##         
    ##  The reporting objects are parts. 
    class ReportingObjectTypeOption(Enum):
        """
        Members Include: <Part> <Component> <Inferred>
        """
        Part: int
        Component: int
        Inferred: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> VisualReport.ReportingObjectTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the possible @link NXOpen::VisualReporting::VisualReport::ReportingStyle NXOpen::VisualReporting::VisualReport::ReportingStyle@endlink 
    ##            for a @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
    ##         
    ##  Matching objects will be colored 
    class ReportingStyleOption(Enum):
        """
        Members Include: <ColorObject> <TagObject> <ColorAndTagObject>
        """
        ColorObject: int
        TagObject: int
        ColorAndTagObject: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> VisualReport.ReportingStyleOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the possible @link NXOpen::VisualReporting::VisualReport::SaveDestination NXOpen::VisualReporting::VisualReport::SaveDestination@endlink  options
    ##            for a @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
    ##         
    ##  Saves the report in the local file system. 
    class SaveDestinationOption(Enum):
        """
        Members Include: <Local> <Teamcenter>
        """
        Local: int
        Teamcenter: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> VisualReport.SaveDestinationOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the possible @link NXOpen::VisualReporting::VisualReport::ScopeType NXOpen::VisualReporting::VisualReport::ScopeType@endlink  options
    ##            for a @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
    ##         
    ##  The report is assembly component report 
    class ScopeTypeOption(Enum):
        """
        Members Include: <Component> <SubPart> <Application>
        """
        Component: int
        SubPart: int
        Application: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> VisualReport.ScopeTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) BitmapName
    ##   the bitmap name of this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def BitmapName(self) -> str:
        """
        Getter for property: (str) BitmapName
          the bitmap name of this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
          
                  
         
        """
        pass
    
    ## Setter for property: (str) BitmapName

    ##   the bitmap name of this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
    ##   
    ##           
    ##  
    ## Setter License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @BitmapName.setter
    def BitmapName(self, bitmapName: str):
        """
        Setter for property: (str) BitmapName
          the bitmap name of this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
          
                  
         
        """
        pass
    
    ## Getter for property: (str) CustomMessage
    ##   the custom message of this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def CustomMessage(self) -> str:
        """
        Getter for property: (str) CustomMessage
          the custom message of this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
          
                  
         
        """
        pass
    
    ## Setter for property: (str) CustomMessage

    ##   the custom message of this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
    ##   
    ##           
    ##  
    ## Setter License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @CustomMessage.setter
    def CustomMessage(self, customMessage: str):
        """
        Setter for property: (str) CustomMessage
          the custom message of this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
          
                  
         
        """
        pass
    
    ## Getter for property: (str) Description
    ##   the description of this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink 
    ##           
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return str
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
          the description of this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink 
                  
            
         
        """
        pass
    
    ## Setter for property: (str) Description

    ##   the description of this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink 
    ##           
    ##     
    ##  
    ## Setter License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
          the description of this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink 
                  
            
         
        """
        pass
    
    ## Getter for property: (str) DescriptiveCategory
    ##   the category of this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return str
    @property
    def DescriptiveCategory(self) -> str:
        """
        Getter for property: (str) DescriptiveCategory
          the category of this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
          
                  
         
        """
        pass
    
    ## Setter for property: (str) DescriptiveCategory

    ##   the category of this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
    ##   
    ##           
    ##  
    ## Setter License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @DescriptiveCategory.setter
    def DescriptiveCategory(self, category: str):
        """
        Setter for property: (str) DescriptiveCategory
          the category of this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
          
                  
         
        """
        pass
    
    ## Getter for property: (str) DestinationTeamcenterFolder
    ##   the destination Teamcenter folder for saving the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  to Teamcenter database.  
    ##   
    ##             
    ##             Note that this property is only needed when NX is connected to Teamcenter and report is saved as a copy to Teamcenter database.
    ##             This @link NXOpen::VisualReporting::VisualReport::DestinationTeamcenterFolder NXOpen::VisualReporting::VisualReport::DestinationTeamcenterFolder@endlink  may return NULL if you haven't 
    ##             set a folder name on this property.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def DestinationTeamcenterFolder(self) -> str:
        """
        Getter for property: (str) DestinationTeamcenterFolder
          the destination Teamcenter folder for saving the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  to Teamcenter database.  
          
                    
                    Note that this property is only needed when NX is connected to Teamcenter and report is saved as a copy to Teamcenter database.
                    This @link NXOpen::VisualReporting::VisualReport::DestinationTeamcenterFolder NXOpen::VisualReporting::VisualReport::DestinationTeamcenterFolder@endlink  may return NULL if you haven't 
                    set a folder name on this property.
                  
         
        """
        pass
    
    ## Setter for property: (str) DestinationTeamcenterFolder

    ##   the destination Teamcenter folder for saving the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  to Teamcenter database.  
    ##   
    ##             
    ##             Note that this property is only needed when NX is connected to Teamcenter and report is saved as a copy to Teamcenter database.
    ##             This @link NXOpen::VisualReporting::VisualReport::DestinationTeamcenterFolder NXOpen::VisualReporting::VisualReport::DestinationTeamcenterFolder@endlink  may return NULL if you haven't 
    ##             set a folder name on this property.
    ##           
    ##  
    ## Setter License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @DestinationTeamcenterFolder.setter
    def DestinationTeamcenterFolder(self, foldername: str):
        """
        Setter for property: (str) DestinationTeamcenterFolder
          the destination Teamcenter folder for saving the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  to Teamcenter database.  
          
                    
                    Note that this property is only needed when NX is connected to Teamcenter and report is saved as a copy to Teamcenter database.
                    This @link NXOpen::VisualReporting::VisualReport::DestinationTeamcenterFolder NXOpen::VisualReporting::VisualReport::DestinationTeamcenterFolder@endlink  may return NULL if you haven't 
                    set a folder name on this property.
                  
         
        """
        pass
    
    ## Getter for property: (str) Filename
    ##   the filename where this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  was opened from or will be saved to.  
    ##   
    ## 
    ##             Note that when NX is connected to Teamcenter, this property is the report dataset identifier from Teamcenter database. 
    ##             If it is a new report, it will be the report dataset name. When the report is save by @link NXOpen::VisualReporting::VisualReport::Save NXOpen::VisualReporting::VisualReport::Save@endlink , 
    ##             the report dataset identifier will be saved in this property.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return str
    @property
    def Filename(self) -> str:
        """
        Getter for property: (str) Filename
          the filename where this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  was opened from or will be saved to.  
          
        
                    Note that when NX is connected to Teamcenter, this property is the report dataset identifier from Teamcenter database. 
                    If it is a new report, it will be the report dataset name. When the report is save by @link NXOpen::VisualReporting::VisualReport::Save NXOpen::VisualReporting::VisualReport::Save@endlink , 
                    the report dataset identifier will be saved in this property.
                  
         
        """
        pass
    
    ## Setter for property: (str) Filename

    ##   the filename where this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  was opened from or will be saved to.  
    ##   
    ## 
    ##             Note that when NX is connected to Teamcenter, this property is the report dataset identifier from Teamcenter database. 
    ##             If it is a new report, it will be the report dataset name. When the report is save by @link NXOpen::VisualReporting::VisualReport::Save NXOpen::VisualReporting::VisualReport::Save@endlink , 
    ##             the report dataset identifier will be saved in this property.
    ##           
    ##  
    ## Setter License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @Filename.setter
    def Filename(self, filename: str):
        """
        Setter for property: (str) Filename
          the filename where this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  was opened from or will be saved to.  
          
        
                    Note that when NX is connected to Teamcenter, this property is the report dataset identifier from Teamcenter database. 
                    If it is a new report, it will be the report dataset name. When the report is save by @link NXOpen::VisualReporting::VisualReport::Save NXOpen::VisualReporting::VisualReport::Save@endlink , 
                    the report dataset identifier will be saved in this property.
                  
         
        """
        pass
    
    ## Getter for property: (bool) IsUnmatchedGroupEnabled
    ##   whether use of @link NXOpen::VisualReporting::VisualReport::UnmatchedGroupLabel NXOpen::VisualReporting::VisualReport::UnmatchedGroupLabel@endlink 
    ##             is enabled.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return bool
    @property
    def IsUnmatchedGroupEnabled(self) -> bool:
        """
        Getter for property: (bool) IsUnmatchedGroupEnabled
          whether use of @link NXOpen::VisualReporting::VisualReport::UnmatchedGroupLabel NXOpen::VisualReporting::VisualReport::UnmatchedGroupLabel@endlink 
                    is enabled.  
          
                  
         
        """
        pass
    
    ## Setter for property: (bool) IsUnmatchedGroupEnabled

    ##   whether use of @link NXOpen::VisualReporting::VisualReport::UnmatchedGroupLabel NXOpen::VisualReporting::VisualReport::UnmatchedGroupLabel@endlink 
    ##             is enabled.  
    ##   
    ##           
    ##  
    ## Setter License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @IsUnmatchedGroupEnabled.setter
    def IsUnmatchedGroupEnabled(self, isUnmatchedGroupEnabled: bool):
        """
        Setter for property: (bool) IsUnmatchedGroupEnabled
          whether use of @link NXOpen::VisualReporting::VisualReport::UnmatchedGroupLabel NXOpen::VisualReporting::VisualReport::UnmatchedGroupLabel@endlink 
                    is enabled.  
          
                  
         
        """
        pass
    
    ## Getter for property: (@link VisualReport.ReportContextOption NXOpen.VisualReporting.VisualReport.ReportContextOption@endlink) ReportContext
    ##   the @link NXOpen::VisualReporting::VisualReport::ReportContextOption NXOpen::VisualReporting::VisualReport::ReportContextOption@endlink  of this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return VisualReport.ReportContextOption
    @property
    def ReportContext(self) -> VisualReport.ReportContextOption:
        """
        Getter for property: (@link VisualReport.ReportContextOption NXOpen.VisualReporting.VisualReport.ReportContextOption@endlink) ReportContext
          the @link NXOpen::VisualReporting::VisualReport::ReportContextOption NXOpen::VisualReporting::VisualReport::ReportContextOption@endlink  of this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
          
                  
         
        """
        pass
    
    ## Setter for property: (@link VisualReport.ReportContextOption NXOpen.VisualReporting.VisualReport.ReportContextOption@endlink) ReportContext

    ##   the @link NXOpen::VisualReporting::VisualReport::ReportContextOption NXOpen::VisualReporting::VisualReport::ReportContextOption@endlink  of this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
    ##   
    ##           
    ##  
    ## Setter License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    @ReportContext.setter
    def ReportContext(self, reportContext: VisualReport.ReportContextOption):
        """
        Setter for property: (@link VisualReport.ReportContextOption NXOpen.VisualReporting.VisualReport.ReportContextOption@endlink) ReportContext
          the @link NXOpen::VisualReporting::VisualReport::ReportContextOption NXOpen::VisualReporting::VisualReport::ReportContextOption@endlink  of this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
          
                  
         
        """
        pass
    
    ## Getter for property: (@link VisualReport.ReportingObjectTypeOption NXOpen.VisualReporting.VisualReport.ReportingObjectTypeOption@endlink) ReportingObjectType
    ##   the @link NXOpen::VisualReporting::VisualReport::ReportingObjectTypeOption NXOpen::VisualReporting::VisualReport::ReportingObjectTypeOption@endlink  of this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
    ##   
    ##             Only valid if the @link NXOpen::VisualReporting::VisualReport::ScopeType NXOpen::VisualReporting::VisualReport::ScopeType@endlink  of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink 
    ##             is @link NXOpen::VisualReporting::VisualReport::ScopeTypeOptionComponent NXOpen::VisualReporting::VisualReport::ScopeTypeOptionComponent@endlink  type.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return VisualReport.ReportingObjectTypeOption
    @property
    def ReportingObjectType(self) -> VisualReport.ReportingObjectTypeOption:
        """
        Getter for property: (@link VisualReport.ReportingObjectTypeOption NXOpen.VisualReporting.VisualReport.ReportingObjectTypeOption@endlink) ReportingObjectType
          the @link NXOpen::VisualReporting::VisualReport::ReportingObjectTypeOption NXOpen::VisualReporting::VisualReport::ReportingObjectTypeOption@endlink  of this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
          
                    Only valid if the @link NXOpen::VisualReporting::VisualReport::ScopeType NXOpen::VisualReporting::VisualReport::ScopeType@endlink  of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink 
                    is @link NXOpen::VisualReporting::VisualReport::ScopeTypeOptionComponent NXOpen::VisualReporting::VisualReport::ScopeTypeOptionComponent@endlink  type.
                  
         
        """
        pass
    
    ## Setter for property: (@link VisualReport.ReportingObjectTypeOption NXOpen.VisualReporting.VisualReport.ReportingObjectTypeOption@endlink) ReportingObjectType

    ##   the @link NXOpen::VisualReporting::VisualReport::ReportingObjectTypeOption NXOpen::VisualReporting::VisualReport::ReportingObjectTypeOption@endlink  of this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
    ##   
    ##             Only valid if the @link NXOpen::VisualReporting::VisualReport::ScopeType NXOpen::VisualReporting::VisualReport::ScopeType@endlink  of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink 
    ##             is @link NXOpen::VisualReporting::VisualReport::ScopeTypeOptionComponent NXOpen::VisualReporting::VisualReport::ScopeTypeOptionComponent@endlink  type.
    ##           
    ##  
    ## Setter License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @ReportingObjectType.setter
    def ReportingObjectType(self, reportingObjectType: VisualReport.ReportingObjectTypeOption):
        """
        Setter for property: (@link VisualReport.ReportingObjectTypeOption NXOpen.VisualReporting.VisualReport.ReportingObjectTypeOption@endlink) ReportingObjectType
          the @link NXOpen::VisualReporting::VisualReport::ReportingObjectTypeOption NXOpen::VisualReporting::VisualReport::ReportingObjectTypeOption@endlink  of this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
          
                    Only valid if the @link NXOpen::VisualReporting::VisualReport::ScopeType NXOpen::VisualReporting::VisualReport::ScopeType@endlink  of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink 
                    is @link NXOpen::VisualReporting::VisualReport::ScopeTypeOptionComponent NXOpen::VisualReporting::VisualReport::ScopeTypeOptionComponent@endlink  type.
                  
         
        """
        pass
    
    ## Getter for property: (@link VisualReport.ReportingStyleOption NXOpen.VisualReporting.VisualReport.ReportingStyleOption@endlink) ReportingStyle
    ##   the @link NXOpen::VisualReporting::VisualReport::ReportingStyleOption NXOpen::VisualReporting::VisualReport::ReportingStyleOption@endlink  of this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return VisualReport.ReportingStyleOption
    @property
    def ReportingStyle(self) -> VisualReport.ReportingStyleOption:
        """
        Getter for property: (@link VisualReport.ReportingStyleOption NXOpen.VisualReporting.VisualReport.ReportingStyleOption@endlink) ReportingStyle
          the @link NXOpen::VisualReporting::VisualReport::ReportingStyleOption NXOpen::VisualReporting::VisualReport::ReportingStyleOption@endlink  of this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
          
                  
         
        """
        pass
    
    ## Setter for property: (@link VisualReport.ReportingStyleOption NXOpen.VisualReporting.VisualReport.ReportingStyleOption@endlink) ReportingStyle

    ##   the @link NXOpen::VisualReporting::VisualReport::ReportingStyleOption NXOpen::VisualReporting::VisualReport::ReportingStyleOption@endlink  of this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
    ##   
    ##           
    ##  
    ## Setter License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ##   <br>  Created in NX7.5.1  <br> 

    @ReportingStyle.setter
    def ReportingStyle(self, reportingStyle: VisualReport.ReportingStyleOption):
        """
        Setter for property: (@link VisualReport.ReportingStyleOption NXOpen.VisualReporting.VisualReport.ReportingStyleOption@endlink) ReportingStyle
          the @link NXOpen::VisualReporting::VisualReport::ReportingStyleOption NXOpen::VisualReporting::VisualReport::ReportingStyleOption@endlink  of this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
          
                  
         
        """
        pass
    
    ## Getter for property: (@link VisualReport.SaveDestinationOption NXOpen.VisualReporting.VisualReport.SaveDestinationOption@endlink) SaveDestination
    ##   the @link NXOpen::VisualReporting::VisualReport::SaveDestinationOption NXOpen::VisualReporting::VisualReport::SaveDestinationOption@endlink  of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
    ##   
    ##             Note that this property will always be @link NXOpen::VisualReporting::VisualReport::SaveDestinationOptionLocal NXOpen::VisualReporting::VisualReport::SaveDestinationOptionLocal@endlink  when NX is not connected to Teamcenter.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return VisualReport.SaveDestinationOption
    @property
    def SaveDestination(self) -> VisualReport.SaveDestinationOption:
        """
        Getter for property: (@link VisualReport.SaveDestinationOption NXOpen.VisualReporting.VisualReport.SaveDestinationOption@endlink) SaveDestination
          the @link NXOpen::VisualReporting::VisualReport::SaveDestinationOption NXOpen::VisualReporting::VisualReport::SaveDestinationOption@endlink  of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
          
                    Note that this property will always be @link NXOpen::VisualReporting::VisualReport::SaveDestinationOptionLocal NXOpen::VisualReporting::VisualReport::SaveDestinationOptionLocal@endlink  when NX is not connected to Teamcenter.
                  
         
        """
        pass
    
    ## Setter for property: (@link VisualReport.SaveDestinationOption NXOpen.VisualReporting.VisualReport.SaveDestinationOption@endlink) SaveDestination

    ##   the @link NXOpen::VisualReporting::VisualReport::SaveDestinationOption NXOpen::VisualReporting::VisualReport::SaveDestinationOption@endlink  of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
    ##   
    ##             Note that this property will always be @link NXOpen::VisualReporting::VisualReport::SaveDestinationOptionLocal NXOpen::VisualReporting::VisualReport::SaveDestinationOptionLocal@endlink  when NX is not connected to Teamcenter.
    ##           
    ##  
    ## Setter License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @SaveDestination.setter
    def SaveDestination(self, destinationOption: VisualReport.SaveDestinationOption):
        """
        Setter for property: (@link VisualReport.SaveDestinationOption NXOpen.VisualReporting.VisualReport.SaveDestinationOption@endlink) SaveDestination
          the @link NXOpen::VisualReporting::VisualReport::SaveDestinationOption NXOpen::VisualReporting::VisualReport::SaveDestinationOption@endlink  of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
          
                    Note that this property will always be @link NXOpen::VisualReporting::VisualReport::SaveDestinationOptionLocal NXOpen::VisualReporting::VisualReport::SaveDestinationOptionLocal@endlink  when NX is not connected to Teamcenter.
                  
         
        """
        pass
    
    ## Getter for property: (@link VisualReport.ScopeTypeOption NXOpen.VisualReporting.VisualReport.ScopeTypeOption@endlink) ScopeType
    ##   the @link NXOpen::VisualReporting::VisualReport::ScopeTypeOption NXOpen::VisualReporting::VisualReport::ScopeTypeOption@endlink  of this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return VisualReport.ScopeTypeOption
    @property
    def ScopeType(self) -> VisualReport.ScopeTypeOption:
        """
        Getter for property: (@link VisualReport.ScopeTypeOption NXOpen.VisualReporting.VisualReport.ScopeTypeOption@endlink) ScopeType
          the @link NXOpen::VisualReporting::VisualReport::ScopeTypeOption NXOpen::VisualReporting::VisualReport::ScopeTypeOption@endlink  of this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
          
                  
         
        """
        pass
    
    ## Getter for property: (@link GroupLabel NXOpen.VisualReporting.GroupLabel@endlink) UnmatchedGroupLabel
    ##   the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  which is used for unmatched object.  
    ##    
    ##             It will return NULL if the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  is not activated.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return GroupLabel
    @property
    def UnmatchedGroupLabel(self) -> GroupLabel:
        """
        Getter for property: (@link GroupLabel NXOpen.VisualReporting.GroupLabel@endlink) UnmatchedGroupLabel
          the @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink  which is used for unmatched object.  
           
                    It will return NULL if the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  is not activated.
                  
         
        """
        pass
    
    ## Getter for property: (@link UnmatchedResultCategory NXOpen.VisualReporting.UnmatchedResultCategory@endlink) UnmatchedResultCategory
    ##   the @link NXOpen::VisualReporting::UnmatchedResultCategory NXOpen::VisualReporting::UnmatchedResultCategory@endlink  from the activated @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
    ##   
    ##             It will return NULL if the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  is not activated.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return UnmatchedResultCategory
    @property
    def UnmatchedResultCategory(self) -> UnmatchedResultCategory:
        """
        Getter for property: (@link UnmatchedResultCategory NXOpen.VisualReporting.UnmatchedResultCategory@endlink) UnmatchedResultCategory
          the @link NXOpen::VisualReporting::UnmatchedResultCategory NXOpen::VisualReporting::UnmatchedResultCategory@endlink  from the activated @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .  
          
                    It will return NULL if the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  is not activated.
                  
         
        """
        pass
    
    ##  Returns the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink s which has been defined in this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
    ##             The returned properties include those properties defined in @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink s, in @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink s,
    ##             and in the referenced properties.
    ##         
    ##  @return definedProperties (@link Property List[NXOpen.VisualReporting.Property]@endlink):  Properties defined in this visual report .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetAllDefinedProperties(visualReport: VisualReport) -> List[Property]:
        """
         Returns the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink s which has been defined in this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
                    The returned properties include those properties defined in @link NXOpen::VisualReporting::Condition NXOpen::VisualReporting::Condition@endlink s, in @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink s,
                    and in the referenced properties.
                
         @return definedProperties (@link Property List[NXOpen.VisualReporting.Property]@endlink):  Properties defined in this visual report .
        """
        pass
    
    ##  Returns the result @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink s from the activated @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
    ##             There are no @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink s if the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  is not activated.
    ##             You can acess the user defined @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink s by @link NXOpen::VisualReporting::VisualReportBuilder::GetManualGroupLabelsOfRule NXOpen::VisualReporting::VisualReportBuilder::GetManualGroupLabelsOfRule@endlink .
    ##         
    ##  @return groupLabels (@link GroupLabel List[NXOpen.VisualReporting.GroupLabel]@endlink): .
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetGroupLabels(visualReport: VisualReport) -> List[GroupLabel]:
        """
         Returns the result @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink s from the activated @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
                    There are no @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink s if the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  is not activated.
                    You can acess the user defined @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink s by @link NXOpen::VisualReporting::VisualReportBuilder::GetManualGroupLabelsOfRule NXOpen::VisualReporting::VisualReportBuilder::GetManualGroupLabelsOfRule@endlink .
                
         @return groupLabels (@link GroupLabel List[NXOpen.VisualReporting.GroupLabel]@endlink): .
        """
        pass
    
    ##  Returns the result @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink s of a @link NXOpen::VisualReporting::ResultCategory NXOpen::VisualReporting::ResultCategory@endlink 
    ##             from the activated @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
    ##         
    ##  @return groupLabels (@link GroupLabel List[NXOpen.VisualReporting.GroupLabel]@endlink): .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="category"> (@link ResultCategory NXOpen.VisualReporting.ResultCategory@endlink) </param>
    def GetGroupLabelsOfResultCategory(visualReport: VisualReport, category: ResultCategory) -> List[GroupLabel]:
        """
         Returns the result @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink s of a @link NXOpen::VisualReporting::ResultCategory NXOpen::VisualReporting::ResultCategory@endlink 
                    from the activated @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
                
         @return groupLabels (@link GroupLabel List[NXOpen.VisualReporting.GroupLabel]@endlink): .
        """
        pass
    
    ##  Gets a comma separated string of the keywords for this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
    ##         
    ##  @return keywords (str): .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetKeywords(visualReport: VisualReport) -> str:
        """
         Gets a comma separated string of the keywords for this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
                
         @return keywords (str): .
        """
        pass
    
    ##  Returns the @link NXOpen::VisualReporting::VisualReport::ObjectTypeOption NXOpen::VisualReporting::VisualReport::ObjectTypeOption@endlink s of this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
    ##             Only valid if the @link NXOpen::VisualReporting::VisualReport::ScopeType NXOpen::VisualReporting::VisualReport::ScopeType@endlink  of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink 
    ##             is @link NXOpen::VisualReporting::VisualReport::ScopeTypeOptionSubPart NXOpen::VisualReporting::VisualReport::ScopeTypeOptionSubPart@endlink  type.
    ##         
    ##  @return objectTypes (@link VisualReport.ObjectTypeOption List[NXOpen.VisualReporting.VisualReport.ObjectTypeOption]@endlink):  The object types .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetObjectTypes(visualReport: VisualReport) -> List[VisualReport.ObjectTypeOption]:
        """
         Returns the @link NXOpen::VisualReporting::VisualReport::ObjectTypeOption NXOpen::VisualReporting::VisualReport::ObjectTypeOption@endlink s of this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
                    Only valid if the @link NXOpen::VisualReporting::VisualReport::ScopeType NXOpen::VisualReporting::VisualReport::ScopeType@endlink  of the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink 
                    is @link NXOpen::VisualReporting::VisualReport::ScopeTypeOptionSubPart NXOpen::VisualReporting::VisualReport::ScopeTypeOptionSubPart@endlink  type.
                
         @return objectTypes (@link VisualReport.ObjectTypeOption List[NXOpen.VisualReporting.VisualReport.ObjectTypeOption]@endlink):  The object types .
        """
        pass
    
    ##  Returns the @link NXOpen::NXObject NXOpen::NXObject@endlink s that belong to the group
    ##             with this @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
    ##         
    ##  @return nxObjects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    ##  A group label of this visual report 
    def GetObjectsInGroup(visualReport: VisualReport, groupLabel: GroupLabel) -> List[NXOpen.NXObject]:
        """
         Returns the @link NXOpen::NXObject NXOpen::NXObject@endlink s that belong to the group
                    with this @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
                
         @return nxObjects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
        """
        pass
    
    ##  Returns the value of the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink s for the @link NXOpen::NXObject NXOpen::NXObject@endlink  in the result @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
    ##             It will return NULL if the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  is not activated, or the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink 
    ##             does not belong to the properties defined in this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink , or the @link NXOpen::NXObject NXOpen::NXObject@endlink  doesn't belong to
    ##             the specified result @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
    ##         
    ##  @return value (str): .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  A property defined in this visual report 
    def GetPropertyValueOfObject(visualReport: VisualReport, property: Property, groupLabel: GroupLabel, nxObject: NXOpen.NXObject) -> str:
        """
         Returns the value of the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink s for the @link NXOpen::NXObject NXOpen::NXObject@endlink  in the result @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
                    It will return NULL if the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  is not activated, or the @link NXOpen::VisualReporting::Property NXOpen::VisualReporting::Property@endlink 
                    does not belong to the properties defined in this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink , or the @link NXOpen::NXObject NXOpen::NXObject@endlink  doesn't belong to
                    the specified result @link NXOpen::VisualReporting::GroupLabel NXOpen::VisualReporting::GroupLabel@endlink .
                
         @return value (str): .
        """
        pass
    
    ##  Returns the @link NXOpen::VisualReporting::ResultCategory NXOpen::VisualReporting::ResultCategory@endlink s from the activated @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
    ##             There are no @link NXOpen::VisualReporting::ResultCategory NXOpen::VisualReporting::ResultCategory@endlink s if the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  is not activated.
    ##         
    ##  @return categories (@link ResultCategory List[NXOpen.VisualReporting.ResultCategory]@endlink): .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetResultCategories(visualReport: VisualReport) -> List[ResultCategory]:
        """
         Returns the @link NXOpen::VisualReporting::ResultCategory NXOpen::VisualReporting::ResultCategory@endlink s from the activated @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
                    There are no @link NXOpen::VisualReporting::ResultCategory NXOpen::VisualReporting::ResultCategory@endlink s if the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  is not activated.
                
         @return categories (@link ResultCategory List[NXOpen.VisualReporting.ResultCategory]@endlink): .
        """
        pass
    
    ##  Return the specified @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink  from this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink 
    ##         
    ##  @return rule (@link Rule NXOpen.VisualReporting.Rule@endlink): .
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    ##  The index of the returned @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink . 
    def GetRule(visualReport: VisualReport, index: int) -> Rule:
        """
         Return the specified @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink  from this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink 
                
         @return rule (@link Rule NXOpen.VisualReporting.Rule@endlink): .
        """
        pass
    
    ##  Returns all the @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink s in this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink 
    ##         
    ##  @return rules (@link Rule List[NXOpen.VisualReporting.Rule]@endlink): .
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetRules(visualReport: VisualReport) -> List[Rule]:
        """
         Returns all the @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink s in this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink 
                
         @return rules (@link Rule List[NXOpen.VisualReporting.Rule]@endlink): .
        """
        pass
    
    ##  Removes the @link NXOpen::VisualReporting::ResultCategory NXOpen::VisualReporting::ResultCategory@endlink  from @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
    ##             The @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  which populates this @link NXOpen::VisualReporting::ResultCategory NXOpen::VisualReporting::ResultCategory@endlink  
    ##             will also be removed from the @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink  in the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
    ##         
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ## <param name="theCategory"> (@link ResultCategory NXOpen.VisualReporting.ResultCategory@endlink) </param>
    def RemoveResultCategory(visualReport: VisualReport, theCategory: ResultCategory) -> None:
        """
         Removes the @link NXOpen::VisualReporting::ResultCategory NXOpen::VisualReporting::ResultCategory@endlink  from @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
                    The @link NXOpen::VisualReporting::Classifier NXOpen::VisualReporting::Classifier@endlink  which populates this @link NXOpen::VisualReporting::ResultCategory NXOpen::VisualReporting::ResultCategory@endlink  
                    will also be removed from the @link NXOpen::VisualReporting::Rule NXOpen::VisualReporting::Rule@endlink  in the @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
                
        """
        pass
    
    ##  Saves this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  to its current @link NXOpen::VisualReporting::VisualReport::Filename NXOpen::VisualReporting::VisualReport::Filename@endlink .
    ## 
    ##             Note that when NX is connected to Teamcenter, the @link NXOpen::VisualReporting::VisualReport::Filename NXOpen::VisualReporting::VisualReport::Filename@endlink  will be 
    ##             updated to the report dataset identifier after the report is saved to Teamcenter database.
    ##         
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: nx_visual_reporting ("Visual Reporting")
    @staticmethod
    def Save(visualReport: VisualReport) -> None:
        """
         Saves this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink  to its current @link NXOpen::VisualReporting::VisualReport::Filename NXOpen::VisualReporting::VisualReport::Filename@endlink .
        
                    Note that when NX is connected to Teamcenter, the @link NXOpen::VisualReporting::VisualReport::Filename NXOpen::VisualReporting::VisualReport::Filename@endlink  will be 
                    updated to the report dataset identifier after the report is saved to Teamcenter database.
                
        """
        pass
    
    ##  Sets a comma separated string of the keywords for this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
    ##         
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: nx_visual_reporting ("Visual Reporting")
    ## 
    ## <param name="keywords"> (str) </param>
    def SetKeywords(visualReport: VisualReport, keywords: str) -> None:
        """
         Sets a comma separated string of the keywords for this @link NXOpen::VisualReporting::VisualReport NXOpen::VisualReporting::VisualReport@endlink .
                
        """
        pass
    
## @package NXOpen.VisualReporting
## Classes, Enums and Structs under NXOpen.VisualReporting namespace

##  @link ClassifierDateGroupMethodOption NXOpen.VisualReporting.ClassifierDateGroupMethodOption @endlink is an alias for @link Classifier.DateGroupMethodOption NXOpen.VisualReporting.Classifier.DateGroupMethodOption@endlink
ClassifierDateGroupMethodOption = Classifier.DateGroupMethodOption


##  @link ClassifierGroupingMethodOption NXOpen.VisualReporting.ClassifierGroupingMethodOption @endlink is an alias for @link Classifier.GroupingMethodOption NXOpen.VisualReporting.Classifier.GroupingMethodOption@endlink
ClassifierGroupingMethodOption = Classifier.GroupingMethodOption


##  @link ClassifierRangeMethodOption NXOpen.VisualReporting.ClassifierRangeMethodOption @endlink is an alias for @link Classifier.RangeMethodOption NXOpen.VisualReporting.Classifier.RangeMethodOption@endlink
ClassifierRangeMethodOption = Classifier.RangeMethodOption


##  @link ClassifierTypeOption NXOpen.VisualReporting.ClassifierTypeOption @endlink is an alias for @link Classifier.TypeOption NXOpen.VisualReporting.Classifier.TypeOption@endlink
ClassifierTypeOption = Classifier.TypeOption


##  @link ConditionOperatorOption NXOpen.VisualReporting.ConditionOperatorOption @endlink is an alias for @link Condition.OperatorOption NXOpen.VisualReporting.Condition.OperatorOption@endlink
ConditionOperatorOption = Condition.OperatorOption


##  @link ConditionTypeOption NXOpen.VisualReporting.ConditionTypeOption @endlink is an alias for @link Condition.TypeOption NXOpen.VisualReporting.Condition.TypeOption@endlink
ConditionTypeOption = Condition.TypeOption


##  @link GroupLabelDisplayStyleOption NXOpen.VisualReporting.GroupLabelDisplayStyleOption @endlink is an alias for @link GroupLabel.DisplayStyleOption NXOpen.VisualReporting.GroupLabel.DisplayStyleOption@endlink
GroupLabelDisplayStyleOption = GroupLabel.DisplayStyleOption


##  @link GroupLabelTagPriorityOption NXOpen.VisualReporting.GroupLabelTagPriorityOption @endlink is an alias for @link GroupLabel.TagPriorityOption NXOpen.VisualReporting.GroupLabel.TagPriorityOption@endlink
GroupLabelTagPriorityOption = GroupLabel.TagPriorityOption


##  @link PropertyDatatypeOption NXOpen.VisualReporting.PropertyDatatypeOption @endlink is an alias for @link Property.DatatypeOption NXOpen.VisualReporting.Property.DatatypeOption@endlink
PropertyDatatypeOption = Property.DatatypeOption


##  @link PropertyTypeOption NXOpen.VisualReporting.PropertyTypeOption @endlink is an alias for @link Property.TypeOption NXOpen.VisualReporting.Property.TypeOption@endlink
PropertyTypeOption = Property.TypeOption


##  @link VisualReportBuilderPropertyUsageOption NXOpen.VisualReporting.VisualReportBuilderPropertyUsageOption @endlink is an alias for @link VisualReportBuilder.PropertyUsageOption NXOpen.VisualReporting.VisualReportBuilder.PropertyUsageOption@endlink
VisualReportBuilderPropertyUsageOption = VisualReportBuilder.PropertyUsageOption


##  @link VisualReportExplorerExploreReportOption NXOpen.VisualReporting.VisualReportExplorerExploreReportOption @endlink is an alias for @link VisualReportExplorer.ExploreReportOption NXOpen.VisualReporting.VisualReportExplorer.ExploreReportOption@endlink
VisualReportExplorerExploreReportOption = VisualReportExplorer.ExploreReportOption


##  @link VisualReportExplorerReportDownStatus NXOpen.VisualReporting.VisualReportExplorerReportDownStatus @endlink is an alias for @link VisualReportExplorer.ReportDownStatus NXOpen.VisualReporting.VisualReportExplorer.ReportDownStatus@endlink
VisualReportExplorerReportDownStatus = VisualReportExplorer.ReportDownStatus


##  @link VisualReportExplorerReportOnObjectsOption NXOpen.VisualReporting.VisualReportExplorerReportOnObjectsOption @endlink is an alias for @link VisualReportExplorer.ReportOnObjectsOption NXOpen.VisualReporting.VisualReportExplorer.ReportOnObjectsOption@endlink
VisualReportExplorerReportOnObjectsOption = VisualReportExplorer.ReportOnObjectsOption


##  @link VisualReportObjectTypeOption NXOpen.VisualReporting.VisualReportObjectTypeOption @endlink is an alias for @link VisualReport.ObjectTypeOption NXOpen.VisualReporting.VisualReport.ObjectTypeOption@endlink
VisualReportObjectTypeOption = VisualReport.ObjectTypeOption


##  @link VisualReportReportContextOption NXOpen.VisualReporting.VisualReportReportContextOption @endlink is an alias for @link VisualReport.ReportContextOption NXOpen.VisualReporting.VisualReport.ReportContextOption@endlink
VisualReportReportContextOption = VisualReport.ReportContextOption


##  @link VisualReportReportingObjectTypeOption NXOpen.VisualReporting.VisualReportReportingObjectTypeOption @endlink is an alias for @link VisualReport.ReportingObjectTypeOption NXOpen.VisualReporting.VisualReport.ReportingObjectTypeOption@endlink
VisualReportReportingObjectTypeOption = VisualReport.ReportingObjectTypeOption


##  @link VisualReportReportingStyleOption NXOpen.VisualReporting.VisualReportReportingStyleOption @endlink is an alias for @link VisualReport.ReportingStyleOption NXOpen.VisualReporting.VisualReport.ReportingStyleOption@endlink
VisualReportReportingStyleOption = VisualReport.ReportingStyleOption


##  @link VisualReportSaveDestinationOption NXOpen.VisualReporting.VisualReportSaveDestinationOption @endlink is an alias for @link VisualReport.SaveDestinationOption NXOpen.VisualReporting.VisualReport.SaveDestinationOption@endlink
VisualReportSaveDestinationOption = VisualReport.SaveDestinationOption


##  @link VisualReportScopeTypeOption NXOpen.VisualReporting.VisualReportScopeTypeOption @endlink is an alias for @link VisualReport.ScopeTypeOption NXOpen.VisualReporting.VisualReport.ScopeTypeOption@endlink
VisualReportScopeTypeOption = VisualReport.ScopeTypeOption


