from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
class FEMassResponse(Response): 
    """ Represents a CaeDseWorkflow.FEMassResponse object."""
    pass
class FEVolumeResponse(Response): 
    """ Represents a CaeDseWorkflow.FEVolumeResponse object."""
    pass
class FEWeightResponse(Response): 
    """ Represents a CaeDseWorkflow.FEWeightResponse object."""
    pass
import NXOpen
class Response(NXOpen.NXObject): 
    """ Represents a CaeDseWorkflow.Response object."""
    pass
import NXOpen
import NXOpen.CAE
import NXOpen.CAE.AeroStructures
class SimulationWorkflowBuilder(NXOpen.Builder): 
    """  Represents Optimization Simulation Workflow Builder.  """
    class FilterCategoryType(Enum):
        """
        Members Include: 
         |Physical|  Physical parameter type 
         |Section|  1D Section parameter type 
         |ModelingObject|  Modeling Object parameter type 
         |Region|  Region parameter type 
         |Mesh|  Mesh parameter type 
         |ResultMeasure|  Result Measure parameter type 
         |ResultProbe|  Result Probe parameter type 
         |MaterialOnBody|  Material on body parameter type 
         |LoadBoundaryCondition|  Load Boundary Condition parameter type 

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
        @staticmethod
        def ValueOf(value: int) -> SimulationWorkflowBuilder.FilterCategoryType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FilterFileType(Enum):
        """
        Members Include: 
         |Sim|  CAE Simulation part type 
         |Afem|  CAE Assembly Fem part type 
         |Fem|  CAE Fem part type 
         |Ideal|  CAE Idealize part type 
         |Cad|  CAD part type 

        """
        Sim: int
        Afem: int
        Fem: int
        Ideal: int
        Cad: int
        @staticmethod
        def ValueOf(value: int) -> SimulationWorkflowBuilder.FilterFileType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetAerostructMarginSolutions(self) -> List[NXOpen.CAE.AeroStructures.MarginSolution]:
        """
         Returns the ordered set of aerostructures margin solutions. 
         Returns marginSolutions ( NXOpen.CAE.AeroStructures.MarginSolution Li):  .
        """
        pass
    def GetFilteredAssociationNames(self) -> List[str]:
        """
         Returns the association names used for filtering workflow design parameters in all parts.  
         Returns assocNames (List[str]): .
        """
        pass
    def GetFilteredAssociationNamesWithAssociatedParts(self) -> Tuple[List[str], List[NXOpen.BasePart]]:
        """
         Returns the association names with associated parts used for filtering workflow design parameters.  
         Returns A tuple consisting of (assocNames, assocParts). 
         - assocNames is: List[str].
         - assocParts is:  NXOpen.BasePart Li.

        """
        pass
    def GetFilteredCategoryTypes(self) -> List[SimulationWorkflowBuilder.FilterCategoryType]:
        """
         Returns the category types that were filtered out for workflow design parameters.  
         Returns catTypes ( SimulationWorkflowBuilder.FilterCategoryType List[NXOpen.C): .
        """
        pass
    def GetFilteredFileTypes(self) -> List[SimulationWorkflowBuilder.FilterFileType]:
        """
         Returns the file types that were filtered out for workflow design parameters.  
         Returns fileTypes ( SimulationWorkflowBuilder.FilterFileType List[NXOpen.C): .
        """
        pass
    def GetName(self) -> str:
        """
         Returns the simulation workflow name.  
         Returns name (str):  Simulation Workflow name .
        """
        pass
    def GetPostsolveJournalName(self) -> str:
        """
         Returns the post-solve journal file name.  
         Returns name (str):  Post-solve Journal name .
        """
        pass
    def GetPresolveJournalName(self) -> str:
        """
         Returns the pre-solve journal file name.  
         Returns name (str):  Pre-solve Journal name .
        """
        pass
    def GetRunSolutionProcessOnly(self) -> bool:
        """
         Returns the option to run only solution processes and not the referenced solutions. 
         Returns runSolutionProcessOnly (bool): .
        """
        pass
    def GetSimulation(self) -> NXOpen.CAE.SimSimulation:
        """
         Returns the simulation part. 
         Returns sim ( NXOpen.CAE.SimSimulation): .
        """
        pass
    def GetSolutions(self) -> List[NXOpen.CAE.SimSolution]:
        """
         Returns the ordered set of solutions. 
         Returns solutions ( NXOpen.CAE.SimSolution Li):  .
        """
        pass
    def GetWorkflow(self) -> SimulationWorkflow:
        """
         Returns the workflow.  
         Returns workflow ( SimulationWorkflow NXOpen.Cae): .
        """
        pass
    def SetAerostructMarginSolutions(self, marginSolutions: List[NXOpen.CAE.AeroStructures.MarginSolution]) -> None:
        """
         Sets the ordered set of aerostructures margin solutions. 
        """
        pass
    def SetFilteredAssociationNames(self, assocNames: List[str]) -> None:
        """
         Sets the association names to use for filtering workflow design parameters in all parts.  
        """
        pass
    def SetFilteredAssociationNamesWithAssociatedParts(self, assocParts: List[NXOpen.BasePart], assocNames: List[str]) -> None:
        """
         Sets the association names with associated parts to use for filtering workflow design parameters.  
        """
        pass
    def SetFilteredCategoryTypes(self, catTypes: List[SimulationWorkflowBuilder.FilterCategoryType]) -> None:
        """
         Sets the category types to be filtered out for workflow design parameters.  
        """
        pass
    def SetFilteredFileTypes(self, fileTypes: List[SimulationWorkflowBuilder.FilterFileType]) -> None:
        """
         Sets the file types to be filtered out for workflow design parameters.  
        """
        pass
    def SetName(self, name: str) -> None:
        """
         Sets the simulation workflow name.  
        """
        pass
    def SetPostsolveJournalName(self, name: str) -> None:
        """
         Sets the post-solve journal file name.  
        """
        pass
    def SetPresolveJournalName(self, name: str) -> None:
        """
         Sets the pre-solve journal file name.  
        """
        pass
    def SetRunSolutionProcessOnly(self, runSolutionProcessOnly: bool) -> None:
        """
         Sets the option to run only solution processes and not the referenced solutions. 
        """
        pass
    def SetSimulation(self, sim: NXOpen.CAE.SimSimulation) -> None:
        """
         Sets the simulation part.  
        """
        pass
    def SetSolutions(self, solutions: List[NXOpen.CAE.SimSolution]) -> None:
        """
         Sets the ordered set of solutions. 
        """
        pass
    def SetWorkflow(self, workflow: SimulationWorkflow) -> None:
        """
         Sets the workflow.  
        """
        pass
import NXOpen
class SimulationWorkflowCollection(NXOpen.Object): 
    """ Represents a collection of NXOpen.CaeDseWorkflow.SimulationWorkflow objects. """
    def CreateEditWorkflowBuilder(part: NXOpen.BasePart, workflow: SimulationWorkflow) -> SimulationWorkflowBuilder:
        """
         Creates a CaeDseWorkflow.SimulationWorkflowBuilder 
         Returns builder ( SimulationWorkflowBuilder NXOpen.Cae): .
        """
        pass
    def CreateWorkflowBuilder(part: NXOpen.BasePart) -> SimulationWorkflowBuilder:
        """
         Creates a CaeDseWorkflow.SimulationWorkflowBuilder 
         Returns builder ( SimulationWorkflowBuilder NXOpen.Cae): .
        """
        pass
import NXOpen.DSEPlatform
class SimulationWorkflow(NXOpen.DSEPlatform.OptimizationWorkflow): 
    """ Represents a CaeDseWorkflow.SimulationWorkflow class object."""
    def GetFEMassResponse(self) -> FEMassResponse:
        """
         Gets a CaeDseWorkflow.FEMassResponse 
         Returns response ( FEMassResponse NXOpen.Cae): .
        """
        pass
    def GetFEVolumeResponse(self) -> FEVolumeResponse:
        """
         Gets a CaeDseWorkflow.FEVolumeResponse 
         Returns response ( FEVolumeResponse NXOpen.Cae): .
        """
        pass
    def GetFEWeightResponse(self) -> FEWeightResponse:
        """
         Gets a CaeDseWorkflow.FEWeightResponse 
         Returns response ( FEWeightResponse NXOpen.Cae): .
        """
        pass
