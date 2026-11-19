from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents a ArchiveImportBuilder builder object.
##      <br> To create a new instance of this class, use @link NXOpen::SIM::KinematicConfigurator::CreateArchiveImportBuilder  NXOpen::SIM::KinematicConfigurator::CreateArchiveImportBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.3  <br> 

class ArchiveImportBuilder(NXOpen.Builder): 
    """ Represents a ArchiveImportBuilder builder object.
    """


    ## Getter for property: (str) FileName
    ##   the archive file name from which to import data   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## @return str
    @property
    def FileName(self) -> str:
        """
        Getter for property: (str) FileName
          the archive file name from which to import data   
            
         
        """
        pass
    
    ## Setter for property: (str) FileName

    ##   the archive file name from which to import data   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    @FileName.setter
    def FileName(self, fileName: str):
        """
        Setter for property: (str) FileName
          the archive file name from which to import data   
            
         
        """
        pass
    
    ## Getter for property: (bool) ImportCollisionAvoidance
    ##   the setting for importing collision avoidance data.  
    ##     If true then collision avoidance data will be imported instead of the machine configuration.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## @return bool
    @property
    def ImportCollisionAvoidance(self) -> bool:
        """
        Getter for property: (bool) ImportCollisionAvoidance
          the setting for importing collision avoidance data.  
            If true then collision avoidance data will be imported instead of the machine configuration.   
         
        """
        pass
    
    ## Setter for property: (bool) ImportCollisionAvoidance

    ##   the setting for importing collision avoidance data.  
    ##     If true then collision avoidance data will be imported instead of the machine configuration.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    @ImportCollisionAvoidance.setter
    def ImportCollisionAvoidance(self, importSetting: bool):
        """
        Setter for property: (bool) ImportCollisionAvoidance
          the setting for importing collision avoidance data.  
            If true then collision avoidance data will be imported instead of the machine configuration.   
         
        """
        pass
    
import NXOpen
##   @brief  Represents the Breakpoint class object  
## 
##     <br> Use the @link NXOpen::SIM::NcProgramManagerBuilder NXOpen::SIM::NcProgramManagerBuilder@endlink  class to create a Breakpoint object.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class Breakpoint(NXOpen.NXObject): 
    """ <summary> Represents the Breakpoint class object </summary>  """


    ## Getter for property: (str) Condition
    ##   the condition for a breakpoint.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return str
    @property
    def Condition(self) -> str:
        """
        Getter for property: (str) Condition
          the condition for a breakpoint.  
             
         
        """
        pass
    
    ## Setter for property: (str) Condition

    ##   the condition for a breakpoint.  
    ##      
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @Condition.setter
    def Condition(self, condition: str):
        """
        Setter for property: (str) Condition
          the condition for a breakpoint.  
             
         
        """
        pass
    
    ##  Activate the breakpoint. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    @staticmethod
    def Activate(breakpoint: Breakpoint) -> None:
        """
         Activate the breakpoint. 
        """
        pass
    
    ##  Deactivate the breakpoint. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    @staticmethod
    def Deactivate(breakpoint: Breakpoint) -> None:
        """
         Deactivate the breakpoint. 
        """
        pass
    
    ##  Delete the breakpoint. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    @staticmethod
    def Delete(breakpoint: Breakpoint) -> None:
        """
         Delete the breakpoint. 
        """
        pass
    
import NXOpen
##  This class is used for the Export Machine Kit Dialog.
##         Calling @link Builder::Commit Builder::Commit@endlink  on this
##         builder will start the export machine kit process
##         and return NULL.
##       <br> Use  @link NXOpen::SIM::KinematicConfigurator::ExportMachineKitBuilder NXOpen::SIM::KinematicConfigurator::ExportMachineKitBuilder@endlink  class to obtain an instance of this class.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class ExportMachineKitBuilder(NXOpen.Builder): 
    """ This class is used for the Export Machine Kit Dialog.
        Calling <ja_method>Builder.Commit</ja_method> on this
        builder will start the export machine kit process
        and return <ja_NULL>.
     """


    ## Getter for property: (str) KitName
    ##   the kit name specify the name of the package.  
    ##    The name should be unique in the target directory.  
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return str
    @property
    def KitName(self) -> str:
        """
        Getter for property: (str) KitName
          the kit name specify the name of the package.  
           The name should be unique in the target directory.  
         
        """
        pass
    
    ## Setter for property: (str) KitName

    ##   the kit name specify the name of the package.  
    ##    The name should be unique in the target directory.  
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @KitName.setter
    def KitName(self, kit_name: str):
        """
        Setter for property: (str) KitName
          the kit name specify the name of the package.  
           The name should be unique in the target directory.  
         
        """
        pass
    
    ## Getter for property: (str) OutputDirectory
    ##   the machine kit output directory specify where the finished package will be stored.  
    ##     
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return str
    @property
    def OutputDirectory(self) -> str:
        """
        Getter for property: (str) OutputDirectory
          the machine kit output directory specify where the finished package will be stored.  
            
         
        """
        pass
    
    ## Setter for property: (str) OutputDirectory

    ##   the machine kit output directory specify where the finished package will be stored.  
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @OutputDirectory.setter
    def OutputDirectory(self, output_directory: str):
        """
        Setter for property: (str) OutputDirectory
          the machine kit output directory specify where the finished package will be stored.  
            
         
        """
        pass
    
    ## Getter for property: (bool) PrintReport
    ##   the machine kit print report checkbox specify if a report will be plotted while create the kit or not.  
    ##     
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def PrintReport(self) -> bool:
        """
        Getter for property: (bool) PrintReport
          the machine kit print report checkbox specify if a report will be plotted while create the kit or not.  
            
         
        """
        pass
    
    ## Setter for property: (bool) PrintReport

    ##   the machine kit print report checkbox specify if a report will be plotted while create the kit or not.  
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @PrintReport.setter
    def PrintReport(self, onOff: bool):
        """
        Setter for property: (bool) PrintReport
          the machine kit print report checkbox specify if a report will be plotted while create the kit or not.  
            
         
        """
        pass
    
    ##  Add a subdirectory to the machine kit at the given directory. The directory can be get in the function GetAllKitPaths.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  directory in kit
    def AddKitDirectory(builder: ExportMachineKitBuilder, directory: str, subDirectory: str) -> None:
        """
         Add a subdirectory to the machine kit at the given directory. The directory can be get in the function GetAllKitPaths.
        """
        pass
    
    ##  Add a file to the machine kit at the given directory. The directory can be get in the function GetAllKitPaths.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  directory in kit
    def AddKitFile(builder: ExportMachineKitBuilder, directory: str, file: str) -> None:
        """
         Add a file to the machine kit at the given directory. The directory can be get in the function GetAllKitPaths.
        """
        pass
    
    ##  Add a folder, all containing files and subfolder to the machine kit at the given directory. 
    ##             The directory can be get in the function GetAllKitPaths.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  directory in kit
    def AddKitFolder(builder: ExportMachineKitBuilder, directory: str, folder: str) -> None:
        """
         Add a folder, all containing files and subfolder to the machine kit at the given directory. 
                    The directory can be get in the function GetAllKitPaths.
        """
        pass
    
    ##  Returns a array of the the file paths that are already in the machine kit. If you want to modify what
    ##             will export with the kit, you need to specify the whole kit path. This function gives the opportunity. 
    ##             This function allocates the memory for kitPaths. The caller is responsible to deallocate the memory.
    ##  @return kitFiles (List[str]):  array of all files of the machine kit.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    @staticmethod
    def GetAllKitPaths(builder: ExportMachineKitBuilder) -> List[str]:
        """
         Returns a array of the the file paths that are already in the machine kit. If you want to modify what
                    will export with the kit, you need to specify the whole kit path. This function gives the opportunity. 
                    This function allocates the memory for kitPaths. The caller is responsible to deallocate the memory.
         @return kitFiles (List[str]):  array of all files of the machine kit.
        """
        pass
    
    ##  Loads all the devices in the current machine. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    @staticmethod
    def LoadDeviceDirectory(builder: ExportMachineKitBuilder) -> None:
        """
         Loads all the devices in the current machine. 
        """
        pass
    
    ##  Loads all the tools in the current machine. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    @staticmethod
    def LoadToolDirectory(builder: ExportMachineKitBuilder) -> None:
        """
         Loads all the tools in the current machine. 
        """
        pass
    
    ##  Removes the given file or directory in the machine kit. The directory can be get in the function GetAllKitPaths.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  directory in kit
    def RemovePathInKit(builder: ExportMachineKitBuilder, directory: str) -> None:
        """
         Removes the given file or directory in the machine kit. The directory can be get in the function GetAllKitPaths.
        """
        pass
    
    ##  Rename a directory to the machine kit at the given directory. The directory can be get in the function GetAllKitPaths.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  directory path in kit
    def RenameKitDirectory(builder: ExportMachineKitBuilder, directory: str, newDirectoryName: str) -> None:
        """
         Rename a directory to the machine kit at the given directory. The directory can be get in the function GetAllKitPaths.
        """
        pass
    
import NXOpen
##  This class is used for the Import Machine Kit Dialog.
##     Calling @link Builder::Commit Builder::Commit@endlink  on this
##     builder will start the import machine kit process
##     and return NULL.
##      <br> Use the @link Part Part@endlink  class to import a Machine Kit object.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class ImportMachineKitBuilder(NXOpen.Builder): 
    """ This class is used for the Import Machine Kit Dialog.
    Calling <ja_method>Builder.Commit</ja_method> on this
    builder will start the import machine kit process
    and return <ja_NULL>.
    """


    ## Getter for property: (str) OutputDirectory
    ##   the machine kit output directory specify where the finished machine folder will be stored.  
    ##     
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return str
    @property
    def OutputDirectory(self) -> str:
        """
        Getter for property: (str) OutputDirectory
          the machine kit output directory specify where the finished machine folder will be stored.  
            
         
        """
        pass
    
    ## Setter for property: (str) OutputDirectory

    ##   the machine kit output directory specify where the finished machine folder will be stored.  
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @OutputDirectory.setter
    def OutputDirectory(self, output_directory: str):
        """
        Setter for property: (str) OutputDirectory
          the machine kit output directory specify where the finished machine folder will be stored.  
            
         
        """
        pass
    
    ## Getter for property: (bool) PrintReport
    ##   the machine print report flat that specifies if a report will be plotted while import the machine or not.  
    ##      
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def PrintReport(self) -> bool:
        """
        Getter for property: (bool) PrintReport
          the machine print report flat that specifies if a report will be plotted while import the machine or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) PrintReport

    ##   the machine print report flat that specifies if a report will be plotted while import the machine or not.  
    ##      
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @PrintReport.setter
    def PrintReport(self, onOff: bool):
        """
        Setter for property: (bool) PrintReport
          the machine print report flat that specifies if a report will be plotted while import the machine or not.  
             
         
        """
        pass
    
import NXOpen
## 
##     Represents a @link NXOpen::SIM::IsvControlPanelBuilder NXOpen::SIM::IsvControlPanelBuilder@endlink 
##      <br> To create a new instance of this class, use @link NXOpen::SIM::KinematicConfigurator::CreateIsvControlPanelBuilder  NXOpen::SIM::KinematicConfigurator::CreateIsvControlPanelBuilder @endlink  <br> 
## 
##   <br>  Created in NX8.0.0  <br> 

class IsvControlPanelBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>NXOpen.SIM.IsvControlPanelBuilder</ja_class>
    """


    ##  Type of record reported in the Simulation Details group 
    ##  Info        
    class DetailType(Enum):
        """
        Members Include: <Info> <Controller> <Limit> <Collision> <Gouge> <Singularity>
        """
        Info: int
        Controller: int
        Limit: int
        Collision: int
        Gouge: int
        Singularity: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> IsvControlPanelBuilder.DetailType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Simulation Language 
    ##  NC language 
    class Language(Enum):
        """
        Members Include: <Nc> <Ac> <Cse>
        """
        Nc: int
        Ac: int
        Cse: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> IsvControlPanelBuilder.Language:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The Single Step Mode type that used in @link  NXOpen::SIM::IsvControlPanelBuilder::VisualizationTypeMachineCodeSimulateCse   NXOpen::SIM::IsvControlPanelBuilder::VisualizationTypeMachineCodeSimulateCse @endlink  simulation mode.
    ##  Step In 
    class SingleStepModeType(Enum):
        """
        Members Include: <StepIn> <StepOver> <StepOut> <DisplayUpdate>
        """
        StepIn: int
        StepOver: int
        StepOut: int
        DisplayUpdate: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> IsvControlPanelBuilder.SingleStepModeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The Single Step type that used in @link  NXOpen::SIM::IsvControlPanelBuilder::VisualizationTypeMachineCodeSimulateMtd   NXOpen::SIM::IsvControlPanelBuilder::VisualizationTypeMachineCodeSimulateMtd @endlink  or
    ##             @link  NXOpen::SIM::IsvControlPanelBuilder::VisualizationTypeToolPathSimulation   NXOpen::SIM::IsvControlPanelBuilder::VisualizationTypeToolPathSimulation @endlink  simulation mode.
    ##             The following @link  NXOpen::SIM::IsvControlPanelBuilder::SingleStepType   NXOpen::SIM::IsvControlPanelBuilder::SingleStepType @endlink  members are removed in NX10.0.2:
    ##             - StepOut
    ##             - StepIn
    ##             - Display
    ##             Replacement:
    ##             Use the following @link  NXOpen::SIM::IsvControlPanelBuilder::SingleStepModeType   NXOpen::SIM::IsvControlPanelBuilder::SingleStepModeType @endlink  member instead:
    ##             - @link  NXOpen::SIM::IsvControlPanelBuilder::SingleStepModeTypeStepOut   NXOpen::SIM::IsvControlPanelBuilder::SingleStepModeTypeStepOut @endlink 
    ##             - @link  NXOpen::SIM::IsvControlPanelBuilder::SingleStepModeTypeStepIn   NXOpen::SIM::IsvControlPanelBuilder::SingleStepModeTypeStepIn @endlink 
    ##             - @link  NXOpen::SIM::IsvControlPanelBuilder::SingleStepModeTypeDisplayUpdate   NXOpen::SIM::IsvControlPanelBuilder::SingleStepModeTypeDisplayUpdate @endlink 
    ##         
    ##  Block 
    class SingleStepType(Enum):
        """
        Members Include: <Block> <Move> <Event>
        """
        Block: int
        Move: int
        Event: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> IsvControlPanelBuilder.SingleStepType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The Visualization type 
    ##  Machine Code Simulate Cse 
    class VisualizationType(Enum):
        """
        Members Include: <MachineCodeSimulateCse> <MachineCodeSimulateMtd> <ToolPathSimulation>
        """
        MachineCodeSimulateCse: int
        MachineCodeSimulateMtd: int
        ToolPathSimulation: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> IsvControlPanelBuilder.VisualizationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Type of VNC Mode  
    ##  ERROR  
    class VncMode(Enum):
        """
        Members Include: <Error> <Notconnected> <Connected> <Booted> <Configured> <Initialized> <ProgramsLoaded> <Reset> <Stop> <Start> <Run>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> IsvControlPanelBuilder.VncMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) ActiveChannel
    ##   the active channel in simulation.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def ActiveChannel(self) -> str:
        """
        Getter for property: (str) ActiveChannel
          the active channel in simulation.  
             
         
        """
        pass
    
    ## Setter for property: (str) ActiveChannel

    ##   the active channel in simulation.  
    ##      
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ActiveChannel.setter
    def ActiveChannel(self, channelName: str):
        """
        Setter for property: (str) ActiveChannel
          the active channel in simulation.  
             
         
        """
        pass
    
    ## Getter for property: (bool) IsInHistoryBuffer
    ##   the simulation is inside history buffer    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## @return bool
    @property
    def IsInHistoryBuffer(self) -> bool:
        """
        Getter for property: (bool) IsInHistoryBuffer
          the simulation is inside history buffer    
            
         
        """
        pass
    
    ## Getter for property: (str) MachineConfiguratorFilename
    ##   the machine configurator filename with full path  
    ##     
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ## 
    ##   <br>  Created in NX10.0.1  <br> 

    ## @return str
    @property
    def MachineConfiguratorFilename(self) -> str:
        """
        Getter for property: (str) MachineConfiguratorFilename
          the machine configurator filename with full path  
            
         
        """
        pass
    
    ## Getter for property: (str) MachineTime
    ##   the current machine time.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return str
    @property
    def MachineTime(self) -> str:
        """
        Getter for property: (str) MachineTime
          the current machine time.  
             
         
        """
        pass
    
    ## Getter for property: (@link SimDebugBuilder NXOpen.SIM.SimDebugBuilder@endlink) SimDebugBuilder
    ##   the sim debug builder   
    ##     
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1899.0.0.  Use @link NXOpen::SIM::KinematicConfigurator::CreateSimDebugBuilder() NXOpen::SIM::KinematicConfigurator::CreateSimDebugBuilder()@endlink  instead to create a SimDebugBuilder.  <br> 

    ## @return SimDebugBuilder
    @property
    def SimDebugBuilder(self) -> SimDebugBuilder:
        """
        Getter for property: (@link SimDebugBuilder NXOpen.SIM.SimDebugBuilder@endlink) SimDebugBuilder
          the sim debug builder   
            
         
        """
        pass
    
    ## Getter for property: (@link LoadSnapshotBuilder NXOpen.SIM.LoadSnapshotBuilder@endlink) SimulationLoadSnapshotBuilder
    ##   the load snapshot builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return LoadSnapshotBuilder
    @property
    def SimulationLoadSnapshotBuilder(self) -> LoadSnapshotBuilder:
        """
        Getter for property: (@link LoadSnapshotBuilder NXOpen.SIM.LoadSnapshotBuilder@endlink) SimulationLoadSnapshotBuilder
          the load snapshot builder   
            
         
        """
        pass
    
    ## Getter for property: (@link SimulationOptionsBuilder NXOpen.CAM.SimulationOptionsBuilder@endlink) SimulationOptionsBuilder
    ##   the simulation options builder   
    ##     
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return SimulationOptionsBuilder
    @property
    def SimulationOptionsBuilder(self) -> SimulationOptionsBuilder:
        """
        Getter for property: (@link SimulationOptionsBuilder NXOpen.CAM.SimulationOptionsBuilder@endlink) SimulationOptionsBuilder
          the simulation options builder   
            
         
        """
        pass
    
    ## Getter for property: (@link SaveSnapshotBuilder NXOpen.SIM.SaveSnapshotBuilder@endlink) SimulationSaveSnapshotBuilder
    ##   the save snapshot builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return SaveSnapshotBuilder
    @property
    def SimulationSaveSnapshotBuilder(self) -> SaveSnapshotBuilder:
        """
        Getter for property: (@link SaveSnapshotBuilder NXOpen.SIM.SaveSnapshotBuilder@endlink) SimulationSaveSnapshotBuilder
          the save snapshot builder   
            
         
        """
        pass
    
    ## Getter for property: (@link IsvControlPanelBuilder.VncMode NXOpen.SIM.IsvControlPanelBuilder.VncMode@endlink) VncStatus
    ##   the mode of VNC   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## @return IsvControlPanelBuilder.VncMode
    @property
    def VncStatus(self) -> IsvControlPanelBuilder.VncMode:
        """
        Getter for property: (@link IsvControlPanelBuilder.VncMode NXOpen.SIM.IsvControlPanelBuilder.VncMode@endlink) VncStatus
          the mode of VNC   
            
         
        """
        pass
    
    ##  Prototype for IsInHistoryBufferChanged callbacks 
    ## A callback definition with the following input arguments: 
    ##  - bool
    ##  and no return type
    IsInHistoryBufferCb = Callable[[bool], None]
    
    
    ##  Registers the IsInHistoryBufferChanged callback. 
    ##  @return handlerId (int):  .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  
    def AddIsInHistoryBuffer(builder: IsvControlPanelBuilder, handler: IsvControlPanelBuilder.IsInHistoryBufferCb) -> int:
        """
         Registers the IsInHistoryBufferChanged callback. 
         @return handlerId (int):  .
        """
        pass
    
    ##  Prototype for SimEnd callbacks 
    ## A callback definition with no input arguments and no return type
    SimEndCb = Callable[[], None]
    
    
    ##  Registers the SimEnd callback. 
    ##  @return handlerId (int):  .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  
    def AddSimEnd(builder: IsvControlPanelBuilder, handler: IsvControlPanelBuilder.SimEndCb) -> int:
        """
         Registers the SimEnd callback. 
         @return handlerId (int):  .
        """
        pass
    
    ##  Prototype for SimStart callbacks 
    ## A callback definition with no input arguments and no return type
    SimStartCb = Callable[[], None]
    
    
    ##  Registers the SimStart callback. 
    ##  @return handlerId (int):  .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddSimStart(builder: IsvControlPanelBuilder, handler: IsvControlPanelBuilder.SimStartCb) -> int:
        """
         Registers the SimStart callback. 
         @return handlerId (int):  .
        """
        pass
    
    ##  Prototype for SimStop callbacks 
    ## A callback definition with no input arguments and no return type
    SimStopCb = Callable[[], None]
    
    
    ##  Registers the SimStop callback. 
    ##  @return handlerId (int):  .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  
    def AddSimStop(builder: IsvControlPanelBuilder, handler: IsvControlPanelBuilder.SimStopCb) -> int:
        """
         Registers the SimStop callback. 
         @return handlerId (int):  .
        """
        pass
    
    ##  Prototype for VNC Status callbacks 
    ## A callback definition with the following input arguments: 
    ##  - @link IsvControlPanelBuilder.VncMode NXOpen.SIM.IsvControlPanelBuilder.VncMode@endlink
    ##  and no return type
    VncStatusCb = Callable[[IsvControlPanelBuilder.VncMode], None]
    
    
    ##  Registers the VNC Status callback. 
    ##  @return handlerId (int):  .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  
    def AddVncStatus(builder: IsvControlPanelBuilder, handler: IsvControlPanelBuilder.VncStatusCb) -> int:
        """
         Registers the VNC Status callback. 
         @return handlerId (int):  .
        """
        pass
    
    ##  Apply the simulation options
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    @staticmethod
    def ApplySimulationOptions(builder: IsvControlPanelBuilder) -> None:
        """
         Apply the simulation options
        """
        pass
    
    ##  Check the syntax of nc programs. 
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  nc programs where the syntax should be checked. 
    def CheckProgramSyntax(builder: IsvControlPanelBuilder, programs: List[NcProgram]) -> None:
        """
         Check the syntax of nc programs. 
        """
        pass
    
    ##  Evaluate expression in NC, CSE or AnyController language
    ##  @return A tuple consisting of (success, value, valueType). 
    ##  - success is: bool. Was the evaluation successful?.
    ##  - value is: str. The expression value.
    ##  - valueType is: str. The expression value's type.

    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The channel name
    @staticmethod
    def EvaluateExpression(builder: IsvControlPanelBuilder, channelName: str, expression: str, language: IsvControlPanelBuilder.Language) -> Tuple[bool, str, str]:
        """
         Evaluate expression in NC, CSE or AnyController language
         @return A tuple consisting of (success, value, valueType). 
         - success is: bool. Was the evaluation successful?.
         - value is: str. The expression value.
         - valueType is: str. The expression value's type.

        """
        pass
    
    ##  Returns a program currently used in the simulation 
    ##  @return program (@link NcProgram NXOpen.SIM.NcProgram@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The channel name. 
    def GetCurrentProgram(builder: IsvControlPanelBuilder, channelName: str, stackLevel: int) -> NcProgram:
        """
         Returns a program currently used in the simulation 
         @return program (@link NcProgram NXOpen.SIM.NcProgram@endlink): .
        """
        pass
    
    ##  Return the Details Information to a specified type 
    ##  @return A tuple consisting of (result, time, description, ncLine, programName, channelName). 
    ##  - result is: bool.
    ##  - time is: float.
    ##  - description is: str.
    ##  - ncLine is: int.
    ##  - programName is: str.
    ##  - channelName is: str.

    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ## 
    ## <param name="type"> (@link IsvControlPanelBuilder.DetailType NXOpen.SIM.IsvControlPanelBuilder.DetailType@endlink) </param>
    ## <param name="position"> (int) </param>
    @staticmethod
    def GetDetail(builder: IsvControlPanelBuilder, type: IsvControlPanelBuilder.DetailType, position: int) -> Tuple[bool, float, str, int, str, str]:
        """
         Return the Details Information to a specified type 
         @return A tuple consisting of (result, time, description, ncLine, programName, channelName). 
         - result is: bool.
         - time is: float.
         - description is: str.
         - ncLine is: int.
         - programName is: str.
         - channelName is: str.

        """
        pass
    
    ##  Return the number of Details of the specified type 
    ##  @return count (int): .
    ## 
    ##   <br>  Created in NX10.0.1  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ## 
    ## <param name="type"> (@link IsvControlPanelBuilder.DetailType NXOpen.SIM.IsvControlPanelBuilder.DetailType@endlink) </param>
    def GetDetailCount(builder: IsvControlPanelBuilder, type: IsvControlPanelBuilder.DetailType) -> int:
        """
         Return the number of Details of the specified type 
         @return count (int): .
        """
        pass
    
    ##  Return the Machining Time Analysis Clock for the specified channel. 
    ##  @return clock (@link TimeAnalysis NXOpen.SIM.TimeAnalysis@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The channel name.
    def GetMachiningTimeAnalysisClock(builder: IsvControlPanelBuilder, channelName: str) -> TimeAnalysis:
        """
         Return the Machining Time Analysis Clock for the specified channel. 
         @return clock (@link TimeAnalysis NXOpen.SIM.TimeAnalysis@endlink): .
        """
        pass
    
    ##  Get the post processor definition and tcl filename with full path
    ##  @return A tuple consisting of (tclFilename, definitionFilename). 
    ##  - tclFilename is: str. The tcl filename with full path.
    ##  - definitionFilename is: str. The definition filename with full path.

    ## 
    ##   <br>  Created in NX10.0.1  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    @staticmethod
    def GetPostprocessorFilename(builder: IsvControlPanelBuilder) -> Tuple[str, str]:
        """
         Get the post processor definition and tcl filename with full path
         @return A tuple consisting of (tclFilename, definitionFilename). 
         - tclFilename is: str. The tcl filename with full path.
         - definitionFilename is: str. The definition filename with full path.

        """
        pass
    
    ##  Gets the show tool path
    ##  @return state (bool): .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetShowToolPath(builder: IsvControlPanelBuilder) -> bool:
        """
         Gets the show tool path
         @return state (bool): .
        """
        pass
    
    ##  Gets the show tool trace
    ##  @return state (bool): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetShowToolTrace(builder: IsvControlPanelBuilder) -> bool:
        """
         Gets the show tool trace
         @return state (bool): .
        """
        pass
    
    ##  Gets the single step in Tool Path Based Simulation
    ##  @return type (@link IsvControlPanelBuilder.SingleStepType NXOpen.SIM.IsvControlPanelBuilder.SingleStepType@endlink): .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSingleStep(builder: IsvControlPanelBuilder) -> IsvControlPanelBuilder.SingleStepType:
        """
         Gets the single step in Tool Path Based Simulation
         @return type (@link IsvControlPanelBuilder.SingleStepType NXOpen.SIM.IsvControlPanelBuilder.SingleStepType@endlink): .
        """
        pass
    
    ##  Gets the single step mode in Machine Code Simulation
    ##  @return type (@link IsvControlPanelBuilder.SingleStepModeType NXOpen.SIM.IsvControlPanelBuilder.SingleStepModeType@endlink): .
    ## 
    ##   <br>  Created in NX10.0.2  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSingleStepMode(builder: IsvControlPanelBuilder) -> IsvControlPanelBuilder.SingleStepModeType:
        """
         Gets the single step mode in Machine Code Simulation
         @return type (@link IsvControlPanelBuilder.SingleStepModeType NXOpen.SIM.IsvControlPanelBuilder.SingleStepModeType@endlink): .
        """
        pass
    
    ##  Gets the visualization
    ##  @return type (@link IsvControlPanelBuilder.VisualizationType NXOpen.SIM.IsvControlPanelBuilder.VisualizationType@endlink): .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetVisualization(builder: IsvControlPanelBuilder) -> IsvControlPanelBuilder.VisualizationType:
        """
         Gets the visualization
         @return type (@link IsvControlPanelBuilder.VisualizationType NXOpen.SIM.IsvControlPanelBuilder.VisualizationType@endlink): .
        """
        pass
    
    ##  Jump to details line
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The details window line
    def JumpToDetailsLine(builder: IsvControlPanelBuilder, line: int) -> None:
        """
         Jump to details line
        """
        pass
    
    ##  Jump to machine time
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The machine time in hh:mm:ss.s format
    def JumpToMachineTime(builder: IsvControlPanelBuilder, machineTime: str) -> None:
        """
         Jump to machine time
        """
        pass
    
    ##  Jump to nc program line in the active channel
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The nc program window line
    @overload
    def JumpToNcProgramLine(self, builder: IsvControlPanelBuilder, line: int) -> None:
        """
         Jump to nc program line in the active channel
        """
        pass
    
    ##  Jump to nc program line in the specified channel
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The channel name. If this is NULL or empty the active channel will be used.
    @overload
    def JumpToNcProgramLine(self, builder: IsvControlPanelBuilder, channelName: str, line: int) -> None:
        """
         Jump to nc program line in the specified channel
        """
        pass
    
    ##   @brief 
    ##             Machine Control Panel: Boot the virtual controller
    ##             Once the virtual controller has been successfully booted, the state remains as long as the part stays open or the machine setup is replaced.
    ##             To shut down the controller manually, @link NXOpen::SIM::IsvControlPanelBuilder::MachineControlShutdownVnck() NXOpen::SIM::IsvControlPanelBuilder::MachineControlShutdownVnck()@endlink  can be invoked.
    ##              
    ## 
    ##  
    ##             
    ##             The new behavior eliminates the wait required to boot the controller. However, it happens that the machine must be restarted. 
    ##             For this purpose @link NXOpen::SIM::IsvControlPanelBuilder::MachineControlShutdownVnck() NXOpen::SIM::IsvControlPanelBuilder::MachineControlShutdownVnck()@endlink  and @link NXOpen::SIM::IsvControlPanelBuilder::MachineControlBootVnck() NXOpen::SIM::IsvControlPanelBuilder::MachineControlBootVnck()@endlink  can be successively invoked.
    ##             
    ##         
    ##  @return success (bool): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    @staticmethod
    def MachineControlBootVnck(builder: IsvControlPanelBuilder) -> bool:
        """
          @brief 
                    Machine Control Panel: Boot the virtual controller
                    Once the virtual controller has been successfully booted, the state remains as long as the part stays open or the machine setup is replaced.
                    To shut down the controller manually, @link NXOpen::SIM::IsvControlPanelBuilder::MachineControlShutdownVnck() NXOpen::SIM::IsvControlPanelBuilder::MachineControlShutdownVnck()@endlink  can be invoked.
                     
        
         
                    
                    The new behavior eliminates the wait required to boot the controller. However, it happens that the machine must be restarted. 
                    For this purpose @link NXOpen::SIM::IsvControlPanelBuilder::MachineControlShutdownVnck() NXOpen::SIM::IsvControlPanelBuilder::MachineControlShutdownVnck()@endlink  and @link NXOpen::SIM::IsvControlPanelBuilder::MachineControlBootVnck() NXOpen::SIM::IsvControlPanelBuilder::MachineControlBootVnck()@endlink  can be successively invoked.
                    
                
         @return success (bool): .
        """
        pass
    
    ##  Machine Control Panel: Clear Alarms for all channels
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ## <param name="builder"> (@link IsvControlPanelBuilder NXOpen.SIM.IsvControlPanelBuilder@endlink) </param>
    @staticmethod
    @overload
    def MachineControlClearAlarm(self, builder: IsvControlPanelBuilder) -> None:
        """
         Machine Control Panel: Clear Alarms for all channels
        """
        pass
    
    ##  Machine Control Panel: Clear Alarms for specific channels
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ## <param name="builder"> (@link IsvControlPanelBuilder NXOpen.SIM.IsvControlPanelBuilder@endlink) </param>
    ## <param name="channels"> (List[str]) </param>
    @overload
    def MachineControlClearAlarm(self, builder: IsvControlPanelBuilder, channels: List[str]) -> None:
        """
         Machine Control Panel: Clear Alarms for specific channels
        """
        pass
    
    ##  Machine Control Panel: Activate Machine Dry Run
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  Enable or disable the dry run
    def MachineControlDryRun(builder: IsvControlPanelBuilder, enable: bool) -> None:
        """
         Machine Control Panel: Activate Machine Dry Run
        """
        pass
    
    ##  Machine Control Panel: Sets Machine Feed Rate Override
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The feed rate override value
    def MachineControlFeedRateOverride(builder: IsvControlPanelBuilder, value: int) -> None:
        """
         Machine Control Panel: Sets Machine Feed Rate Override
        """
        pass
    
    ##  Gets the Channel Names
    ##  @return channels (List[str]):  the names of available channel .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    @staticmethod
    def MachineControlGetChannels(builder: IsvControlPanelBuilder) -> List[str]:
        """
         Gets the Channel Names
         @return channels (List[str]):  the names of available channel .
        """
        pass
    
    ##  Gets the Machine Cycle Time
    ##  @return value (int):  The cycle time in ms.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    @staticmethod
    def MachineControlGetCycleTime(builder: IsvControlPanelBuilder) -> int:
        """
         Gets the Machine Cycle Time
         @return value (int):  The cycle time in ms.
        """
        pass
    
    ##  Machine Control Panel: Gets the Machine Feed Rate Override Maximum Value
    ##  @return value (int):  The feed rate override max value.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    @staticmethod
    def MachineControlGetFeedRateOverrideMaximumValue(builder: IsvControlPanelBuilder) -> int:
        """
         Machine Control Panel: Gets the Machine Feed Rate Override Maximum Value
         @return value (int):  The feed rate override max value.
        """
        pass
    
    ##  Read Variable e.g. VDI Variable, Machine Data
    ##  @return A tuple consisting of (success, variableValue, variableType). 
    ##  - success is: bool.
    ##  - variableValue is: str. The variable value.
    ##  - variableType is: str. The variable type: VDI_SWITCH, VDI_INTEGER, VDI_SINGLESTEP.

    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The channel name, NULL or empty means all channels
    @staticmethod
    def MachineControlReadVariable(builder: IsvControlPanelBuilder, channelName: str, variableName: str) -> Tuple[bool, str, str]:
        """
         Read Variable e.g. VDI Variable, Machine Data
         @return A tuple consisting of (success, variableValue, variableType). 
         - success is: bool.
         - variableValue is: str. The variable value.
         - variableType is: str. The variable type: VDI_SWITCH, VDI_INTEGER, VDI_SINGLESTEP.

        """
        pass
    
    ##  Machine Control Panel: Fast Reset Machine
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    @staticmethod
    def MachineControlResetMachine(builder: IsvControlPanelBuilder) -> None:
        """
         Machine Control Panel: Fast Reset Machine
        """
        pass
    
    ##  Machine Control Panel: Reset the Machine Data (SRAM) to the library Machine Data (SRAM)
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    @staticmethod
    def MachineControlResetMachineData(builder: IsvControlPanelBuilder) -> None:
        """
         Machine Control Panel: Reset the Machine Data (SRAM) to the library Machine Data (SRAM)
        """
        pass
    
    ##  Machine Control Panel: NC Reset for all channels
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ## <param name="builder"> (@link IsvControlPanelBuilder NXOpen.SIM.IsvControlPanelBuilder@endlink) </param>
    @staticmethod
    @overload
    def MachineControlResetNc(self, builder: IsvControlPanelBuilder) -> None:
        """
         Machine Control Panel: NC Reset for all channels
        """
        pass
    
    ##  Machine Control Panel: NC Reset for specific channels
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ## <param name="builder"> (@link IsvControlPanelBuilder NXOpen.SIM.IsvControlPanelBuilder@endlink) </param>
    ## <param name="channels"> (List[str]) </param>
    @overload
    def MachineControlResetNc(self, builder: IsvControlPanelBuilder, channels: List[str]) -> None:
        """
         Machine Control Panel: NC Reset for specific channels
        """
        pass
    
    ##  Machine Control Panel: Reset Part
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    @staticmethod
    def MachineControlResetPart(builder: IsvControlPanelBuilder) -> None:
        """
         Machine Control Panel: Reset Part
        """
        pass
    
    ##  Machine Control Panel: Save the Machine Data (SRAM)
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    @staticmethod
    def MachineControlSaveMachineData(builder: IsvControlPanelBuilder) -> None:
        """
         Machine Control Panel: Save the Machine Data (SRAM)
        """
        pass
    
    ##  Machine Control Panel: Show HMI
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    @staticmethod
    def MachineControlShowHmi(builder: IsvControlPanelBuilder) -> None:
        """
         Machine Control Panel: Show HMI
        """
        pass
    
    ##   @brief 
    ##             Machine Control Panel: Shut down the virtual controller
    ##             Used in conjunction with @link NXOpen::SIM::IsvControlPanelBuilder::MachineControlBootVnck() NXOpen::SIM::IsvControlPanelBuilder::MachineControlBootVnck()@endlink .
    ##              
    ## 
    ##            
    ##         
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    @staticmethod
    def MachineControlShutdownVnck(builder: IsvControlPanelBuilder) -> None:
        """
          @brief 
                    Machine Control Panel: Shut down the virtual controller
                    Used in conjunction with @link NXOpen::SIM::IsvControlPanelBuilder::MachineControlBootVnck() NXOpen::SIM::IsvControlPanelBuilder::MachineControlBootVnck()@endlink .
                     
        
                   
                
        """
        pass
    
    ##  Machine Control Panel: Activate Machine Single Block Mode
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  Enable or disable the single block mode
    def MachineControlSingleBlockMode(builder: IsvControlPanelBuilder, enable: bool) -> None:
        """
         Machine Control Panel: Activate Machine Single Block Mode
        """
        pass
    
    ##  Machine Control Panel: NC Start for all channels
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ## <param name="builder"> (@link IsvControlPanelBuilder NXOpen.SIM.IsvControlPanelBuilder@endlink) </param>
    @staticmethod
    @overload
    def MachineControlStartNc(self, builder: IsvControlPanelBuilder) -> None:
        """
         Machine Control Panel: NC Start for all channels
        """
        pass
    
    ##  Machine Control Panel: NC Start for specific channels
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ## <param name="builder"> (@link IsvControlPanelBuilder NXOpen.SIM.IsvControlPanelBuilder@endlink) </param>
    ## <param name="channels"> (List[str]) </param>
    @overload
    def MachineControlStartNc(self, builder: IsvControlPanelBuilder, channels: List[str]) -> None:
        """
         Machine Control Panel: NC Start for specific channels
        """
        pass
    
    ##  Machine Control Panel: NC Stop for all channels
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ## <param name="builder"> (@link IsvControlPanelBuilder NXOpen.SIM.IsvControlPanelBuilder@endlink) </param>
    @staticmethod
    @overload
    def MachineControlStopNc(self, builder: IsvControlPanelBuilder) -> None:
        """
         Machine Control Panel: NC Stop for all channels
        """
        pass
    
    ##  Machine Control Panel: NC Stop for specific channels
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ## <param name="builder"> (@link IsvControlPanelBuilder NXOpen.SIM.IsvControlPanelBuilder@endlink) </param>
    ## <param name="channels"> (List[str]) </param>
    @overload
    def MachineControlStopNc(self, builder: IsvControlPanelBuilder, channels: List[str]) -> None:
        """
         Machine Control Panel: NC Stop for specific channels
        """
        pass
    
    ##  Write Variable e.g. VDI Variable, Machine Data
    ##  @return success (bool): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The channel name, NULL or empty means all channels
    def MachineControlWriteVariable(builder: IsvControlPanelBuilder, channelName: str, variableName: str, variableValue: str, variableType: str) -> bool:
        """
         Write Variable e.g. VDI Variable, Machine Data
         @return success (bool): .
        """
        pass
    
    ##  Simulation Control Panel: Play Backward
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    @staticmethod
    def PlayBackward(builder: IsvControlPanelBuilder) -> None:
        """
         Simulation Control Panel: Play Backward
        """
        pass
    
    ##  Simulation Control Panel: Play Forward
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    @staticmethod
    def PlayForward(builder: IsvControlPanelBuilder) -> None:
        """
         Simulation Control Panel: Play Forward
        """
        pass
    
    ##  Play to Machine Time
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The machine time in hh:mm:ss.s format
    def PlayToMachineTime(builder: IsvControlPanelBuilder, machineTime: str) -> None:
        """
         Play to Machine Time
        """
        pass
    
    ##  Read simulation settings from xml file 
    ## 
    ##   <br>  Created in NX9.0.1  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ## 
    ## <param name="filename"> (str) </param>
    def ReadSettingsFromFile(builder: IsvControlPanelBuilder, filename: str) -> None:
        """
         Read simulation settings from xml file 
        """
        pass
    
    ##  Unregisters the IsInHistoryBufferChanged callback. 
    ##  @return result (bool):  .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  
    def RemoveIsInHistoryBuffer(builder: IsvControlPanelBuilder, handlerId: int) -> bool:
        """
         Unregisters the IsInHistoryBufferChanged callback. 
         @return result (bool):  .
        """
        pass
    
    ##  Unregisters the SimEnd callback. 
    ##  @return result (bool):  .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  
    def RemoveSimEnd(builder: IsvControlPanelBuilder, handlerId: int) -> bool:
        """
         Unregisters the SimEnd callback. 
         @return result (bool):  .
        """
        pass
    
    ##  Unregisters the SimStart callback. 
    ##  @return result (bool):  .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  
    def RemoveSimStart(builder: IsvControlPanelBuilder, handlerId: int) -> bool:
        """
         Unregisters the SimStart callback. 
         @return result (bool):  .
        """
        pass
    
    ##  Unregisters the SimStop callback. 
    ##  @return result (bool):  .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  
    def RemoveSimStop(builder: IsvControlPanelBuilder, handlerId: int) -> bool:
        """
         Unregisters the SimStop callback. 
         @return result (bool):  .
        """
        pass
    
    ##  Unregisters the VNC Status callback. 
    ##  @return result (bool):  .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  
    def RemoveVncStatus(builder: IsvControlPanelBuilder, handlerId: int) -> bool:
        """
         Unregisters the VNC Status callback. 
         @return result (bool):  .
        """
        pass
    
    ##  Simulation Control Panel: (Full) Reset Machine
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    @staticmethod
    def ResetMachine(builder: IsvControlPanelBuilder) -> None:
        """
         Simulation Control Panel: (Full) Reset Machine
        """
        pass
    
    ##  Save simulation settings to xml file 
    ## 
    ##   <br>  Created in NX9.0.1  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ## 
    ## <param name="filename"> (str) </param>
    def SaveSettingsToFile(builder: IsvControlPanelBuilder, filename: str) -> None:
        """
         Save simulation settings to xml file 
        """
        pass
    
    ##  Set execution cursor to nc program line in the specified channel
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The channel name. If this is NULL or empty the active channel will be used.
    def SetCurrentProgramLine(builder: IsvControlPanelBuilder, channelName: str, line: int) -> None:
        """
         Set execution cursor to nc program line in the specified channel
        """
        pass
    
    ##  Sets the show tool path 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The state
    def SetShowToolPath(builder: IsvControlPanelBuilder, state: bool) -> None:
        """
         Sets the show tool path 
        """
        pass
    
    ##  Sets the show tool trace 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The state
    def SetShowToolTrace(builder: IsvControlPanelBuilder, state: bool) -> None:
        """
         Sets the show tool trace 
        """
        pass
    
    ##  Sets the single step in Tool Path Based Simulation
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The single step type
    def SetSingleStep(builder: IsvControlPanelBuilder, type: IsvControlPanelBuilder.SingleStepType) -> None:
        """
         Sets the single step in Tool Path Based Simulation
        """
        pass
    
    ##  Sets the single step mode in Machine Code Simulation
    ## 
    ##   <br>  Created in NX10.0.2  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The single step mode type
    def SetSingleStepMode(builder: IsvControlPanelBuilder, type: IsvControlPanelBuilder.SingleStepModeType) -> None:
        """
         Sets the single step mode in Machine Code Simulation
        """
        pass
    
    ##  Simulation Control Panel: Simulation Speed
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The simulation speed
    def SetSpeed(builder: IsvControlPanelBuilder, simSpeed: int) -> None:
        """
         Simulation Control Panel: Simulation Speed
        """
        pass
    
    ##  Sets the visualization 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The visualization type
    def SetVisualization(builder: IsvControlPanelBuilder, type: IsvControlPanelBuilder.VisualizationType) -> None:
        """
         Sets the visualization 
        """
        pass
    
    ##  Show snapshot 
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The snapshot 
    def ShowSnapshot(data: IsvControlPanelBuilder, bRunToSimTime: bool, sourceComp: str, snapshot: Snapshot) -> None:
        """
         Show snapshot 
        """
        pass
    
    ##  Simulation Control Panel: Single Step Backward
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    @staticmethod
    def SingleStepBackward(builder: IsvControlPanelBuilder) -> None:
        """
         Simulation Control Panel: Single Step Backward
        """
        pass
    
    ##  Simulation Control Panel: Single Step Forward
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    @staticmethod
    def SingleStepForward(builder: IsvControlPanelBuilder) -> None:
        """
         Simulation Control Panel: Single Step Forward
        """
        pass
    
    ##  Simulation Control Panel: Step to Next Operation
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    @staticmethod
    def StepToNextOperation(builder: IsvControlPanelBuilder) -> None:
        """
         Simulation Control Panel: Step to Next Operation
        """
        pass
    
    ##  Simulation Control Panel: Step to Previous Operation
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    @staticmethod
    def StepToPreviousOperation(builder: IsvControlPanelBuilder) -> None:
        """
         Simulation Control Panel: Step to Previous Operation
        """
        pass
    
    ##  Simulation Control Panel: Stop the simulation
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    @staticmethod
    def Stop(builder: IsvControlPanelBuilder) -> None:
        """
         Simulation Control Panel: Stop the simulation
        """
        pass
    
import NXOpen
##   @brief  Represents the SimKimAxisBuilder class object  
## 
##     <br> Use the @link NXOpen::SIM::KinematicConfigurator NXOpen::SIM::KinematicConfigurator@endlink  class to create a KinematicAxisBuilder object.  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class KinematicAxisBuilder(NXOpen.Builder): 
    """ <summary> Represents the SimKimAxisBuilder class object </summary>  """


    ##  The axis direction type 
    ##  positive X-axis 
    class AxisDirectionType(Enum):
        """
        Members Include: <PositiveX> <NegativeX> <PositiveY> <NegativeY> <PositiveZ> <NegativeZ>
        """
        PositiveX: int
        NegativeX: int
        PositiveY: int
        NegativeY: int
        PositiveZ: int
        NegativeZ: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> KinematicAxisBuilder.AxisDirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The axis motions type 
    ##  linear NC-axis 
    class AxisMotionType(Enum):
        """
        Members Include: <LinearNcAxis> <RotaryNcAxis> <Linear> <Rotary> <RotaryUnlimitedNcAxis> <SpindleNcAxis> <RotaryUnlimited> <Spindle>
        """
        LinearNcAxis: int
        RotaryNcAxis: int
        Linear: int
        Rotary: int
        RotaryUnlimitedNcAxis: int
        SpindleNcAxis: int
        RotaryUnlimited: int
        Spindle: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> KinematicAxisBuilder.AxisMotionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) CoarsePrecision
    ##   the coarse precision.  
    ##   
    ##         This defines the exact stop precision used to determine if a target point has been
    ##         reached, so that the next NC-block can be executed.   
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## @return float
    @property
    def CoarsePrecision(self) -> float:
        """
        Getter for property: (float) CoarsePrecision
          the coarse precision.  
          
                This defines the exact stop precision used to determine if a target point has been
                reached, so that the next NC-block can be executed.   
         
        """
        pass
    
    ## Setter for property: (float) CoarsePrecision

    ##   the coarse precision.  
    ##   
    ##         This defines the exact stop precision used to determine if a target point has been
    ##         reached, so that the next NC-block can be executed.   
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    @CoarsePrecision.setter
    def CoarsePrecision(self, coarse: float):
        """
        Setter for property: (float) CoarsePrecision
          the coarse precision.  
          
                This defines the exact stop precision used to determine if a target point has been
                reached, so that the next NC-block can be executed.   
         
        """
        pass
    
    ## Getter for property: (@link KinematicAxisBuilder.AxisDirectionType NXOpen.SIM.KinematicAxisBuilder.AxisDirectionType@endlink) Direction
    ##   the axis direction   
    ##     
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return KinematicAxisBuilder.AxisDirectionType
    @property
    def Direction(self) -> KinematicAxisBuilder.AxisDirectionType:
        """
        Getter for property: (@link KinematicAxisBuilder.AxisDirectionType NXOpen.SIM.KinematicAxisBuilder.AxisDirectionType@endlink) Direction
          the axis direction   
            
         
        """
        pass
    
    ## Setter for property: (@link KinematicAxisBuilder.AxisDirectionType NXOpen.SIM.KinematicAxisBuilder.AxisDirectionType@endlink) Direction

    ##   the axis direction   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @Direction.setter
    def Direction(self, axisDir: KinematicAxisBuilder.AxisDirectionType):
        """
        Setter for property: (@link KinematicAxisBuilder.AxisDirectionType NXOpen.SIM.KinematicAxisBuilder.AxisDirectionType@endlink) Direction
          the axis direction   
            
         
        """
        pass
    
    ## Getter for property: (float) FinePrecision
    ##   the fine precision.  
    ##   
    ##         This defines the exact stop precision used to determine if a target point has been
    ##         reached, so that the next NC-block can be executed.   
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## @return float
    @property
    def FinePrecision(self) -> float:
        """
        Getter for property: (float) FinePrecision
          the fine precision.  
          
                This defines the exact stop precision used to determine if a target point has been
                reached, so that the next NC-block can be executed.   
         
        """
        pass
    
    ## Setter for property: (float) FinePrecision

    ##   the fine precision.  
    ##   
    ##         This defines the exact stop precision used to determine if a target point has been
    ##         reached, so that the next NC-block can be executed.   
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    @FinePrecision.setter
    def FinePrecision(self, fine: float):
        """
        Setter for property: (float) FinePrecision
          the fine precision.  
          
                This defines the exact stop precision used to determine if a target point has been
                reached, so that the next NC-block can be executed.   
         
        """
        pass
    
    ## Getter for property: (float) InitialValue
    ##   the initial value   
    ##     
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return float
    @property
    def InitialValue(self) -> float:
        """
        Getter for property: (float) InitialValue
          the initial value   
            
         
        """
        pass
    
    ## Setter for property: (float) InitialValue

    ##   the initial value   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @InitialValue.setter
    def InitialValue(self, initial: float):
        """
        Setter for property: (float) InitialValue
          the initial value   
            
         
        """
        pass
    
    ## Getter for property: (float) JerkLimit
    ##   the jerk limit.  
    ##   
    ##         The jerk limit value limits jumps in acceleration.   
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## @return float
    @property
    def JerkLimit(self) -> float:
        """
        Getter for property: (float) JerkLimit
          the jerk limit.  
          
                The jerk limit value limits jumps in acceleration.   
         
        """
        pass
    
    ## Setter for property: (float) JerkLimit

    ##   the jerk limit.  
    ##   
    ##         The jerk limit value limits jumps in acceleration.   
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    @JerkLimit.setter
    def JerkLimit(self, jerk: float):
        """
        Setter for property: (float) JerkLimit
          the jerk limit.  
          
                The jerk limit value limits jumps in acceleration.   
         
        """
        pass
    
    ## Getter for property: (float) JumpVelocity
    ##   the jump velocity.  
    ##   
    ##         The jump velocity define a lag time at the beginning of the motion.   
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## @return float
    @property
    def JumpVelocity(self) -> float:
        """
        Getter for property: (float) JumpVelocity
          the jump velocity.  
          
                The jump velocity define a lag time at the beginning of the motion.   
         
        """
        pass
    
    ## Setter for property: (float) JumpVelocity

    ##   the jump velocity.  
    ##   
    ##         The jump velocity define a lag time at the beginning of the motion.   
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    @JumpVelocity.setter
    def JumpVelocity(self, jump: float):
        """
        Setter for property: (float) JumpVelocity
          the jump velocity.  
          
                The jump velocity define a lag time at the beginning of the motion.   
         
        """
        pass
    
    ## Getter for property: (@link KinematicJunction NXOpen.SIM.KinematicJunction@endlink) Junction
    ##   the junction   
    ##     
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return KinematicJunction
    @property
    def Junction(self) -> KinematicJunction:
        """
        Getter for property: (@link KinematicJunction NXOpen.SIM.KinematicJunction@endlink) Junction
          the junction   
            
         
        """
        pass
    
    ## Setter for property: (@link KinematicJunction NXOpen.SIM.KinematicJunction@endlink) Junction

    ##   the junction   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @Junction.setter
    def Junction(self, jct: KinematicJunction):
        """
        Setter for property: (@link KinematicJunction NXOpen.SIM.KinematicJunction@endlink) Junction
          the junction   
            
         
        """
        pass
    
    ## Getter for property: (float) Kv
    ##   the kv.  
    ##   
    ##         the Kv-Factor is a parameter of the drives. It influences the dragging error (difference
    ##         between ideal motion profile and actual motion profile).   
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## @return float
    @property
    def Kv(self) -> float:
        """
        Getter for property: (float) Kv
          the kv.  
          
                the Kv-Factor is a parameter of the drives. It influences the dragging error (difference
                between ideal motion profile and actual motion profile).   
         
        """
        pass
    
    ## Setter for property: (float) Kv

    ##   the kv.  
    ##   
    ##         the Kv-Factor is a parameter of the drives. It influences the dragging error (difference
    ##         between ideal motion profile and actual motion profile).   
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    @Kv.setter
    def Kv(self, kv: float):
        """
        Setter for property: (float) Kv
          the kv.  
          
                the Kv-Factor is a parameter of the drives. It influences the dragging error (difference
                between ideal motion profile and actual motion profile).   
         
        """
        pass
    
    ## Getter for property: (bool) Limit
    ##   the axis limits flag
    ##          <br> This property is deprecated.  
    ##    Use @link SIM::KinematicAxisBuilder::AxisMotionType SIM::KinematicAxisBuilder::AxisMotionType@endlink  instead.
    ##          <br>    
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX9.0.3.  Use @link SIM::KinematicAxisBuilder::AxisMotionType SIM::KinematicAxisBuilder::AxisMotionType@endlink  instead.  <br> 

    ## @return bool
    @property
    def Limit(self) -> bool:
        """
        Getter for property: (bool) Limit
          the axis limits flag
                 <br> This property is deprecated.  
           Use @link SIM::KinematicAxisBuilder::AxisMotionType SIM::KinematicAxisBuilder::AxisMotionType@endlink  instead.
                 <br>    
         
        """
        pass
    
    ## Setter for property: (bool) Limit

    ##   the axis limits flag
    ##          <br> This property is deprecated.  
    ##    Use @link SIM::KinematicAxisBuilder::AxisMotionType SIM::KinematicAxisBuilder::AxisMotionType@endlink  instead.
    ##          <br>    
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX9.0.3.  Use @link SIM::KinematicAxisBuilder::AxisMotionType SIM::KinematicAxisBuilder::AxisMotionType@endlink  instead.  <br> 

    @Limit.setter
    def Limit(self, result: bool):
        """
        Setter for property: (bool) Limit
          the axis limits flag
                 <br> This property is deprecated.  
           Use @link SIM::KinematicAxisBuilder::AxisMotionType SIM::KinematicAxisBuilder::AxisMotionType@endlink  instead.
                 <br>    
         
        """
        pass
    
    ## Getter for property: (float) LowerLimit
    ##   the lower limit   
    ##     
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return float
    @property
    def LowerLimit(self) -> float:
        """
        Getter for property: (float) LowerLimit
          the lower limit   
            
         
        """
        pass
    
    ## Setter for property: (float) LowerLimit

    ##   the lower limit   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @LowerLimit.setter
    def LowerLimit(self, lower: float):
        """
        Setter for property: (float) LowerLimit
          the lower limit   
            
         
        """
        pass
    
    ## Getter for property: (float) LowerSoftLimit
    ##   the lower soft limit.  
    ##   
    ##         The soft limit on the real machine is checked by the controller to avoid that the machine
    ##         travels into the mechanical stop (Hard Limit) with full speed (prevent damage)   
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## @return float
    @property
    def LowerSoftLimit(self) -> float:
        """
        Getter for property: (float) LowerSoftLimit
          the lower soft limit.  
          
                The soft limit on the real machine is checked by the controller to avoid that the machine
                travels into the mechanical stop (Hard Limit) with full speed (prevent damage)   
         
        """
        pass
    
    ## Setter for property: (float) LowerSoftLimit

    ##   the lower soft limit.  
    ##   
    ##         The soft limit on the real machine is checked by the controller to avoid that the machine
    ##         travels into the mechanical stop (Hard Limit) with full speed (prevent damage)   
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    @LowerSoftLimit.setter
    def LowerSoftLimit(self, lower: float):
        """
        Setter for property: (float) LowerSoftLimit
          the lower soft limit.  
          
                The soft limit on the real machine is checked by the controller to avoid that the machine
                travels into the mechanical stop (Hard Limit) with full speed (prevent damage)   
         
        """
        pass
    
    ## Getter for property: (float) MaxAcceleration
    ##   the max acceleration.  
    ##   
    ##         The maximum acceleration defines how fast the axis can accelerate.   
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## @return float
    @property
    def MaxAcceleration(self) -> float:
        """
        Getter for property: (float) MaxAcceleration
          the max acceleration.  
          
                The maximum acceleration defines how fast the axis can accelerate.   
         
        """
        pass
    
    ## Setter for property: (float) MaxAcceleration

    ##   the max acceleration.  
    ##   
    ##         The maximum acceleration defines how fast the axis can accelerate.   
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    @MaxAcceleration.setter
    def MaxAcceleration(self, max: float):
        """
        Setter for property: (float) MaxAcceleration
          the max acceleration.  
          
                The maximum acceleration defines how fast the axis can accelerate.   
         
        """
        pass
    
    ## Getter for property: (float) MaxDeceleration
    ##   the max deceleration.  
    ##   
    ##         The maximum deceleration defines how fast the axis can decelerate.   
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## @return float
    @property
    def MaxDeceleration(self) -> float:
        """
        Getter for property: (float) MaxDeceleration
          the max deceleration.  
          
                The maximum deceleration defines how fast the axis can decelerate.   
         
        """
        pass
    
    ## Setter for property: (float) MaxDeceleration

    ##   the max deceleration.  
    ##   
    ##         The maximum deceleration defines how fast the axis can decelerate.   
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    @MaxDeceleration.setter
    def MaxDeceleration(self, max: float):
        """
        Setter for property: (float) MaxDeceleration
          the max deceleration.  
          
                The maximum deceleration defines how fast the axis can decelerate.   
         
        """
        pass
    
    ## Getter for property: (float) MaximumVelocity
    ##   the maximum velocity   
    ##     
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return float
    @property
    def MaximumVelocity(self) -> float:
        """
        Getter for property: (float) MaximumVelocity
          the maximum velocity   
            
         
        """
        pass
    
    ## Setter for property: (float) MaximumVelocity

    ##   the maximum velocity   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @MaximumVelocity.setter
    def MaximumVelocity(self, velocity: float):
        """
        Setter for property: (float) MaximumVelocity
          the maximum velocity   
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##   the kinematic axis's name   
    ##     
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
          the kinematic axis's name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##   the kinematic axis's name   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
          the kinematic axis's name   
            
         
        """
        pass
    
    ## Getter for property: (int) Number
    ##   the kinematic axis's number.  
    ##   
    ##         The axis number is used in cases where an axis is programmed through a number 
    ##         instead of through an address (e.g. on Siemens 840D: AX1=10 instead of X10).  
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## @return int
    @property
    def Number(self) -> int:
        """
        Getter for property: (int) Number
          the kinematic axis's number.  
          
                The axis number is used in cases where an axis is programmed through a number 
                instead of through an address (e.g. on Siemens 840D: AX1=10 instead of X10).  
         
        """
        pass
    
    ## Setter for property: (int) Number

    ##   the kinematic axis's number.  
    ##   
    ##         The axis number is used in cases where an axis is programmed through a number 
    ##         instead of through an address (e.g. on Siemens 840D: AX1=10 instead of X10).  
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    @Number.setter
    def Number(self, number: int):
        """
        Setter for property: (int) Number
          the kinematic axis's number.  
          
                The axis number is used in cases where an axis is programmed through a number 
                instead of through an address (e.g. on Siemens 840D: AX1=10 instead of X10).  
         
        """
        pass
    
    ## Getter for property: (@link KinematicAxisBuilder.AxisMotionType NXOpen.SIM.KinematicAxisBuilder.AxisMotionType@endlink) Type
    ##   the axis motion   
    ##     
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return KinematicAxisBuilder.AxisMotionType
    @property
    def Type(self) -> KinematicAxisBuilder.AxisMotionType:
        """
        Getter for property: (@link KinematicAxisBuilder.AxisMotionType NXOpen.SIM.KinematicAxisBuilder.AxisMotionType@endlink) Type
          the axis motion   
            
         
        """
        pass
    
    ## Setter for property: (@link KinematicAxisBuilder.AxisMotionType NXOpen.SIM.KinematicAxisBuilder.AxisMotionType@endlink) Type

    ##   the axis motion   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @Type.setter
    def Type(self, type: KinematicAxisBuilder.AxisMotionType):
        """
        Setter for property: (@link KinematicAxisBuilder.AxisMotionType NXOpen.SIM.KinematicAxisBuilder.AxisMotionType@endlink) Type
          the axis motion   
            
         
        """
        pass
    
    ## Getter for property: (float) UpperLimit
    ##   the upper limit   
    ##     
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return float
    @property
    def UpperLimit(self) -> float:
        """
        Getter for property: (float) UpperLimit
          the upper limit   
            
         
        """
        pass
    
    ## Setter for property: (float) UpperLimit

    ##   the upper limit   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @UpperLimit.setter
    def UpperLimit(self, upper: float):
        """
        Setter for property: (float) UpperLimit
          the upper limit   
            
         
        """
        pass
    
    ## Getter for property: (float) UpperSoftLimit
    ##   the upper soft limit.  
    ##   
    ##         The soft limit on the real machine is checked by the controller to avoid that the machine
    ##         travels into the mechanical stop (Hard Limit) with full speed (prevent damage)   
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## @return float
    @property
    def UpperSoftLimit(self) -> float:
        """
        Getter for property: (float) UpperSoftLimit
          the upper soft limit.  
          
                The soft limit on the real machine is checked by the controller to avoid that the machine
                travels into the mechanical stop (Hard Limit) with full speed (prevent damage)   
         
        """
        pass
    
    ## Setter for property: (float) UpperSoftLimit

    ##   the upper soft limit.  
    ##   
    ##         The soft limit on the real machine is checked by the controller to avoid that the machine
    ##         travels into the mechanical stop (Hard Limit) with full speed (prevent damage)   
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    @UpperSoftLimit.setter
    def UpperSoftLimit(self, upper: float):
        """
        Setter for property: (float) UpperSoftLimit
          the upper soft limit.  
          
                The soft limit on the real machine is checked by the controller to avoid that the machine
                travels into the mechanical stop (Hard Limit) with full speed (prevent damage)   
         
        """
        pass
    
import NXOpen
##   @brief  Represents the SimKimAxis class object  
## 
##     <br> Use the @link NXOpen::SIM::KinematicAxisBuilder NXOpen::SIM::KinematicAxisBuilder@endlink  class to create a KinematicAxis object.  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class KinematicAxis(NXOpen.NXObject): 
    """ <summary> Represents the SimKimAxis class object </summary>  """
    pass


import NXOpen
##  This class is used for define kinematic chains.
##         Calling @link Builder::Commit Builder::Commit@endlink  on this builder will return NULL.
##      <br> To create a new instance of this class, use @link NXOpen::SIM::KinematicConfigurator::DefineKinematicChains  NXOpen::SIM::KinematicConfigurator::DefineKinematicChains @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class KinematicChainConfiguration(NXOpen.Builder): 
    """ This class is used for define kinematic chains.
        Calling <ja_method>Builder.Commit</ja_method> on this builder will return <ja_NULL>.
    """


    ## Getter for property: (@link KinematicChainList NXOpen.SIM.KinematicChainList@endlink) List
    ##   the kinematic chain list   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return KinematicChainList
    @property
    def List(self) -> KinematicChainList:
        """
        Getter for property: (@link KinematicChainList NXOpen.SIM.KinematicChainList@endlink) List
          the kinematic chain list   
            
         
        """
        pass
    
import NXOpen
##  Represents a list of objects. <br> To create a new instance of this class, use @link NXOpen::Part::CreateObjectList  NXOpen::Part::CreateObjectList @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class KinematicChainList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""


    ## Getter for property: (int) Length
    ##   the length of the list   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
          the length of the list   
            
         
        """
        pass
    
    ##  Appends a set of objects to the list
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ##  items to append 
    @overload
    def Append(self, object_list: KinematicChainList, objects: List[KinematicChain]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    
    ##  Appends an object to the list
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  item to append 
    @overload
    def Append(self, object_list: KinematicChainList, objectValue: KinematicChain) -> None:
        """
         Appends an object to the list
            
        """
        pass
    
    ##  Clears the entire list without deleting the objects.  The caller is responsible for 
    ##         accounting for these objects.  If they are not used or deleted by the time the part is 
    ##         closed (in other words, leaked) an error will occur 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Clear(object_list: KinematicChainList) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    
    ##  Deletes the item at the index specified.  The size of the list does
    ##     *   not change, but the item at this index is set to NULL.
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ##  index of item to be deleted 
    def ClearIndex(object_list: KinematicChainList, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
            *   not change, but the item at this index is set to NULL.
            
        """
        pass
    
    ##  Clears the entire list 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  whether to delete the objects when removing them 
    def Clear(object_list: KinematicChainList, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    
    ##  Erases the object from the list, but does not delete the object.
    ##         The list is shifted so that there isn't a null where the object used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  index of item to be removed from the list 
    @overload
    def Erase(self, object_list: KinematicChainList, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    
    ##  Erases the object at the given position from the list.
    ##         The list is shifted so that there isn't a null where the object used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  index of item to be removed from the list 
    @overload
    def Erase(self, object_list: KinematicChainList, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    
    ##  Erases the object from the list, but does not delete the object.
    ##         The list is shifted so that there isn't a null where the object used to exist. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  object to be removed from the list 
    @overload
    def Erase(self, object_list: KinematicChainList, obj: KinematicChain) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    
    ##  Erases the object from the list.
    ##         The list is shifted so that there isn't a null where the object used to exist. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  object to be removed from the list 
    @overload
    def Erase(self, object_list: KinematicChainList, obj: KinematicChain, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    
    ##  Finds the index where the input object appears.  If it does not appear,
    ##     *   -1 is returned.
    ##     
    ##  @return index (int):  index of input object, -1 if not on list .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ##  Object to find index for 
    def FindIndex(object_list: KinematicChainList, obj: KinematicChain) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
            *   -1 is returned.
            
         @return index (int):  index of input object, -1 if not on list .
        """
        pass
    
    ##  Returns the object at the input index.  May be NULL.
    ##     
    ##  @return obj (@link KinematicChain NXOpen.SIM.KinematicChain@endlink):  object found at input index .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ##  index of object to return 
    def FindItem(object_list: KinematicChainList, index: int) -> KinematicChain:
        """
         Returns the object at the input index.  May be NULL.
            
         @return obj (@link KinematicChain NXOpen.SIM.KinematicChain@endlink):  object found at input index .
        """
        pass
    
    ##  Gets the contents of the entire list 
    ##  @return objects (@link KinematicChain List[NXOpen.SIM.KinematicChain]@endlink):  The list contents .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetContents(object_list: KinematicChainList) -> List[KinematicChain]:
        """
         Gets the contents of the entire list 
         @return objects (@link KinematicChain List[NXOpen.SIM.KinematicChain]@endlink):  The list contents .
        """
        pass
    
    ##  Inserts an object at the specified location 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  location at which to insert the object 
    def Insert(object_list: KinematicChainList, location: int, objectValue: KinematicChain) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    
    ##  Move object at the specified location to the bottom of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  location of the item 
    def MoveToBottom(object_list: KinematicChainList, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    
    ##  Move object at the specified location to the top of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  location of the item 
    def MoveToTop(object_list: KinematicChainList, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    
    ##  Sets the contents of the entire list. This overwrites the previous contents of this list, 
    ##         but does not delete any objects that were originally on the list.
    ##      
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  The list contents 
    def SetContents(object_list: KinematicChainList, objects: List[KinematicChain]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    
    ##  Exchanges the position of two objects inside the list.
    ##         The first object is placed where the second used to be,
    ##         and second object where the first used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  location of the first item 
    @overload
    def Swap(self, object_list: KinematicChainList, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
    ##  Exchanges the position of two objects inside the list.
    ##         The first object is placed where the second used to be,
    ##         and second object where the first used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  first item 
    @overload
    def Swap(self, object_list: KinematicChainList, object1: KinematicChain, object2: KinematicChain) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
import NXOpen
##  This class is used for add kinematic chain to the list.
##         Calling @link Builder::Commit Builder::Commit@endlink  on this builder will only return NULL.
##      <br> To create a new instance of this class, use @link NXOpen::SIM::KinematicConfigurator::CreateKinematicChain  NXOpen::SIM::KinematicConfigurator::CreateKinematicChain @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class KinematicChain(NXOpen.Builder): 
    """ This class is used for add kinematic chain to the list.
        Calling <ja_method>Builder.Commit</ja_method> on this builder will only return <ja_NULL>.
    """


    ##  Represents the coordinate plane type 
    ##  ZX 
    class CoordinatePlaneTypes(Enum):
        """
        Members Include: <Zx> <Xy>
        """
        Zx: int
        Xy: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> KinematicChain.CoordinatePlaneTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The preferred solution type 
    ##  Invalid solution 
    class PreferredSolutionType(Enum):
        """
        Members Include: <Invalid> <Shortest> <RangeOne> <RangeTwo>
        """
        Invalid: int
        Shortest: int
        RangeOne: int
        RangeTwo: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> KinematicChain.PreferredSolutionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the kinematic chain type 
    ##  Unknown 
    class Types(Enum):
        """
        Members Include: <Unknown> <Milling> <Turning> <Polar> <Robot>
        """
        Unknown: int
        Milling: int
        Turning: int
        Polar: int
        Robot: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> KinematicChain.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) Axial
    ##   the axial axis of the kinematic chain   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def Axial(self) -> str:
        """
        Getter for property: (str) Axial
          the axial axis of the kinematic chain   
            
         
        """
        pass
    
    ## Setter for property: (str) Axial

    ##   the axial axis of the kinematic chain   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Axial.setter
    def Axial(self, axis: str):
        """
        Setter for property: (str) Axial
          the axial axis of the kinematic chain   
            
         
        """
        pass
    
    ## Getter for property: (str) CoordinateAxes
    ##   the coordinate axes name of the kinematic chain   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def CoordinateAxes(self) -> str:
        """
        Getter for property: (str) CoordinateAxes
          the coordinate axes name of the kinematic chain   
            
         
        """
        pass
    
    ## Setter for property: (str) CoordinateAxes

    ##   the coordinate axes name of the kinematic chain   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @CoordinateAxes.setter
    def CoordinateAxes(self, axis: str):
        """
        Setter for property: (str) CoordinateAxes
          the coordinate axes name of the kinematic chain   
            
         
        """
        pass
    
    ## Getter for property: (@link KinematicChain.CoordinatePlaneTypes NXOpen.SIM.KinematicChain.CoordinatePlaneTypes@endlink) CoordinatePlane
    ##   the coordinate plane type of the kinematic chain   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return KinematicChain.CoordinatePlaneTypes
    @property
    def CoordinatePlane(self) -> KinematicChain.CoordinatePlaneTypes:
        """
        Getter for property: (@link KinematicChain.CoordinatePlaneTypes NXOpen.SIM.KinematicChain.CoordinatePlaneTypes@endlink) CoordinatePlane
          the coordinate plane type of the kinematic chain   
            
         
        """
        pass
    
    ## Setter for property: (@link KinematicChain.CoordinatePlaneTypes NXOpen.SIM.KinematicChain.CoordinatePlaneTypes@endlink) CoordinatePlane

    ##   the coordinate plane type of the kinematic chain   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @CoordinatePlane.setter
    def CoordinatePlane(self, type: KinematicChain.CoordinatePlaneTypes):
        """
        Setter for property: (@link KinematicChain.CoordinatePlaneTypes NXOpen.SIM.KinematicChain.CoordinatePlaneTypes@endlink) CoordinatePlane
          the coordinate plane type of the kinematic chain   
            
         
        """
        pass
    
    ## Getter for property: (str) Device
    ##   the device component of the kinematic chain   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def Device(self) -> str:
        """
        Getter for property: (str) Device
          the device component of the kinematic chain   
            
         
        """
        pass
    
    ## Setter for property: (str) Device

    ##   the device component of the kinematic chain   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Device.setter
    def Device(self, device: str):
        """
        Setter for property: (str) Device
          the device component of the kinematic chain   
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##   the name of the kinematic chain   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
          the name of the kinematic chain   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##   the name of the kinematic chain   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
          the name of the kinematic chain   
            
         
        """
        pass
    
    ## Getter for property: (str) Radial
    ##   the radial axis of the kinematic chain   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def Radial(self) -> str:
        """
        Getter for property: (str) Radial
          the radial axis of the kinematic chain   
            
         
        """
        pass
    
    ## Setter for property: (str) Radial

    ##   the radial axis of the kinematic chain   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Radial.setter
    def Radial(self, axis: str):
        """
        Setter for property: (str) Radial
          the radial axis of the kinematic chain   
            
         
        """
        pass
    
    ## Getter for property: (str) ReferencePointJunction
    ##   the reference point junction of the kinematic chain   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def ReferencePointJunction(self) -> str:
        """
        Getter for property: (str) ReferencePointJunction
          the reference point junction of the kinematic chain   
            
         
        """
        pass
    
    ## Setter for property: (str) ReferencePointJunction

    ##   the reference point junction of the kinematic chain   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ReferencePointJunction.setter
    def ReferencePointJunction(self, refPointJunction: str):
        """
        Setter for property: (str) ReferencePointJunction
          the reference point junction of the kinematic chain   
            
         
        """
        pass
    
    ## Getter for property: (str) Rotary1
    ##   the rotary1 axis of the kinematic chain   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def Rotary1(self) -> str:
        """
        Getter for property: (str) Rotary1
          the rotary1 axis of the kinematic chain   
            
         
        """
        pass
    
    ## Setter for property: (str) Rotary1

    ##   the rotary1 axis of the kinematic chain   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Rotary1.setter
    def Rotary1(self, rotary1: str):
        """
        Setter for property: (str) Rotary1
          the rotary1 axis of the kinematic chain   
            
         
        """
        pass
    
    ## Getter for property: (str) Rotary2
    ##   the rotary2 axis of the kinematic chain   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def Rotary2(self) -> str:
        """
        Getter for property: (str) Rotary2
          the rotary2 axis of the kinematic chain   
            
         
        """
        pass
    
    ## Setter for property: (str) Rotary2

    ##   the rotary2 axis of the kinematic chain   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Rotary2.setter
    def Rotary2(self, rotary2: str):
        """
        Setter for property: (str) Rotary2
          the rotary2 axis of the kinematic chain   
            
         
        """
        pass
    
    ## Getter for property: (str) Rotary3
    ##   the rotary3 axis of the kinematic chain   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def Rotary3(self) -> str:
        """
        Getter for property: (str) Rotary3
          the rotary3 axis of the kinematic chain   
            
         
        """
        pass
    
    ## Setter for property: (str) Rotary3

    ##   the rotary3 axis of the kinematic chain   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Rotary3.setter
    def Rotary3(self, rotary3: str):
        """
        Setter for property: (str) Rotary3
          the rotary3 axis of the kinematic chain   
            
         
        """
        pass
    
    ## Getter for property: (str) Rotary4
    ##   the rotary4 axis of the kinematic chain   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def Rotary4(self) -> str:
        """
        Getter for property: (str) Rotary4
          the rotary4 axis of the kinematic chain   
            
         
        """
        pass
    
    ## Setter for property: (str) Rotary4

    ##   the rotary4 axis of the kinematic chain   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Rotary4.setter
    def Rotary4(self, rotary4: str):
        """
        Setter for property: (str) Rotary4
          the rotary4 axis of the kinematic chain   
            
         
        """
        pass
    
    ## Getter for property: (str) Rotary5
    ##   the rotary5 axis of the kinematic chain   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def Rotary5(self) -> str:
        """
        Getter for property: (str) Rotary5
          the rotary5 axis of the kinematic chain   
            
         
        """
        pass
    
    ## Setter for property: (str) Rotary5

    ##   the rotary5 axis of the kinematic chain   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Rotary5.setter
    def Rotary5(self, rotary5: str):
        """
        Setter for property: (str) Rotary5
          the rotary5 axis of the kinematic chain   
            
         
        """
        pass
    
    ## Getter for property: (str) Rotary6
    ##   the rotary6 axis of the kinematic chain   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def Rotary6(self) -> str:
        """
        Getter for property: (str) Rotary6
          the rotary6 axis of the kinematic chain   
            
         
        """
        pass
    
    ## Setter for property: (str) Rotary6

    ##   the rotary6 axis of the kinematic chain   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Rotary6.setter
    def Rotary6(self, rotary6: str):
        """
        Setter for property: (str) Rotary6
          the rotary6 axis of the kinematic chain   
            
         
        """
        pass
    
    ## Getter for property: (str) Setup
    ##   the setup component of the kinematic chain   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def Setup(self) -> str:
        """
        Getter for property: (str) Setup
          the setup component of the kinematic chain   
            
         
        """
        pass
    
    ## Setter for property: (str) Setup

    ##   the setup component of the kinematic chain   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Setup.setter
    def Setup(self, setup: str):
        """
        Setter for property: (str) Setup
          the setup component of the kinematic chain   
            
         
        """
        pass
    
    ## Getter for property: (@link KinematicChain.Types NXOpen.SIM.KinematicChain.Types@endlink) Type
    ##   the type of the kinematic chain   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return KinematicChain.Types
    @property
    def Type(self) -> KinematicChain.Types:
        """
        Getter for property: (@link KinematicChain.Types NXOpen.SIM.KinematicChain.Types@endlink) Type
          the type of the kinematic chain   
            
         
        """
        pass
    
    ## Setter for property: (@link KinematicChain.Types NXOpen.SIM.KinematicChain.Types@endlink) Type

    ##   the type of the kinematic chain   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Type.setter
    def Type(self, chainType: KinematicChain.Types):
        """
        Setter for property: (@link KinematicChain.Types NXOpen.SIM.KinematicChain.Types@endlink) Type
          the type of the kinematic chain   
            
         
        """
        pass
    
    ## Getter for property: (str) X
    ##   the X axis of the kinematic chain   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def X(self) -> str:
        """
        Getter for property: (str) X
          the X axis of the kinematic chain   
            
         
        """
        pass
    
    ## Setter for property: (str) X

    ##   the X axis of the kinematic chain   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @X.setter
    def X(self, xAxis: str):
        """
        Setter for property: (str) X
          the X axis of the kinematic chain   
            
         
        """
        pass
    
    ## Getter for property: (str) Y
    ##   the Y axis of the kinematic chain   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def Y(self) -> str:
        """
        Getter for property: (str) Y
          the Y axis of the kinematic chain   
            
         
        """
        pass
    
    ## Setter for property: (str) Y

    ##   the Y axis of the kinematic chain   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Y.setter
    def Y(self, yAxis: str):
        """
        Setter for property: (str) Y
          the Y axis of the kinematic chain   
            
         
        """
        pass
    
    ## Getter for property: (str) Z
    ##   the Z axis of the kinematic chain   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def Z(self) -> str:
        """
        Getter for property: (str) Z
          the Z axis of the kinematic chain   
            
         
        """
        pass
    
    ## Setter for property: (str) Z

    ##   the Z axis of the kinematic chain   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Z.setter
    def Z(self, zAxis: str):
        """
        Setter for property: (str) Z
          the Z axis of the kinematic chain   
            
         
        """
        pass
    
import NXOpen
##  Represents a list of objects. <br> To create a new instance of this class, use @link NXOpen::Part::CreateObjectList  NXOpen::Part::CreateObjectList @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class KinematicChannelBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""


    ## Getter for property: (int) Length
    ##   the length of the list   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
          the length of the list   
            
         
        """
        pass
    
    ##  Appends a set of objects to the list
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ##  items to append 
    @overload
    def Append(self, object_list: KinematicChannelBuilderList, objects: List[KinematicChannelBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    
    ##  Appends an object to the list
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  item to append 
    @overload
    def Append(self, object_list: KinematicChannelBuilderList, objectValue: KinematicChannelBuilder) -> None:
        """
         Appends an object to the list
            
        """
        pass
    
    ##  Clears the entire list without deleting the objects.  The caller is responsible for 
    ##         accounting for these objects.  If they are not used or deleted by the time the part is 
    ##         closed (in other words, leaked) an error will occur 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Clear(object_list: KinematicChannelBuilderList) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    
    ##  Deletes the item at the index specified.  The size of the list does
    ##     *   not change, but the item at this index is set to NULL.
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ##  index of item to be deleted 
    def ClearIndex(object_list: KinematicChannelBuilderList, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
            *   not change, but the item at this index is set to NULL.
            
        """
        pass
    
    ##  Clears the entire list 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  whether to delete the objects when removing them 
    def Clear(object_list: KinematicChannelBuilderList, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    
    ##  Erases the object from the list, but does not delete the object.
    ##         The list is shifted so that there isn't a null where the object used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  index of item to be removed from the list 
    @overload
    def Erase(self, object_list: KinematicChannelBuilderList, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    
    ##  Erases the object at the given position from the list.
    ##         The list is shifted so that there isn't a null where the object used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  index of item to be removed from the list 
    @overload
    def Erase(self, object_list: KinematicChannelBuilderList, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    
    ##  Erases the object from the list, but does not delete the object.
    ##         The list is shifted so that there isn't a null where the object used to exist. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  object to be removed from the list 
    @overload
    def Erase(self, object_list: KinematicChannelBuilderList, obj: KinematicChannelBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    
    ##  Erases the object from the list.
    ##         The list is shifted so that there isn't a null where the object used to exist. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  object to be removed from the list 
    @overload
    def Erase(self, object_list: KinematicChannelBuilderList, obj: KinematicChannelBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    
    ##  Finds the index where the input object appears.  If it does not appear,
    ##     *   -1 is returned.
    ##     
    ##  @return index (int):  index of input object, -1 if not on list .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ##  Object to find index for 
    def FindIndex(object_list: KinematicChannelBuilderList, obj: KinematicChannelBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
            *   -1 is returned.
            
         @return index (int):  index of input object, -1 if not on list .
        """
        pass
    
    ##  Returns the object at the input index.  May be NULL.
    ##     
    ##  @return obj (@link KinematicChannelBuilder NXOpen.SIM.KinematicChannelBuilder@endlink):  object found at input index .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ##  index of object to return 
    def FindItem(object_list: KinematicChannelBuilderList, index: int) -> KinematicChannelBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         @return obj (@link KinematicChannelBuilder NXOpen.SIM.KinematicChannelBuilder@endlink):  object found at input index .
        """
        pass
    
    ##  Gets the contents of the entire list 
    ##  @return objects (@link KinematicChannelBuilder List[NXOpen.SIM.KinematicChannelBuilder]@endlink):  The list contents .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetContents(object_list: KinematicChannelBuilderList) -> List[KinematicChannelBuilder]:
        """
         Gets the contents of the entire list 
         @return objects (@link KinematicChannelBuilder List[NXOpen.SIM.KinematicChannelBuilder]@endlink):  The list contents .
        """
        pass
    
    ##  Inserts an object at the specified location 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  location at which to insert the object 
    def Insert(object_list: KinematicChannelBuilderList, location: int, objectValue: KinematicChannelBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    
    ##  Move object at the specified location to the bottom of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  location of the item 
    def MoveToBottom(object_list: KinematicChannelBuilderList, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    
    ##  Move object at the specified location to the top of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  location of the item 
    def MoveToTop(object_list: KinematicChannelBuilderList, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    
    ##  Sets the contents of the entire list. This overwrites the previous contents of this list, 
    ##         but does not delete any objects that were originally on the list.
    ##      
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  The list contents 
    def SetContents(object_list: KinematicChannelBuilderList, objects: List[KinematicChannelBuilder]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    
    ##  Exchanges the position of two objects inside the list.
    ##         The first object is placed where the second used to be,
    ##         and second object where the first used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  location of the first item 
    @overload
    def Swap(self, object_list: KinematicChannelBuilderList, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
    ##  Exchanges the position of two objects inside the list.
    ##         The first object is placed where the second used to be,
    ##         and second object where the first used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  first item 
    @overload
    def Swap(self, object_list: KinematicChannelBuilderList, object1: KinematicChannelBuilder, object2: KinematicChannelBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  This class is used for add kinematic channel to the channel configuratation list.
##         Calling @link Builder::Commit Builder::Commit@endlink  on this builder will only return NULL.
##      <br> To create a new instance of this class, use @link NXOpen::SIM::KinematicConfigurator::CreateKinematicChannelBuilder  NXOpen::SIM::KinematicConfigurator::CreateKinematicChannelBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.3  <br> 

class KinematicChannelBuilder(NXOpen.TaggedObject): 
    """ This class is used for add kinematic channel to the channel configuratation list.
        Calling <ja_method>Builder.Commit</ja_method> on this builder will only return <ja_NULL>.
    """


    ## Getter for property: (str) GeometryAxisX
    ##   the geometry X axis of the channel   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## @return str
    @property
    def GeometryAxisX(self) -> str:
        """
        Getter for property: (str) GeometryAxisX
          the geometry X axis of the channel   
            
         
        """
        pass
    
    ## Setter for property: (str) GeometryAxisX

    ##   the geometry X axis of the channel   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    @GeometryAxisX.setter
    def GeometryAxisX(self, xAxis: str):
        """
        Setter for property: (str) GeometryAxisX
          the geometry X axis of the channel   
            
         
        """
        pass
    
    ## Getter for property: (str) GeometryAxisY
    ##   the geometry Y axis of the channel   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## @return str
    @property
    def GeometryAxisY(self) -> str:
        """
        Getter for property: (str) GeometryAxisY
          the geometry Y axis of the channel   
            
         
        """
        pass
    
    ## Setter for property: (str) GeometryAxisY

    ##   the geometry Y axis of the channel   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    @GeometryAxisY.setter
    def GeometryAxisY(self, yAxis: str):
        """
        Setter for property: (str) GeometryAxisY
          the geometry Y axis of the channel   
            
         
        """
        pass
    
    ## Getter for property: (str) GeometryAxisZ
    ##   the geometry Z axis of the channel   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## @return str
    @property
    def GeometryAxisZ(self) -> str:
        """
        Getter for property: (str) GeometryAxisZ
          the geometry Z axis of the channel   
            
         
        """
        pass
    
    ## Setter for property: (str) GeometryAxisZ

    ##   the geometry Z axis of the channel   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    @GeometryAxisZ.setter
    def GeometryAxisZ(self, zAxis: str):
        """
        Setter for property: (str) GeometryAxisZ
          the geometry Z axis of the channel   
            
         
        """
        pass
    
    ## Getter for property: (str) MainSpindle
    ##   the main spindle of the channel   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## @return str
    @property
    def MainSpindle(self) -> str:
        """
        Getter for property: (str) MainSpindle
          the main spindle of the channel   
            
         
        """
        pass
    
    ## Setter for property: (str) MainSpindle

    ##   the main spindle of the channel   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    @MainSpindle.setter
    def MainSpindle(self, mainSpindle: str):
        """
        Setter for property: (str) MainSpindle
          the main spindle of the channel   
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##   the name of the channel   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
          the name of the channel   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##   the name of the channel   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
          the name of the channel   
            
         
        """
        pass
    
    ##  Gets a list of assigned axes of the channel 
    ##  @return assignedAxes (List[str]):  the list of assigned axes .
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## License requirements: None.
    @staticmethod
    def GetAssignedAxes(builder: KinematicChannelBuilder) -> List[str]:
        """
         Gets a list of assigned axes of the channel 
         @return assignedAxes (List[str]):  the list of assigned axes .
        """
        pass
    
    ##  Gets a list of referenced spindles of the channel 
    ##  @return refSpindles (List[str]):  the list of referenced spindles .
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## License requirements: None.
    @staticmethod
    def GetReferencedSpindles(builder: KinematicChannelBuilder) -> List[str]:
        """
         Gets a list of referenced spindles of the channel 
         @return refSpindles (List[str]):  the list of referenced spindles .
        """
        pass
    
    ##  Sets a list of assigned axes of the channel 
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  the list of assigned axes 
    def SetAssignedAxes(builder: KinematicChannelBuilder, assignedAxes: List[str]) -> None:
        """
         Sets a list of assigned axes of the channel 
        """
        pass
    
    ##  Sets an assigned axis of the channel 
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  the assigned axis 
    def SetAssignedAxis(builder: KinematicChannelBuilder, axisName: str) -> None:
        """
         Sets an assigned axis of the channel 
        """
        pass
    
    ##  Sets a referenced device of the channel 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  the referenced device 
    def SetReferencedDevice(builder: KinematicChannelBuilder, deviceName: str) -> None:
        """
         Sets a referenced device of the channel 
        """
        pass
    
    ##  Sets a referenced spindle of the channel 
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  the referenced spindle 
    def SetReferencedSpindle(builder: KinematicChannelBuilder, spindleName: str) -> None:
        """
         Sets a referenced spindle of the channel 
        """
        pass
    
    ##  Sets a list of referenced spindles of the channel 
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  the list of referenced spindles 
    def SetReferencedSpindles(builder: KinematicChannelBuilder, refSpindles: List[str]) -> None:
        """
         Sets a list of referenced spindles of the channel 
        """
        pass
    
    ##  Sets an unassigned axis of the channel 
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  the unassigned axis 
    def SetUnassignedAxis(builder: KinematicChannelBuilder, axisName: str) -> None:
        """
         Sets an unassigned axis of the channel 
        """
        pass
    
    ##  Sets an unreferenced device of the channel 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  the unreferenced device 
    def SetUnreferencedDevice(builder: KinematicChannelBuilder, deviceName: str) -> None:
        """
         Sets an unreferenced device of the channel 
        """
        pass
    
    ##  Sets an unreferenced spindle of the channel 
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  the unreferenced spindle 
    def SetUnreferencedSpindle(builder: KinematicChannelBuilder, spindleName: str) -> None:
        """
         Sets an unreferenced spindle of the channel 
        """
        pass
    
import NXOpen
##  This class is used for channel configuration.
##         Calling @link Builder::Commit Builder::Commit@endlink  on this builder will return NULL.
##      <br> To create a new instance of this class, use @link NXOpen::SIM::KinematicConfigurator::CreateChannelConfigurationBuilder  NXOpen::SIM::KinematicConfigurator::CreateChannelConfigurationBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.3  <br> 

class KinematicChannelConfigurationBuilder(NXOpen.Builder): 
    """ This class is used for channel configuration.
        Calling <ja_method>Builder.Commit</ja_method> on this builder will return <ja_NULL>.
    """


    ## Getter for property: (@link KinematicChannelBuilderList NXOpen.SIM.KinematicChannelBuilderList@endlink) KinematicChannels
    ##   the list of kinematic channel   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## @return KinematicChannelBuilderList
    @property
    def KinematicChannels(self) -> KinematicChannelBuilderList:
        """
        Getter for property: (@link KinematicChannelBuilderList NXOpen.SIM.KinematicChannelBuilderList@endlink) KinematicChannels
          the list of kinematic channel   
            
         
        """
        pass
    
import NXOpen
##   @brief  Represents the KinematicComponentBuilder class object  
## 
##     <br> To create a new instance of this class, use @link NXOpen::SIM::KinematicComponentCollection::CreateHeadBaseComponentBuilder  NXOpen::SIM::KinematicComponentCollection::CreateHeadBaseComponentBuilder @endlink  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class KinematicComponentBuilder(NXOpen.Builder): 
    """ <summary> Represents the KinematicComponentBuilder class object </summary>  """


    ##  The register types 
    ##  the pocket id defined the register 
    class RegisterTypes(Enum):
        """
        Members Include: <SameAsPocketId> <Specify>
        """
        SameAsPocketId: int
        Specify: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> KinematicComponentBuilder.RegisterTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The SIM KIM system classes 
    ##  Machine Base classification 
    class SystemClass(Enum):
        """
        Members Include: <Machine> <Tool> <Turret> <Pocket> <Temporary> <Part> <Workpiece> <SetupElement> <Basic> <LatheSpindle> <PocketOnHead> <ToolCutting> <Spinning> <TempSpinning> <Head> <RobotMountableComponent> <RobotPickAndPlaceComponent> <ToolNonCutting> <FacingHead> <AdditiveMaterial> <ToolTurret> <Magazine> <ToolSpindle> <LocationPocket> <AssignablePocket> <WorkHolder> <ToolHolder> <Setup>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> KinematicComponentBuilder.SystemClass:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The Working Position Angle type 
    ##  no angle specified 
    class WorkPositionAngleTypes(Enum):
        """
        Members Include: <NotSet> <SpecifyAngle>
        """
        NotSet: int
        SpecifyAngle: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> KinematicComponentBuilder.WorkPositionAngleTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (int) AdjustRegister
    ##   the adjust register   
    ##     
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return int
    @property
    def AdjustRegister(self) -> int:
        """
        Getter for property: (int) AdjustRegister
          the adjust register   
            
         
        """
        pass
    
    ## Setter for property: (int) AdjustRegister

    ##   the adjust register   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @AdjustRegister.setter
    def AdjustRegister(self, adjustReg: int):
        """
        Setter for property: (int) AdjustRegister
          the adjust register   
            
         
        """
        pass
    
    ## Getter for property: (@link KinematicComponentBuilder.RegisterTypes NXOpen.SIM.KinematicComponentBuilder.RegisterTypes@endlink) AdjustRegisterType
    ##   the adjust register type   
    ##     
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return KinematicComponentBuilder.RegisterTypes
    @property
    def AdjustRegisterType(self) -> KinematicComponentBuilder.RegisterTypes:
        """
        Getter for property: (@link KinematicComponentBuilder.RegisterTypes NXOpen.SIM.KinematicComponentBuilder.RegisterTypes@endlink) AdjustRegisterType
          the adjust register type   
            
         
        """
        pass
    
    ## Setter for property: (@link KinematicComponentBuilder.RegisterTypes NXOpen.SIM.KinematicComponentBuilder.RegisterTypes@endlink) AdjustRegisterType

    ##   the adjust register type   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @AdjustRegisterType.setter
    def AdjustRegisterType(self, regType: KinematicComponentBuilder.RegisterTypes):
        """
        Setter for property: (@link KinematicComponentBuilder.RegisterTypes NXOpen.SIM.KinematicComponentBuilder.RegisterTypes@endlink) AdjustRegisterType
          the adjust register type   
            
         
        """
        pass
    
    ## Getter for property: (int) CutcomRegister
    ##   the cutcom register   
    ##     
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return int
    @property
    def CutcomRegister(self) -> int:
        """
        Getter for property: (int) CutcomRegister
          the cutcom register   
            
         
        """
        pass
    
    ## Setter for property: (int) CutcomRegister

    ##   the cutcom register   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @CutcomRegister.setter
    def CutcomRegister(self, cutcomReg: int):
        """
        Setter for property: (int) CutcomRegister
          the cutcom register   
            
         
        """
        pass
    
    ## Getter for property: (@link KinematicComponentBuilder.RegisterTypes NXOpen.SIM.KinematicComponentBuilder.RegisterTypes@endlink) CutcomRegisterType
    ##   the cutcom register type   
    ##     
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return KinematicComponentBuilder.RegisterTypes
    @property
    def CutcomRegisterType(self) -> KinematicComponentBuilder.RegisterTypes:
        """
        Getter for property: (@link KinematicComponentBuilder.RegisterTypes NXOpen.SIM.KinematicComponentBuilder.RegisterTypes@endlink) CutcomRegisterType
          the cutcom register type   
            
         
        """
        pass
    
    ## Setter for property: (@link KinematicComponentBuilder.RegisterTypes NXOpen.SIM.KinematicComponentBuilder.RegisterTypes@endlink) CutcomRegisterType

    ##   the cutcom register type   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @CutcomRegisterType.setter
    def CutcomRegisterType(self, regType: KinematicComponentBuilder.RegisterTypes):
        """
        Setter for property: (@link KinematicComponentBuilder.RegisterTypes NXOpen.SIM.KinematicComponentBuilder.RegisterTypes@endlink) CutcomRegisterType
          the cutcom register type   
            
         
        """
        pass
    
    ## Getter for property: (str) CutterId
    ##   the cutter id string to identify a cutter within a multitool   
    ##     
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return str
    @property
    def CutterId(self) -> str:
        """
        Getter for property: (str) CutterId
          the cutter id string to identify a cutter within a multitool   
            
         
        """
        pass
    
    ## Setter for property: (str) CutterId

    ##   the cutter id string to identify a cutter within a multitool   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @CutterId.setter
    def CutterId(self, cutterIdString: str):
        """
        Setter for property: (str) CutterId
          the cutter id string to identify a cutter within a multitool   
            
         
        """
        pass
    
    ## Getter for property: (str) DeviceId
    ##   the device id   
    ##     
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return str
    @property
    def DeviceId(self) -> str:
        """
        Getter for property: (str) DeviceId
          the device id   
            
         
        """
        pass
    
    ## Setter for property: (str) DeviceId

    ##   the device id   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @DeviceId.setter
    def DeviceId(self, deviceId: str):
        """
        Setter for property: (str) DeviceId
          the device id   
            
         
        """
        pass
    
    ## Getter for property: (int) HolderId
    ##   the holder id   
    ##     
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return int
    @property
    def HolderId(self) -> int:
        """
        Getter for property: (int) HolderId
          the holder id   
            
         
        """
        pass
    
    ## Setter for property: (int) HolderId

    ##   the holder id   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @HolderId.setter
    def HolderId(self, holderId: int):
        """
        Setter for property: (int) HolderId
          the holder id   
            
         
        """
        pass
    
    ## Getter for property: (str) HolderIdString
    ##   the holder id in string   
    ##     
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.5  <br> 

    ## @return str
    @property
    def HolderIdString(self) -> str:
        """
        Getter for property: (str) HolderIdString
          the holder id in string   
            
         
        """
        pass
    
    ## Setter for property: (str) HolderIdString

    ##   the holder id in string   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.5  <br> 

    @HolderIdString.setter
    def HolderIdString(self, holderIdString: str):
        """
        Setter for property: (str) HolderIdString
          the holder id in string   
            
         
        """
        pass
    
    ## Getter for property: (@link KinematicJunctionBuilderList NXOpen.SIM.KinematicJunctionBuilderList@endlink) JunctionList
    ##   the junction list   
    ##     
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return KinematicJunctionBuilderList
    @property
    def JunctionList(self) -> KinematicJunctionBuilderList:
        """
        Getter for property: (@link KinematicJunctionBuilderList NXOpen.SIM.KinematicJunctionBuilderList@endlink) JunctionList
          the junction list   
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##   the kim component's name   
    ##     
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
          the kim component's name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##   the kim component's name   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
          the kim component's name   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfTools
    ##   the number of tools   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def NumberOfTools(self) -> int:
        """
        Getter for property: (int) NumberOfTools
          the number of tools   
            
         
        """
        pass
    
    ## Setter for property: (int) NumberOfTools

    ##   the number of tools   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @NumberOfTools.setter
    def NumberOfTools(self, numTools: int):
        """
        Setter for property: (int) NumberOfTools
          the number of tools   
            
         
        """
        pass
    
    ## Getter for property: (float) WorkPositionAngle
    ##   the working position angle   
    ##     
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return float
    @property
    def WorkPositionAngle(self) -> float:
        """
        Getter for property: (float) WorkPositionAngle
          the working position angle   
            
         
        """
        pass
    
    ## Setter for property: (float) WorkPositionAngle

    ##   the working position angle   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @WorkPositionAngle.setter
    def WorkPositionAngle(self, angle: float):
        """
        Setter for property: (float) WorkPositionAngle
          the working position angle   
            
         
        """
        pass
    
    ## Getter for property: (@link KinematicComponentBuilder.WorkPositionAngleTypes NXOpen.SIM.KinematicComponentBuilder.WorkPositionAngleTypes@endlink) WorkPositionAngleType
    ##   the working position angle type   
    ##     
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return KinematicComponentBuilder.WorkPositionAngleTypes
    @property
    def WorkPositionAngleType(self) -> KinematicComponentBuilder.WorkPositionAngleTypes:
        """
        Getter for property: (@link KinematicComponentBuilder.WorkPositionAngleTypes NXOpen.SIM.KinematicComponentBuilder.WorkPositionAngleTypes@endlink) WorkPositionAngleType
          the working position angle type   
            
         
        """
        pass
    
    ## Setter for property: (@link KinematicComponentBuilder.WorkPositionAngleTypes NXOpen.SIM.KinematicComponentBuilder.WorkPositionAngleTypes@endlink) WorkPositionAngleType

    ##   the working position angle type   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @WorkPositionAngleType.setter
    def WorkPositionAngleType(self, type: KinematicComponentBuilder.WorkPositionAngleTypes):
        """
        Setter for property: (@link KinematicComponentBuilder.WorkPositionAngleTypes NXOpen.SIM.KinematicComponentBuilder.WorkPositionAngleTypes@endlink) WorkPositionAngleType
          the working position angle type   
            
         
        """
        pass
    
    ##  Adds a channel name to the component 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The channel name to add 
    def AddChannelName(builder: KinematicComponentBuilder, channel: str) -> None:
        """
         Adds a channel name to the component 
        """
        pass
    
    ##  Adds a single geometry element 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    ##  The geometry element to add 
    def AddGeometry(builder: KinematicComponentBuilder, geo: NXOpen.NXObject) -> None:
        """
         Adds a single geometry element 
        """
        pass
    
    ##  Adds a holding system to the component 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The holding system to add 
    def AddHoldingSystem(builder: KinematicComponentBuilder, holdSys: str) -> None:
        """
         Adds a holding system to the component 
        """
        pass
    
    ##  Add a system class 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    ##  the system class to add 
    def AddSystemClass(builder: KinematicComponentBuilder, sysClass: KinematicComponentBuilder.SystemClass) -> None:
        """
         Add a system class 
        """
        pass
    
    ##  Adds a user class to the component 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The user class to add 
    def AddUserClassName(builder: KinematicComponentBuilder, uclass: str) -> None:
        """
         Adds a user class to the component 
        """
        pass
    
    ##  Deletes all geometry elements from the component 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    @staticmethod
    def DeleteAllGeometries(builder: KinematicComponentBuilder) -> None:
        """
         Deletes all geometry elements from the component 
        """
        pass
    
    ##  Delete all system classes of the component 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::SIM::KinematicComponentBuilder::DeleteSystemClass NXOpen::SIM::KinematicComponentBuilder::DeleteSystemClass@endlink  instead  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    @staticmethod
    def DeleteAllSystemClasses(builder: KinematicComponentBuilder) -> None:
        """
         Delete all system classes of the component 
        """
        pass
    
    ##  Deletes a channel name from the component 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The channel name to remove 
    def DeleteChannelName(builder: KinematicComponentBuilder, channel: str) -> None:
        """
         Deletes a channel name from the component 
        """
        pass
    
    ##  Deletes a single geometry element from the component 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The geometry to remove 
    def DeleteGeometry(builder: KinematicComponentBuilder, geo: NXOpen.NXObject) -> None:
        """
         Deletes a single geometry element from the component 
        """
        pass
    
    ##  Deletes a holding system from the component 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The holding system to remove 
    def DeleteHoldingSystem(builder: KinematicComponentBuilder, holdSys: str) -> None:
        """
         Deletes a holding system from the component 
        """
        pass
    
    ##  Delete a system class 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  the system class to delete 
    def DeleteSystemClass(builder: KinematicComponentBuilder, sysClasses: KinematicComponentBuilder.SystemClass) -> None:
        """
         Delete a system class 
        """
        pass
    
    ##  Deletes a user class from the component 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The user class to remove 
    def DeleteUserClassName(builder: KinematicComponentBuilder, uclass: str) -> None:
        """
         Deletes a user class from the component 
        """
        pass
    
    ##  Get a list of channel names of the component 
    ##  @return channels (List[str]):  The channel names of the component .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    @staticmethod
    def GetChannelNames(builder: KinematicComponentBuilder) -> List[str]:
        """
         Get a list of channel names of the component 
         @return channels (List[str]):  The channel names of the component .
        """
        pass
    
    ##  Returns the geometry elements assigned to this component 
    ##  @return geos (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  The geometry elements .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    @staticmethod
    def GetGeometries(builder: KinematicComponentBuilder) -> List[NXOpen.NXObject]:
        """
         Returns the geometry elements assigned to this component 
         @return geos (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  The geometry elements .
        """
        pass
    
    ##  Get a list of holding systems of the component 
    ##  @return holdSys (List[str]):  The channel names of the component .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    @staticmethod
    def GetHoldingSystems(builder: KinematicComponentBuilder) -> List[str]:
        """
         Get a list of holding systems of the component 
         @return holdSys (List[str]):  The channel names of the component .
        """
        pass
    
    ##  Does the system save an IPW with the component? 
    ##  @return saveIpw (bool): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    @staticmethod
    def GetSaveIpw(builder: KinematicComponentBuilder) -> bool:
        """
         Does the system save an IPW with the component? 
         @return saveIpw (bool): .
        """
        pass
    
    ##  Returns the component's system classes 
    ##  @return sysClasses (@link KinematicComponentBuilder.SystemClass List[NXOpen.SIM.KinematicComponentBuilder.SystemClass]@endlink):  the component's system classes .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    @staticmethod
    def GetSystemClasses(builder: KinematicComponentBuilder) -> List[KinematicComponentBuilder.SystemClass]:
        """
         Returns the component's system classes 
         @return sysClasses (@link KinematicComponentBuilder.SystemClass List[NXOpen.SIM.KinematicComponentBuilder.SystemClass]@endlink):  the component's system classes .
        """
        pass
    
    ##  Get a list of user classes of the component 
    ##  @return uclass (List[str]):  The user classes of the component .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    @staticmethod
    def GetUserClassNames(builder: KinematicComponentBuilder) -> List[str]:
        """
         Get a list of user classes of the component 
         @return uclass (List[str]):  The user classes of the component .
        """
        pass
    
    ##  Test if the component is a member of the given system class 
    ##  @return result (bool):  TRUE if component is of the system class .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    ##  the system class to test 
    def IsOfSystemClass(builder: KinematicComponentBuilder, sysClass: KinematicComponentBuilder.SystemClass) -> bool:
        """
         Test if the component is a member of the given system class 
         @return result (bool):  TRUE if component is of the system class .
        """
        pass
    
    ##  Renames a channel name from the component 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The old channel name 
    def RenameChannelName(builder: KinematicComponentBuilder, oldName: str, newName: str) -> None:
        """
         Renames a channel name from the component 
        """
        pass
    
    ##  Renames a holding system from the component 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The old holding system 
    def RenameHoldingSystem(builder: KinematicComponentBuilder, oldName: str, newName: str) -> None:
        """
         Renames a holding system from the component 
        """
        pass
    
    ##  Renames a user class from the component 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The old user class 
    def RenameUserClass(builder: KinematicComponentBuilder, oldName: str, newName: str) -> None:
        """
         Renames a user class from the component 
        """
        pass
    
    ##  Sets geometry elements for the component 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  the geometry elements 
    def SetGeometries(builder: KinematicComponentBuilder, geos: List[NXOpen.NXObject]) -> None:
        """
         Sets geometry elements for the component 
        """
        pass
    
    ##  Save an IPW with the component 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ## 
    ## <param name="saveIpw"> (bool) </param>
    def SetSaveIpw(builder: KinematicComponentBuilder, saveIpw: bool) -> None:
        """
         Save an IPW with the component 
        """
        pass
    
import NXOpen
##  Represents the SimKimComponent Collection  <br> To obtain an instance of this class, refer to @link NXOpen::SIM::KinematicConfigurator  NXOpen::SIM::KinematicConfigurator @endlink  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class KinematicComponentCollection(NXOpen.TaggedObjectCollection): 
    """ Represents the SimKimComponent Collection """


    ##  Creates a builder for a kinematic component 
    ##  @return builder (@link KinematicComponentBuilder NXOpen.SIM.KinematicComponentBuilder@endlink):  The component builder .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    ##  The parent for the new component.
    ##                                                                                          Can be NULL 
    def CreateComponentBuilder(simKim: KinematicComponentCollection, parent: KinematicComponent, comp: KinematicComponent) -> KinematicComponentBuilder:
        """
         Creates a builder for a kinematic component 
         @return builder (@link KinematicComponentBuilder NXOpen.SIM.KinematicComponentBuilder@endlink):  The component builder .
        """
        pass
    
    ##  Creates a builder for facing head base component. 
    ##  @return builder (@link KinematicComponentBuilder NXOpen.SIM.KinematicComponentBuilder@endlink):  The new facing head base component builder .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The facing head component to edit. If NULL,
    ##                                                                                     then a new facing head base component is 
    ##                                                                                     created 
    def CreateFacingHeadBaseComponentBuilder(simKim: KinematicComponentCollection, head: KinematicComponent) -> KinematicComponentBuilder:
        """
         Creates a builder for facing head base component. 
         @return builder (@link KinematicComponentBuilder NXOpen.SIM.KinematicComponentBuilder@endlink):  The new facing head base component builder .
        """
        pass
    
    ##  Creates a builder for head base component. 
    ##  @return builder (@link KinematicComponentBuilder NXOpen.SIM.KinematicComponentBuilder@endlink):  The new head base component builder .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    ##  The head component to edit. If NULL,
    ##                                                                                     then a new head base component is 
    ##                                                                                     created 
    def CreateHeadBaseComponentBuilder(simKim: KinematicComponentCollection, head: KinematicComponent) -> KinematicComponentBuilder:
        """
         Creates a builder for head base component. 
         @return builder (@link KinematicComponentBuilder NXOpen.SIM.KinematicComponentBuilder@endlink):  The new head base component builder .
        """
        pass
    
    ##  Creates a builder for a machine base component. 
    ##  @return builder (@link KinematicComponentBuilder NXOpen.SIM.KinematicComponentBuilder@endlink):  The new machine base component builder .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The machine base component to edit.
    ##                                                                                     If NULL, then a new machine base component
    ##                                                                                     is created 
    def CreateMachineBaseComponentBuilder(simKim: KinematicComponentCollection, machine: KinematicComponent) -> KinematicComponentBuilder:
        """
         Creates a builder for a machine base component. 
         @return builder (@link KinematicComponentBuilder NXOpen.SIM.KinematicComponentBuilder@endlink):  The new machine base component builder .
        """
        pass
    
    ##  Creates a builder for tool base component. 
    ##  @return builder (@link KinematicComponentBuilder NXOpen.SIM.KinematicComponentBuilder@endlink):  The new tool base component builder .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    ##  The tool component to edit. If NULL,
    ##                                                                                     then a new tool base component is 
    ##                                                                                     created 
    def CreateToolBaseComponentBuilder(simKim: KinematicComponentCollection, tool: KinematicComponent) -> KinematicComponentBuilder:
        """
         Creates a builder for tool base component. 
         @return builder (@link KinematicComponentBuilder NXOpen.SIM.KinematicComponentBuilder@endlink):  The new tool base component builder .
        """
        pass
    
    ##  Finds the SIM.KinematicComponent object with the given identifier as recorded in a journal.
    ##  @return found (@link KinematicComponent NXOpen.SIM.KinematicComponent@endlink):  the found object .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    ##  the name of the object 
    def FindObject(simKim: KinematicComponentCollection, sid: str) -> KinematicComponent:
        """
         Finds the SIM.KinematicComponent object with the given identifier as recorded in a journal.
         @return found (@link KinematicComponent NXOpen.SIM.KinematicComponent@endlink):  the found object .
        """
        pass
    
import NXOpen
##   @brief  Represents the KinematicComponent class object  
## 
##     <br> Use the @link NXOpen::SIM::KinematicConfigurator NXOpen::SIM::KinematicConfigurator@endlink  class to create a KinematicComponent object.  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class KinematicComponent(NXOpen.NXObject): 
    """ <summary> Represents the KinematicComponent class object </summary>  """


    ##  Deletes ca config properties 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    @staticmethod
    def DeleteCaConfigProperties(comp: KinematicComponent) -> None:
        """
         Deletes ca config properties 
        """
        pass
    
    ##  Deletes a child component 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    ##  The old child component to remove 
    def DeleteComponent(comp: KinematicComponent, oldChild: KinematicComponent) -> None:
        """
         Deletes a child component 
        """
        pass
    
    ##  Gets an axis object in the component 
    ##  @return axis (@link KinematicAxis NXOpen.SIM.KinematicAxis@endlink):  The axis object .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    @staticmethod
    def GetAxis(comp: KinematicComponent) -> KinematicAxis:
        """
         Gets an axis object in the component 
         @return axis (@link KinematicAxis NXOpen.SIM.KinematicAxis@endlink):  The axis object .
        """
        pass
    
    ##  Gets a list of all junctions in the component 
    ##  @return junctions (@link KinematicJunction List[NXOpen.SIM.KinematicJunction]@endlink):  The list of junctions .
    ## 
    ##   <br>  Created in NX8.5.3  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    @staticmethod
    def GetJunctions(comp: KinematicComponent) -> List[KinematicJunction]:
        """
         Gets a list of all junctions in the component 
         @return junctions (@link KinematicJunction List[NXOpen.SIM.KinematicJunction]@endlink):  The list of junctions .
        """
        pass
    
    ##  Adds a new child component 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    ##  The child component to add 
    def InsertComponent(comp: KinematicComponent, newChild: KinematicComponent) -> None:
        """
         Adds a new child component 
        """
        pass
    
    ##  Adds a new junction to the component 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The junction to add 
    def InsertJunction(comp: KinematicComponent, junction: KinematicJunction) -> None:
        """
         Adds a new junction to the component 
        """
        pass
    
import NXOpen
import NXOpen.SIM.PostConfigurator
##   @brief  Represents the ISV base class object  
## 
##     <br> To obtain an instance of this class, use @link NXOpen::Part::KinematicConfigurator  NXOpen::Part::KinematicConfigurator @endlink  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class KinematicConfigurator(NXOpen.NXObject): 
    """ <summary> Represents the ISV base class object </summary>  """


    ##  The unite types for spinning geometries 
    ##  Create the spinning geometries as individual bodies 
    class UniteTypes(Enum):
        """
        Members Include: <Create> <Unite>
        """
        Create: int
        Unite: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> KinematicConfigurator.UniteTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link IsvControlPanelBuilder NXOpen.SIM.IsvControlPanelBuilder@endlink) IsvControlPanelBuilder
    ##   the isv control panel builder   
    ##     
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return IsvControlPanelBuilder
    @property
    def IsvControlPanelBuilder(self) -> IsvControlPanelBuilder:
        """
        Getter for property: (@link IsvControlPanelBuilder NXOpen.SIM.IsvControlPanelBuilder@endlink) IsvControlPanelBuilder
          the isv control panel builder   
            
         
        """
        pass
    
    ##  Returns the ComponentCollection instance belonging to this SimKim 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @link KinematicComponentCollection NXOpen.SIM.KinematicComponentCollection@endlink
    @property
    def ComponentCollection() -> KinematicComponentCollection:
        """
         Returns the ComponentCollection instance belonging to this SimKim 
        """
        pass
    
    ##  Adds a new user channel name to the list of channels 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The new channel name. 
    def AddChannel(kimMain: KinematicConfigurator, channel: str) -> None:
        """
         Adds a new user channel name to the list of channels 
        """
        pass
    
    ##  Adds a new user holding system to the list of holding systems 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The new holding system. 
    def AddHoldingSystem(kimMain: KinematicConfigurator, holdSys: str) -> None:
        """
         Adds a new user holding system to the list of holding systems 
        """
        pass
    
    ##  Adds a new user class name to the list of user classes 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The new user class name 
    def AddUserClassification(kimMain: KinematicConfigurator, userClass: str) -> None:
        """
         Adds a new user class name to the list of user classes 
        """
        pass
    
    ##  Copy a kinematic model.
    ##             User need to call @link NXOpen::SIM::KinematicConfigurator::DeleteKinematicModel NXOpen::SIM::KinematicConfigurator::DeleteKinematicModel@endlink  to delete the copy of kinematic model.
    ##         
    ##  @return kimModel (@link KinematicModel NXOpen.SIM.KinematicModel@endlink):  The copy of kinematic model .
    ## 
    ##   <br>  Created in NX10.0.1  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    @staticmethod
    def CopyKinematicModel(kimMain: KinematicConfigurator) -> KinematicModel:
        """
         Copy a kinematic model.
                    User need to call @link NXOpen::SIM::KinematicConfigurator::DeleteKinematicModel NXOpen::SIM::KinematicConfigurator::DeleteKinematicModel@endlink  to delete the copy of kinematic model.
                
         @return kimModel (@link KinematicModel NXOpen.SIM.KinematicModel@endlink):  The copy of kinematic model .
        """
        pass
    
    ##  Creates a builder to import a Sinumerik archive file 
    ##  @return builder (@link ArchiveImportBuilder NXOpen.SIM.ArchiveImportBuilder@endlink):  The new CamtImport builder .
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## License requirements: nx_isv_mtb ("Machine Tool Builder")
    def CreateArchiveImportBuilder(kimMain: KinematicConfigurator) -> ArchiveImportBuilder:
        """
         Creates a builder to import a Sinumerik archive file 
         @return builder (@link ArchiveImportBuilder NXOpen.SIM.ArchiveImportBuilder@endlink):  The new CamtImport builder .
        """
        pass
    
    ##  Creates a builder for a kinematic axis 
    ##  @return builder (@link KinematicAxisBuilder NXOpen.SIM.KinematicAxisBuilder@endlink):  The new axis builder .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The parent component 
    def CreateAxisBuilder(kimMain: KinematicConfigurator, parent: KinematicComponent, jct: KinematicJunction, axis: KinematicAxis) -> KinematicAxisBuilder:
        """
         Creates a builder for a kinematic axis 
         @return builder (@link KinematicAxisBuilder NXOpen.SIM.KinematicAxisBuilder@endlink):  The new axis builder .
        """
        pass
    
    ##  Creates a builder for a kinematic channel configurator 
    ##  @return builder (@link KinematicChannelConfigurationBuilder NXOpen.SIM.KinematicChannelConfigurationBuilder@endlink):  The new kinematic channel configuration builder .
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    def CreateChannelConfigurationBuilder(kimMain: KinematicConfigurator) -> KinematicChannelConfigurationBuilder:
        """
         Creates a builder for a kinematic channel configurator 
         @return builder (@link KinematicChannelConfigurationBuilder NXOpen.SIM.KinematicChannelConfigurationBuilder@endlink):  The new kinematic channel configuration builder .
        """
        pass
    
    ##  Creates a collision pair builder 
    ##  @return builder (@link CollisionPairBuilder NXOpen.CAM.CollisionPairBuilder@endlink):  The new collision pair builder .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    def CreateCollisionPairBuilder(kimMain: KinematicConfigurator) -> CollisionPairBuilder:
        """
         Creates a collision pair builder 
         @return builder (@link CollisionPairBuilder NXOpen.CAM.CollisionPairBuilder@endlink):  The new collision pair builder .
        """
        pass
    
    ##  Creates a builder to convert from MCD 
    ##  @return builder (@link ConvertFromMCDBuilder NXOpen.CAM.ConvertFromMCDBuilder@endlink):  The new convert from mcd builder .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    def CreateConvertFromMcdBuilder(kimMain: KinematicConfigurator) -> ConvertFromMCDBuilder:
        """
         Creates a builder to convert from MCD 
         @return builder (@link ConvertFromMCDBuilder NXOpen.CAM.ConvertFromMCDBuilder@endlink):  The new convert from mcd builder .
        """
        pass
    
    ##  Creates a builder for a import axis and channel data from mcf 
    ##  @return builder (@link KinematicImportMcfBuilder NXOpen.SIM.KinematicImportMcfBuilder@endlink):  The import axis and channel data builder .
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    def CreateImportMcfBuilder(kimMain: KinematicConfigurator) -> KinematicImportMcfBuilder:
        """
         Creates a builder for a import axis and channel data from mcf 
         @return builder (@link KinematicImportMcfBuilder NXOpen.SIM.KinematicImportMcfBuilder@endlink):  The import axis and channel data builder .
        """
        pass
    
    ##  Creates an isv control panel builder 
    ##  @return builder (@link IsvControlPanelBuilder NXOpen.SIM.IsvControlPanelBuilder@endlink):  The isv control panel builder .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The visualization type
    @overload
    def CreateIsvControlPanelBuilder(self, kimMain: KinematicConfigurator, driverType: IsvControlPanelBuilder.VisualizationType, objects: List[CAMObject]) -> IsvControlPanelBuilder:
        """
         Creates an isv control panel builder 
         @return builder (@link IsvControlPanelBuilder NXOpen.SIM.IsvControlPanelBuilder@endlink):  The isv control panel builder .
        """
        pass
    
    ##  Creates an isv control panel builder with given machine code file name.
    ##  @return builder (@link IsvControlPanelBuilder NXOpen.SIM.IsvControlPanelBuilder@endlink):  The isv control panel builder .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The visualization type
    @overload
    def CreateIsvControlPanelBuilder(self, kimMain: KinematicConfigurator, driverType: IsvControlPanelBuilder.VisualizationType, channelData: NcChannelSelectionData) -> IsvControlPanelBuilder:
        """
         Creates an isv control panel builder with given machine code file name.
         @return builder (@link IsvControlPanelBuilder NXOpen.SIM.IsvControlPanelBuilder@endlink):  The isv control panel builder .
        """
        pass
    
    ##  Creates a builder for a kinematic junction 
    ##  @return builder (@link KinematicJunctionBuilder NXOpen.SIM.KinematicJunctionBuilder@endlink):  The new junction builder .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    ##  The parent component 
    def CreateJunctionBuilder(kimMain: KinematicConfigurator, parent: KinematicComponent, jct: KinematicJunction) -> KinematicJunctionBuilder:
        """
         Creates a builder for a kinematic junction 
         @return builder (@link KinematicJunctionBuilder NXOpen.SIM.KinematicJunctionBuilder@endlink):  The new junction builder .
        """
        pass
    
    ##  Creates a builder for a kinematic chain 
    ##  @return builder (@link KinematicChain NXOpen.SIM.KinematicChain@endlink):  The new kinematic chain builder .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    def CreateKinematicChain(kimMain: KinematicConfigurator) -> KinematicChain:
        """
         Creates a builder for a kinematic chain 
         @return builder (@link KinematicChain NXOpen.SIM.KinematicChain@endlink):  The new kinematic chain builder .
        """
        pass
    
    ##  Creates a builder for a channel 
    ##  @return builder (@link KinematicChannelBuilder NXOpen.SIM.KinematicChannelBuilder@endlink):  The new kinematic channel builder .
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    def CreateKinematicChannelBuilder(kimMain: KinematicConfigurator) -> KinematicChannelBuilder:
        """
         Creates a builder for a channel 
         @return builder (@link KinematicChannelBuilder NXOpen.SIM.KinematicChannelBuilder@endlink):  The new kinematic channel builder .
        """
        pass
    
    ##  Creates a builder for a kinematic sinumerik ca config 
    ##  @return builder (@link KinematicSinumerikCaBuilder NXOpen.SIM.KinematicSinumerikCaBuilder@endlink):  The new kinematic sinumerik ca builder .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  the component to edit 
    def CreateKinematicSinumerikCaBuilder(kimMain: KinematicConfigurator, comp: KinematicComponent) -> KinematicSinumerikCaBuilder:
        """
         Creates a builder for a kinematic sinumerik ca config 
         @return builder (@link KinematicSinumerikCaBuilder NXOpen.SIM.KinematicSinumerikCaBuilder@endlink):  The new kinematic sinumerik ca builder .
        """
        pass
    
    ##  Creates a builder for the machine tool kit 
    ##  @return builder (@link MachineKitBuilder NXOpen.SIM.MachineKitBuilder@endlink):  The machine kit builder .
    ## 
    ##   <br>  Created in NX10.0.2  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    def CreateMachineKitBuilder(kimMain: KinematicConfigurator) -> MachineKitBuilder:
        """
         Creates a builder for the machine tool kit 
         @return builder (@link MachineKitBuilder NXOpen.SIM.MachineKitBuilder@endlink):  The machine kit builder .
        """
        pass
    
    ##  Creates a builder for the machine tool Library dialog 
    ##  @return builder (@link MachineLibraryBuilder NXOpen.SIM.MachineLibraryBuilder@endlink):  The machine Library builder .
    ## 
    ##   <br>  Created in NX10.0.2  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    def CreateMachineLibraryBuilder(kimMain: KinematicConfigurator) -> MachineLibraryBuilder:
        """
         Creates a builder for the machine tool Library dialog 
         @return builder (@link MachineLibraryBuilder NXOpen.SIM.MachineLibraryBuilder@endlink):  The machine Library builder .
        """
        pass
    
    ##  Creates a builder for the Machine Tool Configuration 
    ##  @return builder (@link MachineToolConfiguration NXOpen.SIM.MachineToolConfiguration@endlink):  The new machine tool configuration builder .
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## License requirements: nx_isv_mtb ("Machine Tool Builder")
    def CreateMachineToolConfigurationBuilder(kimMain: KinematicConfigurator) -> MachineToolConfiguration:
        """
         Creates a builder for the Machine Tool Configuration 
         @return builder (@link MachineToolConfiguration NXOpen.SIM.MachineToolConfiguration@endlink):  The new machine tool configuration builder .
        """
        pass
    
    ##  Creates an NcChannelSelectionData object to which files and channels can be assigned.  This is used when constructing the builder. 
    ##  @return ncChannelSelectionData (@link NcChannelSelectionData NXOpen.SIM.NcChannelSelectionData@endlink):  The NC channel selection data.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    def CreateNcChannelSelectionData(kimMain: KinematicConfigurator) -> NcChannelSelectionData:
        """
         Creates an NcChannelSelectionData object to which files and channels can be assigned.  This is used when constructing the builder. 
         @return ncChannelSelectionData (@link NcChannelSelectionData NXOpen.SIM.NcChannelSelectionData@endlink):  The NC channel selection data.
        """
        pass
    
    ##  Creates a builder for the nc program manager 
    ##  @return builder (@link NcProgramManagerBuilder NXOpen.SIM.NcProgramManagerBuilder@endlink):  The nc program manager builder .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    def CreateNcProgramManagerBuilder(kimMain: KinematicConfigurator) -> NcProgramManagerBuilder:
        """
         Creates a builder for the nc program manager 
         @return builder (@link NcProgramManagerBuilder NXOpen.SIM.NcProgramManagerBuilder@endlink):  The nc program manager builder .
        """
        pass
    
    ##  Creates a sim debug builder 
    ##  @return builder (@link SimDebugBuilder NXOpen.SIM.SimDebugBuilder@endlink):  The new sim debug builder .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    def CreateSimDebugBuilder(kimMain: KinematicConfigurator) -> SimDebugBuilder:
        """
         Creates a sim debug builder 
         @return builder (@link SimDebugBuilder NXOpen.SIM.SimDebugBuilder@endlink):  The new sim debug builder .
        """
        pass
    
    ##  Creates a builder for the load snapshot 
    ##  @return builder (@link LoadSnapshotBuilder NXOpen.SIM.LoadSnapshotBuilder@endlink):  The load snapshot builder .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    def CreateSimulationLoadsnapshotBuilder(kimMain: KinematicConfigurator) -> LoadSnapshotBuilder:
        """
         Creates a builder for the load snapshot 
         @return builder (@link LoadSnapshotBuilder NXOpen.SIM.LoadSnapshotBuilder@endlink):  The load snapshot builder .
        """
        pass
    
    ##  Creates a simulation options 
    ##  @return builder (@link SimulationOptionsBuilder NXOpen.CAM.SimulationOptionsBuilder@endlink):  The new simulation options .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The dialog type 
    def CreateSimulationOptionsBuilder(kimMain: KinematicConfigurator, dialogType: SimulationOptionsBuilder.DialogType) -> SimulationOptionsBuilder:
        """
         Creates a simulation options 
         @return builder (@link SimulationOptionsBuilder NXOpen.CAM.SimulationOptionsBuilder@endlink):  The new simulation options .
        """
        pass
    
    ##  Creates a builder for the save snapshot 
    ##  @return builder (@link SaveSnapshotBuilder NXOpen.SIM.SaveSnapshotBuilder@endlink):  The save snapshot builder .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    def CreateSimulationSavesnapshotBuilder(kimMain: KinematicConfigurator) -> SaveSnapshotBuilder:
        """
         Creates a builder for the save snapshot 
         @return builder (@link SaveSnapshotBuilder NXOpen.SIM.SaveSnapshotBuilder@endlink):  The save snapshot builder .
        """
        pass
    
    ##  Creates a builder for a sinumerik ca export spf 
    ##  @return builder (@link SinumerikCaExportBuilder NXOpen.SIM.SinumerikCaExportBuilder@endlink):  The new sinumerik ca export builder .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    def CreateSinumerikCaExportBuilder(kimMain: KinematicConfigurator) -> SinumerikCaExportBuilder:
        """
         Creates a builder for a sinumerik ca export spf 
         @return builder (@link SinumerikCaExportBuilder NXOpen.SIM.SinumerikCaExportBuilder@endlink):  The new sinumerik ca export builder .
        """
        pass
    
    ##  Creates a builder for a sinumerik ca facet 
    ##  @return builder (@link SinumerikCaFacetBuilder NXOpen.SIM.SinumerikCaFacetBuilder@endlink):  The new sinumerik ca facet builder .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    def CreateSinumerikCaFacetBuilder(kimMain: KinematicConfigurator) -> SinumerikCaFacetBuilder:
        """
         Creates a builder for a sinumerik ca facet 
         @return builder (@link SinumerikCaFacetBuilder NXOpen.SIM.SinumerikCaFacetBuilder@endlink):  The new sinumerik ca facet builder .
        """
        pass
    
    ##  Creates a builder for a sinumerik ca placeholder 
    ##  @return builder (@link SinumerikCaPlaceholderBuilder NXOpen.SIM.SinumerikCaPlaceholderBuilder@endlink):  The new sinumerik ca placeholder builder .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    def CreateSinumerikCaPlaceholderBuilder(kimMain: KinematicConfigurator) -> SinumerikCaPlaceholderBuilder:
        """
         Creates a builder for a sinumerik ca placeholder 
         @return builder (@link SinumerikCaPlaceholderBuilder NXOpen.SIM.SinumerikCaPlaceholderBuilder@endlink):  The new sinumerik ca placeholder builder .
        """
        pass
    
    ##  Creates a builder for a sinumerik ca simplify bodies 
    ##  @return builder (@link SinumerikCaSimplifyBodiesBuilder NXOpen.SIM.SinumerikCaSimplifyBodiesBuilder@endlink):  The new sinumerik ca simplify bodies builder .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    def CreateSinumerikCaSimplifyBodiesBuilder(kimMain: KinematicConfigurator) -> SinumerikCaSimplifyBodiesBuilder:
        """
         Creates a builder for a sinumerik ca simplify bodies 
         @return builder (@link SinumerikCaSimplifyBodiesBuilder NXOpen.SIM.SinumerikCaSimplifyBodiesBuilder@endlink):  The new sinumerik ca simplify bodies builder .
        """
        pass
    
    ##  Creates a builder for the smart machine kit debug dialog 
    ##  @return builder (@link SmkDebugBuilder NXOpen.SIM.SmkDebugBuilder@endlink):  The smk debug builder .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    def CreateSmkDebugBuilder(kimMain: KinematicConfigurator) -> SmkDebugBuilder:
        """
         Creates a builder for the smart machine kit debug dialog 
         @return builder (@link SmkDebugBuilder NXOpen.SIM.SmkDebugBuilder@endlink):  The smk debug builder .
        """
        pass
    
    ##  Creates a builder for the smart machine kit machine creation post dialog 
    ##  @return builder (@link NXOpen.SIM.PostConfigurator.CreationPostBuilder NXOpen.SIM.PostConfigurator.CreationPostBuilder@endlink):  The smk machine creation post builder .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    def CreateSmkMachineKitCreationPostBuilder(kimMain: KinematicConfigurator) -> NXOpen.SIM.PostConfigurator.CreationPostBuilder:
        """
         Creates a builder for the smart machine kit machine creation post dialog 
         @return builder (@link NXOpen.SIM.PostConfigurator.CreationPostBuilder NXOpen.SIM.PostConfigurator.CreationPostBuilder@endlink):  The smk machine creation post builder .
        """
        pass
    
    ##  Creates a builder for the smart machine kit machine specific information dialog 
    ##  @return builder (@link SmkMachineKitEditorBuilder NXOpen.SIM.SmkMachineKitEditorBuilder@endlink):  The smk machine specific information builder .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    def CreateSmkMachineKitEditorBuilder(kimMain: KinematicConfigurator) -> SmkMachineKitEditorBuilder:
        """
         Creates a builder for the smart machine kit machine specific information dialog 
         @return builder (@link SmkMachineKitEditorBuilder NXOpen.SIM.SmkMachineKitEditorBuilder@endlink):  The smk machine specific information builder .
        """
        pass
    
    ##  Creates a builder for the transition path editor dialog 
    ##  @return builder (@link SmkTransitionPathEditorBuilder NXOpen.SIM.SmkTransitionPathEditorBuilder@endlink):  The transition path editor builder .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    def CreateSmkTransitionPathEditorBuilder(kimMain: KinematicConfigurator) -> SmkTransitionPathEditorBuilder:
        """
         Creates a builder for the transition path editor dialog 
         @return builder (@link SmkTransitionPathEditorBuilder NXOpen.SIM.SmkTransitionPathEditorBuilder@endlink):  The transition path editor builder .
        """
        pass
    
    ##  Creates a builder for the smart machine kit wizard dialog 
    ##  @return builder (@link SmkWizardBuilder NXOpen.SIM.SmkWizardBuilder@endlink):  The smk wizard builder .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    def CreateSmkWizardBuilder(kimMain: KinematicConfigurator) -> SmkWizardBuilder:
        """
         Creates a builder for the smart machine kit wizard dialog 
         @return builder (@link SmkWizardBuilder NXOpen.SIM.SmkWizardBuilder@endlink):  The smk wizard builder .
        """
        pass
    
    ##  Creates a copy of the given component and spins its assigned geometry around a spinning axis.
    ##             For tool components, the X-axis of the tool tip junction is used as spinning axis. If none
    ##             is defined and for other types of components, the X-axis of the WCS is used.
    ##             The new component has the same parent as the source component. 
    ##  @return clone (@link KinematicComponent NXOpen.SIM.KinematicComponent@endlink):  The new spinning component .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    ##  The source component. 
    def CreateSpinningClone(kimMain: KinematicConfigurator, source: KinematicComponent, combine: bool) -> KinematicComponent:
        """
         Creates a copy of the given component and spins its assigned geometry around a spinning axis.
                    For tool components, the X-axis of the tool tip junction is used as spinning axis. If none
                    is defined and for other types of components, the X-axis of the WCS is used.
                    The new component has the same parent as the source component. 
         @return clone (@link KinematicComponent NXOpen.SIM.KinematicComponent@endlink):  The new spinning component .
        """
        pass
    
    ##  Creates a builder for a kinematic chain configurator 
    ##  @return builder (@link KinematicChainConfiguration NXOpen.SIM.KinematicChainConfiguration@endlink):  The new kinematic chain configuration builder .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    @staticmethod
    def DefineKinematicChains(kimMain: KinematicConfigurator) -> KinematicChainConfiguration:
        """
         Creates a builder for a kinematic chain configurator 
         @return builder (@link KinematicChainConfiguration NXOpen.SIM.KinematicChainConfiguration@endlink):  The new kinematic chain configuration builder .
        """
        pass
    
    ##  Deletes all channels from the kinematic model 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    @staticmethod
    def DeleteAllChannels(kimMain: KinematicConfigurator) -> None:
        """
         Deletes all channels from the kinematic model 
        """
        pass
    
    ##  Delete all holding systems from the kinematic model 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    @staticmethod
    def DeleteAllHoldingSystems(kimMain: KinematicConfigurator) -> None:
        """
         Delete all holding systems from the kinematic model 
        """
        pass
    
    ##  Deletes the given axis 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  the component to delete 
    def DeleteAxis(kimMain: KinematicConfigurator, axis: KinematicAxis) -> None:
        """
         Deletes the given axis 
        """
        pass
    
    ##  Deletes a channel name from the list of channels 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The channel name to delete. 
    def DeleteChannel(kimMain: KinematicConfigurator, channel: str) -> None:
        """
         Deletes a channel name from the list of channels 
        """
        pass
    
    ##  Deletes the given component 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    ##  the component to delete 
    def DeleteComponent(kimMain: KinematicConfigurator, comp: KinematicComponent) -> None:
        """
         Deletes the given component 
        """
        pass
    
    ##  Delete a holding system from the list 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The holding system to delete. 
    def DeleteHoldingSystem(kimMain: KinematicConfigurator, holdSys: str) -> None:
        """
         Delete a holding system from the list 
        """
        pass
    
    ##  Deletes the given junction 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  the component to delete 
    def DeleteJunction(kimMain: KinematicConfigurator, jct: KinematicJunction) -> None:
        """
         Deletes the given junction 
        """
        pass
    
    ##  Delete the copy of kinematic model. 
    ## 
    ##   <br>  Created in NX10.0.1  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The copy of kinematic model 
    def DeleteKinematicModel(kimMain: KinematicConfigurator, kimModel: KinematicModel) -> None:
        """
         Delete the copy of kinematic model. 
        """
        pass
    
    ##  Deletes the entire kinematic model 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    @staticmethod
    def DeleteModel(kimMain: KinematicConfigurator) -> None:
        """
         Deletes the entire kinematic model 
        """
        pass
    
    ##  Delete a root component from the @link NXOpen::SIM::KinematicConfigurator NXOpen::SIM::KinematicConfigurator@endlink  object 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The root component to remove 
    def DeleteRootComponent(kimMain: KinematicConfigurator, oldRoot: KinematicComponent) -> None:
        """
         Delete a root component from the @link NXOpen::SIM::KinematicConfigurator NXOpen::SIM::KinematicConfigurator@endlink  object 
        """
        pass
    
    ##  Deletes a user class name from the list of user classes 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The user class name to delete. 
    def DeleteUserClassification(kimMain: KinematicConfigurator, userClass: str) -> None:
        """
         Deletes a user class name from the list of user classes 
        """
        pass
    
    ##  Encrypt the entire kinematic model 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  the sold to ids 
    def EncryptModel(kimMain: KinematicConfigurator, soldToIDs: List[str], expirationDate: str) -> None:
        """
         Encrypt the entire kinematic model 
        """
        pass
    
    ##  Creates a builder for export the machine tool kit 
    ##  @return builder (@link ExportMachineKitBuilder NXOpen.SIM.ExportMachineKitBuilder@endlink):  The machine kit builder .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The library reference (libref) of the machine to export
    def ExportMachineKitBuilder(kimMain: KinematicConfigurator, machineName: str) -> ExportMachineKitBuilder:
        """
         Creates a builder for export the machine tool kit 
         @return builder (@link ExportMachineKitBuilder NXOpen.SIM.ExportMachineKitBuilder@endlink):  The machine kit builder .
        """
        pass
    
    ##  Export the entire kinematic model 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ## <param name="path"> (str) </param>
    def ExportModel(kimMain: KinematicConfigurator, path: str) -> None:
        """
         Export the entire kinematic model 
        """
        pass
    
    ##  Find the axis with the given name 
    ##  @return A tuple consisting of (axis, pComp, pJct). 
    ##  - axis is: @link KinematicAxis NXOpen.SIM.KinematicAxis@endlink. The axis, if found .
    ##  - pComp is: @link KinematicComponent NXOpen.SIM.KinematicComponent@endlink. The parent component of the axis .
    ##  - pJct is: @link KinematicJunction NXOpen.SIM.KinematicJunction@endlink. The parent junction of the axis .

    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The name to look for 
    @staticmethod
    def FindAxis(kimMain: KinematicConfigurator, name: str) -> Tuple[KinematicAxis, KinematicComponent, KinematicJunction]:
        """
         Find the axis with the given name 
         @return A tuple consisting of (axis, pComp, pJct). 
         - axis is: @link KinematicAxis NXOpen.SIM.KinematicAxis@endlink. The axis, if found .
         - pComp is: @link KinematicComponent NXOpen.SIM.KinematicComponent@endlink. The parent component of the axis .
         - pJct is: @link KinematicJunction NXOpen.SIM.KinematicJunction@endlink. The parent junction of the axis .

        """
        pass
    
    ##  Finds component which are of the given system class 
    ##  @return comps (@link KinematicComponent List[NXOpen.SIM.KinematicComponent]@endlink):  The found components .
    ## 
    ##   <br>  Created in NX8.0.3  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    ##  The system class to look for. 
    def FindComponentsBySystemClass(kimMain: KinematicConfigurator, sysclass: KinematicComponentBuilder.SystemClass) -> List[KinematicComponent]:
        """
         Finds component which are of the given system class 
         @return comps (@link KinematicComponent List[NXOpen.SIM.KinematicComponent]@endlink):  The found components .
        """
        pass
    
    ##  Find the junction with the given name 
    ##  @return jct (@link KinematicJunction NXOpen.SIM.KinematicJunction@endlink):  The junction, if found .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The name to look for 
    @overload
    def FindJunction(self, kimMain: KinematicConfigurator, name: str) -> KinematicJunction:
        """
         Find the junction with the given name 
         @return jct (@link KinematicJunction NXOpen.SIM.KinematicJunction@endlink):  The junction, if found .
        """
        pass
    
    ##  Finds a junction by its coordinate system 
    ##  @return jct (@link KinematicJunction NXOpen.SIM.KinematicJunction@endlink):  The junction for the csys .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  the csys of a junction 
    @overload
    def FindJunction(self, kimMain: KinematicConfigurator, csys: NXOpen.NXObject) -> KinematicJunction:
        """
         Finds a junction by its coordinate system 
         @return jct (@link KinematicJunction NXOpen.SIM.KinematicJunction@endlink):  The junction for the csys .
        """
        pass
    
    ##  Finds the @link NXOpen::SIM::KinematicComponent NXOpen::SIM::KinematicComponent@endlink  which is the owner of this junction 
    ##  @return owner (@link KinematicComponent NXOpen.SIM.KinematicComponent@endlink):  The owning component of the junction .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The junction 
    def FindOwnerOfJunction(kimMain: KinematicConfigurator, jct: KinematicJunction) -> KinematicComponent:
        """
         Finds the @link NXOpen::SIM::KinematicComponent NXOpen::SIM::KinematicComponent@endlink  which is the owner of this junction 
         @return owner (@link KinematicComponent NXOpen.SIM.KinematicComponent@endlink):  The owning component of the junction .
        """
        pass
    
    ##  Finds the @link NXOpen::SIM::KinematicComponent NXOpen::SIM::KinematicComponent@endlink  which is the parent of this component 
    ##  @return parent (@link KinematicComponent NXOpen.SIM.KinematicComponent@endlink):  The parent Component. NULL if comp is root component .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The component 
    def FindParentComponent(kimMain: KinematicConfigurator, comp: KinematicComponent) -> KinematicComponent:
        """
         Finds the @link NXOpen::SIM::KinematicComponent NXOpen::SIM::KinematicComponent@endlink  which is the parent of this component 
         @return parent (@link KinematicComponent NXOpen.SIM.KinematicComponent@endlink):  The parent Component. NULL if comp is root component .
        """
        pass
    
    ##  Gets a list of all axes in the kinematic 
    ##  @return axes (@link KinematicAxis List[NXOpen.SIM.KinematicAxis]@endlink):  The list of axes .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    @staticmethod
    def GetAxes(kimMain: KinematicConfigurator) -> List[KinematicAxis]:
        """
         Gets a list of all axes in the kinematic 
         @return axes (@link KinematicAxis List[NXOpen.SIM.KinematicAxis]@endlink):  The list of axes .
        """
        pass
    
    ##  Gets a list of all axis names in the kinematic 
    ##  @return axes (List[str]):  The list of axis names .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    @staticmethod
    def GetAxisNames(kimMain: KinematicConfigurator) -> List[str]:
        """
         Gets a list of all axis names in the kinematic 
         @return axes (List[str]):  The list of axis names .
        """
        pass
    
    ##  Get a list of all channels 
    ##  @return channels (List[str]):  The list of channels   .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    @staticmethod
    def GetChannels(kimMain: KinematicConfigurator) -> List[str]:
        """
         Get a list of all channels 
         @return channels (List[str]):  The list of channels   .
        """
        pass
    
    ##  Get a list of all holding systems 
    ##  @return holdSys (List[str]):  The holding systems           .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    @staticmethod
    def GetHoldingSystems(kimMain: KinematicConfigurator) -> List[str]:
        """
         Get a list of all holding systems 
         @return holdSys (List[str]):  The holding systems           .
        """
        pass
    
    ##  Gets a list of all junction names in the kinematic 
    ##  @return junctions (List[str]):  The list of junction names .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    @staticmethod
    def GetJunctionNames(kimMain: KinematicConfigurator) -> List[str]:
        """
         Gets a list of all junction names in the kinematic 
         @return junctions (List[str]):  The list of junction names .
        """
        pass
    
    ##  Gets a list of all junctions in the kinematic 
    ##  @return junctions (@link KinematicJunction List[NXOpen.SIM.KinematicJunction]@endlink):  The list of junctions .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    @staticmethod
    def GetJunctions(kimMain: KinematicConfigurator) -> List[KinematicJunction]:
        """
         Gets a list of all junctions in the kinematic 
         @return junctions (@link KinematicJunction List[NXOpen.SIM.KinematicJunction]@endlink):  The list of junctions .
        """
        pass
    
    ##  Returns the custom name of the kinematic model 
    ##  @return name (str):  The kinematic model name .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    @staticmethod
    def GetName(kimMain: KinematicConfigurator) -> str:
        """
         Returns the custom name of the kinematic model 
         @return name (str):  The kinematic model name .
        """
        pass
    
    ##  Get a list of all user classes 
    ##  @return uClasses (List[str]):  The list of user classes   .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    @staticmethod
    def GetUserClassifications(kimMain: KinematicConfigurator) -> List[str]:
        """
         Get a list of all user classes 
         @return uClasses (List[str]):  The list of user classes   .
        """
        pass
    
    ##  Creates a builder for import the machine tool kit from zip file
    ##  @return builder (@link ImportMachineKitBuilder NXOpen.SIM.ImportMachineKitBuilder@endlink):  The import machine zip builder .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  path of the machine tool zip file
    def ImportMachineBuilderFromZipFile(kimMain: KinematicConfigurator, zipPath: str) -> ImportMachineKitBuilder:
        """
         Creates a builder for import the machine tool kit from zip file
         @return builder (@link ImportMachineKitBuilder NXOpen.SIM.ImportMachineKitBuilder@endlink):  The import machine zip builder .
        """
        pass
    
    ##  Creates a builder for import the machine tool kit 
    ##  @return builder (@link ImportMachineKitBuilder NXOpen.SIM.ImportMachineKitBuilder@endlink):  The import machine kit builder .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  path of the machine tool kit file
    def ImportMachineKitBuilder(kimMain: KinematicConfigurator, kitPath: str) -> ImportMachineKitBuilder:
        """
         Creates a builder for import the machine tool kit 
         @return builder (@link ImportMachineKitBuilder NXOpen.SIM.ImportMachineKitBuilder@endlink):  The import machine kit builder .
        """
        pass
    
    ##  Import the machine specific data 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  the full path of the JSON file to be imported 
    def ImportMachineSpecificData(kimMain: KinematicConfigurator, path: str) -> None:
        """
         Import the machine specific data 
        """
        pass
    
    ##  Import the entire kinematic model 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ## <param name="path"> (str) </param>
    def ImportModel(kimMain: KinematicConfigurator, path: str) -> None:
        """
         Import the entire kinematic model 
        """
        pass
    
    ##  Import the nc archive for the Machine Tool Configuration 
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: nx_isv_mtb ("Machine Tool Builder")
    ##  The path to the nc archive file 
    def ImportNcArchive(kimMain: KinematicConfigurator, ncFileName: str, printReport: bool) -> None:
        """
         Import the nc archive for the Machine Tool Configuration 
        """
        pass
    
    ##  Adds a new root component to the @link NXOpen::SIM::KinematicConfigurator NXOpen::SIM::KinematicConfigurator@endlink  object 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The new root component 
    def InsertRootComponent(kimMain: KinematicConfigurator, newRoot: KinematicComponent) -> None:
        """
         Adds a new root component to the @link NXOpen::SIM::KinematicConfigurator NXOpen::SIM::KinematicConfigurator@endlink  object 
        """
        pass
    
    ##  Check if the axis with the given name is assigned to the specified channel
    ##  @return isAssigned (bool):  Boolean result set to true if the axis is found in the kinematic tree and assigned to the channel .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The name of the axis to look for 
    def IsAxisAssignedToChannel(kimMain: KinematicConfigurator, axisName: str, channelName: str) -> bool:
        """
         Check if the axis with the given name is assigned to the specified channel
         @return isAssigned (bool):  Boolean result set to true if the axis is found in the kinematic tree and assigned to the channel .
        """
        pass
    
    ##  Renames a channel name from the list 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The old channel name 
    def RenameChannel(kimMain: KinematicConfigurator, oldName: str, newName: str) -> None:
        """
         Renames a channel name from the list 
        """
        pass
    
    ##  Renames a holding system from the list 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The old holding system 
    def RenameHoldingSystem(kimMain: KinematicConfigurator, oldName: str, newName: str) -> None:
        """
         Renames a holding system from the list 
        """
        pass
    
    ##  Renames a user class name from the list 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The old user class name 
    def RenameUserClassification(kimMain: KinematicConfigurator, oldName: str, newName: str) -> None:
        """
         Renames a user class name from the list 
        """
        pass
    
    ##  Sets the custom name of the kinematic model 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    ##  The new kinematic model name 
    def SetName(kimMain: KinematicConfigurator, name: str) -> None:
        """
         Sets the custom name of the kinematic model 
        """
        pass
    
import NXOpen
##   @brief  Represents a builder for an import axis and channel data  from mcf  
## 
##     <br> Use the @link Part Part@endlink  class to create a KinematicImportMcfBuilder object.  <br> 
## 
##   <br>  Created in NX9.0.3  <br> 

class KinematicImportMcfBuilder(NXOpen.Builder): 
    """ <summary> Represents a builder for an import axis and channel data  from mcf </summary>  """


    ## Getter for property: (bool) IgnoreLimits
    ##   the flag which determines if the Limits of the MCF and the Kim are merge.  
    ##    
    ##             the soft limits are set based on the hard Limits of the Machine Tool Builder
    ##             or if the limits in the mcf are useful they will be taken from MCF.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## @return bool
    @property
    def IgnoreLimits(self) -> bool:
        """
        Getter for property: (bool) IgnoreLimits
          the flag which determines if the Limits of the MCF and the Kim are merge.  
           
                    the soft limits are set based on the hard Limits of the Machine Tool Builder
                    or if the limits in the mcf are useful they will be taken from MCF.  
         
        """
        pass
    
    ## Setter for property: (bool) IgnoreLimits

    ##   the flag which determines if the Limits of the MCF and the Kim are merge.  
    ##    
    ##             the soft limits are set based on the hard Limits of the Machine Tool Builder
    ##             or if the limits in the mcf are useful they will be taken from MCF.  
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    @IgnoreLimits.setter
    def IgnoreLimits(self, replace: bool):
        """
        Setter for property: (bool) IgnoreLimits
          the flag which determines if the Limits of the MCF and the Kim are merge.  
           
                    the soft limits are set based on the hard Limits of the Machine Tool Builder
                    or if the limits in the mcf are useful they will be taken from MCF.  
         
        """
        pass
    
    ## Getter for property: (str) McfPath
    ##   the path from the mcf file   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## @return str
    @property
    def McfPath(self) -> str:
        """
        Getter for property: (str) McfPath
          the path from the mcf file   
            
         
        """
        pass
    
    ## Setter for property: (str) McfPath

    ##   the path from the mcf file   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    @McfPath.setter
    def McfPath(self, path: str):
        """
        Setter for property: (str) McfPath
          the path from the mcf file   
            
         
        """
        pass
    
    ## Getter for property: (bool) ReplaceChannel
    ##   the flag which determines if the channel data of the Machine Tool Builder are 
    ##             deleted befor they are replaced through the Channel data of the MCF-File  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## @return bool
    @property
    def ReplaceChannel(self) -> bool:
        """
        Getter for property: (bool) ReplaceChannel
          the flag which determines if the channel data of the Machine Tool Builder are 
                    deleted befor they are replaced through the Channel data of the MCF-File  
            
         
        """
        pass
    
    ## Setter for property: (bool) ReplaceChannel

    ##   the flag which determines if the channel data of the Machine Tool Builder are 
    ##             deleted befor they are replaced through the Channel data of the MCF-File  
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    @ReplaceChannel.setter
    def ReplaceChannel(self, replace: bool):
        """
        Setter for property: (bool) ReplaceChannel
          the flag which determines if the channel data of the Machine Tool Builder are 
                    deleted befor they are replaced through the Channel data of the MCF-File  
            
         
        """
        pass
    
import NXOpen
##  Represents a list of objects. <br> To create a new instance of this class, use @link NXOpen::Part::CreateObjectList  NXOpen::Part::CreateObjectList @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class KinematicJunctionBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""


    ## Getter for property: (int) Length
    ##   the length of the list   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
          the length of the list   
            
         
        """
        pass
    
    ##  Appends a set of objects to the list
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ##  items to append 
    @overload
    def Append(self, object_list: KinematicJunctionBuilderList, objects: List[KinematicJunctionBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    
    ##  Appends an object to the list
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  item to append 
    @overload
    def Append(self, object_list: KinematicJunctionBuilderList, objectValue: KinematicJunctionBuilder) -> None:
        """
         Appends an object to the list
            
        """
        pass
    
    ##  Clears the entire list without deleting the objects.  The caller is responsible for 
    ##         accounting for these objects.  If they are not used or deleted by the time the part is 
    ##         closed (in other words, leaked) an error will occur 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Clear(object_list: KinematicJunctionBuilderList) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    
    ##  Deletes the item at the index specified.  The size of the list does
    ##     *   not change, but the item at this index is set to NULL.
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ##  index of item to be deleted 
    def ClearIndex(object_list: KinematicJunctionBuilderList, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
            *   not change, but the item at this index is set to NULL.
            
        """
        pass
    
    ##  Clears the entire list 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  whether to delete the objects when removing them 
    def Clear(object_list: KinematicJunctionBuilderList, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    
    ##  Erases the object from the list, but does not delete the object.
    ##         The list is shifted so that there isn't a null where the object used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  index of item to be removed from the list 
    @overload
    def Erase(self, object_list: KinematicJunctionBuilderList, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    
    ##  Erases the object at the given position from the list.
    ##         The list is shifted so that there isn't a null where the object used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  index of item to be removed from the list 
    @overload
    def Erase(self, object_list: KinematicJunctionBuilderList, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    
    ##  Erases the object from the list, but does not delete the object.
    ##         The list is shifted so that there isn't a null where the object used to exist. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  object to be removed from the list 
    @overload
    def Erase(self, object_list: KinematicJunctionBuilderList, obj: KinematicJunctionBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    
    ##  Erases the object from the list.
    ##         The list is shifted so that there isn't a null where the object used to exist. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  object to be removed from the list 
    @overload
    def Erase(self, object_list: KinematicJunctionBuilderList, obj: KinematicJunctionBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    
    ##  Finds the index where the input object appears.  If it does not appear,
    ##     *   -1 is returned.
    ##     
    ##  @return index (int):  index of input object, -1 if not on list .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ##  Object to find index for 
    def FindIndex(object_list: KinematicJunctionBuilderList, obj: KinematicJunctionBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
            *   -1 is returned.
            
         @return index (int):  index of input object, -1 if not on list .
        """
        pass
    
    ##  Returns the object at the input index.  May be NULL.
    ##     
    ##  @return obj (@link KinematicJunctionBuilder NXOpen.SIM.KinematicJunctionBuilder@endlink):  object found at input index .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ##  index of object to return 
    def FindItem(object_list: KinematicJunctionBuilderList, index: int) -> KinematicJunctionBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         @return obj (@link KinematicJunctionBuilder NXOpen.SIM.KinematicJunctionBuilder@endlink):  object found at input index .
        """
        pass
    
    ##  Gets the contents of the entire list 
    ##  @return objects (@link KinematicJunctionBuilder List[NXOpen.SIM.KinematicJunctionBuilder]@endlink):  The list contents .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetContents(object_list: KinematicJunctionBuilderList) -> List[KinematicJunctionBuilder]:
        """
         Gets the contents of the entire list 
         @return objects (@link KinematicJunctionBuilder List[NXOpen.SIM.KinematicJunctionBuilder]@endlink):  The list contents .
        """
        pass
    
    ##  Inserts an object at the specified location 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  location at which to insert the object 
    def Insert(object_list: KinematicJunctionBuilderList, location: int, objectValue: KinematicJunctionBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    
    ##  Move object at the specified location to the bottom of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  location of the item 
    def MoveToBottom(object_list: KinematicJunctionBuilderList, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    
    ##  Move object at the specified location to the top of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  location of the item 
    def MoveToTop(object_list: KinematicJunctionBuilderList, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    
    ##  Sets the contents of the entire list. This overwrites the previous contents of this list, 
    ##         but does not delete any objects that were originally on the list.
    ##      
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  The list contents 
    def SetContents(object_list: KinematicJunctionBuilderList, objects: List[KinematicJunctionBuilder]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    
    ##  Exchanges the position of two objects inside the list.
    ##         The first object is placed where the second used to be,
    ##         and second object where the first used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  location of the first item 
    @overload
    def Swap(self, object_list: KinematicJunctionBuilderList, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
    ##  Exchanges the position of two objects inside the list.
    ##         The first object is placed where the second used to be,
    ##         and second object where the first used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  first item 
    @overload
    def Swap(self, object_list: KinematicJunctionBuilderList, object1: KinematicJunctionBuilder, object2: KinematicJunctionBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
import NXOpen
##   @brief  Represents the SimKimJunctionBuilder class object  
## 
##     <br> Use the @link NXOpen::SIM::KinematicConfigurator NXOpen::SIM::KinematicConfigurator@endlink  class to create a KinematicJunctionBuilder object.  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class KinematicJunctionBuilder(NXOpen.Builder): 
    """ <summary> Represents the SimKimJunctionBuilder class object </summary>  """


    ##  The junction system classes 
    ##  no specal class 
    class SystemClass(Enum):
        """
        Members Include: <NotSet> <Mount> <MachineZero> <ToolZero> <ToolTip> <LatheWpZx> <LatheWpXy> <RobotBase> <RobotFlange> <PositionerBase> <PositionerTool>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> KinematicJunctionBuilder.SystemClass:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link KinematicJunctionBuilder.SystemClass NXOpen.SIM.KinematicJunctionBuilder.SystemClass@endlink) Classification
    ##   the classification of the junction   
    ##     
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return KinematicJunctionBuilder.SystemClass
    @property
    def Classification(self) -> KinematicJunctionBuilder.SystemClass:
        """
        Getter for property: (@link KinematicJunctionBuilder.SystemClass NXOpen.SIM.KinematicJunctionBuilder.SystemClass@endlink) Classification
          the classification of the junction   
            
         
        """
        pass
    
    ## Setter for property: (@link KinematicJunctionBuilder.SystemClass NXOpen.SIM.KinematicJunctionBuilder.SystemClass@endlink) Classification

    ##   the classification of the junction   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @Classification.setter
    def Classification(self, jctClass: KinematicJunctionBuilder.SystemClass):
        """
        Setter for property: (@link KinematicJunctionBuilder.SystemClass NXOpen.SIM.KinematicJunctionBuilder.SystemClass@endlink) Classification
          the classification of the junction   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink) Csys
    ##   the CSYS associated with the junction   
    ##     
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.CartesianCoordinateSystem
    @property
    def Csys(self) -> NXOpen.CartesianCoordinateSystem:
        """
        Getter for property: (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink) Csys
          the CSYS associated with the junction   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink) Csys

    ##   the CSYS associated with the junction   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @Csys.setter
    def Csys(self, csys: NXOpen.CartesianCoordinateSystem):
        """
        Setter for property: (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink) Csys
          the CSYS associated with the junction   
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##   the kim junction's name   
    ##     
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
          the kim junction's name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##   the kim junction's name   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
          the kim junction's name   
            
         
        """
        pass
    
    ##  Create the default CSYS based on WCS 
    ##  @return csys (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink):  the default csys .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    def CreateDefaultCsys(builder: KinematicJunctionBuilder) -> NXOpen.CartesianCoordinateSystem:
        """
         Create the default CSYS based on WCS 
         @return csys (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink):  the default csys .
        """
        pass
    
    ##  Create the tooltip CSYS 
    ##  @return csys (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink):  the tooltip csys .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    def CreateTooltipCsys(builder: KinematicJunctionBuilder) -> NXOpen.CartesianCoordinateSystem:
        """
         Create the tooltip CSYS 
         @return csys (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink):  the tooltip csys .
        """
        pass
    
    ##  Test if this is a machine zero junction 
    ##  @return result (bool):  true if it is the machine zero junction .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    @staticmethod
    def IsMachineZero(builder: KinematicJunctionBuilder) -> bool:
        """
         Test if this is a machine zero junction 
         @return result (bool):  true if it is the machine zero junction .
        """
        pass
    
    ##  Test if the junction is a tool mount junctions 
    ##  @return result (bool):  true if it is a tool mount junction .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    @staticmethod
    def IsToolMount(builder: KinematicJunctionBuilder) -> bool:
        """
         Test if the junction is a tool mount junctions 
         @return result (bool):  true if it is a tool mount junction .
        """
        pass
    
    ##  Test if the junction is a tool tip junctions 
    ##  @return result (bool):  true if it is a tool tip junction .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    @staticmethod
    def IsToolTip(builder: KinematicJunctionBuilder) -> bool:
        """
         Test if the junction is a tool tip junctions 
         @return result (bool):  true if it is a tool tip junction .
        """
        pass
    
import NXOpen
##   @brief  Represents the KinematicJunction class object  
## 
##     <br> Use the @link NXOpen::SIM::KinematicConfigurator NXOpen::SIM::KinematicConfigurator@endlink  class to create a SimKimJunction object.  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class KinematicJunction(NXOpen.NXObject): 
    """ <summary> Represents the KinematicJunction class object </summary>  """


    ## Getter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) Matrix
    ##   the matrix of the junction   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return NXOpen.Matrix3x3
    @property
    def Matrix(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) Matrix
          the matrix of the junction   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) Origin
    ##   the origin of the junction   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return NXOpen.Vector3d
    @property
    def Origin(self) -> NXOpen.Vector3d:
        """
        Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) Origin
          the origin of the junction   
            
         
        """
        pass
    
import NXOpen
##   @brief Represents the Kinematic Model class object. 
## 
##  
##          @code 
##         Example how to move machine axes:
## 
##         Dim kinematicModel As NXOpen.SIM.KinematicModel
##         kinematicModel = kinematicConfigurator.CopyKinematicModel()
##             
##         Dim kinematicAxis_X1 As NXOpen.SIM.KinematicAxis
##         kinematicAxis_X1 = kinematicModel.FindMachineAxis("X1")
## 
##         Dim kinematicAxis_Y1 As NXOpen.SIM.KinematicAxis
##         kinematicAxis_Y1 = kinematicModel.FindMachineAxis("Y1")
## 
##         Dim kinematicAxis_Z1 As NXOpen.SIM.KinematicAxis
##         kinematicAxis_Z1 = kinematicModel.FindMachineAxis("Z1")
## 
##         kinematicModel.SetMachineAxisValue(kinematicAxis_X1, 100)
##         kinematicModel.SetMachineAxisValue(kinematicAxis_Y1, 150)
##         kinematicModel.SetMachineAxisValue(kinematicAxis_Z1, 200)
## 
##         'Move the axes X1, Y1, Z1 to the position 100, 150, 200 on the graphic window simultaneously
##         kinematicModel.UpdateMachineDisplay()
##         ...
##             
##         kinematicConfigurator.DeleteKinematicModel(kinematicModel)
##          @endcode 
##      <br> Use the @link NXOpen::SIM::KinematicConfigurator NXOpen::SIM::KinematicConfigurator@endlink  class to create a KinematicModel object.  <br> 
## 
##   <br>  Created in NX10.0.1  <br> 

class KinematicModel(NXOpen.NXObject): 
    """ <summary>Represents the Kinematic Model class object.</summary>
        <code>
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
        </code>
    """


    ##  Find the machine axis with the given name. 
    ##  @return axis (@link KinematicAxis NXOpen.SIM.KinematicAxis@endlink):  The axis, if found .
    ## 
    ##   <br>  Created in NX10.0.1  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The name to look for 
    def FindMachineAxis(kimModel: KinematicModel, name: str) -> KinematicAxis:
        """
         Find the machine axis with the given name. 
         @return axis (@link KinematicAxis NXOpen.SIM.KinematicAxis@endlink):  The axis, if found .
        """
        pass
    
    ##  Sets the machine axis to the given value.
    ##             User need to call @link NXOpen::SIM::KinematicModel::UpdateMachineDisplay NXOpen::SIM::KinematicModel::UpdateMachineDisplay@endlink  to see the axis moving in the graphic window.
    ##         
    ## 
    ##   <br>  Created in NX10.0.1  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  the machine axis to be moved 
    def SetMachineAxisValue(kimModel: KinematicModel, axis: KinematicAxis, value: float) -> None:
        """
         Sets the machine axis to the given value.
                    User need to call @link NXOpen::SIM::KinematicModel::UpdateMachineDisplay NXOpen::SIM::KinematicModel::UpdateMachineDisplay@endlink  to see the axis moving in the graphic window.
                
        """
        pass
    
    ##  Update machine display.
    ##             This call is needed after call @link NXOpen::SIM::KinematicModel::SetMachineAxisValue NXOpen::SIM::KinematicModel::SetMachineAxisValue@endlink  to see the axis moving in the graphic window.
    ##         
    ## 
    ##   <br>  Created in NX10.0.1  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    @staticmethod
    def UpdateMachineDisplay(kimModel: KinematicModel) -> None:
        """
         Update machine display.
                    This call is needed after call @link NXOpen::SIM::KinematicModel::SetMachineAxisValue NXOpen::SIM::KinematicModel::SetMachineAxisValue@endlink  to see the axis moving in the graphic window.
                
        """
        pass
    
import NXOpen
##  This class is used for edit sinumerik collision avoidance properties.
##         Calling @link Builder::Commit Builder::Commit@endlink  on this builder will only return NULL.
##      <br> Use the @link KinematicConfigurator KinematicConfigurator@endlink  class to create a KinematicSinumerikCaBuilder object.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class KinematicSinumerikCaBuilder(NXOpen.Builder): 
    """ This class is used for edit sinumerik collision avoidance properties.
        Calling <ja_method>Builder.Commit</ja_method> on this builder will only return <ja_NULL>.
    """


    ##  The init state types 
    ##  Active     
    class PlcInitStateTypes(Enum):
        """
        Members Include: <Active> <Inactive> <Preselect>
        """
        Active: int
        Inactive: int
        Preselect: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> KinematicSinumerikCaBuilder.PlcInitStateTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The usage types 
    ##  Collision Check 
    class PlcUsageTypes(Enum):
        """
        Members Include: <CollisionCheck> <Visualize> <All>
        """
        CollisionCheck: int
        Visualize: int
        All: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> KinematicSinumerikCaBuilder.PlcUsageTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (int) DetailLevel
    ##   the detail level for this protection area   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def DetailLevel(self) -> int:
        """
        Getter for property: (int) DetailLevel
          the detail level for this protection area   
            
         
        """
        pass
    
    ## Setter for property: (int) DetailLevel

    ##   the detail level for this protection area   
    ##     
    ##  
    ## Setter License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @DetailLevel.setter
    def DetailLevel(self, level: int):
        """
        Setter for property: (int) DetailLevel
          the detail level for this protection area   
            
         
        """
        pass
    
    ## Getter for property: (int) MagazineIndex
    ##   the magazine index for this automatic protection area   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return int
    @property
    def MagazineIndex(self) -> int:
        """
        Getter for property: (int) MagazineIndex
          the magazine index for this automatic protection area   
            
         
        """
        pass
    
    ## Setter for property: (int) MagazineIndex

    ##   the magazine index for this automatic protection area   
    ##     
    ##  
    ## Setter License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @MagazineIndex.setter
    def MagazineIndex(self, index: int):
        """
        Setter for property: (int) MagazineIndex
          the magazine index for this automatic protection area   
            
         
        """
        pass
    
    ## Getter for property: (int) MagazineLocationIndex
    ##   the magazine location index for this automatic protection area  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return int
    @property
    def MagazineLocationIndex(self) -> int:
        """
        Getter for property: (int) MagazineLocationIndex
          the magazine location index for this automatic protection area  
            
         
        """
        pass
    
    ## Setter for property: (int) MagazineLocationIndex

    ##   the magazine location index for this automatic protection area  
    ##     
    ##  
    ## Setter License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @MagazineLocationIndex.setter
    def MagazineLocationIndex(self, index: int):
        """
        Setter for property: (int) MagazineLocationIndex
          the magazine location index for this automatic protection area  
            
         
        """
        pass
    
    ## Getter for property: (int) PlcBit
    ##   the PLC bit for this protection area  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def PlcBit(self) -> int:
        """
        Getter for property: (int) PlcBit
          the PLC bit for this protection area  
            
         
        """
        pass
    
    ## Setter for property: (int) PlcBit

    ##   the PLC bit for this protection area  
    ##     
    ##  
    ## Setter License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @PlcBit.setter
    def PlcBit(self, bit: int):
        """
        Setter for property: (int) PlcBit
          the PLC bit for this protection area  
            
         
        """
        pass
    
    ## Getter for property: (@link KinematicSinumerikCaBuilder.PlcInitStateTypes NXOpen.SIM.KinematicSinumerikCaBuilder.PlcInitStateTypes@endlink) PlcInitState
    ##   the initial PLC state for this protection area   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return KinematicSinumerikCaBuilder.PlcInitStateTypes
    @property
    def PlcInitState(self) -> KinematicSinumerikCaBuilder.PlcInitStateTypes:
        """
        Getter for property: (@link KinematicSinumerikCaBuilder.PlcInitStateTypes NXOpen.SIM.KinematicSinumerikCaBuilder.PlcInitStateTypes@endlink) PlcInitState
          the initial PLC state for this protection area   
            
         
        """
        pass
    
    ## Setter for property: (@link KinematicSinumerikCaBuilder.PlcInitStateTypes NXOpen.SIM.KinematicSinumerikCaBuilder.PlcInitStateTypes@endlink) PlcInitState

    ##   the initial PLC state for this protection area   
    ##     
    ##  
    ## Setter License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @PlcInitState.setter
    def PlcInitState(self, state: KinematicSinumerikCaBuilder.PlcInitStateTypes):
        """
        Setter for property: (@link KinematicSinumerikCaBuilder.PlcInitStateTypes NXOpen.SIM.KinematicSinumerikCaBuilder.PlcInitStateTypes@endlink) PlcInitState
          the initial PLC state for this protection area   
            
         
        """
        pass
    
    ## Getter for property: (@link KinematicSinumerikCaBuilder.PlcUsageTypes NXOpen.SIM.KinematicSinumerikCaBuilder.PlcUsageTypes@endlink) PlcUsage
    ##   the PLC usage for this protection area   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return KinematicSinumerikCaBuilder.PlcUsageTypes
    @property
    def PlcUsage(self) -> KinematicSinumerikCaBuilder.PlcUsageTypes:
        """
        Getter for property: (@link KinematicSinumerikCaBuilder.PlcUsageTypes NXOpen.SIM.KinematicSinumerikCaBuilder.PlcUsageTypes@endlink) PlcUsage
          the PLC usage for this protection area   
            
         
        """
        pass
    
    ## Setter for property: (@link KinematicSinumerikCaBuilder.PlcUsageTypes NXOpen.SIM.KinematicSinumerikCaBuilder.PlcUsageTypes@endlink) PlcUsage

    ##   the PLC usage for this protection area   
    ##     
    ##  
    ## Setter License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @PlcUsage.setter
    def PlcUsage(self, usage: KinematicSinumerikCaBuilder.PlcUsageTypes):
        """
        Setter for property: (@link KinematicSinumerikCaBuilder.PlcUsageTypes NXOpen.SIM.KinematicSinumerikCaBuilder.PlcUsageTypes@endlink) PlcUsage
          the PLC usage for this protection area   
            
         
        """
        pass
    
    ## Getter for property: (int) TOIndex
    ##   the TO-index for this automatic protection area   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return int
    @property
    def TOIndex(self) -> int:
        """
        Getter for property: (int) TOIndex
          the TO-index for this automatic protection area   
            
         
        """
        pass
    
    ## Setter for property: (int) TOIndex

    ##   the TO-index for this automatic protection area   
    ##     
    ##  
    ## Setter License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @TOIndex.setter
    def TOIndex(self, index: int):
        """
        Setter for property: (int) TOIndex
          the TO-index for this automatic protection area   
            
         
        """
        pass
    
import NXOpen
## 
##     Represents a @link NXOpen::SIM::LoadSnapshotBuilder NXOpen::SIM::LoadSnapshotBuilder@endlink 
##      <br> To create a new instance of this class, use @link NXOpen::SIM::KinematicConfigurator::CreateSimulationLoadsnapshotBuilder  NXOpen::SIM::KinematicConfigurator::CreateSimulationLoadsnapshotBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class LoadSnapshotBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>NXOpen.SIM.LoadSnapshotBuilder</ja_class>
    """


    ## Getter for property: (str) ExternalReference
    ##   the external reference   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return str
    @property
    def ExternalReference(self) -> str:
        """
        Getter for property: (str) ExternalReference
          the external reference   
            
         
        """
        pass
    
    ## Setter for property: (str) ExternalReference

    ##   the external reference   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @ExternalReference.setter
    def ExternalReference(self, reference: str):
        """
        Setter for property: (str) ExternalReference
          the external reference   
            
         
        """
        pass
    
    ## Getter for property: (bool) RunToSimTime
    ##   the run to simulation time   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def RunToSimTime(self) -> bool:
        """
        Getter for property: (bool) RunToSimTime
          the run to simulation time   
            
         
        """
        pass
    
    ## Setter for property: (bool) RunToSimTime

    ##   the run to simulation time   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RunToSimTime.setter
    def RunToSimTime(self, bRunToTime: bool):
        """
        Setter for property: (bool) RunToSimTime
          the run to simulation time   
            
         
        """
        pass
    
    ## Getter for property: (@link Snapshot NXOpen.SIM.Snapshot@endlink) Snapshot
    ##   the snapshot   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return Snapshot
    @property
    def Snapshot(self) -> Snapshot:
        """
        Getter for property: (@link Snapshot NXOpen.SIM.Snapshot@endlink) Snapshot
          the snapshot   
            
         
        """
        pass
    
    ## Setter for property: (@link Snapshot NXOpen.SIM.Snapshot@endlink) Snapshot

    ##   the snapshot   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @Snapshot.setter
    def Snapshot(self, snapshot: Snapshot):
        """
        Setter for property: (@link Snapshot NXOpen.SIM.Snapshot@endlink) Snapshot
          the snapshot   
            
         
        """
        pass
    
    ##  The external snapshots 
    ##  @return snapshot (@link Snapshot List[NXOpen.SIM.Snapshot]@endlink): .
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: None.
    @staticmethod
    def GetExternalSnapshots(builder: LoadSnapshotBuilder) -> List[Snapshot]:
        """
         The external snapshots 
         @return snapshot (@link Snapshot List[NXOpen.SIM.Snapshot]@endlink): .
        """
        pass
    
    ##  Returns the snapshot 
    ##  @return snapshot (@link Snapshot NXOpen.SIM.Snapshot@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.2.  Use new version with few arguments instead.  <br> 

    ## License requirements: None.
    ## <param name="builder"> (@link LoadSnapshotBuilder NXOpen.SIM.LoadSnapshotBuilder@endlink) </param>
    ## <param name="snapshotName"> (str) </param>
    ## <param name="setupName"> (str) </param>
    @overload
    def GetSnapshot(self, builder: LoadSnapshotBuilder, snapshotName: str, setupName: str) -> Snapshot:
        """
         Returns the snapshot 
         @return snapshot (@link Snapshot NXOpen.SIM.Snapshot@endlink): .
        """
        pass
    
    ##  The external snapshot selection
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The blank component where each snapshot is attached 
    def SetExternalSnapshotSelection(builder: LoadSnapshotBuilder, snapshotTags: List[Snapshot], sourceComps: List[str]) -> None:
        """
         The external snapshot selection
        """
        pass
    
import NXOpen
##  This class is used for the Machine Kit Create Dialog.
##         Calling @link Builder::Commit Builder::Commit@endlink  on this
##         builder will start the machine kit creation process
##         and return NULL.
##       <br> Use the @link Part Part@endlink  class to create a MachineKitBuilder object.  <br> 
## 
##   <br>  Created in NX10.0.2  <br> 

class MachineKitBuilder(NXOpen.Builder): 
    """ This class is used for the Machine Kit Create Dialog.
        Calling <ja_method>Builder.Commit</ja_method> on this
        builder will start the machine kit creation process
        and return <ja_NULL>.
     """


    ## Getter for property: (str) Name
    ##   the machine kit name.  
    ##    The name is used for the database entry and the name of the folder.   
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX10.0.2  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
          the machine kit name.  
           The name is used for the database entry and the name of the folder.   
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##   the machine kit name.  
    ##    The name is used for the database entry and the name of the folder.   
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX10.0.2  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
          the machine kit name.  
           The name is used for the database entry and the name of the folder.   
         
        """
        pass
    
    ## Getter for property: (str) OutputDirectory
    ##   the machine kit output directory.  
    ##    This is the location of the machine folder.   
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX10.0.2  <br> 

    ## @return str
    @property
    def OutputDirectory(self) -> str:
        """
        Getter for property: (str) OutputDirectory
          the machine kit output directory.  
           This is the location of the machine folder.   
         
        """
        pass
    
    ## Setter for property: (str) OutputDirectory

    ##   the machine kit output directory.  
    ##    This is the location of the machine folder.   
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX10.0.2  <br> 

    @OutputDirectory.setter
    def OutputDirectory(self, output_directory: str):
        """
        Setter for property: (str) OutputDirectory
          the machine kit output directory.  
           This is the location of the machine folder.   
         
        """
        pass
    
import NXOpen
##  This class is used for the Machine Library Dialog.
##         Calling @link Builder::Commit Builder::Commit@endlink  on this builder will only return NULL.
##       <br> Use the @link Part Part@endlink  class to create a MachineLibraryBuilder object.  <br> 
## 
##   <br>  Created in NX10.0.2  <br> 

class MachineLibraryBuilder(NXOpen.Builder): 
    """ This class is used for the Machine Library Dialog.
        Calling <ja_method>Builder.Commit</ja_method> on this builder will only return <ja_NULL>.
     """


    ##  Edit a specific machine of the database. That will write the machine_database.dat. 
    ## 
    ##   <br>  Created in NX10.0.2  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  machine name (libref)
    def EditMachineLibrary(builder: MachineLibraryBuilder, machineName: str, attName: str, value: str) -> None:
        """
         Edit a specific machine of the database. That will write the machine_database.dat. 
        """
        pass
    
    ##  Returns a array of the library attributes.
    ##             This function allocates the memory for attributeNames. The caller is responsible to deallocate the memory.
    ##  @return attributeNames (List[str]):  array of all attribute names.
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    @staticmethod
    def GetAllAttributeNames(builder: MachineLibraryBuilder) -> List[str]:
        """
         Returns a array of the library attributes.
                    This function allocates the memory for attributeNames. The caller is responsible to deallocate the memory.
         @return attributeNames (List[str]):  array of all attribute names.
        """
        pass
    
    ##  Returns a array of the machine names(librefs) that are in the machine database. 
    ##             This function allocates the memory for machineNames. The caller is responsible to deallocate the memory.
    ##  @return machineNames (List[str]):  array of all machine names (libref).
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    @staticmethod
    def GetAllMachineNames(builder: MachineLibraryBuilder) -> List[str]:
        """
         Returns a array of the machine names(librefs) that are in the machine database. 
                    This function allocates the memory for machineNames. The caller is responsible to deallocate the memory.
         @return machineNames (List[str]):  array of all machine names (libref).
        """
        pass
    
    ##  Returns the attribute value of a specific machine. 
    ##  @return value (str): .
    ## 
    ##   <br>  Created in NX10.0.2  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  machine name (libref)
    def GetValue(builder: MachineLibraryBuilder, machineName: str, attName: str) -> str:
        """
         Returns the attribute value of a specific machine. 
         @return value (str): .
        """
        pass
    
    ##  Insert a machine entry to the machine_database.dat. The libref is the name of the machine entry,
    ##             that is copied, the libref appended by a count and the new entry is put in the list as next entry.
    ##         If the libref is empty, a default entry is add to the bottom of the list. 
    ##  @return machineName (str):  machine name (libref), of the new machien entry.
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  machine name (libref), that will copied
    def InsertEntryToMachineLibrary(builder: MachineLibraryBuilder, selectedMachineName: str) -> str:
        """
         Insert a machine entry to the machine_database.dat. The libref is the name of the machine entry,
                    that is copied, the libref appended by a count and the new entry is put in the list as next entry.
                If the libref is empty, a default entry is add to the bottom of the list. 
         @return machineName (str):  machine name (libref), of the new machien entry.
        """
        pass
    
    ##  Removes a machine entry from the machine_database.dat. The libref is the name of the machine entry,
    ##             that will reomved from the Library. 
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  machine name (libref)
    def RemoveEntryFromMachineLibrary(builder: MachineLibraryBuilder, machineName: str) -> None:
        """
         Removes a machine entry from the machine_database.dat. The libref is the name of the machine entry,
                    that will reomved from the Library. 
        """
        pass
    
import NXOpen
##  Represents a Machine Tool Configuration object.
##      <br> To create a new instance of this class, use @link NXOpen::SIM::KinematicConfigurator::CreateMachineToolConfigurationBuilder  NXOpen::SIM::KinematicConfigurator::CreateMachineToolConfigurationBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.3  <br> 

class MachineToolConfiguration(NXOpen.Builder): 
    """ Represents a Machine Tool Configuration object.
    """


    ##  The controller line 
    ##  The solutionline controller line 
    class ControllerLines(Enum):
        """
        Members Include: <Solutionline> <Powerline>
        """
        Solutionline: int
        Powerline: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MachineToolConfiguration.ControllerLines:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The mdynamics types 
    ##  The Five Axis Milling MDynamics type 
    class MdynamicsTypes(Enum):
        """
        Members Include: <Fiveaxmill>
        """
        Fiveaxmill: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MachineToolConfiguration.MdynamicsTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The plane selection types 
    ##  The operator panel plane type 
    class PlaneTypes(Enum):
        """
        Members Include: <Operator> <G17> <G18> <G19>
        """
        Operator: int
        G17: int
        G18: int
        G19: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MachineToolConfiguration.PlaneTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The machine swiveling types 
    ##  The CYCLE800 swiveling type 
    class SwivelingTypes(Enum):
        """
        Members Include: <Cycle800> <Transarot>
        """
        Cycle800: int
        Transarot: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MachineToolConfiguration.SwivelingTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The machine technology types 
    ##  The mill technology type 
    class TechnologyTypes(Enum):
        """
        Members Include: <Mill> <Turn> <Millturn> <NotSet>
        """
        Mill: int
        Turn: int
        Millturn: int
        NotSet: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MachineToolConfiguration.TechnologyTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The units type 
    ##  The millimeter unit type 
    class UnitTypes(Enum):
        """
        Members Include: <Mm> <In>
        """
        Mm: int
        In: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MachineToolConfiguration.UnitTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link MachineToolConfiguration.ControllerLines NXOpen.SIM.MachineToolConfiguration.ControllerLines@endlink) ControllerLine
    ##   the controller line   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## @return MachineToolConfiguration.ControllerLines
    @property
    def ControllerLine(self) -> MachineToolConfiguration.ControllerLines:
        """
        Getter for property: (@link MachineToolConfiguration.ControllerLines NXOpen.SIM.MachineToolConfiguration.ControllerLines@endlink) ControllerLine
          the controller line   
            
         
        """
        pass
    
    ## Setter for property: (@link MachineToolConfiguration.ControllerLines NXOpen.SIM.MachineToolConfiguration.ControllerLines@endlink) ControllerLine

    ##   the controller line   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    @ControllerLine.setter
    def ControllerLine(self, line: MachineToolConfiguration.ControllerLines):
        """
        Setter for property: (@link MachineToolConfiguration.ControllerLines NXOpen.SIM.MachineToolConfiguration.ControllerLines@endlink) ControllerLine
          the controller line   
            
         
        """
        pass
    
    ## Getter for property: (str) ControllerType
    ##   the controller type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## @return str
    @property
    def ControllerType(self) -> str:
        """
        Getter for property: (str) ControllerType
          the controller type   
            
         
        """
        pass
    
    ## Setter for property: (str) ControllerType

    ##   the controller type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    @ControllerType.setter
    def ControllerType(self, controllerType: str):
        """
        Setter for property: (str) ControllerType
          the controller type   
            
         
        """
        pass
    
    ## Getter for property: (float) CycleTime
    ##   the cycle time   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## @return float
    @property
    def CycleTime(self) -> float:
        """
        Getter for property: (float) CycleTime
          the cycle time   
            
         
        """
        pass
    
    ## Setter for property: (float) CycleTime

    ##   the cycle time   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    @CycleTime.setter
    def CycleTime(self, cycleTime: float):
        """
        Setter for property: (float) CycleTime
          the cycle time   
            
         
        """
        pass
    
    ## Getter for property: (str) MachineName
    ##   the machine name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## @return str
    @property
    def MachineName(self) -> str:
        """
        Getter for property: (str) MachineName
          the machine name   
            
         
        """
        pass
    
    ## Setter for property: (str) MachineName

    ##   the machine name   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    @MachineName.setter
    def MachineName(self, name: str):
        """
        Setter for property: (str) MachineName
          the machine name   
            
         
        """
        pass
    
    ## Getter for property: (str) MachineVendor
    ##   the machine vendor   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## @return str
    @property
    def MachineVendor(self) -> str:
        """
        Getter for property: (str) MachineVendor
          the machine vendor   
            
         
        """
        pass
    
    ## Setter for property: (str) MachineVendor

    ##   the machine vendor   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    @MachineVendor.setter
    def MachineVendor(self, vendor: str):
        """
        Setter for property: (str) MachineVendor
          the machine vendor   
            
         
        """
        pass
    
    ## Getter for property: (str) ToolCarrierName
    ##   the tool carrier name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## @return str
    @property
    def ToolCarrierName(self) -> str:
        """
        Getter for property: (str) ToolCarrierName
          the tool carrier name   
            
         
        """
        pass
    
    ## Setter for property: (str) ToolCarrierName

    ##   the tool carrier name   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    @ToolCarrierName.setter
    def ToolCarrierName(self, carrierName: str):
        """
        Setter for property: (str) ToolCarrierName
          the tool carrier name   
            
         
        """
        pass
    
    ##  Retrieves the archive controller type 
    ##  @return archiveControllerType (int):  The archive controller type .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    @staticmethod
    def GetArchiveControllerType(builder: MachineToolConfiguration) -> int:
        """
         Retrieves the archive controller type 
         @return archiveControllerType (int):  The archive controller type .
        """
        pass
    
    ##  Retrieves the archive controller version 
    ##  @return archiveControllerVersion (str):  The archive controller version .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    @staticmethod
    def GetArchiveControllerVersion(builder: MachineToolConfiguration) -> str:
        """
         Retrieves the archive controller version 
         @return archiveControllerVersion (str):  The archive controller version .
        """
        pass
    
    ##  Retrieves the plane mill from a channel 
    ##  @return planeMill (@link MachineToolConfiguration.PlaneTypes NXOpen.SIM.MachineToolConfiguration.PlaneTypes@endlink):  The plane mill value .
    ## 
    ##   <br>  Created in NX10.0.2  <br> 

    ## License requirements: None.
    ##  The channel in question 
    def GetChannelPlaneMill(builder: MachineToolConfiguration, channelName: str) -> MachineToolConfiguration.PlaneTypes:
        """
         Retrieves the plane mill from a channel 
         @return planeMill (@link MachineToolConfiguration.PlaneTypes NXOpen.SIM.MachineToolConfiguration.PlaneTypes@endlink):  The plane mill value .
        """
        pass
    
    ##  Retrieves the plane turn from a channel 
    ##  @return planeTurn (@link MachineToolConfiguration.PlaneTypes NXOpen.SIM.MachineToolConfiguration.PlaneTypes@endlink):  The plane turn value .
    ## 
    ##   <br>  Created in NX10.0.2  <br> 

    ## License requirements: None.
    ##  The channel in question 
    def GetChannelPlaneTurn(builder: MachineToolConfiguration, channelName: str) -> MachineToolConfiguration.PlaneTypes:
        """
         Retrieves the plane turn from a channel 
         @return planeTurn (@link MachineToolConfiguration.PlaneTypes NXOpen.SIM.MachineToolConfiguration.PlaneTypes@endlink):  The plane turn value .
        """
        pass
    
    ##  Retrieves channel's swiveling mode 
    ##  @return value (@link MachineToolConfiguration.SwivelingTypes NXOpen.SIM.MachineToolConfiguration.SwivelingTypes@endlink):  The swiveling mode value .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  The channel to modify 
    def GetChannelSwiveling(builder: MachineToolConfiguration, channelName: str) -> MachineToolConfiguration.SwivelingTypes:
        """
         Retrieves channel's swiveling mode 
         @return value (@link MachineToolConfiguration.SwivelingTypes NXOpen.SIM.MachineToolConfiguration.SwivelingTypes@endlink):  The swiveling mode value .
        """
        pass
    
    ##  Retrieves machine TCPM support 
    ##  @return value (bool):  The TCPM support value .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  The channel to modify 
    def GetChannelTcpmSupport(builder: MachineToolConfiguration, channelName: str) -> bool:
        """
         Retrieves machine TCPM support 
         @return value (bool):  The TCPM support value .
        """
        pass
    
    ##  Retrieves a channel's subprogram support 
    ##  @return value (bool):  The tool as subprogram mode value .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  The channel to modify 
    def GetChannelToolAsSubprogram(builder: MachineToolConfiguration, channelName: str) -> bool:
        """
         Retrieves a channel's subprogram support 
         @return value (bool):  The tool as subprogram mode value .
        """
        pass
    
    ##  Retrieves a channel's tool command 
    ##  @return toolCommand (str):  The tool command  .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  The channel to modify 
    def GetChannelToolCommand(builder: MachineToolConfiguration, channelName: str) -> str:
        """
         Retrieves a channel's tool command 
         @return toolCommand (str):  The tool command  .
        """
        pass
    
    ##  Retrieves a channel's tool preselect 
    ##  @return toolPreselect (str):  The tool preselect  .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  The channel to modify 
    def GetChannelToolPreselect(builder: MachineToolConfiguration, channelName: str) -> str:
        """
         Retrieves a channel's tool preselect 
         @return toolPreselect (str):  The tool preselect  .
        """
        pass
    
    ##  Retrieves the circular precision 
    ##  @return circularPrecision (float):  The circular precision value .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  The channel to modify 
    def GetCircularPrecision(builder: MachineToolConfiguration, channelName: str) -> float:
        """
         Retrieves the circular precision 
         @return circularPrecision (float):  The circular precision value .
        """
        pass
    
    ##  Retrieves the circular precision factor 
    ##  @return circularPrecisionFactor (float):  The circular precision factor .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  The channel to modify 
    def GetCircularPrecisionFactor(builder: MachineToolConfiguration, channelName: str) -> float:
        """
         Retrieves the circular precision factor 
         @return circularPrecisionFactor (float):  The circular precision factor .
        """
        pass
    
    ##  Retrieves the controller language 
    ##  @return controllerLanguage (str):  The controller language .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    @staticmethod
    def GetControllerLanguage(builder: MachineToolConfiguration) -> str:
        """
         Retrieves the controller language 
         @return controllerLanguage (str):  The controller language .
        """
        pass
    
    ##  Retrieves the controller version 
    ##  @return controllerVersion (str):  The controller version .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    @staticmethod
    def GetControllerVersion(builder: MachineToolConfiguration) -> str:
        """
         Retrieves the controller version 
         @return controllerVersion (str):  The controller version .
        """
        pass
    
    ##  Retrieves the diameter geo axis name, which change the output behavior of length values during turning.
    ##  @return diameterMode (str):  The diameter geo axis name .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ##  The channel to modify 
    def GetDiameterGeoAxisName(builder: MachineToolConfiguration, channelName: str) -> str:
        """
         Retrieves the diameter geo axis name, which change the output behavior of length values during turning.
         @return diameterMode (str):  The diameter geo axis name .
        """
        pass
    
    ##  Retrieves the controller lookahead, which indicates how many lines are evaluate from the controller ahead.
    ##  @return lookAhead (int):  The controller lookahead .
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## License requirements: None.
    ##  The channel to modify 
    def GetLookahead(builder: MachineToolConfiguration, channelName: str) -> int:
        """
         Retrieves the controller lookahead, which indicates how many lines are evaluate from the controller ahead.
         @return lookAhead (int):  The controller lookahead .
        """
        pass
    
    ##  Retrieves the machine technology 
    ##  @return technology (@link MachineToolConfiguration.TechnologyTypes NXOpen.SIM.MachineToolConfiguration.TechnologyTypes@endlink):  The machine technology .
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## License requirements: None.
    ##  The channel to modify 
    def GetMachineTechnology(builder: MachineToolConfiguration, channelName: str) -> MachineToolConfiguration.TechnologyTypes:
        """
         Retrieves the machine technology 
         @return technology (@link MachineToolConfiguration.TechnologyTypes NXOpen.SIM.MachineToolConfiguration.TechnologyTypes@endlink):  The machine technology .
        """
        pass
    
    ##  Retrieve the MDynamics information 
    ##  @return mdynamics (@link MachineToolConfiguration.MdynamicsTypes NXOpen.SIM.MachineToolConfiguration.MdynamicsTypes@endlink):  The mdynamics value .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    @staticmethod
    def GetMdynamics(builder: MachineToolConfiguration) -> MachineToolConfiguration.MdynamicsTypes:
        """
         Retrieve the MDynamics information 
         @return mdynamics (@link MachineToolConfiguration.MdynamicsTypes NXOpen.SIM.MachineToolConfiguration.MdynamicsTypes@endlink):  The mdynamics value .
        """
        pass
    
    ##  Retrieves the degree resolution 
    ##  @return resolutionValue (float):  The degree resolution value .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    @staticmethod
    def GetResolutionDeg(builder: MachineToolConfiguration) -> float:
        """
         Retrieves the degree resolution 
         @return resolutionValue (float):  The degree resolution value .
        """
        pass
    
    ##  Retrieves the millimeter resolution 
    ##  @return resolutionValue (float):  The millimeter resolution value .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    @staticmethod
    def GetResolutionMm(builder: MachineToolConfiguration) -> float:
        """
         Retrieves the millimeter resolution 
         @return resolutionValue (float):  The millimeter resolution value .
        """
        pass
    
    ##  Retrieves the direction selection for a tool carrier. 
    ##  @return directionSelection (int): .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  The channel to which the carrier belongs 
    def GetToolCarrierDirectionSelection(builder: MachineToolConfiguration, channelName: str, carrierName: str) -> int:
        """
         Retrieves the direction selection for a tool carrier. 
         @return directionSelection (int): .
        """
        pass
    
    ##  Retrieves the retraction for a tool carrier. 
    ##  @return retraction (int): .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  The channel to which the carrier belongs 
    def GetToolCarrierRetraction(builder: MachineToolConfiguration, channelName: str, carrierName: str) -> int:
        """
         Retrieves the retraction for a tool carrier. 
         @return retraction (int): .
        """
        pass
    
    ##  Retrieves the swiveling mode for a tool carrier. 
    ##  @return swivelingMode (int): .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  The channel to which the carrier belongs 
    def GetToolCarrierSwivelMode(builder: MachineToolConfiguration, channelName: str, carrierName: str) -> int:
        """
         Retrieves the swiveling mode for a tool carrier. 
         @return swivelingMode (int): .
        """
        pass
    
    ##  Retrieves the X retraction position for a tool carrier. 
    ##  @return xPosition (float): .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  The channel to which the carrier belongs 
    def GetToolCarrierXRetractionPosition(builder: MachineToolConfiguration, channelName: str, carrierName: str) -> float:
        """
         Retrieves the X retraction position for a tool carrier. 
         @return xPosition (float): .
        """
        pass
    
    ##  Retrieves the Y retraction position for a tool carrier. 
    ##  @return yPosition (float): .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  The channel to which the carrier belongs 
    def GetToolCarrierYRetractionPosition(builder: MachineToolConfiguration, channelName: str, carrierName: str) -> float:
        """
         Retrieves the Y retraction position for a tool carrier. 
         @return yPosition (float): .
        """
        pass
    
    ##  Retrieves the Z retraction position for a tool carrier. 
    ##  @return zPosition (float): .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  The channel to which the carrier belongs 
    def GetToolCarrierZRetractionPosition(builder: MachineToolConfiguration, channelName: str, carrierName: str) -> float:
        """
         Retrieves the Z retraction position for a tool carrier. 
         @return zPosition (float): .
        """
        pass
    
    ##  Retrieves the 3D Tool Radius Compensation information 
    ##  @return compensation (bool):  The Tool Radius value .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    @staticmethod
    def GetToolRadiusCompensation(builder: MachineToolConfiguration) -> bool:
        """
         Retrieves the 3D Tool Radius Compensation information 
         @return compensation (bool):  The Tool Radius value .
        """
        pass
    
    ##  Retrieves the used unit 
    ##  @return usedUnit (int):  The used unit .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    @staticmethod
    def GetUsedUnit(builder: MachineToolConfiguration) -> int:
        """
         Retrieves the used unit 
         @return usedUnit (int):  The used unit .
        """
        pass
    
    ##  Sets the archive controller type 
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  The new archive controller type 
    def SetArchiveControllerType(builder: MachineToolConfiguration, newArchiveControllerType: int) -> None:
        """
         Sets the archive controller type 
        """
        pass
    
    ##  Sets the archive controller version 
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  The new archive controller version 
    def SetArchiveControllerVersion(builder: MachineToolConfiguration, newArchiveControllerVersion: str) -> None:
        """
         Sets the archive controller version 
        """
        pass
    
    ##  Sets the plane mill for a channel 
    ## 
    ##   <br>  Created in NX10.0.2  <br> 

    ## License requirements: None.
    ##  The channel to modify 
    def SetChannelPlaneMill(builder: MachineToolConfiguration, channelName: str, newPlaneMill: MachineToolConfiguration.PlaneTypes) -> None:
        """
         Sets the plane mill for a channel 
        """
        pass
    
    ##  Sets the plane turn for a channel 
    ## 
    ##   <br>  Created in NX10.0.2  <br> 

    ## License requirements: None.
    ##  The channel to modify 
    def SetChannelPlaneTurn(builder: MachineToolConfiguration, channelName: str, newPlaneTurn: MachineToolConfiguration.PlaneTypes) -> None:
        """
         Sets the plane turn for a channel 
        """
        pass
    
    ##  Sets the channel's swiveling mode 
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  The channel to modify 
    def SetChannelSwiveling(builder: MachineToolConfiguration, channelName: str, value: MachineToolConfiguration.SwivelingTypes) -> None:
        """
         Sets the channel's swiveling mode 
        """
        pass
    
    ##  Sets the TCPM support value 
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  The channel to modify 
    def SetChannelTcpmSupport(builder: MachineToolConfiguration, channelName: str, value: bool) -> None:
        """
         Sets the TCPM support value 
        """
        pass
    
    ##  Sets a channel's subprogram support 
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  The channel to modify 
    def SetChannelToolAsSubprogram(builder: MachineToolConfiguration, channelName: str, value: bool) -> None:
        """
         Sets a channel's subprogram support 
        """
        pass
    
    ##  Sets a channel's tool command 
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  The channel to modify 
    def SetChannelToolCommand(builder: MachineToolConfiguration, channelName: str, newToolCommand: str) -> None:
        """
         Sets a channel's tool command 
        """
        pass
    
    ##  Sets a channel's tool preselect 
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  The channel to modify 
    def SetChannelToolPreselect(builder: MachineToolConfiguration, channelName: str, newToolPreselect: str) -> None:
        """
         Sets a channel's tool preselect 
        """
        pass
    
    ##  Sets the circular precision 
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  The channel to modify 
    def SetCircularPrecision(builder: MachineToolConfiguration, channelName: str, newCircularPrecision: float) -> None:
        """
         Sets the circular precision 
        """
        pass
    
    ##  Sets the circular precision factor 
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  The channel to modify 
    def SetCircularPrecisionFactor(builder: MachineToolConfiguration, channelName: str, newCircularPrecisionFactor: float) -> None:
        """
         Sets the circular precision factor 
        """
        pass
    
    ##  Sets the controller language 
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  The new controller language 
    def SetControllerLanguage(builder: MachineToolConfiguration, newLanguage: str) -> None:
        """
         Sets the controller language 
        """
        pass
    
    ##  Sets the controller version 
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  The new controller version 
    def SetControllerVersion(builder: MachineToolConfiguration, newVersion: str) -> None:
        """
         Sets the controller version 
        """
        pass
    
    ##  Sets the diameter geo axis name, which change the output behavior of length values during turning.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ##  The channel to modify 
    def SetDiameterGeoAxisName(builder: MachineToolConfiguration, channelName: str, newDiameterMode: str) -> None:
        """
         Sets the diameter geo axis name, which change the output behavior of length values during turning.
        """
        pass
    
    ##  Sets the controller lookahead, which indicates how many lines are evaluate from the controller ahead.
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## License requirements: None.
    ##  The channel to modify 
    def SetLookahead(builder: MachineToolConfiguration, channelName: str, lookAhead: int) -> None:
        """
         Sets the controller lookahead, which indicates how many lines are evaluate from the controller ahead.
        """
        pass
    
    ##  Sets the machine technology 
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## License requirements: None.
    ##  The channel to modify 
    def SetMachineTechnology(builder: MachineToolConfiguration, channelName: str, technology: MachineToolConfiguration.TechnologyTypes) -> None:
        """
         Sets the machine technology 
        """
        pass
    
    ##  Sets the Mdynamics value 
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  The new mdynamics value 
    def SetMdynamics(builder: MachineToolConfiguration, newMDynamicsValue: MachineToolConfiguration.MdynamicsTypes) -> None:
        """
         Sets the Mdynamics value 
        """
        pass
    
    ##  Sets the degree resolution value 
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  The new degree resolution value 
    def SetResolutionDeg(builder: MachineToolConfiguration, newResolutionValue: float) -> None:
        """
         Sets the degree resolution value 
        """
        pass
    
    ##  Sets the millimeter resolution value 
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  The new millimeter resolution value 
    def SetResolutionMm(builder: MachineToolConfiguration, newResolutionValue: float) -> None:
        """
         Sets the millimeter resolution value 
        """
        pass
    
    ##  Sets the direction selection for a tool carrier. 
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  The channel to which the carrier belongs 
    def SetToolCarrierDirectionSelection(builder: MachineToolConfiguration, channelName: str, carrierName: str, newDirectionSelection: int) -> None:
        """
         Sets the direction selection for a tool carrier. 
        """
        pass
    
    ##  Sets the retraction for a tool carrier. 
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  The channel to which the carrier belongs 
    def SetToolCarrierRetraction(builder: MachineToolConfiguration, channelName: str, carrierName: str, newRetraction: int) -> None:
        """
         Sets the retraction for a tool carrier. 
        """
        pass
    
    ##  Sets the swiveling mode for a tool carrier. 
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  The channel to which the carrier belongs 
    def SetToolCarrierSwivelMode(builder: MachineToolConfiguration, channelName: str, carrierName: str, newSwivelingMode: int) -> None:
        """
         Sets the swiveling mode for a tool carrier. 
        """
        pass
    
    ##  Sets the X retraction position for a tool carrier. 
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  The channel to which the carrier belongs 
    def SetToolCarrierXRetractionPosition(builder: MachineToolConfiguration, channelName: str, carrierName: str, newXPosition: float) -> None:
        """
         Sets the X retraction position for a tool carrier. 
        """
        pass
    
    ##  Sets the Y retraction position for a tool carrier. 
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  The channel to which the carrier belongs 
    def SetToolCarrierYRetractionPosition(builder: MachineToolConfiguration, channelName: str, carrierName: str, newYPosition: float) -> None:
        """
         Sets the Y retraction position for a tool carrier. 
        """
        pass
    
    ##  Sets the Z retraction position for a tool carrier. 
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  The channel to which the carrier belongs 
    def SetToolCarrierZRetractionPosition(builder: MachineToolConfiguration, channelName: str, carrierName: str, newZPosition: float) -> None:
        """
         Sets the Z retraction position for a tool carrier. 
        """
        pass
    
    ##  Sets the 3D Tool Radius Compensation information 
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  The new Tool Radius Compensation value 
    def SetToolRadiusCompensation(builder: MachineToolConfiguration, newCompensationValue: bool) -> None:
        """
         Sets the 3D Tool Radius Compensation information 
        """
        pass
    
    ##  Sets the used unit 
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    ##  The new used unit 
    def SetUsedUnit(builder: MachineToolConfiguration, newUsedUnit: int) -> None:
        """
         Sets the used unit 
        """
        pass
    
import NXOpen
##   @brief  Represents the NcChannelSelectionData class object  
## 
##     <br> Use the @link NXOpen::SIM::NcChannelSelectionData NXOpen::SIM::NcChannelSelectionData@endlink  class to create a NcChannelSelectionData object.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class NcChannelSelectionData(NXOpen.NXObject): 
    """ <summary> Represents the NcChannelSelectionData class object </summary>  """


    ##  Assign a file to a channel using the channel number. 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The channel number 
    @overload
    def AssignFile(self, channelData: NcChannelSelectionData, channel: int, file: str) -> None:
        """
         Assign a file to a channel using the channel number. 
        """
        pass
    
    ##  Assign a file to a channel using the channel name. 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The channel name 
    @overload
    def AssignFile(self, channelData: NcChannelSelectionData, channel: str, file: str) -> None:
        """
         Assign a file to a channel using the channel name. 
        """
        pass
    
    ##  Assign an existing main program to a channel using the channel name. 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The channel name 
    def AssignProgram(channelData: NcChannelSelectionData, channel: str, program: NcProgram) -> None:
        """
         Assign an existing main program to a channel using the channel name. 
        """
        pass
    
import NXOpen
##  Represents a NcProgramManagerBuilder builder object.  <br> To create a new instance of this class, use @link NXOpen::SIM::KinematicConfigurator::CreateNcProgramManagerBuilder  NXOpen::SIM::KinematicConfigurator::CreateNcProgramManagerBuilder @endlink  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class NcProgramManagerBuilder(NXOpen.Builder): 
    """ Represents a NcProgramManagerBuilder builder object. """


    ##  Activate all deactivated breakpoints. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    @staticmethod
    def ActivateAllBreakpoints(builder: NcProgramManagerBuilder) -> None:
        """
         Activate all deactivated breakpoints. 
        """
        pass
    
    ##  Activate a breakpoint in a program line. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The program in which the breakpoint is to be activated. 
    def ActivateBreakpoint(builder: NcProgramManagerBuilder, program: NcProgram, lineNumber: int) -> None:
        """
         Activate a breakpoint in a program line. 
        """
        pass
    
    ##  Add a breakpoint to a program line. Simulation stops when it reaches this line.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The program in which the breakpoint is to be added. 
    def AddBreakpoint(builder: NcProgramManagerBuilder, program: NcProgram, lineNumber: int) -> None:
        """
         Add a breakpoint to a program line. Simulation stops when it reaches this line.
        """
        pass
    
    ##  Add a matching breakpoint to program manager. This breakpoint is not associated with a specific program line.
    ##             Simulation stops when the condition string is found in the current program line. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The pattern to look for as a substring in NC program code. 
    def AddMatchingBreakpoint(builder: NcProgramManagerBuilder, condition: str) -> None:
        """
         Add a matching breakpoint to program manager. This breakpoint is not associated with a specific program line.
                    Simulation stops when the condition string is found in the current program line. 
        """
        pass
    
    ##  Deactivate all active breakpoints. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    @staticmethod
    def DeactivateAllBreakpoints(builder: NcProgramManagerBuilder) -> None:
        """
         Deactivate all active breakpoints. 
        """
        pass
    
    ##  Deactivate a breakpoint in a program line. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The program in which the breakpoint is to be deactivated. 
    def DeactivateBreakpoint(builder: NcProgramManagerBuilder, program: NcProgram, lineNumber: int) -> None:
        """
         Deactivate a breakpoint in a program line. 
        """
        pass
    
    ##  Delete all breakpoints. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    @staticmethod
    def DeleteAllBreakpoints(builder: NcProgramManagerBuilder) -> None:
        """
         Delete all breakpoints. 
        """
        pass
    
    ##  Remove a breakpoint from a program line. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The program in which the breakpoint is to be deleted 
    def DeleteBreakpoint(builder: NcProgramManagerBuilder, program: NcProgram, lineNumber: int) -> None:
        """
         Remove a breakpoint from a program line. 
        """
        pass
    
    ##  Get all breakpoints. 
    ##  @return breakpoints (@link Breakpoint List[NXOpen.SIM.Breakpoint]@endlink):  array of all breakpoints .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBreakpoints(builder: NcProgramManagerBuilder) -> List[Breakpoint]:
        """
         Get all breakpoints. 
         @return breakpoints (@link Breakpoint List[NXOpen.SIM.Breakpoint]@endlink):  array of all breakpoints .
        """
        pass
    
    ##  Get the source containing all added programs for external file simulation. 
    ##  @return source (@link NcProgramSource NXOpen.SIM.NcProgramSource@endlink):  source containing all added programs for external file simulation .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    @staticmethod
    def GetExternalFileSource(builder: NcProgramManagerBuilder) -> NcProgramSource:
        """
         Get the source containing all added programs for external file simulation. 
         @return source (@link NcProgramSource NXOpen.SIM.NcProgramSource@endlink):  source containing all added programs for external file simulation .
        """
        pass
    
    ##  Get the source containing all added programs from postprocessor. 
    ##  @return source (@link NcProgramSource NXOpen.SIM.NcProgramSource@endlink):  source containing all added programs from postprocessor .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    @staticmethod
    def GetPostprocessorSource(builder: NcProgramManagerBuilder) -> NcProgramSource:
        """
         Get the source containing all added programs from postprocessor. 
         @return source (@link NcProgramSource NXOpen.SIM.NcProgramSource@endlink):  source containing all added programs from postprocessor .
        """
        pass
    
    ##  Get the source containing all added programs from the CAM Setup location. 
    ##  @return source (@link NcProgramSource NXOpen.SIM.NcProgramSource@endlink):  source containing all added programs from the CAM Setup location .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    @staticmethod
    def GetSetupSource(builder: NcProgramManagerBuilder) -> NcProgramSource:
        """
         Get the source containing all added programs from the CAM Setup location. 
         @return source (@link NcProgramSource NXOpen.SIM.NcProgramSource@endlink):  source containing all added programs from the CAM Setup location .
        """
        pass
    
import NXOpen
##   @brief  Represents the NcProgramSource class object  
## 
##     <br> This object is created by NX.  <br> 
## 
##   <br>  Created in NX12.0.1  <br> 

class NcProgramSource(NXOpen.TaggedObject): 
    """ <summary> Represents the NcProgramSource class object </summary>  """


    ##  Add a Main program to this source.
    ##             This is only allowed on the External File Source.
    ##             This can be requested with @link SIM::NcProgramManagerBuilder::GetExternalFileSource SIM::NcProgramManagerBuilder::GetExternalFileSource@endlink . 
    ##  @return program (@link NcProgram NXOpen.SIM.NcProgram@endlink):  The added program. .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The channel name 
    def AddMainProgram(source: NcProgramSource, channel: str, file: str) -> NcProgram:
        """
         Add a Main program to this source.
                    This is only allowed on the External File Source.
                    This can be requested with @link SIM::NcProgramManagerBuilder::GetExternalFileSource SIM::NcProgramManagerBuilder::GetExternalFileSource@endlink . 
         @return program (@link NcProgram NXOpen.SIM.NcProgram@endlink):  The added program. .
        """
        pass
    
    ##  Add a Subprogram to this source. 
    ##  @return program (@link NcProgram NXOpen.SIM.NcProgram@endlink):  The added program. .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The file to be assigned 
    def AddSubprogram(source: NcProgramSource, file: str) -> NcProgram:
        """
         Add a Subprogram to this source. 
         @return program (@link NcProgram NXOpen.SIM.NcProgram@endlink):  The added program. .
        """
        pass
    
    ##  Create an empty Main program in this source.
    ##             This is only allowed on the External File Source.
    ##             This can be requested with @link SIM::NcProgramManagerBuilder::GetExternalFileSource SIM::NcProgramManagerBuilder::GetExternalFileSource@endlink . 
    ##  @return program (@link NcProgram NXOpen.SIM.NcProgram@endlink):  The created program. .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The channel name 
    def CreateMainProgram(source: NcProgramSource, channel: str, fileName: str) -> NcProgram:
        """
         Create an empty Main program in this source.
                    This is only allowed on the External File Source.
                    This can be requested with @link SIM::NcProgramManagerBuilder::GetExternalFileSource SIM::NcProgramManagerBuilder::GetExternalFileSource@endlink . 
         @return program (@link NcProgram NXOpen.SIM.NcProgram@endlink):  The created program. .
        """
        pass
    
    ##  Delete a program in this source. 
    ##  @return success (bool): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The program to delete. 
    def DeleteProgram(source: NcProgramSource, program: NcProgram) -> bool:
        """
         Delete a program in this source. 
         @return success (bool): .
        """
        pass
    
    ##  Get main program for channel. 
    ##  @return program (@link NcProgram NXOpen.SIM.NcProgram@endlink):  The returned main program. .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The channel name 
    def GetMainProgram(source: NcProgramSource, channel: str) -> NcProgram:
        """
         Get main program for channel. 
         @return program (@link NcProgram NXOpen.SIM.NcProgram@endlink):  The returned main program. .
        """
        pass
    
    ##  Get subprogram with a given ID. 
    ##  @return program (@link NcProgram NXOpen.SIM.NcProgram@endlink):  The returned subprogram. .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The program ID 
    def GetSubprogram(source: NcProgramSource, programId: str) -> NcProgram:
        """
         Get subprogram with a given ID. 
         @return program (@link NcProgram NXOpen.SIM.NcProgram@endlink):  The returned subprogram. .
        """
        pass
    
import NXOpen
##   @brief  Represents the NcProgram class object  
## 
##     <br> Use the @link NXOpen::SIM::NcProgramManagerBuilder NXOpen::SIM::NcProgramManagerBuilder@endlink  class to create a NcProgram object.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class NcProgram(NXOpen.NXObject): 
    """ <summary> Represents the NcProgram class object </summary>  """


    ##  Export program to file. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The file to be exported to 
    def Export(program: NcProgram, file: str) -> None:
        """
         Export program to file. 
        """
        pass
    
    ##  Get the line content of a specific line number. 
    ##  @return lineContent (str):  The content of the specific line .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  the line number of the program (zero based) 
    def GetLine(program: NcProgram, line: int) -> str:
        """
         Get the line content of a specific line number. 
         @return lineContent (str):  The content of the specific line .
        """
        pass
    
    ##  Add a breakpoint. 
    ##  @return breakpoint (@link Breakpoint NXOpen.SIM.Breakpoint@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The line number of the breakpoint (zero based). 
    def InsertBreakpoint(program: NcProgram, line: int) -> Breakpoint:
        """
         Add a breakpoint. 
         @return breakpoint (@link Breakpoint NXOpen.SIM.Breakpoint@endlink): .
        """
        pass
    
import NXOpen
## 
##     Represents a @link NXOpen::SIM::SaveSnapshotBuilder NXOpen::SIM::SaveSnapshotBuilder@endlink 
##      <br> To create a new instance of this class, use @link NXOpen::SIM::KinematicConfigurator::CreateSimulationSavesnapshotBuilder  NXOpen::SIM::KinematicConfigurator::CreateSimulationSavesnapshotBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class SaveSnapshotBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>NXOpen.SIM.SaveSnapshotBuilder</ja_class>
    """


    ##  Sets the source component name 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The source component name 
    def SetSetupName(builder: SaveSnapshotBuilder, name: str) -> None:
        """
         Sets the source component name 
        """
        pass
    
    ##  Sets the snapshot name 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The snapshot name 
    def SetSnapshotName(builder: SaveSnapshotBuilder, name: str) -> None:
        """
         Sets the snapshot name 
        """
        pass
    
import NXOpen
## 
##     Represents a @link NXOpen::SIM::SimDebugBuilder NXOpen::SIM::SimDebugBuilder@endlink 
##      <br> To create a new instance of this class, use @link NXOpen::SIM::KinematicConfigurator::CreateSimDebugBuilder  NXOpen::SIM::KinematicConfigurator::CreateSimDebugBuilder @endlink  <br> 
## 
##   <br>  Created in NX8.0.0  <br> 

class SimDebugBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>NXOpen.SIM.SimDebugBuilder</ja_class>
    """


    ##  Represents the driver type 
    ##  CSE driver 
    class DriverType(Enum):
        """
        Members Include: <Cse> <Mtd>
        """
        Cse: int
        Mtd: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SimDebugBuilder.DriverType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the kinematic model type 
    ##  Main Kinematic Model
    class KinematicModelType(Enum):
        """
        Members Include: <Main> <Simulation> <Driver>
        """
        Main: int
        Simulation: int
        Driver: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SimDebugBuilder.KinematicModelType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The output type 
    ##  Output to syslog 
    class OutputType(Enum):
        """
        Members Include: <Syslog> <ListingWindow> <Autotest> <ToFile>
        """
        Syslog: int
        ListingWindow: int
        Autotest: int
        ToFile: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SimDebugBuilder.OutputType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the printout tags or pointers type 
    ##  Boolean
    class PrintoutTagsOrPointersType(Enum):
        """
        Members Include: <Boolean> <Value> <Name>
        """
        Boolean: int
        Value: int
        Name: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SimDebugBuilder.PrintoutTagsOrPointersType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the trace type 
    ##  Trace Button Down 
    class TraceType(Enum):
        """
        Members Include: <ButtonDown> <Vcr> <Ipw> <Performance> <Collision> <Gouge> <Highlighting> <Details> <PositionalIsv> <SpinningNonSpinning> <KinematicModel> <Event> <LineServer> <Sync> <ToolPathPicking> <CseMotionData> <CseCallStack> <CseToolEvents> <CseCheckSyntax> <ProcessForce> <Findings>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SimDebugBuilder.TraceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the ui type 
    ##  Display Mom Event 
    class UiType(Enum):
        """
        Members Include: <DisplayMomEvent> <ShowPartAndTipJunctions> <GenerateSpinningTools> <UseHybridGougeChecker> <UseMtbOldDialogs> <UseFastTicker> <PrintOutTraceSerialNumbers> <PerformanceDisplayDetail> <PerformanceDisplayTime> <PerformanceIndentTime> <PerformanceDisplayData> <DctkWriteCollisionPairs>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SimDebugBuilder.UiType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link SimDebugBuilder.DriverType NXOpen.SIM.SimDebugBuilder.DriverType@endlink) Driver
    ##   the driver   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return SimDebugBuilder.DriverType
    @property
    def Driver(self) -> SimDebugBuilder.DriverType:
        """
        Getter for property: (@link SimDebugBuilder.DriverType NXOpen.SIM.SimDebugBuilder.DriverType@endlink) Driver
          the driver   
            
         
        """
        pass
    
    ## Setter for property: (@link SimDebugBuilder.DriverType NXOpen.SIM.SimDebugBuilder.DriverType@endlink) Driver

    ##   the driver   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @Driver.setter
    def Driver(self, type: SimDebugBuilder.DriverType):
        """
        Setter for property: (@link SimDebugBuilder.DriverType NXOpen.SIM.SimDebugBuilder.DriverType@endlink) Driver
          the driver   
            
         
        """
        pass
    
    ## Getter for property: (@link SimDebugBuilder.OutputType NXOpen.SIM.SimDebugBuilder.OutputType@endlink) DumpOutput
    ##   the dump output   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return SimDebugBuilder.OutputType
    @property
    def DumpOutput(self) -> SimDebugBuilder.OutputType:
        """
        Getter for property: (@link SimDebugBuilder.OutputType NXOpen.SIM.SimDebugBuilder.OutputType@endlink) DumpOutput
          the dump output   
            
         
        """
        pass
    
    ## Setter for property: (@link SimDebugBuilder.OutputType NXOpen.SIM.SimDebugBuilder.OutputType@endlink) DumpOutput

    ##   the dump output   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @DumpOutput.setter
    def DumpOutput(self, type: SimDebugBuilder.OutputType):
        """
        Setter for property: (@link SimDebugBuilder.OutputType NXOpen.SIM.SimDebugBuilder.OutputType@endlink) DumpOutput
          the dump output   
            
         
        """
        pass
    
    ## Getter for property: (str) DumpToFileName
    ##   the output filename   
    ##     
    ##  
    ## Getter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def DumpToFileName(self) -> str:
        """
        Getter for property: (str) DumpToFileName
          the output filename   
            
         
        """
        pass
    
    ## Setter for property: (str) DumpToFileName

    ##   the output filename   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @DumpToFileName.setter
    def DumpToFileName(self, name: str):
        """
        Setter for property: (str) DumpToFileName
          the output filename   
            
         
        """
        pass
    
    ## Getter for property: (@link SimDebugBuilder.PrintoutTagsOrPointersType NXOpen.SIM.SimDebugBuilder.PrintoutTagsOrPointersType@endlink) PrintoutTags
    ##   the printout tags type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return SimDebugBuilder.PrintoutTagsOrPointersType
    @property
    def PrintoutTags(self) -> SimDebugBuilder.PrintoutTagsOrPointersType:
        """
        Getter for property: (@link SimDebugBuilder.PrintoutTagsOrPointersType NXOpen.SIM.SimDebugBuilder.PrintoutTagsOrPointersType@endlink) PrintoutTags
          the printout tags type   
            
         
        """
        pass
    
    ## Setter for property: (@link SimDebugBuilder.PrintoutTagsOrPointersType NXOpen.SIM.SimDebugBuilder.PrintoutTagsOrPointersType@endlink) PrintoutTags

    ##   the printout tags type   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @PrintoutTags.setter
    def PrintoutTags(self, type: SimDebugBuilder.PrintoutTagsOrPointersType):
        """
        Setter for property: (@link SimDebugBuilder.PrintoutTagsOrPointersType NXOpen.SIM.SimDebugBuilder.PrintoutTagsOrPointersType@endlink) PrintoutTags
          the printout tags type   
            
         
        """
        pass
    
    ##  Gets the trace 
    ##  @return state (bool):  The state.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The trace type
    def GetTrace(data: SimDebugBuilder, type: SimDebugBuilder.TraceType) -> bool:
        """
         Gets the trace 
         @return state (bool):  The state.
        """
        pass
    
    ##  Gets the debug setting 
    ##  @return state (bool):  The state.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  The ui type
    def GetUiSetting(data: SimDebugBuilder, type: SimDebugBuilder.UiType) -> bool:
        """
         Gets the debug setting 
         @return state (bool):  The state.
        """
        pass
    
    ## Sets the trace 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The trace type
    def SetTrace(data: SimDebugBuilder, type: SimDebugBuilder.TraceType, state: bool) -> None:
        """
        Sets the trace 
        """
        pass
    
    ##  Sets the debug setting 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    ##  The ui type
    def SetUiSetting(data: SimDebugBuilder, type: SimDebugBuilder.UiType, state: bool) -> None:
        """
         Sets the debug setting 
        """
        pass
    
import NXOpen
##  This class is used for export a spf file.
##         A call to @link SinumerikCaExportBuilder::ExportSpf  SinumerikCaExportBuilder::ExportSpf @endlink  is used to export a spf file.
##         Calling @link Builder::Commit Builder::Commit@endlink  on this builder will only return NULL.
##      <br> Use the @link NXOpen::Part NXOpen::Part@endlink  class to create a SinumerikCaExportBuilder object.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class SinumerikCaExportBuilder(NXOpen.Builder): 
    """ This class is used for export a spf file.
        A call to <ja_method>SinumerikCaExportBuilder.ExportSpf </ja_method> is used to export a spf file.
        Calling <ja_method>Builder.Commit</ja_method> on this builder will only return <ja_NULL>.
    """


    ## Getter for property: (int) ChainElementIndex
    ##   the index used by chain elements when exporting the SPF file   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def ChainElementIndex(self) -> int:
        """
        Getter for property: (int) ChainElementIndex
          the index used by chain elements when exporting the SPF file   
            
         
        """
        pass
    
    ## Setter for property: (int) ChainElementIndex

    ##   the index used by chain elements when exporting the SPF file   
    ##     
    ##  
    ## Setter License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ChainElementIndex.setter
    def ChainElementIndex(self, index: int):
        """
        Setter for property: (int) ChainElementIndex
          the index used by chain elements when exporting the SPF file   
            
         
        """
        pass
    
    ## Getter for property: (int) CollisionPairIndex
    ##   the index used when exporting collision pairs to the SPF file   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def CollisionPairIndex(self) -> int:
        """
        Getter for property: (int) CollisionPairIndex
          the index used when exporting collision pairs to the SPF file   
            
         
        """
        pass
    
    ## Setter for property: (int) CollisionPairIndex

    ##   the index used when exporting collision pairs to the SPF file   
    ##     
    ##  
    ## Setter License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @CollisionPairIndex.setter
    def CollisionPairIndex(self, index: int):
        """
        Setter for property: (int) CollisionPairIndex
          the index used when exporting collision pairs to the SPF file   
            
         
        """
        pass
    
    ## Getter for property: (bool) DeleteChainsAtStart
    ##   the flag which determines if chains are deleted at the beginning of the export   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def DeleteChainsAtStart(self) -> bool:
        """
        Getter for property: (bool) DeleteChainsAtStart
          the flag which determines if chains are deleted at the beginning of the export   
            
         
        """
        pass
    
    ## Setter for property: (bool) DeleteChainsAtStart

    ##   the flag which determines if chains are deleted at the beginning of the export   
    ##     
    ##  
    ## Setter License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @DeleteChainsAtStart.setter
    def DeleteChainsAtStart(self, deleteChainsAtStart: bool):
        """
        Setter for property: (bool) DeleteChainsAtStart
          the flag which determines if chains are deleted at the beginning of the export   
            
         
        """
        pass
    
    ## Getter for property: (str) FileName
    ##   the output filename of the SPF file   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def FileName(self) -> str:
        """
        Getter for property: (str) FileName
          the output filename of the SPF file   
            
         
        """
        pass
    
    ## Setter for property: (str) FileName

    ##   the output filename of the SPF file   
    ##     
    ##  
    ## Setter License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @FileName.setter
    def FileName(self, name: str):
        """
        Setter for property: (str) FileName
          the output filename of the SPF file   
            
         
        """
        pass
    
    ## Getter for property: (bool) ListOutput
    ##   the flag which determines if the output is printed to a listing window   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def ListOutput(self) -> bool:
        """
        Getter for property: (bool) ListOutput
          the flag which determines if the output is printed to a listing window   
            
         
        """
        pass
    
    ## Setter for property: (bool) ListOutput

    ##   the flag which determines if the output is printed to a listing window   
    ##     
    ##  
    ## Setter License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ListOutput.setter
    def ListOutput(self, output: bool):
        """
        Setter for property: (bool) ListOutput
          the flag which determines if the output is printed to a listing window   
            
         
        """
        pass
    
    ## Getter for property: (int) ProtectionAreaElementIndex
    ##   the index used when exporting protection area elements to the SPF file   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def ProtectionAreaElementIndex(self) -> int:
        """
        Getter for property: (int) ProtectionAreaElementIndex
          the index used when exporting protection area elements to the SPF file   
            
         
        """
        pass
    
    ## Setter for property: (int) ProtectionAreaElementIndex

    ##   the index used when exporting protection area elements to the SPF file   
    ##     
    ##  
    ## Setter License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ProtectionAreaElementIndex.setter
    def ProtectionAreaElementIndex(self, index: int):
        """
        Setter for property: (int) ProtectionAreaElementIndex
          the index used when exporting protection area elements to the SPF file   
            
         
        """
        pass
    
    ## Getter for property: (int) ProtectionAreaIndex
    ##   the index used when exporting protection areas to the SPF file   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def ProtectionAreaIndex(self) -> int:
        """
        Getter for property: (int) ProtectionAreaIndex
          the index used when exporting protection areas to the SPF file   
            
         
        """
        pass
    
    ## Setter for property: (int) ProtectionAreaIndex

    ##   the index used when exporting protection areas to the SPF file   
    ##     
    ##  
    ## Setter License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ProtectionAreaIndex.setter
    def ProtectionAreaIndex(self, index: int):
        """
        Setter for property: (int) ProtectionAreaIndex
          the index used when exporting protection areas to the SPF file   
            
         
        """
        pass
    
    ##  Export to Sinumerik Spf file 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    ##  The name of the node to export to 
    def ExportSpf(builder: SinumerikCaExportBuilder, targetNode: str) -> None:
        """
         Export to Sinumerik Spf file 
        """
        pass
    
import NXOpen
##  This class is used for set the facet tolerance.
##         A call to @link Builder::Commit Builder::Commit@endlink  on this builder will only return NULL.
##      <br> Use the @link Part Part@endlink  class to create a SinumerikCaFacetBuilder object.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class SinumerikCaFacetBuilder(NXOpen.Builder): 
    """ This class is used for set the facet tolerance.
        A call to <ja_method>Builder.Commit</ja_method> on this builder will only return <ja_NULL>.
    """


    ## Getter for property: (float) FacetTolerance
    ##   the facet tolerance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def FacetTolerance(self) -> float:
        """
        Getter for property: (float) FacetTolerance
          the facet tolerance   
            
         
        """
        pass
    
    ## Setter for property: (float) FacetTolerance

    ##   the facet tolerance   
    ##     
    ##  
    ## Setter License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @FacetTolerance.setter
    def FacetTolerance(self, tolerance: float):
        """
        Setter for property: (float) FacetTolerance
          the facet tolerance   
            
         
        """
        pass
    
import NXOpen
##  This class is used for select or unselect component of the placeholder tools.
##         A call to @link Builder::Commit Builder::Commit@endlink  on this builder will only return NULL.
##      <br> Use the @link Part Part@endlink  class to create a SinumerikCaPlaceholderBuilder object.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class SinumerikCaPlaceholderBuilder(NXOpen.Builder): 
    """ This class is used for select or unselect component of the placeholder tools.
        A call to <ja_method>Builder.Commit</ja_method> on this builder will only return <ja_NULL>.
    """


    ##  The select placeholder tools component 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    ##  The selected placeholder component name 
    def SelectComponent(builder: SinumerikCaPlaceholderBuilder, compName: str) -> None:
        """
         The select placeholder tools component 
        """
        pass
    
    ##  The select placeholder tools component 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    ##  The unselected placeholder component name 
    def UnselectComponent(builder: SinumerikCaPlaceholderBuilder, compName: str) -> None:
        """
         The select placeholder tools component 
        """
        pass
    
import NXOpen
##  This class is used for replace geometry.
##         A call to @link SinumerikCaSimplifyBodiesBuilder::DoReplace SinumerikCaSimplifyBodiesBuilder::DoReplace@endlink  will replace the geometry.
##         Calling @link Builder::Commit Builder::Commit@endlink  on this builder will only return NULL.
##      <br> Use the @link Part Part@endlink  class to create a SinumerikCaSimplifyBodiesBuilder object.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class SinumerikCaSimplifyBodiesBuilder(NXOpen.Builder): 
    """ This class is used for replace geometry.
        A call to <ja_method>SinumerikCaSimplifyBodiesBuilder.DoReplace</ja_method> will replace the geometry.
        Calling <ja_method>Builder.Commit</ja_method> on this builder will only return <ja_NULL>.
    """


    ##  Represents the close gap types 
    ##  Sharp 
    class CloseGapTypes(Enum):
        """
        Members Include: <Sharp> <Beveled> <NoOffset>
        """
        Sharp: int
        Beveled: int
        NoOffset: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SinumerikCaSimplifyBodiesBuilder.CloseGapTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The object to replaces with types 
    ##  Nothing 
    class ObjectToReplaceWithTypes(Enum):
        """
        Members Include: <Nothing> <ConvexHull> <BoundingSphere> <BoundingBlock> <BoundingCylinder> <InscribedCylinder>
        """
        Nothing: int
        ConvexHull: int
        BoundingSphere: int
        BoundingBlock: int
        BoundingCylinder: int
        InscribedCylinder: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SinumerikCaSimplifyBodiesBuilder.ObjectToReplaceWithTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) AddOffset
    ##   the  Additional offset.  
    ##    Will expand the wrap.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def AddOffset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) AddOffset
          the  Additional offset.  
           Will expand the wrap.   
         
        """
        pass
    
    ## Getter for property: (bool) Associative
    ##    the Remove parms switch   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
           the Remove parms switch   
            
         
        """
        pass
    
    ## Setter for property: (bool) Associative

    ##    the Remove parms switch   
    ##     
    ##  
    ## Setter License requirements: nx_isv_mtb ("Machine Tool Builder") OR nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Associative.setter
    def Associative(self, associative: bool):
        """
        Setter for property: (bool) Associative
           the Remove parms switch   
            
         
        """
        pass
    
    ## Getter for property: (@link SinumerikCaSimplifyBodiesBuilder.CloseGapTypes NXOpen.SIM.SinumerikCaSimplifyBodiesBuilder.CloseGapTypes@endlink) CloseGaps
    ##   the  Method used to close the gaps after offset of the wrap   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return SinumerikCaSimplifyBodiesBuilder.CloseGapTypes
    @property
    def CloseGaps(self) -> SinumerikCaSimplifyBodiesBuilder.CloseGapTypes:
        """
        Getter for property: (@link SinumerikCaSimplifyBodiesBuilder.CloseGapTypes NXOpen.SIM.SinumerikCaSimplifyBodiesBuilder.CloseGapTypes@endlink) CloseGaps
          the  Method used to close the gaps after offset of the wrap   
            
         
        """
        pass
    
    ## Setter for property: (@link SinumerikCaSimplifyBodiesBuilder.CloseGapTypes NXOpen.SIM.SinumerikCaSimplifyBodiesBuilder.CloseGapTypes@endlink) CloseGaps

    ##   the  Method used to close the gaps after offset of the wrap   
    ##     
    ##  
    ## Setter License requirements: nx_isv_mtb ("Machine Tool Builder") OR nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @CloseGaps.setter
    def CloseGaps(self, closeGaps: SinumerikCaSimplifyBodiesBuilder.CloseGapTypes):
        """
        Setter for property: (@link SinumerikCaSimplifyBodiesBuilder.CloseGapTypes NXOpen.SIM.SinumerikCaSimplifyBodiesBuilder.CloseGapTypes@endlink) CloseGaps
          the  Method used to close the gaps after offset of the wrap   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) CoordSystem
    ##   the coordinate system   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.CoordinateSystem
    @property
    def CoordSystem(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) CoordSystem
          the coordinate system   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) CoordSystem

    ##   the coordinate system   
    ##     
    ##  
    ## Setter License requirements: nx_isv_mtb ("Machine Tool Builder") OR nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @CoordSystem.setter
    def CoordSystem(self, coordSystem: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) CoordSystem
          the coordinate system   
            
         
        """
        pass
    
    ## Getter for property: (float) DistanceTolerance
    ##   the Distance tolerance used to facet the solids.  
    ##    Also used for default offset calculation.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
          the Distance tolerance used to facet the solids.  
           Also used for default offset calculation.   
         
        """
        pass
    
    ## Setter for property: (float) DistanceTolerance

    ##   the Distance tolerance used to facet the solids.  
    ##    Also used for default offset calculation.   
    ##  
    ## Setter License requirements: nx_isv_mtb ("Machine Tool Builder") OR nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @DistanceTolerance.setter
    def DistanceTolerance(self, distTol: float):
        """
        Setter for property: (float) DistanceTolerance
          the Distance tolerance used to facet the solids.  
           Also used for default offset calculation.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) ObjectToReplace
    ##   the object to replace   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def ObjectToReplace(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) ObjectToReplace
          the object to replace   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.PlaneList NXOpen.PlaneList@endlink) PlanesList
    ##   the Planes to split the geometry, tightens the wrap along this plane   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.PlaneList
    @property
    def PlanesList(self) -> NXOpen.PlaneList:
        """
        Getter for property: (@link NXOpen.PlaneList NXOpen.PlaneList@endlink) PlanesList
          the Planes to split the geometry, tightens the wrap along this plane   
            
         
        """
        pass
    
    ## Getter for property: (@link SinumerikCaSimplifyBodiesBuilder.ObjectToReplaceWithTypes NXOpen.SIM.SinumerikCaSimplifyBodiesBuilder.ObjectToReplaceWithTypes@endlink) ReplaceWith
    ##   the object to replace with   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return SinumerikCaSimplifyBodiesBuilder.ObjectToReplaceWithTypes
    @property
    def ReplaceWith(self) -> SinumerikCaSimplifyBodiesBuilder.ObjectToReplaceWithTypes:
        """
        Getter for property: (@link SinumerikCaSimplifyBodiesBuilder.ObjectToReplaceWithTypes NXOpen.SIM.SinumerikCaSimplifyBodiesBuilder.ObjectToReplaceWithTypes@endlink) ReplaceWith
          the object to replace with   
            
         
        """
        pass
    
    ## Setter for property: (@link SinumerikCaSimplifyBodiesBuilder.ObjectToReplaceWithTypes NXOpen.SIM.SinumerikCaSimplifyBodiesBuilder.ObjectToReplaceWithTypes@endlink) ReplaceWith

    ##   the object to replace with   
    ##     
    ##  
    ## Setter License requirements: nx_isv_mtb ("Machine Tool Builder") OR nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ReplaceWith.setter
    def ReplaceWith(self, objectToReplaceWith: SinumerikCaSimplifyBodiesBuilder.ObjectToReplaceWithTypes):
        """
        Setter for property: (@link SinumerikCaSimplifyBodiesBuilder.ObjectToReplaceWithTypes NXOpen.SIM.SinumerikCaSimplifyBodiesBuilder.ObjectToReplaceWithTypes@endlink) ReplaceWith
          the object to replace with   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SplitOffset
    ##   the Offset applied to both sides of the splitting planes.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SplitOffset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SplitOffset
          the Offset applied to both sides of the splitting planes.  
             
         
        """
        pass
    
    ##  Replace the simplify bodies 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_isv_mtb ("Machine Tool Builder") OR nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    @staticmethod
    def DoReplace(builder: SinumerikCaSimplifyBodiesBuilder) -> None:
        """
         Replace the simplify bodies 
        """
        pass
    
import NXOpen
## 
##     Represents a @link SIM::SmkDebugBuilder SIM::SmkDebugBuilder@endlink 
##      <br> To create a new instance of this class, use @link NXOpen::SIM::KinematicConfigurator::CreateSmkDebugBuilder  NXOpen::SIM::KinematicConfigurator::CreateSmkDebugBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class SmkDebugBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>SIM.SmkDebugBuilder</ja_class>
    """


    ##  Represents the dump type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ## </description> </item><item><term> 
    ## MachineKit</term><description> 
    ## </description> </item></list>
    class DumpType(Enum):
        """
        Members Include: <NotSet> <MachineKit>
        """
        NotSet: int
        MachineKit: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SmkDebugBuilder.DumpType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The output type 
    ##  Output to syslog 
    class OutputType(Enum):
        """
        Members Include: <Syslog> <ListingWindow> <Autotest> <ToFile>
        """
        Syslog: int
        ListingWindow: int
        Autotest: int
        ToFile: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SmkDebugBuilder.OutputType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) OutputFile
    ##   the output file   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return str
    @property
    def OutputFile(self) -> str:
        """
        Getter for property: (str) OutputFile
          the output file   
            
         
        """
        pass
    
    ## Setter for property: (str) OutputFile

    ##   the output file   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @OutputFile.setter
    def OutputFile(self, outputFile: str):
        """
        Setter for property: (str) OutputFile
          the output file   
            
         
        """
        pass
    
    ## Getter for property: (str) PartFolder
    ##   the part folder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return str
    @property
    def PartFolder(self) -> str:
        """
        Getter for property: (str) PartFolder
          the part folder   
            
         
        """
        pass
    
    ## Setter for property: (str) PartFolder

    ##   the part folder   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @PartFolder.setter
    def PartFolder(self, partFolder: str):
        """
        Setter for property: (str) PartFolder
          the part folder   
            
         
        """
        pass
    
    ##  Export geometry information 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The part folder 
    def ExportGeometryInformation(data: SmkDebugBuilder, partFolder: str, outputFile: str) -> None:
        """
         Export geometry information 
        """
        pass
    
import NXOpen
##   @brief  Represents the SmkLicenseCensorBuilder class object  
## 
##     <br> Use the @link NXOpen::SIM::KinematicConfigurator NXOpen::SIM::KinematicConfigurator@endlink  class to create a SmkLicenseCensorBuilder object.  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class SmkLicenseCensorBuilder(NXOpen.Builder): 
    """ <summary> Represents the SmkLicenseCensorBuilder class object </summary>  """
    pass


import NXOpen
##   @brief  Represents the SmkMachineKitEditorBuilder class object  
## 
##     <br> Use the @link NXOpen::SIM::KinematicConfigurator NXOpen::SIM::KinematicConfigurator@endlink  class to create a SmkMachineKitEditorBuilder object.  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class SmkMachineKitEditorBuilder(NXOpen.Builder): 
    """ <summary> Represents the SmkMachineKitEditorBuilder class object </summary>  """


    ##  The data classification 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## General</term><description> 
    ## </description> </item><item><term> 
    ## Post</term><description> 
    ## </description> </item><item><term> 
    ## Sim</term><description> 
    ## </description> </item><item><term> 
    ## PostAndSim</term><description> 
    ## </description> </item><item><term> 
    ## Nc</term><description> 
    ## </description> </item></list>
    class DataClassification(Enum):
        """
        Members Include: <General> <Post> <Sim> <PostAndSim> <Nc>
        """
        General: int
        Post: int
        Sim: int
        PostAndSim: int
        Nc: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SmkMachineKitEditorBuilder.DataClassification:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The data type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## String</term><description> 
    ## </description> </item><item><term> 
    ## Int</term><description> 
    ## </description> </item><item><term> 
    ## Double</term><description> 
    ## </description> </item><item><term> 
    ## Enum</term><description> 
    ## </description> </item><item><term> 
    ## MultiString</term><description> 
    ## </description> </item></list>
    class DataType(Enum):
        """
        Members Include: <String> <Int> <Double> <Enum> <MultiString>
        """
        String: int
        Int: int
        Double: int
        Enum: int
        MultiString: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SmkMachineKitEditorBuilder.DataType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The parameters machine mode 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## All</term><description> 
    ## </description> </item><item><term> 
    ## Mill</term><description> 
    ## </description> </item><item><term> 
    ## Lathe</term><description> 
    ## </description> </item><item><term> 
    ## Drill</term><description> 
    ## </description> </item><item><term> 
    ## Wedm</term><description> 
    ## </description> </item><item><term> 
    ## Laser</term><description> 
    ## </description> </item></list>
    class ParametersMachineMode(Enum):
        """
        Members Include: <All> <Mill> <Lathe> <Drill> <Wedm> <Laser>
        """
        All: int
        Mill: int
        Lathe: int
        Drill: int
        Wedm: int
        Laser: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SmkMachineKitEditorBuilder.ParametersMachineMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Adds a new attribute item 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The attribute fullname 
    def AddAttribute(builder: SmkMachineKitEditorBuilder, attributeFullname: str) -> None:
        """
         Adds a new attribute item 
        """
        pass
    
    ##  Adds parameters machine mode 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The attribute fullname 
    def AddParametersMachineMode(builder: SmkMachineKitEditorBuilder, attributeFullname: str, machineMode: SmkMachineKitEditorBuilder.ParametersMachineMode) -> None:
        """
         Adds parameters machine mode 
        """
        pass
    
    ##  Clears parameters machine mode 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The attribute fullname 
    def ClearParametersMachineMode(builder: SmkMachineKitEditorBuilder, attributeFullname: str) -> None:
        """
         Clears parameters machine mode 
        """
        pass
    
    ##  Deletes the attribute item 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The attribute fullname 
    def DeleteAttribute(builder: SmkMachineKitEditorBuilder, attributeFullname: str) -> None:
        """
         Deletes the attribute item 
        """
        pass
    
    ##  Gets  
    ##  @return classification (@link SmkMachineKitEditorBuilder.DataClassification NXOpen.SIM.SmkMachineKitEditorBuilder.DataClassification@endlink):  The attribute classification .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ##  The attribute fullname 
    def GetAttributeClassification(builder: SmkMachineKitEditorBuilder, attributeFullname: str) -> SmkMachineKitEditorBuilder.DataClassification:
        """
         Gets  
         @return classification (@link SmkMachineKitEditorBuilder.DataClassification NXOpen.SIM.SmkMachineKitEditorBuilder.DataClassification@endlink):  The attribute classification .
        """
        pass
    
    ##  Gets  
    ##  @return type (@link SmkMachineKitEditorBuilder.DataType NXOpen.SIM.SmkMachineKitEditorBuilder.DataType@endlink):  The attribute type .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ##  The attribute fullname 
    def GetAttributeType(builder: SmkMachineKitEditorBuilder, attributeFullname: str) -> SmkMachineKitEditorBuilder.DataType:
        """
         Gets  
         @return type (@link SmkMachineKitEditorBuilder.DataType NXOpen.SIM.SmkMachineKitEditorBuilder.DataType@endlink):  The attribute type .
        """
        pass
    
    ##  Gets  
    ##  @return variableName (str):  The attribute variable name .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ##  The attribute fullname 
    def GetAttributeVariableName(builder: SmkMachineKitEditorBuilder, attributeFullname: str) -> str:
        """
         Gets  
         @return variableName (str):  The attribute variable name .
        """
        pass
    
    ##  Gets  
    ##  @return value (float):  The attribute value .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ##  The attribute fullname 
    def GetDoubleAttribute(builder: SmkMachineKitEditorBuilder, attributeFullname: str) -> float:
        """
         Gets  
         @return value (float):  The attribute value .
        """
        pass
    
    ##  Gets  
    ##  @return A tuple consisting of (currentValue, values). 
    ##  - currentValue is: str. The attribute value    .
    ##  - values is: List[str]. options for enum       .

    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ##  The attribute fullname 
    @staticmethod
    def GetEnumAttribute(builder: SmkMachineKitEditorBuilder, attributeFullname: str) -> Tuple[str, List[str]]:
        """
         Gets  
         @return A tuple consisting of (currentValue, values). 
         - currentValue is: str. The attribute value    .
         - values is: List[str]. options for enum       .

        """
        pass
    
    ##  Gets the event classification  
    ##  @return eventClassification (int):  The event classification .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ##  The attribute fullname 
    def GetEventClassification(builder: SmkMachineKitEditorBuilder, attributeFullname: str) -> int:
        """
         Gets the event classification  
         @return eventClassification (int):  The event classification .
        """
        pass
    
    ##  Gets  
    ##  @return value (int):  The attribute value .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ##  The attribute fullname 
    def GetIntegerAttribute(builder: SmkMachineKitEditorBuilder, attributeFullname: str) -> int:
        """
         Gets  
         @return value (int):  The attribute value .
        """
        pass
    
    ##  Gets the machine mode 
    ##  @return machineMode (int):  The machine mode .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ##  The attribute fullname 
    def GetMachineMode(builder: SmkMachineKitEditorBuilder, attributeFullname: str) -> int:
        """
         Gets the machine mode 
         @return machineMode (int):  The machine mode .
        """
        pass
    
    ##  Gets  
    ##  @return value (List[str]):  The attribute value    .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ##  The attribute fullname 
    def GetMultiStringAttribute(builder: SmkMachineKitEditorBuilder, attributeFullname: str) -> List[str]:
        """
         Gets  
         @return value (List[str]):  The attribute value    .
        """
        pass
    
    ##  Gets  
    ##  @return value (str):  The attribute value .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ##  The attribute fullname 
    def GetStringAttribute(builder: SmkMachineKitEditorBuilder, attributeFullname: str) -> str:
        """
         Gets  
         @return value (str):  The attribute value .
        """
        pass
    
    ##  Asks if the attribute exists 
    ##  @return exists (bool):  The attribute exsitence .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ##  The attribute fullname 
    def HasAttribute(builder: SmkMachineKitEditorBuilder, attributeFullname: str) -> bool:
        """
         Asks if the attribute exists 
         @return exists (bool):  The attribute exsitence .
        """
        pass
    
    ##  Sets the attribute classification 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The attribute fullname 
    def SetAttributeClassification(builder: SmkMachineKitEditorBuilder, attributeFullname: str, classification: SmkMachineKitEditorBuilder.DataClassification) -> None:
        """
         Sets the attribute classification 
        """
        pass
    
    ##  Sets the attribute name 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The attribute fullname 
    def SetAttributeName(builder: SmkMachineKitEditorBuilder, attributeFullname: str, newName: str) -> None:
        """
         Sets the attribute name 
        """
        pass
    
    ##  Sets the attribute type 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The attribute fullname 
    def SetAttributeType(builder: SmkMachineKitEditorBuilder, attributeFullname: str, type: SmkMachineKitEditorBuilder.DataType) -> None:
        """
         Sets the attribute type 
        """
        pass
    
    ##  Sets the variable name 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The attribute fullname 
    def SetAttributeVariableName(builder: SmkMachineKitEditorBuilder, attributeFullname: str, variableName: str) -> None:
        """
         Sets the variable name 
        """
        pass
    
    ##  Sets the double attribute value 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The attribute fullname 
    def SetDoubleAttribute(builder: SmkMachineKitEditorBuilder, attributeFullname: str, value: float) -> None:
        """
         Sets the double attribute value 
        """
        pass
    
    ##  Sets the double attribute value 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The attribute fullname 
    def SetEnumAttribute(builder: SmkMachineKitEditorBuilder, attributeFullname: str, value: str) -> None:
        """
         Sets the double attribute value 
        """
        pass
    
    ##  Sets the event classification 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The attribute fullname 
    def SetEventClassification(builder: SmkMachineKitEditorBuilder, attributeFullname: str, eventClassification: int) -> None:
        """
         Sets the event classification 
        """
        pass
    
    ##  Sets the double attribute value 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The attribute fullname 
    def SetIntegerAttribute(builder: SmkMachineKitEditorBuilder, attributeFullname: str, value: int) -> None:
        """
         Sets the double attribute value 
        """
        pass
    
    ##  Sets the machine mode 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The attribute fullname 
    def SetMachineMode(builder: SmkMachineKitEditorBuilder, attributeFullname: str, machineMode: int) -> None:
        """
         Sets the machine mode 
        """
        pass
    
    ##  Sets the multi string attribute values 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The attribute fullname 
    def SetMultiStringAttribute(builder: SmkMachineKitEditorBuilder, attributeFullname: str, values: List[str]) -> None:
        """
         Sets the multi string attribute values 
        """
        pass
    
    ##  Sets the string attribute value 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The attribute fullname 
    def SetStringAttribute(builder: SmkMachineKitEditorBuilder, attributeFullname: str, value: str) -> None:
        """
         Sets the string attribute value 
        """
        pass
    
import NXOpen
##   @brief  Represents the SmkTransitionPathEditorBuilder class object  
## 
##     <br> Use the @link NXOpen::SIM::KinematicConfigurator NXOpen::SIM::KinematicConfigurator@endlink  class to create a SmkTransitionPathEditorBuilder object.  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class SmkTransitionPathEditorBuilder(NXOpen.Builder): 
    """ <summary> Represents the SmkTransitionPathEditorBuilder class object </summary>  """


    ##  The template location 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## FromKinematic</term><description> 
    ## </description> </item><item><term> 
    ## FromOtherPart</term><description> 
    ## </description> </item></list>
    class TemplateLocation(Enum):
        """
        Members Include: <FromKinematic> <FromOtherPart>
        """
        FromKinematic: int
        FromOtherPart: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SmkTransitionPathEditorBuilder.TemplateLocation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The template type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Before</term><description> 
    ## </description> </item><item><term> 
    ## Between</term><description> 
    ## </description> </item><item><term> 
    ## After</term><description> 
    ## </description> </item><item><term> 
    ## BetweenNCM</term><description> 
    ## </description> </item></list>
    class TemplateType(Enum):
        """
        Members Include: <Before> <Between> <After> <BetweenNCM>
        """
        Before: int
        Between: int
        After: int
        BetweenNCM: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SmkTransitionPathEditorBuilder.TemplateType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Gets the template file path 
    ##  @return filePath (str):  The template file path .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2212.0.0.  It is not supported anymore.  <br> 

    ## License requirements: None.
    @staticmethod
    def GetTemplateFilePath(builder: SmkTransitionPathEditorBuilder) -> str:
        """
         Gets the template file path 
         @return filePath (str):  The template file path .
        """
        pass
    
    ##  Gets the template location 
    ##  @return templateLocation (@link SmkTransitionPathEditorBuilder.TemplateLocation NXOpen.SIM.SmkTransitionPathEditorBuilder.TemplateLocation@endlink):  The template location .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2212.0.0.  It is not supported anymore.  <br> 

    ## License requirements: None.
    @staticmethod
    def GetTemplateLocation(builder: SmkTransitionPathEditorBuilder) -> SmkTransitionPathEditorBuilder.TemplateLocation:
        """
         Gets the template location 
         @return templateLocation (@link SmkTransitionPathEditorBuilder.TemplateLocation NXOpen.SIM.SmkTransitionPathEditorBuilder.TemplateLocation@endlink):  The template location .
        """
        pass
    
    ##  Gets the template type 
    ##  @return templateType (@link SmkTransitionPathEditorBuilder.TemplateType NXOpen.SIM.SmkTransitionPathEditorBuilder.TemplateType@endlink):  The template type .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2212.0.0.  It is not supported anymore.  <br> 

    ## License requirements: None.
    @staticmethod
    def GetTemplateType(builder: SmkTransitionPathEditorBuilder) -> SmkTransitionPathEditorBuilder.TemplateType:
        """
         Gets the template type 
         @return templateType (@link SmkTransitionPathEditorBuilder.TemplateType NXOpen.SIM.SmkTransitionPathEditorBuilder.TemplateType@endlink):  The template type .
        """
        pass
    
    ##  Import from default template 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    @staticmethod
    def ImportDefaultTemplate(builder: SmkTransitionPathEditorBuilder) -> None:
        """
         Import from default template 
        """
        pass
    
    ##  Import from other machine 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The template file path 
    def ImportFromOtherMachine(builder: SmkTransitionPathEditorBuilder, filePath: str) -> None:
        """
         Import from other machine 
        """
        pass
    
    ##  Sets the template file path 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2212.0.0.  It is not supported anymore.  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The template file path 
    def SetTemplateFilePath(builder: SmkTransitionPathEditorBuilder, filePath: str) -> None:
        """
         Sets the template file path 
        """
        pass
    
    ##  Sets the template location 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2212.0.0.  It is not supported anymore.  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The template location 
    def SetTemplateLocation(builder: SmkTransitionPathEditorBuilder, templateLocation: SmkTransitionPathEditorBuilder.TemplateLocation) -> None:
        """
         Sets the template location 
        """
        pass
    
    ##  Sets the template type 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2212.0.0.  It is not supported anymore.  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The template type 
    def SetTemplateType(builder: SmkTransitionPathEditorBuilder, templateType: SmkTransitionPathEditorBuilder.TemplateType) -> None:
        """
         Sets the template type 
        """
        pass
    
import NXOpen
import NXOpen.SIM.PostConfigurator
##   @brief  Represents the SimSmkWizardBuilder class object  
## 
##     <br> Use the @link NXOpen::SIM::KinematicConfigurator NXOpen::SIM::KinematicConfigurator@endlink  class to create a SmkWizardBuilder object.  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class SmkWizardBuilder(NXOpen.Builder): 
    """ <summary> Represents the SimSmkWizardBuilder class object </summary>  """


    ##  The archieve file type 
    ##  no archieve file 
    class ArchieveFileType(Enum):
        """
        Members Include: <NotSet> <Specify>
        """
        NotSet: int
        Specify: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SmkWizardBuilder.ArchieveFileType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The axis direction type 
    ##  positive X-axis 
    class AxisDirectionType(Enum):
        """
        Members Include: <PositiveX> <NegativeX> <PositiveY> <NegativeY> <PositiveZ> <NegativeZ>
        """
        PositiveX: int
        NegativeX: int
        PositiveY: int
        NegativeY: int
        PositiveZ: int
        NegativeZ: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SmkWizardBuilder.AxisDirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The axis motions type 
    ##  linear axis    
    class AxisMotionType(Enum):
        """
        Members Include: <Linear> <Rotary> <RotaryUnlimited> <Spindle>
        """
        Linear: int
        Rotary: int
        RotaryUnlimited: int
        Spindle: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SmkWizardBuilder.AxisMotionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The component classification 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Turret</term><description> 
    ## </description> </item><item><term> 
    ## Pocket</term><description> 
    ## </description> </item><item><term> 
    ## PocketOnHead</term><description> 
    ## </description> </item><item><term> 
    ## Part</term><description> 
    ## </description> </item><item><term> 
    ## Workpiece</term><description> 
    ## </description> </item><item><term> 
    ## AdditiveMaterial</term><description> 
    ## </description> </item><item><term> 
    ## SetupElement</term><description> 
    ## </description> </item><item><term> 
    ## LatheSpindle</term><description> 
    ## </description> </item><item><term> 
    ## ToolCutting</term><description> 
    ## </description> </item><item><term> 
    ## ToolNonCutting</term><description> 
    ## </description> </item><item><term> 
    ## Head</term><description> 
    ## </description> </item><item><term> 
    ## ToolTurret</term><description> 
    ## </description> </item><item><term> 
    ## Magazine</term><description> 
    ## </description> </item><item><term> 
    ## ToolSpindle</term><description> 
    ## </description> </item><item><term> 
    ## LocationPocket</term><description> 
    ## </description> </item><item><term> 
    ## AssignablePocket</term><description> 
    ## </description> </item><item><term> 
    ## WorkHolder</term><description> 
    ## </description> </item><item><term> 
    ## ToolHolder</term><description> 
    ## </description> </item><item><term> 
    ## Setup</term><description> 
    ## </description> </item></list>
    class ComponentClassificationType(Enum):
        """
        Members Include: <Turret> <Pocket> <PocketOnHead> <Part> <Workpiece> <AdditiveMaterial> <SetupElement> <LatheSpindle> <ToolCutting> <ToolNonCutting> <Head> <ToolTurret> <Magazine> <ToolSpindle> <LocationPocket> <AssignablePocket> <WorkHolder> <ToolHolder> <Setup>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SmkWizardBuilder.ComponentClassificationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The coordinate reference type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Absolute</term><description> 
    ## </description> </item><item><term> 
    ## MachineZero</term><description> 
    ## </description> </item></list>
    class CoordinateReferenceType(Enum):
        """
        Members Include: <Absolute> <MachineZero>
        """
        Absolute: int
        MachineZero: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SmkWizardBuilder.CoordinateReferenceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The device template type 
    ##  no special device   
    class DeviceTemplateType(Enum):
        """
        Members Include: <NotSet> <Specify>
        """
        NotSet: int
        Specify: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SmkWizardBuilder.DeviceTemplateType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The junction classification 
    ##  no specal class 
    class JunctionClassificationType(Enum):
        """
        Members Include: <NotSet> <ToolMount> <MachineZero> <LatheWpZx> <LatheWpXy> <HeadMount>
        """
        NotSet: int
        ToolMount: int
        MachineZero: int
        LatheWpZx: int
        LatheWpXy: int
        HeadMount: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SmkWizardBuilder.JunctionClassificationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The kinematics version type 
    ##  Classic kinematics model 
    class KinematicsVersionType(Enum):
        """
        Members Include: <Classic> <Mpp>
        """
        Classic: int
        Mpp: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SmkWizardBuilder.KinematicsVersionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The machine type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Mill</term><description> 
    ## </description> </item><item><term> 
    ## Turnmill</term><description> 
    ## </description> </item><item><term> 
    ## Lathe</term><description> 
    ## </description> </item><item><term> 
    ## Millturn</term><description> 
    ## </description> </item><item><term> 
    ## Wedm</term><description> 
    ## </description> </item><item><term> 
    ## Robot</term><description> 
    ## </description> </item><item><term> 
    ## Generic</term><description> 
    ## </description> </item></list>
    class MachineType(Enum):
        """
        Members Include: <Mill> <Turnmill> <Lathe> <Millturn> <Wedm> <Robot> <Generic>
        """
        Mill: int
        Turnmill: int
        Lathe: int
        Millturn: int
        Wedm: int
        Robot: int
        Generic: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SmkWizardBuilder.MachineType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The machine kit output type 
    ##  current installed machines folder 
    class OutputType(Enum):
        """
        Members Include: <InstalledMachines> <Mtk>
        """
        InstalledMachines: int
        Mtk: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SmkWizardBuilder.OutputType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The pocket transform type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## TranslateDelta</term><description> 
    ## </description> </item><item><term> 
    ## TranslateToPoint</term><description> 
    ## </description> </item><item><term> 
    ## RotateTwoPoint</term><description> 
    ## </description> </item><item><term> 
    ## RotatePointVector</term><description> 
    ## </description> </item></list>
    class PocketTransformType(Enum):
        """
        Members Include: <TranslateDelta> <TranslateToPoint> <RotateTwoPoint> <RotatePointVector>
        """
        TranslateDelta: int
        TranslateToPoint: int
        RotateTwoPoint: int
        RotatePointVector: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SmkWizardBuilder.PocketTransformType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The pocket register type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## SameAsHolderId</term><description> 
    ## </description> </item><item><term> 
    ## Specify</term><description> 
    ## </description> </item></list>
    class RegisterType(Enum):
        """
        Members Include: <SameAsHolderId> <Specify>
        """
        SameAsHolderId: int
        Specify: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SmkWizardBuilder.RegisterType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The wizard step 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## TemplateSelection</term><description> 
    ## </description> </item><item><term> 
    ## GeometrySelection</term><description> 
    ## </description> </item><item><term> 
    ## JunctionSelection</term><description> 
    ## </description> </item><item><term> 
    ## AxisDefinition</term><description> 
    ## </description> </item><item><term> 
    ## ChainConfiguration</term><description> 
    ## </description> </item><item><term> 
    ## ChannelConfiguration</term><description> 
    ## </description> </item><item><term> 
    ## MachineToolDataDefinition</term><description> 
    ## </description> </item><item><term> 
    ## CsePostSelection</term><description> 
    ## </description> </item><item><term> 
    ## OutputSelection</term><description> 
    ## </description> </item></list>
    class WizardStep(Enum):
        """
        Members Include: <TemplateSelection> <GeometrySelection> <JunctionSelection> <AxisDefinition> <ChainConfiguration> <ChannelConfiguration> <MachineToolDataDefinition> <CsePostSelection> <OutputSelection>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SmkWizardBuilder.WizardStep:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link SmkWizardBuilder.ArchieveFileType NXOpen.SIM.SmkWizardBuilder.ArchieveFileType@endlink) ArchieveFile
    ##   the machine archive template enum   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return SmkWizardBuilder.ArchieveFileType
    @property
    def ArchieveFile(self) -> SmkWizardBuilder.ArchieveFileType:
        """
        Getter for property: (@link SmkWizardBuilder.ArchieveFileType NXOpen.SIM.SmkWizardBuilder.ArchieveFileType@endlink) ArchieveFile
          the machine archive template enum   
            
         
        """
        pass
    
    ## Setter for property: (@link SmkWizardBuilder.ArchieveFileType NXOpen.SIM.SmkWizardBuilder.ArchieveFileType@endlink) ArchieveFile

    ##   the machine archive template enum   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ArchieveFile.setter
    def ArchieveFile(self, archieveFileEnum: SmkWizardBuilder.ArchieveFileType):
        """
        Setter for property: (@link SmkWizardBuilder.ArchieveFileType NXOpen.SIM.SmkWizardBuilder.ArchieveFileType@endlink) ArchieveFile
          the machine archive template enum   
            
         
        """
        pass
    
    ## Getter for property: (str) ArchieveMachineFilePath
    ##   the smart machine Machine file path   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return str
    @property
    def ArchieveMachineFilePath(self) -> str:
        """
        Getter for property: (str) ArchieveMachineFilePath
          the smart machine Machine file path   
            
         
        """
        pass
    
    ## Setter for property: (str) ArchieveMachineFilePath

    ##   the smart machine Machine file path   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ArchieveMachineFilePath.setter
    def ArchieveMachineFilePath(self, archieveMachineFilePath: str):
        """
        Setter for property: (str) ArchieveMachineFilePath
          the smart machine Machine file path   
            
         
        """
        pass
    
    ## Getter for property: (str) ArchieveTemplateFilePath
    ##   the smart machine template file path   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return str
    @property
    def ArchieveTemplateFilePath(self) -> str:
        """
        Getter for property: (str) ArchieveTemplateFilePath
          the smart machine template file path   
            
         
        """
        pass
    
    ## Setter for property: (str) ArchieveTemplateFilePath

    ##   the smart machine template file path   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ArchieveTemplateFilePath.setter
    def ArchieveTemplateFilePath(self, archieveTemplateFilePath: str):
        """
        Setter for property: (str) ArchieveTemplateFilePath
          the smart machine template file path   
            
         
        """
        pass
    
    ## Getter for property: (bool) CreateCseDriver
    ##   the flag defines whether to create a CSE driver.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def CreateCseDriver(self) -> bool:
        """
        Getter for property: (bool) CreateCseDriver
          the flag defines whether to create a CSE driver.  
              
         
        """
        pass
    
    ## Setter for property: (bool) CreateCseDriver

    ##   the flag defines whether to create a CSE driver.  
    ##       
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @CreateCseDriver.setter
    def CreateCseDriver(self, flagCreateCseDriver: bool):
        """
        Setter for property: (bool) CreateCseDriver
          the flag defines whether to create a CSE driver.  
              
         
        """
        pass
    
    ## Getter for property: (@link SmkWizardBuilder.OutputType NXOpen.SIM.SmkWizardBuilder.OutputType@endlink) CreateKitType
    ##   the type of creating a machine kit.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return SmkWizardBuilder.OutputType
    @property
    def CreateKitType(self) -> SmkWizardBuilder.OutputType:
        """
        Getter for property: (@link SmkWizardBuilder.OutputType NXOpen.SIM.SmkWizardBuilder.OutputType@endlink) CreateKitType
          the type of creating a machine kit.  
              
         
        """
        pass
    
    ## Setter for property: (@link SmkWizardBuilder.OutputType NXOpen.SIM.SmkWizardBuilder.OutputType@endlink) CreateKitType

    ##   the type of creating a machine kit.  
    ##       
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @CreateKitType.setter
    def CreateKitType(self, kitType: SmkWizardBuilder.OutputType):
        """
        Setter for property: (@link SmkWizardBuilder.OutputType NXOpen.SIM.SmkWizardBuilder.OutputType@endlink) CreateKitType
          the type of creating a machine kit.  
              
         
        """
        pass
    
    ## Getter for property: (bool) CreatePostprocessor
    ##   the flag defines whether to create a postprocessor.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def CreatePostprocessor(self) -> bool:
        """
        Getter for property: (bool) CreatePostprocessor
          the flag defines whether to create a postprocessor.  
              
         
        """
        pass
    
    ## Setter for property: (bool) CreatePostprocessor

    ##   the flag defines whether to create a postprocessor.  
    ##       
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @CreatePostprocessor.setter
    def CreatePostprocessor(self, flagCreatePostprocessor: bool):
        """
        Setter for property: (bool) CreatePostprocessor
          the flag defines whether to create a postprocessor.  
              
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SIM.PostConfigurator.CreationPostBuilder NXOpen.SIM.PostConfigurator.CreationPostBuilder@endlink) CreationPostBuilder
    ##   the creation post builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.SIM.PostConfigurator.CreationPostBuilder
    @property
    def CreationPostBuilder(self) -> NXOpen.SIM.PostConfigurator.CreationPostBuilder:
        """
        Getter for property: (@link NXOpen.SIM.PostConfigurator.CreationPostBuilder NXOpen.SIM.PostConfigurator.CreationPostBuilder@endlink) CreationPostBuilder
          the creation post builder   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.SIM.PostConfigurator.CreationPostBuilder NXOpen.SIM.PostConfigurator.CreationPostBuilder@endlink) CreationPostBuilder

    ##   the creation post builder   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @CreationPostBuilder.setter
    def CreationPostBuilder(self, creationPostBuilder: NXOpen.SIM.PostConfigurator.CreationPostBuilder):
        """
        Setter for property: (@link NXOpen.SIM.PostConfigurator.CreationPostBuilder NXOpen.SIM.PostConfigurator.CreationPostBuilder@endlink) CreationPostBuilder
          the creation post builder   
            
         
        """
        pass
    
    ## Getter for property: (str) CseDriverTemplateFile
    ##   the file directory of cse driver template.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return str
    @property
    def CseDriverTemplateFile(self) -> str:
        """
        Getter for property: (str) CseDriverTemplateFile
          the file directory of cse driver template.  
              
         
        """
        pass
    
    ## Setter for property: (str) CseDriverTemplateFile

    ##   the file directory of cse driver template.  
    ##       
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @CseDriverTemplateFile.setter
    def CseDriverTemplateFile(self, file: str):
        """
        Setter for property: (str) CseDriverTemplateFile
          the file directory of cse driver template.  
              
         
        """
        pass
    
    ## Getter for property: (str) CseDriverTemplateName
    ##   the cse driver template name.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return str
    @property
    def CseDriverTemplateName(self) -> str:
        """
        Getter for property: (str) CseDriverTemplateName
          the cse driver template name.  
              
         
        """
        pass
    
    ## Setter for property: (str) CseDriverTemplateName

    ##   the cse driver template name.  
    ##       
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @CseDriverTemplateName.setter
    def CseDriverTemplateName(self, name: str):
        """
        Setter for property: (str) CseDriverTemplateName
          the cse driver template name.  
              
         
        """
        pass
    
    ## Getter for property: (@link SmkWizardBuilder.DeviceTemplateType NXOpen.SIM.SmkWizardBuilder.DeviceTemplateType@endlink) DeviceTemplate
    ##   the device template   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return SmkWizardBuilder.DeviceTemplateType
    @property
    def DeviceTemplate(self) -> SmkWizardBuilder.DeviceTemplateType:
        """
        Getter for property: (@link SmkWizardBuilder.DeviceTemplateType NXOpen.SIM.SmkWizardBuilder.DeviceTemplateType@endlink) DeviceTemplate
          the device template   
            
         
        """
        pass
    
    ## Setter for property: (@link SmkWizardBuilder.DeviceTemplateType NXOpen.SIM.SmkWizardBuilder.DeviceTemplateType@endlink) DeviceTemplate

    ##   the device template   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @DeviceTemplate.setter
    def DeviceTemplate(self, deviceTemplateType: SmkWizardBuilder.DeviceTemplateType):
        """
        Setter for property: (@link SmkWizardBuilder.DeviceTemplateType NXOpen.SIM.SmkWizardBuilder.DeviceTemplateType@endlink) DeviceTemplate
          the device template   
            
         
        """
        pass
    
    ## Getter for property: (str) DeviceTemplateFilePath
    ##   the device template file path   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return str
    @property
    def DeviceTemplateFilePath(self) -> str:
        """
        Getter for property: (str) DeviceTemplateFilePath
          the device template file path   
            
         
        """
        pass
    
    ## Setter for property: (str) DeviceTemplateFilePath

    ##   the device template file path   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @DeviceTemplateFilePath.setter
    def DeviceTemplateFilePath(self, filePath: str):
        """
        Setter for property: (str) DeviceTemplateFilePath
          the device template file path   
            
         
        """
        pass
    
    ## Getter for property: (@link SmkWizardBuilder.CoordinateReferenceType NXOpen.SIM.SmkWizardBuilder.CoordinateReferenceType@endlink) JunctionCoordinateReferenceType
    ##   the type of coordinate reference.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return SmkWizardBuilder.CoordinateReferenceType
    @property
    def JunctionCoordinateReferenceType(self) -> SmkWizardBuilder.CoordinateReferenceType:
        """
        Getter for property: (@link SmkWizardBuilder.CoordinateReferenceType NXOpen.SIM.SmkWizardBuilder.CoordinateReferenceType@endlink) JunctionCoordinateReferenceType
          the type of coordinate reference.  
              
         
        """
        pass
    
    ## Setter for property: (@link SmkWizardBuilder.CoordinateReferenceType NXOpen.SIM.SmkWizardBuilder.CoordinateReferenceType@endlink) JunctionCoordinateReferenceType

    ##   the type of coordinate reference.  
    ##       
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @JunctionCoordinateReferenceType.setter
    def JunctionCoordinateReferenceType(self, refType: SmkWizardBuilder.CoordinateReferenceType):
        """
        Setter for property: (@link SmkWizardBuilder.CoordinateReferenceType NXOpen.SIM.SmkWizardBuilder.CoordinateReferenceType@endlink) JunctionCoordinateReferenceType
          the type of coordinate reference.  
              
         
        """
        pass
    
    ## Getter for property: (str) MachineKitDesc
    ##   the machine kit Description.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def MachineKitDesc(self) -> str:
        """
        Getter for property: (str) MachineKitDesc
          the machine kit Description.  
              
         
        """
        pass
    
    ## Setter for property: (str) MachineKitDesc

    ##   the machine kit Description.  
    ##       
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @MachineKitDesc.setter
    def MachineKitDesc(self, desc: str):
        """
        Setter for property: (str) MachineKitDesc
          the machine kit Description.  
              
         
        """
        pass
    
    ## Getter for property: (@link SmkMachineKitEditorBuilder NXOpen.SIM.SmkMachineKitEditorBuilder@endlink) MachineKitEditorBuilder
    ##   the machine kit editor builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return SmkMachineKitEditorBuilder
    @property
    def MachineKitEditorBuilder(self) -> SmkMachineKitEditorBuilder:
        """
        Getter for property: (@link SmkMachineKitEditorBuilder NXOpen.SIM.SmkMachineKitEditorBuilder@endlink) MachineKitEditorBuilder
          the machine kit editor builder   
            
         
        """
        pass
    
    ## Setter for property: (@link SmkMachineKitEditorBuilder NXOpen.SIM.SmkMachineKitEditorBuilder@endlink) MachineKitEditorBuilder

    ##   the machine kit editor builder   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @MachineKitEditorBuilder.setter
    def MachineKitEditorBuilder(self, machineKitEditorBuilder: SmkMachineKitEditorBuilder):
        """
        Setter for property: (@link SmkMachineKitEditorBuilder NXOpen.SIM.SmkMachineKitEditorBuilder@endlink) MachineKitEditorBuilder
          the machine kit editor builder   
            
         
        """
        pass
    
    ## Getter for property: (str) MachineKitName
    ##   the machine kit name.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return str
    @property
    def MachineKitName(self) -> str:
        """
        Getter for property: (str) MachineKitName
          the machine kit name.  
              
         
        """
        pass
    
    ## Setter for property: (str) MachineKitName

    ##   the machine kit name.  
    ##       
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @MachineKitName.setter
    def MachineKitName(self, name: str):
        """
        Setter for property: (str) MachineKitName
          the machine kit name.  
              
         
        """
        pass
    
    ## Getter for property: (@link SmkWizardBuilder.MachineType NXOpen.SIM.SmkWizardBuilder.MachineType@endlink) MachineKitType
    ##   the type of machine.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return SmkWizardBuilder.MachineType
    @property
    def MachineKitType(self) -> SmkWizardBuilder.MachineType:
        """
        Getter for property: (@link SmkWizardBuilder.MachineType NXOpen.SIM.SmkWizardBuilder.MachineType@endlink) MachineKitType
          the type of machine.  
              
         
        """
        pass
    
    ## Setter for property: (@link SmkWizardBuilder.MachineType NXOpen.SIM.SmkWizardBuilder.MachineType@endlink) MachineKitType

    ##   the type of machine.  
    ##       
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @MachineKitType.setter
    def MachineKitType(self, machineType: SmkWizardBuilder.MachineType):
        """
        Setter for property: (@link SmkWizardBuilder.MachineType NXOpen.SIM.SmkWizardBuilder.MachineType@endlink) MachineKitType
          the type of machine.  
              
         
        """
        pass
    
    ## Getter for property: (str) MachineTemplate
    ##   the machine template name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def MachineTemplate(self) -> str:
        """
        Getter for property: (str) MachineTemplate
          the machine template name   
            
         
        """
        pass
    
    ## Setter for property: (str) MachineTemplate

    ##   the machine template name   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @MachineTemplate.setter
    def MachineTemplate(self, machineTemplateName: str):
        """
        Setter for property: (str) MachineTemplate
          the machine template name   
            
         
        """
        pass
    
    ## Getter for property: (str) MachineTemplateFilePath
    ##   the machine template file path   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def MachineTemplateFilePath(self) -> str:
        """
        Getter for property: (str) MachineTemplateFilePath
          the machine template file path   
            
         
        """
        pass
    
    ## Setter for property: (str) MachineTemplateFilePath

    ##   the machine template file path   
    ##     
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @MachineTemplateFilePath.setter
    def MachineTemplateFilePath(self, machineTemplateFilePath: str):
        """
        Setter for property: (str) MachineTemplateFilePath
          the machine template file path   
            
         
        """
        pass
    
    ## Getter for property: (str) OutputDirectory
    ##   the output directory.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return str
    @property
    def OutputDirectory(self) -> str:
        """
        Getter for property: (str) OutputDirectory
          the output directory.  
              
         
        """
        pass
    
    ## Setter for property: (str) OutputDirectory

    ##   the output directory.  
    ##       
    ##  
    ## Setter License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @OutputDirectory.setter
    def OutputDirectory(self, directory: str):
        """
        Setter for property: (str) OutputDirectory
          the output directory.  
              
         
        """
        pass
    
    ## Getter for property: (@link KinematicChainConfiguration NXOpen.SIM.KinematicChainConfiguration@endlink) SmkKimChainConfigurationBuilder
    ##   the chain configuration builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return KinematicChainConfiguration
    @property
    def SmkKimChainConfigurationBuilder(self) -> KinematicChainConfiguration:
        """
        Getter for property: (@link KinematicChainConfiguration NXOpen.SIM.KinematicChainConfiguration@endlink) SmkKimChainConfigurationBuilder
          the chain configuration builder   
            
         
        """
        pass
    
    ## Getter for property: (@link KinematicChannelConfigurationBuilder NXOpen.SIM.KinematicChannelConfigurationBuilder@endlink) SmkKimChannelConfigurationBuilder
    ##   the channel configuration builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return KinematicChannelConfigurationBuilder
    @property
    def SmkKimChannelConfigurationBuilder(self) -> KinematicChannelConfigurationBuilder:
        """
        Getter for property: (@link KinematicChannelConfigurationBuilder NXOpen.SIM.KinematicChannelConfigurationBuilder@endlink) SmkKimChannelConfigurationBuilder
          the channel configuration builder   
            
         
        """
        pass
    
    ##  Add the junction 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The component name of axis to added 
    def AddAxis(builder: SmkWizardBuilder, compName: str, axisName: str) -> None:
        """
         Add the junction 
        """
        pass
    
    ##  Add the chain 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The chain name 
    def AddChain(builder: SmkWizardBuilder, chainName: str, chainAttributes: str) -> None:
        """
         Add the chain 
        """
        pass
    
    ##  Add the component 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The parent component name to be added 
    def AddComponent(builder: SmkWizardBuilder, parentCompName: str, componentName: str) -> None:
        """
         Add the component 
        """
        pass
    
    ##  Add Classification 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The component name 
    def AddComponentClassification(builder: SmkWizardBuilder, componentName: str, classificationType: SmkWizardBuilder.ComponentClassificationType) -> None:
        """
         Add Classification 
        """
        pass
    
    ##  Add device component 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ## <param name="devicePartPath"> (str) </param>
    ## <param name="layer"> (int) </param>
    ## <param name="transform"> (@link NXOpen.Matrix4x4 NXOpen.Matrix4x4@endlink) </param>
    def AddDeviceComponent(builderTag: SmkWizardBuilder, devicePartPath: str, layer: int, transform: NXOpen.Matrix4x4) -> None:
        """
         Add device component 
        """
        pass
    
    ##  Add device component occurrence 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ## <param name="devicePart"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def AddDevicePartOccurrence(builderTag: SmkWizardBuilder, devicePart: NXOpen.TaggedObject) -> None:
        """
         Add device component occurrence 
        """
        pass
    
    ##  Adds one device template file path 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The device template file path to add 
    def AddDeviceTemplateFilePath(builder: SmkWizardBuilder, filePath: str) -> None:
        """
         Adds one device template file path 
        """
        pass
    
    ##  Adds a single geometry element 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The component name 
    def AddGeometry(builder: SmkWizardBuilder, componentName: str, geo: NXOpen.NXObject) -> None:
        """
         Adds a single geometry element 
        """
        pass
    
    ##  Add the junction 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The parent component name of selected junction 
    def AddJunction(builder: SmkWizardBuilder, componentName: str, junctionName: str) -> None:
        """
         Add the junction 
        """
        pass
    
    ##  Ask machine base component 
    ##  @return baseComponent (str): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    @staticmethod
    def AskMachineBaseComponent(builderTag: SmkWizardBuilder) -> str:
        """
         Ask machine base component 
         @return baseComponent (str): .
        """
        pass
    
    ##  Clear the smk wizard data 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    @staticmethod
    def ClearWizardData(builder: SmkWizardBuilder) -> None:
        """
         Clear the smk wizard data 
        """
        pass
    
    ##  Create chains automatically  
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    def CreateAutoChains(builder: SmkWizardBuilder) -> None:
        """
         Create chains automatically  
        """
        pass
    
    ##  Creates files of the machine kit.  
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    def CreateMachineKit(builder: SmkWizardBuilder) -> None:
        """
         Creates files of the machine kit.  
        """
        pass
    
    ##  Create pocket transform data for pocket generator 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The name of the pocket to be transformed 
    def CreatePocketTransformData(builder: SmkWizardBuilder, pocketName: str) -> None:
        """
         Create pocket transform data for pocket generator 
        """
        pass
    
    ##  Create builder for chain configuration 
    ##  @return chainBuilder (@link KinematicChain NXOpen.SIM.KinematicChain@endlink):  The new kinematic chain builder .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    def CreateSmkKimChainBuilder(builder: SmkWizardBuilder) -> KinematicChain:
        """
         Create builder for chain configuration 
         @return chainBuilder (@link KinematicChain NXOpen.SIM.KinematicChain@endlink):  The new kinematic chain builder .
        """
        pass
    
    ##  Create builder for channel configuration 
    ##  @return channelBuilder (@link KinematicChannelBuilder NXOpen.SIM.KinematicChannelBuilder@endlink):  The new kinematic channel builder .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    def CreateSmkKimChannelBuilder(builder: SmkWizardBuilder) -> KinematicChannelBuilder:
        """
         Create builder for channel configuration 
         @return channelBuilder (@link KinematicChannelBuilder NXOpen.SIM.KinematicChannelBuilder@endlink):  The new kinematic channel builder .
        """
        pass
    
    ##  Deletes all geometry elements from the component 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The component name 
    def DeleteAllGeometries(builder: SmkWizardBuilder, componentName: str) -> None:
        """
         Deletes all geometry elements from the component 
        """
        pass
    
    ##  Delete the axis 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The component name 
    def DeleteAxis(builder: SmkWizardBuilder, compName: str, axisName: str) -> None:
        """
         Delete the axis 
        """
        pass
    
    ##  Delete the chain 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The chain name 
    def DeleteChain(builder: SmkWizardBuilder, chainName: str) -> None:
        """
         Delete the chain 
        """
        pass
    
    ##  Delete the component 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The name of component to be deleted 
    def DeleteComponent(builder: SmkWizardBuilder, componentName: str) -> None:
        """
         Delete the component 
        """
        pass
    
    ##  Deletes one device template file path 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The device template file path to delete 
    def DeleteDeviceTemplateFilePath(builder: SmkWizardBuilder, index: int, filePath: str) -> None:
        """
         Deletes one device template file path 
        """
        pass
    
    ##  Deletes a single geometry element from the component 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The component name 
    def DeleteGeometry(builder: SmkWizardBuilder, componentName: str, geo: NXOpen.NXObject) -> None:
        """
         Deletes a single geometry element from the component 
        """
        pass
    
    ##  Delete the junction 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The junction full name 
    def DeleteJunction(builder: SmkWizardBuilder, jctFullName: str) -> None:
        """
         Delete the junction 
        """
        pass
    
    ##  Generate transform pockets 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The parent component name 
    def GenerateTransformPockets(builder: SmkWizardBuilder, parentCompName: str, pocketName: str) -> None:
        """
         Generate transform pockets 
        """
        pass
    
    ##  Get adjust register 
    ##  @return adjustReg (int):  The adjust regsiter .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ##  The component name 
    def GetAdjustRegister(builder: SmkWizardBuilder, componentName: str) -> int:
        """
         Get adjust register 
         @return adjustReg (int):  The adjust regsiter .
        """
        pass
    
    ##  Gets the axis coarse precision.
    ##             This defines the exact stop precision used to determine if a target point has been
    ##             reached, so that the next NC-block can be executed.  
    ##  @return value (float):  The coarse precission value .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  The axis name 
    def GetAxisCoarsePrecision(builder: SmkWizardBuilder, axisName: str) -> float:
        """
         Gets the axis coarse precision.
                    This defines the exact stop precision used to determine if a target point has been
                    reached, so that the next NC-block can be executed.  
         @return value (float):  The coarse precission value .
        """
        pass
    
    ##  Get the axis direction 
    ##  @return axisDir (@link SmkWizardBuilder.AxisDirectionType NXOpen.SIM.SmkWizardBuilder.AxisDirectionType@endlink):  The axis direction .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  The axis name 
    def GetAxisDirection(builder: SmkWizardBuilder, axisName: str) -> SmkWizardBuilder.AxisDirectionType:
        """
         Get the axis direction 
         @return axisDir (@link SmkWizardBuilder.AxisDirectionType NXOpen.SIM.SmkWizardBuilder.AxisDirectionType@endlink):  The axis direction .
        """
        pass
    
    ##  Get the axis direction on absolute coordinate system  
    ##  @return A tuple consisting of (vectorX, vectorY, vectorZ). 
    ##  - vectorX is: float. The x component of vector .
    ##  - vectorY is: float. The y component of vector .
    ##  - vectorZ is: float. The z component of vector .

    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ##  The axis name 
    @staticmethod
    def GetAxisDirectionVector(builder: SmkWizardBuilder, axisName: str) -> Tuple[float, float, float]:
        """
         Get the axis direction on absolute coordinate system  
         @return A tuple consisting of (vectorX, vectorY, vectorZ). 
         - vectorX is: float. The x component of vector .
         - vectorY is: float. The y component of vector .
         - vectorZ is: float. The z component of vector .

        """
        pass
    
    ##  Gets the axis fine precision.
    ##             This defines the exact stop precision used to determine if a target point has been
    ##             reached, so that the next NC-block can be executed.  
    ##  @return value (float):  The fine precission value .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  The axis name 
    def GetAxisFinePrecision(builder: SmkWizardBuilder, axisName: str) -> float:
        """
         Gets the axis fine precision.
                    This defines the exact stop precision used to determine if a target point has been
                    reached, so that the next NC-block can be executed.  
         @return value (float):  The fine precission value .
        """
        pass
    
    ##  Gets the axis initial value 
    ##  @return initialValue (float):  The initial value .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  The axis name 
    def GetAxisInitialValue(builder: SmkWizardBuilder, axisName: str) -> float:
        """
         Gets the axis initial value 
         @return initialValue (float):  The initial value .
        """
        pass
    
    ##  Gets the axis jerk limit.
    ##             The jerk limit value limits jumps in acceleration. 
    ##  @return value (float):  The jerk limit value .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  The axis name 
    def GetAxisJerkLimit(builder: SmkWizardBuilder, axisName: str) -> float:
        """
         Gets the axis jerk limit.
                    The jerk limit value limits jumps in acceleration. 
         @return value (float):  The jerk limit value .
        """
        pass
    
    ##  Gets the axis jump velocity.
    ##             The jump velocity define a lag time at the beginning of the motion.  
    ##  @return value (float):  The jump velocity value .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  The axis name 
    def GetAxisJumpVelocity(builder: SmkWizardBuilder, axisName: str) -> float:
        """
         Gets the axis jump velocity.
                    The jump velocity define a lag time at the beginning of the motion.  
         @return value (float):  The jump velocity value .
        """
        pass
    
    ##  Gets the axis junction name 
    ##  @return junctionName (str):  The junction name .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  The axis name 
    def GetAxisJunctionName(builder: SmkWizardBuilder, axisName: str) -> str:
        """
         Gets the axis junction name 
         @return junctionName (str):  The junction name .
        """
        pass
    
    ##  Gets the axis kv.
    ##             the Kv-Factor is a parameter of the drives. It influences the dragging error
    ##             (difference between ideal motion profile and actual motion profile).  
    ##  @return value (float):  The kv value .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  The axis name 
    def GetAxisKv(builder: SmkWizardBuilder, axisName: str) -> float:
        """
         Gets the axis kv.
                    the Kv-Factor is a parameter of the drives. It influences the dragging error
                    (difference between ideal motion profile and actual motion profile).  
         @return value (float):  The kv value .
        """
        pass
    
    ##  Gets the axis lower limit 
    ##  @return lowerValue (float):  The lower limit .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  The axis name 
    def GetAxisLowerLimit(builder: SmkWizardBuilder, axisName: str) -> float:
        """
         Gets the axis lower limit 
         @return lowerValue (float):  The lower limit .
        """
        pass
    
    ##  Gets the axis lower soft limit.
    ##             The soft limit on the real machine is checked by the controller to avoid that the machine
    ##             travels into the mechanical stop (Hard Limit) with full speed (prevent damage). 
    ##  @return lowerSoftValue (float):  The lower soft limit .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  The axis name 
    def GetAxisLowerSoftLimit(builder: SmkWizardBuilder, axisName: str) -> float:
        """
         Gets the axis lower soft limit.
                    The soft limit on the real machine is checked by the controller to avoid that the machine
                    travels into the mechanical stop (Hard Limit) with full speed (prevent damage). 
         @return lowerSoftValue (float):  The lower soft limit .
        """
        pass
    
    ##  Gets the axis maximum acceleration. 
    ##             The maximum acceleration defines how fast the axis can accelerate.
    ##  @return value (float):  The maximum acceleration value .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  The axis name 
    def GetAxisMaximumAcceleration(builder: SmkWizardBuilder, axisName: str) -> float:
        """
         Gets the axis maximum acceleration. 
                    The maximum acceleration defines how fast the axis can accelerate.
         @return value (float):  The maximum acceleration value .
        """
        pass
    
    ##  Gets the axis maximum deceleration.
    ##             The maximum deceleration defines how fast the axis can decelerate. 
    ##  @return value (float):  The maximum deceleration value .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  The axis name 
    def GetAxisMaximumDeceleration(builder: SmkWizardBuilder, axisName: str) -> float:
        """
         Gets the axis maximum deceleration.
                    The maximum deceleration defines how fast the axis can decelerate. 
         @return value (float):  The maximum deceleration value .
        """
        pass
    
    ##  Gets the axis maximum velocity 
    ##  @return value (float):  The maximum velocity value .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  The axis name 
    def GetAxisMaximumVelocity(builder: SmkWizardBuilder, axisName: str) -> float:
        """
         Gets the axis maximum velocity 
         @return value (float):  The maximum velocity value .
        """
        pass
    
    ##  Get the axis motion 
    ##  @return A tuple consisting of (type, isNcAxis). 
    ##  - type is: @link SmkWizardBuilder.AxisMotionType NXOpen.SIM.SmkWizardBuilder.AxisMotionType@endlink. The axis motion  .
    ##  - isNcAxis is: bool. The flag if axis is nc axis .

    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  The axis name 
    @staticmethod
    def GetAxisMotion(builder: SmkWizardBuilder, axisName: str) -> Tuple[SmkWizardBuilder.AxisMotionType, bool]:
        """
         Get the axis motion 
         @return A tuple consisting of (type, isNcAxis). 
         - type is: @link SmkWizardBuilder.AxisMotionType NXOpen.SIM.SmkWizardBuilder.AxisMotionType@endlink. The axis motion  .
         - isNcAxis is: bool. The flag if axis is nc axis .

        """
        pass
    
    ##  Gets the axis number.
    ##         The axis number is used in cases where an axis is programmed through a number 
    ##         instead of through an address (e.g. on Siemens 840D: AX1=10 instead of X10).
    ##  @return number (int):  The axis's number .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  The axis name 
    def GetAxisNumber(builder: SmkWizardBuilder, axisName: str) -> int:
        """
         Gets the axis number.
                The axis number is used in cases where an axis is programmed through a number 
                instead of through an address (e.g. on Siemens 840D: AX1=10 instead of X10).
         @return number (int):  The axis's number .
        """
        pass
    
    ##  Gets the axis upper limit 
    ##  @return upperValue (float):  The upper limit .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  The axis name 
    def GetAxisUpperLimit(builder: SmkWizardBuilder, axisName: str) -> float:
        """
         Gets the axis upper limit 
         @return upperValue (float):  The upper limit .
        """
        pass
    
    ##  Gets the axis upper soft limit.
    ##             The soft limit on the real machine is checked by the controller to avoid that the machine
    ##             travels into the mechanical stop (Hard Limit) with full speed (prevent damage). 
    ##  @return upperSoftValue (float):  The upper soft limit .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  The axis name 
    def GetAxisUpperSoftLimit(builder: SmkWizardBuilder, axisName: str) -> float:
        """
         Gets the axis upper soft limit.
                    The soft limit on the real machine is checked by the controller to avoid that the machine
                    travels into the mechanical stop (Hard Limit) with full speed (prevent damage). 
         @return upperSoftValue (float):  The upper soft limit .
        """
        pass
    
    ##  Get capacity 
    ##  @return capacity (int):  The capacity .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ##  The component name 
    def GetCapacity(builder: SmkWizardBuilder, componentName: str) -> int:
        """
         Get capacity 
         @return capacity (int):  The capacity .
        """
        pass
    
    ##  Get channel devices 
    ##  @return devices (List[str]):  The devices assigned to channel .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ##  The channel name 
    def GetChannelDevices(builderTag: SmkWizardBuilder, channelName: str) -> List[str]:
        """
         Get channel devices 
         @return devices (List[str]):  The devices assigned to channel .
        """
        pass
    
    ##  Get cutcom register 
    ##  @return cutcomReg (int):  The cutcom register .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ##  The component name 
    def GetCutcomRegister(builder: SmkWizardBuilder, componentName: str) -> int:
        """
         Get cutcom register 
         @return cutcomReg (int):  The cutcom register .
        """
        pass
    
    ##  Get device id 
    ##  @return deviceId (str):  The device id .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ##  The component name 
    def GetDeviceID(builder: SmkWizardBuilder, componentName: str) -> str:
        """
         Get device id 
         @return deviceId (str):  The device id .
        """
        pass
    
    ##  Get device part mount junction 
    ##  @return mountTag (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ## 
    ## <param name="devicePartPath"> (str) </param>
    def GetDevicePartMountJunction(builderTag: SmkWizardBuilder, devicePartPath: str) -> NXOpen.TaggedObject:
        """
         Get device part mount junction 
         @return mountTag (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink): .
        """
        pass
    
    ##  Returns the geometry elements assigned to this component 
    ##  @return geos (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  The geometry elements .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The component name 
    def GetGeometries(builder: SmkWizardBuilder, componentName: str) -> List[NXOpen.NXObject]:
        """
         Returns the geometry elements assigned to this component 
         @return geos (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  The geometry elements .
        """
        pass
    
    ##  Get holder id 
    ##  @return holderId (str):  The holder id .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ##  The component name 
    def GetHolderID(builder: SmkWizardBuilder, componentName: str) -> str:
        """
         Get holder id 
         @return holderId (str):  The holder id .
        """
        pass
    
    ##  Gets the classification of the junction 
    ##  @return jctClass (@link SmkWizardBuilder.JunctionClassificationType NXOpen.SIM.SmkWizardBuilder.JunctionClassificationType@endlink):  The junction classification .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  The junction fullname 
    def GetJunctionClassification(builder: SmkWizardBuilder, junctionName: str) -> SmkWizardBuilder.JunctionClassificationType:
        """
         Gets the classification of the junction 
         @return jctClass (@link SmkWizardBuilder.JunctionClassificationType NXOpen.SIM.SmkWizardBuilder.JunctionClassificationType@endlink):  The junction classification .
        """
        pass
    
    ##  Gets the junction matrix 
    ##  @return matrix (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink):  The junction matrix .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  The junction fullname 
    def GetJunctionMatrix(builder: SmkWizardBuilder, junctionName: str) -> NXOpen.Matrix3x3:
        """
         Gets the junction matrix 
         @return matrix (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink):  The junction matrix .
        """
        pass
    
    ##  Gets the junction origin 
    ##  @return origin (@link NXOpen.Point3d NXOpen.Point3d@endlink):  The junction origin .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  The junction fullname 
    def GetJunctionOrigin(builder: SmkWizardBuilder, junctionName: str) -> NXOpen.Point3d:
        """
         Gets the junction origin 
         @return origin (@link NXOpen.Point3d NXOpen.Point3d@endlink):  The junction origin .
        """
        pass
    
    ##  Get the kinematics version 
    ##  @return kimVersion (@link SmkWizardBuilder.KinematicsVersionType NXOpen.SIM.SmkWizardBuilder.KinematicsVersionType@endlink):  The kinematics version .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetKinematicsVersion(builder: SmkWizardBuilder) -> SmkWizardBuilder.KinematicsVersionType:
        """
         Get the kinematics version 
         @return kimVersion (@link SmkWizardBuilder.KinematicsVersionType NXOpen.SIM.SmkWizardBuilder.KinematicsVersionType@endlink):  The kinematics version .
        """
        pass
    
    ##  Get the machine kit manufacturer 
    ##  @return manufacturer (str):  The machine kit manufacturer .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetMachineKitManufacturer(builder: SmkWizardBuilder) -> str:
        """
         Get the machine kit manufacturer 
         @return manufacturer (str):  The machine kit manufacturer .
        """
        pass
    
    ##  Get the wizard step 
    ##  @return wizardStep (@link SmkWizardBuilder.WizardStep NXOpen.SIM.SmkWizardBuilder.WizardStep@endlink):  The wizard step .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetWizardStep(builder: SmkWizardBuilder) -> SmkWizardBuilder.WizardStep:
        """
         Get the wizard step 
         @return wizardStep (@link SmkWizardBuilder.WizardStep NXOpen.SIM.SmkWizardBuilder.WizardStep@endlink):  The wizard step .
        """
        pass
    
    ##  Check if axis exists 
    ##  @return result (bool): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="axisName"> (str) </param>
    def HasAxis(builderTag: SmkWizardBuilder, axisName: str) -> bool:
        """
         Check if axis exists 
         @return result (bool): .
        """
        pass
    
    ##  Check if component exists 
    ##  @return result (bool): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="componentName"> (str) </param>
    def HasComponent(builderTag: SmkWizardBuilder, componentName: str) -> bool:
        """
         Check if component exists 
         @return result (bool): .
        """
        pass
    
    ##  Move axis 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The source component of axis being dragged 
    def MoveAxis(builder: SmkWizardBuilder, source: str, target: str) -> None:
        """
         Move axis 
        """
        pass
    
    ##  Move components 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The component is being dragged 
    def MoveComponent(builder: SmkWizardBuilder, source: str, target: str) -> None:
        """
         Move components 
        """
        pass
    
    ##  Move junctions 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The component name of junctions being dragged 
    def MoveJunctions(builder: SmkWizardBuilder, source: str, target: str) -> None:
        """
         Move junctions 
        """
        pass
    
    ##  Parse template json files 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    @staticmethod
    def ParseTemplates(builder: SmkWizardBuilder) -> None:
        """
         Parse template json files 
        """
        pass
    
    ##  Remove Classification 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The component name 
    def RemoveComponentClassification(builder: SmkWizardBuilder, componentName: str, classificationType: SmkWizardBuilder.ComponentClassificationType) -> None:
        """
         Remove Classification 
        """
        pass
    
    ##  Rename the axis 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The component name of axis to be renamed 
    def RenameAxis(builder: SmkWizardBuilder, compName: str, oldAxisName: str, newAxisName: str) -> None:
        """
         Rename the axis 
        """
        pass
    
    ##  Rename the axis junction 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The full name of selected junction 
    def RenameAxisJunction(builder: SmkWizardBuilder, jctFullName: str, newJunctionName: str) -> None:
        """
         Rename the axis junction 
        """
        pass
    
    ##  Rename the chain 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The old chain name 
    def RenameChain(builder: SmkWizardBuilder, oldChainName: str, newChainName: str) -> None:
        """
         Rename the chain 
        """
        pass
    
    ##  Edit the component name 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The name of component to be renamed 
    def RenameComponent(builder: SmkWizardBuilder, componentName: str, newComponentName: str) -> None:
        """
         Edit the component name 
        """
        pass
    
    ##  Rename the junction 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The full name of selected junction 
    def RenameJunction(builder: SmkWizardBuilder, jctFullName: str, newJunctionName: str) -> None:
        """
         Rename the junction 
        """
        pass
    
    ##  Reset the smk wizard 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    @staticmethod
    def ResetWizard(builderTag: SmkWizardBuilder) -> None:
        """
         Reset the smk wizard 
        """
        pass
    
    ##  Set adjust register 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The component name 
    def SetAdjustRegister(builder: SmkWizardBuilder, componentName: str, adjustReg: int) -> None:
        """
         Set adjust register 
        """
        pass
    
    ##  Sets the machine archive data to Machine Kit Editor 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    @staticmethod
    def SetArchieveData(builder: SmkWizardBuilder) -> None:
        """
         Sets the machine archive data to Machine Kit Editor 
        """
        pass
    
    ##  Sets the axis coarse precision.
    ##             This defines the exact stop precision used to determine if a target point has been
    ##             reached, so that the next NC-block can be executed.  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The axis name 
    def SetAxisCoarsePrecision(builder: SmkWizardBuilder, axisName: str, value: float) -> None:
        """
         Sets the axis coarse precision.
                    This defines the exact stop precision used to determine if a target point has been
                    reached, so that the next NC-block can be executed.  
        """
        pass
    
    ##  Set the axis direction 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The axis name 
    def SetAxisDirection(builder: SmkWizardBuilder, axisName: str, axisDir: SmkWizardBuilder.AxisDirectionType) -> None:
        """
         Set the axis direction 
        """
        pass
    
    ##  Sets the axis fine precision.
    ##             This defines the exact stop precision used to determine if a target point has been
    ##             reached, so that the next NC-block can be executed.  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The axis name 
    def SetAxisFinePrecision(builder: SmkWizardBuilder, axisName: str, value: float) -> None:
        """
         Sets the axis fine precision.
                    This defines the exact stop precision used to determine if a target point has been
                    reached, so that the next NC-block can be executed.  
        """
        pass
    
    ##  Gets the axis initial value 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The axis name 
    def SetAxisInitialValue(builder: SmkWizardBuilder, axisName: str, initialValue: float) -> None:
        """
         Gets the axis initial value 
        """
        pass
    
    ##  Sets the axis jerk limit.
    ##             The jerk limit value limits jumps in acceleration. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The axis name 
    def SetAxisJerkLimit(builder: SmkWizardBuilder, axisName: str, value: float) -> None:
        """
         Sets the axis jerk limit.
                    The jerk limit value limits jumps in acceleration. 
        """
        pass
    
    ##  Sets the axis jump velocity.
    ##             The jump velocity define a lag time at the beginning of the motion.  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The axis name 
    def SetAxisJumpVelocity(builder: SmkWizardBuilder, axisName: str, value: float) -> None:
        """
         Sets the axis jump velocity.
                    The jump velocity define a lag time at the beginning of the motion.  
        """
        pass
    
    ##  Sets the axis junction name 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The axis name 
    def SetAxisJunctionName(builder: SmkWizardBuilder, axisName: str, junctionName: str) -> None:
        """
         Sets the axis junction name 
        """
        pass
    
    ##  Sets the axis kv.
    ##             the Kv-Factor is a parameter of the drives. It influences the dragging error 
    ##             (difference between ideal motion profile and actual motion profile).  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The axis name 
    def SetAxisKv(builder: SmkWizardBuilder, axisName: str, value: float) -> None:
        """
         Sets the axis kv.
                    the Kv-Factor is a parameter of the drives. It influences the dragging error 
                    (difference between ideal motion profile and actual motion profile).  
        """
        pass
    
    ##  Sets the axis lower limit 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The axis name 
    def SetAxisLowerLimit(builder: SmkWizardBuilder, axisName: str, lowerValue: float) -> None:
        """
         Sets the axis lower limit 
        """
        pass
    
    ##  Sets the axis lower soft limit.
    ##             The soft limit on the real machine is checked by the controller to avoid that the machine
    ##             travels into the mechanical stop (Hard Limit) with full speed (prevent damage). 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The axis name 
    def SetAxisLowerSoftLimit(builder: SmkWizardBuilder, axisName: str, lowerSoftValue: float) -> None:
        """
         Sets the axis lower soft limit.
                    The soft limit on the real machine is checked by the controller to avoid that the machine
                    travels into the mechanical stop (Hard Limit) with full speed (prevent damage). 
        """
        pass
    
    ##  Sets the axis maximum acceleration. 
    ##             The maximum acceleration defines how fast the axis can accelerate.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The axis name 
    def SetAxisMaximumAcceleration(builder: SmkWizardBuilder, axisName: str, value: float) -> None:
        """
         Sets the axis maximum acceleration. 
                    The maximum acceleration defines how fast the axis can accelerate.
        """
        pass
    
    ##  Sets the axis maximum deceleration.
    ##             The maximum deceleration defines how fast the axis can decelerate. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The axis name 
    def SetAxisMaximumDeceleration(builder: SmkWizardBuilder, axisName: str, value: float) -> None:
        """
         Sets the axis maximum deceleration.
                    The maximum deceleration defines how fast the axis can decelerate. 
        """
        pass
    
    ##  Sets the axis maximum velocity 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The axis name 
    def SetAxisMaximumVelocity(builder: SmkWizardBuilder, axisName: str, value: float) -> None:
        """
         Sets the axis maximum velocity 
        """
        pass
    
    ##  Set the axis motion 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The axis name 
    def SetAxisMotion(builder: SmkWizardBuilder, axisName: str, isNcAxis: bool, type: SmkWizardBuilder.AxisMotionType) -> None:
        """
         Set the axis motion 
        """
        pass
    
    ##  Sets the axis number.
    ##         The axis number is used in cases where an axis is programmed through a number 
    ##         instead of through an address (e.g. on Siemens 840D: AX1=10 instead of X10).
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The axis name 
    def SetAxisNumber(builder: SmkWizardBuilder, axisName: str, number: int) -> None:
        """
         Sets the axis number.
                The axis number is used in cases where an axis is programmed through a number 
                instead of through an address (e.g. on Siemens 840D: AX1=10 instead of X10).
        """
        pass
    
    ##  Sets the axis upper limit 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The axis name 
    def SetAxisUpperLimit(builder: SmkWizardBuilder, axisName: str, upperValue: float) -> None:
        """
         Sets the axis upper limit 
        """
        pass
    
    ##  Sets the axis upper soft limit.
    ##             The soft limit on the real machine is checked by the controller to avoid that the machine
    ##             travels into the mechanical stop (Hard Limit) with full speed (prevent damage). 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The axis name 
    def SetAxisUpperSoftLimit(builder: SmkWizardBuilder, axisName: str, upperSoftValue: float) -> None:
        """
         Sets the axis upper soft limit.
                    The soft limit on the real machine is checked by the controller to avoid that the machine
                    travels into the mechanical stop (Hard Limit) with full speed (prevent damage). 
        """
        pass
    
    ##  Set capacity 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The component name 
    def SetCapacity(builder: SmkWizardBuilder, componentName: str, capacity: int) -> None:
        """
         Set capacity 
        """
        pass
    
    ##  Set cutcom register 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The component name 
    def SetCutcomRegister(builder: SmkWizardBuilder, componentName: str, cutcomReg: int) -> None:
        """
         Set cutcom register 
        """
        pass
    
    ##  Set device id 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The component name 
    def SetDeviceID(builder: SmkWizardBuilder, componentName: str, deviceId: str) -> None:
        """
         Set device id 
        """
        pass
    
    ##  Sets geometry elements for the component 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The component name 
    def SetGeometries(builder: SmkWizardBuilder, componentName: str, geos: List[NXOpen.NXObject]) -> None:
        """
         Sets geometry elements for the component 
        """
        pass
    
    ##  Set holder id 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The component name 
    def SetHolderID(builder: SmkWizardBuilder, componentName: str, holderId: str) -> None:
        """
         Set holder id 
        """
        pass
    
    ##  Sets the classification of the junction 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The junction fullname 
    def SetJunctionClassification(builder: SmkWizardBuilder, junctionName: str, jctClass: SmkWizardBuilder.JunctionClassificationType) -> None:
        """
         Sets the classification of the junction 
        """
        pass
    
    ##  Sets the CSYS associated with the junction 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The junction fullname 
    def SetJunctionCsys(builder: SmkWizardBuilder, junctionName: str, csys: NXOpen.CartesianCoordinateSystem) -> None:
        """
         Sets the CSYS associated with the junction 
        """
        pass
    
    ##  Set the kinematics version 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The kinematics version 
    def SetKinematicsVersion(builder: SmkWizardBuilder, kimVersion: SmkWizardBuilder.KinematicsVersionType) -> None:
        """
         Set the kinematics version 
        """
        pass
    
    ##  Set the machine kit manufacturer 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The machine kit manufacturer 
    def SetMachineKitManufacturer(builder: SmkWizardBuilder, manufacturer: str) -> None:
        """
         Set the machine kit manufacturer 
        """
        pass
    
    ##  Set pocket transform adjust register id increment 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The name of the pocket to be transformed 
    def SetPocketTransformAdjustRegisterIncrement(builder: SmkWizardBuilder, pocketName: str, increment: int) -> None:
        """
         Set pocket transform adjust register id increment 
        """
        pass
    
    ##  Set pocket transform cutcom register increment 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The name of the pocket to be transformed 
    def SetPocketTransformCutcomRegisterIncrement(builder: SmkWizardBuilder, pocketName: str, increment: int) -> None:
        """
         Set pocket transform cutcom register increment 
        """
        pass
    
    ##  Set pocket transform division 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The name of the pocket to be transformed 
    def SetPocketTransformDivision(builder: SmkWizardBuilder, pocketName: str, division: int) -> None:
        """
         Set pocket transform division 
        """
        pass
    
    ##  Set pocket transform holder id increment 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The name of the pocket to be transformed 
    def SetPocketTransformHolderIDIncrement(builder: SmkWizardBuilder, pocketName: str, increment: int) -> None:
        """
         Set pocket transform holder id increment 
        """
        pass
    
    ##  Set pocket transform holder id reference 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The name of the pocket to be transformed 
    def SetPocketTransformHolderIDReference(builder: SmkWizardBuilder, pocketName: str, reference: int) -> None:
        """
         Set pocket transform holder id reference 
        """
        pass
    
    ##  Set pocket transform number of copies 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The name of the pocket to be transformed 
    def SetPocketTransformNumberOfCopies(builder: SmkWizardBuilder, pocketName: str, numOfCopies: int) -> None:
        """
         Set pocket transform number of copies 
        """
        pass
    
    ##  Set pocket transform angle 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The name of the pocket to be transformed 
    def SetPocketTransformRotateAngle(builder: SmkWizardBuilder, pocketName: str, angle: float) -> None:
        """
         Set pocket transform angle 
        """
        pass
    
    ##  Set pocket transform rotate end point 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The name of the pocket to be transformed 
    def SetPocketTransformRotateLineEndPoint(builder: SmkWizardBuilder, pocketName: str, X: float, Y: float, Z: float) -> None:
        """
         Set pocket transform rotate end point 
        """
        pass
    
    ##  Set pocket transform rotate line point 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The name of the pocket to be transformed 
    def SetPocketTransformRotateLinePoint(builder: SmkWizardBuilder, pocketName: str, X: float, Y: float, Z: float) -> None:
        """
         Set pocket transform rotate line point 
        """
        pass
    
    ##  Set pocket transform rotate start point 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The name of the pocket to be transformed 
    def SetPocketTransformRotateLineStartPoint(builder: SmkWizardBuilder, pocketName: str, X: float, Y: float, Z: float) -> None:
        """
         Set pocket transform rotate start point 
        """
        pass
    
    ##  Set pocket transform rotate line vector 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The name of the pocket to be transformed 
    def SetPocketTransformRotateLineVector(builder: SmkWizardBuilder, pocketName: str, i: float, j: float, k: float) -> None:
        """
         Set pocket transform rotate line vector 
        """
        pass
    
    ##  Set pocket transform DeltaXC 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The name of the pocket to be transformed 
    def SetPocketTransformTranslateDeltaXC(builder: SmkWizardBuilder, pocketName: str, deltaXC: float) -> None:
        """
         Set pocket transform DeltaXC 
        """
        pass
    
    ##  Set pocket transform DeltaYC 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The name of the pocket to be transformed 
    def SetPocketTransformTranslateDeltaYC(builder: SmkWizardBuilder, pocketName: str, deltaYC: float) -> None:
        """
         Set pocket transform DeltaYC 
        """
        pass
    
    ##  Set pocket transform DeltaZC 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The name of the pocket to be transformed 
    def SetPocketTransformTranslateDeltaZC(builder: SmkWizardBuilder, pocketName: str, deltaZC: float) -> None:
        """
         Set pocket transform DeltaZC 
        """
        pass
    
    ##  Set pocket transform translate reference point 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The name of the pocket to be transformed 
    def SetPocketTransformTranslateReferencePoint(builder: SmkWizardBuilder, pocketName: str, X: float, Y: float, Z: float) -> None:
        """
         Set pocket transform translate reference point 
        """
        pass
    
    ##  Set pocket transform translate to point 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The name of the pocket to be transformed 
    def SetPocketTransformTranslateToPoint(builder: SmkWizardBuilder, pocketName: str, X: float, Y: float, Z: float) -> None:
        """
         Set pocket transform translate to point 
        """
        pass
    
    ##  Set pocket transform type 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The name of the pocket to be transformed 
    def SetPocketTransformType(builder: SmkWizardBuilder, pocketName: str, transformType: SmkWizardBuilder.PocketTransformType) -> None:
        """
         Set pocket transform type 
        """
        pass
    
    ##  Set the wizard step 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The wizard step 
    def SetWizardStep(builder: SmkWizardBuilder, wizardStep: SmkWizardBuilder.WizardStep) -> None:
        """
         Set the wizard step 
        """
        pass
    
    ##  Update the chain 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    ##  The chain name 
    def UpdateChain(builder: SmkWizardBuilder, chainName: str, chainAttributes: str) -> None:
        """
         Update the chain 
        """
        pass
    
import NXOpen
##   @brief  Represents the Snapshot class object  
## 
##     <br> Use the @link NXOpen::SIM::Snapshot NXOpen::SIM::Snapshot@endlink  class to create a Snapshot object.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class Snapshot(NXOpen.NXObject): 
    """ <summary> Represents the Snapshot class object </summary>  """
    pass


import NXOpen
##   @brief  Represents the TimeAnalysis class object  
## 
##     <br> These objects are created by the simulation for each channel.  <br> 
## 
##   <br>  Created in NX11.0.2  <br> 

class TimeAnalysis(NXOpen.TaggedObject): 
    """ <summary> Represents the TimeAnalysis class object </summary>  """


    ##  Reset the Time Analysis
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    @staticmethod
    def Reset(timeAnalysis: TimeAnalysis) -> None:
        """
         Reset the Time Analysis
        """
        pass
    
    ##  Start the Time Analysis
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    @staticmethod
    def Start(timeAnalysis: TimeAnalysis) -> None:
        """
         Start the Time Analysis
        """
        pass
    
    ##  Stop the Time Analysis
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    @staticmethod
    def Stop(timeAnalysis: TimeAnalysis) -> None:
        """
         Stop the Time Analysis
        """
        pass
    
## @package NXOpen.SIM
## Classes, Enums and Structs under NXOpen.SIM namespace

##  @link IsvControlPanelBuilderDetailType NXOpen.SIM.IsvControlPanelBuilderDetailType @endlink is an alias for @link IsvControlPanelBuilder.DetailType NXOpen.SIM.IsvControlPanelBuilder.DetailType@endlink
IsvControlPanelBuilderDetailType = IsvControlPanelBuilder.DetailType


##  @link IsvControlPanelBuilderLanguage NXOpen.SIM.IsvControlPanelBuilderLanguage @endlink is an alias for @link IsvControlPanelBuilder.Language NXOpen.SIM.IsvControlPanelBuilder.Language@endlink
IsvControlPanelBuilderLanguage = IsvControlPanelBuilder.Language


##  @link IsvControlPanelBuilderSingleStepModeType NXOpen.SIM.IsvControlPanelBuilderSingleStepModeType @endlink is an alias for @link IsvControlPanelBuilder.SingleStepModeType NXOpen.SIM.IsvControlPanelBuilder.SingleStepModeType@endlink
IsvControlPanelBuilderSingleStepModeType = IsvControlPanelBuilder.SingleStepModeType


##  @link IsvControlPanelBuilderSingleStepType NXOpen.SIM.IsvControlPanelBuilderSingleStepType @endlink is an alias for @link IsvControlPanelBuilder.SingleStepType NXOpen.SIM.IsvControlPanelBuilder.SingleStepType@endlink
IsvControlPanelBuilderSingleStepType = IsvControlPanelBuilder.SingleStepType


##  @link IsvControlPanelBuilderVisualizationType NXOpen.SIM.IsvControlPanelBuilderVisualizationType @endlink is an alias for @link IsvControlPanelBuilder.VisualizationType NXOpen.SIM.IsvControlPanelBuilder.VisualizationType@endlink
IsvControlPanelBuilderVisualizationType = IsvControlPanelBuilder.VisualizationType


##  @link IsvControlPanelBuilderVncMode NXOpen.SIM.IsvControlPanelBuilderVncMode @endlink is an alias for @link IsvControlPanelBuilder.VncMode NXOpen.SIM.IsvControlPanelBuilder.VncMode@endlink
IsvControlPanelBuilderVncMode = IsvControlPanelBuilder.VncMode


##  @link KinematicAxisBuilderAxisDirectionType NXOpen.SIM.KinematicAxisBuilderAxisDirectionType @endlink is an alias for @link KinematicAxisBuilder.AxisDirectionType NXOpen.SIM.KinematicAxisBuilder.AxisDirectionType@endlink
KinematicAxisBuilderAxisDirectionType = KinematicAxisBuilder.AxisDirectionType


##  @link KinematicAxisBuilderAxisMotionType NXOpen.SIM.KinematicAxisBuilderAxisMotionType @endlink is an alias for @link KinematicAxisBuilder.AxisMotionType NXOpen.SIM.KinematicAxisBuilder.AxisMotionType@endlink
KinematicAxisBuilderAxisMotionType = KinematicAxisBuilder.AxisMotionType


##  @link KinematicChainCoordinatePlaneTypes NXOpen.SIM.KinematicChainCoordinatePlaneTypes @endlink is an alias for @link KinematicChain.CoordinatePlaneTypes NXOpen.SIM.KinematicChain.CoordinatePlaneTypes@endlink
KinematicChainCoordinatePlaneTypes = KinematicChain.CoordinatePlaneTypes


##  @link KinematicChainPreferredSolutionType NXOpen.SIM.KinematicChainPreferredSolutionType @endlink is an alias for @link KinematicChain.PreferredSolutionType NXOpen.SIM.KinematicChain.PreferredSolutionType@endlink
KinematicChainPreferredSolutionType = KinematicChain.PreferredSolutionType


##  @link KinematicChainTypes NXOpen.SIM.KinematicChainTypes @endlink is an alias for @link KinematicChain.Types NXOpen.SIM.KinematicChain.Types@endlink
KinematicChainTypes = KinematicChain.Types


##  @link KinematicComponentBuilderRegisterTypes NXOpen.SIM.KinematicComponentBuilderRegisterTypes @endlink is an alias for @link KinematicComponentBuilder.RegisterTypes NXOpen.SIM.KinematicComponentBuilder.RegisterTypes@endlink
KinematicComponentBuilderRegisterTypes = KinematicComponentBuilder.RegisterTypes


##  @link KinematicComponentBuilderSystemClass NXOpen.SIM.KinematicComponentBuilderSystemClass @endlink is an alias for @link KinematicComponentBuilder.SystemClass NXOpen.SIM.KinematicComponentBuilder.SystemClass@endlink
KinematicComponentBuilderSystemClass = KinematicComponentBuilder.SystemClass


##  @link KinematicComponentBuilderWorkPositionAngleTypes NXOpen.SIM.KinematicComponentBuilderWorkPositionAngleTypes @endlink is an alias for @link KinematicComponentBuilder.WorkPositionAngleTypes NXOpen.SIM.KinematicComponentBuilder.WorkPositionAngleTypes@endlink
KinematicComponentBuilderWorkPositionAngleTypes = KinematicComponentBuilder.WorkPositionAngleTypes


##  @link KinematicConfiguratorUniteTypes NXOpen.SIM.KinematicConfiguratorUniteTypes @endlink is an alias for @link KinematicConfigurator.UniteTypes NXOpen.SIM.KinematicConfigurator.UniteTypes@endlink
KinematicConfiguratorUniteTypes = KinematicConfigurator.UniteTypes


##  @link KinematicJunctionBuilderSystemClass NXOpen.SIM.KinematicJunctionBuilderSystemClass @endlink is an alias for @link KinematicJunctionBuilder.SystemClass NXOpen.SIM.KinematicJunctionBuilder.SystemClass@endlink
KinematicJunctionBuilderSystemClass = KinematicJunctionBuilder.SystemClass


##  @link KinematicSinumerikCaBuilderPlcInitStateTypes NXOpen.SIM.KinematicSinumerikCaBuilderPlcInitStateTypes @endlink is an alias for @link KinematicSinumerikCaBuilder.PlcInitStateTypes NXOpen.SIM.KinematicSinumerikCaBuilder.PlcInitStateTypes@endlink
KinematicSinumerikCaBuilderPlcInitStateTypes = KinematicSinumerikCaBuilder.PlcInitStateTypes


##  @link KinematicSinumerikCaBuilderPlcUsageTypes NXOpen.SIM.KinematicSinumerikCaBuilderPlcUsageTypes @endlink is an alias for @link KinematicSinumerikCaBuilder.PlcUsageTypes NXOpen.SIM.KinematicSinumerikCaBuilder.PlcUsageTypes@endlink
KinematicSinumerikCaBuilderPlcUsageTypes = KinematicSinumerikCaBuilder.PlcUsageTypes


##  @link MachineToolConfigurationControllerLines NXOpen.SIM.MachineToolConfigurationControllerLines @endlink is an alias for @link MachineToolConfiguration.ControllerLines NXOpen.SIM.MachineToolConfiguration.ControllerLines@endlink
MachineToolConfigurationControllerLines = MachineToolConfiguration.ControllerLines


##  @link MachineToolConfigurationMdynamicsTypes NXOpen.SIM.MachineToolConfigurationMdynamicsTypes @endlink is an alias for @link MachineToolConfiguration.MdynamicsTypes NXOpen.SIM.MachineToolConfiguration.MdynamicsTypes@endlink
MachineToolConfigurationMdynamicsTypes = MachineToolConfiguration.MdynamicsTypes


##  @link MachineToolConfigurationPlaneTypes NXOpen.SIM.MachineToolConfigurationPlaneTypes @endlink is an alias for @link MachineToolConfiguration.PlaneTypes NXOpen.SIM.MachineToolConfiguration.PlaneTypes@endlink
MachineToolConfigurationPlaneTypes = MachineToolConfiguration.PlaneTypes


##  @link MachineToolConfigurationSwivelingTypes NXOpen.SIM.MachineToolConfigurationSwivelingTypes @endlink is an alias for @link MachineToolConfiguration.SwivelingTypes NXOpen.SIM.MachineToolConfiguration.SwivelingTypes@endlink
MachineToolConfigurationSwivelingTypes = MachineToolConfiguration.SwivelingTypes


##  @link MachineToolConfigurationTechnologyTypes NXOpen.SIM.MachineToolConfigurationTechnologyTypes @endlink is an alias for @link MachineToolConfiguration.TechnologyTypes NXOpen.SIM.MachineToolConfiguration.TechnologyTypes@endlink
MachineToolConfigurationTechnologyTypes = MachineToolConfiguration.TechnologyTypes


##  @link MachineToolConfigurationUnitTypes NXOpen.SIM.MachineToolConfigurationUnitTypes @endlink is an alias for @link MachineToolConfiguration.UnitTypes NXOpen.SIM.MachineToolConfiguration.UnitTypes@endlink
MachineToolConfigurationUnitTypes = MachineToolConfiguration.UnitTypes


##  @link SimDebugBuilderDriverType NXOpen.SIM.SimDebugBuilderDriverType @endlink is an alias for @link SimDebugBuilder.DriverType NXOpen.SIM.SimDebugBuilder.DriverType@endlink
SimDebugBuilderDriverType = SimDebugBuilder.DriverType


##  @link SimDebugBuilderKinematicModelType NXOpen.SIM.SimDebugBuilderKinematicModelType @endlink is an alias for @link SimDebugBuilder.KinematicModelType NXOpen.SIM.SimDebugBuilder.KinematicModelType@endlink
SimDebugBuilderKinematicModelType = SimDebugBuilder.KinematicModelType


##  @link SimDebugBuilderOutputType NXOpen.SIM.SimDebugBuilderOutputType @endlink is an alias for @link SimDebugBuilder.OutputType NXOpen.SIM.SimDebugBuilder.OutputType@endlink
SimDebugBuilderOutputType = SimDebugBuilder.OutputType


##  @link SimDebugBuilderPrintoutTagsOrPointersType NXOpen.SIM.SimDebugBuilderPrintoutTagsOrPointersType @endlink is an alias for @link SimDebugBuilder.PrintoutTagsOrPointersType NXOpen.SIM.SimDebugBuilder.PrintoutTagsOrPointersType@endlink
SimDebugBuilderPrintoutTagsOrPointersType = SimDebugBuilder.PrintoutTagsOrPointersType


##  @link SimDebugBuilderTraceType NXOpen.SIM.SimDebugBuilderTraceType @endlink is an alias for @link SimDebugBuilder.TraceType NXOpen.SIM.SimDebugBuilder.TraceType@endlink
SimDebugBuilderTraceType = SimDebugBuilder.TraceType


##  @link SimDebugBuilderUiType NXOpen.SIM.SimDebugBuilderUiType @endlink is an alias for @link SimDebugBuilder.UiType NXOpen.SIM.SimDebugBuilder.UiType@endlink
SimDebugBuilderUiType = SimDebugBuilder.UiType


##  @link SinumerikCaSimplifyBodiesBuilderCloseGapTypes NXOpen.SIM.SinumerikCaSimplifyBodiesBuilderCloseGapTypes @endlink is an alias for @link SinumerikCaSimplifyBodiesBuilder.CloseGapTypes NXOpen.SIM.SinumerikCaSimplifyBodiesBuilder.CloseGapTypes@endlink
SinumerikCaSimplifyBodiesBuilderCloseGapTypes = SinumerikCaSimplifyBodiesBuilder.CloseGapTypes


##  @link SinumerikCaSimplifyBodiesBuilderObjectToReplaceWithTypes NXOpen.SIM.SinumerikCaSimplifyBodiesBuilderObjectToReplaceWithTypes @endlink is an alias for @link SinumerikCaSimplifyBodiesBuilder.ObjectToReplaceWithTypes NXOpen.SIM.SinumerikCaSimplifyBodiesBuilder.ObjectToReplaceWithTypes@endlink
SinumerikCaSimplifyBodiesBuilderObjectToReplaceWithTypes = SinumerikCaSimplifyBodiesBuilder.ObjectToReplaceWithTypes


##  @link SmkDebugBuilderDumpType NXOpen.SIM.SmkDebugBuilderDumpType @endlink is an alias for @link SmkDebugBuilder.DumpType NXOpen.SIM.SmkDebugBuilder.DumpType@endlink
SmkDebugBuilderDumpType = SmkDebugBuilder.DumpType


##  @link SmkDebugBuilderOutputType NXOpen.SIM.SmkDebugBuilderOutputType @endlink is an alias for @link SmkDebugBuilder.OutputType NXOpen.SIM.SmkDebugBuilder.OutputType@endlink
SmkDebugBuilderOutputType = SmkDebugBuilder.OutputType


##  @link SmkMachineKitEditorBuilderDataClassification NXOpen.SIM.SmkMachineKitEditorBuilderDataClassification @endlink is an alias for @link SmkMachineKitEditorBuilder.DataClassification NXOpen.SIM.SmkMachineKitEditorBuilder.DataClassification@endlink
SmkMachineKitEditorBuilderDataClassification = SmkMachineKitEditorBuilder.DataClassification


##  @link SmkMachineKitEditorBuilderDataType NXOpen.SIM.SmkMachineKitEditorBuilderDataType @endlink is an alias for @link SmkMachineKitEditorBuilder.DataType NXOpen.SIM.SmkMachineKitEditorBuilder.DataType@endlink
SmkMachineKitEditorBuilderDataType = SmkMachineKitEditorBuilder.DataType


##  @link SmkMachineKitEditorBuilderParametersMachineMode NXOpen.SIM.SmkMachineKitEditorBuilderParametersMachineMode @endlink is an alias for @link SmkMachineKitEditorBuilder.ParametersMachineMode NXOpen.SIM.SmkMachineKitEditorBuilder.ParametersMachineMode@endlink
SmkMachineKitEditorBuilderParametersMachineMode = SmkMachineKitEditorBuilder.ParametersMachineMode


##  @link SmkTransitionPathEditorBuilderTemplateLocation NXOpen.SIM.SmkTransitionPathEditorBuilderTemplateLocation @endlink is an alias for @link SmkTransitionPathEditorBuilder.TemplateLocation NXOpen.SIM.SmkTransitionPathEditorBuilder.TemplateLocation@endlink
SmkTransitionPathEditorBuilderTemplateLocation = SmkTransitionPathEditorBuilder.TemplateLocation


##  @link SmkTransitionPathEditorBuilderTemplateType NXOpen.SIM.SmkTransitionPathEditorBuilderTemplateType @endlink is an alias for @link SmkTransitionPathEditorBuilder.TemplateType NXOpen.SIM.SmkTransitionPathEditorBuilder.TemplateType@endlink
SmkTransitionPathEditorBuilderTemplateType = SmkTransitionPathEditorBuilder.TemplateType


##  @link SmkWizardBuilderArchieveFileType NXOpen.SIM.SmkWizardBuilderArchieveFileType @endlink is an alias for @link SmkWizardBuilder.ArchieveFileType NXOpen.SIM.SmkWizardBuilder.ArchieveFileType@endlink
SmkWizardBuilderArchieveFileType = SmkWizardBuilder.ArchieveFileType


##  @link SmkWizardBuilderAxisDirectionType NXOpen.SIM.SmkWizardBuilderAxisDirectionType @endlink is an alias for @link SmkWizardBuilder.AxisDirectionType NXOpen.SIM.SmkWizardBuilder.AxisDirectionType@endlink
SmkWizardBuilderAxisDirectionType = SmkWizardBuilder.AxisDirectionType


##  @link SmkWizardBuilderAxisMotionType NXOpen.SIM.SmkWizardBuilderAxisMotionType @endlink is an alias for @link SmkWizardBuilder.AxisMotionType NXOpen.SIM.SmkWizardBuilder.AxisMotionType@endlink
SmkWizardBuilderAxisMotionType = SmkWizardBuilder.AxisMotionType


##  @link SmkWizardBuilderComponentClassificationType NXOpen.SIM.SmkWizardBuilderComponentClassificationType @endlink is an alias for @link SmkWizardBuilder.ComponentClassificationType NXOpen.SIM.SmkWizardBuilder.ComponentClassificationType@endlink
SmkWizardBuilderComponentClassificationType = SmkWizardBuilder.ComponentClassificationType


##  @link SmkWizardBuilderCoordinateReferenceType NXOpen.SIM.SmkWizardBuilderCoordinateReferenceType @endlink is an alias for @link SmkWizardBuilder.CoordinateReferenceType NXOpen.SIM.SmkWizardBuilder.CoordinateReferenceType@endlink
SmkWizardBuilderCoordinateReferenceType = SmkWizardBuilder.CoordinateReferenceType


##  @link SmkWizardBuilderDeviceTemplateType NXOpen.SIM.SmkWizardBuilderDeviceTemplateType @endlink is an alias for @link SmkWizardBuilder.DeviceTemplateType NXOpen.SIM.SmkWizardBuilder.DeviceTemplateType@endlink
SmkWizardBuilderDeviceTemplateType = SmkWizardBuilder.DeviceTemplateType


##  @link SmkWizardBuilderJunctionClassificationType NXOpen.SIM.SmkWizardBuilderJunctionClassificationType @endlink is an alias for @link SmkWizardBuilder.JunctionClassificationType NXOpen.SIM.SmkWizardBuilder.JunctionClassificationType@endlink
SmkWizardBuilderJunctionClassificationType = SmkWizardBuilder.JunctionClassificationType


##  @link SmkWizardBuilderKinematicsVersionType NXOpen.SIM.SmkWizardBuilderKinematicsVersionType @endlink is an alias for @link SmkWizardBuilder.KinematicsVersionType NXOpen.SIM.SmkWizardBuilder.KinematicsVersionType@endlink
SmkWizardBuilderKinematicsVersionType = SmkWizardBuilder.KinematicsVersionType


##  @link SmkWizardBuilderMachineType NXOpen.SIM.SmkWizardBuilderMachineType @endlink is an alias for @link SmkWizardBuilder.MachineType NXOpen.SIM.SmkWizardBuilder.MachineType@endlink
SmkWizardBuilderMachineType = SmkWizardBuilder.MachineType


##  @link SmkWizardBuilderOutputType NXOpen.SIM.SmkWizardBuilderOutputType @endlink is an alias for @link SmkWizardBuilder.OutputType NXOpen.SIM.SmkWizardBuilder.OutputType@endlink
SmkWizardBuilderOutputType = SmkWizardBuilder.OutputType


##  @link SmkWizardBuilderPocketTransformType NXOpen.SIM.SmkWizardBuilderPocketTransformType @endlink is an alias for @link SmkWizardBuilder.PocketTransformType NXOpen.SIM.SmkWizardBuilder.PocketTransformType@endlink
SmkWizardBuilderPocketTransformType = SmkWizardBuilder.PocketTransformType


##  @link SmkWizardBuilderRegisterType NXOpen.SIM.SmkWizardBuilderRegisterType @endlink is an alias for @link SmkWizardBuilder.RegisterType NXOpen.SIM.SmkWizardBuilder.RegisterType@endlink
SmkWizardBuilderRegisterType = SmkWizardBuilder.RegisterType


##  @link SmkWizardBuilderWizardStep NXOpen.SIM.SmkWizardBuilderWizardStep @endlink is an alias for @link SmkWizardBuilder.WizardStep NXOpen.SIM.SmkWizardBuilder.WizardStep@endlink
SmkWizardBuilderWizardStep = SmkWizardBuilder.WizardStep


