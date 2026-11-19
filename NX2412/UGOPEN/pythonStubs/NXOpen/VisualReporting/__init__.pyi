from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class Classifier(NXOpen.NXObject): 
    """ A Classifier within a NXOpen.VisualReporting.Rule.
    """
    class DateGroupMethodOption(Enum):
        """
        Members Include: 
         |Day|  The date grouping by day will be used 
         |Week|  The date grouping by week will be used 
         |Month|  The date grouping by month will be used 
         |Year|  The date grouping by year will be used 

        """
        Day: int
        Week: int
        Month: int
        Year: int
        @staticmethod
        def ValueOf(value: int) -> Classifier.DateGroupMethodOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class GroupingMethodOption(Enum):
        """
        Members Include: 
         |Manual|  Grouping is manual 
         |Automatic|  Grouping is automatic 
         |SemiAutomatic|  Grouping is automatic but some NXOpen.VisualReporting.GroupLabels have been modified 

        """
        Manual: int
        Automatic: int
        SemiAutomatic: int
        @staticmethod
        def ValueOf(value: int) -> Classifier.GroupingMethodOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RangeMethodOption(Enum):
        """
        Members Include: 
         |Number|  A numeric range will be used 
         |Percentage|  A percentage range will be used 

        """
        Number: int
        Percentage: int
        @staticmethod
        def ValueOf(value: int) -> Classifier.RangeMethodOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TypeOption(Enum):
        """
        Members Include: 
         |Simple|  Simple classifier type 
         |Value|  Value classifier type 
         |Range|  Range classifier type 

        """
        Simple: int
        Value: int
        Range: int
        @staticmethod
        def ValueOf(value: int) -> Classifier.TypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
import NXOpen
class Condition(NXOpen.NXObject): 
    """ A Condition within a NXOpen.VisualReporting.Rule.
    """
    class OperatorOption(Enum):
        """
        Members Include: 
         |EqualOperator|   
         |LessThanOperator|   
         |NotLessThanOperator|   
         |GreaterThanOperator|   
         |NotGreaterThanOperator|   
         |NotEqualOperator|   
         |RegularExpressionOperator|   
         |ContainsOperator|   
         |DoesNotContainOperator|   
         |OnOrBeforeOperator|   
         |OnOrAfterOperator|   

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
        @staticmethod
        def ValueOf(value: int) -> Condition.OperatorOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TypeOption(Enum):
        """
        Members Include: 
         |AndCondition|   
         |OrCondition|   
         |NotCondition|   
         |ValueCondition|   

        """
        AndCondition: int
        OrCondition: int
        NotCondition: int
        ValueCondition: int
        @staticmethod
        def ValueOf(value: int) -> Condition.TypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Datatype(self) -> Property.DatatypeOption:
        """
        Getter for property: ( Property.DatatypeOption NXOpen.Vis) Datatype
         Returns the  NXOpen::VisualReporting::Property::DatatypeOption  of this  NXOpen::VisualReporting::Condition .  
          
                    The returned data type will never be
                     NXOpen::VisualReporting::Property::DatatypeOptionUnknown .
                
                    Note that this  NXOpen::VisualReporting::Condition::Datatype  cannot be modified. 
                    Instead it is specified when creating this  NXOpen::VisualReporting::Condition  by using the appropriate function:
                     -  NXOpen::VisualReporting::VisualReportBuilder::CreateStringCondition 
                     -  NXOpen::VisualReporting::VisualReportBuilder::CreateIntegerCondition 
                     -  NXOpen::VisualReporting::VisualReportBuilder::CreateRealCondition 
                     -  NXOpen::VisualReporting::VisualReportBuilder::CreateBooleanCondition 
                    Note that the  NXOpen::VisualReporting::Condition s created using the following functions do not
                    have  NXOpen::VisualReporting::Property::DatatypeOption s and calling this function will cause an error for these:
                     -  NXOpen::VisualReporting::VisualReportBuilder::CreateAndCondition 
                     -  NXOpen::VisualReporting::VisualReportBuilder::CreateOrCondition 
                     -  NXOpen::VisualReporting::VisualReportBuilder::CreateNotCondition 
                  
         
        """
        pass
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the description for this  NXOpen::VisualReporting::Condition .  
          
                    Only valid for a  NXOpen::VisualReporting::Condition  whose
                     NXOpen::VisualReporting::Condition::Type  is  NXOpen::VisualReporting::Condition::TypeOptionValueCondition 
                  
         
        """
        pass
    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
         Returns the description for this  NXOpen::VisualReporting::Condition .  
          
                    Only valid for a  NXOpen::VisualReporting::Condition  whose
                     NXOpen::VisualReporting::Condition::Type  is  NXOpen::VisualReporting::Condition::TypeOptionValueCondition 
                  
         
        """
        pass
    @property
    def HasUserSpecifiedValue(self) -> bool:
        """
        Getter for property: (bool) HasUserSpecifiedValue
         Returns whether this  NXOpen::VisualReporting::Condition  requires user input.  
          
                    Only valid for a  NXOpen::VisualReporting::Condition  whose
                     NXOpen::VisualReporting::Condition::Type  is  NXOpen::VisualReporting::Condition::TypeOptionValueCondition 
                  
         
        """
        pass
    @HasUserSpecifiedValue.setter
    def HasUserSpecifiedValue(self, isUserSpecified: bool):
        """
        Setter for property: (bool) HasUserSpecifiedValue
         Returns whether this  NXOpen::VisualReporting::Condition  requires user input.  
          
                    Only valid for a  NXOpen::VisualReporting::Condition  whose
                     NXOpen::VisualReporting::Condition::Type  is  NXOpen::VisualReporting::Condition::TypeOptionValueCondition 
                  
         
        """
        pass
    @property
    def OperatorType(self) -> Condition.OperatorOption:
        """
        Getter for property: ( Condition.OperatorOption NXOpen.Vis) OperatorType
         Returns the  NXOpen::VisualReporting::Condition::OperatorOption  of this  NXOpen::VisualReporting::Condition .  
           
                    Only valid for a  NXOpen::VisualReporting::Condition  whose
                     NXOpen::VisualReporting::Condition::Type  is  NXOpen::VisualReporting::Condition::TypeOptionValueCondition 
                  
         
        """
        pass
    @OperatorType.setter
    def OperatorType(self, operatorType: Condition.OperatorOption):
        """
        Setter for property: ( Condition.OperatorOption NXOpen.Vis) OperatorType
         Returns the  NXOpen::VisualReporting::Condition::OperatorOption  of this  NXOpen::VisualReporting::Condition .  
           
                    Only valid for a  NXOpen::VisualReporting::Condition  whose
                     NXOpen::VisualReporting::Condition::Type  is  NXOpen::VisualReporting::Condition::TypeOptionValueCondition 
                  
         
        """
        pass
    @property
    def ParentCondition(self) -> Condition:
        """
        Getter for property: ( Condition NXOpen.Vis) ParentCondition
         Returns the parent condition of this  NXOpen::VisualReporting::Condition .  
           If this
                    condition has no parent or if the parent isn't a condition
                    then this returns NULL.
                    Note that this  NXOpen::VisualReporting::Condition::ParentCondition  cannot be modified. 
                    Instead it is determined when inserting this  NXOpen::VisualReporting::Condition  in the  NXOpen::VisualReporting::Rule 
                    by using the appropriate function:
                     -  NXOpen::VisualReporting::VisualReportBuilder::SetFilterConditionOfRule 
                     -  NXOpen::VisualReporting::VisualReportBuilder::AddChildToCondition 
                  
         
        """
        pass
    @property
    def Property(self) -> Property:
        """
        Getter for property: ( Property NXOpen.Vis) Property
         Returns the  NXOpen::VisualReporting::Property  of this  NXOpen::VisualReporting::Condition .  
           If the
                     NXOpen::VisualReporting::Property  is set to NULL, then it is
                    deleted.
                    Only valid for a  NXOpen::VisualReporting::Condition  whose
                     NXOpen::VisualReporting::Condition::Type  is  NXOpen::VisualReporting::Condition::TypeOptionValueCondition 
                  
         
        """
        pass
    @Property.setter
    def Property(self, property: Property):
        """
        Setter for property: ( Property NXOpen.Vis) Property
         Returns the  NXOpen::VisualReporting::Property  of this  NXOpen::VisualReporting::Condition .  
           If the
                     NXOpen::VisualReporting::Property  is set to NULL, then it is
                    deleted.
                    Only valid for a  NXOpen::VisualReporting::Condition  whose
                     NXOpen::VisualReporting::Condition::Type  is  NXOpen::VisualReporting::Condition::TypeOptionValueCondition 
                  
         
        """
        pass
    @property
    def Type(self) -> Condition.TypeOption:
        """
        Getter for property: ( Condition.TypeOption NXOpen.Vis) Type
         Returns the  NXOpen::VisualReporting::Condition::TypeOption  of this  NXOpen::VisualReporting::Condition 
          
          
                    Note that this  NXOpen::VisualReporting::Condition::Type  cannot be modified. 
                    Instead it is determined when creating this  NXOpen::VisualReporting::Condition  by using the appropriate function:
                     -  NXOpen::VisualReporting::VisualReportBuilder::CreateStringCondition 
                     -  NXOpen::VisualReporting::VisualReportBuilder::CreateIntegerCondition 
                     -  NXOpen::VisualReporting::VisualReportBuilder::CreateRealCondition 
                     -  NXOpen::VisualReporting::VisualReportBuilder::CreateBooleanCondition 
                     -  NXOpen::VisualReporting::VisualReportBuilder::CreateAndCondition 
                     -  NXOpen::VisualReporting::VisualReportBuilder::CreateOrCondition 
                     -  NXOpen::VisualReporting::VisualReportBuilder::CreateNotCondition 
                  
         
        """
        pass
    @property
    def UserPrompt(self) -> str:
        """
        Getter for property: (str) UserPrompt
         Returns the user prompt for this  NXOpen::VisualReporting::Condition .  
           Only useful for a condition where
                     NXOpen::VisualReporting::Condition::HasUserSpecifiedValue  is true.
                    Only valid for a  NXOpen::VisualReporting::Condition  whose
                     NXOpen::VisualReporting::Condition::Type  is  NXOpen::VisualReporting::Condition::TypeOptionValueCondition 
                  
         
        """
        pass
    @UserPrompt.setter
    def UserPrompt(self, userPrompt: str):
        """
        Setter for property: (str) UserPrompt
         Returns the user prompt for this  NXOpen::VisualReporting::Condition .  
           Only useful for a condition where
                     NXOpen::VisualReporting::Condition::HasUserSpecifiedValue  is true.
                    Only valid for a  NXOpen::VisualReporting::Condition  whose
                     NXOpen::VisualReporting::Condition::Type  is  NXOpen::VisualReporting::Condition::TypeOptionValueCondition 
                  
         
        """
        pass
    @property
    def Value(self) -> str:
        """
        Getter for property: (str) Value
         Returns the value of this  NXOpen::VisualReporting::Condition .  
           
                    Only valid for a  NXOpen::VisualReporting::Condition  whose
                     NXOpen::VisualReporting::Condition::Type  is  NXOpen::VisualReporting::Condition::TypeOptionValueCondition 
                  
         
        """
        pass
    @Value.setter
    def Value(self, conditionValue: str):
        """
        Setter for property: (str) Value
         Returns the value of this  NXOpen::VisualReporting::Condition .  
           
                    Only valid for a  NXOpen::VisualReporting::Condition  whose
                     NXOpen::VisualReporting::Condition::Type  is  NXOpen::VisualReporting::Condition::TypeOptionValueCondition 
                  
         
        """
        pass
    def GetChildCondition(self, index: int) -> Condition:
        """
         Return the specified child Condition from this NXOpen.VisualReporting.Condition
                
         Returns childCondition ( Condition NXOpen.Vis): .
        """
        pass
    def GetChildConditions(self) -> List[Condition]:
        """
         Returns all the child Conditions in this NXOpen.VisualReporting.Condition
                
         Returns childConditions ( Condition List[NXOpen.V): .
        """
        pass
    def IsChildCondition(self, childCondition: Condition) -> bool:
        """
         Returns whether the given NXOpen.VisualReporting.Condition is an immediate child of this condition
                
         Returns isChild (bool): .
        """
        pass
import NXOpen
class GroupLabel(NXOpen.NXObject): 
    """
        A group label corresponds to a group of objects in the results of an applied 
        NXOpen.VisualReporting.VisualReport.
    """
    class DisplayStyleOption(Enum):
        """
        Members Include: 
         |DeEmphasis|  Matching objects will be de-emphasized 
         |SpecifiedColor|  Matching objects will be shown using NXOpen.VisualReporting.GroupLabel.Color 
         |OriginalColor|  Matching objects will be shown using their original color 
         |AutomaticColor|  Matching objects will be shown using NXOpen.VisualReporting.GroupLabel.Color which is system determined 

        """
        DeEmphasis: int
        SpecifiedColor: int
        OriginalColor: int
        AutomaticColor: int
        @staticmethod
        def ValueOf(value: int) -> GroupLabel.DisplayStyleOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TagPriorityOption(Enum):
        """
        Members Include: 
         |Low|  Low priority 
         |Medium|  Medium priority 
         |High|  Hign priority 

        """
        Low: int
        Medium: int
        High: int
        @staticmethod
        def ValueOf(value: int) -> GroupLabel.TagPriorityOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BitmapName(self) -> str:
        """
        Getter for property: (str) BitmapName
         Returns the bitmap name of this  NXOpen::VisualReporting::GroupLabel .  
          
                  
         
        """
        pass
    @BitmapName.setter
    def BitmapName(self, bitmapName: str):
        """
        Setter for property: (str) BitmapName
         Returns the bitmap name of this  NXOpen::VisualReporting::GroupLabel .  
          
                  
         
        """
        pass
    @property
    def Color(self) -> NXOpen.NXColor.Rgb:
        """
        Getter for property: ( NXOpen.NXColor.Rgb) Color
         Returns the color of the  NXOpen::VisualReporting::GroupLabel    
            
         
        """
        pass
    @Color.setter
    def Color(self, color: NXOpen.NXColor.Rgb):
        """
        Setter for property: ( NXOpen.NXColor.Rgb) Color
         Returns the color of the  NXOpen::VisualReporting::GroupLabel    
            
         
        """
        pass
    @property
    def CustomMessage(self) -> str:
        """
        Getter for property: (str) CustomMessage
         Returns the custom message of this  NXOpen::VisualReporting::GroupLabel .  
          
                  
         
        """
        pass
    @CustomMessage.setter
    def CustomMessage(self, customMessage: str):
        """
        Setter for property: (str) CustomMessage
         Returns the custom message of this  NXOpen::VisualReporting::GroupLabel .  
          
                  
         
        """
        pass
    @property
    def DisplayStyle(self) -> GroupLabel.DisplayStyleOption:
        """
        Getter for property: ( GroupLabel.DisplayStyleOption NXOpen.Vis) DisplayStyle
         Returns the  NXOpen::VisualReporting::GroupLabel::DisplayStyleOption  of the  NXOpen::VisualReporting::GroupLabel    
            
         
        """
        pass
    @DisplayStyle.setter
    def DisplayStyle(self, displayStyle: GroupLabel.DisplayStyleOption):
        """
        Setter for property: ( GroupLabel.DisplayStyleOption NXOpen.Vis) DisplayStyle
         Returns the  NXOpen::VisualReporting::GroupLabel::DisplayStyleOption  of the  NXOpen::VisualReporting::GroupLabel    
            
         
        """
        pass
    @property
    def ErrorLevel(self) -> NXOpen.Validation.Result:
        """
        Getter for property: ( NXOpen.Validation.Result) ErrorLevel
         Returns the Error Level of this  NXOpen::VisualReporting::GroupLabel .  
             
         
        """
        pass
    @ErrorLevel.setter
    def ErrorLevel(self, errorLevel: NXOpen.Validation.Result):
        """
        Setter for property: ( NXOpen.Validation.Result) ErrorLevel
         Returns the Error Level of this  NXOpen::VisualReporting::GroupLabel .  
             
         
        """
        pass
    @property
    def IsManual(self) -> bool:
        """
        Getter for property: (bool) IsManual
         Returns whether the  NXOpen::VisualReporting::GroupLabel  is manual.  
           It is manual if it either has a user-specified
                     NXOpen::NXObject::Name  or if its  NXOpen::VisualReporting::GroupLabel::DisplayStyle  is
                    not  NXOpen::VisualReporting::GroupLabel::DisplayStyleOptionAutomaticColor .
                    You can change a  NXOpen::VisualReporting::GroupLabel  from automatic to manual, but you cannot 
                    change  NXOpen::VisualReporting::GroupLabel  from manual to automatic.
                  
         
        """
        pass
    @IsManual.setter
    def IsManual(self, isManual: bool):
        """
        Setter for property: (bool) IsManual
         Returns whether the  NXOpen::VisualReporting::GroupLabel  is manual.  
           It is manual if it either has a user-specified
                     NXOpen::NXObject::Name  or if its  NXOpen::VisualReporting::GroupLabel::DisplayStyle  is
                    not  NXOpen::VisualReporting::GroupLabel::DisplayStyleOptionAutomaticColor .
                    You can change a  NXOpen::VisualReporting::GroupLabel  from automatic to manual, but you cannot 
                    change  NXOpen::VisualReporting::GroupLabel  from manual to automatic.
                  
         
        """
        pass
    @property
    def IsNameUserSpecified(self) -> bool:
        """
        Getter for property: (bool) IsNameUserSpecified
         Returns whether the  NXOpen::VisualReporting::GroupLabel  has a user-specified  NXOpen::NXObject::Name .  
           If it isn't
                    user-specified, then the system will generate its name automatically.
                  
         
        """
        pass
    @IsNameUserSpecified.setter
    def IsNameUserSpecified(self, isNameUserSpecified: bool):
        """
        Setter for property: (bool) IsNameUserSpecified
         Returns whether the  NXOpen::VisualReporting::GroupLabel  has a user-specified  NXOpen::NXObject::Name .  
           If it isn't
                    user-specified, then the system will generate its name automatically.
                  
         
        """
        pass
    @property
    def LowerBound(self) -> str:
        """
        Getter for property: (str) LowerBound
         Returns the lower bound value of the  NXOpen::VisualReporting::GroupLabel  (if it is being grouped by range)   
            
         
        """
        pass
    @LowerBound.setter
    def LowerBound(self, fromValue: str):
        """
        Setter for property: (str) LowerBound
         Returns the lower bound value of the  NXOpen::VisualReporting::GroupLabel  (if it is being grouped by range)   
            
         
        """
        pass
    @property
    def TagPriority(self) -> GroupLabel.TagPriorityOption:
        """
        Getter for property: ( GroupLabel.TagPriorityOption NXOpen.Vis) TagPriority
         Returns the Tag Priority of this  NXOpen::VisualReporting::GroupLabel .  
             
         
        """
        pass
    @TagPriority.setter
    def TagPriority(self, tagPriority: GroupLabel.TagPriorityOption):
        """
        Setter for property: ( GroupLabel.TagPriorityOption NXOpen.Vis) TagPriority
         Returns the Tag Priority of this  NXOpen::VisualReporting::GroupLabel .  
             
         
        """
        pass
    @property
    def UpperBound(self) -> str:
        """
        Getter for property: (str) UpperBound
         Returns the upper bound value of the  NXOpen::VisualReporting::GroupLabel  (if it is being grouped by range)   
            
         
        """
        pass
    @UpperBound.setter
    def UpperBound(self, upperBound: str):
        """
        Setter for property: (str) UpperBound
         Returns the upper bound value of the  NXOpen::VisualReporting::GroupLabel  (if it is being grouped by range)   
            
         
        """
        pass
    @property
    def Value(self) -> str:
        """
        Getter for property: (str) Value
         Returns the value of the  NXOpen::VisualReporting::GroupLabel  (if it is being grouped by value)   
            
         
        """
        pass
    @Value.setter
    def Value(self, groupLabelValue: str):
        """
        Setter for property: (str) Value
         Returns the value of the  NXOpen::VisualReporting::GroupLabel  (if it is being grouped by value)   
            
         
        """
        pass
import NXOpen
class Property(NXOpen.NXObject): 
    """ A property within either a NXOpen.VisualReporting.Rule or a
        NXOpen.VisualReporting.Condition, or used as referenced property 
        information for the report.
    """
    class DatatypeOption(Enum):
        """
        Members Include: 
         |String|  String data type 
         |Integer|  Integer data type 
         |Real|  Floating point data type 
         |Boolean|  Boolean data type 
         |Unknown|  The data type is unknown 
         |Null|  Null data type
         |Date|  Date data type 

        """
        String: int
        Integer: int
        Real: int
        Boolean: int
        Unknown: int
        Null: int
        Date: int
        @staticmethod
        def ValueOf(value: int) -> Property.DatatypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TypeOption(Enum):
        """
        Members Include: 
         |ArrangementSpecificPositionProperty|  Arrangement specific positioning 
         |AttributeProperty|  Part attribute property 
         |ComponentGroupProperty|  Component group name 
         |ComponentNameProperty|  Component name 
         |DescriptivePartNameProperty|  Descriptive part name 
         |LoadStateProperty|  The load state of the component 
         |MassKgProperty|  The mass of the component in pounds 
         |MassLbProperty|  The mass of the component in kilograms 
         |ModifiedProperty|  Whether the component is modified 
         |MultiCadProperty|  Parts mastered in a CAD system other than NX 
         |PartNameProperty|  Part name 
         |PartUnitsProperty|  Part units 
         |PiecePartProperty|  Piece part 
         |PositionProperty|  The position of the component 
         |PositionControlProperty|  The position control of the component 
         |ReadOnlyProperty|  Whether the component is read-only 
         |ReferenceSetProperty|  The reference set used by the component 
         |RootPartProperty|  Root part occurrence 
         |SuppressionControlProperty|  The suppression control of the component 
         |WeightStatusProperty|  The weight status of the component 
         |TeamcenterProperty|  Teamcenter property 
         |ServerProperty|  Server Property defined in server side report 
         |DegreesOfFreedomProperty|  The freedom degree of the component 
         |RuleEvaluationResultProperty|  Rule Evaluation for results in part 
         |CheckMateResultProperty|  Check-Mate result
         |LastModifiedDateProperty|  last modify date property 
         |RequirementsValidationStatusProperty|  Requirement validate result
         |RepresentationProperty|  Representation Status
         |LastModifiedUserProperty|  last modify user property 
         |ComponentProperty|  Assembly Navigator column property 
         |MassGmProperty|  The mass of the component in grams 
         |PartFamilyMemberProperty|  Part family member 
         |LinkedPartProperty|  Linked part 
         |ProductTemplateProperty|  Product Template 
         |BodyDensityProperty|  Body density property 
         |BodyMassProperty|  Body mass property 
         |BodyRadiusGyrationProperty|  Body radius gyration property 
         |BodySurfaceAreaProperty|  Body surface area property 
         |BodyTypeProperty|  Body type property 
         |BodyVolumeProperty|  Body volume property 
         |BodyWeightProperty|  Body weight property 
         |FaceAreaProperty|  Face area property 
         |FaceTypeProperty|  Face type property 
         |FaceMinRadiusProperty|  Face minimum radius property 
         |FacePerimeterProperty|  Face perimeter property 
         |FacePMIFCFProperty|  Face PMI FCF property 
         |FacePMIFCFCharacteristicsProperty|  Face PMI FCF characteristics property 
         |FacePMIFCFCharFormTolProperty|  Face PMI FCF form characteristics property 
         |FacePMIFCFCharLocationTolProperty|  Face PMI FCF location characteristics property 
         |FacePMIFCFCharOrientationTolProperty|  Face PMI FCF orientation characteristics property 
         |FacePMIFCFCharProfileTolProperty|  Face PMI FCF profile characteristics property 
         |FacePMIFCFCharRunoutTolProperty|  Face PMI FCF run out characteristics property 
         |FacePMIDatumFeatureProperty|  Face PMI datum feature property 
         |FacePMIDatumTargetProperty|  Face PMI datum target property 
         |ObjectAttributeProperty|  Subpart object attribute property 
         |ObjectCreatedByUserProperty|  Subpart object created by user property 
         |ObjectCreatedDateProperty|  Subpart object created date property 
         |ObjectCreatedVersionProperty|  Subpart object created version property 
         |ObjectRefByWaveLinkProperty|  Subpart object referenced by Wave link property 
         |ObjectWaveLinkedProperty|  Subpart object Wave linked property 
         |ObjectModifiedByUserProperty|  Subpart object modified by user property 
         |ObjectModifiedDateProperty|  Subpart object modified date property 
         |ObjectModifiedVersionProperty|  Subpart object modified version property 
         |PartitionMembershipProperty|  Partition Membership property 
         |ComponentAddedDateProperty|  Component Added Date 
         |TeamcenterObjectProperty|  Teamcenter Object property 
         |ComponentPatternTypeProperty|  Component Pattern Type property 
         |ObjectNameProperty|  Subpart object name property 
         |NXOpenProperty|  NX Open property 
         |SheetMetalBendAngleProperty|  Sheet Metal Bend Angle Property 
         |SheetMetalBendRadiusProperty|  Sheet Metal Bend Radius Property 
         |SheetMetalFaceTypeAllProperty|  Sheet Metal All Face Type Property 
         |SheetMetalFaceTypeBendProperty|  Sheet Metal Bend Face Type Property 
         |SheetMetalFaceTypeDeformProperty|  Sheet Metal Deform Face Type Property 
         |SheetMetalFaceTypeWebProperty|  Sheet Metal Web Face Type Property 
         |SheetMetalNeutralFactorProperty|  Sheet Metal Neutral Factor Property 
         |SheetMetalBodyTypeProperty|  Sheet Metal Body Type Property 
         |FeatureFailureProperty|  Feature failure component property 
         |MassIssueProperty|  Mass Issue Property 
         |MassUpdateToggleStatusProperty|  Mass Update Toggle Status Property 
         |LastSavedVersionProperty|  Last Saved Version Property 
         |FlexiblePrintedCircuitDesignFaceTypeTopAndBottomProperty|  Sheet Metal Top And Bottom Face Type Property 
         |MassReferenceSetProperty|  Mass Reference Set Property 
         |BodyReferenceSetNamesProperty|  Body Reference Set Names property 
         |EnvironmentalMaterialProperty|  Environmental Material Property 
         |MakeProcessProperty|  Make Process Property 

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
        MakeProcessProperty: int
        @staticmethod
        def ValueOf(value: int) -> Property.TypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BitmapName(self) -> str:
        """
        Getter for property: (str) BitmapName
         Returns the bitmap name of this property.  
          
                  
         
        """
        pass
    @BitmapName.setter
    def BitmapName(self, bitmapName: str):
        """
        Setter for property: (str) BitmapName
         Returns the bitmap name of this property.  
          
                  
         
        """
        pass
    @property
    def CustomMessage(self) -> str:
        """
        Getter for property: (str) CustomMessage
         Returns the custom message of this property.  
          
                  
         
        """
        pass
    @CustomMessage.setter
    def CustomMessage(self, customMessage: str):
        """
        Setter for property: (str) CustomMessage
         Returns the custom message of this property.  
          
                  
         
        """
        pass
    @property
    def PropertyType(self) -> Property.TypeOption:
        """
        Getter for property: ( Property.TypeOption NXOpen.Vis) PropertyType
         Returns the  NXOpen::VisualReporting::Property::TypeOption  of this  NXOpen::VisualReporting::Property .  
          
                    Note that this  NXOpen::VisualReporting::Property::PropertyType  cannot be modified. 
                    Instead it is specified when creating this  NXOpen::VisualReporting::Property  by using the appropriate function:
                     -  NXOpen::VisualReporting::VisualReportBuilder::CreateProperty 
                  
         
        """
        pass
    @property
    def SystemDatatype(self) -> Property.DatatypeOption:
        """
        Getter for property: ( Property.DatatypeOption NXOpen.Vis) SystemDatatype
         Returns the preferred  NXOpen::VisualReporting::Property::DatatypeOption  that should be used for the
                    owning  NXOpen::VisualReporting::Condition  or  NXOpen::VisualReporting::Classifier .  
          
                    This function will return a data type of 
                     NXOpen::VisualReporting::Property::DatatypeOptionUnknown 
                    for properties whose  NXOpen::VisualReporting::Property::PropertyType  is
                     NXOpen::VisualReporting::Property::TypeOptionTeamcenterProperty , 
                     NXOpen::VisualReporting::Property::TypeOptionServerProperty , 
                    or  NXOpen::VisualReporting::Property::TypeOptionAttributeProperty 
                    where the preferred data type cannot be determined.
                    Note that this  NXOpen::VisualReporting::Property::SystemDatatype  cannot be modified. 
                    Instead it is determined when creating this  NXOpen::VisualReporting::Property  by using the appropriate function:
                     -  NXOpen::VisualReporting::VisualReportBuilder::CreateProperty 
                  
         
        """
        pass
import NXOpen
class ResultCategory(NXOpen.NXObject): 
    """ A result category within a NXOpen.VisualReporting.VisualReport.
    """
    @property
    def BitmapName(self) -> str:
        """
        Getter for property: (str) BitmapName
         Returns the bitmap name of this  NXOpen::VisualReporting::ResultCategory .  
          
                  
         
        """
        pass
    @BitmapName.setter
    def BitmapName(self, bitmapName: str):
        """
        Setter for property: (str) BitmapName
         Returns the bitmap name of this  NXOpen::VisualReporting::ResultCategory .  
          
                  
         
        """
        pass
    @property
    def CustomMessage(self) -> str:
        """
        Getter for property: (str) CustomMessage
         Returns the custom message of this  NXOpen::VisualReporting::ResultCategory .  
          
                  
         
        """
        pass
    @CustomMessage.setter
    def CustomMessage(self, customMessage: str):
        """
        Setter for property: (str) CustomMessage
         Returns the custom message of this  NXOpen::VisualReporting::ResultCategory .  
          
                  
         
        """
        pass
import NXOpen
class Rule(NXOpen.NXObject): 
    """ A rule within a NXOpen.VisualReporting.VisualReport.
    """
    @property
    def ActiveClassifier(self) -> Classifier:
        """
        Getter for property: ( Classifier NXOpen.Vis) ActiveClassifier
         Returns the active  NXOpen::VisualReporting::Classifier  in this  NXOpen::VisualReporting::Rule 
                    for a multiple properties report.  
          
                  
         
        """
        pass
    @ActiveClassifier.setter
    def ActiveClassifier(self, activeClassifier: Classifier):
        """
        Setter for property: ( Classifier NXOpen.Vis) ActiveClassifier
         Returns the active  NXOpen::VisualReporting::Classifier  in this  NXOpen::VisualReporting::Rule 
                    for a multiple properties report.  
          
                  
         
        """
        pass
    @property
    def FilterCondition(self) -> Condition:
        """
        Getter for property: ( Condition NXOpen.Vis) FilterCondition
         Returns the filter  NXOpen::VisualReporting::Condition  from this  NXOpen::VisualReporting::Rule .  
           
                  
         
        """
        pass
    @FilterCondition.setter
    def FilterCondition(self, filterCondition: Condition):
        """
        Setter for property: ( Condition NXOpen.Vis) FilterCondition
         Returns the filter  NXOpen::VisualReporting::Condition  from this  NXOpen::VisualReporting::Rule .  
           
                  
         
        """
        pass
    def GetClassifiers(self) -> List[Classifier]:
        """
         Returns the NXOpen.VisualReporting.Classifiers associated with this NXOpen.VisualReporting.Rule.
                
         Returns classifiers ( Classifier List[NXOpen.V): .
        """
        pass
    def GetIsSmartGroupDateEnabled(self, classifier: Classifier) -> bool:
        """
         The NXOpen.VisualReporting.Classifier.DateGroupMethodOption in this NXOpen.VisualReporting.Classifier 
                    in the NXOpen.VisualReporting.Rule will be determined by the overall date range of all reported objects.
                    
                    For example, if the date range spans over 18 monthes, group by year will be used, otherwise if it is over 3 months, group by month will be used.
                    If the date range is small, within 2 weeks, group by day will be used. 
                    Only valid for a NXOpen.VisualReporting.Classifier whose NXOpen.VisualReporting.Classifier.GroupingMethodOption
                    is NXOpen.VisualReporting.Classifier.GroupingMethodOption.Automatic or
                    NXOpen.VisualReporting.Classifier.GroupingMethodOption.SemiAutomatic and the
                    NXOpen.VisualReporting.Property.DatatypeOption on the NXOpen.VisualReporting.Property
                    is NXOpen.VisualReporting.Property.DatatypeOption.Date.
                
         Returns isSmartGroupDateEnabled (bool): .
        """
        pass
    def SetIsSmartGroupDateEnabled(self, classifier: Classifier, isSmartGroupDateEnabled: bool) -> None:
        """
         The NXOpen.VisualReporting.Classifier.DateGroupMethodOption in this NXOpen.VisualReporting.Classifier 
                    in the NXOpen.VisualReporting.Rule will be determined by the overall date range of all reported objects.
                
        """
        pass
import NXOpen
class SpecifyDateBuilder(NXOpen.Builder): 
    """ Represents a Specify Date Builder"""
    @property
    def Date(self) -> NXOpen.DateBuilder:
        """
        Getter for property: ( NXOpen.DateBuilder) Date
         Returns the date   
            
         
        """
        pass
    @property
    def DateString(self) -> str:
        """
        Getter for property: (str) DateString
         Returns the current date as string  
            
         
        """
        pass
    @property
    def RelativeDateString(self) -> str:
        """
        Getter for property: (str) RelativeDateString
         Returns the current relative date string   
            
         
        """
        pass
    @RelativeDateString.setter
    def RelativeDateString(self, date_string: str):
        """
        Setter for property: (str) RelativeDateString
         Returns the current relative date string   
            
         
        """
        pass
import NXOpen
class UnmatchedResultCategory(NXOpen.NXObject): 
    """ An unmatched result category within a NXOpen.VisualReporting.VisualReport.
    """
    pass
import NXOpen
class VisualReportBuilder(NXOpen.Builder): 
    """ A Builder for creating and editing NXOpen.VisualReporting.VisualReports.
    """
    class PropertyUsageOption(Enum):
        """
        Members Include: 
         |Tooltip| The property is used in tooltip only
         |InfoView| The property is used in info view only
         |TooltipAndInfoView| 

        """
        Tooltip: int
        InfoView: int
        TooltipAndInfoView: int
        @staticmethod
        def ValueOf(value: int) -> VisualReportBuilder.PropertyUsageOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BitmapNameOfReport(self) -> str:
        """
        Getter for property: (str) BitmapNameOfReport
         Returns the bitmap name of the  NXOpen::VisualReporting::VisualReport .  
          
                  
         
        """
        pass
    @BitmapNameOfReport.setter
    def BitmapNameOfReport(self, bitmapName: str):
        """
        Setter for property: (str) BitmapNameOfReport
         Returns the bitmap name of the  NXOpen::VisualReporting::VisualReport .  
          
                  
         
        """
        pass
    @property
    def BitmapNameOfReportingProperty(self) -> str:
        """
        Getter for property: (str) BitmapNameOfReportingProperty
         Returns the bitmap name of the reporting  NXOpen::VisualReporting::Property  in the active  NXOpen::VisualReporting::Classifier .  
           
                  
         
        """
        pass
    @BitmapNameOfReportingProperty.setter
    def BitmapNameOfReportingProperty(self, bitmapName: str):
        """
        Setter for property: (str) BitmapNameOfReportingProperty
         Returns the bitmap name of the reporting  NXOpen::VisualReporting::Property  in the active  NXOpen::VisualReporting::Classifier .  
           
                  
         
        """
        pass
    @property
    def CustomMessageOfReport(self) -> str:
        """
        Getter for property: (str) CustomMessageOfReport
         Returnsthe custom message of the  NXOpen::VisualReporting::VisualReport .  
           
                  
         
        """
        pass
    @CustomMessageOfReport.setter
    def CustomMessageOfReport(self, customMessage: str):
        """
        Setter for property: (str) CustomMessageOfReport
         Returnsthe custom message of the  NXOpen::VisualReporting::VisualReport .  
           
                  
         
        """
        pass
    @property
    def CustomMessageOfReportingProperty(self) -> str:
        """
        Getter for property: (str) CustomMessageOfReportingProperty
         Returnsthe custom message of the reporting  NXOpen::VisualReporting::Property  in the active  NXOpen::VisualReporting::Classifier .  
           
                  
         
        """
        pass
    @CustomMessageOfReportingProperty.setter
    def CustomMessageOfReportingProperty(self, customMessage: str):
        """
        Setter for property: (str) CustomMessageOfReportingProperty
         Returnsthe custom message of the reporting  NXOpen::VisualReporting::Property  in the active  NXOpen::VisualReporting::Classifier .  
           
                  
         
        """
        pass
    @property
    def DescriptionOfVisualReport(self) -> str:
        """
        Getter for property: (str) DescriptionOfVisualReport
         Returns the description of the  NXOpen::VisualReporting::VisualReport  being built by this
                    builder.  
          
                  
         
        """
        pass
    @DescriptionOfVisualReport.setter
    def DescriptionOfVisualReport(self, description: str):
        """
        Setter for property: (str) DescriptionOfVisualReport
         Returns the description of the  NXOpen::VisualReporting::VisualReport  being built by this
                    builder.  
          
                  
         
        """
        pass
    @property
    def DescriptiveCategoryOfVisualReport(self) -> str:
        """
        Getter for property: (str) DescriptiveCategoryOfVisualReport
         Returns the descriptive category of the  NXOpen::VisualReporting::VisualReport 
                    being built by this builder.  
          
                  
         
        """
        pass
    @DescriptiveCategoryOfVisualReport.setter
    def DescriptiveCategoryOfVisualReport(self, category: str):
        """
        Setter for property: (str) DescriptiveCategoryOfVisualReport
         Returns the descriptive category of the  NXOpen::VisualReporting::VisualReport 
                    being built by this builder.  
          
                  
         
        """
        pass
    @property
    def DestinationTeamcenterFolder(self) -> str:
        """
        Getter for property: (str) DestinationTeamcenterFolder
         Returns the destination Teamcenter folder for saving the  NXOpen::VisualReporting::VisualReport  being built by this
                    builder to Teamcenter database.  
          
                    Note that this property is only needed when NX is connected to Teamcenter and report is saved as a copy to Teamcenter database.
                    This  NXOpen::VisualReporting::VisualReport::DestinationTeamcenterFolder  may return NULL if you haven't 
                    set a folder name on this property.
                  
         
        """
        pass
    @DestinationTeamcenterFolder.setter
    def DestinationTeamcenterFolder(self, foldername: str):
        """
        Setter for property: (str) DestinationTeamcenterFolder
         Returns the destination Teamcenter folder for saving the  NXOpen::VisualReporting::VisualReport  being built by this
                    builder to Teamcenter database.  
          
                    Note that this property is only needed when NX is connected to Teamcenter and report is saved as a copy to Teamcenter database.
                    This  NXOpen::VisualReporting::VisualReport::DestinationTeamcenterFolder  may return NULL if you haven't 
                    set a folder name on this property.
                  
         
        """
        pass
    @property
    def FilenameOfVisualReport(self) -> str:
        """
        Getter for property: (str) FilenameOfVisualReport
         Returns the file name of the  NXOpen::VisualReporting::VisualReport  being built by this
                    builder.  
          
                    Note that when NX is connected to Teamcenter, this property is the report dataset identifier from Teamcenter database. 
                    If it is a new report, it will be the report dataset name. When the report is save by  NXOpen::VisualReporting::VisualReportBuilder::Save , 
                    the report dataset identifier will be saved in this property.
                  
         
        """
        pass
    @FilenameOfVisualReport.setter
    def FilenameOfVisualReport(self, filename: str):
        """
        Setter for property: (str) FilenameOfVisualReport
         Returns the file name of the  NXOpen::VisualReporting::VisualReport  being built by this
                    builder.  
          
                    Note that when NX is connected to Teamcenter, this property is the report dataset identifier from Teamcenter database. 
                    If it is a new report, it will be the report dataset name. When the report is save by  NXOpen::VisualReporting::VisualReportBuilder::Save , 
                    the report dataset identifier will be saved in this property.
                  
         
        """
        pass
    @property
    def KeywordsOfVisualReport(self) -> str:
        """
        Getter for property: (str) KeywordsOfVisualReport
         Returns the keywords of the  NXOpen::VisualReporting::VisualReport  being built by this
                    builder.  
          
                  
         
        """
        pass
    @KeywordsOfVisualReport.setter
    def KeywordsOfVisualReport(self, keywords: str):
        """
        Setter for property: (str) KeywordsOfVisualReport
         Returns the keywords of the  NXOpen::VisualReporting::VisualReport  being built by this
                    builder.  
          
                  
         
        """
        pass
    @property
    def ReportContextOfVisualReport(self) -> VisualReport.ReportContextOption:
        """
        Getter for property: ( VisualReport.ReportContextOption NXOpen.Vis) ReportContextOfVisualReport
         Returns the  NXOpen::VisualReporting::VisualReport::ReportContextOption  of the  NXOpen::VisualReporting::VisualReport  being built by this builder.  
          
                  
         
        """
        pass
    @ReportContextOfVisualReport.setter
    def ReportContextOfVisualReport(self, reportContext: VisualReport.ReportContextOption):
        """
        Setter for property: ( VisualReport.ReportContextOption NXOpen.Vis) ReportContextOfVisualReport
         Returns the  NXOpen::VisualReporting::VisualReport::ReportContextOption  of the  NXOpen::VisualReporting::VisualReport  being built by this builder.  
          
                  
         
        """
        pass
    @property
    def ReportNameOfVisualReport(self) -> str:
        """
        Getter for property: (str) ReportNameOfVisualReport
         Returns the name of the  NXOpen::VisualReporting::VisualReport  being built by this builder.  
           
                  
         
        """
        pass
    @ReportNameOfVisualReport.setter
    def ReportNameOfVisualReport(self, reportName: str):
        """
        Setter for property: (str) ReportNameOfVisualReport
         Returns the name of the  NXOpen::VisualReporting::VisualReport  being built by this builder.  
           
                  
         
        """
        pass
    @property
    def ReportingObjectTypeOfVisualReport(self) -> VisualReport.ReportingObjectTypeOption:
        """
        Getter for property: ( VisualReport.ReportingObjectTypeOption NXOpen.Vis) ReportingObjectTypeOfVisualReport
         Returns the reporting object type of the  NXOpen::VisualReporting::VisualReport  being built by this builder.  
          
                    Only valid if the  NXOpen::VisualReporting::VisualReport::ScopeType  of the  NXOpen::VisualReporting::VisualReport 
                    is  NXOpen::VisualReporting::VisualReport::ScopeTypeOptionComponent  type.
                  
         
        """
        pass
    @ReportingObjectTypeOfVisualReport.setter
    def ReportingObjectTypeOfVisualReport(self, reportingObjectType: VisualReport.ReportingObjectTypeOption):
        """
        Setter for property: ( VisualReport.ReportingObjectTypeOption NXOpen.Vis) ReportingObjectTypeOfVisualReport
         Returns the reporting object type of the  NXOpen::VisualReporting::VisualReport  being built by this builder.  
          
                    Only valid if the  NXOpen::VisualReporting::VisualReport::ScopeType  of the  NXOpen::VisualReporting::VisualReport 
                    is  NXOpen::VisualReporting::VisualReport::ScopeTypeOptionComponent  type.
                  
         
        """
        pass
    @property
    def ReportingStyleOfVisualReport(self) -> VisualReport.ReportingStyleOption:
        """
        Getter for property: ( VisualReport.ReportingStyleOption NXOpen.Vis) ReportingStyleOfVisualReport
         Returns the reporting style of the  NXOpen::VisualReporting::VisualReport  being built by this builder.  
          
                  
         
        """
        pass
    @ReportingStyleOfVisualReport.setter
    def ReportingStyleOfVisualReport(self, reportingStyle: VisualReport.ReportingStyleOption):
        """
        Setter for property: ( VisualReport.ReportingStyleOption NXOpen.Vis) ReportingStyleOfVisualReport
         Returns the reporting style of the  NXOpen::VisualReporting::VisualReport  being built by this builder.  
          
                  
         
        """
        pass
    @property
    def SaveDestination(self) -> VisualReport.SaveDestinationOption:
        """
        Getter for property: ( VisualReport.SaveDestinationOption NXOpen.Vis) SaveDestination
         Returns the  NXOpen::VisualReporting::VisualReport::SaveDestinationOption  of the  NXOpen::VisualReporting::VisualReport  being built by this
                    builder.  
          
                    Note that this property will always be  NXOpen::VisualReporting::VisualReport::SaveDestinationOptionLocal  when NX is not connected to Teamcenter.
                  
         
        """
        pass
    @SaveDestination.setter
    def SaveDestination(self, destinationOption: VisualReport.SaveDestinationOption):
        """
        Setter for property: ( VisualReport.SaveDestinationOption NXOpen.Vis) SaveDestination
         Returns the  NXOpen::VisualReporting::VisualReport::SaveDestinationOption  of the  NXOpen::VisualReporting::VisualReport  being built by this
                    builder.  
          
                    Note that this property will always be  NXOpen::VisualReporting::VisualReport::SaveDestinationOptionLocal  when NX is not connected to Teamcenter.
                  
         
        """
        pass
    @property
    def ScopeNameOfVisualReport(self) -> str:
        """
        Getter for property: (str) ScopeNameOfVisualReport
         Returns the scope name of visual report.  
          
                    when set the scope name of visual report, the object type of this scope is also setted, so caller no need to call 
                     NXOpen::VisualReporting::VisualReportBuilder::SetScopeTypeOfVisualReport .
                    but if the scope is  NXOpen::VisualReporting::VisualReport::ScopeTypeOptionSubPart , the caller should also call
                     NXOpen::VisualReporting::VisualReportBuilder::SetObjectTypesOfVisualReport  after setting scope name.
                    note that during setting the scope name of visual report, the  NXOpen::VisualReporting::Rule  of this report will be deleted and initilized, so the caller should 
                    get rule again.
                  
         
        """
        pass
    @ScopeNameOfVisualReport.setter
    def ScopeNameOfVisualReport(self, scopeName: str):
        """
        Setter for property: (str) ScopeNameOfVisualReport
         Returns the scope name of visual report.  
          
                    when set the scope name of visual report, the object type of this scope is also setted, so caller no need to call 
                     NXOpen::VisualReporting::VisualReportBuilder::SetScopeTypeOfVisualReport .
                    but if the scope is  NXOpen::VisualReporting::VisualReport::ScopeTypeOptionSubPart , the caller should also call
                     NXOpen::VisualReporting::VisualReportBuilder::SetObjectTypesOfVisualReport  after setting scope name.
                    note that during setting the scope name of visual report, the  NXOpen::VisualReporting::Rule  of this report will be deleted and initilized, so the caller should 
                    get rule again.
                  
         
        """
        pass
    @property
    def ScopeTypeOfVisualReport(self) -> VisualReport.ScopeTypeOption:
        """
        Getter for property: ( VisualReport.ScopeTypeOption NXOpen.Vis) ScopeTypeOfVisualReport
         Returns the  NXOpen::VisualReporting::VisualReport::ScopeTypeOption  of the  NXOpen::VisualReporting::VisualReport  being built by this builder.  
          
                    note that during setting scope type of visual report, the  NXOpen::VisualReporting::Rule  of this report will be deleted and initilized, so the caller should 
                    get rule again.
                  
         
        """
        pass
    @ScopeTypeOfVisualReport.setter
    def ScopeTypeOfVisualReport(self, scopeType: VisualReport.ScopeTypeOption):
        """
        Setter for property: ( VisualReport.ScopeTypeOption NXOpen.Vis) ScopeTypeOfVisualReport
         Returns the  NXOpen::VisualReporting::VisualReport::ScopeTypeOption  of the  NXOpen::VisualReporting::VisualReport  being built by this builder.  
          
                    note that during setting scope type of visual report, the  NXOpen::VisualReporting::Rule  of this report will be deleted and initilized, so the caller should 
                    get rule again.
                  
         
        """
        pass
    def AddChildToCondition(self, condition: Condition, childCondition: Condition) -> None:
        """
         Add a new child NXOpen.VisualReporting.Condition to this condition. If the child is already a
                    child of another NXOpen.VisualReporting.Condition or NXOpen.VisualReporting.Rule, then it is
                    removed from that other object. The new child must have been created in the same
                    NXOpen.VisualReporting.VisualReport as this parent condition. If this is a
                    NXOpen.VisualReporting.Condition.TypeOption.NotCondition then
                    this replaces the existing child, and the existing child is deleted.
                
        """
        pass
    def CommitAsCopy(self) -> VisualReport:
        """
         When Builder.Commit is called on this builder, it will
                    delete the original NXOpen.VisualReporting.VisualReport whose copy the builder is editing and install the copied
                    NXOpen.VisualReporting.VisualReport to the NXOpen.VisualReporting.VisualReportManager.
                    
                    If it is required not to delete the original NXOpen.VisualReporting.VisualReport,
                    then CommitAsCopy can be called instead. This behaves
                    just like Builder.Commit except it does not delete the
                    original NXOpen.VisualReporting.VisualReport.
                
         Returns newVisualReport ( VisualReport NXOpen.Vis):   .
        """
        pass
    def CreateAndCondition(self) -> Condition:
        """
         Creates a new empty NXOpen.VisualReporting.Condition, but does not add it to a
                    NXOpen.VisualReporting.Rule.
                
         Returns condition ( Condition NXOpen.Vis):  The created condition .
        """
        pass
    def CreateBooleanCondition(self, property: Property, value: bool, operatorType: Condition.OperatorOption) -> Condition:
        """
         Creates a new empty NXOpen.VisualReporting.Condition whose
                    NXOpen.VisualReporting.Condition.Datatype is
                    NXOpen.VisualReporting.Property.DatatypeOption.Boolean,
                    but does not add it to a NXOpen.VisualReporting.Rule.
                
         Returns condition ( Condition NXOpen.Vis):  The created condition .
        """
        pass
    def CreateDateCondition(self, property: Property, value: str, operatorType: Condition.OperatorOption) -> Condition:
        """
         Creates a new empty NXOpen.VisualReporting.Condition whose
                    NXOpen.VisualReporting.Condition.Datatype is
                    NXOpen.VisualReporting.Property.DatatypeOption.Date,
                    but does not add it to a NXOpen.VisualReporting.Rule.
                
         Returns condition ( Condition NXOpen.Vis):  The created condition .
        """
        pass
    def CreateGroupLabel(self, name: str, rule: Rule, afterGroupLabel: GroupLabel) -> GroupLabel:
        """
         Creates a new empty NXOpen.VisualReporting.GroupLabel, and adds it to the given
                    NXOpen.VisualReporting.Rule. This can only be called if the active NXOpen.VisualReporting.Classifier 
                    in this rule is using NXOpen.VisualReporting.Classifier.GroupingMethodOption.Manual grouping.
                
         Returns groupLabel ( GroupLabel NXOpen.Vis):  The created group label .
        """
        pass
    def CreateIntegerCondition(self, property: Property, value: int, operatorType: Condition.OperatorOption) -> Condition:
        """
         Creates a new empty NXOpen.VisualReporting.Condition whose
                    NXOpen.VisualReporting.Condition.Datatype is
                    NXOpen.VisualReporting.Property.DatatypeOption.Integer,
                    but does not add it to a NXOpen.VisualReporting.Rule.
                
         Returns condition ( Condition NXOpen.Vis):  The created condition .
        """
        pass
    def CreateNotCondition(self) -> Condition:
        """
         Creates a new empty NXOpen.VisualReporting.Condition, but does not add it to a
                    NXOpen.VisualReporting.Rule.
                
         Returns condition ( Condition NXOpen.Vis):  The created condition .
        """
        pass
    def CreateNullCondition(self, property: Property, value: bool, operatorType: Condition.OperatorOption) -> Condition:
        """
         Creates a new empty NXOpen.VisualReporting.Condition whose
                    NXOpen.VisualReporting.Condition.Datatype is
                    NXOpen.VisualReporting.Property.DatatypeOption.Null,
                    but does not add it to a NXOpen.VisualReporting.Rule.
                
         Returns condition ( Condition NXOpen.Vis):  The created condition .
        """
        pass
    def CreateOrCondition(self) -> Condition:
        """
         Creates a new empty NXOpen.VisualReporting.Condition, but does not add it to a
                    NXOpen.VisualReporting.Rule.
                
         Returns condition ( Condition NXOpen.Vis):  The created condition .
        """
        pass
    @overload
    def CreateProperty(self, propertyType: Property.TypeOption) -> Property:
        """
         Creates a new empty NXOpen.VisualReporting.Property, but does not add it to a
                    NXOpen.VisualReporting.VisualReport.
                
         Returns property ( Property NXOpen.Vis):  The created property .
        """
        pass
    @overload
    def CreateProperty(self, propertyId: str) -> Property:
        """
         Creates a new empty NXOpen.VisualReporting.Property, but does not add it to a
                    NXOpen.VisualReporting.VisualReport.
                
         Returns createdProperty ( Property NXOpen.Vis):  The created property .
        """
        pass
    def CreateRealCondition(self, property: Property, value: float, operatorType: Condition.OperatorOption, tolerance: float) -> Condition:
        """
         Creates a new empty NXOpen.VisualReporting.Condition whose
                    NXOpen.VisualReporting.Condition.Datatype is
                    NXOpen.VisualReporting.Property.DatatypeOption.Real,
                    but does not add it to a NXOpen.VisualReporting.Rule.
                
         Returns condition ( Condition NXOpen.Vis):  The created condition .
        """
        pass
    def CreateStringCondition(self, property: Property, value: str, operatorType: Condition.OperatorOption) -> Condition:
        """
         Creates a new empty NXOpen.VisualReporting.Condition whose
                    NXOpen.VisualReporting.Condition.Datatype is
                    NXOpen.VisualReporting.Property.DatatypeOption.String,
                    but does not add it to a NXOpen.VisualReporting.Rule.
                
         Returns condition ( Condition NXOpen.Vis):  The created condition .
        """
        pass
    def CreateVisualReport(self) -> VisualReport:
        """
         Creates a new empty NXOpen.VisualReporting.VisualReport and starts editing it.
                    The created NXOpen.VisualReporting.VisualReport will not be added to the
                    NXOpen.VisualReporting.VisualReportManager until Builder.Commit
                    or NXOpen.VisualReporting.VisualReportBuilder.CommitAsCopy is called on this builder.
                
         Returns visualReport ( VisualReport NXOpen.Vis): .
        """
        pass
    def DeleteChildCondition(self, condition: Condition, childCondition: Condition) -> None:
        """
         Deletes a NXOpen.VisualReporting.Condition from its parent condition.
                    If there are NXOpen.VisualReporting.Propertys associated with this condition, these properties will be deleted.
                    If there are child conditions associated with this condtion, these child conditions will be deleted too. 
                
        """
        pass
    def DeleteGroupLabel(self, rule: Rule, groupLabel: GroupLabel) -> None:
        """
         Deletes the given NXOpen.VisualReporting.GroupLabel from the active NXOpen.VisualReporting.Classifier 
                    in this NXOpen.VisualReporting.Rule.
                
        """
        pass
    def DeleteProperty(self, property: Property) -> None:
        """
         Delete NXOpen.VisualReporting.Property which has no owner. Before call this function,
                    User must be sure there is no reference to this object
                
        """
        pass
    def EditVisualReport(self, visualReport: VisualReport) -> None:
        """
         Starts editing a NXOpen.VisualReporting.VisualReport. The builder will create a
                    copy of the given VisualReport and all edits will be applied to that copy. When
                    Builder.Commit is called on this builder, the supplied
                    VisualReport will be deleted and replaced with the new one. Alternatively if
                    NXOpen.VisualReporting.VisualReportBuilder.CommitAsCopy is called, the copied NXOpen.VisualReporting.VisualReport
                    will be added to the NXOpen.VisualReporting.VisualReportManager without deleting the one given in this function.
                    Any current NXOpen.VisualReporting.VisualReport which this builder is currently
                    building will be deleted when this function is called.
                
        """
        pass
    def EnableUnmatchedGroupOfVisualReport(self, enableUnmatchedGroup: bool) -> None:
        """
         Sets whether use of NXOpen.VisualReporting.VisualReport.UnmatchedGroupLabel
                    is enabled for the NXOpen.VisualReporting.VisualReport being built by this builder.
                
        """
        pass
    def GetActiveClassifierOfRule(self, rule: Rule) -> Classifier:
        """
         Gets the active NXOpen.VisualReporting.Classifier in this NXOpen.VisualReporting.Rule
                    for a multiple properties report.
                
         Returns activeClassifier ( Classifier NXOpen.Vis): .
        """
        pass
    def GetAllGroupLabelsOfRule(self, rule: Rule) -> List[GroupLabel]:
        """
         Returns the NXOpen.VisualReporting.GroupLabels associated with the active NXOpen.VisualReporting.Classifier 
                    in this NXOpen.VisualReporting.Rule.
                
         Returns groupLabels ( GroupLabel List[NXOpen.V):  The manually defined groups .
        """
        pass
    def GetBitmapNameOfGroupLabel(self, groupLabel: GroupLabel) -> str:
        """
         Gets the bitmap of the given NXOpen.VisualReporting.GroupLabel.
                
         Returns bitmapName (str):  The bitmap name .
        """
        pass
    def GetChildCondition(self, condition: Condition, index: int) -> Condition:
        """
         Returns the specified child NXOpen.VisualReporting.Condition from this NXOpen.VisualReporting.Condition
                
         Returns childCondition ( Condition NXOpen.Vis): .
        """
        pass
    def GetChildConditions(self, condition: Condition) -> List[Condition]:
        """
         Returns all the child NXOpen.VisualReporting.Conditions in this NXOpen.VisualReporting.Condition
                
         Returns childConditions ( Condition List[NXOpen.V): .
        """
        pass
    def GetClassifierTypeOfRule(self, rule: Rule) -> Classifier.TypeOption:
        """
         Gets the reporting NXOpen.VisualReporting.Classifier.TypeOption for the active NXOpen.VisualReporting.Classifier
                    in this NXOpen.VisualReporting.Rule.
                
         Returns classifierType ( Classifier.TypeOption NXOpen.Vis):  The classifier type .
        """
        pass
    def GetClassifiersOfRule(self, rule: Rule) -> List[Classifier]:
        """
         Returns the NXOpen.VisualReporting.Classifiers associated with this NXOpen.VisualReporting.Rule.
                
         Returns classifiers ( Classifier List[NXOpen.V): .
        """
        pass
    def GetColorOfGroupLabel(self, groupLabel: GroupLabel) -> NXOpen.NXColor.Rgb:
        """
         Gets the NXOpen.VisualReporting.GroupLabel.Color
                    of the given NXOpen.VisualReporting.GroupLabel. 
                
         Returns color ( NXOpen.NXColor.Rgb):  The color .
        """
        pass
    def GetCustomMessageOfGroupLabel(self, groupLabel: GroupLabel) -> str:
        """
         Gets the custom message of the givenNXOpen.VisualReporting.GroupLabel.
                
         Returns customMessage (str):  The bitmap name .
        """
        pass
    def GetDateGroupMethodOfRule(self, rule: Rule) -> Classifier.DateGroupMethodOption:
        """
         Gets the NXOpen.VisualReporting.Classifier.DateGroupMethodOption of the active NXOpen.VisualReporting.Classifier 
                    in the given NXOpen.VisualReporting.Rule. 
                    
                    Only valid if the active NXOpen.VisualReporting.Classifier in the rule 
                    is NXOpen.VisualReporting.Classifier.TypeOption.Range type.
                
         Returns dateGroupMethod ( Classifier.DateGroupMethodOption NXOpen.Vis):  The range method .
        """
        pass
    def GetDescriptionOfCondition(self, condition: Condition) -> str:
        """
         Gets the NXOpen.VisualReporting.Condition.Description of the
                    specified NXOpen.VisualReporting.Condition.
                    Only valid for a NXOpen.VisualReporting.Condition whose
                    NXOpen.VisualReporting.Condition.Type is NXOpen.VisualReporting.Condition.TypeOption.ValueCondition
                
         Returns description (str):  The description .
        """
        pass
    def GetDisplayStyleForGroupLabel(self, groupLabel: GroupLabel) -> GroupLabel.DisplayStyleOption:
        """
         Gets the NXOpen.VisualReporting.GroupLabel.DisplayStyleOption 
                    of the given NXOpen.VisualReporting.GroupLabel 
                
         Returns displayStyle ( GroupLabel.DisplayStyleOption NXOpen.Vis):  The display style .
        """
        pass
    def GetErrorLevelOfGroupLabel(self, groupLabel: GroupLabel) -> NXOpen.Validation.Result:
        """
         Gets the error level of the givenNXOpen.VisualReporting.GroupLabel.
                
         Returns errorLevel ( NXOpen.Validation.Result):  The error level .
        """
        pass
    def GetFilterConditionOfRule(self, rule: Rule) -> Condition:
        """
         Gets the filter NXOpen.VisualReporting.Condition from this rule. 
                
         Returns filterCondition ( Condition NXOpen.Vis):  The filter condition .
        """
        pass
    def GetGroupingMethodOfRule(self, rule: Rule) -> Classifier.GroupingMethodOption:
        """
         Gets the NXOpen.VisualReporting.Classifier.GroupingMethodOption of the active NXOpen.VisualReporting.Classifier
                    in this NXOpen.VisualReporting.Rule.
                
         Returns groupingMethod ( Classifier.GroupingMethodOption NXOpen.Vis):  The grouping method .
        """
        pass
    def GetHasUserSpecifiedValueForCondition(self, condition: Condition) -> bool:
        """
         Gets NXOpen.VisualReporting.Condition.HasUserSpecifiedValue on the
                    specified NXOpen.VisualReporting.Condition.
                    Only valid for a NXOpen.VisualReporting.Condition whose
                    NXOpen.VisualReporting.Condition.Type is NXOpen.VisualReporting.Condition.TypeOption.ValueCondition
                
         Returns isUserSpecified (bool):  Whether the condition's value should be user-specified .
        """
        pass
    def GetLowerBoundOfGroupLabel(self, groupLabel: GroupLabel) -> str:
        """
         Gets the NXOpen.VisualReporting.GroupLabel.LowerBound
                    of the given NXOpen.VisualReporting.GroupLabel.
                
         Returns lowerBound (str):  The lower bound .
        """
        pass
    def GetManualGroupLabelOfRule(self, rule: Rule, index: int) -> GroupLabel:
        """
         Returns the specified NXOpen.VisualReporting.GroupLabels associated with the active NXOpen.VisualReporting.Classifier 
                    in this NXOpen.VisualReporting.Rule which are manually defined.
                
         Returns groupLabel ( GroupLabel NXOpen.Vis):  The specified manually defined group .
        """
        pass
    def GetManualGroupLabelsOfRule(self, rule: Rule) -> List[GroupLabel]:
        """
         Returns the NXOpen.VisualReporting.GroupLabels associated with the active NXOpen.VisualReporting.Classifier 
                    in this NXOpen.VisualReporting.Rule which are manually defined.
                
         Returns groupLabels ( GroupLabel List[NXOpen.V):  The manually defined groups .
        """
        pass
    def GetManualGroupingForRule(self, rule: Rule) -> bool:
        """
         Gets whether the NXOpen.VisualReporting.Classifier.GroupingMethodOption of the active NXOpen.VisualReporting.Classifier
                    in this NXOpen.VisualReporting.Rule is NXOpen.VisualReporting.Classifier.GroupingMethodOption.Manual. 
                
         Returns isManualGrouping (bool):  Whether manual grouping should be used .
        """
        pass
    def GetObjectTypesOfVisualReport(self) -> List[VisualReport.ObjectTypeOption]:
        """
         Gets the NXOpen.VisualReporting.VisualReport.ObjectTypeOptions of the NXOpen.VisualReporting.VisualReport being built by this builder.
                    Only valid if the NXOpen.VisualReporting.VisualReport.ScopeType of the NXOpen.VisualReporting.VisualReport
                    is NXOpen.VisualReporting.VisualReport.ScopeTypeOption.SubPart type.
                
         Returns objectTypes ( VisualReport.ObjectTypeOption List[NXOpen.V):  The object types .
        """
        pass
    def GetOperatorTypeOfCondition(self, condition: Condition) -> Condition.OperatorOption:
        """
         Gets the NXOpen.VisualReporting.Condition.OperatorOption of this condition. Only valid if
                    NXOpen.VisualReporting.Condition.TypeOption is
                    NXOpen.VisualReporting.Condition.TypeOption.ValueCondition
                
         Returns operatorType ( Condition.OperatorOption NXOpen.Vis):  The operator type being set .
        """
        pass
    def GetParentCondition(self, condition: Condition) -> Condition:
        """
         Gets the parent condition of this NXOpen.VisualReporting.Condition. If this
                    condition has no parent or if the parent isn't a condition
                    then this returns .
                
         Returns parentCondition ( Condition NXOpen.Vis): .
        """
        pass
    def GetPropertyForComparison(self, condition: Condition) -> Property:
        """
         Gets the NXOpen.VisualReporting.Property in the value for comparison of this NXOpen.VisualReporting.Condition. 
                
         Returns property ( Property NXOpen.Vis):  The property .
        """
        pass
    def GetPropertyOfCondition(self, condition: Condition) -> Property:
        """
         Gets the NXOpen.VisualReporting.Property of this condition. 
                    Only valid for a NXOpen.VisualReporting.Condition whose
                    NXOpen.VisualReporting.Condition.Type is NXOpen.VisualReporting.Condition.TypeOption.ValueCondition
                
         Returns property ( Property NXOpen.Vis):  The property .
        """
        pass
    def GetPropertySpecification(self, property: Property) -> Tuple[Property.TypeOption, str, str]:
        """
         Gets the property specification of the NXOpen.VisualReporting.Property being built by this builder.
                
         Returns A tuple consisting of (propertyType, key, name). 
         - propertyType is:  Property.TypeOption NXOpen.Vis. Property Type of the NXOpen.VisualReporting.Property .
         - key is: str. property key .
         - name is: str. property name .

        """
        pass
    def GetRangeMethodOfRule(self, rule: Rule) -> Classifier.RangeMethodOption:
        """
         Gets the NXOpen.VisualReporting.Classifier.RangeMethodOption of the active NXOpen.VisualReporting.Classifier 
                    in the given NXOpen.VisualReporting.Rule. 
                    
                    Only valid if the active NXOpen.VisualReporting.Classifier in the rule 
                    is NXOpen.VisualReporting.Classifier.TypeOption.Range type.
                
         Returns rangeMethod ( Classifier.RangeMethodOption NXOpen.Vis):  The range method .
        """
        pass
    def GetReferencePropertiesOfReport(self) -> Tuple[List[Property], List[VisualReportBuilder.PropertyUsageOption], int]:
        """
        Gets the message NXOpen.VisualReporting.Property  list of the NXOpen.VisualReporting.VisualReport. 
                
         Returns A tuple consisting of (properties, usages, notUsed). 
         - properties is:  Property List[NXOpen.V. The reference properties of report.
         - usages is:  VisualReportBuilder.PropertyUsageOption List[NXOpen.V. The usages of report.
         - notUsed is: int.

        """
        pass
    def GetReferencePropertiesOfReportingProperty(self) -> Tuple[List[Property], List[VisualReportBuilder.PropertyUsageOption]]:
        """
         Gets the message NXOpen.VisualReporting.Property  list of the NXOpen.VisualReporting.Property
                    in the active NXOpen.VisualReporting.Classifier. 
                
         Returns A tuple consisting of (properties, usages). 
         - properties is:  Property List[NXOpen.V. The reference properties of property.
         - usages is:  VisualReportBuilder.PropertyUsageOption List[NXOpen.V. The usages .

        """
        pass
    def GetReportingDatatypeOfRule(self, rule: Rule) -> Property.DatatypeOption:
        """
         Gets the NXOpen.VisualReporting.Property.DatatypeOption of the active NXOpen.VisualReporting.Classifier's reporting NXOpen.VisualReporting.Property
                    in this NXOpen.VisualReporting.Rule.
                
         Returns datatype ( Property.DatatypeOption NXOpen.Vis):  The datatype.
        """
        pass
    def GetReportingPropertyOfRule(self, rule: Rule) -> Property:
        """
         Gets the reporting NXOpen.VisualReporting.Property for the active NXOpen.VisualReporting.Classifier
                    in this NXOpen.VisualReporting.Rule.
                
         Returns reportingProperty ( Property NXOpen.Vis):  The property .
        """
        pass
    def GetRule(self, index: int) -> Rule:
        """
         Return the specified NXOpen.VisualReporting.Rule from the NXOpen.VisualReporting.VisualReport
                    being built by this builder.
                
         Returns rule ( Rule NXOpen.Vis): .
        """
        pass
    def GetRules(self) -> List[Rule]:
        """
         Returns all the NXOpen.VisualReporting.Rules in the NXOpen.VisualReporting.VisualReport 
                    being built by this builder.
                
         Returns rules ( Rule List[NXOpen.V): .
        """
        pass
    def GetTagPriorityOfGroupLabel(self, groupLabel: GroupLabel) -> GroupLabel.TagPriorityOption:
        """
         Gets the priority of the givenNXOpen.VisualReporting.GroupLabel.
                
         Returns tagPriority ( GroupLabel.TagPriorityOption NXOpen.Vis):  The priority .
        """
        pass
    def GetToleranceOfRule(self, rule: Rule) -> float:
        """
         Gets the tolerance of the active NXOpen.VisualReporting.Classifier in the given NXOpen.VisualReporting.Rule
                    Only valid if the active NXOpen.VisualReporting.Classifier in the rule 
                    is NXOpen.VisualReporting.Classifier.TypeOption.Value type.
                
         Returns tolerance (float):  The tolerance value .
        """
        pass
    def GetUpperBoundOfGroupLabel(self, groupLabel: GroupLabel) -> str:
        """
         Gets the NXOpen.VisualReporting.GroupLabel.UpperBound
                    of the given NXOpen.VisualReporting.GroupLabel.
                
         Returns upperBound (str):  The upper bound .
        """
        pass
    def GetUserNameOfGroupLabel(self, groupLabel: GroupLabel) -> str:
        """
         Gets the NXOpen.NXObject.Name
                    of the given NXOpen.VisualReporting.GroupLabel. 
                
         Returns name (str):  The name .
        """
        pass
    def GetUserPromptOfCondition(self, condition: Condition) -> str:
        """
         Gets the NXOpen.VisualReporting.Condition.UserPrompt of the
                    specified NXOpen.VisualReporting.Condition.
                    Only valid for a NXOpen.VisualReporting.Condition whose
                    NXOpen.VisualReporting.Condition.Type is NXOpen.VisualReporting.Condition.TypeOption.ValueCondition
                
         Returns userPrompt (str):  The user-prompt  .
        """
        pass
    def GetValueOfCondition(self, condition: Condition) -> str:
        """
         Gets the value of this NXOpen.VisualReporting.Condition. 
                    Only valid for a NXOpen.VisualReporting.Condition whose
                    NXOpen.VisualReporting.Condition.Type is NXOpen.VisualReporting.Condition.TypeOption.ValueCondition
                
         Returns value (str): .
        """
        pass
    def GetValueOfGroupLabel(self, groupLabel: GroupLabel) -> str:
        """
         Gets the NXOpen.VisualReporting.GroupLabel.Value
                    of the given NXOpen.VisualReporting.GroupLabel.
                
         Returns value (str):  The value .
        """
        pass
    def IsChildCondition(self, condition: Condition, childCondition: Condition) -> bool:
        """
         Returns whether the given NXOpen.VisualReporting.Condition is an immediate child of this condition
                
         Returns isChild (bool): .
        """
        pass
    def RemoveChildFromCondition(self, condition: Condition, childCondition: Condition) -> None:
        """
         Removes a condition from its parent condition. If the condition has an associated NXOpen.VisualReporting.Property
                    that will be deleted too. If the condition has any child conditions, those will all
                    be deleted too.
                
        """
        pass
    def RemoveFilterConditionFromRule(self, rule: Rule) -> None:
        """
         Removes any existing filter NXOpen.VisualReporting.Condition from this rule. This will not delete
                    the condition.
                
        """
        pass
    def RemovePropertyFromCondition(self, condition: Condition) -> None:
        """
         Removes the current NXOpen.VisualReporting.Property from this condition
                    without deleting it.
                
        """
        pass
    def Save(self) -> None:
        """
         Saves the NXOpen.VisualReporting.VisualReport to its current NXOpen.VisualReporting.VisualReportBuilder.FilenameOfVisualReport .
                    Note that when NX is connected to Teamcenter, the NXOpen.VisualReporting.VisualReportBuilder.FilenameOfVisualReport will be 
                    updated to the report dataset identifier after the report is saved to Teamcenter database.
                
        """
        pass
    def SetActiveClassifierOfRule(self, rule: Rule, activeClassifier: Classifier) -> None:
        """
         Sets the active NXOpen.VisualReporting.Classifier in this NXOpen.VisualReporting.Rule
                    for a multiple properties report.
                
        """
        pass
    def SetBitmapNameOfGroupLabel(self, groupLabel: GroupLabel, bitmapName: str) -> None:
        """
         Sets the bitmap of the given NXOpen.VisualReporting.GroupLabel.
                
        """
        pass
    def SetClassifierTypeOfRule(self, rule: Rule, classifierType: Classifier.TypeOption) -> Classifier:
        """
         Sets the reporting NXOpen.VisualReporting.Classifier.TypeOption for the active NXOpen.VisualReporting.Classifier
                    in this NXOpen.VisualReporting.Rule.
                    Note that the old NXOpen.VisualReporting.Classifier in this NXOpen.VisualReporting.Rule will be deleted 
                    and a new NXOpen.VisualReporting.Classifier will be created and set as the active NXOpen.VisualReporting.Classifier
                    in this NXOpen.VisualReporting.Rule.
                
         Returns newClassifier ( Classifier NXOpen.Vis):  The new active classifier .
        """
        pass
    def SetColorOfGroupLabel(self, groupLabel: GroupLabel, color: NXOpen.NXColor.Rgb) -> None:
        """
         Sets the NXOpen.VisualReporting.GroupLabel.Color
                    of the given NXOpen.VisualReporting.GroupLabel. This also changes
                    NXOpen.VisualReporting.GroupLabel.DisplayStyle
                    to NXOpen.VisualReporting.GroupLabel.DisplayStyleOption.SpecifiedColor.
                
        """
        pass
    def SetCustomMessageOfGroupLabel(self, groupLabel: GroupLabel, customMessage: str) -> None:
        """
         Sets the custom message of the given NXOpen.VisualReporting.GroupLabel.
                
        """
        pass
    def SetDateGroupMethodOfRule(self, rule: Rule, dateGroupMethod: Classifier.DateGroupMethodOption) -> None:
        """
         Sets the NXOpen.VisualReporting.Classifier.DateGroupMethodOption of the active NXOpen.VisualReporting.Classifier 
                    in the given NXOpen.VisualReporting.Rule. 
                    
                    Only valid if the active NXOpen.VisualReporting.Classifier in the rule 
                    is NXOpen.VisualReporting.Classifier.TypeOption.Range type.
                
        """
        pass
    def SetDescriptionOfCondition(self, condition: Condition, description: str) -> None:
        """
         Sets the NXOpen.VisualReporting.Condition.Description of the
                    specified NXOpen.VisualReporting.Condition.
                    Only valid for a NXOpen.VisualReporting.Condition whose
                    NXOpen.VisualReporting.Condition.Type is NXOpen.VisualReporting.Condition.TypeOption.ValueCondition
                
        """
        pass
    def SetDisplayStyleForGroupLabel(self, groupLabel: GroupLabel, displayStyle: GroupLabel.DisplayStyleOption) -> None:
        """
         Sets the NXOpen.VisualReporting.GroupLabel.DisplayStyleOption 
                    of the given NXOpen.VisualReporting.GroupLabel 
                
        """
        pass
    def SetErrorLevelOfGroupLabel(self, groupLabel: GroupLabel, errorLevel: NXOpen.Validation.Result) -> None:
        """
         Sets the priority of the givenNXOpen.VisualReporting.GroupLabel.
                
        """
        pass
    def SetFilterConditionOfRule(self, rule: Rule, filterCondition: Condition) -> None:
        """
         Sets the filter NXOpen.VisualReporting.Condition from this rule. Setting this will delete
                    any existing NXOpen.VisualReporting.Rule.FilterCondition and all of its children
                    (except it won't delete the replacement NXOpen.VisualReporting.Condition being set
                    by this call).
                
        """
        pass
    def SetGroupingMethodOfRule(self, rule: Rule, groupingMethod: Classifier.GroupingMethodOption) -> None:
        """
         Sets the NXOpen.VisualReporting.Classifier.GroupingMethodOption of the active NXOpen.VisualReporting.Classifier 
                    in the given NXOpen.VisualReporting.Rule.
                    If the active NXOpen.VisualReporting.Classifier uses manual grouping then no NXOpen.VisualReporting.GroupLabels 
                    will be automatically generated, and they should instead be added using NXOpen.VisualReporting.VisualReportBuilder.CreateGroupLabel.
                
        """
        pass
    def SetHasUserSpecifiedValueForCondition(self, condition: Condition, isUserSpecified: bool) -> None:
        """
         Sets NXOpen.VisualReporting.Condition.HasUserSpecifiedValue on the
                    specified NXOpen.VisualReporting.Condition.
                    Only valid for a NXOpen.VisualReporting.Condition whose
                    NXOpen.VisualReporting.Condition.Type is NXOpen.VisualReporting.Condition.TypeOption.ValueCondition
                
        """
        pass
    def SetLowerBoundOfGroupLabel(self, groupLabel: GroupLabel, lowerBound: str) -> None:
        """
         Sets the NXOpen.VisualReporting.GroupLabel.LowerBound
                    of the given NXOpen.VisualReporting.GroupLabel.
                
        """
        pass
    def SetManualGroupingForRule(self, rule: Rule, isManualGrouping: bool) -> None:
        """
         Sets whether the NXOpen.VisualReporting.Classifier.GroupingMethodOption of the active NXOpen.VisualReporting.Classifier
                    in this NXOpen.VisualReporting.Rule is NXOpen.VisualReporting.Classifier.GroupingMethodOption.Manual. 
                    If it uses NXOpen.VisualReporting.Classifier.GroupingMethodOption.Manual, then no
                    NXOpen.VisualReporting.GroupLabels will be automatically generated, and they should
                    instead be added manually as required using NXOpen.VisualReporting.VisualReportBuilder.CreateGroupLabel.
                
        """
        pass
    def SetObjectTypesOfVisualReport(self, objectTypes: List[VisualReport.ObjectTypeOption]) -> None:
        """
         Sets the NXOpen.VisualReporting.VisualReport.ObjectTypeOptions of the NXOpen.VisualReporting.VisualReport being built by this builder.
                    Only valid if the NXOpen.VisualReporting.VisualReport.ScopeType of the NXOpen.VisualReporting.VisualReport
                    is NXOpen.VisualReporting.VisualReport.ScopeTypeOption.SubPart type.
                    note that during setting object type of visual report, the NXOpen.VisualReporting.Rule of this report will be deleted and initilized, so the caller should 
                    get rule again.
                
        """
        pass
    def SetOperatorTypeOfCondition(self, condition: Condition, operatorType: Condition.OperatorOption) -> None:
        """
         Sets the NXOpen.VisualReporting.Condition.OperatorOption of this condition. Only valid if
                    NXOpen.VisualReporting.Condition.TypeOption is
                    NXOpen.VisualReporting.Condition.TypeOption.ValueCondition
                
        """
        pass
    def SetPropertyForComparison(self, condition: Condition, property: Property) -> None:
        """
         Sets the NXOpen.VisualReporting.Property in the value for comparison of this NXOpen.VisualReporting.Condition. If the
                    NXOpen.VisualReporting.Property is set to , then it is
                    deleted.
                
        """
        pass
    def SetPropertyOfCondition(self, condition: Condition, property: Property) -> None:
        """
         Sets the NXOpen.VisualReporting.Property of this condition. If the
                    NXOpen.VisualReporting.Property is set to , then it is
                    deleted.
                    Only valid for a NXOpen.VisualReporting.Condition whose
                    NXOpen.VisualReporting.Condition.Type is NXOpen.VisualReporting.Condition.TypeOption.ValueCondition
                
        """
        pass
    @overload
    def SetPropertySpecification(self, property: Property, key: str) -> None:
        """
         Sets the property specification of the NXOpen.VisualReporting.Property being built by this builder.
                
        """
        pass
    @overload
    def SetPropertySpecification(self, property: Property, key: str, name: str) -> None:
        """
         Sets the property specification of the NXOpen.VisualReporting.Property being built by this builder.
                
        """
        pass
    def SetRangeMethodOfRule(self, rule: Rule, rangeMethod: Classifier.RangeMethodOption) -> None:
        """
         Sets the NXOpen.VisualReporting.Classifier.RangeMethodOption of the active NXOpen.VisualReporting.Classifier 
                    in the given NXOpen.VisualReporting.Rule. 
                    
                    Only valid if the active NXOpen.VisualReporting.Classifier in the rule 
                    is NXOpen.VisualReporting.Classifier.TypeOption.Range type.
                
        """
        pass
    def SetReferencePropertiesOfReport(self, properties: List[Property], usages: List[VisualReportBuilder.PropertyUsageOption]) -> None:
        """
        Sets the message NXOpen.VisualReporting.Property list of the NXOpen.VisualReporting.VisualReport.
                
        """
        pass
    def SetReferencePropertiesOfReportingProperty(self, properties: List[Property], usages: List[VisualReportBuilder.PropertyUsageOption]) -> None:
        """
         Sets the message NXOpen.VisualReporting.Property list of the NXOpen.VisualReporting.Property
                    in the active NXOpen.VisualReporting.Classifier.
                
        """
        pass
    def SetReportingDatatypeOfRule(self, rule: Rule, datatype: Property.DatatypeOption) -> None:
        """
         Sets the NXOpen.VisualReporting.Property.DatatypeOption of the active NXOpen.VisualReporting.Classifier's reporting NXOpen.VisualReporting.Property
                    in this NXOpen.VisualReporting.Rule.
                    However datatype must not be NXOpen.VisualReporting.Property.DatatypeOption.Unknown.
                
        """
        pass
    def SetReportingPropertyOfRule(self, rule: Rule, reportingProperty: Property) -> None:
        """
         Sets the reporting NXOpen.VisualReporting.Property for the active NXOpen.VisualReporting.Classifier
                    in this NXOpen.VisualReporting.Rule.
                    If the reporting NXOpen.VisualReporting.Property of the rule is set to , then it is deleted.
                    Only valid for a NXOpen.VisualReporting.Classifier in this NXOpen.VisualReporting.Rule whose
                    NXOpen.VisualReporting.Classifier.TypeOption is NXOpen.VisualReporting.Classifier.TypeOption.Value
                    or NXOpen.VisualReporting.Classifier.TypeOption.Range.
                
        """
        pass
    def SetTagPriorityOfGroupLabel(self, groupLabel: GroupLabel, tagPriority: GroupLabel.TagPriorityOption) -> None:
        """
         Sets the priority of the givenNXOpen.VisualReporting.GroupLabel.
                
        """
        pass
    def SetToleranceOfRule(self, rule: Rule, tolerance: float) -> None:
        """
         Sets the tolerance of the active NXOpen.VisualReporting.Classifier in the given NXOpen.VisualReporting.Rule
                    Only valid if the active NXOpen.VisualReporting.Classifier in the rule 
                    is NXOpen.VisualReporting.Classifier.TypeOption.Value type.
                
        """
        pass
    def SetUpperBoundOfGroupLabel(self, groupLabel: GroupLabel, upperBound: str) -> None:
        """
         Sets the NXOpen.VisualReporting.GroupLabel.UpperBound
                    of the given NXOpen.VisualReporting.GroupLabel.
                
        """
        pass
    def SetUserNameOfGroupLabel(self, groupLabel: GroupLabel, name: str) -> None:
        """
         Sets the NXOpen.NXObject.Name
                    of the given NXOpen.VisualReporting.GroupLabel. Calling this function
                    will cause NXOpen.VisualReporting.GroupLabel.IsNameUserSpecified
                    to return true.
                
        """
        pass
    def SetUserPromptOfCondition(self, condition: Condition, userPrompt: str) -> None:
        """
         Sets the NXOpen.VisualReporting.Condition.UserPrompt of the
                    specified NXOpen.VisualReporting.Condition.
                    Only valid for a NXOpen.VisualReporting.Condition whose
                    NXOpen.VisualReporting.Condition.Type is NXOpen.VisualReporting.Condition.TypeOption.ValueCondition
                
        """
        pass
    def SetValueOfCondition(self, condition: Condition, value: str) -> None:
        """
         Sets the value of this NXOpen.VisualReporting.Condition. 
                    Only valid for a NXOpen.VisualReporting.Condition whose
                    NXOpen.VisualReporting.Condition.Type is NXOpen.VisualReporting.Condition.TypeOption.ValueCondition
                
        """
        pass
    def SetValueOfGroupLabel(self, groupLabel: GroupLabel, value: str) -> None:
        """
         Sets the NXOpen.VisualReporting.GroupLabel.Value
                    of the given NXOpen.VisualReporting.GroupLabel.
                
        """
        pass
    def UnsetUserNameOfGroupLabel(self, groupLabel: GroupLabel) -> None:
        """
         Resets the NXOpen.VisualReporting.GroupLabel.IsNameUserSpecified
                    status of the given NXOpen.VisualReporting.GroupLabel so that the name is now
                    system-generated.
                
        """
        pass
import NXOpen
class VisualReportCollection(NXOpen.TaggedObjectCollection): 
    """
        A collection of visual reports.
    """
    def FindObject(self, journalIdentifier: str) -> VisualReport:
        """
         Finds the NXOpen.VisualReporting.VisualReport with the given identifier as recorded in a journal. 
                An object may not return the same value as its JournalIdentifier in different versions of 
                the software. However newer versions of the software should find the same object when 
                FindObject is passed older versions of its journal identifier. In general, this method 
                should not be used in handwritten code and exists to support record and playback of journals.
            
                An exception will be thrown if no object can be found with the given journal identifier. 
         Returns visualReport ( VisualReport NXOpen.Vis):  Visual report found, or null if no such visual report exists.
        """
        pass
import NXOpen
class VisualReportExplorer(NXOpen.Object): 
    """
        The Explorer of the results of a visual report.
        The Visual Report Explorer enables a report to focus on specified objects
        or on a particular group in the visual report.
    """
    class ExploreReportOption(Enum):
        """
        Members Include: 
         |Off|  Explore Visual Report results is off 
         |On|  Explore Visual Report results is on 

        """
        Off: int
        On: int
        @staticmethod
        def ValueOf(value: int) -> VisualReportExplorer.ExploreReportOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ReportDownStatus(Enum):
        """
        Members Include: 
         |NotSet|  There are no objects of interest below the specified objects 
         |End|  Report Down has reached the lowest level on all branches of the assembly 
         |More|  There are more objects of interest below the currently reported upon objects 

        """
        NotSet: int
        End: int
        More: int
        @staticmethod
        def ValueOf(value: int) -> VisualReportExplorer.ReportDownStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ReportOnObjectsOption(Enum):
        """
        Members Include: 
         |Replace|  Replace the existing set of objects 
         |Add|  Add to the existing set of objects 

        """
        Replace: int
        Add: int
        @staticmethod
        def ValueOf(value: int) -> VisualReportExplorer.ReportOnObjectsOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ExploreReport(self) -> VisualReportExplorer.ExploreReportOption:
        """
        Getter for property: ( VisualReportExplorer.ExploreReportOption NXOpen.Vis) ExploreReport
         Returns the Explore Report setting
                  
            
         
        """
        pass
    @ExploreReport.setter
    def ExploreReport(self, exploreReportOption: VisualReportExplorer.ExploreReportOption):
        """
        Setter for property: ( VisualReportExplorer.ExploreReportOption NXOpen.Vis) ExploreReport
         Returns the Explore Report setting
                  
            
         
        """
        pass
    def ClearReportObjects() -> None:
        """
         Remove all objects from the visual report.
                
        """
        pass
    def GetExploringGroup() -> GroupLabel:
        """
         Gets the exploring NXOpen.VisualReporting.GroupLabel
                
         Returns groupLabel ( GroupLabel NXOpen.Vis):  The exploring group .
        """
        pass
    def RemoveReportObjects(nxObjects: List[NXOpen.NXObject]) -> None:
        """
         Remove objects from report.
                
        """
        pass
    @overload
    def ReportDown(reportOnObjectsOption: VisualReportExplorer.ReportOnObjectsOption) -> VisualReportExplorer.ReportDownStatus:
        """
         Report down the assembly, starting from the NXOpen.Assemblies.ComponentAssembly.RootComponent.
                    A group to explore should have been specified for this method to         
                    have any effect.
                    The first time this method is called the operation will start from
                    NXOpen.Assemblies.ComponentAssembly.RootComponent.
                    On subsequent calls, the set of objects currently reported upon 
                    will be used as the starting point.
                
         Returns reportDownStatus ( VisualReportExplorer.ReportDownStatus NXOpen.Vis):  Status from the report down operation .
        """
        pass
    @overload
    def ReportDown(nxObjects: List[NXOpen.NXObject], reportOnObjectsOption: VisualReportExplorer.ReportOnObjectsOption) -> VisualReportExplorer.ReportDownStatus:
        """
         Report down from a starting array of objects.
                    A group to explore should have been specified for this method to
                    have any effect.
                    On subsequent calls to NXOpen.VisualReporting.VisualReportExplorer.ReportDown, with no nxObjects
                    array, the set of objects currently reported upon will be used as the 
                    starting point.
                
         Returns reportDownStatus ( VisualReportExplorer.ReportDownStatus NXOpen.Vis):  Status from the report down operation .
        """
        pass
    def ReportOnChildren(nxObjects: List[NXOpen.NXObject], reportOnObjectsOption: VisualReportExplorer.ReportOnObjectsOption) -> None:
        """
         Report on the children of nxObjects.
                    The children will either replace the existing contents of the report
                    or be added to the report.
                    This operation is intended for NXOpen.Assemblies.Components
                    and will report on direct children of the components.
                    If an object is not an instance of NXOpen.Assemblies.Component
                    or if it has no children then nothing will be changed.
                
        """
        pass
    def ReportOnObjects(nxObjects: List[NXOpen.NXObject], reportOnObjectsOption: VisualReportExplorer.ReportOnObjectsOption) -> None:
        """
         Set objects to report upon.
                
        """
        pass
    def ReportOnParents(nxObjects: List[NXOpen.NXObject], reportOnObjectsOption: VisualReportExplorer.ReportOnObjectsOption) -> None:
        """
         Report on the parents of the nxObjects.
                    The parents will either replace the existing contents of the report
                    or be added to the report.
                    This operation is intended for NXOpen.Assemblies.Components
                    and will report on the parent of the component.
                    If the object is not an instance of NXOpen.Assemblies.Component
                    or if it has no parent then nothing will be changed.
                
        """
        pass
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
    def SetGroupToExplore(groupLabel: GroupLabel) -> None:
        """
         Sets the NXOpen.VisualReporting.GroupLabel to explore.
                    The NXOpen.VisualReporting.GroupLabel to explore can be set to .
                    If there is no active visual report, then nothing will happen.
                    Note that the NXOpen.VisualReporting.GroupLabel should belong to the active visual report
                    otherwise the call will fail.
                    This method will also cause the objects reported upon to be reset in the
                    same way as a call to ResetReportObjects.
                
        """
        pass
import NXOpen
class VisualReportManager(NXOpen.Object): 
    """
        A manager for load, creation and activation of visual reports.
    """
    @property
    def Current(self) -> VisualReport:
        """
        Getter for property: ( VisualReport NXOpen.Vis) Current
         Returns 
                    the current  NXOpen::VisualReporting::VisualReport .  
          
                  
         
        """
        pass
    @Current.setter
    def Current(self, visualReport: VisualReport):
        """
        Setter for property: ( VisualReport NXOpen.Vis) Current
         Returns 
                    the current  NXOpen::VisualReporting::VisualReport .  
          
                  
         
        """
        pass
    @property
    def VisualReports() -> VisualReportCollection:
        """
         Returns the  NXOpen::VisualReporting::VisualReportCollection  belonging to this visual report manager 
        """
        pass
    @property
    def VisualReportExplorer() -> VisualReportExplorer:
        """
         Returns the  NXOpen::VisualReporting::VisualReportExplorer  belonging to this visual report manager 
        """
        pass
    def ActivateCurrentVisualReport() -> None:
        """
          Activates the NXOpen.VisualReporting.VisualReportManager.Current visual report. 
        """
        pass
    def CreateSpecifyDateBuilder() -> SpecifyDateBuilder:
        """
         Creates a NXOpen.VisualReporting.SpecifyDateBuilder.
                
         Returns specifyDateBuilder ( SpecifyDateBuilder NXOpen.Vis):  The created builder .
        """
        pass
    def CreateVisualReportBuilder(visualReport: VisualReport) -> VisualReportBuilder:
        """
         Creates a NXOpen.VisualReporting.VisualReportBuilder and starts
                    editing a copy of the given NXOpen.VisualReporting.VisualReport.
                
         Returns visualReportBuilder ( VisualReportBuilder NXOpen.Vis):  The created builder .
        """
        pass
    def DeactivateCurrentVisualReport() -> None:
        """
          Deactivates the NXOpen.VisualReporting.VisualReportManager.Current visual report. 
        """
        pass
    GetBooleanTypePropertyValue = Callable[[NXOpen.NXObject], None]
    GetDateTypePropertyValue = Callable[[NXOpen.NXObject], None]
    GetIntegerTypePropertyValue = Callable[[NXOpen.NXObject], None]
    GetRealTypePropertyValue = Callable[[NXOpen.NXObject], None]
    GetStringTypePropertyValue = Callable[[NXOpen.NXObject], None]
    def MergeReports(visualReports: List[VisualReport], mergedReportName: str, mergedReportDescription: str) -> VisualReport:
        """
         Merges multiple existing NXOpen.VisualReporting.VisualReport into one NXOpen.VisualReporting.VisualReport, but does not set them to be the 
                    NXOpen.VisualReporting.VisualReportManager.Current visual report or activate them, and does not save the merged NXOpen.VisualReporting.VisualReport.
                
         Returns mergedReport ( VisualReport NXOpen.Vis):  merged report .
        """
        pass
    def Open(filename: str) -> VisualReport:
        """
         Opens an existing NXOpen.VisualReporting.VisualReport, but does not set it to be the 
                    NXOpen.VisualReporting.VisualReportManager.Current visual report or activate it.
                    If the visual report file cannot be opened, or if there is a problem parsing the file,
                    then an exception will be raised.
                    If opening a managed report then it is recommended to use NXOpen.VisualReporting.VisualReportManager.OpenReports
                    which can take a container path and list of dataset names
                
         Returns visualReport ( VisualReport NXOpen.Vis):  .
        """
        pass
    def OpenReports(folders: List[str], names: List[str]) -> List[VisualReport]:
        """
         Opens existing NXOpen.VisualReporting.VisualReport, but does not set them to be the 
                    NXOpen.VisualReporting.VisualReportManager.Current visual report or activate them.
                    If the visual report file cannot be opened, or if there is a problem parsing the file,
                    then an exception will be raised.
                    This can be used in native mode by sending in a folder path and filenames, or in
                    managed mode using a container path and dataset names.
                
         Returns visualReports ( VisualReport List[NXOpen.V):  array of opened reports .
        """
        pass
    @overload
    def RegisterProperty(propertyKey: str, propertyName: str, scopeType: VisualReport.ScopeTypeOption, objectTypes: List[VisualReport.ObjectTypeOption], dataType: Property.DatatypeOption, isValidInNative: bool, isValidInTeamcenter: bool, getStringTypePropertyValue: VisualReportManager.GetStringTypePropertyValue) -> None:
        """
         Registers a string type property.
                
                    The property key and property name should be unique in current session.
                    Parameters 'isValidInNative' and 'isValidInTeamcenter' shouldn't be 'false' at the same time.
                
        """
        pass
    @overload
    def RegisterProperty(propertyKey: str, propertyName: str, scopeType: VisualReport.ScopeTypeOption, objectTypes: List[VisualReport.ObjectTypeOption], dataType: Property.DatatypeOption, isValidInNative: bool, isValidInTeamcenter: bool, getIntegerTypePropertyValue: VisualReportManager.GetIntegerTypePropertyValue) -> None:
        """
         Registers an integer type property.
                
                    The property key and property name should be unique in current session.
                    Parameters 'isValidInNative' and 'isValidInTeamcenter' shouldn't be 'false' at the same time.
                
        """
        pass
    @overload
    def RegisterProperty(propertyKey: str, propertyName: str, scopeType: VisualReport.ScopeTypeOption, objectTypes: List[VisualReport.ObjectTypeOption], dataType: Property.DatatypeOption, isValidInNative: bool, isValidInTeamcenter: bool, getRealTypePropertyValue: VisualReportManager.GetRealTypePropertyValue) -> None:
        """
         Registers a double type property.
                
                    The property key and property name should be unique in current session.
                    Parameters 'isValidInNative' and 'isValidInTeamcenter' shouldn't be 'false' at the same time.
                
        """
        pass
    @overload
    def RegisterProperty(propertyKey: str, propertyName: str, scopeType: VisualReport.ScopeTypeOption, objectTypes: List[VisualReport.ObjectTypeOption], dataType: Property.DatatypeOption, isValidInNative: bool, isValidInTeamcenter: bool, getBooleanTypePropertyValue: VisualReportManager.GetBooleanTypePropertyValue) -> None:
        """
         Registers a boolean type property.
                
                    The property key and property name should be unique in current session.
                    Parameters 'isValidInNative' and 'isValidInTeamcenter' shouldn't be 'false' at the same time.
                
        """
        pass
    @overload
    def RegisterProperty(propertyKey: str, propertyName: str, scopeType: VisualReport.ScopeTypeOption, objectTypes: List[VisualReport.ObjectTypeOption], dataType: Property.DatatypeOption, isValidInNative: bool, isValidInTeamcenter: bool, getDateTypePropertyValue: VisualReportManager.GetDateTypePropertyValue) -> None:
        """
         Registers a NXOpen.NXObject.ComputationalTime type property.
                
                    The property key and property name should be unique in current session.
                    Parameters 'isValidInNative' and 'isValidInTeamcenter' shouldn't be 'false' at the same time.
                
        """
        pass
    def Unload(visualReport: VisualReport) -> None:
        """
         Unloads an opened  NXOpen.VisualReporting.VisualReport.
                
        """
        pass
    def UnregisterProperty(propertyKey: str) -> None:
        """
         Unregisters a property.
                
                    When the library which the property resides in is unloaded from NX session, this method should be called to unregister the property.
                
        """
        pass
import NXOpen
class VisualReport(NXOpen.NXObject): 
    """
        A visual report can be activated by the NXOpen.VisualReporting.VisualReportManager to 
        apply colors to objects in the graphics window.
        An active visual report groups objects according to filtering conditions and classification 
        rules.  The contents of the groups can be accessed via NXOpen.VisualReporting.VisualReport.GetGroupLabels
        and NXOpen.VisualReporting.VisualReport.GetObjectsInGroup.
    """
    class ObjectTypeOption(Enum):
        """
        Members Include: 
         |Body|  The report objects are bodies 
         |Face|  The report objects are faces 

        """
        Body: int
        Face: int
        @staticmethod
        def ValueOf(value: int) -> VisualReport.ObjectTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ReportContextOption(Enum):
        """
        Members Include: 
         |Assembly|  Collect objects from entire assembly 
         |WorkPart|  Collect objects from work part only 

        """
        Assembly: int
        WorkPart: int
        @staticmethod
        def ValueOf(value: int) -> VisualReport.ReportContextOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ReportingObjectTypeOption(Enum):
        """
        Members Include: 
         |Part|  The reporting objects are parts. 
         |Component|  The reporting objects are components. 
         |Inferred|  The reporting objects are inferred from the properties used in the report. 

        """
        Part: int
        Component: int
        Inferred: int
        @staticmethod
        def ValueOf(value: int) -> VisualReport.ReportingObjectTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ReportingStyleOption(Enum):
        """
        Members Include: 
         |ColorObject|  Matching objects will be colored 
         |TagObject|  Matching objects will be tagged 
         |ColorAndTagObject|  Matching objects will be both colored and tagged 

        """
        ColorObject: int
        TagObject: int
        ColorAndTagObject: int
        @staticmethod
        def ValueOf(value: int) -> VisualReport.ReportingStyleOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SaveDestinationOption(Enum):
        """
        Members Include: 
         |Local|  Saves the report in the local file system. 
         |Teamcenter|  Saves the report in the Teamcenter database. 

        """
        Local: int
        Teamcenter: int
        @staticmethod
        def ValueOf(value: int) -> VisualReport.SaveDestinationOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ScopeTypeOption(Enum):
        """
        Members Include: 
         |Component|  The report is assembly component report 
         |SubPart|  The report is sub-part object report 
         |Application| The report is an application report

        """
        Component: int
        SubPart: int
        Application: int
        @staticmethod
        def ValueOf(value: int) -> VisualReport.ScopeTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BitmapName(self) -> str:
        """
        Getter for property: (str) BitmapName
         Returns the bitmap name of this  NXOpen::VisualReporting::VisualReport .  
          
                  
         
        """
        pass
    @BitmapName.setter
    def BitmapName(self, bitmapName: str):
        """
        Setter for property: (str) BitmapName
         Returns the bitmap name of this  NXOpen::VisualReporting::VisualReport .  
          
                  
         
        """
        pass
    @property
    def CustomMessage(self) -> str:
        """
        Getter for property: (str) CustomMessage
         Returns the custom message of this  NXOpen::VisualReporting::VisualReport .  
          
                  
         
        """
        pass
    @CustomMessage.setter
    def CustomMessage(self, customMessage: str):
        """
        Setter for property: (str) CustomMessage
         Returns the custom message of this  NXOpen::VisualReporting::VisualReport .  
          
                  
         
        """
        pass
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the description of this  NXOpen::VisualReporting::VisualReport 
                  
            
         
        """
        pass
    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
         Returns the description of this  NXOpen::VisualReporting::VisualReport 
                  
            
         
        """
        pass
    @property
    def DescriptiveCategory(self) -> str:
        """
        Getter for property: (str) DescriptiveCategory
         Returns the category of this  NXOpen::VisualReporting::VisualReport .  
          
                  
         
        """
        pass
    @DescriptiveCategory.setter
    def DescriptiveCategory(self, category: str):
        """
        Setter for property: (str) DescriptiveCategory
         Returns the category of this  NXOpen::VisualReporting::VisualReport .  
          
                  
         
        """
        pass
    @property
    def DestinationTeamcenterFolder(self) -> str:
        """
        Getter for property: (str) DestinationTeamcenterFolder
         Returns the destination Teamcenter folder for saving the  NXOpen::VisualReporting::VisualReport  to Teamcenter database.  
          
                    
                    Note that this property is only needed when NX is connected to Teamcenter and report is saved as a copy to Teamcenter database.
                    This  NXOpen::VisualReporting::VisualReport::DestinationTeamcenterFolder  may return NULL if you haven't 
                    set a folder name on this property.
                  
         
        """
        pass
    @DestinationTeamcenterFolder.setter
    def DestinationTeamcenterFolder(self, foldername: str):
        """
        Setter for property: (str) DestinationTeamcenterFolder
         Returns the destination Teamcenter folder for saving the  NXOpen::VisualReporting::VisualReport  to Teamcenter database.  
          
                    
                    Note that this property is only needed when NX is connected to Teamcenter and report is saved as a copy to Teamcenter database.
                    This  NXOpen::VisualReporting::VisualReport::DestinationTeamcenterFolder  may return NULL if you haven't 
                    set a folder name on this property.
                  
         
        """
        pass
    @property
    def Filename(self) -> str:
        """
        Getter for property: (str) Filename
         Returns the filename where this  NXOpen::VisualReporting::VisualReport  was opened from or will be saved to.  
          
                    Note that when NX is connected to Teamcenter, this property is the report dataset identifier from Teamcenter database. 
                    If it is a new report, it will be the report dataset name. When the report is save by  NXOpen::VisualReporting::VisualReport::Save , 
                    the report dataset identifier will be saved in this property.
                  
         
        """
        pass
    @Filename.setter
    def Filename(self, filename: str):
        """
        Setter for property: (str) Filename
         Returns the filename where this  NXOpen::VisualReporting::VisualReport  was opened from or will be saved to.  
          
                    Note that when NX is connected to Teamcenter, this property is the report dataset identifier from Teamcenter database. 
                    If it is a new report, it will be the report dataset name. When the report is save by  NXOpen::VisualReporting::VisualReport::Save , 
                    the report dataset identifier will be saved in this property.
                  
         
        """
        pass
    @property
    def IsUnmatchedGroupEnabled(self) -> bool:
        """
        Getter for property: (bool) IsUnmatchedGroupEnabled
         Returns whether use of  NXOpen::VisualReporting::VisualReport::UnmatchedGroupLabel 
                    is enabled.  
          
                  
         
        """
        pass
    @IsUnmatchedGroupEnabled.setter
    def IsUnmatchedGroupEnabled(self, isUnmatchedGroupEnabled: bool):
        """
        Setter for property: (bool) IsUnmatchedGroupEnabled
         Returns whether use of  NXOpen::VisualReporting::VisualReport::UnmatchedGroupLabel 
                    is enabled.  
          
                  
         
        """
        pass
    @property
    def ReportContext(self) -> VisualReport.ReportContextOption:
        """
        Getter for property: ( VisualReport.ReportContextOption NXOpen.Vis) ReportContext
         Returns the  NXOpen::VisualReporting::VisualReport::ReportContextOption  of this  NXOpen::VisualReporting::VisualReport .  
          
                  
         
        """
        pass
    @ReportContext.setter
    def ReportContext(self, reportContext: VisualReport.ReportContextOption):
        """
        Setter for property: ( VisualReport.ReportContextOption NXOpen.Vis) ReportContext
         Returns the  NXOpen::VisualReporting::VisualReport::ReportContextOption  of this  NXOpen::VisualReporting::VisualReport .  
          
                  
         
        """
        pass
    @property
    def ReportingObjectType(self) -> VisualReport.ReportingObjectTypeOption:
        """
        Getter for property: ( VisualReport.ReportingObjectTypeOption NXOpen.Vis) ReportingObjectType
         Returns the  NXOpen::VisualReporting::VisualReport::ReportingObjectTypeOption  of this  NXOpen::VisualReporting::VisualReport .  
          
                    Only valid if the  NXOpen::VisualReporting::VisualReport::ScopeType  of the  NXOpen::VisualReporting::VisualReport 
                    is  NXOpen::VisualReporting::VisualReport::ScopeTypeOptionComponent  type.
                  
         
        """
        pass
    @ReportingObjectType.setter
    def ReportingObjectType(self, reportingObjectType: VisualReport.ReportingObjectTypeOption):
        """
        Setter for property: ( VisualReport.ReportingObjectTypeOption NXOpen.Vis) ReportingObjectType
         Returns the  NXOpen::VisualReporting::VisualReport::ReportingObjectTypeOption  of this  NXOpen::VisualReporting::VisualReport .  
          
                    Only valid if the  NXOpen::VisualReporting::VisualReport::ScopeType  of the  NXOpen::VisualReporting::VisualReport 
                    is  NXOpen::VisualReporting::VisualReport::ScopeTypeOptionComponent  type.
                  
         
        """
        pass
    @property
    def ReportingStyle(self) -> VisualReport.ReportingStyleOption:
        """
        Getter for property: ( VisualReport.ReportingStyleOption NXOpen.Vis) ReportingStyle
         Returns the  NXOpen::VisualReporting::VisualReport::ReportingStyleOption  of this  NXOpen::VisualReporting::VisualReport .  
          
                  
         
        """
        pass
    @ReportingStyle.setter
    def ReportingStyle(self, reportingStyle: VisualReport.ReportingStyleOption):
        """
        Setter for property: ( VisualReport.ReportingStyleOption NXOpen.Vis) ReportingStyle
         Returns the  NXOpen::VisualReporting::VisualReport::ReportingStyleOption  of this  NXOpen::VisualReporting::VisualReport .  
          
                  
         
        """
        pass
    @property
    def SaveDestination(self) -> VisualReport.SaveDestinationOption:
        """
        Getter for property: ( VisualReport.SaveDestinationOption NXOpen.Vis) SaveDestination
         Returns the  NXOpen::VisualReporting::VisualReport::SaveDestinationOption  of the  NXOpen::VisualReporting::VisualReport .  
          
                    Note that this property will always be  NXOpen::VisualReporting::VisualReport::SaveDestinationOptionLocal  when NX is not connected to Teamcenter.
                  
         
        """
        pass
    @SaveDestination.setter
    def SaveDestination(self, destinationOption: VisualReport.SaveDestinationOption):
        """
        Setter for property: ( VisualReport.SaveDestinationOption NXOpen.Vis) SaveDestination
         Returns the  NXOpen::VisualReporting::VisualReport::SaveDestinationOption  of the  NXOpen::VisualReporting::VisualReport .  
          
                    Note that this property will always be  NXOpen::VisualReporting::VisualReport::SaveDestinationOptionLocal  when NX is not connected to Teamcenter.
                  
         
        """
        pass
    @property
    def ScopeType(self) -> VisualReport.ScopeTypeOption:
        """
        Getter for property: ( VisualReport.ScopeTypeOption NXOpen.Vis) ScopeType
         Returns the  NXOpen::VisualReporting::VisualReport::ScopeTypeOption  of this  NXOpen::VisualReporting::VisualReport .  
          
                  
         
        """
        pass
    @property
    def UnmatchedGroupLabel(self) -> GroupLabel:
        """
        Getter for property: ( GroupLabel NXOpen.Vis) UnmatchedGroupLabel
         Returns the  NXOpen::VisualReporting::GroupLabel  which is used for unmatched object.  
           
                    It will return NULL if the  NXOpen::VisualReporting::VisualReport  is not activated.
                  
         
        """
        pass
    @property
    def UnmatchedResultCategory(self) -> UnmatchedResultCategory:
        """
        Getter for property: ( UnmatchedResultCategory NXOpen.Vis) UnmatchedResultCategory
         Returns the  NXOpen::VisualReporting::UnmatchedResultCategory  from the activated  NXOpen::VisualReporting::VisualReport .  
          
                    It will return NULL if the  NXOpen::VisualReporting::VisualReport  is not activated.
                  
         
        """
        pass
    def GetAllDefinedProperties(self) -> List[Property]:
        """
         Returns the NXOpen.VisualReporting.Propertys which has been defined in this NXOpen.VisualReporting.VisualReport.
                    The returned properties include those properties defined in NXOpen.VisualReporting.Conditions, in NXOpen.VisualReporting.Classifiers,
                    and in the referenced properties.
                
         Returns definedProperties ( Property List[NXOpen.V):  Properties defined in this visual report .
        """
        pass
    def GetGroupLabels(self) -> List[GroupLabel]:
        """
         Returns the result NXOpen.VisualReporting.GroupLabels from the activated NXOpen.VisualReporting.VisualReport.
                    There are no NXOpen.VisualReporting.GroupLabels if the NXOpen.VisualReporting.VisualReport is not activated.
                    You can acess the user defined NXOpen.VisualReporting.GroupLabels by NXOpen.VisualReporting.VisualReportBuilder.GetManualGroupLabelsOfRule.
                
         Returns groupLabels ( GroupLabel List[NXOpen.V): .
        """
        pass
    def GetGroupLabelsOfResultCategory(self, category: ResultCategory) -> List[GroupLabel]:
        """
         Returns the result NXOpen.VisualReporting.GroupLabels of a NXOpen.VisualReporting.ResultCategory
                    from the activated NXOpen.VisualReporting.VisualReport.
                
         Returns groupLabels ( GroupLabel List[NXOpen.V): .
        """
        pass
    def GetKeywords(self) -> str:
        """
         Gets a comma separated string of the keywords for this NXOpen.VisualReporting.VisualReport.
                
         Returns keywords (str): .
        """
        pass
    def GetObjectTypes(self) -> List[VisualReport.ObjectTypeOption]:
        """
         Returns the NXOpen.VisualReporting.VisualReport.ObjectTypeOptions of this NXOpen.VisualReporting.VisualReport.
                    Only valid if the NXOpen.VisualReporting.VisualReport.ScopeType of the NXOpen.VisualReporting.VisualReport
                    is NXOpen.VisualReporting.VisualReport.ScopeTypeOption.SubPart type.
                
         Returns objectTypes ( VisualReport.ObjectTypeOption List[NXOpen.V):  The object types .
        """
        pass
    def GetObjectsInGroup(self, groupLabel: GroupLabel) -> List[NXOpen.NXObject]:
        """
         Returns the NXOpen.NXObjects that belong to the group
                    with this NXOpen.VisualReporting.GroupLabel.
                
         Returns nxObjects ( NXOpen.NXObject Li): .
        """
        pass
    def GetPropertyValueOfObject(self, property: Property, groupLabel: GroupLabel, nxObject: NXOpen.NXObject) -> str:
        """
         Returns the value of the NXOpen.VisualReporting.Propertys for the NXOpen.NXObject in the result NXOpen.VisualReporting.GroupLabel.
                    It will return  if the NXOpen.VisualReporting.VisualReport is not activated, or the NXOpen.VisualReporting.Property
                    does not belong to the properties defined in this NXOpen.VisualReporting.VisualReport, or the NXOpen.NXObject doesn't belong to
                    the specified result NXOpen.VisualReporting.GroupLabel.
                
         Returns value (str): .
        """
        pass
    def GetResultCategories(self) -> List[ResultCategory]:
        """
         Returns the NXOpen.VisualReporting.ResultCategorys from the activated NXOpen.VisualReporting.VisualReport.
                    There are no NXOpen.VisualReporting.ResultCategorys if the NXOpen.VisualReporting.VisualReport is not activated.
                
         Returns categories ( ResultCategory List[NXOpen.V): .
        """
        pass
    def GetRule(self, index: int) -> Rule:
        """
         Return the specified NXOpen.VisualReporting.Rule from this NXOpen.VisualReporting.VisualReport
                
         Returns rule ( Rule NXOpen.Vis): .
        """
        pass
    def GetRules(self) -> List[Rule]:
        """
         Returns all the NXOpen.VisualReporting.Rules in this NXOpen.VisualReporting.VisualReport
                
         Returns rules ( Rule List[NXOpen.V): .
        """
        pass
    def RemoveResultCategory(self, theCategory: ResultCategory) -> None:
        """
         Removes the NXOpen.VisualReporting.ResultCategory from NXOpen.VisualReporting.VisualReport.
                    The NXOpen.VisualReporting.Classifier which populates this NXOpen.VisualReporting.ResultCategory 
                    will also be removed from the NXOpen.VisualReporting.Rule in the NXOpen.VisualReporting.VisualReport.
                
        """
        pass
    def Save(self) -> None:
        """
         Saves this NXOpen.VisualReporting.VisualReport to its current NXOpen.VisualReporting.VisualReport.Filename.
                    Note that when NX is connected to Teamcenter, the NXOpen.VisualReporting.VisualReport.Filename will be 
                    updated to the report dataset identifier after the report is saved to Teamcenter database.
                
        """
        pass
    def SetKeywords(self, keywords: str) -> None:
        """
         Sets a comma separated string of the keywords for this NXOpen.VisualReporting.VisualReport.
                
        """
        pass
