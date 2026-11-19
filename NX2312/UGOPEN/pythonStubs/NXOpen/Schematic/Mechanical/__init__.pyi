from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen.Schematic.Model
##  Represents the Branch class.  <br> Instance of this can not directly created.  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class Branch(NXOpen.Schematic.Model.BaseObject): 
    """ Represents the Branch class. """


    ##  Gets the ordered objects in the branch.
    ##  @return objs (@link NXOpen.Schematic.Model.BaseObject List[NXOpen.Schematic.Model.BaseObject]@endlink):  the collection of ordered objects except direct connections in the branch. .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetOrderedObjects(branch: Branch) -> List[NXOpen.Schematic.Model.BaseObject]:
        """
         Gets the ordered objects in the branch.
         @return objs (@link NXOpen.Schematic.Model.BaseObject List[NXOpen.Schematic.Model.BaseObject]@endlink):  the collection of ordered objects except direct connections in the branch. .
        """
        pass
    
import NXOpen
import NXOpen.Schematic.Model
##  Represents the Connection class.  <br> Instance of this can not directly created.  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class Connection(NXOpen.Schematic.Model.Connection): 
    """ Represents the Connection class. """


    ##  Gets the connection insulation attribute owner.
    ##  @return attrOwner (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetInsulationAttributeOwner(connection: Connection) -> NXOpen.NXObject:
        """
         Gets the connection insulation attribute owner.
         @return attrOwner (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
        """
        pass
    
    ##  Gets the connection object attribute owner.
    ##  @return attrOwner (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetObjectAttributeOwner(connection: Connection) -> NXOpen.NXObject:
        """
         Gets the connection object attribute owner.
         @return attrOwner (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
        """
        pass
    
    ##  Gets the outlet junctions on the connection.
    ##  @return junctions (@link Junction List[NXOpen.Schematic.Mechanical.Junction]@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetOutletJunctions(connection: Connection) -> List[Junction]:
        """
         Gets the outlet junctions on the connection.
         @return junctions (@link Junction List[NXOpen.Schematic.Mechanical.Junction]@endlink): .
        """
        pass
    
    ##  Gets the connection stock attribute owner.
    ##  @return attrOwner (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStockAttributeOwner(connection: Connection) -> NXOpen.NXObject:
        """
         Gets the connection stock attribute owner.
         @return attrOwner (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
        """
        pass
    
import NXOpen
import NXOpen.Schematic.Model
##  Represents the Junction class.  <br> Instance of this can not directly created.  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class Junction(NXOpen.Schematic.Model.Node): 
    """ Represents the Junction class. """


    ##  Gets the junction classification attribute owner.
    ##  @return attrOwner (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetClassificationAttributeOwner(junction: Junction) -> NXOpen.NXObject:
        """
         Gets the junction classification attribute owner.
         @return attrOwner (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
        """
        pass
    
    ##  Gets the junction object attribute owner.
    ##  @return attrOwner (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetObjectAttributeOwner(junction: Junction) -> NXOpen.NXObject:
        """
         Gets the junction object attribute owner.
         @return attrOwner (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
        """
        pass
    
import NXOpen.Schematic.Model
##  Represents the Port class.  <br> Instance of this can not directly created.  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class Port(NXOpen.Schematic.Model.Port): 
    """ Represents the Port class. """


    ##  Gets the owning junction.
    ##  @return junction (@link Junction NXOpen.Schematic.Mechanical.Junction@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetOwningJunction(port: Port) -> Junction:
        """
         Gets the owning junction.
         @return junction (@link Junction NXOpen.Schematic.Mechanical.Junction@endlink): .
        """
        pass
    
import NXOpen
import NXOpen.PDM
##   @brief  Represents a RunBuilder.  
## 
##    <br> To create a new instance of this class, use @link NXOpen::Schematic::Mechanical::RunsManager::CreateRunBuilder  NXOpen::Schematic::Mechanical::RunsManager::CreateRunBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class RunBuilder(NXOpen.Builder): 
    """ <summary> Represents a RunBuilder. </summary> """


    ## Getter for property: (str) Discipline
    ##   the discipline  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def Discipline(self) -> str:
        """
        Getter for property: (str) Discipline
          the discipline  
            
         
        """
        pass
    
    ## Setter for property: (str) Discipline

    ##   the discipline  
    ##     
    ##  
    ## Setter License requirements: nx_diagramming ("NX Diagramming"), routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @Discipline.setter
    def Discipline(self, discipline: str):
        """
        Setter for property: (str) Discipline
          the discipline  
            
         
        """
        pass
    
    ## Getter for property: (str) DisplayName
    ##   the display name  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def DisplayName(self) -> str:
        """
        Getter for property: (str) DisplayName
          the display name  
            
         
        """
        pass
    
    ## Setter for property: (str) DisplayName

    ##   the display name  
    ##     
    ##  
    ## Setter License requirements: nx_diagramming ("NX Diagramming"), routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @DisplayName.setter
    def DisplayName(self, name: str):
        """
        Setter for property: (str) DisplayName
          the display name  
            
         
        """
        pass
    
    ## Getter for property: (str) Identifier
    ##   the identifier  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def Identifier(self) -> str:
        """
        Getter for property: (str) Identifier
          the identifier  
            
         
        """
        pass
    
    ## Setter for property: (str) Identifier

    ##   the identifier  
    ##     
    ##  
    ## Setter License requirements: nx_diagramming ("NX Diagramming"), routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @Identifier.setter
    def Identifier(self, id: str):
        """
        Setter for property: (str) Identifier
          the identifier  
            
         
        """
        pass
    
    ## Getter for property: (str) LineType
    ##   the line type  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return str
    @property
    def LineType(self) -> str:
        """
        Getter for property: (str) LineType
          the line type  
            
         
        """
        pass
    
    ## Setter for property: (str) LineType

    ##   the line type  
    ##     
    ##  
    ## Setter License requirements: nx_diagramming ("NX Diagramming"), routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @LineType.setter
    def LineType(self, lineType: str):
        """
        Setter for property: (str) LineType
          the line type  
            
         
        """
        pass
    
    ## Getter for property: (str) ObjectApplication
    ##   the application name of the run.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

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
    ## Setter License requirements: nx_diagramming ("NX Diagramming"), routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ObjectApplication.setter
    def ObjectApplication(self, objectApplication: str):
        """
        Setter for property: (str) ObjectApplication
          the application name of the run.  
             
         
        """
        pass
    
    ## Getter for property: (str) Specification
    ##   the specification  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def Specification(self) -> str:
        """
        Getter for property: (str) Specification
          the specification  
            
         
        """
        pass
    
    ## Setter for property: (str) Specification

    ##   the specification  
    ##     
    ##  
    ## Setter License requirements: nx_diagramming ("NX Diagramming"), routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @Specification.setter
    def Specification(self, specification: str):
        """
        Setter for property: (str) Specification
          the specification  
            
         
        """
        pass
    
    ## Getter for property: (bool) Standalone
    ##   whether the run is standalone run which will be reside in logical model part.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def Standalone(self) -> bool:
        """
        Getter for property: (bool) Standalone
          whether the run is standalone run which will be reside in logical model part.  
             
         
        """
        pass
    
    ## Setter for property: (bool) Standalone

    ##   whether the run is standalone run which will be reside in logical model part.  
    ##      
    ##  
    ## Setter License requirements: nx_diagramming ("NX Diagramming"), routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @Standalone.setter
    def Standalone(self, standalone: bool):
        """
        Setter for property: (bool) Standalone
          whether the run is standalone run which will be reside in logical model part.  
             
         
        """
        pass
    
    ##  Set the @link NXOpen::PDM::PartOperationCreateBuilder NXOpen::PDM::PartOperationCreateBuilder@endlink  
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_diagramming ("NX Diagramming"), routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ## <param name="createBuilder"> (@link NXOpen.PDM.PartOperationCreateBuilder NXOpen.PDM.PartOperationCreateBuilder@endlink) </param>
    def SetPartOperationCreateBuilder(builder: RunBuilder, createBuilder: NXOpen.PDM.PartOperationCreateBuilder) -> None:
        """
         Set the @link NXOpen::PDM::PartOperationCreateBuilder NXOpen::PDM::PartOperationCreateBuilder@endlink  
        """
        pass
    
import NXOpen
##  Represents a collection of @link Schematic::Mechanical::Run Schematic::Mechanical::Run@endlink .  <br> To obtain an instance of this class, refer to @link NXOpen::Part  NXOpen::Part @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 
## 
##   <br>  @deprecated Deprecated in NX2312.0.0.  This class is never used and can be safely removed.  <br> 

class RunCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of <ja_class>Schematic.Mechanical.Run</ja_class>. """


    ##  Creates a @link NXOpen::Schematic::Mechanical::RunBuilder NXOpen::Schematic::Mechanical::RunBuilder@endlink . 
    ##  @return builder (@link RunBuilder NXOpen.Schematic.Mechanical.RunBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Move to Run Manager.  <br> 

    ## License requirements: None.
    ##  @link Schematic::Mechanical::Run Schematic::Mechanical::Run@endlink  to be edited, if NULL then create a new one 
    def CreateRunBuilder(part: RunCollection, run: Run) -> RunBuilder:
        """
         Creates a @link NXOpen::Schematic::Mechanical::RunBuilder NXOpen::Schematic::Mechanical::RunBuilder@endlink . 
         @return builder (@link RunBuilder NXOpen.Schematic.Mechanical.RunBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link Schematic::Mechanical::Run Schematic::Mechanical::Run@endlink  with the given identifier as recorded in a journal.
    ##                 An exception will be thrown if no object can be found with given name. 
    ##  @return run (@link Run NXOpen.Schematic.Mechanical.Run@endlink):  @link Schematic::Mechanical::Run Schematic::Mechanical::Run@endlink  with this name. .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  This functionality is never used and can be safely removed.  <br> 

    ## License requirements: None.
    ##  Identifier to be found 
    def FindObject(part: RunCollection, journalIdentifier: str) -> Run:
        """
         Finds the @link Schematic::Mechanical::Run Schematic::Mechanical::Run@endlink  with the given identifier as recorded in a journal.
                        An exception will be thrown if no object can be found with given name. 
         @return run (@link Run NXOpen.Schematic.Mechanical.Run@endlink):  @link Schematic::Mechanical::Run Schematic::Mechanical::Run@endlink  with this name. .
        """
        pass
    
import NXOpen
##  Represents the Runs Manager used to manage runs,
##             including loading and unloading runs, associating/detaching runs to/from the part, setting/clearing
##             the active run, and adding/removing components to/from the runs
##          <br> To obtain an instance of this class, refer to @link NXOpen::Schematic::SchematicManager  NXOpen::Schematic::SchematicManager @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class RunsManager(NXOpen.Object): 
    """ Represents the Runs Manager used to manage runs,
            including loading and unloading runs, associating/detaching runs to/from the part, setting/clearing
            the active run, and adding/removing components to/from the runs
        """


    ##  Associates the run. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ## <param name="run"> (@link Run NXOpen.Schematic.Mechanical.Run@endlink) </param>
    def AssociateRun(part: RunsManager, run: Run) -> None:
        """
         Associates the run. 
        """
        pass
    
    ##  Creates a @link NXOpen::Schematic::Mechanical::RunBuilder NXOpen::Schematic::Mechanical::RunBuilder@endlink . 
    ##  @return builder (@link RunBuilder NXOpen.Schematic.Mechanical.RunBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ##  @link Schematic::Mechanical::Run Schematic::Mechanical::Run@endlink  to be edited, if NULL then create a new one 
    def CreateRunBuilder(part: RunsManager, run: Run) -> RunBuilder:
        """
         Creates a @link NXOpen::Schematic::Mechanical::RunBuilder NXOpen::Schematic::Mechanical::RunBuilder@endlink . 
         @return builder (@link RunBuilder NXOpen.Schematic.Mechanical.RunBuilder@endlink): .
        """
        pass
    
    ##  Dissociates the run. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ## <param name="run"> (@link Run NXOpen.Schematic.Mechanical.Run@endlink) </param>
    def DissociateRun(part: RunsManager, run: Run) -> None:
        """
         Dissociates the run. 
        """
        pass
    
    ##  Gets the only active run. 
    ##  @return run (@link Run NXOpen.Schematic.Mechanical.Run@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetActiveRun(part: RunsManager) -> Run:
        """
         Gets the only active run. 
         @return run (@link Run NXOpen.Schematic.Mechanical.Run@endlink): .
        """
        pass
    
    ##  Gets the loaded runs. 
    ##  @return runs (@link Run List[NXOpen.Schematic.Mechanical.Run]@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetLoadedRuns(part: RunsManager) -> List[Run]:
        """
         Gets the loaded runs. 
         @return runs (@link Run List[NXOpen.Schematic.Mechanical.Run]@endlink): .
        """
        pass
    
    ##  Loads the run. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ## <param name="identifer"> (str) </param>
    ## <param name="revision"> (str) </param>
    def LoadRun(part: RunsManager, identifer: str, revision: str) -> None:
        """
         Loads the run. 
        """
        pass
    
    ##  Makes the run inactive. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ## <param name="run"> (@link Run NXOpen.Schematic.Mechanical.Run@endlink) </param>
    def MakeRunInactive(part: RunsManager, run: Run) -> None:
        """
         Makes the run inactive. 
        """
        pass
    
    ##  Sets the run active. Only one run can be active, and the others will be inactive.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ## <param name="run"> (@link Run NXOpen.Schematic.Mechanical.Run@endlink) </param>
    def SetActiveRun(part: RunsManager, run: Run) -> None:
        """
         Sets the run active. Only one run can be active, and the others will be inactive.
        """
        pass
    
import NXOpen.Schematic.Model
##  Represents the Run class.  <br> To create or edit an instance of this class, use @link NXOpen::Schematic::Mechanical::RunBuilder  NXOpen::Schematic::Mechanical::RunBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class Run(NXOpen.Schematic.Model.BaseObject): 
    """ Represents the Run class. """


    ## Getter for property: (str) Discipline
    ##   the discipline  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def Discipline(self) -> str:
        """
        Getter for property: (str) Discipline
          the discipline  
            
         
        """
        pass
    
    ## Getter for property: (str) Specification
    ##   the specification  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def Specification(self) -> str:
        """
        Getter for property: (str) Specification
          the specification  
            
         
        """
        pass
    
    ##  Gets the branches in the run.
    ##  @return branches (@link Branch List[NXOpen.Schematic.Mechanical.Branch]@endlink):  the collection of branches in the run .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBranches(run: Run) -> List[Branch]:
        """
         Gets the branches in the run.
         @return branches (@link Branch List[NXOpen.Schematic.Mechanical.Branch]@endlink):  the collection of branches in the run .
        """
        pass
    
## @package NXOpen.Schematic.Mechanical
## Classes, Enums and Structs under NXOpen.Schematic.Mechanical namespace

