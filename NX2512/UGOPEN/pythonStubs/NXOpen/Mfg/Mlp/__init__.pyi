from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class Blank(NXOpen.DisplayableObject): 
    """ Represents a Machining Line Planner blank """
    def GetProduct(self) -> Product:
        """
         Get the Product 
         Returns product ( Product NXOpen): .
        """
        pass
import NXOpen
class Command(NXOpen.TaggedObject): 
    """ Represents a Machining Line Planner command """
    def CanUndo(self) -> bool:
        """
         Returns whether this command is undoable 
         Returns canundo (bool): .
        """
        pass
    def CreateInput(self) -> Input:
        """
         Create the command input, to destroy the command input use NXOpen.Mfg.Mlp.Input.Destroy 
         Returns input ( Input NXOpen): .
        """
        pass
    def Destroy(self) -> None:
        """
         Destroy command 
        """
        pass
    def Execute(self, input: Input) -> None:
        """
         Execute the command 
        """
        pass
import NXOpen
class InProcessFeature(NXOpen.DisplayableObject): 
    """ Represents a Machining Line Planner in-process feature """
    def GetMachiningFeature(self) -> MachiningFeature:
        """
         Get the Machining Feature 
         Returns machining_feature ( MachiningFeature NXOpen): .
        """
        pass
    def GetOperation(self) -> Operation:
        """
         Get the Operation 
         Returns operation ( Operation NXOpen): .
        """
        pass
import NXOpen
class Input(NXOpen.TaggedObject): 
    """ Represents a Machining Line Planner command input """
    def AddArgument(self, name: str, value: str) -> None:
        """
         Add input argument for the command 
        """
        pass
    def Destroy(self) -> None:
        """
         Destroy input 
        """
        pass
    def SetProperty(self, name: str, value: str) -> None:
        """
         Set input property for the command 
        """
        pass
    def SetSubjects(self, subjects: List[NXOpen.TaggedObject]) -> None:
        """
         Set input Machining Line Planner subjects that the command will work on 
        """
        pass
    def SetTargets(self, targets: List[NXOpen.TaggedObject]) -> None:
        """
         Set input Machining Line Planner targets for the command 
        """
        pass
import NXOpen
class IProcess(NXOpen.Object): 
    """ Interface to the Machining Line Planner process """
    @abstractmethod
    def GetConstraintPredecessors(self) -> List[IProcess]:
        """
         Get the Constraint Predecessors of this process (note that these are the immediate predecessors, this function does not recurse) 
         Returns constraint_predecessors ( IProcess List[NXOp): .
        """
        pass
    @abstractmethod
    def GetConstraintSuccessors(self) -> List[IProcess]:
        """
         Get the Constraint Successors of this process (note that these are the immediate successors, this function does not recurse) 
         Returns constraint_successors ( IProcess List[NXOp): .
        """
        pass
    @abstractmethod
    def GetPredecessors(self) -> List[IProcess]:
        """
         Get the Predecessors of this process (note that these are the immediate predecessors, this function does not recurse) 
         Returns predecessors ( IProcess List[NXOp): .
        """
        pass
    @abstractmethod
    def GetResource(self) -> IResource:
        """
         Get the Resource used by this process 
         Returns resource ( IResource NXOpen): .
        """
        pass
    @abstractmethod
    def GetSuccessors(self) -> List[IProcess]:
        """
         Get the Successors of this process (note that these are the immediate successors, this function does not recurse) 
         Returns successors ( IProcess List[NXOp): .
        """
        pass
import NXOpen
class IResource(NXOpen.Object): 
    """ Interface to the Machining Line Planner resource """
    @abstractmethod
    def GetProcesses(self) -> List[IProcess]:
        """
         Get the Processes 
         Returns processes ( IProcess List[NXOp): .
        """
        pass
import NXOpen
class Line(NXOpen.DisplayableObject): 
    """ Represents a Machining Line Planner line """
    def FindObject(self, journal_identifier: str) -> NXOpen.INXObject:
        """
         Finds the  Mfg.Mlp.ProcessSetup  with the given identifier as recorded in a journal. 
                    An object may not return the same value as its JournalIdentifier in different versions of 
                    the software. However newer versions of the software should find the same object when 
                    FindObject is passed older versions of its journal identifier. In general, this method 
                    should not be used in handwritten code and exists to support record and playback of journals.
                    An exception will be thrown if no object can be found with the given journal identifier. 
         Returns found ( NXOpen.INXObject):  Setup found, or null if no such setup exists.
        """
        pass
    def GetProcessPlan(self) -> ProcessPlan:
        """
         Get the Process plan 
         Returns process_plan ( ProcessPlan NXOpen): .
        """
        pass
    def GetSetups(self) -> List[ProcessSetup]:
        """
         Get the Setups 
         Returns setups ( ProcessSetup List[NXOp): .
        """
        pass
import NXOpen
class MachineTool(NXOpen.DisplayableObject): 
    """ Represents a Machining Line Planner machine tool """
    pass
import NXOpen
class MachiningFeature(NXOpen.DisplayableObject): 
    """ Represents a Machining Line Planner machining feature """
    def GetInProcessFeatures(self) -> List[InProcessFeature]:
        """
         Get the In-Process Features 
         Returns in_process_features ( InProcessFeature List[NXOp): .
        """
        pass
    def GetPartFeature(self) -> PartFeature:
        """
         Get the Part Feature 
         Returns part_feature ( PartFeature NXOpen): .
        """
        pass
    def GetWorkpieces(self) -> List[Workpiece]:
        """
         Get the Workpieces 
         Returns workpieces ( Workpiece List[NXOp): .
        """
        pass
import NXOpen
class MachiningLinePlanner(NXOpen.Object): 
    """ Represents the Line Planner """
    def CreateCommand(command_id: str) -> Command:
        """
         Create the command by specified string identifier, to destroy the command use NXOpen.Mfg.Mlp.Command.Destroy 
         Returns command ( Command NXOpen): .
        """
        pass
    def GetProcessPlan(part: NXOpen.Part) -> ProcessPlan:
        """
         Returns the ProcessPlan of the given part 
         Returns process_plan ( ProcessPlan NXOpen): .
        """
        pass
import NXOpen
class Operation(NXOpen.DisplayableObject): 
    """ Represents a Machining Line Planner operation """
    def FindObject(self, journal_identifier: str) -> NXOpen.INXObject:
        """
         Finds the  Mfg.Mlp.InProcessFeature  
                    with the given identifier as recorded in a journal. 
                    An object may not return the same value as its JournalIdentifier in different versions of 
                    the software. However newer versions of the software should find the same object when 
                    FindObject is passed older versions of its journal identifier. In general, this method 
                    should not be used in handwritten code and exists to support record and playback of journals.
                    An exception will be thrown if no object can be found with the given journal identifier. 
         Returns found ( NXOpen.INXObject):  Object found, or null if no such in-process feature exists.
        """
        pass
    def GetInProcessFeatures(self) -> List[InProcessFeature]:
        """
         Get the In-Process Features 
         Returns in_process_features ( InProcessFeature List[NXOp): .
        """
        pass
    def GetSetup(self) -> ProcessSetup:
        """
         Get the Setup 
         Returns setup ( ProcessSetup NXOpen): .
        """
        pass
import NXOpen
class PartFeature(NXOpen.DisplayableObject): 
    """ Represents a Machining Line Planner part-feature """
    def GetMachiningFeatures(self) -> List[MachiningFeature]:
        """
         Get the Machining Features of this part feature in setup workpieces 
         Returns machining_features ( MachiningFeature List[NXOp): .
        """
        pass
    def GetPartModel(self) -> Part:
        """
         Get the Part Model 
         Returns part_model ( Part NXOpen): .
        """
        pass
import NXOpen
class Part(NXOpen.DisplayableObject): 
    """ Represents a Machining Line Planner part """
    def FindObject(self, journal_identifier: str) -> NXOpen.INXObject:
        """
         Finds the  Mfg.Mlp.PartFeature  
                    with the given identifier as recorded in a journal. 
                    An object may not return the same value as its JournalIdentifier in different versions of 
                    the software. However newer versions of the software should find the same object when 
                    FindObject is passed older versions of its journal identifier. In general, this method 
                    should not be used in handwritten code and exists to support record and playback of journals.
                    An exception will be thrown if no object can be found with the given journal identifier. 
         Returns found ( NXOpen.INXObject):  Object found, or null if no such partfeature exists.
        """
        pass
    def GetPartFeatures(self) -> List[PartFeature]:
        """
         Get the Part Features 
         Returns part_features ( PartFeature List[NXOp): .
        """
        pass
    def GetProduct(self) -> Product:
        """
         Get the Product 
         Returns product ( Product NXOpen): .
        """
        pass
import NXOpen
class ProcessPlan(NXOpen.DisplayableObject): 
    """ Represents a Machining Line Planner process plan """
    def FindObject(self, journal_identifier: str) -> NXOpen.INXObject:
        """
         Finds the  Mfg.Mlp.Line , not allocated  Mfg.Mlp.ProcessSetup  or  Mfg.Mlp.Product 
                    with the given identifier as recorded in a journal. 
                    An object may not return the same value as its JournalIdentifier in different versions of 
                    the software. However newer versions of the software should find the same object when 
                    FindObject is passed older versions of its journal identifier. In general, this method 
                    should not be used in handwritten code and exists to support record and playback of journals.
                    An exception will be thrown if no object can be found with the given journal identifier. 
         Returns found ( NXOpen.INXObject):  Object found, or null if no such object exists.
        """
        pass
    def GetLine(self) -> Line:
        """
         Get the Line 
         Returns line ( Line NXOpen): .
        """
        pass
    def GetNotAllocatedSetup(self) -> ProcessSetup:
        """
         Get the Not Allocated setup 
         Returns not_allocated_setup ( ProcessSetup NXOpen): .
        """
        pass
    def GetProducts(self) -> List[Product]:
        """
         Get the Products being manufactured in this ProcessPlan 
         Returns products ( Product List[NXOp): .
        """
        pass
    def GetSetups(self) -> List[ProcessSetup]:
        """
         Get the Setups of this ProcessPlan in the order in which they are machined 
         Returns setups ( ProcessSetup List[NXOp): .
        """
        pass
import NXOpen
class ProcessSetup(NXOpen.DisplayableObject): 
    """ Represents a Machining Line Planner process setup """
    def FindObject(self, journal_identifier: str) -> NXOpen.INXObject:
        """
         Finds the  Mfg.Mlp.Operation ,  Mfg.Mlp.Workpiece , 
                     Mfg.Mlp.ToolSet  or  Mfg.Mlp.MachineTool 
                    with the given identifier as recorded in a journal. 
                    An object may not return the same value as its JournalIdentifier in different versions of 
                    the software. However newer versions of the software should find the same object when 
                    FindObject is passed older versions of its journal identifier. In general, this method 
                    should not be used in handwritten code and exists to support record and playback of journals.
                    An exception will be thrown if no object can be found with the given journal identifier. 
         Returns found ( NXOpen.INXObject):  Object found, or null if no such object exists.
        """
        pass
    def GetCamPart(self) -> NXOpen.Part:
        """
         Get the CAM part of this Setup 
         Returns cam_part ( NXOpen.Part): .
        """
        pass
    def GetLine(self) -> Line:
        """
         Get the Line of this setup 
         Returns line ( Line NXOpen): .
        """
        pass
    def GetOperations(self) -> List[Operation]:
        """
         Get the Operations in this Setup in the order in which they are machined 
         Returns operations ( Operation List[NXOp): .
        """
        pass
    def GetProcessPlan(self) -> ProcessPlan:
        """
         Get the Process plan of this setup 
         Returns process_plan ( ProcessPlan NXOpen): .
        """
        pass
    def GetToolSet(self) -> ToolSet:
        """
         Get the Tool Set 
         Returns tool_set ( ToolSet NXOpen): .
        """
        pass
    def GetWorkpieces(self) -> List[Workpiece]:
        """
         Get the Workpieces being manufactured in this setup 
         Returns workpieces ( Workpiece List[NXOp): .
        """
        pass
    def IsNotAllocated(self) -> bool:
        """
         Is this setup the Not Allocated setup 
         Returns is_not_allocated (bool): .
        """
        pass
import NXOpen
class Product(NXOpen.DisplayableObject): 
    """ Represents a Machining Line Planner product """
    def FindObject(self, journal_identifier: str) -> NXOpen.INXObject:
        """
         Finds the  Mfg.Mlp.Blank  or  Mfg.Mlp.Part 
                    with the given identifier as recorded in a journal. 
                    An object may not return the same value as its JournalIdentifier in different versions of 
                    the software. However newer versions of the software should find the same object when 
                    FindObject is passed older versions of its journal identifier. In general, this method 
                    should not be used in handwritten code and exists to support record and playback of journals.
                    An exception will be thrown if no object can be found with the given journal identifier. 
         Returns found ( NXOpen.INXObject):  Object found, or null if no such blank or part model exists.
        """
        pass
    def GetBlankModel(self) -> Blank:
        """
         Get the Blank Model 
         Returns blank_model ( Blank NXOpen): .
        """
        pass
    def GetNotAllocatedWorkpiece(self) -> Workpiece:
        """
         Get the workpiece of this product in the not allocated setup 
         Returns not_allocated_workpiece ( Workpiece NXOpen): .
        """
        pass
    def GetPartModel(self) -> Part:
        """
         Get the Part Model 
         Returns part_model ( Part NXOpen): .
        """
        pass
    def GetWorkpieces(self) -> List[Workpiece]:
        """
         Get the Workpieces 
         Returns workpieces ( Workpiece List[NXOp): .
        """
        pass
import NXOpen
class ToolAssembly(NXOpen.DisplayableObject): 
    """ Represents a Machining Line Planner tool assembly """
    def GetToolSet(self) -> ToolSet:
        """
         Get the Tool Set 
         Returns tool_set ( ToolSet NXOpen): .
        """
        pass
import NXOpen
class ToolSet(NXOpen.DisplayableObject): 
    """ Represents a Machining Line Planner tool set """
    def FindObject(self, journal_identifier: str) -> NXOpen.INXObject:
        """
         Finds the  Mfg.Mlp.ToolAssembly  
                    with the given identifier as recorded in a journal. 
                    An object may not return the same value as its JournalIdentifier in different versions of 
                    the software. However newer versions of the software should find the same object when 
                    FindObject is passed older versions of its journal identifier. In general, this method 
                    should not be used in handwritten code and exists to support record and playback of journals.
                    An exception will be thrown if no object can be found with the given journal identifier. 
         Returns found ( NXOpen.INXObject):  Object found, or null if no such object exists.
        """
        pass
    def GetSetup(self) -> ProcessSetup:
        """
         Get the Setup 
         Returns setup ( ProcessSetup NXOpen): .
        """
        pass
    def GetToolAssemblies(self) -> List[ToolAssembly]:
        """
         Get the Tool Assemblies 
         Returns tool_assemblies ( ToolAssembly List[NXOp): .
        """
        pass
import NXOpen
class Workpiece(NXOpen.DisplayableObject): 
    """ Represents a Machining Line Planner workpiece """
    def FindObject(self, journal_identifier: str) -> NXOpen.INXObject:
        """
         Finds the  Mfg.Mlp.MachiningFeature  with the given identifier as recorded in a journal. 
                    An object may not return the same value as its JournalIdentifier in different versions of 
                    the software. However newer versions of the software should find the same object when 
                    FindObject is passed older versions of its journal identifier. In general, this method 
                    should not be used in handwritten code and exists to support record and playback of journals.
                    An exception will be thrown if no object can be found with the given journal identifier. 
         Returns found ( NXOpen.INXObject):  Object found, or null if no such machining feature exists.
        """
        pass
    def GetMachiningFeatures(self) -> List[MachiningFeature]:
        """
         Get the Machining Features 
         Returns machining_features ( MachiningFeature List[NXOp): .
        """
        pass
    def GetProduct(self) -> Product:
        """
         Get the Product 
         Returns product ( Product NXOpen): .
        """
        pass
    def GetSetup(self) -> ProcessSetup:
        """
         Get the Setup 
         Returns setup ( ProcessSetup NXOpen): .
        """
        pass
