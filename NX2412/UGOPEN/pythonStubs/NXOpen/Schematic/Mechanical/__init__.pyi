from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class BranchBuilder(NXOpen.Builder): 
    """ Edits a branch in a run. """
    @property
    def Insulation(self) -> str:
        """
        Getter for property: (str) Insulation
         Returns the insulation   
            
         
        """
        pass
    @Insulation.setter
    def Insulation(self, insulationId: str):
        """
        Setter for property: (str) Insulation
         Returns the insulation   
            
         
        """
        pass
import NXOpen.Schematic.Model
class Branch(NXOpen.Schematic.Model.BaseObject): 
    """ Represents the Branch class. """
    @property
    def Insulation(self) -> str:
        """
        Getter for property: (str) Insulation
         Returns the insulation   
            
         
        """
        pass
    def GetInsulationSource(self) -> NXOpen.Schematic.Model.BaseObject:
        """
         Gets the object containing the insulation definition.
                    The returned object contains the insulation definition returned from NXOpen.Schematic.Mechanical.Branch.GetInsulationWithInheritance.
         Returns sourceObject ( NXOpen.Schematic.Model.BaseObject): .
        """
        pass
    def GetInsulationWithInheritance(self) -> str:
        """
         Gets the insulation which may be inherited from the parent run.
                    Use NXOpen.Schematic.Mechanical.Branch.GetInsulationSource to get the object that owns the insulation definition.
         Returns insulation (str): .
        """
        pass
    def GetOrderedObjects(self) -> List[NXOpen.Schematic.Model.BaseObject]:
        """
         Gets the ordered objects in the branch.
         Returns objs ( NXOpen.Schematic.Model.BaseObject Li):  the collection of ordered objects except direct connections in the branch. .
        """
        pass
    def GetRun(self) -> Run:
        """
         Gets the parent run of the branch.
         Returns run ( Run NXOpen.Schema): .
        """
        pass
import NXOpen
import NXOpen.Schematic.Model
class Connection(NXOpen.Schematic.Model.Connection): 
    """ Represents the Connection class. """
    @property
    def Insulation(self) -> str:
        """
        Getter for property: (str) Insulation
         Returns the insulation   
            
         
        """
        pass
    def GetBranch(self) -> Branch:
        """
         Gets the parent branch of the connection.
         Returns branch ( Branch NXOpen.Schema): .
        """
        pass
    def GetInsulationAttributeOwner(self) -> NXOpen.NXObject:
        """
         Gets the connection insulation attribute owner.
         Returns attrOwner ( NXOpen.NXObject): .
        """
        pass
    def GetInsulationSource(self) -> NXOpen.Schematic.Model.BaseObject:
        """
         Gets the object containing the insulation definition.
                    The returned object contains the insulation definition returned from NXOpen.Schematic.Mechanical.Connection.GetInsulationWithInheritance.
         Returns sourceObject ( NXOpen.Schematic.Model.BaseObject): .
        """
        pass
    def GetInsulationWithInheritance(self) -> str:
        """
         Gets the insulation which may be inherited from a parent object.
                    The insulation can be inherited from a parent branch or run. Use NXOpen.Schematic.Mechanical.Connection.GetInsulationSource to get the object that owns the insulation definition.
         Returns insulation (str): .
        """
        pass
    def GetObjectAttributeOwner(self) -> NXOpen.NXObject:
        """
         Gets the connection object attribute owner.
         Returns attrOwner ( NXOpen.NXObject): .
        """
        pass
    def GetOutletJunctions(self) -> List[Junction]:
        """
         Gets the outlet junctions on the connection.
         Returns junctions ( Junction List[NXOpen.Sche): .
        """
        pass
    def GetRun(self) -> Run:
        """
         Gets the parent run from the connection.
         Returns run ( Run NXOpen.Schema): .
        """
        pass
    def GetStockAttributeOwner(self) -> NXOpen.NXObject:
        """
         Gets the connection stock attribute owner.
         Returns attrOwner ( NXOpen.NXObject): .
        """
        pass
    def IsDirectConnection(self) -> bool:
        """
         Determines if the connection represents a direct connection.
         Returns directConnection (bool): .
        """
        pass
import NXOpen
import NXOpen.Schematic.Model
class Junction(NXOpen.Schematic.Model.Node): 
    """ Represents the Junction class. """
    def GetBranches(self) -> List[Branch]:
        """
         Gets the branches that the junction participates in.
         Returns branches ( Branch List[NXOpen.Sche): .
        """
        pass
    def GetClassificationAttributeOwner(self) -> NXOpen.NXObject:
        """
         Gets the junction classification attribute owner.
         Returns attrOwner ( NXOpen.NXObject): .
        """
        pass
    def GetConnections(self) -> List[Connection]:
        """
         Gets the connections that the junction participates in.
         Returns connections ( Connection List[NXOpen.Sche): .
        """
        pass
    def GetObjectAttributeOwner(self) -> NXOpen.NXObject:
        """
         Gets the junction object attribute owner.
         Returns attrOwner ( NXOpen.NXObject): .
        """
        pass
    def GetPorts(self) -> List[Port]:
        """
         Gets the gets the ports of the junction.
         Returns ports ( Port List[NXOpen.Sche): .
        """
        pass
import NXOpen.Schematic.Model
class Port(NXOpen.Schematic.Model.Port): 
    """ Represents the Port class. """
    def GetConnection(self) -> Connection:
        """
         Get the connection of the port if it participates in one.
         Returns connection ( Connection NXOpen.Schema): .
        """
        pass
    def GetOwningJunction(self) -> Junction:
        """
         Gets the owning junction.
         Returns junction ( Junction NXOpen.Schema): .
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
         Returns the discipline  
            
         
        """
        pass
    @Discipline.setter
    def Discipline(self, discipline: str):
        """
        Setter for property: (str) Discipline
         Returns the discipline  
            
         
        """
        pass
    @property
    def DisplayName(self) -> str:
        """
        Getter for property: (str) DisplayName
         Returns the display name  
            
         
        """
        pass
    @DisplayName.setter
    def DisplayName(self, name: str):
        """
        Setter for property: (str) DisplayName
         Returns the display name  
            
         
        """
        pass
    @property
    def Identifier(self) -> str:
        """
        Getter for property: (str) Identifier
         Returns the identifier  
            
         
        """
        pass
    @Identifier.setter
    def Identifier(self, id: str):
        """
        Setter for property: (str) Identifier
         Returns the identifier  
            
         
        """
        pass
    @property
    def Insulation(self) -> str:
        """
        Getter for property: (str) Insulation
         Returns the insulation   
            
         
        """
        pass
    @Insulation.setter
    def Insulation(self, insulationId: str):
        """
        Setter for property: (str) Insulation
         Returns the insulation   
            
         
        """
        pass
    @property
    def LineType(self) -> str:
        """
        Getter for property: (str) LineType
         Returns the line type  
            
         
        """
        pass
    @LineType.setter
    def LineType(self, lineType: str):
        """
        Setter for property: (str) LineType
         Returns the line type  
            
         
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
    def Specification(self) -> str:
        """
        Getter for property: (str) Specification
         Returns the specification  
            
         
        """
        pass
    @Specification.setter
    def Specification(self, specification: str):
        """
        Setter for property: (str) Specification
         Returns the specification  
            
         
        """
        pass
    @property
    def Standalone(self) -> bool:
        """
        Getter for property: (bool) Standalone
         Returns whether the run is standalone run which will be reside in logical model part.  
             
         
        """
        pass
    @Standalone.setter
    def Standalone(self, standalone: bool):
        """
        Setter for property: (bool) Standalone
         Returns whether the run is standalone run which will be reside in logical model part.  
             
         
        """
        pass
    def SetPartOperationCreateBuilder(self, createBuilder: NXOpen.PDM.PartOperationCreateBuilder) -> None:
        """
         Set the NXOpen.PDM.PartOperationCreateBuilder 
        """
        pass
import NXOpen
class RunCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Schematic.Mechanical.Run. """
    def CreateRunBuilder(self, run: Run) -> RunBuilder:
        """
         Creates a NXOpen.Schematic.Mechanical.RunBuilder. 
         Returns builder ( RunBuilder NXOpen.Schema): .
        """
        pass
    def FindObject(self, journalIdentifier: str) -> Run:
        """
         Finds the Schematic.Mechanical.Run with the given identifier as recorded in a journal.
                        An exception will be thrown if no object can be found with given name. 
         Returns run ( Run NXOpen.Schema):  Schematic.Mechanical.Run with this name. .
        """
        pass
import NXOpen
class RunsManager(NXOpen.Object): 
    """ Represents the Runs Manager used to manage runs,
            including loading and unloading runs, associatingdetaching runs tofrom the part, settingclearing
            the active run, and addingremoving components tofrom the runs
        """
    def AssociateRun(self, run: Run) -> None:
        """
         Associates the run. 
        """
        pass
    def CreateBranchBuilder(self, branch: Branch) -> BranchBuilder:
        """
         Creates a NXOpen.Schematic.Mechanical.BranchBuilder. 
         Returns builder ( BranchBuilder NXOpen.Schema): .
        """
        pass
    def CreateRunBuilder(self, run: Run) -> RunBuilder:
        """
         Creates a NXOpen.Schematic.Mechanical.RunBuilder. 
         Returns builder ( RunBuilder NXOpen.Schema): .
        """
        pass
    def DissociateRun(self, run: Run) -> None:
        """
         Dissociates the run. 
        """
        pass
    def GetActiveRun(self) -> Run:
        """
         Gets the only active run. 
         Returns run ( Run NXOpen.Schema): .
        """
        pass
    def GetLoadedRuns(self) -> List[Run]:
        """
         Gets the loaded runs. 
         Returns runs ( Run List[NXOpen.Sche): .
        """
        pass
    def LoadAndGetRun(self, identifer: str, revision: str) -> Run:
        """
         Loads and gets the run. 
         Returns run ( Run NXOpen.Schema): .
        """
        pass
    def LoadRun(self, identifer: str, revision: str) -> None:
        """
         Loads the run. 
        """
        pass
    def MakeRunInactive(self, run: Run) -> None:
        """
         Makes the run inactive. 
        """
        pass
    def SetActiveRun(self, run: Run) -> None:
        """
         Sets the run active. Only one run can be active, and the others will be inactive.
        """
        pass
import NXOpen.Schematic.Model
class Run(NXOpen.Schematic.Model.BaseObject): 
    """ Represents the Run class. """
    @property
    def Discipline(self) -> str:
        """
        Getter for property: (str) Discipline
         Returns the discipline  
            
         
        """
        pass
    @property
    def Insulation(self) -> str:
        """
        Getter for property: (str) Insulation
         Returns the insulation   
            
         
        """
        pass
    @property
    def Specification(self) -> str:
        """
        Getter for property: (str) Specification
         Returns the specification  
            
         
        """
        pass
    def GetBranches(self) -> List[Branch]:
        """
         Gets the branches in the run.
         Returns branches ( Branch List[NXOpen.Sche):  the collection of branches in the run .
        """
        pass
