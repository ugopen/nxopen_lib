from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents a @link DSEDesignWorkflow::DesignWorkflowBuilder DSEDesignWorkflow::DesignWorkflowBuilder@endlink  class object. <br> To create a new instance of this class, use @link NXOpen::DSEDesignWorkflow::DesignWorkflowCollection::CreateDesignWorkflowBuilder  NXOpen::DSEDesignWorkflow::DesignWorkflowCollection::CreateDesignWorkflowBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class DesignWorkflowBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>DSEDesignWorkflow.DesignWorkflowBuilder</ja_class> class object."""


    ##  Represents different options to select workflow part.
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## WorkPart</term><description> 
    ## </description> </item><item><term> 
    ## SpecifiedPart</term><description> 
    ## </description> </item></list>
    class WorkflowPartType(Enum):
        """
        Members Include: <WorkPart> <SpecifiedPart>
        """
        WorkPart: int
        SpecifiedPart: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DesignWorkflowBuilder.WorkflowPartType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) WorkflowPart
    ##  Returns the source part occurrence   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def WorkflowPart(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) WorkflowPart
         Returns the source part occurrence   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) WorkflowPart

    ##  Returns the source part occurrence   
    ##     
    ##  
    ## Setter License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @WorkflowPart.setter
    def WorkflowPart(self, workflowPart: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) WorkflowPart
         Returns the source part occurrence   
            
         
        """
        pass
    
    ## Getter for property: (@link DesignWorkflowBuilder.WorkflowPartType NXOpen.DSEDesignWorkflow.DesignWorkflowBuilder.WorkflowPartType@endlink) WorkflowPartReference
    ##  Returns the workflow part selection option type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return DesignWorkflowBuilder.WorkflowPartType
    @property
    def WorkflowPartReference(self) -> DesignWorkflowBuilder.WorkflowPartType:
        """
        Getter for property: (@link DesignWorkflowBuilder.WorkflowPartType NXOpen.DSEDesignWorkflow.DesignWorkflowBuilder.WorkflowPartType@endlink) WorkflowPartReference
         Returns the workflow part selection option type   
            
         
        """
        pass
    
    ## Setter for property: (@link DesignWorkflowBuilder.WorkflowPartType NXOpen.DSEDesignWorkflow.DesignWorkflowBuilder.WorkflowPartType@endlink) WorkflowPartReference

    ##  Returns the workflow part selection option type   
    ##     
    ##  
    ## Setter License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @WorkflowPartReference.setter
    def WorkflowPartReference(self, workflowReference: DesignWorkflowBuilder.WorkflowPartType):
        """
        Setter for property: (@link DesignWorkflowBuilder.WorkflowPartType NXOpen.DSEDesignWorkflow.DesignWorkflowBuilder.WorkflowPartType@endlink) WorkflowPartReference
         Returns the workflow part selection option type   
            
         
        """
        pass
    
import NXOpen
##  Represents a collection of @link NXOpen::DSEDesignWorkflow::DesignWorkflow NXOpen::DSEDesignWorkflow::DesignWorkflow@endlink  objects.  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class DesignWorkflowCollection(NXOpen.Object): 
    """ Represents a collection of <ja_class>NXOpen.DSEDesignWorkflow.DesignWorkflow</ja_class> objects. """


    ##  Creates a @link DSEDesignWorkflow::DesignWorkflowBuilder DSEDesignWorkflow::DesignWorkflowBuilder@endlink  
    ##  @return builder (@link DesignWorkflowBuilder NXOpen.DSEDesignWorkflow.DesignWorkflowBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="desWorkflow"> (@link DesignWorkflow NXOpen.DSEDesignWorkflow.DesignWorkflow@endlink) </param>
    def CreateDesignWorkflowBuilder(part: NXOpen.Part, desWorkflow: DesignWorkflow) -> DesignWorkflowBuilder:
        """
         Creates a @link DSEDesignWorkflow::DesignWorkflowBuilder DSEDesignWorkflow::DesignWorkflowBuilder@endlink  
         @return builder (@link DesignWorkflowBuilder NXOpen.DSEDesignWorkflow.DesignWorkflowBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link DSEDesignWorkflow::PerformancePredictorWorkflowBuilder DSEDesignWorkflow::PerformancePredictorWorkflowBuilder@endlink  
    ##  @return builder (@link PerformancePredictorWorkflowBuilder NXOpen.DSEDesignWorkflow.PerformancePredictorWorkflowBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="desWorkflow"> (@link PerformancePredictorWorkflow NXOpen.DSEDesignWorkflow.PerformancePredictorWorkflow@endlink) </param>
    def CreatePerformancePredictorWorkflowBuilder(part: NXOpen.Part, desWorkflow: PerformancePredictorWorkflow) -> PerformancePredictorWorkflowBuilder:
        """
         Creates a @link DSEDesignWorkflow::PerformancePredictorWorkflowBuilder DSEDesignWorkflow::PerformancePredictorWorkflowBuilder@endlink  
         @return builder (@link PerformancePredictorWorkflowBuilder NXOpen.DSEDesignWorkflow.PerformancePredictorWorkflowBuilder@endlink): .
        """
        pass
    
import NXOpen.DSEPlatform
##  Represents a @link DSEDesignWorkflow::DesignWorkflow DSEDesignWorkflow::DesignWorkflow@endlink  class object. <br> To create or edit an instance of this class, use @link NXOpen::DSEDesignWorkflow::DesignWorkflowBuilder  NXOpen::DSEDesignWorkflow::DesignWorkflowBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class DesignWorkflow(NXOpen.DSEPlatform.OptimizationWorkflow): 
    """ Represents a <ja_class>DSEDesignWorkflow.DesignWorkflow</ja_class> class object."""
    pass


import NXOpen
import NXOpen.DesignSimulation
##  Represents a @link DSEDesignWorkflow::PerformancePredictorWorkflowBuilder DSEDesignWorkflow::PerformancePredictorWorkflowBuilder@endlink  class object. <br> To create a new instance of this class, use @link NXOpen::DSEDesignWorkflow::DesignWorkflowCollection::CreatePerformancePredictorWorkflowBuilder  NXOpen::DSEDesignWorkflow::DesignWorkflowCollection::CreatePerformancePredictorWorkflowBuilder @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class PerformancePredictorWorkflowBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>DSEDesignWorkflow.PerformancePredictorWorkflowBuilder</ja_class> class object."""


    ## Getter for property: (@link DesignWorkflowBuilder NXOpen.DSEDesignWorkflow.DesignWorkflowBuilder@endlink) DesignWorkflow
    ##  Returns the design workflow builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return DesignWorkflowBuilder
    @property
    def DesignWorkflow(self) -> DesignWorkflowBuilder:
        """
        Getter for property: (@link DesignWorkflowBuilder NXOpen.DSEDesignWorkflow.DesignWorkflowBuilder@endlink) DesignWorkflow
         Returns the design workflow builder   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.DesignSimulation.Study NXOpen.DesignSimulation.Study@endlink) PerformancePredictorStudy
    ##  Returns the Performance Predictor study  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.DesignSimulation.Study
    @property
    def PerformancePredictorStudy(self) -> NXOpen.DesignSimulation.Study:
        """
        Getter for property: (@link NXOpen.DesignSimulation.Study NXOpen.DesignSimulation.Study@endlink) PerformancePredictorStudy
         Returns the Performance Predictor study  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.DesignSimulation.Study NXOpen.DesignSimulation.Study@endlink) PerformancePredictorStudy

    ##  Returns the Performance Predictor study  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @PerformancePredictorStudy.setter
    def PerformancePredictorStudy(self, study: NXOpen.DesignSimulation.Study):
        """
        Setter for property: (@link NXOpen.DesignSimulation.Study NXOpen.DesignSimulation.Study@endlink) PerformancePredictorStudy
         Returns the Performance Predictor study  
            
         
        """
        pass
    
    ## Getter for property: (int) StudyIndex
    ##  Returns the Performance Predictor study index  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return int
    @property
    def StudyIndex(self) -> int:
        """
        Getter for property: (int) StudyIndex
         Returns the Performance Predictor study index  
            
         
        """
        pass
    
    ## Setter for property: (int) StudyIndex

    ##  Returns the Performance Predictor study index  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @StudyIndex.setter
    def StudyIndex(self, studyIndex: int):
        """
        Setter for property: (int) StudyIndex
         Returns the Performance Predictor study index  
            
         
        """
        pass
    
##  Represents a @link DSEDesignWorkflow::PerformancePredictorWorkflow DSEDesignWorkflow::PerformancePredictorWorkflow@endlink  class object. <br> To create or edit an instance of this class, use @link NXOpen::DSEDesignWorkflow::PerformancePredictorWorkflowBuilder  NXOpen::DSEDesignWorkflow::PerformancePredictorWorkflowBuilder @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class PerformancePredictorWorkflow(DesignWorkflow): 
    """ Represents a <ja_class>DSEDesignWorkflow.PerformancePredictorWorkflow</ja_class> class object."""
    pass


## @package NXOpen.DSEDesignWorkflow
## Classes, Enums and Structs under NXOpen.DSEDesignWorkflow namespace

##  @link DesignWorkflowBuilderWorkflowPartType NXOpen.DSEDesignWorkflow.DesignWorkflowBuilderWorkflowPartType @endlink is an alias for @link DesignWorkflowBuilder.WorkflowPartType NXOpen.DSEDesignWorkflow.DesignWorkflowBuilder.WorkflowPartType@endlink
DesignWorkflowBuilderWorkflowPartType = DesignWorkflowBuilder.WorkflowPartType


