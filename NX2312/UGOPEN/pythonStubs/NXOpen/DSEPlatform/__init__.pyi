from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents a @link DSEPlatform::ExplorationStudy DSEPlatform::ExplorationStudy@endlink  object. <br> This is an abstract class and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ExplorationStudy(NXOpen.NXObject): 
    """ Represents a <ja_class>DSEPlatform.ExplorationStudy</ja_class> object."""
    pass


import NXOpen
##  Represents a @link DSEPlatform::OptimizationWorkflow DSEPlatform::OptimizationWorkflow@endlink  object. <br> This is an abstract class and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class OptimizationWorkflow(NXOpen.NXObject): 
    """ Represents a <ja_class>DSEPlatform.OptimizationWorkflow</ja_class> object."""
    pass


import NXOpen
##  Represents the Design Space Explorer Study Manager class. <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class StudyManager(NXOpen.Object): 
    """ Represents the Design Space Explorer Study Manager class."""


    ##  Set design workflow on optimization study
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_design_explorer (" NX Design Space Exploration")
    ## <param name="study"> (@link ExplorationStudy NXOpen.DSEPlatform.ExplorationStudy@endlink) </param>
    ## <param name="workflow"> (@link OptimizationWorkflow NXOpen.DSEPlatform.OptimizationWorkflow@endlink) </param>
    def AddWorkflow(study: ExplorationStudy, workflow: OptimizationWorkflow) -> None:
        """
         Set design workflow on optimization study
        """
        pass
    
    ##  Get the active study in the part.
    ##  @return activeStudy (@link ExplorationStudy NXOpen.DSEPlatform.ExplorationStudy@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.BasePart NXOpen.BasePart@endlink) </param>
    @staticmethod
    def GetActiveStudy(part: NXOpen.BasePart) -> ExplorationStudy:
        """
         Get the active study in the part.
         @return activeStudy (@link ExplorationStudy NXOpen.DSEPlatform.ExplorationStudy@endlink): .
        """
        pass
    
    ##  Get the number of studies in the part 
    ##  @return numStudies (int): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.BasePart NXOpen.BasePart@endlink) </param>
    @staticmethod
    def GetNumberOfStudies(part: NXOpen.BasePart) -> int:
        """
         Get the number of studies in the part 
         @return numStudies (int): .
        """
        pass
    
    ##  Get the study at index in the part 
    ##  @return study (@link ExplorationStudy NXOpen.DSEPlatform.ExplorationStudy@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.BasePart NXOpen.BasePart@endlink) </param>
    ## <param name="index"> (int) </param>
    def GetStudyAtIndex(part: NXOpen.BasePart, index: int) -> ExplorationStudy:
        """
         Get the study at index in the part 
         @return study (@link ExplorationStudy NXOpen.DSEPlatform.ExplorationStudy@endlink): .
        """
        pass
    
    ##  Retrieve the workflow on the optimization study
    ##  @return workflow (@link OptimizationWorkflow NXOpen.DSEPlatform.OptimizationWorkflow@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## <param name="study"> (@link ExplorationStudy NXOpen.DSEPlatform.ExplorationStudy@endlink) </param>
    @staticmethod
    def GetWorkflow(study: ExplorationStudy) -> OptimizationWorkflow:
        """
         Retrieve the workflow on the optimization study
         @return workflow (@link OptimizationWorkflow NXOpen.DSEPlatform.OptimizationWorkflow@endlink): .
        """
        pass
    
    ##  Load the workflow part
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_design_explorer (" NX Design Space Exploration")
    ## <param name="workflow"> (@link OptimizationWorkflow NXOpen.DSEPlatform.OptimizationWorkflow@endlink) </param>
    @staticmethod
    def LoadWorkflowPart(workflow: OptimizationWorkflow) -> None:
        """
         Load the workflow part
        """
        pass
    
    ##  Set the active study in the part.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_design_explorer (" NX Design Space Exploration")
    ## <param name="part"> (@link NXOpen.BasePart NXOpen.BasePart@endlink) </param>
    ## <param name="activeStudy"> (@link ExplorationStudy NXOpen.DSEPlatform.ExplorationStudy@endlink) </param>
    def SetActiveStudy(part: NXOpen.BasePart, activeStudy: ExplorationStudy) -> None:
        """
         Set the active study in the part.
        """
        pass
    
import NXOpen
##  Represents Valid Object Value class  <br> This object cannot be created  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ValidObjectValue(NXOpen.TaggedObject): 
    """ Represents Valid Object Value class """
    pass


## @package NXOpen.DSEPlatform
## Classes, Enums and Structs under NXOpen.DSEPlatform namespace

