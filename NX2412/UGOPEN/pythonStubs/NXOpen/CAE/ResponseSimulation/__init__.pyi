from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class BaseBuilder(NXOpen.Builder): 
    """ Represents the abstract builder class for all objects defined in response analysis meta solution """
    @property
    def ObjectLabel(self) -> ObjectLabel:
        """
        Getter for property: ( ObjectLabel NXOpen.CAE.Res) ObjectLabel
         Returns the object label   
            
         
        """
        pass
import NXOpen
class CombinationEvaluationOptions(NXOpen.TaggedObject): 
    """ Represents the setting for combination evaluation. """
    class EvaluationMethod(Enum):
        """
        Members Include: 
         |Abs|  
         |Srss|  
         |Nrl|  
         |Cqc|  
         |NqcDoubleSum|  

        """
        Abs: int
        Srss: int
        Nrl: int
        Cqc: int
        NqcDoubleSum: int
        @staticmethod
        def ValueOf(value: int) -> CombinationEvaluationOptions.EvaluationMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MultipleExcitationCombinationMethod(Enum):
        """
        Members Include: 
         |Abs|  
         |Srs|  

        """
        Abs: int
        Srs: int
        @staticmethod
        def ValueOf(value: int) -> CombinationEvaluationOptions.MultipleExcitationCombinationMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CombinationMethod(self) -> CombinationEvaluationOptions.MultipleExcitationCombinationMethod:
        """
        Getter for property: ( CombinationEvaluationOptions.MultipleExcitationCombinationMethod NXOpen.CAE.Res) CombinationMethod
         Returns the combination method for multiple excitation combination   
            
         
        """
        pass
    @CombinationMethod.setter
    def CombinationMethod(self, combination_method: CombinationEvaluationOptions.MultipleExcitationCombinationMethod):
        """
        Setter for property: ( CombinationEvaluationOptions.MultipleExcitationCombinationMethod NXOpen.CAE.Res) CombinationMethod
         Returns the combination method for multiple excitation combination   
            
         
        """
        pass
    @property
    def EvaluationMethodOption(self) -> CombinationEvaluationOptions.EvaluationMethod:
        """
        Getter for property: ( CombinationEvaluationOptions.EvaluationMethod NXOpen.CAE.Res) EvaluationMethodOption
         Returns the calculation method   
            
         
        """
        pass
    @EvaluationMethodOption.setter
    def EvaluationMethodOption(self, method: CombinationEvaluationOptions.EvaluationMethod):
        """
        Setter for property: ( CombinationEvaluationOptions.EvaluationMethod NXOpen.CAE.Res) EvaluationMethodOption
         Returns the calculation method   
            
         
        """
        pass
    @property
    def NeighboringFactor(self) -> float:
        """
        Getter for property: (float) NeighboringFactor
         Returns the neighboring factor.  
           Must be specified when calculation method is 
                  CAE::ResponseSimulation::CombinationEvaluationOptions::EvaluationMethodNrl    
         
        """
        pass
    @NeighboringFactor.setter
    def NeighboringFactor(self, neighboring_factor: float):
        """
        Setter for property: (float) NeighboringFactor
         Returns the neighboring factor.  
           Must be specified when calculation method is 
                  CAE::ResponseSimulation::CombinationEvaluationOptions::EvaluationMethodNrl    
         
        """
        pass
    @property
    def TimeDuration(self) -> float:
        """
        Getter for property: (float) TimeDuration
         Returns the time duration in second.  
           Must be specified when calculation method is 
                 CAE::ResponseSimulation::CombinationEvaluationOptions::EvaluationMethodNqcDoubleSum    
         
        """
        pass
    @TimeDuration.setter
    def TimeDuration(self, time_duration: float):
        """
        Setter for property: (float) TimeDuration
         Returns the time duration in second.  
           Must be specified when calculation method is 
                 CAE::ResponseSimulation::CombinationEvaluationOptions::EvaluationMethodNqcDoubleSum    
         
        """
        pass
class CoordinateSystem(Enum):
    """
    Members Include: 
     |Nodal|  
     |Global|  
     |Elemental|  
     |Material|  

    """
    Nodal: int
    Global: int
    Elemental: int
    Material: int
    @staticmethod
    def ValueOf(value: int) -> CoordinateSystem:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.CAE
class CsdEvaluationSettingBuilder(FunctionEvaluationSettingBuilder): 
    """ Represents the CSD build """
    @property
    def ReferenceCoordinateSystem(self) -> CoordinateSystem:
        """
        Getter for property: ( CoordinateSystem NXOpen.CAE.Res) ReferenceCoordinateSystem
         Returns the coordinate system of reference element.  
           
                 Available if the result type is 
                  CAE::ResponseSimulation::EvaluationResultTypeStress  
                  CAE::ResponseSimulation::EvaluationResultTypeStrain  
                  CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant  
                  CAE::ResponseSimulation::EvaluationResultTypeElementForce  
                  CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce  
                  
         
        """
        pass
    @ReferenceCoordinateSystem.setter
    def ReferenceCoordinateSystem(self, reference_coordinate_system: CoordinateSystem):
        """
        Setter for property: ( CoordinateSystem NXOpen.CAE.Res) ReferenceCoordinateSystem
         Returns the coordinate system of reference element.  
           
                 Available if the result type is 
                  CAE::ResponseSimulation::EvaluationResultTypeStress  
                  CAE::ResponseSimulation::EvaluationResultTypeStrain  
                  CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant  
                  CAE::ResponseSimulation::EvaluationResultTypeElementForce  
                  CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce  
                  
         
        """
        pass
    @property
    def ReferenceDataLocation(self) -> DataLocation:
        """
        Getter for property: ( DataLocation NXOpen.CAE.Res) ReferenceDataLocation
         Returns the reference element location of reference element.  
           
                 Available if the result type is 
                  CAE::ResponseSimulation::EvaluationResultTypeStress  
                  CAE::ResponseSimulation::EvaluationResultTypeStrain  
                  
         
        """
        pass
    @property
    def ReferenceElement(self) -> NXOpen.CAE.FEElement:
        """
        Getter for property: ( NXOpen.CAE.FEElement) ReferenceElement
         Returns the reference element.  
           
                 Available if the result type is 
                  CAE::ResponseSimulation::EvaluationResultTypeStress  
                  CAE::ResponseSimulation::EvaluationResultTypeStrain  
                  CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant  
                  CAE::ResponseSimulation::EvaluationResultTypeElementForce  
                  CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce  
                  
         
        """
        pass
    @ReferenceElement.setter
    def ReferenceElement(self, reference_element: NXOpen.CAE.FEElement):
        """
        Setter for property: ( NXOpen.CAE.FEElement) ReferenceElement
         Returns the reference element.  
           
                 Available if the result type is 
                  CAE::ResponseSimulation::EvaluationResultTypeStress  
                  CAE::ResponseSimulation::EvaluationResultTypeStrain  
                  CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant  
                  CAE::ResponseSimulation::EvaluationResultTypeElementForce  
                  CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce  
                  
         
        """
        pass
    @property
    def ReferenceElementDataComponent(self) -> DirectionDataComponent:
        """
        Getter for property: ( DirectionDataComponent NXOpen.CAE.Res) ReferenceElementDataComponent
         Returns the direction data component of reference element.  
           
                 Available if the result type is 
                  CAE::ResponseSimulation::EvaluationResultTypeStress  
                  CAE::ResponseSimulation::EvaluationResultTypeStrain  
                  CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant  
                  CAE::ResponseSimulation::EvaluationResultTypeElementForce  
                  CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce  
                  
         
        """
        pass
    @ReferenceElementDataComponent.setter
    def ReferenceElementDataComponent(self, reference_element_data_component: DirectionDataComponent):
        """
        Setter for property: ( DirectionDataComponent NXOpen.CAE.Res) ReferenceElementDataComponent
         Returns the direction data component of reference element.  
           
                 Available if the result type is 
                  CAE::ResponseSimulation::EvaluationResultTypeStress  
                  CAE::ResponseSimulation::EvaluationResultTypeStrain  
                  CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant  
                  CAE::ResponseSimulation::EvaluationResultTypeElementForce  
                  CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce  
                  
         
        """
        pass
    @property
    def ReferenceNode(self) -> NXOpen.CAE.FENode:
        """
        Getter for property: ( NXOpen.CAE.FENode) ReferenceNode
         Returns the reference node.  
           
                 Available if the result type is 
                  CAE::ResponseSimulation::EvaluationResultTypeDisplacement  
                  CAE::ResponseSimulation::EvaluationResultTypeVelocity  
                  CAE::ResponseSimulation::EvaluationResultTypeAcceleration  
                  CAE::ResponseSimulation::EvaluationResultTypeReactionForce  
                  
         
        """
        pass
    @ReferenceNode.setter
    def ReferenceNode(self, reference_node: NXOpen.CAE.FENode):
        """
        Setter for property: ( NXOpen.CAE.FENode) ReferenceNode
         Returns the reference node.  
           
                 Available if the result type is 
                  CAE::ResponseSimulation::EvaluationResultTypeDisplacement  
                  CAE::ResponseSimulation::EvaluationResultTypeVelocity  
                  CAE::ResponseSimulation::EvaluationResultTypeAcceleration  
                  CAE::ResponseSimulation::EvaluationResultTypeReactionForce  
                  
         
        """
        pass
    @property
    def ReferenceNodeDataComponent(self) -> DirectionDataComponent:
        """
        Getter for property: ( DirectionDataComponent NXOpen.CAE.Res) ReferenceNodeDataComponent
         Returns the direction data component of reference node.  
           
                 Available if the result type is 
                  CAE::ResponseSimulation::EvaluationResultTypeDisplacement  
                  CAE::ResponseSimulation::EvaluationResultTypeVelocity  
                  CAE::ResponseSimulation::EvaluationResultTypeAcceleration  
                  CAE::ResponseSimulation::EvaluationResultTypeReactionForce  
                  
         
        """
        pass
    @ReferenceNodeDataComponent.setter
    def ReferenceNodeDataComponent(self, reference_node_data_component: DirectionDataComponent):
        """
        Setter for property: ( DirectionDataComponent NXOpen.CAE.Res) ReferenceNodeDataComponent
         Returns the direction data component of reference node.  
           
                 Available if the result type is 
                  CAE::ResponseSimulation::EvaluationResultTypeDisplacement  
                  CAE::ResponseSimulation::EvaluationResultTypeVelocity  
                  CAE::ResponseSimulation::EvaluationResultTypeAcceleration  
                  CAE::ResponseSimulation::EvaluationResultTypeReactionForce  
                  
         
        """
        pass
    @property
    def ReferenceUserDefinedDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ReferenceUserDefinedDirection
         Returns  the user defined direction of reference node.  
                    
                 Available if the result type is 
                  CAE::ResponseSimulation::EvaluationResultTypeDisplacement  
                  CAE::ResponseSimulation::EvaluationResultTypeVelocity  
                  CAE::ResponseSimulation::EvaluationResultTypeAcceleration  
                  CAE::ResponseSimulation::EvaluationResultTypeReactionForce  
                  
         
        """
        pass
    @ReferenceUserDefinedDirection.setter
    def ReferenceUserDefinedDirection(self, reference_user_defined_direction: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ReferenceUserDefinedDirection
         Returns  the user defined direction of reference node.  
                    
                 Available if the result type is 
                  CAE::ResponseSimulation::EvaluationResultTypeDisplacement  
                  CAE::ResponseSimulation::EvaluationResultTypeVelocity  
                  CAE::ResponseSimulation::EvaluationResultTypeAcceleration  
                  CAE::ResponseSimulation::EvaluationResultTypeReactionForce  
                  
         
        """
        pass
    @property
    def ReferenceUsingUserDefinedDirection(self) -> NodalFunctionEvalRequest:
        """
        Getter for property: ( NodalFunctionEvalRequest NXOpen.CAE.Res) ReferenceUsingUserDefinedDirection
         Returns the option of using user defined direction of the reference node.  
           
                 Available if the result type is 
                  CAE::ResponseSimulation::EvaluationResultTypeDisplacement  
                  CAE::ResponseSimulation::EvaluationResultTypeVelocity  
                  CAE::ResponseSimulation::EvaluationResultTypeAcceleration  
                  CAE::ResponseSimulation::EvaluationResultTypeReactionForce  
                  
         
        """
        pass
    @ReferenceUsingUserDefinedDirection.setter
    def ReferenceUsingUserDefinedDirection(self, reference_using_user_defined_direction: NodalFunctionEvalRequest):
        """
        Setter for property: ( NodalFunctionEvalRequest NXOpen.CAE.Res) ReferenceUsingUserDefinedDirection
         Returns the option of using user defined direction of the reference node.  
           
                 Available if the result type is 
                  CAE::ResponseSimulation::EvaluationResultTypeDisplacement  
                  CAE::ResponseSimulation::EvaluationResultTypeVelocity  
                  CAE::ResponseSimulation::EvaluationResultTypeAcceleration  
                  CAE::ResponseSimulation::EvaluationResultTypeReactionForce  
                  
         
        """
        pass
    @property
    def ResponseCoordinateSystem(self) -> CoordinateSystem:
        """
        Getter for property: ( CoordinateSystem NXOpen.CAE.Res) ResponseCoordinateSystem
         Returns the coordinate system of response elements.  
           
                 Available if the result type is 
                  CAE::ResponseSimulation::EvaluationResultTypeStress  
                  CAE::ResponseSimulation::EvaluationResultTypeStrain  
                  CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant  
                  CAE::ResponseSimulation::EvaluationResultTypeElementForce  
                  CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce  
                  
         
        """
        pass
    @ResponseCoordinateSystem.setter
    def ResponseCoordinateSystem(self, response_coordinate_system: CoordinateSystem):
        """
        Setter for property: ( CoordinateSystem NXOpen.CAE.Res) ResponseCoordinateSystem
         Returns the coordinate system of response elements.  
           
                 Available if the result type is 
                  CAE::ResponseSimulation::EvaluationResultTypeStress  
                  CAE::ResponseSimulation::EvaluationResultTypeStrain  
                  CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant  
                  CAE::ResponseSimulation::EvaluationResultTypeElementForce  
                  CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce  
                  
         
        """
        pass
    @property
    def ResponseDataLocation(self) -> DataLocation:
        """
        Getter for property: ( DataLocation NXOpen.CAE.Res) ResponseDataLocation
         Returns the response element location.  
           
                 Available if the result type is 
                  CAE::ResponseSimulation::EvaluationResultTypeStress  
                  CAE::ResponseSimulation::EvaluationResultTypeStrain  
                  
         
        """
        pass
    @property
    def ResponseElementDataComponent(self) -> DirectionDataComponent:
        """
        Getter for property: ( DirectionDataComponent NXOpen.CAE.Res) ResponseElementDataComponent
         Returns the direction data component of response elements.  
           
                 Available if the result type is 
                  CAE::ResponseSimulation::EvaluationResultTypeStress  
                  CAE::ResponseSimulation::EvaluationResultTypeStrain  
                  CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant  
                  CAE::ResponseSimulation::EvaluationResultTypeElementForce  
                  CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce  
                  
         
        """
        pass
    @ResponseElementDataComponent.setter
    def ResponseElementDataComponent(self, response_element_data_component: DirectionDataComponent):
        """
        Setter for property: ( DirectionDataComponent NXOpen.CAE.Res) ResponseElementDataComponent
         Returns the direction data component of response elements.  
           
                 Available if the result type is 
                  CAE::ResponseSimulation::EvaluationResultTypeStress  
                  CAE::ResponseSimulation::EvaluationResultTypeStrain  
                  CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant  
                  CAE::ResponseSimulation::EvaluationResultTypeElementForce  
                  CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce  
                  
         
        """
        pass
    @property
    def ResponseNodeDataComponent(self) -> DirectionDataComponent:
        """
        Getter for property: ( DirectionDataComponent NXOpen.CAE.Res) ResponseNodeDataComponent
         Returns the direction data component of response node.  
           
                 Available if the result type is 
                  CAE::ResponseSimulation::EvaluationResultTypeDisplacement  
                  CAE::ResponseSimulation::EvaluationResultTypeVelocity  
                  CAE::ResponseSimulation::EvaluationResultTypeAcceleration  
                  CAE::ResponseSimulation::EvaluationResultTypeReactionForce  
                  
         
        """
        pass
    @ResponseNodeDataComponent.setter
    def ResponseNodeDataComponent(self, response_node_data_component: DirectionDataComponent):
        """
        Setter for property: ( DirectionDataComponent NXOpen.CAE.Res) ResponseNodeDataComponent
         Returns the direction data component of response node.  
           
                 Available if the result type is 
                  CAE::ResponseSimulation::EvaluationResultTypeDisplacement  
                  CAE::ResponseSimulation::EvaluationResultTypeVelocity  
                  CAE::ResponseSimulation::EvaluationResultTypeAcceleration  
                  CAE::ResponseSimulation::EvaluationResultTypeReactionForce  
                  
         
        """
        pass
    @property
    def ResponseUserDefinedDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ResponseUserDefinedDirection
         Returns  the user defined direction of response nodes.  
           
                 Available if the result type is 
                  CAE::ResponseSimulation::EvaluationResultTypeDisplacement  
                  CAE::ResponseSimulation::EvaluationResultTypeVelocity  
                  CAE::ResponseSimulation::EvaluationResultTypeAcceleration  
                  CAE::ResponseSimulation::EvaluationResultTypeReactionForce  
                  
         
        """
        pass
    @ResponseUserDefinedDirection.setter
    def ResponseUserDefinedDirection(self, response_user_defined_direction: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ResponseUserDefinedDirection
         Returns  the user defined direction of response nodes.  
           
                 Available if the result type is 
                  CAE::ResponseSimulation::EvaluationResultTypeDisplacement  
                  CAE::ResponseSimulation::EvaluationResultTypeVelocity  
                  CAE::ResponseSimulation::EvaluationResultTypeAcceleration  
                  CAE::ResponseSimulation::EvaluationResultTypeReactionForce  
                  
         
        """
        pass
    @property
    def ResponseUsingUserDefinedDirection(self) -> NodalFunctionEvalRequest:
        """
        Getter for property: ( NodalFunctionEvalRequest NXOpen.CAE.Res) ResponseUsingUserDefinedDirection
         Returns the option of using user defined direction of response nodes.  
           
                 Available if the result type is 
                  CAE::ResponseSimulation::EvaluationResultTypeDisplacement  
                  CAE::ResponseSimulation::EvaluationResultTypeVelocity  
                  CAE::ResponseSimulation::EvaluationResultTypeAcceleration  
                  CAE::ResponseSimulation::EvaluationResultTypeReactionForce  
                  
         
        """
        pass
    @ResponseUsingUserDefinedDirection.setter
    def ResponseUsingUserDefinedDirection(self, response_using_user_defined_direction: NodalFunctionEvalRequest):
        """
        Setter for property: ( NodalFunctionEvalRequest NXOpen.CAE.Res) ResponseUsingUserDefinedDirection
         Returns the option of using user defined direction of response nodes.  
           
                 Available if the result type is 
                  CAE::ResponseSimulation::EvaluationResultTypeDisplacement  
                  CAE::ResponseSimulation::EvaluationResultTypeVelocity  
                  CAE::ResponseSimulation::EvaluationResultTypeAcceleration  
                  CAE::ResponseSimulation::EvaluationResultTypeReactionForce  
                  
         
        """
        pass
    def GetResponseElements(self) -> List[NXOpen.CAE.FEElement]:
        """
         Get the response elments. 
                 Available if the result type is 
                 CAE.ResponseSimulation.EvaluationResultType.Stress 
                 CAE.ResponseSimulation.EvaluationResultType.Strain 
                 CAE.ResponseSimulation.EvaluationResultType.ShellStressResultant 
                 CAE.ResponseSimulation.EvaluationResultType.ElementForce 
                 CAE.ResponseSimulation.EvaluationResultType.BeamElementForce 
                
         Returns response_elements ( NXOpen.CAE.FEElement Li):  .
        """
        pass
    def GetResponseNodes(self) -> List[NXOpen.CAE.FENode]:
        """
         Get the response nodes. 
                 Available if the result type is 
                 CAE.ResponseSimulation.EvaluationResultType.Displacement 
                 CAE.ResponseSimulation.EvaluationResultType.Velocity 
                 CAE.ResponseSimulation.EvaluationResultType.Acceleration 
                 CAE.ResponseSimulation.EvaluationResultType.ReactionForce 
                
         Returns response_node ( NXOpen.CAE.FENode Li):  .
        """
        pass
    def SetResponseElements(self, response_elements: List[NXOpen.CAE.FEElement]) -> None:
        """
         Set the response elments. 
                 Available if the result type is 
                 CAE.ResponseSimulation.EvaluationResultType.Stress 
                 CAE.ResponseSimulation.EvaluationResultType.Strain 
                 CAE.ResponseSimulation.EvaluationResultType.ShellStressResultant 
                 CAE.ResponseSimulation.EvaluationResultType.ElementForce 
                 CAE.ResponseSimulation.EvaluationResultType.BeamElementForce 
                
        """
        pass
    def SetResponseNodes(self, response_node: List[NXOpen.CAE.FENode]) -> None:
        """
         Set the response nodes. 
                 Available if the result type is 
                 CAE.ResponseSimulation.EvaluationResultType.Displacement 
                 CAE.ResponseSimulation.EvaluationResultType.Velocity 
                 CAE.ResponseSimulation.EvaluationResultType.Acceleration 
                 CAE.ResponseSimulation.EvaluationResultType.ReactionForce 
                
        """
        pass
class CsdEvaluationSetting(FunctionEvaluationSetting): 
    """ Represents the class of evaluation setting for CSD """
    pass
class CSDExcitationBuilder(ExcitationBuilder): 
    """ Represents the manager to NXOpen.CAE.ResponseSimulation.CSDExcitation.
     The object of type NXOpen.CAE.ResponseSimulation.CSDExcitation
      can only be created or edited through this class.
     """
    @property
    def CorrelationType(self) -> CSDExcitation.CorrelationType:
        """
        Getter for property: ( CSDExcitation.CorrelationType NXOpen.CAE.Res) CorrelationType
         Returns the correlation type   
            
         
        """
        pass
    @CorrelationType.setter
    def CorrelationType(self, type: CSDExcitation.CorrelationType):
        """
        Setter for property: ( CSDExcitation.CorrelationType NXOpen.CAE.Res) CorrelationType
         Returns the correlation type   
            
         
        """
        pass
    @property
    def CorrelationValue(self) -> float:
        """
        Getter for property: (float) CorrelationValue
         Returns the correlation type   
            
         
        """
        pass
    @CorrelationValue.setter
    def CorrelationValue(self, correlationValue: float):
        """
        Setter for property: (float) CorrelationValue
         Returns the correlation type   
            
         
        """
        pass
    def GetFromFunction(self) -> Tuple[Excitation, Excitation.Component]:
        """
         Returns the from function 
         Returns A tuple consisting of (fromExcitation, componentType). 
         - fromExcitation is:  Excitation NXOpen.CAE.Res. .
         - componentType is:  Excitation.Component NXOpen.CAE.Res. .

        """
        pass
    def GetToFunction(self) -> Tuple[Excitation, Excitation.Component]:
        """
         Returns the to function 
         Returns A tuple consisting of (toExcitation, componentType). 
         - toExcitation is:  Excitation NXOpen.CAE.Res. .
         - componentType is:  Excitation.Component NXOpen.CAE.Res. .

        """
        pass
    def SetFromFunction(self, fromExcitation: Excitation, componentType: Excitation.Component) -> None:
        """
         Sets the from function 
        """
        pass
    def SetToFunction(self, toExcitation: Excitation, componentType: Excitation.Component) -> None:
        """
         Sets the to function 
        """
        pass
class CSDExcitation(Excitation): 
    """ Represents an CSD excitation. CSD excitation could only be used by CSD event. """
    class CorrelationType(Enum):
        """
        Members Include: 
         |PhaseAngle|  
         |TimeDelay|  

        """
        PhaseAngle: int
        TimeDelay: int
        @staticmethod
        def ValueOf(value: int) -> CSDExcitation.CorrelationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
import NXOpen
class DataLocation(NXOpen.TaggedObject): 
    """ Represents the data location to perform evaluation """
    class Beam(Enum):
        """
        Members Include: 
         |C|   
         |D|   
         |E|   
         |F|   

        """
        C: int
        D: int
        E: int
        F: int
        @staticmethod
        def ValueOf(value: int) -> DataLocation.Beam:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Element(Enum):
        """
        Members Include: 
         |Both|   
         |Centroid|   
         |Corners|   

        """
        Both: int
        Centroid: int
        Corners: int
        @staticmethod
        def ValueOf(value: int) -> DataLocation.Element:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Shell(Enum):
        """
        Members Include: 
         |Top|   
         |Bottom|   
         |Middle|   

        """
        Top: int
        Bottom: int
        Middle: int
        @staticmethod
        def ValueOf(value: int) -> DataLocation.Shell:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BeamLocation(self) -> DataLocation.Beam:
        """
        Getter for property: ( DataLocation.Beam NXOpen.CAE.Res) BeamLocation
         Returns the method to define frequency  
            
         
        """
        pass
    @BeamLocation.setter
    def BeamLocation(self, beam_location: DataLocation.Beam):
        """
        Setter for property: ( DataLocation.Beam NXOpen.CAE.Res) BeamLocation
         Returns the method to define frequency  
            
         
        """
        pass
    @property
    def ElementLocation(self) -> DataLocation.Element:
        """
        Getter for property: ( DataLocation.Element NXOpen.CAE.Res) ElementLocation
         Returns the element location.  
           Only available when stress and strain is defined
                by  CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange    
         
        """
        pass
    @ElementLocation.setter
    def ElementLocation(self, element_location: DataLocation.Element):
        """
        Setter for property: ( DataLocation.Element NXOpen.CAE.Res) ElementLocation
         Returns the element location.  
           Only available when stress and strain is defined
                by  CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange    
         
        """
        pass
    @property
    def LayerSelection(self) -> int:
        """
        Getter for property: (int) LayerSelection
         Returns the end value of frequency range.  
           Only available when the frequency is defined 
                by  CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange    
         
        """
        pass
    @LayerSelection.setter
    def LayerSelection(self, layer_number: int):
        """
        Setter for property: (int) LayerSelection
         Returns the end value of frequency range.  
           Only available when the frequency is defined 
                by  CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange    
         
        """
        pass
    @property
    def ShellLocation(self) -> DataLocation.Shell:
        """
        Getter for property: ( DataLocation.Shell NXOpen.CAE.Res) ShellLocation
         Returns the start value of frequency range.  
           Only available when the frequency is defined
                by  CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange    
         
        """
        pass
    @ShellLocation.setter
    def ShellLocation(self, shell_location: DataLocation.Shell):
        """
        Setter for property: ( DataLocation.Shell NXOpen.CAE.Res) ShellLocation
         Returns the start value of frequency range.  
           Only available when the frequency is defined
                by  CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange    
         
        """
        pass
import NXOpen
class DDAMComponentData(NXOpen.TaggedObject): 
    """ Represents an excitation on one specified direction. """
    class LoadingType(Enum):
        """
        Members Include: 
         |Vertical|   
         |Athwartship|   
         |ForeAndAft|   

        """
        Vertical: int
        Athwartship: int
        ForeAndAft: int
        @staticmethod
        def ValueOf(value: int) -> DDAMComponentData.LoadingType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ResponseType(Enum):
        """
        Members Include: 
         |Elastic|   
         |ElasticPlastic|   

        """
        Elastic: int
        ElasticPlastic: int
        @staticmethod
        def ValueOf(value: int) -> DDAMComponentData.ResponseType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def LoadingTypeOption(self) -> DDAMComponentData.LoadingType:
        """
        Getter for property: ( DDAMComponentData.LoadingType NXOpen.CAE.Res) LoadingTypeOption
         Returns the option of loading type   
            
         
        """
        pass
    @LoadingTypeOption.setter
    def LoadingTypeOption(self, loading_type: DDAMComponentData.LoadingType):
        """
        Setter for property: ( DDAMComponentData.LoadingType NXOpen.CAE.Res) LoadingTypeOption
         Returns the option of loading type   
            
         
        """
        pass
    @property
    def ResponseTypeOption(self) -> DDAMComponentData.ResponseType:
        """
        Getter for property: ( DDAMComponentData.ResponseType NXOpen.CAE.Res) ResponseTypeOption
         Returns the option of response type   
            
         
        """
        pass
    @ResponseTypeOption.setter
    def ResponseTypeOption(self, response_type: DDAMComponentData.ResponseType):
        """
        Setter for property: ( DDAMComponentData.ResponseType NXOpen.CAE.Res) ResponseTypeOption
         Returns the option of response type   
            
         
        """
        pass
    def GetComponentType(self) -> Excitation.Component:
        """
         Returns the component type 
         Returns componentType ( Excitation.Component NXOpen.CAE.Res):  .
        """
        pass
    def GetEnable(self) -> bool:
        """
         Returns the enable option 
         Returns enable (bool):  .
        """
        pass
class DDAMExcitationBuilder(ExcitationBuilder): 
    """ Represents the manager to NXOpen.CAE.ResponseSimulation.DDAMExcitation.
     The object of type NXOpen.CAE.ResponseSimulation.DDAMExcitation can only
    be created or edited through this class. """
    @property
    def LoadingType(self) -> DDAMExcitation.LoadingType:
        """
        Getter for property: ( DDAMExcitation.LoadingType NXOpen.CAE.Res) LoadingType
         Returns the loading type  
            
         
        """
        pass
    @LoadingType.setter
    def LoadingType(self, loading_type: DDAMExcitation.LoadingType):
        """
        Setter for property: ( DDAMExcitation.LoadingType NXOpen.CAE.Res) LoadingType
         Returns the loading type  
            
         
        """
        pass
    @property
    def ResponseType(self) -> DDAMExcitation.ResponseType:
        """
        Getter for property: ( DDAMExcitation.ResponseType NXOpen.CAE.Res) ResponseType
         Returns the response type  
            
         
        """
        pass
    @ResponseType.setter
    def ResponseType(self, response_type: DDAMExcitation.ResponseType):
        """
        Setter for property: ( DDAMExcitation.ResponseType NXOpen.CAE.Res) ResponseType
         Returns the response type  
            
         
        """
        pass
    def GetComponentStatus(self, component: Excitation.Component) -> bool:
        """
         Returns the status of a dierction component 
         Returns enable (bool):  .
        """
        pass
    def SetComponentStatus(self, component: Excitation.Component, enable: bool) -> None:
        """
         Sets the status for a direction component
        """
        pass
class DDAMExcitation(Excitation): 
    """ Represents an DDAM excitation. DDAM excitation could only be used by DDAM event. """
    class CoefficientDefinitionType(Enum):
        """
        Members Include: 
         |ByFile|  Get the DDAM coefficients from a DDAM coefficient file 
         |InputManually|  Input the DDAM coefficient manually 

        """
        ByFile: int
        InputManually: int
        @staticmethod
        def ValueOf(value: int) -> DDAMExcitation.CoefficientDefinitionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LoadingType(Enum):
        """
        Members Include: 
         |Vertical|   
         |Athwartship|   
         |ForeAndAft|   

        """
        Vertical: int
        Athwartship: int
        ForeAndAft: int
        @staticmethod
        def ValueOf(value: int) -> DDAMExcitation.LoadingType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MountingType(Enum):
        """
        Members Include: 
         |Hull|   
         |Duck|   
         |ShellPlating|   

        """
        Hull: int
        Duck: int
        ShellPlating: int
        @staticmethod
        def ValueOf(value: int) -> DDAMExcitation.MountingType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ResponseType(Enum):
        """
        Members Include: 
         |Elastic|   
         |ElasticPlastic|   

        """
        Elastic: int
        ElasticPlastic: int
        @staticmethod
        def ValueOf(value: int) -> DDAMExcitation.ResponseType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ShipType(Enum):
        """
        Members Include: 
         |Surface|   
         |Submarine|   

        """
        Surface: int
        Submarine: int
        @staticmethod
        def ValueOf(value: int) -> DDAMExcitation.ShipType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
class DirectionDataComponent(Enum):
    """
    Members Include: 
     |X|  
     |Y|  
     |Z|  
     |Rx|  
     |Ry|  
     |Rz|  
     |Xx|  
     |Yy|  
     |Zz|  
     |Xy|  
     |Xz|  
     |Yz|  
     |Ax|  
     |Sy|  
     |Sz|  
     |Tx|  
     |Byy|  
     |Bz|  
     |Fxx|  
     |Fyy|  
     |Fzz|  
     |Fxy|  
     |Mx|  
     |My|  
     |Mz|  
     |Mxy|  
     |Mxz|  
     |Myz|  
     |Vx|  
     |Vy|  
     |TranslationalMagnitude|  
     |Vonmises|  
     |MaxPrincipal|  
     |MinPrincipal|  
     |MaxShear|  
     |AllNormals|  
     |AllTranslational|  
     |AllForces|  
     |AllDirections|  
     |AllDataComponents|  
     |All|  
     |AllXyPlane|  
     |Leg1|  
     |Leg2|  
     |Leg3|  
     |AllLegs|  

    """
    X: int
    Y: int
    Z: int
    Rx: int
    Ry: int
    Rz: int
    Xx: int
    Yy: int
    Zz: int
    Xy: int
    Xz: int
    Yz: int
    Ax: int
    Sy: int
    Sz: int
    Tx: int
    Byy: int
    Bz: int
    Fxx: int
    Fyy: int
    Fzz: int
    Fxy: int
    Mx: int
    My: int
    Mz: int
    Mxy: int
    Mxz: int
    Myz: int
    Vx: int
    Vy: int
    TranslationalMagnitude: int
    Vonmises: int
    MaxPrincipal: int
    MinPrincipal: int
    MaxShear: int
    AllNormals: int
    AllTranslational: int
    AllForces: int
    AllDirections: int
    AllDataComponents: int
    All: int
    AllXyPlane: int
    Leg1: int
    Leg2: int
    Leg3: int
    AllLegs: int
    @staticmethod
    def ValueOf(value: int) -> DirectionDataComponent:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class DistributedLoadExcitationBuilder(ExcitationBuilder): 
    """ Represents the manager to NXOpen.CAE.ResponseSimulation.DistributedLoadExcitation.
     The object of type NXOpen.CAE.ResponseSimulation.DistributedLoadExcitation
      can only be created or edited through this class.
     """
    @property
    def ExcitationFunction(self) -> FunctionComponentData:
        """
        Getter for property: ( FunctionComponentData NXOpen.CAE.Res) ExcitationFunction
         Returns the magnitude function   
            
         
        """
        pass
class DistributedLoadExcitation(Excitation): 
    """ Represents an excitation of distributed-load type """
    pass
import NXOpen
class DynamicEvaluationOutputSettings(NXOpen.TaggedObject): 
    """ Represents the output setting for dynamic response evaluation"""
    @property
    def PreviewOption(self) -> bool:
        """
        Getter for property: (bool) PreviewOption
         Returns the preview option.  
           If true, the evaluation results will be previewed by plot and not saved to disk until
                 you confirm to save them   
         
        """
        pass
    @PreviewOption.setter
    def PreviewOption(self, preview_option: bool):
        """
        Setter for property: (bool) PreviewOption
         Returns the preview option.  
           If true, the evaluation results will be previewed by plot and not saved to disk until
                 you confirm to save them   
         
        """
        pass
    @property
    def RecordPrefix(self) -> str:
        """
        Getter for property: (str) RecordPrefix
         Returns the prefix of evaluation results record name   
            
         
        """
        pass
    @RecordPrefix.setter
    def RecordPrefix(self, record_prefix: str):
        """
        Setter for property: (str) RecordPrefix
         Returns the prefix of evaluation results record name   
            
         
        """
        pass
import NXOpen
class DynamicResultEvaluationSettingBuilder(NXOpen.Builder): 
    """ Represents the abstract builder class of evaluation setting for all dynamic results evaluations.
    """
    def GetDescriptionString(self) -> List[str]:
        """
         Returns the description. 
         Returns description (List[str]): .
        """
        pass
    def GetResponseResultNameString(self) -> str:
        """
         Returns the response result name. 
         Returns responseResultName (str): .
        """
        pass
    def SetDescriptionString(self, description: List[str]) -> None:
        """
         Sets the description 
        """
        pass
    def SetResponseResultNameString(self, responseResultName: str) -> None:
        """
         Sets the response result name 
        """
        pass
class DynamicResultEvaluationSetting(EvaluationSetting): 
    """ Represents the abstract class of evaluation setting for all dynamic results evaluations.
    """
    pass
class ElementalFunctionEvalBeamLocation(Enum):
    """
    Members Include: 
     |C|  
     |D|  
     |E|  
     |F|  

    """
    C: int
    D: int
    E: int
    F: int
    @staticmethod
    def ValueOf(value: int) -> ElementalFunctionEvalBeamLocation:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen.CAE
class ElementalFunctionEvaluationSettingBuilder(FunctionEvaluationSettingBuilder): 
    """ This is a manager to the NXOpen.CAE.ResponseSimulation.ElementalFunctionEvaluationSetting class. 
    Object of type NXOpen.CAE.ResponseSimulation.ElementalFunctionEvaluationSetting can be 
    created and edited only through this class
     """
    @property
    def BeamDataLocation(self) -> ElementalFunctionEvalBeamLocation:
        """
        Getter for property: ( ElementalFunctionEvalBeamLocation NXOpen.CAE.Res) BeamDataLocation
         Returns the data location of beam element.  
           For more information about beam data location,
                see the Response Simulatin section of the Gateway help   
         
        """
        pass
    @BeamDataLocation.setter
    def BeamDataLocation(self, beam_location: ElementalFunctionEvalBeamLocation):
        """
        Setter for property: ( ElementalFunctionEvalBeamLocation NXOpen.CAE.Res) BeamDataLocation
         Returns the data location of beam element.  
           For more information about beam data location,
                see the Response Simulatin section of the Gateway help   
         
        """
        pass
    @property
    def CoordinateSystem(self) -> CoordinateSystem:
        """
        Getter for property: ( CoordinateSystem NXOpen.CAE.Res) CoordinateSystem
         Returns the coordinate system   
            
         
        """
        pass
    @CoordinateSystem.setter
    def CoordinateSystem(self, coordinate_system: CoordinateSystem):
        """
        Setter for property: ( CoordinateSystem NXOpen.CAE.Res) CoordinateSystem
         Returns the coordinate system   
            
         
        """
        pass
    @property
    def DataComponent(self) -> DirectionDataComponent:
        """
        Getter for property: ( DirectionDataComponent NXOpen.CAE.Res) DataComponent
         Returns the data component of direction   
            
         
        """
        pass
    @DataComponent.setter
    def DataComponent(self, data_component: DirectionDataComponent):
        """
        Setter for property: ( DirectionDataComponent NXOpen.CAE.Res) DataComponent
         Returns the data component of direction   
            
         
        """
        pass
    @property
    def ElementLocation(self) -> ElementLocation:
        """
        Getter for property: ( ElementLocation NXOpen.CAE.Res) ElementLocation
         Returns the evaluation location of element.  
             
         
        """
        pass
    @ElementLocation.setter
    def ElementLocation(self, element_location: ElementLocation):
        """
        Setter for property: ( ElementLocation NXOpen.CAE.Res) ElementLocation
         Returns the evaluation location of element.  
             
         
        """
        pass
    @property
    def ShellEvaluationLocation(self) -> ShellElementEvaluationLocation:
        """
        Getter for property: ( ShellElementEvaluationLocation NXOpen.CAE.Res) ShellEvaluationLocation
         Returns the evaluation location of shell element.  
             
         
        """
        pass
    @ShellEvaluationLocation.setter
    def ShellEvaluationLocation(self, shell_location: ShellElementEvaluationLocation):
        """
        Setter for property: ( ShellElementEvaluationLocation NXOpen.CAE.Res) ShellEvaluationLocation
         Returns the evaluation location of shell element.  
             
         
        """
        pass
    @property
    def SpringForceEvaluationFromDisplacement(self) -> bool:
        """
        Getter for property: (bool) SpringForceEvaluationFromDisplacement
         Returns the spring force evaluation From displacement flag.  
             
         
        """
        pass
    @SpringForceEvaluationFromDisplacement.setter
    def SpringForceEvaluationFromDisplacement(self, spring_force_evaluation_from_displacement: bool):
        """
        Setter for property: (bool) SpringForceEvaluationFromDisplacement
         Returns the spring force evaluation From displacement flag.  
             
         
        """
        pass
    def GetDestinationElements(self) -> List[NXOpen.CAE.FEElement]:
        """
         Returns the destination elements 
         Returns destination_elements ( NXOpen.CAE.FEElement Li):  .
        """
        pass
    def SetDestinationElements(self, destination_element: List[NXOpen.CAE.FEElement]) -> None:
        """
         Sets the destination elements 
        """
        pass
class ElementalFunctionEvaluationSetting(FunctionEvaluationSetting): 
    """Represents the parameters setting for elemental function evaluation. Only available to
    NXOpen.CAE.ResponseSimulation.RSEvent.Type.Transient,
    NXOpen.CAE.ResponseSimulation.RSEvent.Type.Frequency,
    NXOpen.CAE.ResponseSimulation.RSEvent.Type.Random
     """
    pass
class ElementLocation(Enum):
    """
    Members Include: 
     |Both|  
     |Centroid|  
     |Corners|  

    """
    Both: int
    Centroid: int
    Corners: int
    @staticmethod
    def ValueOf(value: int) -> ElementLocation:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class EvaluationParameters(NXOpen.TaggedObject): 
    """ Represents the evaluation parameters for a response simulation meta solution """
    class AnalysisIntegrationMethod(Enum):
        """
        Members Include: 
         |DuhameldIntegral|   
         |NewmarkBeta|   

        """
        DuhameldIntegral: int
        NewmarkBeta: int
        @staticmethod
        def ValueOf(value: int) -> EvaluationParameters.AnalysisIntegrationMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def HypermatrixBufferSize(self) -> int:
        """
        Getter for property: (int) HypermatrixBufferSize
         Returns the buffer allocated for Hypermatrix files   
            
         
        """
        pass
    @HypermatrixBufferSize.setter
    def HypermatrixBufferSize(self, buffer_size: int):
        """
        Setter for property: (int) HypermatrixBufferSize
         Returns the buffer allocated for Hypermatrix files   
            
         
        """
        pass
    @property
    def IntegrationMethod(self) -> EvaluationParameters.AnalysisIntegrationMethod:
        """
        Getter for property: ( EvaluationParameters.AnalysisIntegrationMethod NXOpen.CAE.Res) IntegrationMethod
         Returns the integration method used for transient analysis   
            
         
        """
        pass
    @IntegrationMethod.setter
    def IntegrationMethod(self, method: EvaluationParameters.AnalysisIntegrationMethod):
        """
        Setter for property: ( EvaluationParameters.AnalysisIntegrationMethod NXOpen.CAE.Res) IntegrationMethod
         Returns the integration method used for transient analysis   
            
         
        """
        pass
    @property
    def MaxArraySize(self) -> int:
        """
        Getter for property: (int) MaxArraySize
         Returns the dynamic storage array size allocated for RS evaluations   
            
         
        """
        pass
    @MaxArraySize.setter
    def MaxArraySize(self, max_array_size: int):
        """
        Setter for property: (int) MaxArraySize
         Returns the dynamic storage array size allocated for RS evaluations   
            
         
        """
        pass
    @property
    def MinDampingStatus(self) -> bool:
        """
        Getter for property: (bool) MinDampingStatus
         Returns the minimum damping ratio status   
            
         
        """
        pass
    @MinDampingStatus.setter
    def MinDampingStatus(self, damping_status: bool):
        """
        Setter for property: (bool) MinDampingStatus
         Returns the minimum damping ratio status   
            
         
        """
        pass
    @property
    def ZeroMeanCorrection(self) -> bool:
        """
        Getter for property: (bool) ZeroMeanCorrection
         Returns the time-domain integration of acceleration excitations,
                    used in evaluating time responses to acceleration loads.  
           
                    false: no correction, meaning that "rigid drifting" shows in the
                           displacement response when an acceleration excitation is applied;
                    true:  the software corrects for drifting by assuming a zero mean. Rigid drifting is filtered
                           out based on a numerical integration that does not assume an initial condition.  
         
        """
        pass
    @ZeroMeanCorrection.setter
    def ZeroMeanCorrection(self, correction_value: bool):
        """
        Setter for property: (bool) ZeroMeanCorrection
         Returns the time-domain integration of acceleration excitations,
                    used in evaluating time responses to acceleration loads.  
           
                    false: no correction, meaning that "rigid drifting" shows in the
                           displacement response when an acceleration excitation is applied;
                    true:  the software corrects for drifting by assuming a zero mean. Rigid drifting is filtered
                           out based on a numerical integration that does not assume an initial condition.  
         
        """
        pass
class EvaluationResultType(Enum):
    """
    Members Include: 
     |Receptance|  
     |Mobility|  
     |Inertance|  
     |Displacement|  
     |Velocity|  
     |Acceleration|  
     |Stress|  
     |Strain|  
     |StrainEnergy|  
     |ShellResultant|  
     |ElementForce|  
     |BeamElementForce|  
     |ShellStressResultant|  
     |ReactionForce|  

    """
    Receptance: int
    Mobility: int
    Inertance: int
    Displacement: int
    Velocity: int
    Acceleration: int
    Stress: int
    Strain: int
    StrainEnergy: int
    ShellResultant: int
    ElementForce: int
    BeamElementForce: int
    ShellStressResultant: int
    ReactionForce: int
    @staticmethod
    def ValueOf(value: int) -> EvaluationResultType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class EvaluationSettingBuilder(NXOpen.Builder): 
    """ Represents the abstract builder class of all evaluation setting classes. """
    pass
import NXOpen
class EvaluationSettingManager(NXOpen.Object): 
    """ Represents the manager of all evaluation setting objects. Any evaluation setting object must 
    be created through this class """
    def CreateCsdEvaluationSettingBuilder(self, setting: CsdEvaluationSetting) -> CsdEvaluationSettingBuilder:
        """
         Creates CSD evaluation setting object 
         Returns builder ( CsdEvaluationSettingBuilder NXOpen.CAE.Res):   .
        """
        pass
    def CreateElementalFunctionEvaluationSettingBuilder(self, setting: ElementalFunctionEvaluationSetting) -> ElementalFunctionEvaluationSettingBuilder:
        """
         Creates elemental function evaluation setting object 
         Returns builder ( ElementalFunctionEvaluationSettingBuilder NXOpen.CAE.Res):   .
        """
        pass
    def CreateFrfEvaluationSettingBuilder(self, setting: FrfEvaluationSetting) -> FrfEvaluationSettingBuilder:
        """
         Creates FRF evaluation setting object 
         Returns builder ( FrfEvaluationSettingBuilder NXOpen.CAE.Res):   .
        """
        pass
    def CreateLcrResultsEvaluationSettingBuilder(self, setting: LcrResultsEvaluationSetting) -> LcrResultsEvaluationSettingBuilder:
        """
         Creates LCR results evaluation setting object 
         Returns builder ( LcrResultsEvaluationSettingBuilder NXOpen.CAE.Res):   .
        """
        pass
    def CreateNodalFunctionEvaluationSettingBuilder(self, setting: NodalFunctionEvaluationSetting) -> NodalFunctionEvaluationSettingBuilder:
        """
         Creates nodal function evaluation setting object 
         Returns builder ( NodalFunctionEvaluationSettingBuilder NXOpen.CAE.Res):   .
        """
        pass
    def CreatePeakValueEvaluationSettingBuilder(self, setting: PeakValueEvaluationSetting) -> PeakValueEvaluationSettingBuilder:
        """
         Creates peak value evaluation setting object 
         Returns builder ( PeakValueEvaluationSettingBuilder NXOpen.CAE.Res):   .
        """
        pass
    def CreateResponseResultsEvaluationSettingBuilder(self, setting: ResponseResultsEvaluationSetting) -> ResponseResultsEvaluationSettingBuilder:
        """
         Creates response results evaluation setting object 
         Returns builder ( ResponseResultsEvaluationSettingBuilder NXOpen.CAE.Res):   .
        """
        pass
    def CreateRmsResultsEvaluationSettingBuilder(self, setting: RmsResultsEvaluationSetting) -> RmsResultsEvaluationSettingBuilder:
        """
         Creates RMS results evaluation setting object 
         Returns builder ( RmsResultsEvaluationSettingBuilder NXOpen.CAE.Res):   .
        """
        pass
    def CreateSensorEvaluationSettingBuilder(self, setting: SensorEvaluationSetting) -> SensorEvaluationSettingBuilder:
        """
         Creates sensor evaluation setting object 
         Returns builder ( SensorEvaluationSettingBuilder NXOpen.CAE.Res):   .
        """
        pass
    def CreateStrainGageEvaluationSettingBuilder(self, setting: StrainGageEvaluationSetting) -> StrainGageEvaluationSettingBuilder:
        """
         Creates strain gage evaluation setting object 
         Returns builder ( StrainGageEvaluationSettingBuilder NXOpen.CAE.Res):   .
        """
        pass
    def CreateStrengthResultsEvaluationSettingBuilder(self, setting: StrengthResultsEvaluationSetting) -> StrengthResultsEvaluationSettingBuilder:
        """
         Creates strength results evaluation setting object 
         Returns builder ( StrengthResultsEvaluationSettingBuilder NXOpen.CAE.Res):   .
        """
        pass
    def CreateTransmissibilityEvaluationSettingBuilder(self, setting: TransmissibilityEvaluationSetting) -> TransmissibilityEvaluationSettingBuilder:
        """
         Creates transmissibility evaluation setting object 
         Returns builder ( TransmissibilityEvaluationSettingBuilder NXOpen.CAE.Res):   .
        """
        pass
import NXOpen
class EvaluationSetting(NXOpen.NXObject): 
    """ Represents the abstract class of all evaluation setting classes. """
    def Destroy(self) -> None:
        """
         Destroies the evaluation setting object after evaluation. 
        """
        pass
class ExcitationBuilder(BaseBuilder): 
    """ Represents the abstract excitation builder class. Any of real excitation builder
        must inherit from this class.
     """
    class ExcitationLocationType(Enum):
        """
        Members Include: 
         |StaticLoad|   
         |DistributedLoad|   
         |NodalForce|   
         |EnforcedMotion|   

        """
        StaticLoad: int
        DistributedLoad: int
        NodalForce: int
        EnforcedMotion: int
        @staticmethod
        def ValueOf(value: int) -> ExcitationBuilder.ExcitationLocationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DynamicEvent(self) -> RSEvent:
        """
        Getter for property: ( RSEvent NXOpen.CAE.Res) DynamicEvent
         Returns the parent dynamic event object   
            
         
        """
        pass
    @property
    def ExcitationLocationDefinition(self) -> ExcitationLocationDefinition:
        """
        Getter for property: ( ExcitationLocationDefinition NXOpen.CAE.Res) ExcitationLocationDefinition
         Returns the excitation location definition   
            
         
        """
        pass
import NXOpen
class ExcitationCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of excitation objects """
    def CreateCsdExcitationBuilder(self, excitation: CSDExcitation) -> CSDExcitationBuilder:
        """
         Creates the builder object of NXOpen.CAE.ResponseSimulation.DDAMExcitation 
         Returns builder ( CSDExcitationBuilder NXOpen.CAE.Res):   .
        """
        pass
    def CreateDdamExcitationBuilder(self, excitation: DDAMExcitation) -> DDAMExcitationBuilder:
        """
         Creates the builder object of NXOpen.CAE.ResponseSimulation.DDAMExcitation 
         Returns builder ( DDAMExcitationBuilder NXOpen.CAE.Res):   .
        """
        pass
    def CreateDistributedLoadExcitationBuilder(self, excitation: DistributedLoadExcitation) -> DistributedLoadExcitationBuilder:
        """
         Creates the builder object of NXOpen.CAE.ResponseSimulation.DistributedLoadExcitation
         Returns builder ( DistributedLoadExcitationBuilder NXOpen.CAE.Res):   .
        """
        pass
    def CreateRotationalDdamExcitationBuilder(self, excitation: DDAMExcitation) -> DDAMExcitationBuilder:
        """
         Creates the builder object of NXOpen.CAE.ResponseSimulation.DDAMExcitation 
         Returns builder ( DDAMExcitationBuilder NXOpen.CAE.Res):   .
        """
        pass
    def CreateRotationalNodalFunctionExcitationBuilder(self, excitation: RotationalNodalFunctionExcitation) -> RotationalNodalFunctionExcitationBuilder:
        """
         Creates the builder object of NXOpen.CAE.ResponseSimulation.RotationalNodalFunctionExcitation 
         Returns builder ( RotationalNodalFunctionExcitationBuilder NXOpen.CAE.Res):   .
        """
        pass
    def CreateStaticLoadExcitationBuilder(self, excitation: StaticLoadExcitation) -> StaticLoadExcitationBuilder:
        """
         Creates the builder object of NXOpen.CAE.ResponseSimulation.StaticLoadExcitation
         Returns builder ( StaticLoadExcitationBuilder NXOpen.CAE.Res):   .
        """
        pass
    def CreateTranslationalDdamExcitationBuilder(self, excitation: DDAMExcitation) -> DDAMExcitationBuilder:
        """
         Creates the builder object of NXOpen.CAE.ResponseSimulation.DDAMExcitation 
         Returns builder ( DDAMExcitationBuilder NXOpen.CAE.Res):   .
        """
        pass
    def CreateTranslationalNodalFunctionExcitationBuilder(self, excitation: TranslationalNodalFunctionExcitation) -> TranslationalNodalFunctionExcitationBuilder:
        """
         Creates the builder object of NXOpen.CAE.ResponseSimulation.TranslationalNodalFunctionExcitation 
         Returns builder ( TranslationalNodalFunctionExcitationBuilder NXOpen.CAE.Res):   .
        """
        pass
    def CreateVelocityImpactExcitationBuilder(self, excitation: VelocityImpactExcitation) -> VelocityImpactExcitationBuilder:
        """
         Creates the builder object of NXOpen.CAE.ResponseSimulation.VelocityImpactExcitation 
         Returns builder ( VelocityImpactExcitationBuilder NXOpen.CAE.Res):   .
        """
        pass
    def DeleteExcitation(self, excitation: Excitation) -> None:
        """
         Deletes an excitation 
        """
        pass
    def FindObject(self, name: str) -> Excitation:
        """
         Finds an excitation with specified excitation name 
         Returns excitation ( Excitation NXOpen.CAE.Res):   .
        """
        pass
import NXOpen
class ExcitationLocationDefinition(NXOpen.TaggedObject): 
    """ Represents the manager to CAE.ResponseSimulation.DistributedLoadExcitation.
     The object of type CAE.ResponseSimulation.DistributedLoadExcitation
      can only be created or edited through this class.
     """
    @property
    def ExcitationLocation(self) -> NXOpen.SelectObject:
        """
        Getter for property: ( NXOpen.SelectObject) ExcitationLocation
         Returns the excitation location on which the excitation will be applied.  
           The excitation location
                type could be force location, enforced motion location or dynamic load defined in response 
                dynamic solution.   
         
        """
        pass
    @property
    def ExcitationLocationId(self) -> int:
        """
        Getter for property: (int) ExcitationLocationId
         Returns the ID of excitation location on which the excitation will be applied.  
           The excitation location ID
                could be node label or load set label   
         
        """
        pass
    @ExcitationLocationId.setter
    def ExcitationLocationId(self, excitaitonLocationId: int):
        """
        Setter for property: (int) ExcitationLocationId
         Returns the ID of excitation location on which the excitation will be applied.  
           The excitation location ID
                could be node label or load set label   
         
        """
        pass
    @property
    def ExcitationLocationType(self) -> ExcitationBuilder.ExcitationLocationType:
        """
        Getter for property: ( ExcitationBuilder.ExcitationLocationType NXOpen.CAE.Res) ExcitationLocationType
         Returns the type of excitaion location   
            
         
        """
        pass
    @ExcitationLocationType.setter
    def ExcitationLocationType(self, excitationLocationType: ExcitationBuilder.ExcitationLocationType):
        """
        Setter for property: ( ExcitationBuilder.ExcitationLocationType NXOpen.CAE.Res) ExcitationLocationType
         Returns the type of excitaion location   
            
         
        """
        pass
    @property
    def ExcitationLocationlist(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) ExcitationLocationlist
         Returns the excitation location list on which the excitation will be applied.  
           The excitation location
                type could be force location, enforced motion location or dynamic load defined in response 
                dynamic solution   
         
        """
        pass
import NXOpen
class Excitation(NXOpen.NXObject): 
    """ Represents the abstract class of dynamic excitations """
    class Component(Enum):
        """
        Members Include: 
         |DistributedLoad|  
         |X|   
         |Y|   
         |Z|   
         |Rx|   
         |Ry|   
         |Rz|   
         |UserDefined|  

        """
        DistributedLoad: int
        X: int
        Y: int
        Z: int
        Rx: int
        Ry: int
        Rz: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> Excitation.Component:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ExcitationName(self) -> str:
        """
        Getter for property: (str) ExcitationName
         Returns the excitation name   
            
         
        """
        pass
    @ExcitationName.setter
    def ExcitationName(self, excitationName: str):
        """
        Setter for property: (str) ExcitationName
         Returns the excitation name   
            
         
        """
        pass
    def Destroy(self) -> None:
        """
         Deletes a response simulation excitation 
        """
        pass
import NXOpen
class FrequencyDefinition(NXOpen.TaggedObject): 
    """ Represents the frequency setting to perform FRF evaluation """
    class Definition(Enum):
        """
        Members Include: 
         |Range|   
         |ModalContribution|   

        """
        Range: int
        ModalContribution: int
        @staticmethod
        def ValueOf(value: int) -> FrequencyDefinition.Definition:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class InterpolationMethod(Enum):
        """
        Members Include: 
         |LogLog|   
         |LogLinear|   
         |LinearLinear|   

        """
        LogLog: int
        LogLinear: int
        LinearLinear: int
        @staticmethod
        def ValueOf(value: int) -> FrequencyDefinition.InterpolationMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ContributorNumber(self) -> int:
        """
        Getter for property: (int) ContributorNumber
         Returns the number of contributors.  
           Only available when maximu contributors
                 will be generated   
         
        """
        pass
    @ContributorNumber.setter
    def ContributorNumber(self, contributorNumber: int):
        """
        Setter for property: (int) ContributorNumber
         Returns the number of contributors.  
           Only available when maximu contributors
                 will be generated   
         
        """
        pass
    @property
    def EndValue(self) -> float:
        """
        Getter for property: (float) EndValue
         Returns the end value of frequency range.  
           Only available when the frequency is defined 
                by  CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange    
         
        """
        pass
    @EndValue.setter
    def EndValue(self, end_value: float):
        """
        Setter for property: (float) EndValue
         Returns the end value of frequency range.  
           Only available when the frequency is defined 
                by  CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange    
         
        """
        pass
    @property
    def EvaluationType(self) -> FrequencyDefinition.Definition:
        """
        Getter for property: ( FrequencyDefinition.Definition NXOpen.CAE.Res) EvaluationType
         Returns the method to define frequency  
            
         
        """
        pass
    @EvaluationType.setter
    def EvaluationType(self, type: FrequencyDefinition.Definition):
        """
        Setter for property: ( FrequencyDefinition.Definition NXOpen.CAE.Res) EvaluationType
         Returns the method to define frequency  
            
         
        """
        pass
    @property
    def GenerateMaximumContributors(self) -> bool:
        """
        Getter for property: (bool) GenerateMaximumContributors
         Returns the option for generating maximum contributors or not.  
           Only available when
                frequency definition metod is  CAE::ResponseSimulation::FrequencyDefinition::DefinitionModalContribution    
         
        """
        pass
    @GenerateMaximumContributors.setter
    def GenerateMaximumContributors(self, generateMaximumContributors: bool):
        """
        Setter for property: (bool) GenerateMaximumContributors
         Returns the option for generating maximum contributors or not.  
           Only available when
                frequency definition metod is  CAE::ResponseSimulation::FrequencyDefinition::DefinitionModalContribution    
         
        """
        pass
    @property
    def InterpolationMethodOption(self) -> FrequencyDefinition.InterpolationMethod:
        """
        Getter for property: ( FrequencyDefinition.InterpolationMethod NXOpen.CAE.Res) InterpolationMethodOption
         Returns the interpolation method.  
           Only available when the frequency is defined by
                 CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange    
         
        """
        pass
    @InterpolationMethodOption.setter
    def InterpolationMethodOption(self, interpolation_method: FrequencyDefinition.InterpolationMethod):
        """
        Setter for property: ( FrequencyDefinition.InterpolationMethod NXOpen.CAE.Res) InterpolationMethodOption
         Returns the interpolation method.  
           Only available when the frequency is defined by
                 CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange    
         
        """
        pass
    @property
    def NormalizeResults(self) -> bool:
        """
        Getter for property: (bool) NormalizeResults
         Returns the option to normalize results.  
           Only available when maximu contributors
                 will be generated   
         
        """
        pass
    @NormalizeResults.setter
    def NormalizeResults(self, normalizeResults: bool):
        """
        Setter for property: (bool) NormalizeResults
         Returns the option to normalize results.  
           Only available when maximu contributors
                 will be generated   
         
        """
        pass
    @property
    def SpectralLine(self) -> int:
        """
        Getter for property: (int) SpectralLine
         Returns the additional spectral lines.  
           Only available when frequency is defined 
                by  CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange    
         
        """
        pass
    @SpectralLine.setter
    def SpectralLine(self, spectral_lines: int):
        """
        Setter for property: (int) SpectralLine
         Returns the additional spectral lines.  
           Only available when frequency is defined 
                by  CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange    
         
        """
        pass
    @property
    def StartValue(self) -> float:
        """
        Getter for property: (float) StartValue
         Returns the start value of frequency range.  
           Only available when the frequency is defined
                by  CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange    
         
        """
        pass
    @StartValue.setter
    def StartValue(self, start_value: float):
        """
        Setter for property: (float) StartValue
         Returns the start value of frequency range.  
           Only available when the frequency is defined
                by  CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange    
         
        """
        pass
    def GetFrequencies(self) -> List[float]:
        """
         Returns frequency values to perform FRF evaluation. Only available when the frequency definition 
                method is CAE.ResponseSimulation.FrequencyDefinition.Definition.ModalContribution 
         Returns frequencies (List[float]):  .
        """
        pass
    def SetFrequencies(self, frequencies: List[float]) -> None:
        """
         Sets the frequency values to perform FRF evaluation. Only available when the frequency definition 
                method is CAE.ResponseSimulation.FrequencyDefinition.Definition.ModalContribution 
        """
        pass
class FrfEvaluationSettingBuilder(ModalResultsEvaluationSettingBuilder): 
    """ This is a manager to the NXOpen.CAE.ResponseSimulation.FrfEvaluationSetting class. 
    Object of type NXOpen.CAE.ResponseSimulation.FrfEvaluationSetting can be 
    created and edited only through this class
     """
    pass
class FrfEvaluationSetting(ModalResultsEvaluationSetting): 
    """ Represents the parameters setting for FRF results evaluation """
    pass
import NXOpen
import NXOpen.CAE
class FunctionComponentData(NXOpen.TaggedObject): 
    """ Represents a function component setting of 
    NXOpen.CAE.ResponseSimulation.NodalFunctionExcitation on one direction """
    @property
    def Enable(self) -> bool:
        """
        Getter for property: (bool) Enable
         Returns the option to enable the function component to be used while evaluating   
            
         
        """
        pass
    @Enable.setter
    def Enable(self, enable_option: bool):
        """
        Setter for property: (bool) Enable
         Returns the option to enable the function component to be used while evaluating   
            
         
        """
        pass
    @property
    def Function(self) -> NXOpen.CAE.Function:
        """
        Getter for property: ( NXOpen.CAE.Function) Function
         Returns the function to be applied   
            
         
        """
        pass
    @Function.setter
    def Function(self, excitation_function: NXOpen.CAE.Function):
        """
        Setter for property: ( NXOpen.CAE.Function) Function
         Returns the function to be applied   
            
         
        """
        pass
    @property
    def PhaseAngle(self) -> float:
        """
        Getter for property: (float) PhaseAngle
         Returns the phase angle.  
           Only available when the onwer event is 
                 NXOpen::CAE::ResponseSimulation::RSEvent::TypeTransient    
         
        """
        pass
    @PhaseAngle.setter
    def PhaseAngle(self, phase_angle: float):
        """
        Setter for property: (float) PhaseAngle
         Returns the phase angle.  
           Only available when the onwer event is 
                 NXOpen::CAE::ResponseSimulation::RSEvent::TypeTransient    
         
        """
        pass
    @property
    def ScalarFactor(self) -> float:
        """
        Getter for property: (float) ScalarFactor
         Returns the scalar factor   
            
         
        """
        pass
    @ScalarFactor.setter
    def ScalarFactor(self, scalar_factor: float):
        """
        Setter for property: (float) ScalarFactor
         Returns the scalar factor   
            
         
        """
        pass
    def GetComponentType(self) -> Excitation.Component:
        """
         Returns the component type 
         Returns component_type ( Excitation.Component NXOpen.CAE.Res):  .
        """
        pass
import NXOpen
class FunctionEvaluationOutputSettings(NXOpen.TaggedObject): 
    """ Represents the output setting for function response evaluation"""
    @property
    def RecordPrefix(self) -> str:
        """
        Getter for property: (str) RecordPrefix
         Returns the prefix of evaluation results record name   
            
         
        """
        pass
    @RecordPrefix.setter
    def RecordPrefix(self, record_prefix: str):
        """
        Setter for property: (str) RecordPrefix
         Returns the prefix of evaluation results record name   
            
         
        """
        pass
    @property
    def ShowPlot(self) -> bool:
        """
        Getter for property: (bool) ShowPlot
         Returns the option of show plot.  
           If true, the evaluation results will be displayed on screen   
         
        """
        pass
    @ShowPlot.setter
    def ShowPlot(self, show_plot: bool):
        """
        Setter for property: (bool) ShowPlot
         Returns the option of show plot.  
           If true, the evaluation results will be displayed on screen   
         
        """
        pass
    @property
    def StoreOption(self) -> bool:
        """
        Getter for property: (bool) StoreOption
         Returns the store option.  
           If true, the evaluation results will be stored on disk   
         
        """
        pass
    @StoreOption.setter
    def StoreOption(self, store_option: bool):
        """
        Setter for property: (bool) StoreOption
         Returns the store option.  
           If true, the evaluation results will be stored on disk   
         
        """
        pass
import NXOpen
class FunctionEvaluationSettingBuilder(NXOpen.Builder): 
    """ Represents the abstract builder class of evaluation setting for function response evaluation
    """
    @property
    def OutputSettings(self) -> FunctionEvaluationOutputSettings:
        """
        Getter for property: ( FunctionEvaluationOutputSettings NXOpen.CAE.Res) OutputSettings
         Returns the output setting.  
             
         
        """
        pass
    @property
    def ResultType(self) -> EvaluationResultType:
        """
        Getter for property: ( EvaluationResultType NXOpen.CAE.Res) ResultType
         Returns the result type   
            
         
        """
        pass
    @ResultType.setter
    def ResultType(self, result_type: EvaluationResultType):
        """
        Setter for property: ( EvaluationResultType NXOpen.CAE.Res) ResultType
         Returns the result type   
            
         
        """
        pass
class FunctionEvaluationSetting(EvaluationSetting): 
    """ Represents the abstract class of evaluation setting for function response evaluation
    """
    pass
import NXOpen
class InitialConditions(NXOpen.NXObject): 
    """ Represents the initial condition setting of transient event """
    class EntryMethod(Enum):
        """
        Members Include: 
         |ManualData|   
         |FromEef|   

        """
        ManualData: int
        FromEef: int
        @staticmethod
        def ValueOf(value: int) -> InitialConditions.EntryMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Type(Enum):
        """
        Members Include: 
         |QuasiStatic|   
         |Zero|   
         |UserDefined|   

        """
        QuasiStatic: int
        Zero: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> InitialConditions.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def EntryMethodOption(self) -> InitialConditions.EntryMethod:
        """
        Getter for property: ( InitialConditions.EntryMethod NXOpen.CAE.Res) EntryMethodOption
         Returns the entry method of user customization   
            
         
        """
        pass
    @EntryMethodOption.setter
    def EntryMethodOption(self, entry_method: InitialConditions.EntryMethod):
        """
        Setter for property: ( InitialConditions.EntryMethod NXOpen.CAE.Res) EntryMethodOption
         Returns the entry method of user customization   
            
         
        """
        pass
    @property
    def ExistingEefFile(self) -> str:
        """
        Getter for property: (str) ExistingEefFile
         Returns an existing EEF file containing initial condition.  
           Only available when the 
                initial condition type is  CAE::ResponseSimulation::InitialConditions::TypeUserDefined 
                and the entry method is  CAE::ResponseSimulation::InitialConditions::EntryMethodFromEef    
         
        """
        pass
    @ExistingEefFile.setter
    def ExistingEefFile(self, eef_file: str):
        """
        Setter for property: (str) ExistingEefFile
         Returns an existing EEF file containing initial condition.  
           Only available when the 
                initial condition type is  CAE::ResponseSimulation::InitialConditions::TypeUserDefined 
                and the entry method is  CAE::ResponseSimulation::InitialConditions::EntryMethodFromEef    
         
        """
        pass
    @property
    def InitialConditionType(self) -> InitialConditions.Type:
        """
        Getter for property: ( InitialConditions.Type NXOpen.CAE.Res) InitialConditionType
         Returns the definition method   
            
         
        """
        pass
    @InitialConditionType.setter
    def InitialConditionType(self, initial_condition_type: InitialConditions.Type):
        """
        Setter for property: ( InitialConditions.Type NXOpen.CAE.Res) InitialConditionType
         Returns the definition method   
            
         
        """
        pass
    def GetAllCustomizedInitialData(self) -> List[ModeInitialData]:
        """
         Returns customized initial data of all normal modes. Only available when initial condition type is 
                CAE.ResponseSimulation.InitialConditions.Type.UserDefined 
         Returns initial_data ( ModeInitialData List[NXOpen.CAE.R):  .
        """
        pass
    def GetCustomizedInitialDataById(self, mode_id: int) -> ModeInitialData:
        """
         Returns customized initial data of normal mode by mode id. Only available when initial condition
                type is CAE.ResponseSimulation.InitialConditions.Type.UserDefined 
         Returns initial_data ( ModeInitialData NXOpen.CAE.Res):  .
        """
        pass
class InterpolationMethod(Enum):
    """
    Members Include: 
     |LogLog|   
     |LinearLinear|   
     |LinearLog|   
     |LogLinear|   

    """
    LogLog: int
    LinearLinear: int
    LinearLog: int
    LogLinear: int
    @staticmethod
    def ValueOf(value: int) -> InterpolationMethod:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class LcrResultsEvaluationSettingBuilder(RmsResultsEvaluationSettingBuilder): 
    """ This is a manager to the NXOpen.CAE.ResponseSimulation.LcrResultsEvaluationSetting class. 
    Object of type NXOpen.CAE.ResponseSimulation.LcrResultsEvaluationSetting can be 
    created and edited only through this class
     """
    @property
    def CrossingLevelExpression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CrossingLevelExpression
         Returns the crossing level expression  
            
         
        """
        pass
class LcrResultsEvaluationSetting(RmsResultsEvaluationSetting): 
    """ Represents the parameters setting of LCR results evaluation. Only available when
    event type is NXOpen.CAE.ResponseSimulation.RSEvent.Type.Random. For more information,
    see the Response Dynamics Section of the Gateway Help """
    pass
import NXOpen
class Manager(NXOpen.Object): 
    """ Represents the Response Dynamics manager to contain all Response Dynamics objects """
    @property
    def Solutions() -> SolutionCollection:
        """
         Returns the Response Dynamics solution collection belonging to this sim part 
        """
        pass
    @property
    def Events() -> RSEventCollection:
        """
         Returns the Response Dynamics event collection belonging to this sim part 
        """
        pass
    @property
    def Excitations() -> ExcitationCollection:
        """
         Returns the Response Dynamics excitation collection belonging to this sim part 
        """
        pass
    @property
    def EvaluationSettingManager() -> EvaluationSettingManager:
        """
         Returns the Response Dynamics evaluation data manager belonging to this sim part 
        """
        pass
    @property
    def Sensors() -> SensorCollection:
        """
         Returns the Response Dynamics sensor collection belonging to this sim part 
        """
        pass
    @property
    def StrainGages() -> StrainGageCollection:
        """
         Returns the Response Dynamics strain gage collection belonging to this sim part 
        """
        pass
import NXOpen
class ModalProperties(NXOpen.NXObject): 
    """ Represents the modal presentation of a response analysis meta solution """
    def Activate(self, activate: bool) -> None:
        """
         Sets activate or deactivate status for all normal modes 
        """
        pass
    def DeactivateModesBelowLimit(self, limit: float) -> None:
        """
         Sets deactivate status for all normal modes that are less than the % Mass Limit Specified 
        """
        pass
    def GetAttachmentModeCount(self) -> int:
        """
         Returns the count of attachment modes 
         Returns mode_count (int):  .
        """
        pass
    def GetConstrainModeCount(self) -> int:
        """
         Returns the count of constrain modes 
         Returns mode_count (int):  .
        """
        pass
    def GetNormalModeById(self, mode_id: int) -> NormalMode:
        """
         Returns normal mode with specified node ID 
         Returns normal_mode ( NormalMode NXOpen.CAE.Res):  .
        """
        pass
    def GetNormalModeCount(self) -> int:
        """
         Returns the count of normal modes 
         Returns mode_count (int):  .
        """
        pass
    def GetNormalModes(self) -> List[NormalMode]:
        """
         Returns all normal modes 
         Returns normal_modes ( NormalMode List[NXOpen.CAE.R):  .
        """
        pass
    def GetPhysicalDampingSettings(self) -> PhysicalDampingSettings:
        """
         Returns the physical damping setting object 
         Returns physical_damping_settings ( PhysicalDampingSettings NXOpen.CAE.Res): .
        """
        pass
    def SetDampingFactors(self, viscous_damping: float, hysteretic_damping: float) -> None:
        """
         Set damping factors for all normal modes 
        """
        pass
    def SetRayleighDamping(self, alpha_factor: float, belta_factor: float) -> None:
        """
         Set rayleigh's damping for all normal modes 
        """
        pass
import NXOpen.CAE
class ModalResultsEvaluationSettingBuilder(FunctionEvaluationSettingBuilder): 
    """ Represents the abstract builder class of evaluation setting for FRF and transmissibility """
    @property
    def DataLocation(self) -> DataLocation:
        """
        Getter for property: ( DataLocation NXOpen.CAE.Res) DataLocation
         Returns the frequency setting   
            
         
        """
        pass
    @property
    def EvaluationProperty(self) -> FrequencyDefinition:
        """
        Getter for property: ( FrequencyDefinition NXOpen.CAE.Res) EvaluationProperty
         Returns the frequency setting   
            
         
        """
        pass
    @property
    def InputDirection(self) -> DirectionDataComponent:
        """
        Getter for property: ( DirectionDataComponent NXOpen.CAE.Res) InputDirection
         Returns the source direction data component   
            
         
        """
        pass
    @InputDirection.setter
    def InputDirection(self, data_component: DirectionDataComponent):
        """
        Setter for property: ( DirectionDataComponent NXOpen.CAE.Res) InputDirection
         Returns the source direction data component   
            
         
        """
        pass
    @property
    def InputNode(self) -> NXOpen.CAE.FENode:
        """
        Getter for property: ( NXOpen.CAE.FENode) InputNode
         Returns the source node.  
             
         
        """
        pass
    @InputNode.setter
    def InputNode(self, source_node: NXOpen.CAE.FENode):
        """
        Setter for property: ( NXOpen.CAE.FENode) InputNode
         Returns the source node.  
             
         
        """
        pass
    @property
    def ObservationNode(self) -> NXOpen.CAE.FENode:
        """
        Getter for property: ( NXOpen.CAE.FENode) ObservationNode
         Returns the observation nodes.  
            
         
        """
        pass
    @ObservationNode.setter
    def ObservationNode(self, observation_node: NXOpen.CAE.FENode):
        """
        Setter for property: ( NXOpen.CAE.FENode) ObservationNode
         Returns the observation nodes.  
            
         
        """
        pass
    @property
    def OutputRequest(self) -> DirectionDataComponent:
        """
        Getter for property: ( DirectionDataComponent NXOpen.CAE.Res) OutputRequest
         Returns the destination direction data component   
            
         
        """
        pass
    @OutputRequest.setter
    def OutputRequest(self, data_component: DirectionDataComponent):
        """
        Setter for property: ( DirectionDataComponent NXOpen.CAE.Res) OutputRequest
         Returns the destination direction data component   
            
         
        """
        pass
    def GetOutputElements(self) -> List[NXOpen.CAE.FEElement]:
        """
         Returns destination nodes. Only available when result type is 
                CAE.ResponseSimulation.EvaluationResultType.Stress,
                CAE.ResponseSimulation.EvaluationResultType.Strain,
                CAE.ResponseSimulation.EvaluationResultType.ShellStressResultant 
         Returns destination_elements ( NXOpen.CAE.FEElement Li):  .
        """
        pass
    def GetOutputNodes(self) -> List[NXOpen.CAE.FENode]:
        """
         Returns destination nodes. Only available when result type is 
                CAE.ResponseSimulation.EvaluationResultType.Displacement,
                CAE.ResponseSimulation.EvaluationResultType.Velocity,
                CAE.ResponseSimulation.EvaluationResultType.Acceleration,
                CAE.ResponseSimulation.EvaluationResultType.ReactionForce 
         Returns destination_node ( NXOpen.CAE.FENode Li):  .
        """
        pass
    def SetOutputElements(self, destination_elements: List[NXOpen.CAE.FEElement]) -> None:
        """
         Sets destination nodes 
        """
        pass
    def SetOutputNodes(self, destination_node: List[NXOpen.CAE.FENode]) -> None:
        """
         Sets destination nodes 
        """
        pass
class ModalResultsEvaluationSetting(FunctionEvaluationSetting): 
    """ Represents the abstract class of evaluation setting for FRF and transmissibility """
    pass
import NXOpen
class ModeInitialData(NXOpen.NXObject): 
    """ Represents the initial setting for a normal mode """
    @property
    def InitialDisplacement(self) -> float:
        """
        Getter for property: (float) InitialDisplacement
         Returns the initial diaplacement   
            
         
        """
        pass
    @InitialDisplacement.setter
    def InitialDisplacement(self, initial_displacement: float):
        """
        Setter for property: (float) InitialDisplacement
         Returns the initial diaplacement   
            
         
        """
        pass
    @property
    def InitialVelocity(self) -> float:
        """
        Getter for property: (float) InitialVelocity
         Returns the initial velocity   
            
         
        """
        pass
    @InitialVelocity.setter
    def InitialVelocity(self, initial_velocity: float):
        """
        Setter for property: (float) InitialVelocity
         Returns the initial velocity   
            
         
        """
        pass
    def GetModeId(self) -> int:
        """
         Returns normal mode ID 
         Returns mode_id (int):  .
        """
        pass
class NodalAveragingOption(Enum):
    """
    Members Include: 
     |Shells|  
     |Solids|  

    """
    Shells: int
    Solids: int
    @staticmethod
    def ValueOf(value: int) -> NodalAveragingOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class NodalFunctionEvalBeamLocation(Enum):
    """
    Members Include: 
     |C|  Stress Recovery point C on a beam cross section 
     |D|  Stress Recovery point D on a beam cross section 
     |E|  Stress Recovery point E on a beam cross section 
     |F|  Stress Recovery point F on a beam cross section 
     |All|  All four Stress Recovery points on a beam cross section 

    """
    C: int
    D: int
    E: int
    F: int
    All: int
    @staticmethod
    def ValueOf(value: int) -> NodalFunctionEvalBeamLocation:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class NodalFunctionEvalRequest(Enum):
    """
    Members Include: 
     |UserDefinedDirection|  
     |DataComponent|  

    """
    UserDefinedDirection: int
    DataComponent: int
    @staticmethod
    def ValueOf(value: int) -> NodalFunctionEvalRequest:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class NodalFunctionEvalShellLocation(Enum):
    """
    Members Include: 
     |Top|  Top layer 
     |Middle|  Middle layer 
     |Bottom|  Bottom layer 
     |All|  All three layers 

    """
    Top: int
    Middle: int
    Bottom: int
    All: int
    @staticmethod
    def ValueOf(value: int) -> NodalFunctionEvalShellLocation:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.CAE
class NodalFunctionEvaluationSettingBuilder(FunctionEvaluationSettingBuilder): 
    """ This is a manager to the NXOpen.CAE.ResponseSimulation.NodalFunctionEvaluationSetting class. 
    Object of type NXOpen.CAE.ResponseSimulation.NodalFunctionEvaluationSetting can be 
    created and edited only through this class
     """
    @property
    def BeamDataLocation(self) -> NodalFunctionEvalBeamLocation:
        """
        Getter for property: ( NodalFunctionEvalBeamLocation NXOpen.CAE.Res) BeamDataLocation
         Returns the evaluation location of beam element, which is available when 
                     NXOpen::CAE::ResponseSimulation::EvaluationResultType  is 
                     NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStress , or
                     NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStrain    
            
         
        """
        pass
    @BeamDataLocation.setter
    def BeamDataLocation(self, beam_location: NodalFunctionEvalBeamLocation):
        """
        Setter for property: ( NodalFunctionEvalBeamLocation NXOpen.CAE.Res) BeamDataLocation
         Returns the evaluation location of beam element, which is available when 
                     NXOpen::CAE::ResponseSimulation::EvaluationResultType  is 
                     NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStress , or
                     NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStrain    
            
         
        """
        pass
    @property
    def CoordinateSystem(self) -> CoordinateSystem:
        """
        Getter for property: ( CoordinateSystem NXOpen.CAE.Res) CoordinateSystem
         Returns the coordinate system   
            
         
        """
        pass
    @CoordinateSystem.setter
    def CoordinateSystem(self, coordinate_system: CoordinateSystem):
        """
        Setter for property: ( CoordinateSystem NXOpen.CAE.Res) CoordinateSystem
         Returns the coordinate system   
            
         
        """
        pass
    @property
    def DataComponent(self) -> DirectionDataComponent:
        """
        Getter for property: ( DirectionDataComponent NXOpen.CAE.Res) DataComponent
         Returns the direction data component   
            
         
        """
        pass
    @DataComponent.setter
    def DataComponent(self, data_component: DirectionDataComponent):
        """
        Setter for property: ( DirectionDataComponent NXOpen.CAE.Res) DataComponent
         Returns the direction data component   
            
         
        """
        pass
    @property
    def RelativeNode(self) -> NXOpen.CAE.FENode:
        """
        Getter for property: ( NXOpen.CAE.FENode) RelativeNode
         Returns the relative node    
            
         
        """
        pass
    @RelativeNode.setter
    def RelativeNode(self, relative_node: NXOpen.CAE.FENode):
        """
        Setter for property: ( NXOpen.CAE.FENode) RelativeNode
         Returns the relative node    
            
         
        """
        pass
    @property
    def ShellDataLocation(self) -> NodalFunctionEvalShellLocation:
        """
        Getter for property: ( NodalFunctionEvalShellLocation NXOpen.CAE.Res) ShellDataLocation
         Returns the evaluation location of shell element, which is available when 
                     NXOpen::CAE::ResponseSimulation::EvaluationResultType  is 
                     NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStress , or
                     NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStrain    
            
         
        """
        pass
    @ShellDataLocation.setter
    def ShellDataLocation(self, shell_location: NodalFunctionEvalShellLocation):
        """
        Setter for property: ( NodalFunctionEvalShellLocation NXOpen.CAE.Res) ShellDataLocation
         Returns the evaluation location of shell element, which is available when 
                     NXOpen::CAE::ResponseSimulation::EvaluationResultType  is 
                     NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStress , or
                     NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStrain    
            
         
        """
        pass
    @property
    def UserDefinedDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) UserDefinedDirection
         Returns  the user defined direction   
            
         
        """
        pass
    @UserDefinedDirection.setter
    def UserDefinedDirection(self, user_defined_direction: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) UserDefinedDirection
         Returns  the user defined direction   
            
         
        """
        pass
    @property
    def UsingUserDefinedDirection(self) -> NodalFunctionEvalRequest:
        """
        Getter for property: ( NodalFunctionEvalRequest NXOpen.CAE.Res) UsingUserDefinedDirection
         Returns the option of using user defined direction   
            
         
        """
        pass
    @UsingUserDefinedDirection.setter
    def UsingUserDefinedDirection(self, using_user_defined_direction: NodalFunctionEvalRequest):
        """
        Setter for property: ( NodalFunctionEvalRequest NXOpen.CAE.Res) UsingUserDefinedDirection
         Returns the option of using user defined direction   
            
         
        """
        pass
    def GetDestinationNodes(self) -> List[NXOpen.CAE.FENode]:
        """
          Returns the destination nodes 
         Returns destination_nodes ( NXOpen.CAE.FENode Li):  .
        """
        pass
    def SetDestinationNodes(self, destination_nodes: List[NXOpen.CAE.FENode]) -> None:
        """
         Sets the destination nodes 
        """
        pass
class NodalFunctionEvaluationSetting(FunctionEvaluationSetting): 
    """ Represents the parameters setting of nodal function response evaluation. Available to all
    kinds of event type """
    pass
import NXOpen
class NodalFunctionExcitationBuilder(ExcitationBuilder): 
    """ Represents the manager to NXOpen.CAE.ResponseSimulation.NodalFunctionExcitation. 
    The objects of NXOpen.CAE.ResponseSimulation.NodalFunctionExcitation 
    can be created or edited on through this class """
    @property
    def FrequencyRangeLowerBound(self) -> float:
        """
        Getter for property: (float) FrequencyRangeLowerBound
         Returns the lower bound frequency   
            
         
        """
        pass
    @FrequencyRangeLowerBound.setter
    def FrequencyRangeLowerBound(self, lower_bound: float):
        """
        Setter for property: (float) FrequencyRangeLowerBound
         Returns the lower bound frequency   
            
         
        """
        pass
    @property
    def FrequencyRangeUpperBound(self) -> float:
        """
        Getter for property: (float) FrequencyRangeUpperBound
         Returns the upper bound frequency   
            
         
        """
        pass
    @FrequencyRangeUpperBound.setter
    def FrequencyRangeUpperBound(self, upper_bound: float):
        """
        Setter for property: (float) FrequencyRangeUpperBound
         Returns the upper bound frequency   
            
         
        """
        pass
    @property
    def InheritFrequencyRangeFromFunction(self) -> bool:
        """
        Getter for property: (bool) InheritFrequencyRangeFromFunction
         Returns the option to inherit frequency Range from function   
            
         
        """
        pass
    @InheritFrequencyRangeFromFunction.setter
    def InheritFrequencyRangeFromFunction(self, inherit_from_function: bool):
        """
        Setter for property: (bool) InheritFrequencyRangeFromFunction
         Returns the option to inherit frequency Range from function   
            
         
        """
        pass
    @property
    def InitialAccelerationX(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InitialAccelerationX
         Returns the initial acceleration X   
            
         
        """
        pass
    @property
    def InitialAccelerationY(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InitialAccelerationY
         Returns the initial acceleration Y   
            
         
        """
        pass
    @property
    def InitialAccelerationZ(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InitialAccelerationZ
         Returns the initial acceleration Z  
            
         
        """
        pass
    @property
    def InitialDisplacementX(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InitialDisplacementX
         Returns the inital X Displacement   
            
         
        """
        pass
    @property
    def InitialDisplacementY(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InitialDisplacementY
         Returns the inital Y Displacement   
            
         
        """
        pass
    @property
    def InitialDisplacementZ(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InitialDisplacementZ
         Returns the inital Z Displacement   
            
         
        """
        pass
    @property
    def InitialUserDefDirAcceleration(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InitialUserDefDirAcceleration
         Returns the inital user defined direction Acceleration   
            
         
        """
        pass
    @property
    def InitialUserDefDirDisplacement(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InitialUserDefDirDisplacement
         Returns the inital user defined direction Displacement   
            
         
        """
        pass
    @property
    def InitialUserDefDirVelocity(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InitialUserDefDirVelocity
         Returns the inital user defined direction Velocity   
            
         
        """
        pass
    @property
    def InitialVelocityX(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InitialVelocityX
         Returns the initial velocity X   
            
         
        """
        pass
    @property
    def InitialVelocityY(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InitialVelocityY
         Returns the initial velocity Y   
            
         
        """
        pass
    @property
    def InitialVelocityZ(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InitialVelocityZ
         Returns the initial velocity Z   
            
         
        """
        pass
    @property
    def UserSpecifiedInitialExcitationConditionsToggle(self) -> bool:
        """
        Getter for property: (bool) UserSpecifiedInitialExcitationConditionsToggle
         Returns the user specified initial excitation conditions toggle   
            
         
        """
        pass
    @UserSpecifiedInitialExcitationConditionsToggle.setter
    def UserSpecifiedInitialExcitationConditionsToggle(self, initial_conditions_toggle: bool):
        """
        Setter for property: (bool) UserSpecifiedInitialExcitationConditionsToggle
         Returns the user specified initial excitation conditions toggle   
            
         
        """
        pass
class NodalFunctionExcitation(Excitation): 
    """ Represents the abstract class of nodal function excitation """
    class Type(Enum):
        """
        Members Include: 
         |NodalForce|   
         |EnforcedMotion|   

        """
        NodalForce: int
        EnforcedMotion: int
        @staticmethod
        def ValueOf(value: int) -> NodalFunctionExcitation.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
import NXOpen
class NormalMode(NXOpen.NXObject): 
    """ Represents the properties of one normal mode """
    @property
    def Active(self) -> bool:
        """
        Getter for property: (bool) Active
         Returns the activate status   
            
         
        """
        pass
    @Active.setter
    def Active(self, active: bool):
        """
        Setter for property: (bool) Active
         Returns the activate status   
            
         
        """
        pass
    @property
    def Hysteretic(self) -> float:
        """
        Getter for property: (float) Hysteretic
         Returns the hysteretic factor   
            
         
        """
        pass
    @Hysteretic.setter
    def Hysteretic(self, hysteretic: float):
        """
        Setter for property: (float) Hysteretic
         Returns the hysteretic factor   
            
         
        """
        pass
    @property
    def Viscous(self) -> float:
        """
        Getter for property: (float) Viscous
         Returns the viscous factor   
            
         
        """
        pass
    @Viscous.setter
    def Viscous(self, viscous: float):
        """
        Setter for property: (float) Viscous
         Returns the viscous factor   
            
         
        """
        pass
    def GetFrequency(self) -> float:
        """
         Returns the natrual frequency of the normal mode 
         Returns frequency (float):  .
        """
        pass
    def GetMass(self) -> float:
        """
         Returns the mass of the normal mode 
         Returns mass (float):  .
        """
        pass
    def GetModeId(self) -> int:
        """
         Returns mode ID 
         Returns mode_id (int):  .
        """
        pass
    def GetPhysicalHysteretic(self) -> float:
        """
         Returns the physical hysteretic factor 
         Returns physical_hysteretic (float):  .
        """
        pass
    def GetPhysicalViscous(self) -> float:
        """
         Returns the physical viscous factor 
         Returns physical_viscous (float):  .
        """
        pass
    def GetRxMass(self) -> float:
        """
         Returns the percent mass of Rx direction component 
         Returns rx_mass (float):  .
        """
        pass
    def GetRyMass(self) -> float:
        """
         Returns the percent mass of Ry direction component 
         Returns ry_mass (float):  .
        """
        pass
    def GetRzMass(self) -> float:
        """
         Returns the percent mass of Rz direction component 
         Returns rz_mass (float):  .
        """
        pass
    def GetStiffeness(self) -> float:
        """
         Returns the stiffeness of the normal mode 
         Returns stiffeness (float):  .
        """
        pass
    def GetXMass(self) -> float:
        """
         Returns the percent mass of X direction component 
         Returns x_mass (float):  .
        """
        pass
    def GetYMass(self) -> float:
        """
         Returns the percent mass of Y direction component 
         Returns y_mass (float):  .
        """
        pass
    def GetZMass(self) -> float:
        """
         Returns the percent mass of Z direction component 
         Returns z_mass (float):  .
        """
        pass
import NXOpen
class ObjectLabel(NXOpen.TaggedObject): 
    """ Represents the setting to label an object. Includes name and description """
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the object name   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the object name   
            
         
        """
        pass
    def GetDescriptions(self) -> List[str]:
        """
         Returns the description for the object 
         Returns description (List[str]):  .
        """
        pass
    def SetDescriptions(self, description: List[str]) -> None:
        """
         Sets the description for the object 
        """
        pass
class PeakValueEvaluationSettingBuilder(PrlResultsEvaluationSettingBuilder): 
    """ This is a manager to the NXOpen.CAE.ResponseSimulation.PeakValueEvaluationSetting class. 
    Object of type NXOpen.CAE.ResponseSimulation.PeakValueEvaluationSetting can be 
    created and edited only through this class
     """
    @property
    def CombinationOptions(self) -> CombinationEvaluationOptions:
        """
        Getter for property: ( CombinationEvaluationOptions NXOpen.CAE.Res) CombinationOptions
         Returns the setting of combination evaluation.  
           Only available when event type is
                 NXOpen::CAE::ResponseSimulation::RSEvent::TypeRandom  or
                 NXOpen::CAE::ResponseSimulation::RSEvent::TypeResponseSpectrum   
         
        """
        pass
class PeakValueEvaluationSetting(PrlResultsEvaluationSetting): 
    """ Represents the parameters setting of peak value evaluation. Only NOT available when
    event type is NXOpen.CAE.ResponseSimulation.RSEvent.Type.Random. For more information,
    see the Response Dynamics section of the Gateway Help """
    pass
import NXOpen
class PhysicalDampingSettings(NXOpen.TaggedObject): 
    """ Represents the physical damping settings for a response simulation meta solution """
    @property
    def PhysicalHystereticScalingFactor(self) -> float:
        """
        Getter for property: (float) PhysicalHystereticScalingFactor
         Returns the scaling factor for physical hysteretic damping   
            
         
        """
        pass
    @PhysicalHystereticScalingFactor.setter
    def PhysicalHystereticScalingFactor(self, scalingFactor: float):
        """
        Setter for property: (float) PhysicalHystereticScalingFactor
         Returns the scaling factor for physical hysteretic damping   
            
         
        """
        pass
    @property
    def PhysicalViscousScalingFactor(self) -> float:
        """
        Getter for property: (float) PhysicalViscousScalingFactor
         Returns the scaling factor for physical viscous damping   
            
         
        """
        pass
    @PhysicalViscousScalingFactor.setter
    def PhysicalViscousScalingFactor(self, scalingFactor: float):
        """
        Setter for property: (float) PhysicalViscousScalingFactor
         Returns the scaling factor for physical viscous damping   
            
         
        """
        pass
    @property
    def UsingPhysicalHysteretic(self) -> bool:
        """
        Getter for property: (bool) UsingPhysicalHysteretic
         Returns the usage setting for physical hysteretic damping   
            
         
        """
        pass
    @UsingPhysicalHysteretic.setter
    def UsingPhysicalHysteretic(self, usingPhysicalHysteretic: bool):
        """
        Setter for property: (bool) UsingPhysicalHysteretic
         Returns the usage setting for physical hysteretic damping   
            
         
        """
        pass
    @property
    def UsingPhysicalViscous(self) -> bool:
        """
        Getter for property: (bool) UsingPhysicalViscous
         Returns the usage setting for physical viscous damping   
            
         
        """
        pass
    @UsingPhysicalViscous.setter
    def UsingPhysicalViscous(self, usingPhysicalViscous: bool):
        """
        Setter for property: (bool) UsingPhysicalViscous
         Returns the usage setting for physical viscous damping   
            
         
        """
        pass
import NXOpen.CAE
class PrlResultsEvaluationSettingBuilder(DynamicResultEvaluationSettingBuilder): 
    """ Represents the abstract builder class of evaluation setting for peak value, RMS results
    and LCR results. """
    @property
    def CoordinateSystem(self) -> CoordinateSystem:
        """
        Getter for property: ( CoordinateSystem NXOpen.CAE.Res) CoordinateSystem
         Returns the coordinate system.  
           Only available when the result type is 
                 NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStress ,
                 NXOpen::CAE::ResponseSimulation::EvaluationResultTypeShellResultant 
                  
         
        """
        pass
    @CoordinateSystem.setter
    def CoordinateSystem(self, coordinate_system: CoordinateSystem):
        """
        Setter for property: ( CoordinateSystem NXOpen.CAE.Res) CoordinateSystem
         Returns the coordinate system.  
           Only available when the result type is 
                 NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStress ,
                 NXOpen::CAE::ResponseSimulation::EvaluationResultTypeShellResultant 
                  
         
        """
        pass
    @property
    def ObservationNode(self) -> NXOpen.CAE.FENode:
        """
        Getter for property: ( NXOpen.CAE.FENode) ObservationNode
         Returns the relative node.  
          Only available when result type is 
                 NXOpen::CAE::ResponseSimulation::EvaluationResultTypeDisplacement ,
                 NXOpen::CAE::ResponseSimulation::EvaluationResultTypeAcceleration ,
                 NXOpen::CAE::ResponseSimulation::EvaluationResultTypeElementForce 
                  
         
        """
        pass
    @ObservationNode.setter
    def ObservationNode(self, relative_node: NXOpen.CAE.FENode):
        """
        Setter for property: ( NXOpen.CAE.FENode) ObservationNode
         Returns the relative node.  
          Only available when result type is 
                 NXOpen::CAE::ResponseSimulation::EvaluationResultTypeDisplacement ,
                 NXOpen::CAE::ResponseSimulation::EvaluationResultTypeAcceleration ,
                 NXOpen::CAE::ResponseSimulation::EvaluationResultTypeElementForce 
                  
         
        """
        pass
    @property
    def Relative(self) -> bool:
        """
        Getter for property: (bool) Relative
         Returns the option of using the observation node in evaluation
                  
            
         
        """
        pass
    @Relative.setter
    def Relative(self, relative: bool):
        """
        Setter for property: (bool) Relative
         Returns the option of using the observation node in evaluation
                  
            
         
        """
        pass
    @property
    def ResultType(self) -> EvaluationResultType:
        """
        Getter for property: ( EvaluationResultType NXOpen.CAE.Res) ResultType
         Returns the result type   
            
         
        """
        pass
    @ResultType.setter
    def ResultType(self, result_type: EvaluationResultType):
        """
        Setter for property: ( EvaluationResultType NXOpen.CAE.Res) ResultType
         Returns the result type   
            
         
        """
        pass
    @property
    def SpringForceEvaluationFromDisplacement(self) -> bool:
        """
        Getter for property: (bool) SpringForceEvaluationFromDisplacement
         Returns the spring force evaluation from displacement flag.  
             
         
        """
        pass
    @SpringForceEvaluationFromDisplacement.setter
    def SpringForceEvaluationFromDisplacement(self, spring_force_evaluation_from_displacement: bool):
        """
        Setter for property: (bool) SpringForceEvaluationFromDisplacement
         Returns the spring force evaluation from displacement flag.  
             
         
        """
        pass
    def GetDataComponents(self) -> List[DirectionDataComponent]:
        """
         Returns the direction data components. The condidate choices will be changed according to 
                NXOpen.CAE.ResponseSimulation.EvaluationResultType setting
                
         Returns data_component ( DirectionDataComponent List[NXOpen.CAE.R):  .
        """
        pass
    def GetOutputElements(self) -> List[NXOpen.CAE.FEElement]:
        """
         Returns the destination elements. Only available when the result type is 
                NXOpen.CAE.ResponseSimulation.EvaluationResultType.Stress,
                NXOpen.CAE.ResponseSimulation.EvaluationResultType.ShellResultant
                
         Returns destination_elements ( NXOpen.CAE.FEElement Li):  .
        """
        pass
    def GetOutputNodes(self) -> List[NXOpen.CAE.FENode]:
        """
         Returns the destination nodes. Only available when result type is 
                NXOpen.CAE.ResponseSimulation.EvaluationResultType.Displacement,
                NXOpen.CAE.ResponseSimulation.EvaluationResultType.Acceleration,
                NXOpen.CAE.ResponseSimulation.EvaluationResultType.ElementForce
                
         Returns destination_nodes ( NXOpen.CAE.FENode Li):  .
        """
        pass
    def SetDataComponents(self, data_component: List[DirectionDataComponent]) -> None:
        """
         Sets the direction data components. The condidate choices will be changed according to 
                NXOpen.CAE.ResponseSimulation.EvaluationResultType setting
                
        """
        pass
    def SetOutputElements(self, destination_elements: List[NXOpen.CAE.FEElement]) -> None:
        """
         Sets the destination elements 
        """
        pass
    def SetOutputNodes(self, destination_nodes: List[NXOpen.CAE.FENode]) -> None:
        """
         Sets the destination nodes 
        """
        pass
class PrlResultsEvaluationSetting(DynamicResultEvaluationSetting): 
    """ Represents the abstract class of evaluation setting for peak value, RMS results
    and LCR results. """
    pass
class ResponseDomainDefinitionMethod(Enum):
    """
    Members Include: 
     |StartEndPoint|  
     |KeyIn|  
     |NaturalFrequency|  

    """
    StartEndPoint: int
    KeyIn: int
    NaturalFrequency: int
    @staticmethod
    def ValueOf(value: int) -> ResponseDomainDefinitionMethod:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen.CAE
class ResponseResultsEvaluationSettingBuilder(DynamicResultEvaluationSettingBuilder): 
    """ This is a manager to the NXOpen.CAE.ResponseSimulation.ResponseResultsEvaluationSetting class. 
    Object of type NXOpen.CAE.ResponseSimulation.ResponseResultsEvaluationSetting can be 
    created and edited only through this class
     """
    @property
    def DecimationOrder(self) -> int:
        """
        Getter for property: (int) DecimationOrder
         Returns the decimation order of domain setting.  
           Only available when response domain is
                  CAE::ResponseSimulation::ResponseDomainDefinitionMethodStartEndPoint    
         
        """
        pass
    @DecimationOrder.setter
    def DecimationOrder(self, decimation_order: int):
        """
        Setter for property: (int) DecimationOrder
         Returns the decimation order of domain setting.  
           Only available when response domain is
                  CAE::ResponseSimulation::ResponseDomainDefinitionMethodStartEndPoint    
         
        """
        pass
    @property
    def EndPoint(self) -> float:
        """
        Getter for property: (float) EndPoint
         Returns the end value of domain setting.  
           Only available when response domain is 
                  CAE::ResponseSimulation::ResponseDomainDefinitionMethodStartEndPoint    
         
        """
        pass
    @EndPoint.setter
    def EndPoint(self, end_point: float):
        """
        Setter for property: (float) EndPoint
         Returns the end value of domain setting.  
           Only available when response domain is 
                  CAE::ResponseSimulation::ResponseDomainDefinitionMethodStartEndPoint    
         
        """
        pass
    @property
    def PointValue(self) -> float:
        """
        Getter for property: (float) PointValue
         Returns the method choosed to define select point value.  
           Only available when response domain is 
                  CAE::ResponseSimulation::ResponseDomainDefinitionMethodKeyIn    
         
        """
        pass
    @PointValue.setter
    def PointValue(self, point_value: float):
        """
        Setter for property: (float) PointValue
         Returns the method choosed to define select point value.  
           Only available when response domain is 
                  CAE::ResponseSimulation::ResponseDomainDefinitionMethodKeyIn    
         
        """
        pass
    @property
    def ResponseDomainDefinitionOption(self) -> ResponseDomainDefinitionMethod:
        """
        Getter for property: ( ResponseDomainDefinitionMethod NXOpen.CAE.Res) ResponseDomainDefinitionOption
         Returns the method choosed to define response domain   
            
         
        """
        pass
    @ResponseDomainDefinitionOption.setter
    def ResponseDomainDefinitionOption(self, definitions_method: ResponseDomainDefinitionMethod):
        """
        Setter for property: ( ResponseDomainDefinitionMethod NXOpen.CAE.Res) ResponseDomainDefinitionOption
         Returns the method choosed to define response domain   
            
         
        """
        pass
    @property
    def SpringForceEvaluationFromDisplacement(self) -> bool:
        """
        Getter for property: (bool) SpringForceEvaluationFromDisplacement
         Returns the spring force evaluation from displacement flag.  
             
         
        """
        pass
    @SpringForceEvaluationFromDisplacement.setter
    def SpringForceEvaluationFromDisplacement(self, spring_force_evaluation_from_displacement: bool):
        """
        Setter for property: (bool) SpringForceEvaluationFromDisplacement
         Returns the spring force evaluation from displacement flag.  
             
         
        """
        pass
    @property
    def StartPoint(self) -> float:
        """
        Getter for property: (float) StartPoint
         Returns the start value of domain setting.  
           Only available when response domain is 
                  CAE::ResponseSimulation::ResponseDomainDefinitionMethodStartEndPoint    
         
        """
        pass
    @StartPoint.setter
    def StartPoint(self, start_point: float):
        """
        Setter for property: (float) StartPoint
         Returns the start value of domain setting.  
           Only available when response domain is 
                  CAE::ResponseSimulation::ResponseDomainDefinitionMethodStartEndPoint    
         
        """
        pass
    def GetDestinationElements(self) -> List[NXOpen.CAE.FEElement]:
        """
         Returns the destination elements 
         Returns destination_elements ( NXOpen.CAE.FEElement Li):  .
        """
        pass
    def GetDestinationNodes(self) -> List[NXOpen.CAE.FENode]:
        """
         Returns the destination nodes 
         Returns destination_nodes ( NXOpen.CAE.FENode Li):  .
        """
        pass
    def GetOutputOptions(self) -> List[EvaluationResultType]:
        """
         Returns the output options 
         Returns output_options ( EvaluationResultType List[NXOpen.CAE.R):  .
        """
        pass
    def GetPointsValueList(self) -> List[float]:
        """
         Returns the points value list 
         Returns points_value_list (List[float]):  .
        """
        pass
    def SetDestinationElements(self, destination_element: List[NXOpen.CAE.FEElement]) -> None:
        """
         Sets the destination elements 
        """
        pass
    def SetDestinationNodes(self, destination_nodes: List[NXOpen.CAE.FENode]) -> None:
        """
         Sets the destination nodes 
        """
        pass
    def SetOutputOptions(self, output_options: List[EvaluationResultType]) -> None:
        """
         Sets the output options 
        """
        pass
    def SetPointsValueList(self, points_value_list: List[float]) -> None:
        """
         Sets the points value list 
        """
        pass
class ResponseResultsEvaluationSetting(DynamicResultEvaluationSetting): 
    """ Represents the parameters setting for response results evaluation. Only available when 
    event type are NXOpen.CAE.ResponseSimulation.RSEvent.Type.Transient and 
    NXOpen.CAE.ResponseSimulation.RSEvent.Type.Frequency. For more information, see the 
    Response Dynamics section of the Gateway Help """
    pass
class RmsLcrEvaluationMethod(Enum):
    """
    Members Include: 
     |SmallNumberItems|  Small number of evaluation items 
     |LargeNumberItems|  Large number of evaluation items 
     |AutomaticSelection|  Automatic selection 

    """
    SmallNumberItems: int
    LargeNumberItems: int
    AutomaticSelection: int
    @staticmethod
    def ValueOf(value: int) -> RmsLcrEvaluationMethod:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class RmsResultsEvaluationSettingBuilder(PrlResultsEvaluationSettingBuilder): 
    """ This is a manager to the NXOpen.CAE.ResponseSimulation.RmsResultsEvaluationSetting class.
    Object of type NXOpen.CAE.ResponseSimulation.RmsResultsEvaluationSetting can be
    created and edited only through this class
     """
    @property
    def EvaluationMethod(self) -> RmsLcrEvaluationMethod:
        """
        Getter for property: ( RmsLcrEvaluationMethod NXOpen.CAE.Res) EvaluationMethod
         Returns the evaluation method for RMS   
            
         
        """
        pass
    @EvaluationMethod.setter
    def EvaluationMethod(self, evaluationMethod: RmsLcrEvaluationMethod):
        """
        Setter for property: ( RmsLcrEvaluationMethod NXOpen.CAE.Res) EvaluationMethod
         Returns the evaluation method for RMS   
            
         
        """
        pass
class RmsResultsEvaluationSetting(PrlResultsEvaluationSetting): 
    """Represents the parameters setting for RMS results evaluation in response analysis. Only
    available when event type is NXOpen.CAE.ResponseSimulation.RSEvent.Type.Random """
    pass
class RotationalDDAMExcitationBuilder(DDAMExcitationBuilder): 
    """ Represents the manager to CAE.ResponseSimulation.DDAMExcitation.
     The object of type CAE.ResponseSimulation.DDAMExcitation can only
    be created or edited through this class. """
    pass
class RotationalDDAMExcitation(DDAMExcitation): 
    """ Represents an DDAM excitation. DDAM excitation could only be used by DDAM event. """
    pass
class RotationalNodalFunctionExcitationBuilder(NodalFunctionExcitationBuilder): 
    """ Represents the manager to NXOpen.CAE.ResponseSimulation.RotationalNodalFunctionExcitation. 
    The objects of NXOpen.CAE.ResponseSimulation.RotationalNodalFunctionExcitation 
    can be created or edited on through this class """
    @property
    def FunctionComponentRx(self) -> FunctionComponentData:
        """
        Getter for property: ( FunctionComponentData NXOpen.CAE.Res) FunctionComponentRx
         Returns the function component of Rx direction    
            
         
        """
        pass
    @property
    def FunctionComponentRy(self) -> FunctionComponentData:
        """
        Getter for property: ( FunctionComponentData NXOpen.CAE.Res) FunctionComponentRy
         Returns the function component of Ry direction   
            
         
        """
        pass
    @property
    def FunctionComponentRz(self) -> FunctionComponentData:
        """
        Getter for property: ( FunctionComponentData NXOpen.CAE.Res) FunctionComponentRz
         Returns the function component of Rz direction   
            
         
        """
        pass
class RotationalNodalFunctionExcitation(NodalFunctionExcitation): 
    """ Represents a rotational nodal function excitation """
    pass
import NXOpen
class RSDisplayObject(NXOpen.NXObject): 
    """  Represents a BC display attributes """
    @property
    def DisplayName(self) -> bool:
        """
        Getter for property: (bool) DisplayName
         Returns the truefalse flag based on whether the name of the BC is
                    displayed in the graphics window   
            
         
        """
        pass
    @DisplayName.setter
    def DisplayName(self, name_flag: bool):
        """
        Setter for property: (bool) DisplayName
         Returns the truefalse flag based on whether the name of the BC is
                    displayed in the graphics window   
            
         
        """
        pass
    @property
    def Scale(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Scale
         Returns the RS display scaling factor
                    this option specifies the scale of the graphic symbol relative to the size of the bounding box of the RS OBject.  
          
                    scale -\ 0 
                   
         
        """
        pass
import NXOpen
class RSEventAttributes(NXOpen.TaggedObject): 
    """ Represents all possible attributes setting for response analysis event """
    @property
    def AnalysisType(self) -> RSEvent.AnalysisType:
        """
        Getter for property: ( RSEvent.AnalysisType NXOpen.CAE.Res) AnalysisType
         Returns the analysis type.  
           Only available for transient event and frequency event   
         
        """
        pass
    @AnalysisType.setter
    def AnalysisType(self, analysis_type: RSEvent.AnalysisType):
        """
        Setter for property: ( RSEvent.AnalysisType NXOpen.CAE.Res) AnalysisType
         Returns the analysis type.  
           Only available for transient event and frequency event   
         
        """
        pass
    @property
    def CoefficientDefinitionMethod(self) -> DDAMExcitation.CoefficientDefinitionType:
        """
        Getter for property: ( DDAMExcitation.CoefficientDefinitionType NXOpen.CAE.Res) CoefficientDefinitionMethod
         Returns the DDAM coefficient definition method   
            
         
        """
        pass
    @CoefficientDefinitionMethod.setter
    def CoefficientDefinitionMethod(self, definition_method: DDAMExcitation.CoefficientDefinitionType):
        """
        Setter for property: ( DDAMExcitation.CoefficientDefinitionType NXOpen.CAE.Res) CoefficientDefinitionMethod
         Returns the DDAM coefficient definition method   
            
         
        """
        pass
    @property
    def CoefficientFile(self) -> str:
        """
        Getter for property: (str) CoefficientFile
         Returns the DDAM coefficients definition file.  
           Only available when event type is
                 CAE::ResponseSimulation::DDAMExcitation::CoefficientDefinitionTypeByFile .   
         
        """
        pass
    @CoefficientFile.setter
    def CoefficientFile(self, coefficient_file: str):
        """
        Setter for property: (str) CoefficientFile
         Returns the DDAM coefficients definition file.  
           Only available when event type is
                 CAE::ResponseSimulation::DDAMExcitation::CoefficientDefinitionTypeByFile .   
         
        """
        pass
    @property
    def Duration(self) -> float:
        """
        Getter for property: (float) Duration
         Returns the time duration in second for transient event   
            
         
        """
        pass
    @Duration.setter
    def Duration(self, duration: float):
        """
        Setter for property: (float) Duration
         Returns the time duration in second for transient event   
            
         
        """
        pass
    @property
    def DurationOption(self) -> RSEvent.DurationOption:
        """
        Getter for property: ( RSEvent.DurationOption NXOpen.CAE.Res) DurationOption
         Returns the time duration optionin option for transient event   
            
         
        """
        pass
    @DurationOption.setter
    def DurationOption(self, duration_option: RSEvent.DurationOption):
        """
        Setter for property: ( RSEvent.DurationOption NXOpen.CAE.Res) DurationOption
         Returns the time duration optionin option for transient event   
            
         
        """
        pass
    @property
    def FastRmsMethod(self) -> bool:
        """
        Getter for property: (bool) FastRmsMethod
         Returns the Use Fast RMS Method.  
           Only available when event type is
                 CAE::ResponseSimulation::RSEvent::TypeRandom ,
                  
         
        """
        pass
    @FastRmsMethod.setter
    def FastRmsMethod(self, fast_rms_method: bool):
        """
        Setter for property: (bool) FastRmsMethod
         Returns the Use Fast RMS Method.  
           Only available when event type is
                 CAE::ResponseSimulation::RSEvent::TypeRandom ,
                  
         
        """
        pass
    @property
    def Formulation(self) -> RSEvent.DdamFormulationType:
        """
        Getter for property: ( RSEvent.DdamFormulationType NXOpen.CAE.Res) Formulation
         Returns the DDAM formulation type  
            
         
        """
        pass
    @Formulation.setter
    def Formulation(self, formulation: RSEvent.DdamFormulationType):
        """
        Setter for property: ( RSEvent.DdamFormulationType NXOpen.CAE.Res) Formulation
         Returns the DDAM formulation type  
            
         
        """
        pass
    @property
    def InterpolationMethod(self) -> InterpolationMethod:
        """
        Getter for property: ( InterpolationMethod NXOpen.CAE.Res) InterpolationMethod
         Returns the interpolation method.  
           only available when event type is
                 CAE::ResponseSimulation::RSEvent::TypeFrequency ,
                 CAE::ResponseSimulation::RSEvent::TypeRandom , 
                 CAE::ResponseSimulation::RSEvent::TypeResponseSpectrum ,
                  
         
        """
        pass
    @InterpolationMethod.setter
    def InterpolationMethod(self, interpolation_method: InterpolationMethod):
        """
        Setter for property: ( InterpolationMethod NXOpen.CAE.Res) InterpolationMethod
         Returns the interpolation method.  
           only available when event type is
                 CAE::ResponseSimulation::RSEvent::TypeFrequency ,
                 CAE::ResponseSimulation::RSEvent::TypeRandom , 
                 CAE::ResponseSimulation::RSEvent::TypeResponseSpectrum ,
                  
         
        """
        pass
    @property
    def MinimumGValue(self) -> float:
        """
        Getter for property: (float) MinimumGValue
         Returns the Minimum G value   
            
         
        """
        pass
    @MinimumGValue.setter
    def MinimumGValue(self, minimumG: float):
        """
        Setter for property: (float) MinimumGValue
         Returns the Minimum G value   
            
         
        """
        pass
    @property
    def MountingType(self) -> DDAMExcitation.MountingType:
        """
        Getter for property: ( DDAMExcitation.MountingType NXOpen.CAE.Res) MountingType
         Returns the ship type  
            
         
        """
        pass
    @MountingType.setter
    def MountingType(self, mounting_type: DDAMExcitation.MountingType):
        """
        Setter for property: ( DDAMExcitation.MountingType NXOpen.CAE.Res) MountingType
         Returns the ship type  
            
         
        """
        pass
    @property
    def ResponseType(self) -> DDAMExcitation.ResponseType:
        """
        Getter for property: ( DDAMExcitation.ResponseType NXOpen.CAE.Res) ResponseType
         Returns the DDAM response type  
            
         
        """
        pass
    @ResponseType.setter
    def ResponseType(self, response_type: DDAMExcitation.ResponseType):
        """
        Setter for property: ( DDAMExcitation.ResponseType NXOpen.CAE.Res) ResponseType
         Returns the DDAM response type  
            
         
        """
        pass
    @property
    def ShipType(self) -> DDAMExcitation.ShipType:
        """
        Getter for property: ( DDAMExcitation.ShipType NXOpen.CAE.Res) ShipType
         Returns the ship type  
            
         
        """
        pass
    @ShipType.setter
    def ShipType(self, ship_type: DDAMExcitation.ShipType):
        """
        Setter for property: ( DDAMExcitation.ShipType NXOpen.CAE.Res) ShipType
         Returns the ship type  
            
         
        """
        pass
    @property
    def Spacing(self) -> RSEvent.SpacingType:
        """
        Getter for property: ( RSEvent.SpacingType NXOpen.CAE.Res) Spacing
         Returns the spacing type  
            
         
        """
        pass
    @Spacing.setter
    def Spacing(self, spacing: RSEvent.SpacingType):
        """
        Setter for property: ( RSEvent.SpacingType NXOpen.CAE.Res) Spacing
         Returns the spacing type  
            
         
        """
        pass
    @property
    def SpectralLines(self) -> int:
        """
        Getter for property: (int) SpectralLines
         Returns the spectral lines setting.  
           Only available when event type is
                 CAE::ResponseSimulation::RSEvent::TypeFrequency ,
                 CAE::ResponseSimulation::RSEvent::TypeRandom ,
                 CAE::ResponseSimulation::RSEvent::TypeResponseSpectrum ,
                  
         
        """
        pass
    @SpectralLines.setter
    def SpectralLines(self, spectral_lines: int):
        """
        Setter for property: (int) SpectralLines
         Returns the spectral lines setting.  
           Only available when event type is
                 CAE::ResponseSimulation::RSEvent::TypeFrequency ,
                 CAE::ResponseSimulation::RSEvent::TypeRandom ,
                 CAE::ResponseSimulation::RSEvent::TypeResponseSpectrum ,
                  
         
        """
        pass
class RSEventBuilder(BaseBuilder): 
    """ Represents the manager of CAE.ResponseSimulation.RSEvent. 
    The object of type NXOpen.CAE.ResponseSimulation.RSEvent can be 
    created or deleted only through this class. """
    @property
    def Attributes(self) -> RSEventAttributes:
        """
        Getter for property: ( RSEventAttributes NXOpen.CAE.Res) Attributes
         Returns the attributes setting   
            
         
        """
        pass
    @property
    def EventParameters(self) -> RSEventParameters:
        """
        Getter for property: ( RSEventParameters NXOpen.CAE.Res) EventParameters
         Returns the random base excitation event parameters   
            
         
        """
        pass
    @property
    def EventType(self) -> RSEvent.Type:
        """
        Getter for property: ( RSEvent.Type NXOpen.CAE.Res) EventType
         Returns the event type   
            
         
        """
        pass
    @EventType.setter
    def EventType(self, event_type: RSEvent.Type):
        """
        Setter for property: ( RSEvent.Type NXOpen.CAE.Res) EventType
         Returns the event type   
            
         
        """
        pass
    @property
    def InitialConditions(self) -> InitialConditions:
        """
        Getter for property: ( InitialConditions NXOpen.CAE.Res) InitialConditions
         Returns the initial condition setting.  
           Only available when event type is 
                 NXOpen::CAE::ResponseSimulation::RSEvent::TypeTransient    
         
        """
        pass
    @property
    def OutputSetting(self) -> RSEventOutputSetting:
        """
        Getter for property: ( RSEventOutputSetting NXOpen.CAE.Res) OutputSetting
         Returns the output setting   
            
         
        """
        pass
    @property
    def ResponseSimulationSolution(self) -> Solution:
        """
        Getter for property: ( Solution NXOpen.CAE.Res) ResponseSimulationSolution
         Returns the parent response simulation solution   
            
         
        """
        pass
import NXOpen
class RSEventCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of response analysis event """
    def CreateEventBuilder(self, ra_event: RSEvent) -> RSEventBuilder:
        """
         Creates a event buider 
         Returns builder ( RSEventBuilder NXOpen.CAE.Res):   .
        """
        pass
    def DeleteEvent(self, ra_event: RSEvent) -> None:
        """
         Deletes an event 
        """
        pass
    def FindObject(self, name: str) -> RSEvent:
        """
         Finds an event with specified event name 
         Returns ra_event ( RSEvent NXOpen.CAE.Res):   .
        """
        pass
import NXOpen
class RSEventOutputSetting(NXOpen.TaggedObject): 
    """ Reprensents the output setting for an event """
    @property
    def FemGeometrySaveOption(self) -> bool:
        """
        Getter for property: (bool) FemGeometrySaveOption
         Returns the option to save FEM information with evaluation results.  
           The option could not be
                changed after the event is created.   
         
        """
        pass
    @FemGeometrySaveOption.setter
    def FemGeometrySaveOption(self, save_fem_geometry: bool):
        """
        Setter for property: (bool) FemGeometrySaveOption
         Returns the option to save FEM information with evaluation results.  
           The option could not be
                changed after the event is created.   
         
        """
        pass
import NXOpen
import NXOpen.CAE
class RSEventParameters(NXOpen.TaggedObject): 
    """ Reprensents the parameters of the random base excitation event """
    @property
    def AmplitudeInterpMethod(self) -> RSEvent.InterpolationMethod:
        """
        Getter for property: ( RSEvent.InterpolationMethod NXOpen.CAE.Res) AmplitudeInterpMethod
         Returns the Amplitude interpolation method   
            
         
        """
        pass
    @AmplitudeInterpMethod.setter
    def AmplitudeInterpMethod(self, amplitude_interpolation_method: RSEvent.InterpolationMethod):
        """
        Setter for property: ( RSEvent.InterpolationMethod NXOpen.CAE.Res) AmplitudeInterpMethod
         Returns the Amplitude interpolation method   
            
         
        """
        pass
    @property
    def ConfidenceLevel(self) -> float:
        """
        Getter for property: (float) ConfidenceLevel
         Returns the confidence level value   
            
         
        """
        pass
    @ConfidenceLevel.setter
    def ConfidenceLevel(self, confidence_level: float):
        """
        Setter for property: (float) ConfidenceLevel
         Returns the confidence level value   
            
         
        """
        pass
    @property
    def ConfidenceLevelOption(self) -> RSEvent.ConfidenceLevelOption:
        """
        Getter for property: ( RSEvent.ConfidenceLevelOption NXOpen.CAE.Res) ConfidenceLevelOption
         Returns the confidence level option   
            
         
        """
        pass
    @ConfidenceLevelOption.setter
    def ConfidenceLevelOption(self, confidence_level_option: RSEvent.ConfidenceLevelOption):
        """
        Setter for property: ( RSEvent.ConfidenceLevelOption NXOpen.CAE.Res) ConfidenceLevelOption
         Returns the confidence level option   
            
         
        """
        pass
    @property
    def FrequencyInterpMethod(self) -> RSEvent.InterpolationMethod:
        """
        Getter for property: ( RSEvent.InterpolationMethod NXOpen.CAE.Res) FrequencyInterpMethod
         Returns the Frequency interpolation method   
            
         
        """
        pass
    @FrequencyInterpMethod.setter
    def FrequencyInterpMethod(self, frequency_interpolation_method: RSEvent.InterpolationMethod):
        """
        Setter for property: ( RSEvent.InterpolationMethod NXOpen.CAE.Res) FrequencyInterpMethod
         Returns the Frequency interpolation method   
            
         
        """
        pass
    @property
    def FrequencyOutputRequestObject(self) -> NXOpen.CAE.ModelingObjectPropertyTable:
        """
        Getter for property: ( NXOpen.CAE.ModelingObjectPropertyTable) FrequencyOutputRequestObject
         Returns the Frequency output request modeling object   
            
         
        """
        pass
    @FrequencyOutputRequestObject.setter
    def FrequencyOutputRequestObject(self, ssmo: NXOpen.CAE.ModelingObjectPropertyTable):
        """
        Setter for property: ( NXOpen.CAE.ModelingObjectPropertyTable) FrequencyOutputRequestObject
         Returns the Frequency output request modeling object   
            
         
        """
        pass
    @property
    def OutputRequestObject(self) -> NXOpen.CAE.ModelingObjectPropertyTable:
        """
        Getter for property: ( NXOpen.CAE.ModelingObjectPropertyTable) OutputRequestObject
         Returns the output request modeling object   
            
         
        """
        pass
    @OutputRequestObject.setter
    def OutputRequestObject(self, ssmo: NXOpen.CAE.ModelingObjectPropertyTable):
        """
        Setter for property: ( NXOpen.CAE.ModelingObjectPropertyTable) OutputRequestObject
         Returns the output request modeling object   
            
         
        """
        pass
    @property
    def RandomOutputRequestObject(self) -> NXOpen.CAE.ModelingObjectPropertyTable:
        """
        Getter for property: ( NXOpen.CAE.ModelingObjectPropertyTable) RandomOutputRequestObject
         Returns the Random output request modeling object   
            
         
        """
        pass
    @RandomOutputRequestObject.setter
    def RandomOutputRequestObject(self, ssmo: NXOpen.CAE.ModelingObjectPropertyTable):
        """
        Setter for property: ( NXOpen.CAE.ModelingObjectPropertyTable) RandomOutputRequestObject
         Returns the Random output request modeling object   
            
         
        """
        pass
    @property
    def ReferenceType(self) -> RSEvent.ReferenceType:
        """
        Getter for property: ( RSEvent.ReferenceType NXOpen.CAE.Res) ReferenceType
         Returns the confidence level option   
            
         
        """
        pass
    @ReferenceType.setter
    def ReferenceType(self, reference_type: RSEvent.ReferenceType):
        """
        Setter for property: ( RSEvent.ReferenceType NXOpen.CAE.Res) ReferenceType
         Returns the confidence level option   
            
         
        """
        pass
    @property
    def SineOutputRequestObject(self) -> NXOpen.CAE.ModelingObjectPropertyTable:
        """
        Getter for property: ( NXOpen.CAE.ModelingObjectPropertyTable) SineOutputRequestObject
         Returns the Sine output request modeling object   
            
         
        """
        pass
    @SineOutputRequestObject.setter
    def SineOutputRequestObject(self, ssmo: NXOpen.CAE.ModelingObjectPropertyTable):
        """
        Setter for property: ( NXOpen.CAE.ModelingObjectPropertyTable) SineOutputRequestObject
         Returns the Sine output request modeling object   
            
         
        """
        pass
    @property
    def StandardDeviation(self) -> float:
        """
        Getter for property: (float) StandardDeviation
         Returns the standard deviation value   
            
         
        """
        pass
    @StandardDeviation.setter
    def StandardDeviation(self, standard_deviation: float):
        """
        Setter for property: (float) StandardDeviation
         Returns the standard deviation value   
            
         
        """
        pass
    @property
    def StaticContributions(self) -> bool:
        """
        Getter for property: (bool) StaticContributions
         Returns the residual vector static contribution   
            
         
        """
        pass
    @StaticContributions.setter
    def StaticContributions(self, static_ontributions: bool):
        """
        Setter for property: (bool) StaticContributions
         Returns the residual vector static contribution   
            
         
        """
        pass
import NXOpen
class RSEventSolverParameters(NXOpen.TaggedObject): 
    """ Represents a response analysis event """
    class DdamCoefficientType(Enum):
        """
        Members Include: 
         |Af|  
         |Vf|  
         |Aa|  
         |Ab|  
         |Ac|  
         |Ad|  
         |Va|  
         |Vb|  
         |Vc|  

        """
        Af: int
        Vf: int
        Aa: int
        Ab: int
        Ac: int
        Ad: int
        Va: int
        Vb: int
        Vc: int
        @staticmethod
        def ValueOf(value: int) -> RSEventSolverParameters.DdamCoefficientType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DdamCoefficientA(self) -> float:
        """
        Getter for property: (float) DdamCoefficientA
         Returns the DDAM A coefficient   
            
         
        """
        pass
    @DdamCoefficientA.setter
    def DdamCoefficientA(self, coefficientA: float):
        """
        Setter for property: (float) DdamCoefficientA
         Returns the DDAM A coefficient   
            
         
        """
        pass
    @property
    def DdamCoefficientV(self) -> float:
        """
        Getter for property: (float) DdamCoefficientV
         Returns the DDAM V coefficient   
            
         
        """
        pass
    @DdamCoefficientV.setter
    def DdamCoefficientV(self, coefficientV: float):
        """
        Setter for property: (float) DdamCoefficientV
         Returns the DDAM V coefficient   
            
         
        """
        pass
    def GetDdamCoefficient(self, coefficientType: RSEventSolverParameters.DdamCoefficientType) -> float:
        """
         Returns DDAM coefficient value of the specified type 
         Returns coefficient (float): .
        """
        pass
    def SetDdamCoefficient(self, coefficientType: RSEventSolverParameters.DdamCoefficientType, coefficient: float) -> None:
        """
         Sets the DDAM coefficient value of the specified type 
        """
        pass
import NXOpen
class RSEvent(NXOpen.NXObject): 
    """ Represents a response analysis event """
    class AnalysisType(Enum):
        """
        Members Include: 
         |ModeAcceleration|   
         |ModeDisplacement|   

        """
        ModeAcceleration: int
        ModeDisplacement: int
        @staticmethod
        def ValueOf(value: int) -> RSEvent.AnalysisType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ConfidenceLevelOption(Enum):
        """
        Members Include: 
         |UserDefined| 
         |StandardDeviations| 
         |Rms| 

        """
        UserDefined: int
        StandardDeviations: int
        Rms: int
        @staticmethod
        def ValueOf(value: int) -> RSEvent.ConfidenceLevelOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DdamFormulationType(Enum):
        """
        Members Include: 
         |Standard| 
         |UserDefined| 

        """
        Standard: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> RSEvent.DdamFormulationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DurationOption(Enum):
        """
        Members Include: 
         |ExcitationFunction|  
         |UserDefined| 

        """
        ExcitationFunction: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> RSEvent.DurationOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class InterpolationMethod(Enum):
        """
        Members Include: 
         |Log| 
         |Linear| 

        """
        Log: int
        Linear: int
        @staticmethod
        def ValueOf(value: int) -> RSEvent.InterpolationMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ReferenceType(Enum):
        """
        Members Include: 
         |Relative| 
         |Absolute| 

        """
        Relative: int
        Absolute: int
        @staticmethod
        def ValueOf(value: int) -> RSEvent.ReferenceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ResultFileType(Enum):
        """
        Members Include: 
         |ModalResponse|  Result file to be used as Restart File, which extension is ".eef" or ".sef" 
         |FunctionResponse|  Result file to contain function response evaluation results, which extenstion is ".afu" 
         |DynamicResponse|  Result file to contain dynamic response evaluation results, which extension is ".rs2" 
         |ContourFunctionResponse|  Result file to contain the contour and function results, which extension is ".op2 and .bun" 

        """
        ModalResponse: int
        FunctionResponse: int
        DynamicResponse: int
        ContourFunctionResponse: int
        @staticmethod
        def ValueOf(value: int) -> RSEvent.ResultFileType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SpacingType(Enum):
        """
        Members Include: 
         |Even|   
         |Uneven|   

        """
        Even: int
        Uneven: int
        @staticmethod
        def ValueOf(value: int) -> RSEvent.SpacingType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Type(Enum):
        """
        Members Include: 
         |Transient|   
         |Frequency|   
         |Random|   
         |ResponseSpectrum|   
         |Ddam|   
         |Static|   
         |RandomBaseExcitation|   
         |SineBaseExcitation|   

        """
        Transient: int
        Frequency: int
        Random: int
        ResponseSpectrum: int
        Ddam: int
        Static: int
        RandomBaseExcitation: int
        SineBaseExcitation: int
        @staticmethod
        def ValueOf(value: int) -> RSEvent.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def BaseExcitationEventSolve(self, runInBackground: bool) -> int:
        """
         Solve the Randome Base Excitation and the Sine Base Excitation events. The results is stored in an op2 file, which file name
                could be returned by NXOpen.CAE.ResponseSimulation.RSEvent.GetResultFileName 
         Returns pid (int):  Process id of the event solver run .
        """
        pass
    def BaseExcitationEventWriteBatchFile(self) -> None:
        """
         Write the batch file with the full command to run the solver from the command line for the Random Base Excitation and the Sine Base Excitation events. 
        """
        pass
    def BaseExcitationEventWriteInputFile(self) -> None:
        """
         Write the solver input xml file of the Random Base Excitation and the Sine Base Excitation events. 
        """
        pass
    def CheckObsoleteStatus(self) -> None:
        """
         Check the obsolete status of the event. 
        """
        pass
    def DeleteResultFiles(self, result_file_type: RSEvent.ResultFileType) -> None:
        """
         Deletes all result files of the event. 
        """
        pass
    def Destroy(self, deleteResultFile: bool) -> None:
        """
         Deletes a response simulation dynamic event, including all excitations
                    under it 
        """
        pass
    def EvaluateCsd(self, evaluation_setting: CsdEvaluationSetting) -> None:
        """
         Performs evaluation for CSD. The evaluation results will be stored in an AFU file, 
                which name could be returned by NXOpen.CAE.ResponseSimulation.RSEvent.GetResultFileName 
        """
        pass
    def EvaluateElementalFunctionResponse(self, evaluation_setting: ElementalFunctionEvaluationSetting) -> None:
        """
         Performs evaluation for elemental function response. The results is stored in an AFU file, which file name
                could be returned by NXOpen.CAE.ResponseSimulation.RSEvent.GetResultFileName 
        """
        pass
    def EvaluateLcrResults(self, evaluation_setting: LcrResultsEvaluationSetting) -> None:
        """
         Performs evaluation for LCR results. The results is stored in an RS2 file, which file name
                could be returned by NXOpen.CAE.ResponseSimulation.RSEvent.GetResultFileName 
        """
        pass
    def EvaluateModalFunctionResponse(self) -> None:
        """
         Performs evaluation for modal function response. The results is stored in an AFU file, which file name
                could be returned by NXOpen.CAE.ResponseSimulation.RSEvent.GetResultFileName 
        """
        pass
    def EvaluateModalResponse(self) -> None:
        """
         Performs evaluation for modal response. The results is getting eef file, which file name
                could be returned by NXOpen.CAE.ResponseSimulation.RSEvent.GetResultFileName 
        """
        pass
    def EvaluateNodalFunctionResponse(self, evaluation_setting: NodalFunctionEvaluationSetting) -> None:
        """
         Performs evaluation for nodal function response. The results is stored in an AFU file, which file name
                could be returned by NXOpen.CAE.ResponseSimulation.RSEvent.GetResultFileName 
        """
        pass
    def EvaluatePeakValueResults(self, evaluation_setting: PeakValueEvaluationSetting) -> None:
        """
         Performs evaluation for peak value results. The results is stored in an RS2 file, which file name
                could be returned by NXOpen.CAE.ResponseSimulation.RSEvent.GetResultFileName.  
        """
        pass
    def EvaluateResponseResults(self, evaluation_setting: ResponseResultsEvaluationSetting) -> None:
        """
         Performs evaluation for response results. The results is stored in an RS2 file, which file name
                could be returned by NXOpen.CAE.ResponseSimulation.RSEvent.GetResultFileName.  
        """
        pass
    def EvaluateRmsResults(self, evaluation_setting: RmsResultsEvaluationSetting) -> None:
        """
         Perfroms evaluation for RMS results. The results is stored in an RS2 file, which file name
                could be returned by NXOpen.CAE.ResponseSimulation.RSEvent.GetResultFileName. 
        """
        pass
    @overload
    def EvaluateSensorResponse(self) -> None:
        """
         Performs evaluation for sensor response. The results is stored in an AFU file, which file name
                could be returned by NXOpen.CAE.ResponseSimulation.RSEvent.GetResultFileName 
        """
        pass
    @overload
    def EvaluateSensorResponse(self, evaluation_setting: SensorEvaluationSetting) -> None:
        """
         Performs evaluation for sensor response. The results is stored in an AFU file, which file name
                could be returned by NXOpen.CAE.ResponseSimulation.RSEvent.GetResultFileName 
        """
        pass
    def EvaluateStrainGageResponse(self, evaluation_setting: StrainGageEvaluationSetting) -> None:
        """
         Performs evaluation for strain gage response. The results is stored in an AFU file, which file name
                could be returned by NXOpen.CAE.ResponseSimulation.RSEvent.GetResultFileName 
        """
        pass
    def EvaluateStrengthResults(self, evaluation_setting: StrengthResultsEvaluationSetting) -> None:
        """
         Performs evaluation for strength results. The results is stored in an RS2 file, which file name
                could be returned by NXOpen.CAE.ResponseSimulation.RSEvent.GetResultFileName.  
        """
        pass
    def Export(self, event_definition_file: str) -> None:
        """
         Exports event definition to a XML file 
        """
        pass
    def GetCalculateStaticOffset(self) -> bool:
        """
         Returns the option setting for calculating static offset result.
                The staic offset calculation is only available to transient event 
         Returns calculateStaticOffset (bool):  .
        """
        pass
    def GetEventName(self) -> str:
        """
         Returns the event name 
         Returns eventName (str):  .
        """
        pass
    def GetExcitations(self) -> List[Excitation]:
        """
         Returns all excitations of an event 
         Returns excitations ( Excitation List[NXOpen.CAE.R):  .
        """
        pass
    def GetResultFileName(self, result_file_type: RSEvent.ResultFileType) -> str:
        """
         Returns result file name of specified type 
         Returns result_file_name (str):  .
        """
        pass
    def GetSolverParameters(self) -> RSEventSolverParameters:
        """
         Returns the solver parameters 
         Returns solver_parameters ( RSEventSolverParameters NXOpen.CAE.Res):  .
        """
        pass
    def LoadFunctionResults(self) -> bool:
        """
         Loads function results of the event. 
         Returns unitsMismatch (bool):  flag indicating if the output file unit system is valid .
        """
        pass
    def RbeEventSolve(self, runInBackground: bool) -> int:
        """
         Solve the Random Base Excitation Event. The results is stored in an op2 file, which file name
                could be returned by NXOpen.CAE.ResponseSimulation.RSEvent.GetResultFileName 
         Returns pid (int):  Process id of the event solver run .
        """
        pass
    def RbeEventWriteBatchFile(self) -> None:
        """
         Write the batch file with the full command to run the solver from the command line. 
        """
        pass
    def RbeEventWriteInputFile(self) -> None:
        """
         Write the solver input xml file of the Random Base Excitation Event. 
        """
        pass
    def SetCalculateStaticOffset(self, calculateStaticOffset: bool) -> None:
        """
         Set the option setting for calculating static offset result. The static offset calculation is
                only available to transient event 
        """
        pass
    def SetEventName(self, eventName: str, renameResultFile: bool) -> None:
        """
         Sets the event name 
        """
        pass
import NXOpen
import NXOpen.CAE
class SensorBuilder(BaseBuilder): 
    """ Represents a NXOpen.CAE.ResponseSimulation.SensorBuilder
     """
    @property
    def ReverseNormalDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseNormalDirection
         Returns the option for reverse the normal direction.  
           
                    Only available when the sensor type is
                     CAE::ResponseSimulation::SensorTypeNormal     
         
        """
        pass
    @ReverseNormalDirection.setter
    def ReverseNormalDirection(self, normal_direction: bool):
        """
        Setter for property: (bool) ReverseNormalDirection
         Returns the option for reverse the normal direction.  
           
                    Only available when the sensor type is
                     CAE::ResponseSimulation::SensorTypeNormal     
         
        """
        pass
    @property
    def SensorCoordinateType(self) -> SensorCoordinateType:
        """
        Getter for property: ( SensorCoordinateType NXOpen.CAE.Res) SensorCoordinateType
         Returns the sensor's coordinate type   
            
         
        """
        pass
    @SensorCoordinateType.setter
    def SensorCoordinateType(self, coordinate_type: SensorCoordinateType):
        """
        Setter for property: ( SensorCoordinateType NXOpen.CAE.Res) SensorCoordinateType
         Returns the sensor's coordinate type   
            
         
        """
        pass
    @property
    def SensorDirectionX(self) -> bool:
        """
        Getter for property: (bool) SensorDirectionX
         Returns the setting for x direction compontent of sensor.  
           
                    If true, the response on direction x will be calculated.
                    Only available when the sensor type is
                     CAE::ResponseSimulation::SensorTypeComponent     
         
        """
        pass
    @SensorDirectionX.setter
    def SensorDirectionX(self, direction_x: bool):
        """
        Setter for property: (bool) SensorDirectionX
         Returns the setting for x direction compontent of sensor.  
           
                    If true, the response on direction x will be calculated.
                    Only available when the sensor type is
                     CAE::ResponseSimulation::SensorTypeComponent     
         
        """
        pass
    @property
    def SensorDirectionY(self) -> bool:
        """
        Getter for property: (bool) SensorDirectionY
         Returns the setting for y direction compontent of sensor.  
           
                    If true, the response on direction y will be calculated.
                    Only available when the sensor type is
                     CAE::ResponseSimulation::SensorTypeComponent     
         
        """
        pass
    @SensorDirectionY.setter
    def SensorDirectionY(self, direction_y: bool):
        """
        Setter for property: (bool) SensorDirectionY
         Returns the setting for y direction compontent of sensor.  
           
                    If true, the response on direction y will be calculated.
                    Only available when the sensor type is
                     CAE::ResponseSimulation::SensorTypeComponent     
         
        """
        pass
    @property
    def SensorDirectionZ(self) -> bool:
        """
        Getter for property: (bool) SensorDirectionZ
         Returns the setting for z direction compontent of sensor.  
           
                    If true, the response on direction z will be calculated.
                    Only available when the sensor type is
                     CAE::ResponseSimulation::SensorTypeComponent     
         
        """
        pass
    @SensorDirectionZ.setter
    def SensorDirectionZ(self, direction_z: bool):
        """
        Setter for property: (bool) SensorDirectionZ
         Returns the setting for z direction compontent of sensor.  
           
                    If true, the response on direction z will be calculated.
                    Only available when the sensor type is
                     CAE::ResponseSimulation::SensorTypeComponent     
         
        """
        pass
    @property
    def SensorResultType(self) -> SensorResultType:
        """
        Getter for property: ( SensorResultType NXOpen.CAE.Res) SensorResultType
         Returns the sensor's result type   
            
         
        """
        pass
    @SensorResultType.setter
    def SensorResultType(self, result_type: SensorResultType):
        """
        Setter for property: ( SensorResultType NXOpen.CAE.Res) SensorResultType
         Returns the sensor's result type   
            
         
        """
        pass
    @property
    def SensorRotationX(self) -> bool:
        """
        Getter for property: (bool) SensorRotationX
         Returns the setting for x rotation compontent of sensor.  
           
                    If true, the response on rotation x will be calculated.
                    Only available when the sensor type is
                     CAE::ResponseSimulation::SensorTypeComponent     
         
        """
        pass
    @SensorRotationX.setter
    def SensorRotationX(self, rotation_x: bool):
        """
        Setter for property: (bool) SensorRotationX
         Returns the setting for x rotation compontent of sensor.  
           
                    If true, the response on rotation x will be calculated.
                    Only available when the sensor type is
                     CAE::ResponseSimulation::SensorTypeComponent     
         
        """
        pass
    @property
    def SensorRotationY(self) -> bool:
        """
        Getter for property: (bool) SensorRotationY
         Returns the setting for y rotation compontent of sensor.  
           
                    If true, the response on rotation y will be calculated.
                    Only available when the sensor type is
                     CAE::ResponseSimulation::SensorTypeComponent     
         
        """
        pass
    @SensorRotationY.setter
    def SensorRotationY(self, rotation_y: bool):
        """
        Setter for property: (bool) SensorRotationY
         Returns the setting for y rotation compontent of sensor.  
           
                    If true, the response on rotation y will be calculated.
                    Only available when the sensor type is
                     CAE::ResponseSimulation::SensorTypeComponent     
         
        """
        pass
    @property
    def SensorRotationZ(self) -> bool:
        """
        Getter for property: (bool) SensorRotationZ
         Returns the setting for z rotation compontent of sensor.  
           
                    If true, the response on rotation z will be calculated.
                    Only available when the sensor type is
                     CAE::ResponseSimulation::SensorTypeComponent     
         
        """
        pass
    @SensorRotationZ.setter
    def SensorRotationZ(self, rotation_z: bool):
        """
        Setter for property: (bool) SensorRotationZ
         Returns the setting for z rotation compontent of sensor.  
           
                    If true, the response on rotation z will be calculated.
                    Only available when the sensor type is
                     CAE::ResponseSimulation::SensorTypeComponent     
         
        """
        pass
    @property
    def SensorType(self) -> SensorType:
        """
        Getter for property: ( SensorType NXOpen.CAE.Res) SensorType
         Returns the sensor's type   
            
         
        """
        pass
    @SensorType.setter
    def SensorType(self, sensor_type: SensorType):
        """
        Setter for property: ( SensorType NXOpen.CAE.Res) SensorType
         Returns the sensor's type   
            
         
        """
        pass
    @property
    def SensorVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) SensorVector
         Returns the user defined direction.  
          
                    Only available when the sensor type is
                     CAE::ResponseSimulation::SensorTypeDirection    
         
        """
        pass
    @SensorVector.setter
    def SensorVector(self, sensor_vector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) SensorVector
         Returns the user defined direction.  
          
                    Only available when the sensor type is
                     CAE::ResponseSimulation::SensorTypeDirection    
         
        """
        pass
    def GetSelectedNodes(self) -> List[NXOpen.CAE.FENode]:
        """
         Returns the destination nodes 
         Returns destination_nodes ( NXOpen.CAE.FENode Li):  .
        """
        pass
    def SetSelectedNodes(self, destination_nodes: List[NXOpen.CAE.FENode]) -> None:
        """
         Sets the destination nodes 
        """
        pass
import NXOpen
class SensorCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of response analysis sensor """
    def CreateSensorBuilder(self, rs_sensor: Sensor) -> SensorBuilder:
        """
         Creates a sensor buider 
         Returns builder ( SensorBuilder NXOpen.CAE.Res):   .
        """
        pass
    def DeleteSensor(self, rs_sensor: Sensor) -> None:
        """
         Deletes an sensor 
        """
        pass
    def FindObject(self, name: str) -> Sensor:
        """
         Finds an sensor with specified event name 
         Returns sensor ( Sensor NXOpen.CAE.Res):   .
        """
        pass
class SensorCoordinateType(Enum):
    """
    Members Include: 
     |NodalCs|  
     |GlobalCs|  

    """
    NodalCs: int
    GlobalCs: int
    @staticmethod
    def ValueOf(value: int) -> SensorCoordinateType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class SensorEvaluationSettingBuilder(FunctionEvaluationSettingBuilder): 
    """ This is a manager to the NXOpen.CAE.ResponseSimulation.SensorEvaluationSetting class. 
        Object of type NXOpen.CAE.ResponseSimulation.SensorEvaluationSetting can be 
        created and edited only through this class
         """
    @property
    def Sensor(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) Sensor
         Returns the destination sensor   
            
         
        """
        pass
class SensorEvaluationSetting(DynamicResultEvaluationSetting): 
    """ Represents the parameters setting for sensor evaluation.  For more information, see the 
    Response Dynamics section of the Gateway Help """
    pass
class SensorResultType(Enum):
    """
    Members Include: 
     |Displacement|  
     |Velocity|  
     |Acceleration|  
     |ReactionForce|  

    """
    Displacement: int
    Velocity: int
    Acceleration: int
    ReactionForce: int
    @staticmethod
    def ValueOf(value: int) -> SensorResultType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class SensorType(Enum):
    """
    Members Include: 
     |Component|  
     |Direction|  
     |Normal|  

    """
    Component: int
    Direction: int
    Normal: int
    @staticmethod
    def ValueOf(value: int) -> SensorType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class Sensor(NXOpen.DisplayableObject): 
    """ Represents a NXOpen.CAE.ResponseSimulation.Sensor
     """
    def GetDisplayAttribute(self) -> RSDisplayObject:
        """
         Get display attribute of sensor 
         Returns display_attr ( RSDisplayObject NXOpen.CAE.Res):   .
        """
        pass
class ShellElementEvaluationLocation(Enum):
    """
    Members Include: 
     |Top|  
     |Middle|  
     |Bottom|  

    """
    Top: int
    Middle: int
    Bottom: int
    @staticmethod
    def ValueOf(value: int) -> ShellElementEvaluationLocation:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class SolutionAttributes(NXOpen.TaggedObject): 
    """ Represents attributes setting of response analysis meta solution """
    @property
    def RigidBodyToleranceExp(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RigidBodyToleranceExp
         Returns the tolerance expression   
            
         
        """
        pass
import NXOpen.CAE
class SolutionBuilder(BaseBuilder): 
    """ This is a manager to the NXOpen.CAE.ResponseSimulation.Solution class. 
    Object of type NXOpen.CAE.ResponseSimulation.Solution can be 
    created and edited only through this class
     """
    @property
    def Attributes(self) -> SolutionAttributes:
        """
        Getter for property: ( SolutionAttributes NXOpen.CAE.Res) Attributes
         Returns the attributes setting   
            
         
        """
        pass
    @property
    def ImportedEefFile(self) -> str:
        """
        Getter for property: (str) ImportedEefFile
         Returns the EEF file imported to create an imported response analysis meta solution.  
           There is 
                    event definition containing in the EEF file. An event will be created with the solution.
                    To the imported solution and event, the users can only perform evaluation and not able to
                    create new events and excitations
                   
         
        """
        pass
    @ImportedEefFile.setter
    def ImportedEefFile(self, imported_eef_file: str):
        """
        Setter for property: (str) ImportedEefFile
         Returns the EEF file imported to create an imported response analysis meta solution.  
           There is 
                    event definition containing in the EEF file. An event will be created with the solution.
                    To the imported solution and event, the users can only perform evaluation and not able to
                    create new events and excitations
                   
         
        """
        pass
    @property
    def ReferencedSolution(self) -> NXOpen.CAE.SimSolution:
        """
        Getter for property: ( NXOpen.CAE.SimSolution) ReferencedSolution
         Returns the referenced solution which must be a SEMODES 103 solution with modal results solved   
            
         
        """
        pass
    @ReferencedSolution.setter
    def ReferencedSolution(self, referenced_solution: NXOpen.CAE.SimSolution):
        """
        Setter for property: ( NXOpen.CAE.SimSolution) ReferencedSolution
         Returns the referenced solution which must be a SEMODES 103 solution with modal results solved   
            
         
        """
        pass
    @property
    def ScratchDir(self) -> str:
        """
        Getter for property: (str) ScratchDir
         Returns the scratch file is used for Response Dynamics Evaluations.  
           
                    The OP2,RS2,EEF file are processed in this area and copied to the original location as needed.
                   
         
        """
        pass
    @ScratchDir.setter
    def ScratchDir(self, scratch_dir: str):
        """
        Setter for property: (str) ScratchDir
         Returns the scratch file is used for Response Dynamics Evaluations.  
           
                    The OP2,RS2,EEF file are processed in this area and copied to the original location as needed.
                   
         
        """
        pass
    @property
    def UseNastranResultDir(self) -> bool:
        """
        Getter for property: (bool) UseNastranResultDir
         Returns the nastran result directory is used for Response Dynamics Evaluations if this toggle is ON
                   
            
         
        """
        pass
    @UseNastranResultDir.setter
    def UseNastranResultDir(self, use_nastran_result_dir: bool):
        """
        Setter for property: (bool) UseNastranResultDir
         Returns the nastran result directory is used for Response Dynamics Evaluations if this toggle is ON
                   
            
         
        """
        pass
    @property
    def UseScratchDir(self) -> bool:
        """
        Getter for property: (bool) UseScratchDir
         Returns the scratch file is used for Response Dynamics Evaluations.  
           
                    This option turns the usage of the scratch directory on or off.
                   
         
        """
        pass
    @UseScratchDir.setter
    def UseScratchDir(self, use_scratch_dir: bool):
        """
        Setter for property: (bool) UseScratchDir
         Returns the scratch file is used for Response Dynamics Evaluations.  
           
                    This option turns the usage of the scratch directory on or off.
                   
         
        """
        pass
import NXOpen
class SolutionCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of response analysis meta solution """
    @property
    def ActiveSolution(self) -> Solution:
        """
        Getter for property: ( Solution NXOpen.CAE.Res) ActiveSolution
         Returns the active solution   
            
         
        """
        pass
    @ActiveSolution.setter
    def ActiveSolution(self, active_solution: Solution):
        """
        Setter for property: ( Solution NXOpen.CAE.Res) ActiveSolution
         Returns the active solution   
            
         
        """
        pass
    def CloneSolution(self, old_solution: Solution, suggested_name: str) -> Solution:
        """
         Clones a response analysis meta solution 
         Returns new_solution ( Solution NXOpen.CAE.Res):  the  newly created CAE.ResponseSimulation.Solution  .
        """
        pass
    def CreateSolutionBuilder(self, ra_solution: Solution) -> SolutionBuilder:
        """
         Creates the builder object of response analysis meta solution 
         Returns ra_solution_builder ( SolutionBuilder NXOpen.CAE.Res):  .
        """
        pass
    def FindObject(self, solution_name: str) -> Solution:
        """
         Finds a response analysis meta solution with specified solution name 
         Returns found ( Solution NXOpen.CAE.Res):  .
        """
        pass
import NXOpen
class Solution(NXOpen.NXObject): 
    """ Represents a meta solution providing response analysis functionalities in the .sim file  """
    @property
    def ActiveEvent(self) -> RSEvent:
        """
        Getter for property: ( RSEvent NXOpen.CAE.Res) ActiveEvent
         Returns the active event   
            
         
        """
        pass
    @ActiveEvent.setter
    def ActiveEvent(self, active_event: RSEvent):
        """
        Setter for property: ( RSEvent NXOpen.CAE.Res) ActiveEvent
         Returns the active event   
            
         
        """
        pass
    def CheckObsoleteStatus(self) -> None:
        """
         Checks status and updates solution properties for the solution which became obsolete because
                    referenced modal shape file was changed. The solution will be reactivated as normal state after status checking. 
        """
        pass
    def CloneEvent(self, source_event: RSEvent, suggested_name: str) -> RSEvent:
        """
         Clones an event to the solution 
         Returns new_event ( RSEvent NXOpen.CAE.Res):   .
        """
        pass
    def CloneSensor(self, source_sensor: Sensor, suggested_name: str) -> Sensor:
        """
         Clones a sensor to the solution 
         Returns new_sensor ( Sensor NXOpen.CAE.Res):   .
        """
        pass
    def CloneStrainGage(self, source_gage: StrainGage, suggested_name: str) -> StrainGage:
        """
         Clones a strain gage to the solution 
         Returns new_gage ( StrainGage NXOpen.CAE.Res):   .
        """
        pass
    def Destroy(self, deleteResultFile: bool) -> None:
        """
         Deletes a response simulation solution, including all events and excitations
                    under it 
        """
        pass
    def EvaluateFrf(self, evaluation_setting: FrfEvaluationSetting) -> None:
        """
         Performs evaluation for FRF. The evaluation results will be stored in an AFU file,
                which name could be returned by NXOpen.CAE.ResponseSimulation.Solution.GetResultFileName 
        """
        pass
    def EvaluateTransmissibility(self, evaluation_setting: TransmissibilityEvaluationSetting) -> None:
        """
         Performs evaluation for transimissibility. The evaluation results will be stored in an AFU file,
                which name could be returned by NXOpen.CAE.ResponseSimulation.Solution.GetResultFileName 
        """
        pass
    def GetEvaluationParameters(self) -> EvaluationParameters:
        """
         Returns the evaluation parameters of Response Analysis Meta solution
         Returns evaluation_parameters ( EvaluationParameters NXOpen.CAE.Res):  .
        """
        pass
    def GetEvents(self) -> List[RSEvent]:
        """
         Returns all the events of the solution
         Returns events ( RSEvent List[NXOpen.CAE.R):  .
        """
        pass
    def GetModalProperties(self) -> ModalProperties:
        """
         Returns the modal properties of Response Analysis Meta solution
         Returns modal_properties ( ModalProperties NXOpen.CAE.Res):  .
        """
        pass
    def GetResultFileName(self) -> str:
        """
         Returns the result file name of solution 
         Returns result_file_name (str):  .
        """
        pass
    def GetSolutionName(self) -> str:
        """
         Returns the response simulation solution name 
         Returns solutionName (str):  .
        """
        pass
    def ImportEvent(self, event_definition_file: str, suggested_name: str) -> RSEvent:
        """
         Imports an event to the solution 
         Returns new_event ( RSEvent NXOpen.CAE.Res):   .
        """
        pass
    def SetSolutionName(self, solutionName: str, renameResultFile: bool) -> None:
        """
         Sets the response simulation solution name 
        """
        pass
class StaticLoadExcitationBuilder(ExcitationBuilder): 
    """ Represents the manager to NXOpen.CAE.ResponseSimulation.StaticLoadExcitation.
     The object of type NXOpen.CAE.ResponseSimulation.StaticLoadExcitation
      can only be created or edited through this class.
     """
    @property
    def ExcitationFunction(self) -> FunctionComponentData:
        """
        Getter for property: ( FunctionComponentData NXOpen.CAE.Res) ExcitationFunction
         Returns the magnitude function   
            
         
        """
        pass
class StaticLoadExcitation(Excitation): 
    """ Represents an excitation of static load type """
    pass
import NXOpen
import NXOpen.CAE
class StrainGageBuilder(BaseBuilder): 
    """
    Represents a StrainGageBuilder
    """
    @property
    def Csys(self) -> NXOpen.SmartObject:
        """
        Getter for property: ( NXOpen.SmartObject) Csys
         Returns the orientation direction, Only available when the strain gage's orientation plane type is
                     CAE::ResponseSimulation::StrainGageOrientationPlaneCsys   
            
         
        """
        pass
    @Csys.setter
    def Csys(self, orientation_coord_system: NXOpen.SmartObject):
        """
        Setter for property: ( NXOpen.SmartObject) Csys
         Returns the orientation direction, Only available when the strain gage's orientation plane type is
                     CAE::ResponseSimulation::StrainGageOrientationPlaneCsys   
            
         
        """
        pass
    @property
    def GageType(self) -> StrainGageType:
        """
        Getter for property: ( StrainGageType NXOpen.CAE.Res) GageType
         Returns the type of strain gage  
            
         
        """
        pass
    @GageType.setter
    def GageType(self, gage_type: StrainGageType):
        """
        Setter for property: ( StrainGageType NXOpen.CAE.Res) GageType
         Returns the type of strain gage  
            
         
        """
        pass
    @property
    def Placement(self) -> StrainGagePlacementType:
        """
        Getter for property: ( StrainGagePlacementType NXOpen.CAE.Res) Placement
         Returns the placement type of strain gage  
            
         
        """
        pass
    @Placement.setter
    def Placement(self, gage_placement: StrainGagePlacementType):
        """
        Setter for property: ( StrainGagePlacementType NXOpen.CAE.Res) Placement
         Returns the placement type of strain gage  
            
         
        """
        pass
    @property
    def Plane(self) -> StrainGageOrientationPlane:
        """
        Getter for property: ( StrainGageOrientationPlane NXOpen.CAE.Res) Plane
         Returns the orientation plane type of strain gage  
            
         
        """
        pass
    @Plane.setter
    def Plane(self, plane: StrainGageOrientationPlane):
        """
        Setter for property: ( StrainGageOrientationPlane NXOpen.CAE.Res) Plane
         Returns the orientation plane type of strain gage  
            
         
        """
        pass
    @property
    def ResultType(self) -> StrainGageResult:
        """
        Getter for property: ( StrainGageResult NXOpen.CAE.Res) ResultType
         Returns the result type of strain gage  
            
         
        """
        pass
    @ResultType.setter
    def ResultType(self, result_type: StrainGageResult):
        """
        Setter for property: ( StrainGageResult NXOpen.CAE.Res) ResultType
         Returns the result type of strain gage  
            
         
        """
        pass
    @property
    def RotationAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RotationAngle
         Returns the rotation angle, Only available when the strain gage's orientation plane type is
                     CAE::ResponseSimulation::StrainGageOrientationPlaneCsys    
            
         
        """
        pass
    @property
    def SelectedElementFaces(self) -> NXOpen.CAE.SelectFEElemFaceList:
        """
        Getter for property: ( NXOpen.CAE.SelectFEElemFaceList) SelectedElementFaces
         Returns  the selected element face.  
          
                    Only available when the strain gage's placement type is
                     CAE::ResponseSimulation::StrainGagePlacementTypeElementFaceCenter     
         
        """
        pass
    @property
    def SelectedNode(self) -> NXOpen.CAE.SelectFENodeList:
        """
        Getter for property: ( NXOpen.CAE.SelectFENodeList) SelectedNode
         Returns the destination nodes, Only available when the strain gage's placement type is
                     CAE::ResponseSimulation::StrainGagePlacementTypeNode     
            
         
        """
        pass
    @property
    def ShellElementFace(self) -> StrainGageShellElementFaceType:
        """
        Getter for property: ( StrainGageShellElementFaceType NXOpen.CAE.Res) ShellElementFace
         Returns the shell element face location type of strain gage   
            
         
        """
        pass
    @ShellElementFace.setter
    def ShellElementFace(self, shell_element_face: StrainGageShellElementFaceType):
        """
        Setter for property: ( StrainGageShellElementFaceType NXOpen.CAE.Res) ShellElementFace
         Returns the shell element face location type of strain gage   
            
         
        """
        pass
import NXOpen
class StrainGageCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of response analysis strain gage """
    def CreateStrainGageBuilder(self, strain_gage: StrainGage) -> StrainGageBuilder:
        """
         Creates a strain gage buider 
         Returns builder ( StrainGageBuilder NXOpen.CAE.Res):   .
        """
        pass
    def FindObject(self, name: str) -> StrainGage:
        """
         Finds an strain gage with specified gage name 
         Returns strain_gage ( StrainGage NXOpen.CAE.Res):   .
        """
        pass
import NXOpen
class StrainGageEvaluationSettingBuilder(FunctionEvaluationSettingBuilder): 
    """ This is a manager to the NXOpen.CAE.ResponseSimulation.StrainGageEvaluationSetting class. 
        Object of type NXOpen.CAE.ResponseSimulation.StrainGageEvaluationSetting can be 
        created and edited only through this class
         """
    @property
    def DataComponent(self) -> DirectionDataComponent:
        """
        Getter for property: ( DirectionDataComponent NXOpen.CAE.Res) DataComponent
         Returns the data component of strain gage evaluation results  
            
         
        """
        pass
    @DataComponent.setter
    def DataComponent(self, data_component: DirectionDataComponent):
        """
        Setter for property: ( DirectionDataComponent NXOpen.CAE.Res) DataComponent
         Returns the data component of strain gage evaluation results  
            
         
        """
        pass
    @property
    def StrainGage(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) StrainGage
         Returns the destination strain Gages   
            
         
        """
        pass
class StrainGageEvaluationSetting(DynamicResultEvaluationSetting): 
    """ Represents the parameters setting for strain gage evaluation.  For more information, see the 
    Response Dynamics section of the Gateway Help """
    pass
class StrainGageOrientationPlane(Enum):
    """
    Members Include: 
     |FacePlane|  
     |Csys|  

    """
    FacePlane: int
    Csys: int
    @staticmethod
    def ValueOf(value: int) -> StrainGageOrientationPlane:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class StrainGagePlacementType(Enum):
    """
    Members Include: 
     |Node|  
     |ElementFaceCenter|  

    """
    Node: int
    ElementFaceCenter: int
    @staticmethod
    def ValueOf(value: int) -> StrainGagePlacementType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class StrainGageResult(Enum):
    """
    Members Include: 
     |Strain|  
     |Stress|  

    """
    Strain: int
    Stress: int
    @staticmethod
    def ValueOf(value: int) -> StrainGageResult:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class StrainGageShellElementFaceType(Enum):
    """
    Members Include: 
     |Top|  
     |Botton|  

    """
    Top: int
    Botton: int
    @staticmethod
    def ValueOf(value: int) -> StrainGageShellElementFaceType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class StrainGageType(Enum):
    """
    Members Include: 
     |UniAxial|  
     |BiAxial|  
     |Rosette45DegreeIncrement|  Rosette 0-45-90 
     |Rosette60DegreeIncrement|  Rosette 0-60-120 

    """
    UniAxial: int
    BiAxial: int
    Rosette45DegreeIncrement: int
    Rosette60DegreeIncrement: int
    @staticmethod
    def ValueOf(value: int) -> StrainGageType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class StrainGage(NXOpen.DisplayableObject): 
    """ Represents a NXOpen.CAE.ResponseSimulation.StrainGage
        """
    def GetDisplayAttribute(self) -> RSDisplayObject:
        """
         Get display attribute of gage 
         Returns display_attr ( RSDisplayObject NXOpen.CAE.Res):   .
        """
        pass
import NXOpen.CAE
class StrengthResultsEvaluationSettingBuilder(DynamicResultEvaluationSettingBuilder): 
    """ This is a manager to the NXOpen.CAE.ResponseSimulation.StrengthResultsEvaluationSetting class. 
    Object of type NXOpen.CAE.ResponseSimulation.StrengthResultsEvaluationSetting can be 
    created and edited only through this class
     """
    @property
    def CombinationOptionsBuilder(self) -> CombinationEvaluationOptions:
        """
        Getter for property: ( CombinationEvaluationOptions NXOpen.CAE.Res) CombinationOptionsBuilder
         Returns the setting of combination evaluation   
            
         
        """
        pass
    @property
    def DataLocation(self) -> DataLocation:
        """
        Getter for property: ( DataLocation NXOpen.CAE.Res) DataLocation
         Returns the setting of combination evaluation   
            
         
        """
        pass
    @property
    def MaterialDefinitionType(self) -> StrengthStressMaterialDefinitionMethod:
        """
        Getter for property: ( StrengthStressMaterialDefinitionMethod NXOpen.CAE.Res) MaterialDefinitionType
         Returns the definition method of material   
            
         
        """
        pass
    @MaterialDefinitionType.setter
    def MaterialDefinitionType(self, material_property: StrengthStressMaterialDefinitionMethod):
        """
        Setter for property: ( StrengthStressMaterialDefinitionMethod NXOpen.CAE.Res) MaterialDefinitionType
         Returns the definition method of material   
            
         
        """
        pass
    @property
    def MaterialOverrideOption(self) -> bool:
        """
        Getter for property: (bool) MaterialOverrideOption
         Returns the choice of override material property or not.  
           If false, the material safty factor will be read 
                     from destination element selected, else a customized value will be used   
         
        """
        pass
    @MaterialOverrideOption.setter
    def MaterialOverrideOption(self, override_material_property: bool):
        """
        Setter for property: (bool) MaterialOverrideOption
         Returns the choice of override material property or not.  
           If false, the material safty factor will be read 
                     from destination element selected, else a customized value will be used   
         
        """
        pass
    @property
    def MaterialSafetyFactor(self) -> float:
        """
        Getter for property: (float) MaterialSafetyFactor
         Returns the customized material safety factor   
            
         
        """
        pass
    @MaterialSafetyFactor.setter
    def MaterialSafetyFactor(self, safety_factor: float):
        """
        Setter for property: (float) MaterialSafetyFactor
         Returns the customized material safety factor   
            
         
        """
        pass
    @property
    def StandardDeviation(self) -> float:
        """
        Getter for property: (float) StandardDeviation
         Returns the customized standard deviation for random event   
            
         
        """
        pass
    @StandardDeviation.setter
    def StandardDeviation(self, standard_deviation: float):
        """
        Setter for property: (float) StandardDeviation
         Returns the customized standard deviation for random event   
            
         
        """
        pass
    @property
    def StressCriteriaType(self) -> StrengthStressCriteria:
        """
        Getter for property: ( StrengthStressCriteria NXOpen.CAE.Res) StressCriteriaType
         Returns the stress criteria type   
            
         
        """
        pass
    @StressCriteriaType.setter
    def StressCriteriaType(self, stress_criteria: StrengthStressCriteria):
        """
        Setter for property: ( StrengthStressCriteria NXOpen.CAE.Res) StressCriteriaType
         Returns the stress criteria type   
            
         
        """
        pass
    @property
    def StressOptionType(self) -> StrengthStressOption:
        """
        Getter for property: ( StrengthStressOption NXOpen.CAE.Res) StressOptionType
         Returns the stress option type   
            
         
        """
        pass
    @StressOptionType.setter
    def StressOptionType(self, stress_option: StrengthStressOption):
        """
        Setter for property: ( StrengthStressOption NXOpen.CAE.Res) StressOptionType
         Returns the stress option type   
            
         
        """
        pass
    def GetDestinationElements(self) -> List[NXOpen.CAE.FEElement]:
        """
         Returns the destination elements 
         Returns destination_elements ( NXOpen.CAE.FEElement Li):  .
        """
        pass
    def SetDestinationElements(self, destination_element: List[NXOpen.CAE.FEElement]) -> None:
        """
         Sets the destination elements 
        """
        pass
class StrengthResultsEvaluationSetting(DynamicResultEvaluationSetting): 
    """ Represents parameters setting for strength results evaluation. Available to all kinds of 
    event type """
    pass
class StrengthStressCriteria(Enum):
    """
    Members Include: 
     |VonMises|  
     |MaxPrinciple|  
     |MinPrinciple|  

    """
    VonMises: int
    MaxPrinciple: int
    MinPrinciple: int
    @staticmethod
    def ValueOf(value: int) -> StrengthStressCriteria:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class StrengthStressMaterialDefinitionMethod(Enum):
    """
    Members Include: 
     |UltimateSafety|  
     |YieldSafety|  

    """
    UltimateSafety: int
    YieldSafety: int
    @staticmethod
    def ValueOf(value: int) -> StrengthStressMaterialDefinitionMethod:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class StrengthStressOption(Enum):
    """
    Members Include: 
     |ElementMaximum|  
     |NodeOnElement|  

    """
    ElementMaximum: int
    NodeOnElement: int
    @staticmethod
    def ValueOf(value: int) -> StrengthStressOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class TranslationalDDAMExcitationBuilder(DDAMExcitationBuilder): 
    """ Represents the manager to CAE.ResponseSimulation.DDAMExcitation.
     The object of type CAE.ResponseSimulation.DDAMExcitation can only
    be created or edited through this class. """
    pass
class TranslationalDDAMExcitation(DDAMExcitation): 
    """ Represents an DDAM excitation. DDAM excitation could only be used by DDAM event. """
    pass
import NXOpen
class TranslationalNodalFunctionExcitationBuilder(NodalFunctionExcitationBuilder): 
    """ Represents the manager to NXOpen.CAE.ResponseSimulation.TranslationalNodalFunctionExcitation. 
    The objects of NXOpen.CAE.ResponseSimulation.TranslationalNodalFunctionExcitation 
    can be created or edited on through this class """
    class RotationAxisType(Enum):
        """
        Members Include: 
         |X|   
         |Y|   
         |Z|   

        """
        X: int
        Y: int
        Z: int
        @staticmethod
        def ValueOf(value: int) -> TranslationalNodalFunctionExcitationBuilder.RotationAxisType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def EnableUserDefinedDirection(self) -> bool:
        """
        Getter for property: (bool) EnableUserDefinedDirection
         Returns the excitation function definition method   
            
         
        """
        pass
    @EnableUserDefinedDirection.setter
    def EnableUserDefinedDirection(self, enable_user_defefined_direction: bool):
        """
        Setter for property: (bool) EnableUserDefinedDirection
         Returns the excitation function definition method   
            
         
        """
        pass
    @property
    def EnableUserDefinedRotation(self) -> bool:
        """
        Getter for property: (bool) EnableUserDefinedRotation
         Returns the excitation function definition method   
            
         
        """
        pass
    @EnableUserDefinedRotation.setter
    def EnableUserDefinedRotation(self, enable_user_defined_rotation: bool):
        """
        Setter for property: (bool) EnableUserDefinedRotation
         Returns the excitation function definition method   
            
         
        """
        pass
    @property
    def FunctionComponentX(self) -> FunctionComponentData:
        """
        Getter for property: ( FunctionComponentData NXOpen.CAE.Res) FunctionComponentX
         Returns the function component of X direction    
            
         
        """
        pass
    @property
    def FunctionComponentY(self) -> FunctionComponentData:
        """
        Getter for property: ( FunctionComponentData NXOpen.CAE.Res) FunctionComponentY
         Returns the function component of Y direction   
            
         
        """
        pass
    @property
    def FunctionComponentZ(self) -> FunctionComponentData:
        """
        Getter for property: ( FunctionComponentData NXOpen.CAE.Res) FunctionComponentZ
         Returns the function component of Z direction   
            
         
        """
        pass
    @property
    def RotationAxis(self) -> TranslationalNodalFunctionExcitationBuilder.RotationAxisType:
        """
        Getter for property: ( TranslationalNodalFunctionExcitationBuilder.RotationAxisType NXOpen.CAE.Res) RotationAxis
         Returns the rotation axis   
            
         
        """
        pass
    @RotationAxis.setter
    def RotationAxis(self, rotation_axis: TranslationalNodalFunctionExcitationBuilder.RotationAxisType):
        """
        Setter for property: ( TranslationalNodalFunctionExcitationBuilder.RotationAxisType NXOpen.CAE.Res) RotationAxis
         Returns the rotation axis   
            
         
        """
        pass
    @property
    def UserDefinedDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) UserDefinedDirection
         Returns the magnitude direction   
            
         
        """
        pass
    @UserDefinedDirection.setter
    def UserDefinedDirection(self, magnitude_direction: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) UserDefinedDirection
         Returns the magnitude direction   
            
         
        """
        pass
    @property
    def UserDefinedFunction(self) -> FunctionComponentData:
        """
        Getter for property: ( FunctionComponentData NXOpen.CAE.Res) UserDefinedFunction
         Returns the magnitude function   
            
         
        """
        pass
class TranslationalNodalFunctionExcitation(NodalFunctionExcitation): 
    """ Represents a translational nodal function excitation """
    pass
class TransmissibilityEvaluationSettingBuilder(ModalResultsEvaluationSettingBuilder): 
    """ This is a manager to the NXOpen.CAE.ResponseSimulation.TransmissibilityEvaluationSetting class. 
    Object of type NXOpen.CAE.ResponseSimulation.TransmissibilityEvaluationSetting can be 
    created and edited only through this class
     """
    class MotionType(Enum):
        """
        Members Include: 
         |Displacement|   
         |Velocity|   
         |Acceleration|   

        """
        Displacement: int
        Velocity: int
        Acceleration: int
        @staticmethod
        def ValueOf(value: int) -> TransmissibilityEvaluationSettingBuilder.MotionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def InputMotionType(self) -> TransmissibilityEvaluationSettingBuilder.MotionType:
        """
        Getter for property: ( TransmissibilityEvaluationSettingBuilder.MotionType NXOpen.CAE.Res) InputMotionType
         Returns the input motion type   
            
         
        """
        pass
    @InputMotionType.setter
    def InputMotionType(self, motion_type: TransmissibilityEvaluationSettingBuilder.MotionType):
        """
        Setter for property: ( TransmissibilityEvaluationSettingBuilder.MotionType NXOpen.CAE.Res) InputMotionType
         Returns the input motion type   
            
         
        """
        pass
class TransmissibilityEvaluationSetting(ModalResultsEvaluationSetting): 
    """ Represents parameters setting for transmissibility evaluation """
    pass
import NXOpen
import NXOpen.GeometricUtilities
class VelocityImpactDirection(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.CAE.ResponseSimulation.VelocityImpactDirection
    """
    class DirectionType(Enum):
        """
        Members Include: 
         |NodalComponent|  
         |UserDefined|  

        """
        NodalComponent: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> VelocityImpactDirection.DirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class NodalComponentType(Enum):
        """
        Members Include: 
         |Dof1|  
         |Dof2|  
         |Dof3|  

        """
        Dof1: int
        Dof2: int
        Dof3: int
        @staticmethod
        def ValueOf(value: int) -> VelocityImpactDirection.NodalComponentType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DirectionOption(self) -> VelocityImpactDirection.DirectionType:
        """
        Getter for property: ( VelocityImpactDirection.DirectionType NXOpen.CAE.Res) DirectionOption
         Returns the direction option   
            
         
        """
        pass
    @DirectionOption.setter
    def DirectionOption(self, mDirectionOption: VelocityImpactDirection.DirectionType):
        """
        Setter for property: ( VelocityImpactDirection.DirectionType NXOpen.CAE.Res) DirectionOption
         Returns the direction option   
            
         
        """
        pass
    @property
    def NodalComponent(self) -> VelocityImpactDirection.NodalComponentType:
        """
        Getter for property: ( VelocityImpactDirection.NodalComponentType NXOpen.CAE.Res) NodalComponent
         Returns the selected nodal component   
            
         
        """
        pass
    @NodalComponent.setter
    def NodalComponent(self, nodalComponent: VelocityImpactDirection.NodalComponentType):
        """
        Setter for property: ( VelocityImpactDirection.NodalComponentType NXOpen.CAE.Res) NodalComponent
         Returns the selected nodal component   
            
         
        """
        pass
    @property
    def ReverseDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseDirection
         Returns the option to reverse direction of nodal component or not.  
           Only valid when direction option is
                 NXOpen::CAE::ResponseSimulation::VelocityImpactDirection::DirectionTypeNodalComponent    
         
        """
        pass
    @ReverseDirection.setter
    def ReverseDirection(self, reverseDirection: bool):
        """
        Setter for property: (bool) ReverseDirection
         Returns the option to reverse direction of nodal component or not.  
           Only valid when direction option is
                 NXOpen::CAE::ResponseSimulation::VelocityImpactDirection::DirectionTypeNodalComponent    
         
        """
        pass
    @property
    def UserDefinedDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) UserDefinedDirection
         Returns the user-defined direction  
            
         
        """
        pass
    @UserDefinedDirection.setter
    def UserDefinedDirection(self, userDefinedDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) UserDefinedDirection
         Returns the user-defined direction  
            
         
        """
        pass
class VelocityImpactExcitationBuilder(ExcitationBuilder): 
    """
    Represents a NXOpen.CAE.ResponseSimulation.VelocityImpactExcitationBuilder
    """
    class ImpactMethodType(Enum):
        """
        Members Include: 
         |ConstantVelocity|  the users will only be able to specify the velocity for the impact 
         |DropImpact|  the users will be able to specify the drop height or the desired velocity at the impact

        """
        ConstantVelocity: int
        DropImpact: int
        @staticmethod
        def ValueOf(value: int) -> VelocityImpactExcitationBuilder.ImpactMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ImpactDirection(self) -> VelocityImpactDirection:
        """
        Getter for property: ( VelocityImpactDirection NXOpen.CAE.Res) ImpactDirection
         Returns the impact direction setting  
            
         
        """
        pass
    @property
    def ImpactMethod(self) -> VelocityImpactExcitationBuilder.ImpactMethodType:
        """
        Getter for property: ( VelocityImpactExcitationBuilder.ImpactMethodType NXOpen.CAE.Res) ImpactMethod
         Returns the impact method   
            
         
        """
        pass
    @ImpactMethod.setter
    def ImpactMethod(self, impactMethod: VelocityImpactExcitationBuilder.ImpactMethodType):
        """
        Setter for property: ( VelocityImpactExcitationBuilder.ImpactMethodType NXOpen.CAE.Res) ImpactMethod
         Returns the impact method   
            
         
        """
        pass
    @property
    def ImpactParameters(self) -> VelocityImpactParameters:
        """
        Getter for property: ( VelocityImpactParameters NXOpen.CAE.Res) ImpactParameters
         Returns the impact parameters setting  
            
         
        """
        pass
class VelocityImpactExcitation(Excitation): 
    """ Represents a velocity impact excitation """
    pass
import NXOpen
import NXOpen.GeometricUtilities
class VelocityImpactParameters(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.CAE.ResponseSimulation.VelocityImpactParameters
    """
    class StartPositionType(Enum):
        """
        Members Include: 
         |AtDrop|  Calculation starts from the drop time
         |BeforeImpact|  Calculation ends at the impact time 
         |AtImpact|  Calculation starts from the impact time 

        """
        AtDrop: int
        BeforeImpact: int
        AtImpact: int
        @staticmethod
        def ValueOf(value: int) -> VelocityImpactParameters.StartPositionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DropHeight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DropHeight
         Returns the drop height.  
           Not available if the impact excitation is of type   
                CAE::ResponseSimulation::VelocityImpactExcitationBuilder::ImpactMethodTypeConstantVelocity
                    
         
        """
        pass
    @property
    def PulseDuration(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PulseDuration
         Returns the impact pulse duration   
            
         
        """
        pass
    @property
    def StartPosition(self) -> VelocityImpactParameters.StartPositionType:
        """
        Getter for property: ( VelocityImpactParameters.StartPositionType NXOpen.CAE.Res) StartPosition
         Returns the start position   
            
         
        """
        pass
    @StartPosition.setter
    def StartPosition(self, mStartPosition: VelocityImpactParameters.StartPositionType):
        """
        Setter for property: ( VelocityImpactParameters.StartPositionType NXOpen.CAE.Res) StartPosition
         Returns the start position   
            
         
        """
        pass
    @property
    def TimeStep(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TimeStep
         Returns the time step.  
           The value must be larger than 120 of the impact pulse duration   
         
        """
        pass
    @property
    def Velocity(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Velocity
         Returns the velocity   
            
         
        """
        pass
