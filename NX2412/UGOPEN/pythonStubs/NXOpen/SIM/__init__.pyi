from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class ArchiveImportBuilder(NXOpen.Builder): 
    """ Represents a ArchiveImportBuilder builder object.
    """
    @property
    def FileName(self) -> str:
        """
        Getter for property: (str) FileName
         Returns the archive file name from which to import data   
            
         
        """
        pass
    @FileName.setter
    def FileName(self, fileName: str):
        """
        Setter for property: (str) FileName
         Returns the archive file name from which to import data   
            
         
        """
        pass
    @property
    def ImportCollisionAvoidance(self) -> bool:
        """
        Getter for property: (bool) ImportCollisionAvoidance
         Returns the setting for importing collision avoidance data.  
            If true then collision avoidance data will be imported instead of the machine configuration.   
         
        """
        pass
    @ImportCollisionAvoidance.setter
    def ImportCollisionAvoidance(self, importSetting: bool):
        """
        Setter for property: (bool) ImportCollisionAvoidance
         Returns the setting for importing collision avoidance data.  
            If true then collision avoidance data will be imported instead of the machine configuration.   
         
        """
        pass
import NXOpen
class Breakpoint(NXOpen.NXObject): 
    """  Represents the Breakpoint class object   """
    @property
    def Condition(self) -> str:
        """
        Getter for property: (str) Condition
         Returns the condition for a breakpoint.  
             
         
        """
        pass
    @Condition.setter
    def Condition(self, condition: str):
        """
        Setter for property: (str) Condition
         Returns the condition for a breakpoint.  
             
         
        """
        pass
    def Activate(self) -> None:
        """
         Activate the breakpoint. 
        """
        pass
    def Deactivate(self) -> None:
        """
         Deactivate the breakpoint. 
        """
        pass
    def Delete(self) -> None:
        """
         Delete the breakpoint. 
        """
        pass
import NXOpen
class ExportMachineKitBuilder(NXOpen.Builder): 
    """ This class is used for the Export Machine Kit Dialog.
        Calling Builder.Commit on this
        builder will start the export machine kit process
        and return .
     """
    @property
    def KitName(self) -> str:
        """
        Getter for property: (str) KitName
         Returns the kit name specify the name of the package.  
           The name should be unique in the target directory.  
         
        """
        pass
    @KitName.setter
    def KitName(self, kit_name: str):
        """
        Setter for property: (str) KitName
         Returns the kit name specify the name of the package.  
           The name should be unique in the target directory.  
         
        """
        pass
    @property
    def OutputDirectory(self) -> str:
        """
        Getter for property: (str) OutputDirectory
         Returns the machine kit output directory specify where the finished package will be stored.  
            
         
        """
        pass
    @OutputDirectory.setter
    def OutputDirectory(self, output_directory: str):
        """
        Setter for property: (str) OutputDirectory
         Returns the machine kit output directory specify where the finished package will be stored.  
            
         
        """
        pass
    @property
    def PrintReport(self) -> bool:
        """
        Getter for property: (bool) PrintReport
         Returns the machine kit print report checkbox specify if a report will be plotted while create the kit or not.  
            
         
        """
        pass
    @PrintReport.setter
    def PrintReport(self, onOff: bool):
        """
        Setter for property: (bool) PrintReport
         Returns the machine kit print report checkbox specify if a report will be plotted while create the kit or not.  
            
         
        """
        pass
    def AddKitDirectory(self, directory: str, subDirectory: str) -> None:
        """
         Add a subdirectory to the machine kit at the given directory. The directory can be get in the function GetAllKitPaths.
        """
        pass
    def AddKitFile(self, directory: str, file: str) -> None:
        """
         Add a file to the machine kit at the given directory. The directory can be get in the function GetAllKitPaths.
        """
        pass
    def AddKitFolder(self, directory: str, folder: str) -> None:
        """
         Add a folder, all containing files and subfolder to the machine kit at the given directory. 
                    The directory can be get in the function GetAllKitPaths.
        """
        pass
    def GetAllKitPaths(self) -> List[str]:
        """
         Returns a array of the the file paths that are already in the machine kit. If you want to modify what
                    will export with the kit, you need to specify the whole kit path. This function gives the opportunity. 
                    This function allocates the memory for kitPaths. The caller is responsible to deallocate the memory.
         Returns kitFiles (List[str]):  array of all files of the machine kit.
        """
        pass
    def LoadDeviceDirectory(self) -> None:
        """
         Loads all the devices in the current machine. 
        """
        pass
    def LoadToolDirectory(self) -> None:
        """
         Loads all the tools in the current machine. 
        """
        pass
    def RemovePathInKit(self, directory: str) -> None:
        """
         Removes the given file or directory in the machine kit. The directory can be get in the function GetAllKitPaths.
        """
        pass
    def RenameKitDirectory(self, directory: str, newDirectoryName: str) -> None:
        """
         Rename a directory to the machine kit at the given directory. The directory can be get in the function GetAllKitPaths.
        """
        pass
import NXOpen
class ImportMachineKitBuilder(NXOpen.Builder): 
    """ This class is used for the Import Machine Kit Dialog.
    Calling Builder.Commit on this
    builder will start the import machine kit process
    and return .
    """
    @property
    def OutputDirectory(self) -> str:
        """
        Getter for property: (str) OutputDirectory
         Returns the machine kit output directory specify where the finished machine folder will be stored.  
            
         
        """
        pass
    @OutputDirectory.setter
    def OutputDirectory(self, output_directory: str):
        """
        Setter for property: (str) OutputDirectory
         Returns the machine kit output directory specify where the finished machine folder will be stored.  
            
         
        """
        pass
    @property
    def PrintReport(self) -> bool:
        """
        Getter for property: (bool) PrintReport
         Returns the machine print report flat that specifies if a report will be plotted while import the machine or not.  
             
         
        """
        pass
    @PrintReport.setter
    def PrintReport(self, onOff: bool):
        """
        Setter for property: (bool) PrintReport
         Returns the machine print report flat that specifies if a report will be plotted while import the machine or not.  
             
         
        """
        pass
import NXOpen
class IsvControlPanelBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.SIM.IsvControlPanelBuilder
    """
    class DetailType(Enum):
        """
        Members Include: 
         |Info|  Info        
         |Controller|  Controller  
         |Limit|  Limit       
         |Collision|  Collision   
         |Gouge|  Gouge       
         |Singularity|  Singularity 

        """
        Info: int
        Controller: int
        Limit: int
        Collision: int
        Gouge: int
        Singularity: int
        @staticmethod
        def ValueOf(value: int) -> IsvControlPanelBuilder.DetailType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Language(Enum):
        """
        Members Include: 
         |Nc|  NC language 
         |Ac|  AC language 
         |Cse|  CSE language 

        """
        Nc: int
        Ac: int
        Cse: int
        @staticmethod
        def ValueOf(value: int) -> IsvControlPanelBuilder.Language:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SingleStepModeType(Enum):
        """
        Members Include: 
         |StepIn|  Step In 
         |StepOver|  Step Over 
         |StepOut|  Step Out 
         |DisplayUpdate|  Display 

        """
        StepIn: int
        StepOver: int
        StepOut: int
        DisplayUpdate: int
        @staticmethod
        def ValueOf(value: int) -> IsvControlPanelBuilder.SingleStepModeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SingleStepType(Enum):
        """
        Members Include: 
         |Block|  Block 
         |Move|  Move 
         |Event|  Event 

        """
        Block: int
        Move: int
        Event: int
        @staticmethod
        def ValueOf(value: int) -> IsvControlPanelBuilder.SingleStepType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class VisualizationType(Enum):
        """
        Members Include: 
         |MachineCodeSimulateCse|  Machine Code Simulate Cse 
         |MachineCodeSimulateMtd|  Machine Code Simulate Mtd 
         |ToolPathSimulation|  Tool Path Simulate 

        """
        MachineCodeSimulateCse: int
        MachineCodeSimulateMtd: int
        ToolPathSimulation: int
        @staticmethod
        def ValueOf(value: int) -> IsvControlPanelBuilder.VisualizationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class VncMode(Enum):
        """
        Members Include: 
         |Error|  ERROR  
         |Notconnected|  NOT CONNECTED 
         |Connected|  CONNECTED 
         |Booted|  BOOTED 
         |Configured|  CONFIGURED 
         |Initialized|  INITIALIZED 
         |ProgramsLoaded|  PROGRAMS LOADED 
         |Reset|  RESET 
         |Stop|  STOP 
         |Start|  START 
         |Run|  RUN 

        """
        Error: int
        Notconnected: int
        Connected: int
        Booted: int
        Configured: int
        Initialized: int
        ProgramsLoaded: int
        Reset: int
        Stop: int
        Start: int
        Run: int
        @staticmethod
        def ValueOf(value: int) -> IsvControlPanelBuilder.VncMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ActiveChannel(self) -> str:
        """
        Getter for property: (str) ActiveChannel
         Returns the active channel in simulation.  
             
         
        """
        pass
    @ActiveChannel.setter
    def ActiveChannel(self, channelName: str):
        """
        Setter for property: (str) ActiveChannel
         Returns the active channel in simulation.  
             
         
        """
        pass
    @property
    def IsInHistoryBuffer(self) -> bool:
        """
        Getter for property: (bool) IsInHistoryBuffer
         Returns the simulation is inside history buffer    
            
         
        """
        pass
    @property
    def MachineConfiguratorFilename(self) -> str:
        """
        Getter for property: (str) MachineConfiguratorFilename
         Returns the machine configurator filename with full path  
            
         
        """
        pass
    @property
    def MachineTime(self) -> str:
        """
        Getter for property: (str) MachineTime
         Returns the current machine time.  
             
         
        """
        pass
    @property
    def SimDebugBuilder(self) -> SimDebugBuilder:
        """
        Getter for property: ( SimDebugBuilder NXOp) SimDebugBuilder
         Returns the sim debug builder   
            
         
        """
        pass
    @property
    def SimulationLoadSnapshotBuilder(self) -> LoadSnapshotBuilder:
        """
        Getter for property: ( LoadSnapshotBuilder NXOp) SimulationLoadSnapshotBuilder
         Returns the load snapshot builder   
            
         
        """
        pass
    @property
    def SimulationOptionsBuilder(self) -> SimulationOptionsBuilder:
        """
        Getter for property: ( SimulationOptionsBuilder NXOp) SimulationOptionsBuilder
         Returns the simulation options builder   
            
         
        """
        pass
    @property
    def SimulationSaveSnapshotBuilder(self) -> SaveSnapshotBuilder:
        """
        Getter for property: ( SaveSnapshotBuilder NXOp) SimulationSaveSnapshotBuilder
         Returns the save snapshot builder   
            
         
        """
        pass
    @property
    def VncStatus(self) -> IsvControlPanelBuilder.VncMode:
        """
        Getter for property: ( IsvControlPanelBuilder.VncMode NXOp) VncStatus
         Returns the mode of VNC   
            
         
        """
        pass
    IsInHistoryBufferCb = Callable[[bool], None]
    def AddIsInHistoryBuffer(self, handler: IsvControlPanelBuilder.IsInHistoryBufferCb) -> int:
        """
         Registers the IsInHistoryBufferChanged callback. 
         Returns handlerId (int):  .
        """
        pass
    SimEndCb = Callable[[], None]
    def AddSimEnd(self, handler: IsvControlPanelBuilder.SimEndCb) -> int:
        """
         Registers the SimEnd callback. 
         Returns handlerId (int):  .
        """
        pass
    SimStartCb = Callable[[], None]
    def AddSimStart(self, handler: IsvControlPanelBuilder.SimStartCb) -> int:
        """
         Registers the SimStart callback. 
         Returns handlerId (int):  .
        """
        pass
    SimStopCb = Callable[[], None]
    def AddSimStop(self, handler: IsvControlPanelBuilder.SimStopCb) -> int:
        """
         Registers the SimStop callback. 
         Returns handlerId (int):  .
        """
        pass
    VncStatusCb = Callable[[IsvControlPanelBuilder.VncMode], None]
    def AddVncStatus(self, handler: IsvControlPanelBuilder.VncStatusCb) -> int:
        """
         Registers the VNC Status callback. 
         Returns handlerId (int):  .
        """
        pass
    def ApplySimulationOptions(self) -> None:
        """
         Apply the simulation options
        """
        pass
    def CheckProgramSyntax(self, programs: List[NcProgram]) -> None:
        """
         Check the syntax of nc programs. 
        """
        pass
    def EvaluateExpression(self, channelName: str, expression: str, language: IsvControlPanelBuilder.Language) -> Tuple[bool, str, str]:
        """
         Evaluate expression in NC, CSE or AnyController language
         Returns A tuple consisting of (success, value, valueType). 
         - success is: bool. Was the evaluation successful?.
         - value is: str. The expression value.
         - valueType is: str. The expression value's type.

        """
        pass
    def GetCurrentProgram(self, channelName: str, stackLevel: int) -> NcProgram:
        """
         Returns a program currently used in the simulation 
         Returns program ( NcProgram NXOp): .
        """
        pass
    def GetDetail(self, type: IsvControlPanelBuilder.DetailType, position: int) -> Tuple[bool, float, str, int, str, str]:
        """
         Return the Details Information to a specified type 
         Returns A tuple consisting of (result, time, description, ncLine, programName, channelName). 
         - result is: bool.
         - time is: float.
         - description is: str.
         - ncLine is: int.
         - programName is: str.
         - channelName is: str.

        """
        pass
    def GetDetailCount(self, type: IsvControlPanelBuilder.DetailType) -> int:
        """
         Return the number of Details of the specified type 
         Returns count (int): .
        """
        pass
    def GetMachiningTimeAnalysisClock(self, channelName: str) -> TimeAnalysis:
        """
         Return the Machining Time Analysis Clock for the specified channel. 
         Returns clock ( TimeAnalysis NXOp): .
        """
        pass
    def GetPostprocessorFilename(self) -> Tuple[str, str]:
        """
         Get the post processor definition and tcl filename with full path
         Returns A tuple consisting of (tclFilename, definitionFilename). 
         - tclFilename is: str. The tcl filename with full path.
         - definitionFilename is: str. The definition filename with full path.

        """
        pass
    def GetShowToolPath(self) -> bool:
        """
         Gets the show tool path
         Returns state (bool): .
        """
        pass
    def GetShowToolTrace(self) -> bool:
        """
         Gets the show tool trace
         Returns state (bool): .
        """
        pass
    def GetSingleStep(self) -> IsvControlPanelBuilder.SingleStepType:
        """
         Gets the single step in Tool Path Based Simulation
         Returns type ( IsvControlPanelBuilder.SingleStepType NXOp): .
        """
        pass
    def GetSingleStepMode(self) -> IsvControlPanelBuilder.SingleStepModeType:
        """
         Gets the single step mode in Machine Code Simulation
         Returns type ( IsvControlPanelBuilder.SingleStepModeType NXOp): .
        """
        pass
    def GetVisualization(self) -> IsvControlPanelBuilder.VisualizationType:
        """
         Gets the visualization
         Returns type ( IsvControlPanelBuilder.VisualizationType NXOp): .
        """
        pass
    def JumpToDetailsLine(self, line: int) -> None:
        """
         Jump to details line
        """
        pass
    def JumpToMachineTime(self, machineTime: str) -> None:
        """
         Jump to machine time
        """
        pass
    @overload
    def JumpToNcProgramLine(self, line: int) -> None:
        """
         Jump to nc program line in the active channel
        """
        pass
    @overload
    def JumpToNcProgramLine(self, channelName: str, line: int) -> None:
        """
         Jump to nc program line in the specified channel
        """
        pass
    def MachineControlBootVnck(self) -> bool:
        """
         
                    Machine Control Panel: Boot the virtual controller
                    Once the virtual controller has been successfully booted, the state remains as long as the part stays open or the machine setup is replaced.
                    To shut down the controller manually, NXOpen.SIM.IsvControlPanelBuilder.MachineControlShutdownVnck() can be invoked.
                    
                    
                    The new behavior eliminates the wait required to boot the controller. However, it happens that the machine must be restarted. 
                    For this purpose NXOpen.SIM.IsvControlPanelBuilder.MachineControlShutdownVnck() and NXOpen.SIM.IsvControlPanelBuilder.MachineControlBootVnck() can be successively invoked.
                    
                
         Returns success (bool): .
        """
        pass
    @overload
    def MachineControlClearAlarm(self) -> None:
        """
         Machine Control Panel: Clear Alarms for all channels
        """
        pass
    @overload
    def MachineControlClearAlarm(self, channels: List[str]) -> None:
        """
         Machine Control Panel: Clear Alarms for specific channels
        """
        pass
    def MachineControlDryRun(self, enable: bool) -> None:
        """
         Machine Control Panel: Activate Machine Dry Run
        """
        pass
    def MachineControlFeedRateOverride(self, value: int) -> None:
        """
         Machine Control Panel: Sets Machine Feed Rate Override
        """
        pass
    def MachineControlGetChannels(self) -> List[str]:
        """
         Gets the Channel Names
         Returns channels (List[str]):  the names of available channel .
        """
        pass
    def MachineControlGetCycleTime(self) -> int:
        """
         Gets the Machine Cycle Time
         Returns value (int):  The cycle time in ms.
        """
        pass
    def MachineControlGetFeedRateOverrideMaximumValue(self) -> int:
        """
         Machine Control Panel: Gets the Machine Feed Rate Override Maximum Value
         Returns value (int):  The feed rate override max value.
        """
        pass
    def MachineControlReadVariable(self, channelName: str, variableName: str) -> Tuple[bool, str, str]:
        """
         Read Variable e.g. VDI Variable, Machine Data
         Returns A tuple consisting of (success, variableValue, variableType). 
         - success is: bool.
         - variableValue is: str. The variable value.
         - variableType is: str. The variable type: VDI_SWITCH, VDI_INTEGER, VDI_SINGLESTEP.

        """
        pass
    def MachineControlResetMachine(self) -> None:
        """
         Machine Control Panel: Fast Reset Machine
        """
        pass
    def MachineControlResetMachineData(self) -> None:
        """
         Machine Control Panel: Reset the Machine Data (SRAM) to the library Machine Data (SRAM)
        """
        pass
    @overload
    def MachineControlResetNc(self) -> None:
        """
         Machine Control Panel: NC Reset for all channels
        """
        pass
    @overload
    def MachineControlResetNc(self, channels: List[str]) -> None:
        """
         Machine Control Panel: NC Reset for specific channels
        """
        pass
    def MachineControlResetPart(self) -> None:
        """
         Machine Control Panel: Reset Part
        """
        pass
    def MachineControlSaveMachineData(self) -> None:
        """
         Machine Control Panel: Save the Machine Data (SRAM)
        """
        pass
    def MachineControlShowHmi(self) -> None:
        """
         Machine Control Panel: Show HMI
        """
        pass
    def MachineControlShutdownVnck(self) -> None:
        """
         
                    Machine Control Panel: Shut down the virtual controller
                    Used in conjunction with NXOpen.SIM.IsvControlPanelBuilder.MachineControlBootVnck().
                              
                
        """
        pass
    def MachineControlSingleBlockMode(self, enable: bool) -> None:
        """
         Machine Control Panel: Activate Machine Single Block Mode
        """
        pass
    @overload
    def MachineControlStartNc(self) -> None:
        """
         Machine Control Panel: NC Start for all channels
        """
        pass
    @overload
    def MachineControlStartNc(self, channels: List[str]) -> None:
        """
         Machine Control Panel: NC Start for specific channels
        """
        pass
    @overload
    def MachineControlStopNc(self) -> None:
        """
         Machine Control Panel: NC Stop for all channels
        """
        pass
    @overload
    def MachineControlStopNc(self, channels: List[str]) -> None:
        """
         Machine Control Panel: NC Stop for specific channels
        """
        pass
    def MachineControlWriteVariable(self, channelName: str, variableName: str, variableValue: str, variableType: str) -> bool:
        """
         Write Variable e.g. VDI Variable, Machine Data
         Returns success (bool): .
        """
        pass
    def PlayBackward(self) -> None:
        """
         Simulation Control Panel: Play Backward
        """
        pass
    def PlayForward(self) -> None:
        """
         Simulation Control Panel: Play Forward
        """
        pass
    def PlayToMachineTime(self, machineTime: str) -> None:
        """
         Play to Machine Time
        """
        pass
    def ReadSettingsFromFile(self, filename: str) -> None:
        """
         Read simulation settings from xml file 
        """
        pass
    def RemoveIsInHistoryBuffer(self, handlerId: int) -> bool:
        """
         Unregisters the IsInHistoryBufferChanged callback. 
         Returns result (bool):  .
        """
        pass
    def RemoveSimEnd(self, handlerId: int) -> bool:
        """
         Unregisters the SimEnd callback. 
         Returns result (bool):  .
        """
        pass
    def RemoveSimStart(self, handlerId: int) -> bool:
        """
         Unregisters the SimStart callback. 
         Returns result (bool):  .
        """
        pass
    def RemoveSimStop(self, handlerId: int) -> bool:
        """
         Unregisters the SimStop callback. 
         Returns result (bool):  .
        """
        pass
    def RemoveVncStatus(self, handlerId: int) -> bool:
        """
         Unregisters the VNC Status callback. 
         Returns result (bool):  .
        """
        pass
    def ResetMachine(self) -> None:
        """
         Simulation Control Panel: (Full) Reset Machine
        """
        pass
    def SaveSettingsToFile(self, filename: str) -> None:
        """
         Save simulation settings to xml file 
        """
        pass
    def SetCurrentProgramLine(self, channelName: str, line: int) -> None:
        """
         Set execution cursor to nc program line in the specified channel
        """
        pass
    def SetShowToolPath(self, state: bool) -> None:
        """
         Sets the show tool path 
        """
        pass
    def SetShowToolTrace(self, state: bool) -> None:
        """
         Sets the show tool trace 
        """
        pass
    def SetSingleStep(self, type: IsvControlPanelBuilder.SingleStepType) -> None:
        """
         Sets the single step in Tool Path Based Simulation
        """
        pass
    def SetSingleStepMode(self, type: IsvControlPanelBuilder.SingleStepModeType) -> None:
        """
         Sets the single step mode in Machine Code Simulation
        """
        pass
    def SetSpeed(self, simSpeed: int) -> None:
        """
         Simulation Control Panel: Simulation Speed
        """
        pass
    def SetVisualization(self, type: IsvControlPanelBuilder.VisualizationType) -> None:
        """
         Sets the visualization 
        """
        pass
    def ShowSnapshot(self, bRunToSimTime: bool, sourceComp: str, snapshot: Snapshot) -> None:
        """
         Show snapshot 
        """
        pass
    def SingleStepBackward(self) -> None:
        """
         Simulation Control Panel: Single Step Backward
        """
        pass
    def SingleStepForward(self) -> None:
        """
         Simulation Control Panel: Single Step Forward
        """
        pass
    def StepToNextOperation(self) -> None:
        """
         Simulation Control Panel: Step to Next Operation
        """
        pass
    def StepToPreviousOperation(self) -> None:
        """
         Simulation Control Panel: Step to Previous Operation
        """
        pass
    def Stop(self) -> None:
        """
         Simulation Control Panel: Stop the simulation
        """
        pass
import NXOpen
class KinematicAxisBuilder(NXOpen.Builder): 
    """  Represents the SimKimAxisBuilder class object   """
    class AxisDirectionType(Enum):
        """
        Members Include: 
         |PositiveX|  positive X-axis 
         |NegativeX|  negative X-axis 
         |PositiveY|  positive Y-axis 
         |NegativeY|  negative Y-axis 
         |PositiveZ|  positive Z-axis 
         |NegativeZ|  negative Z-axis 

        """
        PositiveX: int
        NegativeX: int
        PositiveY: int
        NegativeY: int
        PositiveZ: int
        NegativeZ: int
        @staticmethod
        def ValueOf(value: int) -> KinematicAxisBuilder.AxisDirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class AxisMotionType(Enum):
        """
        Members Include: 
         |LinearNcAxis|  linear NC-axis 
         |RotaryNcAxis|  rotary NC-axis 
         |Linear|  linear axis    
         |Rotary|  rotary axis    
         |RotaryUnlimitedNcAxis|  rotary unlimited NC-axis 
         |SpindleNcAxis|  spindle NC-axis 
         |RotaryUnlimited| rotary axis unlimited
         |Spindle|  spindle    

        """
        LinearNcAxis: int
        RotaryNcAxis: int
        Linear: int
        Rotary: int
        RotaryUnlimitedNcAxis: int
        SpindleNcAxis: int
        RotaryUnlimited: int
        Spindle: int
        @staticmethod
        def ValueOf(value: int) -> KinematicAxisBuilder.AxisMotionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CoarsePrecision(self) -> float:
        """
        Getter for property: (float) CoarsePrecision
         Returns the coarse precision.  
          
                This defines the exact stop precision used to determine if a target point has been
                reached, so that the next NC-block can be executed.   
         
        """
        pass
    @CoarsePrecision.setter
    def CoarsePrecision(self, coarse: float):
        """
        Setter for property: (float) CoarsePrecision
         Returns the coarse precision.  
          
                This defines the exact stop precision used to determine if a target point has been
                reached, so that the next NC-block can be executed.   
         
        """
        pass
    @property
    def Direction(self) -> KinematicAxisBuilder.AxisDirectionType:
        """
        Getter for property: ( KinematicAxisBuilder.AxisDirectionType NXOp) Direction
         Returns the axis direction   
            
         
        """
        pass
    @Direction.setter
    def Direction(self, axisDir: KinematicAxisBuilder.AxisDirectionType):
        """
        Setter for property: ( KinematicAxisBuilder.AxisDirectionType NXOp) Direction
         Returns the axis direction   
            
         
        """
        pass
    @property
    def FinePrecision(self) -> float:
        """
        Getter for property: (float) FinePrecision
         Returns the fine precision.  
          
                This defines the exact stop precision used to determine if a target point has been
                reached, so that the next NC-block can be executed.   
         
        """
        pass
    @FinePrecision.setter
    def FinePrecision(self, fine: float):
        """
        Setter for property: (float) FinePrecision
         Returns the fine precision.  
          
                This defines the exact stop precision used to determine if a target point has been
                reached, so that the next NC-block can be executed.   
         
        """
        pass
    @property
    def InitialValue(self) -> float:
        """
        Getter for property: (float) InitialValue
         Returns the initial value   
            
         
        """
        pass
    @InitialValue.setter
    def InitialValue(self, initial: float):
        """
        Setter for property: (float) InitialValue
         Returns the initial value   
            
         
        """
        pass
    @property
    def JerkLimit(self) -> float:
        """
        Getter for property: (float) JerkLimit
         Returns the jerk limit.  
          
                The jerk limit value limits jumps in acceleration.   
         
        """
        pass
    @JerkLimit.setter
    def JerkLimit(self, jerk: float):
        """
        Setter for property: (float) JerkLimit
         Returns the jerk limit.  
          
                The jerk limit value limits jumps in acceleration.   
         
        """
        pass
    @property
    def JumpVelocity(self) -> float:
        """
        Getter for property: (float) JumpVelocity
         Returns the jump velocity.  
          
                The jump velocity define a lag time at the beginning of the motion.   
         
        """
        pass
    @JumpVelocity.setter
    def JumpVelocity(self, jump: float):
        """
        Setter for property: (float) JumpVelocity
         Returns the jump velocity.  
          
                The jump velocity define a lag time at the beginning of the motion.   
         
        """
        pass
    @property
    def Junction(self) -> KinematicJunction:
        """
        Getter for property: ( KinematicJunction NXOp) Junction
         Returns the junction   
            
         
        """
        pass
    @Junction.setter
    def Junction(self, jct: KinematicJunction):
        """
        Setter for property: ( KinematicJunction NXOp) Junction
         Returns the junction   
            
         
        """
        pass
    @property
    def Kv(self) -> float:
        """
        Getter for property: (float) Kv
         Returns the kv.  
          
                the Kv-Factor is a parameter of the drives. It influences the dragging error (difference
                between ideal motion profile and actual motion profile).   
         
        """
        pass
    @Kv.setter
    def Kv(self, kv: float):
        """
        Setter for property: (float) Kv
         Returns the kv.  
          
                the Kv-Factor is a parameter of the drives. It influences the dragging error (difference
                between ideal motion profile and actual motion profile).   
         
        """
        pass
    @property
    def Limit(self) -> bool:
        """
        Getter for property: (bool) Limit
         Returns the axis limits flag
                  This property is deprecated.  
           Use  SIM::KinematicAxisBuilder::AxisMotionType  instead.
                     
         
        """
        pass
    @Limit.setter
    def Limit(self, result: bool):
        """
        Setter for property: (bool) Limit
         Returns the axis limits flag
                  This property is deprecated.  
           Use  SIM::KinematicAxisBuilder::AxisMotionType  instead.
                     
         
        """
        pass
    @property
    def LowerLimit(self) -> float:
        """
        Getter for property: (float) LowerLimit
         Returns the lower limit   
            
         
        """
        pass
    @LowerLimit.setter
    def LowerLimit(self, lower: float):
        """
        Setter for property: (float) LowerLimit
         Returns the lower limit   
            
         
        """
        pass
    @property
    def LowerSoftLimit(self) -> float:
        """
        Getter for property: (float) LowerSoftLimit
         Returns the lower soft limit.  
          
                The soft limit on the real machine is checked by the controller to avoid that the machine
                travels into the mechanical stop (Hard Limit) with full speed (prevent damage)   
         
        """
        pass
    @LowerSoftLimit.setter
    def LowerSoftLimit(self, lower: float):
        """
        Setter for property: (float) LowerSoftLimit
         Returns the lower soft limit.  
          
                The soft limit on the real machine is checked by the controller to avoid that the machine
                travels into the mechanical stop (Hard Limit) with full speed (prevent damage)   
         
        """
        pass
    @property
    def MaxAcceleration(self) -> float:
        """
        Getter for property: (float) MaxAcceleration
         Returns the max acceleration.  
          
                The maximum acceleration defines how fast the axis can accelerate.   
         
        """
        pass
    @MaxAcceleration.setter
    def MaxAcceleration(self, max: float):
        """
        Setter for property: (float) MaxAcceleration
         Returns the max acceleration.  
          
                The maximum acceleration defines how fast the axis can accelerate.   
         
        """
        pass
    @property
    def MaxDeceleration(self) -> float:
        """
        Getter for property: (float) MaxDeceleration
         Returns the max deceleration.  
          
                The maximum deceleration defines how fast the axis can decelerate.   
         
        """
        pass
    @MaxDeceleration.setter
    def MaxDeceleration(self, max: float):
        """
        Setter for property: (float) MaxDeceleration
         Returns the max deceleration.  
          
                The maximum deceleration defines how fast the axis can decelerate.   
         
        """
        pass
    @property
    def MaximumVelocity(self) -> float:
        """
        Getter for property: (float) MaximumVelocity
         Returns the maximum velocity   
            
         
        """
        pass
    @MaximumVelocity.setter
    def MaximumVelocity(self, velocity: float):
        """
        Setter for property: (float) MaximumVelocity
         Returns the maximum velocity   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the kinematic axis's name   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the kinematic axis's name   
            
         
        """
        pass
    @property
    def Number(self) -> int:
        """
        Getter for property: (int) Number
         Returns the kinematic axis's number.  
          
                The axis number is used in cases where an axis is programmed through a number 
                instead of through an address (e.g. on Siemens 840D: AX1=10 instead of X10).  
         
        """
        pass
    @Number.setter
    def Number(self, number: int):
        """
        Setter for property: (int) Number
         Returns the kinematic axis's number.  
          
                The axis number is used in cases where an axis is programmed through a number 
                instead of through an address (e.g. on Siemens 840D: AX1=10 instead of X10).  
         
        """
        pass
    @property
    def Type(self) -> KinematicAxisBuilder.AxisMotionType:
        """
        Getter for property: ( KinematicAxisBuilder.AxisMotionType NXOp) Type
         Returns the axis motion   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: KinematicAxisBuilder.AxisMotionType):
        """
        Setter for property: ( KinematicAxisBuilder.AxisMotionType NXOp) Type
         Returns the axis motion   
            
         
        """
        pass
    @property
    def UpperLimit(self) -> float:
        """
        Getter for property: (float) UpperLimit
         Returns the upper limit   
            
         
        """
        pass
    @UpperLimit.setter
    def UpperLimit(self, upper: float):
        """
        Setter for property: (float) UpperLimit
         Returns the upper limit   
            
         
        """
        pass
    @property
    def UpperSoftLimit(self) -> float:
        """
        Getter for property: (float) UpperSoftLimit
         Returns the upper soft limit.  
          
                The soft limit on the real machine is checked by the controller to avoid that the machine
                travels into the mechanical stop (Hard Limit) with full speed (prevent damage)   
         
        """
        pass
    @UpperSoftLimit.setter
    def UpperSoftLimit(self, upper: float):
        """
        Setter for property: (float) UpperSoftLimit
         Returns the upper soft limit.  
          
                The soft limit on the real machine is checked by the controller to avoid that the machine
                travels into the mechanical stop (Hard Limit) with full speed (prevent damage)   
         
        """
        pass
import NXOpen
class KinematicAxis(NXOpen.NXObject): 
    """  Represents the SimKimAxis class object   """
    pass
import NXOpen
class KinematicChainConfiguration(NXOpen.Builder): 
    """ This class is used for define kinematic chains.
        Calling Builder.Commit on this builder will return .
    """
    @property
    def List(self) -> KinematicChainList:
        """
        Getter for property: ( KinematicChainList NXOp) List
         Returns the kinematic chain list   
            
         
        """
        pass
import NXOpen
class KinematicChainList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[KinematicChain]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: KinematicChain) -> None:
        """
         Appends an object to the list
            
        """
        pass
    @overload
    def Clear(self) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    def ClearIndex(self, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
               not change, but the item at this index is set to NULL.
            
        """
        pass
    @overload
    def Clear(self, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    @overload
    def Erase(self, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, obj: KinematicChain) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: KinematicChain, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: KinematicChain) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> KinematicChain:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( KinematicChain NXOp):  object found at input index .
        """
        pass
    def GetContents(self) -> List[KinematicChain]:
        """
         Gets the contents of the entire list 
         Returns objects ( KinematicChain List[NX):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: KinematicChain) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    def MoveToBottom(self, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    def MoveToTop(self, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    def SetContents(self, objects: List[KinematicChain]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    @overload
    def Swap(self, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    @overload
    def Swap(self, object1: KinematicChain, object2: KinematicChain) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class KinematicChain(NXOpen.Builder): 
    """ This class is used for add kinematic chain to the list.
        Calling Builder.Commit on this builder will only return .
    """
    class CoordinatePlaneTypes(Enum):
        """
        Members Include: 
         |Zx|  ZX 
         |Xy|  XY 

        """
        Zx: int
        Xy: int
        @staticmethod
        def ValueOf(value: int) -> KinematicChain.CoordinatePlaneTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PreferredSolutionType(Enum):
        """
        Members Include: 
         |Invalid|  Invalid solution 
         |Shortest|  Shortest distance solution 
         |RangeOne|  Solution range one 
         |RangeTwo|  Solution range two 

        """
        Invalid: int
        Shortest: int
        RangeOne: int
        RangeTwo: int
        @staticmethod
        def ValueOf(value: int) -> KinematicChain.PreferredSolutionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |Unknown|  Unknown 
         |Milling|  Milling 
         |Turning|  Turning 
         |Polar|  Polar   
         |Robot|  Robot   

        """
        Unknown: int
        Milling: int
        Turning: int
        Polar: int
        Robot: int
        @staticmethod
        def ValueOf(value: int) -> KinematicChain.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Axial(self) -> str:
        """
        Getter for property: (str) Axial
         Returns the axial axis of the kinematic chain   
            
         
        """
        pass
    @Axial.setter
    def Axial(self, axis: str):
        """
        Setter for property: (str) Axial
         Returns the axial axis of the kinematic chain   
            
         
        """
        pass
    @property
    def CoordinateAxes(self) -> str:
        """
        Getter for property: (str) CoordinateAxes
         Returns the coordinate axes name of the kinematic chain   
            
         
        """
        pass
    @CoordinateAxes.setter
    def CoordinateAxes(self, axis: str):
        """
        Setter for property: (str) CoordinateAxes
         Returns the coordinate axes name of the kinematic chain   
            
         
        """
        pass
    @property
    def CoordinatePlane(self) -> KinematicChain.CoordinatePlaneTypes:
        """
        Getter for property: ( KinematicChain.CoordinatePlaneTypes NXOp) CoordinatePlane
         Returns the coordinate plane type of the kinematic chain   
            
         
        """
        pass
    @CoordinatePlane.setter
    def CoordinatePlane(self, type: KinematicChain.CoordinatePlaneTypes):
        """
        Setter for property: ( KinematicChain.CoordinatePlaneTypes NXOp) CoordinatePlane
         Returns the coordinate plane type of the kinematic chain   
            
         
        """
        pass
    @property
    def Device(self) -> str:
        """
        Getter for property: (str) Device
         Returns the device component of the kinematic chain   
            
         
        """
        pass
    @Device.setter
    def Device(self, device: str):
        """
        Setter for property: (str) Device
         Returns the device component of the kinematic chain   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name of the kinematic chain   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name of the kinematic chain   
            
         
        """
        pass
    @property
    def Radial(self) -> str:
        """
        Getter for property: (str) Radial
         Returns the radial axis of the kinematic chain   
            
         
        """
        pass
    @Radial.setter
    def Radial(self, axis: str):
        """
        Setter for property: (str) Radial
         Returns the radial axis of the kinematic chain   
            
         
        """
        pass
    @property
    def ReferencePointJunction(self) -> str:
        """
        Getter for property: (str) ReferencePointJunction
         Returns the reference point junction of the kinematic chain   
            
         
        """
        pass
    @ReferencePointJunction.setter
    def ReferencePointJunction(self, refPointJunction: str):
        """
        Setter for property: (str) ReferencePointJunction
         Returns the reference point junction of the kinematic chain   
            
         
        """
        pass
    @property
    def Rotary1(self) -> str:
        """
        Getter for property: (str) Rotary1
         Returns the rotary1 axis of the kinematic chain   
            
         
        """
        pass
    @Rotary1.setter
    def Rotary1(self, rotary1: str):
        """
        Setter for property: (str) Rotary1
         Returns the rotary1 axis of the kinematic chain   
            
         
        """
        pass
    @property
    def Rotary2(self) -> str:
        """
        Getter for property: (str) Rotary2
         Returns the rotary2 axis of the kinematic chain   
            
         
        """
        pass
    @Rotary2.setter
    def Rotary2(self, rotary2: str):
        """
        Setter for property: (str) Rotary2
         Returns the rotary2 axis of the kinematic chain   
            
         
        """
        pass
    @property
    def Rotary3(self) -> str:
        """
        Getter for property: (str) Rotary3
         Returns the rotary3 axis of the kinematic chain   
            
         
        """
        pass
    @Rotary3.setter
    def Rotary3(self, rotary3: str):
        """
        Setter for property: (str) Rotary3
         Returns the rotary3 axis of the kinematic chain   
            
         
        """
        pass
    @property
    def Rotary4(self) -> str:
        """
        Getter for property: (str) Rotary4
         Returns the rotary4 axis of the kinematic chain   
            
         
        """
        pass
    @Rotary4.setter
    def Rotary4(self, rotary4: str):
        """
        Setter for property: (str) Rotary4
         Returns the rotary4 axis of the kinematic chain   
            
         
        """
        pass
    @property
    def Rotary5(self) -> str:
        """
        Getter for property: (str) Rotary5
         Returns the rotary5 axis of the kinematic chain   
            
         
        """
        pass
    @Rotary5.setter
    def Rotary5(self, rotary5: str):
        """
        Setter for property: (str) Rotary5
         Returns the rotary5 axis of the kinematic chain   
            
         
        """
        pass
    @property
    def Rotary6(self) -> str:
        """
        Getter for property: (str) Rotary6
         Returns the rotary6 axis of the kinematic chain   
            
         
        """
        pass
    @Rotary6.setter
    def Rotary6(self, rotary6: str):
        """
        Setter for property: (str) Rotary6
         Returns the rotary6 axis of the kinematic chain   
            
         
        """
        pass
    @property
    def Setup(self) -> str:
        """
        Getter for property: (str) Setup
         Returns the setup component of the kinematic chain   
            
         
        """
        pass
    @Setup.setter
    def Setup(self, setup: str):
        """
        Setter for property: (str) Setup
         Returns the setup component of the kinematic chain   
            
         
        """
        pass
    @property
    def Type(self) -> KinematicChain.Types:
        """
        Getter for property: ( KinematicChain.Types NXOp) Type
         Returns the type of the kinematic chain   
            
         
        """
        pass
    @Type.setter
    def Type(self, chainType: KinematicChain.Types):
        """
        Setter for property: ( KinematicChain.Types NXOp) Type
         Returns the type of the kinematic chain   
            
         
        """
        pass
    @property
    def X(self) -> str:
        """
        Getter for property: (str) X
         Returns the X axis of the kinematic chain   
            
         
        """
        pass
    @X.setter
    def X(self, xAxis: str):
        """
        Setter for property: (str) X
         Returns the X axis of the kinematic chain   
            
         
        """
        pass
    @property
    def Y(self) -> str:
        """
        Getter for property: (str) Y
         Returns the Y axis of the kinematic chain   
            
         
        """
        pass
    @Y.setter
    def Y(self, yAxis: str):
        """
        Setter for property: (str) Y
         Returns the Y axis of the kinematic chain   
            
         
        """
        pass
    @property
    def Z(self) -> str:
        """
        Getter for property: (str) Z
         Returns the Z axis of the kinematic chain   
            
         
        """
        pass
    @Z.setter
    def Z(self, zAxis: str):
        """
        Setter for property: (str) Z
         Returns the Z axis of the kinematic chain   
            
         
        """
        pass
import NXOpen
class KinematicChannelBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[KinematicChannelBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: KinematicChannelBuilder) -> None:
        """
         Appends an object to the list
            
        """
        pass
    @overload
    def Clear(self) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    def ClearIndex(self, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
               not change, but the item at this index is set to NULL.
            
        """
        pass
    @overload
    def Clear(self, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    @overload
    def Erase(self, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, obj: KinematicChannelBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: KinematicChannelBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: KinematicChannelBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> KinematicChannelBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( KinematicChannelBuilder NXOp):  object found at input index .
        """
        pass
    def GetContents(self) -> List[KinematicChannelBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( KinematicChannelBuilder List[NX):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: KinematicChannelBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    def MoveToBottom(self, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    def MoveToTop(self, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    def SetContents(self, objects: List[KinematicChannelBuilder]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    @overload
    def Swap(self, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    @overload
    def Swap(self, object1: KinematicChannelBuilder, object2: KinematicChannelBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class KinematicChannelBuilder(NXOpen.TaggedObject): 
    """ This class is used for add kinematic channel to the channel configuratation list.
        Calling Builder.Commit on this builder will only return .
    """
    @property
    def GeometryAxisX(self) -> str:
        """
        Getter for property: (str) GeometryAxisX
         Returns the geometry X axis of the channel   
            
         
        """
        pass
    @GeometryAxisX.setter
    def GeometryAxisX(self, xAxis: str):
        """
        Setter for property: (str) GeometryAxisX
         Returns the geometry X axis of the channel   
            
         
        """
        pass
    @property
    def GeometryAxisY(self) -> str:
        """
        Getter for property: (str) GeometryAxisY
         Returns the geometry Y axis of the channel   
            
         
        """
        pass
    @GeometryAxisY.setter
    def GeometryAxisY(self, yAxis: str):
        """
        Setter for property: (str) GeometryAxisY
         Returns the geometry Y axis of the channel   
            
         
        """
        pass
    @property
    def GeometryAxisZ(self) -> str:
        """
        Getter for property: (str) GeometryAxisZ
         Returns the geometry Z axis of the channel   
            
         
        """
        pass
    @GeometryAxisZ.setter
    def GeometryAxisZ(self, zAxis: str):
        """
        Setter for property: (str) GeometryAxisZ
         Returns the geometry Z axis of the channel   
            
         
        """
        pass
    @property
    def MainSpindle(self) -> str:
        """
        Getter for property: (str) MainSpindle
         Returns the main spindle of the channel   
            
         
        """
        pass
    @MainSpindle.setter
    def MainSpindle(self, mainSpindle: str):
        """
        Setter for property: (str) MainSpindle
         Returns the main spindle of the channel   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name of the channel   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name of the channel   
            
         
        """
        pass
    def GetAssignedAxes(self) -> List[str]:
        """
         Gets a list of assigned axes of the channel 
         Returns assignedAxes (List[str]):  the list of assigned axes .
        """
        pass
    def GetReferencedSpindles(self) -> List[str]:
        """
         Gets a list of referenced spindles of the channel 
         Returns refSpindles (List[str]):  the list of referenced spindles .
        """
        pass
    def SetAssignedAxes(self, assignedAxes: List[str]) -> None:
        """
         Sets a list of assigned axes of the channel 
        """
        pass
    def SetAssignedAxis(self, axisName: str) -> None:
        """
         Sets an assigned axis of the channel 
        """
        pass
    def SetReferencedDevice(self, deviceName: str) -> None:
        """
         Sets a referenced device of the channel 
        """
        pass
    def SetReferencedSpindle(self, spindleName: str) -> None:
        """
         Sets a referenced spindle of the channel 
        """
        pass
    def SetReferencedSpindles(self, refSpindles: List[str]) -> None:
        """
         Sets a list of referenced spindles of the channel 
        """
        pass
    def SetUnassignedAxis(self, axisName: str) -> None:
        """
         Sets an unassigned axis of the channel 
        """
        pass
    def SetUnreferencedDevice(self, deviceName: str) -> None:
        """
         Sets an unreferenced device of the channel 
        """
        pass
    def SetUnreferencedSpindle(self, spindleName: str) -> None:
        """
         Sets an unreferenced spindle of the channel 
        """
        pass
import NXOpen
class KinematicChannelConfigurationBuilder(NXOpen.Builder): 
    """ This class is used for channel configuration.
        Calling Builder.Commit on this builder will return .
    """
    @property
    def KinematicChannels(self) -> KinematicChannelBuilderList:
        """
        Getter for property: ( KinematicChannelBuilderList NXOp) KinematicChannels
         Returns the list of kinematic channel   
            
         
        """
        pass
import NXOpen
class KinematicComponentBuilder(NXOpen.Builder): 
    """  Represents the KinematicComponentBuilder class object   """
    class RegisterTypes(Enum):
        """
        Members Include: 
         |SameAsPocketId|  the pocket id defined the value 
         |Specify|  the value is specified 
         |SameAsParent|  the value is inherited from the parent 

        """
        SameAsPocketId: int
        Specify: int
        SameAsParent: int
        @staticmethod
        def ValueOf(value: int) -> KinematicComponentBuilder.RegisterTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SystemClass(Enum):
        """
        Members Include: 
         |Machine|  Machine Base classification 
         |Tool|  Tool classification 
         |Turret|  Device classification 
         |Pocket|  Static Holder classification 
         |Temporary|  Temporary classification 
         |Part|  Part - Setup classification 
         |Workpiece|  Workpiece - Setup classification 
         |SetupElement|  Any setup element classification 
         |Basic|  Only available in a BASIC machine.
                                                                                        If this bit is set, then the machine part
                                                                                        can be used for simulation when only
                                                                                        UG_ISV_BASIC license is available
                                                                                    
         |LatheSpindle|  Lathe Spindle classification 
         |PocketOnHead|  Dynamic Holder classification 
         |ToolCutting|  Tool Cutting  classification 
         |Spinning|  Spinning classification 
         |TempSpinning|  Temporary spinning classification (only for internal use) 
         |Head|  Head class 
         |RobotMountableComponent|  Mountable robot component 
         |RobotPickAndPlaceComponent|  Pick and place robot component 
         |ToolNonCutting|  Non cutting portion of tool 
         |FacingHead|  Facing head 
         |AdditiveMaterial|  Additive Material - Setup classification 
         |ToolTurret|  Turret classification 
         |Magazine|  Magazine classification 
         |ToolSpindle|  Spindle classification 
         |LocationPocket|  Location Holder classification 
         |AssignablePocket|  Assignable Holder classification 
         |WorkHolder|  Work Holder classification 
         |ToolHolder|  Tool Holder classification 
         |Setup|  Setup classification 

        """
        Machine: int
        Tool: int
        Turret: int
        Pocket: int
        Temporary: int
        Part: int
        Workpiece: int
        SetupElement: int
        Basic: int
        LatheSpindle: int
        PocketOnHead: int
        ToolCutting: int
        Spinning: int
        TempSpinning: int
        Head: int
        RobotMountableComponent: int
        RobotPickAndPlaceComponent: int
        ToolNonCutting: int
        FacingHead: int
        AdditiveMaterial: int
        ToolTurret: int
        Magazine: int
        ToolSpindle: int
        LocationPocket: int
        AssignablePocket: int
        WorkHolder: int
        ToolHolder: int
        Setup: int
        @staticmethod
        def ValueOf(value: int) -> KinematicComponentBuilder.SystemClass:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class WorkPositionAngleTypes(Enum):
        """
        Members Include: 
         |NotSet|  no angle specified 
         |SpecifyAngle|  angle is specified 

        """
        NotSet: int
        SpecifyAngle: int
        @staticmethod
        def ValueOf(value: int) -> KinematicComponentBuilder.WorkPositionAngleTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AdjustRegister(self) -> int:
        """
        Getter for property: (int) AdjustRegister
         Returns the adjust register   
            
         
        """
        pass
    @AdjustRegister.setter
    def AdjustRegister(self, adjustReg: int):
        """
        Setter for property: (int) AdjustRegister
         Returns the adjust register   
            
         
        """
        pass
    @property
    def AdjustRegisterType(self) -> KinematicComponentBuilder.RegisterTypes:
        """
        Getter for property: ( KinematicComponentBuilder.RegisterTypes NXOp) AdjustRegisterType
         Returns the adjust register type   
            
         
        """
        pass
    @AdjustRegisterType.setter
    def AdjustRegisterType(self, regType: KinematicComponentBuilder.RegisterTypes):
        """
        Setter for property: ( KinematicComponentBuilder.RegisterTypes NXOp) AdjustRegisterType
         Returns the adjust register type   
            
         
        """
        pass
    @property
    def CutcomRegister(self) -> int:
        """
        Getter for property: (int) CutcomRegister
         Returns the cutcom register   
            
         
        """
        pass
    @CutcomRegister.setter
    def CutcomRegister(self, cutcomReg: int):
        """
        Setter for property: (int) CutcomRegister
         Returns the cutcom register   
            
         
        """
        pass
    @property
    def CutcomRegisterType(self) -> KinematicComponentBuilder.RegisterTypes:
        """
        Getter for property: ( KinematicComponentBuilder.RegisterTypes NXOp) CutcomRegisterType
         Returns the cutcom register type   
            
         
        """
        pass
    @CutcomRegisterType.setter
    def CutcomRegisterType(self, regType: KinematicComponentBuilder.RegisterTypes):
        """
        Setter for property: ( KinematicComponentBuilder.RegisterTypes NXOp) CutcomRegisterType
         Returns the cutcom register type   
            
         
        """
        pass
    @property
    def CutterId(self) -> str:
        """
        Getter for property: (str) CutterId
         Returns the cutter id string to identify a cutter within a multitool   
            
         
        """
        pass
    @CutterId.setter
    def CutterId(self, cutterIdString: str):
        """
        Setter for property: (str) CutterId
         Returns the cutter id string to identify a cutter within a multitool   
            
         
        """
        pass
    @property
    def DeviceId(self) -> str:
        """
        Getter for property: (str) DeviceId
         Returns the device id   
            
         
        """
        pass
    @DeviceId.setter
    def DeviceId(self, deviceId: str):
        """
        Setter for property: (str) DeviceId
         Returns the device id   
            
         
        """
        pass
    @property
    def HolderId(self) -> int:
        """
        Getter for property: (int) HolderId
         Returns the holder id   
            
         
        """
        pass
    @HolderId.setter
    def HolderId(self, holderId: int):
        """
        Setter for property: (int) HolderId
         Returns the holder id   
            
         
        """
        pass
    @property
    def HolderIdString(self) -> str:
        """
        Getter for property: (str) HolderIdString
         Returns the holder id in string   
            
         
        """
        pass
    @HolderIdString.setter
    def HolderIdString(self, holderIdString: str):
        """
        Setter for property: (str) HolderIdString
         Returns the holder id in string   
            
         
        """
        pass
    @property
    def HolderIdType(self) -> KinematicComponentBuilder.RegisterTypes:
        """
        Getter for property: ( KinematicComponentBuilder.RegisterTypes NXOp) HolderIdType
         Returns the holder id type   
            
         
        """
        pass
    @HolderIdType.setter
    def HolderIdType(self, type: KinematicComponentBuilder.RegisterTypes):
        """
        Setter for property: ( KinematicComponentBuilder.RegisterTypes NXOp) HolderIdType
         Returns the holder id type   
            
         
        """
        pass
    @property
    def JunctionList(self) -> KinematicJunctionBuilderList:
        """
        Getter for property: ( KinematicJunctionBuilderList NXOp) JunctionList
         Returns the junction list   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the kim component's name   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the kim component's name   
            
         
        """
        pass
    @property
    def NumberOfTools(self) -> int:
        """
        Getter for property: (int) NumberOfTools
         Returns the number of tools   
            
         
        """
        pass
    @NumberOfTools.setter
    def NumberOfTools(self, numTools: int):
        """
        Setter for property: (int) NumberOfTools
         Returns the number of tools   
            
         
        """
        pass
    @property
    def WorkPositionAngle(self) -> float:
        """
        Getter for property: (float) WorkPositionAngle
         Returns the working position angle   
            
         
        """
        pass
    @WorkPositionAngle.setter
    def WorkPositionAngle(self, angle: float):
        """
        Setter for property: (float) WorkPositionAngle
         Returns the working position angle   
            
         
        """
        pass
    @property
    def WorkPositionAngleType(self) -> KinematicComponentBuilder.WorkPositionAngleTypes:
        """
        Getter for property: ( KinematicComponentBuilder.WorkPositionAngleTypes NXOp) WorkPositionAngleType
         Returns the working position angle type   
            
         
        """
        pass
    @WorkPositionAngleType.setter
    def WorkPositionAngleType(self, type: KinematicComponentBuilder.WorkPositionAngleTypes):
        """
        Setter for property: ( KinematicComponentBuilder.WorkPositionAngleTypes NXOp) WorkPositionAngleType
         Returns the working position angle type   
            
         
        """
        pass
    def AddChannelName(self, channel: str) -> None:
        """
         Adds a channel name to the component 
        """
        pass
    def AddGeometry(self, geo: NXOpen.NXObject) -> None:
        """
         Adds a single geometry element 
        """
        pass
    def AddHoldingSystem(self, holdSys: str) -> None:
        """
         Adds a holding system to the component 
        """
        pass
    def AddSystemClass(self, sysClass: KinematicComponentBuilder.SystemClass) -> None:
        """
         Add a system class 
        """
        pass
    def AddUserClassName(self, uclass: str) -> None:
        """
         Adds a user class to the component 
        """
        pass
    def DeleteAllGeometries(self) -> None:
        """
         Deletes all geometry elements from the component 
        """
        pass
    def DeleteAllSystemClasses(self) -> None:
        """
         Delete all system classes of the component 
        """
        pass
    def DeleteChannelName(self, channel: str) -> None:
        """
         Deletes a channel name from the component 
        """
        pass
    def DeleteGeometry(self, geo: NXOpen.NXObject) -> None:
        """
         Deletes a single geometry element from the component 
        """
        pass
    def DeleteHoldingSystem(self, holdSys: str) -> None:
        """
         Deletes a holding system from the component 
        """
        pass
    def DeleteSystemClass(self, sysClasses: KinematicComponentBuilder.SystemClass) -> None:
        """
         Delete a system class 
        """
        pass
    def DeleteUserClassName(self, uclass: str) -> None:
        """
         Deletes a user class from the component 
        """
        pass
    def GetChannelNames(self) -> List[str]:
        """
         Get a list of channel names of the component 
         Returns channels (List[str]):  The channel names of the component .
        """
        pass
    def GetGeometries(self) -> List[NXOpen.NXObject]:
        """
         Returns the geometry elements assigned to this component 
         Returns geos ( NXOpen.NXObject Li):  The geometry elements .
        """
        pass
    def GetHoldingSystems(self) -> List[str]:
        """
         Get a list of holding systems of the component 
         Returns holdSys (List[str]):  The channel names of the component .
        """
        pass
    def GetSaveIpw(self) -> bool:
        """
         Does the system save an IPW with the component? 
         Returns saveIpw (bool): .
        """
        pass
    def GetSystemClasses(self) -> List[KinematicComponentBuilder.SystemClass]:
        """
         Returns the component's system classes 
         Returns sysClasses ( KinematicComponentBuilder.SystemClass List[NX):  the component's system classes .
        """
        pass
    def GetUserClassNames(self) -> List[str]:
        """
         Get a list of user classes of the component 
         Returns uclass (List[str]):  The user classes of the component .
        """
        pass
    def IsOfSystemClass(self, sysClass: KinematicComponentBuilder.SystemClass) -> bool:
        """
         Test if the component is a member of the given system class 
         Returns result (bool):  TRUE if component is of the system class .
        """
        pass
    def RenameChannelName(self, oldName: str, newName: str) -> None:
        """
         Renames a channel name from the component 
        """
        pass
    def RenameHoldingSystem(self, oldName: str, newName: str) -> None:
        """
         Renames a holding system from the component 
        """
        pass
    def RenameUserClass(self, oldName: str, newName: str) -> None:
        """
         Renames a user class from the component 
        """
        pass
    def SetGeometries(self, geos: List[NXOpen.NXObject]) -> None:
        """
         Sets geometry elements for the component 
        """
        pass
    def SetSaveIpw(self, saveIpw: bool) -> None:
        """
         Save an IPW with the component 
        """
        pass
import NXOpen
class KinematicComponentCollection(NXOpen.TaggedObjectCollection): 
    """ Represents the SimKimComponent Collection """
    def CreateComponentBuilder(self, parent: KinematicComponent, comp: KinematicComponent) -> KinematicComponentBuilder:
        """
         Creates a builder for a kinematic component 
         Returns builder ( KinematicComponentBuilder NXOp):  The component builder .
        """
        pass
    def CreateFacingHeadBaseComponentBuilder(self, head: KinematicComponent) -> KinematicComponentBuilder:
        """
         Creates a builder for facing head base component. 
         Returns builder ( KinematicComponentBuilder NXOp):  The new facing head base component builder .
        """
        pass
    def CreateHeadBaseComponentBuilder(self, head: KinematicComponent) -> KinematicComponentBuilder:
        """
         Creates a builder for head base component. 
         Returns builder ( KinematicComponentBuilder NXOp):  The new head base component builder .
        """
        pass
    def CreateMachineBaseComponentBuilder(self, machine: KinematicComponent) -> KinematicComponentBuilder:
        """
         Creates a builder for a machine base component. 
         Returns builder ( KinematicComponentBuilder NXOp):  The new machine base component builder .
        """
        pass
    def CreateToolBaseComponentBuilder(self, tool: KinematicComponent) -> KinematicComponentBuilder:
        """
         Creates a builder for tool base component. 
         Returns builder ( KinematicComponentBuilder NXOp):  The new tool base component builder .
        """
        pass
    def FindObject(self, sid: str) -> KinematicComponent:
        """
         Finds the SIM.KinematicComponent object with the given identifier as recorded in a journal.
         Returns found ( KinematicComponent NXOp):  the found object .
        """
        pass
    def IsMppKinematicsModel(self) -> bool:
        """
         Checks if the current model is a machine powered programming kinematics model 
         Returns result (bool): .
        """
        pass
import NXOpen
class KinematicComponent(NXOpen.NXObject): 
    """  Represents the KinematicComponent class object   """
    def DeleteCaConfigProperties(self) -> None:
        """
         Deletes ca config properties 
        """
        pass
    def DeleteComponent(self, oldChild: KinematicComponent) -> None:
        """
         Deletes a child component 
        """
        pass
    def GetAxis(self) -> KinematicAxis:
        """
         Gets an axis object in the component 
         Returns axis ( KinematicAxis NXOp):  The axis object .
        """
        pass
    def GetJunctions(self) -> List[KinematicJunction]:
        """
         Gets a list of all junctions in the component 
         Returns junctions ( KinematicJunction List[NX):  The list of junctions .
        """
        pass
    def GetParent(self) -> KinematicComponent:
        """
         Gets the parent component 
         Returns parent ( KinematicComponent NXOp):  The parent component .
        """
        pass
    def InsertComponent(self, newChild: KinematicComponent) -> None:
        """
         Adds a new child component 
        """
        pass
    def InsertJunction(self, junction: KinematicJunction) -> None:
        """
         Adds a new junction to the component 
        """
        pass
import NXOpen
import NXOpen.SIM.PostConfigurator
class KinematicConfigurator(NXOpen.NXObject): 
    """  Represents the ISV base class object   """
    class UniteTypes(Enum):
        """
        Members Include: 
         |Create|  Create the spinning geometries as individual bodies 
         |Unite|  Unite the spinning geometries into one body 

        """
        Create: int
        Unite: int
        @staticmethod
        def ValueOf(value: int) -> KinematicConfigurator.UniteTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def IsvControlPanelBuilder(self) -> IsvControlPanelBuilder:
        """
        Getter for property: ( IsvControlPanelBuilder NXOp) IsvControlPanelBuilder
         Returns the isv control panel builder   
            
         
        """
        pass
    @property
    def ComponentCollection() -> KinematicComponentCollection:
        """
         Returns the ComponentCollection instance belonging to this SimKim 
        """
        pass
    def AddChannel(self, channel: str) -> None:
        """
         Adds a new user channel name to the list of channels 
        """
        pass
    def AddHoldingSystem(self, holdSys: str) -> None:
        """
         Adds a new user holding system to the list of holding systems 
        """
        pass
    def AddPocketToDynamicItems(self) -> KinematicComponent:
        """
         Adds a pocket to dynamic items 
         Returns pocket ( KinematicComponent NXOp):  The created pocket .
        """
        pass
    def AddUserClassification(self, userClass: str) -> None:
        """
         Adds a new user class name to the list of user classes 
        """
        pass
    def CopyKinematicModel(self) -> KinematicModel:
        """
         Copy a kinematic model.
                    User need to call NXOpen.SIM.KinematicConfigurator.DeleteKinematicModel to delete the copy of kinematic model.
                
         Returns kimModel ( KinematicModel NXOp):  The copy of kinematic model .
        """
        pass
    def CreateArchiveImportBuilder(self) -> ArchiveImportBuilder:
        """
         Creates a builder to import a Sinumerik archive file 
         Returns builder ( ArchiveImportBuilder NXOp):  The new CamtImport builder .
        """
        pass
    def CreateAxisBuilder(self, parent: KinematicComponent, jct: KinematicJunction, axis: KinematicAxis) -> KinematicAxisBuilder:
        """
         Creates a builder for a kinematic axis 
         Returns builder ( KinematicAxisBuilder NXOp):  The new axis builder .
        """
        pass
    def CreateChannelConfigurationBuilder(self) -> KinematicChannelConfigurationBuilder:
        """
         Creates a builder for a kinematic channel configurator 
         Returns builder ( KinematicChannelConfigurationBuilder NXOp):  The new kinematic channel configuration builder .
        """
        pass
    def CreateCollisionPairBuilder(self) -> CollisionPairBuilder:
        """
         Creates a collision pair builder 
         Returns builder ( CollisionPairBuilder NXOp):  The new collision pair builder .
        """
        pass
    def CreateConvertFromMcdBuilder(self) -> ConvertFromMCDBuilder:
        """
         Creates a builder to convert from MCD 
         Returns builder ( ConvertFromMCDBuilder NXOp):  The new convert from mcd builder .
        """
        pass
    def CreateImportMcfBuilder(self) -> KinematicImportMcfBuilder:
        """
         Creates a builder for a import axis and channel data from mcf 
         Returns builder ( KinematicImportMcfBuilder NXOp):  The import axis and channel data builder .
        """
        pass
    @overload
    def CreateIsvControlPanelBuilder(self, driverType: IsvControlPanelBuilder.VisualizationType, objects: List[CAMObject]) -> IsvControlPanelBuilder:
        """
         Creates an isv control panel builder 
         Returns builder ( IsvControlPanelBuilder NXOp):  The isv control panel builder .
        """
        pass
    @overload
    def CreateIsvControlPanelBuilder(self, driverType: IsvControlPanelBuilder.VisualizationType, channelData: NcChannelSelectionData) -> IsvControlPanelBuilder:
        """
         Creates an isv control panel builder with given machine code file name.
         Returns builder ( IsvControlPanelBuilder NXOp):  The isv control panel builder .
        """
        pass
    def CreateJunctionBuilder(self, parent: KinematicComponent, jct: KinematicJunction) -> KinematicJunctionBuilder:
        """
         Creates a builder for a kinematic junction 
         Returns builder ( KinematicJunctionBuilder NXOp):  The new junction builder .
        """
        pass
    def CreateKinematicChain(self) -> KinematicChain:
        """
         Creates a builder for a kinematic chain 
         Returns builder ( KinematicChain NXOp):  The new kinematic chain builder .
        """
        pass
    def CreateKinematicChannelBuilder(self) -> KinematicChannelBuilder:
        """
         Creates a builder for a channel 
         Returns builder ( KinematicChannelBuilder NXOp):  The new kinematic channel builder .
        """
        pass
    def CreateKinematicSinumerikCaBuilder(self, comp: KinematicComponent) -> KinematicSinumerikCaBuilder:
        """
         Creates a builder for a kinematic sinumerik ca config 
         Returns builder ( KinematicSinumerikCaBuilder NXOp):  The new kinematic sinumerik ca builder .
        """
        pass
    def CreateMachineKitBuilder(self) -> MachineKitBuilder:
        """
         Creates a builder for the machine tool kit 
         Returns builder ( MachineKitBuilder NXOp):  The machine kit builder .
        """
        pass
    def CreateMachineLibraryBuilder(self) -> MachineLibraryBuilder:
        """
         Creates a builder for the machine tool Library dialog 
         Returns builder ( MachineLibraryBuilder NXOp):  The machine Library builder .
        """
        pass
    def CreateMachineToolConfigurationBuilder(self) -> MachineToolConfiguration:
        """
         Creates a builder for the Machine Tool Configuration 
         Returns builder ( MachineToolConfiguration NXOp):  The new machine tool configuration builder .
        """
        pass
    def CreateNcChannelSelectionData(self) -> NcChannelSelectionData:
        """
         Creates an NcChannelSelectionData object to which files and channels can be assigned.  This is used when constructing the builder. 
         Returns ncChannelSelectionData ( NcChannelSelectionData NXOp):  The NC channel selection data.
        """
        pass
    def CreateNcProgramManagerBuilder(self) -> NcProgramManagerBuilder:
        """
         Creates a builder for the nc program manager 
         Returns builder ( NcProgramManagerBuilder NXOp):  The nc program manager builder .
        """
        pass
    def CreateSimDebugBuilder(self) -> SimDebugBuilder:
        """
         Creates a sim debug builder 
         Returns builder ( SimDebugBuilder NXOp):  The new sim debug builder .
        """
        pass
    def CreateSimulationLoadsnapshotBuilder(self) -> LoadSnapshotBuilder:
        """
         Creates a builder for the load snapshot 
         Returns builder ( LoadSnapshotBuilder NXOp):  The load snapshot builder .
        """
        pass
    def CreateSimulationOptionsBuilder(self, dialogType: SimulationOptionsBuilder.DialogType) -> SimulationOptionsBuilder:
        """
         Creates a simulation options 
         Returns builder ( SimulationOptionsBuilder NXOp):  The new simulation options .
        """
        pass
    def CreateSimulationSavesnapshotBuilder(self) -> SaveSnapshotBuilder:
        """
         Creates a builder for the save snapshot 
         Returns builder ( SaveSnapshotBuilder NXOp):  The save snapshot builder .
        """
        pass
    def CreateSinumerikCaExportBuilder(self) -> SinumerikCaExportBuilder:
        """
         Creates a builder for a sinumerik ca export spf 
         Returns builder ( SinumerikCaExportBuilder NXOp):  The new sinumerik ca export builder .
        """
        pass
    def CreateSinumerikCaFacetBuilder(self) -> SinumerikCaFacetBuilder:
        """
         Creates a builder for a sinumerik ca facet 
         Returns builder ( SinumerikCaFacetBuilder NXOp):  The new sinumerik ca facet builder .
        """
        pass
    def CreateSinumerikCaPlaceholderBuilder(self) -> SinumerikCaPlaceholderBuilder:
        """
         Creates a builder for a sinumerik ca placeholder 
         Returns builder ( SinumerikCaPlaceholderBuilder NXOp):  The new sinumerik ca placeholder builder .
        """
        pass
    def CreateSinumerikCaSimplifyBodiesBuilder(self) -> SinumerikCaSimplifyBodiesBuilder:
        """
         Creates a builder for a sinumerik ca simplify bodies 
         Returns builder ( SinumerikCaSimplifyBodiesBuilder NXOp):  The new sinumerik ca simplify bodies builder .
        """
        pass
    def CreateSmkDebugBuilder(self) -> SmkDebugBuilder:
        """
         Creates a builder for the smart machine kit debug dialog 
         Returns builder ( SmkDebugBuilder NXOp):  The smk debug builder .
        """
        pass
    def CreateSmkMachineKitCreationPostBuilder(self) -> NXOpen.SIM.PostConfigurator.CreationPostBuilder:
        """
         Creates a builder for the smart machine kit machine creation post dialog 
         Returns builder ( NXOpen.SIM.PostConfigurator.CreationPostBuilder):  The smk machine creation post builder .
        """
        pass
    def CreateSmkMachineKitEditorBuilder(self) -> SmkMachineKitEditorBuilder:
        """
         Creates a builder for the smart machine kit machine specific information dialog 
         Returns builder ( SmkMachineKitEditorBuilder NXOp):  The smk machine specific information builder .
        """
        pass
    def CreateSmkTransitionPathEditorBuilder(self) -> SmkTransitionPathEditorBuilder:
        """
         Creates a builder for the transition path editor dialog 
         Returns builder ( SmkTransitionPathEditorBuilder NXOp):  The transition path editor builder .
        """
        pass
    def CreateSmkWizardBuilder(self) -> SmkWizardBuilder:
        """
         Creates a builder for the smart machine kit wizard dialog 
         Returns builder ( SmkWizardBuilder NXOp):  The smk wizard builder .
        """
        pass
    def CreateSpinningClone(self, source: KinematicComponent, combine: bool) -> KinematicComponent:
        """
         Creates a copy of the given component and spins its assigned geometry around a spinning axis.
                    For tool components, the X-axis of the tool tip junction is used as spinning axis. If none
                    is defined and for other types of components, the X-axis of the WCS is used.
                    The new component has the same parent as the source component. 
         Returns clone ( KinematicComponent NXOp):  The new spinning component .
        """
        pass
    def DefineKinematicChains(self) -> KinematicChainConfiguration:
        """
         Creates a builder for a kinematic chain configurator 
         Returns builder ( KinematicChainConfiguration NXOp):  The new kinematic chain configuration builder .
        """
        pass
    def DeleteAllChannels(self) -> None:
        """
         Deletes all channels from the kinematic model 
        """
        pass
    def DeleteAllHoldingSystems(self) -> None:
        """
         Delete all holding systems from the kinematic model 
        """
        pass
    def DeleteAxis(self, axis: KinematicAxis) -> None:
        """
         Deletes the given axis 
        """
        pass
    def DeleteChannel(self, channel: str) -> None:
        """
         Deletes a channel name from the list of channels 
        """
        pass
    def DeleteComponent(self, comp: KinematicComponent) -> None:
        """
         Deletes the given component 
        """
        pass
    def DeleteDevice(self, component: KinematicComponent) -> None:
        """
         Deletes the given device 
        """
        pass
    def DeleteHoldingSystem(self, holdSys: str) -> None:
        """
         Delete a holding system from the list 
        """
        pass
    def DeleteJunction(self, jct: KinematicJunction) -> None:
        """
         Deletes the given junction 
        """
        pass
    def DeleteKinematicModel(self, kimModel: KinematicModel) -> None:
        """
         Delete the copy of kinematic model. 
        """
        pass
    def DeleteLastPocketFromDynamicItems(self) -> None:
        """
         Deletes last pocket from dynamic items 
        """
        pass
    def DeleteModel(self) -> None:
        """
         Deletes the entire kinematic model 
        """
        pass
    def DeleteRootComponent(self, oldRoot: KinematicComponent) -> None:
        """
         Delete a root component from the NXOpen.SIM.KinematicConfigurator object 
        """
        pass
    def DeleteTool(self, component: KinematicComponent) -> None:
        """
         Deletes the given tool 
        """
        pass
    def DeleteUserClassification(self, userClass: str) -> None:
        """
         Deletes a user class name from the list of user classes 
        """
        pass
    def EncryptModel(self, soldToIDs: List[str], expirationDate: str) -> None:
        """
         Encrypt the entire kinematic model 
        """
        pass
    def ExportMachineKitBuilder(self, machineName: str) -> ExportMachineKitBuilder:
        """
         Creates a builder for export the machine tool kit 
         Returns builder ( ExportMachineKitBuilder NXOp):  The machine kit builder .
        """
        pass
    def ExportModel(self, path: str) -> None:
        """
         Export the entire kinematic model 
        """
        pass
    def FindAvailablePocket(self, component: KinematicComponent) -> KinematicComponent:
        """
         Finds an available pocket in the given component 
         Returns pocket ( KinematicComponent NXOp):  The found pocket .
        """
        pass
    def FindAxis(self, name: str) -> Tuple[KinematicAxis, KinematicComponent, KinematicJunction]:
        """
         Find the axis with the given name 
         Returns A tuple consisting of (axis, pComp, pJct). 
         - axis is:  KinematicAxis NXOp. The axis, if found .
         - pComp is:  KinematicComponent NXOp. The parent component of the axis .
         - pJct is:  KinematicJunction NXOp. The parent junction of the axis .

        """
        pass
    def FindComponentsBySystemClass(self, sysclass: KinematicComponentBuilder.SystemClass) -> List[KinematicComponent]:
        """
         Finds component which are of the given system class 
         Returns comps ( KinematicComponent List[NX):  The found components .
        """
        pass
    @overload
    def FindJunction(self, name: str) -> KinematicJunction:
        """
         Find the junction with the given name 
         Returns jct ( KinematicJunction NXOp):  The junction, if found .
        """
        pass
    @overload
    def FindJunction(self, csys: NXOpen.NXObject) -> KinematicJunction:
        """
         Finds a junction by its coordinate system 
         Returns jct ( KinematicJunction NXOp):  The junction for the csys .
        """
        pass
    def FindOwnerOfJunction(self, jct: KinematicJunction) -> KinematicComponent:
        """
         Finds the NXOpen.SIM.KinematicComponent which is the owner of this junction 
         Returns owner ( KinematicComponent NXOp):  The owning component of the junction .
        """
        pass
    def FindParentComponent(self, comp: KinematicComponent) -> KinematicComponent:
        """
         Finds the NXOpen.SIM.KinematicComponent which is the parent of this component 
         Returns parent ( KinematicComponent NXOp):  The parent Component. NULL if comp is root component .
        """
        pass
    def GetAxes(self) -> List[KinematicAxis]:
        """
         Gets a list of all axes in the kinematic 
         Returns axes ( KinematicAxis List[NX):  The list of axes .
        """
        pass
    def GetAxisNames(self) -> List[str]:
        """
         Gets a list of all axis names in the kinematic 
         Returns axes (List[str]):  The list of axis names .
        """
        pass
    def GetChannels(self) -> List[str]:
        """
         Get a list of all channels 
         Returns channels (List[str]):  The list of channels   .
        """
        pass
    def GetHoldingSystems(self) -> List[str]:
        """
         Get a list of all holding systems 
         Returns holdSys (List[str]):  The holding systems           .
        """
        pass
    def GetJunctionNames(self) -> List[str]:
        """
         Gets a list of all junction names in the kinematic 
         Returns junctions (List[str]):  The list of junction names .
        """
        pass
    def GetJunctions(self) -> List[KinematicJunction]:
        """
         Gets a list of all junctions in the kinematic 
         Returns junctions ( KinematicJunction List[NX):  The list of junctions .
        """
        pass
    def GetName(self) -> str:
        """
         Returns the custom name of the kinematic model 
         Returns name (str):  The kinematic model name .
        """
        pass
    def GetUserClassifications(self) -> List[str]:
        """
         Get a list of all user classes 
         Returns uClasses (List[str]):  The list of user classes   .
        """
        pass
    def ImportMachineBuilderFromZipFile(self, zipPath: str) -> ImportMachineKitBuilder:
        """
         Creates a builder for import the machine tool kit from zip file
         Returns builder ( ImportMachineKitBuilder NXOp):  The import machine zip builder .
        """
        pass
    def ImportMachineKitBuilder(self, kitPath: str) -> ImportMachineKitBuilder:
        """
         Creates a builder for import the machine tool kit 
         Returns builder ( ImportMachineKitBuilder NXOp):  The import machine kit builder .
        """
        pass
    def ImportMachineSpecificData(self, path: str) -> None:
        """
         Import the machine specific data 
        """
        pass
    def ImportModel(self, path: str) -> None:
        """
         Import the entire kinematic model 
        """
        pass
    def ImportNcArchive(self, ncFileName: str, printReport: bool) -> None:
        """
         Import the nc archive for the Machine Tool Configuration 
        """
        pass
    def InsertRootComponent(self, newRoot: KinematicComponent) -> None:
        """
         Adds a new root component to the NXOpen.SIM.KinematicConfigurator object 
        """
        pass
    def IsAxisAssignedToChannel(self, axisName: str, channelName: str) -> bool:
        """
         Check if the axis with the given name is assigned to the specified channel
         Returns isAssigned (bool):  Boolean result set to true if the axis is found in the kinematic tree and assigned to the channel .
        """
        pass
    def MoveComponent(self, component: KinematicComponent, target: KinematicComponent) -> None:
        """
         Moves the given component 
        """
        pass
    def RenameChannel(self, oldName: str, newName: str) -> None:
        """
         Renames a channel name from the list 
        """
        pass
    def RenameHoldingSystem(self, oldName: str, newName: str) -> None:
        """
         Renames a holding system from the list 
        """
        pass
    def RenameUserClassification(self, oldName: str, newName: str) -> None:
        """
         Renames a user class name from the list 
        """
        pass
    def SetName(self, name: str) -> None:
        """
         Sets the custom name of the kinematic model 
        """
        pass
import NXOpen
class KinematicImportMcfBuilder(NXOpen.Builder): 
    """  Represents a builder for an import axis and channel data  from mcf   """
    @property
    def IgnoreLimits(self) -> bool:
        """
        Getter for property: (bool) IgnoreLimits
         Returns the flag which determines if the Limits of the MCF and the Kim are merge.  
           
                    the soft limits are set based on the hard Limits of the Machine Tool Builder
                    or if the limits in the mcf are useful they will be taken from MCF.  
         
        """
        pass
    @IgnoreLimits.setter
    def IgnoreLimits(self, replace: bool):
        """
        Setter for property: (bool) IgnoreLimits
         Returns the flag which determines if the Limits of the MCF and the Kim are merge.  
           
                    the soft limits are set based on the hard Limits of the Machine Tool Builder
                    or if the limits in the mcf are useful they will be taken from MCF.  
         
        """
        pass
    @property
    def McfPath(self) -> str:
        """
        Getter for property: (str) McfPath
         Returns the path from the mcf file   
            
         
        """
        pass
    @McfPath.setter
    def McfPath(self, path: str):
        """
        Setter for property: (str) McfPath
         Returns the path from the mcf file   
            
         
        """
        pass
    @property
    def ReplaceChannel(self) -> bool:
        """
        Getter for property: (bool) ReplaceChannel
         Returns the flag which determines if the channel data of the Machine Tool Builder are 
                    deleted befor they are replaced through the Channel data of the MCF-File  
            
         
        """
        pass
    @ReplaceChannel.setter
    def ReplaceChannel(self, replace: bool):
        """
        Setter for property: (bool) ReplaceChannel
         Returns the flag which determines if the channel data of the Machine Tool Builder are 
                    deleted befor they are replaced through the Channel data of the MCF-File  
            
         
        """
        pass
import NXOpen
class KinematicJunctionBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[KinematicJunctionBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: KinematicJunctionBuilder) -> None:
        """
         Appends an object to the list
            
        """
        pass
    @overload
    def Clear(self) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    def ClearIndex(self, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
               not change, but the item at this index is set to NULL.
            
        """
        pass
    @overload
    def Clear(self, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    @overload
    def Erase(self, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, obj: KinematicJunctionBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: KinematicJunctionBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: KinematicJunctionBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> KinematicJunctionBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( KinematicJunctionBuilder NXOp):  object found at input index .
        """
        pass
    def GetContents(self) -> List[KinematicJunctionBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( KinematicJunctionBuilder List[NX):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: KinematicJunctionBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    def MoveToBottom(self, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    def MoveToTop(self, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    def SetContents(self, objects: List[KinematicJunctionBuilder]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    @overload
    def Swap(self, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    @overload
    def Swap(self, object1: KinematicJunctionBuilder, object2: KinematicJunctionBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class KinematicJunctionBuilder(NXOpen.Builder): 
    """  Represents the SimKimJunctionBuilder class object   """
    class SystemClass(Enum):
        """
        Members Include: 
         |NotSet|  no specal class 
         |Mount|  a mounting junction 
         |MachineZero|  the machine zero junction 
         |ToolZero|  the tool mounting point 
         |ToolTip|  The tool tip junction 
         |LatheWpZx|  Lathe Work Plane ZX 
         |LatheWpXy|  Lathe Work Plane XY 
         |RobotBase|  the robot base junction 
         |RobotFlange|  the robot flange junction 
         |PositionerBase|  the positioner base junction 
         |PositionerTool|  the positioner tool junction 

        """
        NotSet: int
        Mount: int
        MachineZero: int
        ToolZero: int
        ToolTip: int
        LatheWpZx: int
        LatheWpXy: int
        RobotBase: int
        RobotFlange: int
        PositionerBase: int
        PositionerTool: int
        @staticmethod
        def ValueOf(value: int) -> KinematicJunctionBuilder.SystemClass:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Classification(self) -> KinematicJunctionBuilder.SystemClass:
        """
        Getter for property: ( KinematicJunctionBuilder.SystemClass NXOp) Classification
         Returns the classification of the junction   
            
         
        """
        pass
    @Classification.setter
    def Classification(self, jctClass: KinematicJunctionBuilder.SystemClass):
        """
        Setter for property: ( KinematicJunctionBuilder.SystemClass NXOp) Classification
         Returns the classification of the junction   
            
         
        """
        pass
    @property
    def Csys(self) -> NXOpen.CartesianCoordinateSystem:
        """
        Getter for property: ( NXOpen.CartesianCoordinateSystem) Csys
         Returns the CSYS associated with the junction   
            
         
        """
        pass
    @Csys.setter
    def Csys(self, csys: NXOpen.CartesianCoordinateSystem):
        """
        Setter for property: ( NXOpen.CartesianCoordinateSystem) Csys
         Returns the CSYS associated with the junction   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the kim junction's name   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the kim junction's name   
            
         
        """
        pass
    def CreateDefaultCsys(self) -> NXOpen.CartesianCoordinateSystem:
        """
         Create the default CSYS based on WCS 
         Returns csys ( NXOpen.CartesianCoordinateSystem):  the default csys .
        """
        pass
    def CreateTooltipCsys(self) -> NXOpen.CartesianCoordinateSystem:
        """
         Create the tooltip CSYS 
         Returns csys ( NXOpen.CartesianCoordinateSystem):  the tooltip csys .
        """
        pass
    def IsMachineZero(self) -> bool:
        """
         Test if this is a machine zero junction 
         Returns result (bool):  true if it is the machine zero junction .
        """
        pass
    def IsToolMount(self) -> bool:
        """
         Test if the junction is a tool mount junctions 
         Returns result (bool):  true if it is a tool mount junction .
        """
        pass
    def IsToolTip(self) -> bool:
        """
         Test if the junction is a tool tip junctions 
         Returns result (bool):  true if it is a tool tip junction .
        """
        pass
import NXOpen
class KinematicJunction(NXOpen.NXObject): 
    """  Represents the KinematicJunction class object   """
    @property
    def Matrix(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: ( NXOpen.Matrix3x3) Matrix
         Returns the matrix of the junction   
            
         
        """
        pass
    @property
    def Origin(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) Origin
         Returns the origin of the junction   
            
         
        """
        pass
import NXOpen
class KinematicModel(NXOpen.NXObject): 
    """ Represents the Kinematic Model class object.
        
        Example how to move machine axes:

        Dim kinematicModel As NXOpen.SIM.KinematicModel
        kinematicModel = kinematicConfigurator.CopyKinematicModel()
            
        Dim kinematicAxis_X1 As NXOpen.SIM.KinematicAxis
        kinematicAxis_X1 = kinematicModel.FindMachineAxis("X1")

        Dim kinematicAxis_Y1 As NXOpen.SIM.KinematicAxis
        kinematicAxis_Y1 = kinematicModel.FindMachineAxis("Y1")

        Dim kinematicAxis_Z1 As NXOpen.SIM.KinematicAxis
        kinematicAxis_Z1 = kinematicModel.FindMachineAxis("Z1")

        kinematicModel.SetMachineAxisValue(kinematicAxis_X1, 100)
        kinematicModel.SetMachineAxisValue(kinematicAxis_Y1, 150)
        kinematicModel.SetMachineAxisValue(kinematicAxis_Z1, 200)

        'Move the axes X1, Y1, Z1 to the position 100, 150, 200 on the graphic window simultaneously
        kinematicModel.UpdateMachineDisplay()
        ...
            
        kinematicConfigurator.DeleteKinematicModel(kinematicModel)
        
    """
    def FindMachineAxis(self, name: str) -> KinematicAxis:
        """
         Find the machine axis with the given name. 
         Returns axis ( KinematicAxis NXOp):  The axis, if found .
        """
        pass
    def SetMachineAxisValue(self, axis: KinematicAxis, value: float) -> None:
        """
         Sets the machine axis to the given value.
                    User need to call NXOpen.SIM.KinematicModel.UpdateMachineDisplay to see the axis moving in the graphic window.
                
        """
        pass
    def UpdateMachineDisplay(self) -> None:
        """
         Update machine display.
                    This call is needed after call NXOpen.SIM.KinematicModel.SetMachineAxisValue to see the axis moving in the graphic window.
                
        """
        pass
import NXOpen
class KinematicSinumerikCaBuilder(NXOpen.Builder): 
    """ This class is used for edit sinumerik collision avoidance properties.
        Calling Builder.Commit on this builder will only return .
    """
    class PlcInitStateTypes(Enum):
        """
        Members Include: 
         |Active|  Active     
         |Inactive|  Inactive   
         |Preselect|  Preselect 

        """
        Active: int
        Inactive: int
        Preselect: int
        @staticmethod
        def ValueOf(value: int) -> KinematicSinumerikCaBuilder.PlcInitStateTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PlcUsageTypes(Enum):
        """
        Members Include: 
         |CollisionCheck|  Collision Check 
         |Visualize|  Visualize       
         |All|  All             

        """
        CollisionCheck: int
        Visualize: int
        All: int
        @staticmethod
        def ValueOf(value: int) -> KinematicSinumerikCaBuilder.PlcUsageTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DetailLevel(self) -> int:
        """
        Getter for property: (int) DetailLevel
         Returns the detail level for this protection area   
            
         
        """
        pass
    @DetailLevel.setter
    def DetailLevel(self, level: int):
        """
        Setter for property: (int) DetailLevel
         Returns the detail level for this protection area   
            
         
        """
        pass
    @property
    def MagazineIndex(self) -> int:
        """
        Getter for property: (int) MagazineIndex
         Returns the magazine index for this automatic protection area   
            
         
        """
        pass
    @MagazineIndex.setter
    def MagazineIndex(self, index: int):
        """
        Setter for property: (int) MagazineIndex
         Returns the magazine index for this automatic protection area   
            
         
        """
        pass
    @property
    def MagazineLocationIndex(self) -> int:
        """
        Getter for property: (int) MagazineLocationIndex
         Returns the magazine location index for this automatic protection area  
            
         
        """
        pass
    @MagazineLocationIndex.setter
    def MagazineLocationIndex(self, index: int):
        """
        Setter for property: (int) MagazineLocationIndex
         Returns the magazine location index for this automatic protection area  
            
         
        """
        pass
    @property
    def PlcBit(self) -> int:
        """
        Getter for property: (int) PlcBit
         Returns the PLC bit for this protection area  
            
         
        """
        pass
    @PlcBit.setter
    def PlcBit(self, bit: int):
        """
        Setter for property: (int) PlcBit
         Returns the PLC bit for this protection area  
            
         
        """
        pass
    @property
    def PlcInitState(self) -> KinematicSinumerikCaBuilder.PlcInitStateTypes:
        """
        Getter for property: ( KinematicSinumerikCaBuilder.PlcInitStateTypes NXOp) PlcInitState
         Returns the initial PLC state for this protection area   
            
         
        """
        pass
    @PlcInitState.setter
    def PlcInitState(self, state: KinematicSinumerikCaBuilder.PlcInitStateTypes):
        """
        Setter for property: ( KinematicSinumerikCaBuilder.PlcInitStateTypes NXOp) PlcInitState
         Returns the initial PLC state for this protection area   
            
         
        """
        pass
    @property
    def PlcUsage(self) -> KinematicSinumerikCaBuilder.PlcUsageTypes:
        """
        Getter for property: ( KinematicSinumerikCaBuilder.PlcUsageTypes NXOp) PlcUsage
         Returns the PLC usage for this protection area   
            
         
        """
        pass
    @PlcUsage.setter
    def PlcUsage(self, usage: KinematicSinumerikCaBuilder.PlcUsageTypes):
        """
        Setter for property: ( KinematicSinumerikCaBuilder.PlcUsageTypes NXOp) PlcUsage
         Returns the PLC usage for this protection area   
            
         
        """
        pass
    @property
    def TOIndex(self) -> int:
        """
        Getter for property: (int) TOIndex
         Returns the TO-index for this automatic protection area   
            
         
        """
        pass
    @TOIndex.setter
    def TOIndex(self, index: int):
        """
        Setter for property: (int) TOIndex
         Returns the TO-index for this automatic protection area   
            
         
        """
        pass
import NXOpen
class LoadSnapshotBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.SIM.LoadSnapshotBuilder
    """
    @property
    def ExternalReference(self) -> str:
        """
        Getter for property: (str) ExternalReference
         Returns the external reference   
            
         
        """
        pass
    @ExternalReference.setter
    def ExternalReference(self, reference: str):
        """
        Setter for property: (str) ExternalReference
         Returns the external reference   
            
         
        """
        pass
    @property
    def RunToSimTime(self) -> bool:
        """
        Getter for property: (bool) RunToSimTime
         Returns the run to simulation time   
            
         
        """
        pass
    @RunToSimTime.setter
    def RunToSimTime(self, bRunToTime: bool):
        """
        Setter for property: (bool) RunToSimTime
         Returns the run to simulation time   
            
         
        """
        pass
    @property
    def Snapshot(self) -> Snapshot:
        """
        Getter for property: ( Snapshot NXOp) Snapshot
         Returns the snapshot   
            
         
        """
        pass
    @Snapshot.setter
    def Snapshot(self, snapshot: Snapshot):
        """
        Setter for property: ( Snapshot NXOp) Snapshot
         Returns the snapshot   
            
         
        """
        pass
    def GetExternalSnapshots(self) -> List[Snapshot]:
        """
         The external snapshots 
         Returns snapshot ( Snapshot List[NX): .
        """
        pass
    @overload
    def GetSnapshot(self, snapshotName: str, setupName: str) -> Snapshot:
        """
         Returns the snapshot 
         Returns snapshot ( Snapshot NXOp): .
        """
        pass
    def SetExternalSnapshotSelection(self, snapshotTags: List[Snapshot], sourceComps: List[str]) -> None:
        """
         The external snapshot selection
        """
        pass
import NXOpen
class MachineKitBuilder(NXOpen.Builder): 
    """ This class is used for the Machine Kit Create Dialog.
        Calling Builder.Commit on this
        builder will start the machine kit creation process
        and return .
     """
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the machine kit name.  
           The name is used for the database entry and the name of the folder.   
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the machine kit name.  
           The name is used for the database entry and the name of the folder.   
         
        """
        pass
    @property
    def OutputDirectory(self) -> str:
        """
        Getter for property: (str) OutputDirectory
         Returns the machine kit output directory.  
           This is the location of the machine folder.   
         
        """
        pass
    @OutputDirectory.setter
    def OutputDirectory(self, output_directory: str):
        """
        Setter for property: (str) OutputDirectory
         Returns the machine kit output directory.  
           This is the location of the machine folder.   
         
        """
        pass
import NXOpen
class MachineLibraryBuilder(NXOpen.Builder): 
    """ This class is used for the Machine Library Dialog.
        Calling Builder.Commit on this builder will only return .
     """
    def EditMachineLibrary(self, machineName: str, attName: str, value: str) -> None:
        """
         Edit a specific machine of the database. That will write the machine_database.dat. 
        """
        pass
    def GetAllAttributeNames(self) -> List[str]:
        """
         Returns a array of the library attributes.
                    This function allocates the memory for attributeNames. The caller is responsible to deallocate the memory.
         Returns attributeNames (List[str]):  array of all attribute names.
        """
        pass
    def GetAllMachineNames(self) -> List[str]:
        """
         Returns a array of the machine names(librefs) that are in the machine database. 
                    This function allocates the memory for machineNames. The caller is responsible to deallocate the memory.
         Returns machineNames (List[str]):  array of all machine names (libref).
        """
        pass
    def GetValue(self, machineName: str, attName: str) -> str:
        """
         Returns the attribute value of a specific machine. 
         Returns value (str): .
        """
        pass
    def InsertEntryToMachineLibrary(self, selectedMachineName: str) -> str:
        """
         Insert a machine entry to the machine_database.dat. The libref is the name of the machine entry,
                    that is copied, the libref appended by a count and the new entry is put in the list as next entry.
                If the libref is empty, a default entry is add to the bottom of the list. 
         Returns machineName (str):  machine name (libref), of the new machien entry.
        """
        pass
    def RemoveEntryFromMachineLibrary(self, machineName: str) -> None:
        """
         Removes a machine entry from the machine_database.dat. The libref is the name of the machine entry,
                    that will reomved from the Library. 
        """
        pass
import NXOpen
class MachineToolConfiguration(NXOpen.Builder): 
    """ Represents a Machine Tool Configuration object.
    """
    class ControllerLines(Enum):
        """
        Members Include: 
         |Solutionline|  The solutionline controller line 
         |Powerline|  The powerline controller line 

        """
        Solutionline: int
        Powerline: int
        @staticmethod
        def ValueOf(value: int) -> MachineToolConfiguration.ControllerLines:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MdynamicsTypes(Enum):
        """
        Members Include: 
         |Fiveaxmill|  The Five Axis Milling MDynamics type 

        """
        Fiveaxmill: int
        @staticmethod
        def ValueOf(value: int) -> MachineToolConfiguration.MdynamicsTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PlaneTypes(Enum):
        """
        Members Include: 
         |Operator|  The operator panel plane type 
         |G17|  The G17 plane type 
         |G18|  The G18 plane type 
         |G19|  The G19 plane type 

        """
        Operator: int
        G17: int
        G18: int
        G19: int
        @staticmethod
        def ValueOf(value: int) -> MachineToolConfiguration.PlaneTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SwivelingTypes(Enum):
        """
        Members Include: 
         |Cycle800|  The CYCLE800 swiveling type 
         |Transarot|  The TRANSAROT swiveling type 

        """
        Cycle800: int
        Transarot: int
        @staticmethod
        def ValueOf(value: int) -> MachineToolConfiguration.SwivelingTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TechnologyTypes(Enum):
        """
        Members Include: 
         |Mill|  The mill technology type 
         |Turn|  The lathe technology type 
         |Millturn|  The millturn technology type 
         |NotSet|  No technology type 

        """
        Mill: int
        Turn: int
        Millturn: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> MachineToolConfiguration.TechnologyTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class UnitTypes(Enum):
        """
        Members Include: 
         |Mm|  The millimeter unit type 
         |In|  The inch unit type 

        """
        Mm: int
        In: int
        @staticmethod
        def ValueOf(value: int) -> MachineToolConfiguration.UnitTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ControllerLine(self) -> MachineToolConfiguration.ControllerLines:
        """
        Getter for property: ( MachineToolConfiguration.ControllerLines NXOp) ControllerLine
         Returns the controller line   
            
         
        """
        pass
    @ControllerLine.setter
    def ControllerLine(self, line: MachineToolConfiguration.ControllerLines):
        """
        Setter for property: ( MachineToolConfiguration.ControllerLines NXOp) ControllerLine
         Returns the controller line   
            
         
        """
        pass
    @property
    def ControllerType(self) -> str:
        """
        Getter for property: (str) ControllerType
         Returns the controller type   
            
         
        """
        pass
    @ControllerType.setter
    def ControllerType(self, controllerType: str):
        """
        Setter for property: (str) ControllerType
         Returns the controller type   
            
         
        """
        pass
    @property
    def CycleTime(self) -> float:
        """
        Getter for property: (float) CycleTime
         Returns the cycle time   
            
         
        """
        pass
    @CycleTime.setter
    def CycleTime(self, cycleTime: float):
        """
        Setter for property: (float) CycleTime
         Returns the cycle time   
            
         
        """
        pass
    @property
    def MachineName(self) -> str:
        """
        Getter for property: (str) MachineName
         Returns the machine name   
            
         
        """
        pass
    @MachineName.setter
    def MachineName(self, name: str):
        """
        Setter for property: (str) MachineName
         Returns the machine name   
            
         
        """
        pass
    @property
    def MachineVendor(self) -> str:
        """
        Getter for property: (str) MachineVendor
         Returns the machine vendor   
            
         
        """
        pass
    @MachineVendor.setter
    def MachineVendor(self, vendor: str):
        """
        Setter for property: (str) MachineVendor
         Returns the machine vendor   
            
         
        """
        pass
    @property
    def ToolCarrierName(self) -> str:
        """
        Getter for property: (str) ToolCarrierName
         Returns the tool carrier name   
            
         
        """
        pass
    @ToolCarrierName.setter
    def ToolCarrierName(self, carrierName: str):
        """
        Setter for property: (str) ToolCarrierName
         Returns the tool carrier name   
            
         
        """
        pass
    def GetArchiveControllerType(self) -> int:
        """
         Retrieves the archive controller type 
         Returns archiveControllerType (int):  The archive controller type .
        """
        pass
    def GetArchiveControllerVersion(self) -> str:
        """
         Retrieves the archive controller version 
         Returns archiveControllerVersion (str):  The archive controller version .
        """
        pass
    def GetChannelPlaneMill(self, channelName: str) -> MachineToolConfiguration.PlaneTypes:
        """
         Retrieves the plane mill from a channel 
         Returns planeMill ( MachineToolConfiguration.PlaneTypes NXOp):  The plane mill value .
        """
        pass
    def GetChannelPlaneTurn(self, channelName: str) -> MachineToolConfiguration.PlaneTypes:
        """
         Retrieves the plane turn from a channel 
         Returns planeTurn ( MachineToolConfiguration.PlaneTypes NXOp):  The plane turn value .
        """
        pass
    def GetChannelSwiveling(self, channelName: str) -> MachineToolConfiguration.SwivelingTypes:
        """
         Retrieves channel's swiveling mode 
         Returns value ( MachineToolConfiguration.SwivelingTypes NXOp):  The swiveling mode value .
        """
        pass
    def GetChannelTcpmSupport(self, channelName: str) -> bool:
        """
         Retrieves machine TCPM support 
         Returns value (bool):  The TCPM support value .
        """
        pass
    def GetChannelToolAsSubprogram(self, channelName: str) -> bool:
        """
         Retrieves a channel's subprogram support 
         Returns value (bool):  The tool as subprogram mode value .
        """
        pass
    def GetChannelToolCommand(self, channelName: str) -> str:
        """
         Retrieves a channel's tool command 
         Returns toolCommand (str):  The tool command  .
        """
        pass
    def GetChannelToolPreselect(self, channelName: str) -> str:
        """
         Retrieves a channel's tool preselect 
         Returns toolPreselect (str):  The tool preselect  .
        """
        pass
    def GetCircularPrecision(self, channelName: str) -> float:
        """
         Retrieves the circular precision 
         Returns circularPrecision (float):  The circular precision value .
        """
        pass
    def GetCircularPrecisionFactor(self, channelName: str) -> float:
        """
         Retrieves the circular precision factor 
         Returns circularPrecisionFactor (float):  The circular precision factor .
        """
        pass
    def GetControllerLanguage(self) -> str:
        """
         Retrieves the controller language 
         Returns controllerLanguage (str):  The controller language .
        """
        pass
    def GetControllerVersion(self) -> str:
        """
         Retrieves the controller version 
         Returns controllerVersion (str):  The controller version .
        """
        pass
    def GetDiameterGeoAxisName(self, channelName: str) -> str:
        """
         Retrieves the diameter geo axis name, which change the output behavior of length values during turning.
         Returns diameterMode (str):  The diameter geo axis name .
        """
        pass
    def GetLookahead(self, channelName: str) -> int:
        """
         Retrieves the controller lookahead, which indicates how many lines are evaluate from the controller ahead.
         Returns lookAhead (int):  The controller lookahead .
        """
        pass
    def GetMachineTechnology(self, channelName: str) -> MachineToolConfiguration.TechnologyTypes:
        """
         Retrieves the machine technology 
         Returns technology ( MachineToolConfiguration.TechnologyTypes NXOp):  The machine technology .
        """
        pass
    def GetMdynamics(self) -> MachineToolConfiguration.MdynamicsTypes:
        """
         Retrieve the MDynamics information 
         Returns mdynamics ( MachineToolConfiguration.MdynamicsTypes NXOp):  The mdynamics value .
        """
        pass
    def GetResolutionDeg(self) -> float:
        """
         Retrieves the degree resolution 
         Returns resolutionValue (float):  The degree resolution value .
        """
        pass
    def GetResolutionMm(self) -> float:
        """
         Retrieves the millimeter resolution 
         Returns resolutionValue (float):  The millimeter resolution value .
        """
        pass
    def GetToolCarrierDirectionSelection(self, channelName: str, carrierName: str) -> int:
        """
         Retrieves the direction selection for a tool carrier. 
         Returns directionSelection (int): .
        """
        pass
    def GetToolCarrierRetraction(self, channelName: str, carrierName: str) -> int:
        """
         Retrieves the retraction for a tool carrier. 
         Returns retraction (int): .
        """
        pass
    def GetToolCarrierSwivelMode(self, channelName: str, carrierName: str) -> int:
        """
         Retrieves the swiveling mode for a tool carrier. 
         Returns swivelingMode (int): .
        """
        pass
    def GetToolCarrierXRetractionPosition(self, channelName: str, carrierName: str) -> float:
        """
         Retrieves the X retraction position for a tool carrier. 
         Returns xPosition (float): .
        """
        pass
    def GetToolCarrierYRetractionPosition(self, channelName: str, carrierName: str) -> float:
        """
         Retrieves the Y retraction position for a tool carrier. 
         Returns yPosition (float): .
        """
        pass
    def GetToolCarrierZRetractionPosition(self, channelName: str, carrierName: str) -> float:
        """
         Retrieves the Z retraction position for a tool carrier. 
         Returns zPosition (float): .
        """
        pass
    def GetToolRadiusCompensation(self) -> bool:
        """
         Retrieves the 3D Tool Radius Compensation information 
         Returns compensation (bool):  The Tool Radius value .
        """
        pass
    def GetUsedUnit(self) -> int:
        """
         Retrieves the used unit 
         Returns usedUnit (int):  The used unit .
        """
        pass
    def SetArchiveControllerType(self, newArchiveControllerType: int) -> None:
        """
         Sets the archive controller type 
        """
        pass
    def SetArchiveControllerVersion(self, newArchiveControllerVersion: str) -> None:
        """
         Sets the archive controller version 
        """
        pass
    def SetChannelPlaneMill(self, channelName: str, newPlaneMill: MachineToolConfiguration.PlaneTypes) -> None:
        """
         Sets the plane mill for a channel 
        """
        pass
    def SetChannelPlaneTurn(self, channelName: str, newPlaneTurn: MachineToolConfiguration.PlaneTypes) -> None:
        """
         Sets the plane turn for a channel 
        """
        pass
    def SetChannelSwiveling(self, channelName: str, value: MachineToolConfiguration.SwivelingTypes) -> None:
        """
         Sets the channel's swiveling mode 
        """
        pass
    def SetChannelTcpmSupport(self, channelName: str, value: bool) -> None:
        """
         Sets the TCPM support value 
        """
        pass
    def SetChannelToolAsSubprogram(self, channelName: str, value: bool) -> None:
        """
         Sets a channel's subprogram support 
        """
        pass
    def SetChannelToolCommand(self, channelName: str, newToolCommand: str) -> None:
        """
         Sets a channel's tool command 
        """
        pass
    def SetChannelToolPreselect(self, channelName: str, newToolPreselect: str) -> None:
        """
         Sets a channel's tool preselect 
        """
        pass
    def SetCircularPrecision(self, channelName: str, newCircularPrecision: float) -> None:
        """
         Sets the circular precision 
        """
        pass
    def SetCircularPrecisionFactor(self, channelName: str, newCircularPrecisionFactor: float) -> None:
        """
         Sets the circular precision factor 
        """
        pass
    def SetControllerLanguage(self, newLanguage: str) -> None:
        """
         Sets the controller language 
        """
        pass
    def SetControllerVersion(self, newVersion: str) -> None:
        """
         Sets the controller version 
        """
        pass
    def SetDiameterGeoAxisName(self, channelName: str, newDiameterMode: str) -> None:
        """
         Sets the diameter geo axis name, which change the output behavior of length values during turning.
        """
        pass
    def SetLookahead(self, channelName: str, lookAhead: int) -> None:
        """
         Sets the controller lookahead, which indicates how many lines are evaluate from the controller ahead.
        """
        pass
    def SetMachineTechnology(self, channelName: str, technology: MachineToolConfiguration.TechnologyTypes) -> None:
        """
         Sets the machine technology 
        """
        pass
    def SetMdynamics(self, newMDynamicsValue: MachineToolConfiguration.MdynamicsTypes) -> None:
        """
         Sets the Mdynamics value 
        """
        pass
    def SetResolutionDeg(self, newResolutionValue: float) -> None:
        """
         Sets the degree resolution value 
        """
        pass
    def SetResolutionMm(self, newResolutionValue: float) -> None:
        """
         Sets the millimeter resolution value 
        """
        pass
    def SetToolCarrierDirectionSelection(self, channelName: str, carrierName: str, newDirectionSelection: int) -> None:
        """
         Sets the direction selection for a tool carrier. 
        """
        pass
    def SetToolCarrierRetraction(self, channelName: str, carrierName: str, newRetraction: int) -> None:
        """
         Sets the retraction for a tool carrier. 
        """
        pass
    def SetToolCarrierSwivelMode(self, channelName: str, carrierName: str, newSwivelingMode: int) -> None:
        """
         Sets the swiveling mode for a tool carrier. 
        """
        pass
    def SetToolCarrierXRetractionPosition(self, channelName: str, carrierName: str, newXPosition: float) -> None:
        """
         Sets the X retraction position for a tool carrier. 
        """
        pass
    def SetToolCarrierYRetractionPosition(self, channelName: str, carrierName: str, newYPosition: float) -> None:
        """
         Sets the Y retraction position for a tool carrier. 
        """
        pass
    def SetToolCarrierZRetractionPosition(self, channelName: str, carrierName: str, newZPosition: float) -> None:
        """
         Sets the Z retraction position for a tool carrier. 
        """
        pass
    def SetToolRadiusCompensation(self, newCompensationValue: bool) -> None:
        """
         Sets the 3D Tool Radius Compensation information 
        """
        pass
    def SetUsedUnit(self, newUsedUnit: int) -> None:
        """
         Sets the used unit 
        """
        pass
import NXOpen
class NcChannelSelectionData(NXOpen.NXObject): 
    """  Represents the NcChannelSelectionData class object   """
    @overload
    def AssignFile(self, channel: int, file: str) -> None:
        """
         Assign a file to a channel using the channel number. 
        """
        pass
    @overload
    def AssignFile(self, channel: str, file: str) -> None:
        """
         Assign a file to a channel using the channel name. 
        """
        pass
    def AssignProgram(self, channel: str, program: NcProgram) -> None:
        """
         Assign an existing main program to a channel using the channel name. 
        """
        pass
import NXOpen
class NcProgramManagerBuilder(NXOpen.Builder): 
    """ Represents a NcProgramManagerBuilder builder object. """
    def ActivateAllBreakpoints(self) -> None:
        """
         Activate all deactivated breakpoints. 
        """
        pass
    def ActivateBreakpoint(self, program: NcProgram, lineNumber: int) -> None:
        """
         Activate a breakpoint in a program line. 
        """
        pass
    def AddBreakpoint(self, program: NcProgram, lineNumber: int) -> None:
        """
         Add a breakpoint to a program line. Simulation stops when it reaches this line.
        """
        pass
    def AddDataBreakpoint(self, condition: str) -> None:
        """
         Add a data breakpoint to program manager. This breakpoint is not associated with a specific program line.
                    Simulation stops when the condition's value changes. 
        """
        pass
    def AddMatchingBreakpoint(self, condition: str) -> None:
        """
         Add a matching breakpoint to program manager. This breakpoint is not associated with a specific program line.
                    Simulation stops when the condition string is found in the current program line. 
        """
        pass
    def DeactivateAllBreakpoints(self) -> None:
        """
         Deactivate all active breakpoints. 
        """
        pass
    def DeactivateBreakpoint(self, program: NcProgram, lineNumber: int) -> None:
        """
         Deactivate a breakpoint in a program line. 
        """
        pass
    def DeleteAllBreakpoints(self) -> None:
        """
         Delete all breakpoints. 
        """
        pass
    def DeleteBreakpoint(self, program: NcProgram, lineNumber: int) -> None:
        """
         Remove a breakpoint from a program line. 
        """
        pass
    def GetBreakpoints(self) -> List[Breakpoint]:
        """
         Get all breakpoints. 
         Returns breakpoints ( Breakpoint List[NX):  array of all breakpoints .
        """
        pass
    def GetExternalFileSource(self) -> NcProgramSource:
        """
         Get the source containing all added programs for external file simulation. 
         Returns source ( NcProgramSource NXOp):  source containing all added programs for external file simulation .
        """
        pass
    def GetPostprocessorSource(self) -> NcProgramSource:
        """
         Get the source containing all added programs from postprocessor. 
         Returns source ( NcProgramSource NXOp):  source containing all added programs from postprocessor .
        """
        pass
    def GetSetupSource(self) -> NcProgramSource:
        """
         Get the source containing all added programs from the CAM Setup location. 
         Returns source ( NcProgramSource NXOp):  source containing all added programs from the CAM Setup location .
        """
        pass
import NXOpen
class NcProgramSource(NXOpen.TaggedObject): 
    """  Represents the NcProgramSource class object   """
    def AddMainProgram(self, channel: str, file: str) -> NcProgram:
        """
         Add a Main program to this source.
                    This is only allowed on the External File Source.
                    This can be requested with SIM.NcProgramManagerBuilder.GetExternalFileSource. 
         Returns program ( NcProgram NXOp):  The added program. .
        """
        pass
    def AddSubprogram(self, file: str) -> NcProgram:
        """
         Add a Subprogram to this source. 
         Returns program ( NcProgram NXOp):  The added program. .
        """
        pass
    def CreateMainProgram(self, channel: str, fileName: str) -> NcProgram:
        """
         Create an empty Main program in this source.
                    This is only allowed on the External File Source.
                    This can be requested with SIM.NcProgramManagerBuilder.GetExternalFileSource. 
         Returns program ( NcProgram NXOp):  The created program. .
        """
        pass
    def DeleteProgram(self, program: NcProgram) -> bool:
        """
         Delete a program in this source. 
         Returns success (bool): .
        """
        pass
    def GetMainProgram(self, channel: str) -> NcProgram:
        """
         Get main program for channel. 
         Returns program ( NcProgram NXOp):  The returned main program. .
        """
        pass
    def GetSubprogram(self, programId: str) -> NcProgram:
        """
         Get subprogram with a given ID. 
         Returns program ( NcProgram NXOp):  The returned subprogram. .
        """
        pass
import NXOpen
class NcProgram(NXOpen.NXObject): 
    """  Represents the NcProgram class object   """
    def Export(self, file: str) -> None:
        """
         Export program to file. 
        """
        pass
    def GetLine(self, line: int) -> str:
        """
         Get the line content of a specific line number. 
         Returns lineContent (str):  The content of the specific line .
        """
        pass
    def InsertBreakpoint(self, line: int) -> Breakpoint:
        """
         Add a breakpoint. 
         Returns breakpoint ( Breakpoint NXOp): .
        """
        pass
import NXOpen
class SaveSnapshotBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.SIM.SaveSnapshotBuilder
    """
    def SetSetupName(self, name: str) -> None:
        """
         Sets the source component name 
        """
        pass
    def SetSnapshotName(self, name: str) -> None:
        """
         Sets the snapshot name 
        """
        pass
import NXOpen
class SimDebugBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.SIM.SimDebugBuilder
    """
    class DriverType(Enum):
        """
        Members Include: 
         |Cse|  CSE driver 
         |Mtd|  MTD driver 

        """
        Cse: int
        Mtd: int
        @staticmethod
        def ValueOf(value: int) -> SimDebugBuilder.DriverType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class KinematicModelType(Enum):
        """
        Members Include: 
         |Main|  Main Kinematic Model
         |Simulation|  Simulation Kinematic Model
         |Driver|  Driver Kinematic Model

        """
        Main: int
        Simulation: int
        Driver: int
        @staticmethod
        def ValueOf(value: int) -> SimDebugBuilder.KinematicModelType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OutputType(Enum):
        """
        Members Include: 
         |Syslog|  Output to syslog 
         |ListingWindow|  Output to listing window 
         |Autotest|  Output to autotest 
         |ToFile|  Output to file 

        """
        Syslog: int
        ListingWindow: int
        Autotest: int
        ToFile: int
        @staticmethod
        def ValueOf(value: int) -> SimDebugBuilder.OutputType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PrintoutTagsOrPointersType(Enum):
        """
        Members Include: 
         |Boolean|  Boolean
         |Value|  Value
         |Name|  Name

        """
        Boolean: int
        Value: int
        Name: int
        @staticmethod
        def ValueOf(value: int) -> SimDebugBuilder.PrintoutTagsOrPointersType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TraceType(Enum):
        """
        Members Include: 
         |ButtonDown|  Trace Button Down 
         |Vcr|  Trace Vcr 
         |Ipw|  Trace Ipw 
         |Performance|  Trace Performance 
         |Collision|  Trace Collision 
         |Gouge|  Trace Gouge 
         |Highlighting|  Trace Highlighting 
         |Details|  Trace Details 
         |PositionalIsv|  Trace Positional Isv 
         |SpinningNonSpinning|  Trace Spinning Nonspinning 
         |KinematicModel|  Trace Kinematic Model 
         |Event|  Trace Event 
         |LineServer|  Trace Line Server 
         |Sync|  Trace Sync 
         |ToolPathPicking|  Trace ToolPath Picking
         |CseMotionData|  Trace Cse Motions
         |CseCallStack|  Trace Cse Programs
         |CseToolEvents|  Trace Cse Tool Events
         |CseCheckSyntax|  Trace Check Syntax
         |ProcessForce|  Trace Process Forces 
         |Findings|  Trace Findings 

        """
        ButtonDown: int
        Vcr: int
        Ipw: int
        Performance: int
        Collision: int
        Gouge: int
        Highlighting: int
        Details: int
        PositionalIsv: int
        SpinningNonSpinning: int
        KinematicModel: int
        Event: int
        LineServer: int
        Sync: int
        ToolPathPicking: int
        CseMotionData: int
        CseCallStack: int
        CseToolEvents: int
        CseCheckSyntax: int
        ProcessForce: int
        Findings: int
        @staticmethod
        def ValueOf(value: int) -> SimDebugBuilder.TraceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class UiType(Enum):
        """
        Members Include: 
         |DisplayMomEvent|  Display Mom Event 
         |ShowPartAndTipJunctions|  Show Part And Tip Junction 
         |GenerateSpinningTools|  Generate Spinning Tools 
         |UseHybridGougeChecker|  Use Hybrid Gouge Checker 
         |UseMtbOldDialogs|  Use MTB Old Dialogs 
         |UseFastTicker|  Use Fast Ticker 
         |PrintOutTraceSerialNumbers|  Print Out Trace Serial Numbers 
         |PerformanceDisplayDetail|  Performance Display Detail 
         |PerformanceDisplayTime|  Performance Display Time 
         |PerformanceIndentTime|  Performance Indent Time 
         |PerformanceDisplayData|  Performance Display Data 
         |DctkWriteCollisionPairs|  Write Collision Pairs 

        """
        DisplayMomEvent: int
        ShowPartAndTipJunctions: int
        GenerateSpinningTools: int
        UseHybridGougeChecker: int
        UseMtbOldDialogs: int
        UseFastTicker: int
        PrintOutTraceSerialNumbers: int
        PerformanceDisplayDetail: int
        PerformanceDisplayTime: int
        PerformanceIndentTime: int
        PerformanceDisplayData: int
        DctkWriteCollisionPairs: int
        @staticmethod
        def ValueOf(value: int) -> SimDebugBuilder.UiType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Driver(self) -> SimDebugBuilder.DriverType:
        """
        Getter for property: ( SimDebugBuilder.DriverType NXOp) Driver
         Returns the driver   
            
         
        """
        pass
    @Driver.setter
    def Driver(self, type: SimDebugBuilder.DriverType):
        """
        Setter for property: ( SimDebugBuilder.DriverType NXOp) Driver
         Returns the driver   
            
         
        """
        pass
    @property
    def DumpOutput(self) -> SimDebugBuilder.OutputType:
        """
        Getter for property: ( SimDebugBuilder.OutputType NXOp) DumpOutput
         Returns the dump output   
            
         
        """
        pass
    @DumpOutput.setter
    def DumpOutput(self, type: SimDebugBuilder.OutputType):
        """
        Setter for property: ( SimDebugBuilder.OutputType NXOp) DumpOutput
         Returns the dump output   
            
         
        """
        pass
    @property
    def DumpToFileName(self) -> str:
        """
        Getter for property: (str) DumpToFileName
         Returns the output filename   
            
         
        """
        pass
    @DumpToFileName.setter
    def DumpToFileName(self, name: str):
        """
        Setter for property: (str) DumpToFileName
         Returns the output filename   
            
         
        """
        pass
    @property
    def PrintoutTags(self) -> SimDebugBuilder.PrintoutTagsOrPointersType:
        """
        Getter for property: ( SimDebugBuilder.PrintoutTagsOrPointersType NXOp) PrintoutTags
         Returns the printout tags type   
            
         
        """
        pass
    @PrintoutTags.setter
    def PrintoutTags(self, type: SimDebugBuilder.PrintoutTagsOrPointersType):
        """
        Setter for property: ( SimDebugBuilder.PrintoutTagsOrPointersType NXOp) PrintoutTags
         Returns the printout tags type   
            
         
        """
        pass
    def GetTrace(self, type: SimDebugBuilder.TraceType) -> bool:
        """
         Gets the trace 
         Returns state (bool):  The state.
        """
        pass
    def GetUiSetting(self, type: SimDebugBuilder.UiType) -> bool:
        """
         Gets the debug setting 
         Returns state (bool):  The state.
        """
        pass
    def SetTrace(self, type: SimDebugBuilder.TraceType, state: bool) -> None:
        """
        Sets the trace 
        """
        pass
    def SetUiSetting(self, type: SimDebugBuilder.UiType, state: bool) -> None:
        """
         Sets the debug setting 
        """
        pass
import NXOpen
class SinumerikCaExportBuilder(NXOpen.Builder): 
    """ This class is used for export a spf file.
        A call to SinumerikCaExportBuilder.ExportSpf  is used to export a spf file.
        Calling Builder.Commit on this builder will only return .
    """
    @property
    def ChainElementIndex(self) -> int:
        """
        Getter for property: (int) ChainElementIndex
         Returns the index used by chain elements when exporting the SPF file   
            
         
        """
        pass
    @ChainElementIndex.setter
    def ChainElementIndex(self, index: int):
        """
        Setter for property: (int) ChainElementIndex
         Returns the index used by chain elements when exporting the SPF file   
            
         
        """
        pass
    @property
    def CollisionPairIndex(self) -> int:
        """
        Getter for property: (int) CollisionPairIndex
         Returns the index used when exporting collision pairs to the SPF file   
            
         
        """
        pass
    @CollisionPairIndex.setter
    def CollisionPairIndex(self, index: int):
        """
        Setter for property: (int) CollisionPairIndex
         Returns the index used when exporting collision pairs to the SPF file   
            
         
        """
        pass
    @property
    def DeleteChainsAtStart(self) -> bool:
        """
        Getter for property: (bool) DeleteChainsAtStart
         Returns the flag which determines if chains are deleted at the beginning of the export   
            
         
        """
        pass
    @DeleteChainsAtStart.setter
    def DeleteChainsAtStart(self, deleteChainsAtStart: bool):
        """
        Setter for property: (bool) DeleteChainsAtStart
         Returns the flag which determines if chains are deleted at the beginning of the export   
            
         
        """
        pass
    @property
    def FileName(self) -> str:
        """
        Getter for property: (str) FileName
         Returns the output filename of the SPF file   
            
         
        """
        pass
    @FileName.setter
    def FileName(self, name: str):
        """
        Setter for property: (str) FileName
         Returns the output filename of the SPF file   
            
         
        """
        pass
    @property
    def ListOutput(self) -> bool:
        """
        Getter for property: (bool) ListOutput
         Returns the flag which determines if the output is printed to a listing window   
            
         
        """
        pass
    @ListOutput.setter
    def ListOutput(self, output: bool):
        """
        Setter for property: (bool) ListOutput
         Returns the flag which determines if the output is printed to a listing window   
            
         
        """
        pass
    @property
    def ProtectionAreaElementIndex(self) -> int:
        """
        Getter for property: (int) ProtectionAreaElementIndex
         Returns the index used when exporting protection area elements to the SPF file   
            
         
        """
        pass
    @ProtectionAreaElementIndex.setter
    def ProtectionAreaElementIndex(self, index: int):
        """
        Setter for property: (int) ProtectionAreaElementIndex
         Returns the index used when exporting protection area elements to the SPF file   
            
         
        """
        pass
    @property
    def ProtectionAreaIndex(self) -> int:
        """
        Getter for property: (int) ProtectionAreaIndex
         Returns the index used when exporting protection areas to the SPF file   
            
         
        """
        pass
    @ProtectionAreaIndex.setter
    def ProtectionAreaIndex(self, index: int):
        """
        Setter for property: (int) ProtectionAreaIndex
         Returns the index used when exporting protection areas to the SPF file   
            
         
        """
        pass
    def ExportSpf(self, targetNode: str) -> None:
        """
         Export to Sinumerik Spf file 
        """
        pass
import NXOpen
class SinumerikCaFacetBuilder(NXOpen.Builder): 
    """ This class is used for set the facet tolerance.
        A call to Builder.Commit on this builder will only return .
    """
    @property
    def FacetTolerance(self) -> float:
        """
        Getter for property: (float) FacetTolerance
         Returns the facet tolerance   
            
         
        """
        pass
    @FacetTolerance.setter
    def FacetTolerance(self, tolerance: float):
        """
        Setter for property: (float) FacetTolerance
         Returns the facet tolerance   
            
         
        """
        pass
import NXOpen
class SinumerikCaPlaceholderBuilder(NXOpen.Builder): 
    """ This class is used for select or unselect component of the placeholder tools.
        A call to Builder.Commit on this builder will only return .
    """
    def SelectComponent(self, compName: str) -> None:
        """
         The select placeholder tools component 
        """
        pass
    def UnselectComponent(self, compName: str) -> None:
        """
         The select placeholder tools component 
        """
        pass
import NXOpen
class SinumerikCaSimplifyBodiesBuilder(NXOpen.Builder): 
    """ This class is used for replace geometry.
        A call to SinumerikCaSimplifyBodiesBuilder.DoReplace will replace the geometry.
        Calling Builder.Commit on this builder will only return .
    """
    class CloseGapTypes(Enum):
        """
        Members Include: 
         |Sharp|  Sharp 
         |Beveled|  Beveled 
         |NoOffset|  No Offset 

        """
        Sharp: int
        Beveled: int
        NoOffset: int
        @staticmethod
        def ValueOf(value: int) -> SinumerikCaSimplifyBodiesBuilder.CloseGapTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ObjectToReplaceWithTypes(Enum):
        """
        Members Include: 
         |Nothing|  Nothing 
         |ConvexHull|  Convex Hull 
         |BoundingSphere|  Bounding Sphere 
         |BoundingBlock|  Bounding Block 
         |BoundingCylinder|  Bounding Cylinder 
         |InscribedCylinder|  Inscribed Cylinder 

        """
        Nothing: int
        ConvexHull: int
        BoundingSphere: int
        BoundingBlock: int
        BoundingCylinder: int
        InscribedCylinder: int
        @staticmethod
        def ValueOf(value: int) -> SinumerikCaSimplifyBodiesBuilder.ObjectToReplaceWithTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AddOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) AddOffset
         Returns the  Additional offset.  
           Will expand the wrap.   
         
        """
        pass
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns  the Remove parms switch   
            
         
        """
        pass
    @Associative.setter
    def Associative(self, associative: bool):
        """
        Setter for property: (bool) Associative
         Returns  the Remove parms switch   
            
         
        """
        pass
    @property
    def CloseGaps(self) -> SinumerikCaSimplifyBodiesBuilder.CloseGapTypes:
        """
        Getter for property: ( SinumerikCaSimplifyBodiesBuilder.CloseGapTypes NXOp) CloseGaps
         Returns the  Method used to close the gaps after offset of the wrap   
            
         
        """
        pass
    @CloseGaps.setter
    def CloseGaps(self, closeGaps: SinumerikCaSimplifyBodiesBuilder.CloseGapTypes):
        """
        Setter for property: ( SinumerikCaSimplifyBodiesBuilder.CloseGapTypes NXOp) CloseGaps
         Returns the  Method used to close the gaps after offset of the wrap   
            
         
        """
        pass
    @property
    def CoordSystem(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) CoordSystem
         Returns the coordinate system   
            
         
        """
        pass
    @CoordSystem.setter
    def CoordSystem(self, coordSystem: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) CoordSystem
         Returns the coordinate system   
            
         
        """
        pass
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the Distance tolerance used to facet the solids.  
           Also used for default offset calculation.   
         
        """
        pass
    @DistanceTolerance.setter
    def DistanceTolerance(self, distTol: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the Distance tolerance used to facet the solids.  
           Also used for default offset calculation.   
         
        """
        pass
    @property
    def ObjectToReplace(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) ObjectToReplace
         Returns the object to replace   
            
         
        """
        pass
    @property
    def PlanesList(self) -> NXOpen.PlaneList:
        """
        Getter for property: ( NXOpen.PlaneList) PlanesList
         Returns the Planes to split the geometry, tightens the wrap along this plane   
            
         
        """
        pass
    @property
    def ReplaceWith(self) -> SinumerikCaSimplifyBodiesBuilder.ObjectToReplaceWithTypes:
        """
        Getter for property: ( SinumerikCaSimplifyBodiesBuilder.ObjectToReplaceWithTypes NXOp) ReplaceWith
         Returns the object to replace with   
            
         
        """
        pass
    @ReplaceWith.setter
    def ReplaceWith(self, objectToReplaceWith: SinumerikCaSimplifyBodiesBuilder.ObjectToReplaceWithTypes):
        """
        Setter for property: ( SinumerikCaSimplifyBodiesBuilder.ObjectToReplaceWithTypes NXOp) ReplaceWith
         Returns the object to replace with   
            
         
        """
        pass
    @property
    def SplitOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SplitOffset
         Returns the Offset applied to both sides of the splitting planes.  
             
         
        """
        pass
    def DoReplace(self) -> None:
        """
         Replace the simplify bodies 
        """
        pass
import NXOpen
class SmkDebugBuilder(NXOpen.Builder): 
    """
    Represents a SIM.SmkDebugBuilder
    """
    class DumpType(Enum):
        """
        Members Include: 
         |NotSet| 
         |MachineKit| 

        """
        NotSet: int
        MachineKit: int
        @staticmethod
        def ValueOf(value: int) -> SmkDebugBuilder.DumpType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OutputType(Enum):
        """
        Members Include: 
         |Syslog|  Output to syslog 
         |ListingWindow|  Output to listing window 
         |Autotest|  Output to autotest 
         |ToFile|  Output to file 

        """
        Syslog: int
        ListingWindow: int
        Autotest: int
        ToFile: int
        @staticmethod
        def ValueOf(value: int) -> SmkDebugBuilder.OutputType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def OutputFile(self) -> str:
        """
        Getter for property: (str) OutputFile
         Returns the output file   
            
         
        """
        pass
    @OutputFile.setter
    def OutputFile(self, outputFile: str):
        """
        Setter for property: (str) OutputFile
         Returns the output file   
            
         
        """
        pass
    @property
    def PartFolder(self) -> str:
        """
        Getter for property: (str) PartFolder
         Returns the part folder   
            
         
        """
        pass
    @PartFolder.setter
    def PartFolder(self, partFolder: str):
        """
        Setter for property: (str) PartFolder
         Returns the part folder   
            
         
        """
        pass
    def ExportGeometryInformation(self, partFolder: str, outputFile: str) -> None:
        """
         Export geometry information 
        """
        pass
import NXOpen
class SmkLicenseCensorBuilder(NXOpen.Builder): 
    """  Represents the SmkLicenseCensorBuilder class object   """
    pass
import NXOpen
class SmkMachineKitEditorBuilder(NXOpen.Builder): 
    """  Represents the SmkMachineKitEditorBuilder class object   """
    class DataClassification(Enum):
        """
        Members Include: 
         |General| 
         |Post| 
         |Sim| 
         |PostAndSim| 
         |Nc| 

        """
        General: int
        Post: int
        Sim: int
        PostAndSim: int
        Nc: int
        @staticmethod
        def ValueOf(value: int) -> SmkMachineKitEditorBuilder.DataClassification:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DataType(Enum):
        """
        Members Include: 
         |String| 
         |Int| 
         |Double| 
         |Enum| 
         |MultiString| 

        """
        String: int
        Int: int
        Double: int
        Enum: int
        MultiString: int
        @staticmethod
        def ValueOf(value: int) -> SmkMachineKitEditorBuilder.DataType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ParametersMachineMode(Enum):
        """
        Members Include: 
         |All| 
         |Mill| 
         |Lathe| 
         |Drill| 
         |Wedm| 
         |Laser| 

        """
        All: int
        Mill: int
        Lathe: int
        Drill: int
        Wedm: int
        Laser: int
        @staticmethod
        def ValueOf(value: int) -> SmkMachineKitEditorBuilder.ParametersMachineMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def AddAttribute(self, attributeFullname: str) -> None:
        """
         Adds a new attribute item 
        """
        pass
    def AddParametersMachineMode(self, attributeFullname: str, machineMode: SmkMachineKitEditorBuilder.ParametersMachineMode) -> None:
        """
         Adds parameters machine mode 
        """
        pass
    def ClearParametersMachineMode(self, attributeFullname: str) -> None:
        """
         Clears parameters machine mode 
        """
        pass
    def DeleteAttribute(self, attributeFullname: str) -> None:
        """
         Deletes the attribute item 
        """
        pass
    def GetAttributeClassification(self, attributeFullname: str) -> SmkMachineKitEditorBuilder.DataClassification:
        """
         Gets  
         Returns classification ( SmkMachineKitEditorBuilder.DataClassification NXOp):  The attribute classification .
        """
        pass
    def GetAttributeType(self, attributeFullname: str) -> SmkMachineKitEditorBuilder.DataType:
        """
         Gets  
         Returns type ( SmkMachineKitEditorBuilder.DataType NXOp):  The attribute type .
        """
        pass
    def GetAttributeVariableName(self, attributeFullname: str) -> str:
        """
         Gets  
         Returns variableName (str):  The attribute variable name .
        """
        pass
    def GetDoubleAttribute(self, attributeFullname: str) -> float:
        """
         Gets  
         Returns value (float):  The attribute value .
        """
        pass
    def GetEnumAttribute(self, attributeFullname: str) -> Tuple[str, List[str]]:
        """
         Gets  
         Returns A tuple consisting of (currentValue, values). 
         - currentValue is: str. The attribute value    .
         - values is: List[str]. options for enum       .

        """
        pass
    def GetEventClassification(self, attributeFullname: str) -> int:
        """
         Gets the event classification  
         Returns eventClassification (int):  The event classification .
        """
        pass
    def GetIntegerAttribute(self, attributeFullname: str) -> int:
        """
         Gets  
         Returns value (int):  The attribute value .
        """
        pass
    def GetMachineMode(self, attributeFullname: str) -> int:
        """
         Gets the machine mode 
         Returns machineMode (int):  The machine mode .
        """
        pass
    def GetMultiStringAttribute(self, attributeFullname: str) -> List[str]:
        """
         Gets  
         Returns value (List[str]):  The attribute value    .
        """
        pass
    def GetStringAttribute(self, attributeFullname: str) -> str:
        """
         Gets  
         Returns value (str):  The attribute value .
        """
        pass
    def HasAttribute(self, attributeFullname: str) -> bool:
        """
         Asks if the attribute exists 
         Returns exists (bool):  The attribute exsitence .
        """
        pass
    def SetAttributeClassification(self, attributeFullname: str, classification: SmkMachineKitEditorBuilder.DataClassification) -> None:
        """
         Sets the attribute classification 
        """
        pass
    def SetAttributeName(self, attributeFullname: str, newName: str) -> None:
        """
         Sets the attribute name 
        """
        pass
    def SetAttributeType(self, attributeFullname: str, type: SmkMachineKitEditorBuilder.DataType) -> None:
        """
         Sets the attribute type 
        """
        pass
    def SetAttributeVariableName(self, attributeFullname: str, variableName: str) -> None:
        """
         Sets the variable name 
        """
        pass
    def SetDoubleAttribute(self, attributeFullname: str, value: float) -> None:
        """
         Sets the double attribute value 
        """
        pass
    def SetEnumAttribute(self, attributeFullname: str, value: str) -> None:
        """
         Sets the double attribute value 
        """
        pass
    def SetEventClassification(self, attributeFullname: str, eventClassification: int) -> None:
        """
         Sets the event classification 
        """
        pass
    def SetIntegerAttribute(self, attributeFullname: str, value: int) -> None:
        """
         Sets the double attribute value 
        """
        pass
    def SetMachineMode(self, attributeFullname: str, machineMode: int) -> None:
        """
         Sets the machine mode 
        """
        pass
    def SetMultiStringAttribute(self, attributeFullname: str, values: List[str]) -> None:
        """
         Sets the multi string attribute values 
        """
        pass
    def SetStringAttribute(self, attributeFullname: str, value: str) -> None:
        """
         Sets the string attribute value 
        """
        pass
import NXOpen
class SmkTransitionPathEditorBuilder(NXOpen.Builder): 
    """  Represents the SmkTransitionPathEditorBuilder class object   """
    class TemplateLocation(Enum):
        """
        Members Include: 
         |FromKinematic| 
         |FromOtherPart| 

        """
        FromKinematic: int
        FromOtherPart: int
        @staticmethod
        def ValueOf(value: int) -> SmkTransitionPathEditorBuilder.TemplateLocation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TemplateType(Enum):
        """
        Members Include: 
         |Before| 
         |Between| 
         |After| 
         |BetweenNCM| 

        """
        Before: int
        Between: int
        After: int
        BetweenNCM: int
        @staticmethod
        def ValueOf(value: int) -> SmkTransitionPathEditorBuilder.TemplateType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetTemplateFilePath(self) -> str:
        """
         Gets the template file path 
         Returns filePath (str):  The template file path .
        """
        pass
    def GetTemplateLocation(self) -> SmkTransitionPathEditorBuilder.TemplateLocation:
        """
         Gets the template location 
         Returns templateLocation ( SmkTransitionPathEditorBuilder.TemplateLocation NXOp):  The template location .
        """
        pass
    def GetTemplateType(self) -> SmkTransitionPathEditorBuilder.TemplateType:
        """
         Gets the template type 
         Returns templateType ( SmkTransitionPathEditorBuilder.TemplateType NXOp):  The template type .
        """
        pass
    def ImportDefaultTemplate(self) -> None:
        """
         Import from default template 
        """
        pass
    def ImportFromOtherMachine(self, filePath: str) -> None:
        """
         Import from other machine 
        """
        pass
    def SetTemplateFilePath(self, filePath: str) -> None:
        """
         Sets the template file path 
        """
        pass
    def SetTemplateLocation(self, templateLocation: SmkTransitionPathEditorBuilder.TemplateLocation) -> None:
        """
         Sets the template location 
        """
        pass
    def SetTemplateType(self, templateType: SmkTransitionPathEditorBuilder.TemplateType) -> None:
        """
         Sets the template type 
        """
        pass
import NXOpen
import NXOpen.SIM.PostConfigurator
class SmkWizardBuilder(NXOpen.Builder): 
    """  Represents the SimSmkWizardBuilder class object   """
    class ArchieveFileType(Enum):
        """
        Members Include: 
         |NotSet|  no archieve file 
         |Specify|  user archieve file 

        """
        NotSet: int
        Specify: int
        @staticmethod
        def ValueOf(value: int) -> SmkWizardBuilder.ArchieveFileType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class AxisDirectionType(Enum):
        """
        Members Include: 
         |PositiveX|  positive X-axis 
         |NegativeX|  negative X-axis 
         |PositiveY|  positive Y-axis 
         |NegativeY|  negative Y-axis 
         |PositiveZ|  positive Z-axis 
         |NegativeZ|  negative Z-axis 

        """
        PositiveX: int
        NegativeX: int
        PositiveY: int
        NegativeY: int
        PositiveZ: int
        NegativeZ: int
        @staticmethod
        def ValueOf(value: int) -> SmkWizardBuilder.AxisDirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class AxisMotionType(Enum):
        """
        Members Include: 
         |Linear|  linear axis    
         |Rotary|  rotary axis    
         |RotaryUnlimited| rotary axis unlimited
         |Spindle|  spindle    

        """
        Linear: int
        Rotary: int
        RotaryUnlimited: int
        Spindle: int
        @staticmethod
        def ValueOf(value: int) -> SmkWizardBuilder.AxisMotionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ComponentClassificationType(Enum):
        """
        Members Include: 
         |Turret| 
         |Pocket| 
         |PocketOnHead| 
         |Part| 
         |Workpiece| 
         |AdditiveMaterial| 
         |SetupElement| 
         |LatheSpindle| 
         |ToolCutting| 
         |ToolNonCutting| 
         |Head| 
         |ToolTurret| 
         |Magazine| 
         |ToolSpindle| 
         |LocationPocket| 
         |AssignablePocket| 
         |WorkHolder| 
         |ToolHolder| 
         |Setup| 

        """
        Turret: int
        Pocket: int
        PocketOnHead: int
        Part: int
        Workpiece: int
        AdditiveMaterial: int
        SetupElement: int
        LatheSpindle: int
        ToolCutting: int
        ToolNonCutting: int
        Head: int
        ToolTurret: int
        Magazine: int
        ToolSpindle: int
        LocationPocket: int
        AssignablePocket: int
        WorkHolder: int
        ToolHolder: int
        Setup: int
        @staticmethod
        def ValueOf(value: int) -> SmkWizardBuilder.ComponentClassificationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CoordinateReferenceType(Enum):
        """
        Members Include: 
         |Absolute| 
         |MachineZero| 

        """
        Absolute: int
        MachineZero: int
        @staticmethod
        def ValueOf(value: int) -> SmkWizardBuilder.CoordinateReferenceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DeviceTemplateType(Enum):
        """
        Members Include: 
         |NotSet|  no special device   
         |Specify|  user defined device 

        """
        NotSet: int
        Specify: int
        @staticmethod
        def ValueOf(value: int) -> SmkWizardBuilder.DeviceTemplateType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class JunctionClassificationType(Enum):
        """
        Members Include: 
         |NotSet|  no specal class 
         |ToolMount|  a mounting junction 
         |MachineZero|  the machine zero junction 
         |LatheWpZx|  Lathe Work Plane ZX 
         |LatheWpXy|  Lathe Work Plane XY 
         |HeadMount|  head mount junction 

        """
        NotSet: int
        ToolMount: int
        MachineZero: int
        LatheWpZx: int
        LatheWpXy: int
        HeadMount: int
        @staticmethod
        def ValueOf(value: int) -> SmkWizardBuilder.JunctionClassificationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class KinematicsVersionType(Enum):
        """
        Members Include: 
         |Classic|  Classic kinematics model 
         |Mpp|  Machine Powered Programming kinematics model 

        """
        Classic: int
        Mpp: int
        @staticmethod
        def ValueOf(value: int) -> SmkWizardBuilder.KinematicsVersionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MachineType(Enum):
        """
        Members Include: 
         |Mill| 
         |Turnmill| 
         |Lathe| 
         |Millturn| 
         |Wedm| 
         |Robot| 
         |Generic| 

        """
        Mill: int
        Turnmill: int
        Lathe: int
        Millturn: int
        Wedm: int
        Robot: int
        Generic: int
        @staticmethod
        def ValueOf(value: int) -> SmkWizardBuilder.MachineType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OutputType(Enum):
        """
        Members Include: 
         |InstalledMachines|  current installed machines folder 
         |Mtk|  mtk file 

        """
        InstalledMachines: int
        Mtk: int
        @staticmethod
        def ValueOf(value: int) -> SmkWizardBuilder.OutputType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PocketTransformType(Enum):
        """
        Members Include: 
         |TranslateDelta| 
         |TranslateToPoint| 
         |RotateTwoPoint| 
         |RotatePointVector| 

        """
        TranslateDelta: int
        TranslateToPoint: int
        RotateTwoPoint: int
        RotatePointVector: int
        @staticmethod
        def ValueOf(value: int) -> SmkWizardBuilder.PocketTransformType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RegisterType(Enum):
        """
        Members Include: 
         |SameAsHolderId| 
         |SameAsParent| 
         |Specify| 

        """
        SameAsHolderId: int
        SameAsParent: int
        Specify: int
        @staticmethod
        def ValueOf(value: int) -> SmkWizardBuilder.RegisterType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class WizardStep(Enum):
        """
        Members Include: 
         |TemplateSelection| 
         |GeometrySelection| 
         |JunctionSelection| 
         |AxisDefinition| 
         |ChainConfiguration| 
         |ChannelConfiguration| 
         |MachineToolDataDefinition| 
         |CsePostSelection| 
         |OutputSelection| 

        """
        TemplateSelection: int
        GeometrySelection: int
        JunctionSelection: int
        AxisDefinition: int
        ChainConfiguration: int
        ChannelConfiguration: int
        MachineToolDataDefinition: int
        CsePostSelection: int
        OutputSelection: int
        @staticmethod
        def ValueOf(value: int) -> SmkWizardBuilder.WizardStep:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ArchieveFile(self) -> SmkWizardBuilder.ArchieveFileType:
        """
        Getter for property: ( SmkWizardBuilder.ArchieveFileType NXOp) ArchieveFile
         Returns the machine archive template enum   
            
         
        """
        pass
    @ArchieveFile.setter
    def ArchieveFile(self, archieveFileEnum: SmkWizardBuilder.ArchieveFileType):
        """
        Setter for property: ( SmkWizardBuilder.ArchieveFileType NXOp) ArchieveFile
         Returns the machine archive template enum   
            
         
        """
        pass
    @property
    def ArchieveMachineFilePath(self) -> str:
        """
        Getter for property: (str) ArchieveMachineFilePath
         Returns the smart machine Machine file path   
            
         
        """
        pass
    @ArchieveMachineFilePath.setter
    def ArchieveMachineFilePath(self, archieveMachineFilePath: str):
        """
        Setter for property: (str) ArchieveMachineFilePath
         Returns the smart machine Machine file path   
            
         
        """
        pass
    @property
    def ArchieveTemplateFilePath(self) -> str:
        """
        Getter for property: (str) ArchieveTemplateFilePath
         Returns the smart machine template file path   
            
         
        """
        pass
    @ArchieveTemplateFilePath.setter
    def ArchieveTemplateFilePath(self, archieveTemplateFilePath: str):
        """
        Setter for property: (str) ArchieveTemplateFilePath
         Returns the smart machine template file path   
            
         
        """
        pass
    @property
    def CreateCseDriver(self) -> bool:
        """
        Getter for property: (bool) CreateCseDriver
         Returns the flag defines whether to create a CSE driver.  
              
         
        """
        pass
    @CreateCseDriver.setter
    def CreateCseDriver(self, flagCreateCseDriver: bool):
        """
        Setter for property: (bool) CreateCseDriver
         Returns the flag defines whether to create a CSE driver.  
              
         
        """
        pass
    @property
    def CreateKitType(self) -> SmkWizardBuilder.OutputType:
        """
        Getter for property: ( SmkWizardBuilder.OutputType NXOp) CreateKitType
         Returns the type of creating a machine kit.  
              
         
        """
        pass
    @CreateKitType.setter
    def CreateKitType(self, kitType: SmkWizardBuilder.OutputType):
        """
        Setter for property: ( SmkWizardBuilder.OutputType NXOp) CreateKitType
         Returns the type of creating a machine kit.  
              
         
        """
        pass
    @property
    def CreatePostprocessor(self) -> bool:
        """
        Getter for property: (bool) CreatePostprocessor
         Returns the flag defines whether to create a postprocessor.  
              
         
        """
        pass
    @CreatePostprocessor.setter
    def CreatePostprocessor(self, flagCreatePostprocessor: bool):
        """
        Setter for property: (bool) CreatePostprocessor
         Returns the flag defines whether to create a postprocessor.  
              
         
        """
        pass
    @property
    def CreationPostBuilder(self) -> NXOpen.SIM.PostConfigurator.CreationPostBuilder:
        """
        Getter for property: ( NXOpen.SIM.PostConfigurator.CreationPostBuilder) CreationPostBuilder
         Returns the creation post builder   
            
         
        """
        pass
    @CreationPostBuilder.setter
    def CreationPostBuilder(self, creationPostBuilder: NXOpen.SIM.PostConfigurator.CreationPostBuilder):
        """
        Setter for property: ( NXOpen.SIM.PostConfigurator.CreationPostBuilder) CreationPostBuilder
         Returns the creation post builder   
            
         
        """
        pass
    @property
    def CseDriverTemplateFile(self) -> str:
        """
        Getter for property: (str) CseDriverTemplateFile
         Returns the file directory of cse driver template.  
              
         
        """
        pass
    @CseDriverTemplateFile.setter
    def CseDriverTemplateFile(self, file: str):
        """
        Setter for property: (str) CseDriverTemplateFile
         Returns the file directory of cse driver template.  
              
         
        """
        pass
    @property
    def CseDriverTemplateName(self) -> str:
        """
        Getter for property: (str) CseDriverTemplateName
         Returns the cse driver template name.  
              
         
        """
        pass
    @CseDriverTemplateName.setter
    def CseDriverTemplateName(self, name: str):
        """
        Setter for property: (str) CseDriverTemplateName
         Returns the cse driver template name.  
              
         
        """
        pass
    @property
    def DeviceTemplate(self) -> SmkWizardBuilder.DeviceTemplateType:
        """
        Getter for property: ( SmkWizardBuilder.DeviceTemplateType NXOp) DeviceTemplate
         Returns the device template   
            
         
        """
        pass
    @DeviceTemplate.setter
    def DeviceTemplate(self, deviceTemplateType: SmkWizardBuilder.DeviceTemplateType):
        """
        Setter for property: ( SmkWizardBuilder.DeviceTemplateType NXOp) DeviceTemplate
         Returns the device template   
            
         
        """
        pass
    @property
    def DeviceTemplateFilePath(self) -> str:
        """
        Getter for property: (str) DeviceTemplateFilePath
         Returns the device template file path   
            
         
        """
        pass
    @DeviceTemplateFilePath.setter
    def DeviceTemplateFilePath(self, filePath: str):
        """
        Setter for property: (str) DeviceTemplateFilePath
         Returns the device template file path   
            
         
        """
        pass
    @property
    def JunctionCoordinateReferenceType(self) -> SmkWizardBuilder.CoordinateReferenceType:
        """
        Getter for property: ( SmkWizardBuilder.CoordinateReferenceType NXOp) JunctionCoordinateReferenceType
         Returns the type of coordinate reference.  
              
         
        """
        pass
    @JunctionCoordinateReferenceType.setter
    def JunctionCoordinateReferenceType(self, refType: SmkWizardBuilder.CoordinateReferenceType):
        """
        Setter for property: ( SmkWizardBuilder.CoordinateReferenceType NXOp) JunctionCoordinateReferenceType
         Returns the type of coordinate reference.  
              
         
        """
        pass
    @property
    def MachineKitDesc(self) -> str:
        """
        Getter for property: (str) MachineKitDesc
         Returns the machine kit Description.  
              
         
        """
        pass
    @MachineKitDesc.setter
    def MachineKitDesc(self, desc: str):
        """
        Setter for property: (str) MachineKitDesc
         Returns the machine kit Description.  
              
         
        """
        pass
    @property
    def MachineKitEditorBuilder(self) -> SmkMachineKitEditorBuilder:
        """
        Getter for property: ( SmkMachineKitEditorBuilder NXOp) MachineKitEditorBuilder
         Returns the machine kit editor builder   
            
         
        """
        pass
    @MachineKitEditorBuilder.setter
    def MachineKitEditorBuilder(self, machineKitEditorBuilder: SmkMachineKitEditorBuilder):
        """
        Setter for property: ( SmkMachineKitEditorBuilder NXOp) MachineKitEditorBuilder
         Returns the machine kit editor builder   
            
         
        """
        pass
    @property
    def MachineKitName(self) -> str:
        """
        Getter for property: (str) MachineKitName
         Returns the machine kit name.  
              
         
        """
        pass
    @MachineKitName.setter
    def MachineKitName(self, name: str):
        """
        Setter for property: (str) MachineKitName
         Returns the machine kit name.  
              
         
        """
        pass
    @property
    def MachineKitType(self) -> SmkWizardBuilder.MachineType:
        """
        Getter for property: ( SmkWizardBuilder.MachineType NXOp) MachineKitType
         Returns the type of machine.  
              
         
        """
        pass
    @MachineKitType.setter
    def MachineKitType(self, machineType: SmkWizardBuilder.MachineType):
        """
        Setter for property: ( SmkWizardBuilder.MachineType NXOp) MachineKitType
         Returns the type of machine.  
              
         
        """
        pass
    @property
    def MachineTemplate(self) -> str:
        """
        Getter for property: (str) MachineTemplate
         Returns the machine template name   
            
         
        """
        pass
    @MachineTemplate.setter
    def MachineTemplate(self, machineTemplateName: str):
        """
        Setter for property: (str) MachineTemplate
         Returns the machine template name   
            
         
        """
        pass
    @property
    def MachineTemplateFilePath(self) -> str:
        """
        Getter for property: (str) MachineTemplateFilePath
         Returns the machine template file path   
            
         
        """
        pass
    @MachineTemplateFilePath.setter
    def MachineTemplateFilePath(self, machineTemplateFilePath: str):
        """
        Setter for property: (str) MachineTemplateFilePath
         Returns the machine template file path   
            
         
        """
        pass
    @property
    def OutputDirectory(self) -> str:
        """
        Getter for property: (str) OutputDirectory
         Returns the output directory.  
              
         
        """
        pass
    @OutputDirectory.setter
    def OutputDirectory(self, directory: str):
        """
        Setter for property: (str) OutputDirectory
         Returns the output directory.  
              
         
        """
        pass
    @property
    def SmkKimChainConfigurationBuilder(self) -> KinematicChainConfiguration:
        """
        Getter for property: ( KinematicChainConfiguration NXOp) SmkKimChainConfigurationBuilder
         Returns the chain configuration builder   
            
         
        """
        pass
    @property
    def SmkKimChannelConfigurationBuilder(self) -> KinematicChannelConfigurationBuilder:
        """
        Getter for property: ( KinematicChannelConfigurationBuilder NXOp) SmkKimChannelConfigurationBuilder
         Returns the channel configuration builder   
            
         
        """
        pass
    def AddAxis(self, compName: str, axisName: str) -> None:
        """
         Add the junction 
        """
        pass
    def AddChain(self, chainName: str, chainAttributes: str) -> None:
        """
         Add the chain 
        """
        pass
    def AddComponent(self, parentCompName: str, componentName: str) -> None:
        """
         Add the component 
        """
        pass
    def AddComponentClassification(self, componentName: str, classificationType: SmkWizardBuilder.ComponentClassificationType) -> None:
        """
         Add Classification 
        """
        pass
    def AddDeviceComponent(self, devicePartPath: str, layer: int, transform: NXOpen.Matrix4x4) -> None:
        """
         Add device component 
        """
        pass
    def AddDevicePartOccurrence(self, devicePart: NXOpen.TaggedObject) -> None:
        """
         Add device component occurrence 
        """
        pass
    def AddDeviceTemplateFilePath(self, filePath: str) -> None:
        """
         Adds one device template file path 
        """
        pass
    def AddGeometry(self, componentName: str, geo: NXOpen.NXObject) -> None:
        """
         Adds a single geometry element 
        """
        pass
    def AddJunction(self, componentName: str, junctionName: str) -> None:
        """
         Add the junction 
        """
        pass
    def AskMachineBaseComponent(self) -> str:
        """
         Ask machine base component 
         Returns baseComponent (str): .
        """
        pass
    def ClearWizardData(self) -> None:
        """
         Clear the smk wizard data 
        """
        pass
    def CreateAutoChains(self) -> None:
        """
         Create chains automatically  
        """
        pass
    def CreateMachineKit(self) -> None:
        """
         Creates files of the machine kit.  
        """
        pass
    def CreatePocketTransformData(self, pocketName: str) -> None:
        """
         Create pocket transform data for pocket generator 
        """
        pass
    def CreateSmkKimChainBuilder(self) -> KinematicChain:
        """
         Create builder for chain configuration 
         Returns chainBuilder ( KinematicChain NXOp):  The new kinematic chain builder .
        """
        pass
    def CreateSmkKimChannelBuilder(self) -> KinematicChannelBuilder:
        """
         Create builder for channel configuration 
         Returns channelBuilder ( KinematicChannelBuilder NXOp):  The new kinematic channel builder .
        """
        pass
    def DeleteAllGeometries(self, componentName: str) -> None:
        """
         Deletes all geometry elements from the component 
        """
        pass
    def DeleteAxis(self, compName: str, axisName: str) -> None:
        """
         Delete the axis 
        """
        pass
    def DeleteChain(self, chainName: str) -> None:
        """
         Delete the chain 
        """
        pass
    def DeleteComponent(self, componentName: str) -> None:
        """
         Delete the component 
        """
        pass
    def DeleteDeviceTemplateFilePath(self, index: int, filePath: str) -> None:
        """
         Deletes one device template file path 
        """
        pass
    def DeleteGeometry(self, componentName: str, geo: NXOpen.NXObject) -> None:
        """
         Deletes a single geometry element from the component 
        """
        pass
    def DeleteJunction(self, jctFullName: str) -> None:
        """
         Delete the junction 
        """
        pass
    def GenerateTransformPockets(self, parentCompName: str, pocketName: str) -> None:
        """
         Generate transform pockets 
        """
        pass
    def GetAdjustRegister(self, componentName: str) -> int:
        """
         Get adjust register 
         Returns adjustReg (int):  The adjust regsiter .
        """
        pass
    def GetAxisCoarsePrecision(self, axisName: str) -> float:
        """
         Gets the axis coarse precision.
                    This defines the exact stop precision used to determine if a target point has been
                    reached, so that the next NC-block can be executed.  
         Returns value (float):  The coarse precission value .
        """
        pass
    def GetAxisDirection(self, axisName: str) -> SmkWizardBuilder.AxisDirectionType:
        """
         Get the axis direction 
         Returns axisDir ( SmkWizardBuilder.AxisDirectionType NXOp):  The axis direction .
        """
        pass
    def GetAxisDirectionVector(self, axisName: str) -> Tuple[float, float, float]:
        """
         Get the axis direction on absolute coordinate system  
         Returns A tuple consisting of (vectorX, vectorY, vectorZ). 
         - vectorX is: float. The x component of vector .
         - vectorY is: float. The y component of vector .
         - vectorZ is: float. The z component of vector .

        """
        pass
    def GetAxisFinePrecision(self, axisName: str) -> float:
        """
         Gets the axis fine precision.
                    This defines the exact stop precision used to determine if a target point has been
                    reached, so that the next NC-block can be executed.  
         Returns value (float):  The fine precission value .
        """
        pass
    def GetAxisInitialValue(self, axisName: str) -> float:
        """
         Gets the axis initial value 
         Returns initialValue (float):  The initial value .
        """
        pass
    def GetAxisJerkLimit(self, axisName: str) -> float:
        """
         Gets the axis jerk limit.
                    The jerk limit value limits jumps in acceleration. 
         Returns value (float):  The jerk limit value .
        """
        pass
    def GetAxisJumpVelocity(self, axisName: str) -> float:
        """
         Gets the axis jump velocity.
                    The jump velocity define a lag time at the beginning of the motion.  
         Returns value (float):  The jump velocity value .
        """
        pass
    def GetAxisJunctionName(self, axisName: str) -> str:
        """
         Gets the axis junction name 
         Returns junctionName (str):  The junction name .
        """
        pass
    def GetAxisKv(self, axisName: str) -> float:
        """
         Gets the axis kv.
                    the Kv-Factor is a parameter of the drives. It influences the dragging error
                    (difference between ideal motion profile and actual motion profile).  
         Returns value (float):  The kv value .
        """
        pass
    def GetAxisLowerLimit(self, axisName: str) -> float:
        """
         Gets the axis lower limit 
         Returns lowerValue (float):  The lower limit .
        """
        pass
    def GetAxisLowerSoftLimit(self, axisName: str) -> float:
        """
         Gets the axis lower soft limit.
                    The soft limit on the real machine is checked by the controller to avoid that the machine
                    travels into the mechanical stop (Hard Limit) with full speed (prevent damage). 
         Returns lowerSoftValue (float):  The lower soft limit .
        """
        pass
    def GetAxisMaximumAcceleration(self, axisName: str) -> float:
        """
         Gets the axis maximum acceleration.
                    The maximum acceleration defines how fast the axis can accelerate.
         Returns value (float):  The maximum acceleration value .
        """
        pass
    def GetAxisMaximumDeceleration(self, axisName: str) -> float:
        """
         Gets the axis maximum deceleration.
                    The maximum deceleration defines how fast the axis can decelerate. 
         Returns value (float):  The maximum deceleration value .
        """
        pass
    def GetAxisMaximumVelocity(self, axisName: str) -> float:
        """
         Gets the axis maximum velocity 
         Returns value (float):  The maximum velocity value .
        """
        pass
    def GetAxisMotion(self, axisName: str) -> Tuple[SmkWizardBuilder.AxisMotionType, bool]:
        """
         Get the axis motion 
         Returns A tuple consisting of (type, isNcAxis). 
         - type is:  SmkWizardBuilder.AxisMotionType NXOp. The axis motion  .
         - isNcAxis is: bool. The flag if axis is nc axis .

        """
        pass
    def GetAxisNumber(self, axisName: str) -> int:
        """
         Gets the axis number.
                The axis number is used in cases where an axis is programmed through a number
                instead of through an address (e.g. on Siemens 840D: AX1=10 instead of X10).
         Returns number (int):  The axis's number .
        """
        pass
    def GetAxisUpperLimit(self, axisName: str) -> float:
        """
         Gets the axis upper limit 
         Returns upperValue (float):  The upper limit .
        """
        pass
    def GetAxisUpperSoftLimit(self, axisName: str) -> float:
        """
         Gets the axis upper soft limit.
                    The soft limit on the real machine is checked by the controller to avoid that the machine
                    travels into the mechanical stop (Hard Limit) with full speed (prevent damage). 
         Returns upperSoftValue (float):  The upper soft limit .
        """
        pass
    def GetCapacity(self, componentName: str) -> int:
        """
         Get capacity 
         Returns capacity (int):  The capacity .
        """
        pass
    def GetChannelDevices(self, channelName: str) -> List[str]:
        """
         Get channel devices 
         Returns devices (List[str]):  The devices assigned to channel .
        """
        pass
    def GetCutcomRegister(self, componentName: str) -> int:
        """
         Get cutcom register 
         Returns cutcomReg (int):  The cutcom register .
        """
        pass
    def GetDeviceID(self, componentName: str) -> str:
        """
         Get device id 
         Returns deviceId (str):  The device id .
        """
        pass
    def GetDevicePartMountJunction(self, devicePartPath: str) -> NXOpen.TaggedObject:
        """
         Get device part mount junction 
         Returns mountTag ( NXOpen.TaggedObject): .
        """
        pass
    def GetGeometries(self, componentName: str) -> List[NXOpen.NXObject]:
        """
         Returns the geometry elements assigned to this component 
         Returns geos ( NXOpen.NXObject Li):  The geometry elements .
        """
        pass
    def GetHolderID(self, componentName: str) -> str:
        """
         Get holder id 
         Returns holderId (str):  The holder id .
        """
        pass
    def GetJunctionClassification(self, junctionName: str) -> SmkWizardBuilder.JunctionClassificationType:
        """
         Gets the classification of the junction 
         Returns jctClass ( SmkWizardBuilder.JunctionClassificationType NXOp):  The junction classification .
        """
        pass
    def GetJunctionMatrix(self, junctionName: str) -> NXOpen.Matrix3x3:
        """
         Gets the junction matrix 
         Returns matrix ( NXOpen.Matrix3x3):  The junction matrix .
        """
        pass
    def GetJunctionOrigin(self, junctionName: str) -> NXOpen.Point3d:
        """
         Gets the junction origin 
         Returns origin ( NXOpen.Point3d):  The junction origin .
        """
        pass
    def GetKinematicsVersion(self) -> SmkWizardBuilder.KinematicsVersionType:
        """
         Get the kinematics version 
         Returns kimVersion ( SmkWizardBuilder.KinematicsVersionType NXOp):  The kinematics version .
        """
        pass
    def GetMachineKitManufacturer(self) -> str:
        """
         Get the machine kit manufacturer 
         Returns manufacturer (str):  The machine kit manufacturer .
        """
        pass
    def GetWizardStep(self) -> SmkWizardBuilder.WizardStep:
        """
         Get the wizard step 
         Returns wizardStep ( SmkWizardBuilder.WizardStep NXOp):  The wizard step .
        """
        pass
    def HasAxis(self, axisName: str) -> bool:
        """
         Check if axis exists 
         Returns result (bool): .
        """
        pass
    def HasComponent(self, componentName: str) -> bool:
        """
         Check if component exists 
         Returns result (bool): .
        """
        pass
    def MoveAxis(self, source: str, target: str) -> None:
        """
         Move axis 
        """
        pass
    def MoveComponent(self, source: str, target: str) -> None:
        """
         Move components 
        """
        pass
    def MoveJunctions(self, source: str, target: str) -> None:
        """
         Move junctions 
        """
        pass
    def ParseTemplates(self) -> None:
        """
         Parse template json files 
        """
        pass
    def RemoveComponentClassification(self, componentName: str, classificationType: SmkWizardBuilder.ComponentClassificationType) -> None:
        """
         Remove Classification 
        """
        pass
    def RenameAxis(self, compName: str, oldAxisName: str, newAxisName: str) -> None:
        """
         Rename the axis 
        """
        pass
    def RenameAxisJunction(self, jctFullName: str, newJunctionName: str) -> None:
        """
         Rename the axis junction 
        """
        pass
    def RenameChain(self, oldChainName: str, newChainName: str) -> None:
        """
         Rename the chain 
        """
        pass
    def RenameComponent(self, componentName: str, newComponentName: str) -> None:
        """
         Edit the component name 
        """
        pass
    def RenameJunction(self, jctFullName: str, newJunctionName: str) -> None:
        """
         Rename the junction 
        """
        pass
    def ResetWizard(self) -> None:
        """
         Reset the smk wizard 
        """
        pass
    def SetAdjustRegister(self, componentName: str, adjustReg: int) -> None:
        """
         Set adjust register 
        """
        pass
    def SetArchieveData(self) -> None:
        """
         Sets the machine archive data to Machine Kit Editor 
        """
        pass
    def SetAxisCoarsePrecision(self, axisName: str, value: float) -> None:
        """
         Sets the axis coarse precision.
                    This defines the exact stop precision used to determine if a target point has been
                    reached, so that the next NC-block can be executed.  
        """
        pass
    def SetAxisDirection(self, axisName: str, axisDir: SmkWizardBuilder.AxisDirectionType) -> None:
        """
         Set the axis direction 
        """
        pass
    def SetAxisFinePrecision(self, axisName: str, value: float) -> None:
        """
         Sets the axis fine precision.
                    This defines the exact stop precision used to determine if a target point has been
                    reached, so that the next NC-block can be executed.  
        """
        pass
    def SetAxisInitialValue(self, axisName: str, initialValue: float) -> None:
        """
         Gets the axis initial value 
        """
        pass
    def SetAxisJerkLimit(self, axisName: str, value: float) -> None:
        """
         Sets the axis jerk limit.
                    The jerk limit value limits jumps in acceleration. 
        """
        pass
    def SetAxisJumpVelocity(self, axisName: str, value: float) -> None:
        """
         Sets the axis jump velocity.
                    The jump velocity define a lag time at the beginning of the motion.  
        """
        pass
    def SetAxisJunctionName(self, axisName: str, junctionName: str) -> None:
        """
         Sets the axis junction name 
        """
        pass
    def SetAxisKv(self, axisName: str, value: float) -> None:
        """
         Sets the axis kv.
                    the Kv-Factor is a parameter of the drives. It influences the dragging error
                    (difference between ideal motion profile and actual motion profile).  
        """
        pass
    def SetAxisLowerLimit(self, axisName: str, lowerValue: float) -> None:
        """
         Sets the axis lower limit 
        """
        pass
    def SetAxisLowerSoftLimit(self, axisName: str, lowerSoftValue: float) -> None:
        """
         Sets the axis lower soft limit.
                    The soft limit on the real machine is checked by the controller to avoid that the machine
                    travels into the mechanical stop (Hard Limit) with full speed (prevent damage). 
        """
        pass
    def SetAxisMaximumAcceleration(self, axisName: str, value: float) -> None:
        """
         Sets the axis maximum acceleration.
                    The maximum acceleration defines how fast the axis can accelerate.
        """
        pass
    def SetAxisMaximumDeceleration(self, axisName: str, value: float) -> None:
        """
         Sets the axis maximum deceleration.
                    The maximum deceleration defines how fast the axis can decelerate. 
        """
        pass
    def SetAxisMaximumVelocity(self, axisName: str, value: float) -> None:
        """
         Sets the axis maximum velocity 
        """
        pass
    def SetAxisMotion(self, axisName: str, isNcAxis: bool, type: SmkWizardBuilder.AxisMotionType) -> None:
        """
         Set the axis motion 
        """
        pass
    def SetAxisNumber(self, axisName: str, number: int) -> None:
        """
         Sets the axis number.
                The axis number is used in cases where an axis is programmed through a number
                instead of through an address (e.g. on Siemens 840D: AX1=10 instead of X10).
        """
        pass
    def SetAxisUpperLimit(self, axisName: str, upperValue: float) -> None:
        """
         Sets the axis upper limit 
        """
        pass
    def SetAxisUpperSoftLimit(self, axisName: str, upperSoftValue: float) -> None:
        """
         Sets the axis upper soft limit.
                    The soft limit on the real machine is checked by the controller to avoid that the machine
                    travels into the mechanical stop (Hard Limit) with full speed (prevent damage). 
        """
        pass
    def SetCapacity(self, componentName: str, capacity: int) -> None:
        """
         Set capacity 
        """
        pass
    def SetCutcomRegister(self, componentName: str, cutcomReg: int) -> None:
        """
         Set cutcom register 
        """
        pass
    def SetDeviceID(self, componentName: str, deviceId: str) -> None:
        """
         Set device id 
        """
        pass
    def SetGeometries(self, componentName: str, geos: List[NXOpen.NXObject]) -> None:
        """
         Sets geometry elements for the component 
        """
        pass
    def SetHolderID(self, componentName: str, holderId: str) -> None:
        """
         Set holder id 
        """
        pass
    def SetJunctionClassification(self, junctionName: str, jctClass: SmkWizardBuilder.JunctionClassificationType) -> None:
        """
         Sets the classification of the junction 
        """
        pass
    def SetJunctionCsys(self, junctionName: str, csys: NXOpen.CartesianCoordinateSystem) -> None:
        """
         Sets the CSYS associated with the junction 
        """
        pass
    def SetKinematicsVersion(self, kimVersion: SmkWizardBuilder.KinematicsVersionType) -> None:
        """
         Set the kinematics version 
        """
        pass
    def SetMachineKitManufacturer(self, manufacturer: str) -> None:
        """
         Set the machine kit manufacturer 
        """
        pass
    def SetPocketTransformAdjustRegisterIncrement(self, pocketName: str, increment: int) -> None:
        """
         Set pocket transform adjust register id increment 
        """
        pass
    def SetPocketTransformCutcomRegisterIncrement(self, pocketName: str, increment: int) -> None:
        """
         Set pocket transform cutcom register increment 
        """
        pass
    def SetPocketTransformDivision(self, pocketName: str, division: int) -> None:
        """
         Set pocket transform division 
        """
        pass
    def SetPocketTransformHolderIDIncrement(self, pocketName: str, increment: int) -> None:
        """
         Set pocket transform holder id increment 
        """
        pass
    def SetPocketTransformHolderIDReference(self, pocketName: str, reference: int) -> None:
        """
         Set pocket transform holder id reference 
        """
        pass
    def SetPocketTransformNumberOfCopies(self, pocketName: str, numOfCopies: int) -> None:
        """
         Set pocket transform number of copies 
        """
        pass
    def SetPocketTransformRotateAngle(self, pocketName: str, angle: float) -> None:
        """
         Set pocket transform angle 
        """
        pass
    def SetPocketTransformRotateLineEndPoint(self, pocketName: str, X: float, Y: float, Z: float) -> None:
        """
         Set pocket transform rotate end point 
        """
        pass
    def SetPocketTransformRotateLinePoint(self, pocketName: str, X: float, Y: float, Z: float) -> None:
        """
         Set pocket transform rotate line point 
        """
        pass
    def SetPocketTransformRotateLineStartPoint(self, pocketName: str, X: float, Y: float, Z: float) -> None:
        """
         Set pocket transform rotate start point 
        """
        pass
    def SetPocketTransformRotateLineVector(self, pocketName: str, i: float, j: float, k: float) -> None:
        """
         Set pocket transform rotate line vector 
        """
        pass
    def SetPocketTransformTranslateDeltaXC(self, pocketName: str, deltaXC: float) -> None:
        """
         Set pocket transform DeltaXC 
        """
        pass
    def SetPocketTransformTranslateDeltaYC(self, pocketName: str, deltaYC: float) -> None:
        """
         Set pocket transform DeltaYC 
        """
        pass
    def SetPocketTransformTranslateDeltaZC(self, pocketName: str, deltaZC: float) -> None:
        """
         Set pocket transform DeltaZC 
        """
        pass
    def SetPocketTransformTranslateReferencePoint(self, pocketName: str, X: float, Y: float, Z: float) -> None:
        """
         Set pocket transform translate reference point 
        """
        pass
    def SetPocketTransformTranslateToPoint(self, pocketName: str, X: float, Y: float, Z: float) -> None:
        """
         Set pocket transform translate to point 
        """
        pass
    def SetPocketTransformType(self, pocketName: str, transformType: SmkWizardBuilder.PocketTransformType) -> None:
        """
         Set pocket transform type 
        """
        pass
    def SetWizardStep(self, wizardStep: SmkWizardBuilder.WizardStep) -> None:
        """
         Set the wizard step 
        """
        pass
    def UpdateChain(self, chainName: str, chainAttributes: str) -> None:
        """
         Update the chain 
        """
        pass
import NXOpen
class Snapshot(NXOpen.NXObject): 
    """  Represents the Snapshot class object   """
    pass
import NXOpen
class TimeAnalysis(NXOpen.TaggedObject): 
    """  Represents the TimeAnalysis class object   """
    def Reset(self) -> None:
        """
         Reset the Time Analysis
        """
        pass
    def Start(self) -> None:
        """
         Start the Time Analysis
        """
        pass
    def Stop(self) -> None:
        """
         Stop the Time Analysis
        """
        pass
