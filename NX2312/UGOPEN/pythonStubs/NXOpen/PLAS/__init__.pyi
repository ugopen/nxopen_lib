from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
##   @brief  Represents a ControlLoopBuilder.  
## 
##    <br> To create a new instance of this class, use @link NXOpen::PLAS::PlasManager::CreateControlLoopBuilder  NXOpen::PLAS::PlasManager::CreateControlLoopBuilder @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class ControlLoopBuilder(RunBuilder): 
    """ <summary> Represents a ControlLoopBuilder. </summary> """


    ## Getter for property: (str) ProcessVariable
    ##   the process variable of the control loop.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def ProcessVariable(self) -> str:
        """
        Getter for property: (str) ProcessVariable
          the process variable of the control loop.  
             
         
        """
        pass
    
    ## Setter for property: (str) ProcessVariable

    ##   the process variable of the control loop.  
    ##      
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ProcessVariable.setter
    def ProcessVariable(self, processVariable: str):
        """
        Setter for property: (str) ProcessVariable
          the process variable of the control loop.  
             
         
        """
        pass
    
##  Represents the ControlLoop class.  <br> To create or edit an instance of this class, use @link NXOpen::PLAS::ControlLoopBuilder  NXOpen::PLAS::ControlLoopBuilder @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class ControlLoop(Run): 
    """ Represents the ControlLoop class. """
    pass


import NXOpen
##  A manager to deal with all objects.  <br> To obtain an instance of this class, refer to @link NXOpen::Part  NXOpen::Part @endlink  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class PlasManager(NXOpen.Object): 
    """ A manager to deal with all objects. """


    ## Getter for property: (@link Run NXOpen.PLAS.Run@endlink) ActiveControlLoop
    ##   the active control loop   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return Run
    @property
    def ActiveControlLoop(self) -> Run:
        """
        Getter for property: (@link Run NXOpen.PLAS.Run@endlink) ActiveControlLoop
          the active control loop   
            
         
        """
        pass
    
    ## Setter for property: (@link Run NXOpen.PLAS.Run@endlink) ActiveControlLoop

    ##   the active control loop   
    ##     
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ActiveControlLoop.setter
    def ActiveControlLoop(self, controlLoop: Run):
        """
        Setter for property: (@link Run NXOpen.PLAS.Run@endlink) ActiveControlLoop
          the active control loop   
            
         
        """
        pass
    
    ## Getter for property: (@link Run NXOpen.PLAS.Run@endlink) ActiveRun
    ##   the active run   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return Run
    @property
    def ActiveRun(self) -> Run:
        """
        Getter for property: (@link Run NXOpen.PLAS.Run@endlink) ActiveRun
          the active run   
            
         
        """
        pass
    
    ## Setter for property: (@link Run NXOpen.PLAS.Run@endlink) ActiveRun

    ##   the active run   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @ActiveRun.setter
    def ActiveRun(self, run: Run):
        """
        Setter for property: (@link Run NXOpen.PLAS.Run@endlink) ActiveRun
          the active run   
            
         
        """
        pass
    
    ##  Creates a @link PLAS::ControlLoopBuilder PLAS::ControlLoopBuilder@endlink . 
    ##  @return builder (@link ControlLoopBuilder NXOpen.PLAS.ControlLoopBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ##  @link PLAS::ControlLoop PLAS::ControlLoop@endlink  to be edited, if NULL then create a new one 
    def CreateControlLoopBuilder(part: PlasManager, run: Run) -> ControlLoopBuilder:
        """
         Creates a @link PLAS::ControlLoopBuilder PLAS::ControlLoopBuilder@endlink . 
         @return builder (@link ControlLoopBuilder NXOpen.PLAS.ControlLoopBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link PLAS::RunBuilder PLAS::RunBuilder@endlink . 
    ##  @return builder (@link RunBuilder NXOpen.PLAS.RunBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    ##  @link PLAS::Run PLAS::Run@endlink  to be edited, if NULL then create a new one 
    def CreateRunBuilder(part: PlasManager, run: Run) -> RunBuilder:
        """
         Creates a @link PLAS::RunBuilder PLAS::RunBuilder@endlink . 
         @return builder (@link RunBuilder NXOpen.PLAS.RunBuilder@endlink): .
        """
        pass
    
import NXOpen
import NXOpen.PDM
##   @brief  Represents a RunBuilder.  
## 
##    <br> To create a new instance of this class, use @link NXOpen::PLAS::PlasManager::CreateRunBuilder  NXOpen::PLAS::PlasManager::CreateRunBuilder @endlink  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class RunBuilder(NXOpen.Builder): 
    """ <summary> Represents a RunBuilder. </summary> """


    ## Getter for property: (str) Discipline
    ##   the current discipline of this run.  
    ##    Discipline define things such as the default specifications, 
    ##         starting nodes for parts and stock, synonyms, etc.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def Discipline(self) -> str:
        """
        Getter for property: (str) Discipline
          the current discipline of this run.  
           Discipline define things such as the default specifications, 
                starting nodes for parts and stock, synonyms, etc.  
         
        """
        pass
    
    ## Setter for property: (str) Discipline

    ##   the current discipline of this run.  
    ##    Discipline define things such as the default specifications, 
    ##         starting nodes for parts and stock, synonyms, etc.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Discipline.setter
    def Discipline(self, discipline: str):
        """
        Setter for property: (str) Discipline
          the current discipline of this run.  
           Discipline define things such as the default specifications, 
                starting nodes for parts and stock, synonyms, etc.  
         
        """
        pass
    
    ## Getter for property: (bool) IsUnassigned
    ##   whether the run is unassigned   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def IsUnassigned(self) -> bool:
        """
        Getter for property: (bool) IsUnassigned
          whether the run is unassigned   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsUnassigned

    ##   whether the run is unassigned   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @IsUnassigned.setter
    def IsUnassigned(self, isUnassigned: bool):
        """
        Setter for property: (bool) IsUnassigned
          whether the run is unassigned   
            
         
        """
        pass
    
    ## Getter for property: (str) LineTypePathId
    ##   the line type path ID of the run.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return str
    @property
    def LineTypePathId(self) -> str:
        """
        Getter for property: (str) LineTypePathId
          the line type path ID of the run.  
             
         
        """
        pass
    
    ## Setter for property: (str) LineTypePathId

    ##   the line type path ID of the run.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @LineTypePathId.setter
    def LineTypePathId(self, lineTypePathId: str):
        """
        Setter for property: (str) LineTypePathId
          the line type path ID of the run.  
             
         
        """
        pass
    
    ## Getter for property: (str) ObjectApplication
    ##   the application name of the run.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return str
    @property
    def ObjectApplication(self) -> str:
        """
        Getter for property: (str) ObjectApplication
          the application name of the run.  
             
         
        """
        pass
    
    ## Setter for property: (str) ObjectApplication

    ##   the application name of the run.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @ObjectApplication.setter
    def ObjectApplication(self, objectApplication: str):
        """
        Setter for property: (str) ObjectApplication
          the application name of the run.  
             
         
        """
        pass
    
    ## Getter for property: (str) PipeSpecPathId
    ##   the pipe specification object of this run.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return str
    @property
    def PipeSpecPathId(self) -> str:
        """
        Getter for property: (str) PipeSpecPathId
          the pipe specification object of this run.  
             
         
        """
        pass
    
    ## Setter for property: (str) PipeSpecPathId

    ##   the pipe specification object of this run.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @PipeSpecPathId.setter
    def PipeSpecPathId(self, pipeSpecPathId: str):
        """
        Setter for property: (str) PipeSpecPathId
          the pipe specification object of this run.  
             
         
        """
        pass
    
    ##  Gets the known logical object. 
    ##  @return logicalObject (@link NXOpen.PDM.LogicalObject NXOpen.PDM.LogicalObject@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    @staticmethod
    def GetLogicalObject(builder: RunBuilder) -> NXOpen.PDM.LogicalObject:
        """
         Gets the known logical object. 
         @return logicalObject (@link NXOpen.PDM.LogicalObject NXOpen.PDM.LogicalObject@endlink): .
        """
        pass
    
import NXOpen.PDM
##  Represents the Run class.  <br> To create or edit an instance of this class, use @link NXOpen::PLAS::RunBuilder  NXOpen::PLAS::RunBuilder @endlink  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class Run(NXOpen.PDM.ElementGroup): 
    """ Represents the Run class. """


    ##  Get the branches in the run.
    ##  @return branches (@link NXOpen.PDM.OrderedElementGroup List[NXOpen.PDM.OrderedElementGroup]@endlink):  the collection of branches in the run .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBranches(run: Run) -> List[NXOpen.PDM.OrderedElementGroup]:
        """
         Get the branches in the run.
         @return branches (@link NXOpen.PDM.OrderedElementGroup List[NXOpen.PDM.OrderedElementGroup]@endlink):  the collection of branches in the run .
        """
        pass
    
    ##  Moves branch from one run to another. the original branch will be destroyed 
    ##  @return newbranch (@link NXOpen.PDM.OrderedElementGroup NXOpen.PDM.OrderedElementGroup@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="destinationRun"> (@link Run NXOpen.PLAS.Run@endlink) </param>
    ## <param name="oldbranch"> (@link NXOpen.PDM.OrderedElementGroup NXOpen.PDM.OrderedElementGroup@endlink) </param>
    def ReparentBranch(sourceRun: Run, destinationRun: Run, oldbranch: NXOpen.PDM.OrderedElementGroup) -> NXOpen.PDM.OrderedElementGroup:
        """
         Moves branch from one run to another. the original branch will be destroyed 
         @return newbranch (@link NXOpen.PDM.OrderedElementGroup NXOpen.PDM.OrderedElementGroup@endlink): .
        """
        pass
    
## @package NXOpen.PLAS
## Classes, Enums and Structs under NXOpen.PLAS namespace

