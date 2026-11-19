from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.CAE
##   Represents Optimization Simulation Workflow Builder.   <br> To create a new instance of this class, use @link NXOpen::CaeDseWorkflow::SimulationWorkflowCollection::CreateWorkflowBuilder  NXOpen::CaeDseWorkflow::SimulationWorkflowCollection::CreateWorkflowBuilder @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class SimulationWorkflowBuilder(NXOpen.Builder): 
    """  Represents Optimization Simulation Workflow Builder.  """


    ##  Used to specify the CAE category types to be filtered out for @link CaeDseWorkflow::SimulationWorkflow CaeDseWorkflow::SimulationWorkflow@endlink  design parameters. 
    ##  Physical parameter type 
    class FilterCategoryType(Enum):
        """
        Members Include: <Physical> <Section> <ModelingObject> <Region> <Mesh> <ResultMeasure> <ResultProbe>
        """
        Physical: int
        Section: int
        ModelingObject: int
        Region: int
        Mesh: int
        ResultMeasure: int
        ResultProbe: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SimulationWorkflowBuilder.FilterCategoryType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Used to specify the file types to be filtered out for @link CaeDseWorkflow::SimulationWorkflow CaeDseWorkflow::SimulationWorkflow@endlink  design parameters. 
    ##  CAE Simulation part type 
    class FilterFileType(Enum):
        """
        Members Include: <Sim> <Afem> <Fem> <Ideal> <Cad>
        """
        Sim: int
        Afem: int
        Fem: int
        Ideal: int
        Cad: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SimulationWorkflowBuilder.FilterFileType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Returns the category types that were filtered out for workflow design parameters.  
    ##  @return catTypes (@link SimulationWorkflowBuilder.FilterCategoryType List[NXOpen.CaeDseWorkflow.SimulationWorkflowBuilder.FilterCategoryType]@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetFilteredCategoryTypes(builder: SimulationWorkflowBuilder) -> List[SimulationWorkflowBuilder.FilterCategoryType]:
        """
         Returns the category types that were filtered out for workflow design parameters.  
         @return catTypes (@link SimulationWorkflowBuilder.FilterCategoryType List[NXOpen.CaeDseWorkflow.SimulationWorkflowBuilder.FilterCategoryType]@endlink): .
        """
        pass
    
    ##  Returns the file types that were filtered out for workflow design parameters.  
    ##  @return fileTypes (@link SimulationWorkflowBuilder.FilterFileType List[NXOpen.CaeDseWorkflow.SimulationWorkflowBuilder.FilterFileType]@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetFilteredFileTypes(builder: SimulationWorkflowBuilder) -> List[SimulationWorkflowBuilder.FilterFileType]:
        """
         Returns the file types that were filtered out for workflow design parameters.  
         @return fileTypes (@link SimulationWorkflowBuilder.FilterFileType List[NXOpen.CaeDseWorkflow.SimulationWorkflowBuilder.FilterFileType]@endlink): .
        """
        pass
    
    ##  Returns the simulation workflow name.  
    ##  @return name (str):  Simulation Workflow name .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetName(builder: SimulationWorkflowBuilder) -> str:
        """
         Returns the simulation workflow name.  
         @return name (str):  Simulation Workflow name .
        """
        pass
    
    ##  Returns the post-solve journal file name.  
    ##  @return name (str):  Post-solve Journal name .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPostsolveJournalName(builder: SimulationWorkflowBuilder) -> str:
        """
         Returns the post-solve journal file name.  
         @return name (str):  Post-solve Journal name .
        """
        pass
    
    ##  Returns the pre-solve journal file name.  
    ##  @return name (str):  Pre-solve Journal name .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPresolveJournalName(builder: SimulationWorkflowBuilder) -> str:
        """
         Returns the pre-solve journal file name.  
         @return name (str):  Pre-solve Journal name .
        """
        pass
    
    ##  Returns the simulation part. 
    ##  @return sim (@link NXOpen.CAE.SimSimulation NXOpen.CAE.SimSimulation@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSimulation(builder: SimulationWorkflowBuilder) -> NXOpen.CAE.SimSimulation:
        """
         Returns the simulation part. 
         @return sim (@link NXOpen.CAE.SimSimulation NXOpen.CAE.SimSimulation@endlink): .
        """
        pass
    
    ##  Returns the ordered set of solutions. 
    ##  @return solutions (@link NXOpen.CAE.SimSolution List[NXOpen.CAE.SimSolution]@endlink):  .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSolutions(builder: SimulationWorkflowBuilder) -> List[NXOpen.CAE.SimSolution]:
        """
         Returns the ordered set of solutions. 
         @return solutions (@link NXOpen.CAE.SimSolution List[NXOpen.CAE.SimSolution]@endlink):  .
        """
        pass
    
    ##  Returns the workflow.  
    ##  @return workflow (@link SimulationWorkflow NXOpen.CaeDseWorkflow.SimulationWorkflow@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetWorkflow(builder: SimulationWorkflowBuilder) -> SimulationWorkflow:
        """
         Returns the workflow.  
         @return workflow (@link SimulationWorkflow NXOpen.CaeDseWorkflow.SimulationWorkflow@endlink): .
        """
        pass
    
    ##  Sets the category types to be filtered out for workflow design parameters.  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: sc_design_explorer (" Simulation Worfkflow for Design Space Explorer")
    ## 
    ## <param name="catTypes"> (@link SimulationWorkflowBuilder.FilterCategoryType List[NXOpen.CaeDseWorkflow.SimulationWorkflowBuilder.FilterCategoryType]@endlink) </param>
    def SetFilteredCategoryTypes(builder: SimulationWorkflowBuilder, catTypes: List[SimulationWorkflowBuilder.FilterCategoryType]) -> None:
        """
         Sets the category types to be filtered out for workflow design parameters.  
        """
        pass
    
    ##  Sets the file types to be filtered out for workflow design parameters.  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: sc_design_explorer (" Simulation Worfkflow for Design Space Explorer")
    ## 
    ## <param name="fileTypes"> (@link SimulationWorkflowBuilder.FilterFileType List[NXOpen.CaeDseWorkflow.SimulationWorkflowBuilder.FilterFileType]@endlink) </param>
    def SetFilteredFileTypes(builder: SimulationWorkflowBuilder, fileTypes: List[SimulationWorkflowBuilder.FilterFileType]) -> None:
        """
         Sets the file types to be filtered out for workflow design parameters.  
        """
        pass
    
    ##  Sets the simulation workflow name.  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: sc_design_explorer (" Simulation Worfkflow for Design Space Explorer")
    ##  Simulation Workflow name 
    def SetName(builder: SimulationWorkflowBuilder, name: str) -> None:
        """
         Sets the simulation workflow name.  
        """
        pass
    
    ##  Sets the post-solve journal file name.  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: sc_design_explorer (" Simulation Worfkflow for Design Space Explorer")
    ##  Post-solve Journal name 
    def SetPostsolveJournalName(builder: SimulationWorkflowBuilder, name: str) -> None:
        """
         Sets the post-solve journal file name.  
        """
        pass
    
    ##  Sets the pre-solve journal file name.  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: sc_design_explorer (" Simulation Worfkflow for Design Space Explorer")
    ##  Pre-solve Journal name 
    def SetPresolveJournalName(builder: SimulationWorkflowBuilder, name: str) -> None:
        """
         Sets the pre-solve journal file name.  
        """
        pass
    
    ##  Sets the simulation part.  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: sc_design_explorer (" Simulation Worfkflow for Design Space Explorer")
    ## 
    ## <param name="sim"> (@link NXOpen.CAE.SimSimulation NXOpen.CAE.SimSimulation@endlink) </param>
    def SetSimulation(builder: SimulationWorkflowBuilder, sim: NXOpen.CAE.SimSimulation) -> None:
        """
         Sets the simulation part.  
        """
        pass
    
    ##  Sets the ordered set of solutions. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: sc_design_explorer (" Simulation Worfkflow for Design Space Explorer")
    ##   
    def SetSolutions(builder: SimulationWorkflowBuilder, solutions: List[NXOpen.CAE.SimSolution]) -> None:
        """
         Sets the ordered set of solutions. 
        """
        pass
    
    ##  Sets the workflow.  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: sc_design_explorer (" Simulation Worfkflow for Design Space Explorer")
    ## 
    ## <param name="workflow"> (@link SimulationWorkflow NXOpen.CaeDseWorkflow.SimulationWorkflow@endlink) </param>
    def SetWorkflow(builder: SimulationWorkflowBuilder, workflow: SimulationWorkflow) -> None:
        """
         Sets the workflow.  
        """
        pass
    
import NXOpen
##  Represents a collection of @link NXOpen::CaeDseWorkflow::SimulationWorkflow NXOpen::CaeDseWorkflow::SimulationWorkflow@endlink  objects.  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class SimulationWorkflowCollection(NXOpen.Object): 
    """ Represents a collection of <ja_class>NXOpen.CaeDseWorkflow.SimulationWorkflow</ja_class> objects. """


    ##  Creates a @link CaeDseWorkflow::SimulationWorkflowBuilder CaeDseWorkflow::SimulationWorkflowBuilder@endlink  
    ##  @return builder (@link SimulationWorkflowBuilder NXOpen.CaeDseWorkflow.SimulationWorkflowBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: sc_design_explorer (" Simulation Worfkflow for Design Space Explorer")
    ## <param name="part"> (@link NXOpen.BasePart NXOpen.BasePart@endlink) </param>
    ## <param name="workflow"> (@link SimulationWorkflow NXOpen.CaeDseWorkflow.SimulationWorkflow@endlink) </param>
    def CreateEditWorkflowBuilder(part: NXOpen.BasePart, workflow: SimulationWorkflow) -> SimulationWorkflowBuilder:
        """
         Creates a @link CaeDseWorkflow::SimulationWorkflowBuilder CaeDseWorkflow::SimulationWorkflowBuilder@endlink  
         @return builder (@link SimulationWorkflowBuilder NXOpen.CaeDseWorkflow.SimulationWorkflowBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link CaeDseWorkflow::SimulationWorkflowBuilder CaeDseWorkflow::SimulationWorkflowBuilder@endlink  
    ##  @return builder (@link SimulationWorkflowBuilder NXOpen.CaeDseWorkflow.SimulationWorkflowBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: sc_design_explorer (" Simulation Worfkflow for Design Space Explorer")
    ## <param name="part"> (@link NXOpen.BasePart NXOpen.BasePart@endlink) </param>
    def CreateWorkflowBuilder(part: NXOpen.BasePart) -> SimulationWorkflowBuilder:
        """
         Creates a @link CaeDseWorkflow::SimulationWorkflowBuilder CaeDseWorkflow::SimulationWorkflowBuilder@endlink  
         @return builder (@link SimulationWorkflowBuilder NXOpen.CaeDseWorkflow.SimulationWorkflowBuilder@endlink): .
        """
        pass
    
import NXOpen.DSEPlatform
##  Represents a @link CaeDseWorkflow::SimulationWorkflow CaeDseWorkflow::SimulationWorkflow@endlink  class object. <br> To create or edit an instance of this class, use @link NXOpen::CaeDseWorkflow::SimulationWorkflowBuilder  NXOpen::CaeDseWorkflow::SimulationWorkflowBuilder @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class SimulationWorkflow(NXOpen.DSEPlatform.OptimizationWorkflow): 
    """ Represents a <ja_class>CaeDseWorkflow.SimulationWorkflow</ja_class> class object."""
    pass


## @package NXOpen.CaeDseWorkflow
## Classes, Enums and Structs under NXOpen.CaeDseWorkflow namespace

##  @link SimulationWorkflowBuilderFilterCategoryType NXOpen.CaeDseWorkflow.SimulationWorkflowBuilderFilterCategoryType @endlink is an alias for @link SimulationWorkflowBuilder.FilterCategoryType NXOpen.CaeDseWorkflow.SimulationWorkflowBuilder.FilterCategoryType@endlink
SimulationWorkflowBuilderFilterCategoryType = SimulationWorkflowBuilder.FilterCategoryType


##  @link SimulationWorkflowBuilderFilterFileType NXOpen.CaeDseWorkflow.SimulationWorkflowBuilderFilterFileType @endlink is an alias for @link SimulationWorkflowBuilder.FilterFileType NXOpen.CaeDseWorkflow.SimulationWorkflowBuilder.FilterFileType@endlink
SimulationWorkflowBuilderFilterFileType = SimulationWorkflowBuilder.FilterFileType


