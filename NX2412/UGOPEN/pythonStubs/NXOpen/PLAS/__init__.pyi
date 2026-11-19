from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
class ControlLoopBuilder(RunBuilder): 
    """  Represents a ControlLoopBuilder.  """
    @property
    def ProcessVariable(self) -> str:
        """
        Getter for property: (str) ProcessVariable
         Returns the process variable of the control loop.  
             
         
        """
        pass
    @ProcessVariable.setter
    def ProcessVariable(self, processVariable: str):
        """
        Setter for property: (str) ProcessVariable
         Returns the process variable of the control loop.  
             
         
        """
        pass
class ControlLoop(Run): 
    """ Represents the ControlLoop class. """
    pass
import NXOpen
class PlasManager(NXOpen.Object): 
    """ A manager to deal with all objects. """
    @property
    def ActiveControlLoop(self) -> Run:
        """
        Getter for property: ( Run NXOpe) ActiveControlLoop
         Returns the active control loop   
            
         
        """
        pass
    @ActiveControlLoop.setter
    def ActiveControlLoop(self, controlLoop: Run):
        """
        Setter for property: ( Run NXOpe) ActiveControlLoop
         Returns the active control loop   
            
         
        """
        pass
    @property
    def ActiveRun(self) -> Run:
        """
        Getter for property: ( Run NXOpe) ActiveRun
         Returns the active run   
            
         
        """
        pass
    @ActiveRun.setter
    def ActiveRun(self, run: Run):
        """
        Setter for property: ( Run NXOpe) ActiveRun
         Returns the active run   
            
         
        """
        pass
    def CreateControlLoopBuilder(self, run: Run) -> ControlLoopBuilder:
        """
         Creates a PLAS.ControlLoopBuilder. 
         Returns builder ( ControlLoopBuilder NXOpe): .
        """
        pass
    def CreateRunBuilder(self, run: Run) -> RunBuilder:
        """
         Creates a PLAS.RunBuilder. 
         Returns builder ( RunBuilder NXOpe): .
        """
        pass
import NXOpen
import NXOpen.PDM
class RunBuilder(NXOpen.Builder): 
    """  Represents a RunBuilder.  """
    @property
    def Discipline(self) -> str:
        """
        Getter for property: (str) Discipline
         Returns the current discipline of this run.  
           Discipline define things such as the default specifications, 
                starting nodes for parts and stock, synonyms, etc.  
         
        """
        pass
    @Discipline.setter
    def Discipline(self, discipline: str):
        """
        Setter for property: (str) Discipline
         Returns the current discipline of this run.  
           Discipline define things such as the default specifications, 
                starting nodes for parts and stock, synonyms, etc.  
         
        """
        pass
    @property
    def IsUnassigned(self) -> bool:
        """
        Getter for property: (bool) IsUnassigned
         Returns whether the run is unassigned   
            
         
        """
        pass
    @IsUnassigned.setter
    def IsUnassigned(self, isUnassigned: bool):
        """
        Setter for property: (bool) IsUnassigned
         Returns whether the run is unassigned   
            
         
        """
        pass
    @property
    def LineTypePathId(self) -> str:
        """
        Getter for property: (str) LineTypePathId
         Returns the line type path ID of the run.  
             
         
        """
        pass
    @LineTypePathId.setter
    def LineTypePathId(self, lineTypePathId: str):
        """
        Setter for property: (str) LineTypePathId
         Returns the line type path ID of the run.  
             
         
        """
        pass
    @property
    def ObjectApplication(self) -> str:
        """
        Getter for property: (str) ObjectApplication
         Returns the application name of the run.  
             
         
        """
        pass
    @ObjectApplication.setter
    def ObjectApplication(self, objectApplication: str):
        """
        Setter for property: (str) ObjectApplication
         Returns the application name of the run.  
             
         
        """
        pass
    @property
    def PipeSpecPathId(self) -> str:
        """
        Getter for property: (str) PipeSpecPathId
         Returns the pipe specification object of this run.  
             
         
        """
        pass
    @PipeSpecPathId.setter
    def PipeSpecPathId(self, pipeSpecPathId: str):
        """
        Setter for property: (str) PipeSpecPathId
         Returns the pipe specification object of this run.  
             
         
        """
        pass
    def GetLogicalObject(self) -> NXOpen.PDM.LogicalObject:
        """
         Gets the known logical object. 
         Returns logicalObject ( NXOpen.PDM.LogicalObject): .
        """
        pass
import NXOpen.PDM
class Run(NXOpen.PDM.ElementGroup): 
    """ Represents the Run class. """
    def GetBranches(self) -> List[NXOpen.PDM.OrderedElementGroup]:
        """
         Get the branches in the run.
         Returns branches ( NXOpen.PDM.OrderedElementGroup Li):  the collection of branches in the run .
        """
        pass
    def ReparentBranch(self, destinationRun: Run, oldbranch: NXOpen.PDM.OrderedElementGroup) -> NXOpen.PDM.OrderedElementGroup:
        """
         Moves branch from one run to another. the original branch will be destroyed 
         Returns newbranch ( NXOpen.PDM.OrderedElementGroup): .
        """
        pass
