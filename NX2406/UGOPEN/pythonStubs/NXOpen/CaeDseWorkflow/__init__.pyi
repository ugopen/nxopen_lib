from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
##  Represents a @link CaeDseWorkflow::FEMassResponse CaeDseWorkflow::FEMassResponse@endlink  object. <br> To create a new instance of this class, use @link NXOpen::CaeDseWorkflow::SimulationWorkflow::GetFEMassResponse  NXOpen::CaeDseWorkflow::SimulationWorkflow::GetFEMassResponse @endlink  <br> 
## 
##   <br>  Created in NX2406.0.0  <br> 

class FEMassResponse(Response): 
    """ Represents a <ja_class>CaeDseWorkflow.FEMassResponse</ja_class> object."""
    pass


##  Represents a @link CaeDseWorkflow::FEVolumeResponse CaeDseWorkflow::FEVolumeResponse@endlink  object. <br> To create a new instance of this class, use @link NXOpen::CaeDseWorkflow::SimulationWorkflow::GetFEVolumeResponse  NXOpen::CaeDseWorkflow::SimulationWorkflow::GetFEVolumeResponse @endlink  <br> 
## 
##   <br>  Created in NX2406.0.0  <br> 

class FEVolumeResponse(Response): 
    """ Represents a <ja_class>CaeDseWorkflow.FEVolumeResponse</ja_class> object."""
    pass


##  Represents a @link CaeDseWorkflow::FEWeightResponse CaeDseWorkflow::FEWeightResponse@endlink  object. <br> To create a new instance of this class, use @link NXOpen::CaeDseWorkflow::SimulationWorkflow::GetFEWeightResponse  NXOpen::CaeDseWorkflow::SimulationWorkflow::GetFEWeightResponse @endlink  <br> 
## 
##   <br>  Created in NX2406.0.0  <br> 

class FEWeightResponse(Response): 
    """ Represents a <ja_class>CaeDseWorkflow.FEWeightResponse</ja_class> object."""
    pass


import NXOpen
##  Represents a @link CaeDseWorkflow::Response CaeDseWorkflow::Response@endlink  object. <br> This is an abstract class and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX2406.0.0  <br> 

class Response(NXOpen.NXObject): 
    """ Represents a <ja_class>CaeDseWorkflow.Response</ja_class> object."""
    pass


import NXOpen
import NXOpen.CAE
##   Represents Optimization Simulation Workflow Builder.   <br> To create a new instance of this class, use @link NXOpen::CaeDseWorkflow::SimulationWorkflowCollection::CreateWorkflowBuilder  NXOpen::CaeDseWorkflow::SimulationWorkflowCollection::CreateWorkflowBuilder @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class SimulationWorkflowBuilder(NXOpen.Builder): 
    """  Represents Optimization Simulation Workflow Builder.  """


    ##  Used to specify the CAE category types to be filtered out for @link CaeDseWorkflow::SimulationWorkflow CaeDseWorkflow::SimulationWorkflow@endlink  design parameters. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Physical</term><description> 
    ##  Physical parameter type </description> </item><item><term> 
    ## Section</term><description> 
    ##  1D Section parameter type </description> </item><item><term> 
    ## ModelingObject</term><description> 
    ##  Modeling Object parameter type </description> </item><item><term> 
    ## Region</term><description> 
    ##  Region parameter type </description> </item><item><term> 
    ## Mesh</term><description> 
    ##  Mesh parameter type </description> </item><item><term> 
    ## ResultMeasure</term><description> 
    ##  Result Measure parameter type </description> </item><item><term> 
    ## ResultProbe</term><description> 
    ##  Result Probe parameter type </description> </item><item><term> 
    ## MaterialOnBody</term><description> 
    ##  Material on body parameter type </description> </item><item><term> 
    ## LoadBoundaryCondition</term><description> 
    ##  Load/ Boundary Condition parameter type </description> </item></list>
    class FilterCategoryType(Enum):
        """
        Members Include: <Physical> <Section> <ModelingObject> <Region> <Mesh> <ResultMeasure> <ResultProbe> <MaterialOnBody> <LoadBoundaryCondition>
        """
        Physical: int
        Section: int
        ModelingObject: int
        Region: int
        Mesh: int
        ResultMeasure: int
        ResultProbe: int
        MaterialOnBody: int
        LoadBoundaryCondition: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SimulationWorkflowBuilder.FilterCategoryType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Used to specify the file types to be filtered out for @link CaeDseWorkflow::SimulationWorkflow CaeDseWorkflow::SimulationWorkflow@endlink  design parameters. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Sim</term><description> 
    ##  CAE Simulation part type </description> </item><item><term> 
    ## Afem</term><description> 
    ##  CAE Assembly Fem part type </description> </item><item><term> 
    ## Fem</term><description> 
    ##  CAE Fem part type </description> </item><item><term> 
    ## Ideal</term><description> 
    ##  CAE Idealize part type </description> </item><item><term> 
    ## Cad</term><description> 
    ##  CAD part type </description> </item></list>
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
    
    
    ##  Returns the association names used for filtering workflow design parameters in all parts.  
    ##  @return assocNames (List[str]): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    def GetFilteredAssociationNames(self) -> List[str]:
        """
         Returns the association names used for filtering workflow design parameters in all parts.  
         @return assocNames (List[str]): .
        """
        pass
    
    ##  Returns the association names with associated parts used for filtering workflow design parameters.  
    ##  @return A tuple consisting of (assocNames, assocParts). 
    ##  - assocNames is: List[str].
    ##  - assocParts is: @link NXOpen.BasePart List[NXOpen.BasePart]@endlink.

    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    def GetFilteredAssociationNamesWithAssociatedParts(self) -> Tuple[List[str], List[NXOpen.BasePart]]:
        """
         Returns the association names with associated parts used for filtering workflow design parameters.  
         @return A tuple consisting of (assocNames, assocParts). 
         - assocNames is: List[str].
         - assocParts is: @link NXOpen.BasePart List[NXOpen.BasePart]@endlink.

        """
        pass
    
    ##  Returns the category types that were filtered out for workflow design parameters.  
    ##  @return catTypes (@link SimulationWorkflowBuilder.FilterCategoryType List[NXOpen.CaeDseWorkflow.SimulationWorkflowBuilder.FilterCategoryType]@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def GetFilteredCategoryTypes(self) -> List[SimulationWorkflowBuilder.FilterCategoryType]:
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
    def GetFilteredFileTypes(self) -> List[SimulationWorkflowBuilder.FilterFileType]:
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
    def GetName(self) -> str:
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
    def GetPostsolveJournalName(self) -> str:
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
    def GetPresolveJournalName(self) -> str:
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
    def GetSimulation(self) -> NXOpen.CAE.SimSimulation:
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
    def GetSolutions(self) -> List[NXOpen.CAE.SimSolution]:
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
    def GetWorkflow(self) -> SimulationWorkflow:
        """
         Returns the workflow.  
         @return workflow (@link SimulationWorkflow NXOpen.CaeDseWorkflow.SimulationWorkflow@endlink): .
        """
        pass
    
    ##  Sets the association names to use for filtering workflow design parameters in all parts.  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: sc_design_explr_eval (" Simcenter 3D Design Space Exploration Evaluation Only")
    ## 
    ## <param name="assocNames"> (List[str]) </param>
    def SetFilteredAssociationNames(self, assocNames: List[str]) -> None:
        """
         Sets the association names to use for filtering workflow design parameters in all parts.  
        """
        pass
    
    ##  Sets the association names with associated parts to use for filtering workflow design parameters.  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: sc_design_explr_eval (" Simcenter 3D Design Space Exploration Evaluation Only")
    ## 
    ## <param name="assocParts"> (@link NXOpen.BasePart List[NXOpen.BasePart]@endlink) </param>
    ## <param name="assocNames"> (List[str]) </param>
    def SetFilteredAssociationNamesWithAssociatedParts(self, assocParts: List[NXOpen.BasePart], assocNames: List[str]) -> None:
        """
         Sets the association names with associated parts to use for filtering workflow design parameters.  
        """
        pass
    
    ##  Sets the category types to be filtered out for workflow design parameters.  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: sc_design_explr_eval (" Simcenter 3D Design Space Exploration Evaluation Only")
    ## 
    ## <param name="catTypes"> (@link SimulationWorkflowBuilder.FilterCategoryType List[NXOpen.CaeDseWorkflow.SimulationWorkflowBuilder.FilterCategoryType]@endlink) </param>
    def SetFilteredCategoryTypes(self, catTypes: List[SimulationWorkflowBuilder.FilterCategoryType]) -> None:
        """
         Sets the category types to be filtered out for workflow design parameters.  
        """
        pass
    
    ##  Sets the file types to be filtered out for workflow design parameters.  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: sc_design_explr_eval (" Simcenter 3D Design Space Exploration Evaluation Only")
    ## 
    ## <param name="fileTypes"> (@link SimulationWorkflowBuilder.FilterFileType List[NXOpen.CaeDseWorkflow.SimulationWorkflowBuilder.FilterFileType]@endlink) </param>
    def SetFilteredFileTypes(self, fileTypes: List[SimulationWorkflowBuilder.FilterFileType]) -> None:
        """
         Sets the file types to be filtered out for workflow design parameters.  
        """
        pass
    
    ##  Sets the simulation workflow name.  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: sc_design_explr_eval (" Simcenter 3D Design Space Exploration Evaluation Only")
    ## 
    ## <param name="name"> (str)  Simulation Workflow name </param>
    def SetName(self, name: str) -> None:
        """
         Sets the simulation workflow name.  
        """
        pass
    
    ##  Sets the post-solve journal file name.  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: sc_design_explr_eval (" Simcenter 3D Design Space Exploration Evaluation Only")
    ## 
    ## <param name="name"> (str)  Post-solve Journal name </param>
    def SetPostsolveJournalName(self, name: str) -> None:
        """
         Sets the post-solve journal file name.  
        """
        pass
    
    ##  Sets the pre-solve journal file name.  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: sc_design_explr_eval (" Simcenter 3D Design Space Exploration Evaluation Only")
    ## 
    ## <param name="name"> (str)  Pre-solve Journal name </param>
    def SetPresolveJournalName(self, name: str) -> None:
        """
         Sets the pre-solve journal file name.  
        """
        pass
    
    ##  Sets the simulation part.  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: sc_design_explr_eval (" Simcenter 3D Design Space Exploration Evaluation Only")
    ## 
    ## <param name="sim"> (@link NXOpen.CAE.SimSimulation NXOpen.CAE.SimSimulation@endlink) </param>
    def SetSimulation(self, sim: NXOpen.CAE.SimSimulation) -> None:
        """
         Sets the simulation part.  
        """
        pass
    
    ##  Sets the ordered set of solutions. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: sc_design_explr_eval (" Simcenter 3D Design Space Exploration Evaluation Only")
    ## 
    ## <param name="solutions"> (@link NXOpen.CAE.SimSolution List[NXOpen.CAE.SimSolution]@endlink)   </param>
    def SetSolutions(self, solutions: List[NXOpen.CAE.SimSolution]) -> None:
        """
         Sets the ordered set of solutions. 
        """
        pass
    
    ##  Sets the workflow.  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: sc_design_explr_eval (" Simcenter 3D Design Space Exploration Evaluation Only")
    ## 
    ## <param name="workflow"> (@link SimulationWorkflow NXOpen.CaeDseWorkflow.SimulationWorkflow@endlink) </param>
    def SetWorkflow(self, workflow: SimulationWorkflow) -> None:
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

    ## License requirements: sc_design_explr_eval (" Simcenter 3D Design Space Exploration Evaluation Only")
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

    ## License requirements: sc_design_explr_eval (" Simcenter 3D Design Space Exploration Evaluation Only")
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


    ##  Gets a @link CaeDseWorkflow::FEMassResponse CaeDseWorkflow::FEMassResponse@endlink  
    ##  @return response (@link FEMassResponse NXOpen.CaeDseWorkflow.FEMassResponse@endlink): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: sc_design_explr_eval (" Simcenter 3D Design Space Exploration Evaluation Only")
    def GetFEMassResponse(self) -> FEMassResponse:
        """
         Gets a @link CaeDseWorkflow::FEMassResponse CaeDseWorkflow::FEMassResponse@endlink  
         @return response (@link FEMassResponse NXOpen.CaeDseWorkflow.FEMassResponse@endlink): .
        """
        pass
    
    ##  Gets a @link CaeDseWorkflow::FEVolumeResponse CaeDseWorkflow::FEVolumeResponse@endlink  
    ##  @return response (@link FEVolumeResponse NXOpen.CaeDseWorkflow.FEVolumeResponse@endlink): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: sc_design_explr_eval (" Simcenter 3D Design Space Exploration Evaluation Only")
    def GetFEVolumeResponse(self) -> FEVolumeResponse:
        """
         Gets a @link CaeDseWorkflow::FEVolumeResponse CaeDseWorkflow::FEVolumeResponse@endlink  
         @return response (@link FEVolumeResponse NXOpen.CaeDseWorkflow.FEVolumeResponse@endlink): .
        """
        pass
    
    ##  Gets a @link CaeDseWorkflow::FEWeightResponse CaeDseWorkflow::FEWeightResponse@endlink  
    ##  @return response (@link FEWeightResponse NXOpen.CaeDseWorkflow.FEWeightResponse@endlink): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: sc_design_explr_eval (" Simcenter 3D Design Space Exploration Evaluation Only")
    def GetFEWeightResponse(self) -> FEWeightResponse:
        """
         Gets a @link CaeDseWorkflow::FEWeightResponse CaeDseWorkflow::FEWeightResponse@endlink  
         @return response (@link FEWeightResponse NXOpen.CaeDseWorkflow.FEWeightResponse@endlink): .
        """
        pass
    
## @package NXOpen.CaeDseWorkflow
## Classes, Enums and Structs under NXOpen.CaeDseWorkflow namespace

##  @link SimulationWorkflowBuilderFilterCategoryType NXOpen.CaeDseWorkflow.SimulationWorkflowBuilderFilterCategoryType @endlink is an alias for @link SimulationWorkflowBuilder.FilterCategoryType NXOpen.CaeDseWorkflow.SimulationWorkflowBuilder.FilterCategoryType@endlink
SimulationWorkflowBuilderFilterCategoryType = SimulationWorkflowBuilder.FilterCategoryType


##  @link SimulationWorkflowBuilderFilterFileType NXOpen.CaeDseWorkflow.SimulationWorkflowBuilderFilterFileType @endlink is an alias for @link SimulationWorkflowBuilder.FilterFileType NXOpen.CaeDseWorkflow.SimulationWorkflowBuilder.FilterFileType@endlink
SimulationWorkflowBuilderFilterFileType = SimulationWorkflowBuilder.FilterFileType


