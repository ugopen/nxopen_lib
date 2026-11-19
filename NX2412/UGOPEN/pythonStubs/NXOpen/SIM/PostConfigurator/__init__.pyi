from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class AddLayerBuilder(NXOpen.Builder): 
    """ This class is used to create a new layer.
            Calling Builder.Commit on this builder will only return .
        """
    @property
    def CreateDefinitionFile(self) -> bool:
        """
        Getter for property: (bool) CreateDefinitionFile
         Returns the flag of create def file   
            
         
        """
        pass
    @CreateDefinitionFile.setter
    def CreateDefinitionFile(self, hasCreateDefFile: bool):
        """
        Setter for property: (bool) CreateDefinitionFile
         Returns the flag of create def file   
            
         
        """
        pass
    @property
    def CreateDirectoryForLayer(self) -> bool:
        """
        Getter for property: (bool) CreateDirectoryForLayer
         Returns the flag of create tcl file   
            
         
        """
        pass
    @CreateDirectoryForLayer.setter
    def CreateDirectoryForLayer(self, hasCreateFolder: bool):
        """
        Setter for property: (bool) CreateDirectoryForLayer
         Returns the flag of create tcl file   
            
         
        """
        pass
    @property
    def CreateTclFile(self) -> bool:
        """
        Getter for property: (bool) CreateTclFile
         Returns the flag of create tcl file   
            
         
        """
        pass
    @CreateTclFile.setter
    def CreateTclFile(self, hasCreateTclFile: bool):
        """
        Setter for property: (bool) CreateTclFile
         Returns the flag of create tcl file   
            
         
        """
        pass
    @property
    def CreateUserDefinedEventFile(self) -> bool:
        """
        Getter for property: (bool) CreateUserDefinedEventFile
         Returns the flag of create cdl file   
            
         
        """
        pass
    @CreateUserDefinedEventFile.setter
    def CreateUserDefinedEventFile(self, hasCreateCdlFile: bool):
        """
        Setter for property: (bool) CreateUserDefinedEventFile
         Returns the flag of create cdl file   
            
         
        """
        pass
    @property
    def LayerFileName(self) -> str:
        """
        Getter for property: (str) LayerFileName
         Returns the layer file name   
            
         
        """
        pass
    @LayerFileName.setter
    def LayerFileName(self, fileName: str):
        """
        Setter for property: (str) LayerFileName
         Returns the layer file name   
            
         
        """
        pass
    @property
    def LayerName(self) -> str:
        """
        Getter for property: (str) LayerName
         Returns the layer name   
            
         
        """
        pass
    @LayerName.setter
    def LayerName(self, name: str):
        """
        Setter for property: (str) LayerName
         Returns the layer name   
            
         
        """
        pass
import NXOpen
class CreationPostBuilder(NXOpen.Builder): 
    """ This class is used to create a new postprocessor.
            Calling Builder.Commit on this builder will only return .
        """
    @property
    def ControllerName(self) -> str:
        """
        Getter for property: (str) ControllerName
         Returns the controller's name that is used for the postprocessor.  
            
         
        """
        pass
    @ControllerName.setter
    def ControllerName(self, name: str):
        """
        Setter for property: (str) ControllerName
         Returns the controller's name that is used for the postprocessor.  
            
         
        """
        pass
    @property
    def CreateDirectoryForPostprocessor(self) -> bool:
        """
        Getter for property: (bool) CreateDirectoryForPostprocessor
         Returns the Flag whether postprocessor's output directory is created with the postprocessor name or not.  
             
         
        """
        pass
    @CreateDirectoryForPostprocessor.setter
    def CreateDirectoryForPostprocessor(self, toggleState: bool):
        """
        Setter for property: (bool) CreateDirectoryForPostprocessor
         Returns the Flag whether postprocessor's output directory is created with the postprocessor name or not.  
             
         
        """
        pass
    @property
    def MachineName(self) -> str:
        """
        Getter for property: (str) MachineName
         Returns the machine's name that is used for the postprocessor.  
            
         
        """
        pass
    @MachineName.setter
    def MachineName(self, name: str):
        """
        Setter for property: (str) MachineName
         Returns the machine's name that is used for the postprocessor.  
            
         
        """
        pass
    @property
    def ManufacturerName(self) -> str:
        """
        Getter for property: (str) ManufacturerName
         Returns the manufacturer's name that is used for the postprocessor.  
            
         
        """
        pass
    @ManufacturerName.setter
    def ManufacturerName(self, name: str):
        """
        Setter for property: (str) ManufacturerName
         Returns the manufacturer's name that is used for the postprocessor.  
            
         
        """
        pass
    @property
    def PostprocessorName(self) -> str:
        """
        Getter for property: (str) PostprocessorName
         Returns the postprocessor's name.  
             
         
        """
        pass
    @PostprocessorName.setter
    def PostprocessorName(self, name: str):
        """
        Setter for property: (str) PostprocessorName
         Returns the postprocessor's name.  
             
         
        """
        pass
    @property
    def PostprocessorOutputDirectory(self) -> str:
        """
        Getter for property: (str) PostprocessorOutputDirectory
         Returns the postprocessor's output directory where the postprocessor is created.  
             
         
        """
        pass
    @PostprocessorOutputDirectory.setter
    def PostprocessorOutputDirectory(self, outputDirectory: str):
        """
        Setter for property: (str) PostprocessorOutputDirectory
         Returns the postprocessor's output directory where the postprocessor is created.  
             
         
        """
        pass
    def GetControllerNames(self) -> List[str]:
        """
         Returns the list of controller names in the postprocessor.
         Returns controllerNames (List[str]):  the list of available controller .
        """
        pass
    def GetLayerNameValue(self, layerName: str) -> str:
        """
         Returns the layer value.
         Returns value (str):  The layer value .
        """
        pass
    def GetLayerNames(self, layerName: str) -> List[str]:
        """
         Returns the list of layer value in the postprocessor.
         Returns layerValues (List[str]):  the list of available layer value .
        """
        pass
    def GetMachineNames(self) -> List[str]:
        """
         Returns the list of machine names in the postprocessor.
         Returns machineNames (List[str]):  the list of available machine .
        """
        pass
    def GetManufacturerNames(self) -> List[str]:
        """
         Returns the list of manufacturer names in the postprocessor.
         Returns manufacturerNames (List[str]):  the list of available manufacturer .
        """
        pass
    def SetLayerNameValue(self, layerName: str, value: str) -> None:
        """
         Sets the layer value.
        """
        pass
import NXOpen
class DefEditorBuilder(NXOpen.Builder): 
    """ This class is used to create a post definition editor builder.
            Calling Builder.Commit on this builder will only return .
        """
    class AddressForceType(Enum):
        """
        Members Include: 
         |On| 
         |Once| 
         |Always| 

        """
        On: int
        Once: int
        Always: int
        @staticmethod
        def ValueOf(value: int) -> DefEditorBuilder.AddressForceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class AddressLeaderType(Enum):
        """
        Members Include: 
         |Literal| 
         |Expression| 

        """
        Literal: int
        Expression: int
        @staticmethod
        def ValueOf(value: int) -> DefEditorBuilder.AddressLeaderType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class AddressLimitHandleType(Enum):
        """
        Members Include: 
         |TruncateValue| 
         |WarnUser| 
         |AbortProcess| 
         |Reset| 

        """
        TruncateValue: int
        WarnUser: int
        AbortProcess: int
        Reset: int
        @staticmethod
        def ValueOf(value: int) -> DefEditorBuilder.AddressLimitHandleType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class AddressTrailerType(Enum):
        """
        Members Include: 
         |Literal| 
         |Expression| 

        """
        Literal: int
        Expression: int
        @staticmethod
        def ValueOf(value: int) -> DefEditorBuilder.AddressTrailerType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class BlockItemType(Enum):
        """
        Members Include: 
         |Literal| 
         |Address| 
         |TurboAddress| 

        """
        Literal: int
        Address: int
        TurboAddress: int
        @staticmethod
        def ValueOf(value: int) -> DefEditorBuilder.BlockItemType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FormatType(Enum):
        """
        Members Include: 
         |Numeric| 
         |Text| 

        """
        Numeric: int
        Text: int
        @staticmethod
        def ValueOf(value: int) -> DefEditorBuilder.FormatType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CurrentLayer(self) -> str:
        """
        Getter for property: (str) CurrentLayer
         Returns the current layer.  
           The current layer is editing by DefEditor   
         
        """
        pass
    @CurrentLayer.setter
    def CurrentLayer(self, layerName: str):
        """
        Setter for property: (str) CurrentLayer
         Returns the current layer.  
           The current layer is editing by DefEditor   
         
        """
        pass
    def AddAddress(self, addressName: str, formatName: str, zeroLimitName: str, forceType: DefEditorBuilder.AddressForceType, leader: str, leaderType: DefEditorBuilder.AddressLeaderType, trailer: str, trailerType: DefEditorBuilder.AddressTrailerType, maxIsDefine: bool, maxLimit: float, maxHandeType: DefEditorBuilder.AddressLimitHandleType, minIsDefine: bool, minLimit: float, minHandeType: DefEditorBuilder.AddressLimitHandleType) -> None:
        """
         Add new address to custom def file, replace existing one 
        """
        pass
    def AddAddressWithOmit(self, addressName: str, formatName: str, zeroLimitName: str, forceType: DefEditorBuilder.AddressForceType, leader: str, leaderType: DefEditorBuilder.AddressLeaderType, trailer: str, trailerType: DefEditorBuilder.AddressTrailerType, maxIsDefine: bool, maxLimit: float, maxHandeType: DefEditorBuilder.AddressLimitHandleType, minIsDefine: bool, minLimit: float, minHandeType: DefEditorBuilder.AddressLimitHandleType, omit: str) -> None:
        """
         Add omit to address 
        """
        pass
    def AddBlockAddress(self, blockTemplateName: str, blockAddressName: str, blockItemType: int, expression: str, addressIndex: int, isOptional: bool, hasNoWordSeparator: bool) -> None:
        """
         Add block address to custom def file
        """
        pass
    def AddBlockTemplate(self, blockTemplateName: str, blockAddressName: List[str], blockItemType: List[DefEditorBuilder.BlockItemType], expression: List[str], addressIndex: List[int], isOptional: List[bool], hasNoWordSeparator: List[bool]) -> None:
        """
         Add new block template to custom def file, replace existing one 
        """
        pass
    def AddFormat(self, formatName: str, isOutputLeaderPlusSign: bool, isOutputLeadingZeros: bool, isOutputDecimalPoint: bool, isOutputTrailingZeros: bool, visibleDigits: int, visibleDecimals: int, formatType: DefEditorBuilder.FormatType) -> None:
        """
         Add format to custom def file, replace existing one 
        """
        pass
    def DeleteAddress(self, addressName: str) -> None:
        """
         Delete address of custom def file 
        """
        pass
    def DeleteBlockAddress(self, blockTemplateName: str, addressName: str) -> None:
        """
         Delete block address of custom def file 
        """
        pass
    def DeleteBlockTemplate(self, blockTemplateName: str) -> None:
        """
         Delete block template of custom def file 
        """
        pass
    def DeleteFormat(self, formatName: str) -> None:
        """
         Delete format of custom def file 
        """
        pass
    def GetAddressOmit(self, addressName: str) -> str:
        """
         Get omit of address  
         Returns omit (str):  the address omit.
        """
        pass
import NXOpen
class EncryptPostprocessorFilesBuilder(NXOpen.Builder): 
    """ This class is used to encrypt the post builder or tcl based postprocessor.
            Calling Builder.Commit on this builder will only return .
        """
    @property
    def ExpirationDate(self) -> str:
        """
        Getter for property: (str) ExpirationDate
         Returns the expiration date.  
             
         
        """
        pass
    @ExpirationDate.setter
    def ExpirationDate(self, expirationDate: str):
        """
        Setter for property: (str) ExpirationDate
         Returns the expiration date.  
             
         
        """
        pass
    @property
    def SMKSLicensecheck(self) -> str:
        """
        Getter for property: (str) SMKSLicensecheck
         Returns the SMKS license check.  
             
         
        """
        pass
    @SMKSLicensecheck.setter
    def SMKSLicensecheck(self, smksLicensecheck: str):
        """
        Setter for property: (str) SMKSLicensecheck
         Returns the SMKS license check.  
             
         
        """
        pass
    def GetEncryptPostprocessorFiles(self) -> List[str]:
        """
         Gets the encrypt postprocessor files. 
                        This function allocates the memory for encryptFiles. The caller is responsible to deallocate the memory. 
         Returns encryptFiles (List[str]):  the encrypt files .
        """
        pass
    def GetSoldToIds(self) -> str:
        """
         Gets the sold to ids. 
         Returns soldToIDs (str):  the sold to ids .
        """
        pass
    def SetEncryptPostprocessorFiles(self, encryptFilename: List[str]) -> None:
        """
         Sets the encrypt postprocessor files. 
        """
        pass
    def SetSoldToIds(self, soldToIDs: str) -> None:
        """
         Sets the sold to ids. 
        """
        pass
import NXOpen
class LayerManagerBuilder(NXOpen.Builder): 
    """ This class is represents a SIM.PostConfigurator.LayerManagerBuilder.
            Calling Builder.Commit on this builder will only return .
        """
    @property
    def AddLayerBuilder(self) -> AddLayerBuilder:
        """
        Getter for property: ( AddLayerBuilder NXOpen.SIM.Po) AddLayerBuilder
         Returns the add layer builder   
            
         
        """
        pass
    def ExportLayer(self, layerName: str, destFolder: str) -> None:
        """
         Exports a specific layer 
        """
        pass
    def ImportLayer(self, layerFile: str) -> None:
        """
         Imports a specific layer 
        """
        pass
    def RemoveLayer(self, layerName: str) -> None:
        """
         Removes a specific layer 
        """
        pass
import NXOpen
import NXOpen.CAM
class PostConfiguratorBuilder(NXOpen.Builder): 
    """ This class is used to create a post configurator builder.
            Calling Builder.Commit on this builder will only return .
        """
    class DefWriterErrorType(Enum):
        """
        Members Include: 
         |NoError| 
         |DirWriteprotectError| 
         |NoCustomerError| 
         |CustomFileExistError| 
         |FileWriteprotectError| 
         |UnknownError| 

        """
        NoError: int
        DirWriteprotectError: int
        NoCustomerError: int
        CustomFileExistError: int
        FileWriteprotectError: int
        UnknownError: int
        @staticmethod
        def ValueOf(value: int) -> PostConfiguratorBuilder.DefWriterErrorType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PropertyAccessType(Enum):
        """
        Members Include: 
         |No|  The property has no read or write access. 
         |Read|  The property has read only access. 
         |Full|  The property has read and write access. 

        """
        No: int
        Read: int
        Full: int
        @staticmethod
        def ValueOf(value: int) -> PostConfiguratorBuilder.PropertyAccessType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PropertyDataFieldType(Enum):
        """
        Members Include: 
         |Unknown|  Unknown datafield type 
         |Single|  Single datafield type 
         |Option|  Option datafield type 

        """
        Unknown: int
        Single: int
        Option: int
        @staticmethod
        def ValueOf(value: int) -> PostConfiguratorBuilder.PropertyDataFieldType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PropertyDataType(Enum):
        """
        Members Include: 
         |Unknown|  Unknown data type 
         |Integer|  Integer data type 
         |Double|  Double data type 
         |String|  String data type 
         |Option|  Option data type 
         |Vector|  Vector data type 
         |Multistring|  Multistring data type 
         |Point|  Point data type 

        """
        Unknown: int
        Integer: int
        Double: int
        String: int
        Option: int
        Vector: int
        Multistring: int
        Point: int
        @staticmethod
        def ValueOf(value: int) -> PostConfiguratorBuilder.PropertyDataType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PropertyOptionType(Enum):
        """
        Members Include: 
         |Unknown|  Unknown option type 
         |Value|  Value option type 
         |Enum|  Enum option type 

        """
        Unknown: int
        Value: int
        Enum: int
        @staticmethod
        def ValueOf(value: int) -> PostConfiguratorBuilder.PropertyOptionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PropertyValueChangedStatusType(Enum):
        """
        Members Include: 
         |Unchanged|  If the value is equal to default value. 
         |Changed|  If the value is different to default value. 
         |UnremoveUnchanged|  If the value is equal to default value and the property cannot be removed. 
         |UnremoveChanged|  If the value is different to default value and the property cannot be removed. 
         |UnaddUnchanged|  If the value is equal to default value and the property cannot be added. 
         |UnaddChanged|  If the value is different to default value and the property cannot be added. 

        """
        Unchanged: int
        Changed: int
        UnremoveUnchanged: int
        UnremoveChanged: int
        UnaddUnchanged: int
        UnaddChanged: int
        @staticmethod
        def ValueOf(value: int) -> PostConfiguratorBuilder.PropertyValueChangedStatusType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class UnitsType(Enum):
        """
        Members Include: 
         |Millimeters|  The Units is in Millimeters. 
         |Inches|  The Units is in Inches. 
         |MillimetersAndInches|  The Units is in Millimeters and Inches. 

        """
        Millimeters: int
        Inches: int
        MillimetersAndInches: int
        @staticmethod
        def ValueOf(value: int) -> PostConfiguratorBuilder.UnitsType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DateValue(self) -> NXOpen.DateBuilder:
        """
        Getter for property: ( NXOpen.DateBuilder) DateValue
         Returns the date value.  
           The Date object will contain the value for expiration date.   
         
        """
        pass
    @property
    def DefEditorBuilder(self) -> DefEditorBuilder:
        """
        Getter for property: ( DefEditorBuilder NXOpen.SIM.Po) DefEditorBuilder
         Returns the def editor builder.  
             
         
        """
        pass
    @property
    def LayerManagerBuilder(self) -> LayerManagerBuilder:
        """
        Getter for property: ( LayerManagerBuilder NXOpen.SIM.Po) LayerManagerBuilder
         Returns the layer editor builder   
            
         
        """
        pass
    @property
    def UdeEditorBuilder(self) -> UdeEditorBuilder:
        """
        Getter for property: ( UdeEditorBuilder NXOpen.SIM.Po) UdeEditorBuilder
         Returns the ude editor builder   
            
         
        """
        pass
    @property
    def Units(self) -> PostConfiguratorBuilder.UnitsType:
        """
        Getter for property: ( PostConfiguratorBuilder.UnitsType NXOpen.SIM.Po) Units
         Returns the displayed units in post configurator properties  
            
         
        """
        pass
    @Units.setter
    def Units(self, type: PostConfiguratorBuilder.UnitsType):
        """
        Setter for property: ( PostConfiguratorBuilder.UnitsType NXOpen.SIM.Po) Units
         Returns the displayed units in post configurator properties  
            
         
        """
        pass
    @property
    def UpdatePostprocessorBuilder(self) -> UpdatePostprocessorBuilder:
        """
        Getter for property: ( UpdatePostprocessorBuilder NXOpen.SIM.Po) UpdatePostprocessorBuilder
         Returns the update postprocessor builder   
            
         
        """
        pass
    def AddProperty(self, chainID: str, configurationObjectID: str, propertyID: str) -> None:
        """
         Adds the property to the selected chain
                        The configurationObjectID and propertyID are documented under NX Help-Manufacturing(CAM)-Post Configurator-Post Configurator configuration objets. 
        """
        pass
    def CopyPropertyDataToClipboard(self, configurationObjectID: str, propertyID: str) -> None:
        """
         Copy the property data to the clipboard. 
                        The configurationObjectID and propertyID are documented under NX Help-Manufacturing(CAM)-Post Configurator-Post Configurator configuration objets.
        """
        pass
    def CreateCustomCdlFile(self) -> None:
        """
         Creates the Customer Cdl File. 
        """
        pass
    def CreateCustomDefFile(self) -> PostConfiguratorBuilder.DefWriterErrorType:
        """
         Create custom def file. 
         Returns errorCode ( PostConfiguratorBuilder.DefWriterErrorType NXOpen.SIM.Po): .
        """
        pass
    def EncryptPostConfiguratorFiles(self, soldToID: str, expirationDate: str) -> None:
        """
         Encrypts a post processor with Sold-To ID and expiration date. 
        """
        pass
    def GetPropertyAccessType(self, chainID: str, configurationObjectID: str, propertyID: str) -> PostConfiguratorBuilder.PropertyAccessType:
        """
         Gets the property access type. 
                        The configurationObjectID and propertyID are documented under NX Help-Manufacturing(CAM)-Post Configurator-Post Configurator configuration objets. 
         Returns accessType ( PostConfiguratorBuilder.PropertyAccessType NXOpen.SIM.Po):  the access type .
        """
        pass
    def GetPropertyChainIds(self) -> List[str]:
        """
         Gets the property chain ids. 
                        This function allocates the memory for chainIds. The caller is responsible to deallocate the memory. 
         Returns chainIds (List[str]):  the chain ids .
        """
        pass
    def GetPropertyConfigurationObjectIds(self) -> List[str]:
        """
         Gets the property configuration object ids. 
                        This function allocates the memory for chainIds. The caller is responsible to deallocate the memory. 
         Returns configurationObjectIds (List[str]):  the configuraton object ids .
        """
        pass
    def GetPropertyDataFieldType(self, chainID: str, configurationObjectID: str, propertyID: str) -> PostConfiguratorBuilder.PropertyDataFieldType:
        """
         Gets the property data field type. 
                        The configurationObjectID and propertyID are documented under NX Help-Manufacturing(CAM)-Post Configurator-Post Configurator configuration objets. 
         Returns dataFieldType ( PostConfiguratorBuilder.PropertyDataFieldType NXOpen.SIM.Po):  the data field type .
        """
        pass
    def GetPropertyDataType(self, chainID: str, configurationObjectID: str, propertyID: str) -> PostConfiguratorBuilder.PropertyDataType:
        """
         Gets the property data type. 
                        The configurationObjectID and propertyID are documented under NX Help-Manufacturing(CAM)-Post Configurator-Post Configurator configuration objets. 
         Returns dataType ( PostConfiguratorBuilder.PropertyDataType NXOpen.SIM.Po):  the data type .
        """
        pass
    def GetPropertyDefaultValue(self, chainID: str, configurationObjectID: str, propertyID: str) -> List[str]:
        """
         Gets the property default value.
                        The configurationObjectID and propertyID are documented under NX Help-Manufacturing(CAM)-Post Configurator-Post Configurator configuration objets.
                        This function allocates the memory for defaultValues. The caller is responsible to deallocate the memory. 
         Returns defaultValues (List[str]):  the default values .
        """
        pass
    def GetPropertyDescriptionImage(self, chainID: str, configurationObjectID: str, propertyID: str) -> str:
        """
         Gets the property description image.
                        The configurationObjectID and propertyID are documented under NX Help-Manufacturing(CAM)-Post Configurator-Post Configurator configuration objets. 
         Returns descriptionImage (str):  the description image .
        """
        pass
    def GetPropertyDescriptionText(self, chainID: str, configurationObjectID: str, propertyID: str) -> str:
        """
         Gets the property description text.
                        The configurationObjectID and propertyID are documented under NX Help-Manufacturing(CAM)-Post Configurator-Post Configurator configuration objets. 
         Returns descriptionText (str):  the description text .
        """
        pass
    def GetPropertyIds(self) -> List[str]:
        """
         Gets the property ids. 
                        This function allocates the memory for chainIds. The caller is responsible to deallocate the memory. 
         Returns propertyIds (List[str]):  the property ids .
        """
        pass
    def GetPropertyOptionType(self, chainID: str, configurationObjectID: str, propertyID: str) -> PostConfiguratorBuilder.PropertyOptionType:
        """
         Gets the property option type. 
                        The configurationObjectID and propertyID are documented under NX Help-Manufacturing(CAM)-Post Configurator-Post Configurator configuration objets. 
         Returns optionType ( PostConfiguratorBuilder.PropertyOptionType NXOpen.SIM.Po):  the option type .
        """
        pass
    def GetPropertyOptionsIdValue(self, chainID: str, configurationObjectID: str, propertyID: str) -> str:
        """
         Gets the property options ID value. 
                        The configurationObjectID and propertyID are documented under NX Help-Manufacturing(CAM)-Post Configurator-Post Configurator configuration objets. 
         Returns optionsIDValue (str):  the options id value .
        """
        pass
    def GetPropertyOptionsValue(self, chainID: str, configurationObjectID: str, propertyID: str) -> str:
        """
         Gets the property options value. 
                        The configurationObjectID and propertyID are documented under NX Help-Manufacturing(CAM)-Post Configurator-Post Configurator configuration objets. 
         Returns optionsValue (str):  the options value .
        """
        pass
    def GetPropertyValue(self, chainID: str, configurationObjectID: str, propertyID: str) -> List[str]:
        """
         Gets the property value.
                        The configurationObjectID and propertyID are documented under NX Help-Manufacturing(CAM)-Post Configurator-Post Configurator configuration objets.
                        This function allocates the memory for values. The caller is responsible to deallocate the memory. 
         Returns values (List[str]):  the values .
        """
        pass
    def GetPropertyValueChangedStatus(self, chainID: str, configurationObjectID: str, propertyID: str) -> PostConfiguratorBuilder.PropertyValueChangedStatusType:
        """
         Gets the property value changed status. 
                        The configurationObjectID and propertyID are documented under NX Help-Manufacturing(CAM)-Post Configurator-Post Configurator configuration objets. 
         Returns valueChangedStatus ( PostConfiguratorBuilder.PropertyValueChangedStatusType NXOpen.SIM.Po):  the value changed status .
        """
        pass
    def ListPropertyDataInInformationWindow(self, configurationObjectID: str, propertyID: str) -> None:
        """
         Lists the property data in the information window. 
                        The configurationObjectID and propertyID are documented under NX Help-Manufacturing(CAM)-Post Configurator-Post Configurator configuration objets.
        """
        pass
    def OpenDocumentation(self) -> None:
        """
         Execute the tcl script to open the external documentation. 
        """
        pass
    def PostProcess(self, objects: List[NXOpen.CAM.CAMObject], outputFilename: str, showOutputToListingWindow: bool) -> None:
        """
         Postprocess the selected operation. 
        """
        pass
    def RemoveProperty(self, chainID: str, configurationObjectID: str, propertyID: str) -> None:
        """
         Removes the property from the selected chain
                        The configurationObjectID and propertyID are documented under NX Help-Manufacturing(CAM)-Post Configurator-Post Configurator configuration objets. 
        """
        pass
    def Reset(self) -> None:
        """
         Resets the post configurator data. 
        """
        pass
    def Save(self) -> None:
        """
         Saves the post configurator data. 
        """
        pass
    def SaveAs(self, postprocessorName: str, outputDirectory: str) -> None:
        """
         Saves the post configurator data in different name. 
        """
        pass
    def SetPropertyToDefaultValue(self, chainID: str, configurationObjectID: str, propertyID: str) -> None:
        """
         Sets the property to default value. 
                        The configurationObjectID and propertyID are documented under NX Help-Manufacturing(CAM)-Post Configurator-Post Configurator configuration objets.
        """
        pass
    @overload
    def SetPropertyValue(self, chainID: str, configurationObjectID: str, propertyID: str, value: str) -> None:
        """
         Sets the property with string value. 
                        The configurationObjectID and propertyID are documented under NX Help-Manufacturing(CAM)-Post Configurator-Post Configurator configuration objets.
        """
        pass
    @overload
    def SetPropertyValue(self, chainID: str, configurationObjectID: str, propertyID: str, value: List[str]) -> None:
        """
         Sets the property with multistring value. 
                        The configurationObjectID and propertyID are documented under NX Help-Manufacturing(CAM)-Post Configurator-Post Configurator configuration objets.
        """
        pass
    @overload
    def SetPropertyValue(self, chainID: str, configurationObjectID: str, propertyID: str, value: int) -> None:
        """
         Sets the property with integer value. 
                        The configurationObjectID and propertyID are documented under NX Help-Manufacturing(CAM)-Post Configurator-Post Configurator configuration objets.
        """
        pass
    @overload
    def SetPropertyValue(self, chainID: str, configurationObjectID: str, propertyID: str, value: float) -> None:
        """
         Sets the property with double value. 
                        The configurationObjectID and propertyID are documented under NX Help-Manufacturing(CAM)-Post Configurator-Post Configurator configuration objets.
        """
        pass
    @overload
    def SetPropertyValue(self, chainID: str, configurationObjectID: str, propertyID: str, firstValue: float, secondValue: float, thirdValue: float) -> None:
        """
         Sets the property with double array value. Used for vector or point property
                        The configurationObjectID and propertyID are documented under NX Help-Manufacturing(CAM)-Post Configurator-Post Configurator configuration objets.
        """
        pass
    def ShowChanges(self) -> None:
        """
         Shows the post configurator data changes in the listing window. 
        """
        pass
    def UpdateUdeEditorBuilder(self) -> None:
        """
         Update the ude editor builder. 
        """
        pass
import NXOpen
class PostConfiguratorDebugBuilder(NXOpen.Builder): 
    """ This class is represents a SIM.PostConfigurator.PostConfiguratorDebugBuilder.
            Calling Builder.Commit on this builder will only return .
        """
    class DumpType(Enum):
        """
        Members Include: 
         |NotSet|  Dump Nothing 
         |ShowChanges|  Dump Show Changes 
         |ShowAllSettings|  Dump All Setting Values 

        """
        NotSet: int
        ShowChanges: int
        ShowAllSettings: int
        @staticmethod
        def ValueOf(value: int) -> PostConfiguratorDebugBuilder.DumpType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OutputType(Enum):
        """
        Members Include: 
         |Syslog|  Output to syslog 
         |ListingWindow|  Output to listing window 
         |Xml|  Output to xml 
         |ToFile|  Output to file 

        """
        Syslog: int
        ListingWindow: int
        Xml: int
        ToFile: int
        @staticmethod
        def ValueOf(value: int) -> PostConfiguratorDebugBuilder.OutputType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TraceType(Enum):
        """
        Members Include: 
         |CreatePostprocessor|  Trace Create Postprocessor 
         |SelectPostprocessor|  Trace Select Postprocessor 

        """
        CreatePostprocessor: int
        SelectPostprocessor: int
        @staticmethod
        def ValueOf(value: int) -> PostConfiguratorDebugBuilder.TraceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Dump(self) -> PostConfiguratorDebugBuilder.DumpType:
        """
        Getter for property: ( PostConfiguratorDebugBuilder.DumpType NXOpen.SIM.Po) Dump
         Returns the dump   
            
         
        """
        pass
    @Dump.setter
    def Dump(self, type: PostConfiguratorDebugBuilder.DumpType):
        """
        Setter for property: ( PostConfiguratorDebugBuilder.DumpType NXOpen.SIM.Po) Dump
         Returns the dump   
            
         
        """
        pass
    @property
    def Output(self) -> PostConfiguratorDebugBuilder.OutputType:
        """
        Getter for property: ( PostConfiguratorDebugBuilder.OutputType NXOpen.SIM.Po) Output
         Returns the output   
            
         
        """
        pass
    @Output.setter
    def Output(self, type: PostConfiguratorDebugBuilder.OutputType):
        """
        Setter for property: ( PostConfiguratorDebugBuilder.OutputType NXOpen.SIM.Po) Output
         Returns the output   
            
         
        """
        pass
    @property
    def OutputToFileName(self) -> str:
        """
        Getter for property: (str) OutputToFileName
         Returns the output filename   
            
         
        """
        pass
    @OutputToFileName.setter
    def OutputToFileName(self, name: str):
        """
        Setter for property: (str) OutputToFileName
         Returns the output filename   
            
         
        """
        pass
    def GetTrace(self, type: PostConfiguratorDebugBuilder.TraceType) -> bool:
        """
         Gets the trace 
         Returns state (bool):  The state.
        """
        pass
    def SetTrace(self, type: PostConfiguratorDebugBuilder.TraceType, state: bool) -> None:
        """
        Sets the trace 
        """
        pass
import NXOpen
class PostConfiguratorManager(NXOpen.Object): 
    """ Represents Post Configurator Manager"""
    def CreateCreationPostBuilder() -> CreationPostBuilder:
        """
         Creates a NXOpen.SIM.PostConfigurator.CreationPostBuilder object 
         Returns creationPostBuilder ( CreationPostBuilder NXOpen.SIM.Po):  The new creation post builder .
        """
        pass
    def CreateEncryptPostprocessorFilesBuilder(postProcessorFilename: str) -> EncryptPostprocessorFilesBuilder:
        """
         Creates a NXOpen.SIM.PostConfigurator.EncryptPostprocessorFilesBuilder object 
         Returns postConfiguratorBuilder ( EncryptPostprocessorFilesBuilder NXOpen.SIM.Po):  The new encrypt postprocessor files builder .
        """
        pass
    def CreatePostConfiguratorBuilder(postProcessorFilename: str) -> PostConfiguratorBuilder:
        """
         Creates a NXOpen.SIM.PostConfigurator.PostConfiguratorBuilder object 
         Returns postConfiguratorBuilder ( PostConfiguratorBuilder NXOpen.SIM.Po):  The new post configurator builder .
        """
        pass
    def CreatePostConfiguratorDebugBuilder() -> PostConfiguratorDebugBuilder:
        """
         Creates a NXOpen.SIM.PostConfigurator.PostConfiguratorDebugBuilder object 
         Returns postConfiguratorDebugBuilder ( PostConfiguratorDebugBuilder NXOpen.SIM.Po):  The new post configurator debug builder .
        """
        pass
    def CreateUdeBuilder() -> UdeBuilder:
        """
         Creates a NXOpen.SIM.PostConfigurator.UdeBuilder object 
         Returns udeBuilder ( UdeBuilder NXOpen.SIM.Po):  The new ude builder .
        """
        pass
    def CreateUdeParameterBuilder() -> UdeParameterBuilder:
        """
         Creates a NXOpen.SIM.PostConfigurator.UdeParameterBuilder object 
         Returns udeParameterBuilder ( UdeParameterBuilder NXOpen.SIM.Po):  The new ude parameter builder .
        """
        pass
import NXOpen
class UdeBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[UdeBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: UdeBuilder) -> None:
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
    def Erase(self, obj: UdeBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: UdeBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: UdeBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> UdeBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( UdeBuilder NXOpen.SIM.Po):  object found at input index .
        """
        pass
    def GetContents(self) -> List[UdeBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( UdeBuilder List[NXOpen.SIM.):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: UdeBuilder) -> None:
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
    def SetContents(self, objects: List[UdeBuilder]) -> None:
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
    def Swap(self, object1: UdeBuilder, object2: UdeBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class UdeBuilder(NXOpen.Builder): 
    """ This class is used to create a new event.
            Calling Builder.Commit on this builder will only return .
        """
    class CdlWriteType(Enum):
        """
        Members Include: 
         |Event|  Event   
         |Cycle|  Cycle 
         |SysCycle|  SysCycle 

        """
        Event: int
        Cycle: int
        SysCycle: int
        @staticmethod
        def ValueOf(value: int) -> UdeBuilder.CdlWriteType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class EventDescriptionType(Enum):
        """
        Members Include: 
         |NotSet|  None   
         |Specify|  Specify 

        """
        NotSet: int
        Specify: int
        @staticmethod
        def ValueOf(value: int) -> UdeBuilder.EventDescriptionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CdlWrite(self) -> UdeBuilder.CdlWriteType:
        """
        Getter for property: ( UdeBuilder.CdlWriteType NXOpen.SIM.Po) CdlWrite
         Returns the cdl write type   
            
         
        """
        pass
    @CdlWrite.setter
    def CdlWrite(self, cdlWriteType: UdeBuilder.CdlWriteType):
        """
        Setter for property: ( UdeBuilder.CdlWriteType NXOpen.SIM.Po) CdlWrite
         Returns the cdl write type   
            
         
        """
        pass
    @property
    def EventCategoryDrilling(self) -> bool:
        """
        Getter for property: (bool) EventCategoryDrilling
         Returns the event category drilling   
            
         
        """
        pass
    @EventCategoryDrilling.setter
    def EventCategoryDrilling(self, hasCategoryDrilling: bool):
        """
        Setter for property: (bool) EventCategoryDrilling
         Returns the event category drilling   
            
         
        """
        pass
    @property
    def EventCategoryInvalid(self) -> bool:
        """
        Getter for property: (bool) EventCategoryInvalid
         Returns the event category invalid   
            
         
        """
        pass
    @EventCategoryInvalid.setter
    def EventCategoryInvalid(self, hasCategoryInvalid: bool):
        """
        Setter for property: (bool) EventCategoryInvalid
         Returns the event category invalid   
            
         
        """
        pass
    @property
    def EventCategoryMilling(self) -> bool:
        """
        Getter for property: (bool) EventCategoryMilling
         Returns the event category milling   
            
         
        """
        pass
    @EventCategoryMilling.setter
    def EventCategoryMilling(self, hasCategoryMilling: bool):
        """
        Setter for property: (bool) EventCategoryMilling
         Returns the event category milling   
            
         
        """
        pass
    @property
    def EventCategoryTurning(self) -> bool:
        """
        Getter for property: (bool) EventCategoryTurning
         Returns the event category turning   
            
         
        """
        pass
    @EventCategoryTurning.setter
    def EventCategoryTurning(self, hasCategoryTurning: bool):
        """
        Setter for property: (bool) EventCategoryTurning
         Returns the event category turning   
            
         
        """
        pass
    @property
    def EventCategoryWireEDM(self) -> bool:
        """
        Getter for property: (bool) EventCategoryWireEDM
         Returns the event category wire EDM   
            
         
        """
        pass
    @EventCategoryWireEDM.setter
    def EventCategoryWireEDM(self, hasCategoryWireEDM: bool):
        """
        Setter for property: (bool) EventCategoryWireEDM
         Returns the event category wire EDM   
            
         
        """
        pass
    @property
    def EventDescription(self) -> UdeBuilder.EventDescriptionType:
        """
        Getter for property: ( UdeBuilder.EventDescriptionType NXOpen.SIM.Po) EventDescription
         Returns the event description type   
            
         
        """
        pass
    @EventDescription.setter
    def EventDescription(self, eventDescription: UdeBuilder.EventDescriptionType):
        """
        Setter for property: ( UdeBuilder.EventDescriptionType NXOpen.SIM.Po) EventDescription
         Returns the event description type   
            
         
        """
        pass
    @property
    def EventHelpDescription(self) -> str:
        """
        Getter for property: (str) EventHelpDescription
         Returns the event description   
            
         
        """
        pass
    @EventHelpDescription.setter
    def EventHelpDescription(self, helpDescription: str):
        """
        Setter for property: (str) EventHelpDescription
         Returns the event description   
            
         
        """
        pass
    @property
    def EventHelpLocation(self) -> str:
        """
        Getter for property: (str) EventHelpLocation
         Returns the event url location   
            
         
        """
        pass
    @EventHelpLocation.setter
    def EventHelpLocation(self, helpLocation: str):
        """
        Setter for property: (str) EventHelpLocation
         Returns the event url location   
            
         
        """
        pass
    @property
    def EventID(self) -> str:
        """
        Getter for property: (str) EventID
         Returns the event ID   
            
         
        """
        pass
    @EventID.setter
    def EventID(self, stringEventID: str):
        """
        Setter for property: (str) EventID
         Returns the event ID   
            
         
        """
        pass
    @property
    def EventName(self) -> str:
        """
        Getter for property: (str) EventName
         Returns the event name   
            
         
        """
        pass
    @EventName.setter
    def EventName(self, name: str):
        """
        Setter for property: (str) EventName
         Returns the event name   
            
         
        """
        pass
    @property
    def PostEvent(self) -> str:
        """
        Getter for property: (str) PostEvent
         Returns the post event   
            
         
        """
        pass
    @PostEvent.setter
    def PostEvent(self, postEventID: str):
        """
        Setter for property: (str) PostEvent
         Returns the post event   
            
         
        """
        pass
    @property
    def UdeParameterList(self) -> UdeParameterBuilderList:
        """
        Getter for property: ( UdeParameterBuilderList NXOpen.SIM.Po) UdeParameterList
         Returns the ude parameter list   
            
         
        """
        pass
    def AddItem(self, itemBuilder: UdeParameterBuilder) -> None:
        """
         Adds item to item used list 
        """
        pass
    def DeleteItem(self, itemBuilder: UdeParameterBuilder) -> None:
        """
         Deletes parameter from ude list 
        """
        pass
    def DeleteItems(self) -> None:
        """
         Deletes all parameters from ude list 
        """
        pass
    def GetUdeParameterBuilder(self, parameterID: str) -> UdeParameterBuilder:
        """
         Returns the ude parameter builder by parameter ID 
         Returns itemBuilder ( UdeParameterBuilder NXOpen.SIM.Po):  the ude parameter builder .
        """
        pass
    def RenameParameterID(self, itemBuilder: UdeParameterBuilder, oldParameterID: str, newParameterID: str) -> None:
        """
         Renames the parameter ID 
        """
        pass
import NXOpen
class UdeEditorBuilder(NXOpen.Builder): 
    """ This class is represents a SIM.PostConfigurator.UdeEditorBuilder.
            Calling Builder.Commit on this builder will only return .
        """
    @property
    def UdeBuilderList(self) -> UdeBuilderList:
        """
        Getter for property: ( UdeBuilderList NXOpen.SIM.Po) UdeBuilderList
         Returns the ude list   
            
         
        """
        pass
    def AddNewEvent(self) -> UdeBuilder:
        """
         Adds event to event list 
         Returns udeBuilder ( UdeBuilder NXOpen.SIM.Po):  the new ude builder .
        """
        pass
    def AddUdeHandler(self, udeBuilder: UdeBuilder) -> None:
        """
         Add event handler for selected event 
        """
        pass
    def CopyEventToCdlFile(self, udeBuilder: UdeBuilder, cdlFile: str) -> UdeBuilder:
        """
         Duplicates selected event to targeted cdl file
         Returns newUdeBuilder ( UdeBuilder NXOpen.SIM.Po):  the new ude builder .
        """
        pass
    def DuplicateEvent(self, udeBuilder: UdeBuilder) -> UdeBuilder:
        """
         Duplicates selected event from event list 
         Returns newUdeBuilder ( UdeBuilder NXOpen.SIM.Po):  the new ude builder .
        """
        pass
    def GetUdeBuilder(self, eventHandlerID: str) -> UdeBuilder:
        """
         Returns the ude builder by event handler ID 
         Returns udeBuilder ( UdeBuilder NXOpen.SIM.Po):  the ude builder .
        """
        pass
    def GetUdeBuilderByCdl(self, eventID: str, cdlFile: str) -> UdeBuilder:
        """
         Returns the ude builder by event handler ID and cdl File
         Returns udeBuilder ( UdeBuilder NXOpen.SIM.Po):  the ude builder .
        """
        pass
    def ListEvent(self, udeBuilder: UdeBuilder) -> None:
        """
         Lists selected event to listing window 
        """
        pass
    def ReloadUDEAndUDC(self) -> None:
        """
         Reload UDE and UDC 
        """
        pass
    def RemoveEvent(self, udeBuilder: UdeBuilder) -> None:
        """
         Removes selected event from event list 
        """
        pass
    def RemoveUdeHandler(self, udeBuilder: UdeBuilder) -> None:
        """
         Remove event handler of selected event 
        """
        pass
import NXOpen
class UdeParameterBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[UdeParameterBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: UdeParameterBuilder) -> None:
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
    def Erase(self, obj: UdeParameterBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: UdeParameterBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: UdeParameterBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> UdeParameterBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( UdeParameterBuilder NXOpen.SIM.Po):  object found at input index .
        """
        pass
    def GetContents(self) -> List[UdeParameterBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( UdeParameterBuilder List[NXOpen.SIM.):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: UdeParameterBuilder) -> None:
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
    def SetContents(self, objects: List[UdeParameterBuilder]) -> None:
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
    def Swap(self, object1: UdeParameterBuilder, object2: UdeParameterBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class UdeParameterBuilder(NXOpen.Builder): 
    """ This class is used to create a new event item.
            Calling Builder.Commit on this builder will only return .
        """
    class GroupStateType(Enum):
        """
        Members Include: 
         |Open|  Open   
         |Closed|  Closed 
         |End|  End 

        """
        Open: int
        Closed: int
        End: int
        @staticmethod
        def ValueOf(value: int) -> UdeParameterBuilder.GroupStateType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ParameterStatusType(Enum):
        """
        Members Include: 
         |NotSet|  None - Text Status is Invisible  
         |On|  On   - Text Status is Activate   
         |Off|  Off  - Text Status is Deactivate 

        """
        NotSet: int
        On: int
        Off: int
        @staticmethod
        def ValueOf(value: int) -> UdeParameterBuilder.ParameterStatusType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Type(Enum):
        """
        Members Include: 
         |Group|  Group       
         |Double|  Double      
         |Integer|  Integer     
         |String|  String      
         |Boolean|  Boolean     
         |Enumeration|  Enumeration 
         |Vector|  Vector      
         |Point|  Point       
         |Bitmap|  Bitmap      

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
        @staticmethod
        def ValueOf(value: int) -> UdeParameterBuilder.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DoubleDefaultValue(self) -> float:
        """
        Getter for property: (float) DoubleDefaultValue
         Returns the double default value   
            
         
        """
        pass
    @DoubleDefaultValue.setter
    def DoubleDefaultValue(self, doubleDefaultValue: float):
        """
        Setter for property: (float) DoubleDefaultValue
         Returns the double default value   
            
         
        """
        pass
    @property
    def EnumerationDefaultValue(self) -> str:
        """
        Getter for property: (str) EnumerationDefaultValue
         Returns the enumumeration item default value   
            
         
        """
        pass
    @EnumerationDefaultValue.setter
    def EnumerationDefaultValue(self, enumerationDefaultValue: str):
        """
        Setter for property: (str) EnumerationDefaultValue
         Returns the enumumeration item default value   
            
         
        """
        pass
    @property
    def GroupState(self) -> UdeParameterBuilder.GroupStateType:
        """
        Getter for property: ( UdeParameterBuilder.GroupStateType NXOpen.SIM.Po) GroupState
         Returns the group state   
            
         
        """
        pass
    @GroupState.setter
    def GroupState(self, state: UdeParameterBuilder.GroupStateType):
        """
        Setter for property: ( UdeParameterBuilder.GroupStateType NXOpen.SIM.Po) GroupState
         Returns the group state   
            
         
        """
        pass
    @property
    def IntegerDefaultValue(self) -> int:
        """
        Getter for property: (int) IntegerDefaultValue
         Returns the integer default value   
            
         
        """
        pass
    @IntegerDefaultValue.setter
    def IntegerDefaultValue(self, integerDefaultValue: int):
        """
        Setter for property: (int) IntegerDefaultValue
         Returns the integer default value   
            
         
        """
        pass
    @property
    def ItemType(self) -> UdeParameterBuilder.Type:
        """
        Getter for property: ( UdeParameterBuilder.Type NXOpen.SIM.Po) ItemType
         Returns the item type   
            
         
        """
        pass
    @ItemType.setter
    def ItemType(self, itemType: UdeParameterBuilder.Type):
        """
        Setter for property: ( UdeParameterBuilder.Type NXOpen.SIM.Po) ItemType
         Returns the item type   
            
         
        """
        pass
    @property
    def ParameterID(self) -> str:
        """
        Getter for property: (str) ParameterID
         Returns the parameter ID   
            
         
        """
        pass
    @ParameterID.setter
    def ParameterID(self, paramID: str):
        """
        Setter for property: (str) ParameterID
         Returns the parameter ID   
            
         
        """
        pass
    @property
    def ParameterStatus(self) -> UdeParameterBuilder.ParameterStatusType:
        """
        Getter for property: ( UdeParameterBuilder.ParameterStatusType NXOpen.SIM.Po) ParameterStatus
         Returns the item status   
            
         
        """
        pass
    @ParameterStatus.setter
    def ParameterStatus(self, parameterStatus: UdeParameterBuilder.ParameterStatusType):
        """
        Setter for property: ( UdeParameterBuilder.ParameterStatusType NXOpen.SIM.Po) ParameterStatus
         Returns the item status   
            
         
        """
        pass
    @property
    def StringDefaultValue(self) -> str:
        """
        Getter for property: (str) StringDefaultValue
         Returns the string default value   
            
         
        """
        pass
    @StringDefaultValue.setter
    def StringDefaultValue(self, stringDefaultValue: str):
        """
        Setter for property: (str) StringDefaultValue
         Returns the string default value   
            
         
        """
        pass
    @property
    def ToggleDefaultValue(self) -> bool:
        """
        Getter for property: (bool) ToggleDefaultValue
         Returns the toggle default value   
            
         
        """
        pass
    @ToggleDefaultValue.setter
    def ToggleDefaultValue(self, toggleDefaultValue: bool):
        """
        Setter for property: (bool) ToggleDefaultValue
         Returns the toggle default value   
            
         
        """
        pass
    @property
    def UILabel(self) -> str:
        """
        Getter for property: (str) UILabel
         Returns the User Interface Label   
            
         
        """
        pass
    @UILabel.setter
    def UILabel(self, uiLabel: str):
        """
        Setter for property: (str) UILabel
         Returns the User Interface Label   
            
         
        """
        pass
    def GetEnumerationItems(self) -> List[str]:
        """
         Gets a list of enumeration items 
         Returns enumerationItems (List[str]):  the list of enumeration items .
        """
        pass
    def SetEnumerationItems(self, enumerationItems: List[str]) -> None:
        """
         Sets a list of enumeration items 
        """
        pass
    def SetGroup(self, parentBuilder: UdeParameterBuilder) -> None:
        """
         Sets the ude parameter builder group 
        """
        pass
import NXOpen
class UpdatePostprocessorBuilder(NXOpen.Builder): 
    """ This class is used to update the postprocessor to the new library.
            Calling Builder.Commit on this builder will only return .
        """
    class UpdatePostprocessorType(Enum):
        """
        Members Include: 
         |FromCurrentNXVersion|  Update Postprocessor Library from Current NX Version 
         |FromPostRegistry|  Update Postprocessor Library from Post Registry 
         |Kinematic|  Update Postprocessor Kinematic 

        """
        FromCurrentNXVersion: int
        FromPostRegistry: int
        Kinematic: int
        @staticmethod
        def ValueOf(value: int) -> UpdatePostprocessorBuilder.UpdatePostprocessorType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CreateBackup(self) -> bool:
        """
        Getter for property: (bool) CreateBackup
         Returns the create backup options  
            
         
        """
        pass
    @CreateBackup.setter
    def CreateBackup(self, createBackup: bool):
        """
        Setter for property: (bool) CreateBackup
         Returns the create backup options  
            
         
        """
        pass
    @property
    def CurrentPostprocessorVersion(self) -> str:
        """
        Getter for property: (str) CurrentPostprocessorVersion
         Returns the current postprocessor version   
            
         
        """
        pass
    @CurrentPostprocessorVersion.setter
    def CurrentPostprocessorVersion(self, currentPostprocessor: str):
        """
        Setter for property: (str) CurrentPostprocessorVersion
         Returns the current postprocessor version   
            
         
        """
        pass
    @property
    def PostRegistryPath(self) -> str:
        """
        Getter for property: (str) PostRegistryPath
         Returns the post registry path   
            
         
        """
        pass
    @PostRegistryPath.setter
    def PostRegistryPath(self, filename: str):
        """
        Setter for property: (str) PostRegistryPath
         Returns the post registry path   
            
         
        """
        pass
    @property
    def UpdateCustomLayers(self) -> bool:
        """
        Getter for property: (bool) UpdateCustomLayers
         Returns the update custom layers options  
            
         
        """
        pass
    @UpdateCustomLayers.setter
    def UpdateCustomLayers(self, updateCustomLayers: bool):
        """
        Setter for property: (bool) UpdateCustomLayers
         Returns the update custom layers options  
            
         
        """
        pass
    @property
    def UpdatePostprocessor(self) -> UpdatePostprocessorBuilder.UpdatePostprocessorType:
        """
        Getter for property: ( UpdatePostprocessorBuilder.UpdatePostprocessorType NXOpen.SIM.Po) UpdatePostprocessor
         Returns the update postprocessor type   
            
         
        """
        pass
    @UpdatePostprocessor.setter
    def UpdatePostprocessor(self, updatePostprocessorType: UpdatePostprocessorBuilder.UpdatePostprocessorType):
        """
        Setter for property: ( UpdatePostprocessorBuilder.UpdatePostprocessorType NXOpen.SIM.Po) UpdatePostprocessor
         Returns the update postprocessor type   
            
         
        """
        pass
    @property
    def UpdateToVersion(self) -> str:
        """
        Getter for property: (str) UpdateToVersion
         Returns the update to version   
            
         
        """
        pass
    @UpdateToVersion.setter
    def UpdateToVersion(self, updateToVersion: str):
        """
        Setter for property: (str) UpdateToVersion
         Returns the update to version   
            
         
        """
        pass
