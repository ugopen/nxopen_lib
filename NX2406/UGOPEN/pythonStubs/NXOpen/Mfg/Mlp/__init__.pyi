from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents a Machining Line Planner blank  <br> To obtain an instance of this class use GetBlankModel of Product.  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class Blank(NXOpen.DisplayableObject): 
    """ Represents a Machining Line Planner blank """


    ##  Get the Product 
    ##  @return product (@link Product NXOpen.Mfg.Mlp.Product@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def GetProduct(self) -> Product:
        """
         Get the Product 
         @return product (@link Product NXOpen.Mfg.Mlp.Product@endlink): .
        """
        pass
    
import NXOpen
##  Represents a Machining Line Planner command  <br> To obtain an instance of this class use @link NXOpen::Mfg::Mlp::MachiningLinePlanner::CreateCommand NXOpen::Mfg::Mlp::MachiningLinePlanner::CreateCommand@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class Command(NXOpen.TaggedObject): 
    """ Represents a Machining Line Planner command """


    ##  Returns whether this command is undoable 
    ##  @return canundo (bool): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def CanUndo(self) -> bool:
        """
         Returns whether this command is undoable 
         @return canundo (bool): .
        """
        pass
    
    ##  Create the command input, to destroy the command input use @link NXOpen::Mfg::Mlp::Input::Destroy NXOpen::Mfg::Mlp::Input::Destroy@endlink  
    ##  @return input (@link Input NXOpen.Mfg.Mlp.Input@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_mlp_setup (" NX Multi Setup Planner")
    def CreateInput(self) -> Input:
        """
         Create the command input, to destroy the command input use @link NXOpen::Mfg::Mlp::Input::Destroy NXOpen::Mfg::Mlp::Input::Destroy@endlink  
         @return input (@link Input NXOpen.Mfg.Mlp.Input@endlink): .
        """
        pass
    
    ##  Destroy command 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_mlp_setup (" NX Multi Setup Planner")
    def Destroy(self) -> None:
        """
         Destroy command 
        """
        pass
    
    ##  Execute the command 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_mlp_setup (" NX Multi Setup Planner")
    ## 
    ## <param name="input"> (@link Input NXOpen.Mfg.Mlp.Input@endlink) </param>
    def Execute(self, input: Input) -> None:
        """
         Execute the command 
        """
        pass
    
import NXOpen
##  Represents a Machining Line Planner in-process feature  <br> To obtain an instance of this class use GetInProcessFeatures of Operation or MachiningFeature.  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class InProcessFeature(NXOpen.DisplayableObject): 
    """ Represents a Machining Line Planner in-process feature """


    ##  Get the Machining Feature 
    ##  @return machining_feature (@link MachiningFeature NXOpen.Mfg.Mlp.MachiningFeature@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def GetMachiningFeature(self) -> MachiningFeature:
        """
         Get the Machining Feature 
         @return machining_feature (@link MachiningFeature NXOpen.Mfg.Mlp.MachiningFeature@endlink): .
        """
        pass
    
    ##  Get the Operation 
    ##  @return operation (@link Operation NXOpen.Mfg.Mlp.Operation@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def GetOperation(self) -> Operation:
        """
         Get the Operation 
         @return operation (@link Operation NXOpen.Mfg.Mlp.Operation@endlink): .
        """
        pass
    
import NXOpen
##  Represents a Machining Line Planner command input  <br> To obtain an instance of this class use @link NXOpen::Mfg::Mlp::Command::CreateInput NXOpen::Mfg::Mlp::Command::CreateInput@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class Input(NXOpen.TaggedObject): 
    """ Represents a Machining Line Planner command input """


    ##  Add input argument for the command 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_mlp_setup (" NX Multi Setup Planner")
    ## 
    ## <param name="name"> (str) </param>
    ## <param name="value"> (str) </param>
    def AddArgument(self, name: str, value: str) -> None:
        """
         Add input argument for the command 
        """
        pass
    
    ##  Destroy input 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_mlp_setup (" NX Multi Setup Planner")
    def Destroy(self) -> None:
        """
         Destroy input 
        """
        pass
    
    ##  Set input property for the command 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_mlp_setup (" NX Multi Setup Planner")
    ## 
    ## <param name="name"> (str) </param>
    ## <param name="value"> (str) </param>
    def SetProperty(self, name: str, value: str) -> None:
        """
         Set input property for the command 
        """
        pass
    
    ##  Set input Machining Line Planner subjects that the command will work on 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_mlp_setup (" NX Multi Setup Planner")
    ## 
    ## <param name="subjects"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink) </param>
    def SetSubjects(self, subjects: List[NXOpen.TaggedObject]) -> None:
        """
         Set input Machining Line Planner subjects that the command will work on 
        """
        pass
    
    ##  Set input Machining Line Planner targets for the command 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_mlp_setup (" NX Multi Setup Planner")
    ## 
    ## <param name="targets"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink) </param>
    def SetTargets(self, targets: List[NXOpen.TaggedObject]) -> None:
        """
         Set input Machining Line Planner targets for the command 
        """
        pass
    
import NXOpen
##  Interface to the Machining Line Planner process  <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX11.0.2  <br> 

class IProcess(NXOpen.Object): 
    """ Interface to the Machining Line Planner process """


    ##  Get the Constraint Predecessors of this process (note that these are the immediate predecessors, this function does not recurse) 
    ##  @return constraint_predecessors (@link IProcess List[NXOpen.Mfg.Mlp.IProcess]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    @abstractmethod
    def GetConstraintPredecessors(self) -> List[IProcess]:
        """
         Get the Constraint Predecessors of this process (note that these are the immediate predecessors, this function does not recurse) 
         @return constraint_predecessors (@link IProcess List[NXOpen.Mfg.Mlp.IProcess]@endlink): .
        """
        pass
    
    ##  Get the Constraint Successors of this process (note that these are the immediate successors, this function does not recurse) 
    ##  @return constraint_successors (@link IProcess List[NXOpen.Mfg.Mlp.IProcess]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    @abstractmethod
    def GetConstraintSuccessors(self) -> List[IProcess]:
        """
         Get the Constraint Successors of this process (note that these are the immediate successors, this function does not recurse) 
         @return constraint_successors (@link IProcess List[NXOpen.Mfg.Mlp.IProcess]@endlink): .
        """
        pass
    
    ##  Get the Predecessors of this process (note that these are the immediate predecessors, this function does not recurse) 
    ##  @return predecessors (@link IProcess List[NXOpen.Mfg.Mlp.IProcess]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    @abstractmethod
    def GetPredecessors(self) -> List[IProcess]:
        """
         Get the Predecessors of this process (note that these are the immediate predecessors, this function does not recurse) 
         @return predecessors (@link IProcess List[NXOpen.Mfg.Mlp.IProcess]@endlink): .
        """
        pass
    
    ##  Get the Resource used by this process 
    ##  @return resource (@link IResource NXOpen.Mfg.Mlp.IResource@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    @abstractmethod
    def GetResource(self) -> IResource:
        """
         Get the Resource used by this process 
         @return resource (@link IResource NXOpen.Mfg.Mlp.IResource@endlink): .
        """
        pass
    
    ##  Get the Successors of this process (note that these are the immediate successors, this function does not recurse) 
    ##  @return successors (@link IProcess List[NXOpen.Mfg.Mlp.IProcess]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    @abstractmethod
    def GetSuccessors(self) -> List[IProcess]:
        """
         Get the Successors of this process (note that these are the immediate successors, this function does not recurse) 
         @return successors (@link IProcess List[NXOpen.Mfg.Mlp.IProcess]@endlink): .
        """
        pass
    
import NXOpen
##  Interface to the Machining Line Planner resource  <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX11.0.2  <br> 

class IResource(NXOpen.Object): 
    """ Interface to the Machining Line Planner resource """


    ##  Get the Processes 
    ##  @return processes (@link IProcess List[NXOpen.Mfg.Mlp.IProcess]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    @abstractmethod
    def GetProcesses(self) -> List[IProcess]:
        """
         Get the Processes 
         @return processes (@link IProcess List[NXOpen.Mfg.Mlp.IProcess]@endlink): .
        """
        pass
    
import NXOpen
##  Represents a Machining Line Planner line  <br> To obtain an instance of this class use GetLine of ProcessPlan or ProcessSetup.  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class Line(NXOpen.DisplayableObject): 
    """ Represents a Machining Line Planner line """


    ##  Finds the @link  Mfg::Mlp::ProcessSetup   Mfg::Mlp::ProcessSetup @endlink  with the given identifier as recorded in a journal. 
    ##             An object may not return the same value as its JournalIdentifier in different versions of 
    ##             the software. However newer versions of the software should find the same object when 
    ##             FindObject is passed older versions of its journal identifier. In general, this method 
    ##             should not be used in handwritten code and exists to support record and playback of journals.
    ## 
    ##             An exception will be thrown if no object can be found with the given journal identifier. 
    ##  @return found (@link NXOpen.INXObject NXOpen.INXObject@endlink):  Setup found, or null if no such setup exists.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="journal_identifier"> (str)  Name of the setup to be found </param>
    def FindObject(self, journal_identifier: str) -> NXOpen.INXObject:
        """
         Finds the @link  Mfg::Mlp::ProcessSetup   Mfg::Mlp::ProcessSetup @endlink  with the given identifier as recorded in a journal. 
                    An object may not return the same value as its JournalIdentifier in different versions of 
                    the software. However newer versions of the software should find the same object when 
                    FindObject is passed older versions of its journal identifier. In general, this method 
                    should not be used in handwritten code and exists to support record and playback of journals.
        
                    An exception will be thrown if no object can be found with the given journal identifier. 
         @return found (@link NXOpen.INXObject NXOpen.INXObject@endlink):  Setup found, or null if no such setup exists.
        """
        pass
    
    ##  Get the Process plan 
    ##  @return process_plan (@link ProcessPlan NXOpen.Mfg.Mlp.ProcessPlan@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def GetProcessPlan(self) -> ProcessPlan:
        """
         Get the Process plan 
         @return process_plan (@link ProcessPlan NXOpen.Mfg.Mlp.ProcessPlan@endlink): .
        """
        pass
    
    ##  Get the Setups 
    ##  @return setups (@link ProcessSetup List[NXOpen.Mfg.Mlp.ProcessSetup]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def GetSetups(self) -> List[ProcessSetup]:
        """
         Get the Setups 
         @return setups (@link ProcessSetup List[NXOpen.Mfg.Mlp.ProcessSetup]@endlink): .
        """
        pass
    
import NXOpen
##  Represents a Machining Line Planner machine tool  <br> To obtain an instance of this class use GetMachineTool (not yet implemented!) of ProcessSetup.  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class MachineTool(NXOpen.DisplayableObject): 
    """ Represents a Machining Line Planner machine tool """
    pass


import NXOpen
##  Represents a Machining Line Planner machining feature  <br> To obtain an instance of this class use GetMachiningFeature of InProcessFeature or GetMachiningFeatures of Workpiece or PartFeature.  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class MachiningFeature(NXOpen.DisplayableObject): 
    """ Represents a Machining Line Planner machining feature """


    ##  Get the In-Process Features 
    ##  @return in_process_features (@link InProcessFeature List[NXOpen.Mfg.Mlp.InProcessFeature]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def GetInProcessFeatures(self) -> List[InProcessFeature]:
        """
         Get the In-Process Features 
         @return in_process_features (@link InProcessFeature List[NXOpen.Mfg.Mlp.InProcessFeature]@endlink): .
        """
        pass
    
    ##  Get the Part Feature 
    ##  @return part_feature (@link PartFeature NXOpen.Mfg.Mlp.PartFeature@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def GetPartFeature(self) -> PartFeature:
        """
         Get the Part Feature 
         @return part_feature (@link PartFeature NXOpen.Mfg.Mlp.PartFeature@endlink): .
        """
        pass
    
    ##  Get the Workpieces 
    ##  @return workpieces (@link Workpiece List[NXOpen.Mfg.Mlp.Workpiece]@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def GetWorkpieces(self) -> List[Workpiece]:
        """
         Get the Workpieces 
         @return workpieces (@link Workpiece List[NXOpen.Mfg.Mlp.Workpiece]@endlink): .
        """
        pass
    
import NXOpen
##  Represents the Line Planner  <br> To obtain an instance use the static method @link NXOpen::Mfg::Mlp::MachiningLinePlanner::GetMachiningLinePlanner NXOpen::Mfg::Mlp::MachiningLinePlanner::GetMachiningLinePlanner@endlink .  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class MachiningLinePlanner(NXOpen.Object): 
    """ Represents the Line Planner """


    ##  Create the command by specified string identifier, to destroy the command use @link NXOpen::Mfg::Mlp::Command::Destroy NXOpen::Mfg::Mlp::Command::Destroy@endlink  
    ##  @return command (@link Command NXOpen.Mfg.Mlp.Command@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_mlp_setup (" NX Multi Setup Planner")
    ## <param name="command_id"> (str)  command identifier </param>
    def CreateCommand(command_id: str) -> Command:
        """
         Create the command by specified string identifier, to destroy the command use @link NXOpen::Mfg::Mlp::Command::Destroy NXOpen::Mfg::Mlp::Command::Destroy@endlink  
         @return command (@link Command NXOpen.Mfg.Mlp.Command@endlink): .
        """
        pass
    
    ##  Returns the ProcessPlan of the given part 
    ##  @return process_plan (@link ProcessPlan NXOpen.Mfg.Mlp.ProcessPlan@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink)  part to get the process plan from </param>
    def GetProcessPlan(part: NXOpen.Part) -> ProcessPlan:
        """
         Returns the ProcessPlan of the given part 
         @return process_plan (@link ProcessPlan NXOpen.Mfg.Mlp.ProcessPlan@endlink): .
        """
        pass
    
import NXOpen
##  Represents a Machining Line Planner operation  <br> To obtain an instance of this class use GetOperation of InProcessFeature or GetOperations of ProcessSetup.  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class Operation(NXOpen.DisplayableObject): 
    """ Represents a Machining Line Planner operation """


    ##  Finds the @link  Mfg::Mlp::InProcessFeature   Mfg::Mlp::InProcessFeature @endlink  
    ##             with the given identifier as recorded in a journal. 
    ##             An object may not return the same value as its JournalIdentifier in different versions of 
    ##             the software. However newer versions of the software should find the same object when 
    ##             FindObject is passed older versions of its journal identifier. In general, this method 
    ##             should not be used in handwritten code and exists to support record and playback of journals.
    ## 
    ##             An exception will be thrown if no object can be found with the given journal identifier. 
    ##  @return found (@link NXOpen.INXObject NXOpen.INXObject@endlink):  Object found, or null if no such in-process feature exists.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="journal_identifier"> (str)  Name of the in-process feature to be found </param>
    def FindObject(self, journal_identifier: str) -> NXOpen.INXObject:
        """
         Finds the @link  Mfg::Mlp::InProcessFeature   Mfg::Mlp::InProcessFeature @endlink  
                    with the given identifier as recorded in a journal. 
                    An object may not return the same value as its JournalIdentifier in different versions of 
                    the software. However newer versions of the software should find the same object when 
                    FindObject is passed older versions of its journal identifier. In general, this method 
                    should not be used in handwritten code and exists to support record and playback of journals.
        
                    An exception will be thrown if no object can be found with the given journal identifier. 
         @return found (@link NXOpen.INXObject NXOpen.INXObject@endlink):  Object found, or null if no such in-process feature exists.
        """
        pass
    
    ##  Get the In-Process Features 
    ##  @return in_process_features (@link InProcessFeature List[NXOpen.Mfg.Mlp.InProcessFeature]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def GetInProcessFeatures(self) -> List[InProcessFeature]:
        """
         Get the In-Process Features 
         @return in_process_features (@link InProcessFeature List[NXOpen.Mfg.Mlp.InProcessFeature]@endlink): .
        """
        pass
    
    ##  Get the Setup 
    ##  @return setup (@link ProcessSetup NXOpen.Mfg.Mlp.ProcessSetup@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def GetSetup(self) -> ProcessSetup:
        """
         Get the Setup 
         @return setup (@link ProcessSetup NXOpen.Mfg.Mlp.ProcessSetup@endlink): .
        """
        pass
    
import NXOpen
##  Represents a Machining Line Planner part-feature  <br> To obtain an instance of this class use GetPartFeature of MachiningFeature or GetPartFeatures or Part.  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class PartFeature(NXOpen.DisplayableObject): 
    """ Represents a Machining Line Planner part-feature """


    ##  Get the Machining Features of this part feature in setup workpieces 
    ##  @return machining_features (@link MachiningFeature List[NXOpen.Mfg.Mlp.MachiningFeature]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def GetMachiningFeatures(self) -> List[MachiningFeature]:
        """
         Get the Machining Features of this part feature in setup workpieces 
         @return machining_features (@link MachiningFeature List[NXOpen.Mfg.Mlp.MachiningFeature]@endlink): .
        """
        pass
    
    ##  Get the Part Model 
    ##  @return part_model (@link Part NXOpen.Mfg.Mlp.Part@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def GetPartModel(self) -> Part:
        """
         Get the Part Model 
         @return part_model (@link Part NXOpen.Mfg.Mlp.Part@endlink): .
        """
        pass
    
import NXOpen
##  Represents a Machining Line Planner part  <br> To obtain an instance of this class use GetPartModel of Product or PartFeature.  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class Part(NXOpen.DisplayableObject): 
    """ Represents a Machining Line Planner part """


    ##  Finds the @link  Mfg::Mlp::PartFeature   Mfg::Mlp::PartFeature @endlink  
    ##             with the given identifier as recorded in a journal. 
    ##             An object may not return the same value as its JournalIdentifier in different versions of 
    ##             the software. However newer versions of the software should find the same object when 
    ##             FindObject is passed older versions of its journal identifier. In general, this method 
    ##             should not be used in handwritten code and exists to support record and playback of journals.
    ## 
    ##             An exception will be thrown if no object can be found with the given journal identifier. 
    ##  @return found (@link NXOpen.INXObject NXOpen.INXObject@endlink):  Object found, or null if no such partfeature exists.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="journal_identifier"> (str)  Name of the partfeature to be found </param>
    def FindObject(self, journal_identifier: str) -> NXOpen.INXObject:
        """
         Finds the @link  Mfg::Mlp::PartFeature   Mfg::Mlp::PartFeature @endlink  
                    with the given identifier as recorded in a journal. 
                    An object may not return the same value as its JournalIdentifier in different versions of 
                    the software. However newer versions of the software should find the same object when 
                    FindObject is passed older versions of its journal identifier. In general, this method 
                    should not be used in handwritten code and exists to support record and playback of journals.
        
                    An exception will be thrown if no object can be found with the given journal identifier. 
         @return found (@link NXOpen.INXObject NXOpen.INXObject@endlink):  Object found, or null if no such partfeature exists.
        """
        pass
    
    ##  Get the Part Features 
    ##  @return part_features (@link PartFeature List[NXOpen.Mfg.Mlp.PartFeature]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def GetPartFeatures(self) -> List[PartFeature]:
        """
         Get the Part Features 
         @return part_features (@link PartFeature List[NXOpen.Mfg.Mlp.PartFeature]@endlink): .
        """
        pass
    
    ##  Get the Product 
    ##  @return product (@link Product NXOpen.Mfg.Mlp.Product@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def GetProduct(self) -> Product:
        """
         Get the Product 
         @return product (@link Product NXOpen.Mfg.Mlp.Product@endlink): .
        """
        pass
    
import NXOpen
##  Represents a Machining Line Planner process plan  <br> To obtain an instance of this class use @link NXOpen::Mfg::Mlp::MachiningLinePlanner NXOpen::Mfg::Mlp::MachiningLinePlanner@endlink   <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class ProcessPlan(NXOpen.DisplayableObject): 
    """ Represents a Machining Line Planner process plan """


    ##  Finds the @link  Mfg::Mlp::Line   Mfg::Mlp::Line @endlink , not allocated @link  Mfg::Mlp::ProcessSetup   Mfg::Mlp::ProcessSetup @endlink  or @link  Mfg::Mlp::Product   Mfg::Mlp::Product @endlink 
    ##             with the given identifier as recorded in a journal. 
    ##             An object may not return the same value as its JournalIdentifier in different versions of 
    ##             the software. However newer versions of the software should find the same object when 
    ##             FindObject is passed older versions of its journal identifier. In general, this method 
    ##             should not be used in handwritten code and exists to support record and playback of journals.
    ## 
    ##             An exception will be thrown if no object can be found with the given journal identifier. 
    ##  @return found (@link NXOpen.INXObject NXOpen.INXObject@endlink):  Object found, or null if no such object exists.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="journal_identifier"> (str)  Name of the line, not allocated setup or product to be found </param>
    def FindObject(self, journal_identifier: str) -> NXOpen.INXObject:
        """
         Finds the @link  Mfg::Mlp::Line   Mfg::Mlp::Line @endlink , not allocated @link  Mfg::Mlp::ProcessSetup   Mfg::Mlp::ProcessSetup @endlink  or @link  Mfg::Mlp::Product   Mfg::Mlp::Product @endlink 
                    with the given identifier as recorded in a journal. 
                    An object may not return the same value as its JournalIdentifier in different versions of 
                    the software. However newer versions of the software should find the same object when 
                    FindObject is passed older versions of its journal identifier. In general, this method 
                    should not be used in handwritten code and exists to support record and playback of journals.
        
                    An exception will be thrown if no object can be found with the given journal identifier. 
         @return found (@link NXOpen.INXObject NXOpen.INXObject@endlink):  Object found, or null if no such object exists.
        """
        pass
    
    ##  Get the Line 
    ##  @return line (@link Line NXOpen.Mfg.Mlp.Line@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def GetLine(self) -> Line:
        """
         Get the Line 
         @return line (@link Line NXOpen.Mfg.Mlp.Line@endlink): .
        """
        pass
    
    ##  Get the Not Allocated setup 
    ##  @return not_allocated_setup (@link ProcessSetup NXOpen.Mfg.Mlp.ProcessSetup@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def GetNotAllocatedSetup(self) -> ProcessSetup:
        """
         Get the Not Allocated setup 
         @return not_allocated_setup (@link ProcessSetup NXOpen.Mfg.Mlp.ProcessSetup@endlink): .
        """
        pass
    
    ##  Get the Products being manufactured in this ProcessPlan 
    ##  @return products (@link Product List[NXOpen.Mfg.Mlp.Product]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def GetProducts(self) -> List[Product]:
        """
         Get the Products being manufactured in this ProcessPlan 
         @return products (@link Product List[NXOpen.Mfg.Mlp.Product]@endlink): .
        """
        pass
    
    ##  Get the Setups of this ProcessPlan in the order in which they are machined 
    ##  @return setups (@link ProcessSetup List[NXOpen.Mfg.Mlp.ProcessSetup]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def GetSetups(self) -> List[ProcessSetup]:
        """
         Get the Setups of this ProcessPlan in the order in which they are machined 
         @return setups (@link ProcessSetup List[NXOpen.Mfg.Mlp.ProcessSetup]@endlink): .
        """
        pass
    
import NXOpen
##  Represents a Machining Line Planner process setup  <br> To obtain an instance of this class use GetSetup of Operation, Workpiece or ToolSet or GetSetups on ProcessPlan or Line.  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class ProcessSetup(NXOpen.DisplayableObject): 
    """ Represents a Machining Line Planner process setup """


    ##  Finds the @link  Mfg::Mlp::Operation   Mfg::Mlp::Operation @endlink , @link  Mfg::Mlp::Workpiece   Mfg::Mlp::Workpiece @endlink , 
    ##             @link  Mfg::Mlp::ToolSet   Mfg::Mlp::ToolSet @endlink  or @link  Mfg::Mlp::MachineTool   Mfg::Mlp::MachineTool @endlink 
    ##             with the given identifier as recorded in a journal. 
    ##             An object may not return the same value as its JournalIdentifier in different versions of 
    ##             the software. However newer versions of the software should find the same object when 
    ##             FindObject is passed older versions of its journal identifier. In general, this method 
    ##             should not be used in handwritten code and exists to support record and playback of journals.
    ## 
    ##             An exception will be thrown if no object can be found with the given journal identifier. 
    ##  @return found (@link NXOpen.INXObject NXOpen.INXObject@endlink):  Object found, or null if no such object exists.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="journal_identifier"> (str)  Name of the operation, workpiece, machinetool or toolset to be found </param>
    def FindObject(self, journal_identifier: str) -> NXOpen.INXObject:
        """
         Finds the @link  Mfg::Mlp::Operation   Mfg::Mlp::Operation @endlink , @link  Mfg::Mlp::Workpiece   Mfg::Mlp::Workpiece @endlink , 
                    @link  Mfg::Mlp::ToolSet   Mfg::Mlp::ToolSet @endlink  or @link  Mfg::Mlp::MachineTool   Mfg::Mlp::MachineTool @endlink 
                    with the given identifier as recorded in a journal. 
                    An object may not return the same value as its JournalIdentifier in different versions of 
                    the software. However newer versions of the software should find the same object when 
                    FindObject is passed older versions of its journal identifier. In general, this method 
                    should not be used in handwritten code and exists to support record and playback of journals.
        
                    An exception will be thrown if no object can be found with the given journal identifier. 
         @return found (@link NXOpen.INXObject NXOpen.INXObject@endlink):  Object found, or null if no such object exists.
        """
        pass
    
    ##  Get the CAM part of this Setup 
    ##  @return cam_part (@link NXOpen.Part NXOpen.Part@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    def GetCamPart(self) -> NXOpen.Part:
        """
         Get the CAM part of this Setup 
         @return cam_part (@link NXOpen.Part NXOpen.Part@endlink): .
        """
        pass
    
    ##  Get the Line of this setup 
    ##  @return line (@link Line NXOpen.Mfg.Mlp.Line@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def GetLine(self) -> Line:
        """
         Get the Line of this setup 
         @return line (@link Line NXOpen.Mfg.Mlp.Line@endlink): .
        """
        pass
    
    ##  Get the Operations in this Setup in the order in which they are machined 
    ##  @return operations (@link Operation List[NXOpen.Mfg.Mlp.Operation]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def GetOperations(self) -> List[Operation]:
        """
         Get the Operations in this Setup in the order in which they are machined 
         @return operations (@link Operation List[NXOpen.Mfg.Mlp.Operation]@endlink): .
        """
        pass
    
    ##  Get the Process plan of this setup 
    ##  @return process_plan (@link ProcessPlan NXOpen.Mfg.Mlp.ProcessPlan@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def GetProcessPlan(self) -> ProcessPlan:
        """
         Get the Process plan of this setup 
         @return process_plan (@link ProcessPlan NXOpen.Mfg.Mlp.ProcessPlan@endlink): .
        """
        pass
    
    ##  Get the Tool Set 
    ##  @return tool_set (@link ToolSet NXOpen.Mfg.Mlp.ToolSet@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def GetToolSet(self) -> ToolSet:
        """
         Get the Tool Set 
         @return tool_set (@link ToolSet NXOpen.Mfg.Mlp.ToolSet@endlink): .
        """
        pass
    
    ##  Get the Workpieces being manufactured in this setup 
    ##  @return workpieces (@link Workpiece List[NXOpen.Mfg.Mlp.Workpiece]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def GetWorkpieces(self) -> List[Workpiece]:
        """
         Get the Workpieces being manufactured in this setup 
         @return workpieces (@link Workpiece List[NXOpen.Mfg.Mlp.Workpiece]@endlink): .
        """
        pass
    
    ##  Is this setup the Not Allocated setup 
    ##  @return is_not_allocated (bool): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def IsNotAllocated(self) -> bool:
        """
         Is this setup the Not Allocated setup 
         @return is_not_allocated (bool): .
        """
        pass
    
import NXOpen
##  Represents a Machining Line Planner product  <br> To obtain an instance of this class use GetProducts of ProcessPlan.  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class Product(NXOpen.DisplayableObject): 
    """ Represents a Machining Line Planner product """


    ##  Finds the @link  Mfg::Mlp::Blank   Mfg::Mlp::Blank @endlink  or @link  Mfg::Mlp::Part   Mfg::Mlp::Part @endlink 
    ##             with the given identifier as recorded in a journal. 
    ##             An object may not return the same value as its JournalIdentifier in different versions of 
    ##             the software. However newer versions of the software should find the same object when 
    ##             FindObject is passed older versions of its journal identifier. In general, this method 
    ##             should not be used in handwritten code and exists to support record and playback of journals.
    ## 
    ##             An exception will be thrown if no object can be found with the given journal identifier. 
    ##  @return found (@link NXOpen.INXObject NXOpen.INXObject@endlink):  Object found, or null if no such blank or part model exists.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="journal_identifier"> (str)  Name of the blank or part model to be found </param>
    def FindObject(self, journal_identifier: str) -> NXOpen.INXObject:
        """
         Finds the @link  Mfg::Mlp::Blank   Mfg::Mlp::Blank @endlink  or @link  Mfg::Mlp::Part   Mfg::Mlp::Part @endlink 
                    with the given identifier as recorded in a journal. 
                    An object may not return the same value as its JournalIdentifier in different versions of 
                    the software. However newer versions of the software should find the same object when 
                    FindObject is passed older versions of its journal identifier. In general, this method 
                    should not be used in handwritten code and exists to support record and playback of journals.
        
                    An exception will be thrown if no object can be found with the given journal identifier. 
         @return found (@link NXOpen.INXObject NXOpen.INXObject@endlink):  Object found, or null if no such blank or part model exists.
        """
        pass
    
    ##  Get the Blank Model 
    ##  @return blank_model (@link Blank NXOpen.Mfg.Mlp.Blank@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def GetBlankModel(self) -> Blank:
        """
         Get the Blank Model 
         @return blank_model (@link Blank NXOpen.Mfg.Mlp.Blank@endlink): .
        """
        pass
    
    ##  Get the workpiece of this product in the not allocated setup 
    ##  @return not_allocated_workpiece (@link Workpiece NXOpen.Mfg.Mlp.Workpiece@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def GetNotAllocatedWorkpiece(self) -> Workpiece:
        """
         Get the workpiece of this product in the not allocated setup 
         @return not_allocated_workpiece (@link Workpiece NXOpen.Mfg.Mlp.Workpiece@endlink): .
        """
        pass
    
    ##  Get the Part Model 
    ##  @return part_model (@link Part NXOpen.Mfg.Mlp.Part@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def GetPartModel(self) -> Part:
        """
         Get the Part Model 
         @return part_model (@link Part NXOpen.Mfg.Mlp.Part@endlink): .
        """
        pass
    
    ##  Get the Workpieces 
    ##  @return workpieces (@link Workpiece List[NXOpen.Mfg.Mlp.Workpiece]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def GetWorkpieces(self) -> List[Workpiece]:
        """
         Get the Workpieces 
         @return workpieces (@link Workpiece List[NXOpen.Mfg.Mlp.Workpiece]@endlink): .
        """
        pass
    
import NXOpen
##  Represents a Machining Line Planner tool assembly  <br> To obtain an instance of this class use (not yet implemented!) GetToolAssembly of Operation.  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class ToolAssembly(NXOpen.DisplayableObject): 
    """ Represents a Machining Line Planner tool assembly """


    ##  Get the Tool Set 
    ##  @return tool_set (@link ToolSet NXOpen.Mfg.Mlp.ToolSet@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def GetToolSet(self) -> ToolSet:
        """
         Get the Tool Set 
         @return tool_set (@link ToolSet NXOpen.Mfg.Mlp.ToolSet@endlink): .
        """
        pass
    
import NXOpen
##  Represents a Machining Line Planner tool set  <br> To obtain an instance of this class use GetToolSet of ToolAssembly.  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class ToolSet(NXOpen.DisplayableObject): 
    """ Represents a Machining Line Planner tool set """


    ##  Finds the @link  Mfg::Mlp::ToolAssembly   Mfg::Mlp::ToolAssembly @endlink  
    ##             with the given identifier as recorded in a journal. 
    ##             An object may not return the same value as its JournalIdentifier in different versions of 
    ##             the software. However newer versions of the software should find the same object when 
    ##             FindObject is passed older versions of its journal identifier. In general, this method 
    ##             should not be used in handwritten code and exists to support record and playback of journals.
    ## 
    ##             An exception will be thrown if no object can be found with the given journal identifier. 
    ##  @return found (@link NXOpen.INXObject NXOpen.INXObject@endlink):  Object found, or null if no such object exists.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="journal_identifier"> (str)  Name of the tool assembly to be found </param>
    def FindObject(self, journal_identifier: str) -> NXOpen.INXObject:
        """
         Finds the @link  Mfg::Mlp::ToolAssembly   Mfg::Mlp::ToolAssembly @endlink  
                    with the given identifier as recorded in a journal. 
                    An object may not return the same value as its JournalIdentifier in different versions of 
                    the software. However newer versions of the software should find the same object when 
                    FindObject is passed older versions of its journal identifier. In general, this method 
                    should not be used in handwritten code and exists to support record and playback of journals.
        
                    An exception will be thrown if no object can be found with the given journal identifier. 
         @return found (@link NXOpen.INXObject NXOpen.INXObject@endlink):  Object found, or null if no such object exists.
        """
        pass
    
    ##  Get the Setup 
    ##  @return setup (@link ProcessSetup NXOpen.Mfg.Mlp.ProcessSetup@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def GetSetup(self) -> ProcessSetup:
        """
         Get the Setup 
         @return setup (@link ProcessSetup NXOpen.Mfg.Mlp.ProcessSetup@endlink): .
        """
        pass
    
    ##  Get the Tool Assemblies 
    ##  @return tool_assemblies (@link ToolAssembly List[NXOpen.Mfg.Mlp.ToolAssembly]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def GetToolAssemblies(self) -> List[ToolAssembly]:
        """
         Get the Tool Assemblies 
         @return tool_assemblies (@link ToolAssembly List[NXOpen.Mfg.Mlp.ToolAssembly]@endlink): .
        """
        pass
    
import NXOpen
##  Represents a Machining Line Planner workpiece  <br> To obtain an instance of this class, use GetWorkpiece of MachiningFeature or GetWorkpieces of ProcessSetup or Product.  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class Workpiece(NXOpen.DisplayableObject): 
    """ Represents a Machining Line Planner workpiece """


    ##  Finds the @link  Mfg::Mlp::MachiningFeature   Mfg::Mlp::MachiningFeature @endlink  with the given identifier as recorded in a journal. 
    ##             An object may not return the same value as its JournalIdentifier in different versions of 
    ##             the software. However newer versions of the software should find the same object when 
    ##             FindObject is passed older versions of its journal identifier. In general, this method 
    ##             should not be used in handwritten code and exists to support record and playback of journals.
    ## 
    ##             An exception will be thrown if no object can be found with the given journal identifier. 
    ##  @return found (@link NXOpen.INXObject NXOpen.INXObject@endlink):  Object found, or null if no such machining feature exists.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="journal_identifier"> (str)  Name of the machining feature to be found </param>
    def FindObject(self, journal_identifier: str) -> NXOpen.INXObject:
        """
         Finds the @link  Mfg::Mlp::MachiningFeature   Mfg::Mlp::MachiningFeature @endlink  with the given identifier as recorded in a journal. 
                    An object may not return the same value as its JournalIdentifier in different versions of 
                    the software. However newer versions of the software should find the same object when 
                    FindObject is passed older versions of its journal identifier. In general, this method 
                    should not be used in handwritten code and exists to support record and playback of journals.
        
                    An exception will be thrown if no object can be found with the given journal identifier. 
         @return found (@link NXOpen.INXObject NXOpen.INXObject@endlink):  Object found, or null if no such machining feature exists.
        """
        pass
    
    ##  Get the Machining Features 
    ##  @return machining_features (@link MachiningFeature List[NXOpen.Mfg.Mlp.MachiningFeature]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def GetMachiningFeatures(self) -> List[MachiningFeature]:
        """
         Get the Machining Features 
         @return machining_features (@link MachiningFeature List[NXOpen.Mfg.Mlp.MachiningFeature]@endlink): .
        """
        pass
    
    ##  Get the Product 
    ##  @return product (@link Product NXOpen.Mfg.Mlp.Product@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def GetProduct(self) -> Product:
        """
         Get the Product 
         @return product (@link Product NXOpen.Mfg.Mlp.Product@endlink): .
        """
        pass
    
    ##  Get the Setup 
    ##  @return setup (@link ProcessSetup NXOpen.Mfg.Mlp.ProcessSetup@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def GetSetup(self) -> ProcessSetup:
        """
         Get the Setup 
         @return setup (@link ProcessSetup NXOpen.Mfg.Mlp.ProcessSetup@endlink): .
        """
        pass
    
## @package NXOpen.Mfg.Mlp
## Classes, Enums and Structs under NXOpen.Mfg.Mlp namespace

