from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class ExplorationStudy(NXOpen.NXObject): 
    """ Represents a DSEPlatform.ExplorationStudy object."""
    pass
import NXOpen
class OptimizationWorkflow(NXOpen.NXObject): 
    """ Represents a DSEPlatform.OptimizationWorkflow object."""
    pass
import NXOpen
class StudyManager(NXOpen.Object): 
    """ Represents the Design Space Explorer Study Manager class."""
    def AddWorkflow(study: ExplorationStudy, workflow: OptimizationWorkflow) -> None:
        """
         Set design workflow on optimization study
        """
        pass
    def GetActiveStudy(part: NXOpen.BasePart) -> ExplorationStudy:
        """
         Get the active study in the part.
         Returns activeStudy ( ExplorationStudy NXOpen.D): .
        """
        pass
    def GetNumberOfStudies(part: NXOpen.BasePart) -> int:
        """
         Get the number of studies in the part 
         Returns numStudies (int): .
        """
        pass
    def GetStudyAtIndex(part: NXOpen.BasePart, index: int) -> ExplorationStudy:
        """
         Get the study at index in the part 
         Returns study ( ExplorationStudy NXOpen.D): .
        """
        pass
    def GetWorkflow(study: ExplorationStudy) -> OptimizationWorkflow:
        """
         Retrieve the workflow on the optimization study
         Returns workflow ( OptimizationWorkflow NXOpen.D): .
        """
        pass
    def LoadWorkflowPart(workflow: OptimizationWorkflow) -> None:
        """
         Load the workflow part
        """
        pass
    def SetActiveStudy(part: NXOpen.BasePart, activeStudy: ExplorationStudy) -> None:
        """
         Set the active study in the part.
        """
        pass
import NXOpen
class ValidObjectValue(NXOpen.TaggedObject): 
    """ Represents Valid Object Value class """
    pass
