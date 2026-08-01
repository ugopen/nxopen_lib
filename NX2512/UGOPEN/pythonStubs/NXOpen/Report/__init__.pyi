from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class AutomationLogger(NXOpen.Object): 
    """ Represents the automation logger to log information for report automation program. """
    class MessageType(Enum):
        """
        Members Include: 
         |Empty|  None 
         |Information|  Information message 
         |Debug|  Debug message  
         |Exception|  Exception message 

        """
        Empty: int
        Information: int
        Debug: int
        Exception: int
        @staticmethod
        def ValueOf(value: int) -> AutomationLogger.MessageType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def Clear() -> None:
        """
         Clears the messages in the logger. 
        """
        pass
    def IsEmpty() -> bool:
        """
         Has messages in the logger.
         Returns empty (bool): .
        """
        pass
    @overload
    def LogMessage(message: str) -> None:
        """
         Adds debug message to the logger.
        """
        pass
    @overload
    def LogMessage(message: str, messageType: AutomationLogger.MessageType) -> None:
        """
         Adds required type of message to the logger.
        """
        pass
    def SaveLog(logFileName: str) -> None:
        """
         Saves the messages in the logger to a file. 
        """
        pass
import NXOpen
import NXOpen.Assemblies
class BaseArgument(NXOpen.TaggedObject): 
    """ Represents an abstract command argument. """
    class Type(Enum):
        """
        Members Include: 
         |Integer|  Argument for integer data 
         |Double|  Argument for double data 
         |String|  Argument for string data 
         |Enumeration|  Argument for enumeration data 

        """
        Integer: int
        Double: int
        String: int
        Enumeration: int
        @staticmethod
        def ValueOf(value: int) -> BaseArgument.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DisplayName(self) -> str:
        """
        Getter for property: (str) DisplayName
         Returns the argument display name   
            
         
        """
        pass
    @DisplayName.setter
    def DisplayName(self, displayName: str):
        """
        Setter for property: (str) DisplayName
         Returns the argument display name   
            
         
        """
        pass
    @property
    def Hint(self) -> str:
        """
        Getter for property: (str) Hint
         Returns the argument hint.  
             
         
        """
        pass
    @Hint.setter
    def Hint(self, argumentHint: str):
        """
        Setter for property: (str) Hint
         Returns the argument hint.  
             
         
        """
        pass
    @property
    def IsOccurrence(self) -> bool:
        """
        Getter for property: (bool) IsOccurrence
         Returns whether this object is an occurrence or not.  
             
         
        """
        pass
    @property
    def JournalIdentifier(self) -> str:
        """
        Getter for property: (str) JournalIdentifier
         Returns the identifier that would be recorded in a journal for this object.  
           
            This may not be the same across different releases of the software.   
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the custom name of the object.  
              
         
        """
        pass
    @property
    def Optional(self) -> bool:
        """
        Getter for property: (bool) Optional
         Returns    a value that indicates whether this argument is optional or not.  
            
            
         
        """
        pass
    @Optional.setter
    def Optional(self, isOptional: bool):
        """
        Setter for property: (bool) Optional
         Returns    a value that indicates whether this argument is optional or not.  
            
            
         
        """
        pass
    @property
    def OwningComponent(self) -> NXOpen.Assemblies.Component:
        """
        Getter for property: ( NXOpen.Assemblies.Component) OwningComponent
         Returns the owning component, if this object is an occurrence.  
             
         
        """
        pass
    @property
    def OwningPart(self) -> NXOpen.BasePart:
        """
        Getter for property: ( NXOpen.BasePart) OwningPart
         Returns the owning part of this object   
            
         
        """
        pass
    @property
    def Prototype(self) -> NXOpen.INXObject:
        """
        Getter for property: ( NXOpen.INXObject) Prototype
         Returns the prototype of this object if it is an occurrence.  
             
         
        """
        pass
import NXOpen
class BaseItem(NXOpen.NXObject): 
    """ Represents an abstract report item.  """
    @property
    def DisplayName(self) -> str:
        """
        Getter for property: (str) DisplayName
         Returns the item display name.  
             
         
        """
        pass
    @property
    def Hint(self) -> str:
        """
        Getter for property: (str) Hint
         Returns the item hint.  
             
         
        """
        pass
    def Clear(self) -> None:
        """
         Clears the content in this class. 
        """
        pass
import NXOpen
class CommandBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Report.CommandBuilder. """
    class UserInputLocation(Enum):
        """
        Members Include: 
         |BeforeAutomation|  The user item before automation 
         |AfterAutomation|  The user item after automation 

        """
        BeforeAutomation: int
        AfterAutomation: int
        @staticmethod
        def ValueOf(value: int) -> CommandBuilder.UserInputLocation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Active(self) -> bool:
        """
        Getter for property: (bool) Active
         Returns    a value that indicates whether the command is active or not.  
            
            
         
        """
        pass
    @Active.setter
    def Active(self, isActive: bool):
        """
        Setter for property: (bool) Active
         Returns    a value that indicates whether the command is active or not.  
            
            
         
        """
        pass
    @property
    def Alias(self) -> str:
        """
        Getter for property: (str) Alias
         Returns the command alias name   
            
         
        """
        pass
    @Alias.setter
    def Alias(self, aliasName: str):
        """
        Setter for property: (str) Alias
         Returns the command alias name   
            
         
        """
        pass
    @property
    def DisplayName(self) -> str:
        """
        Getter for property: (str) DisplayName
         Returns the command display name   
            
         
        """
        pass
    @DisplayName.setter
    def DisplayName(self, displayName: str):
        """
        Setter for property: (str) DisplayName
         Returns the command display name   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the command name   
            
         
        """
        pass
    @Name.setter
    def Name(self, commandName: str):
        """
        Setter for property: (str) Name
         Returns the command name   
            
         
        """
        pass
    @property
    def ProgramInformation(self) -> ProgramInformation:
        """
        Getter for property: ( ProgramInformation NXOpen) ProgramInformation
         Returns the automation program information object.  
             
         
        """
        pass
    def AddArgument(self, argumentType: BaseArgument.Type) -> BaseArgument:
        """
         Adds an argument and adds it to the command. 
         Returns pArgument ( BaseArgument NXOpen):   .
        """
        pass
    def AddUserInput(self, userInputLocation: CommandBuilder.UserInputLocation, userInputType: UserInput.Type) -> UserInput:
        """
         Adds an user input and adds it to command. 
         Returns pUserInput ( UserInput NXOpen):   .
        """
        pass
    def GetArguments(self) -> List[BaseArgument]:
        """
         Gets all arguments in the command. 
         Returns pArguments ( BaseArgument List[NXOp):   .
        """
        pass
    def GetHint(self) -> List[str]:
        """
         Gets the command hint 
         Returns commandHint (List[str]): .
        """
        pass
    def GetNamespaces(self) -> List[str]:
        """
         Gets the categories which command apply to. 
         Returns pNamespaces (List[str]): .
        """
        pass
    def GetUserInputs(self, userInputLocation: CommandBuilder.UserInputLocation) -> List[UserInput]:
        """
         Gets all user inputs. 
         Returns pUserInputs ( UserInput List[NXOp):   .
        """
        pass
    def MoveUserInputs(self, userInputLocation: CommandBuilder.UserInputLocation, pUserInputs: List[UserInput], isBeforeRefUserInput: bool, pRefUserInputs: UserInput) -> None:
        """
         Moves the user inputs to the new position. 
        """
        pass
    def RemoveArguments(self, pArguments: List[BaseArgument]) -> None:
        """
         Removes the arguments. 
        """
        pass
    def RemoveUserInputs(self, userInputLocation: CommandBuilder.UserInputLocation, pUserInputs: List[UserInput]) -> None:
        """
         Removes the user inputs. 
        """
        pass
    def SetHint(self, commandHint: List[str]) -> None:
        """
         Sets the command hint 
        """
        pass
    def SetNamespaces(self, pNamespaces: List[str]) -> None:
        """
         Sets the categories which command apply to. 
        """
        pass
import NXOpen
class CommandImporter(NXOpen.TransientObject): 
    """ Represents a command importer to import the commands into command libary. """
    class OverrideOption(Enum):
        """
        Members Include: 
         |Ignore|  No action, do not import to library 
         |Replace|  Import to replace the existing one  
         |Copy|  Import and append a new one 

        """
        Ignore: int
        Replace: int
        Copy: int
        @staticmethod
        def ValueOf(value: int) -> CommandImporter.OverrideOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ImportOption(self) -> CommandImporter.OverrideOption:
        """
        Getter for property: ( CommandImporter.OverrideOption NXOpen) ImportOption
         Returns the command override option.  
             
         
        """
        pass
    @ImportOption.setter
    def ImportOption(self, importOption: CommandImporter.OverrideOption):
        """
        Setter for property: ( CommandImporter.OverrideOption NXOpen) ImportOption
         Returns the command override option.  
             
         
        """
        pass
    def Dispose(self) -> None:
        """
         Destroys the object 
        """
        pass
    def GetImportCandidates(self) -> List[Command]:
        """
         Gets all candidate commands in library file. 
         Returns pCommands ( Command List[NXOp): .
        """
        pass
    def ImportCommands(self, pCommandIndexes: List[int]) -> None:
        """
         Imports the selected commands into command library. 
        """
        pass
import NXOpen
import NXOpen.Assemblies
class CommandLibrary(NXOpen.TaggedObject): 
    """ Represents a command library in the command manager."""
    class MoveCommandLocation(Enum):
        """
        Members Include: 
         |Before|  Move commands ahead of a referenced command 
         |After|  Move commands behind a referenced command 

        """
        Before: int
        After: int
        @staticmethod
        def ValueOf(value: int) -> CommandLibrary.MoveCommandLocation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def IsOccurrence(self) -> bool:
        """
        Getter for property: (bool) IsOccurrence
         Returns whether this object is an occurrence or not.  
             
         
        """
        pass
    @property
    def JournalIdentifier(self) -> str:
        """
        Getter for property: (str) JournalIdentifier
         Returns the identifier that would be recorded in a journal for this object.  
           
            This may not be the same across different releases of the software.   
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the custom name of the object.  
              
         
        """
        pass
    @property
    def OwningComponent(self) -> NXOpen.Assemblies.Component:
        """
        Getter for property: ( NXOpen.Assemblies.Component) OwningComponent
         Returns the owning component, if this object is an occurrence.  
             
         
        """
        pass
    @property
    def OwningPart(self) -> NXOpen.BasePart:
        """
        Getter for property: ( NXOpen.BasePart) OwningPart
         Returns the owning part of this object   
            
         
        """
        pass
    @property
    def Prototype(self) -> NXOpen.INXObject:
        """
        Getter for property: ( NXOpen.INXObject) Prototype
         Returns the prototype of this object if it is an occurrence.  
             
         
        """
        pass
    def GetCommands(self) -> List[Command]:
        """
         Gets all commands in command library. 
         Returns pCommands ( Command List[NXOp):   .
        """
        pass
    def MoveCommands(self, pCommand: List[Command], newLocation: CommandLibrary.MoveCommandLocation, pReferenceCommand: Command) -> None:
        """
         Moves the commands to the new position. 
        """
        pass
    def Save(self) -> None:
        """
         Saves all commands to their binding xml file. 
        """
        pass
import NXOpen
class CommandManager(NXOpen.Object): 
    """ Represents the command manager. """
    def CreateCommandBuilder(commandLibrary: CommandLibrary, command: Command) -> CommandBuilder:
        """
         Creates the command builder. 
         Returns builder ( CommandBuilder NXOpen):   .
        """
        pass
    def ExportCommandsToLibraryFile(pCommands: List[Command], libraryFile: str) -> None:
        """
         Export selected commands to a library folder zip file. 
        """
        pass
    def Find(journalIdentifier: str) -> NXOpen.TaggedObject:
        """
         Finds the TaggedObject with the given identifier as recorded in a journal. 
         Returns foundObject ( NXOpen.TaggedObject):  Object found, or null if no such object exists .
        """
        pass
    def GetCommandLibraries() -> List[CommandLibrary]:
        """
         Gets all command libraries. 
         Returns pCommandLibraries ( CommandLibrary List[NXOp):   .
        """
        pass
    def NewCommandImporter(pCommandLibrary: CommandLibrary, libraryFile: str) -> CommandImporter:
        """
         Creates a transient object  NXOpen.Report.CommandImporter  to import
                    the selected commands of a command library file to a command library. The object
                    should be destroyed after finishing import. 
         Returns pCommandImporter ( CommandImporter NXOpen): .
        """
        pass
import NXOpen
class Command(NXOpen.NXObject): 
    """ Represents a command in command library. """
    def Delete(self) -> None:
        """
         Deletes the command. 
        """
        pass
class DoubleArgument(BaseArgument): 
    """ Represents an argument for double type data. This class
        does not include upper bound and lower bound in default. """
    @property
    def DefaultValue(self) -> float:
        """
        Getter for property: (float) DefaultValue
         Returns the arguement dafault value.  
             
         
        """
        pass
    @DefaultValue.setter
    def DefaultValue(self, argumentValue: float):
        """
        Setter for property: (float) DefaultValue
         Returns the arguement dafault value.  
             
         
        """
        pass
    @property
    def IncludeLowerBound(self) -> bool:
        """
        Getter for property: (bool) IncludeLowerBound
         Returns    a value that indicates whether includes the lower bound.  
            
            
         
        """
        pass
    @IncludeLowerBound.setter
    def IncludeLowerBound(self, includeLowerBound: bool):
        """
        Setter for property: (bool) IncludeLowerBound
         Returns    a value that indicates whether includes the lower bound.  
            
            
         
        """
        pass
    @property
    def IncludeUpperBound(self) -> bool:
        """
        Getter for property: (bool) IncludeUpperBound
         Returns    a value that indicates whether includes the upper bound.  
            
            
         
        """
        pass
    @IncludeUpperBound.setter
    def IncludeUpperBound(self, includeUpperBound: bool):
        """
        Setter for property: (bool) IncludeUpperBound
         Returns    a value that indicates whether includes the upper bound.  
            
            
         
        """
        pass
    @property
    def MaximumValue(self) -> float:
        """
        Getter for property: (float) MaximumValue
         Returns the maximum value.  
             
         
        """
        pass
    @MaximumValue.setter
    def MaximumValue(self, maximumValue: float):
        """
        Setter for property: (float) MaximumValue
         Returns the maximum value.  
             
         
        """
        pass
    @property
    def MimimumValue(self) -> float:
        """
        Getter for property: (float) MimimumValue
         Returns the minimum value.  
             
         
        """
        pass
    @MimimumValue.setter
    def MimimumValue(self, minimumValue: float):
        """
        Setter for property: (float) MimimumValue
         Returns the minimum value.  
             
         
        """
        pass
class EnumerationArgument(BaseArgument): 
    """ Represents an argument for enumeration type data. """
    @property
    def DefaultValue(self) -> int:
        """
        Getter for property: (int) DefaultValue
         Returns the argument default value.  
           The default value index is between 0 and options count queried
                    by  NXOpen::Report::EnumerationArgument::GetEnumerationOptions , 0 is inclusive.   
         
        """
        pass
    @DefaultValue.setter
    def DefaultValue(self, defaultValueIndex: int):
        """
        Setter for property: (int) DefaultValue
         Returns the argument default value.  
           The default value index is between 0 and options count queried
                    by  NXOpen::Report::EnumerationArgument::GetEnumerationOptions , 0 is inclusive.   
         
        """
        pass
    def GetEnumerationOptions(self) -> List[str]:
        """
         Gets the enumeration options. 
         Returns enumerationOptions (List[str]):   .
        """
        pass
    def SetEnumerationOptions(self, enumerationOptions: List[str]) -> None:
        """
         Sets the enumeration options. 
        """
        pass
import NXOpen
class ImageOption(NXOpen.TaggedObject): 
    """ Represents an image option object.  """
    @property
    def ImageHeight(self) -> float:
        """
        Getter for property: (float) ImageHeight
         Returns the image height .  
             
         
        """
        pass
    @ImageHeight.setter
    def ImageHeight(self, imageHeight: float):
        """
        Setter for property: (float) ImageHeight
         Returns the image height .  
             
         
        """
        pass
    @property
    def ImageRotation(self) -> float:
        """
        Getter for property: (float) ImageRotation
         Returns the image rotation angle in degree.  
             
         
        """
        pass
    @ImageRotation.setter
    def ImageRotation(self, imageRotation: float):
        """
        Setter for property: (float) ImageRotation
         Returns the image rotation angle in degree.  
             
         
        """
        pass
    @property
    def ImageWidth(self) -> float:
        """
        Getter for property: (float) ImageWidth
         Returns the image width .  
             
         
        """
        pass
    @ImageWidth.setter
    def ImageWidth(self, imageWidth: float):
        """
        Setter for property: (float) ImageWidth
         Returns the image width .  
             
         
        """
        pass
    @property
    def LockOriginalAspectRatio(self) -> bool:
        """
        Getter for property: (bool) LockOriginalAspectRatio
         Returns    a value that indicates whether locks original image aspect ratio.  
           If locks ratio, the image
                    width will be updated according to the ratio when image height changes , and vice versa. 
            
         
        """
        pass
    @LockOriginalAspectRatio.setter
    def LockOriginalAspectRatio(self, lockRatio: bool):
        """
        Setter for property: (bool) LockOriginalAspectRatio
         Returns    a value that indicates whether locks original image aspect ratio.  
           If locks ratio, the image
                    width will be updated according to the ratio when image height changes , and vice versa. 
            
         
        """
        pass
class ImagesGroupItem(BaseItem): 
    """ Represents a images group item.  """
    def CopyImage(self, pReportImage: ReportImage) -> ReportImage:
        """
         Copy a NXOpen.Report.ReportImage to the this class. 
         Returns pReportImageCopy ( ReportImage NXOpen):  copy of the input image .
        """
        pass
    def CreateImage(self, imageFile: str, displayName: str) -> ReportImage:
        """
         Creates an image in images group. 
         Returns pReportImage ( ReportImage NXOpen):   .
        """
        pass
    def DeleteImages(self) -> None:
        """
         Deletes all images in class. 
        """
        pass
    def GetImages(self) -> List[ReportImage]:
        """
         Gets all images in images group. 
         Returns pReportImages ( ReportImage List[NXOp):   .
        """
        pass
    def MoveImages(self, pReportImages: List[ReportImage], newLocation: Report.MoveItemLocation, pReferencedImage: ReportImage) -> None:
        """
         Moves the images to the new position. 
        """
        pass
class IntegerArgument(BaseArgument): 
    """ Represents an argument for integer type data. This class
        does not include upper bound and lower bound in default. """
    @property
    def DefaultValue(self) -> int:
        """
        Getter for property: (int) DefaultValue
         Returns the argument default value.  
             
         
        """
        pass
    @DefaultValue.setter
    def DefaultValue(self, defaultValue: int):
        """
        Setter for property: (int) DefaultValue
         Returns the argument default value.  
             
         
        """
        pass
    @property
    def IncludeLowerBound(self) -> bool:
        """
        Getter for property: (bool) IncludeLowerBound
         Returns    a value that indicates whether includes the lower bound.  
            
            
         
        """
        pass
    @IncludeLowerBound.setter
    def IncludeLowerBound(self, includeLowerBound: bool):
        """
        Setter for property: (bool) IncludeLowerBound
         Returns    a value that indicates whether includes the lower bound.  
            
            
         
        """
        pass
    @property
    def IncludeUpperBound(self) -> bool:
        """
        Getter for property: (bool) IncludeUpperBound
         Returns    a value that indicates whether includes the upper bound.  
            
            
         
        """
        pass
    @IncludeUpperBound.setter
    def IncludeUpperBound(self, includeUpperBound: bool):
        """
        Setter for property: (bool) IncludeUpperBound
         Returns    a value that indicates whether includes the upper bound.  
            
            
         
        """
        pass
    @property
    def MaximumValue(self) -> int:
        """
        Getter for property: (int) MaximumValue
         Returns the maximum value.  
             
         
        """
        pass
    @MaximumValue.setter
    def MaximumValue(self, maximumValue: int):
        """
        Setter for property: (int) MaximumValue
         Returns the maximum value.  
             
         
        """
        pass
    @property
    def MinimumValue(self) -> int:
        """
        Getter for property: (int) MinimumValue
         Returns the minimum value.  
             
         
        """
        pass
    @MinimumValue.setter
    def MinimumValue(self, minimumValue: int):
        """
        Setter for property: (int) MinimumValue
         Returns the minimum value.  
             
         
        """
        pass
import NXOpen
class IReportCollection(NXOpen.INXObject): 
    """ This interface is used to manage associated reports Report.Report """
    @abstractmethod
    def CreateReport(self, templateFile: str, reportName: str, listError: bool) -> Report:
        """
         Creates a Report.Report in this report collection.
                    NX will not create a report if the report name is empty or existed. 
         Returns pReport ( Report NXOpen):   .
        """
        pass
    @abstractmethod
    def GetReports(self) -> List[Report]:
        """
         Gets all reports in the report collection. 
         Returns pReports ( Report List[NXOp):   .
        """
        pass
import NXOpen
class IUserItem(NXOpen.INXObject): 
    """ Represents an user defined report item. """
    @abstractmethod
    def SetDisplayName(self, displayName: str) -> None:
        """
         Sets the display name. 
        """
        pass
import NXOpen
import NXOpen.Assemblies
class ProgramInformation(NXOpen.TaggedObject): 
    """ Represents the program information for command automation. """
    class LanguageType(Enum):
        """
        Members Include: 
         |NotSet|  None language 
         |CPlusplus|  C plus plus language 
         |CSharp|  C sharp language  
         |Vb|  Visual basic language  
         |Java|  Java language  
         |Python|  Python language  

        """
        NotSet: int
        CPlusplus: int
        CSharp: int
        Vb: int
        Java: int
        Python: int
        @staticmethod
        def ValueOf(value: int) -> ProgramInformation.LanguageType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FunctionName(self) -> str:
        """
        Getter for property: (str) FunctionName
         Returns the program entry function name.  
          
                    CPlusplus language: the function name is the exported function following required interface,
                    Java language: the function name is the exported java class name,
                    CSharp, Vb and Python language: the function name is "Main".   
         
        """
        pass
    @FunctionName.setter
    def FunctionName(self, functionName: str):
        """
        Setter for property: (str) FunctionName
         Returns the program entry function name.  
          
                    CPlusplus language: the function name is the exported function following required interface,
                    Java language: the function name is the exported java class name,
                    CSharp, Vb and Python language: the function name is "Main".   
         
        """
        pass
    @property
    def IsOccurrence(self) -> bool:
        """
        Getter for property: (bool) IsOccurrence
         Returns whether this object is an occurrence or not.  
             
         
        """
        pass
    @property
    def JournalIdentifier(self) -> str:
        """
        Getter for property: (str) JournalIdentifier
         Returns the identifier that would be recorded in a journal for this object.  
           
            This may not be the same across different releases of the software.   
         
        """
        pass
    @property
    def Language(self) -> ProgramInformation.LanguageType:
        """
        Getter for property: ( ProgramInformation.LanguageType NXOpen) Language
         Returns the automation program language.  
             
         
        """
        pass
    @Language.setter
    def Language(self, languageType: ProgramInformation.LanguageType):
        """
        Setter for property: ( ProgramInformation.LanguageType NXOpen) Language
         Returns the automation program language.  
             
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the custom name of the object.  
              
         
        """
        pass
    @property
    def OwningComponent(self) -> NXOpen.Assemblies.Component:
        """
        Getter for property: ( NXOpen.Assemblies.Component) OwningComponent
         Returns the owning component, if this object is an occurrence.  
             
         
        """
        pass
    @property
    def OwningPart(self) -> NXOpen.BasePart:
        """
        Getter for property: ( NXOpen.BasePart) OwningPart
         Returns the owning part of this object   
            
         
        """
        pass
    @property
    def ProgramFile(self) -> str:
        """
        Getter for property: (str) ProgramFile
         Returns the automation program executer file.  
          
                    CPlusplus language: the dll file,
                    CSharp language: the CS file or CS dll file,
                    Vb language: the VB file or VB dll file,
                    Java language: the Jar file,
                    Python language: the Py file.   
         
        """
        pass
    @ProgramFile.setter
    def ProgramFile(self, programFile: str):
        """
        Setter for property: (str) ProgramFile
         Returns the automation program executer file.  
          
                    CPlusplus language: the dll file,
                    CSharp language: the CS file or CS dll file,
                    Vb language: the VB file or VB dll file,
                    Java language: the Jar file,
                    Python language: the Py file.   
         
        """
        pass
    @property
    def Prototype(self) -> NXOpen.INXObject:
        """
        Getter for property: ( NXOpen.INXObject) Prototype
         Returns the prototype of this object if it is an occurrence.  
             
         
        """
        pass
import NXOpen
class ReportImage(NXOpen.NXObject): 
    """ Represents a report image. """
    @property
    def Caption(self) -> str:
        """
        Getter for property: (str) Caption
         Returns the image caption text.  
             
         
        """
        pass
    @Caption.setter
    def Caption(self, captionText: str):
        """
        Setter for property: (str) Caption
         Returns the image caption text.  
             
         
        """
        pass
    @property
    def ImageOption(self) -> ImageOption:
        """
        Getter for property: ( ImageOption NXOpen) ImageOption
         Returns the image option.  
             
         
        """
        pass
    def SetImage(self, imageFile: str) -> None:
        """
         Replaces the old image file with a new image file. 
        """
        pass
import NXOpen
class ReportManager(NXOpen.Object): 
    """ Represents the report manager. """
    @property
    def Preference(self) -> ReportPreference:
        """
        Getter for property: ( ReportPreference NXOpen) Preference
         Returns the report preference.  
             
         
        """
        pass
    @property
    def AutomationLogger() -> AutomationLogger:
        """
         Returns the  NXOpen::Report::AutomationLogger  belonging to the report manager 
        """
        pass
    @property
    def CommandManager() -> CommandManager:
        """
         Returns the  NXOpen::Report::CommandManager  belonging to the report manager 
        """
        pass
    def CreateResultXmlFileWriter() -> ResultXmlFileWriter:
        """
         Creates a new NXOpen.Report.ResultXmlFileWriter object.
         Returns writer ( ResultXmlFileWriter NXOpen):   .
        """
        pass
    def GetOriginalImageDimension(imageFullFileName: str) -> Tuple[float, float]:
        """
         Gets the original dimension of a given image file. 
         Returns A tuple consisting of (width, height). 
         - width is: float. .
         - height is: float. .

        """
        pass
import NXOpen
class ReportPreference(NXOpen.TaggedObject): 
    """ Manages the preference data. """
    @property
    def MaximumRecentReportDocumentCount(self) -> int:
        """
        Getter for property: (int) MaximumRecentReportDocumentCount
         Returns the maximum count of the recent report documents which could be viewed   
            
         
        """
        pass
    @MaximumRecentReportDocumentCount.setter
    def MaximumRecentReportDocumentCount(self, maxRecentReportDoc: int):
        """
        Setter for property: (int) MaximumRecentReportDocumentCount
         Returns the maximum count of the recent report documents which could be viewed   
            
         
        """
        pass
    @property
    def OpenReportDocumentAfterExport(self) -> bool:
        """
        Getter for property: (bool) OpenReportDocumentAfterExport
         Returns the option indicates whether to open report document after exporting report   
            
         
        """
        pass
    @OpenReportDocumentAfterExport.setter
    def OpenReportDocumentAfterExport(self, openReportAfterExportSetting: bool):
        """
        Setter for property: (bool) OpenReportDocumentAfterExport
         Returns the option indicates whether to open report document after exporting report   
            
         
        """
        pass
    @property
    def SearchTemplateFromSiteDirectory(self) -> bool:
        """
        Getter for property: (bool) SearchTemplateFromSiteDirectory
         Returns the option indicates whether to use site template directory as start to choose a report template file    
            
         
        """
        pass
    @SearchTemplateFromSiteDirectory.setter
    def SearchTemplateFromSiteDirectory(self, searchTemplateFromSiteDirectorySetting: bool):
        """
        Setter for property: (bool) SearchTemplateFromSiteDirectory
         Returns the option indicates whether to use site template directory as start to choose a report template file    
            
         
        """
        pass
    @property
    def UsePartDirectoryAsDefaultExportLocation(self) -> bool:
        """
        Getter for property: (bool) UsePartDirectoryAsDefaultExportLocation
         Returns the option indicates whehter to use part direcotry as default report document location    
            
         
        """
        pass
    @UsePartDirectoryAsDefaultExportLocation.setter
    def UsePartDirectoryAsDefaultExportLocation(self, usePartDirAsDefaultExportLocationSetting: bool):
        """
        Setter for property: (bool) UsePartDirectoryAsDefaultExportLocation
         Returns the option indicates whehter to use part direcotry as default report document location    
            
         
        """
        pass
    @property
    def ViewImageAfterSnapshotting(self) -> bool:
        """
        Getter for property: (bool) ViewImageAfterSnapshotting
         Returns the option indicates whether to view image after snopshotting    
            
         
        """
        pass
    @ViewImageAfterSnapshotting.setter
    def ViewImageAfterSnapshotting(self, viewImageAfterSnapshotSetting: bool):
        """
        Setter for property: (bool) ViewImageAfterSnapshotting
         Returns the option indicates whether to view image after snopshotting    
            
         
        """
        pass
    def SaveMemoryFile(self) -> None:
        """
         Saves preference settings to memory file 
        """
        pass
import NXOpen
import NXOpen.OpenXml
class ResultXmlFileWriter(NXOpen.TransientObject): 
    """  Contains methods for adding document data and generating result XML file 
    for CAE Report.  """
    def AddImageGroup(self) -> NXOpen.OpenXml.ImageGroupDocumentData:
        """
         Creates a new NXOpen.OpenXml.ImageGroupDocumentData object.
                Does not to free this object, it will be free while deleting 
                NXOpen.Report.ResultXmlFileWriter object
         Returns data ( NXOpen.OpenXml.ImageGroupDocumentData):  the image group data .
        """
        pass
    def AddTable(self, columnSize: int, rowSize: int) -> NXOpen.OpenXml.TableDocumentData:
        """
         Creates a new NXOpen.OpenXml.TableDocumentData object.
                Does not to free this object, it will be free while deleting 
                NXOpen.Report.ResultXmlFileWriter object
         Returns data ( NXOpen.OpenXml.TableDocumentData):  the table data .
        """
        pass
    def AddText(self, textContent: str) -> NXOpen.OpenXml.TextDocumentData:
        """
         Creates a new NXOpen.OpenXml.TextDocumentData object.
                Does not to free this object, it will be free while deleting 
                NXOpen.Report.ResultXmlFileWriter object
         Returns data ( NXOpen.OpenXml.TextDocumentData):  the text data .
        """
        pass
    def DeleteAllData(self) -> None:
        """
         Removes all document data
        """
        pass
    def DeleteNthData(self, index: int) -> None:
        """
         Removes the nth document data
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    def GetDataCount(self) -> int:
        """
         Gets the number of data to be exported
         Returns dataCount (int):  the number of data .
        """
        pass
    def GetNthData(self, index: int) -> NXOpen.OpenXml.DocumentData:
        """
         Gets the nth document data object.
                Does not to free this object, it will be free while deleting 
                NXOpen.Report.ResultXmlFileWriter object
         Returns data ( NXOpen.OpenXml.DocumentData):  the data.
        """
        pass
    def SaveToFile(self, fileName: str) -> None:
        """
         Exports all document data to result XML file
        """
        pass
class StringArgument(BaseArgument): 
    """ Represents an argument for string type data. """
    @property
    def DefaultValue(self) -> str:
        """
        Getter for property: (str) DefaultValue
         Returns the argument default value.  
             
         
        """
        pass
    @DefaultValue.setter
    def DefaultValue(self, defaultValue: str):
        """
        Setter for property: (str) DefaultValue
         Returns the argument default value.  
             
         
        """
        pass
class TemplateItem(BaseItem): 
    """ Represents a template item object. """
    def GetChildItems(self, itemsLocation: CommandBuilder.UserInputLocation) -> List[BaseItem]:
        """
         Gets child items in template item. 
         Returns pItems ( BaseItem List[NXOp): .
        """
        pass
class TextItem(BaseItem): 
    """ Represents a text item. """
    def GetText(self) -> List[str]:
        """
         Get the text content. 
         Returns lineTexts (List[str]):   .
        """
        pass
    def SetText(self, lineTexts: List[str]) -> None:
        """
         Set the text content. 
        """
        pass
class UserImagesGroupItem(ImagesGroupItem): 
    """ Represents a user images group item.  """
    pass
import NXOpen
import NXOpen.Assemblies
class UserInput(NXOpen.TaggedObject): 
    """ Represents a user input in command. """
    class Type(Enum):
        """
        Members Include: 
         |Text|  User input for text data 
         |Images|  User input for images data  

        """
        Text: int
        Images: int
        @staticmethod
        def ValueOf(value: int) -> UserInput.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def InputType(self) -> UserInput.Type:
        """
        Getter for property: ( UserInput.Type NXOpen) InputType
         Returns the user input type.  
             
         
        """
        pass
    @InputType.setter
    def InputType(self, inputType: UserInput.Type):
        """
        Setter for property: ( UserInput.Type NXOpen) InputType
         Returns the user input type.  
             
         
        """
        pass
    @property
    def IsOccurrence(self) -> bool:
        """
        Getter for property: (bool) IsOccurrence
         Returns whether this object is an occurrence or not.  
             
         
        """
        pass
    @property
    def JournalIdentifier(self) -> str:
        """
        Getter for property: (str) JournalIdentifier
         Returns the identifier that would be recorded in a journal for this object.  
           
            This may not be the same across different releases of the software.   
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the custom name of the object.  
              
         
        """
        pass
    @property
    def OwningComponent(self) -> NXOpen.Assemblies.Component:
        """
        Getter for property: ( NXOpen.Assemblies.Component) OwningComponent
         Returns the owning component, if this object is an occurrence.  
             
         
        """
        pass
    @property
    def OwningPart(self) -> NXOpen.BasePart:
        """
        Getter for property: ( NXOpen.BasePart) OwningPart
         Returns the owning part of this object   
            
         
        """
        pass
    @property
    def Prototype(self) -> NXOpen.INXObject:
        """
        Getter for property: ( NXOpen.INXObject) Prototype
         Returns the prototype of this object if it is an occurrence.  
             
         
        """
        pass
    def GetHint(self) -> List[str]:
        """
         Gets the user input hint. 
         Returns inputHint (List[str]): .
        """
        pass
    def SetHint(self, inputHint: List[str]) -> None:
        """
         Sets the user input hint. 
        """
        pass
class UserTextItem(TextItem): 
    """ Represents a user text item. """
    pass
