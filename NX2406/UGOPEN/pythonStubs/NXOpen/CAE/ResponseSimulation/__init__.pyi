from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents the abstract builder class for all objects defined in response analysis meta solution  <br> This is an abstract class, and cannot be created.  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class BaseBuilder(NXOpen.Builder): 
    """ Represents the abstract builder class for all objects defined in response analysis meta solution """


    ## Getter for property: (@link ObjectLabel NXOpen.CAE.ResponseSimulation.ObjectLabel@endlink) ObjectLabel
    ##  Returns the object label   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return ObjectLabel
    @property
    def ObjectLabel(self) -> ObjectLabel:
        """
        Getter for property: (@link ObjectLabel NXOpen.CAE.ResponseSimulation.ObjectLabel@endlink) ObjectLabel
         Returns the object label   
            
         
        """
        pass
    
import NXOpen
##  Represents the setting for combination evaluation. 
## 
##   <br>  Created in NX5.0.0  <br> 

class CombinationEvaluationOptions(NXOpen.TaggedObject): 
    """ Represents the setting for combination evaluation. """


    ##  Specifies the calculation method of combination evaluation 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Abs</term><description> 
    ##  </description> </item><item><term> 
    ## Srss</term><description> 
    ##  </description> </item><item><term> 
    ## Nrl</term><description> 
    ##  </description> </item><item><term> 
    ## Cqc</term><description> 
    ##  </description> </item><item><term> 
    ## NqcDoubleSum</term><description> 
    ##  </description> </item></list>
    class EvaluationMethod(Enum):
        """
        Members Include: <Abs> <Srss> <Nrl> <Cqc> <NqcDoubleSum>
        """
        Abs: int
        Srss: int
        Nrl: int
        Cqc: int
        NqcDoubleSum: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CombinationEvaluationOptions.EvaluationMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Specifies combination method for multiple excitation combination 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Abs</term><description> 
    ##  </description> </item><item><term> 
    ## Srs</term><description> 
    ##  </description> </item></list>
    class MultipleExcitationCombinationMethod(Enum):
        """
        Members Include: <Abs> <Srs>
        """
        Abs: int
        Srs: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CombinationEvaluationOptions.MultipleExcitationCombinationMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link CombinationEvaluationOptions.MultipleExcitationCombinationMethod NXOpen.CAE.ResponseSimulation.CombinationEvaluationOptions.MultipleExcitationCombinationMethod@endlink) CombinationMethod
    ##  Returns the combination method for multiple excitation combination   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return CombinationEvaluationOptions.MultipleExcitationCombinationMethod
    @property
    def CombinationMethod(self) -> CombinationEvaluationOptions.MultipleExcitationCombinationMethod:
        """
        Getter for property: (@link CombinationEvaluationOptions.MultipleExcitationCombinationMethod NXOpen.CAE.ResponseSimulation.CombinationEvaluationOptions.MultipleExcitationCombinationMethod@endlink) CombinationMethod
         Returns the combination method for multiple excitation combination   
            
         
        """
        pass
    
    ## Setter for property: (@link CombinationEvaluationOptions.MultipleExcitationCombinationMethod NXOpen.CAE.ResponseSimulation.CombinationEvaluationOptions.MultipleExcitationCombinationMethod@endlink) CombinationMethod

    ##  Returns the combination method for multiple excitation combination   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @CombinationMethod.setter
    def CombinationMethod(self, combination_method: CombinationEvaluationOptions.MultipleExcitationCombinationMethod):
        """
        Setter for property: (@link CombinationEvaluationOptions.MultipleExcitationCombinationMethod NXOpen.CAE.ResponseSimulation.CombinationEvaluationOptions.MultipleExcitationCombinationMethod@endlink) CombinationMethod
         Returns the combination method for multiple excitation combination   
            
         
        """
        pass
    
    ## Getter for property: (@link CombinationEvaluationOptions.EvaluationMethod NXOpen.CAE.ResponseSimulation.CombinationEvaluationOptions.EvaluationMethod@endlink) EvaluationMethodOption
    ##  Returns the calculation method   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return CombinationEvaluationOptions.EvaluationMethod
    @property
    def EvaluationMethodOption(self) -> CombinationEvaluationOptions.EvaluationMethod:
        """
        Getter for property: (@link CombinationEvaluationOptions.EvaluationMethod NXOpen.CAE.ResponseSimulation.CombinationEvaluationOptions.EvaluationMethod@endlink) EvaluationMethodOption
         Returns the calculation method   
            
         
        """
        pass
    
    ## Setter for property: (@link CombinationEvaluationOptions.EvaluationMethod NXOpen.CAE.ResponseSimulation.CombinationEvaluationOptions.EvaluationMethod@endlink) EvaluationMethodOption

    ##  Returns the calculation method   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @EvaluationMethodOption.setter
    def EvaluationMethodOption(self, method: CombinationEvaluationOptions.EvaluationMethod):
        """
        Setter for property: (@link CombinationEvaluationOptions.EvaluationMethod NXOpen.CAE.ResponseSimulation.CombinationEvaluationOptions.EvaluationMethod@endlink) EvaluationMethodOption
         Returns the calculation method   
            
         
        """
        pass
    
    ## Getter for property: (float) NeighboringFactor
    ##  Returns the neighboring factor.  
    ##    Must be specified when calculation method is 
    ##         @link  CAE::ResponseSimulation::CombinationEvaluationOptions::EvaluationMethodNrl  CAE::ResponseSimulation::CombinationEvaluationOptions::EvaluationMethodNrl@endlink    
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def NeighboringFactor(self) -> float:
        """
        Getter for property: (float) NeighboringFactor
         Returns the neighboring factor.  
           Must be specified when calculation method is 
                @link  CAE::ResponseSimulation::CombinationEvaluationOptions::EvaluationMethodNrl  CAE::ResponseSimulation::CombinationEvaluationOptions::EvaluationMethodNrl@endlink    
         
        """
        pass
    
    ## Setter for property: (float) NeighboringFactor

    ##  Returns the neighboring factor.  
    ##    Must be specified when calculation method is 
    ##         @link  CAE::ResponseSimulation::CombinationEvaluationOptions::EvaluationMethodNrl  CAE::ResponseSimulation::CombinationEvaluationOptions::EvaluationMethodNrl@endlink    
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @NeighboringFactor.setter
    def NeighboringFactor(self, neighboring_factor: float):
        """
        Setter for property: (float) NeighboringFactor
         Returns the neighboring factor.  
           Must be specified when calculation method is 
                @link  CAE::ResponseSimulation::CombinationEvaluationOptions::EvaluationMethodNrl  CAE::ResponseSimulation::CombinationEvaluationOptions::EvaluationMethodNrl@endlink    
         
        """
        pass
    
    ## Getter for property: (float) TimeDuration
    ##  Returns the time duration in second.  
    ##    Must be specified when calculation method is 
    ##         @link CAE::ResponseSimulation::CombinationEvaluationOptions::EvaluationMethodNqcDoubleSum CAE::ResponseSimulation::CombinationEvaluationOptions::EvaluationMethodNqcDoubleSum@endlink    
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def TimeDuration(self) -> float:
        """
        Getter for property: (float) TimeDuration
         Returns the time duration in second.  
           Must be specified when calculation method is 
                @link CAE::ResponseSimulation::CombinationEvaluationOptions::EvaluationMethodNqcDoubleSum CAE::ResponseSimulation::CombinationEvaluationOptions::EvaluationMethodNqcDoubleSum@endlink    
         
        """
        pass
    
    ## Setter for property: (float) TimeDuration

    ##  Returns the time duration in second.  
    ##    Must be specified when calculation method is 
    ##         @link CAE::ResponseSimulation::CombinationEvaluationOptions::EvaluationMethodNqcDoubleSum CAE::ResponseSimulation::CombinationEvaluationOptions::EvaluationMethodNqcDoubleSum@endlink    
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @TimeDuration.setter
    def TimeDuration(self, time_duration: float):
        """
        Setter for property: (float) TimeDuration
         Returns the time duration in second.  
           Must be specified when calculation method is 
                @link CAE::ResponseSimulation::CombinationEvaluationOptions::EvaluationMethodNqcDoubleSum CAE::ResponseSimulation::CombinationEvaluationOptions::EvaluationMethodNqcDoubleSum@endlink    
         
        """
        pass
    
##  Specifies the coordinate system 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Nodal</term><description> 
##  </description> </item><item><term> 
## Global</term><description> 
##  </description> </item><item><term> 
## Elemental</term><description> 
##  </description> </item><item><term> 
## Material</term><description> 
##  </description> </item></list>
class CoordinateSystem(Enum):
    """
    Members Include: <Nodal> <Global> <Elemental> <Material>
    """
    Nodal: int
    Global: int
    Elemental: int
    Material: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> CoordinateSystem:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
import NXOpen.CAE
##  Represents the CSD build  <br> To create a new instance of this class, use @link NXOpen::CAE::ResponseSimulation::EvaluationSettingManager::CreateCsdEvaluationSettingBuilder  NXOpen::CAE::ResponseSimulation::EvaluationSettingManager::CreateCsdEvaluationSettingBuilder @endlink  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class CsdEvaluationSettingBuilder(FunctionEvaluationSettingBuilder): 
    """ Represents the CSD build """


    ## Getter for property: (@link CoordinateSystem NXOpen.CAE.ResponseSimulation.CoordinateSystem@endlink) ReferenceCoordinateSystem
    ##  Returns the coordinate system of reference element.  
    ##    
    ##          Available if the result type is 
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
    ##           
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return CoordinateSystem
    @property
    def ReferenceCoordinateSystem(self) -> CoordinateSystem:
        """
        Getter for property: (@link CoordinateSystem NXOpen.CAE.ResponseSimulation.CoordinateSystem@endlink) ReferenceCoordinateSystem
         Returns the coordinate system of reference element.  
           
                 Available if the result type is 
                 @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
                  
         
        """
        pass
    
    ## Setter for property: (@link CoordinateSystem NXOpen.CAE.ResponseSimulation.CoordinateSystem@endlink) ReferenceCoordinateSystem

    ##  Returns the coordinate system of reference element.  
    ##    
    ##          Available if the result type is 
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
    ##           
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @ReferenceCoordinateSystem.setter
    def ReferenceCoordinateSystem(self, reference_coordinate_system: CoordinateSystem):
        """
        Setter for property: (@link CoordinateSystem NXOpen.CAE.ResponseSimulation.CoordinateSystem@endlink) ReferenceCoordinateSystem
         Returns the coordinate system of reference element.  
           
                 Available if the result type is 
                 @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
                  
         
        """
        pass
    
    ## Getter for property: (@link DataLocation NXOpen.CAE.ResponseSimulation.DataLocation@endlink) ReferenceDataLocation
    ##  Returns the reference element location of reference element.  
    ##    
    ##          Available if the result type is 
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
    ##           
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return DataLocation
    @property
    def ReferenceDataLocation(self) -> DataLocation:
        """
        Getter for property: (@link DataLocation NXOpen.CAE.ResponseSimulation.DataLocation@endlink) ReferenceDataLocation
         Returns the reference element location of reference element.  
           
                 Available if the result type is 
                 @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) ReferenceElement
    ##  Returns the reference element.  
    ##    
    ##          Available if the result type is 
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
    ##           
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.CAE.FEElement
    @property
    def ReferenceElement(self) -> NXOpen.CAE.FEElement:
        """
        Getter for property: (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) ReferenceElement
         Returns the reference element.  
           
                 Available if the result type is 
                 @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
                  
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) ReferenceElement

    ##  Returns the reference element.  
    ##    
    ##          Available if the result type is 
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
    ##           
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @ReferenceElement.setter
    def ReferenceElement(self, reference_element: NXOpen.CAE.FEElement):
        """
        Setter for property: (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) ReferenceElement
         Returns the reference element.  
           
                 Available if the result type is 
                 @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
                  
         
        """
        pass
    
    ## Getter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) ReferenceElementDataComponent
    ##  Returns the direction data component of reference element.  
    ##    
    ##          Available if the result type is 
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
    ##           
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return DirectionDataComponent
    @property
    def ReferenceElementDataComponent(self) -> DirectionDataComponent:
        """
        Getter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) ReferenceElementDataComponent
         Returns the direction data component of reference element.  
           
                 Available if the result type is 
                 @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
                  
         
        """
        pass
    
    ## Setter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) ReferenceElementDataComponent

    ##  Returns the direction data component of reference element.  
    ##    
    ##          Available if the result type is 
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
    ##           
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @ReferenceElementDataComponent.setter
    def ReferenceElementDataComponent(self, reference_element_data_component: DirectionDataComponent):
        """
        Setter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) ReferenceElementDataComponent
         Returns the direction data component of reference element.  
           
                 Available if the result type is 
                 @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.FENode NXOpen.CAE.FENode@endlink) ReferenceNode
    ##  Returns the reference node.  
    ##    
    ##          Available if the result type is 
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
    ##           
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.CAE.FENode
    @property
    def ReferenceNode(self) -> NXOpen.CAE.FENode:
        """
        Getter for property: (@link NXOpen.CAE.FENode NXOpen.CAE.FENode@endlink) ReferenceNode
         Returns the reference node.  
           
                 Available if the result type is 
                 @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
                  
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.FENode NXOpen.CAE.FENode@endlink) ReferenceNode

    ##  Returns the reference node.  
    ##    
    ##          Available if the result type is 
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
    ##           
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @ReferenceNode.setter
    def ReferenceNode(self, reference_node: NXOpen.CAE.FENode):
        """
        Setter for property: (@link NXOpen.CAE.FENode NXOpen.CAE.FENode@endlink) ReferenceNode
         Returns the reference node.  
           
                 Available if the result type is 
                 @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
                  
         
        """
        pass
    
    ## Getter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) ReferenceNodeDataComponent
    ##  Returns the direction data component of reference node.  
    ##    
    ##          Available if the result type is 
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
    ##           
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return DirectionDataComponent
    @property
    def ReferenceNodeDataComponent(self) -> DirectionDataComponent:
        """
        Getter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) ReferenceNodeDataComponent
         Returns the direction data component of reference node.  
           
                 Available if the result type is 
                 @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
                  
         
        """
        pass
    
    ## Setter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) ReferenceNodeDataComponent

    ##  Returns the direction data component of reference node.  
    ##    
    ##          Available if the result type is 
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
    ##           
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @ReferenceNodeDataComponent.setter
    def ReferenceNodeDataComponent(self, reference_node_data_component: DirectionDataComponent):
        """
        Setter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) ReferenceNodeDataComponent
         Returns the direction data component of reference node.  
           
                 Available if the result type is 
                 @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ReferenceUserDefinedDirection
    ##  Returns  the user defined direction of reference node.  
    ##             
    ##          Available if the result type is 
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
    ##           
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def ReferenceUserDefinedDirection(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ReferenceUserDefinedDirection
         Returns  the user defined direction of reference node.  
                    
                 Available if the result type is 
                 @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
                  
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ReferenceUserDefinedDirection

    ##  Returns  the user defined direction of reference node.  
    ##             
    ##          Available if the result type is 
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
    ##           
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @ReferenceUserDefinedDirection.setter
    def ReferenceUserDefinedDirection(self, reference_user_defined_direction: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ReferenceUserDefinedDirection
         Returns  the user defined direction of reference node.  
                    
                 Available if the result type is 
                 @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
                  
         
        """
        pass
    
    ## Getter for property: (@link NodalFunctionEvalRequest NXOpen.CAE.ResponseSimulation.NodalFunctionEvalRequest@endlink) ReferenceUsingUserDefinedDirection
    ##  Returns the option of using user defined direction of the reference node.  
    ##    
    ##          Available if the result type is 
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
    ##           
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NodalFunctionEvalRequest
    @property
    def ReferenceUsingUserDefinedDirection(self) -> NodalFunctionEvalRequest:
        """
        Getter for property: (@link NodalFunctionEvalRequest NXOpen.CAE.ResponseSimulation.NodalFunctionEvalRequest@endlink) ReferenceUsingUserDefinedDirection
         Returns the option of using user defined direction of the reference node.  
           
                 Available if the result type is 
                 @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
                  
         
        """
        pass
    
    ## Setter for property: (@link NodalFunctionEvalRequest NXOpen.CAE.ResponseSimulation.NodalFunctionEvalRequest@endlink) ReferenceUsingUserDefinedDirection

    ##  Returns the option of using user defined direction of the reference node.  
    ##    
    ##          Available if the result type is 
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
    ##           
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @ReferenceUsingUserDefinedDirection.setter
    def ReferenceUsingUserDefinedDirection(self, reference_using_user_defined_direction: NodalFunctionEvalRequest):
        """
        Setter for property: (@link NodalFunctionEvalRequest NXOpen.CAE.ResponseSimulation.NodalFunctionEvalRequest@endlink) ReferenceUsingUserDefinedDirection
         Returns the option of using user defined direction of the reference node.  
           
                 Available if the result type is 
                 @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
                  
         
        """
        pass
    
    ## Getter for property: (@link CoordinateSystem NXOpen.CAE.ResponseSimulation.CoordinateSystem@endlink) ResponseCoordinateSystem
    ##  Returns the coordinate system of response elements.  
    ##    
    ##          Available if the result type is 
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
    ##           
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return CoordinateSystem
    @property
    def ResponseCoordinateSystem(self) -> CoordinateSystem:
        """
        Getter for property: (@link CoordinateSystem NXOpen.CAE.ResponseSimulation.CoordinateSystem@endlink) ResponseCoordinateSystem
         Returns the coordinate system of response elements.  
           
                 Available if the result type is 
                 @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
                  
         
        """
        pass
    
    ## Setter for property: (@link CoordinateSystem NXOpen.CAE.ResponseSimulation.CoordinateSystem@endlink) ResponseCoordinateSystem

    ##  Returns the coordinate system of response elements.  
    ##    
    ##          Available if the result type is 
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
    ##           
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @ResponseCoordinateSystem.setter
    def ResponseCoordinateSystem(self, response_coordinate_system: CoordinateSystem):
        """
        Setter for property: (@link CoordinateSystem NXOpen.CAE.ResponseSimulation.CoordinateSystem@endlink) ResponseCoordinateSystem
         Returns the coordinate system of response elements.  
           
                 Available if the result type is 
                 @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
                  
         
        """
        pass
    
    ## Getter for property: (@link DataLocation NXOpen.CAE.ResponseSimulation.DataLocation@endlink) ResponseDataLocation
    ##  Returns the response element location.  
    ##    
    ##          Available if the result type is 
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
    ##           
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return DataLocation
    @property
    def ResponseDataLocation(self) -> DataLocation:
        """
        Getter for property: (@link DataLocation NXOpen.CAE.ResponseSimulation.DataLocation@endlink) ResponseDataLocation
         Returns the response element location.  
           
                 Available if the result type is 
                 @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
                  
         
        """
        pass
    
    ## Getter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) ResponseElementDataComponent
    ##  Returns the direction data component of response elements.  
    ##    
    ##          Available if the result type is 
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
    ##           
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return DirectionDataComponent
    @property
    def ResponseElementDataComponent(self) -> DirectionDataComponent:
        """
        Getter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) ResponseElementDataComponent
         Returns the direction data component of response elements.  
           
                 Available if the result type is 
                 @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
                  
         
        """
        pass
    
    ## Setter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) ResponseElementDataComponent

    ##  Returns the direction data component of response elements.  
    ##    
    ##          Available if the result type is 
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
    ##           
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @ResponseElementDataComponent.setter
    def ResponseElementDataComponent(self, response_element_data_component: DirectionDataComponent):
        """
        Setter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) ResponseElementDataComponent
         Returns the direction data component of response elements.  
           
                 Available if the result type is 
                 @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
                  
         
        """
        pass
    
    ## Getter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) ResponseNodeDataComponent
    ##  Returns the direction data component of response node.  
    ##    
    ##          Available if the result type is 
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
    ##           
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return DirectionDataComponent
    @property
    def ResponseNodeDataComponent(self) -> DirectionDataComponent:
        """
        Getter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) ResponseNodeDataComponent
         Returns the direction data component of response node.  
           
                 Available if the result type is 
                 @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
                  
         
        """
        pass
    
    ## Setter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) ResponseNodeDataComponent

    ##  Returns the direction data component of response node.  
    ##    
    ##          Available if the result type is 
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
    ##           
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @ResponseNodeDataComponent.setter
    def ResponseNodeDataComponent(self, response_node_data_component: DirectionDataComponent):
        """
        Setter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) ResponseNodeDataComponent
         Returns the direction data component of response node.  
           
                 Available if the result type is 
                 @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ResponseUserDefinedDirection
    ##  Returns  the user defined direction of response nodes.  
    ##    
    ##          Available if the result type is 
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
    ##           
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def ResponseUserDefinedDirection(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ResponseUserDefinedDirection
         Returns  the user defined direction of response nodes.  
           
                 Available if the result type is 
                 @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
                  
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ResponseUserDefinedDirection

    ##  Returns  the user defined direction of response nodes.  
    ##    
    ##          Available if the result type is 
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
    ##           
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @ResponseUserDefinedDirection.setter
    def ResponseUserDefinedDirection(self, response_user_defined_direction: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ResponseUserDefinedDirection
         Returns  the user defined direction of response nodes.  
           
                 Available if the result type is 
                 @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
                  
         
        """
        pass
    
    ## Getter for property: (@link NodalFunctionEvalRequest NXOpen.CAE.ResponseSimulation.NodalFunctionEvalRequest@endlink) ResponseUsingUserDefinedDirection
    ##  Returns the option of using user defined direction of response nodes.  
    ##    
    ##          Available if the result type is 
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
    ##           
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NodalFunctionEvalRequest
    @property
    def ResponseUsingUserDefinedDirection(self) -> NodalFunctionEvalRequest:
        """
        Getter for property: (@link NodalFunctionEvalRequest NXOpen.CAE.ResponseSimulation.NodalFunctionEvalRequest@endlink) ResponseUsingUserDefinedDirection
         Returns the option of using user defined direction of response nodes.  
           
                 Available if the result type is 
                 @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
                  
         
        """
        pass
    
    ## Setter for property: (@link NodalFunctionEvalRequest NXOpen.CAE.ResponseSimulation.NodalFunctionEvalRequest@endlink) ResponseUsingUserDefinedDirection

    ##  Returns the option of using user defined direction of response nodes.  
    ##    
    ##          Available if the result type is 
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
    ##           
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @ResponseUsingUserDefinedDirection.setter
    def ResponseUsingUserDefinedDirection(self, response_using_user_defined_direction: NodalFunctionEvalRequest):
        """
        Setter for property: (@link NodalFunctionEvalRequest NXOpen.CAE.ResponseSimulation.NodalFunctionEvalRequest@endlink) ResponseUsingUserDefinedDirection
         Returns the option of using user defined direction of response nodes.  
           
                 Available if the result type is 
                 @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
                  
         
        """
        pass
    
    ##  Get the response elments. 
    ##          Available if the result type is 
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
    ##         
    ##  @return response_elements (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink):  .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetResponseElements(self) -> List[NXOpen.CAE.FEElement]:
        """
         Get the response elments. 
                 Available if the result type is 
                 @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
                
         @return response_elements (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink):  .
        """
        pass
    
    ##  Get the response nodes. 
    ##          Available if the result type is 
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
    ##         
    ##  @return response_node (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink):  .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetResponseNodes(self) -> List[NXOpen.CAE.FENode]:
        """
         Get the response nodes. 
                 Available if the result type is 
                 @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
                
         @return response_node (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink):  .
        """
        pass
    
    ##  Set the response elments. 
    ##          Available if the result type is 
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
    ##         
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="response_elements"> (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink)  </param>
    def SetResponseElements(self, response_elements: List[NXOpen.CAE.FEElement]) -> None:
        """
         Set the response elments. 
                 Available if the result type is 
                 @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeElementForce CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce CAE::ResponseSimulation::EvaluationResultTypeBeamElementForce@endlink  
                
        """
        pass
    
    ##  Set the response nodes. 
    ##          Available if the result type is 
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
    ##          @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
    ##         
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="response_node"> (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink)  </param>
    def SetResponseNodes(self, response_node: List[NXOpen.CAE.FENode]) -> None:
        """
         Set the response nodes. 
                 Available if the result type is 
                 @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink  
                 @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
                
        """
        pass
    
##  Represents the class of evaluation setting for CSD  <br> To create or edit an instance of this class, use @link NXOpen::CAE::ResponseSimulation::CsdEvaluationSettingBuilder  NXOpen::CAE::ResponseSimulation::CsdEvaluationSettingBuilder @endlink  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class CsdEvaluationSetting(FunctionEvaluationSetting): 
    """ Represents the class of evaluation setting for CSD """
    pass


##  Represents the manager to @link NXOpen::CAE::ResponseSimulation::CSDExcitation NXOpen::CAE::ResponseSimulation::CSDExcitation@endlink .
##      The object of type @link NXOpen::CAE::ResponseSimulation::CSDExcitation NXOpen::CAE::ResponseSimulation::CSDExcitation@endlink 
##       can only be created or edited through this class.
##       <br> To create a new instance of this class, use @link NXOpen::CAE::ResponseSimulation::ExcitationCollection::CreateCsdExcitationBuilder  NXOpen::CAE::ResponseSimulation::ExcitationCollection::CreateCsdExcitationBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class CSDExcitationBuilder(ExcitationBuilder): 
    """ Represents the manager to <ja_class>NXOpen.CAE.ResponseSimulation.CSDExcitation</ja_class>.
     The object of type <ja_class>NXOpen.CAE.ResponseSimulation.CSDExcitation</ja_class>
      can only be created or edited through this class.
     """


    ## Getter for property: (@link CSDExcitation.CorrelationType NXOpen.CAE.ResponseSimulation.CSDExcitation.CorrelationType@endlink) CorrelationType
    ##  Returns the correlation type   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return CSDExcitation.CorrelationType
    @property
    def CorrelationType(self) -> CSDExcitation.CorrelationType:
        """
        Getter for property: (@link CSDExcitation.CorrelationType NXOpen.CAE.ResponseSimulation.CSDExcitation.CorrelationType@endlink) CorrelationType
         Returns the correlation type   
            
         
        """
        pass
    
    ## Setter for property: (@link CSDExcitation.CorrelationType NXOpen.CAE.ResponseSimulation.CSDExcitation.CorrelationType@endlink) CorrelationType

    ##  Returns the correlation type   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @CorrelationType.setter
    def CorrelationType(self, type: CSDExcitation.CorrelationType):
        """
        Setter for property: (@link CSDExcitation.CorrelationType NXOpen.CAE.ResponseSimulation.CSDExcitation.CorrelationType@endlink) CorrelationType
         Returns the correlation type   
            
         
        """
        pass
    
    ## Getter for property: (float) CorrelationValue
    ##  Returns the correlation type   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def CorrelationValue(self) -> float:
        """
        Getter for property: (float) CorrelationValue
         Returns the correlation type   
            
         
        """
        pass
    
    ## Setter for property: (float) CorrelationValue

    ##  Returns the correlation type   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @CorrelationValue.setter
    def CorrelationValue(self, correlationValue: float):
        """
        Setter for property: (float) CorrelationValue
         Returns the correlation type   
            
         
        """
        pass
    
    ##  Returns the from function 
    ##  @return A tuple consisting of (fromExcitation, componentType). 
    ##  - fromExcitation is: @link Excitation NXOpen.CAE.ResponseSimulation.Excitation@endlink. .
    ##  - componentType is: @link Excitation.Component NXOpen.CAE.ResponseSimulation.Excitation.Component@endlink. .

    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetFromFunction(self) -> Tuple[Excitation, Excitation.Component]:
        """
         Returns the from function 
         @return A tuple consisting of (fromExcitation, componentType). 
         - fromExcitation is: @link Excitation NXOpen.CAE.ResponseSimulation.Excitation@endlink. .
         - componentType is: @link Excitation.Component NXOpen.CAE.ResponseSimulation.Excitation.Component@endlink. .

        """
        pass
    
    ##  Returns the to function 
    ##  @return A tuple consisting of (toExcitation, componentType). 
    ##  - toExcitation is: @link Excitation NXOpen.CAE.ResponseSimulation.Excitation@endlink. .
    ##  - componentType is: @link Excitation.Component NXOpen.CAE.ResponseSimulation.Excitation.Component@endlink. .

    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetToFunction(self) -> Tuple[Excitation, Excitation.Component]:
        """
         Returns the to function 
         @return A tuple consisting of (toExcitation, componentType). 
         - toExcitation is: @link Excitation NXOpen.CAE.ResponseSimulation.Excitation@endlink. .
         - componentType is: @link Excitation.Component NXOpen.CAE.ResponseSimulation.Excitation.Component@endlink. .

        """
        pass
    
    ##  Sets the from function 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="fromExcitation"> (@link Excitation NXOpen.CAE.ResponseSimulation.Excitation@endlink)  </param>
    ## <param name="componentType"> (@link Excitation.Component NXOpen.CAE.ResponseSimulation.Excitation.Component@endlink)  </param>
    def SetFromFunction(self, fromExcitation: Excitation, componentType: Excitation.Component) -> None:
        """
         Sets the from function 
        """
        pass
    
    ##  Sets the to function 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="toExcitation"> (@link Excitation NXOpen.CAE.ResponseSimulation.Excitation@endlink)  </param>
    ## <param name="componentType"> (@link Excitation.Component NXOpen.CAE.ResponseSimulation.Excitation.Component@endlink)  </param>
    def SetToFunction(self, toExcitation: Excitation, componentType: Excitation.Component) -> None:
        """
         Sets the to function 
        """
        pass
    
##  Represents an CSD excitation. CSD excitation could only be used by CSD event.  <br> To create or edit an instance of this class, use @link NXOpen::CAE::ResponseSimulation::CSDExcitationBuilder  NXOpen::CAE::ResponseSimulation::CSDExcitationBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class CSDExcitation(Excitation): 
    """ Represents an CSD excitation. CSD excitation could only be used by CSD event. """


    ## Represents the correlation type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## PhaseAngle</term><description> 
    ##  </description> </item><item><term> 
    ## TimeDelay</term><description> 
    ##  </description> </item></list>
    class CorrelationType(Enum):
        """
        Members Include: <PhaseAngle> <TimeDelay>
        """
        PhaseAngle: int
        TimeDelay: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CSDExcitation.CorrelationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
import NXOpen
##  Represents the data location to perform evaluation 
## 
##   <br>  Created in NX5.0.0  <br> 

class DataLocation(NXOpen.TaggedObject): 
    """ Represents the data location to perform evaluation """


    ##  Specifies the location for beam 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## C</term><description> 
    ##   </description> </item><item><term> 
    ## D</term><description> 
    ##   </description> </item><item><term> 
    ## E</term><description> 
    ##   </description> </item><item><term> 
    ## F</term><description> 
    ##   </description> </item></list>
    class Beam(Enum):
        """
        Members Include: <C> <D> <E> <F>
        """
        C: int
        D: int
        E: int
        F: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DataLocation.Beam:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Specifies the element location for element 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Both</term><description> 
    ##   </description> </item><item><term> 
    ## Centroid</term><description> 
    ##   </description> </item><item><term> 
    ## Corners</term><description> 
    ##   </description> </item></list>
    class Element(Enum):
        """
        Members Include: <Both> <Centroid> <Corners>
        """
        Both: int
        Centroid: int
        Corners: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DataLocation.Element:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Specifies the location for shell 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Top</term><description> 
    ##   </description> </item><item><term> 
    ## Bottom</term><description> 
    ##   </description> </item><item><term> 
    ## Middle</term><description> 
    ##   </description> </item></list>
    class Shell(Enum):
        """
        Members Include: <Top> <Bottom> <Middle>
        """
        Top: int
        Bottom: int
        Middle: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DataLocation.Shell:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link DataLocation.Beam NXOpen.CAE.ResponseSimulation.DataLocation.Beam@endlink) BeamLocation
    ##  Returns the method to define frequency  
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return DataLocation.Beam
    @property
    def BeamLocation(self) -> DataLocation.Beam:
        """
        Getter for property: (@link DataLocation.Beam NXOpen.CAE.ResponseSimulation.DataLocation.Beam@endlink) BeamLocation
         Returns the method to define frequency  
            
         
        """
        pass
    
    ## Setter for property: (@link DataLocation.Beam NXOpen.CAE.ResponseSimulation.DataLocation.Beam@endlink) BeamLocation

    ##  Returns the method to define frequency  
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @BeamLocation.setter
    def BeamLocation(self, beam_location: DataLocation.Beam):
        """
        Setter for property: (@link DataLocation.Beam NXOpen.CAE.ResponseSimulation.DataLocation.Beam@endlink) BeamLocation
         Returns the method to define frequency  
            
         
        """
        pass
    
    ## Getter for property: (@link DataLocation.Element NXOpen.CAE.ResponseSimulation.DataLocation.Element@endlink) ElementLocation
    ##  Returns the element location.  
    ##    Only available when stress and strain is defined
    ##         by @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange@endlink    
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return DataLocation.Element
    @property
    def ElementLocation(self) -> DataLocation.Element:
        """
        Getter for property: (@link DataLocation.Element NXOpen.CAE.ResponseSimulation.DataLocation.Element@endlink) ElementLocation
         Returns the element location.  
           Only available when stress and strain is defined
                by @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange@endlink    
         
        """
        pass
    
    ## Setter for property: (@link DataLocation.Element NXOpen.CAE.ResponseSimulation.DataLocation.Element@endlink) ElementLocation

    ##  Returns the element location.  
    ##    Only available when stress and strain is defined
    ##         by @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange@endlink    
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @ElementLocation.setter
    def ElementLocation(self, element_location: DataLocation.Element):
        """
        Setter for property: (@link DataLocation.Element NXOpen.CAE.ResponseSimulation.DataLocation.Element@endlink) ElementLocation
         Returns the element location.  
           Only available when stress and strain is defined
                by @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange@endlink    
         
        """
        pass
    
    ## Getter for property: (int) LayerSelection
    ##  Returns the end value of frequency range.  
    ##    Only available when the frequency is defined 
    ##         by @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange@endlink    
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def LayerSelection(self) -> int:
        """
        Getter for property: (int) LayerSelection
         Returns the end value of frequency range.  
           Only available when the frequency is defined 
                by @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange@endlink    
         
        """
        pass
    
    ## Setter for property: (int) LayerSelection

    ##  Returns the end value of frequency range.  
    ##    Only available when the frequency is defined 
    ##         by @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange@endlink    
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @LayerSelection.setter
    def LayerSelection(self, layer_number: int):
        """
        Setter for property: (int) LayerSelection
         Returns the end value of frequency range.  
           Only available when the frequency is defined 
                by @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange@endlink    
         
        """
        pass
    
    ## Getter for property: (@link DataLocation.Shell NXOpen.CAE.ResponseSimulation.DataLocation.Shell@endlink) ShellLocation
    ##  Returns the start value of frequency range.  
    ##    Only available when the frequency is defined
    ##         by @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange@endlink    
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return DataLocation.Shell
    @property
    def ShellLocation(self) -> DataLocation.Shell:
        """
        Getter for property: (@link DataLocation.Shell NXOpen.CAE.ResponseSimulation.DataLocation.Shell@endlink) ShellLocation
         Returns the start value of frequency range.  
           Only available when the frequency is defined
                by @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange@endlink    
         
        """
        pass
    
    ## Setter for property: (@link DataLocation.Shell NXOpen.CAE.ResponseSimulation.DataLocation.Shell@endlink) ShellLocation

    ##  Returns the start value of frequency range.  
    ##    Only available when the frequency is defined
    ##         by @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange@endlink    
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ShellLocation.setter
    def ShellLocation(self, shell_location: DataLocation.Shell):
        """
        Setter for property: (@link DataLocation.Shell NXOpen.CAE.ResponseSimulation.DataLocation.Shell@endlink) ShellLocation
         Returns the start value of frequency range.  
           Only available when the frequency is defined
                by @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange@endlink    
         
        """
        pass
    
import NXOpen
##  Represents an excitation on one specified direction. 
## 
##   <br>  Created in NX5.0.0  <br> 

class DDAMComponentData(NXOpen.TaggedObject): 
    """ Represents an excitation on one specified direction. """


    ##  Specifies the loading type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Vertical</term><description> 
    ##   </description> </item><item><term> 
    ## Athwartship</term><description> 
    ##   </description> </item><item><term> 
    ## ForeAndAft</term><description> 
    ##   </description> </item></list>
    class LoadingType(Enum):
        """
        Members Include: <Vertical> <Athwartship> <ForeAndAft>
        """
        Vertical: int
        Athwartship: int
        ForeAndAft: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DDAMComponentData.LoadingType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Specifies the response type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Elastic</term><description> 
    ##   </description> </item><item><term> 
    ## ElasticPlastic</term><description> 
    ##   </description> </item></list>
    class ResponseType(Enum):
        """
        Members Include: <Elastic> <ElasticPlastic>
        """
        Elastic: int
        ElasticPlastic: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DDAMComponentData.ResponseType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link DDAMComponentData.LoadingType NXOpen.CAE.ResponseSimulation.DDAMComponentData.LoadingType@endlink) LoadingTypeOption
    ##  Returns the option of loading type   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return DDAMComponentData.LoadingType
    @property
    def LoadingTypeOption(self) -> DDAMComponentData.LoadingType:
        """
        Getter for property: (@link DDAMComponentData.LoadingType NXOpen.CAE.ResponseSimulation.DDAMComponentData.LoadingType@endlink) LoadingTypeOption
         Returns the option of loading type   
            
         
        """
        pass
    
    ## Setter for property: (@link DDAMComponentData.LoadingType NXOpen.CAE.ResponseSimulation.DDAMComponentData.LoadingType@endlink) LoadingTypeOption

    ##  Returns the option of loading type   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @LoadingTypeOption.setter
    def LoadingTypeOption(self, loading_type: DDAMComponentData.LoadingType):
        """
        Setter for property: (@link DDAMComponentData.LoadingType NXOpen.CAE.ResponseSimulation.DDAMComponentData.LoadingType@endlink) LoadingTypeOption
         Returns the option of loading type   
            
         
        """
        pass
    
    ## Getter for property: (@link DDAMComponentData.ResponseType NXOpen.CAE.ResponseSimulation.DDAMComponentData.ResponseType@endlink) ResponseTypeOption
    ##  Returns the option of response type   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return DDAMComponentData.ResponseType
    @property
    def ResponseTypeOption(self) -> DDAMComponentData.ResponseType:
        """
        Getter for property: (@link DDAMComponentData.ResponseType NXOpen.CAE.ResponseSimulation.DDAMComponentData.ResponseType@endlink) ResponseTypeOption
         Returns the option of response type   
            
         
        """
        pass
    
    ## Setter for property: (@link DDAMComponentData.ResponseType NXOpen.CAE.ResponseSimulation.DDAMComponentData.ResponseType@endlink) ResponseTypeOption

    ##  Returns the option of response type   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ResponseTypeOption.setter
    def ResponseTypeOption(self, response_type: DDAMComponentData.ResponseType):
        """
        Setter for property: (@link DDAMComponentData.ResponseType NXOpen.CAE.ResponseSimulation.DDAMComponentData.ResponseType@endlink) ResponseTypeOption
         Returns the option of response type   
            
         
        """
        pass
    
    ##  Returns the component type 
    ##  @return componentType (@link Excitation.Component NXOpen.CAE.ResponseSimulation.Excitation.Component@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetComponentType(self) -> Excitation.Component:
        """
         Returns the component type 
         @return componentType (@link Excitation.Component NXOpen.CAE.ResponseSimulation.Excitation.Component@endlink):  .
        """
        pass
    
    ##  Returns the enable option 
    ##  @return enable (bool):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetEnable(self) -> bool:
        """
         Returns the enable option 
         @return enable (bool):  .
        """
        pass
    
##  Represents the manager to @link NXOpen::CAE::ResponseSimulation::DDAMExcitation NXOpen::CAE::ResponseSimulation::DDAMExcitation@endlink .
##      The object of type @link NXOpen::CAE::ResponseSimulation::DDAMExcitation NXOpen::CAE::ResponseSimulation::DDAMExcitation@endlink  can only
##     be created or edited through this class.  <br> To create a new instance of this class, use @link NXOpen::CAE::ResponseSimulation::ExcitationCollection::CreateDdamExcitationBuilder  NXOpen::CAE::ResponseSimulation::ExcitationCollection::CreateDdamExcitationBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class DDAMExcitationBuilder(ExcitationBuilder): 
    """ Represents the manager to <ja_class>NXOpen.CAE.ResponseSimulation.DDAMExcitation</ja_class>.
     The object of type <ja_class>NXOpen.CAE.ResponseSimulation.DDAMExcitation</ja_class> can only
    be created or edited through this class. """


    ## Getter for property: (@link DDAMExcitation.LoadingType NXOpen.CAE.ResponseSimulation.DDAMExcitation.LoadingType@endlink) LoadingType
    ##  Returns the loading type  
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return DDAMExcitation.LoadingType
    @property
    def LoadingType(self) -> DDAMExcitation.LoadingType:
        """
        Getter for property: (@link DDAMExcitation.LoadingType NXOpen.CAE.ResponseSimulation.DDAMExcitation.LoadingType@endlink) LoadingType
         Returns the loading type  
            
         
        """
        pass
    
    ## Setter for property: (@link DDAMExcitation.LoadingType NXOpen.CAE.ResponseSimulation.DDAMExcitation.LoadingType@endlink) LoadingType

    ##  Returns the loading type  
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @LoadingType.setter
    def LoadingType(self, loading_type: DDAMExcitation.LoadingType):
        """
        Setter for property: (@link DDAMExcitation.LoadingType NXOpen.CAE.ResponseSimulation.DDAMExcitation.LoadingType@endlink) LoadingType
         Returns the loading type  
            
         
        """
        pass
    
    ## Getter for property: (@link DDAMExcitation.ResponseType NXOpen.CAE.ResponseSimulation.DDAMExcitation.ResponseType@endlink) ResponseType
    ##  Returns the response type  
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return DDAMExcitation.ResponseType
    @property
    def ResponseType(self) -> DDAMExcitation.ResponseType:
        """
        Getter for property: (@link DDAMExcitation.ResponseType NXOpen.CAE.ResponseSimulation.DDAMExcitation.ResponseType@endlink) ResponseType
         Returns the response type  
            
         
        """
        pass
    
    ## Setter for property: (@link DDAMExcitation.ResponseType NXOpen.CAE.ResponseSimulation.DDAMExcitation.ResponseType@endlink) ResponseType

    ##  Returns the response type  
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ResponseType.setter
    def ResponseType(self, response_type: DDAMExcitation.ResponseType):
        """
        Setter for property: (@link DDAMExcitation.ResponseType NXOpen.CAE.ResponseSimulation.DDAMExcitation.ResponseType@endlink) ResponseType
         Returns the response type  
            
         
        """
        pass
    
    ##  Returns the status of a dierction component 
    ##  @return enable (bool):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="component"> (@link Excitation.Component NXOpen.CAE.ResponseSimulation.Excitation.Component@endlink)  </param>
    def GetComponentStatus(self, component: Excitation.Component) -> bool:
        """
         Returns the status of a dierction component 
         @return enable (bool):  .
        """
        pass
    
    ##  Sets the status for a direction component
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="component"> (@link Excitation.Component NXOpen.CAE.ResponseSimulation.Excitation.Component@endlink)  </param>
    ## <param name="enable"> (bool)  </param>
    def SetComponentStatus(self, component: Excitation.Component, enable: bool) -> None:
        """
         Sets the status for a direction component
        """
        pass
    
##  Represents an DDAM excitation. DDAM excitation could only be used by DDAM event.  <br> To create or edit an instance of this class, use @link NXOpen::CAE::ResponseSimulation::DDAMExcitationBuilder  NXOpen::CAE::ResponseSimulation::DDAMExcitationBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class DDAMExcitation(Excitation): 
    """ Represents an DDAM excitation. DDAM excitation could only be used by DDAM event. """


    ##  the choices of define DDAM coefficients. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ByFile</term><description> 
    ##  Get the DDAM coefficients from a DDAM coefficient file </description> </item><item><term> 
    ## InputManually</term><description> 
    ##  Input the DDAM coefficient manually </description> </item></list>
    class CoefficientDefinitionType(Enum):
        """
        Members Include: <ByFile> <InputManually>
        """
        ByFile: int
        InputManually: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DDAMExcitation.CoefficientDefinitionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Specifies the loading type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Vertical</term><description> 
    ##   </description> </item><item><term> 
    ## Athwartship</term><description> 
    ##   </description> </item><item><term> 
    ## ForeAndAft</term><description> 
    ##   </description> </item></list>
    class LoadingType(Enum):
        """
        Members Include: <Vertical> <Athwartship> <ForeAndAft>
        """
        Vertical: int
        Athwartship: int
        ForeAndAft: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DDAMExcitation.LoadingType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Specifies the mounting type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Hull</term><description> 
    ##   </description> </item><item><term> 
    ## Duck</term><description> 
    ##   </description> </item><item><term> 
    ## ShellPlating</term><description> 
    ##   </description> </item></list>
    class MountingType(Enum):
        """
        Members Include: <Hull> <Duck> <ShellPlating>
        """
        Hull: int
        Duck: int
        ShellPlating: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DDAMExcitation.MountingType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Specifies the response type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Elastic</term><description> 
    ##   </description> </item><item><term> 
    ## ElasticPlastic</term><description> 
    ##   </description> </item></list>
    class ResponseType(Enum):
        """
        Members Include: <Elastic> <ElasticPlastic>
        """
        Elastic: int
        ElasticPlastic: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DDAMExcitation.ResponseType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Specifies the ship type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Surface</term><description> 
    ##   </description> </item><item><term> 
    ## Submarine</term><description> 
    ##   </description> </item></list>
    class ShipType(Enum):
        """
        Members Include: <Surface> <Submarine>
        """
        Surface: int
        Submarine: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DDAMExcitation.ShipType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
##  Specifies the direction data components 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## X</term><description> 
##  </description> </item><item><term> 
## Y</term><description> 
##  </description> </item><item><term> 
## Z</term><description> 
##  </description> </item><item><term> 
## Rx</term><description> 
##  </description> </item><item><term> 
## Ry</term><description> 
##  </description> </item><item><term> 
## Rz</term><description> 
##  </description> </item><item><term> 
## Xx</term><description> 
##  </description> </item><item><term> 
## Yy</term><description> 
##  </description> </item><item><term> 
## Zz</term><description> 
##  </description> </item><item><term> 
## Xy</term><description> 
##  </description> </item><item><term> 
## Xz</term><description> 
##  </description> </item><item><term> 
## Yz</term><description> 
##  </description> </item><item><term> 
## Ax</term><description> 
##  </description> </item><item><term> 
## Sy</term><description> 
##  </description> </item><item><term> 
## Sz</term><description> 
##  </description> </item><item><term> 
## Tx</term><description> 
##  </description> </item><item><term> 
## Byy</term><description> 
##  </description> </item><item><term> 
## Bz</term><description> 
##  </description> </item><item><term> 
## Fxx</term><description> 
##  </description> </item><item><term> 
## Fyy</term><description> 
##  </description> </item><item><term> 
## Fzz</term><description> 
##  </description> </item><item><term> 
## Fxy</term><description> 
##  </description> </item><item><term> 
## Mx</term><description> 
##  </description> </item><item><term> 
## My</term><description> 
##  </description> </item><item><term> 
## Mz</term><description> 
##  </description> </item><item><term> 
## Mxy</term><description> 
##  </description> </item><item><term> 
## Mxz</term><description> 
##  </description> </item><item><term> 
## Myz</term><description> 
##  </description> </item><item><term> 
## Vx</term><description> 
##  </description> </item><item><term> 
## Vy</term><description> 
##  </description> </item><item><term> 
## TranslationalMagnitude</term><description> 
##  </description> </item><item><term> 
## Vonmises</term><description> 
##  </description> </item><item><term> 
## MaxPrincipal</term><description> 
##  </description> </item><item><term> 
## MinPrincipal</term><description> 
##  </description> </item><item><term> 
## MaxShear</term><description> 
##  </description> </item><item><term> 
## AllNormals</term><description> 
##  </description> </item><item><term> 
## AllTranslational</term><description> 
##  </description> </item><item><term> 
## AllForces</term><description> 
##  </description> </item><item><term> 
## AllDirections</term><description> 
##  </description> </item><item><term> 
## AllDataComponents</term><description> 
##  </description> </item><item><term> 
## All</term><description> 
##  </description> </item><item><term> 
## AllXyPlane</term><description> 
##  </description> </item><item><term> 
## Leg1</term><description> 
##  </description> </item><item><term> 
## Leg2</term><description> 
##  </description> </item><item><term> 
## Leg3</term><description> 
##  </description> </item><item><term> 
## AllLegs</term><description> 
##  </description> </item></list>
class DirectionDataComponent(Enum):
    """
    Members Include: <X> <Y> <Z> <Rx> <Ry> <Rz> <Xx> <Yy> <Zz> <Xy> <Xz> <Yz> <Ax> <Sy> <Sz> <Tx> <Byy> <Bz> <Fxx> <Fyy> <Fzz> <Fxy> <Mx> <My> <Mz> <Mxy> <Mxz> <Myz> <Vx> <Vy> <TranslationalMagnitude> <Vonmises> <MaxPrincipal> <MinPrincipal> <MaxShear> <AllNormals> <AllTranslational> <AllForces> <AllDirections> <AllDataComponents> <All> <AllXyPlane> <Leg1> <Leg2> <Leg3> <AllLegs>
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
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> DirectionDataComponent:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the manager to @link NXOpen::CAE::ResponseSimulation::DistributedLoadExcitation NXOpen::CAE::ResponseSimulation::DistributedLoadExcitation@endlink .
##      The object of type @link NXOpen::CAE::ResponseSimulation::DistributedLoadExcitation NXOpen::CAE::ResponseSimulation::DistributedLoadExcitation@endlink 
##       can only be created or edited through this class.
##       <br> To create a new instance of this class, use @link NXOpen::CAE::ResponseSimulation::ExcitationCollection::CreateDistributedLoadExcitationBuilder  NXOpen::CAE::ResponseSimulation::ExcitationCollection::CreateDistributedLoadExcitationBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class DistributedLoadExcitationBuilder(ExcitationBuilder): 
    """ Represents the manager to <ja_class>NXOpen.CAE.ResponseSimulation.DistributedLoadExcitation</ja_class>.
     The object of type <ja_class>NXOpen.CAE.ResponseSimulation.DistributedLoadExcitation</ja_class>
      can only be created or edited through this class.
     """


    ## Getter for property: (@link FunctionComponentData NXOpen.CAE.ResponseSimulation.FunctionComponentData@endlink) ExcitationFunction
    ##  Returns the magnitude function   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return FunctionComponentData
    @property
    def ExcitationFunction(self) -> FunctionComponentData:
        """
        Getter for property: (@link FunctionComponentData NXOpen.CAE.ResponseSimulation.FunctionComponentData@endlink) ExcitationFunction
         Returns the magnitude function   
            
         
        """
        pass
    
##  Represents an excitation of distributed-load type  <br> To create or edit an instance of this class, use @link NXOpen::CAE::ResponseSimulation::DistributedLoadExcitationBuilder  NXOpen::CAE::ResponseSimulation::DistributedLoadExcitationBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class DistributedLoadExcitation(Excitation): 
    """ Represents an excitation of distributed-load type """
    pass


import NXOpen
##  Represents the output setting for dynamic response evaluation
## 
##   <br>  Created in NX5.0.0  <br> 

class DynamicEvaluationOutputSettings(NXOpen.TaggedObject): 
    """ Represents the output setting for dynamic response evaluation"""


    ## Getter for property: (bool) PreviewOption
    ##  Returns the preview option.  
    ##    If true, the evaluation results will be previewed by plot and not saved to disk until
    ##          you confirm to save them   
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def PreviewOption(self) -> bool:
        """
        Getter for property: (bool) PreviewOption
         Returns the preview option.  
           If true, the evaluation results will be previewed by plot and not saved to disk until
                 you confirm to save them   
         
        """
        pass
    
    ## Setter for property: (bool) PreviewOption

    ##  Returns the preview option.  
    ##    If true, the evaluation results will be previewed by plot and not saved to disk until
    ##          you confirm to save them   
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @PreviewOption.setter
    def PreviewOption(self, preview_option: bool):
        """
        Setter for property: (bool) PreviewOption
         Returns the preview option.  
           If true, the evaluation results will be previewed by plot and not saved to disk until
                 you confirm to save them   
         
        """
        pass
    
    ## Getter for property: (str) RecordPrefix
    ##  Returns the prefix of evaluation results record name   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return str
    @property
    def RecordPrefix(self) -> str:
        """
        Getter for property: (str) RecordPrefix
         Returns the prefix of evaluation results record name   
            
         
        """
        pass
    
    ## Setter for property: (str) RecordPrefix

    ##  Returns the prefix of evaluation results record name   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @RecordPrefix.setter
    def RecordPrefix(self, record_prefix: str):
        """
        Setter for property: (str) RecordPrefix
         Returns the prefix of evaluation results record name   
            
         
        """
        pass
    
import NXOpen
##  Represents the abstract builder class of evaluation setting for all dynamic results evaluations.
##      <br> This is an abstract class, and cannot be created.  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class DynamicResultEvaluationSettingBuilder(NXOpen.Builder): 
    """ Represents the abstract builder class of evaluation setting for all dynamic results evaluations.
    """


    ##  Returns the description. 
    ##  @return description (List[str]): .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetDescriptionString(self) -> List[str]:
        """
         Returns the description. 
         @return description (List[str]): .
        """
        pass
    
    ##  Returns the response result name. 
    ##  @return responseResultName (str): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetResponseResultNameString(self) -> str:
        """
         Returns the response result name. 
         @return responseResultName (str): .
        """
        pass
    
    ##  Sets the description 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="description"> (List[str])  </param>
    def SetDescriptionString(self, description: List[str]) -> None:
        """
         Sets the description 
        """
        pass
    
    ##  Sets the response result name 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="responseResultName"> (str)  </param>
    def SetResponseResultNameString(self, responseResultName: str) -> None:
        """
         Sets the response result name 
        """
        pass
    
##  Represents the abstract class of evaluation setting for all dynamic results evaluations.
##      <br> This is an abstract class, and cannot be created.  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class DynamicResultEvaluationSetting(EvaluationSetting): 
    """ Represents the abstract class of evaluation setting for all dynamic results evaluations.
    """
    pass


##  Specifies beam element evaluation locations 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## C</term><description> 
##  </description> </item><item><term> 
## D</term><description> 
##  </description> </item><item><term> 
## E</term><description> 
##  </description> </item><item><term> 
## F</term><description> 
##  </description> </item></list>
class ElementalFunctionEvalBeamLocation(Enum):
    """
    Members Include: <C> <D> <E> <F>
    """
    C: int
    D: int
    E: int
    F: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> ElementalFunctionEvalBeamLocation:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen.CAE
##  This is a manager to the @link NXOpen::CAE::ResponseSimulation::ElementalFunctionEvaluationSetting NXOpen::CAE::ResponseSimulation::ElementalFunctionEvaluationSetting@endlink  class. 
##     Object of type @link NXOpen::CAE::ResponseSimulation::ElementalFunctionEvaluationSetting NXOpen::CAE::ResponseSimulation::ElementalFunctionEvaluationSetting@endlink  can be 
##     created and edited only through this class
##       <br> To create a new instance of this class, use @link NXOpen::CAE::ResponseSimulation::EvaluationSettingManager::CreateElementalFunctionEvaluationSettingBuilder  NXOpen::CAE::ResponseSimulation::EvaluationSettingManager::CreateElementalFunctionEvaluationSettingBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class ElementalFunctionEvaluationSettingBuilder(FunctionEvaluationSettingBuilder): 
    """ This is a manager to the <ja_class>NXOpen.CAE.ResponseSimulation.ElementalFunctionEvaluationSetting</ja_class> class. 
    Object of type <ja_class>NXOpen.CAE.ResponseSimulation.ElementalFunctionEvaluationSetting</ja_class> can be 
    created and edited only through this class
     """


    ## Getter for property: (@link ElementalFunctionEvalBeamLocation NXOpen.CAE.ResponseSimulation.ElementalFunctionEvalBeamLocation@endlink) BeamDataLocation
    ##  Returns the data location of beam element.  
    ##    For more information about beam data location,
    ##         see the Response Simulatin section of the Gateway help   
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return ElementalFunctionEvalBeamLocation
    @property
    def BeamDataLocation(self) -> ElementalFunctionEvalBeamLocation:
        """
        Getter for property: (@link ElementalFunctionEvalBeamLocation NXOpen.CAE.ResponseSimulation.ElementalFunctionEvalBeamLocation@endlink) BeamDataLocation
         Returns the data location of beam element.  
           For more information about beam data location,
                see the Response Simulatin section of the Gateway help   
         
        """
        pass
    
    ## Setter for property: (@link ElementalFunctionEvalBeamLocation NXOpen.CAE.ResponseSimulation.ElementalFunctionEvalBeamLocation@endlink) BeamDataLocation

    ##  Returns the data location of beam element.  
    ##    For more information about beam data location,
    ##         see the Response Simulatin section of the Gateway help   
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @BeamDataLocation.setter
    def BeamDataLocation(self, beam_location: ElementalFunctionEvalBeamLocation):
        """
        Setter for property: (@link ElementalFunctionEvalBeamLocation NXOpen.CAE.ResponseSimulation.ElementalFunctionEvalBeamLocation@endlink) BeamDataLocation
         Returns the data location of beam element.  
           For more information about beam data location,
                see the Response Simulatin section of the Gateway help   
         
        """
        pass
    
    ## Getter for property: (@link CoordinateSystem NXOpen.CAE.ResponseSimulation.CoordinateSystem@endlink) CoordinateSystem
    ##  Returns the coordinate system   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return CoordinateSystem
    @property
    def CoordinateSystem(self) -> CoordinateSystem:
        """
        Getter for property: (@link CoordinateSystem NXOpen.CAE.ResponseSimulation.CoordinateSystem@endlink) CoordinateSystem
         Returns the coordinate system   
            
         
        """
        pass
    
    ## Setter for property: (@link CoordinateSystem NXOpen.CAE.ResponseSimulation.CoordinateSystem@endlink) CoordinateSystem

    ##  Returns the coordinate system   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @CoordinateSystem.setter
    def CoordinateSystem(self, coordinate_system: CoordinateSystem):
        """
        Setter for property: (@link CoordinateSystem NXOpen.CAE.ResponseSimulation.CoordinateSystem@endlink) CoordinateSystem
         Returns the coordinate system   
            
         
        """
        pass
    
    ## Getter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) DataComponent
    ##  Returns the data component of direction   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return DirectionDataComponent
    @property
    def DataComponent(self) -> DirectionDataComponent:
        """
        Getter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) DataComponent
         Returns the data component of direction   
            
         
        """
        pass
    
    ## Setter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) DataComponent

    ##  Returns the data component of direction   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @DataComponent.setter
    def DataComponent(self, data_component: DirectionDataComponent):
        """
        Setter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) DataComponent
         Returns the data component of direction   
            
         
        """
        pass
    
    ## Getter for property: (@link ElementLocation NXOpen.CAE.ResponseSimulation.ElementLocation@endlink) ElementLocation
    ##  Returns the evaluation location of element.  
    ##      
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return ElementLocation
    @property
    def ElementLocation(self) -> ElementLocation:
        """
        Getter for property: (@link ElementLocation NXOpen.CAE.ResponseSimulation.ElementLocation@endlink) ElementLocation
         Returns the evaluation location of element.  
             
         
        """
        pass
    
    ## Setter for property: (@link ElementLocation NXOpen.CAE.ResponseSimulation.ElementLocation@endlink) ElementLocation

    ##  Returns the evaluation location of element.  
    ##      
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @ElementLocation.setter
    def ElementLocation(self, element_location: ElementLocation):
        """
        Setter for property: (@link ElementLocation NXOpen.CAE.ResponseSimulation.ElementLocation@endlink) ElementLocation
         Returns the evaluation location of element.  
             
         
        """
        pass
    
    ## Getter for property: (@link ShellElementEvaluationLocation NXOpen.CAE.ResponseSimulation.ShellElementEvaluationLocation@endlink) ShellEvaluationLocation
    ##  Returns the evaluation location of shell element.  
    ##      
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return ShellElementEvaluationLocation
    @property
    def ShellEvaluationLocation(self) -> ShellElementEvaluationLocation:
        """
        Getter for property: (@link ShellElementEvaluationLocation NXOpen.CAE.ResponseSimulation.ShellElementEvaluationLocation@endlink) ShellEvaluationLocation
         Returns the evaluation location of shell element.  
             
         
        """
        pass
    
    ## Setter for property: (@link ShellElementEvaluationLocation NXOpen.CAE.ResponseSimulation.ShellElementEvaluationLocation@endlink) ShellEvaluationLocation

    ##  Returns the evaluation location of shell element.  
    ##      
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ShellEvaluationLocation.setter
    def ShellEvaluationLocation(self, shell_location: ShellElementEvaluationLocation):
        """
        Setter for property: (@link ShellElementEvaluationLocation NXOpen.CAE.ResponseSimulation.ShellElementEvaluationLocation@endlink) ShellEvaluationLocation
         Returns the evaluation location of shell element.  
             
         
        """
        pass
    
    ## Getter for property: (bool) SpringForceEvaluationFromDisplacement
    ##  Returns the spring force evaluation From displacement flag.  
    ##      
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def SpringForceEvaluationFromDisplacement(self) -> bool:
        """
        Getter for property: (bool) SpringForceEvaluationFromDisplacement
         Returns the spring force evaluation From displacement flag.  
             
         
        """
        pass
    
    ## Setter for property: (bool) SpringForceEvaluationFromDisplacement

    ##  Returns the spring force evaluation From displacement flag.  
    ##      
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @SpringForceEvaluationFromDisplacement.setter
    def SpringForceEvaluationFromDisplacement(self, spring_force_evaluation_from_displacement: bool):
        """
        Setter for property: (bool) SpringForceEvaluationFromDisplacement
         Returns the spring force evaluation From displacement flag.  
             
         
        """
        pass
    
    ##  Returns the destination elements 
    ##  @return destination_elements (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetDestinationElements(self) -> List[NXOpen.CAE.FEElement]:
        """
         Returns the destination elements 
         @return destination_elements (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink):  .
        """
        pass
    
    ##  Sets the destination elements 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="destination_element"> (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink)  </param>
    def SetDestinationElements(self, destination_element: List[NXOpen.CAE.FEElement]) -> None:
        """
         Sets the destination elements 
        """
        pass
    
## Represents the parameters setting for elemental function evaluation. Only available to
##     @link NXOpen::CAE::ResponseSimulation::RSEvent::TypeTransient NXOpen::CAE::ResponseSimulation::RSEvent::TypeTransient@endlink ,
##     @link NXOpen::CAE::ResponseSimulation::RSEvent::TypeFrequency NXOpen::CAE::ResponseSimulation::RSEvent::TypeFrequency@endlink ,
##     @link NXOpen::CAE::ResponseSimulation::RSEvent::TypeRandom NXOpen::CAE::ResponseSimulation::RSEvent::TypeRandom@endlink 
##       <br> To create or edit an instance of this class, use @link NXOpen::CAE::ResponseSimulation::ElementalFunctionEvaluationSettingBuilder  NXOpen::CAE::ResponseSimulation::ElementalFunctionEvaluationSettingBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class ElementalFunctionEvaluationSetting(FunctionEvaluationSetting): 
    """Represents the parameters setting for elemental function evaluation. Only available to
    <ja_enum_member>NXOpen.CAE.ResponseSimulation.RSEvent.Type.Transient</ja_enum_member>,
    <ja_enum_member>NXOpen.CAE.ResponseSimulation.RSEvent.Type.Frequency</ja_enum_member>,
    <ja_enum_member>NXOpen.CAE.ResponseSimulation.RSEvent.Type.Random</ja_enum_member>
     """
    pass


##  Specifies element locations 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Both</term><description> 
##  </description> </item><item><term> 
## Centroid</term><description> 
##  </description> </item><item><term> 
## Corners</term><description> 
##  </description> </item></list>
class ElementLocation(Enum):
    """
    Members Include: <Both> <Centroid> <Corners>
    """
    Both: int
    Centroid: int
    Corners: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> ElementLocation:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##  Represents the evaluation parameters for a response simulation meta solution  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class EvaluationParameters(NXOpen.TaggedObject): 
    """ Represents the evaluation parameters for a response simulation meta solution """


    ##  the integration method used for transient analysis 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## DuhameldIntegral</term><description> 
    ##   </description> </item><item><term> 
    ## NewmarkBeta</term><description> 
    ##   </description> </item></list>
    class AnalysisIntegrationMethod(Enum):
        """
        Members Include: <DuhameldIntegral> <NewmarkBeta>
        """
        DuhameldIntegral: int
        NewmarkBeta: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> EvaluationParameters.AnalysisIntegrationMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (int) HypermatrixBufferSize
    ##  Returns the buffer allocated for Hypermatrix files   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return int
    @property
    def HypermatrixBufferSize(self) -> int:
        """
        Getter for property: (int) HypermatrixBufferSize
         Returns the buffer allocated for Hypermatrix files   
            
         
        """
        pass
    
    ## Setter for property: (int) HypermatrixBufferSize

    ##  Returns the buffer allocated for Hypermatrix files   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @HypermatrixBufferSize.setter
    def HypermatrixBufferSize(self, buffer_size: int):
        """
        Setter for property: (int) HypermatrixBufferSize
         Returns the buffer allocated for Hypermatrix files   
            
         
        """
        pass
    
    ## Getter for property: (@link EvaluationParameters.AnalysisIntegrationMethod NXOpen.CAE.ResponseSimulation.EvaluationParameters.AnalysisIntegrationMethod@endlink) IntegrationMethod
    ##  Returns the integration method used for transient analysis   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return EvaluationParameters.AnalysisIntegrationMethod
    @property
    def IntegrationMethod(self) -> EvaluationParameters.AnalysisIntegrationMethod:
        """
        Getter for property: (@link EvaluationParameters.AnalysisIntegrationMethod NXOpen.CAE.ResponseSimulation.EvaluationParameters.AnalysisIntegrationMethod@endlink) IntegrationMethod
         Returns the integration method used for transient analysis   
            
         
        """
        pass
    
    ## Setter for property: (@link EvaluationParameters.AnalysisIntegrationMethod NXOpen.CAE.ResponseSimulation.EvaluationParameters.AnalysisIntegrationMethod@endlink) IntegrationMethod

    ##  Returns the integration method used for transient analysis   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @IntegrationMethod.setter
    def IntegrationMethod(self, method: EvaluationParameters.AnalysisIntegrationMethod):
        """
        Setter for property: (@link EvaluationParameters.AnalysisIntegrationMethod NXOpen.CAE.ResponseSimulation.EvaluationParameters.AnalysisIntegrationMethod@endlink) IntegrationMethod
         Returns the integration method used for transient analysis   
            
         
        """
        pass
    
    ## Getter for property: (int) MaxArraySize
    ##  Returns the dynamic storage array size allocated for RS evaluations   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return int
    @property
    def MaxArraySize(self) -> int:
        """
        Getter for property: (int) MaxArraySize
         Returns the dynamic storage array size allocated for RS evaluations   
            
         
        """
        pass
    
    ## Setter for property: (int) MaxArraySize

    ##  Returns the dynamic storage array size allocated for RS evaluations   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @MaxArraySize.setter
    def MaxArraySize(self, max_array_size: int):
        """
        Setter for property: (int) MaxArraySize
         Returns the dynamic storage array size allocated for RS evaluations   
            
         
        """
        pass
    
    ## Getter for property: (bool) MinDampingStatus
    ##  Returns the minimum damping ratio status   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def MinDampingStatus(self) -> bool:
        """
        Getter for property: (bool) MinDampingStatus
         Returns the minimum damping ratio status   
            
         
        """
        pass
    
    ## Setter for property: (bool) MinDampingStatus

    ##  Returns the minimum damping ratio status   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @MinDampingStatus.setter
    def MinDampingStatus(self, damping_status: bool):
        """
        Setter for property: (bool) MinDampingStatus
         Returns the minimum damping ratio status   
            
         
        """
        pass
    
    ## Getter for property: (bool) ZeroMeanCorrection
    ##  Returns the time-domain integration of acceleration excitations,
    ##             used in evaluating time responses to acceleration loads.  
    ##    
    ##             false: no correction, meaning that "rigid drifting" shows in the
    ##                    displacement response when an acceleration excitation is applied;
    ##             true:  the software corrects for drifting by assuming a zero mean. Rigid drifting is filtered
    ##                    out based on a numerical integration that does not assume an initial condition.  
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
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
    
    ## Setter for property: (bool) ZeroMeanCorrection

    ##  Returns the time-domain integration of acceleration excitations,
    ##             used in evaluating time responses to acceleration loads.  
    ##    
    ##             false: no correction, meaning that "rigid drifting" shows in the
    ##                    displacement response when an acceleration excitation is applied;
    ##             true:  the software corrects for drifting by assuming a zero mean. Rigid drifting is filtered
    ##                    out based on a numerical integration that does not assume an initial condition.  
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

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
    
##  Specifies the evaluation result type 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Receptance</term><description> 
##  </description> </item><item><term> 
## Mobility</term><description> 
##  </description> </item><item><term> 
## Inertance</term><description> 
##  </description> </item><item><term> 
## Displacement</term><description> 
##  </description> </item><item><term> 
## Velocity</term><description> 
##  </description> </item><item><term> 
## Acceleration</term><description> 
##  </description> </item><item><term> 
## Stress</term><description> 
##  </description> </item><item><term> 
## Strain</term><description> 
##  </description> </item><item><term> 
## StrainEnergy</term><description> 
##  </description> </item><item><term> 
## ShellResultant</term><description> 
##  </description> </item><item><term> 
## ElementForce</term><description> 
##  </description> </item><item><term> 
## BeamElementForce</term><description> 
##  </description> </item><item><term> 
## ShellStressResultant</term><description> 
##  </description> </item><item><term> 
## ReactionForce</term><description> 
##  </description> </item></list>
class EvaluationResultType(Enum):
    """
    Members Include: <Receptance> <Mobility> <Inertance> <Displacement> <Velocity> <Acceleration> <Stress> <Strain> <StrainEnergy> <ShellResultant> <ElementForce> <BeamElementForce> <ShellStressResultant> <ReactionForce>
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
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> EvaluationResultType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##  Represents the abstract builder class of all evaluation setting classes.  <br> This is an abstract class, and cannot be created.  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class EvaluationSettingBuilder(NXOpen.Builder): 
    """ Represents the abstract builder class of all evaluation setting classes. """
    pass


import NXOpen
##  Represents the manager of all evaluation setting objects. Any evaluation setting object must 
##     be created through this class  <br> To obtain an instance of this class, refer to @link NXOpen::CAE::ResponseSimulation::Manager  NXOpen::CAE::ResponseSimulation::Manager @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class EvaluationSettingManager(NXOpen.Object): 
    """ Represents the manager of all evaluation setting objects. Any evaluation setting object must 
    be created through this class """


    ##  Creates CSD evaluation setting object 
    ##  @return builder (@link CsdEvaluationSettingBuilder NXOpen.CAE.ResponseSimulation.CsdEvaluationSettingBuilder@endlink):   .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="setting"> (@link CsdEvaluationSetting NXOpen.CAE.ResponseSimulation.CsdEvaluationSetting@endlink)  </param>
    def CreateCsdEvaluationSettingBuilder(self, setting: CsdEvaluationSetting) -> CsdEvaluationSettingBuilder:
        """
         Creates CSD evaluation setting object 
         @return builder (@link CsdEvaluationSettingBuilder NXOpen.CAE.ResponseSimulation.CsdEvaluationSettingBuilder@endlink):   .
        """
        pass
    
    ##  Creates elemental function evaluation setting object 
    ##  @return builder (@link ElementalFunctionEvaluationSettingBuilder NXOpen.CAE.ResponseSimulation.ElementalFunctionEvaluationSettingBuilder@endlink):   .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="setting"> (@link ElementalFunctionEvaluationSetting NXOpen.CAE.ResponseSimulation.ElementalFunctionEvaluationSetting@endlink)  </param>
    def CreateElementalFunctionEvaluationSettingBuilder(self, setting: ElementalFunctionEvaluationSetting) -> ElementalFunctionEvaluationSettingBuilder:
        """
         Creates elemental function evaluation setting object 
         @return builder (@link ElementalFunctionEvaluationSettingBuilder NXOpen.CAE.ResponseSimulation.ElementalFunctionEvaluationSettingBuilder@endlink):   .
        """
        pass
    
    ##  Creates FRF evaluation setting object 
    ##  @return builder (@link FrfEvaluationSettingBuilder NXOpen.CAE.ResponseSimulation.FrfEvaluationSettingBuilder@endlink):   .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="setting"> (@link FrfEvaluationSetting NXOpen.CAE.ResponseSimulation.FrfEvaluationSetting@endlink)  </param>
    def CreateFrfEvaluationSettingBuilder(self, setting: FrfEvaluationSetting) -> FrfEvaluationSettingBuilder:
        """
         Creates FRF evaluation setting object 
         @return builder (@link FrfEvaluationSettingBuilder NXOpen.CAE.ResponseSimulation.FrfEvaluationSettingBuilder@endlink):   .
        """
        pass
    
    ##  Creates LCR results evaluation setting object 
    ##  @return builder (@link LcrResultsEvaluationSettingBuilder NXOpen.CAE.ResponseSimulation.LcrResultsEvaluationSettingBuilder@endlink):   .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="setting"> (@link LcrResultsEvaluationSetting NXOpen.CAE.ResponseSimulation.LcrResultsEvaluationSetting@endlink)  </param>
    def CreateLcrResultsEvaluationSettingBuilder(self, setting: LcrResultsEvaluationSetting) -> LcrResultsEvaluationSettingBuilder:
        """
         Creates LCR results evaluation setting object 
         @return builder (@link LcrResultsEvaluationSettingBuilder NXOpen.CAE.ResponseSimulation.LcrResultsEvaluationSettingBuilder@endlink):   .
        """
        pass
    
    ##  Creates nodal function evaluation setting object 
    ##  @return builder (@link NodalFunctionEvaluationSettingBuilder NXOpen.CAE.ResponseSimulation.NodalFunctionEvaluationSettingBuilder@endlink):   .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="setting"> (@link NodalFunctionEvaluationSetting NXOpen.CAE.ResponseSimulation.NodalFunctionEvaluationSetting@endlink)  </param>
    def CreateNodalFunctionEvaluationSettingBuilder(self, setting: NodalFunctionEvaluationSetting) -> NodalFunctionEvaluationSettingBuilder:
        """
         Creates nodal function evaluation setting object 
         @return builder (@link NodalFunctionEvaluationSettingBuilder NXOpen.CAE.ResponseSimulation.NodalFunctionEvaluationSettingBuilder@endlink):   .
        """
        pass
    
    ##  Creates peak value evaluation setting object 
    ##  @return builder (@link PeakValueEvaluationSettingBuilder NXOpen.CAE.ResponseSimulation.PeakValueEvaluationSettingBuilder@endlink):   .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="setting"> (@link PeakValueEvaluationSetting NXOpen.CAE.ResponseSimulation.PeakValueEvaluationSetting@endlink)  </param>
    def CreatePeakValueEvaluationSettingBuilder(self, setting: PeakValueEvaluationSetting) -> PeakValueEvaluationSettingBuilder:
        """
         Creates peak value evaluation setting object 
         @return builder (@link PeakValueEvaluationSettingBuilder NXOpen.CAE.ResponseSimulation.PeakValueEvaluationSettingBuilder@endlink):   .
        """
        pass
    
    ##  Creates response results evaluation setting object 
    ##  @return builder (@link ResponseResultsEvaluationSettingBuilder NXOpen.CAE.ResponseSimulation.ResponseResultsEvaluationSettingBuilder@endlink):   .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="setting"> (@link ResponseResultsEvaluationSetting NXOpen.CAE.ResponseSimulation.ResponseResultsEvaluationSetting@endlink)  </param>
    def CreateResponseResultsEvaluationSettingBuilder(self, setting: ResponseResultsEvaluationSetting) -> ResponseResultsEvaluationSettingBuilder:
        """
         Creates response results evaluation setting object 
         @return builder (@link ResponseResultsEvaluationSettingBuilder NXOpen.CAE.ResponseSimulation.ResponseResultsEvaluationSettingBuilder@endlink):   .
        """
        pass
    
    ##  Creates RMS results evaluation setting object 
    ##  @return builder (@link RmsResultsEvaluationSettingBuilder NXOpen.CAE.ResponseSimulation.RmsResultsEvaluationSettingBuilder@endlink):   .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="setting"> (@link RmsResultsEvaluationSetting NXOpen.CAE.ResponseSimulation.RmsResultsEvaluationSetting@endlink)  </param>
    def CreateRmsResultsEvaluationSettingBuilder(self, setting: RmsResultsEvaluationSetting) -> RmsResultsEvaluationSettingBuilder:
        """
         Creates RMS results evaluation setting object 
         @return builder (@link RmsResultsEvaluationSettingBuilder NXOpen.CAE.ResponseSimulation.RmsResultsEvaluationSettingBuilder@endlink):   .
        """
        pass
    
    ##  Creates sensor evaluation setting object 
    ##  @return builder (@link SensorEvaluationSettingBuilder NXOpen.CAE.ResponseSimulation.SensorEvaluationSettingBuilder@endlink):   .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="setting"> (@link SensorEvaluationSetting NXOpen.CAE.ResponseSimulation.SensorEvaluationSetting@endlink)  </param>
    def CreateSensorEvaluationSettingBuilder(self, setting: SensorEvaluationSetting) -> SensorEvaluationSettingBuilder:
        """
         Creates sensor evaluation setting object 
         @return builder (@link SensorEvaluationSettingBuilder NXOpen.CAE.ResponseSimulation.SensorEvaluationSettingBuilder@endlink):   .
        """
        pass
    
    ##  Creates strain gage evaluation setting object 
    ##  @return builder (@link StrainGageEvaluationSettingBuilder NXOpen.CAE.ResponseSimulation.StrainGageEvaluationSettingBuilder@endlink):   .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="setting"> (@link StrainGageEvaluationSetting NXOpen.CAE.ResponseSimulation.StrainGageEvaluationSetting@endlink)  </param>
    def CreateStrainGageEvaluationSettingBuilder(self, setting: StrainGageEvaluationSetting) -> StrainGageEvaluationSettingBuilder:
        """
         Creates strain gage evaluation setting object 
         @return builder (@link StrainGageEvaluationSettingBuilder NXOpen.CAE.ResponseSimulation.StrainGageEvaluationSettingBuilder@endlink):   .
        """
        pass
    
    ##  Creates strength results evaluation setting object 
    ##  @return builder (@link StrengthResultsEvaluationSettingBuilder NXOpen.CAE.ResponseSimulation.StrengthResultsEvaluationSettingBuilder@endlink):   .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="setting"> (@link StrengthResultsEvaluationSetting NXOpen.CAE.ResponseSimulation.StrengthResultsEvaluationSetting@endlink)  </param>
    def CreateStrengthResultsEvaluationSettingBuilder(self, setting: StrengthResultsEvaluationSetting) -> StrengthResultsEvaluationSettingBuilder:
        """
         Creates strength results evaluation setting object 
         @return builder (@link StrengthResultsEvaluationSettingBuilder NXOpen.CAE.ResponseSimulation.StrengthResultsEvaluationSettingBuilder@endlink):   .
        """
        pass
    
    ##  Creates transmissibility evaluation setting object 
    ##  @return builder (@link TransmissibilityEvaluationSettingBuilder NXOpen.CAE.ResponseSimulation.TransmissibilityEvaluationSettingBuilder@endlink):   .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="setting"> (@link TransmissibilityEvaluationSetting NXOpen.CAE.ResponseSimulation.TransmissibilityEvaluationSetting@endlink)  </param>
    def CreateTransmissibilityEvaluationSettingBuilder(self, setting: TransmissibilityEvaluationSetting) -> TransmissibilityEvaluationSettingBuilder:
        """
         Creates transmissibility evaluation setting object 
         @return builder (@link TransmissibilityEvaluationSettingBuilder NXOpen.CAE.ResponseSimulation.TransmissibilityEvaluationSettingBuilder@endlink):   .
        """
        pass
    
import NXOpen
##  Represents the abstract class of all evaluation setting classes.  <br> This is an abstract class, and cannot be created.  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class EvaluationSetting(NXOpen.NXObject): 
    """ Represents the abstract class of all evaluation setting classes. """


    ##  Destroies the evaluation setting object after evaluation. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def Destroy(self) -> None:
        """
         Destroies the evaluation setting object after evaluation. 
        """
        pass
    
##  Represents the abstract excitation builder class. Any of real excitation builder
##         must inherit from this class.
##       <br> This is an abstract class, and cannot be created.  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class ExcitationBuilder(BaseBuilder): 
    """ Represents the abstract excitation builder class. Any of real excitation builder
        must inherit from this class.
     """


    ##  the type of excitation location 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## StaticLoad</term><description> 
    ##   </description> </item><item><term> 
    ## DistributedLoad</term><description> 
    ##   </description> </item><item><term> 
    ## NodalForce</term><description> 
    ##   </description> </item><item><term> 
    ## EnforcedMotion</term><description> 
    ##   </description> </item></list>
    class ExcitationLocationType(Enum):
        """
        Members Include: <StaticLoad> <DistributedLoad> <NodalForce> <EnforcedMotion>
        """
        StaticLoad: int
        DistributedLoad: int
        NodalForce: int
        EnforcedMotion: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ExcitationBuilder.ExcitationLocationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link RSEvent NXOpen.CAE.ResponseSimulation.RSEvent@endlink) DynamicEvent
    ##  Returns the parent dynamic event object   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return RSEvent
    @property
    def DynamicEvent(self) -> RSEvent:
        """
        Getter for property: (@link RSEvent NXOpen.CAE.ResponseSimulation.RSEvent@endlink) DynamicEvent
         Returns the parent dynamic event object   
            
         
        """
        pass
    
    ## Getter for property: (@link ExcitationLocationDefinition NXOpen.CAE.ResponseSimulation.ExcitationLocationDefinition@endlink) ExcitationLocationDefinition
    ##  Returns the excitation location definition   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return ExcitationLocationDefinition
    @property
    def ExcitationLocationDefinition(self) -> ExcitationLocationDefinition:
        """
        Getter for property: (@link ExcitationLocationDefinition NXOpen.CAE.ResponseSimulation.ExcitationLocationDefinition@endlink) ExcitationLocationDefinition
         Returns the excitation location definition   
            
         
        """
        pass
    
import NXOpen
##  Represents a collection of excitation objects  <br> To obtain an instance of this class, refer to @link NXOpen::CAE::ResponseSimulation::Manager  NXOpen::CAE::ResponseSimulation::Manager @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class ExcitationCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of excitation objects """


    ##  Creates the builder object of @link NXOpen::CAE::ResponseSimulation::DDAMExcitation NXOpen::CAE::ResponseSimulation::DDAMExcitation@endlink  
    ##  @return builder (@link CSDExcitationBuilder NXOpen.CAE.ResponseSimulation.CSDExcitationBuilder@endlink):   .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="excitation"> (@link CSDExcitation NXOpen.CAE.ResponseSimulation.CSDExcitation@endlink)   </param>
    def CreateCsdExcitationBuilder(self, excitation: CSDExcitation) -> CSDExcitationBuilder:
        """
         Creates the builder object of @link NXOpen::CAE::ResponseSimulation::DDAMExcitation NXOpen::CAE::ResponseSimulation::DDAMExcitation@endlink  
         @return builder (@link CSDExcitationBuilder NXOpen.CAE.ResponseSimulation.CSDExcitationBuilder@endlink):   .
        """
        pass
    
    ##  Creates the builder object of @link NXOpen::CAE::ResponseSimulation::DDAMExcitation NXOpen::CAE::ResponseSimulation::DDAMExcitation@endlink  
    ##  @return builder (@link DDAMExcitationBuilder NXOpen.CAE.ResponseSimulation.DDAMExcitationBuilder@endlink):   .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="excitation"> (@link DDAMExcitation NXOpen.CAE.ResponseSimulation.DDAMExcitation@endlink)   </param>
    def CreateDdamExcitationBuilder(self, excitation: DDAMExcitation) -> DDAMExcitationBuilder:
        """
         Creates the builder object of @link NXOpen::CAE::ResponseSimulation::DDAMExcitation NXOpen::CAE::ResponseSimulation::DDAMExcitation@endlink  
         @return builder (@link DDAMExcitationBuilder NXOpen.CAE.ResponseSimulation.DDAMExcitationBuilder@endlink):   .
        """
        pass
    
    ##  Creates the builder object of @link NXOpen::CAE::ResponseSimulation::DistributedLoadExcitation NXOpen::CAE::ResponseSimulation::DistributedLoadExcitation@endlink 
    ##  @return builder (@link DistributedLoadExcitationBuilder NXOpen.CAE.ResponseSimulation.DistributedLoadExcitationBuilder@endlink):   .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="excitation"> (@link DistributedLoadExcitation NXOpen.CAE.ResponseSimulation.DistributedLoadExcitation@endlink)   </param>
    def CreateDistributedLoadExcitationBuilder(self, excitation: DistributedLoadExcitation) -> DistributedLoadExcitationBuilder:
        """
         Creates the builder object of @link NXOpen::CAE::ResponseSimulation::DistributedLoadExcitation NXOpen::CAE::ResponseSimulation::DistributedLoadExcitation@endlink 
         @return builder (@link DistributedLoadExcitationBuilder NXOpen.CAE.ResponseSimulation.DistributedLoadExcitationBuilder@endlink):   .
        """
        pass
    
    ##  Creates the builder object of @link NXOpen::CAE::ResponseSimulation::DDAMExcitation NXOpen::CAE::ResponseSimulation::DDAMExcitation@endlink  
    ##  @return builder (@link DDAMExcitationBuilder NXOpen.CAE.ResponseSimulation.DDAMExcitationBuilder@endlink):   .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="excitation"> (@link DDAMExcitation NXOpen.CAE.ResponseSimulation.DDAMExcitation@endlink)   </param>
    def CreateRotationalDdamExcitationBuilder(self, excitation: DDAMExcitation) -> DDAMExcitationBuilder:
        """
         Creates the builder object of @link NXOpen::CAE::ResponseSimulation::DDAMExcitation NXOpen::CAE::ResponseSimulation::DDAMExcitation@endlink  
         @return builder (@link DDAMExcitationBuilder NXOpen.CAE.ResponseSimulation.DDAMExcitationBuilder@endlink):   .
        """
        pass
    
    ##  Creates the builder object of @link NXOpen::CAE::ResponseSimulation::RotationalNodalFunctionExcitation NXOpen::CAE::ResponseSimulation::RotationalNodalFunctionExcitation@endlink  
    ##  @return builder (@link RotationalNodalFunctionExcitationBuilder NXOpen.CAE.ResponseSimulation.RotationalNodalFunctionExcitationBuilder@endlink):   .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="excitation"> (@link RotationalNodalFunctionExcitation NXOpen.CAE.ResponseSimulation.RotationalNodalFunctionExcitation@endlink)   </param>
    def CreateRotationalNodalFunctionExcitationBuilder(self, excitation: RotationalNodalFunctionExcitation) -> RotationalNodalFunctionExcitationBuilder:
        """
         Creates the builder object of @link NXOpen::CAE::ResponseSimulation::RotationalNodalFunctionExcitation NXOpen::CAE::ResponseSimulation::RotationalNodalFunctionExcitation@endlink  
         @return builder (@link RotationalNodalFunctionExcitationBuilder NXOpen.CAE.ResponseSimulation.RotationalNodalFunctionExcitationBuilder@endlink):   .
        """
        pass
    
    ##  Creates the builder object of @link NXOpen::CAE::ResponseSimulation::StaticLoadExcitation NXOpen::CAE::ResponseSimulation::StaticLoadExcitation@endlink 
    ##  @return builder (@link StaticLoadExcitationBuilder NXOpen.CAE.ResponseSimulation.StaticLoadExcitationBuilder@endlink):   .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="excitation"> (@link StaticLoadExcitation NXOpen.CAE.ResponseSimulation.StaticLoadExcitation@endlink)   </param>
    def CreateStaticLoadExcitationBuilder(self, excitation: StaticLoadExcitation) -> StaticLoadExcitationBuilder:
        """
         Creates the builder object of @link NXOpen::CAE::ResponseSimulation::StaticLoadExcitation NXOpen::CAE::ResponseSimulation::StaticLoadExcitation@endlink 
         @return builder (@link StaticLoadExcitationBuilder NXOpen.CAE.ResponseSimulation.StaticLoadExcitationBuilder@endlink):   .
        """
        pass
    
    ##  Creates the builder object of @link NXOpen::CAE::ResponseSimulation::DDAMExcitation NXOpen::CAE::ResponseSimulation::DDAMExcitation@endlink  
    ##  @return builder (@link DDAMExcitationBuilder NXOpen.CAE.ResponseSimulation.DDAMExcitationBuilder@endlink):   .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="excitation"> (@link DDAMExcitation NXOpen.CAE.ResponseSimulation.DDAMExcitation@endlink)   </param>
    def CreateTranslationalDdamExcitationBuilder(self, excitation: DDAMExcitation) -> DDAMExcitationBuilder:
        """
         Creates the builder object of @link NXOpen::CAE::ResponseSimulation::DDAMExcitation NXOpen::CAE::ResponseSimulation::DDAMExcitation@endlink  
         @return builder (@link DDAMExcitationBuilder NXOpen.CAE.ResponseSimulation.DDAMExcitationBuilder@endlink):   .
        """
        pass
    
    ##  Creates the builder object of @link NXOpen::CAE::ResponseSimulation::TranslationalNodalFunctionExcitation NXOpen::CAE::ResponseSimulation::TranslationalNodalFunctionExcitation@endlink  
    ##  @return builder (@link TranslationalNodalFunctionExcitationBuilder NXOpen.CAE.ResponseSimulation.TranslationalNodalFunctionExcitationBuilder@endlink):   .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="excitation"> (@link TranslationalNodalFunctionExcitation NXOpen.CAE.ResponseSimulation.TranslationalNodalFunctionExcitation@endlink)   </param>
    def CreateTranslationalNodalFunctionExcitationBuilder(self, excitation: TranslationalNodalFunctionExcitation) -> TranslationalNodalFunctionExcitationBuilder:
        """
         Creates the builder object of @link NXOpen::CAE::ResponseSimulation::TranslationalNodalFunctionExcitation NXOpen::CAE::ResponseSimulation::TranslationalNodalFunctionExcitation@endlink  
         @return builder (@link TranslationalNodalFunctionExcitationBuilder NXOpen.CAE.ResponseSimulation.TranslationalNodalFunctionExcitationBuilder@endlink):   .
        """
        pass
    
    ##  Creates the builder object of @link NXOpen::CAE::ResponseSimulation::VelocityImpactExcitation NXOpen::CAE::ResponseSimulation::VelocityImpactExcitation@endlink  
    ##  @return builder (@link VelocityImpactExcitationBuilder NXOpen.CAE.ResponseSimulation.VelocityImpactExcitationBuilder@endlink):   .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="excitation"> (@link VelocityImpactExcitation NXOpen.CAE.ResponseSimulation.VelocityImpactExcitation@endlink)   </param>
    def CreateVelocityImpactExcitationBuilder(self, excitation: VelocityImpactExcitation) -> VelocityImpactExcitationBuilder:
        """
         Creates the builder object of @link NXOpen::CAE::ResponseSimulation::VelocityImpactExcitation NXOpen::CAE::ResponseSimulation::VelocityImpactExcitation@endlink  
         @return builder (@link VelocityImpactExcitationBuilder NXOpen.CAE.ResponseSimulation.VelocityImpactExcitationBuilder@endlink):   .
        """
        pass
    
    ##  Deletes an excitation 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="excitation"> (@link Excitation NXOpen.CAE.ResponseSimulation.Excitation@endlink)   </param>
    def DeleteExcitation(self, excitation: Excitation) -> None:
        """
         Deletes an excitation 
        """
        pass
    
    ##  Finds an excitation with specified excitation name 
    ##  @return excitation (@link Excitation NXOpen.CAE.ResponseSimulation.Excitation@endlink):   .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="name"> (str)   </param>
    def FindObject(self, name: str) -> Excitation:
        """
         Finds an excitation with specified excitation name 
         @return excitation (@link Excitation NXOpen.CAE.ResponseSimulation.Excitation@endlink):   .
        """
        pass
    
import NXOpen
##  Represents the manager to @link CAE::ResponseSimulation::DistributedLoadExcitation CAE::ResponseSimulation::DistributedLoadExcitation@endlink .
##      The object of type @link CAE::ResponseSimulation::DistributedLoadExcitation CAE::ResponseSimulation::DistributedLoadExcitation@endlink 
##       can only be created or edited through this class.
##      
## 
##   <br>  Created in NX5.0.0  <br> 

class ExcitationLocationDefinition(NXOpen.TaggedObject): 
    """ Represents the manager to <ja_class>CAE.ResponseSimulation.DistributedLoadExcitation</ja_class>.
     The object of type <ja_class>CAE.ResponseSimulation.DistributedLoadExcitation</ja_class>
      can only be created or edited through this class.
     """


    ## Getter for property: (@link NXOpen.SelectObject NXOpen.SelectObject@endlink) ExcitationLocation
    ##  Returns the excitation location on which the excitation will be applied.  
    ##    The excitation location
    ##         type could be force location, enforced motion location or dynamic load defined in response 
    ##         dynamic solution.   
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return NXOpen.SelectObject
    @property
    def ExcitationLocation(self) -> NXOpen.SelectObject:
        """
        Getter for property: (@link NXOpen.SelectObject NXOpen.SelectObject@endlink) ExcitationLocation
         Returns the excitation location on which the excitation will be applied.  
           The excitation location
                type could be force location, enforced motion location or dynamic load defined in response 
                dynamic solution.   
         
        """
        pass
    
    ## Getter for property: (int) ExcitationLocationId
    ##  Returns the ID of excitation location on which the excitation will be applied.  
    ##    The excitation location ID
    ##         could be node label or load set label   
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def ExcitationLocationId(self) -> int:
        """
        Getter for property: (int) ExcitationLocationId
         Returns the ID of excitation location on which the excitation will be applied.  
           The excitation location ID
                could be node label or load set label   
         
        """
        pass
    
    ## Setter for property: (int) ExcitationLocationId

    ##  Returns the ID of excitation location on which the excitation will be applied.  
    ##    The excitation location ID
    ##         could be node label or load set label   
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ExcitationLocationId.setter
    def ExcitationLocationId(self, excitaitonLocationId: int):
        """
        Setter for property: (int) ExcitationLocationId
         Returns the ID of excitation location on which the excitation will be applied.  
           The excitation location ID
                could be node label or load set label   
         
        """
        pass
    
    ## Getter for property: (@link ExcitationBuilder.ExcitationLocationType NXOpen.CAE.ResponseSimulation.ExcitationBuilder.ExcitationLocationType@endlink) ExcitationLocationType
    ##  Returns the type of excitaion location   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return ExcitationBuilder.ExcitationLocationType
    @property
    def ExcitationLocationType(self) -> ExcitationBuilder.ExcitationLocationType:
        """
        Getter for property: (@link ExcitationBuilder.ExcitationLocationType NXOpen.CAE.ResponseSimulation.ExcitationBuilder.ExcitationLocationType@endlink) ExcitationLocationType
         Returns the type of excitaion location   
            
         
        """
        pass
    
    ## Setter for property: (@link ExcitationBuilder.ExcitationLocationType NXOpen.CAE.ResponseSimulation.ExcitationBuilder.ExcitationLocationType@endlink) ExcitationLocationType

    ##  Returns the type of excitaion location   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ExcitationLocationType.setter
    def ExcitationLocationType(self, excitationLocationType: ExcitationBuilder.ExcitationLocationType):
        """
        Setter for property: (@link ExcitationBuilder.ExcitationLocationType NXOpen.CAE.ResponseSimulation.ExcitationBuilder.ExcitationLocationType@endlink) ExcitationLocationType
         Returns the type of excitaion location   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) ExcitationLocationlist
    ##  Returns the excitation location list on which the excitation will be applied.  
    ##    The excitation location
    ##         type could be force location, enforced motion location or dynamic load defined in response 
    ##         dynamic solution   
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.SelectTaggedObjectList
    @property
    def ExcitationLocationlist(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) ExcitationLocationlist
         Returns the excitation location list on which the excitation will be applied.  
           The excitation location
                type could be force location, enforced motion location or dynamic load defined in response 
                dynamic solution   
         
        """
        pass
    
import NXOpen
##  Represents the abstract class of dynamic excitations  <br> This is an abstract class, and cannot be created.  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class Excitation(NXOpen.NXObject): 
    """ Represents the abstract class of dynamic excitations """


    ## Represents the component type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## DistributedLoad</term><description> 
    ##  </description> </item><item><term> 
    ## X</term><description> 
    ##   </description> </item><item><term> 
    ## Y</term><description> 
    ##   </description> </item><item><term> 
    ## Z</term><description> 
    ##   </description> </item><item><term> 
    ## Rx</term><description> 
    ##   </description> </item><item><term> 
    ## Ry</term><description> 
    ##   </description> </item><item><term> 
    ## Rz</term><description> 
    ##   </description> </item><item><term> 
    ## UserDefined</term><description> 
    ##  </description> </item></list>
    class Component(Enum):
        """
        Members Include: <DistributedLoad> <X> <Y> <Z> <Rx> <Ry> <Rz> <UserDefined>
        """
        DistributedLoad: int
        X: int
        Y: int
        Z: int
        Rx: int
        Ry: int
        Rz: int
        UserDefined: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Excitation.Component:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) ExcitationName
    ##  Returns the excitation name   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return str
    @property
    def ExcitationName(self) -> str:
        """
        Getter for property: (str) ExcitationName
         Returns the excitation name   
            
         
        """
        pass
    
    ## Setter for property: (str) ExcitationName

    ##  Returns the excitation name   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ExcitationName.setter
    def ExcitationName(self, excitationName: str):
        """
        Setter for property: (str) ExcitationName
         Returns the excitation name   
            
         
        """
        pass
    
    ##  Deletes a response simulation excitation 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def Destroy(self) -> None:
        """
         Deletes a response simulation excitation 
        """
        pass
    
import NXOpen
##  Represents the frequency setting to perform FRF evaluation 
## 
##   <br>  Created in NX5.0.0  <br> 

class FrequencyDefinition(NXOpen.TaggedObject): 
    """ Represents the frequency setting to perform FRF evaluation """


    ##  Specifies the method to define frequency 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Range</term><description> 
    ##   </description> </item><item><term> 
    ## ModalContribution</term><description> 
    ##   </description> </item></list>
    class Definition(Enum):
        """
        Members Include: <Range> <ModalContribution>
        """
        Range: int
        ModalContribution: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FrequencyDefinition.Definition:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Specifies the method for interpolation 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## LogLog</term><description> 
    ##   </description> </item><item><term> 
    ## LogLinear</term><description> 
    ##   </description> </item><item><term> 
    ## LinearLinear</term><description> 
    ##   </description> </item></list>
    class InterpolationMethod(Enum):
        """
        Members Include: <LogLog> <LogLinear> <LinearLinear>
        """
        LogLog: int
        LogLinear: int
        LinearLinear: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FrequencyDefinition.InterpolationMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (int) ContributorNumber
    ##  Returns the number of contributors.  
    ##    Only available when maximu contributors
    ##          will be generated   
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return int
    @property
    def ContributorNumber(self) -> int:
        """
        Getter for property: (int) ContributorNumber
         Returns the number of contributors.  
           Only available when maximu contributors
                 will be generated   
         
        """
        pass
    
    ## Setter for property: (int) ContributorNumber

    ##  Returns the number of contributors.  
    ##    Only available when maximu contributors
    ##          will be generated   
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @ContributorNumber.setter
    def ContributorNumber(self, contributorNumber: int):
        """
        Setter for property: (int) ContributorNumber
         Returns the number of contributors.  
           Only available when maximu contributors
                 will be generated   
         
        """
        pass
    
    ## Getter for property: (float) EndValue
    ##  Returns the end value of frequency range.  
    ##    Only available when the frequency is defined 
    ##         by @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange@endlink    
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def EndValue(self) -> float:
        """
        Getter for property: (float) EndValue
         Returns the end value of frequency range.  
           Only available when the frequency is defined 
                by @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange@endlink    
         
        """
        pass
    
    ## Setter for property: (float) EndValue

    ##  Returns the end value of frequency range.  
    ##    Only available when the frequency is defined 
    ##         by @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange@endlink    
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @EndValue.setter
    def EndValue(self, end_value: float):
        """
        Setter for property: (float) EndValue
         Returns the end value of frequency range.  
           Only available when the frequency is defined 
                by @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange@endlink    
         
        """
        pass
    
    ## Getter for property: (@link FrequencyDefinition.Definition NXOpen.CAE.ResponseSimulation.FrequencyDefinition.Definition@endlink) EvaluationType
    ##  Returns the method to define frequency  
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return FrequencyDefinition.Definition
    @property
    def EvaluationType(self) -> FrequencyDefinition.Definition:
        """
        Getter for property: (@link FrequencyDefinition.Definition NXOpen.CAE.ResponseSimulation.FrequencyDefinition.Definition@endlink) EvaluationType
         Returns the method to define frequency  
            
         
        """
        pass
    
    ## Setter for property: (@link FrequencyDefinition.Definition NXOpen.CAE.ResponseSimulation.FrequencyDefinition.Definition@endlink) EvaluationType

    ##  Returns the method to define frequency  
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @EvaluationType.setter
    def EvaluationType(self, type: FrequencyDefinition.Definition):
        """
        Setter for property: (@link FrequencyDefinition.Definition NXOpen.CAE.ResponseSimulation.FrequencyDefinition.Definition@endlink) EvaluationType
         Returns the method to define frequency  
            
         
        """
        pass
    
    ## Getter for property: (bool) GenerateMaximumContributors
    ##  Returns the option for generating maximum contributors or not.  
    ##    Only available when
    ##         frequency definition metod is @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionModalContribution CAE::ResponseSimulation::FrequencyDefinition::DefinitionModalContribution@endlink    
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def GenerateMaximumContributors(self) -> bool:
        """
        Getter for property: (bool) GenerateMaximumContributors
         Returns the option for generating maximum contributors or not.  
           Only available when
                frequency definition metod is @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionModalContribution CAE::ResponseSimulation::FrequencyDefinition::DefinitionModalContribution@endlink    
         
        """
        pass
    
    ## Setter for property: (bool) GenerateMaximumContributors

    ##  Returns the option for generating maximum contributors or not.  
    ##    Only available when
    ##         frequency definition metod is @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionModalContribution CAE::ResponseSimulation::FrequencyDefinition::DefinitionModalContribution@endlink    
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @GenerateMaximumContributors.setter
    def GenerateMaximumContributors(self, generateMaximumContributors: bool):
        """
        Setter for property: (bool) GenerateMaximumContributors
         Returns the option for generating maximum contributors or not.  
           Only available when
                frequency definition metod is @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionModalContribution CAE::ResponseSimulation::FrequencyDefinition::DefinitionModalContribution@endlink    
         
        """
        pass
    
    ## Getter for property: (@link FrequencyDefinition.InterpolationMethod NXOpen.CAE.ResponseSimulation.FrequencyDefinition.InterpolationMethod@endlink) InterpolationMethodOption
    ##  Returns the interpolation method.  
    ##    Only available when the frequency is defined by
    ##         @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange@endlink    
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return FrequencyDefinition.InterpolationMethod
    @property
    def InterpolationMethodOption(self) -> FrequencyDefinition.InterpolationMethod:
        """
        Getter for property: (@link FrequencyDefinition.InterpolationMethod NXOpen.CAE.ResponseSimulation.FrequencyDefinition.InterpolationMethod@endlink) InterpolationMethodOption
         Returns the interpolation method.  
           Only available when the frequency is defined by
                @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange@endlink    
         
        """
        pass
    
    ## Setter for property: (@link FrequencyDefinition.InterpolationMethod NXOpen.CAE.ResponseSimulation.FrequencyDefinition.InterpolationMethod@endlink) InterpolationMethodOption

    ##  Returns the interpolation method.  
    ##    Only available when the frequency is defined by
    ##         @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange@endlink    
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @InterpolationMethodOption.setter
    def InterpolationMethodOption(self, interpolation_method: FrequencyDefinition.InterpolationMethod):
        """
        Setter for property: (@link FrequencyDefinition.InterpolationMethod NXOpen.CAE.ResponseSimulation.FrequencyDefinition.InterpolationMethod@endlink) InterpolationMethodOption
         Returns the interpolation method.  
           Only available when the frequency is defined by
                @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange@endlink    
         
        """
        pass
    
    ## Getter for property: (bool) NormalizeResults
    ##  Returns the option to normalize results.  
    ##    Only available when maximu contributors
    ##          will be generated   
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def NormalizeResults(self) -> bool:
        """
        Getter for property: (bool) NormalizeResults
         Returns the option to normalize results.  
           Only available when maximu contributors
                 will be generated   
         
        """
        pass
    
    ## Setter for property: (bool) NormalizeResults

    ##  Returns the option to normalize results.  
    ##    Only available when maximu contributors
    ##          will be generated   
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @NormalizeResults.setter
    def NormalizeResults(self, normalizeResults: bool):
        """
        Setter for property: (bool) NormalizeResults
         Returns the option to normalize results.  
           Only available when maximu contributors
                 will be generated   
         
        """
        pass
    
    ## Getter for property: (int) SpectralLine
    ##  Returns the additional spectral lines.  
    ##    Only available when frequency is defined 
    ##         by @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange@endlink    
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def SpectralLine(self) -> int:
        """
        Getter for property: (int) SpectralLine
         Returns the additional spectral lines.  
           Only available when frequency is defined 
                by @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange@endlink    
         
        """
        pass
    
    ## Setter for property: (int) SpectralLine

    ##  Returns the additional spectral lines.  
    ##    Only available when frequency is defined 
    ##         by @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange@endlink    
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @SpectralLine.setter
    def SpectralLine(self, spectral_lines: int):
        """
        Setter for property: (int) SpectralLine
         Returns the additional spectral lines.  
           Only available when frequency is defined 
                by @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange@endlink    
         
        """
        pass
    
    ## Getter for property: (float) StartValue
    ##  Returns the start value of frequency range.  
    ##    Only available when the frequency is defined
    ##         by @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange@endlink    
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def StartValue(self) -> float:
        """
        Getter for property: (float) StartValue
         Returns the start value of frequency range.  
           Only available when the frequency is defined
                by @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange@endlink    
         
        """
        pass
    
    ## Setter for property: (float) StartValue

    ##  Returns the start value of frequency range.  
    ##    Only available when the frequency is defined
    ##         by @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange@endlink    
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @StartValue.setter
    def StartValue(self, start_value: float):
        """
        Setter for property: (float) StartValue
         Returns the start value of frequency range.  
           Only available when the frequency is defined
                by @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange@endlink    
         
        """
        pass
    
    ##  Returns frequency values to perform FRF evaluation. Only available when the frequency definition 
    ##         method is @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionModalContribution CAE::ResponseSimulation::FrequencyDefinition::DefinitionModalContribution@endlink  
    ##  @return frequencies (List[float]):  .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetFrequencies(self) -> List[float]:
        """
         Returns frequency values to perform FRF evaluation. Only available when the frequency definition 
                method is @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionModalContribution CAE::ResponseSimulation::FrequencyDefinition::DefinitionModalContribution@endlink  
         @return frequencies (List[float]):  .
        """
        pass
    
    ##  Sets the frequency values to perform FRF evaluation. Only available when the frequency definition 
    ##         method is @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionModalContribution CAE::ResponseSimulation::FrequencyDefinition::DefinitionModalContribution@endlink  
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="frequencies"> (List[float])  </param>
    def SetFrequencies(self, frequencies: List[float]) -> None:
        """
         Sets the frequency values to perform FRF evaluation. Only available when the frequency definition 
                method is @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionModalContribution CAE::ResponseSimulation::FrequencyDefinition::DefinitionModalContribution@endlink  
        """
        pass
    
##  This is a manager to the @link NXOpen::CAE::ResponseSimulation::FrfEvaluationSetting NXOpen::CAE::ResponseSimulation::FrfEvaluationSetting@endlink  class. 
##     Object of type @link NXOpen::CAE::ResponseSimulation::FrfEvaluationSetting NXOpen::CAE::ResponseSimulation::FrfEvaluationSetting@endlink  can be 
##     created and edited only through this class
##       <br> To create a new instance of this class, use @link NXOpen::CAE::ResponseSimulation::EvaluationSettingManager::CreateFrfEvaluationSettingBuilder  NXOpen::CAE::ResponseSimulation::EvaluationSettingManager::CreateFrfEvaluationSettingBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class FrfEvaluationSettingBuilder(ModalResultsEvaluationSettingBuilder): 
    """ This is a manager to the <ja_class>NXOpen.CAE.ResponseSimulation.FrfEvaluationSetting</ja_class> class. 
    Object of type <ja_class>NXOpen.CAE.ResponseSimulation.FrfEvaluationSetting</ja_class> can be 
    created and edited only through this class
     """
    pass


##  Represents the parameters setting for FRF results evaluation  <br> To create or edit an instance of this class, use @link NXOpen::CAE::ResponseSimulation::FrfEvaluationSettingBuilder  NXOpen::CAE::ResponseSimulation::FrfEvaluationSettingBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class FrfEvaluationSetting(ModalResultsEvaluationSetting): 
    """ Represents the parameters setting for FRF results evaluation """
    pass


import NXOpen
import NXOpen.CAE
##  Represents a function component setting of 
##     @link NXOpen::CAE::ResponseSimulation::NodalFunctionExcitation NXOpen::CAE::ResponseSimulation::NodalFunctionExcitation@endlink  on one direction 
## 
##   <br>  Created in NX5.0.0  <br> 

class FunctionComponentData(NXOpen.TaggedObject): 
    """ Represents a function component setting of 
    <ja_class>NXOpen.CAE.ResponseSimulation.NodalFunctionExcitation</ja_class> on one direction """


    ## Getter for property: (bool) Enable
    ##  Returns the option to enable the function component to be used while evaluating   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Enable(self) -> bool:
        """
        Getter for property: (bool) Enable
         Returns the option to enable the function component to be used while evaluating   
            
         
        """
        pass
    
    ## Setter for property: (bool) Enable

    ##  Returns the option to enable the function component to be used while evaluating   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Enable.setter
    def Enable(self, enable_option: bool):
        """
        Setter for property: (bool) Enable
         Returns the option to enable the function component to be used while evaluating   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.Function NXOpen.CAE.Function@endlink) Function
    ##  Returns the function to be applied   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return NXOpen.CAE.Function
    @property
    def Function(self) -> NXOpen.CAE.Function:
        """
        Getter for property: (@link NXOpen.CAE.Function NXOpen.CAE.Function@endlink) Function
         Returns the function to be applied   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.Function NXOpen.CAE.Function@endlink) Function

    ##  Returns the function to be applied   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Function.setter
    def Function(self, excitation_function: NXOpen.CAE.Function):
        """
        Setter for property: (@link NXOpen.CAE.Function NXOpen.CAE.Function@endlink) Function
         Returns the function to be applied   
            
         
        """
        pass
    
    ## Getter for property: (float) PhaseAngle
    ##  Returns the phase angle.  
    ##    Only available when the onwer event is 
    ##         @link NXOpen::CAE::ResponseSimulation::RSEvent::TypeTransient NXOpen::CAE::ResponseSimulation::RSEvent::TypeTransient@endlink    
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def PhaseAngle(self) -> float:
        """
        Getter for property: (float) PhaseAngle
         Returns the phase angle.  
           Only available when the onwer event is 
                @link NXOpen::CAE::ResponseSimulation::RSEvent::TypeTransient NXOpen::CAE::ResponseSimulation::RSEvent::TypeTransient@endlink    
         
        """
        pass
    
    ## Setter for property: (float) PhaseAngle

    ##  Returns the phase angle.  
    ##    Only available when the onwer event is 
    ##         @link NXOpen::CAE::ResponseSimulation::RSEvent::TypeTransient NXOpen::CAE::ResponseSimulation::RSEvent::TypeTransient@endlink    
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @PhaseAngle.setter
    def PhaseAngle(self, phase_angle: float):
        """
        Setter for property: (float) PhaseAngle
         Returns the phase angle.  
           Only available when the onwer event is 
                @link NXOpen::CAE::ResponseSimulation::RSEvent::TypeTransient NXOpen::CAE::ResponseSimulation::RSEvent::TypeTransient@endlink    
         
        """
        pass
    
    ## Getter for property: (float) ScalarFactor
    ##  Returns the scalar factor   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def ScalarFactor(self) -> float:
        """
        Getter for property: (float) ScalarFactor
         Returns the scalar factor   
            
         
        """
        pass
    
    ## Setter for property: (float) ScalarFactor

    ##  Returns the scalar factor   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ScalarFactor.setter
    def ScalarFactor(self, scalar_factor: float):
        """
        Setter for property: (float) ScalarFactor
         Returns the scalar factor   
            
         
        """
        pass
    
    ##  Returns the component type 
    ##  @return component_type (@link Excitation.Component NXOpen.CAE.ResponseSimulation.Excitation.Component@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetComponentType(self) -> Excitation.Component:
        """
         Returns the component type 
         @return component_type (@link Excitation.Component NXOpen.CAE.ResponseSimulation.Excitation.Component@endlink):  .
        """
        pass
    
import NXOpen
##  Represents the output setting for function response evaluation
## 
##   <br>  Created in NX5.0.0  <br> 

class FunctionEvaluationOutputSettings(NXOpen.TaggedObject): 
    """ Represents the output setting for function response evaluation"""


    ## Getter for property: (str) RecordPrefix
    ##  Returns the prefix of evaluation results record name   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return str
    @property
    def RecordPrefix(self) -> str:
        """
        Getter for property: (str) RecordPrefix
         Returns the prefix of evaluation results record name   
            
         
        """
        pass
    
    ## Setter for property: (str) RecordPrefix

    ##  Returns the prefix of evaluation results record name   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @RecordPrefix.setter
    def RecordPrefix(self, record_prefix: str):
        """
        Setter for property: (str) RecordPrefix
         Returns the prefix of evaluation results record name   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowPlot
    ##  Returns the option of show plot.  
    ##    If true, the evaluation results will be displayed on screen   
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def ShowPlot(self) -> bool:
        """
        Getter for property: (bool) ShowPlot
         Returns the option of show plot.  
           If true, the evaluation results will be displayed on screen   
         
        """
        pass
    
    ## Setter for property: (bool) ShowPlot

    ##  Returns the option of show plot.  
    ##    If true, the evaluation results will be displayed on screen   
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ShowPlot.setter
    def ShowPlot(self, show_plot: bool):
        """
        Setter for property: (bool) ShowPlot
         Returns the option of show plot.  
           If true, the evaluation results will be displayed on screen   
         
        """
        pass
    
    ## Getter for property: (bool) StoreOption
    ##  Returns the store option.  
    ##    If true, the evaluation results will be stored on disk   
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def StoreOption(self) -> bool:
        """
        Getter for property: (bool) StoreOption
         Returns the store option.  
           If true, the evaluation results will be stored on disk   
         
        """
        pass
    
    ## Setter for property: (bool) StoreOption

    ##  Returns the store option.  
    ##    If true, the evaluation results will be stored on disk   
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @StoreOption.setter
    def StoreOption(self, store_option: bool):
        """
        Setter for property: (bool) StoreOption
         Returns the store option.  
           If true, the evaluation results will be stored on disk   
         
        """
        pass
    
import NXOpen
##  Represents the abstract builder class of evaluation setting for function response evaluation
##      <br> This is an abstract class, and cannot be created.  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class FunctionEvaluationSettingBuilder(NXOpen.Builder): 
    """ Represents the abstract builder class of evaluation setting for function response evaluation
    """


    ## Getter for property: (@link FunctionEvaluationOutputSettings NXOpen.CAE.ResponseSimulation.FunctionEvaluationOutputSettings@endlink) OutputSettings
    ##  Returns the output setting.  
    ##      
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return FunctionEvaluationOutputSettings
    @property
    def OutputSettings(self) -> FunctionEvaluationOutputSettings:
        """
        Getter for property: (@link FunctionEvaluationOutputSettings NXOpen.CAE.ResponseSimulation.FunctionEvaluationOutputSettings@endlink) OutputSettings
         Returns the output setting.  
             
         
        """
        pass
    
    ## Getter for property: (@link EvaluationResultType NXOpen.CAE.ResponseSimulation.EvaluationResultType@endlink) ResultType
    ##  Returns the result type   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return EvaluationResultType
    @property
    def ResultType(self) -> EvaluationResultType:
        """
        Getter for property: (@link EvaluationResultType NXOpen.CAE.ResponseSimulation.EvaluationResultType@endlink) ResultType
         Returns the result type   
            
         
        """
        pass
    
    ## Setter for property: (@link EvaluationResultType NXOpen.CAE.ResponseSimulation.EvaluationResultType@endlink) ResultType

    ##  Returns the result type   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ResultType.setter
    def ResultType(self, result_type: EvaluationResultType):
        """
        Setter for property: (@link EvaluationResultType NXOpen.CAE.ResponseSimulation.EvaluationResultType@endlink) ResultType
         Returns the result type   
            
         
        """
        pass
    
##  Represents the abstract class of evaluation setting for function response evaluation
##      <br> This is an abstract class, and cannot be created.  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class FunctionEvaluationSetting(EvaluationSetting): 
    """ Represents the abstract class of evaluation setting for function response evaluation
    """
    pass


import NXOpen
##  Represents the initial condition setting of transient event 
## 
##   <br>  Created in NX5.0.0  <br> 

class InitialConditions(NXOpen.NXObject): 
    """ Represents the initial condition setting of transient event """


    ##  Specifies how to define initial condition for the user customization 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ManualData</term><description> 
    ##   </description> </item><item><term> 
    ## FromEef</term><description> 
    ##   </description> </item></list>
    class EntryMethod(Enum):
        """
        Members Include: <ManualData> <FromEef>
        """
        ManualData: int
        FromEef: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> InitialConditions.EntryMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Specifies the method to define initial condition 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## QuasiStatic</term><description> 
    ##   </description> </item><item><term> 
    ## Zero</term><description> 
    ##   </description> </item><item><term> 
    ## UserDefined</term><description> 
    ##   </description> </item></list>
    class Type(Enum):
        """
        Members Include: <QuasiStatic> <Zero> <UserDefined>
        """
        QuasiStatic: int
        Zero: int
        UserDefined: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> InitialConditions.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link InitialConditions.EntryMethod NXOpen.CAE.ResponseSimulation.InitialConditions.EntryMethod@endlink) EntryMethodOption
    ##  Returns the entry method of user customization   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return InitialConditions.EntryMethod
    @property
    def EntryMethodOption(self) -> InitialConditions.EntryMethod:
        """
        Getter for property: (@link InitialConditions.EntryMethod NXOpen.CAE.ResponseSimulation.InitialConditions.EntryMethod@endlink) EntryMethodOption
         Returns the entry method of user customization   
            
         
        """
        pass
    
    ## Setter for property: (@link InitialConditions.EntryMethod NXOpen.CAE.ResponseSimulation.InitialConditions.EntryMethod@endlink) EntryMethodOption

    ##  Returns the entry method of user customization   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @EntryMethodOption.setter
    def EntryMethodOption(self, entry_method: InitialConditions.EntryMethod):
        """
        Setter for property: (@link InitialConditions.EntryMethod NXOpen.CAE.ResponseSimulation.InitialConditions.EntryMethod@endlink) EntryMethodOption
         Returns the entry method of user customization   
            
         
        """
        pass
    
    ## Getter for property: (str) ExistingEefFile
    ##  Returns an existing EEF file containing initial condition.  
    ##    Only available when the 
    ##         initial condition type is @link CAE::ResponseSimulation::InitialConditions::TypeUserDefined CAE::ResponseSimulation::InitialConditions::TypeUserDefined@endlink 
    ##         and the entry method is @link CAE::ResponseSimulation::InitialConditions::EntryMethodFromEef CAE::ResponseSimulation::InitialConditions::EntryMethodFromEef@endlink    
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return str
    @property
    def ExistingEefFile(self) -> str:
        """
        Getter for property: (str) ExistingEefFile
         Returns an existing EEF file containing initial condition.  
           Only available when the 
                initial condition type is @link CAE::ResponseSimulation::InitialConditions::TypeUserDefined CAE::ResponseSimulation::InitialConditions::TypeUserDefined@endlink 
                and the entry method is @link CAE::ResponseSimulation::InitialConditions::EntryMethodFromEef CAE::ResponseSimulation::InitialConditions::EntryMethodFromEef@endlink    
         
        """
        pass
    
    ## Setter for property: (str) ExistingEefFile

    ##  Returns an existing EEF file containing initial condition.  
    ##    Only available when the 
    ##         initial condition type is @link CAE::ResponseSimulation::InitialConditions::TypeUserDefined CAE::ResponseSimulation::InitialConditions::TypeUserDefined@endlink 
    ##         and the entry method is @link CAE::ResponseSimulation::InitialConditions::EntryMethodFromEef CAE::ResponseSimulation::InitialConditions::EntryMethodFromEef@endlink    
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ExistingEefFile.setter
    def ExistingEefFile(self, eef_file: str):
        """
        Setter for property: (str) ExistingEefFile
         Returns an existing EEF file containing initial condition.  
           Only available when the 
                initial condition type is @link CAE::ResponseSimulation::InitialConditions::TypeUserDefined CAE::ResponseSimulation::InitialConditions::TypeUserDefined@endlink 
                and the entry method is @link CAE::ResponseSimulation::InitialConditions::EntryMethodFromEef CAE::ResponseSimulation::InitialConditions::EntryMethodFromEef@endlink    
         
        """
        pass
    
    ## Getter for property: (@link InitialConditions.Type NXOpen.CAE.ResponseSimulation.InitialConditions.Type@endlink) InitialConditionType
    ##  Returns the definition method   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return InitialConditions.Type
    @property
    def InitialConditionType(self) -> InitialConditions.Type:
        """
        Getter for property: (@link InitialConditions.Type NXOpen.CAE.ResponseSimulation.InitialConditions.Type@endlink) InitialConditionType
         Returns the definition method   
            
         
        """
        pass
    
    ## Setter for property: (@link InitialConditions.Type NXOpen.CAE.ResponseSimulation.InitialConditions.Type@endlink) InitialConditionType

    ##  Returns the definition method   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @InitialConditionType.setter
    def InitialConditionType(self, initial_condition_type: InitialConditions.Type):
        """
        Setter for property: (@link InitialConditions.Type NXOpen.CAE.ResponseSimulation.InitialConditions.Type@endlink) InitialConditionType
         Returns the definition method   
            
         
        """
        pass
    
    ##  Returns customized initial data of all normal modes. Only available when initial condition type is 
    ##         @link CAE::ResponseSimulation::InitialConditions::TypeUserDefined CAE::ResponseSimulation::InitialConditions::TypeUserDefined@endlink  
    ##  @return initial_data (@link ModeInitialData List[NXOpen.CAE.ResponseSimulation.ModeInitialData]@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetAllCustomizedInitialData(self) -> List[ModeInitialData]:
        """
         Returns customized initial data of all normal modes. Only available when initial condition type is 
                @link CAE::ResponseSimulation::InitialConditions::TypeUserDefined CAE::ResponseSimulation::InitialConditions::TypeUserDefined@endlink  
         @return initial_data (@link ModeInitialData List[NXOpen.CAE.ResponseSimulation.ModeInitialData]@endlink):  .
        """
        pass
    
    ##  Returns customized initial data of normal mode by mode id. Only available when initial condition
    ##         type is @link CAE::ResponseSimulation::InitialConditions::TypeUserDefined CAE::ResponseSimulation::InitialConditions::TypeUserDefined@endlink  
    ##  @return initial_data (@link ModeInitialData NXOpen.CAE.ResponseSimulation.ModeInitialData@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="mode_id"> (int)  </param>
    def GetCustomizedInitialDataById(self, mode_id: int) -> ModeInitialData:
        """
         Returns customized initial data of normal mode by mode id. Only available when initial condition
                type is @link CAE::ResponseSimulation::InitialConditions::TypeUserDefined CAE::ResponseSimulation::InitialConditions::TypeUserDefined@endlink  
         @return initial_data (@link ModeInitialData NXOpen.CAE.ResponseSimulation.ModeInitialData@endlink):  .
        """
        pass
    
##  This enum defines interpolation method 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## LogLog</term><description> 
##   </description> </item><item><term> 
## LinearLinear</term><description> 
##   </description> </item><item><term> 
## LinearLog</term><description> 
##   </description> </item><item><term> 
## LogLinear</term><description> 
##   </description> </item></list>
class InterpolationMethod(Enum):
    """
    Members Include: <LogLog> <LinearLinear> <LinearLog> <LogLinear>
    """
    LogLog: int
    LinearLinear: int
    LinearLog: int
    LogLinear: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> InterpolationMethod:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##  This is a manager to the @link NXOpen::CAE::ResponseSimulation::LcrResultsEvaluationSetting NXOpen::CAE::ResponseSimulation::LcrResultsEvaluationSetting@endlink  class. 
##     Object of type @link NXOpen::CAE::ResponseSimulation::LcrResultsEvaluationSetting NXOpen::CAE::ResponseSimulation::LcrResultsEvaluationSetting@endlink  can be 
##     created and edited only through this class
##       <br> To create a new instance of this class, use @link NXOpen::CAE::ResponseSimulation::EvaluationSettingManager::CreateLcrResultsEvaluationSettingBuilder  NXOpen::CAE::ResponseSimulation::EvaluationSettingManager::CreateLcrResultsEvaluationSettingBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class LcrResultsEvaluationSettingBuilder(RmsResultsEvaluationSettingBuilder): 
    """ This is a manager to the <ja_class>NXOpen.CAE.ResponseSimulation.LcrResultsEvaluationSetting</ja_class> class. 
    Object of type <ja_class>NXOpen.CAE.ResponseSimulation.LcrResultsEvaluationSetting</ja_class> can be 
    created and edited only through this class
     """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) CrossingLevelExpression
    ##  Returns the crossing level expression  
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.Expression
    @property
    def CrossingLevelExpression(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) CrossingLevelExpression
         Returns the crossing level expression  
            
         
        """
        pass
    
##  Represents the parameters setting of LCR results evaluation. Only available when
##     event type is @link NXOpen::CAE::ResponseSimulation::RSEvent::TypeRandom NXOpen::CAE::ResponseSimulation::RSEvent::TypeRandom@endlink . For more information,
##     see the Response Dynamics Section of the Gateway Help  <br> To create or edit an instance of this class, use @link NXOpen::CAE::ResponseSimulation::LcrResultsEvaluationSettingBuilder  NXOpen::CAE::ResponseSimulation::LcrResultsEvaluationSettingBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class LcrResultsEvaluationSetting(RmsResultsEvaluationSetting): 
    """ Represents the parameters setting of LCR results evaluation. Only available when
    event type is <ja_enum_member>NXOpen.CAE.ResponseSimulation.RSEvent.Type.Random</ja_enum_member>. For more information,
    see the Response Dynamics Section of the Gateway Help """
    pass


import NXOpen
##  Represents the Response Dynamics manager to contain all Response Dynamics objects  <br> To obtain an instance of this class, refer to @link NXOpen::CAE::SimSimulation  NXOpen::CAE::SimSimulation @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class Manager(NXOpen.Object): 
    """ Represents the Response Dynamics manager to contain all Response Dynamics objects """


    ##  Returns the Response Dynamics solution collection belonging to this sim part 
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @link SolutionCollection NXOpen.CAE.ResponseSimulation.SolutionCollection@endlink
    @property
    def Solutions() -> SolutionCollection:
        """
         Returns the Response Dynamics solution collection belonging to this sim part 
        """
        pass
    
    ##  Returns the Response Dynamics event collection belonging to this sim part 
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @link RSEventCollection NXOpen.CAE.ResponseSimulation.RSEventCollection@endlink
    @property
    def Events() -> RSEventCollection:
        """
         Returns the Response Dynamics event collection belonging to this sim part 
        """
        pass
    
    ##  Returns the Response Dynamics excitation collection belonging to this sim part 
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @link ExcitationCollection NXOpen.CAE.ResponseSimulation.ExcitationCollection@endlink
    @property
    def Excitations() -> ExcitationCollection:
        """
         Returns the Response Dynamics excitation collection belonging to this sim part 
        """
        pass
    
    ##  Returns the Response Dynamics evaluation data manager belonging to this sim part 
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @link EvaluationSettingManager NXOpen.CAE.ResponseSimulation.EvaluationSettingManager@endlink
    @property
    def EvaluationSettingManager() -> EvaluationSettingManager:
        """
         Returns the Response Dynamics evaluation data manager belonging to this sim part 
        """
        pass
    
    ##  Returns the Response Dynamics sensor collection belonging to this sim part 
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @link SensorCollection NXOpen.CAE.ResponseSimulation.SensorCollection@endlink
    @property
    def Sensors() -> SensorCollection:
        """
         Returns the Response Dynamics sensor collection belonging to this sim part 
        """
        pass
    
    ##  Returns the Response Dynamics strain gage collection belonging to this sim part 
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @link StrainGageCollection NXOpen.CAE.ResponseSimulation.StrainGageCollection@endlink
    @property
    def StrainGages() -> StrainGageCollection:
        """
         Returns the Response Dynamics strain gage collection belonging to this sim part 
        """
        pass
    
import NXOpen
##  Represents the modal presentation of a response analysis meta solution 
## 
##   <br>  Created in NX5.0.0  <br> 

class ModalProperties(NXOpen.NXObject): 
    """ Represents the modal presentation of a response analysis meta solution """


    ##  Sets activate or deactivate status for all normal modes 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="activate"> (bool)  </param>
    def Activate(self, activate: bool) -> None:
        """
         Sets activate or deactivate status for all normal modes 
        """
        pass
    
    ##  Sets deactivate status for all normal modes that are less than the % Mass Limit Specified 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="limit"> (float)  </param>
    def DeactivateModesBelowLimit(self, limit: float) -> None:
        """
         Sets deactivate status for all normal modes that are less than the % Mass Limit Specified 
        """
        pass
    
    ##  Returns the count of attachment modes 
    ##  @return mode_count (int):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetAttachmentModeCount(self) -> int:
        """
         Returns the count of attachment modes 
         @return mode_count (int):  .
        """
        pass
    
    ##  Returns the count of constrain modes 
    ##  @return mode_count (int):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetConstrainModeCount(self) -> int:
        """
         Returns the count of constrain modes 
         @return mode_count (int):  .
        """
        pass
    
    ##  Returns normal mode with specified node ID 
    ##  @return normal_mode (@link NormalMode NXOpen.CAE.ResponseSimulation.NormalMode@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="mode_id"> (int)  </param>
    def GetNormalModeById(self, mode_id: int) -> NormalMode:
        """
         Returns normal mode with specified node ID 
         @return normal_mode (@link NormalMode NXOpen.CAE.ResponseSimulation.NormalMode@endlink):  .
        """
        pass
    
    ##  Returns the count of normal modes 
    ##  @return mode_count (int):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetNormalModeCount(self) -> int:
        """
         Returns the count of normal modes 
         @return mode_count (int):  .
        """
        pass
    
    ##  Returns all normal modes 
    ##  @return normal_modes (@link NormalMode List[NXOpen.CAE.ResponseSimulation.NormalMode]@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetNormalModes(self) -> List[NormalMode]:
        """
         Returns all normal modes 
         @return normal_modes (@link NormalMode List[NXOpen.CAE.ResponseSimulation.NormalMode]@endlink):  .
        """
        pass
    
    ##  Returns the physical damping setting object 
    ##  @return physical_damping_settings (@link PhysicalDampingSettings NXOpen.CAE.ResponseSimulation.PhysicalDampingSettings@endlink): .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetPhysicalDampingSettings(self) -> PhysicalDampingSettings:
        """
         Returns the physical damping setting object 
         @return physical_damping_settings (@link PhysicalDampingSettings NXOpen.CAE.ResponseSimulation.PhysicalDampingSettings@endlink): .
        """
        pass
    
    ##  Set damping factors for all normal modes 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="viscous_damping"> (float)  </param>
    ## <param name="hysteretic_damping"> (float)  </param>
    def SetDampingFactors(self, viscous_damping: float, hysteretic_damping: float) -> None:
        """
         Set damping factors for all normal modes 
        """
        pass
    
    ##  Set rayleigh's damping for all normal modes 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="alpha_factor"> (float)  </param>
    ## <param name="belta_factor"> (float)  </param>
    def SetRayleighDamping(self, alpha_factor: float, belta_factor: float) -> None:
        """
         Set rayleigh's damping for all normal modes 
        """
        pass
    
import NXOpen.CAE
##  Represents the abstract builder class of evaluation setting for FRF and transmissibility  <br> This is an abstract class, and cannot be created.  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class ModalResultsEvaluationSettingBuilder(FunctionEvaluationSettingBuilder): 
    """ Represents the abstract builder class of evaluation setting for FRF and transmissibility """


    ## Getter for property: (@link DataLocation NXOpen.CAE.ResponseSimulation.DataLocation@endlink) DataLocation
    ##  Returns the frequency setting   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return DataLocation
    @property
    def DataLocation(self) -> DataLocation:
        """
        Getter for property: (@link DataLocation NXOpen.CAE.ResponseSimulation.DataLocation@endlink) DataLocation
         Returns the frequency setting   
            
         
        """
        pass
    
    ## Getter for property: (@link FrequencyDefinition NXOpen.CAE.ResponseSimulation.FrequencyDefinition@endlink) EvaluationProperty
    ##  Returns the frequency setting   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return FrequencyDefinition
    @property
    def EvaluationProperty(self) -> FrequencyDefinition:
        """
        Getter for property: (@link FrequencyDefinition NXOpen.CAE.ResponseSimulation.FrequencyDefinition@endlink) EvaluationProperty
         Returns the frequency setting   
            
         
        """
        pass
    
    ## Getter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) InputDirection
    ##  Returns the source direction data component   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return DirectionDataComponent
    @property
    def InputDirection(self) -> DirectionDataComponent:
        """
        Getter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) InputDirection
         Returns the source direction data component   
            
         
        """
        pass
    
    ## Setter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) InputDirection

    ##  Returns the source direction data component   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @InputDirection.setter
    def InputDirection(self, data_component: DirectionDataComponent):
        """
        Setter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) InputDirection
         Returns the source direction data component   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.FENode NXOpen.CAE.FENode@endlink) InputNode
    ##  Returns the source node.  
    ##      
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return NXOpen.CAE.FENode
    @property
    def InputNode(self) -> NXOpen.CAE.FENode:
        """
        Getter for property: (@link NXOpen.CAE.FENode NXOpen.CAE.FENode@endlink) InputNode
         Returns the source node.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.FENode NXOpen.CAE.FENode@endlink) InputNode

    ##  Returns the source node.  
    ##      
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @InputNode.setter
    def InputNode(self, source_node: NXOpen.CAE.FENode):
        """
        Setter for property: (@link NXOpen.CAE.FENode NXOpen.CAE.FENode@endlink) InputNode
         Returns the source node.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.FENode NXOpen.CAE.FENode@endlink) ObservationNode
    ##  Returns the observation nodes.  
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return NXOpen.CAE.FENode
    @property
    def ObservationNode(self) -> NXOpen.CAE.FENode:
        """
        Getter for property: (@link NXOpen.CAE.FENode NXOpen.CAE.FENode@endlink) ObservationNode
         Returns the observation nodes.  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.FENode NXOpen.CAE.FENode@endlink) ObservationNode

    ##  Returns the observation nodes.  
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ObservationNode.setter
    def ObservationNode(self, observation_node: NXOpen.CAE.FENode):
        """
        Setter for property: (@link NXOpen.CAE.FENode NXOpen.CAE.FENode@endlink) ObservationNode
         Returns the observation nodes.  
            
         
        """
        pass
    
    ## Getter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) OutputRequest
    ##  Returns the destination direction data component   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return DirectionDataComponent
    @property
    def OutputRequest(self) -> DirectionDataComponent:
        """
        Getter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) OutputRequest
         Returns the destination direction data component   
            
         
        """
        pass
    
    ## Setter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) OutputRequest

    ##  Returns the destination direction data component   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @OutputRequest.setter
    def OutputRequest(self, data_component: DirectionDataComponent):
        """
        Setter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) OutputRequest
         Returns the destination direction data component   
            
         
        """
        pass
    
    ##  Returns destination nodes. Only available when result type is 
    ##         @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink ,
    ##         @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink ,
    ##         @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
    ##  @return destination_elements (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetOutputElements(self) -> List[NXOpen.CAE.FEElement]:
        """
         Returns destination nodes. Only available when result type is 
                @link CAE::ResponseSimulation::EvaluationResultTypeStress CAE::ResponseSimulation::EvaluationResultTypeStress@endlink ,
                @link CAE::ResponseSimulation::EvaluationResultTypeStrain CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink ,
                @link CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant CAE::ResponseSimulation::EvaluationResultTypeShellStressResultant@endlink  
         @return destination_elements (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink):  .
        """
        pass
    
    ##  Returns destination nodes. Only available when result type is 
    ##         @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink ,
    ##         @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink ,
    ##         @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink ,
    ##         @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
    ##  @return destination_node (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetOutputNodes(self) -> List[NXOpen.CAE.FENode]:
        """
         Returns destination nodes. Only available when result type is 
                @link CAE::ResponseSimulation::EvaluationResultTypeDisplacement CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink ,
                @link CAE::ResponseSimulation::EvaluationResultTypeVelocity CAE::ResponseSimulation::EvaluationResultTypeVelocity@endlink ,
                @link CAE::ResponseSimulation::EvaluationResultTypeAcceleration CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink ,
                @link CAE::ResponseSimulation::EvaluationResultTypeReactionForce CAE::ResponseSimulation::EvaluationResultTypeReactionForce@endlink  
         @return destination_node (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink):  .
        """
        pass
    
    ##  Sets destination nodes 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="destination_elements"> (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink)  </param>
    def SetOutputElements(self, destination_elements: List[NXOpen.CAE.FEElement]) -> None:
        """
         Sets destination nodes 
        """
        pass
    
    ##  Sets destination nodes 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="destination_node"> (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink)  </param>
    def SetOutputNodes(self, destination_node: List[NXOpen.CAE.FENode]) -> None:
        """
         Sets destination nodes 
        """
        pass
    
##  Represents the abstract class of evaluation setting for FRF and transmissibility  <br> This is an abstract class, and cannot be created.  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class ModalResultsEvaluationSetting(FunctionEvaluationSetting): 
    """ Represents the abstract class of evaluation setting for FRF and transmissibility """
    pass


import NXOpen
##  Represents the initial setting for a normal mode 
## 
##   <br>  Created in NX5.0.0  <br> 

class ModeInitialData(NXOpen.NXObject): 
    """ Represents the initial setting for a normal mode """


    ## Getter for property: (float) InitialDisplacement
    ##  Returns the initial diaplacement   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def InitialDisplacement(self) -> float:
        """
        Getter for property: (float) InitialDisplacement
         Returns the initial diaplacement   
            
         
        """
        pass
    
    ## Setter for property: (float) InitialDisplacement

    ##  Returns the initial diaplacement   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @InitialDisplacement.setter
    def InitialDisplacement(self, initial_displacement: float):
        """
        Setter for property: (float) InitialDisplacement
         Returns the initial diaplacement   
            
         
        """
        pass
    
    ## Getter for property: (float) InitialVelocity
    ##  Returns the initial velocity   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def InitialVelocity(self) -> float:
        """
        Getter for property: (float) InitialVelocity
         Returns the initial velocity   
            
         
        """
        pass
    
    ## Setter for property: (float) InitialVelocity

    ##  Returns the initial velocity   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @InitialVelocity.setter
    def InitialVelocity(self, initial_velocity: float):
        """
        Setter for property: (float) InitialVelocity
         Returns the initial velocity   
            
         
        """
        pass
    
    ##  Returns normal mode ID 
    ##  @return mode_id (int):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetModeId(self) -> int:
        """
         Returns normal mode ID 
         @return mode_id (int):  .
        """
        pass
    
##  Specifies nodal averaging options 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Shells</term><description> 
##  </description> </item><item><term> 
## Solids</term><description> 
##  </description> </item></list>
class NodalAveragingOption(Enum):
    """
    Members Include: <Shells> <Solids>
    """
    Shells: int
    Solids: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> NodalAveragingOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Specifies beam element evaluation locations for nodal function evaluation 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## C</term><description> 
##  Stress Recovery point C on a beam cross section </description> </item><item><term> 
## D</term><description> 
##  Stress Recovery point D on a beam cross section </description> </item><item><term> 
## E</term><description> 
##  Stress Recovery point E on a beam cross section </description> </item><item><term> 
## F</term><description> 
##  Stress Recovery point F on a beam cross section </description> </item><item><term> 
## All</term><description> 
##  All four Stress Recovery points on a beam cross section </description> </item></list>
class NodalFunctionEvalBeamLocation(Enum):
    """
    Members Include: <C> <D> <E> <F> <All>
    """
    C: int
    D: int
    E: int
    F: int
    All: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> NodalFunctionEvalBeamLocation:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Specifies response request for nodal function evaluation 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## UserDefinedDirection</term><description> 
##  </description> </item><item><term> 
## DataComponent</term><description> 
##  </description> </item></list>
class NodalFunctionEvalRequest(Enum):
    """
    Members Include: <UserDefinedDirection> <DataComponent>
    """
    UserDefinedDirection: int
    DataComponent: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> NodalFunctionEvalRequest:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Specifies shell element evaluation locations for nodal function evaluation 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Top</term><description> 
##  Top layer </description> </item><item><term> 
## Middle</term><description> 
##  Middle layer </description> </item><item><term> 
## Bottom</term><description> 
##  Bottom layer </description> </item><item><term> 
## All</term><description> 
##  All three layers </description> </item></list>
class NodalFunctionEvalShellLocation(Enum):
    """
    Members Include: <Top> <Middle> <Bottom> <All>
    """
    Top: int
    Middle: int
    Bottom: int
    All: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> NodalFunctionEvalShellLocation:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
import NXOpen.CAE
##  This is a manager to the @link NXOpen::CAE::ResponseSimulation::NodalFunctionEvaluationSetting NXOpen::CAE::ResponseSimulation::NodalFunctionEvaluationSetting@endlink  class. 
##     Object of type @link NXOpen::CAE::ResponseSimulation::NodalFunctionEvaluationSetting NXOpen::CAE::ResponseSimulation::NodalFunctionEvaluationSetting@endlink  can be 
##     created and edited only through this class
##       <br> To create a new instance of this class, use @link NXOpen::CAE::ResponseSimulation::EvaluationSettingManager::CreateNodalFunctionEvaluationSettingBuilder  NXOpen::CAE::ResponseSimulation::EvaluationSettingManager::CreateNodalFunctionEvaluationSettingBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class NodalFunctionEvaluationSettingBuilder(FunctionEvaluationSettingBuilder): 
    """ This is a manager to the <ja_class>NXOpen.CAE.ResponseSimulation.NodalFunctionEvaluationSetting</ja_class> class. 
    Object of type <ja_class>NXOpen.CAE.ResponseSimulation.NodalFunctionEvaluationSetting</ja_class> can be 
    created and edited only through this class
     """


    ## Getter for property: (@link NodalFunctionEvalBeamLocation NXOpen.CAE.ResponseSimulation.NodalFunctionEvalBeamLocation@endlink) BeamDataLocation
    ##  Returns the evaluation location of beam element, which is available when 
    ##             @link NXOpen::CAE::ResponseSimulation::EvaluationResultType NXOpen::CAE::ResponseSimulation::EvaluationResultType@endlink  is 
    ##             @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStress NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStress@endlink , or
    ##             @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStrain NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink    
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NodalFunctionEvalBeamLocation
    @property
    def BeamDataLocation(self) -> NodalFunctionEvalBeamLocation:
        """
        Getter for property: (@link NodalFunctionEvalBeamLocation NXOpen.CAE.ResponseSimulation.NodalFunctionEvalBeamLocation@endlink) BeamDataLocation
         Returns the evaluation location of beam element, which is available when 
                    @link NXOpen::CAE::ResponseSimulation::EvaluationResultType NXOpen::CAE::ResponseSimulation::EvaluationResultType@endlink  is 
                    @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStress NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStress@endlink , or
                    @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStrain NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink    
            
         
        """
        pass
    
    ## Setter for property: (@link NodalFunctionEvalBeamLocation NXOpen.CAE.ResponseSimulation.NodalFunctionEvalBeamLocation@endlink) BeamDataLocation

    ##  Returns the evaluation location of beam element, which is available when 
    ##             @link NXOpen::CAE::ResponseSimulation::EvaluationResultType NXOpen::CAE::ResponseSimulation::EvaluationResultType@endlink  is 
    ##             @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStress NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStress@endlink , or
    ##             @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStrain NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink    
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @BeamDataLocation.setter
    def BeamDataLocation(self, beam_location: NodalFunctionEvalBeamLocation):
        """
        Setter for property: (@link NodalFunctionEvalBeamLocation NXOpen.CAE.ResponseSimulation.NodalFunctionEvalBeamLocation@endlink) BeamDataLocation
         Returns the evaluation location of beam element, which is available when 
                    @link NXOpen::CAE::ResponseSimulation::EvaluationResultType NXOpen::CAE::ResponseSimulation::EvaluationResultType@endlink  is 
                    @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStress NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStress@endlink , or
                    @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStrain NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink    
            
         
        """
        pass
    
    ## Getter for property: (@link CoordinateSystem NXOpen.CAE.ResponseSimulation.CoordinateSystem@endlink) CoordinateSystem
    ##  Returns the coordinate system   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return CoordinateSystem
    @property
    def CoordinateSystem(self) -> CoordinateSystem:
        """
        Getter for property: (@link CoordinateSystem NXOpen.CAE.ResponseSimulation.CoordinateSystem@endlink) CoordinateSystem
         Returns the coordinate system   
            
         
        """
        pass
    
    ## Setter for property: (@link CoordinateSystem NXOpen.CAE.ResponseSimulation.CoordinateSystem@endlink) CoordinateSystem

    ##  Returns the coordinate system   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @CoordinateSystem.setter
    def CoordinateSystem(self, coordinate_system: CoordinateSystem):
        """
        Setter for property: (@link CoordinateSystem NXOpen.CAE.ResponseSimulation.CoordinateSystem@endlink) CoordinateSystem
         Returns the coordinate system   
            
         
        """
        pass
    
    ## Getter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) DataComponent
    ##  Returns the direction data component   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return DirectionDataComponent
    @property
    def DataComponent(self) -> DirectionDataComponent:
        """
        Getter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) DataComponent
         Returns the direction data component   
            
         
        """
        pass
    
    ## Setter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) DataComponent

    ##  Returns the direction data component   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @DataComponent.setter
    def DataComponent(self, data_component: DirectionDataComponent):
        """
        Setter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) DataComponent
         Returns the direction data component   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.FENode NXOpen.CAE.FENode@endlink) RelativeNode
    ##  Returns the relative node    
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return NXOpen.CAE.FENode
    @property
    def RelativeNode(self) -> NXOpen.CAE.FENode:
        """
        Getter for property: (@link NXOpen.CAE.FENode NXOpen.CAE.FENode@endlink) RelativeNode
         Returns the relative node    
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.FENode NXOpen.CAE.FENode@endlink) RelativeNode

    ##  Returns the relative node    
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @RelativeNode.setter
    def RelativeNode(self, relative_node: NXOpen.CAE.FENode):
        """
        Setter for property: (@link NXOpen.CAE.FENode NXOpen.CAE.FENode@endlink) RelativeNode
         Returns the relative node    
            
         
        """
        pass
    
    ## Getter for property: (@link NodalFunctionEvalShellLocation NXOpen.CAE.ResponseSimulation.NodalFunctionEvalShellLocation@endlink) ShellDataLocation
    ##  Returns the evaluation location of shell element, which is available when 
    ##             @link NXOpen::CAE::ResponseSimulation::EvaluationResultType NXOpen::CAE::ResponseSimulation::EvaluationResultType@endlink  is 
    ##             @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStress NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStress@endlink , or
    ##             @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStrain NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink    
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NodalFunctionEvalShellLocation
    @property
    def ShellDataLocation(self) -> NodalFunctionEvalShellLocation:
        """
        Getter for property: (@link NodalFunctionEvalShellLocation NXOpen.CAE.ResponseSimulation.NodalFunctionEvalShellLocation@endlink) ShellDataLocation
         Returns the evaluation location of shell element, which is available when 
                    @link NXOpen::CAE::ResponseSimulation::EvaluationResultType NXOpen::CAE::ResponseSimulation::EvaluationResultType@endlink  is 
                    @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStress NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStress@endlink , or
                    @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStrain NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink    
            
         
        """
        pass
    
    ## Setter for property: (@link NodalFunctionEvalShellLocation NXOpen.CAE.ResponseSimulation.NodalFunctionEvalShellLocation@endlink) ShellDataLocation

    ##  Returns the evaluation location of shell element, which is available when 
    ##             @link NXOpen::CAE::ResponseSimulation::EvaluationResultType NXOpen::CAE::ResponseSimulation::EvaluationResultType@endlink  is 
    ##             @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStress NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStress@endlink , or
    ##             @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStrain NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink    
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ShellDataLocation.setter
    def ShellDataLocation(self, shell_location: NodalFunctionEvalShellLocation):
        """
        Setter for property: (@link NodalFunctionEvalShellLocation NXOpen.CAE.ResponseSimulation.NodalFunctionEvalShellLocation@endlink) ShellDataLocation
         Returns the evaluation location of shell element, which is available when 
                    @link NXOpen::CAE::ResponseSimulation::EvaluationResultType NXOpen::CAE::ResponseSimulation::EvaluationResultType@endlink  is 
                    @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStress NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStress@endlink , or
                    @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStrain NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStrain@endlink    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) UserDefinedDirection
    ##  Returns  the user defined direction   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def UserDefinedDirection(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) UserDefinedDirection
         Returns  the user defined direction   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) UserDefinedDirection

    ##  Returns  the user defined direction   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @UserDefinedDirection.setter
    def UserDefinedDirection(self, user_defined_direction: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) UserDefinedDirection
         Returns  the user defined direction   
            
         
        """
        pass
    
    ## Getter for property: (@link NodalFunctionEvalRequest NXOpen.CAE.ResponseSimulation.NodalFunctionEvalRequest@endlink) UsingUserDefinedDirection
    ##  Returns the option of using user defined direction   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return NodalFunctionEvalRequest
    @property
    def UsingUserDefinedDirection(self) -> NodalFunctionEvalRequest:
        """
        Getter for property: (@link NodalFunctionEvalRequest NXOpen.CAE.ResponseSimulation.NodalFunctionEvalRequest@endlink) UsingUserDefinedDirection
         Returns the option of using user defined direction   
            
         
        """
        pass
    
    ## Setter for property: (@link NodalFunctionEvalRequest NXOpen.CAE.ResponseSimulation.NodalFunctionEvalRequest@endlink) UsingUserDefinedDirection

    ##  Returns the option of using user defined direction   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @UsingUserDefinedDirection.setter
    def UsingUserDefinedDirection(self, using_user_defined_direction: NodalFunctionEvalRequest):
        """
        Setter for property: (@link NodalFunctionEvalRequest NXOpen.CAE.ResponseSimulation.NodalFunctionEvalRequest@endlink) UsingUserDefinedDirection
         Returns the option of using user defined direction   
            
         
        """
        pass
    
    ##   Returns the destination nodes 
    ##  @return destination_nodes (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetDestinationNodes(self) -> List[NXOpen.CAE.FENode]:
        """
          Returns the destination nodes 
         @return destination_nodes (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink):  .
        """
        pass
    
    ##  Sets the destination nodes 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="destination_nodes"> (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink)  </param>
    def SetDestinationNodes(self, destination_nodes: List[NXOpen.CAE.FENode]) -> None:
        """
         Sets the destination nodes 
        """
        pass
    
##  Represents the parameters setting of nodal function response evaluation. Available to all
##     kinds of event type  <br> To create or edit an instance of this class, use @link NXOpen::CAE::ResponseSimulation::NodalFunctionEvaluationSettingBuilder  NXOpen::CAE::ResponseSimulation::NodalFunctionEvaluationSettingBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class NodalFunctionEvaluationSetting(FunctionEvaluationSetting): 
    """ Represents the parameters setting of nodal function response evaluation. Available to all
    kinds of event type """
    pass


import NXOpen
##  Represents the manager to @link NXOpen::CAE::ResponseSimulation::NodalFunctionExcitation NXOpen::CAE::ResponseSimulation::NodalFunctionExcitation@endlink . 
##     The objects of @link NXOpen::CAE::ResponseSimulation::NodalFunctionExcitation NXOpen::CAE::ResponseSimulation::NodalFunctionExcitation@endlink  
##     can be created or edited on through this class  <br> This is an abstract class, and cannot be created.  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class NodalFunctionExcitationBuilder(ExcitationBuilder): 
    """ Represents the manager to <ja_class>NXOpen.CAE.ResponseSimulation.NodalFunctionExcitation</ja_class>. 
    The objects of <ja_class>NXOpen.CAE.ResponseSimulation.NodalFunctionExcitation</ja_class> 
    can be created or edited on through this class """


    ## Getter for property: (float) FrequencyRangeLowerBound
    ##  Returns the lower bound frequency   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def FrequencyRangeLowerBound(self) -> float:
        """
        Getter for property: (float) FrequencyRangeLowerBound
         Returns the lower bound frequency   
            
         
        """
        pass
    
    ## Setter for property: (float) FrequencyRangeLowerBound

    ##  Returns the lower bound frequency   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @FrequencyRangeLowerBound.setter
    def FrequencyRangeLowerBound(self, lower_bound: float):
        """
        Setter for property: (float) FrequencyRangeLowerBound
         Returns the lower bound frequency   
            
         
        """
        pass
    
    ## Getter for property: (float) FrequencyRangeUpperBound
    ##  Returns the upper bound frequency   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def FrequencyRangeUpperBound(self) -> float:
        """
        Getter for property: (float) FrequencyRangeUpperBound
         Returns the upper bound frequency   
            
         
        """
        pass
    
    ## Setter for property: (float) FrequencyRangeUpperBound

    ##  Returns the upper bound frequency   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @FrequencyRangeUpperBound.setter
    def FrequencyRangeUpperBound(self, upper_bound: float):
        """
        Setter for property: (float) FrequencyRangeUpperBound
         Returns the upper bound frequency   
            
         
        """
        pass
    
    ## Getter for property: (bool) InheritFrequencyRangeFromFunction
    ##  Returns the option to inherit frequency Range from function   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def InheritFrequencyRangeFromFunction(self) -> bool:
        """
        Getter for property: (bool) InheritFrequencyRangeFromFunction
         Returns the option to inherit frequency Range from function   
            
         
        """
        pass
    
    ## Setter for property: (bool) InheritFrequencyRangeFromFunction

    ##  Returns the option to inherit frequency Range from function   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @InheritFrequencyRangeFromFunction.setter
    def InheritFrequencyRangeFromFunction(self, inherit_from_function: bool):
        """
        Setter for property: (bool) InheritFrequencyRangeFromFunction
         Returns the option to inherit frequency Range from function   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InitialAccelerationX
    ##  Returns the initial acceleration X   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def InitialAccelerationX(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InitialAccelerationX
         Returns the initial acceleration X   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InitialAccelerationY
    ##  Returns the initial acceleration Y   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def InitialAccelerationY(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InitialAccelerationY
         Returns the initial acceleration Y   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InitialAccelerationZ
    ##  Returns the initial acceleration Z  
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def InitialAccelerationZ(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InitialAccelerationZ
         Returns the initial acceleration Z  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InitialDisplacementX
    ##  Returns the inital X Displacement   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def InitialDisplacementX(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InitialDisplacementX
         Returns the inital X Displacement   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InitialDisplacementY
    ##  Returns the inital Y Displacement   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def InitialDisplacementY(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InitialDisplacementY
         Returns the inital Y Displacement   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InitialDisplacementZ
    ##  Returns the inital Z Displacement   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def InitialDisplacementZ(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InitialDisplacementZ
         Returns the inital Z Displacement   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InitialUserDefDirAcceleration
    ##  Returns the inital user defined direction Acceleration   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def InitialUserDefDirAcceleration(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InitialUserDefDirAcceleration
         Returns the inital user defined direction Acceleration   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InitialUserDefDirDisplacement
    ##  Returns the inital user defined direction Displacement   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def InitialUserDefDirDisplacement(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InitialUserDefDirDisplacement
         Returns the inital user defined direction Displacement   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InitialUserDefDirVelocity
    ##  Returns the inital user defined direction Velocity   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def InitialUserDefDirVelocity(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InitialUserDefDirVelocity
         Returns the inital user defined direction Velocity   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InitialVelocityX
    ##  Returns the initial velocity X   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def InitialVelocityX(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InitialVelocityX
         Returns the initial velocity X   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InitialVelocityY
    ##  Returns the initial velocity Y   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def InitialVelocityY(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InitialVelocityY
         Returns the initial velocity Y   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InitialVelocityZ
    ##  Returns the initial velocity Z   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def InitialVelocityZ(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InitialVelocityZ
         Returns the initial velocity Z   
            
         
        """
        pass
    
    ## Getter for property: (bool) UserSpecifiedInitialExcitationConditionsToggle
    ##  Returns the user specified initial excitation conditions toggle   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def UserSpecifiedInitialExcitationConditionsToggle(self) -> bool:
        """
        Getter for property: (bool) UserSpecifiedInitialExcitationConditionsToggle
         Returns the user specified initial excitation conditions toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) UserSpecifiedInitialExcitationConditionsToggle

    ##  Returns the user specified initial excitation conditions toggle   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @UserSpecifiedInitialExcitationConditionsToggle.setter
    def UserSpecifiedInitialExcitationConditionsToggle(self, initial_conditions_toggle: bool):
        """
        Setter for property: (bool) UserSpecifiedInitialExcitationConditionsToggle
         Returns the user specified initial excitation conditions toggle   
            
         
        """
        pass
    
##  Represents the abstract class of nodal function excitation  <br> This is an abstract class, and cannot be created.  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class NodalFunctionExcitation(Excitation): 
    """ Represents the abstract class of nodal function excitation """


    ##  the subtype of nodal function excitation 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NodalForce</term><description> 
    ##   </description> </item><item><term> 
    ## EnforcedMotion</term><description> 
    ##   </description> </item></list>
    class Type(Enum):
        """
        Members Include: <NodalForce> <EnforcedMotion>
        """
        NodalForce: int
        EnforcedMotion: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> NodalFunctionExcitation.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
import NXOpen
##  Represents the properties of one normal mode 
## 
##   <br>  Created in NX5.0.0  <br> 

class NormalMode(NXOpen.NXObject): 
    """ Represents the properties of one normal mode """


    ## Getter for property: (bool) Active
    ##  Returns the activate status   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Active(self) -> bool:
        """
        Getter for property: (bool) Active
         Returns the activate status   
            
         
        """
        pass
    
    ## Setter for property: (bool) Active

    ##  Returns the activate status   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Active.setter
    def Active(self, active: bool):
        """
        Setter for property: (bool) Active
         Returns the activate status   
            
         
        """
        pass
    
    ## Getter for property: (float) Hysteretic
    ##  Returns the hysteretic factor   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def Hysteretic(self) -> float:
        """
        Getter for property: (float) Hysteretic
         Returns the hysteretic factor   
            
         
        """
        pass
    
    ## Setter for property: (float) Hysteretic

    ##  Returns the hysteretic factor   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Hysteretic.setter
    def Hysteretic(self, hysteretic: float):
        """
        Setter for property: (float) Hysteretic
         Returns the hysteretic factor   
            
         
        """
        pass
    
    ## Getter for property: (float) Viscous
    ##  Returns the viscous factor   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def Viscous(self) -> float:
        """
        Getter for property: (float) Viscous
         Returns the viscous factor   
            
         
        """
        pass
    
    ## Setter for property: (float) Viscous

    ##  Returns the viscous factor   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Viscous.setter
    def Viscous(self, viscous: float):
        """
        Setter for property: (float) Viscous
         Returns the viscous factor   
            
         
        """
        pass
    
    ##  Returns the natrual frequency of the normal mode 
    ##  @return frequency (float):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetFrequency(self) -> float:
        """
         Returns the natrual frequency of the normal mode 
         @return frequency (float):  .
        """
        pass
    
    ##  Returns the mass of the normal mode 
    ##  @return mass (float):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetMass(self) -> float:
        """
         Returns the mass of the normal mode 
         @return mass (float):  .
        """
        pass
    
    ##  Returns mode ID 
    ##  @return mode_id (int):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetModeId(self) -> int:
        """
         Returns mode ID 
         @return mode_id (int):  .
        """
        pass
    
    ##  Returns the physical hysteretic factor 
    ##  @return physical_hysteretic (float):  .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetPhysicalHysteretic(self) -> float:
        """
         Returns the physical hysteretic factor 
         @return physical_hysteretic (float):  .
        """
        pass
    
    ##  Returns the physical viscous factor 
    ##  @return physical_viscous (float):  .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetPhysicalViscous(self) -> float:
        """
         Returns the physical viscous factor 
         @return physical_viscous (float):  .
        """
        pass
    
    ##  Returns the percent mass of Rx direction component 
    ##  @return rx_mass (float):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetRxMass(self) -> float:
        """
         Returns the percent mass of Rx direction component 
         @return rx_mass (float):  .
        """
        pass
    
    ##  Returns the percent mass of Ry direction component 
    ##  @return ry_mass (float):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetRyMass(self) -> float:
        """
         Returns the percent mass of Ry direction component 
         @return ry_mass (float):  .
        """
        pass
    
    ##  Returns the percent mass of Rz direction component 
    ##  @return rz_mass (float):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetRzMass(self) -> float:
        """
         Returns the percent mass of Rz direction component 
         @return rz_mass (float):  .
        """
        pass
    
    ##  Returns the stiffeness of the normal mode 
    ##  @return stiffeness (float):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetStiffeness(self) -> float:
        """
         Returns the stiffeness of the normal mode 
         @return stiffeness (float):  .
        """
        pass
    
    ##  Returns the percent mass of X direction component 
    ##  @return x_mass (float):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetXMass(self) -> float:
        """
         Returns the percent mass of X direction component 
         @return x_mass (float):  .
        """
        pass
    
    ##  Returns the percent mass of Y direction component 
    ##  @return y_mass (float):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetYMass(self) -> float:
        """
         Returns the percent mass of Y direction component 
         @return y_mass (float):  .
        """
        pass
    
    ##  Returns the percent mass of Z direction component 
    ##  @return z_mass (float):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetZMass(self) -> float:
        """
         Returns the percent mass of Z direction component 
         @return z_mass (float):  .
        """
        pass
    
import NXOpen
##  Represents the setting to label an object. Includes name and description 
## 
##   <br>  Created in NX5.0.0  <br> 

class ObjectLabel(NXOpen.TaggedObject): 
    """ Represents the setting to label an object. Includes name and description """


    ## Getter for property: (str) Name
    ##  Returns the object name   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the object name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the object name   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the object name   
            
         
        """
        pass
    
    ##  Returns the description for the object 
    ##  @return description (List[str]):  .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetDescriptions(self) -> List[str]:
        """
         Returns the description for the object 
         @return description (List[str]):  .
        """
        pass
    
    ##  Sets the description for the object 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="description"> (List[str])  </param>
    def SetDescriptions(self, description: List[str]) -> None:
        """
         Sets the description for the object 
        """
        pass
    
##  This is a manager to the @link NXOpen::CAE::ResponseSimulation::PeakValueEvaluationSetting NXOpen::CAE::ResponseSimulation::PeakValueEvaluationSetting@endlink  class. 
##     Object of type @link NXOpen::CAE::ResponseSimulation::PeakValueEvaluationSetting NXOpen::CAE::ResponseSimulation::PeakValueEvaluationSetting@endlink  can be 
##     created and edited only through this class
##       <br> To create a new instance of this class, use @link NXOpen::CAE::ResponseSimulation::EvaluationSettingManager::CreatePeakValueEvaluationSettingBuilder  NXOpen::CAE::ResponseSimulation::EvaluationSettingManager::CreatePeakValueEvaluationSettingBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class PeakValueEvaluationSettingBuilder(PrlResultsEvaluationSettingBuilder): 
    """ This is a manager to the <ja_class>NXOpen.CAE.ResponseSimulation.PeakValueEvaluationSetting</ja_class> class. 
    Object of type <ja_class>NXOpen.CAE.ResponseSimulation.PeakValueEvaluationSetting</ja_class> can be 
    created and edited only through this class
     """


    ## Getter for property: (@link CombinationEvaluationOptions NXOpen.CAE.ResponseSimulation.CombinationEvaluationOptions@endlink) CombinationOptions
    ##  Returns the setting of combination evaluation.  
    ##    Only available when event type is
    ##         @link NXOpen::CAE::ResponseSimulation::RSEvent::TypeRandom NXOpen::CAE::ResponseSimulation::RSEvent::TypeRandom@endlink  or
    ##         @link NXOpen::CAE::ResponseSimulation::RSEvent::TypeResponseSpectrum NXOpen::CAE::ResponseSimulation::RSEvent::TypeResponseSpectrum@endlink   
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return CombinationEvaluationOptions
    @property
    def CombinationOptions(self) -> CombinationEvaluationOptions:
        """
        Getter for property: (@link CombinationEvaluationOptions NXOpen.CAE.ResponseSimulation.CombinationEvaluationOptions@endlink) CombinationOptions
         Returns the setting of combination evaluation.  
           Only available when event type is
                @link NXOpen::CAE::ResponseSimulation::RSEvent::TypeRandom NXOpen::CAE::ResponseSimulation::RSEvent::TypeRandom@endlink  or
                @link NXOpen::CAE::ResponseSimulation::RSEvent::TypeResponseSpectrum NXOpen::CAE::ResponseSimulation::RSEvent::TypeResponseSpectrum@endlink   
         
        """
        pass
    
##  Represents the parameters setting of peak value evaluation. Only NOT available when
##     event type is @link NXOpen::CAE::ResponseSimulation::RSEvent::TypeRandom NXOpen::CAE::ResponseSimulation::RSEvent::TypeRandom@endlink . For more information,
##     see the Response Dynamics section of the Gateway Help  <br> To create or edit an instance of this class, use @link NXOpen::CAE::ResponseSimulation::PeakValueEvaluationSettingBuilder  NXOpen::CAE::ResponseSimulation::PeakValueEvaluationSettingBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class PeakValueEvaluationSetting(PrlResultsEvaluationSetting): 
    """ Represents the parameters setting of peak value evaluation. Only NOT available when
    event type is <ja_enum_member>NXOpen.CAE.ResponseSimulation.RSEvent.Type.Random</ja_enum_member>. For more information,
    see the Response Dynamics section of the Gateway Help """
    pass


import NXOpen
##  Represents the physical damping settings for a response simulation meta solution 
## 
##   <br>  Created in NX6.0.0  <br> 

class PhysicalDampingSettings(NXOpen.TaggedObject): 
    """ Represents the physical damping settings for a response simulation meta solution """


    ## Getter for property: (float) PhysicalHystereticScalingFactor
    ##  Returns the scaling factor for physical hysteretic damping   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return float
    @property
    def PhysicalHystereticScalingFactor(self) -> float:
        """
        Getter for property: (float) PhysicalHystereticScalingFactor
         Returns the scaling factor for physical hysteretic damping   
            
         
        """
        pass
    
    ## Setter for property: (float) PhysicalHystereticScalingFactor

    ##  Returns the scaling factor for physical hysteretic damping   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @PhysicalHystereticScalingFactor.setter
    def PhysicalHystereticScalingFactor(self, scalingFactor: float):
        """
        Setter for property: (float) PhysicalHystereticScalingFactor
         Returns the scaling factor for physical hysteretic damping   
            
         
        """
        pass
    
    ## Getter for property: (float) PhysicalViscousScalingFactor
    ##  Returns the scaling factor for physical viscous damping   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return float
    @property
    def PhysicalViscousScalingFactor(self) -> float:
        """
        Getter for property: (float) PhysicalViscousScalingFactor
         Returns the scaling factor for physical viscous damping   
            
         
        """
        pass
    
    ## Setter for property: (float) PhysicalViscousScalingFactor

    ##  Returns the scaling factor for physical viscous damping   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @PhysicalViscousScalingFactor.setter
    def PhysicalViscousScalingFactor(self, scalingFactor: float):
        """
        Setter for property: (float) PhysicalViscousScalingFactor
         Returns the scaling factor for physical viscous damping   
            
         
        """
        pass
    
    ## Getter for property: (bool) UsingPhysicalHysteretic
    ##  Returns the usage setting for physical hysteretic damping   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def UsingPhysicalHysteretic(self) -> bool:
        """
        Getter for property: (bool) UsingPhysicalHysteretic
         Returns the usage setting for physical hysteretic damping   
            
         
        """
        pass
    
    ## Setter for property: (bool) UsingPhysicalHysteretic

    ##  Returns the usage setting for physical hysteretic damping   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @UsingPhysicalHysteretic.setter
    def UsingPhysicalHysteretic(self, usingPhysicalHysteretic: bool):
        """
        Setter for property: (bool) UsingPhysicalHysteretic
         Returns the usage setting for physical hysteretic damping   
            
         
        """
        pass
    
    ## Getter for property: (bool) UsingPhysicalViscous
    ##  Returns the usage setting for physical viscous damping   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def UsingPhysicalViscous(self) -> bool:
        """
        Getter for property: (bool) UsingPhysicalViscous
         Returns the usage setting for physical viscous damping   
            
         
        """
        pass
    
    ## Setter for property: (bool) UsingPhysicalViscous

    ##  Returns the usage setting for physical viscous damping   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @UsingPhysicalViscous.setter
    def UsingPhysicalViscous(self, usingPhysicalViscous: bool):
        """
        Setter for property: (bool) UsingPhysicalViscous
         Returns the usage setting for physical viscous damping   
            
         
        """
        pass
    
import NXOpen.CAE
##  Represents the abstract builder class of evaluation setting for peak value, RMS results
##     and LCR results.  <br> This is an abstract class, and cannot be created.  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class PrlResultsEvaluationSettingBuilder(DynamicResultEvaluationSettingBuilder): 
    """ Represents the abstract builder class of evaluation setting for peak value, RMS results
    and LCR results. """


    ## Getter for property: (@link CoordinateSystem NXOpen.CAE.ResponseSimulation.CoordinateSystem@endlink) CoordinateSystem
    ##  Returns the coordinate system.  
    ##    Only available when the result type is 
    ##         @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStress NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStress@endlink ,
    ##         @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeShellResultant NXOpen::CAE::ResponseSimulation::EvaluationResultTypeShellResultant@endlink 
    ##           
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return CoordinateSystem
    @property
    def CoordinateSystem(self) -> CoordinateSystem:
        """
        Getter for property: (@link CoordinateSystem NXOpen.CAE.ResponseSimulation.CoordinateSystem@endlink) CoordinateSystem
         Returns the coordinate system.  
           Only available when the result type is 
                @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStress NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStress@endlink ,
                @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeShellResultant NXOpen::CAE::ResponseSimulation::EvaluationResultTypeShellResultant@endlink 
                  
         
        """
        pass
    
    ## Setter for property: (@link CoordinateSystem NXOpen.CAE.ResponseSimulation.CoordinateSystem@endlink) CoordinateSystem

    ##  Returns the coordinate system.  
    ##    Only available when the result type is 
    ##         @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStress NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStress@endlink ,
    ##         @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeShellResultant NXOpen::CAE::ResponseSimulation::EvaluationResultTypeShellResultant@endlink 
    ##           
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @CoordinateSystem.setter
    def CoordinateSystem(self, coordinate_system: CoordinateSystem):
        """
        Setter for property: (@link CoordinateSystem NXOpen.CAE.ResponseSimulation.CoordinateSystem@endlink) CoordinateSystem
         Returns the coordinate system.  
           Only available when the result type is 
                @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStress NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStress@endlink ,
                @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeShellResultant NXOpen::CAE::ResponseSimulation::EvaluationResultTypeShellResultant@endlink 
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.FENode NXOpen.CAE.FENode@endlink) ObservationNode
    ##  Returns the relative node.  
    ##   Only available when result type is 
    ##         @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeDisplacement NXOpen::CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink ,
    ##         @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeAcceleration NXOpen::CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink ,
    ##         @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeElementForce NXOpen::CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink 
    ##           
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return NXOpen.CAE.FENode
    @property
    def ObservationNode(self) -> NXOpen.CAE.FENode:
        """
        Getter for property: (@link NXOpen.CAE.FENode NXOpen.CAE.FENode@endlink) ObservationNode
         Returns the relative node.  
          Only available when result type is 
                @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeDisplacement NXOpen::CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink ,
                @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeAcceleration NXOpen::CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink ,
                @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeElementForce NXOpen::CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink 
                  
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.FENode NXOpen.CAE.FENode@endlink) ObservationNode

    ##  Returns the relative node.  
    ##   Only available when result type is 
    ##         @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeDisplacement NXOpen::CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink ,
    ##         @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeAcceleration NXOpen::CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink ,
    ##         @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeElementForce NXOpen::CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink 
    ##           
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ObservationNode.setter
    def ObservationNode(self, relative_node: NXOpen.CAE.FENode):
        """
        Setter for property: (@link NXOpen.CAE.FENode NXOpen.CAE.FENode@endlink) ObservationNode
         Returns the relative node.  
          Only available when result type is 
                @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeDisplacement NXOpen::CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink ,
                @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeAcceleration NXOpen::CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink ,
                @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeElementForce NXOpen::CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink 
                  
         
        """
        pass
    
    ## Getter for property: (bool) Relative
    ##  Returns the option of using the observation node in evaluation
    ##           
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Relative(self) -> bool:
        """
        Getter for property: (bool) Relative
         Returns the option of using the observation node in evaluation
                  
            
         
        """
        pass
    
    ## Setter for property: (bool) Relative

    ##  Returns the option of using the observation node in evaluation
    ##           
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Relative.setter
    def Relative(self, relative: bool):
        """
        Setter for property: (bool) Relative
         Returns the option of using the observation node in evaluation
                  
            
         
        """
        pass
    
    ## Getter for property: (@link EvaluationResultType NXOpen.CAE.ResponseSimulation.EvaluationResultType@endlink) ResultType
    ##  Returns the result type   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return EvaluationResultType
    @property
    def ResultType(self) -> EvaluationResultType:
        """
        Getter for property: (@link EvaluationResultType NXOpen.CAE.ResponseSimulation.EvaluationResultType@endlink) ResultType
         Returns the result type   
            
         
        """
        pass
    
    ## Setter for property: (@link EvaluationResultType NXOpen.CAE.ResponseSimulation.EvaluationResultType@endlink) ResultType

    ##  Returns the result type   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ResultType.setter
    def ResultType(self, result_type: EvaluationResultType):
        """
        Setter for property: (@link EvaluationResultType NXOpen.CAE.ResponseSimulation.EvaluationResultType@endlink) ResultType
         Returns the result type   
            
         
        """
        pass
    
    ## Getter for property: (bool) SpringForceEvaluationFromDisplacement
    ##  Returns the spring force evaluation from displacement flag.  
    ##      
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def SpringForceEvaluationFromDisplacement(self) -> bool:
        """
        Getter for property: (bool) SpringForceEvaluationFromDisplacement
         Returns the spring force evaluation from displacement flag.  
             
         
        """
        pass
    
    ## Setter for property: (bool) SpringForceEvaluationFromDisplacement

    ##  Returns the spring force evaluation from displacement flag.  
    ##      
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @SpringForceEvaluationFromDisplacement.setter
    def SpringForceEvaluationFromDisplacement(self, spring_force_evaluation_from_displacement: bool):
        """
        Setter for property: (bool) SpringForceEvaluationFromDisplacement
         Returns the spring force evaluation from displacement flag.  
             
         
        """
        pass
    
    ##  Returns the direction data components. The condidate choices will be changed according to 
    ##         @link NXOpen::CAE::ResponseSimulation::EvaluationResultType NXOpen::CAE::ResponseSimulation::EvaluationResultType@endlink  setting
    ##         
    ##  @return data_component (@link DirectionDataComponent List[NXOpen.CAE.ResponseSimulation.DirectionDataComponent]@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetDataComponents(self) -> List[DirectionDataComponent]:
        """
         Returns the direction data components. The condidate choices will be changed according to 
                @link NXOpen::CAE::ResponseSimulation::EvaluationResultType NXOpen::CAE::ResponseSimulation::EvaluationResultType@endlink  setting
                
         @return data_component (@link DirectionDataComponent List[NXOpen.CAE.ResponseSimulation.DirectionDataComponent]@endlink):  .
        """
        pass
    
    ##  Returns the destination elements. Only available when the result type is 
    ##         @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStress NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStress@endlink ,
    ##         @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeShellResultant NXOpen::CAE::ResponseSimulation::EvaluationResultTypeShellResultant@endlink 
    ##         
    ##  @return destination_elements (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetOutputElements(self) -> List[NXOpen.CAE.FEElement]:
        """
         Returns the destination elements. Only available when the result type is 
                @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStress NXOpen::CAE::ResponseSimulation::EvaluationResultTypeStress@endlink ,
                @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeShellResultant NXOpen::CAE::ResponseSimulation::EvaluationResultTypeShellResultant@endlink 
                
         @return destination_elements (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink):  .
        """
        pass
    
    ##  Returns the destination nodes. Only available when result type is 
    ##         @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeDisplacement NXOpen::CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink ,
    ##         @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeAcceleration NXOpen::CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink ,
    ##         @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeElementForce NXOpen::CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink 
    ##         
    ##  @return destination_nodes (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetOutputNodes(self) -> List[NXOpen.CAE.FENode]:
        """
         Returns the destination nodes. Only available when result type is 
                @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeDisplacement NXOpen::CAE::ResponseSimulation::EvaluationResultTypeDisplacement@endlink ,
                @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeAcceleration NXOpen::CAE::ResponseSimulation::EvaluationResultTypeAcceleration@endlink ,
                @link NXOpen::CAE::ResponseSimulation::EvaluationResultTypeElementForce NXOpen::CAE::ResponseSimulation::EvaluationResultTypeElementForce@endlink 
                
         @return destination_nodes (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink):  .
        """
        pass
    
    ##  Sets the direction data components. The condidate choices will be changed according to 
    ##         @link NXOpen::CAE::ResponseSimulation::EvaluationResultType NXOpen::CAE::ResponseSimulation::EvaluationResultType@endlink  setting
    ##         
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="data_component"> (@link DirectionDataComponent List[NXOpen.CAE.ResponseSimulation.DirectionDataComponent]@endlink)  </param>
    def SetDataComponents(self, data_component: List[DirectionDataComponent]) -> None:
        """
         Sets the direction data components. The condidate choices will be changed according to 
                @link NXOpen::CAE::ResponseSimulation::EvaluationResultType NXOpen::CAE::ResponseSimulation::EvaluationResultType@endlink  setting
                
        """
        pass
    
    ##  Sets the destination elements 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="destination_elements"> (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink)  </param>
    def SetOutputElements(self, destination_elements: List[NXOpen.CAE.FEElement]) -> None:
        """
         Sets the destination elements 
        """
        pass
    
    ##  Sets the destination nodes 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="destination_nodes"> (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink)  </param>
    def SetOutputNodes(self, destination_nodes: List[NXOpen.CAE.FENode]) -> None:
        """
         Sets the destination nodes 
        """
        pass
    
##  Represents the abstract class of evaluation setting for peak value, RMS results
##     and LCR results.  <br> This is an abstract class, and cannot be created.  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class PrlResultsEvaluationSetting(DynamicResultEvaluationSetting): 
    """ Represents the abstract class of evaluation setting for peak value, RMS results
    and LCR results. """
    pass


##  Specifies response result evaluation options
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## StartEndPoint</term><description> 
##  </description> </item><item><term> 
## KeyIn</term><description> 
##  </description> </item><item><term> 
## NaturalFrequency</term><description> 
##  </description> </item></list>
class ResponseDomainDefinitionMethod(Enum):
    """
    Members Include: <StartEndPoint> <KeyIn> <NaturalFrequency>
    """
    StartEndPoint: int
    KeyIn: int
    NaturalFrequency: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> ResponseDomainDefinitionMethod:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen.CAE
##  This is a manager to the @link NXOpen::CAE::ResponseSimulation::ResponseResultsEvaluationSetting NXOpen::CAE::ResponseSimulation::ResponseResultsEvaluationSetting@endlink  class. 
##     Object of type @link NXOpen::CAE::ResponseSimulation::ResponseResultsEvaluationSetting NXOpen::CAE::ResponseSimulation::ResponseResultsEvaluationSetting@endlink  can be 
##     created and edited only through this class
##       <br> To create a new instance of this class, use @link NXOpen::CAE::ResponseSimulation::EvaluationSettingManager::CreateResponseResultsEvaluationSettingBuilder  NXOpen::CAE::ResponseSimulation::EvaluationSettingManager::CreateResponseResultsEvaluationSettingBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class ResponseResultsEvaluationSettingBuilder(DynamicResultEvaluationSettingBuilder): 
    """ This is a manager to the <ja_class>NXOpen.CAE.ResponseSimulation.ResponseResultsEvaluationSetting</ja_class> class. 
    Object of type <ja_class>NXOpen.CAE.ResponseSimulation.ResponseResultsEvaluationSetting</ja_class> can be 
    created and edited only through this class
     """


    ## Getter for property: (int) DecimationOrder
    ##  Returns the decimation order of domain setting.  
    ##    Only available when response domain is
    ##          @link CAE::ResponseSimulation::ResponseDomainDefinitionMethodStartEndPoint CAE::ResponseSimulation::ResponseDomainDefinitionMethodStartEndPoint@endlink    
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def DecimationOrder(self) -> int:
        """
        Getter for property: (int) DecimationOrder
         Returns the decimation order of domain setting.  
           Only available when response domain is
                 @link CAE::ResponseSimulation::ResponseDomainDefinitionMethodStartEndPoint CAE::ResponseSimulation::ResponseDomainDefinitionMethodStartEndPoint@endlink    
         
        """
        pass
    
    ## Setter for property: (int) DecimationOrder

    ##  Returns the decimation order of domain setting.  
    ##    Only available when response domain is
    ##          @link CAE::ResponseSimulation::ResponseDomainDefinitionMethodStartEndPoint CAE::ResponseSimulation::ResponseDomainDefinitionMethodStartEndPoint@endlink    
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @DecimationOrder.setter
    def DecimationOrder(self, decimation_order: int):
        """
        Setter for property: (int) DecimationOrder
         Returns the decimation order of domain setting.  
           Only available when response domain is
                 @link CAE::ResponseSimulation::ResponseDomainDefinitionMethodStartEndPoint CAE::ResponseSimulation::ResponseDomainDefinitionMethodStartEndPoint@endlink    
         
        """
        pass
    
    ## Getter for property: (float) EndPoint
    ##  Returns the end value of domain setting.  
    ##    Only available when response domain is 
    ##          @link CAE::ResponseSimulation::ResponseDomainDefinitionMethodStartEndPoint CAE::ResponseSimulation::ResponseDomainDefinitionMethodStartEndPoint@endlink    
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def EndPoint(self) -> float:
        """
        Getter for property: (float) EndPoint
         Returns the end value of domain setting.  
           Only available when response domain is 
                 @link CAE::ResponseSimulation::ResponseDomainDefinitionMethodStartEndPoint CAE::ResponseSimulation::ResponseDomainDefinitionMethodStartEndPoint@endlink    
         
        """
        pass
    
    ## Setter for property: (float) EndPoint

    ##  Returns the end value of domain setting.  
    ##    Only available when response domain is 
    ##          @link CAE::ResponseSimulation::ResponseDomainDefinitionMethodStartEndPoint CAE::ResponseSimulation::ResponseDomainDefinitionMethodStartEndPoint@endlink    
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @EndPoint.setter
    def EndPoint(self, end_point: float):
        """
        Setter for property: (float) EndPoint
         Returns the end value of domain setting.  
           Only available when response domain is 
                 @link CAE::ResponseSimulation::ResponseDomainDefinitionMethodStartEndPoint CAE::ResponseSimulation::ResponseDomainDefinitionMethodStartEndPoint@endlink    
         
        """
        pass
    
    ## Getter for property: (float) PointValue
    ##  Returns the method choosed to define select point value.  
    ##    Only available when response domain is 
    ##          @link CAE::ResponseSimulation::ResponseDomainDefinitionMethodKeyIn CAE::ResponseSimulation::ResponseDomainDefinitionMethodKeyIn@endlink    
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def PointValue(self) -> float:
        """
        Getter for property: (float) PointValue
         Returns the method choosed to define select point value.  
           Only available when response domain is 
                 @link CAE::ResponseSimulation::ResponseDomainDefinitionMethodKeyIn CAE::ResponseSimulation::ResponseDomainDefinitionMethodKeyIn@endlink    
         
        """
        pass
    
    ## Setter for property: (float) PointValue

    ##  Returns the method choosed to define select point value.  
    ##    Only available when response domain is 
    ##          @link CAE::ResponseSimulation::ResponseDomainDefinitionMethodKeyIn CAE::ResponseSimulation::ResponseDomainDefinitionMethodKeyIn@endlink    
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @PointValue.setter
    def PointValue(self, point_value: float):
        """
        Setter for property: (float) PointValue
         Returns the method choosed to define select point value.  
           Only available when response domain is 
                 @link CAE::ResponseSimulation::ResponseDomainDefinitionMethodKeyIn CAE::ResponseSimulation::ResponseDomainDefinitionMethodKeyIn@endlink    
         
        """
        pass
    
    ## Getter for property: (@link ResponseDomainDefinitionMethod NXOpen.CAE.ResponseSimulation.ResponseDomainDefinitionMethod@endlink) ResponseDomainDefinitionOption
    ##  Returns the method choosed to define response domain   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return ResponseDomainDefinitionMethod
    @property
    def ResponseDomainDefinitionOption(self) -> ResponseDomainDefinitionMethod:
        """
        Getter for property: (@link ResponseDomainDefinitionMethod NXOpen.CAE.ResponseSimulation.ResponseDomainDefinitionMethod@endlink) ResponseDomainDefinitionOption
         Returns the method choosed to define response domain   
            
         
        """
        pass
    
    ## Setter for property: (@link ResponseDomainDefinitionMethod NXOpen.CAE.ResponseSimulation.ResponseDomainDefinitionMethod@endlink) ResponseDomainDefinitionOption

    ##  Returns the method choosed to define response domain   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ResponseDomainDefinitionOption.setter
    def ResponseDomainDefinitionOption(self, definitions_method: ResponseDomainDefinitionMethod):
        """
        Setter for property: (@link ResponseDomainDefinitionMethod NXOpen.CAE.ResponseSimulation.ResponseDomainDefinitionMethod@endlink) ResponseDomainDefinitionOption
         Returns the method choosed to define response domain   
            
         
        """
        pass
    
    ## Getter for property: (bool) SpringForceEvaluationFromDisplacement
    ##  Returns the spring force evaluation from displacement flag.  
    ##      
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def SpringForceEvaluationFromDisplacement(self) -> bool:
        """
        Getter for property: (bool) SpringForceEvaluationFromDisplacement
         Returns the spring force evaluation from displacement flag.  
             
         
        """
        pass
    
    ## Setter for property: (bool) SpringForceEvaluationFromDisplacement

    ##  Returns the spring force evaluation from displacement flag.  
    ##      
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @SpringForceEvaluationFromDisplacement.setter
    def SpringForceEvaluationFromDisplacement(self, spring_force_evaluation_from_displacement: bool):
        """
        Setter for property: (bool) SpringForceEvaluationFromDisplacement
         Returns the spring force evaluation from displacement flag.  
             
         
        """
        pass
    
    ## Getter for property: (float) StartPoint
    ##  Returns the start value of domain setting.  
    ##    Only available when response domain is 
    ##          @link CAE::ResponseSimulation::ResponseDomainDefinitionMethodStartEndPoint CAE::ResponseSimulation::ResponseDomainDefinitionMethodStartEndPoint@endlink    
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def StartPoint(self) -> float:
        """
        Getter for property: (float) StartPoint
         Returns the start value of domain setting.  
           Only available when response domain is 
                 @link CAE::ResponseSimulation::ResponseDomainDefinitionMethodStartEndPoint CAE::ResponseSimulation::ResponseDomainDefinitionMethodStartEndPoint@endlink    
         
        """
        pass
    
    ## Setter for property: (float) StartPoint

    ##  Returns the start value of domain setting.  
    ##    Only available when response domain is 
    ##          @link CAE::ResponseSimulation::ResponseDomainDefinitionMethodStartEndPoint CAE::ResponseSimulation::ResponseDomainDefinitionMethodStartEndPoint@endlink    
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @StartPoint.setter
    def StartPoint(self, start_point: float):
        """
        Setter for property: (float) StartPoint
         Returns the start value of domain setting.  
           Only available when response domain is 
                 @link CAE::ResponseSimulation::ResponseDomainDefinitionMethodStartEndPoint CAE::ResponseSimulation::ResponseDomainDefinitionMethodStartEndPoint@endlink    
         
        """
        pass
    
    ##  Returns the destination elements 
    ##  @return destination_elements (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetDestinationElements(self) -> List[NXOpen.CAE.FEElement]:
        """
         Returns the destination elements 
         @return destination_elements (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink):  .
        """
        pass
    
    ##  Returns the destination nodes 
    ##  @return destination_nodes (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetDestinationNodes(self) -> List[NXOpen.CAE.FENode]:
        """
         Returns the destination nodes 
         @return destination_nodes (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink):  .
        """
        pass
    
    ##  Returns the output options 
    ##  @return output_options (@link EvaluationResultType List[NXOpen.CAE.ResponseSimulation.EvaluationResultType]@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetOutputOptions(self) -> List[EvaluationResultType]:
        """
         Returns the output options 
         @return output_options (@link EvaluationResultType List[NXOpen.CAE.ResponseSimulation.EvaluationResultType]@endlink):  .
        """
        pass
    
    ##  Returns the points value list 
    ##  @return points_value_list (List[float]):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetPointsValueList(self) -> List[float]:
        """
         Returns the points value list 
         @return points_value_list (List[float]):  .
        """
        pass
    
    ##  Sets the destination elements 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="destination_element"> (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink)  </param>
    def SetDestinationElements(self, destination_element: List[NXOpen.CAE.FEElement]) -> None:
        """
         Sets the destination elements 
        """
        pass
    
    ##  Sets the destination nodes 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="destination_nodes"> (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink)  </param>
    def SetDestinationNodes(self, destination_nodes: List[NXOpen.CAE.FENode]) -> None:
        """
         Sets the destination nodes 
        """
        pass
    
    ##  Sets the output options 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="output_options"> (@link EvaluationResultType List[NXOpen.CAE.ResponseSimulation.EvaluationResultType]@endlink)  </param>
    def SetOutputOptions(self, output_options: List[EvaluationResultType]) -> None:
        """
         Sets the output options 
        """
        pass
    
    ##  Sets the points value list 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="points_value_list"> (List[float])  </param>
    def SetPointsValueList(self, points_value_list: List[float]) -> None:
        """
         Sets the points value list 
        """
        pass
    
##  Represents the parameters setting for response results evaluation. Only available when 
##     event type are @link NXOpen::CAE::ResponseSimulation::RSEvent::TypeTransient NXOpen::CAE::ResponseSimulation::RSEvent::TypeTransient@endlink  and 
##     @link NXOpen::CAE::ResponseSimulation::RSEvent::TypeFrequency NXOpen::CAE::ResponseSimulation::RSEvent::TypeFrequency@endlink . For more information, see the 
##     Response Dynamics section of the Gateway Help  <br> To create or edit an instance of this class, use @link NXOpen::CAE::ResponseSimulation::ResponseResultsEvaluationSettingBuilder  NXOpen::CAE::ResponseSimulation::ResponseResultsEvaluationSettingBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class ResponseResultsEvaluationSetting(DynamicResultEvaluationSetting): 
    """ Represents the parameters setting for response results evaluation. Only available when 
    event type are <ja_enum_member>NXOpen.CAE.ResponseSimulation.RSEvent.Type.Transient</ja_enum_member> and 
    <ja_enum_member>NXOpen.CAE.ResponseSimulation.RSEvent.Type.Frequency</ja_enum_member>. For more information, see the 
    Response Dynamics section of the Gateway Help """
    pass


##  Specifies the evaluation method for RMS or LCR calculation 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## SmallNumberItems</term><description> 
##  Small number of evaluation items </description> </item><item><term> 
## LargeNumberItems</term><description> 
##  Large number of evaluation items </description> </item><item><term> 
## AutomaticSelection</term><description> 
##  Automatic selection </description> </item></list>
class RmsLcrEvaluationMethod(Enum):
    """
    Members Include: <SmallNumberItems> <LargeNumberItems> <AutomaticSelection>
    """
    SmallNumberItems: int
    LargeNumberItems: int
    AutomaticSelection: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> RmsLcrEvaluationMethod:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  This is a manager to the @link NXOpen::CAE::ResponseSimulation::RmsResultsEvaluationSetting NXOpen::CAE::ResponseSimulation::RmsResultsEvaluationSetting@endlink  class.
##     Object of type @link NXOpen::CAE::ResponseSimulation::RmsResultsEvaluationSetting NXOpen::CAE::ResponseSimulation::RmsResultsEvaluationSetting@endlink  can be
##     created and edited only through this class
##       <br> To create a new instance of this class, use @link NXOpen::CAE::ResponseSimulation::EvaluationSettingManager::CreateRmsResultsEvaluationSettingBuilder  NXOpen::CAE::ResponseSimulation::EvaluationSettingManager::CreateRmsResultsEvaluationSettingBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class RmsResultsEvaluationSettingBuilder(PrlResultsEvaluationSettingBuilder): 
    """ This is a manager to the <ja_class>NXOpen.CAE.ResponseSimulation.RmsResultsEvaluationSetting</ja_class> class.
    Object of type <ja_class>NXOpen.CAE.ResponseSimulation.RmsResultsEvaluationSetting</ja_class> can be
    created and edited only through this class
     """


    ## Getter for property: (@link RmsLcrEvaluationMethod NXOpen.CAE.ResponseSimulation.RmsLcrEvaluationMethod@endlink) EvaluationMethod
    ##  Returns the evaluation method for RMS   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return RmsLcrEvaluationMethod
    @property
    def EvaluationMethod(self) -> RmsLcrEvaluationMethod:
        """
        Getter for property: (@link RmsLcrEvaluationMethod NXOpen.CAE.ResponseSimulation.RmsLcrEvaluationMethod@endlink) EvaluationMethod
         Returns the evaluation method for RMS   
            
         
        """
        pass
    
    ## Setter for property: (@link RmsLcrEvaluationMethod NXOpen.CAE.ResponseSimulation.RmsLcrEvaluationMethod@endlink) EvaluationMethod

    ##  Returns the evaluation method for RMS   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @EvaluationMethod.setter
    def EvaluationMethod(self, evaluationMethod: RmsLcrEvaluationMethod):
        """
        Setter for property: (@link RmsLcrEvaluationMethod NXOpen.CAE.ResponseSimulation.RmsLcrEvaluationMethod@endlink) EvaluationMethod
         Returns the evaluation method for RMS   
            
         
        """
        pass
    
## Represents the parameters setting for RMS results evaluation in response analysis. Only
##     available when event type is @link NXOpen::CAE::ResponseSimulation::RSEvent::TypeRandom NXOpen::CAE::ResponseSimulation::RSEvent::TypeRandom@endlink   <br> To create or edit an instance of this class, use @link NXOpen::CAE::ResponseSimulation::RmsResultsEvaluationSettingBuilder  NXOpen::CAE::ResponseSimulation::RmsResultsEvaluationSettingBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class RmsResultsEvaluationSetting(PrlResultsEvaluationSetting): 
    """Represents the parameters setting for RMS results evaluation in response analysis. Only
    available when event type is <ja_enum_member>NXOpen.CAE.ResponseSimulation.RSEvent.Type.Random</ja_enum_member> """
    pass


##  Represents the manager to @link CAE::ResponseSimulation::DDAMExcitation CAE::ResponseSimulation::DDAMExcitation@endlink .
##      The object of type @link CAE::ResponseSimulation::DDAMExcitation CAE::ResponseSimulation::DDAMExcitation@endlink  can only
##     be created or edited through this class.  <br> To create a new instance of this class, use @link NXOpen::CAE::ResponseSimulation::ExcitationCollection::CreateRotationalDdamExcitationBuilder  NXOpen::CAE::ResponseSimulation::ExcitationCollection::CreateRotationalDdamExcitationBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class RotationalDDAMExcitationBuilder(DDAMExcitationBuilder): 
    """ Represents the manager to <ja_class>CAE.ResponseSimulation.DDAMExcitation</ja_class>.
     The object of type <ja_class>CAE.ResponseSimulation.DDAMExcitation</ja_class> can only
    be created or edited through this class. """
    pass


##  Represents an DDAM excitation. DDAM excitation could only be used by DDAM event.  <br> To create or edit an instance of this class, use @link NXOpen::CAE::ResponseSimulation::RotationalDDAMExcitationBuilder  NXOpen::CAE::ResponseSimulation::RotationalDDAMExcitationBuilder @endlink  <br> 
class RotationalDDAMExcitation(DDAMExcitation): 
    """ Represents an DDAM excitation. DDAM excitation could only be used by DDAM event. """
    pass


##  Represents the manager to @link NXOpen::CAE::ResponseSimulation::RotationalNodalFunctionExcitation NXOpen::CAE::ResponseSimulation::RotationalNodalFunctionExcitation@endlink . 
##     The objects of @link NXOpen::CAE::ResponseSimulation::RotationalNodalFunctionExcitation NXOpen::CAE::ResponseSimulation::RotationalNodalFunctionExcitation@endlink  
##     can be created or edited on through this class  <br> To create a new instance of this class, use @link NXOpen::CAE::ResponseSimulation::ExcitationCollection::CreateRotationalNodalFunctionExcitationBuilder  NXOpen::CAE::ResponseSimulation::ExcitationCollection::CreateRotationalNodalFunctionExcitationBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class RotationalNodalFunctionExcitationBuilder(NodalFunctionExcitationBuilder): 
    """ Represents the manager to <ja_class>NXOpen.CAE.ResponseSimulation.RotationalNodalFunctionExcitation</ja_class>. 
    The objects of <ja_class>NXOpen.CAE.ResponseSimulation.RotationalNodalFunctionExcitation</ja_class> 
    can be created or edited on through this class """


    ## Getter for property: (@link FunctionComponentData NXOpen.CAE.ResponseSimulation.FunctionComponentData@endlink) FunctionComponentRx
    ##  Returns the function component of Rx direction    
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return FunctionComponentData
    @property
    def FunctionComponentRx(self) -> FunctionComponentData:
        """
        Getter for property: (@link FunctionComponentData NXOpen.CAE.ResponseSimulation.FunctionComponentData@endlink) FunctionComponentRx
         Returns the function component of Rx direction    
            
         
        """
        pass
    
    ## Getter for property: (@link FunctionComponentData NXOpen.CAE.ResponseSimulation.FunctionComponentData@endlink) FunctionComponentRy
    ##  Returns the function component of Ry direction   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return FunctionComponentData
    @property
    def FunctionComponentRy(self) -> FunctionComponentData:
        """
        Getter for property: (@link FunctionComponentData NXOpen.CAE.ResponseSimulation.FunctionComponentData@endlink) FunctionComponentRy
         Returns the function component of Ry direction   
            
         
        """
        pass
    
    ## Getter for property: (@link FunctionComponentData NXOpen.CAE.ResponseSimulation.FunctionComponentData@endlink) FunctionComponentRz
    ##  Returns the function component of Rz direction   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return FunctionComponentData
    @property
    def FunctionComponentRz(self) -> FunctionComponentData:
        """
        Getter for property: (@link FunctionComponentData NXOpen.CAE.ResponseSimulation.FunctionComponentData@endlink) FunctionComponentRz
         Returns the function component of Rz direction   
            
         
        """
        pass
    
##  Represents a rotational nodal function excitation  <br> To create or edit an instance of this class, use @link NXOpen::CAE::ResponseSimulation::RotationalNodalFunctionExcitationBuilder  NXOpen::CAE::ResponseSimulation::RotationalNodalFunctionExcitationBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class RotationalNodalFunctionExcitation(NodalFunctionExcitation): 
    """ Represents a rotational nodal function excitation """
    pass


import NXOpen
##   @brief  Represents a BC display attributes 
## 
##   
## 
##   <br>  Created in NX6.0.0  <br> 

class RSDisplayObject(NXOpen.NXObject): 
    """ <summary> Represents a BC display attributes</summary> """


    ## Getter for property: (bool) DisplayName
    ##  Returns the true/false flag based on whether the name of the BC is
    ##             displayed in the graphics window   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def DisplayName(self) -> bool:
        """
        Getter for property: (bool) DisplayName
         Returns the true/false flag based on whether the name of the BC is
                    displayed in the graphics window   
            
         
        """
        pass
    
    ## Setter for property: (bool) DisplayName

    ##  Returns the true/false flag based on whether the name of the BC is
    ##             displayed in the graphics window   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @DisplayName.setter
    def DisplayName(self, name_flag: bool):
        """
        Setter for property: (bool) DisplayName
         Returns the true/false flag based on whether the name of the BC is
                    displayed in the graphics window   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Scale
    ##  Returns the RS display scaling factor
    ##             this option specifies the scale of the graphic symbol relative to the size of the bounding box of the RS OBject.  
    ##   
    ##             scale -\> 0 
    ##            
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Scale(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Scale
         Returns the RS display scaling factor
                    this option specifies the scale of the graphic symbol relative to the size of the bounding box of the RS OBject.  
          
                    scale -\> 0 
                   
         
        """
        pass
    
import NXOpen
##  Represents all possible attributes setting for response analysis event 
## 
##   <br>  Created in NX5.0.0  <br> 

class RSEventAttributes(NXOpen.TaggedObject): 
    """ Represents all possible attributes setting for response analysis event """


    ## Getter for property: (@link RSEvent.AnalysisType NXOpen.CAE.ResponseSimulation.RSEvent.AnalysisType@endlink) AnalysisType
    ##  Returns the analysis type.  
    ##    Only available for transient event and frequency event   
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return RSEvent.AnalysisType
    @property
    def AnalysisType(self) -> RSEvent.AnalysisType:
        """
        Getter for property: (@link RSEvent.AnalysisType NXOpen.CAE.ResponseSimulation.RSEvent.AnalysisType@endlink) AnalysisType
         Returns the analysis type.  
           Only available for transient event and frequency event   
         
        """
        pass
    
    ## Setter for property: (@link RSEvent.AnalysisType NXOpen.CAE.ResponseSimulation.RSEvent.AnalysisType@endlink) AnalysisType

    ##  Returns the analysis type.  
    ##    Only available for transient event and frequency event   
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @AnalysisType.setter
    def AnalysisType(self, analysis_type: RSEvent.AnalysisType):
        """
        Setter for property: (@link RSEvent.AnalysisType NXOpen.CAE.ResponseSimulation.RSEvent.AnalysisType@endlink) AnalysisType
         Returns the analysis type.  
           Only available for transient event and frequency event   
         
        """
        pass
    
    ## Getter for property: (@link DDAMExcitation.CoefficientDefinitionType NXOpen.CAE.ResponseSimulation.DDAMExcitation.CoefficientDefinitionType@endlink) CoefficientDefinitionMethod
    ##  Returns the DDAM coefficient definition method   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return DDAMExcitation.CoefficientDefinitionType
    @property
    def CoefficientDefinitionMethod(self) -> DDAMExcitation.CoefficientDefinitionType:
        """
        Getter for property: (@link DDAMExcitation.CoefficientDefinitionType NXOpen.CAE.ResponseSimulation.DDAMExcitation.CoefficientDefinitionType@endlink) CoefficientDefinitionMethod
         Returns the DDAM coefficient definition method   
            
         
        """
        pass
    
    ## Setter for property: (@link DDAMExcitation.CoefficientDefinitionType NXOpen.CAE.ResponseSimulation.DDAMExcitation.CoefficientDefinitionType@endlink) CoefficientDefinitionMethod

    ##  Returns the DDAM coefficient definition method   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @CoefficientDefinitionMethod.setter
    def CoefficientDefinitionMethod(self, definition_method: DDAMExcitation.CoefficientDefinitionType):
        """
        Setter for property: (@link DDAMExcitation.CoefficientDefinitionType NXOpen.CAE.ResponseSimulation.DDAMExcitation.CoefficientDefinitionType@endlink) CoefficientDefinitionMethod
         Returns the DDAM coefficient definition method   
            
         
        """
        pass
    
    ## Getter for property: (str) CoefficientFile
    ##  Returns the DDAM coefficients definition file.  
    ##    Only available when event type is
    ##         @link CAE::ResponseSimulation::DDAMExcitation::CoefficientDefinitionTypeByFile CAE::ResponseSimulation::DDAMExcitation::CoefficientDefinitionTypeByFile@endlink .   
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return str
    @property
    def CoefficientFile(self) -> str:
        """
        Getter for property: (str) CoefficientFile
         Returns the DDAM coefficients definition file.  
           Only available when event type is
                @link CAE::ResponseSimulation::DDAMExcitation::CoefficientDefinitionTypeByFile CAE::ResponseSimulation::DDAMExcitation::CoefficientDefinitionTypeByFile@endlink .   
         
        """
        pass
    
    ## Setter for property: (str) CoefficientFile

    ##  Returns the DDAM coefficients definition file.  
    ##    Only available when event type is
    ##         @link CAE::ResponseSimulation::DDAMExcitation::CoefficientDefinitionTypeByFile CAE::ResponseSimulation::DDAMExcitation::CoefficientDefinitionTypeByFile@endlink .   
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @CoefficientFile.setter
    def CoefficientFile(self, coefficient_file: str):
        """
        Setter for property: (str) CoefficientFile
         Returns the DDAM coefficients definition file.  
           Only available when event type is
                @link CAE::ResponseSimulation::DDAMExcitation::CoefficientDefinitionTypeByFile CAE::ResponseSimulation::DDAMExcitation::CoefficientDefinitionTypeByFile@endlink .   
         
        """
        pass
    
    ## Getter for property: (float) Duration
    ##  Returns the time duration in second for transient event   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def Duration(self) -> float:
        """
        Getter for property: (float) Duration
         Returns the time duration in second for transient event   
            
         
        """
        pass
    
    ## Setter for property: (float) Duration

    ##  Returns the time duration in second for transient event   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Duration.setter
    def Duration(self, duration: float):
        """
        Setter for property: (float) Duration
         Returns the time duration in second for transient event   
            
         
        """
        pass
    
    ## Getter for property: (@link RSEvent.DurationOption NXOpen.CAE.ResponseSimulation.RSEvent.DurationOption@endlink) DurationOption
    ##  Returns the time duration optionin option for transient event   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return RSEvent.DurationOption
    @property
    def DurationOption(self) -> RSEvent.DurationOption:
        """
        Getter for property: (@link RSEvent.DurationOption NXOpen.CAE.ResponseSimulation.RSEvent.DurationOption@endlink) DurationOption
         Returns the time duration optionin option for transient event   
            
         
        """
        pass
    
    ## Setter for property: (@link RSEvent.DurationOption NXOpen.CAE.ResponseSimulation.RSEvent.DurationOption@endlink) DurationOption

    ##  Returns the time duration optionin option for transient event   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @DurationOption.setter
    def DurationOption(self, duration_option: RSEvent.DurationOption):
        """
        Setter for property: (@link RSEvent.DurationOption NXOpen.CAE.ResponseSimulation.RSEvent.DurationOption@endlink) DurationOption
         Returns the time duration optionin option for transient event   
            
         
        """
        pass
    
    ## Getter for property: (bool) FastRmsMethod
    ##  Returns the Use Fast RMS Method.  
    ##    Only available when event type is
    ##         @link CAE::ResponseSimulation::RSEvent::TypeRandom CAE::ResponseSimulation::RSEvent::TypeRandom@endlink >,
    ##           
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def FastRmsMethod(self) -> bool:
        """
        Getter for property: (bool) FastRmsMethod
         Returns the Use Fast RMS Method.  
           Only available when event type is
                @link CAE::ResponseSimulation::RSEvent::TypeRandom CAE::ResponseSimulation::RSEvent::TypeRandom@endlink >,
                  
         
        """
        pass
    
    ## Setter for property: (bool) FastRmsMethod

    ##  Returns the Use Fast RMS Method.  
    ##    Only available when event type is
    ##         @link CAE::ResponseSimulation::RSEvent::TypeRandom CAE::ResponseSimulation::RSEvent::TypeRandom@endlink >,
    ##           
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @FastRmsMethod.setter
    def FastRmsMethod(self, fast_rms_method: bool):
        """
        Setter for property: (bool) FastRmsMethod
         Returns the Use Fast RMS Method.  
           Only available when event type is
                @link CAE::ResponseSimulation::RSEvent::TypeRandom CAE::ResponseSimulation::RSEvent::TypeRandom@endlink >,
                  
         
        """
        pass
    
    ## Getter for property: (@link RSEvent.DdamFormulationType NXOpen.CAE.ResponseSimulation.RSEvent.DdamFormulationType@endlink) Formulation
    ##  Returns the DDAM formulation type  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.2  <br> 

    ## @return RSEvent.DdamFormulationType
    @property
    def Formulation(self) -> RSEvent.DdamFormulationType:
        """
        Getter for property: (@link RSEvent.DdamFormulationType NXOpen.CAE.ResponseSimulation.RSEvent.DdamFormulationType@endlink) Formulation
         Returns the DDAM formulation type  
            
         
        """
        pass
    
    ## Setter for property: (@link RSEvent.DdamFormulationType NXOpen.CAE.ResponseSimulation.RSEvent.DdamFormulationType@endlink) Formulation

    ##  Returns the DDAM formulation type  
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX7.5.2  <br> 

    @Formulation.setter
    def Formulation(self, formulation: RSEvent.DdamFormulationType):
        """
        Setter for property: (@link RSEvent.DdamFormulationType NXOpen.CAE.ResponseSimulation.RSEvent.DdamFormulationType@endlink) Formulation
         Returns the DDAM formulation type  
            
         
        """
        pass
    
    ## Getter for property: (@link InterpolationMethod NXOpen.CAE.ResponseSimulation.InterpolationMethod@endlink) InterpolationMethod
    ##  Returns the interpolation method.  
    ##    only available when event type is
    ##         @link CAE::ResponseSimulation::RSEvent::TypeFrequency CAE::ResponseSimulation::RSEvent::TypeFrequency@endlink ,
    ##         @link CAE::ResponseSimulation::RSEvent::TypeRandom CAE::ResponseSimulation::RSEvent::TypeRandom@endlink , 
    ##         @link CAE::ResponseSimulation::RSEvent::TypeResponseSpectrum CAE::ResponseSimulation::RSEvent::TypeResponseSpectrum@endlink ,
    ##           
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return InterpolationMethod
    @property
    def InterpolationMethod(self) -> InterpolationMethod:
        """
        Getter for property: (@link InterpolationMethod NXOpen.CAE.ResponseSimulation.InterpolationMethod@endlink) InterpolationMethod
         Returns the interpolation method.  
           only available when event type is
                @link CAE::ResponseSimulation::RSEvent::TypeFrequency CAE::ResponseSimulation::RSEvent::TypeFrequency@endlink ,
                @link CAE::ResponseSimulation::RSEvent::TypeRandom CAE::ResponseSimulation::RSEvent::TypeRandom@endlink , 
                @link CAE::ResponseSimulation::RSEvent::TypeResponseSpectrum CAE::ResponseSimulation::RSEvent::TypeResponseSpectrum@endlink ,
                  
         
        """
        pass
    
    ## Setter for property: (@link InterpolationMethod NXOpen.CAE.ResponseSimulation.InterpolationMethod@endlink) InterpolationMethod

    ##  Returns the interpolation method.  
    ##    only available when event type is
    ##         @link CAE::ResponseSimulation::RSEvent::TypeFrequency CAE::ResponseSimulation::RSEvent::TypeFrequency@endlink ,
    ##         @link CAE::ResponseSimulation::RSEvent::TypeRandom CAE::ResponseSimulation::RSEvent::TypeRandom@endlink , 
    ##         @link CAE::ResponseSimulation::RSEvent::TypeResponseSpectrum CAE::ResponseSimulation::RSEvent::TypeResponseSpectrum@endlink ,
    ##           
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @InterpolationMethod.setter
    def InterpolationMethod(self, interpolation_method: InterpolationMethod):
        """
        Setter for property: (@link InterpolationMethod NXOpen.CAE.ResponseSimulation.InterpolationMethod@endlink) InterpolationMethod
         Returns the interpolation method.  
           only available when event type is
                @link CAE::ResponseSimulation::RSEvent::TypeFrequency CAE::ResponseSimulation::RSEvent::TypeFrequency@endlink ,
                @link CAE::ResponseSimulation::RSEvent::TypeRandom CAE::ResponseSimulation::RSEvent::TypeRandom@endlink , 
                @link CAE::ResponseSimulation::RSEvent::TypeResponseSpectrum CAE::ResponseSimulation::RSEvent::TypeResponseSpectrum@endlink ,
                  
         
        """
        pass
    
    ## Getter for property: (float) MinimumGValue
    ##  Returns the Minimum G value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.2  <br> 

    ## @return float
    @property
    def MinimumGValue(self) -> float:
        """
        Getter for property: (float) MinimumGValue
         Returns the Minimum G value   
            
         
        """
        pass
    
    ## Setter for property: (float) MinimumGValue

    ##  Returns the Minimum G value   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX7.5.2  <br> 

    @MinimumGValue.setter
    def MinimumGValue(self, minimumG: float):
        """
        Setter for property: (float) MinimumGValue
         Returns the Minimum G value   
            
         
        """
        pass
    
    ## Getter for property: (@link DDAMExcitation.MountingType NXOpen.CAE.ResponseSimulation.DDAMExcitation.MountingType@endlink) MountingType
    ##  Returns the ship type  
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return DDAMExcitation.MountingType
    @property
    def MountingType(self) -> DDAMExcitation.MountingType:
        """
        Getter for property: (@link DDAMExcitation.MountingType NXOpen.CAE.ResponseSimulation.DDAMExcitation.MountingType@endlink) MountingType
         Returns the ship type  
            
         
        """
        pass
    
    ## Setter for property: (@link DDAMExcitation.MountingType NXOpen.CAE.ResponseSimulation.DDAMExcitation.MountingType@endlink) MountingType

    ##  Returns the ship type  
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @MountingType.setter
    def MountingType(self, mounting_type: DDAMExcitation.MountingType):
        """
        Setter for property: (@link DDAMExcitation.MountingType NXOpen.CAE.ResponseSimulation.DDAMExcitation.MountingType@endlink) MountingType
         Returns the ship type  
            
         
        """
        pass
    
    ## Getter for property: (@link DDAMExcitation.ResponseType NXOpen.CAE.ResponseSimulation.DDAMExcitation.ResponseType@endlink) ResponseType
    ##  Returns the DDAM response type  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return DDAMExcitation.ResponseType
    @property
    def ResponseType(self) -> DDAMExcitation.ResponseType:
        """
        Getter for property: (@link DDAMExcitation.ResponseType NXOpen.CAE.ResponseSimulation.DDAMExcitation.ResponseType@endlink) ResponseType
         Returns the DDAM response type  
            
         
        """
        pass
    
    ## Setter for property: (@link DDAMExcitation.ResponseType NXOpen.CAE.ResponseSimulation.DDAMExcitation.ResponseType@endlink) ResponseType

    ##  Returns the DDAM response type  
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @ResponseType.setter
    def ResponseType(self, response_type: DDAMExcitation.ResponseType):
        """
        Setter for property: (@link DDAMExcitation.ResponseType NXOpen.CAE.ResponseSimulation.DDAMExcitation.ResponseType@endlink) ResponseType
         Returns the DDAM response type  
            
         
        """
        pass
    
    ## Getter for property: (@link DDAMExcitation.ShipType NXOpen.CAE.ResponseSimulation.DDAMExcitation.ShipType@endlink) ShipType
    ##  Returns the ship type  
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return DDAMExcitation.ShipType
    @property
    def ShipType(self) -> DDAMExcitation.ShipType:
        """
        Getter for property: (@link DDAMExcitation.ShipType NXOpen.CAE.ResponseSimulation.DDAMExcitation.ShipType@endlink) ShipType
         Returns the ship type  
            
         
        """
        pass
    
    ## Setter for property: (@link DDAMExcitation.ShipType NXOpen.CAE.ResponseSimulation.DDAMExcitation.ShipType@endlink) ShipType

    ##  Returns the ship type  
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ShipType.setter
    def ShipType(self, ship_type: DDAMExcitation.ShipType):
        """
        Setter for property: (@link DDAMExcitation.ShipType NXOpen.CAE.ResponseSimulation.DDAMExcitation.ShipType@endlink) ShipType
         Returns the ship type  
            
         
        """
        pass
    
    ## Getter for property: (@link RSEvent.SpacingType NXOpen.CAE.ResponseSimulation.RSEvent.SpacingType@endlink) Spacing
    ##  Returns the spacing type  
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return RSEvent.SpacingType
    @property
    def Spacing(self) -> RSEvent.SpacingType:
        """
        Getter for property: (@link RSEvent.SpacingType NXOpen.CAE.ResponseSimulation.RSEvent.SpacingType@endlink) Spacing
         Returns the spacing type  
            
         
        """
        pass
    
    ## Setter for property: (@link RSEvent.SpacingType NXOpen.CAE.ResponseSimulation.RSEvent.SpacingType@endlink) Spacing

    ##  Returns the spacing type  
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Spacing.setter
    def Spacing(self, spacing: RSEvent.SpacingType):
        """
        Setter for property: (@link RSEvent.SpacingType NXOpen.CAE.ResponseSimulation.RSEvent.SpacingType@endlink) Spacing
         Returns the spacing type  
            
         
        """
        pass
    
    ## Getter for property: (int) SpectralLines
    ##  Returns the spectral lines setting.  
    ##    Only available when event type is
    ##         @link CAE::ResponseSimulation::RSEvent::TypeFrequency CAE::ResponseSimulation::RSEvent::TypeFrequency@endlink ,
    ##         @link CAE::ResponseSimulation::RSEvent::TypeRandom CAE::ResponseSimulation::RSEvent::TypeRandom@endlink ,
    ##         @link CAE::ResponseSimulation::RSEvent::TypeResponseSpectrum CAE::ResponseSimulation::RSEvent::TypeResponseSpectrum@endlink ,
    ##           
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def SpectralLines(self) -> int:
        """
        Getter for property: (int) SpectralLines
         Returns the spectral lines setting.  
           Only available when event type is
                @link CAE::ResponseSimulation::RSEvent::TypeFrequency CAE::ResponseSimulation::RSEvent::TypeFrequency@endlink ,
                @link CAE::ResponseSimulation::RSEvent::TypeRandom CAE::ResponseSimulation::RSEvent::TypeRandom@endlink ,
                @link CAE::ResponseSimulation::RSEvent::TypeResponseSpectrum CAE::ResponseSimulation::RSEvent::TypeResponseSpectrum@endlink ,
                  
         
        """
        pass
    
    ## Setter for property: (int) SpectralLines

    ##  Returns the spectral lines setting.  
    ##    Only available when event type is
    ##         @link CAE::ResponseSimulation::RSEvent::TypeFrequency CAE::ResponseSimulation::RSEvent::TypeFrequency@endlink ,
    ##         @link CAE::ResponseSimulation::RSEvent::TypeRandom CAE::ResponseSimulation::RSEvent::TypeRandom@endlink ,
    ##         @link CAE::ResponseSimulation::RSEvent::TypeResponseSpectrum CAE::ResponseSimulation::RSEvent::TypeResponseSpectrum@endlink ,
    ##           
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @SpectralLines.setter
    def SpectralLines(self, spectral_lines: int):
        """
        Setter for property: (int) SpectralLines
         Returns the spectral lines setting.  
           Only available when event type is
                @link CAE::ResponseSimulation::RSEvent::TypeFrequency CAE::ResponseSimulation::RSEvent::TypeFrequency@endlink ,
                @link CAE::ResponseSimulation::RSEvent::TypeRandom CAE::ResponseSimulation::RSEvent::TypeRandom@endlink ,
                @link CAE::ResponseSimulation::RSEvent::TypeResponseSpectrum CAE::ResponseSimulation::RSEvent::TypeResponseSpectrum@endlink ,
                  
         
        """
        pass
    
##  Represents the manager of CAE.ResponseSimulation.RSEvent. 
##     The object of type @link NXOpen::CAE::ResponseSimulation::RSEvent NXOpen::CAE::ResponseSimulation::RSEvent@endlink  can be 
##     created or deleted only through this class.  <br> To create a new instance of this class, use @link NXOpen::CAE::ResponseSimulation::RSEventCollection::CreateEventBuilder  NXOpen::CAE::ResponseSimulation::RSEventCollection::CreateEventBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class RSEventBuilder(BaseBuilder): 
    """ Represents the manager of CAE.ResponseSimulation.RSEvent. 
    The object of type <ja_class>NXOpen.CAE.ResponseSimulation.RSEvent</ja_class> can be 
    created or deleted only through this class. """


    ## Getter for property: (@link RSEventAttributes NXOpen.CAE.ResponseSimulation.RSEventAttributes@endlink) Attributes
    ##  Returns the attributes setting   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return RSEventAttributes
    @property
    def Attributes(self) -> RSEventAttributes:
        """
        Getter for property: (@link RSEventAttributes NXOpen.CAE.ResponseSimulation.RSEventAttributes@endlink) Attributes
         Returns the attributes setting   
            
         
        """
        pass
    
    ## Getter for property: (@link RSEventParameters NXOpen.CAE.ResponseSimulation.RSEventParameters@endlink) EventParameters
    ##  Returns the random base excitation event parameters   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return RSEventParameters
    @property
    def EventParameters(self) -> RSEventParameters:
        """
        Getter for property: (@link RSEventParameters NXOpen.CAE.ResponseSimulation.RSEventParameters@endlink) EventParameters
         Returns the random base excitation event parameters   
            
         
        """
        pass
    
    ## Getter for property: (@link RSEvent.Type NXOpen.CAE.ResponseSimulation.RSEvent.Type@endlink) EventType
    ##  Returns the event type   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return RSEvent.Type
    @property
    def EventType(self) -> RSEvent.Type:
        """
        Getter for property: (@link RSEvent.Type NXOpen.CAE.ResponseSimulation.RSEvent.Type@endlink) EventType
         Returns the event type   
            
         
        """
        pass
    
    ## Setter for property: (@link RSEvent.Type NXOpen.CAE.ResponseSimulation.RSEvent.Type@endlink) EventType

    ##  Returns the event type   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @EventType.setter
    def EventType(self, event_type: RSEvent.Type):
        """
        Setter for property: (@link RSEvent.Type NXOpen.CAE.ResponseSimulation.RSEvent.Type@endlink) EventType
         Returns the event type   
            
         
        """
        pass
    
    ## Getter for property: (@link InitialConditions NXOpen.CAE.ResponseSimulation.InitialConditions@endlink) InitialConditions
    ##  Returns the initial condition setting.  
    ##    Only available when event type is 
    ##         @link NXOpen::CAE::ResponseSimulation::RSEvent::TypeTransient NXOpen::CAE::ResponseSimulation::RSEvent::TypeTransient@endlink    
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return InitialConditions
    @property
    def InitialConditions(self) -> InitialConditions:
        """
        Getter for property: (@link InitialConditions NXOpen.CAE.ResponseSimulation.InitialConditions@endlink) InitialConditions
         Returns the initial condition setting.  
           Only available when event type is 
                @link NXOpen::CAE::ResponseSimulation::RSEvent::TypeTransient NXOpen::CAE::ResponseSimulation::RSEvent::TypeTransient@endlink    
         
        """
        pass
    
    ## Getter for property: (@link RSEventOutputSetting NXOpen.CAE.ResponseSimulation.RSEventOutputSetting@endlink) OutputSetting
    ##  Returns the output setting   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return RSEventOutputSetting
    @property
    def OutputSetting(self) -> RSEventOutputSetting:
        """
        Getter for property: (@link RSEventOutputSetting NXOpen.CAE.ResponseSimulation.RSEventOutputSetting@endlink) OutputSetting
         Returns the output setting   
            
         
        """
        pass
    
    ## Getter for property: (@link Solution NXOpen.CAE.ResponseSimulation.Solution@endlink) ResponseSimulationSolution
    ##  Returns the parent response simulation solution   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return Solution
    @property
    def ResponseSimulationSolution(self) -> Solution:
        """
        Getter for property: (@link Solution NXOpen.CAE.ResponseSimulation.Solution@endlink) ResponseSimulationSolution
         Returns the parent response simulation solution   
            
         
        """
        pass
    
import NXOpen
##  Represents a collection of response analysis event  <br> To obtain an instance of this class, refer to @link NXOpen::CAE::ResponseSimulation::Manager  NXOpen::CAE::ResponseSimulation::Manager @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class RSEventCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of response analysis event """


    ##  Creates a event buider 
    ##  @return builder (@link RSEventBuilder NXOpen.CAE.ResponseSimulation.RSEventBuilder@endlink):   .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="ra_event"> (@link RSEvent NXOpen.CAE.ResponseSimulation.RSEvent@endlink)   </param>
    def CreateEventBuilder(self, ra_event: RSEvent) -> RSEventBuilder:
        """
         Creates a event buider 
         @return builder (@link RSEventBuilder NXOpen.CAE.ResponseSimulation.RSEventBuilder@endlink):   .
        """
        pass
    
    ##  Deletes an event 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="ra_event"> (@link RSEvent NXOpen.CAE.ResponseSimulation.RSEvent@endlink)   </param>
    def DeleteEvent(self, ra_event: RSEvent) -> None:
        """
         Deletes an event 
        """
        pass
    
    ##  Finds an event with specified event name 
    ##  @return ra_event (@link RSEvent NXOpen.CAE.ResponseSimulation.RSEvent@endlink):   .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="name"> (str)   </param>
    def FindObject(self, name: str) -> RSEvent:
        """
         Finds an event with specified event name 
         @return ra_event (@link RSEvent NXOpen.CAE.ResponseSimulation.RSEvent@endlink):   .
        """
        pass
    
import NXOpen
##  Reprensents the output setting for an event 
## 
##   <br>  Created in NX5.0.0  <br> 

class RSEventOutputSetting(NXOpen.TaggedObject): 
    """ Reprensents the output setting for an event """


    ## Getter for property: (bool) FemGeometrySaveOption
    ##  Returns the option to save FEM information with evaluation results.  
    ##    The option could not be
    ##         changed after the event is created.   
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def FemGeometrySaveOption(self) -> bool:
        """
        Getter for property: (bool) FemGeometrySaveOption
         Returns the option to save FEM information with evaluation results.  
           The option could not be
                changed after the event is created.   
         
        """
        pass
    
    ## Setter for property: (bool) FemGeometrySaveOption

    ##  Returns the option to save FEM information with evaluation results.  
    ##    The option could not be
    ##         changed after the event is created.   
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

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
##  Reprensents the parameters of the random base excitation event 
## 
##   <br>  Created in NX1953.0.0  <br> 

class RSEventParameters(NXOpen.TaggedObject): 
    """ Reprensents the parameters of the random base excitation event """


    ## Getter for property: (@link RSEvent.InterpolationMethod NXOpen.CAE.ResponseSimulation.RSEvent.InterpolationMethod@endlink) AmplitudeInterpMethod
    ##  Returns the Amplitude interpolation method   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return RSEvent.InterpolationMethod
    @property
    def AmplitudeInterpMethod(self) -> RSEvent.InterpolationMethod:
        """
        Getter for property: (@link RSEvent.InterpolationMethod NXOpen.CAE.ResponseSimulation.RSEvent.InterpolationMethod@endlink) AmplitudeInterpMethod
         Returns the Amplitude interpolation method   
            
         
        """
        pass
    
    ## Setter for property: (@link RSEvent.InterpolationMethod NXOpen.CAE.ResponseSimulation.RSEvent.InterpolationMethod@endlink) AmplitudeInterpMethod

    ##  Returns the Amplitude interpolation method   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @AmplitudeInterpMethod.setter
    def AmplitudeInterpMethod(self, amplitude_interpolation_method: RSEvent.InterpolationMethod):
        """
        Setter for property: (@link RSEvent.InterpolationMethod NXOpen.CAE.ResponseSimulation.RSEvent.InterpolationMethod@endlink) AmplitudeInterpMethod
         Returns the Amplitude interpolation method   
            
         
        """
        pass
    
    ## Getter for property: (float) ConfidenceLevel
    ##  Returns the confidence level value   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def ConfidenceLevel(self) -> float:
        """
        Getter for property: (float) ConfidenceLevel
         Returns the confidence level value   
            
         
        """
        pass
    
    ## Setter for property: (float) ConfidenceLevel

    ##  Returns the confidence level value   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ConfidenceLevel.setter
    def ConfidenceLevel(self, confidence_level: float):
        """
        Setter for property: (float) ConfidenceLevel
         Returns the confidence level value   
            
         
        """
        pass
    
    ## Getter for property: (@link RSEvent.ConfidenceLevelOption NXOpen.CAE.ResponseSimulation.RSEvent.ConfidenceLevelOption@endlink) ConfidenceLevelOption
    ##  Returns the confidence level option   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return RSEvent.ConfidenceLevelOption
    @property
    def ConfidenceLevelOption(self) -> RSEvent.ConfidenceLevelOption:
        """
        Getter for property: (@link RSEvent.ConfidenceLevelOption NXOpen.CAE.ResponseSimulation.RSEvent.ConfidenceLevelOption@endlink) ConfidenceLevelOption
         Returns the confidence level option   
            
         
        """
        pass
    
    ## Setter for property: (@link RSEvent.ConfidenceLevelOption NXOpen.CAE.ResponseSimulation.RSEvent.ConfidenceLevelOption@endlink) ConfidenceLevelOption

    ##  Returns the confidence level option   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ConfidenceLevelOption.setter
    def ConfidenceLevelOption(self, confidence_level_option: RSEvent.ConfidenceLevelOption):
        """
        Setter for property: (@link RSEvent.ConfidenceLevelOption NXOpen.CAE.ResponseSimulation.RSEvent.ConfidenceLevelOption@endlink) ConfidenceLevelOption
         Returns the confidence level option   
            
         
        """
        pass
    
    ## Getter for property: (@link RSEvent.InterpolationMethod NXOpen.CAE.ResponseSimulation.RSEvent.InterpolationMethod@endlink) FrequencyInterpMethod
    ##  Returns the Frequency interpolation method   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return RSEvent.InterpolationMethod
    @property
    def FrequencyInterpMethod(self) -> RSEvent.InterpolationMethod:
        """
        Getter for property: (@link RSEvent.InterpolationMethod NXOpen.CAE.ResponseSimulation.RSEvent.InterpolationMethod@endlink) FrequencyInterpMethod
         Returns the Frequency interpolation method   
            
         
        """
        pass
    
    ## Setter for property: (@link RSEvent.InterpolationMethod NXOpen.CAE.ResponseSimulation.RSEvent.InterpolationMethod@endlink) FrequencyInterpMethod

    ##  Returns the Frequency interpolation method   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @FrequencyInterpMethod.setter
    def FrequencyInterpMethod(self, frequency_interpolation_method: RSEvent.InterpolationMethod):
        """
        Setter for property: (@link RSEvent.InterpolationMethod NXOpen.CAE.ResponseSimulation.RSEvent.InterpolationMethod@endlink) FrequencyInterpMethod
         Returns the Frequency interpolation method   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.ModelingObjectPropertyTable NXOpen.CAE.ModelingObjectPropertyTable@endlink) FrequencyOutputRequestObject
    ##  Returns the Frequency output request modeling object   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.CAE.ModelingObjectPropertyTable
    @property
    def FrequencyOutputRequestObject(self) -> NXOpen.CAE.ModelingObjectPropertyTable:
        """
        Getter for property: (@link NXOpen.CAE.ModelingObjectPropertyTable NXOpen.CAE.ModelingObjectPropertyTable@endlink) FrequencyOutputRequestObject
         Returns the Frequency output request modeling object   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.ModelingObjectPropertyTable NXOpen.CAE.ModelingObjectPropertyTable@endlink) FrequencyOutputRequestObject

    ##  Returns the Frequency output request modeling object   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @FrequencyOutputRequestObject.setter
    def FrequencyOutputRequestObject(self, ssmo: NXOpen.CAE.ModelingObjectPropertyTable):
        """
        Setter for property: (@link NXOpen.CAE.ModelingObjectPropertyTable NXOpen.CAE.ModelingObjectPropertyTable@endlink) FrequencyOutputRequestObject
         Returns the Frequency output request modeling object   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.ModelingObjectPropertyTable NXOpen.CAE.ModelingObjectPropertyTable@endlink) OutputRequestObject
    ##  Returns the output request modeling object   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1980.0.0.  Use @link NXOpen::CAE::ResponseSimulation::RSEventParameters::RandomOutputRequestObject NXOpen::CAE::ResponseSimulation::RSEventParameters::RandomOutputRequestObject@endlink  instead.  <br> 

    ## @return NXOpen.CAE.ModelingObjectPropertyTable
    @property
    def OutputRequestObject(self) -> NXOpen.CAE.ModelingObjectPropertyTable:
        """
        Getter for property: (@link NXOpen.CAE.ModelingObjectPropertyTable NXOpen.CAE.ModelingObjectPropertyTable@endlink) OutputRequestObject
         Returns the output request modeling object   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.ModelingObjectPropertyTable NXOpen.CAE.ModelingObjectPropertyTable@endlink) OutputRequestObject

    ##  Returns the output request modeling object   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1980.0.0.  Use @link NXOpen::CAE::ResponseSimulation::RSEventParameters::RandomOutputRequestObject NXOpen::CAE::ResponseSimulation::RSEventParameters::RandomOutputRequestObject@endlink  instead.  <br> 

    @OutputRequestObject.setter
    def OutputRequestObject(self, ssmo: NXOpen.CAE.ModelingObjectPropertyTable):
        """
        Setter for property: (@link NXOpen.CAE.ModelingObjectPropertyTable NXOpen.CAE.ModelingObjectPropertyTable@endlink) OutputRequestObject
         Returns the output request modeling object   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.ModelingObjectPropertyTable NXOpen.CAE.ModelingObjectPropertyTable@endlink) RandomOutputRequestObject
    ##  Returns the Random output request modeling object   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.CAE.ModelingObjectPropertyTable
    @property
    def RandomOutputRequestObject(self) -> NXOpen.CAE.ModelingObjectPropertyTable:
        """
        Getter for property: (@link NXOpen.CAE.ModelingObjectPropertyTable NXOpen.CAE.ModelingObjectPropertyTable@endlink) RandomOutputRequestObject
         Returns the Random output request modeling object   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.ModelingObjectPropertyTable NXOpen.CAE.ModelingObjectPropertyTable@endlink) RandomOutputRequestObject

    ##  Returns the Random output request modeling object   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RandomOutputRequestObject.setter
    def RandomOutputRequestObject(self, ssmo: NXOpen.CAE.ModelingObjectPropertyTable):
        """
        Setter for property: (@link NXOpen.CAE.ModelingObjectPropertyTable NXOpen.CAE.ModelingObjectPropertyTable@endlink) RandomOutputRequestObject
         Returns the Random output request modeling object   
            
         
        """
        pass
    
    ## Getter for property: (@link RSEvent.ReferenceType NXOpen.CAE.ResponseSimulation.RSEvent.ReferenceType@endlink) ReferenceType
    ##  Returns the confidence level option   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return RSEvent.ReferenceType
    @property
    def ReferenceType(self) -> RSEvent.ReferenceType:
        """
        Getter for property: (@link RSEvent.ReferenceType NXOpen.CAE.ResponseSimulation.RSEvent.ReferenceType@endlink) ReferenceType
         Returns the confidence level option   
            
         
        """
        pass
    
    ## Setter for property: (@link RSEvent.ReferenceType NXOpen.CAE.ResponseSimulation.RSEvent.ReferenceType@endlink) ReferenceType

    ##  Returns the confidence level option   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ReferenceType.setter
    def ReferenceType(self, reference_type: RSEvent.ReferenceType):
        """
        Setter for property: (@link RSEvent.ReferenceType NXOpen.CAE.ResponseSimulation.RSEvent.ReferenceType@endlink) ReferenceType
         Returns the confidence level option   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.ModelingObjectPropertyTable NXOpen.CAE.ModelingObjectPropertyTable@endlink) SineOutputRequestObject
    ##  Returns the Sine output request modeling object   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.CAE.ModelingObjectPropertyTable
    @property
    def SineOutputRequestObject(self) -> NXOpen.CAE.ModelingObjectPropertyTable:
        """
        Getter for property: (@link NXOpen.CAE.ModelingObjectPropertyTable NXOpen.CAE.ModelingObjectPropertyTable@endlink) SineOutputRequestObject
         Returns the Sine output request modeling object   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.ModelingObjectPropertyTable NXOpen.CAE.ModelingObjectPropertyTable@endlink) SineOutputRequestObject

    ##  Returns the Sine output request modeling object   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @SineOutputRequestObject.setter
    def SineOutputRequestObject(self, ssmo: NXOpen.CAE.ModelingObjectPropertyTable):
        """
        Setter for property: (@link NXOpen.CAE.ModelingObjectPropertyTable NXOpen.CAE.ModelingObjectPropertyTable@endlink) SineOutputRequestObject
         Returns the Sine output request modeling object   
            
         
        """
        pass
    
    ## Getter for property: (float) StandardDeviation
    ##  Returns the standard deviation value   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def StandardDeviation(self) -> float:
        """
        Getter for property: (float) StandardDeviation
         Returns the standard deviation value   
            
         
        """
        pass
    
    ## Setter for property: (float) StandardDeviation

    ##  Returns the standard deviation value   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @StandardDeviation.setter
    def StandardDeviation(self, standard_deviation: float):
        """
        Setter for property: (float) StandardDeviation
         Returns the standard deviation value   
            
         
        """
        pass
    
    ## Getter for property: (bool) StaticContributions
    ##  Returns the residual vector static contribution   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def StaticContributions(self) -> bool:
        """
        Getter for property: (bool) StaticContributions
         Returns the residual vector static contribution   
            
         
        """
        pass
    
    ## Setter for property: (bool) StaticContributions

    ##  Returns the residual vector static contribution   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @StaticContributions.setter
    def StaticContributions(self, static_ontributions: bool):
        """
        Setter for property: (bool) StaticContributions
         Returns the residual vector static contribution   
            
         
        """
        pass
    
import NXOpen
##  Represents a response analysis event 
## 
##   <br>  Created in NX5.0.0  <br> 

class RSEventSolverParameters(NXOpen.TaggedObject): 
    """ Represents a response analysis event """


    ##  Represents DDAM coefficient type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Af</term><description> 
    ##  </description> </item><item><term> 
    ## Vf</term><description> 
    ##  </description> </item><item><term> 
    ## Aa</term><description> 
    ##  </description> </item><item><term> 
    ## Ab</term><description> 
    ##  </description> </item><item><term> 
    ## Ac</term><description> 
    ##  </description> </item><item><term> 
    ## Ad</term><description> 
    ##  </description> </item><item><term> 
    ## Va</term><description> 
    ##  </description> </item><item><term> 
    ## Vb</term><description> 
    ##  </description> </item><item><term> 
    ## Vc</term><description> 
    ##  </description> </item></list>
    class DdamCoefficientType(Enum):
        """
        Members Include: <Af> <Vf> <Aa> <Ab> <Ac> <Ad> <Va> <Vb> <Vc>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RSEventSolverParameters.DdamCoefficientType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) DdamCoefficientA
    ##  Returns the DDAM A coefficient   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def DdamCoefficientA(self) -> float:
        """
        Getter for property: (float) DdamCoefficientA
         Returns the DDAM A coefficient   
            
         
        """
        pass
    
    ## Setter for property: (float) DdamCoefficientA

    ##  Returns the DDAM A coefficient   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @DdamCoefficientA.setter
    def DdamCoefficientA(self, coefficientA: float):
        """
        Setter for property: (float) DdamCoefficientA
         Returns the DDAM A coefficient   
            
         
        """
        pass
    
    ## Getter for property: (float) DdamCoefficientV
    ##  Returns the DDAM V coefficient   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def DdamCoefficientV(self) -> float:
        """
        Getter for property: (float) DdamCoefficientV
         Returns the DDAM V coefficient   
            
         
        """
        pass
    
    ## Setter for property: (float) DdamCoefficientV

    ##  Returns the DDAM V coefficient   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @DdamCoefficientV.setter
    def DdamCoefficientV(self, coefficientV: float):
        """
        Setter for property: (float) DdamCoefficientV
         Returns the DDAM V coefficient   
            
         
        """
        pass
    
    ##  Returns DDAM coefficient value of the specified type 
    ##  @return coefficient (float): .
    ## 
    ##   <br>  Created in NX7.5.2  <br> 

    ## License requirements: None.
    ## 
    ## <param name="coefficientType"> (@link RSEventSolverParameters.DdamCoefficientType NXOpen.CAE.ResponseSimulation.RSEventSolverParameters.DdamCoefficientType@endlink) </param>
    def GetDdamCoefficient(self, coefficientType: RSEventSolverParameters.DdamCoefficientType) -> float:
        """
         Returns DDAM coefficient value of the specified type 
         @return coefficient (float): .
        """
        pass
    
    ##  Sets the DDAM coefficient value of the specified type 
    ## 
    ##   <br>  Created in NX7.5.2  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="coefficientType"> (@link RSEventSolverParameters.DdamCoefficientType NXOpen.CAE.ResponseSimulation.RSEventSolverParameters.DdamCoefficientType@endlink) </param>
    ## <param name="coefficient"> (float) </param>
    def SetDdamCoefficient(self, coefficientType: RSEventSolverParameters.DdamCoefficientType, coefficient: float) -> None:
        """
         Sets the DDAM coefficient value of the specified type 
        """
        pass
    
import NXOpen
##  Represents a response analysis event  <br> To create or edit an instance of this class, use @link NXOpen::CAE::ResponseSimulation::RSEventBuilder  NXOpen::CAE::ResponseSimulation::RSEventBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class RSEvent(NXOpen.NXObject): 
    """ Represents a response analysis event """


    ##  the analysis type of response analysis event. Only available for
    ##        @link NXOpen::CAE::ResponseSimulation::RSEvent::TypeTransient NXOpen::CAE::ResponseSimulation::RSEvent::TypeTransient@endlink  and 
    ##        @link NXOpen::CAE::ResponseSimulation::RSEvent::TypeFrequency NXOpen::CAE::ResponseSimulation::RSEvent::TypeFrequency@endlink  
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ModeAcceleration</term><description> 
    ##   </description> </item><item><term> 
    ## ModeDisplacement</term><description> 
    ##   </description> </item></list>
    class AnalysisType(Enum):
        """
        Members Include: <ModeAcceleration> <ModeDisplacement>
        """
        ModeAcceleration: int
        ModeDisplacement: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RSEvent.AnalysisType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the confidence level option 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## UserDefined</term><description> 
    ## </description> </item><item><term> 
    ## StandardDeviations</term><description> 
    ## </description> </item><item><term> 
    ## Rms</term><description> 
    ## </description> </item></list>
    class ConfidenceLevelOption(Enum):
        """
        Members Include: <UserDefined> <StandardDeviations> <Rms>
        """
        UserDefined: int
        StandardDeviations: int
        Rms: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RSEvent.ConfidenceLevelOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the fromulation type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Standard</term><description> 
    ## </description> </item><item><term> 
    ## UserDefined</term><description> 
    ## </description> </item></list>
    class DdamFormulationType(Enum):
        """
        Members Include: <Standard> <UserDefined>
        """
        Standard: int
        UserDefined: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RSEvent.DdamFormulationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the duration option 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ExcitationFunction</term><description> 
    ##  </description> </item><item><term> 
    ## UserDefined</term><description> 
    ## </description> </item></list>
    class DurationOption(Enum):
        """
        Members Include: <ExcitationFunction> <UserDefined>
        """
        ExcitationFunction: int
        UserDefined: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RSEvent.DurationOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the interpolation method option 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Log</term><description> 
    ## </description> </item><item><term> 
    ## Linear</term><description> 
    ## </description> </item></list>
    class InterpolationMethod(Enum):
        """
        Members Include: <Log> <Linear>
        """
        Log: int
        Linear: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RSEvent.InterpolationMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the reference type option 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Relative</term><description> 
    ## </description> </item><item><term> 
    ## Absolute</term><description> 
    ## </description> </item></list>
    class ReferenceType(Enum):
        """
        Members Include: <Relative> <Absolute>
        """
        Relative: int
        Absolute: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RSEvent.ReferenceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the result file type of event. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ModalResponse</term><description> 
    ##  Result file to be used as Restart File, which extension is ".eef" or ".sef" </description> </item><item><term> 
    ## FunctionResponse</term><description> 
    ##  Result file to contain function response evaluation results, which extenstion is ".afu" </description> </item><item><term> 
    ## DynamicResponse</term><description> 
    ##  Result file to contain dynamic response evaluation results, which extension is ".rs2" </description> </item><item><term> 
    ## ContourFunctionResponse</term><description> 
    ##  Result file to contain the contour and function results, which extension is ".op2 and .bun" </description> </item></list>
    class ResultFileType(Enum):
        """
        Members Include: <ModalResponse> <FunctionResponse> <DynamicResponse> <ContourFunctionResponse>
        """
        ModalResponse: int
        FunctionResponse: int
        DynamicResponse: int
        ContourFunctionResponse: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RSEvent.ResultFileType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the spacing type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Even</term><description> 
    ##   </description> </item><item><term> 
    ## Uneven</term><description> 
    ##   </description> </item></list>
    class SpacingType(Enum):
        """
        Members Include: <Even> <Uneven>
        """
        Even: int
        Uneven: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RSEvent.SpacingType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the type of reponse analysis event 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Transient</term><description> 
    ##   </description> </item><item><term> 
    ## Frequency</term><description> 
    ##   </description> </item><item><term> 
    ## Random</term><description> 
    ##   </description> </item><item><term> 
    ## ResponseSpectrum</term><description> 
    ##   </description> </item><item><term> 
    ## Ddam</term><description> 
    ##   </description> </item><item><term> 
    ## Static</term><description> 
    ##   </description> </item><item><term> 
    ## RandomBaseExcitation</term><description> 
    ##   </description> </item><item><term> 
    ## SineBaseExcitation</term><description> 
    ##   </description> </item></list>
    class Type(Enum):
        """
        Members Include: <Transient> <Frequency> <Random> <ResponseSpectrum> <Ddam> <Static> <RandomBaseExcitation> <SineBaseExcitation>
        """
        Transient: int
        Frequency: int
        Random: int
        ResponseSpectrum: int
        Ddam: int
        Static: int
        RandomBaseExcitation: int
        SineBaseExcitation: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RSEvent.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Solve the Randome Base Excitation and the Sine Base Excitation events. The results is stored in an op2 file, which file name
    ##         could be returned by @link NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName@endlink  
    ##  @return pid (int):  Process id of the event solver run .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="runInBackground"> (bool)  Run the solver in the background. </param>
    def BaseExcitationEventSolve(self, runInBackground: bool) -> int:
        """
         Solve the Randome Base Excitation and the Sine Base Excitation events. The results is stored in an op2 file, which file name
                could be returned by @link NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName@endlink  
         @return pid (int):  Process id of the event solver run .
        """
        pass
    
    ##  Write the batch file with the full command to run the solver from the command line for the Random Base Excitation and the Sine Base Excitation events. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def BaseExcitationEventWriteBatchFile(self) -> None:
        """
         Write the batch file with the full command to run the solver from the command line for the Random Base Excitation and the Sine Base Excitation events. 
        """
        pass
    
    ##  Write the solver input xml file of the Random Base Excitation and the Sine Base Excitation events. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def BaseExcitationEventWriteInputFile(self) -> None:
        """
         Write the solver input xml file of the Random Base Excitation and the Sine Base Excitation events. 
        """
        pass
    
    ##  Check the obsolete status of the event. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def CheckObsoleteStatus(self) -> None:
        """
         Check the obsolete status of the event. 
        """
        pass
    
    ##  Deletes all result files of the event. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="result_file_type"> (@link RSEvent.ResultFileType NXOpen.CAE.ResponseSimulation.RSEvent.ResultFileType@endlink)  </param>
    def DeleteResultFiles(self, result_file_type: RSEvent.ResultFileType) -> None:
        """
         Deletes all result files of the event. 
        """
        pass
    
    ##  Deletes a response simulation dynamic event, including all excitations
    ##             under it 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="deleteResultFile"> (bool)  delete the result files associated with the solution or not </param>
    def Destroy(self, deleteResultFile: bool) -> None:
        """
         Deletes a response simulation dynamic event, including all excitations
                    under it 
        """
        pass
    
    ##  Performs evaluation for CSD. The evaluation results will be stored in an AFU file, 
    ##         which name could be returned by @link NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName@endlink  
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="evaluation_setting"> (@link CsdEvaluationSetting NXOpen.CAE.ResponseSimulation.CsdEvaluationSetting@endlink)  </param>
    def EvaluateCsd(self, evaluation_setting: CsdEvaluationSetting) -> None:
        """
         Performs evaluation for CSD. The evaluation results will be stored in an AFU file, 
                which name could be returned by @link NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName@endlink  
        """
        pass
    
    ##  Performs evaluation for elemental function response. The results is stored in an AFU file, which file name
    ##         could be returned by @link NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName@endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="evaluation_setting"> (@link ElementalFunctionEvaluationSetting NXOpen.CAE.ResponseSimulation.ElementalFunctionEvaluationSetting@endlink)  </param>
    def EvaluateElementalFunctionResponse(self, evaluation_setting: ElementalFunctionEvaluationSetting) -> None:
        """
         Performs evaluation for elemental function response. The results is stored in an AFU file, which file name
                could be returned by @link NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName@endlink  
        """
        pass
    
    ##  Performs evaluation for LCR results. The results is stored in an RS2 file, which file name
    ##         could be returned by @link NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName@endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="evaluation_setting"> (@link LcrResultsEvaluationSetting NXOpen.CAE.ResponseSimulation.LcrResultsEvaluationSetting@endlink)  </param>
    def EvaluateLcrResults(self, evaluation_setting: LcrResultsEvaluationSetting) -> None:
        """
         Performs evaluation for LCR results. The results is stored in an RS2 file, which file name
                could be returned by @link NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName@endlink  
        """
        pass
    
    ##  Performs evaluation for modal function response. The results is stored in an AFU file, which file name
    ##         could be returned by @link NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName@endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def EvaluateModalFunctionResponse(self) -> None:
        """
         Performs evaluation for modal function response. The results is stored in an AFU file, which file name
                could be returned by @link NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName@endlink  
        """
        pass
    
    ##  Performs evaluation for modal response. The results is getting eef file, which file name
    ##         could be returned by @link NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName@endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def EvaluateModalResponse(self) -> None:
        """
         Performs evaluation for modal response. The results is getting eef file, which file name
                could be returned by @link NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName@endlink  
        """
        pass
    
    ##  Performs evaluation for nodal function response. The results is stored in an AFU file, which file name
    ##         could be returned by @link NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName@endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="evaluation_setting"> (@link NodalFunctionEvaluationSetting NXOpen.CAE.ResponseSimulation.NodalFunctionEvaluationSetting@endlink)  </param>
    def EvaluateNodalFunctionResponse(self, evaluation_setting: NodalFunctionEvaluationSetting) -> None:
        """
         Performs evaluation for nodal function response. The results is stored in an AFU file, which file name
                could be returned by @link NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName@endlink  
        """
        pass
    
    ##  Performs evaluation for peak value results. The results is stored in an RS2 file, which file name
    ##         could be returned by @link NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName@endlink .  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="evaluation_setting"> (@link PeakValueEvaluationSetting NXOpen.CAE.ResponseSimulation.PeakValueEvaluationSetting@endlink)  </param>
    def EvaluatePeakValueResults(self, evaluation_setting: PeakValueEvaluationSetting) -> None:
        """
         Performs evaluation for peak value results. The results is stored in an RS2 file, which file name
                could be returned by @link NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName@endlink .  
        """
        pass
    
    ##  Performs evaluation for response results. The results is stored in an RS2 file, which file name
    ##         could be returned by @link NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName@endlink .  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="evaluation_setting"> (@link ResponseResultsEvaluationSetting NXOpen.CAE.ResponseSimulation.ResponseResultsEvaluationSetting@endlink)  </param>
    def EvaluateResponseResults(self, evaluation_setting: ResponseResultsEvaluationSetting) -> None:
        """
         Performs evaluation for response results. The results is stored in an RS2 file, which file name
                could be returned by @link NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName@endlink .  
        """
        pass
    
    ##  Perfroms evaluation for RMS results. The results is stored in an RS2 file, which file name
    ##         could be returned by @link NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName@endlink . 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="evaluation_setting"> (@link RmsResultsEvaluationSetting NXOpen.CAE.ResponseSimulation.RmsResultsEvaluationSetting@endlink)  </param>
    def EvaluateRmsResults(self, evaluation_setting: RmsResultsEvaluationSetting) -> None:
        """
         Perfroms evaluation for RMS results. The results is stored in an RS2 file, which file name
                could be returned by @link NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName@endlink . 
        """
        pass
    
    ##  Performs evaluation for sensor response. The results is stored in an AFU file, which file name
    ##         could be returned by @link NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName@endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## <param name="ra_event"> (@link RSEvent NXOpen.CAE.ResponseSimulation.RSEvent@endlink) </param>
    @overload
    def EvaluateSensorResponse(self) -> None:
        """
         Performs evaluation for sensor response. The results is stored in an AFU file, which file name
                could be returned by @link NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName@endlink  
        """
        pass
    
    ##  Performs evaluation for sensor response. The results is stored in an AFU file, which file name
    ##         could be returned by @link NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName@endlink  
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## <param name="ra_event"> (@link RSEvent NXOpen.CAE.ResponseSimulation.RSEvent@endlink) </param>
    ## <param name="evaluation_setting"> (@link SensorEvaluationSetting NXOpen.CAE.ResponseSimulation.SensorEvaluationSetting@endlink)  </param>
    @overload
    def EvaluateSensorResponse(self, evaluation_setting: SensorEvaluationSetting) -> None:
        """
         Performs evaluation for sensor response. The results is stored in an AFU file, which file name
                could be returned by @link NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName@endlink  
        """
        pass
    
    ##  Performs evaluation for strain gage response. The results is stored in an AFU file, which file name
    ##         could be returned by @link NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName@endlink  
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="evaluation_setting"> (@link StrainGageEvaluationSetting NXOpen.CAE.ResponseSimulation.StrainGageEvaluationSetting@endlink)  </param>
    def EvaluateStrainGageResponse(self, evaluation_setting: StrainGageEvaluationSetting) -> None:
        """
         Performs evaluation for strain gage response. The results is stored in an AFU file, which file name
                could be returned by @link NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName@endlink  
        """
        pass
    
    ##  Performs evaluation for strength results. The results is stored in an RS2 file, which file name
    ##         could be returned by @link NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName@endlink .  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="evaluation_setting"> (@link StrengthResultsEvaluationSetting NXOpen.CAE.ResponseSimulation.StrengthResultsEvaluationSetting@endlink)  </param>
    def EvaluateStrengthResults(self, evaluation_setting: StrengthResultsEvaluationSetting) -> None:
        """
         Performs evaluation for strength results. The results is stored in an RS2 file, which file name
                could be returned by @link NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName@endlink .  
        """
        pass
    
    ##  Exports event definition to a XML file 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="event_definition_file"> (str)  </param>
    def Export(self, event_definition_file: str) -> None:
        """
         Exports event definition to a XML file 
        """
        pass
    
    ##  Returns the option setting for calculating static offset result.
    ##         The staic offset calculation is only available to transient event 
    ##  @return calculateStaticOffset (bool):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetCalculateStaticOffset(self) -> bool:
        """
         Returns the option setting for calculating static offset result.
                The staic offset calculation is only available to transient event 
         @return calculateStaticOffset (bool):  .
        """
        pass
    
    ##  Returns the event name 
    ##  @return eventName (str):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetEventName(self) -> str:
        """
         Returns the event name 
         @return eventName (str):  .
        """
        pass
    
    ##  Returns all excitations of an event 
    ##  @return excitations (@link Excitation List[NXOpen.CAE.ResponseSimulation.Excitation]@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetExcitations(self) -> List[Excitation]:
        """
         Returns all excitations of an event 
         @return excitations (@link Excitation List[NXOpen.CAE.ResponseSimulation.Excitation]@endlink):  .
        """
        pass
    
    ##  Returns result file name of specified type 
    ##  @return result_file_name (str):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="result_file_type"> (@link RSEvent.ResultFileType NXOpen.CAE.ResponseSimulation.RSEvent.ResultFileType@endlink)  </param>
    def GetResultFileName(self, result_file_type: RSEvent.ResultFileType) -> str:
        """
         Returns result file name of specified type 
         @return result_file_name (str):  .
        """
        pass
    
    ##  Returns the solver parameters 
    ##  @return solver_parameters (@link RSEventSolverParameters NXOpen.CAE.ResponseSimulation.RSEventSolverParameters@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetSolverParameters(self) -> RSEventSolverParameters:
        """
         Returns the solver parameters 
         @return solver_parameters (@link RSEventSolverParameters NXOpen.CAE.ResponseSimulation.RSEventSolverParameters@endlink):  .
        """
        pass
    
    ##  Loads function results of the event. 
    ##  @return unitsMismatch (bool):  flag indicating if the output file unit system is valid .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def LoadFunctionResults(self) -> bool:
        """
         Loads function results of the event. 
         @return unitsMismatch (bool):  flag indicating if the output file unit system is valid .
        """
        pass
    
    ##  Solve the Random Base Excitation Event. The results is stored in an op2 file, which file name
    ##         could be returned by @link NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName@endlink  
    ##  @return pid (int):  Process id of the event solver run .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="runInBackground"> (bool)  Run the solver in the background. </param>
    def RbeEventSolve(self, runInBackground: bool) -> int:
        """
         Solve the Random Base Excitation Event. The results is stored in an op2 file, which file name
                could be returned by @link NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName NXOpen::CAE::ResponseSimulation::RSEvent::GetResultFileName@endlink  
         @return pid (int):  Process id of the event solver run .
        """
        pass
    
    ##  Write the batch file with the full command to run the solver from the command line. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def RbeEventWriteBatchFile(self) -> None:
        """
         Write the batch file with the full command to run the solver from the command line. 
        """
        pass
    
    ##  Write the solver input xml file of the Random Base Excitation Event. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def RbeEventWriteInputFile(self) -> None:
        """
         Write the solver input xml file of the Random Base Excitation Event. 
        """
        pass
    
    ##  Set the option setting for calculating static offset result. The static offset calculation is
    ##         only available to transient event 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="calculateStaticOffset"> (bool)  </param>
    def SetCalculateStaticOffset(self, calculateStaticOffset: bool) -> None:
        """
         Set the option setting for calculating static offset result. The static offset calculation is
                only available to transient event 
        """
        pass
    
    ##  Sets the event name 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="eventName"> (str)  </param>
    ## <param name="renameResultFile"> (bool)  if there are result files associated with the event, rename them or not</param>
    def SetEventName(self, eventName: str, renameResultFile: bool) -> None:
        """
         Sets the event name 
        """
        pass
    
import NXOpen
import NXOpen.CAE
##  Represents a @link NXOpen::CAE::ResponseSimulation::SensorBuilder NXOpen::CAE::ResponseSimulation::SensorBuilder@endlink 
##       <br> To create a new instance of this class, use @link NXOpen::CAE::ResponseSimulation::SensorCollection::CreateSensorBuilder  NXOpen::CAE::ResponseSimulation::SensorCollection::CreateSensorBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class SensorBuilder(BaseBuilder): 
    """ Represents a <ja_class>NXOpen.CAE.ResponseSimulation.SensorBuilder</ja_class>
     """


    ## Getter for property: (bool) ReverseNormalDirection
    ##  Returns the option for reverse the normal direction.  
    ##    
    ##             Only available when the sensor type is
    ##             @link CAE::ResponseSimulation::SensorTypeNormal CAE::ResponseSimulation::SensorTypeNormal@endlink     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def ReverseNormalDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseNormalDirection
         Returns the option for reverse the normal direction.  
           
                    Only available when the sensor type is
                    @link CAE::ResponseSimulation::SensorTypeNormal CAE::ResponseSimulation::SensorTypeNormal@endlink     
         
        """
        pass
    
    ## Setter for property: (bool) ReverseNormalDirection

    ##  Returns the option for reverse the normal direction.  
    ##    
    ##             Only available when the sensor type is
    ##             @link CAE::ResponseSimulation::SensorTypeNormal CAE::ResponseSimulation::SensorTypeNormal@endlink     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @ReverseNormalDirection.setter
    def ReverseNormalDirection(self, normal_direction: bool):
        """
        Setter for property: (bool) ReverseNormalDirection
         Returns the option for reverse the normal direction.  
           
                    Only available when the sensor type is
                    @link CAE::ResponseSimulation::SensorTypeNormal CAE::ResponseSimulation::SensorTypeNormal@endlink     
         
        """
        pass
    
    ## Getter for property: (@link SensorCoordinateType NXOpen.CAE.ResponseSimulation.SensorCoordinateType@endlink) SensorCoordinateType
    ##  Returns the sensor's coordinate type   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return SensorCoordinateType
    @property
    def SensorCoordinateType(self) -> SensorCoordinateType:
        """
        Getter for property: (@link SensorCoordinateType NXOpen.CAE.ResponseSimulation.SensorCoordinateType@endlink) SensorCoordinateType
         Returns the sensor's coordinate type   
            
         
        """
        pass
    
    ## Setter for property: (@link SensorCoordinateType NXOpen.CAE.ResponseSimulation.SensorCoordinateType@endlink) SensorCoordinateType

    ##  Returns the sensor's coordinate type   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @SensorCoordinateType.setter
    def SensorCoordinateType(self, coordinate_type: SensorCoordinateType):
        """
        Setter for property: (@link SensorCoordinateType NXOpen.CAE.ResponseSimulation.SensorCoordinateType@endlink) SensorCoordinateType
         Returns the sensor's coordinate type   
            
         
        """
        pass
    
    ## Getter for property: (bool) SensorDirectionX
    ##  Returns the setting for x direction compontent of sensor.  
    ##    
    ##             If true, the response on direction x will be calculated.
    ##             Only available when the sensor type is
    ##             @link CAE::ResponseSimulation::SensorTypeComponent CAE::ResponseSimulation::SensorTypeComponent@endlink     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def SensorDirectionX(self) -> bool:
        """
        Getter for property: (bool) SensorDirectionX
         Returns the setting for x direction compontent of sensor.  
           
                    If true, the response on direction x will be calculated.
                    Only available when the sensor type is
                    @link CAE::ResponseSimulation::SensorTypeComponent CAE::ResponseSimulation::SensorTypeComponent@endlink     
         
        """
        pass
    
    ## Setter for property: (bool) SensorDirectionX

    ##  Returns the setting for x direction compontent of sensor.  
    ##    
    ##             If true, the response on direction x will be calculated.
    ##             Only available when the sensor type is
    ##             @link CAE::ResponseSimulation::SensorTypeComponent CAE::ResponseSimulation::SensorTypeComponent@endlink     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @SensorDirectionX.setter
    def SensorDirectionX(self, direction_x: bool):
        """
        Setter for property: (bool) SensorDirectionX
         Returns the setting for x direction compontent of sensor.  
           
                    If true, the response on direction x will be calculated.
                    Only available when the sensor type is
                    @link CAE::ResponseSimulation::SensorTypeComponent CAE::ResponseSimulation::SensorTypeComponent@endlink     
         
        """
        pass
    
    ## Getter for property: (bool) SensorDirectionY
    ##  Returns the setting for y direction compontent of sensor.  
    ##    
    ##             If true, the response on direction y will be calculated.
    ##             Only available when the sensor type is
    ##             @link CAE::ResponseSimulation::SensorTypeComponent CAE::ResponseSimulation::SensorTypeComponent@endlink     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def SensorDirectionY(self) -> bool:
        """
        Getter for property: (bool) SensorDirectionY
         Returns the setting for y direction compontent of sensor.  
           
                    If true, the response on direction y will be calculated.
                    Only available when the sensor type is
                    @link CAE::ResponseSimulation::SensorTypeComponent CAE::ResponseSimulation::SensorTypeComponent@endlink     
         
        """
        pass
    
    ## Setter for property: (bool) SensorDirectionY

    ##  Returns the setting for y direction compontent of sensor.  
    ##    
    ##             If true, the response on direction y will be calculated.
    ##             Only available when the sensor type is
    ##             @link CAE::ResponseSimulation::SensorTypeComponent CAE::ResponseSimulation::SensorTypeComponent@endlink     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @SensorDirectionY.setter
    def SensorDirectionY(self, direction_y: bool):
        """
        Setter for property: (bool) SensorDirectionY
         Returns the setting for y direction compontent of sensor.  
           
                    If true, the response on direction y will be calculated.
                    Only available when the sensor type is
                    @link CAE::ResponseSimulation::SensorTypeComponent CAE::ResponseSimulation::SensorTypeComponent@endlink     
         
        """
        pass
    
    ## Getter for property: (bool) SensorDirectionZ
    ##  Returns the setting for z direction compontent of sensor.  
    ##    
    ##             If true, the response on direction z will be calculated.
    ##             Only available when the sensor type is
    ##             @link CAE::ResponseSimulation::SensorTypeComponent CAE::ResponseSimulation::SensorTypeComponent@endlink     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def SensorDirectionZ(self) -> bool:
        """
        Getter for property: (bool) SensorDirectionZ
         Returns the setting for z direction compontent of sensor.  
           
                    If true, the response on direction z will be calculated.
                    Only available when the sensor type is
                    @link CAE::ResponseSimulation::SensorTypeComponent CAE::ResponseSimulation::SensorTypeComponent@endlink     
         
        """
        pass
    
    ## Setter for property: (bool) SensorDirectionZ

    ##  Returns the setting for z direction compontent of sensor.  
    ##    
    ##             If true, the response on direction z will be calculated.
    ##             Only available when the sensor type is
    ##             @link CAE::ResponseSimulation::SensorTypeComponent CAE::ResponseSimulation::SensorTypeComponent@endlink     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @SensorDirectionZ.setter
    def SensorDirectionZ(self, direction_z: bool):
        """
        Setter for property: (bool) SensorDirectionZ
         Returns the setting for z direction compontent of sensor.  
           
                    If true, the response on direction z will be calculated.
                    Only available when the sensor type is
                    @link CAE::ResponseSimulation::SensorTypeComponent CAE::ResponseSimulation::SensorTypeComponent@endlink     
         
        """
        pass
    
    ## Getter for property: (@link SensorResultType NXOpen.CAE.ResponseSimulation.SensorResultType@endlink) SensorResultType
    ##  Returns the sensor's result type   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return SensorResultType
    @property
    def SensorResultType(self) -> SensorResultType:
        """
        Getter for property: (@link SensorResultType NXOpen.CAE.ResponseSimulation.SensorResultType@endlink) SensorResultType
         Returns the sensor's result type   
            
         
        """
        pass
    
    ## Setter for property: (@link SensorResultType NXOpen.CAE.ResponseSimulation.SensorResultType@endlink) SensorResultType

    ##  Returns the sensor's result type   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @SensorResultType.setter
    def SensorResultType(self, result_type: SensorResultType):
        """
        Setter for property: (@link SensorResultType NXOpen.CAE.ResponseSimulation.SensorResultType@endlink) SensorResultType
         Returns the sensor's result type   
            
         
        """
        pass
    
    ## Getter for property: (bool) SensorRotationX
    ##  Returns the setting for x rotation compontent of sensor.  
    ##    
    ##             If true, the response on rotation x will be calculated.
    ##             Only available when the sensor type is
    ##             @link CAE::ResponseSimulation::SensorTypeComponent CAE::ResponseSimulation::SensorTypeComponent@endlink     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def SensorRotationX(self) -> bool:
        """
        Getter for property: (bool) SensorRotationX
         Returns the setting for x rotation compontent of sensor.  
           
                    If true, the response on rotation x will be calculated.
                    Only available when the sensor type is
                    @link CAE::ResponseSimulation::SensorTypeComponent CAE::ResponseSimulation::SensorTypeComponent@endlink     
         
        """
        pass
    
    ## Setter for property: (bool) SensorRotationX

    ##  Returns the setting for x rotation compontent of sensor.  
    ##    
    ##             If true, the response on rotation x will be calculated.
    ##             Only available when the sensor type is
    ##             @link CAE::ResponseSimulation::SensorTypeComponent CAE::ResponseSimulation::SensorTypeComponent@endlink     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @SensorRotationX.setter
    def SensorRotationX(self, rotation_x: bool):
        """
        Setter for property: (bool) SensorRotationX
         Returns the setting for x rotation compontent of sensor.  
           
                    If true, the response on rotation x will be calculated.
                    Only available when the sensor type is
                    @link CAE::ResponseSimulation::SensorTypeComponent CAE::ResponseSimulation::SensorTypeComponent@endlink     
         
        """
        pass
    
    ## Getter for property: (bool) SensorRotationY
    ##  Returns the setting for y rotation compontent of sensor.  
    ##    
    ##             If true, the response on rotation y will be calculated.
    ##             Only available when the sensor type is
    ##             @link CAE::ResponseSimulation::SensorTypeComponent CAE::ResponseSimulation::SensorTypeComponent@endlink     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def SensorRotationY(self) -> bool:
        """
        Getter for property: (bool) SensorRotationY
         Returns the setting for y rotation compontent of sensor.  
           
                    If true, the response on rotation y will be calculated.
                    Only available when the sensor type is
                    @link CAE::ResponseSimulation::SensorTypeComponent CAE::ResponseSimulation::SensorTypeComponent@endlink     
         
        """
        pass
    
    ## Setter for property: (bool) SensorRotationY

    ##  Returns the setting for y rotation compontent of sensor.  
    ##    
    ##             If true, the response on rotation y will be calculated.
    ##             Only available when the sensor type is
    ##             @link CAE::ResponseSimulation::SensorTypeComponent CAE::ResponseSimulation::SensorTypeComponent@endlink     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @SensorRotationY.setter
    def SensorRotationY(self, rotation_y: bool):
        """
        Setter for property: (bool) SensorRotationY
         Returns the setting for y rotation compontent of sensor.  
           
                    If true, the response on rotation y will be calculated.
                    Only available when the sensor type is
                    @link CAE::ResponseSimulation::SensorTypeComponent CAE::ResponseSimulation::SensorTypeComponent@endlink     
         
        """
        pass
    
    ## Getter for property: (bool) SensorRotationZ
    ##  Returns the setting for z rotation compontent of sensor.  
    ##    
    ##             If true, the response on rotation z will be calculated.
    ##             Only available when the sensor type is
    ##             @link CAE::ResponseSimulation::SensorTypeComponent CAE::ResponseSimulation::SensorTypeComponent@endlink     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def SensorRotationZ(self) -> bool:
        """
        Getter for property: (bool) SensorRotationZ
         Returns the setting for z rotation compontent of sensor.  
           
                    If true, the response on rotation z will be calculated.
                    Only available when the sensor type is
                    @link CAE::ResponseSimulation::SensorTypeComponent CAE::ResponseSimulation::SensorTypeComponent@endlink     
         
        """
        pass
    
    ## Setter for property: (bool) SensorRotationZ

    ##  Returns the setting for z rotation compontent of sensor.  
    ##    
    ##             If true, the response on rotation z will be calculated.
    ##             Only available when the sensor type is
    ##             @link CAE::ResponseSimulation::SensorTypeComponent CAE::ResponseSimulation::SensorTypeComponent@endlink     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @SensorRotationZ.setter
    def SensorRotationZ(self, rotation_z: bool):
        """
        Setter for property: (bool) SensorRotationZ
         Returns the setting for z rotation compontent of sensor.  
           
                    If true, the response on rotation z will be calculated.
                    Only available when the sensor type is
                    @link CAE::ResponseSimulation::SensorTypeComponent CAE::ResponseSimulation::SensorTypeComponent@endlink     
         
        """
        pass
    
    ## Getter for property: (@link SensorType NXOpen.CAE.ResponseSimulation.SensorType@endlink) SensorType
    ##  Returns the sensor's type   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return SensorType
    @property
    def SensorType(self) -> SensorType:
        """
        Getter for property: (@link SensorType NXOpen.CAE.ResponseSimulation.SensorType@endlink) SensorType
         Returns the sensor's type   
            
         
        """
        pass
    
    ## Setter for property: (@link SensorType NXOpen.CAE.ResponseSimulation.SensorType@endlink) SensorType

    ##  Returns the sensor's type   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @SensorType.setter
    def SensorType(self, sensor_type: SensorType):
        """
        Setter for property: (@link SensorType NXOpen.CAE.ResponseSimulation.SensorType@endlink) SensorType
         Returns the sensor's type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SensorVector
    ##  Returns the user defined direction.  
    ##   
    ##             Only available when the sensor type is
    ##             @link CAE::ResponseSimulation::SensorTypeDirection CAE::ResponseSimulation::SensorTypeDirection@endlink    
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def SensorVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SensorVector
         Returns the user defined direction.  
          
                    Only available when the sensor type is
                    @link CAE::ResponseSimulation::SensorTypeDirection CAE::ResponseSimulation::SensorTypeDirection@endlink    
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SensorVector

    ##  Returns the user defined direction.  
    ##   
    ##             Only available when the sensor type is
    ##             @link CAE::ResponseSimulation::SensorTypeDirection CAE::ResponseSimulation::SensorTypeDirection@endlink    
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @SensorVector.setter
    def SensorVector(self, sensor_vector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SensorVector
         Returns the user defined direction.  
          
                    Only available when the sensor type is
                    @link CAE::ResponseSimulation::SensorTypeDirection CAE::ResponseSimulation::SensorTypeDirection@endlink    
         
        """
        pass
    
    ##  Returns the destination nodes 
    ##  @return destination_nodes (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetSelectedNodes(self) -> List[NXOpen.CAE.FENode]:
        """
         Returns the destination nodes 
         @return destination_nodes (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink):  .
        """
        pass
    
    ##  Sets the destination nodes 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="destination_nodes"> (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink)  </param>
    def SetSelectedNodes(self, destination_nodes: List[NXOpen.CAE.FENode]) -> None:
        """
         Sets the destination nodes 
        """
        pass
    
import NXOpen
##  Represents a collection of response analysis sensor  <br> To obtain an instance of this class, refer to @link NXOpen::CAE::ResponseSimulation::Manager  NXOpen::CAE::ResponseSimulation::Manager @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class SensorCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of response analysis sensor """


    ##  Creates a sensor buider 
    ##  @return builder (@link SensorBuilder NXOpen.CAE.ResponseSimulation.SensorBuilder@endlink):   .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="rs_sensor"> (@link Sensor NXOpen.CAE.ResponseSimulation.Sensor@endlink)   </param>
    def CreateSensorBuilder(self, rs_sensor: Sensor) -> SensorBuilder:
        """
         Creates a sensor buider 
         @return builder (@link SensorBuilder NXOpen.CAE.ResponseSimulation.SensorBuilder@endlink):   .
        """
        pass
    
    ##  Deletes an sensor 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="rs_sensor"> (@link Sensor NXOpen.CAE.ResponseSimulation.Sensor@endlink)   </param>
    def DeleteSensor(self, rs_sensor: Sensor) -> None:
        """
         Deletes an sensor 
        """
        pass
    
    ##  Finds an sensor with specified event name 
    ##  @return sensor (@link Sensor NXOpen.CAE.ResponseSimulation.Sensor@endlink):   .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="name"> (str)   </param>
    def FindObject(self, name: str) -> Sensor:
        """
         Finds an sensor with specified event name 
         @return sensor (@link Sensor NXOpen.CAE.ResponseSimulation.Sensor@endlink):   .
        """
        pass
    
##  Specifies the coordinate type of Sensor 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## NodalCs</term><description> 
##  </description> </item><item><term> 
## GlobalCs</term><description> 
##  </description> </item></list>
class SensorCoordinateType(Enum):
    """
    Members Include: <NodalCs> <GlobalCs>
    """
    NodalCs: int
    GlobalCs: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> SensorCoordinateType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##  This is a manager to the @link NXOpen::CAE::ResponseSimulation::SensorEvaluationSetting NXOpen::CAE::ResponseSimulation::SensorEvaluationSetting@endlink  class. 
##         Object of type @link NXOpen::CAE::ResponseSimulation::SensorEvaluationSetting NXOpen::CAE::ResponseSimulation::SensorEvaluationSetting@endlink  can be 
##         created and edited only through this class
##           <br> To create a new instance of this class, use @link NXOpen::CAE::ResponseSimulation::EvaluationSettingManager::CreateSensorEvaluationSettingBuilder  NXOpen::CAE::ResponseSimulation::EvaluationSettingManager::CreateSensorEvaluationSettingBuilder @endlink  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class SensorEvaluationSettingBuilder(FunctionEvaluationSettingBuilder): 
    """ This is a manager to the <ja_class>NXOpen.CAE.ResponseSimulation.SensorEvaluationSetting</ja_class> class. 
        Object of type <ja_class>NXOpen.CAE.ResponseSimulation.SensorEvaluationSetting</ja_class> can be 
        created and edited only through this class
         """


    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Sensor
    ##  Returns the destination sensor   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def Sensor(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Sensor
         Returns the destination sensor   
            
         
        """
        pass
    
##  Represents the parameters setting for sensor evaluation.  For more information, see the 
##     Response Dynamics section of the Gateway Help  <br> To create or edit an instance of this class, use @link NXOpen::CAE::ResponseSimulation::SensorEvaluationSettingBuilder  NXOpen::CAE::ResponseSimulation::SensorEvaluationSettingBuilder @endlink  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class SensorEvaluationSetting(DynamicResultEvaluationSetting): 
    """ Represents the parameters setting for sensor evaluation.  For more information, see the 
    Response Dynamics section of the Gateway Help """
    pass


##  Specifies the result type of Sensor 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Displacement</term><description> 
##  </description> </item><item><term> 
## Velocity</term><description> 
##  </description> </item><item><term> 
## Acceleration</term><description> 
##  </description> </item><item><term> 
## ReactionForce</term><description> 
##  </description> </item></list>
class SensorResultType(Enum):
    """
    Members Include: <Displacement> <Velocity> <Acceleration> <ReactionForce>
    """
    Displacement: int
    Velocity: int
    Acceleration: int
    ReactionForce: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> SensorResultType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Specifies the type of Sensor 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Component</term><description> 
##  </description> </item><item><term> 
## Direction</term><description> 
##  </description> </item><item><term> 
## Normal</term><description> 
##  </description> </item></list>
class SensorType(Enum):
    """
    Members Include: <Component> <Direction> <Normal>
    """
    Component: int
    Direction: int
    Normal: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> SensorType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##  Represents a @link NXOpen::CAE::ResponseSimulation::Sensor NXOpen::CAE::ResponseSimulation::Sensor@endlink 
##       <br> To create or edit an instance of this class, use @link NXOpen::CAE::ResponseSimulation::SensorBuilder  NXOpen::CAE::ResponseSimulation::SensorBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class Sensor(NXOpen.DisplayableObject): 
    """ Represents a <ja_class>NXOpen.CAE.ResponseSimulation.Sensor</ja_class>
     """


    ##  Get display attribute of sensor 
    ##  @return display_attr (@link RSDisplayObject NXOpen.CAE.ResponseSimulation.RSDisplayObject@endlink):   .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetDisplayAttribute(self) -> RSDisplayObject:
        """
         Get display attribute of sensor 
         @return display_attr (@link RSDisplayObject NXOpen.CAE.ResponseSimulation.RSDisplayObject@endlink):   .
        """
        pass
    
##  Specifies shell element evaluation locations 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Top</term><description> 
##  </description> </item><item><term> 
## Middle</term><description> 
##  </description> </item><item><term> 
## Bottom</term><description> 
##  </description> </item></list>
class ShellElementEvaluationLocation(Enum):
    """
    Members Include: <Top> <Middle> <Bottom>
    """
    Top: int
    Middle: int
    Bottom: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> ShellElementEvaluationLocation:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##  Represents attributes setting of response analysis meta solution 
## 
##   <br>  Created in NX6.0.0  <br> 

class SolutionAttributes(NXOpen.TaggedObject): 
    """ Represents attributes setting of response analysis meta solution """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RigidBodyToleranceExp
    ##  Returns the tolerance expression   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RigidBodyToleranceExp(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RigidBodyToleranceExp
         Returns the tolerance expression   
            
         
        """
        pass
    
import NXOpen.CAE
##  This is a manager to the @link NXOpen::CAE::ResponseSimulation::Solution NXOpen::CAE::ResponseSimulation::Solution@endlink  class. 
##     Object of type @link NXOpen::CAE::ResponseSimulation::Solution NXOpen::CAE::ResponseSimulation::Solution@endlink  can be 
##     created and edited only through this class
##       <br> To create a new instance of this class, use @link NXOpen::CAE::ResponseSimulation::SolutionCollection::CreateSolutionBuilder  NXOpen::CAE::ResponseSimulation::SolutionCollection::CreateSolutionBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class SolutionBuilder(BaseBuilder): 
    """ This is a manager to the <ja_class>NXOpen.CAE.ResponseSimulation.Solution</ja_class> class. 
    Object of type <ja_class>NXOpen.CAE.ResponseSimulation.Solution</ja_class> can be 
    created and edited only through this class
     """


    ## Getter for property: (@link SolutionAttributes NXOpen.CAE.ResponseSimulation.SolutionAttributes@endlink) Attributes
    ##  Returns the attributes setting   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return SolutionAttributes
    @property
    def Attributes(self) -> SolutionAttributes:
        """
        Getter for property: (@link SolutionAttributes NXOpen.CAE.ResponseSimulation.SolutionAttributes@endlink) Attributes
         Returns the attributes setting   
            
         
        """
        pass
    
    ## Getter for property: (str) ImportedEefFile
    ##  Returns the EEF file imported to create an imported response analysis meta solution.  
    ##    There is 
    ##             event definition containing in the EEF file. An event will be created with the solution.
    ##             To the imported solution and event, the users can only perform evaluation and not able to
    ##             create new events and excitations
    ##            
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return str
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
    
    ## Setter for property: (str) ImportedEefFile

    ##  Returns the EEF file imported to create an imported response analysis meta solution.  
    ##    There is 
    ##             event definition containing in the EEF file. An event will be created with the solution.
    ##             To the imported solution and event, the users can only perform evaluation and not able to
    ##             create new events and excitations
    ##            
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

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
    
    ## Getter for property: (@link NXOpen.CAE.SimSolution NXOpen.CAE.SimSolution@endlink) ReferencedSolution
    ##  Returns the referenced solution which must be a SEMODES *103 solution with modal results solved   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return NXOpen.CAE.SimSolution
    @property
    def ReferencedSolution(self) -> NXOpen.CAE.SimSolution:
        """
        Getter for property: (@link NXOpen.CAE.SimSolution NXOpen.CAE.SimSolution@endlink) ReferencedSolution
         Returns the referenced solution which must be a SEMODES *103 solution with modal results solved   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.SimSolution NXOpen.CAE.SimSolution@endlink) ReferencedSolution

    ##  Returns the referenced solution which must be a SEMODES *103 solution with modal results solved   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ReferencedSolution.setter
    def ReferencedSolution(self, referenced_solution: NXOpen.CAE.SimSolution):
        """
        Setter for property: (@link NXOpen.CAE.SimSolution NXOpen.CAE.SimSolution@endlink) ReferencedSolution
         Returns the referenced solution which must be a SEMODES *103 solution with modal results solved   
            
         
        """
        pass
    
    ## Getter for property: (str) ScratchDir
    ##  Returns the scratch file is used for Response Dynamics Evaluations.  
    ##    
    ##             The OP2,RS2,EEF file are processed in this area and copied to the original location as needed.
    ##            
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def ScratchDir(self) -> str:
        """
        Getter for property: (str) ScratchDir
         Returns the scratch file is used for Response Dynamics Evaluations.  
           
                    The OP2,RS2,EEF file are processed in this area and copied to the original location as needed.
                   
         
        """
        pass
    
    ## Setter for property: (str) ScratchDir

    ##  Returns the scratch file is used for Response Dynamics Evaluations.  
    ##    
    ##             The OP2,RS2,EEF file are processed in this area and copied to the original location as needed.
    ##            
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ScratchDir.setter
    def ScratchDir(self, scratch_dir: str):
        """
        Setter for property: (str) ScratchDir
         Returns the scratch file is used for Response Dynamics Evaluations.  
           
                    The OP2,RS2,EEF file are processed in this area and copied to the original location as needed.
                   
         
        """
        pass
    
    ## Getter for property: (bool) UseNastranResultDir
    ##  Returns the nastran result directory is used for Response Dynamics Evaluations if this toggle is ON
    ##            
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def UseNastranResultDir(self) -> bool:
        """
        Getter for property: (bool) UseNastranResultDir
         Returns the nastran result directory is used for Response Dynamics Evaluations if this toggle is ON
                   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseNastranResultDir

    ##  Returns the nastran result directory is used for Response Dynamics Evaluations if this toggle is ON
    ##            
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @UseNastranResultDir.setter
    def UseNastranResultDir(self, use_nastran_result_dir: bool):
        """
        Setter for property: (bool) UseNastranResultDir
         Returns the nastran result directory is used for Response Dynamics Evaluations if this toggle is ON
                   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseScratchDir
    ##  Returns the scratch file is used for Response Dynamics Evaluations.  
    ##    
    ##             This option turns the usage of the scratch directory on or off.
    ##            
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def UseScratchDir(self) -> bool:
        """
        Getter for property: (bool) UseScratchDir
         Returns the scratch file is used for Response Dynamics Evaluations.  
           
                    This option turns the usage of the scratch directory on or off.
                   
         
        """
        pass
    
    ## Setter for property: (bool) UseScratchDir

    ##  Returns the scratch file is used for Response Dynamics Evaluations.  
    ##    
    ##             This option turns the usage of the scratch directory on or off.
    ##            
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseScratchDir.setter
    def UseScratchDir(self, use_scratch_dir: bool):
        """
        Setter for property: (bool) UseScratchDir
         Returns the scratch file is used for Response Dynamics Evaluations.  
           
                    This option turns the usage of the scratch directory on or off.
                   
         
        """
        pass
    
import NXOpen
##  Represents a collection of response analysis meta solution  <br> To obtain an instance of this class, refer to @link NXOpen::CAE::ResponseSimulation::Manager  NXOpen::CAE::ResponseSimulation::Manager @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class SolutionCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of response analysis meta solution """


    ## Getter for property: (@link Solution NXOpen.CAE.ResponseSimulation.Solution@endlink) ActiveSolution
    ##  Returns the active solution   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return Solution
    @property
    def ActiveSolution(self) -> Solution:
        """
        Getter for property: (@link Solution NXOpen.CAE.ResponseSimulation.Solution@endlink) ActiveSolution
         Returns the active solution   
            
         
        """
        pass
    
    ## Setter for property: (@link Solution NXOpen.CAE.ResponseSimulation.Solution@endlink) ActiveSolution

    ##  Returns the active solution   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ActiveSolution.setter
    def ActiveSolution(self, active_solution: Solution):
        """
        Setter for property: (@link Solution NXOpen.CAE.ResponseSimulation.Solution@endlink) ActiveSolution
         Returns the active solution   
            
         
        """
        pass
    
    ##  Clones a response analysis meta solution 
    ##  @return new_solution (@link Solution NXOpen.CAE.ResponseSimulation.Solution@endlink):  the  newly created @link CAE::ResponseSimulation::Solution CAE::ResponseSimulation::Solution@endlink   .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="old_solution"> (@link Solution NXOpen.CAE.ResponseSimulation.Solution@endlink)  the @link CAE::SimSolution CAE::SimSolution@endlink  to be cloned </param>
    ## <param name="suggested_name"> (str)  name to use instead of default name (may be NULL) </param>
    def CloneSolution(self, old_solution: Solution, suggested_name: str) -> Solution:
        """
         Clones a response analysis meta solution 
         @return new_solution (@link Solution NXOpen.CAE.ResponseSimulation.Solution@endlink):  the  newly created @link CAE::ResponseSimulation::Solution CAE::ResponseSimulation::Solution@endlink   .
        """
        pass
    
    ##  Creates the builder object of response analysis meta solution 
    ##  @return ra_solution_builder (@link SolutionBuilder NXOpen.CAE.ResponseSimulation.SolutionBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="ra_solution"> (@link Solution NXOpen.CAE.ResponseSimulation.Solution@endlink)  </param>
    def CreateSolutionBuilder(self, ra_solution: Solution) -> SolutionBuilder:
        """
         Creates the builder object of response analysis meta solution 
         @return ra_solution_builder (@link SolutionBuilder NXOpen.CAE.ResponseSimulation.SolutionBuilder@endlink):  .
        """
        pass
    
    ##  Finds a response analysis meta solution with specified solution name 
    ##  @return found (@link Solution NXOpen.CAE.ResponseSimulation.Solution@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="solution_name"> (str)   </param>
    def FindObject(self, solution_name: str) -> Solution:
        """
         Finds a response analysis meta solution with specified solution name 
         @return found (@link Solution NXOpen.CAE.ResponseSimulation.Solution@endlink):  .
        """
        pass
    
import NXOpen
##  Represents a meta solution providing response analysis functionalities in the .sim file   <br> To create or edit an instance of this class, use @link NXOpen::CAE::ResponseSimulation::SolutionBuilder  NXOpen::CAE::ResponseSimulation::SolutionBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class Solution(NXOpen.NXObject): 
    """ Represents a meta solution providing response analysis functionalities in the .sim file  """


    ## Getter for property: (@link RSEvent NXOpen.CAE.ResponseSimulation.RSEvent@endlink) ActiveEvent
    ##  Returns the active event   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return RSEvent
    @property
    def ActiveEvent(self) -> RSEvent:
        """
        Getter for property: (@link RSEvent NXOpen.CAE.ResponseSimulation.RSEvent@endlink) ActiveEvent
         Returns the active event   
            
         
        """
        pass
    
    ## Setter for property: (@link RSEvent NXOpen.CAE.ResponseSimulation.RSEvent@endlink) ActiveEvent

    ##  Returns the active event   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ActiveEvent.setter
    def ActiveEvent(self, active_event: RSEvent):
        """
        Setter for property: (@link RSEvent NXOpen.CAE.ResponseSimulation.RSEvent@endlink) ActiveEvent
         Returns the active event   
            
         
        """
        pass
    
    ##  Checks status and updates solution properties for the solution which became obsolete because
    ##             referenced modal shape file was changed. The solution will be reactivated as normal state after status checking. 
    ## 
    ##   <br>  Created in NX8.0.1  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def CheckObsoleteStatus(self) -> None:
        """
         Checks status and updates solution properties for the solution which became obsolete because
                    referenced modal shape file was changed. The solution will be reactivated as normal state after status checking. 
        """
        pass
    
    ##  Clones an event to the solution 
    ##  @return new_event (@link RSEvent NXOpen.CAE.ResponseSimulation.RSEvent@endlink):   .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="source_event"> (@link RSEvent NXOpen.CAE.ResponseSimulation.RSEvent@endlink)  </param>
    ## <param name="suggested_name"> (str)  </param>
    def CloneEvent(self, source_event: RSEvent, suggested_name: str) -> RSEvent:
        """
         Clones an event to the solution 
         @return new_event (@link RSEvent NXOpen.CAE.ResponseSimulation.RSEvent@endlink):   .
        """
        pass
    
    ##  Clones a sensor to the solution 
    ##  @return new_sensor (@link Sensor NXOpen.CAE.ResponseSimulation.Sensor@endlink):   .
    ## 
    ##   <br>  Created in NX5.0.1  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="source_sensor"> (@link Sensor NXOpen.CAE.ResponseSimulation.Sensor@endlink)  </param>
    ## <param name="suggested_name"> (str)  </param>
    def CloneSensor(self, source_sensor: Sensor, suggested_name: str) -> Sensor:
        """
         Clones a sensor to the solution 
         @return new_sensor (@link Sensor NXOpen.CAE.ResponseSimulation.Sensor@endlink):   .
        """
        pass
    
    ##  Clones a strain gage to the solution 
    ##  @return new_gage (@link StrainGage NXOpen.CAE.ResponseSimulation.StrainGage@endlink):   .
    ## 
    ##   <br>  Created in NX5.0.1  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="source_gage"> (@link StrainGage NXOpen.CAE.ResponseSimulation.StrainGage@endlink)  </param>
    ## <param name="suggested_name"> (str)  </param>
    def CloneStrainGage(self, source_gage: StrainGage, suggested_name: str) -> StrainGage:
        """
         Clones a strain gage to the solution 
         @return new_gage (@link StrainGage NXOpen.CAE.ResponseSimulation.StrainGage@endlink):   .
        """
        pass
    
    ##  Deletes a response simulation solution, including all events and excitations
    ##             under it 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="deleteResultFile"> (bool)  delete the result files associated with the solution or not </param>
    def Destroy(self, deleteResultFile: bool) -> None:
        """
         Deletes a response simulation solution, including all events and excitations
                    under it 
        """
        pass
    
    ##  Performs evaluation for FRF. The evaluation results will be stored in an AFU file,
    ##         which name could be returned by @link NXOpen::CAE::ResponseSimulation::Solution::GetResultFileName NXOpen::CAE::ResponseSimulation::Solution::GetResultFileName@endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="evaluation_setting"> (@link FrfEvaluationSetting NXOpen.CAE.ResponseSimulation.FrfEvaluationSetting@endlink)  </param>
    def EvaluateFrf(self, evaluation_setting: FrfEvaluationSetting) -> None:
        """
         Performs evaluation for FRF. The evaluation results will be stored in an AFU file,
                which name could be returned by @link NXOpen::CAE::ResponseSimulation::Solution::GetResultFileName NXOpen::CAE::ResponseSimulation::Solution::GetResultFileName@endlink  
        """
        pass
    
    ##  Performs evaluation for transimissibility. The evaluation results will be stored in an AFU file,
    ##         which name could be returned by @link NXOpen::CAE::ResponseSimulation::Solution::GetResultFileName NXOpen::CAE::ResponseSimulation::Solution::GetResultFileName@endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="evaluation_setting"> (@link TransmissibilityEvaluationSetting NXOpen.CAE.ResponseSimulation.TransmissibilityEvaluationSetting@endlink)  </param>
    def EvaluateTransmissibility(self, evaluation_setting: TransmissibilityEvaluationSetting) -> None:
        """
         Performs evaluation for transimissibility. The evaluation results will be stored in an AFU file,
                which name could be returned by @link NXOpen::CAE::ResponseSimulation::Solution::GetResultFileName NXOpen::CAE::ResponseSimulation::Solution::GetResultFileName@endlink  
        """
        pass
    
    ##  Returns the evaluation parameters of Response Analysis Meta solution
    ##  @return evaluation_parameters (@link EvaluationParameters NXOpen.CAE.ResponseSimulation.EvaluationParameters@endlink):  .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetEvaluationParameters(self) -> EvaluationParameters:
        """
         Returns the evaluation parameters of Response Analysis Meta solution
         @return evaluation_parameters (@link EvaluationParameters NXOpen.CAE.ResponseSimulation.EvaluationParameters@endlink):  .
        """
        pass
    
    ##  Returns all the events of the solution
    ##  @return events (@link RSEvent List[NXOpen.CAE.ResponseSimulation.RSEvent]@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetEvents(self) -> List[RSEvent]:
        """
         Returns all the events of the solution
         @return events (@link RSEvent List[NXOpen.CAE.ResponseSimulation.RSEvent]@endlink):  .
        """
        pass
    
    ##  Returns the modal properties of Response Analysis Meta solution
    ##  @return modal_properties (@link ModalProperties NXOpen.CAE.ResponseSimulation.ModalProperties@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetModalProperties(self) -> ModalProperties:
        """
         Returns the modal properties of Response Analysis Meta solution
         @return modal_properties (@link ModalProperties NXOpen.CAE.ResponseSimulation.ModalProperties@endlink):  .
        """
        pass
    
    ##  Returns the result file name of solution 
    ##  @return result_file_name (str):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetResultFileName(self) -> str:
        """
         Returns the result file name of solution 
         @return result_file_name (str):  .
        """
        pass
    
    ##  Returns the response simulation solution name 
    ##  @return solutionName (str):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetSolutionName(self) -> str:
        """
         Returns the response simulation solution name 
         @return solutionName (str):  .
        """
        pass
    
    ##  Imports an event to the solution 
    ##  @return new_event (@link RSEvent NXOpen.CAE.ResponseSimulation.RSEvent@endlink):   .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="event_definition_file"> (str)  </param>
    ## <param name="suggested_name"> (str)  </param>
    def ImportEvent(self, event_definition_file: str, suggested_name: str) -> RSEvent:
        """
         Imports an event to the solution 
         @return new_event (@link RSEvent NXOpen.CAE.ResponseSimulation.RSEvent@endlink):   .
        """
        pass
    
    ##  Sets the response simulation solution name 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="solutionName"> (str)  </param>
    ## <param name="renameResultFile"> (bool)  if there are result files associated with the solution, rename the files or not</param>
    def SetSolutionName(self, solutionName: str, renameResultFile: bool) -> None:
        """
         Sets the response simulation solution name 
        """
        pass
    
##  Represents the manager to @link NXOpen::CAE::ResponseSimulation::StaticLoadExcitation NXOpen::CAE::ResponseSimulation::StaticLoadExcitation@endlink .
##      The object of type @link NXOpen::CAE::ResponseSimulation::StaticLoadExcitation NXOpen::CAE::ResponseSimulation::StaticLoadExcitation@endlink 
##       can only be created or edited through this class.
##       <br> To create a new instance of this class, use @link NXOpen::CAE::ResponseSimulation::ExcitationCollection::CreateStaticLoadExcitationBuilder  NXOpen::CAE::ResponseSimulation::ExcitationCollection::CreateStaticLoadExcitationBuilder @endlink  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class StaticLoadExcitationBuilder(ExcitationBuilder): 
    """ Represents the manager to <ja_class>NXOpen.CAE.ResponseSimulation.StaticLoadExcitation</ja_class>.
     The object of type <ja_class>NXOpen.CAE.ResponseSimulation.StaticLoadExcitation</ja_class>
      can only be created or edited through this class.
     """


    ## Getter for property: (@link FunctionComponentData NXOpen.CAE.ResponseSimulation.FunctionComponentData@endlink) ExcitationFunction
    ##  Returns the magnitude function   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return FunctionComponentData
    @property
    def ExcitationFunction(self) -> FunctionComponentData:
        """
        Getter for property: (@link FunctionComponentData NXOpen.CAE.ResponseSimulation.FunctionComponentData@endlink) ExcitationFunction
         Returns the magnitude function   
            
         
        """
        pass
    
##  Represents an excitation of static load type  <br> To create or edit an instance of this class, use @link NXOpen::CAE::ResponseSimulation::StaticLoadExcitationBuilder  NXOpen::CAE::ResponseSimulation::StaticLoadExcitationBuilder @endlink  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class StaticLoadExcitation(Excitation): 
    """ Represents an excitation of static load type """
    pass


import NXOpen
import NXOpen.CAE
## 
##     Represents a StrainGageBuilder
##      <br> To create a new instance of this class, use @link NXOpen::CAE::ResponseSimulation::StrainGageCollection::CreateStrainGageBuilder  NXOpen::CAE::ResponseSimulation::StrainGageCollection::CreateStrainGageBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## GageType </term> <description> 
##  
## UniAxial </description> </item> 
## 
## <item><term> 
##  
## Placement </term> <description> 
##  
## Node </description> </item> 
## 
## <item><term> 
##  
## Plane </term> <description> 
##  
## FacePlane </description> </item> 
## 
## <item><term> 
##  
## ResultType </term> <description> 
##  
## Strain </description> </item> 
## 
## <item><term> 
##  
## RotationAngle.Value </term> <description> 
##  
## 0.0 (millimeters part), 0.0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ShellElementFace </term> <description> 
##  
## Top </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX6.0.0  <br> 

class StrainGageBuilder(BaseBuilder): 
    """
    Represents a StrainGageBuilder
    """


    ## Getter for property: (@link NXOpen.SmartObject NXOpen.SmartObject@endlink) Csys
    ##  Returns the orientation direction, Only available when the strain gage's orientation plane type is
    ##             @link CAE::ResponseSimulation::StrainGageOrientationPlaneCsys CAE::ResponseSimulation::StrainGageOrientationPlaneCsys@endlink   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.SmartObject
    @property
    def Csys(self) -> NXOpen.SmartObject:
        """
        Getter for property: (@link NXOpen.SmartObject NXOpen.SmartObject@endlink) Csys
         Returns the orientation direction, Only available when the strain gage's orientation plane type is
                    @link CAE::ResponseSimulation::StrainGageOrientationPlaneCsys CAE::ResponseSimulation::StrainGageOrientationPlaneCsys@endlink   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.SmartObject NXOpen.SmartObject@endlink) Csys

    ##  Returns the orientation direction, Only available when the strain gage's orientation plane type is
    ##             @link CAE::ResponseSimulation::StrainGageOrientationPlaneCsys CAE::ResponseSimulation::StrainGageOrientationPlaneCsys@endlink   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @Csys.setter
    def Csys(self, orientation_coord_system: NXOpen.SmartObject):
        """
        Setter for property: (@link NXOpen.SmartObject NXOpen.SmartObject@endlink) Csys
         Returns the orientation direction, Only available when the strain gage's orientation plane type is
                    @link CAE::ResponseSimulation::StrainGageOrientationPlaneCsys CAE::ResponseSimulation::StrainGageOrientationPlaneCsys@endlink   
            
         
        """
        pass
    
    ## Getter for property: (@link StrainGageType NXOpen.CAE.ResponseSimulation.StrainGageType@endlink) GageType
    ##  Returns the type of strain gage  
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return StrainGageType
    @property
    def GageType(self) -> StrainGageType:
        """
        Getter for property: (@link StrainGageType NXOpen.CAE.ResponseSimulation.StrainGageType@endlink) GageType
         Returns the type of strain gage  
            
         
        """
        pass
    
    ## Setter for property: (@link StrainGageType NXOpen.CAE.ResponseSimulation.StrainGageType@endlink) GageType

    ##  Returns the type of strain gage  
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @GageType.setter
    def GageType(self, gage_type: StrainGageType):
        """
        Setter for property: (@link StrainGageType NXOpen.CAE.ResponseSimulation.StrainGageType@endlink) GageType
         Returns the type of strain gage  
            
         
        """
        pass
    
    ## Getter for property: (@link StrainGagePlacementType NXOpen.CAE.ResponseSimulation.StrainGagePlacementType@endlink) Placement
    ##  Returns the placement type of strain gage  
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return StrainGagePlacementType
    @property
    def Placement(self) -> StrainGagePlacementType:
        """
        Getter for property: (@link StrainGagePlacementType NXOpen.CAE.ResponseSimulation.StrainGagePlacementType@endlink) Placement
         Returns the placement type of strain gage  
            
         
        """
        pass
    
    ## Setter for property: (@link StrainGagePlacementType NXOpen.CAE.ResponseSimulation.StrainGagePlacementType@endlink) Placement

    ##  Returns the placement type of strain gage  
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @Placement.setter
    def Placement(self, gage_placement: StrainGagePlacementType):
        """
        Setter for property: (@link StrainGagePlacementType NXOpen.CAE.ResponseSimulation.StrainGagePlacementType@endlink) Placement
         Returns the placement type of strain gage  
            
         
        """
        pass
    
    ## Getter for property: (@link StrainGageOrientationPlane NXOpen.CAE.ResponseSimulation.StrainGageOrientationPlane@endlink) Plane
    ##  Returns the orientation plane type of strain gage  
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return StrainGageOrientationPlane
    @property
    def Plane(self) -> StrainGageOrientationPlane:
        """
        Getter for property: (@link StrainGageOrientationPlane NXOpen.CAE.ResponseSimulation.StrainGageOrientationPlane@endlink) Plane
         Returns the orientation plane type of strain gage  
            
         
        """
        pass
    
    ## Setter for property: (@link StrainGageOrientationPlane NXOpen.CAE.ResponseSimulation.StrainGageOrientationPlane@endlink) Plane

    ##  Returns the orientation plane type of strain gage  
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @Plane.setter
    def Plane(self, plane: StrainGageOrientationPlane):
        """
        Setter for property: (@link StrainGageOrientationPlane NXOpen.CAE.ResponseSimulation.StrainGageOrientationPlane@endlink) Plane
         Returns the orientation plane type of strain gage  
            
         
        """
        pass
    
    ## Getter for property: (@link StrainGageResult NXOpen.CAE.ResponseSimulation.StrainGageResult@endlink) ResultType
    ##  Returns the result type of strain gage  
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return StrainGageResult
    @property
    def ResultType(self) -> StrainGageResult:
        """
        Getter for property: (@link StrainGageResult NXOpen.CAE.ResponseSimulation.StrainGageResult@endlink) ResultType
         Returns the result type of strain gage  
            
         
        """
        pass
    
    ## Setter for property: (@link StrainGageResult NXOpen.CAE.ResponseSimulation.StrainGageResult@endlink) ResultType

    ##  Returns the result type of strain gage  
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @ResultType.setter
    def ResultType(self, result_type: StrainGageResult):
        """
        Setter for property: (@link StrainGageResult NXOpen.CAE.ResponseSimulation.StrainGageResult@endlink) ResultType
         Returns the result type of strain gage  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RotationAngle
    ##  Returns the rotation angle, Only available when the strain gage's orientation plane type is
    ##             @link CAE::ResponseSimulation::StrainGageOrientationPlaneCsys CAE::ResponseSimulation::StrainGageOrientationPlaneCsys@endlink    
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RotationAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RotationAngle
         Returns the rotation angle, Only available when the strain gage's orientation plane type is
                    @link CAE::ResponseSimulation::StrainGageOrientationPlaneCsys CAE::ResponseSimulation::StrainGageOrientationPlaneCsys@endlink    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.SelectFEElemFaceList NXOpen.CAE.SelectFEElemFaceList@endlink) SelectedElementFaces
    ##  Returns  the selected element face.  
    ##   
    ##             Only available when the strain gage's placement type is
    ##             @link CAE::ResponseSimulation::StrainGagePlacementTypeElementFaceCenter CAE::ResponseSimulation::StrainGagePlacementTypeElementFaceCenter@endlink     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX7.5.2  <br> 

    ## @return NXOpen.CAE.SelectFEElemFaceList
    @property
    def SelectedElementFaces(self) -> NXOpen.CAE.SelectFEElemFaceList:
        """
        Getter for property: (@link NXOpen.CAE.SelectFEElemFaceList NXOpen.CAE.SelectFEElemFaceList@endlink) SelectedElementFaces
         Returns  the selected element face.  
          
                    Only available when the strain gage's placement type is
                    @link CAE::ResponseSimulation::StrainGagePlacementTypeElementFaceCenter CAE::ResponseSimulation::StrainGagePlacementTypeElementFaceCenter@endlink     
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.SelectFENodeList NXOpen.CAE.SelectFENodeList@endlink) SelectedNode
    ##  Returns the destination nodes, Only available when the strain gage's placement type is
    ##             @link CAE::ResponseSimulation::StrainGagePlacementTypeNode CAE::ResponseSimulation::StrainGagePlacementTypeNode@endlink     
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.CAE.SelectFENodeList
    @property
    def SelectedNode(self) -> NXOpen.CAE.SelectFENodeList:
        """
        Getter for property: (@link NXOpen.CAE.SelectFENodeList NXOpen.CAE.SelectFENodeList@endlink) SelectedNode
         Returns the destination nodes, Only available when the strain gage's placement type is
                    @link CAE::ResponseSimulation::StrainGagePlacementTypeNode CAE::ResponseSimulation::StrainGagePlacementTypeNode@endlink     
            
         
        """
        pass
    
    ## Getter for property: (@link StrainGageShellElementFaceType NXOpen.CAE.ResponseSimulation.StrainGageShellElementFaceType@endlink) ShellElementFace
    ##  Returns the shell element face location type of strain gage   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return StrainGageShellElementFaceType
    @property
    def ShellElementFace(self) -> StrainGageShellElementFaceType:
        """
        Getter for property: (@link StrainGageShellElementFaceType NXOpen.CAE.ResponseSimulation.StrainGageShellElementFaceType@endlink) ShellElementFace
         Returns the shell element face location type of strain gage   
            
         
        """
        pass
    
    ## Setter for property: (@link StrainGageShellElementFaceType NXOpen.CAE.ResponseSimulation.StrainGageShellElementFaceType@endlink) ShellElementFace

    ##  Returns the shell element face location type of strain gage   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @ShellElementFace.setter
    def ShellElementFace(self, shell_element_face: StrainGageShellElementFaceType):
        """
        Setter for property: (@link StrainGageShellElementFaceType NXOpen.CAE.ResponseSimulation.StrainGageShellElementFaceType@endlink) ShellElementFace
         Returns the shell element face location type of strain gage   
            
         
        """
        pass
    
import NXOpen
##  Represents a collection of response analysis strain gage  <br> To obtain an instance of this class, refer to @link NXOpen::CAE::ResponseSimulation::Manager  NXOpen::CAE::ResponseSimulation::Manager @endlink  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class StrainGageCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of response analysis strain gage """


    ##  Creates a strain gage buider 
    ##  @return builder (@link StrainGageBuilder NXOpen.CAE.ResponseSimulation.StrainGageBuilder@endlink):   .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="strain_gage"> (@link StrainGage NXOpen.CAE.ResponseSimulation.StrainGage@endlink)   </param>
    def CreateStrainGageBuilder(self, strain_gage: StrainGage) -> StrainGageBuilder:
        """
         Creates a strain gage buider 
         @return builder (@link StrainGageBuilder NXOpen.CAE.ResponseSimulation.StrainGageBuilder@endlink):   .
        """
        pass
    
    ##  Finds an strain gage with specified gage name 
    ##  @return strain_gage (@link StrainGage NXOpen.CAE.ResponseSimulation.StrainGage@endlink):   .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="name"> (str)   </param>
    def FindObject(self, name: str) -> StrainGage:
        """
         Finds an strain gage with specified gage name 
         @return strain_gage (@link StrainGage NXOpen.CAE.ResponseSimulation.StrainGage@endlink):   .
        """
        pass
    
import NXOpen
##  This is a manager to the @link NXOpen::CAE::ResponseSimulation::StrainGageEvaluationSetting NXOpen::CAE::ResponseSimulation::StrainGageEvaluationSetting@endlink  class. 
##         Object of type @link NXOpen::CAE::ResponseSimulation::StrainGageEvaluationSetting NXOpen::CAE::ResponseSimulation::StrainGageEvaluationSetting@endlink  can be 
##         created and edited only through this class
##           <br> To create a new instance of this class, use @link NXOpen::CAE::ResponseSimulation::EvaluationSettingManager::CreateStrainGageEvaluationSettingBuilder  NXOpen::CAE::ResponseSimulation::EvaluationSettingManager::CreateStrainGageEvaluationSettingBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DataComponent </term> <description> 
##  
## AllXyPlane </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX6.0.0  <br> 

class StrainGageEvaluationSettingBuilder(FunctionEvaluationSettingBuilder): 
    """ This is a manager to the <ja_class>NXOpen.CAE.ResponseSimulation.StrainGageEvaluationSetting</ja_class> class. 
        Object of type <ja_class>NXOpen.CAE.ResponseSimulation.StrainGageEvaluationSetting</ja_class> can be 
        created and edited only through this class
         """


    ## Getter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) DataComponent
    ##  Returns the data component of strain gage evaluation results  
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return DirectionDataComponent
    @property
    def DataComponent(self) -> DirectionDataComponent:
        """
        Getter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) DataComponent
         Returns the data component of strain gage evaluation results  
            
         
        """
        pass
    
    ## Setter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) DataComponent

    ##  Returns the data component of strain gage evaluation results  
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @DataComponent.setter
    def DataComponent(self, data_component: DirectionDataComponent):
        """
        Setter for property: (@link DirectionDataComponent NXOpen.CAE.ResponseSimulation.DirectionDataComponent@endlink) DataComponent
         Returns the data component of strain gage evaluation results  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) StrainGage
    ##  Returns the destination strain Gages   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def StrainGage(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) StrainGage
         Returns the destination strain Gages   
            
         
        """
        pass
    
##  Represents the parameters setting for strain gage evaluation.  For more information, see the 
##     Response Dynamics section of the Gateway Help  <br> To create or edit an instance of this class, use @link NXOpen::CAE::ResponseSimulation::StrainGageEvaluationSettingBuilder  NXOpen::CAE::ResponseSimulation::StrainGageEvaluationSettingBuilder @endlink  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class StrainGageEvaluationSetting(DynamicResultEvaluationSetting): 
    """ Represents the parameters setting for strain gage evaluation.  For more information, see the 
    Response Dynamics section of the Gateway Help """
    pass


##  Specifies the orientation plane type of Strain Gage 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## FacePlane</term><description> 
##  </description> </item><item><term> 
## Csys</term><description> 
##  </description> </item></list>
class StrainGageOrientationPlane(Enum):
    """
    Members Include: <FacePlane> <Csys>
    """
    FacePlane: int
    Csys: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> StrainGageOrientationPlane:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Specifies the placement type of Strain Gage 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Node</term><description> 
##  </description> </item><item><term> 
## ElementFaceCenter</term><description> 
##  </description> </item></list>
class StrainGagePlacementType(Enum):
    """
    Members Include: <Node> <ElementFaceCenter>
    """
    Node: int
    ElementFaceCenter: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> StrainGagePlacementType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Specifies the result type of Strain Gage 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Strain</term><description> 
##  </description> </item><item><term> 
## Stress</term><description> 
##  </description> </item></list>
class StrainGageResult(Enum):
    """
    Members Include: <Strain> <Stress>
    """
    Strain: int
    Stress: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> StrainGageResult:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Specifies the shell element location type of Strain Gage 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Top</term><description> 
##  </description> </item><item><term> 
## Botton</term><description> 
##  </description> </item></list>
class StrainGageShellElementFaceType(Enum):
    """
    Members Include: <Top> <Botton>
    """
    Top: int
    Botton: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> StrainGageShellElementFaceType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Specifies the type of Strain Gage 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## UniAxial</term><description> 
##  </description> </item><item><term> 
## BiAxial</term><description> 
##  </description> </item><item><term> 
## Rosette45DegreeIncrement</term><description> 
##  Rosette 0-45-90 </description> </item><item><term> 
## Rosette60DegreeIncrement</term><description> 
##  Rosette 0-60-120 </description> </item></list>
class StrainGageType(Enum):
    """
    Members Include: <UniAxial> <BiAxial> <Rosette45DegreeIncrement> <Rosette60DegreeIncrement>
    """
    UniAxial: int
    BiAxial: int
    Rosette45DegreeIncrement: int
    Rosette60DegreeIncrement: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> StrainGageType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##  Represents a @link NXOpen::CAE::ResponseSimulation::StrainGage NXOpen::CAE::ResponseSimulation::StrainGage@endlink 
##          <br> To create or edit an instance of this class, use @link NXOpen::CAE::ResponseSimulation::StrainGageBuilder  NXOpen::CAE::ResponseSimulation::StrainGageBuilder @endlink  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class StrainGage(NXOpen.DisplayableObject): 
    """ Represents a <ja_class>NXOpen.CAE.ResponseSimulation.StrainGage</ja_class>
        """


    ##  Get display attribute of gage 
    ##  @return display_attr (@link RSDisplayObject NXOpen.CAE.ResponseSimulation.RSDisplayObject@endlink):   .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetDisplayAttribute(self) -> RSDisplayObject:
        """
         Get display attribute of gage 
         @return display_attr (@link RSDisplayObject NXOpen.CAE.ResponseSimulation.RSDisplayObject@endlink):   .
        """
        pass
    
import NXOpen.CAE
##  This is a manager to the @link NXOpen::CAE::ResponseSimulation::StrengthResultsEvaluationSetting NXOpen::CAE::ResponseSimulation::StrengthResultsEvaluationSetting@endlink  class. 
##     Object of type @link NXOpen::CAE::ResponseSimulation::StrengthResultsEvaluationSetting NXOpen::CAE::ResponseSimulation::StrengthResultsEvaluationSetting@endlink  can be 
##     created and edited only through this class
##       <br> To create a new instance of this class, use @link NXOpen::CAE::ResponseSimulation::EvaluationSettingManager::CreateStrengthResultsEvaluationSettingBuilder  NXOpen::CAE::ResponseSimulation::EvaluationSettingManager::CreateStrengthResultsEvaluationSettingBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class StrengthResultsEvaluationSettingBuilder(DynamicResultEvaluationSettingBuilder): 
    """ This is a manager to the <ja_class>NXOpen.CAE.ResponseSimulation.StrengthResultsEvaluationSetting</ja_class> class. 
    Object of type <ja_class>NXOpen.CAE.ResponseSimulation.StrengthResultsEvaluationSetting</ja_class> can be 
    created and edited only through this class
     """


    ## Getter for property: (@link CombinationEvaluationOptions NXOpen.CAE.ResponseSimulation.CombinationEvaluationOptions@endlink) CombinationOptionsBuilder
    ##  Returns the setting of combination evaluation   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return CombinationEvaluationOptions
    @property
    def CombinationOptionsBuilder(self) -> CombinationEvaluationOptions:
        """
        Getter for property: (@link CombinationEvaluationOptions NXOpen.CAE.ResponseSimulation.CombinationEvaluationOptions@endlink) CombinationOptionsBuilder
         Returns the setting of combination evaluation   
            
         
        """
        pass
    
    ## Getter for property: (@link DataLocation NXOpen.CAE.ResponseSimulation.DataLocation@endlink) DataLocation
    ##  Returns the setting of combination evaluation   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return DataLocation
    @property
    def DataLocation(self) -> DataLocation:
        """
        Getter for property: (@link DataLocation NXOpen.CAE.ResponseSimulation.DataLocation@endlink) DataLocation
         Returns the setting of combination evaluation   
            
         
        """
        pass
    
    ## Getter for property: (@link StrengthStressMaterialDefinitionMethod NXOpen.CAE.ResponseSimulation.StrengthStressMaterialDefinitionMethod@endlink) MaterialDefinitionType
    ##  Returns the definition method of material   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return StrengthStressMaterialDefinitionMethod
    @property
    def MaterialDefinitionType(self) -> StrengthStressMaterialDefinitionMethod:
        """
        Getter for property: (@link StrengthStressMaterialDefinitionMethod NXOpen.CAE.ResponseSimulation.StrengthStressMaterialDefinitionMethod@endlink) MaterialDefinitionType
         Returns the definition method of material   
            
         
        """
        pass
    
    ## Setter for property: (@link StrengthStressMaterialDefinitionMethod NXOpen.CAE.ResponseSimulation.StrengthStressMaterialDefinitionMethod@endlink) MaterialDefinitionType

    ##  Returns the definition method of material   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @MaterialDefinitionType.setter
    def MaterialDefinitionType(self, material_property: StrengthStressMaterialDefinitionMethod):
        """
        Setter for property: (@link StrengthStressMaterialDefinitionMethod NXOpen.CAE.ResponseSimulation.StrengthStressMaterialDefinitionMethod@endlink) MaterialDefinitionType
         Returns the definition method of material   
            
         
        """
        pass
    
    ## Getter for property: (bool) MaterialOverrideOption
    ##  Returns the choice of override material property or not.  
    ##    If false, the material safty factor will be read 
    ##              from destination element selected, else a customized value will be used   
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def MaterialOverrideOption(self) -> bool:
        """
        Getter for property: (bool) MaterialOverrideOption
         Returns the choice of override material property or not.  
           If false, the material safty factor will be read 
                     from destination element selected, else a customized value will be used   
         
        """
        pass
    
    ## Setter for property: (bool) MaterialOverrideOption

    ##  Returns the choice of override material property or not.  
    ##    If false, the material safty factor will be read 
    ##              from destination element selected, else a customized value will be used   
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @MaterialOverrideOption.setter
    def MaterialOverrideOption(self, override_material_property: bool):
        """
        Setter for property: (bool) MaterialOverrideOption
         Returns the choice of override material property or not.  
           If false, the material safty factor will be read 
                     from destination element selected, else a customized value will be used   
         
        """
        pass
    
    ## Getter for property: (float) MaterialSafetyFactor
    ##  Returns the customized material safety factor   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def MaterialSafetyFactor(self) -> float:
        """
        Getter for property: (float) MaterialSafetyFactor
         Returns the customized material safety factor   
            
         
        """
        pass
    
    ## Setter for property: (float) MaterialSafetyFactor

    ##  Returns the customized material safety factor   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @MaterialSafetyFactor.setter
    def MaterialSafetyFactor(self, safety_factor: float):
        """
        Setter for property: (float) MaterialSafetyFactor
         Returns the customized material safety factor   
            
         
        """
        pass
    
    ## Getter for property: (float) StandardDeviation
    ##  Returns the customized standard deviation for random event   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def StandardDeviation(self) -> float:
        """
        Getter for property: (float) StandardDeviation
         Returns the customized standard deviation for random event   
            
         
        """
        pass
    
    ## Setter for property: (float) StandardDeviation

    ##  Returns the customized standard deviation for random event   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @StandardDeviation.setter
    def StandardDeviation(self, standard_deviation: float):
        """
        Setter for property: (float) StandardDeviation
         Returns the customized standard deviation for random event   
            
         
        """
        pass
    
    ## Getter for property: (@link StrengthStressCriteria NXOpen.CAE.ResponseSimulation.StrengthStressCriteria@endlink) StressCriteriaType
    ##  Returns the stress criteria type   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return StrengthStressCriteria
    @property
    def StressCriteriaType(self) -> StrengthStressCriteria:
        """
        Getter for property: (@link StrengthStressCriteria NXOpen.CAE.ResponseSimulation.StrengthStressCriteria@endlink) StressCriteriaType
         Returns the stress criteria type   
            
         
        """
        pass
    
    ## Setter for property: (@link StrengthStressCriteria NXOpen.CAE.ResponseSimulation.StrengthStressCriteria@endlink) StressCriteriaType

    ##  Returns the stress criteria type   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @StressCriteriaType.setter
    def StressCriteriaType(self, stress_criteria: StrengthStressCriteria):
        """
        Setter for property: (@link StrengthStressCriteria NXOpen.CAE.ResponseSimulation.StrengthStressCriteria@endlink) StressCriteriaType
         Returns the stress criteria type   
            
         
        """
        pass
    
    ## Getter for property: (@link StrengthStressOption NXOpen.CAE.ResponseSimulation.StrengthStressOption@endlink) StressOptionType
    ##  Returns the stress option type   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return StrengthStressOption
    @property
    def StressOptionType(self) -> StrengthStressOption:
        """
        Getter for property: (@link StrengthStressOption NXOpen.CAE.ResponseSimulation.StrengthStressOption@endlink) StressOptionType
         Returns the stress option type   
            
         
        """
        pass
    
    ## Setter for property: (@link StrengthStressOption NXOpen.CAE.ResponseSimulation.StrengthStressOption@endlink) StressOptionType

    ##  Returns the stress option type   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @StressOptionType.setter
    def StressOptionType(self, stress_option: StrengthStressOption):
        """
        Setter for property: (@link StrengthStressOption NXOpen.CAE.ResponseSimulation.StrengthStressOption@endlink) StressOptionType
         Returns the stress option type   
            
         
        """
        pass
    
    ##  Returns the destination elements 
    ##  @return destination_elements (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    def GetDestinationElements(self) -> List[NXOpen.CAE.FEElement]:
        """
         Returns the destination elements 
         @return destination_elements (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink):  .
        """
        pass
    
    ##  Sets the destination elements 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ## <param name="destination_element"> (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink)  </param>
    def SetDestinationElements(self, destination_element: List[NXOpen.CAE.FEElement]) -> None:
        """
         Sets the destination elements 
        """
        pass
    
##  Represents parameters setting for strength results evaluation. Available to all kinds of 
##     event type  <br> To create or edit an instance of this class, use @link NXOpen::CAE::ResponseSimulation::StrengthResultsEvaluationSettingBuilder  NXOpen::CAE::ResponseSimulation::StrengthResultsEvaluationSettingBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class StrengthResultsEvaluationSetting(DynamicResultEvaluationSetting): 
    """ Represents parameters setting for strength results evaluation. Available to all kinds of 
    event type """
    pass


##  Specifies strength stress criteria 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## VonMises</term><description> 
##  </description> </item><item><term> 
## MaxPrinciple</term><description> 
##  </description> </item><item><term> 
## MinPrinciple</term><description> 
##  </description> </item></list>
class StrengthStressCriteria(Enum):
    """
    Members Include: <VonMises> <MaxPrinciple> <MinPrinciple>
    """
    VonMises: int
    MaxPrinciple: int
    MinPrinciple: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> StrengthStressCriteria:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Specifies the definition method for material 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## UltimateSafety</term><description> 
##  </description> </item><item><term> 
## YieldSafety</term><description> 
##  </description> </item></list>
class StrengthStressMaterialDefinitionMethod(Enum):
    """
    Members Include: <UltimateSafety> <YieldSafety>
    """
    UltimateSafety: int
    YieldSafety: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> StrengthStressMaterialDefinitionMethod:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  The options of stress 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## ElementMaximum</term><description> 
##  </description> </item><item><term> 
## NodeOnElement</term><description> 
##  </description> </item></list>
class StrengthStressOption(Enum):
    """
    Members Include: <ElementMaximum> <NodeOnElement>
    """
    ElementMaximum: int
    NodeOnElement: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> StrengthStressOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the manager to @link CAE::ResponseSimulation::DDAMExcitation CAE::ResponseSimulation::DDAMExcitation@endlink .
##      The object of type @link CAE::ResponseSimulation::DDAMExcitation CAE::ResponseSimulation::DDAMExcitation@endlink  can only
##     be created or edited through this class.  <br> To create a new instance of this class, use @link NXOpen::CAE::ResponseSimulation::ExcitationCollection::CreateTranslationalDdamExcitationBuilder  NXOpen::CAE::ResponseSimulation::ExcitationCollection::CreateTranslationalDdamExcitationBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class TranslationalDDAMExcitationBuilder(DDAMExcitationBuilder): 
    """ Represents the manager to <ja_class>CAE.ResponseSimulation.DDAMExcitation</ja_class>.
     The object of type <ja_class>CAE.ResponseSimulation.DDAMExcitation</ja_class> can only
    be created or edited through this class. """
    pass


##  Represents an DDAM excitation. DDAM excitation could only be used by DDAM event.  <br> To create or edit an instance of this class, use @link NXOpen::CAE::ResponseSimulation::TranslationalDDAMExcitationBuilder  NXOpen::CAE::ResponseSimulation::TranslationalDDAMExcitationBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class TranslationalDDAMExcitation(DDAMExcitation): 
    """ Represents an DDAM excitation. DDAM excitation could only be used by DDAM event. """
    pass


import NXOpen
##  Represents the manager to @link NXOpen::CAE::ResponseSimulation::TranslationalNodalFunctionExcitation NXOpen::CAE::ResponseSimulation::TranslationalNodalFunctionExcitation@endlink . 
##     The objects of @link NXOpen::CAE::ResponseSimulation::TranslationalNodalFunctionExcitation NXOpen::CAE::ResponseSimulation::TranslationalNodalFunctionExcitation@endlink  
##     can be created or edited on through this class  <br> To create a new instance of this class, use @link NXOpen::CAE::ResponseSimulation::ExcitationCollection::CreateTranslationalNodalFunctionExcitationBuilder  NXOpen::CAE::ResponseSimulation::ExcitationCollection::CreateTranslationalNodalFunctionExcitationBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class TranslationalNodalFunctionExcitationBuilder(NodalFunctionExcitationBuilder): 
    """ Represents the manager to <ja_class>NXOpen.CAE.ResponseSimulation.TranslationalNodalFunctionExcitation</ja_class>. 
    The objects of <ja_class>NXOpen.CAE.ResponseSimulation.TranslationalNodalFunctionExcitation</ja_class> 
    can be created or edited on through this class """


    ## Represents the rotation axis type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## X</term><description> 
    ##   </description> </item><item><term> 
    ## Y</term><description> 
    ##   </description> </item><item><term> 
    ## Z</term><description> 
    ##   </description> </item></list>
    class RotationAxisType(Enum):
        """
        Members Include: <X> <Y> <Z>
        """
        X: int
        Y: int
        Z: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TranslationalNodalFunctionExcitationBuilder.RotationAxisType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) EnableUserDefinedDirection
    ##  Returns the excitation function definition method   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def EnableUserDefinedDirection(self) -> bool:
        """
        Getter for property: (bool) EnableUserDefinedDirection
         Returns the excitation function definition method   
            
         
        """
        pass
    
    ## Setter for property: (bool) EnableUserDefinedDirection

    ##  Returns the excitation function definition method   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @EnableUserDefinedDirection.setter
    def EnableUserDefinedDirection(self, enable_user_defefined_direction: bool):
        """
        Setter for property: (bool) EnableUserDefinedDirection
         Returns the excitation function definition method   
            
         
        """
        pass
    
    ## Getter for property: (bool) EnableUserDefinedRotation
    ##  Returns the excitation function definition method   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def EnableUserDefinedRotation(self) -> bool:
        """
        Getter for property: (bool) EnableUserDefinedRotation
         Returns the excitation function definition method   
            
         
        """
        pass
    
    ## Setter for property: (bool) EnableUserDefinedRotation

    ##  Returns the excitation function definition method   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @EnableUserDefinedRotation.setter
    def EnableUserDefinedRotation(self, enable_user_defined_rotation: bool):
        """
        Setter for property: (bool) EnableUserDefinedRotation
         Returns the excitation function definition method   
            
         
        """
        pass
    
    ## Getter for property: (@link FunctionComponentData NXOpen.CAE.ResponseSimulation.FunctionComponentData@endlink) FunctionComponentX
    ##  Returns the function component of X direction    
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return FunctionComponentData
    @property
    def FunctionComponentX(self) -> FunctionComponentData:
        """
        Getter for property: (@link FunctionComponentData NXOpen.CAE.ResponseSimulation.FunctionComponentData@endlink) FunctionComponentX
         Returns the function component of X direction    
            
         
        """
        pass
    
    ## Getter for property: (@link FunctionComponentData NXOpen.CAE.ResponseSimulation.FunctionComponentData@endlink) FunctionComponentY
    ##  Returns the function component of Y direction   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return FunctionComponentData
    @property
    def FunctionComponentY(self) -> FunctionComponentData:
        """
        Getter for property: (@link FunctionComponentData NXOpen.CAE.ResponseSimulation.FunctionComponentData@endlink) FunctionComponentY
         Returns the function component of Y direction   
            
         
        """
        pass
    
    ## Getter for property: (@link FunctionComponentData NXOpen.CAE.ResponseSimulation.FunctionComponentData@endlink) FunctionComponentZ
    ##  Returns the function component of Z direction   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return FunctionComponentData
    @property
    def FunctionComponentZ(self) -> FunctionComponentData:
        """
        Getter for property: (@link FunctionComponentData NXOpen.CAE.ResponseSimulation.FunctionComponentData@endlink) FunctionComponentZ
         Returns the function component of Z direction   
            
         
        """
        pass
    
    ## Getter for property: (@link TranslationalNodalFunctionExcitationBuilder.RotationAxisType NXOpen.CAE.ResponseSimulation.TranslationalNodalFunctionExcitationBuilder.RotationAxisType@endlink) RotationAxis
    ##  Returns the rotation axis   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return TranslationalNodalFunctionExcitationBuilder.RotationAxisType
    @property
    def RotationAxis(self) -> TranslationalNodalFunctionExcitationBuilder.RotationAxisType:
        """
        Getter for property: (@link TranslationalNodalFunctionExcitationBuilder.RotationAxisType NXOpen.CAE.ResponseSimulation.TranslationalNodalFunctionExcitationBuilder.RotationAxisType@endlink) RotationAxis
         Returns the rotation axis   
            
         
        """
        pass
    
    ## Setter for property: (@link TranslationalNodalFunctionExcitationBuilder.RotationAxisType NXOpen.CAE.ResponseSimulation.TranslationalNodalFunctionExcitationBuilder.RotationAxisType@endlink) RotationAxis

    ##  Returns the rotation axis   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @RotationAxis.setter
    def RotationAxis(self, rotation_axis: TranslationalNodalFunctionExcitationBuilder.RotationAxisType):
        """
        Setter for property: (@link TranslationalNodalFunctionExcitationBuilder.RotationAxisType NXOpen.CAE.ResponseSimulation.TranslationalNodalFunctionExcitationBuilder.RotationAxisType@endlink) RotationAxis
         Returns the rotation axis   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) UserDefinedDirection
    ##  Returns the magnitude direction   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def UserDefinedDirection(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) UserDefinedDirection
         Returns the magnitude direction   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) UserDefinedDirection

    ##  Returns the magnitude direction   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @UserDefinedDirection.setter
    def UserDefinedDirection(self, magnitude_direction: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) UserDefinedDirection
         Returns the magnitude direction   
            
         
        """
        pass
    
    ## Getter for property: (@link FunctionComponentData NXOpen.CAE.ResponseSimulation.FunctionComponentData@endlink) UserDefinedFunction
    ##  Returns the magnitude function   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return FunctionComponentData
    @property
    def UserDefinedFunction(self) -> FunctionComponentData:
        """
        Getter for property: (@link FunctionComponentData NXOpen.CAE.ResponseSimulation.FunctionComponentData@endlink) UserDefinedFunction
         Returns the magnitude function   
            
         
        """
        pass
    
##  Represents a translational nodal function excitation  <br> To create or edit an instance of this class, use @link NXOpen::CAE::ResponseSimulation::TranslationalNodalFunctionExcitationBuilder  NXOpen::CAE::ResponseSimulation::TranslationalNodalFunctionExcitationBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class TranslationalNodalFunctionExcitation(NodalFunctionExcitation): 
    """ Represents a translational nodal function excitation """
    pass


##  This is a manager to the @link NXOpen::CAE::ResponseSimulation::TransmissibilityEvaluationSetting NXOpen::CAE::ResponseSimulation::TransmissibilityEvaluationSetting@endlink  class. 
##     Object of type @link NXOpen::CAE::ResponseSimulation::TransmissibilityEvaluationSetting NXOpen::CAE::ResponseSimulation::TransmissibilityEvaluationSetting@endlink  can be 
##     created and edited only through this class
##       <br> To create a new instance of this class, use @link NXOpen::CAE::ResponseSimulation::EvaluationSettingManager::CreateTransmissibilityEvaluationSettingBuilder  NXOpen::CAE::ResponseSimulation::EvaluationSettingManager::CreateTransmissibilityEvaluationSettingBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class TransmissibilityEvaluationSettingBuilder(ModalResultsEvaluationSettingBuilder): 
    """ This is a manager to the <ja_class>NXOpen.CAE.ResponseSimulation.TransmissibilityEvaluationSetting</ja_class> class. 
    Object of type <ja_class>NXOpen.CAE.ResponseSimulation.TransmissibilityEvaluationSetting</ja_class> can be 
    created and edited only through this class
     """


    ##  This enum defines input motion type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Displacement</term><description> 
    ##   </description> </item><item><term> 
    ## Velocity</term><description> 
    ##   </description> </item><item><term> 
    ## Acceleration</term><description> 
    ##   </description> </item></list>
    class MotionType(Enum):
        """
        Members Include: <Displacement> <Velocity> <Acceleration>
        """
        Displacement: int
        Velocity: int
        Acceleration: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TransmissibilityEvaluationSettingBuilder.MotionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link TransmissibilityEvaluationSettingBuilder.MotionType NXOpen.CAE.ResponseSimulation.TransmissibilityEvaluationSettingBuilder.MotionType@endlink) InputMotionType
    ##  Returns the input motion type   
    ##     
    ##  
    ## Getter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return TransmissibilityEvaluationSettingBuilder.MotionType
    @property
    def InputMotionType(self) -> TransmissibilityEvaluationSettingBuilder.MotionType:
        """
        Getter for property: (@link TransmissibilityEvaluationSettingBuilder.MotionType NXOpen.CAE.ResponseSimulation.TransmissibilityEvaluationSettingBuilder.MotionType@endlink) InputMotionType
         Returns the input motion type   
            
         
        """
        pass
    
    ## Setter for property: (@link TransmissibilityEvaluationSettingBuilder.MotionType NXOpen.CAE.ResponseSimulation.TransmissibilityEvaluationSettingBuilder.MotionType@endlink) InputMotionType

    ##  Returns the input motion type   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @InputMotionType.setter
    def InputMotionType(self, motion_type: TransmissibilityEvaluationSettingBuilder.MotionType):
        """
        Setter for property: (@link TransmissibilityEvaluationSettingBuilder.MotionType NXOpen.CAE.ResponseSimulation.TransmissibilityEvaluationSettingBuilder.MotionType@endlink) InputMotionType
         Returns the input motion type   
            
         
        """
        pass
    
##  Represents parameters setting for transmissibility evaluation  <br> To create or edit an instance of this class, use @link NXOpen::CAE::ResponseSimulation::TransmissibilityEvaluationSettingBuilder  NXOpen::CAE::ResponseSimulation::TransmissibilityEvaluationSettingBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class TransmissibilityEvaluationSetting(ModalResultsEvaluationSetting): 
    """ Represents parameters setting for transmissibility evaluation """
    pass


import NXOpen
import NXOpen.GeometricUtilities
## 
##     Represents a @link NXOpen::CAE::ResponseSimulation::VelocityImpactDirection NXOpen::CAE::ResponseSimulation::VelocityImpactDirection@endlink 
##     
## 
##   <br>  Created in NX6.0.0  <br> 

class VelocityImpactDirection(NXOpen.TaggedObject): 
    """
    Represents a <ja_class>NXOpen.CAE.ResponseSimulation.VelocityImpactDirection</ja_class>
    """


    ##  the direction options for impact 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NodalComponent</term><description> 
    ##  </description> </item><item><term> 
    ## UserDefined</term><description> 
    ##  </description> </item></list>
    class DirectionType(Enum):
        """
        Members Include: <NodalComponent> <UserDefined>
        """
        NodalComponent: int
        UserDefined: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> VelocityImpactDirection.DirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the types of nodal component 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Dof1</term><description> 
    ##  </description> </item><item><term> 
    ## Dof2</term><description> 
    ##  </description> </item><item><term> 
    ## Dof3</term><description> 
    ##  </description> </item></list>
    class NodalComponentType(Enum):
        """
        Members Include: <Dof1> <Dof2> <Dof3>
        """
        Dof1: int
        Dof2: int
        Dof3: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> VelocityImpactDirection.NodalComponentType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link VelocityImpactDirection.DirectionType NXOpen.CAE.ResponseSimulation.VelocityImpactDirection.DirectionType@endlink) DirectionOption
    ##  Returns the direction option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return VelocityImpactDirection.DirectionType
    @property
    def DirectionOption(self) -> VelocityImpactDirection.DirectionType:
        """
        Getter for property: (@link VelocityImpactDirection.DirectionType NXOpen.CAE.ResponseSimulation.VelocityImpactDirection.DirectionType@endlink) DirectionOption
         Returns the direction option   
            
         
        """
        pass
    
    ## Setter for property: (@link VelocityImpactDirection.DirectionType NXOpen.CAE.ResponseSimulation.VelocityImpactDirection.DirectionType@endlink) DirectionOption

    ##  Returns the direction option   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @DirectionOption.setter
    def DirectionOption(self, mDirectionOption: VelocityImpactDirection.DirectionType):
        """
        Setter for property: (@link VelocityImpactDirection.DirectionType NXOpen.CAE.ResponseSimulation.VelocityImpactDirection.DirectionType@endlink) DirectionOption
         Returns the direction option   
            
         
        """
        pass
    
    ## Getter for property: (@link VelocityImpactDirection.NodalComponentType NXOpen.CAE.ResponseSimulation.VelocityImpactDirection.NodalComponentType@endlink) NodalComponent
    ##  Returns the selected nodal component   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return VelocityImpactDirection.NodalComponentType
    @property
    def NodalComponent(self) -> VelocityImpactDirection.NodalComponentType:
        """
        Getter for property: (@link VelocityImpactDirection.NodalComponentType NXOpen.CAE.ResponseSimulation.VelocityImpactDirection.NodalComponentType@endlink) NodalComponent
         Returns the selected nodal component   
            
         
        """
        pass
    
    ## Setter for property: (@link VelocityImpactDirection.NodalComponentType NXOpen.CAE.ResponseSimulation.VelocityImpactDirection.NodalComponentType@endlink) NodalComponent

    ##  Returns the selected nodal component   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @NodalComponent.setter
    def NodalComponent(self, nodalComponent: VelocityImpactDirection.NodalComponentType):
        """
        Setter for property: (@link VelocityImpactDirection.NodalComponentType NXOpen.CAE.ResponseSimulation.VelocityImpactDirection.NodalComponentType@endlink) NodalComponent
         Returns the selected nodal component   
            
         
        """
        pass
    
    ## Getter for property: (bool) ReverseDirection
    ##  Returns the option to reverse direction of nodal component or not.  
    ##    Only valid when direction option is
    ##         @link NXOpen::CAE::ResponseSimulation::VelocityImpactDirection::DirectionTypeNodalComponent NXOpen::CAE::ResponseSimulation::VelocityImpactDirection::DirectionTypeNodalComponent@endlink    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def ReverseDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseDirection
         Returns the option to reverse direction of nodal component or not.  
           Only valid when direction option is
                @link NXOpen::CAE::ResponseSimulation::VelocityImpactDirection::DirectionTypeNodalComponent NXOpen::CAE::ResponseSimulation::VelocityImpactDirection::DirectionTypeNodalComponent@endlink    
         
        """
        pass
    
    ## Setter for property: (bool) ReverseDirection

    ##  Returns the option to reverse direction of nodal component or not.  
    ##    Only valid when direction option is
    ##         @link NXOpen::CAE::ResponseSimulation::VelocityImpactDirection::DirectionTypeNodalComponent NXOpen::CAE::ResponseSimulation::VelocityImpactDirection::DirectionTypeNodalComponent@endlink    
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @ReverseDirection.setter
    def ReverseDirection(self, reverseDirection: bool):
        """
        Setter for property: (bool) ReverseDirection
         Returns the option to reverse direction of nodal component or not.  
           Only valid when direction option is
                @link NXOpen::CAE::ResponseSimulation::VelocityImpactDirection::DirectionTypeNodalComponent NXOpen::CAE::ResponseSimulation::VelocityImpactDirection::DirectionTypeNodalComponent@endlink    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) UserDefinedDirection
    ##  Returns the user-defined direction  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def UserDefinedDirection(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) UserDefinedDirection
         Returns the user-defined direction  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) UserDefinedDirection

    ##  Returns the user-defined direction  
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @UserDefinedDirection.setter
    def UserDefinedDirection(self, userDefinedDirection: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) UserDefinedDirection
         Returns the user-defined direction  
            
         
        """
        pass
    
## 
##     Represents a @link NXOpen::CAE::ResponseSimulation::VelocityImpactExcitationBuilder NXOpen::CAE::ResponseSimulation::VelocityImpactExcitationBuilder@endlink 
##      <br> To create a new instance of this class, use @link NXOpen::CAE::ResponseSimulation::ExcitationCollection::CreateVelocityImpactExcitationBuilder  NXOpen::CAE::ResponseSimulation::ExcitationCollection::CreateVelocityImpactExcitationBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## ImpactDirection.DirectionOption </term> <description> 
##  
## NodalComponent </description> </item> 
## 
## <item><term> 
##  
## ImpactDirection.NodalComponent </term> <description> 
##  
## Dof1 </description> </item> 
## 
## <item><term> 
##  
## ImpactMethod </term> <description> 
##  
## ConstantVelocity </description> </item> 
## 
## <item><term> 
##  
## ImpactParameters.DropHeight.Value </term> <description> 
##  
## 1.0 (millimeters part), 1.0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ImpactParameters.PulseDuration.Value </term> <description> 
##  
## 1.0 (millimeters part), 1.0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ImpactParameters.StartPosition </term> <description> 
##  
## AtDrop </description> </item> 
## 
## <item><term> 
##  
## ImpactParameters.TimeStep.Value </term> <description> 
##  
## 1.0 (millimeters part), 1.0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ImpactParameters.Velocity.Value </term> <description> 
##  
## 1.0 (millimeters part), 1.0 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX6.0.0  <br> 

class VelocityImpactExcitationBuilder(ExcitationBuilder): 
    """
    Represents a <ja_class>NXOpen.CAE.ResponseSimulation.VelocityImpactExcitationBuilder</ja_class>
    """


    ##  the impact definiton methods 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ConstantVelocity</term><description> 
    ##  the users will only be able to specify the velocity for the impact </description> </item><item><term> 
    ## DropImpact</term><description> 
    ##  the users will be able to specify the drop height or the desired velocity at the impact</description> </item></list>
    class ImpactMethodType(Enum):
        """
        Members Include: <ConstantVelocity> <DropImpact>
        """
        ConstantVelocity: int
        DropImpact: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> VelocityImpactExcitationBuilder.ImpactMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link VelocityImpactDirection NXOpen.CAE.ResponseSimulation.VelocityImpactDirection@endlink) ImpactDirection
    ##  Returns the impact direction setting  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return VelocityImpactDirection
    @property
    def ImpactDirection(self) -> VelocityImpactDirection:
        """
        Getter for property: (@link VelocityImpactDirection NXOpen.CAE.ResponseSimulation.VelocityImpactDirection@endlink) ImpactDirection
         Returns the impact direction setting  
            
         
        """
        pass
    
    ## Getter for property: (@link VelocityImpactExcitationBuilder.ImpactMethodType NXOpen.CAE.ResponseSimulation.VelocityImpactExcitationBuilder.ImpactMethodType@endlink) ImpactMethod
    ##  Returns the impact method   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return VelocityImpactExcitationBuilder.ImpactMethodType
    @property
    def ImpactMethod(self) -> VelocityImpactExcitationBuilder.ImpactMethodType:
        """
        Getter for property: (@link VelocityImpactExcitationBuilder.ImpactMethodType NXOpen.CAE.ResponseSimulation.VelocityImpactExcitationBuilder.ImpactMethodType@endlink) ImpactMethod
         Returns the impact method   
            
         
        """
        pass
    
    ## Setter for property: (@link VelocityImpactExcitationBuilder.ImpactMethodType NXOpen.CAE.ResponseSimulation.VelocityImpactExcitationBuilder.ImpactMethodType@endlink) ImpactMethod

    ##  Returns the impact method   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @ImpactMethod.setter
    def ImpactMethod(self, impactMethod: VelocityImpactExcitationBuilder.ImpactMethodType):
        """
        Setter for property: (@link VelocityImpactExcitationBuilder.ImpactMethodType NXOpen.CAE.ResponseSimulation.VelocityImpactExcitationBuilder.ImpactMethodType@endlink) ImpactMethod
         Returns the impact method   
            
         
        """
        pass
    
    ## Getter for property: (@link VelocityImpactParameters NXOpen.CAE.ResponseSimulation.VelocityImpactParameters@endlink) ImpactParameters
    ##  Returns the impact parameters setting  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return VelocityImpactParameters
    @property
    def ImpactParameters(self) -> VelocityImpactParameters:
        """
        Getter for property: (@link VelocityImpactParameters NXOpen.CAE.ResponseSimulation.VelocityImpactParameters@endlink) ImpactParameters
         Returns the impact parameters setting  
            
         
        """
        pass
    
##  Represents a velocity impact excitation  <br> To create or edit an instance of this class, use @link NXOpen::CAE::ResponseSimulation::VelocityImpactExcitationBuilder  NXOpen::CAE::ResponseSimulation::VelocityImpactExcitationBuilder @endlink  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class VelocityImpactExcitation(Excitation): 
    """ Represents a velocity impact excitation """
    pass


import NXOpen
import NXOpen.GeometricUtilities
## 
##     Represents a @link NXOpen::CAE::ResponseSimulation::VelocityImpactParameters NXOpen::CAE::ResponseSimulation::VelocityImpactParameters@endlink 
##     
## 
##   <br>  Created in NX6.0.0  <br> 

class VelocityImpactParameters(NXOpen.TaggedObject): 
    """
    Represents a <ja_class>NXOpen.CAE.ResponseSimulation.VelocityImpactParameters</ja_class>
    """


    ##  the calculation start position for impact 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## AtDrop</term><description> 
    ##  Calculation starts from the drop time</description> </item><item><term> 
    ## BeforeImpact</term><description> 
    ##  Calculation ends at the impact time </description> </item><item><term> 
    ## AtImpact</term><description> 
    ##  Calculation starts from the impact time </description> </item></list>
    class StartPositionType(Enum):
        """
        Members Include: <AtDrop> <BeforeImpact> <AtImpact>
        """
        AtDrop: int
        BeforeImpact: int
        AtImpact: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> VelocityImpactParameters.StartPositionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DropHeight
    ##  Returns the drop height.  
    ##    Not available if the impact excitation is of type @link  
    ##         CAE::ResponseSimulation::VelocityImpactExcitationBuilder::ImpactMethodTypeConstantVelocity
    ##           
    ##         CAE::ResponseSimulation::VelocityImpactExcitationBuilder::ImpactMethodTypeConstantVelocity
    ##         @endlink    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DropHeight(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DropHeight
         Returns the drop height.  
           Not available if the impact excitation is of type @link  
                CAE::ResponseSimulation::VelocityImpactExcitationBuilder::ImpactMethodTypeConstantVelocity
                  
                CAE::ResponseSimulation::VelocityImpactExcitationBuilder::ImpactMethodTypeConstantVelocity
                @endlink    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) PulseDuration
    ##  Returns the impact pulse duration   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def PulseDuration(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) PulseDuration
         Returns the impact pulse duration   
            
         
        """
        pass
    
    ## Getter for property: (@link VelocityImpactParameters.StartPositionType NXOpen.CAE.ResponseSimulation.VelocityImpactParameters.StartPositionType@endlink) StartPosition
    ##  Returns the start position   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return VelocityImpactParameters.StartPositionType
    @property
    def StartPosition(self) -> VelocityImpactParameters.StartPositionType:
        """
        Getter for property: (@link VelocityImpactParameters.StartPositionType NXOpen.CAE.ResponseSimulation.VelocityImpactParameters.StartPositionType@endlink) StartPosition
         Returns the start position   
            
         
        """
        pass
    
    ## Setter for property: (@link VelocityImpactParameters.StartPositionType NXOpen.CAE.ResponseSimulation.VelocityImpactParameters.StartPositionType@endlink) StartPosition

    ##  Returns the start position   
    ##     
    ##  
    ## Setter License requirements: nx_response_anlys ("NX Response Analysis")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @StartPosition.setter
    def StartPosition(self, mStartPosition: VelocityImpactParameters.StartPositionType):
        """
        Setter for property: (@link VelocityImpactParameters.StartPositionType NXOpen.CAE.ResponseSimulation.VelocityImpactParameters.StartPositionType@endlink) StartPosition
         Returns the start position   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TimeStep
    ##  Returns the time step.  
    ##    The value must be larger than 1/20 of the impact pulse duration   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def TimeStep(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TimeStep
         Returns the time step.  
           The value must be larger than 1/20 of the impact pulse duration   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Velocity
    ##  Returns the velocity   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Velocity(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Velocity
         Returns the velocity   
            
         
        """
        pass
    
## @package NXOpen.CAE.ResponseSimulation
## Classes, Enums and Structs under NXOpen.CAE.ResponseSimulation namespace

##  @link CombinationEvaluationOptionsEvaluationMethod NXOpen.CAE.ResponseSimulation.CombinationEvaluationOptionsEvaluationMethod @endlink is an alias for @link CombinationEvaluationOptions.EvaluationMethod NXOpen.CAE.ResponseSimulation.CombinationEvaluationOptions.EvaluationMethod@endlink
CombinationEvaluationOptionsEvaluationMethod = CombinationEvaluationOptions.EvaluationMethod


##  @link CombinationEvaluationOptionsMultipleExcitationCombinationMethod NXOpen.CAE.ResponseSimulation.CombinationEvaluationOptionsMultipleExcitationCombinationMethod @endlink is an alias for @link CombinationEvaluationOptions.MultipleExcitationCombinationMethod NXOpen.CAE.ResponseSimulation.CombinationEvaluationOptions.MultipleExcitationCombinationMethod@endlink
CombinationEvaluationOptionsMultipleExcitationCombinationMethod = CombinationEvaluationOptions.MultipleExcitationCombinationMethod


##  @link CSDExcitationCorrelationType NXOpen.CAE.ResponseSimulation.CSDExcitationCorrelationType @endlink is an alias for @link CSDExcitation.CorrelationType NXOpen.CAE.ResponseSimulation.CSDExcitation.CorrelationType@endlink
CSDExcitationCorrelationType = CSDExcitation.CorrelationType


##  @link DataLocationBeam NXOpen.CAE.ResponseSimulation.DataLocationBeam @endlink is an alias for @link DataLocation.Beam NXOpen.CAE.ResponseSimulation.DataLocation.Beam@endlink
DataLocationBeam = DataLocation.Beam


##  @link DataLocationElement NXOpen.CAE.ResponseSimulation.DataLocationElement @endlink is an alias for @link DataLocation.Element NXOpen.CAE.ResponseSimulation.DataLocation.Element@endlink
DataLocationElement = DataLocation.Element


##  @link DataLocationShell NXOpen.CAE.ResponseSimulation.DataLocationShell @endlink is an alias for @link DataLocation.Shell NXOpen.CAE.ResponseSimulation.DataLocation.Shell@endlink
DataLocationShell = DataLocation.Shell


##  @link DDAMComponentDataLoadingType NXOpen.CAE.ResponseSimulation.DDAMComponentDataLoadingType @endlink is an alias for @link DDAMComponentData.LoadingType NXOpen.CAE.ResponseSimulation.DDAMComponentData.LoadingType@endlink
DDAMComponentDataLoadingType = DDAMComponentData.LoadingType


##  @link DDAMComponentDataResponseType NXOpen.CAE.ResponseSimulation.DDAMComponentDataResponseType @endlink is an alias for @link DDAMComponentData.ResponseType NXOpen.CAE.ResponseSimulation.DDAMComponentData.ResponseType@endlink
DDAMComponentDataResponseType = DDAMComponentData.ResponseType


##  @link DDAMExcitationCoefficientDefinitionType NXOpen.CAE.ResponseSimulation.DDAMExcitationCoefficientDefinitionType @endlink is an alias for @link DDAMExcitation.CoefficientDefinitionType NXOpen.CAE.ResponseSimulation.DDAMExcitation.CoefficientDefinitionType@endlink
DDAMExcitationCoefficientDefinitionType = DDAMExcitation.CoefficientDefinitionType


##  @link DDAMExcitationLoadingType NXOpen.CAE.ResponseSimulation.DDAMExcitationLoadingType @endlink is an alias for @link DDAMExcitation.LoadingType NXOpen.CAE.ResponseSimulation.DDAMExcitation.LoadingType@endlink
DDAMExcitationLoadingType = DDAMExcitation.LoadingType


##  @link DDAMExcitationMountingType NXOpen.CAE.ResponseSimulation.DDAMExcitationMountingType @endlink is an alias for @link DDAMExcitation.MountingType NXOpen.CAE.ResponseSimulation.DDAMExcitation.MountingType@endlink
DDAMExcitationMountingType = DDAMExcitation.MountingType


##  @link DDAMExcitationResponseType NXOpen.CAE.ResponseSimulation.DDAMExcitationResponseType @endlink is an alias for @link DDAMExcitation.ResponseType NXOpen.CAE.ResponseSimulation.DDAMExcitation.ResponseType@endlink
DDAMExcitationResponseType = DDAMExcitation.ResponseType


##  @link DDAMExcitationShipType NXOpen.CAE.ResponseSimulation.DDAMExcitationShipType @endlink is an alias for @link DDAMExcitation.ShipType NXOpen.CAE.ResponseSimulation.DDAMExcitation.ShipType@endlink
DDAMExcitationShipType = DDAMExcitation.ShipType


##  @link EvaluationParametersAnalysisIntegrationMethod NXOpen.CAE.ResponseSimulation.EvaluationParametersAnalysisIntegrationMethod @endlink is an alias for @link EvaluationParameters.AnalysisIntegrationMethod NXOpen.CAE.ResponseSimulation.EvaluationParameters.AnalysisIntegrationMethod@endlink
EvaluationParametersAnalysisIntegrationMethod = EvaluationParameters.AnalysisIntegrationMethod


##  @link ExcitationBuilderExcitationLocationType NXOpen.CAE.ResponseSimulation.ExcitationBuilderExcitationLocationType @endlink is an alias for @link ExcitationBuilder.ExcitationLocationType NXOpen.CAE.ResponseSimulation.ExcitationBuilder.ExcitationLocationType@endlink
ExcitationBuilderExcitationLocationType = ExcitationBuilder.ExcitationLocationType


##  @link ExcitationComponent NXOpen.CAE.ResponseSimulation.ExcitationComponent @endlink is an alias for @link Excitation.Component NXOpen.CAE.ResponseSimulation.Excitation.Component@endlink
ExcitationComponent = Excitation.Component


##  @link FrequencyDefinitionDefinition NXOpen.CAE.ResponseSimulation.FrequencyDefinitionDefinition @endlink is an alias for @link FrequencyDefinition.Definition NXOpen.CAE.ResponseSimulation.FrequencyDefinition.Definition@endlink
FrequencyDefinitionDefinition = FrequencyDefinition.Definition


##  @link FrequencyDefinitionInterpolationMethod NXOpen.CAE.ResponseSimulation.FrequencyDefinitionInterpolationMethod @endlink is an alias for @link FrequencyDefinition.InterpolationMethod NXOpen.CAE.ResponseSimulation.FrequencyDefinition.InterpolationMethod@endlink
FrequencyDefinitionInterpolationMethod = FrequencyDefinition.InterpolationMethod


##  @link InitialConditionsEntryMethod NXOpen.CAE.ResponseSimulation.InitialConditionsEntryMethod @endlink is an alias for @link InitialConditions.EntryMethod NXOpen.CAE.ResponseSimulation.InitialConditions.EntryMethod@endlink
InitialConditionsEntryMethod = InitialConditions.EntryMethod


##  @link InitialConditionsType NXOpen.CAE.ResponseSimulation.InitialConditionsType @endlink is an alias for @link InitialConditions.Type NXOpen.CAE.ResponseSimulation.InitialConditions.Type@endlink
InitialConditionsType = InitialConditions.Type


##  @link NodalFunctionExcitationType NXOpen.CAE.ResponseSimulation.NodalFunctionExcitationType @endlink is an alias for @link NodalFunctionExcitation.Type NXOpen.CAE.ResponseSimulation.NodalFunctionExcitation.Type@endlink
NodalFunctionExcitationType = NodalFunctionExcitation.Type


##  @link RSEventSolverParametersDdamCoefficientType NXOpen.CAE.ResponseSimulation.RSEventSolverParametersDdamCoefficientType @endlink is an alias for @link RSEventSolverParameters.DdamCoefficientType NXOpen.CAE.ResponseSimulation.RSEventSolverParameters.DdamCoefficientType@endlink
RSEventSolverParametersDdamCoefficientType = RSEventSolverParameters.DdamCoefficientType


##  @link RSEventAnalysisType NXOpen.CAE.ResponseSimulation.RSEventAnalysisType @endlink is an alias for @link RSEvent.AnalysisType NXOpen.CAE.ResponseSimulation.RSEvent.AnalysisType@endlink
RSEventAnalysisType = RSEvent.AnalysisType


##  @link RSEventConfidenceLevelOption NXOpen.CAE.ResponseSimulation.RSEventConfidenceLevelOption @endlink is an alias for @link RSEvent.ConfidenceLevelOption NXOpen.CAE.ResponseSimulation.RSEvent.ConfidenceLevelOption@endlink
RSEventConfidenceLevelOption = RSEvent.ConfidenceLevelOption


##  @link RSEventDdamFormulationType NXOpen.CAE.ResponseSimulation.RSEventDdamFormulationType @endlink is an alias for @link RSEvent.DdamFormulationType NXOpen.CAE.ResponseSimulation.RSEvent.DdamFormulationType@endlink
RSEventDdamFormulationType = RSEvent.DdamFormulationType


##  @link RSEventDurationOption NXOpen.CAE.ResponseSimulation.RSEventDurationOption @endlink is an alias for @link RSEvent.DurationOption NXOpen.CAE.ResponseSimulation.RSEvent.DurationOption@endlink
RSEventDurationOption = RSEvent.DurationOption


##  @link RSEventInterpolationMethod NXOpen.CAE.ResponseSimulation.RSEventInterpolationMethod @endlink is an alias for @link RSEvent.InterpolationMethod NXOpen.CAE.ResponseSimulation.RSEvent.InterpolationMethod@endlink
RSEventInterpolationMethod = RSEvent.InterpolationMethod


##  @link RSEventReferenceType NXOpen.CAE.ResponseSimulation.RSEventReferenceType @endlink is an alias for @link RSEvent.ReferenceType NXOpen.CAE.ResponseSimulation.RSEvent.ReferenceType@endlink
RSEventReferenceType = RSEvent.ReferenceType


##  @link RSEventResultFileType NXOpen.CAE.ResponseSimulation.RSEventResultFileType @endlink is an alias for @link RSEvent.ResultFileType NXOpen.CAE.ResponseSimulation.RSEvent.ResultFileType@endlink
RSEventResultFileType = RSEvent.ResultFileType


##  @link RSEventSpacingType NXOpen.CAE.ResponseSimulation.RSEventSpacingType @endlink is an alias for @link RSEvent.SpacingType NXOpen.CAE.ResponseSimulation.RSEvent.SpacingType@endlink
RSEventSpacingType = RSEvent.SpacingType


##  @link RSEventType NXOpen.CAE.ResponseSimulation.RSEventType @endlink is an alias for @link RSEvent.Type NXOpen.CAE.ResponseSimulation.RSEvent.Type@endlink
RSEventType = RSEvent.Type


##  @link TranslationalNodalFunctionExcitationBuilderRotationAxisType NXOpen.CAE.ResponseSimulation.TranslationalNodalFunctionExcitationBuilderRotationAxisType @endlink is an alias for @link TranslationalNodalFunctionExcitationBuilder.RotationAxisType NXOpen.CAE.ResponseSimulation.TranslationalNodalFunctionExcitationBuilder.RotationAxisType@endlink
TranslationalNodalFunctionExcitationBuilderRotationAxisType = TranslationalNodalFunctionExcitationBuilder.RotationAxisType


##  @link TransmissibilityEvaluationSettingBuilderMotionType NXOpen.CAE.ResponseSimulation.TransmissibilityEvaluationSettingBuilderMotionType @endlink is an alias for @link TransmissibilityEvaluationSettingBuilder.MotionType NXOpen.CAE.ResponseSimulation.TransmissibilityEvaluationSettingBuilder.MotionType@endlink
TransmissibilityEvaluationSettingBuilderMotionType = TransmissibilityEvaluationSettingBuilder.MotionType


##  @link VelocityImpactDirectionDirectionType NXOpen.CAE.ResponseSimulation.VelocityImpactDirectionDirectionType @endlink is an alias for @link VelocityImpactDirection.DirectionType NXOpen.CAE.ResponseSimulation.VelocityImpactDirection.DirectionType@endlink
VelocityImpactDirectionDirectionType = VelocityImpactDirection.DirectionType


##  @link VelocityImpactDirectionNodalComponentType NXOpen.CAE.ResponseSimulation.VelocityImpactDirectionNodalComponentType @endlink is an alias for @link VelocityImpactDirection.NodalComponentType NXOpen.CAE.ResponseSimulation.VelocityImpactDirection.NodalComponentType@endlink
VelocityImpactDirectionNodalComponentType = VelocityImpactDirection.NodalComponentType


##  @link VelocityImpactExcitationBuilderImpactMethodType NXOpen.CAE.ResponseSimulation.VelocityImpactExcitationBuilderImpactMethodType @endlink is an alias for @link VelocityImpactExcitationBuilder.ImpactMethodType NXOpen.CAE.ResponseSimulation.VelocityImpactExcitationBuilder.ImpactMethodType@endlink
VelocityImpactExcitationBuilderImpactMethodType = VelocityImpactExcitationBuilder.ImpactMethodType


##  @link VelocityImpactParametersStartPositionType NXOpen.CAE.ResponseSimulation.VelocityImpactParametersStartPositionType @endlink is an alias for @link VelocityImpactParameters.StartPositionType NXOpen.CAE.ResponseSimulation.VelocityImpactParameters.StartPositionType@endlink
VelocityImpactParametersStartPositionType = VelocityImpactParameters.StartPositionType


