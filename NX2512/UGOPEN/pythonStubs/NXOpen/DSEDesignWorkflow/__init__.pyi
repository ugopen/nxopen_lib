from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class DesignWorkflowBuilder(NXOpen.Builder): 
    """ Represents a DSEDesignWorkflow.DesignWorkflowBuilder class object."""
    class WorkflowPartType(Enum):
        """
        Members Include: 
         |WorkPart| 
         |SpecifiedPart| 

        """
        WorkPart: int
        SpecifiedPart: int
        @staticmethod
        def ValueOf(value: int) -> DesignWorkflowBuilder.WorkflowPartType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def WorkflowPart(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) WorkflowPart
         Returns the source part occurrence   
            
         
        """
        pass
    @WorkflowPart.setter
    def WorkflowPart(self, workflowPart: NXOpen.TaggedObject):
        """
        Setter for property: ( NXOpen.TaggedObject) WorkflowPart
         Returns the source part occurrence   
            
         
        """
        pass
    @property
    def WorkflowPartReference(self) -> DesignWorkflowBuilder.WorkflowPartType:
        """
        Getter for property: ( DesignWorkflowBuilder.WorkflowPartType NXOpen.DSED) WorkflowPartReference
         Returns the workflow part selection option type   
            
         
        """
        pass
    @WorkflowPartReference.setter
    def WorkflowPartReference(self, workflowReference: DesignWorkflowBuilder.WorkflowPartType):
        """
        Setter for property: ( DesignWorkflowBuilder.WorkflowPartType NXOpen.DSED) WorkflowPartReference
         Returns the workflow part selection option type   
            
         
        """
        pass
import NXOpen
class DesignWorkflowCollection(NXOpen.Object): 
    """ Represents a collection of NXOpen.DSEDesignWorkflow.DesignWorkflow objects. """
    def CreateDesignWorkflowBuilder(part: NXOpen.Part, desWorkflow: DesignWorkflow) -> DesignWorkflowBuilder:
        """
         Creates a DSEDesignWorkflow.DesignWorkflowBuilder 
         Returns builder ( DesignWorkflowBuilder NXOpen.DSED): .
        """
        pass
    def CreatePerformancePredictorWorkflowBuilder(part: NXOpen.Part, desWorkflow: PerformancePredictorWorkflow) -> PerformancePredictorWorkflowBuilder:
        """
         Creates a DSEDesignWorkflow.PerformancePredictorWorkflowBuilder 
         Returns builder ( PerformancePredictorWorkflowBuilder NXOpen.DSED): .
        """
        pass
import NXOpen.DSEPlatform
class DesignWorkflow(NXOpen.DSEPlatform.OptimizationWorkflow): 
    """ Represents a DSEDesignWorkflow.DesignWorkflow class object."""
    pass
import NXOpen
import NXOpen.DesignSimulation
class PerformancePredictorWorkflowBuilder(NXOpen.Builder): 
    """ Represents a DSEDesignWorkflow.PerformancePredictorWorkflowBuilder class object."""
    @property
    def DesignWorkflow(self) -> DesignWorkflowBuilder:
        """
        Getter for property: ( DesignWorkflowBuilder NXOpen.DSED) DesignWorkflow
         Returns the design workflow builder   
            
         
        """
        pass
    @property
    def PerformancePredictorStudy(self) -> NXOpen.DesignSimulation.Study:
        """
        Getter for property: ( NXOpen.DesignSimulation.Study) PerformancePredictorStudy
         Returns the Performance Predictor study  
            
         
        """
        pass
    @PerformancePredictorStudy.setter
    def PerformancePredictorStudy(self, study: NXOpen.DesignSimulation.Study):
        """
        Setter for property: ( NXOpen.DesignSimulation.Study) PerformancePredictorStudy
         Returns the Performance Predictor study  
            
         
        """
        pass
    @property
    def StudyIndex(self) -> int:
        """
        Getter for property: (int) StudyIndex
         Returns the Performance Predictor study index  
            
         
        """
        pass
    @StudyIndex.setter
    def StudyIndex(self, studyIndex: int):
        """
        Setter for property: (int) StudyIndex
         Returns the Performance Predictor study index  
            
         
        """
        pass
class PerformancePredictorWorkflow(DesignWorkflow): 
    """ Represents a DSEDesignWorkflow.PerformancePredictorWorkflow class object."""
    pass
