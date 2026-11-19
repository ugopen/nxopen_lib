from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class CircuitCheckActionList(NXOpen.NXObject): 
    """  Class representing a list of circuit check actions  """
    def Deselect(self, action: CircuitCheckAction) -> None:
        """
         Deselect the specified action to avoid using it in the quality audit.
                     
        """
        pass
    def DeselectAll(self) -> None:
        """
         Deselect all available actions.
                     
        """
        pass
    def GetAction(self, id: CircuitCheckAction.Id) -> CircuitCheckAction:
        """
         Get the action by id. See NXOpen.CAE.Magnet.CircuitCheckAction.Id for the full list of possible actions.
                     
         Returns action ( CircuitCheckAction NXOpen.C): .
        """
        pass
    def GetSelectedActions(self) -> List[CircuitCheckAction]:
        """
         Returns an array of all selected actions.
                     
         Returns actions ( CircuitCheckAction List[NXOpen):  The selected actions .
        """
        pass
    def IsSelected(self, action: CircuitCheckAction) -> bool:
        """
         Tells if the action is to be used in the quality audit.
                     
         Returns selected (bool): .
        """
        pass
    def Select(self, action: CircuitCheckAction) -> None:
        """
         Select the specified action to be used in the quality audit.
                     
        """
        pass
    def SelectAll(self) -> None:
        """
         Select all available actions.
                     
        """
        pass
import NXOpen
class CircuitCheckAction(NXOpen.NXObject): 
    """  Class representing an individual circuit check action  """
    class Id(Enum):
        """
        Members Include: 
         |CoilsWithExcitation| 
         |ComponentsWithoutReference| 
         |OpenConnections| 
         |SolutionCompatibility| 
         |SubcircuitTags| 
         |UniqueCoils| 
         |UnplacedCoils| 
         |UnreferencedSimulationObjects| 

        """
        CoilsWithExcitation: int
        ComponentsWithoutReference: int
        OpenConnections: int
        SolutionCompatibility: int
        SubcircuitTags: int
        UniqueCoils: int
        UnplacedCoils: int
        UnreferencedSimulationObjects: int
        @staticmethod
        def ValueOf(value: int) -> CircuitCheckAction.Id:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ActionId(self) -> CircuitCheckAction.Id:
        """
        Getter for property: ( CircuitCheckAction.Id NXOpen.C) ActionId
         Returns the action id   
            
         
        """
        pass
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the description of this action   
            
         
        """
        pass
    def GetResults(self) -> List[CircuitCheckResult]:
        """
         Get the CAE.Magnet.CircuitCheckResult list obtained from the latest check 
         Returns results ( CircuitCheckResult List[NXOpen): .
        """
        pass
    def Perform(self) -> None:
        """
         Performs the action. 
        """
        pass
import NXOpen.CAE
class CircuitCheckCoilsWithExcitationResult(CircuitCheckResult): 
    """  This result shows the coils that have excitation assigned. """
    def GetCoil(self) -> NXOpen.CAE.SimBC:
        """
         Gets the component of this result 
         Returns component ( NXOpen.CAE.SimBC): .
        """
        pass
class CircuitCheckCoilsWithExcitation(CircuitCheckAction): 
    """  This action has as result coils that have excitation assigned. """
    pass
class CircuitCheckComponentsWithoutReferenceResult(CircuitCheckResult): 
    """  This result shows the circuit component that is missing a reference. """
    def GetComponent(self) -> CircuitComponent:
        """
         Gets the circuit component of this result 
         Returns component ( CircuitComponent NXOpen.C): .
        """
        pass
class CircuitCheckComponentsWithoutReference(CircuitCheckAction): 
    """  This action has as result a circuit component that is missing a reference. """
    pass
import NXOpen
class CircuitCheckManager(NXOpen.Object): 
    """  The Circuit Check Manager class offers means to check for errors in circuit designs  """
    @property
    def ActionList(self) -> CircuitCheckActionList:
        """
        Getter for property: ( CircuitCheckActionList NXOpen.C) ActionList
         Returns the action list   
            
         
        """
        pass
    def FindObject(journalIdentifier: str) -> NXOpen.INXObject:
        """
         Finds the  NXOpen.INXObject  with the given identifier as recorded in a journal. 
                    An object may not return the same value as its JournalIdentifier in different versions of 
                    the software. However newer versions of the software should find the same object when 
                    FindObject is passed older versions of its journal identifier. In general, this method 
                    should not be used in handwritten code and exists to support record and playback of journals.
                    An exception will be thrown if no object can be found with the given journal identifier. 
         Returns found ( NXOpen.INXObject):  An object matching the journal identifier .
        """
        pass
    def PerformActions(inputActions: List[CircuitCheckAction]) -> None:
        """
         This method performs circuit checks on the selected objects. 
        """
        pass
import NXOpen
class CircuitCheckOpenConnectionsResult(CircuitCheckResult): 
    """  This result shows the connections that have an open end. """
    def GetObject(self) -> NXOpen.NXObject:
        """
         Gets the component of this result 
         Returns component ( NXOpen.NXObject): .
        """
        pass
class CircuitCheckOpenConnections(CircuitCheckAction): 
    """  This action has as result open connections. """
    pass
import NXOpen
class CircuitCheckResult(NXOpen.NXObject): 
    """  The Circuit Check Result class offers means to access information about specific problems found while performing specific circuit checks. """
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the description of this result    
            
         
        """
        pass
    @property
    def OwningAction(self) -> CircuitCheckAction:
        """
        Getter for property: ( CircuitCheckAction NXOpen.C) OwningAction
         Returns the owning action    
            
         
        """
        pass
import NXOpen.CAE
class CircuitCheckSolutionCompatibilityResult(CircuitCheckResult): 
    """  This result shows the circuit components that are not compatible with the solution. """
    def GetComponent(self) -> CircuitComponent:
        """
         Gets the component of this result 
         Returns component ( CircuitComponent NXOpen.C): .
        """
        pass
    def GetSolution(self) -> NXOpen.CAE.SimSolution:
        """
         Gets the solution of this result 
         Returns solution ( NXOpen.CAE.SimSolution): .
        """
        pass
class CircuitCheckSolutionCompatibility(CircuitCheckAction): 
    """  This action has as result circuit components that are not compatible with the solution. """
    pass
class CircuitCheckSubcircuitTagResult(CircuitCheckResult): 
    """  This result shows a subcircuit that is missing tags. """
    def GetSubcircuit(self) -> Circuit:
        """
         Gets the subcircuit that does not contain any tags. 
         Returns subcircuit ( Circuit NXOpen.C): .
        """
        pass
class CircuitCheckSubcircuitTag(CircuitCheckAction): 
    """  This action has as result subcircuits that are missing tags. """
    pass
import NXOpen.CAE
class CircuitCheckUniqueCoilsResult(CircuitCheckResult): 
    """  This result shows the coils that are referenced multiple times. """
    def GetCoil(self) -> NXOpen.CAE.SimBC:
        """
         Gets the component of this result 
         Returns component ( NXOpen.CAE.SimBC): .
        """
        pass
class CircuitCheckUniqueCoils(CircuitCheckAction): 
    """  This action has as result coils that are referenced multiple times. """
    pass
import NXOpen.CAE
class CircuitCheckUnplacedCoilsResult(CircuitCheckResult): 
    """  This result shows the coils from the Simulation that are not placed in the circuit. """
    def GetCoil(self) -> NXOpen.CAE.SimBC:
        """
         Gets the component of this result 
         Returns component ( NXOpen.CAE.SimBC): .
        """
        pass
class CircuitCheckUnplacedCoils(CircuitCheckAction): 
    """  This action has as result coils from the Simulation that are not placed in the circuit. """
    pass
import NXOpen.CAE
class CircuitCheckUnreferencedSimulationObjectsResult(CircuitCheckResult): 
    """  This result shows the simulation objects that are not referenced in the Solution. """
    def GetSimulationObject(self) -> NXOpen.CAE.SimBC:
        """
         Gets the component of this result 
         Returns component ( NXOpen.CAE.SimBC): .
        """
        pass
class CircuitCheckUnreferencedSimulationObjects(CircuitCheckAction): 
    """  This action has as result simulation objects that are not referenced in the Solution. """
    pass
import NXOpen
class CircuitCollection(NXOpen.TaggedObjectCollection): 
    """  Provides methods for managing NXOpen.CAE.Magnet.Circuit """
    def CreateCircuit(self, name: str) -> Circuit:
        """
         Creates a magnet circuit of given name 
         Returns circuit ( Circuit NXOpen.C): .
        """
        pass
    def CreateRotorCageBuilder(self) -> RotorCageBuilder:
        """
         Creates the builder of a NXOpen.CAE.Magnet.Circuit object with type JA_MAGNET_CIRCUIT_Type_RotorCage. 
         Returns builder ( RotorCageBuilder NXOpen.C): .
        """
        pass
    def CreateSubcircuit(self, name: str) -> Circuit:
        """
         Creates a magnet subcircuit of given name 
         Returns circuit ( Circuit NXOpen.C): .
        """
        pass
    def CreateWindingBuilder(self) -> WindingBuilder:
        """
         Creates the builder of a NXOpen.CAE.Magnet.Circuit object with type JA_MAGNET_CIRCUIT_Type_Winding. 
         Returns builder ( WindingBuilder NXOpen.C): .
        """
        pass
    def FindObject(self, name: str) -> Circuit:
        """
         Finds the  NXOpen.CAE.Magnet.Circuit  with the given name.
                        An exception will be thrown if no object can be found with the given name. 
         Returns circuit ( Circuit NXOpen.C): .
        """
        pass
    def Information(self) -> None:
        """
         Displays the information about this Circuit Collection in the listing window; the window must be open prior to this call. 
        """
        pass
import NXOpen
import NXOpen.CAE
class CircuitComponentBuilder(NXOpen.Builder): 
    """  This is a builder to the CAE.Magnet.CircuitComponent class.
                      Objects of type CAE.Magnet.CircuitComponent can be created and edited
                      only through this class """
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name of the circuit component   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name of the circuit component   
            
         
        """
        pass
    @property
    def PropertyTable(self) -> NXOpen.CAE.PropertyTable:
        """
        Getter for property: ( NXOpen.CAE.PropertyTable) PropertyTable
         Returns the property table for the  CAE::Magnet::CircuitComponent  object   
            
         
        """
        pass
import NXOpen
class CircuitComponent(NXOpen.NXObject): 
    """  Represents a magnet circuit component  """
    def CloneCircuitComponent(self) -> CircuitComponent:
        """
         Clones a circuit component. 
         Returns componentClone ( CircuitComponent NXOpen.C):  cloned circuit component .
        """
        pass
    def CreateComponentBuilder(self) -> CircuitComponentBuilder:
        """
         Creates the builder of a NXOpen.CAE.Magnet.CircuitComponent object to edit. 
         Returns builder ( CircuitComponentBuilder NXOpen.C): .
        """
        pass
    def GetPort(self, index: int) -> Port:
        """
         Gets a port. 
         Returns port ( Port NXOpen.C): .
        """
        pass
    def Information(self) -> None:
        """
         Displays the information about this Circuit Component in the listing window; the window must be open prior to this call. 
        """
        pass
import NXOpen
class Circuit(NXOpen.NXObject): 
    """  Represents a magnet circuit  """
    class Type(Enum):
        """
        Members Include: 
         |Circuit| 
         |Winding|  used as subcomponent 
         |Subcircuit|  used as subcomponent 
         |RotorCage| 

        """
        Circuit: int
        Winding: int
        Subcircuit: int
        RotorCage: int
        @staticmethod
        def ValueOf(value: int) -> Circuit.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name of the circuit   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name of the circuit   
            
         
        """
        pass
    def CloneCircuit(self) -> Tuple[Circuit, str]:
        """
         
                            Clones a circuit.
                        
                        
                            If the active solution does not reference a circuit yet and the clone is valid for it,
                            a reference will be added.
                         
         Returns A tuple consisting of (circuitClone, message). 
         - circuitClone is:  Circuit NXOpen.C. cloned circuit .
         - message is: str. If applicable, this gives an explanation,
                                                       why a circuit reference was not added to the active solution. .

        """
        pass
    def CreateComponentBuilderByDescriptor(self, descriptorName: str) -> CircuitComponentBuilder:
        """
         Creates the builder of a new NXOpen.CAE.Magnet.CircuitComponent object. 
         Returns builder ( CircuitComponentBuilder NXOpen.C): .
        """
        pass
    def CreateConnection(self, startPort: Port, endPort: Port) -> Connection:
        """
         Creates a connection. 
         Returns connection ( Connection NXOpen.C):  new connection .
        """
        pass
    def Information(self) -> None:
        """
         Displays the information about this Circuit in the listing window; the window must be open prior to this call. 
        """
        pass
import NXOpen
import NXOpen.Diagramming
class Connection(NXOpen.Diagramming.Connection): 
    """  Represents a magnet connection  """
    def SetEndPort(self, port: Port) -> None:
        """
         Sets the referenced port. 
        """
        pass
    def SetGeometry(self, geometryPoints: List[NXOpen.Point2d]) -> None:
        """
         Sets the shape of the connection. 
        """
        pass
    def SetStartPort(self, port: Port) -> None:
        """
         Sets the referencing port. 
        """
        pass
import NXOpen
class GlobalSelectionBuilder(NXOpen.Builder): 
    """ Global Selection """
    @property
    def Selection(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) Selection
         Returns the selected objects   
            
         
        """
        pass
import NXOpen
import NXOpen.Diagramming
class Node(NXOpen.Diagramming.Node): 
    """  Represents a magnet node  """
    def GetCircuitComponent(self) -> CircuitComponent:
        """
         Gets the circuit component. 
         Returns component ( CircuitComponent NXOpen.C): .
        """
        pass
    def SetLocation(self, location: NXOpen.Point2d) -> None:
        """
         Sets the location. 
        """
        pass
    def SetRotation(self, rotation: float) -> None:
        """
         Sets the rotation. 
        """
        pass
import NXOpen.Diagramming
class Port(NXOpen.Diagramming.Port): 
    """  Represents a magnet port  """
    def GetPortId(self) -> str:
        """
         Gets the port id. 
         Returns portId (str): .
        """
        pass
import NXOpen
import NXOpen.CAE
import NXOpen.Fields
class RotorCageBuilder(NXOpen.Builder): 
    """  This is a builder to the CAE.Magnet.Circuit class with type JA_MAGNET_CIRCUIT_Type_RotorCage.
                      Such objects can be created and edited only through this class """
    class Periodic(Enum):
        """
        Members Include: 
         |NotSet| 
         |FullModel| 
         |Even| 
         |Odd| 

        """
        NotSet: int
        FullModel: int
        Even: int
        Odd: int
        @staticmethod
        def ValueOf(value: int) -> RotorCageBuilder.Periodic:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Endring(self) -> bool:
        """
        Getter for property: (bool) Endring
         Returns the information if there is an end ring.  
             
         
        """
        pass
    @Endring.setter
    def Endring(self, endring: bool):
        """
        Setter for property: (bool) Endring
         Returns the information if there is an end ring.  
             
         
        """
        pass
    @property
    def EndringInductance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EndringInductance
         Returns the end ring inductance value.  
             
         
        """
        pass
    @property
    def EndringResistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EndringResistance
         Returns the end ring resistance value.  
             
         
        """
        pass
    @property
    def InitialCurrent(self) -> NXOpen.Fields.FieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.FieldWrapper) InitialCurrent
         Returns the initial current for each coil.  
          
                        independent variable: coil number
                        dependent variable: initial current  
         
        """
        pass
    @InitialCurrent.setter
    def InitialCurrent(self, initialCurrent: NXOpen.Fields.FieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.FieldWrapper) InitialCurrent
         Returns the initial current for each coil.  
          
                        independent variable: coil number
                        dependent variable: initial current  
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name of the rotor cage.  
             
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name of the rotor cage.  
             
         
        """
        pass
    @property
    def Overhang(self) -> bool:
        """
        Getter for property: (bool) Overhang
         Returns the information if there is an overhang.  
             
         
        """
        pass
    @Overhang.setter
    def Overhang(self, overhang: bool):
        """
        Setter for property: (bool) Overhang
         Returns the information if there is an overhang.  
             
         
        """
        pass
    @property
    def OverhangInductance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) OverhangInductance
         Returns the overhang inductance value.  
             
         
        """
        pass
    @property
    def OverhangResistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) OverhangResistance
         Returns the overhang resistance value.  
             
         
        """
        pass
    @property
    def Periodicity(self) -> RotorCageBuilder.Periodic:
        """
        Getter for property: ( RotorCageBuilder.Periodic NXOpen.C) Periodicity
         Returns the periodicity.  
             
         
        """
        pass
    @Periodicity.setter
    def Periodicity(self, periodicity: RotorCageBuilder.Periodic):
        """
        Setter for property: ( RotorCageBuilder.Periodic NXOpen.C) Periodicity
         Returns the periodicity.  
             
         
        """
        pass
    def AddCoil(self, coil: NXOpen.CAE.SimBC) -> None:
        """
         Adds a coil to the rotor cage. 
        """
        pass
import NXOpen.Diagramming
class Sheet(NXOpen.Diagramming.Sheet): 
    """  Represents a magnet sheet  """
    def ActivateGrid(self) -> None:
        """
         Sets the grid properties to show a rectangular grid and snap to it. 
        """
        pass
import NXOpen
import NXOpen.CAE
class WindingBuilder(NXOpen.Builder): 
    """  This is a builder to the CAE.Magnet.Circuit class with type JA_MAGNET_CIRCUIT_Type_Winding.
                      Such objects can be created and edited only through this class """
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name of the winding.  
             
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name of the winding.  
             
         
        """
        pass
    @property
    def NumParallelPaths(self) -> int:
        """
        Getter for property: (int) NumParallelPaths
         Returns the number of parallel paths.  
             
         
        """
        pass
    @NumParallelPaths.setter
    def NumParallelPaths(self, numParallelPaths: int):
        """
        Setter for property: (int) NumParallelPaths
         Returns the number of parallel paths.  
             
         
        """
        pass
    def AddCoil(self, coil: NXOpen.CAE.SimBC) -> None:
        """
         Adds a coil to the winding. 
        """
        pass
