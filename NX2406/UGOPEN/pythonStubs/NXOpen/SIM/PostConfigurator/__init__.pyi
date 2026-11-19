from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  This class is used to create a new layer.
##             Calling @link Builder::Commit Builder::Commit@endlink  on this builder will only return NULL.
##          <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class AddLayerBuilder(NXOpen.Builder): 
    """ This class is used to create a new layer.
            Calling <ja_method>Builder.Commit</ja_method> on this builder will only return <ja_NULL>.
        """


    ## Getter for property: (bool) CreateDefinitionFile
    ##  Returns the flag of create def file   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def CreateDefinitionFile(self) -> bool:
        """
        Getter for property: (bool) CreateDefinitionFile
         Returns the flag of create def file   
            
         
        """
        pass
    
    ## Setter for property: (bool) CreateDefinitionFile

    ##  Returns the flag of create def file   
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @CreateDefinitionFile.setter
    def CreateDefinitionFile(self, hasCreateDefFile: bool):
        """
        Setter for property: (bool) CreateDefinitionFile
         Returns the flag of create def file   
            
         
        """
        pass
    
    ## Getter for property: (bool) CreateDirectoryForLayer
    ##  Returns the flag of create tcl file   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def CreateDirectoryForLayer(self) -> bool:
        """
        Getter for property: (bool) CreateDirectoryForLayer
         Returns the flag of create tcl file   
            
         
        """
        pass
    
    ## Setter for property: (bool) CreateDirectoryForLayer

    ##  Returns the flag of create tcl file   
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @CreateDirectoryForLayer.setter
    def CreateDirectoryForLayer(self, hasCreateFolder: bool):
        """
        Setter for property: (bool) CreateDirectoryForLayer
         Returns the flag of create tcl file   
            
         
        """
        pass
    
    ## Getter for property: (bool) CreateTclFile
    ##  Returns the flag of create tcl file   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def CreateTclFile(self) -> bool:
        """
        Getter for property: (bool) CreateTclFile
         Returns the flag of create tcl file   
            
         
        """
        pass
    
    ## Setter for property: (bool) CreateTclFile

    ##  Returns the flag of create tcl file   
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @CreateTclFile.setter
    def CreateTclFile(self, hasCreateTclFile: bool):
        """
        Setter for property: (bool) CreateTclFile
         Returns the flag of create tcl file   
            
         
        """
        pass
    
    ## Getter for property: (bool) CreateUserDefinedEventFile
    ##  Returns the flag of create cdl file   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def CreateUserDefinedEventFile(self) -> bool:
        """
        Getter for property: (bool) CreateUserDefinedEventFile
         Returns the flag of create cdl file   
            
         
        """
        pass
    
    ## Setter for property: (bool) CreateUserDefinedEventFile

    ##  Returns the flag of create cdl file   
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @CreateUserDefinedEventFile.setter
    def CreateUserDefinedEventFile(self, hasCreateCdlFile: bool):
        """
        Setter for property: (bool) CreateUserDefinedEventFile
         Returns the flag of create cdl file   
            
         
        """
        pass
    
    ## Getter for property: (str) LayerFileName
    ##  Returns the layer file name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def LayerFileName(self) -> str:
        """
        Getter for property: (str) LayerFileName
         Returns the layer file name   
            
         
        """
        pass
    
    ## Setter for property: (str) LayerFileName

    ##  Returns the layer file name   
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @LayerFileName.setter
    def LayerFileName(self, fileName: str):
        """
        Setter for property: (str) LayerFileName
         Returns the layer file name   
            
         
        """
        pass
    
    ## Getter for property: (str) LayerName
    ##  Returns the layer name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def LayerName(self) -> str:
        """
        Getter for property: (str) LayerName
         Returns the layer name   
            
         
        """
        pass
    
    ## Setter for property: (str) LayerName

    ##  Returns the layer name   
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @LayerName.setter
    def LayerName(self, name: str):
        """
        Setter for property: (str) LayerName
         Returns the layer name   
            
         
        """
        pass
    
import NXOpen
##  This class is used to create a new postprocessor.
##             Calling @link Builder::Commit Builder::Commit@endlink  on this builder will only return NULL.
##          <br> To create a new instance of this class, use @link NXOpen::SIM::PostConfigurator::PostConfiguratorManager::CreateCreationPostBuilder  NXOpen::SIM::PostConfigurator::PostConfiguratorManager::CreateCreationPostBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.3  <br> 

class CreationPostBuilder(NXOpen.Builder): 
    """ This class is used to create a new postprocessor.
            Calling <ja_method>Builder.Commit</ja_method> on this builder will only return <ja_NULL>.
        """


    ## Getter for property: (str) ControllerName
    ##  Returns the controller's name that is used for the postprocessor.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## @return str
    @property
    def ControllerName(self) -> str:
        """
        Getter for property: (str) ControllerName
         Returns the controller's name that is used for the postprocessor.  
            
         
        """
        pass
    
    ## Setter for property: (str) ControllerName

    ##  Returns the controller's name that is used for the postprocessor.  
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    @ControllerName.setter
    def ControllerName(self, name: str):
        """
        Setter for property: (str) ControllerName
         Returns the controller's name that is used for the postprocessor.  
            
         
        """
        pass
    
    ## Getter for property: (bool) CreateDirectoryForPostprocessor
    ##  Returns the Flag whether postprocessor's output directory is created with the postprocessor name or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return bool
    @property
    def CreateDirectoryForPostprocessor(self) -> bool:
        """
        Getter for property: (bool) CreateDirectoryForPostprocessor
         Returns the Flag whether postprocessor's output directory is created with the postprocessor name or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateDirectoryForPostprocessor

    ##  Returns the Flag whether postprocessor's output directory is created with the postprocessor name or not.  
    ##      
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @CreateDirectoryForPostprocessor.setter
    def CreateDirectoryForPostprocessor(self, toggleState: bool):
        """
        Setter for property: (bool) CreateDirectoryForPostprocessor
         Returns the Flag whether postprocessor's output directory is created with the postprocessor name or not.  
             
         
        """
        pass
    
    ## Getter for property: (str) MachineName
    ##  Returns the machine's name that is used for the postprocessor.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## @return str
    @property
    def MachineName(self) -> str:
        """
        Getter for property: (str) MachineName
         Returns the machine's name that is used for the postprocessor.  
            
         
        """
        pass
    
    ## Setter for property: (str) MachineName

    ##  Returns the machine's name that is used for the postprocessor.  
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    @MachineName.setter
    def MachineName(self, name: str):
        """
        Setter for property: (str) MachineName
         Returns the machine's name that is used for the postprocessor.  
            
         
        """
        pass
    
    ## Getter for property: (str) ManufacturerName
    ##  Returns the manufacturer's name that is used for the postprocessor.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## @return str
    @property
    def ManufacturerName(self) -> str:
        """
        Getter for property: (str) ManufacturerName
         Returns the manufacturer's name that is used for the postprocessor.  
            
         
        """
        pass
    
    ## Setter for property: (str) ManufacturerName

    ##  Returns the manufacturer's name that is used for the postprocessor.  
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    @ManufacturerName.setter
    def ManufacturerName(self, name: str):
        """
        Setter for property: (str) ManufacturerName
         Returns the manufacturer's name that is used for the postprocessor.  
            
         
        """
        pass
    
    ## Getter for property: (str) PostprocessorName
    ##  Returns the postprocessor's name.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## @return str
    @property
    def PostprocessorName(self) -> str:
        """
        Getter for property: (str) PostprocessorName
         Returns the postprocessor's name.  
             
         
        """
        pass
    
    ## Setter for property: (str) PostprocessorName

    ##  Returns the postprocessor's name.  
    ##      
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    @PostprocessorName.setter
    def PostprocessorName(self, name: str):
        """
        Setter for property: (str) PostprocessorName
         Returns the postprocessor's name.  
             
         
        """
        pass
    
    ## Getter for property: (str) PostprocessorOutputDirectory
    ##  Returns the postprocessor's output directory where the postprocessor is created.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## @return str
    @property
    def PostprocessorOutputDirectory(self) -> str:
        """
        Getter for property: (str) PostprocessorOutputDirectory
         Returns the postprocessor's output directory where the postprocessor is created.  
             
         
        """
        pass
    
    ## Setter for property: (str) PostprocessorOutputDirectory

    ##  Returns the postprocessor's output directory where the postprocessor is created.  
    ##      
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    @PostprocessorOutputDirectory.setter
    def PostprocessorOutputDirectory(self, outputDirectory: str):
        """
        Setter for property: (str) PostprocessorOutputDirectory
         Returns the postprocessor's output directory where the postprocessor is created.  
             
         
        """
        pass
    
    ##  Returns the list of controller names in the postprocessor.
    ##  @return controllerNames (List[str]):  the list of available controller .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    def GetControllerNames(self) -> List[str]:
        """
         Returns the list of controller names in the postprocessor.
         @return controllerNames (List[str]):  the list of available controller .
        """
        pass
    
    ##  Returns the layer value.
    ##  @return value (str):  The layer value .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="layerName"> (str)  The layer name </param>
    def GetLayerNameValue(self, layerName: str) -> str:
        """
         Returns the layer value.
         @return value (str):  The layer value .
        """
        pass
    
    ##  Returns the list of layer value in the postprocessor.
    ##  @return layerValues (List[str]):  the list of available layer value .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="layerName"> (str)  The layer name </param>
    def GetLayerNames(self, layerName: str) -> List[str]:
        """
         Returns the list of layer value in the postprocessor.
         @return layerValues (List[str]):  the list of available layer value .
        """
        pass
    
    ##  Returns the list of machine names in the postprocessor.
    ##  @return machineNames (List[str]):  the list of available machine .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    def GetMachineNames(self) -> List[str]:
        """
         Returns the list of machine names in the postprocessor.
         @return machineNames (List[str]):  the list of available machine .
        """
        pass
    
    ##  Returns the list of manufacturer names in the postprocessor.
    ##  @return manufacturerNames (List[str]):  the list of available manufacturer .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: None.
    def GetManufacturerNames(self) -> List[str]:
        """
         Returns the list of manufacturer names in the postprocessor.
         @return manufacturerNames (List[str]):  the list of available manufacturer .
        """
        pass
    
    ##  Sets the layer value.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ## <param name="layerName"> (str)  The layer name </param>
    ## <param name="value"> (str)  The layer value </param>
    def SetLayerNameValue(self, layerName: str, value: str) -> None:
        """
         Sets the layer value.
        """
        pass
    
import NXOpen
##  This class is used to create a post definition editor builder.
##             Calling @link Builder::Commit Builder::Commit@endlink  on this builder will only return NULL.
##          <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class DefEditorBuilder(NXOpen.Builder): 
    """ This class is used to create a post definition editor builder.
            Calling <ja_method>Builder.Commit</ja_method> on this builder will only return <ja_NULL>.
        """


    ##  The address force type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## On</term><description> 
    ## </description> </item><item><term> 
    ## Once</term><description> 
    ## </description> </item><item><term> 
    ## Always</term><description> 
    ## </description> </item></list>
    class AddressForceType(Enum):
        """
        Members Include: <On> <Once> <Always>
        """
        On: int
        Once: int
        Always: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DefEditorBuilder.AddressForceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The address leader type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Literal</term><description> 
    ## </description> </item><item><term> 
    ## Expression</term><description> 
    ## </description> </item></list>
    class AddressLeaderType(Enum):
        """
        Members Include: <Literal> <Expression>
        """
        Literal: int
        Expression: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DefEditorBuilder.AddressLeaderType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The address limit handle 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## TruncateValue</term><description> 
    ## </description> </item><item><term> 
    ## WarnUser</term><description> 
    ## </description> </item><item><term> 
    ## AbortProcess</term><description> 
    ## </description> </item><item><term> 
    ## Reset</term><description> 
    ## </description> </item></list>
    class AddressLimitHandleType(Enum):
        """
        Members Include: <TruncateValue> <WarnUser> <AbortProcess> <Reset>
        """
        TruncateValue: int
        WarnUser: int
        AbortProcess: int
        Reset: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DefEditorBuilder.AddressLimitHandleType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The address trailer type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Literal</term><description> 
    ## </description> </item><item><term> 
    ## Expression</term><description> 
    ## </description> </item></list>
    class AddressTrailerType(Enum):
        """
        Members Include: <Literal> <Expression>
        """
        Literal: int
        Expression: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DefEditorBuilder.AddressTrailerType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The block template item type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Literal</term><description> 
    ## </description> </item><item><term> 
    ## Address</term><description> 
    ## </description> </item><item><term> 
    ## TurboAddress</term><description> 
    ## </description> </item></list>
    class BlockItemType(Enum):
        """
        Members Include: <Literal> <Address> <TurboAddress>
        """
        Literal: int
        Address: int
        TurboAddress: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DefEditorBuilder.BlockItemType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The format type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Numeric</term><description> 
    ## </description> </item><item><term> 
    ## Text</term><description> 
    ## </description> </item></list>
    class FormatType(Enum):
        """
        Members Include: <Numeric> <Text>
        """
        Numeric: int
        Text: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DefEditorBuilder.FormatType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) CurrentLayer
    ##  Returns the current layer.  
    ##    The current layer is editing by DefEditor   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return str
    @property
    def CurrentLayer(self) -> str:
        """
        Getter for property: (str) CurrentLayer
         Returns the current layer.  
           The current layer is editing by DefEditor   
         
        """
        pass
    
    ## Setter for property: (str) CurrentLayer

    ##  Returns the current layer.  
    ##    The current layer is editing by DefEditor   
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @CurrentLayer.setter
    def CurrentLayer(self, layerName: str):
        """
        Setter for property: (str) CurrentLayer
         Returns the current layer.  
           The current layer is editing by DefEditor   
         
        """
        pass
    
    ##  Add new address to custom def file, replace existing one 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ## <param name="addressName"> (str) </param>
    ## <param name="formatName"> (str) </param>
    ## <param name="zeroLimitName"> (str) </param>
    ## <param name="forceType"> (@link DefEditorBuilder.AddressForceType NXOpen.SIM.PostConfigurator.DefEditorBuilder.AddressForceType@endlink) </param>
    ## <param name="leader"> (str) </param>
    ## <param name="leaderType"> (@link DefEditorBuilder.AddressLeaderType NXOpen.SIM.PostConfigurator.DefEditorBuilder.AddressLeaderType@endlink) </param>
    ## <param name="trailer"> (str) </param>
    ## <param name="trailerType"> (@link DefEditorBuilder.AddressTrailerType NXOpen.SIM.PostConfigurator.DefEditorBuilder.AddressTrailerType@endlink) </param>
    ## <param name="maxIsDefine"> (bool) </param>
    ## <param name="maxLimit"> (float) </param>
    ## <param name="maxHandeType"> (@link DefEditorBuilder.AddressLimitHandleType NXOpen.SIM.PostConfigurator.DefEditorBuilder.AddressLimitHandleType@endlink) </param>
    ## <param name="minIsDefine"> (bool) </param>
    ## <param name="minLimit"> (float) </param>
    ## <param name="minHandeType"> (@link DefEditorBuilder.AddressLimitHandleType NXOpen.SIM.PostConfigurator.DefEditorBuilder.AddressLimitHandleType@endlink) </param>
    def AddAddress(self, addressName: str, formatName: str, zeroLimitName: str, forceType: DefEditorBuilder.AddressForceType, leader: str, leaderType: DefEditorBuilder.AddressLeaderType, trailer: str, trailerType: DefEditorBuilder.AddressTrailerType, maxIsDefine: bool, maxLimit: float, maxHandeType: DefEditorBuilder.AddressLimitHandleType, minIsDefine: bool, minLimit: float, minHandeType: DefEditorBuilder.AddressLimitHandleType) -> None:
        """
         Add new address to custom def file, replace existing one 
        """
        pass
    
    ##  Add omit to address 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ## <param name="addressName"> (str) </param>
    ## <param name="formatName"> (str) </param>
    ## <param name="zeroLimitName"> (str) </param>
    ## <param name="forceType"> (@link DefEditorBuilder.AddressForceType NXOpen.SIM.PostConfigurator.DefEditorBuilder.AddressForceType@endlink) </param>
    ## <param name="leader"> (str) </param>
    ## <param name="leaderType"> (@link DefEditorBuilder.AddressLeaderType NXOpen.SIM.PostConfigurator.DefEditorBuilder.AddressLeaderType@endlink) </param>
    ## <param name="trailer"> (str) </param>
    ## <param name="trailerType"> (@link DefEditorBuilder.AddressTrailerType NXOpen.SIM.PostConfigurator.DefEditorBuilder.AddressTrailerType@endlink) </param>
    ## <param name="maxIsDefine"> (bool) </param>
    ## <param name="maxLimit"> (float) </param>
    ## <param name="maxHandeType"> (@link DefEditorBuilder.AddressLimitHandleType NXOpen.SIM.PostConfigurator.DefEditorBuilder.AddressLimitHandleType@endlink) </param>
    ## <param name="minIsDefine"> (bool) </param>
    ## <param name="minLimit"> (float) </param>
    ## <param name="minHandeType"> (@link DefEditorBuilder.AddressLimitHandleType NXOpen.SIM.PostConfigurator.DefEditorBuilder.AddressLimitHandleType@endlink) </param>
    ## <param name="omit"> (str) </param>
    def AddAddressWithOmit(self, addressName: str, formatName: str, zeroLimitName: str, forceType: DefEditorBuilder.AddressForceType, leader: str, leaderType: DefEditorBuilder.AddressLeaderType, trailer: str, trailerType: DefEditorBuilder.AddressTrailerType, maxIsDefine: bool, maxLimit: float, maxHandeType: DefEditorBuilder.AddressLimitHandleType, minIsDefine: bool, minLimit: float, minHandeType: DefEditorBuilder.AddressLimitHandleType, omit: str) -> None:
        """
         Add omit to address 
        """
        pass
    
    ##  Add block address to custom def file
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ## <param name="blockTemplateName"> (str) </param>
    ## <param name="blockAddressName"> (str) </param>
    ## <param name="blockItemType"> (int) </param>
    ## <param name="expression"> (str) </param>
    ## <param name="addressIndex"> (int) </param>
    ## <param name="isOptional"> (bool) </param>
    ## <param name="hasNoWordSeparator"> (bool) </param>
    def AddBlockAddress(self, blockTemplateName: str, blockAddressName: str, blockItemType: int, expression: str, addressIndex: int, isOptional: bool, hasNoWordSeparator: bool) -> None:
        """
         Add block address to custom def file
        """
        pass
    
    ##  Add new block template to custom def file, replace existing one 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ## <param name="blockTemplateName"> (str) </param>
    ## <param name="blockAddressName"> (List[str]) </param>
    ## <param name="blockItemType"> (@link DefEditorBuilder.BlockItemType List[NXOpen.SIM.PostConfigurator.DefEditorBuilder.BlockItemType]@endlink) </param>
    ## <param name="expression"> (List[str]) </param>
    ## <param name="addressIndex"> (List[int]) </param>
    ## <param name="isOptional"> (List[bool]) </param>
    ## <param name="hasNoWordSeparator"> (List[bool]) </param>
    def AddBlockTemplate(self, blockTemplateName: str, blockAddressName: List[str], blockItemType: List[DefEditorBuilder.BlockItemType], expression: List[str], addressIndex: List[int], isOptional: List[bool], hasNoWordSeparator: List[bool]) -> None:
        """
         Add new block template to custom def file, replace existing one 
        """
        pass
    
    ##  Add format to custom def file, replace existing one 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ## <param name="formatName"> (str) </param>
    ## <param name="isOutputLeaderPlusSign"> (bool) </param>
    ## <param name="isOutputLeadingZeros"> (bool) </param>
    ## <param name="isOutputDecimalPoint"> (bool) </param>
    ## <param name="isOutputTrailingZeros"> (bool) </param>
    ## <param name="visibleDigits"> (int) </param>
    ## <param name="visibleDecimals"> (int) </param>
    ## <param name="formatType"> (@link DefEditorBuilder.FormatType NXOpen.SIM.PostConfigurator.DefEditorBuilder.FormatType@endlink) </param>
    def AddFormat(self, formatName: str, isOutputLeaderPlusSign: bool, isOutputLeadingZeros: bool, isOutputDecimalPoint: bool, isOutputTrailingZeros: bool, visibleDigits: int, visibleDecimals: int, formatType: DefEditorBuilder.FormatType) -> None:
        """
         Add format to custom def file, replace existing one 
        """
        pass
    
    ##  Delete address of custom def file 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ## <param name="addressName"> (str) </param>
    def DeleteAddress(self, addressName: str) -> None:
        """
         Delete address of custom def file 
        """
        pass
    
    ##  Delete block address of custom def file 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ## <param name="blockTemplateName"> (str) </param>
    ## <param name="addressName"> (str) </param>
    def DeleteBlockAddress(self, blockTemplateName: str, addressName: str) -> None:
        """
         Delete block address of custom def file 
        """
        pass
    
    ##  Delete block template of custom def file 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ## <param name="blockTemplateName"> (str) </param>
    def DeleteBlockTemplate(self, blockTemplateName: str) -> None:
        """
         Delete block template of custom def file 
        """
        pass
    
    ##  Delete format of custom def file 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ## <param name="formatName"> (str) </param>
    def DeleteFormat(self, formatName: str) -> None:
        """
         Delete format of custom def file 
        """
        pass
    
    ##  Get omit of address  
    ##  @return omit (str):  the address omit.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="addressName"> (str)  the address name</param>
    def GetAddressOmit(self, addressName: str) -> str:
        """
         Get omit of address  
         @return omit (str):  the address omit.
        """
        pass
    
import NXOpen
##  This class is used to encrypt the post builder or tcl based postprocessor.
##             Calling @link Builder::Commit Builder::Commit@endlink  on this builder will only return NULL.
##          <br> To create a new instance of this class, use @link NXOpen::SIM::PostConfigurator::PostConfiguratorManager::CreateEncryptPostprocessorFilesBuilder  NXOpen::SIM::PostConfigurator::PostConfiguratorManager::CreateEncryptPostprocessorFilesBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class EncryptPostprocessorFilesBuilder(NXOpen.Builder): 
    """ This class is used to encrypt the post builder or tcl based postprocessor.
            Calling <ja_method>Builder.Commit</ja_method> on this builder will only return <ja_NULL>.
        """


    ## Getter for property: (str) ExpirationDate
    ##  Returns the expiration date.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def ExpirationDate(self) -> str:
        """
        Getter for property: (str) ExpirationDate
         Returns the expiration date.  
             
         
        """
        pass
    
    ## Setter for property: (str) ExpirationDate

    ##  Returns the expiration date.  
    ##      
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ExpirationDate.setter
    def ExpirationDate(self, expirationDate: str):
        """
        Setter for property: (str) ExpirationDate
         Returns the expiration date.  
             
         
        """
        pass
    
    ## Getter for property: (str) SMKSLicensecheck
    ##  Returns the SMKS license check.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def SMKSLicensecheck(self) -> str:
        """
        Getter for property: (str) SMKSLicensecheck
         Returns the SMKS license check.  
             
         
        """
        pass
    
    ## Setter for property: (str) SMKSLicensecheck

    ##  Returns the SMKS license check.  
    ##      
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @SMKSLicensecheck.setter
    def SMKSLicensecheck(self, smksLicensecheck: str):
        """
        Setter for property: (str) SMKSLicensecheck
         Returns the SMKS license check.  
             
         
        """
        pass
    
    ##  Gets the encrypt postprocessor files. 
    ##                 This function allocates the memory for encryptFiles. The caller is responsible to deallocate the memory. 
    ##  @return encryptFiles (List[str]):  the encrypt files .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    def GetEncryptPostprocessorFiles(self) -> List[str]:
        """
         Gets the encrypt postprocessor files. 
                        This function allocates the memory for encryptFiles. The caller is responsible to deallocate the memory. 
         @return encryptFiles (List[str]):  the encrypt files .
        """
        pass
    
    ##  Gets the sold to ids. 
    ##  @return soldToIDs (str):  the sold to ids .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    def GetSoldToIds(self) -> str:
        """
         Gets the sold to ids. 
         @return soldToIDs (str):  the sold to ids .
        """
        pass
    
    ##  Sets the encrypt postprocessor files. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator")
    ## 
    ## <param name="encryptFilename"> (List[str])  the fullpath encrypt filename </param>
    def SetEncryptPostprocessorFiles(self, encryptFilename: List[str]) -> None:
        """
         Sets the encrypt postprocessor files. 
        """
        pass
    
    ##  Sets the sold to ids. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator")
    ## 
    ## <param name="soldToIDs"> (str)  the sold to ids </param>
    def SetSoldToIds(self, soldToIDs: str) -> None:
        """
         Sets the sold to ids. 
        """
        pass
    
import NXOpen
##  This class is represents a @link SIM::PostConfigurator::LayerManagerBuilder SIM::PostConfigurator::LayerManagerBuilder@endlink .
##             Calling @link Builder::Commit Builder::Commit@endlink  on this builder will only return NULL.
##          <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX12.0.1  <br> 

class LayerManagerBuilder(NXOpen.Builder): 
    """ This class is represents a <ja_class>SIM.PostConfigurator.LayerManagerBuilder</ja_class>.
            Calling <ja_method>Builder.Commit</ja_method> on this builder will only return <ja_NULL>.
        """


    ## Getter for property: (@link AddLayerBuilder NXOpen.SIM.PostConfigurator.AddLayerBuilder@endlink) AddLayerBuilder
    ##  Returns the add layer builder   
    ##     
    ##  
    ## Getter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return AddLayerBuilder
    @property
    def AddLayerBuilder(self) -> AddLayerBuilder:
        """
        Getter for property: (@link AddLayerBuilder NXOpen.SIM.PostConfigurator.AddLayerBuilder@endlink) AddLayerBuilder
         Returns the add layer builder   
            
         
        """
        pass
    
    ##  Exports a specific layer 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ## <param name="layerName"> (str)  the layer name </param>
    ## <param name="destFolder"> (str)  the export folder </param>
    def ExportLayer(self, layerName: str, destFolder: str) -> None:
        """
         Exports a specific layer 
        """
        pass
    
    ##  Imports a specific layer 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ## <param name="layerFile"> (str)  the import layer file </param>
    def ImportLayer(self, layerFile: str) -> None:
        """
         Imports a specific layer 
        """
        pass
    
    ##  Removes a specific layer 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ## <param name="layerName"> (str)  the layer name </param>
    def RemoveLayer(self, layerName: str) -> None:
        """
         Removes a specific layer 
        """
        pass
    
import NXOpen
import NXOpen.CAM
##  This class is used to create a post configurator builder.
##             Calling @link Builder::Commit Builder::Commit@endlink  on this builder will only return NULL.
##          <br> To create a new instance of this class, use @link NXOpen::SIM::PostConfigurator::PostConfiguratorManager::CreatePostConfiguratorBuilder  NXOpen::SIM::PostConfigurator::PostConfiguratorManager::CreatePostConfiguratorBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.3  <br> 

class PostConfiguratorBuilder(NXOpen.Builder): 
    """ This class is used to create a post configurator builder.
            Calling <ja_method>Builder.Commit</ja_method> on this builder will only return <ja_NULL>.
        """


    ##  The result of creating custom definition file 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NoError</term><description> 
    ## </description> </item><item><term> 
    ## DirWriteprotectError</term><description> 
    ## </description> </item><item><term> 
    ## NoCustomerError</term><description> 
    ## </description> </item><item><term> 
    ## CustomFileExistError</term><description> 
    ## </description> </item><item><term> 
    ## FileWriteprotectError</term><description> 
    ## </description> </item><item><term> 
    ## UnknownError</term><description> 
    ## </description> </item></list>
    class DefWriterErrorType(Enum):
        """
        Members Include: <NoError> <DirWriteprotectError> <NoCustomerError> <CustomFileExistError> <FileWriteprotectError> <UnknownError>
        """
        NoError: int
        DirWriteprotectError: int
        NoCustomerError: int
        CustomFileExistError: int
        FileWriteprotectError: int
        UnknownError: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PostConfiguratorBuilder.DefWriterErrorType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The property access type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## No</term><description> 
    ##  The property has no read or write access. </description> </item><item><term> 
    ## Read</term><description> 
    ##  The property has read only access. </description> </item><item><term> 
    ## Full</term><description> 
    ##  The property has read and write access. </description> </item></list>
    class PropertyAccessType(Enum):
        """
        Members Include: <No> <Read> <Full>
        """
        No: int
        Read: int
        Full: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PostConfiguratorBuilder.PropertyAccessType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The property datafield type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Unknown</term><description> 
    ##  Unknown datafield type </description> </item><item><term> 
    ## Single</term><description> 
    ##  Single datafield type </description> </item><item><term> 
    ## Option</term><description> 
    ##  Option datafield type </description> </item></list>
    class PropertyDataFieldType(Enum):
        """
        Members Include: <Unknown> <Single> <Option>
        """
        Unknown: int
        Single: int
        Option: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PostConfiguratorBuilder.PropertyDataFieldType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The property data type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Unknown</term><description> 
    ##  Unknown data type </description> </item><item><term> 
    ## Integer</term><description> 
    ##  Integer data type </description> </item><item><term> 
    ## Double</term><description> 
    ##  Double data type </description> </item><item><term> 
    ## String</term><description> 
    ##  String data type </description> </item><item><term> 
    ## Option</term><description> 
    ##  Option data type </description> </item><item><term> 
    ## Vector</term><description> 
    ##  Vector data type </description> </item><item><term> 
    ## Multistring</term><description> 
    ##  Multistring data type </description> </item><item><term> 
    ## Point</term><description> 
    ##  Point data type </description> </item></list>
    class PropertyDataType(Enum):
        """
        Members Include: <Unknown> <Integer> <Double> <String> <Option> <Vector> <Multistring> <Point>
        """
        Unknown: int
        Integer: int
        Double: int
        String: int
        Option: int
        Vector: int
        Multistring: int
        Point: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PostConfiguratorBuilder.PropertyDataType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The property option type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Unknown</term><description> 
    ##  Unknown option type </description> </item><item><term> 
    ## Value</term><description> 
    ##  Value option type </description> </item><item><term> 
    ## Enum</term><description> 
    ##  Enum option type </description> </item></list>
    class PropertyOptionType(Enum):
        """
        Members Include: <Unknown> <Value> <Enum>
        """
        Unknown: int
        Value: int
        Enum: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PostConfiguratorBuilder.PropertyOptionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The property value changed status type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Unchanged</term><description> 
    ##  If the value is equal to default value. </description> </item><item><term> 
    ## Changed</term><description> 
    ##  If the value is different to default value. </description> </item><item><term> 
    ## UnremoveUnchanged</term><description> 
    ##  If the value is equal to default value and the property cannot be removed. </description> </item><item><term> 
    ## UnremoveChanged</term><description> 
    ##  If the value is different to default value and the property cannot be removed. </description> </item><item><term> 
    ## UnaddUnchanged</term><description> 
    ##  If the value is equal to default value and the property cannot be added. </description> </item><item><term> 
    ## UnaddChanged</term><description> 
    ##  If the value is different to default value and the property cannot be added. </description> </item></list>
    class PropertyValueChangedStatusType(Enum):
        """
        Members Include: <Unchanged> <Changed> <UnremoveUnchanged> <UnremoveChanged> <UnaddUnchanged> <UnaddChanged>
        """
        Unchanged: int
        Changed: int
        UnremoveUnchanged: int
        UnremoveChanged: int
        UnaddUnchanged: int
        UnaddChanged: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PostConfiguratorBuilder.PropertyValueChangedStatusType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The displayed unit system type in the post configurator properties 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Millimeters</term><description> 
    ##  The Units is in Millimeters. </description> </item><item><term> 
    ## Inches</term><description> 
    ##  The Units is in Inches. </description> </item><item><term> 
    ## MillimetersAndInches</term><description> 
    ##  The Units is in Millimeters and Inches. </description> </item></list>
    class UnitsType(Enum):
        """
        Members Include: <Millimeters> <Inches> <MillimetersAndInches>
        """
        Millimeters: int
        Inches: int
        MillimetersAndInches: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PostConfiguratorBuilder.UnitsType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.DateBuilder NXOpen.DateBuilder@endlink) DateValue
    ##  Returns the date value.  
    ##    The Date object will contain the value for expiration date.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## @return NXOpen.DateBuilder
    @property
    def DateValue(self) -> NXOpen.DateBuilder:
        """
        Getter for property: (@link NXOpen.DateBuilder NXOpen.DateBuilder@endlink) DateValue
         Returns the date value.  
           The Date object will contain the value for expiration date.   
         
        """
        pass
    
    ## Getter for property: (@link DefEditorBuilder NXOpen.SIM.PostConfigurator.DefEditorBuilder@endlink) DefEditorBuilder
    ##  Returns the def editor builder.  
    ##      
    ##  
    ## Getter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return DefEditorBuilder
    @property
    def DefEditorBuilder(self) -> DefEditorBuilder:
        """
        Getter for property: (@link DefEditorBuilder NXOpen.SIM.PostConfigurator.DefEditorBuilder@endlink) DefEditorBuilder
         Returns the def editor builder.  
             
         
        """
        pass
    
    ## Getter for property: (@link LayerManagerBuilder NXOpen.SIM.PostConfigurator.LayerManagerBuilder@endlink) LayerManagerBuilder
    ##  Returns the layer editor builder   
    ##     
    ##  
    ## Getter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return LayerManagerBuilder
    @property
    def LayerManagerBuilder(self) -> LayerManagerBuilder:
        """
        Getter for property: (@link LayerManagerBuilder NXOpen.SIM.PostConfigurator.LayerManagerBuilder@endlink) LayerManagerBuilder
         Returns the layer editor builder   
            
         
        """
        pass
    
    ## Getter for property: (@link UdeEditorBuilder NXOpen.SIM.PostConfigurator.UdeEditorBuilder@endlink) UdeEditorBuilder
    ##  Returns the ude editor builder   
    ##     
    ##  
    ## Getter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return UdeEditorBuilder
    @property
    def UdeEditorBuilder(self) -> UdeEditorBuilder:
        """
        Getter for property: (@link UdeEditorBuilder NXOpen.SIM.PostConfigurator.UdeEditorBuilder@endlink) UdeEditorBuilder
         Returns the ude editor builder   
            
         
        """
        pass
    
    ## Getter for property: (@link PostConfiguratorBuilder.UnitsType NXOpen.SIM.PostConfigurator.PostConfiguratorBuilder.UnitsType@endlink) Units
    ##  Returns the displayed units in post configurator properties  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return PostConfiguratorBuilder.UnitsType
    @property
    def Units(self) -> PostConfiguratorBuilder.UnitsType:
        """
        Getter for property: (@link PostConfiguratorBuilder.UnitsType NXOpen.SIM.PostConfigurator.PostConfiguratorBuilder.UnitsType@endlink) Units
         Returns the displayed units in post configurator properties  
            
         
        """
        pass
    
    ## Setter for property: (@link PostConfiguratorBuilder.UnitsType NXOpen.SIM.PostConfigurator.PostConfiguratorBuilder.UnitsType@endlink) Units

    ##  Returns the displayed units in post configurator properties  
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @Units.setter
    def Units(self, type: PostConfiguratorBuilder.UnitsType):
        """
        Setter for property: (@link PostConfiguratorBuilder.UnitsType NXOpen.SIM.PostConfigurator.PostConfiguratorBuilder.UnitsType@endlink) Units
         Returns the displayed units in post configurator properties  
            
         
        """
        pass
    
    ## Getter for property: (@link UpdatePostprocessorBuilder NXOpen.SIM.PostConfigurator.UpdatePostprocessorBuilder@endlink) UpdatePostprocessorBuilder
    ##  Returns the update postprocessor builder   
    ##     
    ##  
    ## Getter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return UpdatePostprocessorBuilder
    @property
    def UpdatePostprocessorBuilder(self) -> UpdatePostprocessorBuilder:
        """
        Getter for property: (@link UpdatePostprocessorBuilder NXOpen.SIM.PostConfigurator.UpdatePostprocessorBuilder@endlink) UpdatePostprocessorBuilder
         Returns the update postprocessor builder   
            
         
        """
        pass
    
    ##  Adds the property to the selected chain
    ##                 The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ## <param name="chainID"> (str)  the chain id where the property should be added. "Default" as chain ID is not allowed </param>
    ## <param name="configurationObjectID"> (str)  the configuration object id </param>
    ## <param name="propertyID"> (str)  the property id </param>
    def AddProperty(self, chainID: str, configurationObjectID: str, propertyID: str) -> None:
        """
         Adds the property to the selected chain
                        The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets. 
        """
        pass
    
    ##  Copy the property data to the clipboard. 
    ##                 The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ## <param name="configurationObjectID"> (str)  the configuration object id </param>
    ## <param name="propertyID"> (str)  the property id </param>
    def CopyPropertyDataToClipboard(self, configurationObjectID: str, propertyID: str) -> None:
        """
         Copy the property data to the clipboard. 
                        The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets.
        """
        pass
    
    ##  Creates the Customer Cdl File. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    def CreateCustomCdlFile(self) -> None:
        """
         Creates the Customer Cdl File. 
        """
        pass
    
    ##  Create custom def file. 
    ##  @return errorCode (@link PostConfiguratorBuilder.DefWriterErrorType NXOpen.SIM.PostConfigurator.PostConfiguratorBuilder.DefWriterErrorType@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    def CreateCustomDefFile(self) -> PostConfiguratorBuilder.DefWriterErrorType:
        """
         Create custom def file. 
         @return errorCode (@link PostConfiguratorBuilder.DefWriterErrorType NXOpen.SIM.PostConfigurator.PostConfiguratorBuilder.DefWriterErrorType@endlink): .
        """
        pass
    
    ##  Encrypts a post processor with Sold-To ID and expiration date. 
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ## <param name="soldToID"> (str)  the sold to id </param>
    ## <param name="expirationDate"> (str)  the expiration date </param>
    def EncryptPostConfiguratorFiles(self, soldToID: str, expirationDate: str) -> None:
        """
         Encrypts a post processor with Sold-To ID and expiration date. 
        """
        pass
    
    ##  Gets the property access type. 
    ##                 The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets. 
    ##  @return accessType (@link PostConfiguratorBuilder.PropertyAccessType NXOpen.SIM.PostConfigurator.PostConfiguratorBuilder.PropertyAccessType@endlink):  the access type .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="chainID"> (str)  the chain id, for the single chain use empty string ("") or null pointer or "Default" as chain id. </param>
    ## <param name="configurationObjectID"> (str)  the configuration object id </param>
    ## <param name="propertyID"> (str)  the property id </param>
    def GetPropertyAccessType(self, chainID: str, configurationObjectID: str, propertyID: str) -> PostConfiguratorBuilder.PropertyAccessType:
        """
         Gets the property access type. 
                        The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets. 
         @return accessType (@link PostConfiguratorBuilder.PropertyAccessType NXOpen.SIM.PostConfigurator.PostConfiguratorBuilder.PropertyAccessType@endlink):  the access type .
        """
        pass
    
    ##  Gets the property chain ids. 
    ##                 This function allocates the memory for chainIds. The caller is responsible to deallocate the memory. 
    ##  @return chainIds (List[str]):  the chain ids .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def GetPropertyChainIds(self) -> List[str]:
        """
         Gets the property chain ids. 
                        This function allocates the memory for chainIds. The caller is responsible to deallocate the memory. 
         @return chainIds (List[str]):  the chain ids .
        """
        pass
    
    ##  Gets the property configuration object ids. 
    ##                 This function allocates the memory for chainIds. The caller is responsible to deallocate the memory. 
    ##  @return configurationObjectIds (List[str]):  the configuraton object ids .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def GetPropertyConfigurationObjectIds(self) -> List[str]:
        """
         Gets the property configuration object ids. 
                        This function allocates the memory for chainIds. The caller is responsible to deallocate the memory. 
         @return configurationObjectIds (List[str]):  the configuraton object ids .
        """
        pass
    
    ##  Gets the property data field type. 
    ##                 The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets. 
    ##  @return dataFieldType (@link PostConfiguratorBuilder.PropertyDataFieldType NXOpen.SIM.PostConfigurator.PostConfiguratorBuilder.PropertyDataFieldType@endlink):  the data field type .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="chainID"> (str)  the chain id, for the single chain use empty string ("") or null pointer or "Default" as chain id. </param>
    ## <param name="configurationObjectID"> (str)  the configuration object id </param>
    ## <param name="propertyID"> (str)  the property id </param>
    def GetPropertyDataFieldType(self, chainID: str, configurationObjectID: str, propertyID: str) -> PostConfiguratorBuilder.PropertyDataFieldType:
        """
         Gets the property data field type. 
                        The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets. 
         @return dataFieldType (@link PostConfiguratorBuilder.PropertyDataFieldType NXOpen.SIM.PostConfigurator.PostConfiguratorBuilder.PropertyDataFieldType@endlink):  the data field type .
        """
        pass
    
    ##  Gets the property data type. 
    ##                 The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets. 
    ##  @return dataType (@link PostConfiguratorBuilder.PropertyDataType NXOpen.SIM.PostConfigurator.PostConfiguratorBuilder.PropertyDataType@endlink):  the data type .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="chainID"> (str)  the chain id, for the single chain use empty string ("") or null pointer or "Default" as chain id. </param>
    ## <param name="configurationObjectID"> (str)  the configuration object id </param>
    ## <param name="propertyID"> (str)  the property id </param>
    def GetPropertyDataType(self, chainID: str, configurationObjectID: str, propertyID: str) -> PostConfiguratorBuilder.PropertyDataType:
        """
         Gets the property data type. 
                        The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets. 
         @return dataType (@link PostConfiguratorBuilder.PropertyDataType NXOpen.SIM.PostConfigurator.PostConfiguratorBuilder.PropertyDataType@endlink):  the data type .
        """
        pass
    
    ##  Gets the property default value.
    ##                 The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets.
    ##                 This function allocates the memory for defaultValues. The caller is responsible to deallocate the memory. 
    ##  @return defaultValues (List[str]):  the default values .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="chainID"> (str)  the chain id, for the single chain use empty string ("") or null pointer or "Default" as chain id. </param>
    ## <param name="configurationObjectID"> (str)  the configuration object id </param>
    ## <param name="propertyID"> (str)  the property id </param>
    def GetPropertyDefaultValue(self, chainID: str, configurationObjectID: str, propertyID: str) -> List[str]:
        """
         Gets the property default value.
                        The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets.
                        This function allocates the memory for defaultValues. The caller is responsible to deallocate the memory. 
         @return defaultValues (List[str]):  the default values .
        """
        pass
    
    ##  Gets the property description image.
    ##                 The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets. 
    ##  @return descriptionImage (str):  the description image .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="chainID"> (str)  the chain id, for the single chain use empty string ("") or null pointer or "Default" as chain id. </param>
    ## <param name="configurationObjectID"> (str)  the configuration object id </param>
    ## <param name="propertyID"> (str)  the property id </param>
    def GetPropertyDescriptionImage(self, chainID: str, configurationObjectID: str, propertyID: str) -> str:
        """
         Gets the property description image.
                        The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets. 
         @return descriptionImage (str):  the description image .
        """
        pass
    
    ##  Gets the property description text.
    ##                 The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets. 
    ##  @return descriptionText (str):  the description text .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="chainID"> (str)  the chain id, for the single chain use empty string ("") or null pointer or "Default" as chain id. </param>
    ## <param name="configurationObjectID"> (str)  the configuration object id </param>
    ## <param name="propertyID"> (str)  the property id </param>
    def GetPropertyDescriptionText(self, chainID: str, configurationObjectID: str, propertyID: str) -> str:
        """
         Gets the property description text.
                        The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets. 
         @return descriptionText (str):  the description text .
        """
        pass
    
    ##  Gets the property ids. 
    ##                 This function allocates the memory for chainIds. The caller is responsible to deallocate the memory. 
    ##  @return propertyIds (List[str]):  the property ids .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def GetPropertyIds(self) -> List[str]:
        """
         Gets the property ids. 
                        This function allocates the memory for chainIds. The caller is responsible to deallocate the memory. 
         @return propertyIds (List[str]):  the property ids .
        """
        pass
    
    ##  Gets the property option type. 
    ##                 The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets. 
    ##  @return optionType (@link PostConfiguratorBuilder.PropertyOptionType NXOpen.SIM.PostConfigurator.PostConfiguratorBuilder.PropertyOptionType@endlink):  the option type .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="chainID"> (str)  the chain id, for the single chain use empty string ("") or null pointer or "Default" as chain id. </param>
    ## <param name="configurationObjectID"> (str)  the configuration object id </param>
    ## <param name="propertyID"> (str)  the property id </param>
    def GetPropertyOptionType(self, chainID: str, configurationObjectID: str, propertyID: str) -> PostConfiguratorBuilder.PropertyOptionType:
        """
         Gets the property option type. 
                        The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets. 
         @return optionType (@link PostConfiguratorBuilder.PropertyOptionType NXOpen.SIM.PostConfigurator.PostConfiguratorBuilder.PropertyOptionType@endlink):  the option type .
        """
        pass
    
    ##  Gets the property options ID value. 
    ##                 The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets. 
    ##  @return optionsIDValue (str):  the options id value .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="chainID"> (str)  the chain id, for the single chain use empty string ("") or null pointer or "Default" as chain id. </param>
    ## <param name="configurationObjectID"> (str)  the configuration object id </param>
    ## <param name="propertyID"> (str)  the property id </param>
    def GetPropertyOptionsIdValue(self, chainID: str, configurationObjectID: str, propertyID: str) -> str:
        """
         Gets the property options ID value. 
                        The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets. 
         @return optionsIDValue (str):  the options id value .
        """
        pass
    
    ##  Gets the property options value. 
    ##                 The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets. 
    ##  @return optionsValue (str):  the options value .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="chainID"> (str)  the chain id, for the single chain use empty string ("") or null pointer or "Default" as chain id. </param>
    ## <param name="configurationObjectID"> (str)  the configuration object id </param>
    ## <param name="propertyID"> (str)  the property id </param>
    def GetPropertyOptionsValue(self, chainID: str, configurationObjectID: str, propertyID: str) -> str:
        """
         Gets the property options value. 
                        The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets. 
         @return optionsValue (str):  the options value .
        """
        pass
    
    ##  Gets the property value.
    ##                 The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets.
    ##                 This function allocates the memory for values. The caller is responsible to deallocate the memory. 
    ##  @return values (List[str]):  the values .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="chainID"> (str)  the chain id, for the single chain use empty string ("") or null pointer or "Default" as chain id. </param>
    ## <param name="configurationObjectID"> (str)  the configuration object id </param>
    ## <param name="propertyID"> (str)  the property id </param>
    def GetPropertyValue(self, chainID: str, configurationObjectID: str, propertyID: str) -> List[str]:
        """
         Gets the property value.
                        The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets.
                        This function allocates the memory for values. The caller is responsible to deallocate the memory. 
         @return values (List[str]):  the values .
        """
        pass
    
    ##  Gets the property value changed status. 
    ##                 The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets. 
    ##  @return valueChangedStatus (@link PostConfiguratorBuilder.PropertyValueChangedStatusType NXOpen.SIM.PostConfigurator.PostConfiguratorBuilder.PropertyValueChangedStatusType@endlink):  the value changed status .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="chainID"> (str)  the chain id, for the single chain use empty string ("") or null pointer or "Default" as chain id. </param>
    ## <param name="configurationObjectID"> (str)  the configuration object id </param>
    ## <param name="propertyID"> (str)  the property id </param>
    def GetPropertyValueChangedStatus(self, chainID: str, configurationObjectID: str, propertyID: str) -> PostConfiguratorBuilder.PropertyValueChangedStatusType:
        """
         Gets the property value changed status. 
                        The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets. 
         @return valueChangedStatus (@link PostConfiguratorBuilder.PropertyValueChangedStatusType NXOpen.SIM.PostConfigurator.PostConfiguratorBuilder.PropertyValueChangedStatusType@endlink):  the value changed status .
        """
        pass
    
    ##  Lists the property data in the information window. 
    ##                 The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ## <param name="configurationObjectID"> (str)  the configuration object id </param>
    ## <param name="propertyID"> (str)  the property id </param>
    def ListPropertyDataInInformationWindow(self, configurationObjectID: str, propertyID: str) -> None:
        """
         Lists the property data in the information window. 
                        The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets.
        """
        pass
    
    ##  Execute the tcl script to open the external documentation. 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    def OpenDocumentation(self) -> None:
        """
         Execute the tcl script to open the external documentation. 
        """
        pass
    
    ##  Postprocess the selected operation. 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ## <param name="objects"> (@link NXOpen.CAM.CAMObject List[NXOpen.CAM.CAMObject]@endlink)  array of objects </param>
    ## <param name="outputFilename"> (str)  the output filename </param>
    ## <param name="showOutputToListingWindow"> (bool)  the flag for show output to listing window  </param>
    def PostProcess(self, objects: List[NXOpen.CAM.CAMObject], outputFilename: str, showOutputToListingWindow: bool) -> None:
        """
         Postprocess the selected operation. 
        """
        pass
    
    ##  Removes the property from the selected chain
    ##                 The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ## <param name="chainID"> (str)  the chain id where the property should be removed. "Default" as chain ID is not allowed </param>
    ## <param name="configurationObjectID"> (str)  the configuration object id </param>
    ## <param name="propertyID"> (str)  the property id </param>
    def RemoveProperty(self, chainID: str, configurationObjectID: str, propertyID: str) -> None:
        """
         Removes the property from the selected chain
                        The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets. 
        """
        pass
    
    ##  Resets the post configurator data. 
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    def Reset(self) -> None:
        """
         Resets the post configurator data. 
        """
        pass
    
    ##  Saves the post configurator data. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    def Save(self) -> None:
        """
         Saves the post configurator data. 
        """
        pass
    
    ##  Saves the post configurator data in different name. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ## <param name="postprocessorName"> (str)  the postprocessor name </param>
    ## <param name="outputDirectory"> (str)  the output directory </param>
    def SaveAs(self, postprocessorName: str, outputDirectory: str) -> None:
        """
         Saves the post configurator data in different name. 
        """
        pass
    
    ##  Sets the property to default value. 
    ##                 The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ## <param name="chainID"> (str)  the chain id, for the single chain use empty string ("") or null pointer or "Default" as chain id. </param>
    ## <param name="configurationObjectID"> (str)  the configuration object id </param>
    ## <param name="propertyID"> (str)  the property id </param>
    def SetPropertyToDefaultValue(self, chainID: str, configurationObjectID: str, propertyID: str) -> None:
        """
         Sets the property to default value. 
                        The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets.
        """
        pass
    
    ##  Sets the property with string value. 
    ##                 The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## <param name="builder"> (@link PostConfiguratorBuilder NXOpen.SIM.PostConfigurator.PostConfiguratorBuilder@endlink) </param>
    ## <param name="chainID"> (str)  the chain id, for the single chain use empty string ("") or null pointer or "Default" as chain id. </param>
    ## <param name="configurationObjectID"> (str)  the configuration object id </param>
    ## <param name="propertyID"> (str)  the property id </param>
    ## <param name="value"> (str)  the value </param>
    @overload
    def SetPropertyValue(self, chainID: str, configurationObjectID: str, propertyID: str, value: str) -> None:
        """
         Sets the property with string value. 
                        The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets.
        """
        pass
    
    ##  Sets the property with multistring value. 
    ##                 The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## <param name="builder"> (@link PostConfiguratorBuilder NXOpen.SIM.PostConfigurator.PostConfiguratorBuilder@endlink) </param>
    ## <param name="chainID"> (str)  the chain id, for the single chain use empty string ("") or null pointer or "Default" as chain id. </param>
    ## <param name="configurationObjectID"> (str)  the configuration object id </param>
    ## <param name="propertyID"> (str)  the property id </param>
    ## <param name="value"> (List[str])  the string array value </param>
    @overload
    def SetPropertyValue(self, chainID: str, configurationObjectID: str, propertyID: str, value: List[str]) -> None:
        """
         Sets the property with multistring value. 
                        The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets.
        """
        pass
    
    ##  Sets the property with integer value. 
    ##                 The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## <param name="builder"> (@link PostConfiguratorBuilder NXOpen.SIM.PostConfigurator.PostConfiguratorBuilder@endlink) </param>
    ## <param name="chainID"> (str)  the chain id, for the single chain use empty string ("") or null pointer or "Default" as chain id. </param>
    ## <param name="configurationObjectID"> (str)  the configuration object id </param>
    ## <param name="propertyID"> (str)  the property id </param>
    ## <param name="value"> (int)  the value </param>
    @overload
    def SetPropertyValue(self, chainID: str, configurationObjectID: str, propertyID: str, value: int) -> None:
        """
         Sets the property with integer value. 
                        The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets.
        """
        pass
    
    ##  Sets the property with double value. 
    ##                 The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## <param name="builder"> (@link PostConfiguratorBuilder NXOpen.SIM.PostConfigurator.PostConfiguratorBuilder@endlink) </param>
    ## <param name="chainID"> (str)  the chain id, for the single chain use empty string ("") or null pointer or "Default" as chain id. </param>
    ## <param name="configurationObjectID"> (str)  the configuration object id </param>
    ## <param name="propertyID"> (str)  the property id </param>
    ## <param name="value"> (float)  the value </param>
    @overload
    def SetPropertyValue(self, chainID: str, configurationObjectID: str, propertyID: str, value: float) -> None:
        """
         Sets the property with double value. 
                        The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets.
        """
        pass
    
    ##  Sets the property with double array value. Used for vector or point property
    ##                 The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## <param name="builder"> (@link PostConfiguratorBuilder NXOpen.SIM.PostConfigurator.PostConfiguratorBuilder@endlink) </param>
    ## <param name="chainID"> (str)  the chain id, for the single chain use empty string ("") or null pointer or "Default" as chain id. </param>
    ## <param name="configurationObjectID"> (str)  the configuration object id </param>
    ## <param name="propertyID"> (str)  the property id </param>
    ## <param name="firstValue"> (float)  the first value </param>
    ## <param name="secondValue"> (float)  the second value </param>
    ## <param name="thirdValue"> (float)  the third value </param>
    @overload
    def SetPropertyValue(self, chainID: str, configurationObjectID: str, propertyID: str, firstValue: float, secondValue: float, thirdValue: float) -> None:
        """
         Sets the property with double array value. Used for vector or point property
                        The configurationObjectID and propertyID are documented under NX Help->Manufacturing(CAM)->Post Configurator->Post Configurator configuration objets.
        """
        pass
    
    ##  Shows the post configurator data changes in the listing window. 
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    def ShowChanges(self) -> None:
        """
         Shows the post configurator data changes in the listing window. 
        """
        pass
    
    ##  Update the ude editor builder. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def UpdateUdeEditorBuilder(self) -> None:
        """
         Update the ude editor builder. 
        """
        pass
    
import NXOpen
##  This class is represents a @link SIM::PostConfigurator::PostConfiguratorDebugBuilder SIM::PostConfigurator::PostConfiguratorDebugBuilder@endlink .
##             Calling @link Builder::Commit Builder::Commit@endlink  on this builder will only return NULL.
##          <br> To create a new instance of this class, use @link NXOpen::SIM::PostConfigurator::PostConfiguratorManager::CreatePostConfiguratorDebugBuilder  NXOpen::SIM::PostConfigurator::PostConfiguratorManager::CreatePostConfiguratorDebugBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.2  <br> 

class PostConfiguratorDebugBuilder(NXOpen.Builder): 
    """ This class is represents a <ja_class>SIM.PostConfigurator.PostConfiguratorDebugBuilder</ja_class>.
            Calling <ja_method>Builder.Commit</ja_method> on this builder will only return <ja_NULL>.
        """


    ##  Represents the dump type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ##  Dump Nothing </description> </item><item><term> 
    ## ShowChanges</term><description> 
    ##  Dump Show Changes </description> </item><item><term> 
    ## ShowAllSettings</term><description> 
    ##  Dump All Setting Values </description> </item></list>
    class DumpType(Enum):
        """
        Members Include: <NotSet> <ShowChanges> <ShowAllSettings>
        """
        NotSet: int
        ShowChanges: int
        ShowAllSettings: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PostConfiguratorDebugBuilder.DumpType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The output type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Syslog</term><description> 
    ##  Output to syslog </description> </item><item><term> 
    ## ListingWindow</term><description> 
    ##  Output to listing window </description> </item><item><term> 
    ## Xml</term><description> 
    ##  Output to xml </description> </item><item><term> 
    ## ToFile</term><description> 
    ##  Output to file </description> </item></list>
    class OutputType(Enum):
        """
        Members Include: <Syslog> <ListingWindow> <Xml> <ToFile>
        """
        Syslog: int
        ListingWindow: int
        Xml: int
        ToFile: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PostConfiguratorDebugBuilder.OutputType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the trace type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## CreatePostprocessor</term><description> 
    ##  Trace Create Postprocessor </description> </item><item><term> 
    ## SelectPostprocessor</term><description> 
    ##  Trace Select Postprocessor </description> </item></list>
    class TraceType(Enum):
        """
        Members Include: <CreatePostprocessor> <SelectPostprocessor>
        """
        CreatePostprocessor: int
        SelectPostprocessor: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PostConfiguratorDebugBuilder.TraceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link PostConfiguratorDebugBuilder.DumpType NXOpen.SIM.PostConfigurator.PostConfiguratorDebugBuilder.DumpType@endlink) Dump
    ##  Returns the dump   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return PostConfiguratorDebugBuilder.DumpType
    @property
    def Dump(self) -> PostConfiguratorDebugBuilder.DumpType:
        """
        Getter for property: (@link PostConfiguratorDebugBuilder.DumpType NXOpen.SIM.PostConfigurator.PostConfiguratorDebugBuilder.DumpType@endlink) Dump
         Returns the dump   
            
         
        """
        pass
    
    ## Setter for property: (@link PostConfiguratorDebugBuilder.DumpType NXOpen.SIM.PostConfigurator.PostConfiguratorDebugBuilder.DumpType@endlink) Dump

    ##  Returns the dump   
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Dump.setter
    def Dump(self, type: PostConfiguratorDebugBuilder.DumpType):
        """
        Setter for property: (@link PostConfiguratorDebugBuilder.DumpType NXOpen.SIM.PostConfigurator.PostConfiguratorDebugBuilder.DumpType@endlink) Dump
         Returns the dump   
            
         
        """
        pass
    
    ## Getter for property: (@link PostConfiguratorDebugBuilder.OutputType NXOpen.SIM.PostConfigurator.PostConfiguratorDebugBuilder.OutputType@endlink) Output
    ##  Returns the output   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return PostConfiguratorDebugBuilder.OutputType
    @property
    def Output(self) -> PostConfiguratorDebugBuilder.OutputType:
        """
        Getter for property: (@link PostConfiguratorDebugBuilder.OutputType NXOpen.SIM.PostConfigurator.PostConfiguratorDebugBuilder.OutputType@endlink) Output
         Returns the output   
            
         
        """
        pass
    
    ## Setter for property: (@link PostConfiguratorDebugBuilder.OutputType NXOpen.SIM.PostConfigurator.PostConfiguratorDebugBuilder.OutputType@endlink) Output

    ##  Returns the output   
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @Output.setter
    def Output(self, type: PostConfiguratorDebugBuilder.OutputType):
        """
        Setter for property: (@link PostConfiguratorDebugBuilder.OutputType NXOpen.SIM.PostConfigurator.PostConfiguratorDebugBuilder.OutputType@endlink) Output
         Returns the output   
            
         
        """
        pass
    
    ## Getter for property: (str) OutputToFileName
    ##  Returns the output filename   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return str
    @property
    def OutputToFileName(self) -> str:
        """
        Getter for property: (str) OutputToFileName
         Returns the output filename   
            
         
        """
        pass
    
    ## Setter for property: (str) OutputToFileName

    ##  Returns the output filename   
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @OutputToFileName.setter
    def OutputToFileName(self, name: str):
        """
        Setter for property: (str) OutputToFileName
         Returns the output filename   
            
         
        """
        pass
    
    ##  Gets the trace 
    ##  @return state (bool):  The state.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: None.
    ## 
    ## <param name="type"> (@link PostConfiguratorDebugBuilder.TraceType NXOpen.SIM.PostConfigurator.PostConfiguratorDebugBuilder.TraceType@endlink)  The trace type</param>
    def GetTrace(self, type: PostConfiguratorDebugBuilder.TraceType) -> bool:
        """
         Gets the trace 
         @return state (bool):  The state.
        """
        pass
    
    ## Sets the trace 
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator")
    ## 
    ## <param name="type"> (@link PostConfiguratorDebugBuilder.TraceType NXOpen.SIM.PostConfigurator.PostConfiguratorDebugBuilder.TraceType@endlink)  The trace type</param>
    ## <param name="state"> (bool)  The state</param>
    def SetTrace(self, type: PostConfiguratorDebugBuilder.TraceType, state: bool) -> None:
        """
        Sets the trace 
        """
        pass
    
import NXOpen
##  Represents Post Configurator Manager <br> Use @link NXOpen::Session::PostConfiguratorManager NXOpen::Session::PostConfiguratorManager@endlink  to get the instance of this class.  <br> 
## 
##   <br>  Created in NX10.0.3  <br> 

class PostConfiguratorManager(NXOpen.Object): 
    """ Represents Post Configurator Manager"""


    ##  Creates a @link NXOpen::SIM::PostConfigurator::CreationPostBuilder NXOpen::SIM::PostConfigurator::CreationPostBuilder@endlink  object 
    ##  @return creationPostBuilder (@link CreationPostBuilder NXOpen.SIM.PostConfigurator.CreationPostBuilder@endlink):  The new creation post builder .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    def CreateCreationPostBuilder() -> CreationPostBuilder:
        """
         Creates a @link NXOpen::SIM::PostConfigurator::CreationPostBuilder NXOpen::SIM::PostConfigurator::CreationPostBuilder@endlink  object 
         @return creationPostBuilder (@link CreationPostBuilder NXOpen.SIM.PostConfigurator.CreationPostBuilder@endlink):  The new creation post builder .
        """
        pass
    
    ##  Creates a @link NXOpen::SIM::PostConfigurator::EncryptPostprocessorFilesBuilder NXOpen::SIM::PostConfigurator::EncryptPostprocessorFilesBuilder@endlink  object 
    ##  @return postConfiguratorBuilder (@link EncryptPostprocessorFilesBuilder NXOpen.SIM.PostConfigurator.EncryptPostprocessorFilesBuilder@endlink):  The new encrypt postprocessor files builder .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator")
    ## <param name="postProcessorFilename"> (str)  the post processor filename (.pui) </param>
    def CreateEncryptPostprocessorFilesBuilder(postProcessorFilename: str) -> EncryptPostprocessorFilesBuilder:
        """
         Creates a @link NXOpen::SIM::PostConfigurator::EncryptPostprocessorFilesBuilder NXOpen::SIM::PostConfigurator::EncryptPostprocessorFilesBuilder@endlink  object 
         @return postConfiguratorBuilder (@link EncryptPostprocessorFilesBuilder NXOpen.SIM.PostConfigurator.EncryptPostprocessorFilesBuilder@endlink):  The new encrypt postprocessor files builder .
        """
        pass
    
    ##  Creates a @link NXOpen::SIM::PostConfigurator::PostConfiguratorBuilder NXOpen::SIM::PostConfigurator::PostConfiguratorBuilder@endlink  object 
    ##  @return postConfiguratorBuilder (@link PostConfiguratorBuilder NXOpen.SIM.PostConfigurator.PostConfiguratorBuilder@endlink):  The new post configurator builder .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## <param name="postProcessorFilename"> (str)  the post processor filename </param>
    def CreatePostConfiguratorBuilder(postProcessorFilename: str) -> PostConfiguratorBuilder:
        """
         Creates a @link NXOpen::SIM::PostConfigurator::PostConfiguratorBuilder NXOpen::SIM::PostConfigurator::PostConfiguratorBuilder@endlink  object 
         @return postConfiguratorBuilder (@link PostConfiguratorBuilder NXOpen.SIM.PostConfigurator.PostConfiguratorBuilder@endlink):  The new post configurator builder .
        """
        pass
    
    ##  Creates a @link NXOpen::SIM::PostConfigurator::PostConfiguratorDebugBuilder NXOpen::SIM::PostConfigurator::PostConfiguratorDebugBuilder@endlink  object 
    ##  @return postConfiguratorDebugBuilder (@link PostConfiguratorDebugBuilder NXOpen.SIM.PostConfigurator.PostConfiguratorDebugBuilder@endlink):  The new post configurator debug builder .
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator")
    def CreatePostConfiguratorDebugBuilder() -> PostConfiguratorDebugBuilder:
        """
         Creates a @link NXOpen::SIM::PostConfigurator::PostConfiguratorDebugBuilder NXOpen::SIM::PostConfigurator::PostConfiguratorDebugBuilder@endlink  object 
         @return postConfiguratorDebugBuilder (@link PostConfiguratorDebugBuilder NXOpen.SIM.PostConfigurator.PostConfiguratorDebugBuilder@endlink):  The new post configurator debug builder .
        """
        pass
    
    ##  Creates a @link NXOpen::SIM::PostConfigurator::UdeBuilder NXOpen::SIM::PostConfigurator::UdeBuilder@endlink  object 
    ##  @return udeBuilder (@link UdeBuilder NXOpen.SIM.PostConfigurator.UdeBuilder@endlink):  The new ude builder .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    def CreateUdeBuilder() -> UdeBuilder:
        """
         Creates a @link NXOpen::SIM::PostConfigurator::UdeBuilder NXOpen::SIM::PostConfigurator::UdeBuilder@endlink  object 
         @return udeBuilder (@link UdeBuilder NXOpen.SIM.PostConfigurator.UdeBuilder@endlink):  The new ude builder .
        """
        pass
    
    ##  Creates a @link NXOpen::SIM::PostConfigurator::UdeParameterBuilder NXOpen::SIM::PostConfigurator::UdeParameterBuilder@endlink  object 
    ##  @return udeParameterBuilder (@link UdeParameterBuilder NXOpen.SIM.PostConfigurator.UdeParameterBuilder@endlink):  The new ude parameter builder .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    def CreateUdeParameterBuilder() -> UdeParameterBuilder:
        """
         Creates a @link NXOpen::SIM::PostConfigurator::UdeParameterBuilder NXOpen::SIM::PostConfigurator::UdeParameterBuilder@endlink  object 
         @return udeParameterBuilder (@link UdeParameterBuilder NXOpen.SIM.PostConfigurator.UdeParameterBuilder@endlink):  The new ude parameter builder .
        """
        pass
    
import NXOpen
##  Represents a list of objects. <br> To create a new instance of this class, use @link NXOpen::Part::CreateObjectList  NXOpen::Part::CreateObjectList @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class UdeBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""


    ## Getter for property: (int) Length
    ##  Returns the length of the list   
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
         Returns the length of the list   
            
         
        """
        pass
    
    ##  Appends a set of objects to the list
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link UdeBuilderList NXOpen.SIM.PostConfigurator.UdeBuilderList@endlink) </param>
    ## <param name="objects"> (@link UdeBuilder List[NXOpen.SIM.PostConfigurator.UdeBuilder]@endlink)  items to append </param>
    @overload
    def Append(self, objects: List[UdeBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    
    ##  Appends an object to the list
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link UdeBuilderList NXOpen.SIM.PostConfigurator.UdeBuilderList@endlink) </param>
    ## <param name="objectValue"> (@link UdeBuilder NXOpen.SIM.PostConfigurator.UdeBuilder@endlink)  item to append </param>
    @overload
    def Append(self, objectValue: UdeBuilder) -> None:
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
    ## <param name="object_list"> (@link UdeBuilderList NXOpen.SIM.PostConfigurator.UdeBuilderList@endlink) </param>
    @overload
    def Clear(self) -> None:
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
    ## 
    ## <param name="delete_idx"> (int)  index of item to be deleted </param>
    def ClearIndex(self, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
            *   not change, but the item at this index is set to NULL.
            
        """
        pass
    
    ##  Clears the entire list 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link UdeBuilderList NXOpen.SIM.PostConfigurator.UdeBuilderList@endlink) </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the objects when removing them </param>
    @overload
    def Clear(self, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    
    ##  Erases the object from the list, but does not delete the object.
    ##         The list is shifted so that there isn't a null where the object used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link UdeBuilderList NXOpen.SIM.PostConfigurator.UdeBuilderList@endlink) </param>
    ## <param name="index"> (int)  index of item to be removed from the list </param>
    @overload
    def Erase(self, index: int) -> None:
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
    ## <param name="object_list"> (@link UdeBuilderList NXOpen.SIM.PostConfigurator.UdeBuilderList@endlink) </param>
    ## <param name="index"> (int)  index of item to be removed from the list </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the object </param>
    @overload
    def Erase(self, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    ## <param name="object_list"> (@link UdeBuilderList NXOpen.SIM.PostConfigurator.UdeBuilderList@endlink) </param>
    ## <param name="obj"> (@link UdeBuilder NXOpen.SIM.PostConfigurator.UdeBuilder@endlink)  object to be removed from the list </param>
    @overload
    def Erase(self, obj: UdeBuilder) -> None:
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
    ## <param name="object_list"> (@link UdeBuilderList NXOpen.SIM.PostConfigurator.UdeBuilderList@endlink) </param>
    ## <param name="obj"> (@link UdeBuilder NXOpen.SIM.PostConfigurator.UdeBuilder@endlink)  object to be removed from the list </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the object </param>
    @overload
    def Erase(self, obj: UdeBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    ## 
    ## <param name="obj"> (@link UdeBuilder NXOpen.SIM.PostConfigurator.UdeBuilder@endlink)  Object to find index for </param>
    def FindIndex(self, obj: UdeBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
            *   -1 is returned.
            
         @return index (int):  index of input object, -1 if not on list .
        """
        pass
    
    ##  Returns the object at the input index.  May be NULL.
    ##     
    ##  @return obj (@link UdeBuilder NXOpen.SIM.PostConfigurator.UdeBuilder@endlink):  object found at input index .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  index of object to return </param>
    def FindItem(self, index: int) -> UdeBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         @return obj (@link UdeBuilder NXOpen.SIM.PostConfigurator.UdeBuilder@endlink):  object found at input index .
        """
        pass
    
    ##  Gets the contents of the entire list 
    ##  @return objects (@link UdeBuilder List[NXOpen.SIM.PostConfigurator.UdeBuilder]@endlink):  The list contents .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetContents(self) -> List[UdeBuilder]:
        """
         Gets the contents of the entire list 
         @return objects (@link UdeBuilder List[NXOpen.SIM.PostConfigurator.UdeBuilder]@endlink):  The list contents .
        """
        pass
    
    ##  Inserts an object at the specified location 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="location"> (int)  location at which to insert the object </param>
    ## <param name="objectValue"> (@link UdeBuilder NXOpen.SIM.PostConfigurator.UdeBuilder@endlink)  object to be inserted </param>
    def Insert(self, location: int, objectValue: UdeBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    
    ##  Move object at the specified location to the bottom of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  location of the item </param>
    def MoveToBottom(self, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    
    ##  Move object at the specified location to the top of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  location of the item </param>
    def MoveToTop(self, index: int) -> None:
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
    ## 
    ## <param name="objects"> (@link UdeBuilder List[NXOpen.SIM.PostConfigurator.UdeBuilder]@endlink)  The list contents </param>
    def SetContents(self, objects: List[UdeBuilder]) -> None:
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
    ## <param name="object_list"> (@link UdeBuilderList NXOpen.SIM.PostConfigurator.UdeBuilderList@endlink) </param>
    ## <param name="index1"> (int)  location of the first item </param>
    ## <param name="index2"> (int)  location of the second item </param>
    @overload
    def Swap(self, index1: int, index2: int) -> None:
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
    ## <param name="object_list"> (@link UdeBuilderList NXOpen.SIM.PostConfigurator.UdeBuilderList@endlink) </param>
    ## <param name="object1"> (@link UdeBuilder NXOpen.SIM.PostConfigurator.UdeBuilder@endlink)  first item </param>
    ## <param name="object2"> (@link UdeBuilder NXOpen.SIM.PostConfigurator.UdeBuilder@endlink)  second item </param>
    @overload
    def Swap(self, object1: UdeBuilder, object2: UdeBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
import NXOpen
##  This class is used to create a new event.
##             Calling @link Builder::Commit Builder::Commit@endlink  on this builder will only return NULL.
##          <br> To create a new instance of this class, use @link NXOpen::SIM::PostConfigurator::PostConfiguratorManager::CreateUdeBuilder  NXOpen::SIM::PostConfigurator::PostConfiguratorManager::CreateUdeBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.1  <br> 

class UdeBuilder(NXOpen.Builder): 
    """ This class is used to create a new event.
            Calling <ja_method>Builder.Commit</ja_method> on this builder will only return <ja_NULL>.
        """


    ##  Type of Cdl Write Type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Event</term><description> 
    ##  Event   </description> </item><item><term> 
    ## Cycle</term><description> 
    ##  Cycle </description> </item><item><term> 
    ## SysCycle</term><description> 
    ##  SysCycle </description> </item></list>
    class CdlWriteType(Enum):
        """
        Members Include: <Event> <Cycle> <SysCycle>
        """
        Event: int
        Cycle: int
        SysCycle: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> UdeBuilder.CdlWriteType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Type of Event Description  
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ##  None   </description> </item><item><term> 
    ## Specify</term><description> 
    ##  Specify </description> </item></list>
    class EventDescriptionType(Enum):
        """
        Members Include: <NotSet> <Specify>
        """
        NotSet: int
        Specify: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> UdeBuilder.EventDescriptionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) EventCategoryDrilling
    ##  Returns the event category drilling   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return bool
    @property
    def EventCategoryDrilling(self) -> bool:
        """
        Getter for property: (bool) EventCategoryDrilling
         Returns the event category drilling   
            
         
        """
        pass
    
    ## Setter for property: (bool) EventCategoryDrilling

    ##  Returns the event category drilling   
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @EventCategoryDrilling.setter
    def EventCategoryDrilling(self, hasCategoryDrilling: bool):
        """
        Setter for property: (bool) EventCategoryDrilling
         Returns the event category drilling   
            
         
        """
        pass
    
    ## Getter for property: (bool) EventCategoryInvalid
    ##  Returns the event category invalid   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def EventCategoryInvalid(self) -> bool:
        """
        Getter for property: (bool) EventCategoryInvalid
         Returns the event category invalid   
            
         
        """
        pass
    
    ## Setter for property: (bool) EventCategoryInvalid

    ##  Returns the event category invalid   
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @EventCategoryInvalid.setter
    def EventCategoryInvalid(self, hasCategoryInvalid: bool):
        """
        Setter for property: (bool) EventCategoryInvalid
         Returns the event category invalid   
            
         
        """
        pass
    
    ## Getter for property: (bool) EventCategoryMilling
    ##  Returns the event category milling   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return bool
    @property
    def EventCategoryMilling(self) -> bool:
        """
        Getter for property: (bool) EventCategoryMilling
         Returns the event category milling   
            
         
        """
        pass
    
    ## Setter for property: (bool) EventCategoryMilling

    ##  Returns the event category milling   
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @EventCategoryMilling.setter
    def EventCategoryMilling(self, hasCategoryMilling: bool):
        """
        Setter for property: (bool) EventCategoryMilling
         Returns the event category milling   
            
         
        """
        pass
    
    ## Getter for property: (bool) EventCategoryTurning
    ##  Returns the event category turning   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return bool
    @property
    def EventCategoryTurning(self) -> bool:
        """
        Getter for property: (bool) EventCategoryTurning
         Returns the event category turning   
            
         
        """
        pass
    
    ## Setter for property: (bool) EventCategoryTurning

    ##  Returns the event category turning   
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @EventCategoryTurning.setter
    def EventCategoryTurning(self, hasCategoryTurning: bool):
        """
        Setter for property: (bool) EventCategoryTurning
         Returns the event category turning   
            
         
        """
        pass
    
    ## Getter for property: (bool) EventCategoryWireEDM
    ##  Returns the event category wire EDM   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return bool
    @property
    def EventCategoryWireEDM(self) -> bool:
        """
        Getter for property: (bool) EventCategoryWireEDM
         Returns the event category wire EDM   
            
         
        """
        pass
    
    ## Setter for property: (bool) EventCategoryWireEDM

    ##  Returns the event category wire EDM   
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @EventCategoryWireEDM.setter
    def EventCategoryWireEDM(self, hasCategoryWireEDM: bool):
        """
        Setter for property: (bool) EventCategoryWireEDM
         Returns the event category wire EDM   
            
         
        """
        pass
    
    ## Getter for property: (@link UdeBuilder.EventDescriptionType NXOpen.SIM.PostConfigurator.UdeBuilder.EventDescriptionType@endlink) EventDescription
    ##  Returns the event description type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return UdeBuilder.EventDescriptionType
    @property
    def EventDescription(self) -> UdeBuilder.EventDescriptionType:
        """
        Getter for property: (@link UdeBuilder.EventDescriptionType NXOpen.SIM.PostConfigurator.UdeBuilder.EventDescriptionType@endlink) EventDescription
         Returns the event description type   
            
         
        """
        pass
    
    ## Setter for property: (@link UdeBuilder.EventDescriptionType NXOpen.SIM.PostConfigurator.UdeBuilder.EventDescriptionType@endlink) EventDescription

    ##  Returns the event description type   
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @EventDescription.setter
    def EventDescription(self, eventDescription: UdeBuilder.EventDescriptionType):
        """
        Setter for property: (@link UdeBuilder.EventDescriptionType NXOpen.SIM.PostConfigurator.UdeBuilder.EventDescriptionType@endlink) EventDescription
         Returns the event description type   
            
         
        """
        pass
    
    ## Getter for property: (str) EventHelpDescription
    ##  Returns the event description   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return str
    @property
    def EventHelpDescription(self) -> str:
        """
        Getter for property: (str) EventHelpDescription
         Returns the event description   
            
         
        """
        pass
    
    ## Setter for property: (str) EventHelpDescription

    ##  Returns the event description   
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @EventHelpDescription.setter
    def EventHelpDescription(self, helpDescription: str):
        """
        Setter for property: (str) EventHelpDescription
         Returns the event description   
            
         
        """
        pass
    
    ## Getter for property: (str) EventHelpLocation
    ##  Returns the event url location   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return str
    @property
    def EventHelpLocation(self) -> str:
        """
        Getter for property: (str) EventHelpLocation
         Returns the event url location   
            
         
        """
        pass
    
    ## Setter for property: (str) EventHelpLocation

    ##  Returns the event url location   
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @EventHelpLocation.setter
    def EventHelpLocation(self, helpLocation: str):
        """
        Setter for property: (str) EventHelpLocation
         Returns the event url location   
            
         
        """
        pass
    
    ## Getter for property: (str) EventID
    ##  Returns the event ID   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return str
    @property
    def EventID(self) -> str:
        """
        Getter for property: (str) EventID
         Returns the event ID   
            
         
        """
        pass
    
    ## Setter for property: (str) EventID

    ##  Returns the event ID   
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @EventID.setter
    def EventID(self, stringEventID: str):
        """
        Setter for property: (str) EventID
         Returns the event ID   
            
         
        """
        pass
    
    ## Getter for property: (str) EventName
    ##  Returns the event name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return str
    @property
    def EventName(self) -> str:
        """
        Getter for property: (str) EventName
         Returns the event name   
            
         
        """
        pass
    
    ## Setter for property: (str) EventName

    ##  Returns the event name   
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @EventName.setter
    def EventName(self, name: str):
        """
        Setter for property: (str) EventName
         Returns the event name   
            
         
        """
        pass
    
    ## Getter for property: (str) PostEvent
    ##  Returns the post event   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return str
    @property
    def PostEvent(self) -> str:
        """
        Getter for property: (str) PostEvent
         Returns the post event   
            
         
        """
        pass
    
    ## Setter for property: (str) PostEvent

    ##  Returns the post event   
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @PostEvent.setter
    def PostEvent(self, postEventID: str):
        """
        Setter for property: (str) PostEvent
         Returns the post event   
            
         
        """
        pass
    
    ## Getter for property: (@link UdeParameterBuilderList NXOpen.SIM.PostConfigurator.UdeParameterBuilderList@endlink) UdeParameterList
    ##  Returns the ude parameter list   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return UdeParameterBuilderList
    @property
    def UdeParameterList(self) -> UdeParameterBuilderList:
        """
        Getter for property: (@link UdeParameterBuilderList NXOpen.SIM.PostConfigurator.UdeParameterBuilderList@endlink) UdeParameterList
         Returns the ude parameter list   
            
         
        """
        pass
    
    ##  Adds item to item used list 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ## <param name="itemBuilder"> (@link UdeParameterBuilder NXOpen.SIM.PostConfigurator.UdeParameterBuilder@endlink) </param>
    def AddItem(self, itemBuilder: UdeParameterBuilder) -> None:
        """
         Adds item to item used list 
        """
        pass
    
    ##  Deletes parameter from ude list 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ## <param name="itemBuilder"> (@link UdeParameterBuilder NXOpen.SIM.PostConfigurator.UdeParameterBuilder@endlink) </param>
    def DeleteItem(self, itemBuilder: UdeParameterBuilder) -> None:
        """
         Deletes parameter from ude list 
        """
        pass
    
    ##  Deletes all parameters from ude list 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    def DeleteItems(self) -> None:
        """
         Deletes all parameters from ude list 
        """
        pass
    
    ##  Returns the ude parameter builder by parameter ID 
    ##  @return itemBuilder (@link UdeParameterBuilder NXOpen.SIM.PostConfigurator.UdeParameterBuilder@endlink):  the ude parameter builder .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterID"> (str) </param>
    def GetUdeParameterBuilder(self, parameterID: str) -> UdeParameterBuilder:
        """
         Returns the ude parameter builder by parameter ID 
         @return itemBuilder (@link UdeParameterBuilder NXOpen.SIM.PostConfigurator.UdeParameterBuilder@endlink):  the ude parameter builder .
        """
        pass
    
    ##  Renames the parameter ID 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ## <param name="itemBuilder"> (@link UdeParameterBuilder NXOpen.SIM.PostConfigurator.UdeParameterBuilder@endlink) </param>
    ## <param name="oldParameterID"> (str) </param>
    ## <param name="newParameterID"> (str) </param>
    def RenameParameterID(self, itemBuilder: UdeParameterBuilder, oldParameterID: str, newParameterID: str) -> None:
        """
         Renames the parameter ID 
        """
        pass
    
import NXOpen
##  This class is represents a @link SIM::PostConfigurator::UdeEditorBuilder SIM::PostConfigurator::UdeEditorBuilder@endlink .
##             Calling @link Builder::Commit Builder::Commit@endlink  on this builder will only return NULL.
##          <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX12.0.1  <br> 

class UdeEditorBuilder(NXOpen.Builder): 
    """ This class is represents a <ja_class>SIM.PostConfigurator.UdeEditorBuilder</ja_class>.
            Calling <ja_method>Builder.Commit</ja_method> on this builder will only return <ja_NULL>.
        """


    ## Getter for property: (@link UdeBuilderList NXOpen.SIM.PostConfigurator.UdeBuilderList@endlink) UdeBuilderList
    ##  Returns the ude list   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return UdeBuilderList
    @property
    def UdeBuilderList(self) -> UdeBuilderList:
        """
        Getter for property: (@link UdeBuilderList NXOpen.SIM.PostConfigurator.UdeBuilderList@endlink) UdeBuilderList
         Returns the ude list   
            
         
        """
        pass
    
    ##  Adds event to event list 
    ##  @return udeBuilder (@link UdeBuilder NXOpen.SIM.PostConfigurator.UdeBuilder@endlink):  the new ude builder .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    def AddNewEvent(self) -> UdeBuilder:
        """
         Adds event to event list 
         @return udeBuilder (@link UdeBuilder NXOpen.SIM.PostConfigurator.UdeBuilder@endlink):  the new ude builder .
        """
        pass
    
    ##  Duplicates selected event to targeted cdl file
    ##  @return newUdeBuilder (@link UdeBuilder NXOpen.SIM.PostConfigurator.UdeBuilder@endlink):  the new ude builder .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ## <param name="udeBuilder"> (@link UdeBuilder NXOpen.SIM.PostConfigurator.UdeBuilder@endlink)  the ude builder to copy </param>
    ## <param name="cdlFile"> (str)  the cdl file name </param>
    def CopyEventToCdlFile(self, udeBuilder: UdeBuilder, cdlFile: str) -> UdeBuilder:
        """
         Duplicates selected event to targeted cdl file
         @return newUdeBuilder (@link UdeBuilder NXOpen.SIM.PostConfigurator.UdeBuilder@endlink):  the new ude builder .
        """
        pass
    
    ##  Duplicates selected event from event list 
    ##  @return newUdeBuilder (@link UdeBuilder NXOpen.SIM.PostConfigurator.UdeBuilder@endlink):  the new ude builder .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ## <param name="udeBuilder"> (@link UdeBuilder NXOpen.SIM.PostConfigurator.UdeBuilder@endlink) </param>
    def DuplicateEvent(self, udeBuilder: UdeBuilder) -> UdeBuilder:
        """
         Duplicates selected event from event list 
         @return newUdeBuilder (@link UdeBuilder NXOpen.SIM.PostConfigurator.UdeBuilder@endlink):  the new ude builder .
        """
        pass
    
    ##  Returns the ude builder by event handler ID 
    ##  @return udeBuilder (@link UdeBuilder NXOpen.SIM.PostConfigurator.UdeBuilder@endlink):  the ude builder .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="eventHandlerID"> (str) </param>
    def GetUdeBuilder(self, eventHandlerID: str) -> UdeBuilder:
        """
         Returns the ude builder by event handler ID 
         @return udeBuilder (@link UdeBuilder NXOpen.SIM.PostConfigurator.UdeBuilder@endlink):  the ude builder .
        """
        pass
    
    ##  Returns the ude builder by event handler ID and cdl File
    ##  @return udeBuilder (@link UdeBuilder NXOpen.SIM.PostConfigurator.UdeBuilder@endlink):  the ude builder .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="eventID"> (str)  the event ID </param>
    ## <param name="cdlFile"> (str)  the cdl file name </param>
    def GetUdeBuilderByCdl(self, eventID: str, cdlFile: str) -> UdeBuilder:
        """
         Returns the ude builder by event handler ID and cdl File
         @return udeBuilder (@link UdeBuilder NXOpen.SIM.PostConfigurator.UdeBuilder@endlink):  the ude builder .
        """
        pass
    
    ##  Lists selected event to listing window 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ## <param name="udeBuilder"> (@link UdeBuilder NXOpen.SIM.PostConfigurator.UdeBuilder@endlink)  the ude builder </param>
    def ListEvent(self, udeBuilder: UdeBuilder) -> None:
        """
         Lists selected event to listing window 
        """
        pass
    
    ##  Removes selected event from event list 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ## <param name="udeBuilder"> (@link UdeBuilder NXOpen.SIM.PostConfigurator.UdeBuilder@endlink)  the ude builder </param>
    def RemoveEvent(self, udeBuilder: UdeBuilder) -> None:
        """
         Removes selected event from event list 
        """
        pass
    
import NXOpen
##  Represents a list of objects. <br> To create a new instance of this class, use @link NXOpen::Part::CreateObjectList  NXOpen::Part::CreateObjectList @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class UdeParameterBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""


    ## Getter for property: (int) Length
    ##  Returns the length of the list   
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
         Returns the length of the list   
            
         
        """
        pass
    
    ##  Appends a set of objects to the list
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link UdeParameterBuilderList NXOpen.SIM.PostConfigurator.UdeParameterBuilderList@endlink) </param>
    ## <param name="objects"> (@link UdeParameterBuilder List[NXOpen.SIM.PostConfigurator.UdeParameterBuilder]@endlink)  items to append </param>
    @overload
    def Append(self, objects: List[UdeParameterBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    
    ##  Appends an object to the list
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link UdeParameterBuilderList NXOpen.SIM.PostConfigurator.UdeParameterBuilderList@endlink) </param>
    ## <param name="objectValue"> (@link UdeParameterBuilder NXOpen.SIM.PostConfigurator.UdeParameterBuilder@endlink)  item to append </param>
    @overload
    def Append(self, objectValue: UdeParameterBuilder) -> None:
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
    ## <param name="object_list"> (@link UdeParameterBuilderList NXOpen.SIM.PostConfigurator.UdeParameterBuilderList@endlink) </param>
    @overload
    def Clear(self) -> None:
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
    ## 
    ## <param name="delete_idx"> (int)  index of item to be deleted </param>
    def ClearIndex(self, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
            *   not change, but the item at this index is set to NULL.
            
        """
        pass
    
    ##  Clears the entire list 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link UdeParameterBuilderList NXOpen.SIM.PostConfigurator.UdeParameterBuilderList@endlink) </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the objects when removing them </param>
    @overload
    def Clear(self, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    
    ##  Erases the object from the list, but does not delete the object.
    ##         The list is shifted so that there isn't a null where the object used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link UdeParameterBuilderList NXOpen.SIM.PostConfigurator.UdeParameterBuilderList@endlink) </param>
    ## <param name="index"> (int)  index of item to be removed from the list </param>
    @overload
    def Erase(self, index: int) -> None:
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
    ## <param name="object_list"> (@link UdeParameterBuilderList NXOpen.SIM.PostConfigurator.UdeParameterBuilderList@endlink) </param>
    ## <param name="index"> (int)  index of item to be removed from the list </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the object </param>
    @overload
    def Erase(self, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    ## <param name="object_list"> (@link UdeParameterBuilderList NXOpen.SIM.PostConfigurator.UdeParameterBuilderList@endlink) </param>
    ## <param name="obj"> (@link UdeParameterBuilder NXOpen.SIM.PostConfigurator.UdeParameterBuilder@endlink)  object to be removed from the list </param>
    @overload
    def Erase(self, obj: UdeParameterBuilder) -> None:
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
    ## <param name="object_list"> (@link UdeParameterBuilderList NXOpen.SIM.PostConfigurator.UdeParameterBuilderList@endlink) </param>
    ## <param name="obj"> (@link UdeParameterBuilder NXOpen.SIM.PostConfigurator.UdeParameterBuilder@endlink)  object to be removed from the list </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the object </param>
    @overload
    def Erase(self, obj: UdeParameterBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    ## 
    ## <param name="obj"> (@link UdeParameterBuilder NXOpen.SIM.PostConfigurator.UdeParameterBuilder@endlink)  Object to find index for </param>
    def FindIndex(self, obj: UdeParameterBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
            *   -1 is returned.
            
         @return index (int):  index of input object, -1 if not on list .
        """
        pass
    
    ##  Returns the object at the input index.  May be NULL.
    ##     
    ##  @return obj (@link UdeParameterBuilder NXOpen.SIM.PostConfigurator.UdeParameterBuilder@endlink):  object found at input index .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  index of object to return </param>
    def FindItem(self, index: int) -> UdeParameterBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         @return obj (@link UdeParameterBuilder NXOpen.SIM.PostConfigurator.UdeParameterBuilder@endlink):  object found at input index .
        """
        pass
    
    ##  Gets the contents of the entire list 
    ##  @return objects (@link UdeParameterBuilder List[NXOpen.SIM.PostConfigurator.UdeParameterBuilder]@endlink):  The list contents .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetContents(self) -> List[UdeParameterBuilder]:
        """
         Gets the contents of the entire list 
         @return objects (@link UdeParameterBuilder List[NXOpen.SIM.PostConfigurator.UdeParameterBuilder]@endlink):  The list contents .
        """
        pass
    
    ##  Inserts an object at the specified location 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="location"> (int)  location at which to insert the object </param>
    ## <param name="objectValue"> (@link UdeParameterBuilder NXOpen.SIM.PostConfigurator.UdeParameterBuilder@endlink)  object to be inserted </param>
    def Insert(self, location: int, objectValue: UdeParameterBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    
    ##  Move object at the specified location to the bottom of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  location of the item </param>
    def MoveToBottom(self, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    
    ##  Move object at the specified location to the top of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  location of the item </param>
    def MoveToTop(self, index: int) -> None:
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
    ## 
    ## <param name="objects"> (@link UdeParameterBuilder List[NXOpen.SIM.PostConfigurator.UdeParameterBuilder]@endlink)  The list contents </param>
    def SetContents(self, objects: List[UdeParameterBuilder]) -> None:
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
    ## <param name="object_list"> (@link UdeParameterBuilderList NXOpen.SIM.PostConfigurator.UdeParameterBuilderList@endlink) </param>
    ## <param name="index1"> (int)  location of the first item </param>
    ## <param name="index2"> (int)  location of the second item </param>
    @overload
    def Swap(self, index1: int, index2: int) -> None:
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
    ## <param name="object_list"> (@link UdeParameterBuilderList NXOpen.SIM.PostConfigurator.UdeParameterBuilderList@endlink) </param>
    ## <param name="object1"> (@link UdeParameterBuilder NXOpen.SIM.PostConfigurator.UdeParameterBuilder@endlink)  first item </param>
    ## <param name="object2"> (@link UdeParameterBuilder NXOpen.SIM.PostConfigurator.UdeParameterBuilder@endlink)  second item </param>
    @overload
    def Swap(self, object1: UdeParameterBuilder, object2: UdeParameterBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
import NXOpen
##  This class is used to create a new event item.
##             Calling @link Builder::Commit Builder::Commit@endlink  on this builder will only return NULL.
##          <br> To create a new instance of this class, use @link NXOpen::SIM::PostConfigurator::PostConfiguratorManager::CreateUdeParameterBuilder  NXOpen::SIM::PostConfigurator::PostConfiguratorManager::CreateUdeParameterBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.1  <br> 

class UdeParameterBuilder(NXOpen.Builder): 
    """ This class is used to create a new event item.
            Calling <ja_method>Builder.Commit</ja_method> on this builder will only return <ja_NULL>.
        """


    ##  Type of Group State  
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Open</term><description> 
    ##  Open   </description> </item><item><term> 
    ## Closed</term><description> 
    ##  Closed </description> </item><item><term> 
    ## End</term><description> 
    ##  End </description> </item></list>
    class GroupStateType(Enum):
        """
        Members Include: <Open> <Closed> <End>
        """
        Open: int
        Closed: int
        End: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> UdeParameterBuilder.GroupStateType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Type of Event Parameter Status 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ##  None - Text Status is Invisible  </description> </item><item><term> 
    ## On</term><description> 
    ##  On   - Text Status is Activate   </description> </item><item><term> 
    ## Off</term><description> 
    ##  Off  - Text Status is Deactivate </description> </item></list>
    class ParameterStatusType(Enum):
        """
        Members Include: <NotSet> <On> <Off>
        """
        NotSet: int
        On: int
        Off: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> UdeParameterBuilder.ParameterStatusType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Type of Event Item  
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Group</term><description> 
    ##  Group       </description> </item><item><term> 
    ## Double</term><description> 
    ##  Double      </description> </item><item><term> 
    ## Integer</term><description> 
    ##  Integer     </description> </item><item><term> 
    ## String</term><description> 
    ##  String      </description> </item><item><term> 
    ## Boolean</term><description> 
    ##  Boolean     </description> </item><item><term> 
    ## Enumeration</term><description> 
    ##  Enumeration </description> </item><item><term> 
    ## Vector</term><description> 
    ##  Vector      </description> </item><item><term> 
    ## Point</term><description> 
    ##  Point       </description> </item><item><term> 
    ## Bitmap</term><description> 
    ##  Bitmap      </description> </item></list>
    class Type(Enum):
        """
        Members Include: <Group> <Double> <Integer> <String> <Boolean> <Enumeration> <Vector> <Point> <Bitmap>
        """
        Group: int
        Double: int
        Integer: int
        String: int
        Boolean: int
        Enumeration: int
        Vector: int
        Point: int
        Bitmap: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> UdeParameterBuilder.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) DoubleDefaultValue
    ##  Returns the double default value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return float
    @property
    def DoubleDefaultValue(self) -> float:
        """
        Getter for property: (float) DoubleDefaultValue
         Returns the double default value   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleDefaultValue

    ##  Returns the double default value   
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @DoubleDefaultValue.setter
    def DoubleDefaultValue(self, doubleDefaultValue: float):
        """
        Setter for property: (float) DoubleDefaultValue
         Returns the double default value   
            
         
        """
        pass
    
    ## Getter for property: (str) EnumerationDefaultValue
    ##  Returns the enumumeration item default value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return str
    @property
    def EnumerationDefaultValue(self) -> str:
        """
        Getter for property: (str) EnumerationDefaultValue
         Returns the enumumeration item default value   
            
         
        """
        pass
    
    ## Setter for property: (str) EnumerationDefaultValue

    ##  Returns the enumumeration item default value   
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @EnumerationDefaultValue.setter
    def EnumerationDefaultValue(self, enumerationDefaultValue: str):
        """
        Setter for property: (str) EnumerationDefaultValue
         Returns the enumumeration item default value   
            
         
        """
        pass
    
    ## Getter for property: (@link UdeParameterBuilder.GroupStateType NXOpen.SIM.PostConfigurator.UdeParameterBuilder.GroupStateType@endlink) GroupState
    ##  Returns the group state   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return UdeParameterBuilder.GroupStateType
    @property
    def GroupState(self) -> UdeParameterBuilder.GroupStateType:
        """
        Getter for property: (@link UdeParameterBuilder.GroupStateType NXOpen.SIM.PostConfigurator.UdeParameterBuilder.GroupStateType@endlink) GroupState
         Returns the group state   
            
         
        """
        pass
    
    ## Setter for property: (@link UdeParameterBuilder.GroupStateType NXOpen.SIM.PostConfigurator.UdeParameterBuilder.GroupStateType@endlink) GroupState

    ##  Returns the group state   
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @GroupState.setter
    def GroupState(self, state: UdeParameterBuilder.GroupStateType):
        """
        Setter for property: (@link UdeParameterBuilder.GroupStateType NXOpen.SIM.PostConfigurator.UdeParameterBuilder.GroupStateType@endlink) GroupState
         Returns the group state   
            
         
        """
        pass
    
    ## Getter for property: (int) IntegerDefaultValue
    ##  Returns the integer default value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return int
    @property
    def IntegerDefaultValue(self) -> int:
        """
        Getter for property: (int) IntegerDefaultValue
         Returns the integer default value   
            
         
        """
        pass
    
    ## Setter for property: (int) IntegerDefaultValue

    ##  Returns the integer default value   
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @IntegerDefaultValue.setter
    def IntegerDefaultValue(self, integerDefaultValue: int):
        """
        Setter for property: (int) IntegerDefaultValue
         Returns the integer default value   
            
         
        """
        pass
    
    ## Getter for property: (@link UdeParameterBuilder.Type NXOpen.SIM.PostConfigurator.UdeParameterBuilder.Type@endlink) ItemType
    ##  Returns the item type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return UdeParameterBuilder.Type
    @property
    def ItemType(self) -> UdeParameterBuilder.Type:
        """
        Getter for property: (@link UdeParameterBuilder.Type NXOpen.SIM.PostConfigurator.UdeParameterBuilder.Type@endlink) ItemType
         Returns the item type   
            
         
        """
        pass
    
    ## Setter for property: (@link UdeParameterBuilder.Type NXOpen.SIM.PostConfigurator.UdeParameterBuilder.Type@endlink) ItemType

    ##  Returns the item type   
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @ItemType.setter
    def ItemType(self, itemType: UdeParameterBuilder.Type):
        """
        Setter for property: (@link UdeParameterBuilder.Type NXOpen.SIM.PostConfigurator.UdeParameterBuilder.Type@endlink) ItemType
         Returns the item type   
            
         
        """
        pass
    
    ## Getter for property: (str) ParameterID
    ##  Returns the parameter ID   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return str
    @property
    def ParameterID(self) -> str:
        """
        Getter for property: (str) ParameterID
         Returns the parameter ID   
            
         
        """
        pass
    
    ## Setter for property: (str) ParameterID

    ##  Returns the parameter ID   
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @ParameterID.setter
    def ParameterID(self, paramID: str):
        """
        Setter for property: (str) ParameterID
         Returns the parameter ID   
            
         
        """
        pass
    
    ## Getter for property: (@link UdeParameterBuilder.ParameterStatusType NXOpen.SIM.PostConfigurator.UdeParameterBuilder.ParameterStatusType@endlink) ParameterStatus
    ##  Returns the item status   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return UdeParameterBuilder.ParameterStatusType
    @property
    def ParameterStatus(self) -> UdeParameterBuilder.ParameterStatusType:
        """
        Getter for property: (@link UdeParameterBuilder.ParameterStatusType NXOpen.SIM.PostConfigurator.UdeParameterBuilder.ParameterStatusType@endlink) ParameterStatus
         Returns the item status   
            
         
        """
        pass
    
    ## Setter for property: (@link UdeParameterBuilder.ParameterStatusType NXOpen.SIM.PostConfigurator.UdeParameterBuilder.ParameterStatusType@endlink) ParameterStatus

    ##  Returns the item status   
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @ParameterStatus.setter
    def ParameterStatus(self, parameterStatus: UdeParameterBuilder.ParameterStatusType):
        """
        Setter for property: (@link UdeParameterBuilder.ParameterStatusType NXOpen.SIM.PostConfigurator.UdeParameterBuilder.ParameterStatusType@endlink) ParameterStatus
         Returns the item status   
            
         
        """
        pass
    
    ## Getter for property: (str) StringDefaultValue
    ##  Returns the string default value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return str
    @property
    def StringDefaultValue(self) -> str:
        """
        Getter for property: (str) StringDefaultValue
         Returns the string default value   
            
         
        """
        pass
    
    ## Setter for property: (str) StringDefaultValue

    ##  Returns the string default value   
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @StringDefaultValue.setter
    def StringDefaultValue(self, stringDefaultValue: str):
        """
        Setter for property: (str) StringDefaultValue
         Returns the string default value   
            
         
        """
        pass
    
    ## Getter for property: (bool) ToggleDefaultValue
    ##  Returns the toggle default value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return bool
    @property
    def ToggleDefaultValue(self) -> bool:
        """
        Getter for property: (bool) ToggleDefaultValue
         Returns the toggle default value   
            
         
        """
        pass
    
    ## Setter for property: (bool) ToggleDefaultValue

    ##  Returns the toggle default value   
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @ToggleDefaultValue.setter
    def ToggleDefaultValue(self, toggleDefaultValue: bool):
        """
        Setter for property: (bool) ToggleDefaultValue
         Returns the toggle default value   
            
         
        """
        pass
    
    ## Getter for property: (str) UILabel
    ##  Returns the User Interface Label   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return str
    @property
    def UILabel(self) -> str:
        """
        Getter for property: (str) UILabel
         Returns the User Interface Label   
            
         
        """
        pass
    
    ## Setter for property: (str) UILabel

    ##  Returns the User Interface Label   
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @UILabel.setter
    def UILabel(self, uiLabel: str):
        """
        Setter for property: (str) UILabel
         Returns the User Interface Label   
            
         
        """
        pass
    
    ##  Gets a list of enumeration items 
    ##  @return enumerationItems (List[str]):  the list of enumeration items .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    def GetEnumerationItems(self) -> List[str]:
        """
         Gets a list of enumeration items 
         @return enumerationItems (List[str]):  the list of enumeration items .
        """
        pass
    
    ##  Sets a list of enumeration items 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ## <param name="enumerationItems"> (List[str])  the list of enumeration items </param>
    def SetEnumerationItems(self, enumerationItems: List[str]) -> None:
        """
         Sets a list of enumeration items 
        """
        pass
    
    ##  Sets the ude parameter builder group 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ## <param name="parentBuilder"> (@link UdeParameterBuilder NXOpen.SIM.PostConfigurator.UdeParameterBuilder@endlink)  the parameter builder group </param>
    def SetGroup(self, parentBuilder: UdeParameterBuilder) -> None:
        """
         Sets the ude parameter builder group 
        """
        pass
    
import NXOpen
##  This class is used to update the postprocessor to the new library.
##             Calling @link Builder::Commit Builder::Commit@endlink  on this builder will only return NULL.
##          <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class UpdatePostprocessorBuilder(NXOpen.Builder): 
    """ This class is used to update the postprocessor to the new library.
            Calling <ja_method>Builder.Commit</ja_method> on this builder will only return <ja_NULL>.
        """


    ##  Represents the update library type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## FromCurrentNXVersion</term><description> 
    ##  Update Postprocessor Library from Current NX Version </description> </item><item><term> 
    ## FromPostRegistry</term><description> 
    ##  Update Postprocessor Library from Post Registry </description> </item><item><term> 
    ## Kinematic</term><description> 
    ##  Update Postprocessor Kinematic </description> </item></list>
    class UpdatePostprocessorType(Enum):
        """
        Members Include: <FromCurrentNXVersion> <FromPostRegistry> <Kinematic>
        """
        FromCurrentNXVersion: int
        FromPostRegistry: int
        Kinematic: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> UpdatePostprocessorBuilder.UpdatePostprocessorType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) CreateBackup
    ##  Returns the create backup options  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def CreateBackup(self) -> bool:
        """
        Getter for property: (bool) CreateBackup
         Returns the create backup options  
            
         
        """
        pass
    
    ## Setter for property: (bool) CreateBackup

    ##  Returns the create backup options  
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @CreateBackup.setter
    def CreateBackup(self, createBackup: bool):
        """
        Setter for property: (bool) CreateBackup
         Returns the create backup options  
            
         
        """
        pass
    
    ## Getter for property: (str) CurrentPostprocessorVersion
    ##  Returns the current postprocessor version   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def CurrentPostprocessorVersion(self) -> str:
        """
        Getter for property: (str) CurrentPostprocessorVersion
         Returns the current postprocessor version   
            
         
        """
        pass
    
    ## Setter for property: (str) CurrentPostprocessorVersion

    ##  Returns the current postprocessor version   
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @CurrentPostprocessorVersion.setter
    def CurrentPostprocessorVersion(self, currentPostprocessor: str):
        """
        Setter for property: (str) CurrentPostprocessorVersion
         Returns the current postprocessor version   
            
         
        """
        pass
    
    ## Getter for property: (str) PostRegistryPath
    ##  Returns the post registry path   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def PostRegistryPath(self) -> str:
        """
        Getter for property: (str) PostRegistryPath
         Returns the post registry path   
            
         
        """
        pass
    
    ## Setter for property: (str) PostRegistryPath

    ##  Returns the post registry path   
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @PostRegistryPath.setter
    def PostRegistryPath(self, filename: str):
        """
        Setter for property: (str) PostRegistryPath
         Returns the post registry path   
            
         
        """
        pass
    
    ## Getter for property: (bool) UpdateCustomLayers
    ##  Returns the update custom layers options  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return bool
    @property
    def UpdateCustomLayers(self) -> bool:
        """
        Getter for property: (bool) UpdateCustomLayers
         Returns the update custom layers options  
            
         
        """
        pass
    
    ## Setter for property: (bool) UpdateCustomLayers

    ##  Returns the update custom layers options  
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @UpdateCustomLayers.setter
    def UpdateCustomLayers(self, updateCustomLayers: bool):
        """
        Setter for property: (bool) UpdateCustomLayers
         Returns the update custom layers options  
            
         
        """
        pass
    
    ## Getter for property: (@link UpdatePostprocessorBuilder.UpdatePostprocessorType NXOpen.SIM.PostConfigurator.UpdatePostprocessorBuilder.UpdatePostprocessorType@endlink) UpdatePostprocessor
    ##  Returns the update postprocessor type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return UpdatePostprocessorBuilder.UpdatePostprocessorType
    @property
    def UpdatePostprocessor(self) -> UpdatePostprocessorBuilder.UpdatePostprocessorType:
        """
        Getter for property: (@link UpdatePostprocessorBuilder.UpdatePostprocessorType NXOpen.SIM.PostConfigurator.UpdatePostprocessorBuilder.UpdatePostprocessorType@endlink) UpdatePostprocessor
         Returns the update postprocessor type   
            
         
        """
        pass
    
    ## Setter for property: (@link UpdatePostprocessorBuilder.UpdatePostprocessorType NXOpen.SIM.PostConfigurator.UpdatePostprocessorBuilder.UpdatePostprocessorType@endlink) UpdatePostprocessor

    ##  Returns the update postprocessor type   
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @UpdatePostprocessor.setter
    def UpdatePostprocessor(self, updatePostprocessorType: UpdatePostprocessorBuilder.UpdatePostprocessorType):
        """
        Setter for property: (@link UpdatePostprocessorBuilder.UpdatePostprocessorType NXOpen.SIM.PostConfigurator.UpdatePostprocessorBuilder.UpdatePostprocessorType@endlink) UpdatePostprocessor
         Returns the update postprocessor type   
            
         
        """
        pass
    
    ## Getter for property: (str) UpdateToVersion
    ##  Returns the update to version   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def UpdateToVersion(self) -> str:
        """
        Getter for property: (str) UpdateToVersion
         Returns the update to version   
            
         
        """
        pass
    
    ## Setter for property: (str) UpdateToVersion

    ##  Returns the update to version   
    ##     
    ##  
    ## Setter License requirements: nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @UpdateToVersion.setter
    def UpdateToVersion(self, updateToVersion: str):
        """
        Setter for property: (str) UpdateToVersion
         Returns the update to version   
            
         
        """
        pass
    
## @package NXOpen.SIM.PostConfigurator
## Classes, Enums and Structs under NXOpen.SIM.PostConfigurator namespace

##  @link DefEditorBuilderAddressForceType NXOpen.SIM.PostConfigurator.DefEditorBuilderAddressForceType @endlink is an alias for @link DefEditorBuilder.AddressForceType NXOpen.SIM.PostConfigurator.DefEditorBuilder.AddressForceType@endlink
DefEditorBuilderAddressForceType = DefEditorBuilder.AddressForceType


##  @link DefEditorBuilderAddressLeaderType NXOpen.SIM.PostConfigurator.DefEditorBuilderAddressLeaderType @endlink is an alias for @link DefEditorBuilder.AddressLeaderType NXOpen.SIM.PostConfigurator.DefEditorBuilder.AddressLeaderType@endlink
DefEditorBuilderAddressLeaderType = DefEditorBuilder.AddressLeaderType


##  @link DefEditorBuilderAddressLimitHandleType NXOpen.SIM.PostConfigurator.DefEditorBuilderAddressLimitHandleType @endlink is an alias for @link DefEditorBuilder.AddressLimitHandleType NXOpen.SIM.PostConfigurator.DefEditorBuilder.AddressLimitHandleType@endlink
DefEditorBuilderAddressLimitHandleType = DefEditorBuilder.AddressLimitHandleType


##  @link DefEditorBuilderAddressTrailerType NXOpen.SIM.PostConfigurator.DefEditorBuilderAddressTrailerType @endlink is an alias for @link DefEditorBuilder.AddressTrailerType NXOpen.SIM.PostConfigurator.DefEditorBuilder.AddressTrailerType@endlink
DefEditorBuilderAddressTrailerType = DefEditorBuilder.AddressTrailerType


##  @link DefEditorBuilderBlockItemType NXOpen.SIM.PostConfigurator.DefEditorBuilderBlockItemType @endlink is an alias for @link DefEditorBuilder.BlockItemType NXOpen.SIM.PostConfigurator.DefEditorBuilder.BlockItemType@endlink
DefEditorBuilderBlockItemType = DefEditorBuilder.BlockItemType


##  @link DefEditorBuilderFormatType NXOpen.SIM.PostConfigurator.DefEditorBuilderFormatType @endlink is an alias for @link DefEditorBuilder.FormatType NXOpen.SIM.PostConfigurator.DefEditorBuilder.FormatType@endlink
DefEditorBuilderFormatType = DefEditorBuilder.FormatType


##  @link PostConfiguratorBuilderDefWriterErrorType NXOpen.SIM.PostConfigurator.PostConfiguratorBuilderDefWriterErrorType @endlink is an alias for @link PostConfiguratorBuilder.DefWriterErrorType NXOpen.SIM.PostConfigurator.PostConfiguratorBuilder.DefWriterErrorType@endlink
PostConfiguratorBuilderDefWriterErrorType = PostConfiguratorBuilder.DefWriterErrorType


##  @link PostConfiguratorBuilderPropertyAccessType NXOpen.SIM.PostConfigurator.PostConfiguratorBuilderPropertyAccessType @endlink is an alias for @link PostConfiguratorBuilder.PropertyAccessType NXOpen.SIM.PostConfigurator.PostConfiguratorBuilder.PropertyAccessType@endlink
PostConfiguratorBuilderPropertyAccessType = PostConfiguratorBuilder.PropertyAccessType


##  @link PostConfiguratorBuilderPropertyDataFieldType NXOpen.SIM.PostConfigurator.PostConfiguratorBuilderPropertyDataFieldType @endlink is an alias for @link PostConfiguratorBuilder.PropertyDataFieldType NXOpen.SIM.PostConfigurator.PostConfiguratorBuilder.PropertyDataFieldType@endlink
PostConfiguratorBuilderPropertyDataFieldType = PostConfiguratorBuilder.PropertyDataFieldType


##  @link PostConfiguratorBuilderPropertyDataType NXOpen.SIM.PostConfigurator.PostConfiguratorBuilderPropertyDataType @endlink is an alias for @link PostConfiguratorBuilder.PropertyDataType NXOpen.SIM.PostConfigurator.PostConfiguratorBuilder.PropertyDataType@endlink
PostConfiguratorBuilderPropertyDataType = PostConfiguratorBuilder.PropertyDataType


##  @link PostConfiguratorBuilderPropertyOptionType NXOpen.SIM.PostConfigurator.PostConfiguratorBuilderPropertyOptionType @endlink is an alias for @link PostConfiguratorBuilder.PropertyOptionType NXOpen.SIM.PostConfigurator.PostConfiguratorBuilder.PropertyOptionType@endlink
PostConfiguratorBuilderPropertyOptionType = PostConfiguratorBuilder.PropertyOptionType


##  @link PostConfiguratorBuilderPropertyValueChangedStatusType NXOpen.SIM.PostConfigurator.PostConfiguratorBuilderPropertyValueChangedStatusType @endlink is an alias for @link PostConfiguratorBuilder.PropertyValueChangedStatusType NXOpen.SIM.PostConfigurator.PostConfiguratorBuilder.PropertyValueChangedStatusType@endlink
PostConfiguratorBuilderPropertyValueChangedStatusType = PostConfiguratorBuilder.PropertyValueChangedStatusType


##  @link PostConfiguratorBuilderUnitsType NXOpen.SIM.PostConfigurator.PostConfiguratorBuilderUnitsType @endlink is an alias for @link PostConfiguratorBuilder.UnitsType NXOpen.SIM.PostConfigurator.PostConfiguratorBuilder.UnitsType@endlink
PostConfiguratorBuilderUnitsType = PostConfiguratorBuilder.UnitsType


##  @link PostConfiguratorDebugBuilderDumpType NXOpen.SIM.PostConfigurator.PostConfiguratorDebugBuilderDumpType @endlink is an alias for @link PostConfiguratorDebugBuilder.DumpType NXOpen.SIM.PostConfigurator.PostConfiguratorDebugBuilder.DumpType@endlink
PostConfiguratorDebugBuilderDumpType = PostConfiguratorDebugBuilder.DumpType


##  @link PostConfiguratorDebugBuilderOutputType NXOpen.SIM.PostConfigurator.PostConfiguratorDebugBuilderOutputType @endlink is an alias for @link PostConfiguratorDebugBuilder.OutputType NXOpen.SIM.PostConfigurator.PostConfiguratorDebugBuilder.OutputType@endlink
PostConfiguratorDebugBuilderOutputType = PostConfiguratorDebugBuilder.OutputType


##  @link PostConfiguratorDebugBuilderTraceType NXOpen.SIM.PostConfigurator.PostConfiguratorDebugBuilderTraceType @endlink is an alias for @link PostConfiguratorDebugBuilder.TraceType NXOpen.SIM.PostConfigurator.PostConfiguratorDebugBuilder.TraceType@endlink
PostConfiguratorDebugBuilderTraceType = PostConfiguratorDebugBuilder.TraceType


##  @link UdeBuilderCdlWriteType NXOpen.SIM.PostConfigurator.UdeBuilderCdlWriteType @endlink is an alias for @link UdeBuilder.CdlWriteType NXOpen.SIM.PostConfigurator.UdeBuilder.CdlWriteType@endlink
UdeBuilderCdlWriteType = UdeBuilder.CdlWriteType


##  @link UdeBuilderEventDescriptionType NXOpen.SIM.PostConfigurator.UdeBuilderEventDescriptionType @endlink is an alias for @link UdeBuilder.EventDescriptionType NXOpen.SIM.PostConfigurator.UdeBuilder.EventDescriptionType@endlink
UdeBuilderEventDescriptionType = UdeBuilder.EventDescriptionType


##  @link UdeParameterBuilderGroupStateType NXOpen.SIM.PostConfigurator.UdeParameterBuilderGroupStateType @endlink is an alias for @link UdeParameterBuilder.GroupStateType NXOpen.SIM.PostConfigurator.UdeParameterBuilder.GroupStateType@endlink
UdeParameterBuilderGroupStateType = UdeParameterBuilder.GroupStateType


##  @link UdeParameterBuilderParameterStatusType NXOpen.SIM.PostConfigurator.UdeParameterBuilderParameterStatusType @endlink is an alias for @link UdeParameterBuilder.ParameterStatusType NXOpen.SIM.PostConfigurator.UdeParameterBuilder.ParameterStatusType@endlink
UdeParameterBuilderParameterStatusType = UdeParameterBuilder.ParameterStatusType


##  @link UdeParameterBuilderType NXOpen.SIM.PostConfigurator.UdeParameterBuilderType @endlink is an alias for @link UdeParameterBuilder.Type NXOpen.SIM.PostConfigurator.UdeParameterBuilder.Type@endlink
UdeParameterBuilderType = UdeParameterBuilder.Type


##  @link UpdatePostprocessorBuilderUpdatePostprocessorType NXOpen.SIM.PostConfigurator.UpdatePostprocessorBuilderUpdatePostprocessorType @endlink is an alias for @link UpdatePostprocessorBuilder.UpdatePostprocessorType NXOpen.SIM.PostConfigurator.UpdatePostprocessorBuilder.UpdatePostprocessorType@endlink
UpdatePostprocessorBuilderUpdatePostprocessorType = UpdatePostprocessorBuilder.UpdatePostprocessorType


