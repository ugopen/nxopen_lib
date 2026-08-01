from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class AnalysisParamsBuilder(NXOpen.Builder): 
    """ Represents a MoldCooling.AnalysisParams builder """
    class SimulationTypeEnum(Enum):
        """
        Members Include: 
         |SteadyState|  Steady State Simulation 
         |Transient|  Transient Simulation 

        """
        SteadyState: int
        Transient: int
        @staticmethod
        def ValueOf(value: int) -> AnalysisParamsBuilder.SimulationTypeEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TimeStepOptionEnum(Enum):
        """
        Members Include: 
         |Automatic|  Use the default automatic time step option 
         |NumSteps|  Specify a number of time steps 
         |Constant|  Specify a constant time step value 

        """
        Automatic: int
        NumSteps: int
        Constant: int
        @staticmethod
        def ValueOf(value: int) -> AnalysisParamsBuilder.TimeStepOptionEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TransientTargetEnum(Enum):
        """
        Members Include: 
         |EndTime|  Stop after end-type is reached 
         |Temperature|  Stop when target temperature is reached 

        """
        EndTime: int
        Temperature: int
        @staticmethod
        def ValueOf(value: int) -> AnalysisParamsBuilder.TransientTargetEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ConstantTimeStep(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ConstantTimeStep
         Returns the constant time step value   
            
         
        """
        pass
    @property
    def EndTime(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EndTime
         Returns the end time for a transient simulation   
            
         
        """
        pass
    @property
    def FluidMeshResolution(self) -> int:
        """
        Getter for property: (int) FluidMeshResolution
         Returns the fluid mesh resolution   
            
         
        """
        pass
    @FluidMeshResolution.setter
    def FluidMeshResolution(self, fluidMeshResolution: int):
        """
        Setter for property: (int) FluidMeshResolution
         Returns the fluid mesh resolution   
            
         
        """
        pass
    @property
    def MaxEndTime(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxEndTime
         Returns the maximum end time for a temperature target transient simulation   
            
         
        """
        pass
    @property
    def MeshResolution(self) -> int:
        """
        Getter for property: (int) MeshResolution
         Returns the mesh resolution   
            
         
        """
        pass
    @MeshResolution.setter
    def MeshResolution(self, meshResolution: int):
        """
        Setter for property: (int) MeshResolution
         Returns the mesh resolution   
            
         
        """
        pass
    @property
    def MeshSizeFactor(self) -> int:
        """
        Getter for property: (int) MeshSizeFactor
         Returns the mesh size factor   
            
         
        """
        pass
    @MeshSizeFactor.setter
    def MeshSizeFactor(self, meshSizeFactor: int):
        """
        Setter for property: (int) MeshSizeFactor
         Returns the mesh size factor   
            
         
        """
        pass
    @property
    def MoldTemperature(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MoldTemperature
         Returns the initial mold temperature   
            
         
        """
        pass
    @property
    def NumTimeSteps(self) -> int:
        """
        Getter for property: (int) NumTimeSteps
         Returns the number of time steps   
            
         
        """
        pass
    @NumTimeSteps.setter
    def NumTimeSteps(self, numTimeSteps: int):
        """
        Setter for property: (int) NumTimeSteps
         Returns the number of time steps   
            
         
        """
        pass
    @property
    def PartTemperature(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PartTemperature
         Returns the initial part temperature   
            
         
        """
        pass
    @property
    def PhaseChangeActivation(self) -> bool:
        """
        Getter for property: (bool) PhaseChangeActivation
         Returns the phase change activation   
            
         
        """
        pass
    @PhaseChangeActivation.setter
    def PhaseChangeActivation(self, phaseChangeActivation: bool):
        """
        Setter for property: (bool) PhaseChangeActivation
         Returns the phase change activation   
            
         
        """
        pass
    @property
    def SimulationType(self) -> AnalysisParamsBuilder.SimulationTypeEnum:
        """
        Getter for property: ( AnalysisParamsBuilder.SimulationTypeEnum NXOpen.M) SimulationType
         Returns the type of simulation   
            
         
        """
        pass
    @SimulationType.setter
    def SimulationType(self, simulationType: AnalysisParamsBuilder.SimulationTypeEnum):
        """
        Setter for property: ( AnalysisParamsBuilder.SimulationTypeEnum NXOpen.M) SimulationType
         Returns the type of simulation   
            
         
        """
        pass
    @property
    def TargetTemperature(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TargetTemperature
         Returns the temperature target for a transient simulation   
            
         
        """
        pass
    @property
    def TimeStepOption(self) -> AnalysisParamsBuilder.TimeStepOptionEnum:
        """
        Getter for property: ( AnalysisParamsBuilder.TimeStepOptionEnum NXOpen.M) TimeStepOption
         Returns the time step option   
            
         
        """
        pass
    @TimeStepOption.setter
    def TimeStepOption(self, timeStepOption: AnalysisParamsBuilder.TimeStepOptionEnum):
        """
        Setter for property: ( AnalysisParamsBuilder.TimeStepOptionEnum NXOpen.M) TimeStepOption
         Returns the time step option   
            
         
        """
        pass
    @property
    def TransientTargetType(self) -> AnalysisParamsBuilder.TransientTargetEnum:
        """
        Getter for property: ( AnalysisParamsBuilder.TransientTargetEnum NXOpen.M) TransientTargetType
         Returns the target type of the transient simulation   
            
         
        """
        pass
    @TransientTargetType.setter
    def TransientTargetType(self, transientTargetType: AnalysisParamsBuilder.TransientTargetEnum):
        """
        Setter for property: ( AnalysisParamsBuilder.TransientTargetEnum NXOpen.M) TransientTargetType
         Returns the target type of the transient simulation   
            
         
        """
        pass
import NXOpen
class AnalysisParams(NXOpen.NXObject): 
    """ Encapsulates the various parameters needed for a mold cooling simulation """
    pass
import NXOpen
class CircuitBuilder(NXOpen.Builder): 
    """ Represents a MoldCooling.Circuit builder """
    class WallFrictionType(Enum):
        """
        Members Include: 
         |Smooth|  Smooth     
         |Rough|  Rough 

        """
        Smooth: int
        Rough: int
        @staticmethod
        def ValueOf(value: int) -> CircuitBuilder.WallFrictionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Diameter
         Returns the cooling circuit section diameter   
            
         
        """
        pass
    @property
    def Inlets(self) -> NXOpen.SelectPointList:
        """
        Getter for property: ( NXOpen.SelectPointList) Inlets
         Returns the cooling circuit inlets   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the cooling circuit name   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the cooling circuit name   
            
         
        """
        pass
    @property
    def Outlets(self) -> NXOpen.SelectPointList:
        """
        Getter for property: ( NXOpen.SelectPointList) Outlets
         Returns the cooling circuit outlets   
            
         
        """
        pass
    @property
    def Path(self) -> NXOpen.SelectCurveList:
        """
        Getter for property: ( NXOpen.SelectCurveList) Path
         Returns the cooling circuit path   
            
         
        """
        pass
    @property
    def RoughnessHeight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RoughnessHeight
         Returns the cooling circuit roughness height   
            
         
        """
        pass
    @property
    def WallFriction(self) -> CircuitBuilder.WallFrictionType:
        """
        Getter for property: ( CircuitBuilder.WallFrictionType NXOpen.M) WallFriction
         Returns the cooling circuit wall friction type   
            
         
        """
        pass
    @WallFriction.setter
    def WallFriction(self, wallFriction: CircuitBuilder.WallFrictionType):
        """
        Setter for property: ( CircuitBuilder.WallFrictionType NXOpen.M) WallFriction
         Returns the cooling circuit wall friction type   
            
         
        """
        pass
import NXOpen
class CircuitCollection(NXOpen.TaggedObjectCollection): 
    """  Represents collection MoldCooling.Circuit. """
    def FindObject(part: NXOpen.Part, name: str) -> Circuit:
        """
         Finds a cooling circuit with the specified name 
         Returns found ( Circuit NXOpen.M): .
        """
        pass
    def GetCircuits(part: NXOpen.Part) -> List[Circuit]:
        """
         Returns the list of cooling circuits 
         Returns circuits ( Circuit List[NXOpen): .
        """
        pass
import NXOpen
class CircuitParamsBuilder(NXOpen.Builder): 
    """ Represents a MoldCooling.CircuitParams builder """
    class FlowModeOption(Enum):
        """
        Members Include: 
         |VolumeFlowRate| 
         |StaticPressureGauge| 

        """
        VolumeFlowRate: int
        StaticPressureGauge: int
        @staticmethod
        def ValueOf(value: int) -> CircuitParamsBuilder.FlowModeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FlowMode(self) -> CircuitParamsBuilder.FlowModeOption:
        """
        Getter for property: ( CircuitParamsBuilder.FlowModeOption NXOpen.M) FlowMode
         Returns the flow mode   
            
         
        """
        pass
    @FlowMode.setter
    def FlowMode(self, flowMode: CircuitParamsBuilder.FlowModeOption):
        """
        Setter for property: ( CircuitParamsBuilder.FlowModeOption NXOpen.M) FlowMode
         Returns the flow mode   
            
         
        """
        pass
    @property
    def FluidMaterial(self) -> NXOpen.PhysicalMaterial:
        """
        Getter for property: ( NXOpen.PhysicalMaterial) FluidMaterial
         Returns the fluid material   
            
         
        """
        pass
    @FluidMaterial.setter
    def FluidMaterial(self, fluidMaterial: NXOpen.PhysicalMaterial):
        """
        Setter for property: ( NXOpen.PhysicalMaterial) FluidMaterial
         Returns the fluid material   
            
         
        """
        pass
    @property
    def InletStaticPressure(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InletStaticPressure
         Returns the inlet static pressure   
            
         
        """
        pass
    @property
    def InletTemperature(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InletTemperature
         Returns the inlet temperature   
            
         
        """
        pass
    @property
    def InletVolumeFlowRate(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InletVolumeFlowRate
         Returns the inlet volume flow rate   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name of the thermal parameter object   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name of the thermal parameter object   
            
         
        """
        pass
    @property
    def OutletStaticPressure(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) OutletStaticPressure
         Returns the outlet static pressure   
            
         
        """
        pass
import NXOpen
class CircuitParamsCollection(NXOpen.TaggedObjectCollection): 
    """  Represents collection MoldCooling.CircuitParams. """
    def FindObject(part: NXOpen.Part, name: str) -> CircuitParams:
        """
         Finds a cooling circuit fluid parameters set with the specified name 
         Returns found ( CircuitParams NXOpen.M): .
        """
        pass
    def GetParams(part: NXOpen.Part) -> List[CircuitParams]:
        """
         Returns the list of cooling circuit fluid parameters 
         Returns params ( CircuitParams List[NXOpen): .
        """
        pass
import NXOpen
class CircuitParams(NXOpen.NXObject): 
    """ Encapsulates the various parameters needed for a mold cooling simulation """
    pass
import NXOpen
class Circuit(NXOpen.NXObject): 
    """ Represents a mold cooling circuit """
    def AssignParams(self, params: CircuitParams) -> None:
        """
         Assigns thermal parameters to the circuit. The circuit actually creates an internal reference
                    to the MoldCooling.CircuitParams object and you can assign the same 
                    parameter set to more than one circuit. 
        """
        pass
    def GetAssignedParams(self) -> CircuitParams:
        """
         Returns the MoldCooling.CircuitParams object assigned to that cooling circuit 
         Returns params ( CircuitParams NXOpen.M): .
        """
        pass
import NXOpen
class FlowCircuitBuilder(NXOpen.Builder): 
    """ Represents a MoldCooling.Circuit builder """
    class WallFrictionType(Enum):
        """
        Members Include: 
         |Smooth|  Smooth 
         |Rough|  Rough 

        """
        Smooth: int
        Rough: int
        @staticmethod
        def ValueOf(value: int) -> FlowCircuitBuilder.WallFrictionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CircuitBodies(self) -> NXOpen.SelectBodyList:
        """
        Getter for property: ( NXOpen.SelectBodyList) CircuitBodies
         Returns the cooling circuit channel bodies   
            
         
        """
        pass
    @property
    def Inlets(self) -> NXOpen.SelectFaceList:
        """
        Getter for property: ( NXOpen.SelectFaceList) Inlets
         Returns the cooling circuit inlet faces   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the cooling circuit name   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the cooling circuit name   
            
         
        """
        pass
    @property
    def Outlets(self) -> NXOpen.SelectFaceList:
        """
        Getter for property: ( NXOpen.SelectFaceList) Outlets
         Returns the cooling circuit outlet faces   
            
         
        """
        pass
    @property
    def RoughnessHeight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RoughnessHeight
         Returns the cooling circuit roughness height   
            
         
        """
        pass
    @property
    def WallFriction(self) -> FlowCircuitBuilder.WallFrictionType:
        """
        Getter for property: ( FlowCircuitBuilder.WallFrictionType NXOpen.M) WallFriction
         Returns the cooling circuit wall friction type   
            
         
        """
        pass
    @WallFriction.setter
    def WallFriction(self, wallFriction: FlowCircuitBuilder.WallFrictionType):
        """
        Setter for property: ( FlowCircuitBuilder.WallFrictionType NXOpen.M) WallFriction
         Returns the cooling circuit wall friction type   
            
         
        """
        pass
import NXOpen
class Manager(NXOpen.Object): 
    """  Manager class for the mold cooling application. This is the main entry point to access and create mold cooling objects. """
    class AnalysisContext(Enum):
        """
        Members Include: 
         |Thermal|  Thermal Mold Cooling Analysis Context 
         |Flow|  Coupled Thermal-Flow Mold Cooling Analysis Context 

        """
        Thermal: int
        Flow: int
        @staticmethod
        def ValueOf(value: int) -> Manager.AnalysisContext:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Circuits() -> CircuitCollection:
        """
         Returns cooling circuits collection 
        """
        pass
    @property
    def CircuitFluidParams() -> CircuitParamsCollection:
        """
         Returns cooling circuits collection 
        """
        pass
    def CreateAnalysisParamsBuilder(part: NXOpen.Part, params: AnalysisParams) -> AnalysisParamsBuilder:
        """
         Creates a NXOpen.MoldCooling.AnalysisParamsBuilder. 
         Returns builder ( AnalysisParamsBuilder NXOpen.M): .
        """
        pass
    def CreateCircuitBuilder(part: NXOpen.Part, circuit: Circuit) -> CircuitBuilder:
        """
         Creates a NXOpen.MoldCooling.CircuitBuilder. 
         Returns builder ( CircuitBuilder NXOpen.M): .
        """
        pass
    def CreateCircuitParamsBuilder(part: NXOpen.Part, params: CircuitParams) -> CircuitParamsBuilder:
        """
         Creates a NXOpen.MoldCooling.CircuitParamsBuilder. 
         Returns builder ( CircuitParamsBuilder NXOpen.M): .
        """
        pass
    def CreateFlowCircuitBuilder(part: NXOpen.Part, circuit: Circuit) -> FlowCircuitBuilder:
        """
         Creates a NXOpen.MoldCooling.FlowCircuitBuilder. 
         Returns builder ( FlowCircuitBuilder NXOpen.M): .
        """
        pass
    def CreateMoldBodyBuilder(part: NXOpen.Part, mold: MoldBody) -> MoldBodyBuilder:
        """
         Creates a NXOpen.MoldCooling.MoldBodyBuilder. 
         Returns builder ( MoldBodyBuilder NXOpen.M): .
        """
        pass
    def DeleteCircuit(part: NXOpen.Part, circuit: Circuit) -> None:
        """
         Deletes the selected cooling circuit 
        """
        pass
    def DeleteCircuitParams(part: NXOpen.Part, params: CircuitParams) -> None:
        """
         Deletes the selected cooling circuit fluid parameters 
        """
        pass
    def FindAnalysisParams(part: NXOpen.Part) -> AnalysisParams:
        """
         Finds the NXOpen.MoldCooling.AnalysisParams stored in the part, or  if it hasn't been created yet. 
         Returns params ( AnalysisParams NXOpen.M): .
        """
        pass
    def FindMoldBody(part: NXOpen.Part) -> MoldBody:
        """
         Finds the NXOpen.MoldCooling.MoldBody stored in the part, or  if it hasn't been created yet. 
         Returns mold ( MoldBody NXOpen.M): .
        """
        pass
    def FindSolverOptions(part: NXOpen.Part) -> SolverOptions:
        """
         Finds the NXOpen.MoldCooling.SolverOptions stored in the part. 
         Returns options ( SolverOptions NXOpen.M): .
        """
        pass
    def GetAnalysisContext(part: NXOpen.Part) -> Manager.AnalysisContext:
        """
         Returns the mold cooling analysis context for the given part. 
         Returns context ( Manager.AnalysisContext NXOpen.M): .
        """
        pass
    def ImportMoldWizardCircuits(part: NXOpen.Part) -> None:
        """
         Import mold wizard cooling circuits 
        """
        pass
    def RunSimulation(part: NXOpen.Part) -> None:
        """
         Runs the mold cooling thermal simulation. 
        """
        pass
    def RunSimulationInternal(part: NXOpen.Part, logfile: str) -> None:
        """
         Internally Runs the mold cooling thermal simulation. This method should not be called in an NXOpen program,
                 it is meant to be used internally only.
                
        """
        pass
    def SetAnalysisContext(part: NXOpen.Part, context: Manager.AnalysisContext) -> None:
        """
         Changes the mold cooling analysis context for the given part. 
        """
        pass
import NXOpen
class MoldBodyBuilder(NXOpen.Builder): 
    """ Represents a MoldCooling.MoldBodyBuilder builder """
    @property
    def CavityMaterial(self) -> NXOpen.PhysicalMaterial:
        """
        Getter for property: ( NXOpen.PhysicalMaterial) CavityMaterial
         Returns the selected material for the mold cavity   
            
         
        """
        pass
    @CavityMaterial.setter
    def CavityMaterial(self, cavityMaterial: NXOpen.PhysicalMaterial):
        """
        Setter for property: ( NXOpen.PhysicalMaterial) CavityMaterial
         Returns the selected material for the mold cavity   
            
         
        """
        pass
    @property
    def CoreMaterial(self) -> NXOpen.PhysicalMaterial:
        """
        Getter for property: ( NXOpen.PhysicalMaterial) CoreMaterial
         Returns the selected material for the mold core   
            
         
        """
        pass
    @CoreMaterial.setter
    def CoreMaterial(self, coreMaterial: NXOpen.PhysicalMaterial):
        """
        Setter for property: ( NXOpen.PhysicalMaterial) CoreMaterial
         Returns the selected material for the mold core   
            
         
        """
        pass
    @property
    def PartMaterial(self) -> NXOpen.PhysicalMaterial:
        """
        Getter for property: ( NXOpen.PhysicalMaterial) PartMaterial
         Returns the selected material for the mold part   
            
         
        """
        pass
    @PartMaterial.setter
    def PartMaterial(self, partMaterial: NXOpen.PhysicalMaterial):
        """
        Setter for property: ( NXOpen.PhysicalMaterial) PartMaterial
         Returns the selected material for the mold part   
            
         
        """
        pass
    @property
    def SelectCavityBodies(self) -> NXOpen.SelectBodyList:
        """
        Getter for property: ( NXOpen.SelectBodyList) SelectCavityBodies
         Returns the cavity bodies selection   
            
         
        """
        pass
    @property
    def SelectCoreBodies(self) -> NXOpen.SelectBodyList:
        """
        Getter for property: ( NXOpen.SelectBodyList) SelectCoreBodies
         Returns the core bodies selection   
            
         
        """
        pass
    @property
    def SelectPartBodies(self) -> NXOpen.SelectBodyList:
        """
        Getter for property: ( NXOpen.SelectBodyList) SelectPartBodies
         Returns the part bodies selection   
            
         
        """
        pass
import NXOpen
class MoldBody(NXOpen.NXObject): 
    """ Represents mold body that is to be modeled in a mold cooling simulation """
    pass
import NXOpen
class SolverOptions(NXOpen.NXObject): 
    """ Represents the solver options for the mold cooling analysis """
    @property
    def KeepAllFiles(self) -> bool:
        """
        Getter for property: (bool) KeepAllFiles
         Returns the option to keep all analysis generated files   
            
         
        """
        pass
    @KeepAllFiles.setter
    def KeepAllFiles(self, keepAllFiles: bool):
        """
        Setter for property: (bool) KeepAllFiles
         Returns the option to keep all analysis generated files   
            
         
        """
        pass
    @property
    def NumProcessors(self) -> int:
        """
        Getter for property: (int) NumProcessors
         Returns the number of processors to use for the parallel run   
            
         
        """
        pass
    @NumProcessors.setter
    def NumProcessors(self, numProcessors: int):
        """
        Setter for property: (int) NumProcessors
         Returns the number of processors to use for the parallel run   
            
         
        """
        pass
    @property
    def ParallelRun(self) -> bool:
        """
        Getter for property: (bool) ParallelRun
         Returns the option to run the analysis in parallel   
            
         
        """
        pass
    @ParallelRun.setter
    def ParallelRun(self, parallelRun: bool):
        """
        Setter for property: (bool) ParallelRun
         Returns the option to run the analysis in parallel   
            
         
        """
        pass
