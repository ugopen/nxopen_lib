from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents the automation logger to log information for report automation program.  <br> No support KF.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class AutomationLogger(NXOpen.Object): 
    """ Represents the automation logger to log information for report automation program. """


    ##  Represents the automation logger message type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Empty</term><description> 
    ##  None </description> </item><item><term> 
    ## Information</term><description> 
    ##  Information message </description> </item><item><term> 
    ## Debug</term><description> 
    ##  Debug message  </description> </item><item><term> 
    ## Exception</term><description> 
    ##  Exception message </description> </item></list>
    class MessageType(Enum):
        """
        Members Include: <Empty> <Information> <Debug> <Exception>
        """
        Empty: int
        Information: int
        Debug: int
        Exception: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AutomationLogger.MessageType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Clears the messages in the logger. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def Clear() -> None:
        """
         Clears the messages in the logger. 
        """
        pass
    
    ##  Has messages in the logger.
    ##  @return empty (bool): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def IsEmpty() -> bool:
        """
         Has messages in the logger.
         @return empty (bool): .
        """
        pass
    
    ##  Adds debug message to the logger.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## <param name="message"> (str) </param>
    @overload
    def LogMessage(message: str) -> None:
        """
         Adds debug message to the logger.
        """
        pass
    
    ##  Adds required type of message to the logger.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## <param name="message"> (str) </param>
    ## <param name="messageType"> (@link AutomationLogger.MessageType NXOpen.Report.AutomationLogger.MessageType@endlink) </param>
    @overload
    def LogMessage(message: str, messageType: AutomationLogger.MessageType) -> None:
        """
         Adds required type of message to the logger.
        """
        pass
    
    ##  Saves the messages in the logger to a file. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## <param name="logFileName"> (str) </param>
    def SaveLog(logFileName: str) -> None:
        """
         Saves the messages in the logger to a file. 
        """
        pass
    
import NXOpen
import NXOpen.Assemblies
##  Represents an abstract command argument.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class BaseArgument(NXOpen.TaggedObject): 
    """ Represents an abstract command argument. """


    ##  Represents the argument type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Integer</term><description> 
    ##  Argument for integer data </description> </item><item><term> 
    ## Double</term><description> 
    ##  Argument for double data </description> </item><item><term> 
    ## String</term><description> 
    ##  Argument for string data </description> </item><item><term> 
    ## Enumeration</term><description> 
    ##  Argument for enumeration data </description> </item></list>
    class Type(Enum):
        """
        Members Include: <Integer> <Double> <String> <Enumeration>
        """
        Integer: int
        Double: int
        String: int
        Enumeration: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> BaseArgument.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) DisplayName
    ##  Returns the argument display name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return str
    @property
    def DisplayName(self) -> str:
        """
        Getter for property: (str) DisplayName
         Returns the argument display name   
            
         
        """
        pass
    
    ## Setter for property: (str) DisplayName

    ##  Returns the argument display name   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @DisplayName.setter
    def DisplayName(self, displayName: str):
        """
        Setter for property: (str) DisplayName
         Returns the argument display name   
            
         
        """
        pass
    
    ## Getter for property: (str) Hint
    ##  Returns the argument hint.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return str
    @property
    def Hint(self) -> str:
        """
        Getter for property: (str) Hint
         Returns the argument hint.  
             
         
        """
        pass
    
    ## Setter for property: (str) Hint

    ##  Returns the argument hint.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @Hint.setter
    def Hint(self, argumentHint: str):
        """
        Setter for property: (str) Hint
         Returns the argument hint.  
             
         
        """
        pass
    
    ## Getter for property: (bool) IsOccurrence
    ##  Returns whether this object is an occurrence or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @return bool
    @property
    def IsOccurrence(self) -> bool:
        """
        Getter for property: (bool) IsOccurrence
         Returns whether this object is an occurrence or not.  
             
         
        """
        pass
    
    ## Getter for property: (str) JournalIdentifier
    ##  Returns the identifier that would be recorded in a journal for this object.  
    ##    
    ##     This may not be the same across different releases of the software.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @return str
    @property
    def JournalIdentifier(self) -> str:
        """
        Getter for property: (str) JournalIdentifier
         Returns the identifier that would be recorded in a journal for this object.  
           
            This may not be the same across different releases of the software.   
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the custom name of the object.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the custom name of the object.  
              
         
        """
        pass
    
    ## Getter for property: (bool) Optional
    ##  Returns  @brief  a value that indicates whether this argument is optional or not.  
    ##     
    ## 
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def Optional(self) -> bool:
        """
        Getter for property: (bool) Optional
         Returns  @brief  a value that indicates whether this argument is optional or not.  
            
        
            
         
        """
        pass
    
    ## Setter for property: (bool) Optional

    ##  Returns  @brief  a value that indicates whether this argument is optional or not.  
    ##     
    ## 
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @Optional.setter
    def Optional(self, isOptional: bool):
        """
        Setter for property: (bool) Optional
         Returns  @brief  a value that indicates whether this argument is optional or not.  
            
        
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink) OwningComponent
    ##  Returns the owning component, if this object is an occurrence.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @return NXOpen.Assemblies.Component
    @property
    def OwningComponent(self) -> NXOpen.Assemblies.Component:
        """
        Getter for property: (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink) OwningComponent
         Returns the owning component, if this object is an occurrence.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.BasePart NXOpen.BasePart@endlink) OwningPart
    ##  Returns the owning part of this object   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @return NXOpen.BasePart
    @property
    def OwningPart(self) -> NXOpen.BasePart:
        """
        Getter for property: (@link NXOpen.BasePart NXOpen.BasePart@endlink) OwningPart
         Returns the owning part of this object   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.INXObject NXOpen.INXObject@endlink) Prototype
    ##  Returns the prototype of this object if it is an occurrence.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @return NXOpen.INXObject
    @property
    def Prototype(self) -> NXOpen.INXObject:
        """
        Getter for property: (@link NXOpen.INXObject NXOpen.INXObject@endlink) Prototype
         Returns the prototype of this object if it is an occurrence.  
             
         
        """
        pass
    
import NXOpen
##  Represents an abstract report item.   <br> Not support KF.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class BaseItem(NXOpen.NXObject): 
    """ Represents an abstract report item.  """


    ## Getter for property: (str) DisplayName
    ##  Returns the item display name.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return str
    @property
    def DisplayName(self) -> str:
        """
        Getter for property: (str) DisplayName
         Returns the item display name.  
             
         
        """
        pass
    
    ## Getter for property: (str) Hint
    ##  Returns the item hint.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return str
    @property
    def Hint(self) -> str:
        """
        Getter for property: (str) Hint
         Returns the item hint.  
             
         
        """
        pass
    
    ##  Clears the content in this class. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def Clear(self) -> None:
        """
         Clears the content in this class. 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Report::CommandBuilder NXOpen::Report::CommandBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::Report::CommandManager::CreateCommandBuilder  NXOpen::Report::CommandManager::CreateCommandBuilder @endlink  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class CommandBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Report.CommandBuilder</ja_class>. """


    ##  Represents the user input location in command. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## BeforeAutomation</term><description> 
    ##  The user item before automation </description> </item><item><term> 
    ## AfterAutomation</term><description> 
    ##  The user item after automation </description> </item></list>
    class UserInputLocation(Enum):
        """
        Members Include: <BeforeAutomation> <AfterAutomation>
        """
        BeforeAutomation: int
        AfterAutomation: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CommandBuilder.UserInputLocation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) Active
    ##  Returns  @brief  a value that indicates whether the command is active or not.  
    ##     
    ## 
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def Active(self) -> bool:
        """
        Getter for property: (bool) Active
         Returns  @brief  a value that indicates whether the command is active or not.  
            
        
            
         
        """
        pass
    
    ## Setter for property: (bool) Active

    ##  Returns  @brief  a value that indicates whether the command is active or not.  
    ##     
    ## 
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @Active.setter
    def Active(self, isActive: bool):
        """
        Setter for property: (bool) Active
         Returns  @brief  a value that indicates whether the command is active or not.  
            
        
            
         
        """
        pass
    
    ## Getter for property: (str) Alias
    ##  Returns the command alias name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def Alias(self) -> str:
        """
        Getter for property: (str) Alias
         Returns the command alias name   
            
         
        """
        pass
    
    ## Setter for property: (str) Alias

    ##  Returns the command alias name   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Alias.setter
    def Alias(self, aliasName: str):
        """
        Setter for property: (str) Alias
         Returns the command alias name   
            
         
        """
        pass
    
    ## Getter for property: (str) DisplayName
    ##  Returns the command display name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return str
    @property
    def DisplayName(self) -> str:
        """
        Getter for property: (str) DisplayName
         Returns the command display name   
            
         
        """
        pass
    
    ## Setter for property: (str) DisplayName

    ##  Returns the command display name   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @DisplayName.setter
    def DisplayName(self, displayName: str):
        """
        Setter for property: (str) DisplayName
         Returns the command display name   
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the command name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the command name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the command name   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @Name.setter
    def Name(self, commandName: str):
        """
        Setter for property: (str) Name
         Returns the command name   
            
         
        """
        pass
    
    ## Getter for property: (@link ProgramInformation NXOpen.Report.ProgramInformation@endlink) ProgramInformation
    ##  Returns the automation program information object.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return ProgramInformation
    @property
    def ProgramInformation(self) -> ProgramInformation:
        """
        Getter for property: (@link ProgramInformation NXOpen.Report.ProgramInformation@endlink) ProgramInformation
         Returns the automation program information object.  
             
         
        """
        pass
    
    ##  Adds an argument and adds it to the command. 
    ##  @return pArgument (@link BaseArgument NXOpen.Report.BaseArgument@endlink):   .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="argumentType"> (@link BaseArgument.Type NXOpen.Report.BaseArgument.Type@endlink)   </param>
    def AddArgument(self, argumentType: BaseArgument.Type) -> BaseArgument:
        """
         Adds an argument and adds it to the command. 
         @return pArgument (@link BaseArgument NXOpen.Report.BaseArgument@endlink):   .
        """
        pass
    
    ##  Adds an user input and adds it to command. 
    ##  @return pUserInput (@link UserInput NXOpen.Report.UserInput@endlink):   .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="userInputLocation"> (@link CommandBuilder.UserInputLocation NXOpen.Report.CommandBuilder.UserInputLocation@endlink)   </param>
    ## <param name="userInputType"> (@link UserInput.Type NXOpen.Report.UserInput.Type@endlink)   </param>
    def AddUserInput(self, userInputLocation: CommandBuilder.UserInputLocation, userInputType: UserInput.Type) -> UserInput:
        """
         Adds an user input and adds it to command. 
         @return pUserInput (@link UserInput NXOpen.Report.UserInput@endlink):   .
        """
        pass
    
    ##  Gets all arguments in the command. 
    ##  @return pArguments (@link BaseArgument List[NXOpen.Report.BaseArgument]@endlink):   .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetArguments(self) -> List[BaseArgument]:
        """
         Gets all arguments in the command. 
         @return pArguments (@link BaseArgument List[NXOpen.Report.BaseArgument]@endlink):   .
        """
        pass
    
    ##  Gets the command hint 
    ##  @return commandHint (List[str]): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetHint(self) -> List[str]:
        """
         Gets the command hint 
         @return commandHint (List[str]): .
        """
        pass
    
    ##  Gets the categories which command apply to. 
    ##  @return pNamespaces (List[str]): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetNamespaces(self) -> List[str]:
        """
         Gets the categories which command apply to. 
         @return pNamespaces (List[str]): .
        """
        pass
    
    ##  Gets all user inputs. 
    ##  @return pUserInputs (@link UserInput List[NXOpen.Report.UserInput]@endlink):   .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="userInputLocation"> (@link CommandBuilder.UserInputLocation NXOpen.Report.CommandBuilder.UserInputLocation@endlink)   </param>
    def GetUserInputs(self, userInputLocation: CommandBuilder.UserInputLocation) -> List[UserInput]:
        """
         Gets all user inputs. 
         @return pUserInputs (@link UserInput List[NXOpen.Report.UserInput]@endlink):   .
        """
        pass
    
    ##  Moves the user inputs to the new position. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="userInputLocation"> (@link CommandBuilder.UserInputLocation NXOpen.Report.CommandBuilder.UserInputLocation@endlink) </param>
    ## <param name="pUserInputs"> (@link UserInput List[NXOpen.Report.UserInput]@endlink) </param>
    ## <param name="isBeforeRefUserInput"> (bool) </param>
    ## <param name="pRefUserInputs"> (@link UserInput NXOpen.Report.UserInput@endlink)  the target reference user input </param>
    def MoveUserInputs(self, userInputLocation: CommandBuilder.UserInputLocation, pUserInputs: List[UserInput], isBeforeRefUserInput: bool, pRefUserInputs: UserInput) -> None:
        """
         Moves the user inputs to the new position. 
        """
        pass
    
    ##  Removes the arguments. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="pArguments"> (@link BaseArgument List[NXOpen.Report.BaseArgument]@endlink)   </param>
    def RemoveArguments(self, pArguments: List[BaseArgument]) -> None:
        """
         Removes the arguments. 
        """
        pass
    
    ##  Removes the user inputs. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="userInputLocation"> (@link CommandBuilder.UserInputLocation NXOpen.Report.CommandBuilder.UserInputLocation@endlink) </param>
    ## <param name="pUserInputs"> (@link UserInput List[NXOpen.Report.UserInput]@endlink) </param>
    def RemoveUserInputs(self, userInputLocation: CommandBuilder.UserInputLocation, pUserInputs: List[UserInput]) -> None:
        """
         Removes the user inputs. 
        """
        pass
    
    ##  Sets the command hint 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="commandHint"> (List[str]) </param>
    def SetHint(self, commandHint: List[str]) -> None:
        """
         Sets the command hint 
        """
        pass
    
    ##  Sets the categories which command apply to. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="pNamespaces"> (List[str]) </param>
    def SetNamespaces(self, pNamespaces: List[str]) -> None:
        """
         Sets the categories which command apply to. 
        """
        pass
    
import NXOpen
##  Represents a command importer to import the commands into command libary. 
## 
##   <br>  Created in NX11.0.0  <br> 

class CommandImporter(NXOpen.TransientObject): 
    """ Represents a command importer to import the commands into command libary. """


    ##  Represents the override option when there is already a command existing. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Ignore</term><description> 
    ##  No action, do not import to library </description> </item><item><term> 
    ## Replace</term><description> 
    ##  Import to replace the existing one  </description> </item><item><term> 
    ## Copy</term><description> 
    ##  Import and append a new one </description> </item></list>
    class OverrideOption(Enum):
        """
        Members Include: <Ignore> <Replace> <Copy>
        """
        Ignore: int
        Replace: int
        Copy: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CommandImporter.OverrideOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link CommandImporter.OverrideOption NXOpen.Report.CommandImporter.OverrideOption@endlink) ImportOption
    ##  Returns the command override option.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return CommandImporter.OverrideOption
    @property
    def ImportOption(self) -> CommandImporter.OverrideOption:
        """
        Getter for property: (@link CommandImporter.OverrideOption NXOpen.Report.CommandImporter.OverrideOption@endlink) ImportOption
         Returns the command override option.  
             
         
        """
        pass
    
    ## Setter for property: (@link CommandImporter.OverrideOption NXOpen.Report.CommandImporter.OverrideOption@endlink) ImportOption

    ##  Returns the command override option.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @ImportOption.setter
    def ImportOption(self, importOption: CommandImporter.OverrideOption):
        """
        Setter for property: (@link CommandImporter.OverrideOption NXOpen.Report.CommandImporter.OverrideOption@endlink) ImportOption
         Returns the command override option.  
             
         
        """
        pass
    
    ##  Destroys the object 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Destroys the object 
        """
        pass
    
    ##  Gets all candidate commands in library file. 
    ##  @return pCommands (@link Command List[NXOpen.Report.Command]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetImportCandidates(self) -> List[Command]:
        """
         Gets all candidate commands in library file. 
         @return pCommands (@link Command List[NXOpen.Report.Command]@endlink): .
        """
        pass
    
    ##  Imports the selected commands into command library. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="pCommandIndexes"> (List[int]) </param>
    def ImportCommands(self, pCommandIndexes: List[int]) -> None:
        """
         Imports the selected commands into command library. 
        """
        pass
    
import NXOpen
import NXOpen.Assemblies
##  Represents a command library in the command manager. <br> Not support KF.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class CommandLibrary(NXOpen.TaggedObject): 
    """ Represents a command library in the command manager."""


    ##  Represents the moving command location. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Before</term><description> 
    ##  Move commands ahead of a referenced command </description> </item><item><term> 
    ## After</term><description> 
    ##  Move commands behind a referenced command </description> </item></list>
    class MoveCommandLocation(Enum):
        """
        Members Include: <Before> <After>
        """
        Before: int
        After: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CommandLibrary.MoveCommandLocation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) IsOccurrence
    ##  Returns whether this object is an occurrence or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @return bool
    @property
    def IsOccurrence(self) -> bool:
        """
        Getter for property: (bool) IsOccurrence
         Returns whether this object is an occurrence or not.  
             
         
        """
        pass
    
    ## Getter for property: (str) JournalIdentifier
    ##  Returns the identifier that would be recorded in a journal for this object.  
    ##    
    ##     This may not be the same across different releases of the software.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @return str
    @property
    def JournalIdentifier(self) -> str:
        """
        Getter for property: (str) JournalIdentifier
         Returns the identifier that would be recorded in a journal for this object.  
           
            This may not be the same across different releases of the software.   
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the custom name of the object.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the custom name of the object.  
              
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink) OwningComponent
    ##  Returns the owning component, if this object is an occurrence.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @return NXOpen.Assemblies.Component
    @property
    def OwningComponent(self) -> NXOpen.Assemblies.Component:
        """
        Getter for property: (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink) OwningComponent
         Returns the owning component, if this object is an occurrence.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.BasePart NXOpen.BasePart@endlink) OwningPart
    ##  Returns the owning part of this object   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @return NXOpen.BasePart
    @property
    def OwningPart(self) -> NXOpen.BasePart:
        """
        Getter for property: (@link NXOpen.BasePart NXOpen.BasePart@endlink) OwningPart
         Returns the owning part of this object   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.INXObject NXOpen.INXObject@endlink) Prototype
    ##  Returns the prototype of this object if it is an occurrence.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @return NXOpen.INXObject
    @property
    def Prototype(self) -> NXOpen.INXObject:
        """
        Getter for property: (@link NXOpen.INXObject NXOpen.INXObject@endlink) Prototype
         Returns the prototype of this object if it is an occurrence.  
             
         
        """
        pass
    
    ##  Gets all commands in command library. 
    ##  @return pCommands (@link Command List[NXOpen.Report.Command]@endlink):   .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetCommands(self) -> List[Command]:
        """
         Gets all commands in command library. 
         @return pCommands (@link Command List[NXOpen.Report.Command]@endlink):   .
        """
        pass
    
    ##  Moves the commands to the new position. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="pCommand"> (@link Command List[NXOpen.Report.Command]@endlink)   </param>
    ## <param name="newLocation"> (@link CommandLibrary.MoveCommandLocation NXOpen.Report.CommandLibrary.MoveCommandLocation@endlink)   </param>
    ## <param name="pReferenceCommand"> (@link Command NXOpen.Report.Command@endlink)   </param>
    def MoveCommands(self, pCommand: List[Command], newLocation: CommandLibrary.MoveCommandLocation, pReferenceCommand: Command) -> None:
        """
         Moves the commands to the new position. 
        """
        pass
    
    ##  Saves all commands to their binding xml file. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def Save(self) -> None:
        """
         Saves all commands to their binding xml file. 
        """
        pass
    
import NXOpen
##  Represents the command manager.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class CommandManager(NXOpen.Object): 
    """ Represents the command manager. """


    ##  Creates the command builder. 
    ##  @return builder (@link CommandBuilder NXOpen.Report.CommandBuilder@endlink):   .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## <param name="commandLibrary"> (@link CommandLibrary NXOpen.Report.CommandLibrary@endlink)   </param>
    ## <param name="command"> (@link Command NXOpen.Report.Command@endlink)   </param>
    def CreateCommandBuilder(commandLibrary: CommandLibrary, command: Command) -> CommandBuilder:
        """
         Creates the command builder. 
         @return builder (@link CommandBuilder NXOpen.Report.CommandBuilder@endlink):   .
        """
        pass
    
    ##  Export selected commands to a library folder zip file. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## <param name="pCommands"> (@link Command List[NXOpen.Report.Command]@endlink) </param>
    ## <param name="libraryFile"> (str)  Library folder zip file name with full path </param>
    def ExportCommandsToLibraryFile(pCommands: List[Command], libraryFile: str) -> None:
        """
         Export selected commands to a library folder zip file. 
        """
        pass
    
    ##  Finds the @link TaggedObject TaggedObject@endlink  with the given identifier as recorded in a journal. 
    ##  @return foundObject (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink):  Object found, or null if no such object exists .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## <param name="journalIdentifier"> (str)  Identifier of the @link TaggedObject TaggedObject@endlink  to be found </param>
    def Find(journalIdentifier: str) -> NXOpen.TaggedObject:
        """
         Finds the @link TaggedObject TaggedObject@endlink  with the given identifier as recorded in a journal. 
         @return foundObject (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink):  Object found, or null if no such object exists .
        """
        pass
    
    ##  Gets all command libraries. 
    ##  @return pCommandLibraries (@link CommandLibrary List[NXOpen.Report.CommandLibrary]@endlink):   .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetCommandLibraries() -> List[CommandLibrary]:
        """
         Gets all command libraries. 
         @return pCommandLibraries (@link CommandLibrary List[NXOpen.Report.CommandLibrary]@endlink):   .
        """
        pass
    
    ##  Creates a transient object @link  NXOpen::Report::CommandImporter   NXOpen::Report::CommandImporter @endlink  to import
    ##             the selected commands of a command library file to a command library. The object
    ##             should be destroyed after finishing import. 
    ##  @return pCommandImporter (@link CommandImporter NXOpen.Report.CommandImporter@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## <param name="pCommandLibrary"> (@link CommandLibrary NXOpen.Report.CommandLibrary@endlink) </param>
    ## <param name="libraryFile"> (str)   Library folder zip file name with full path </param>
    def NewCommandImporter(pCommandLibrary: CommandLibrary, libraryFile: str) -> CommandImporter:
        """
         Creates a transient object @link  NXOpen::Report::CommandImporter   NXOpen::Report::CommandImporter @endlink  to import
                    the selected commands of a command library file to a command library. The object
                    should be destroyed after finishing import. 
         @return pCommandImporter (@link CommandImporter NXOpen.Report.CommandImporter@endlink): .
        """
        pass
    
import NXOpen
##  Represents a command in command library.  <br> To create or edit an instance of this class, use @link NXOpen::Report::CommandBuilder  NXOpen::Report::CommandBuilder @endlink  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class Command(NXOpen.NXObject): 
    """ Represents a command in command library. """


    ##  Deletes the command. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def Delete(self) -> None:
        """
         Deletes the command. 
        """
        pass
    
##  Represents an argument for double type data. This class
##         does not include upper bound and lower bound in default.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class DoubleArgument(BaseArgument): 
    """ Represents an argument for double type data. This class
        does not include upper bound and lower bound in default. """


    ## Getter for property: (float) DefaultValue
    ##  Returns the arguement dafault value.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return float
    @property
    def DefaultValue(self) -> float:
        """
        Getter for property: (float) DefaultValue
         Returns the arguement dafault value.  
             
         
        """
        pass
    
    ## Setter for property: (float) DefaultValue

    ##  Returns the arguement dafault value.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @DefaultValue.setter
    def DefaultValue(self, argumentValue: float):
        """
        Setter for property: (float) DefaultValue
         Returns the arguement dafault value.  
             
         
        """
        pass
    
    ## Getter for property: (bool) IncludeLowerBound
    ##  Returns  @brief  a value that indicates whether includes the lower bound.  
    ##     
    ## 
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def IncludeLowerBound(self) -> bool:
        """
        Getter for property: (bool) IncludeLowerBound
         Returns  @brief  a value that indicates whether includes the lower bound.  
            
        
            
         
        """
        pass
    
    ## Setter for property: (bool) IncludeLowerBound

    ##  Returns  @brief  a value that indicates whether includes the lower bound.  
    ##     
    ## 
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @IncludeLowerBound.setter
    def IncludeLowerBound(self, includeLowerBound: bool):
        """
        Setter for property: (bool) IncludeLowerBound
         Returns  @brief  a value that indicates whether includes the lower bound.  
            
        
            
         
        """
        pass
    
    ## Getter for property: (bool) IncludeUpperBound
    ##  Returns  @brief  a value that indicates whether includes the upper bound.  
    ##     
    ## 
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def IncludeUpperBound(self) -> bool:
        """
        Getter for property: (bool) IncludeUpperBound
         Returns  @brief  a value that indicates whether includes the upper bound.  
            
        
            
         
        """
        pass
    
    ## Setter for property: (bool) IncludeUpperBound

    ##  Returns  @brief  a value that indicates whether includes the upper bound.  
    ##     
    ## 
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @IncludeUpperBound.setter
    def IncludeUpperBound(self, includeUpperBound: bool):
        """
        Setter for property: (bool) IncludeUpperBound
         Returns  @brief  a value that indicates whether includes the upper bound.  
            
        
            
         
        """
        pass
    
    ## Getter for property: (float) MaximumValue
    ##  Returns the maximum value.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return float
    @property
    def MaximumValue(self) -> float:
        """
        Getter for property: (float) MaximumValue
         Returns the maximum value.  
             
         
        """
        pass
    
    ## Setter for property: (float) MaximumValue

    ##  Returns the maximum value.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @MaximumValue.setter
    def MaximumValue(self, maximumValue: float):
        """
        Setter for property: (float) MaximumValue
         Returns the maximum value.  
             
         
        """
        pass
    
    ## Getter for property: (float) MimimumValue
    ##  Returns the minimum value.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return float
    @property
    def MimimumValue(self) -> float:
        """
        Getter for property: (float) MimimumValue
         Returns the minimum value.  
             
         
        """
        pass
    
    ## Setter for property: (float) MimimumValue

    ##  Returns the minimum value.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @MimimumValue.setter
    def MimimumValue(self, minimumValue: float):
        """
        Setter for property: (float) MimimumValue
         Returns the minimum value.  
             
         
        """
        pass
    
##  Represents an argument for enumeration type data.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class EnumerationArgument(BaseArgument): 
    """ Represents an argument for enumeration type data. """


    ## Getter for property: (int) DefaultValue
    ##  Returns the argument default value.  
    ##    The default value index is between 0 and options count queried
    ##             by @link NXOpen::Report::EnumerationArgument::GetEnumerationOptions NXOpen::Report::EnumerationArgument::GetEnumerationOptions@endlink , 0 is inclusive.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return int
    @property
    def DefaultValue(self) -> int:
        """
        Getter for property: (int) DefaultValue
         Returns the argument default value.  
           The default value index is between 0 and options count queried
                    by @link NXOpen::Report::EnumerationArgument::GetEnumerationOptions NXOpen::Report::EnumerationArgument::GetEnumerationOptions@endlink , 0 is inclusive.   
         
        """
        pass
    
    ## Setter for property: (int) DefaultValue

    ##  Returns the argument default value.  
    ##    The default value index is between 0 and options count queried
    ##             by @link NXOpen::Report::EnumerationArgument::GetEnumerationOptions NXOpen::Report::EnumerationArgument::GetEnumerationOptions@endlink , 0 is inclusive.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @DefaultValue.setter
    def DefaultValue(self, defaultValueIndex: int):
        """
        Setter for property: (int) DefaultValue
         Returns the argument default value.  
           The default value index is between 0 and options count queried
                    by @link NXOpen::Report::EnumerationArgument::GetEnumerationOptions NXOpen::Report::EnumerationArgument::GetEnumerationOptions@endlink , 0 is inclusive.   
         
        """
        pass
    
    ##  Gets the enumeration options. 
    ##  @return enumerationOptions (List[str]):   .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetEnumerationOptions(self) -> List[str]:
        """
         Gets the enumeration options. 
         @return enumerationOptions (List[str]):   .
        """
        pass
    
    ##  Sets the enumeration options. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="enumerationOptions"> (List[str])   </param>
    def SetEnumerationOptions(self, enumerationOptions: List[str]) -> None:
        """
         Sets the enumeration options. 
        """
        pass
    
import NXOpen
##  Represents an image option object.  
## 
##   <br>  Created in NX11.0.0  <br> 

class ImageOption(NXOpen.TaggedObject): 
    """ Represents an image option object.  """


    ## Getter for property: (float) ImageHeight
    ##  Returns the image height .  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return float
    @property
    def ImageHeight(self) -> float:
        """
        Getter for property: (float) ImageHeight
         Returns the image height .  
             
         
        """
        pass
    
    ## Setter for property: (float) ImageHeight

    ##  Returns the image height .  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @ImageHeight.setter
    def ImageHeight(self, imageHeight: float):
        """
        Setter for property: (float) ImageHeight
         Returns the image height .  
             
         
        """
        pass
    
    ## Getter for property: (float) ImageRotation
    ##  Returns the image rotation angle in degree.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return float
    @property
    def ImageRotation(self) -> float:
        """
        Getter for property: (float) ImageRotation
         Returns the image rotation angle in degree.  
             
         
        """
        pass
    
    ## Setter for property: (float) ImageRotation

    ##  Returns the image rotation angle in degree.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @ImageRotation.setter
    def ImageRotation(self, imageRotation: float):
        """
        Setter for property: (float) ImageRotation
         Returns the image rotation angle in degree.  
             
         
        """
        pass
    
    ## Getter for property: (float) ImageWidth
    ##  Returns the image width .  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return float
    @property
    def ImageWidth(self) -> float:
        """
        Getter for property: (float) ImageWidth
         Returns the image width .  
             
         
        """
        pass
    
    ## Setter for property: (float) ImageWidth

    ##  Returns the image width .  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @ImageWidth.setter
    def ImageWidth(self, imageWidth: float):
        """
        Setter for property: (float) ImageWidth
         Returns the image width .  
             
         
        """
        pass
    
    ## Getter for property: (bool) LockOriginalAspectRatio
    ##  Returns  @brief  a value that indicates whether locks original image aspect ratio.  
    ##    If locks ratio, the image
    ##             width will be updated according to the ratio when image height changes , and vice versa. 
    ## 
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def LockOriginalAspectRatio(self) -> bool:
        """
        Getter for property: (bool) LockOriginalAspectRatio
         Returns  @brief  a value that indicates whether locks original image aspect ratio.  
           If locks ratio, the image
                    width will be updated according to the ratio when image height changes , and vice versa. 
        
            
         
        """
        pass
    
    ## Setter for property: (bool) LockOriginalAspectRatio

    ##  Returns  @brief  a value that indicates whether locks original image aspect ratio.  
    ##    If locks ratio, the image
    ##             width will be updated according to the ratio when image height changes , and vice versa. 
    ## 
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @LockOriginalAspectRatio.setter
    def LockOriginalAspectRatio(self, lockRatio: bool):
        """
        Setter for property: (bool) LockOriginalAspectRatio
         Returns  @brief  a value that indicates whether locks original image aspect ratio.  
           If locks ratio, the image
                    width will be updated according to the ratio when image height changes , and vice versa. 
        
            
         
        """
        pass
    
##  Represents a images group item.   <br> Not support KF.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class ImagesGroupItem(BaseItem): 
    """ Represents a images group item.  """


    ##  Copy a @link NXOpen::Report::ReportImage NXOpen::Report::ReportImage@endlink  to the this class. 
    ##  @return pReportImageCopy (@link ReportImage NXOpen.Report.ReportImage@endlink):  copy of the input image .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="pReportImage"> (@link ReportImage NXOpen.Report.ReportImage@endlink)  input image </param>
    def CopyImage(self, pReportImage: ReportImage) -> ReportImage:
        """
         Copy a @link NXOpen::Report::ReportImage NXOpen::Report::ReportImage@endlink  to the this class. 
         @return pReportImageCopy (@link ReportImage NXOpen.Report.ReportImage@endlink):  copy of the input image .
        """
        pass
    
    ##  Creates an image in images group. 
    ##  @return pReportImage (@link ReportImage NXOpen.Report.ReportImage@endlink):   .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="imageFile"> (str) </param>
    ## <param name="displayName"> (str) </param>
    def CreateImage(self, imageFile: str, displayName: str) -> ReportImage:
        """
         Creates an image in images group. 
         @return pReportImage (@link ReportImage NXOpen.Report.ReportImage@endlink):   .
        """
        pass
    
    ##  Deletes all images in class. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def DeleteImages(self) -> None:
        """
         Deletes all images in class. 
        """
        pass
    
    ##  Gets all images in images group. 
    ##  @return pReportImages (@link ReportImage List[NXOpen.Report.ReportImage]@endlink):   .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetImages(self) -> List[ReportImage]:
        """
         Gets all images in images group. 
         @return pReportImages (@link ReportImage List[NXOpen.Report.ReportImage]@endlink):   .
        """
        pass
    
    ##  Moves the images to the new position. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="pReportImages"> (@link ReportImage List[NXOpen.Report.ReportImage]@endlink)   </param>
    ## <param name="newLocation"> (@link Report.MoveItemLocation NXOpen.Report.Report.MoveItemLocation@endlink)   </param>
    ## <param name="pReferencedImage"> (@link ReportImage NXOpen.Report.ReportImage@endlink)   </param>
    def MoveImages(self, pReportImages: List[ReportImage], newLocation: Report.MoveItemLocation, pReferencedImage: ReportImage) -> None:
        """
         Moves the images to the new position. 
        """
        pass
    
##  Represents an argument for integer type data. This class
##         does not include upper bound and lower bound in default.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class IntegerArgument(BaseArgument): 
    """ Represents an argument for integer type data. This class
        does not include upper bound and lower bound in default. """


    ## Getter for property: (int) DefaultValue
    ##  Returns the argument default value.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return int
    @property
    def DefaultValue(self) -> int:
        """
        Getter for property: (int) DefaultValue
         Returns the argument default value.  
             
         
        """
        pass
    
    ## Setter for property: (int) DefaultValue

    ##  Returns the argument default value.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @DefaultValue.setter
    def DefaultValue(self, defaultValue: int):
        """
        Setter for property: (int) DefaultValue
         Returns the argument default value.  
             
         
        """
        pass
    
    ## Getter for property: (bool) IncludeLowerBound
    ##  Returns  @brief  a value that indicates whether includes the lower bound.  
    ##     
    ## 
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def IncludeLowerBound(self) -> bool:
        """
        Getter for property: (bool) IncludeLowerBound
         Returns  @brief  a value that indicates whether includes the lower bound.  
            
        
            
         
        """
        pass
    
    ## Setter for property: (bool) IncludeLowerBound

    ##  Returns  @brief  a value that indicates whether includes the lower bound.  
    ##     
    ## 
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @IncludeLowerBound.setter
    def IncludeLowerBound(self, includeLowerBound: bool):
        """
        Setter for property: (bool) IncludeLowerBound
         Returns  @brief  a value that indicates whether includes the lower bound.  
            
        
            
         
        """
        pass
    
    ## Getter for property: (bool) IncludeUpperBound
    ##  Returns  @brief  a value that indicates whether includes the upper bound.  
    ##     
    ## 
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def IncludeUpperBound(self) -> bool:
        """
        Getter for property: (bool) IncludeUpperBound
         Returns  @brief  a value that indicates whether includes the upper bound.  
            
        
            
         
        """
        pass
    
    ## Setter for property: (bool) IncludeUpperBound

    ##  Returns  @brief  a value that indicates whether includes the upper bound.  
    ##     
    ## 
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @IncludeUpperBound.setter
    def IncludeUpperBound(self, includeUpperBound: bool):
        """
        Setter for property: (bool) IncludeUpperBound
         Returns  @brief  a value that indicates whether includes the upper bound.  
            
        
            
         
        """
        pass
    
    ## Getter for property: (int) MaximumValue
    ##  Returns the maximum value.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return int
    @property
    def MaximumValue(self) -> int:
        """
        Getter for property: (int) MaximumValue
         Returns the maximum value.  
             
         
        """
        pass
    
    ## Setter for property: (int) MaximumValue

    ##  Returns the maximum value.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @MaximumValue.setter
    def MaximumValue(self, maximumValue: int):
        """
        Setter for property: (int) MaximumValue
         Returns the maximum value.  
             
         
        """
        pass
    
    ## Getter for property: (int) MinimumValue
    ##  Returns the minimum value.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return int
    @property
    def MinimumValue(self) -> int:
        """
        Getter for property: (int) MinimumValue
         Returns the minimum value.  
             
         
        """
        pass
    
    ## Setter for property: (int) MinimumValue

    ##  Returns the minimum value.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @MinimumValue.setter
    def MinimumValue(self, minimumValue: int):
        """
        Setter for property: (int) MinimumValue
         Returns the minimum value.  
             
         
        """
        pass
    
import NXOpen
##  This interface is used to manage associated reports @link Report::Report Report::Report@endlink  
## 
##   <br>  Created in NX11.0.0  <br> 

class IReportCollection(NXOpen.INXObject): 
    """ This interface is used to manage associated reports <ja_class>Report.Report</ja_class> """


    ##  Creates a @link Report::Report Report::Report@endlink  in this report collection.
    ##             NX will not create a report if the report name is empty or existed. 
    ##  @return pReport (@link Report NXOpen.Report.Report@endlink):   .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="templateFile"> (str)   Template file name with full path </param>
    ## <param name="reportName"> (str)   Report name </param>
    ## <param name="listError"> (bool)  list error information in listing window </param>
    @abstractmethod
    def CreateReport(self, templateFile: str, reportName: str, listError: bool) -> Report:
        """
         Creates a @link Report::Report Report::Report@endlink  in this report collection.
                    NX will not create a report if the report name is empty or existed. 
         @return pReport (@link Report NXOpen.Report.Report@endlink):   .
        """
        pass
    
    ##  Gets all reports in the report collection. 
    ##  @return pReports (@link Report List[NXOpen.Report.Report]@endlink):   .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    @abstractmethod
    def GetReports(self) -> List[Report]:
        """
         Gets all reports in the report collection. 
         @return pReports (@link Report List[NXOpen.Report.Report]@endlink):   .
        """
        pass
    
import NXOpen
##  Represents an user defined report item. 
## 
##   <br>  Created in NX11.0.0  <br> 

class IUserItem(NXOpen.INXObject): 
    """ Represents an user defined report item. """


    ##  Sets the display name. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="displayName"> (str)   </param>
    @abstractmethod
    def SetDisplayName(self, displayName: str) -> None:
        """
         Sets the display name. 
        """
        pass
    
import NXOpen
import NXOpen.Assemblies
##  Represents the program information for command automation. 
## 
##   <br>  Created in NX11.0.0  <br> 

class ProgramInformation(NXOpen.TaggedObject): 
    """ Represents the program information for command automation. """


    ##  Represents the automation program. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ##  None language </description> </item><item><term> 
    ## CPlusplus</term><description> 
    ##  C plus plus language </description> </item><item><term> 
    ## CSharp</term><description> 
    ##  C sharp language  </description> </item><item><term> 
    ## Vb</term><description> 
    ##  Visual basic language  </description> </item><item><term> 
    ## Java</term><description> 
    ##  Java language  </description> </item><item><term> 
    ## Python</term><description> 
    ##  Python language  </description> </item></list>
    class LanguageType(Enum):
        """
        Members Include: <NotSet> <CPlusplus> <CSharp> <Vb> <Java> <Python>
        """
        NotSet: int
        CPlusplus: int
        CSharp: int
        Vb: int
        Java: int
        Python: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ProgramInformation.LanguageType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) FunctionName
    ##  Returns the program entry function name.  
    ##   
    ##             CPlusplus language: the function name is the exported function following required interface,
    ##             Java language: the function name is the exported java class name,
    ##             CSharp, Vb and Python language: the function name is "Main".   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return str
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
    
    ## Setter for property: (str) FunctionName

    ##  Returns the program entry function name.  
    ##   
    ##             CPlusplus language: the function name is the exported function following required interface,
    ##             Java language: the function name is the exported java class name,
    ##             CSharp, Vb and Python language: the function name is "Main".   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

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
    
    ## Getter for property: (bool) IsOccurrence
    ##  Returns whether this object is an occurrence or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @return bool
    @property
    def IsOccurrence(self) -> bool:
        """
        Getter for property: (bool) IsOccurrence
         Returns whether this object is an occurrence or not.  
             
         
        """
        pass
    
    ## Getter for property: (str) JournalIdentifier
    ##  Returns the identifier that would be recorded in a journal for this object.  
    ##    
    ##     This may not be the same across different releases of the software.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @return str
    @property
    def JournalIdentifier(self) -> str:
        """
        Getter for property: (str) JournalIdentifier
         Returns the identifier that would be recorded in a journal for this object.  
           
            This may not be the same across different releases of the software.   
         
        """
        pass
    
    ## Getter for property: (@link ProgramInformation.LanguageType NXOpen.Report.ProgramInformation.LanguageType@endlink) Language
    ##  Returns the automation program language.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return ProgramInformation.LanguageType
    @property
    def Language(self) -> ProgramInformation.LanguageType:
        """
        Getter for property: (@link ProgramInformation.LanguageType NXOpen.Report.ProgramInformation.LanguageType@endlink) Language
         Returns the automation program language.  
             
         
        """
        pass
    
    ## Setter for property: (@link ProgramInformation.LanguageType NXOpen.Report.ProgramInformation.LanguageType@endlink) Language

    ##  Returns the automation program language.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @Language.setter
    def Language(self, languageType: ProgramInformation.LanguageType):
        """
        Setter for property: (@link ProgramInformation.LanguageType NXOpen.Report.ProgramInformation.LanguageType@endlink) Language
         Returns the automation program language.  
             
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the custom name of the object.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the custom name of the object.  
              
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink) OwningComponent
    ##  Returns the owning component, if this object is an occurrence.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @return NXOpen.Assemblies.Component
    @property
    def OwningComponent(self) -> NXOpen.Assemblies.Component:
        """
        Getter for property: (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink) OwningComponent
         Returns the owning component, if this object is an occurrence.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.BasePart NXOpen.BasePart@endlink) OwningPart
    ##  Returns the owning part of this object   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @return NXOpen.BasePart
    @property
    def OwningPart(self) -> NXOpen.BasePart:
        """
        Getter for property: (@link NXOpen.BasePart NXOpen.BasePart@endlink) OwningPart
         Returns the owning part of this object   
            
         
        """
        pass
    
    ## Getter for property: (str) ProgramFile
    ##  Returns the automation program executer file.  
    ##   
    ##             CPlusplus language: the dll file,
    ##             CSharp language: the CS file or CS dll file,
    ##             Vb language: the VB file or VB dll file,
    ##             Java language: the Jar file,
    ##             Python language: the Py file.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return str
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
    
    ## Setter for property: (str) ProgramFile

    ##  Returns the automation program executer file.  
    ##   
    ##             CPlusplus language: the dll file,
    ##             CSharp language: the CS file or CS dll file,
    ##             Vb language: the VB file or VB dll file,
    ##             Java language: the Jar file,
    ##             Python language: the Py file.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

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
    
    ## Getter for property: (@link NXOpen.INXObject NXOpen.INXObject@endlink) Prototype
    ##  Returns the prototype of this object if it is an occurrence.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @return NXOpen.INXObject
    @property
    def Prototype(self) -> NXOpen.INXObject:
        """
        Getter for property: (@link NXOpen.INXObject NXOpen.INXObject@endlink) Prototype
         Returns the prototype of this object if it is an occurrence.  
             
         
        """
        pass
    
import NXOpen
##  Represents a report image.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class ReportImage(NXOpen.NXObject): 
    """ Represents a report image. """


    ## Getter for property: (str) Caption
    ##  Returns the image caption text.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return str
    @property
    def Caption(self) -> str:
        """
        Getter for property: (str) Caption
         Returns the image caption text.  
             
         
        """
        pass
    
    ## Setter for property: (str) Caption

    ##  Returns the image caption text.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @Caption.setter
    def Caption(self, captionText: str):
        """
        Setter for property: (str) Caption
         Returns the image caption text.  
             
         
        """
        pass
    
    ## Getter for property: (@link ImageOption NXOpen.Report.ImageOption@endlink) ImageOption
    ##  Returns the image option.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return ImageOption
    @property
    def ImageOption(self) -> ImageOption:
        """
        Getter for property: (@link ImageOption NXOpen.Report.ImageOption@endlink) ImageOption
         Returns the image option.  
             
         
        """
        pass
    
    ##  Replaces the old image file with a new image file. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="imageFile"> (str)   </param>
    def SetImage(self, imageFile: str) -> None:
        """
         Replaces the old image file with a new image file. 
        """
        pass
    
import NXOpen
##  Represents the report manager.  <br> To obtain an instance of this class use @link NXOpen::Session::ReportManager NXOpen::Session::ReportManager@endlink .  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class ReportManager(NXOpen.Object): 
    """ Represents the report manager. """


    ## Getter for property: (@link ReportPreference NXOpen.Report.ReportPreference@endlink) Preference
    ##  Returns the report preference.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return ReportPreference
    @property
    def Preference(self) -> ReportPreference:
        """
        Getter for property: (@link ReportPreference NXOpen.Report.ReportPreference@endlink) Preference
         Returns the report preference.  
             
         
        """
        pass
    
    ##  Returns the @link NXOpen::Report::AutomationLogger NXOpen::Report::AutomationLogger@endlink  belonging to the report manager 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @link AutomationLogger NXOpen.Report.AutomationLogger@endlink
    @property
    def AutomationLogger() -> AutomationLogger:
        """
         Returns the @link NXOpen::Report::AutomationLogger NXOpen::Report::AutomationLogger@endlink  belonging to the report manager 
        """
        pass
    
    ##  Returns the @link NXOpen::Report::CommandManager NXOpen::Report::CommandManager@endlink  belonging to the report manager 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @link CommandManager NXOpen.Report.CommandManager@endlink
    @property
    def CommandManager() -> CommandManager:
        """
         Returns the @link NXOpen::Report::CommandManager NXOpen::Report::CommandManager@endlink  belonging to the report manager 
        """
        pass
    
    ##  Creates a new @link NXOpen::Report::ResultXmlFileWriter NXOpen::Report::ResultXmlFileWriter@endlink  object.
    ##  @return writer (@link ResultXmlFileWriter NXOpen.Report.ResultXmlFileWriter@endlink):   .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def CreateResultXmlFileWriter() -> ResultXmlFileWriter:
        """
         Creates a new @link NXOpen::Report::ResultXmlFileWriter NXOpen::Report::ResultXmlFileWriter@endlink  object.
         @return writer (@link ResultXmlFileWriter NXOpen.Report.ResultXmlFileWriter@endlink):   .
        """
        pass
    
    ##  Gets the original dimension of a given image file. 
    ##  @return A tuple consisting of (width, height). 
    ##  - width is: float. .
    ##  - height is: float. .

    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## <param name="imageFullFileName"> (str)  the full image file name </param>
    def GetOriginalImageDimension(imageFullFileName: str) -> Tuple[float, float]:
        """
         Gets the original dimension of a given image file. 
         @return A tuple consisting of (width, height). 
         - width is: float. .
         - height is: float. .

        """
        pass
    
import NXOpen
##  Manages the preference data.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class ReportPreference(NXOpen.TaggedObject): 
    """ Manages the preference data. """


    ## Getter for property: (int) MaximumRecentReportDocumentCount
    ##  Returns the maximum count of the recent report documents which could be viewed   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return int
    @property
    def MaximumRecentReportDocumentCount(self) -> int:
        """
        Getter for property: (int) MaximumRecentReportDocumentCount
         Returns the maximum count of the recent report documents which could be viewed   
            
         
        """
        pass
    
    ## Setter for property: (int) MaximumRecentReportDocumentCount

    ##  Returns the maximum count of the recent report documents which could be viewed   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @MaximumRecentReportDocumentCount.setter
    def MaximumRecentReportDocumentCount(self, maxRecentReportDoc: int):
        """
        Setter for property: (int) MaximumRecentReportDocumentCount
         Returns the maximum count of the recent report documents which could be viewed   
            
         
        """
        pass
    
    ## Getter for property: (bool) OpenReportDocumentAfterExport
    ##  Returns the option indicates whether to open report document after exporting report   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def OpenReportDocumentAfterExport(self) -> bool:
        """
        Getter for property: (bool) OpenReportDocumentAfterExport
         Returns the option indicates whether to open report document after exporting report   
            
         
        """
        pass
    
    ## Setter for property: (bool) OpenReportDocumentAfterExport

    ##  Returns the option indicates whether to open report document after exporting report   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @OpenReportDocumentAfterExport.setter
    def OpenReportDocumentAfterExport(self, openReportAfterExportSetting: bool):
        """
        Setter for property: (bool) OpenReportDocumentAfterExport
         Returns the option indicates whether to open report document after exporting report   
            
         
        """
        pass
    
    ## Getter for property: (bool) SearchTemplateFromSiteDirectory
    ##  Returns the option indicates whether to use site template directory as start to choose a report template file    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def SearchTemplateFromSiteDirectory(self) -> bool:
        """
        Getter for property: (bool) SearchTemplateFromSiteDirectory
         Returns the option indicates whether to use site template directory as start to choose a report template file    
            
         
        """
        pass
    
    ## Setter for property: (bool) SearchTemplateFromSiteDirectory

    ##  Returns the option indicates whether to use site template directory as start to choose a report template file    
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @SearchTemplateFromSiteDirectory.setter
    def SearchTemplateFromSiteDirectory(self, searchTemplateFromSiteDirectorySetting: bool):
        """
        Setter for property: (bool) SearchTemplateFromSiteDirectory
         Returns the option indicates whether to use site template directory as start to choose a report template file    
            
         
        """
        pass
    
    ## Getter for property: (bool) UsePartDirectoryAsDefaultExportLocation
    ##  Returns the option indicates whehter to use part direcotry as default report document location    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def UsePartDirectoryAsDefaultExportLocation(self) -> bool:
        """
        Getter for property: (bool) UsePartDirectoryAsDefaultExportLocation
         Returns the option indicates whehter to use part direcotry as default report document location    
            
         
        """
        pass
    
    ## Setter for property: (bool) UsePartDirectoryAsDefaultExportLocation

    ##  Returns the option indicates whehter to use part direcotry as default report document location    
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @UsePartDirectoryAsDefaultExportLocation.setter
    def UsePartDirectoryAsDefaultExportLocation(self, usePartDirAsDefaultExportLocationSetting: bool):
        """
        Setter for property: (bool) UsePartDirectoryAsDefaultExportLocation
         Returns the option indicates whehter to use part direcotry as default report document location    
            
         
        """
        pass
    
    ## Getter for property: (bool) ViewImageAfterSnapshotting
    ##  Returns the option indicates whether to view image after snopshotting    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def ViewImageAfterSnapshotting(self) -> bool:
        """
        Getter for property: (bool) ViewImageAfterSnapshotting
         Returns the option indicates whether to view image after snopshotting    
            
         
        """
        pass
    
    ## Setter for property: (bool) ViewImageAfterSnapshotting

    ##  Returns the option indicates whether to view image after snopshotting    
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @ViewImageAfterSnapshotting.setter
    def ViewImageAfterSnapshotting(self, viewImageAfterSnapshotSetting: bool):
        """
        Setter for property: (bool) ViewImageAfterSnapshotting
         Returns the option indicates whether to view image after snopshotting    
            
         
        """
        pass
    
    ##  Saves preference settings to memory file 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def SaveMemoryFile(self) -> None:
        """
         Saves preference settings to memory file 
        """
        pass
    
import NXOpen
import NXOpen.OpenXml
##   @brief  Contains methods for adding document data and generating result XML file 
##     for CAE Report.  
## 
##   
## 
##   <br>  Created in NX11.0.0  <br> 

class ResultXmlFileWriter(NXOpen.TransientObject): 
    """ <summary> Contains methods for adding document data and generating result XML file 
    for CAE Report. </summary> """


    ##  Creates a new @link NXOpen::OpenXml::ImageGroupDocumentData NXOpen::OpenXml::ImageGroupDocumentData@endlink  object.
    ##         Does not to free this object, it will be free while deleting 
    ##         @link NXOpen::Report::ResultXmlFileWriter NXOpen::Report::ResultXmlFileWriter@endlink  object
    ##  @return data (@link NXOpen.OpenXml.ImageGroupDocumentData NXOpen.OpenXml.ImageGroupDocumentData@endlink):  the image group data .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def AddImageGroup(self) -> NXOpen.OpenXml.ImageGroupDocumentData:
        """
         Creates a new @link NXOpen::OpenXml::ImageGroupDocumentData NXOpen::OpenXml::ImageGroupDocumentData@endlink  object.
                Does not to free this object, it will be free while deleting 
                @link NXOpen::Report::ResultXmlFileWriter NXOpen::Report::ResultXmlFileWriter@endlink  object
         @return data (@link NXOpen.OpenXml.ImageGroupDocumentData NXOpen.OpenXml.ImageGroupDocumentData@endlink):  the image group data .
        """
        pass
    
    ##  Creates a new @link NXOpen::OpenXml::TableDocumentData NXOpen::OpenXml::TableDocumentData@endlink  object.
    ##         Does not to free this object, it will be free while deleting 
    ##         @link NXOpen::Report::ResultXmlFileWriter NXOpen::Report::ResultXmlFileWriter@endlink  object
    ##  @return data (@link NXOpen.OpenXml.TableDocumentData NXOpen.OpenXml.TableDocumentData@endlink):  the table data .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="columnSize"> (int)  the column size of the table</param>
    ## <param name="rowSize"> (int)  the row size of the table</param>
    def AddTable(self, columnSize: int, rowSize: int) -> NXOpen.OpenXml.TableDocumentData:
        """
         Creates a new @link NXOpen::OpenXml::TableDocumentData NXOpen::OpenXml::TableDocumentData@endlink  object.
                Does not to free this object, it will be free while deleting 
                @link NXOpen::Report::ResultXmlFileWriter NXOpen::Report::ResultXmlFileWriter@endlink  object
         @return data (@link NXOpen.OpenXml.TableDocumentData NXOpen.OpenXml.TableDocumentData@endlink):  the table data .
        """
        pass
    
    ##  Creates a new @link NXOpen::OpenXml::TextDocumentData NXOpen::OpenXml::TextDocumentData@endlink  object.
    ##         Does not to free this object, it will be free while deleting 
    ##         @link NXOpen::Report::ResultXmlFileWriter NXOpen::Report::ResultXmlFileWriter@endlink  object
    ##  @return data (@link NXOpen.OpenXml.TextDocumentData NXOpen.OpenXml.TextDocumentData@endlink):  the text data .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="textContent"> (str)  the content of the text data</param>
    def AddText(self, textContent: str) -> NXOpen.OpenXml.TextDocumentData:
        """
         Creates a new @link NXOpen::OpenXml::TextDocumentData NXOpen::OpenXml::TextDocumentData@endlink  object.
                Does not to free this object, it will be free while deleting 
                @link NXOpen::Report::ResultXmlFileWriter NXOpen::Report::ResultXmlFileWriter@endlink  object
         @return data (@link NXOpen.OpenXml.TextDocumentData NXOpen.OpenXml.TextDocumentData@endlink):  the text data .
        """
        pass
    
    ##  Removes all document data
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def DeleteAllData(self) -> None:
        """
         Removes all document data
        """
        pass
    
    ##  Removes the nth document data
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  the index of data</param>
    def DeleteNthData(self, index: int) -> None:
        """
         Removes the nth document data
        """
        pass
    
    ##  Frees the object from memory.  After this method is called,
    ##         it is illegal to use the object.  In .NET, this method is automatically
    ##         called when the object is deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    
    ##  Gets the number of data to be exported
    ##  @return dataCount (int):  the number of data .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetDataCount(self) -> int:
        """
         Gets the number of data to be exported
         @return dataCount (int):  the number of data .
        """
        pass
    
    ##  Gets the nth document data object.
    ##         Does not to free this object, it will be free while deleting 
    ##         @link NXOpen::Report::ResultXmlFileWriter NXOpen::Report::ResultXmlFileWriter@endlink  object
    ##  @return data (@link NXOpen.OpenXml.DocumentData NXOpen.OpenXml.DocumentData@endlink):  the data.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  the index of data</param>
    def GetNthData(self, index: int) -> NXOpen.OpenXml.DocumentData:
        """
         Gets the nth document data object.
                Does not to free this object, it will be free while deleting 
                @link NXOpen::Report::ResultXmlFileWriter NXOpen::Report::ResultXmlFileWriter@endlink  object
         @return data (@link NXOpen.OpenXml.DocumentData NXOpen.OpenXml.DocumentData@endlink):  the data.
        """
        pass
    
    ##  Exports all document data to result XML file
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="fileName"> (str)  the file name to be exported</param>
    def SaveToFile(self, fileName: str) -> None:
        """
         Exports all document data to result XML file
        """
        pass
    
##  Represents an argument for string type data.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class StringArgument(BaseArgument): 
    """ Represents an argument for string type data. """


    ## Getter for property: (str) DefaultValue
    ##  Returns the argument default value.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return str
    @property
    def DefaultValue(self) -> str:
        """
        Getter for property: (str) DefaultValue
         Returns the argument default value.  
             
         
        """
        pass
    
    ## Setter for property: (str) DefaultValue

    ##  Returns the argument default value.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @DefaultValue.setter
    def DefaultValue(self, defaultValue: str):
        """
        Setter for property: (str) DefaultValue
         Returns the argument default value.  
             
         
        """
        pass
    
##  Represents a template item object.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class TemplateItem(BaseItem): 
    """ Represents a template item object. """


    ##  Gets child items in template item. 
    ##  @return pItems (@link BaseItem List[NXOpen.Report.BaseItem]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="itemsLocation"> (@link CommandBuilder.UserInputLocation NXOpen.Report.CommandBuilder.UserInputLocation@endlink) </param>
    def GetChildItems(self, itemsLocation: CommandBuilder.UserInputLocation) -> List[BaseItem]:
        """
         Gets child items in template item. 
         @return pItems (@link BaseItem List[NXOpen.Report.BaseItem]@endlink): .
        """
        pass
    
##  Represents a text item.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class TextItem(BaseItem): 
    """ Represents a text item. """


    ##  Get the text content. 
    ##  @return lineTexts (List[str]):   .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetText(self) -> List[str]:
        """
         Get the text content. 
         @return lineTexts (List[str]):   .
        """
        pass
    
    ##  Set the text content. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="lineTexts"> (List[str])   </param>
    def SetText(self, lineTexts: List[str]) -> None:
        """
         Set the text content. 
        """
        pass
    
##  Represents a user images group item.   <br> Not support KF.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class UserImagesGroupItem(ImagesGroupItem): 
    """ Represents a user images group item.  """
    pass


import NXOpen
import NXOpen.Assemblies
##  Represents a user input in command.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class UserInput(NXOpen.TaggedObject): 
    """ Represents a user input in command. """


    ##  Represents the user input type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Text</term><description> 
    ##  User input for text data </description> </item><item><term> 
    ## Images</term><description> 
    ##  User input for images data  </description> </item></list>
    class Type(Enum):
        """
        Members Include: <Text> <Images>
        """
        Text: int
        Images: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> UserInput.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link UserInput.Type NXOpen.Report.UserInput.Type@endlink) InputType
    ##  Returns the user input type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return UserInput.Type
    @property
    def InputType(self) -> UserInput.Type:
        """
        Getter for property: (@link UserInput.Type NXOpen.Report.UserInput.Type@endlink) InputType
         Returns the user input type.  
             
         
        """
        pass
    
    ## Setter for property: (@link UserInput.Type NXOpen.Report.UserInput.Type@endlink) InputType

    ##  Returns the user input type.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @InputType.setter
    def InputType(self, inputType: UserInput.Type):
        """
        Setter for property: (@link UserInput.Type NXOpen.Report.UserInput.Type@endlink) InputType
         Returns the user input type.  
             
         
        """
        pass
    
    ## Getter for property: (bool) IsOccurrence
    ##  Returns whether this object is an occurrence or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @return bool
    @property
    def IsOccurrence(self) -> bool:
        """
        Getter for property: (bool) IsOccurrence
         Returns whether this object is an occurrence or not.  
             
         
        """
        pass
    
    ## Getter for property: (str) JournalIdentifier
    ##  Returns the identifier that would be recorded in a journal for this object.  
    ##    
    ##     This may not be the same across different releases of the software.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @return str
    @property
    def JournalIdentifier(self) -> str:
        """
        Getter for property: (str) JournalIdentifier
         Returns the identifier that would be recorded in a journal for this object.  
           
            This may not be the same across different releases of the software.   
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the custom name of the object.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the custom name of the object.  
              
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink) OwningComponent
    ##  Returns the owning component, if this object is an occurrence.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @return NXOpen.Assemblies.Component
    @property
    def OwningComponent(self) -> NXOpen.Assemblies.Component:
        """
        Getter for property: (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink) OwningComponent
         Returns the owning component, if this object is an occurrence.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.BasePart NXOpen.BasePart@endlink) OwningPart
    ##  Returns the owning part of this object   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @return NXOpen.BasePart
    @property
    def OwningPart(self) -> NXOpen.BasePart:
        """
        Getter for property: (@link NXOpen.BasePart NXOpen.BasePart@endlink) OwningPart
         Returns the owning part of this object   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.INXObject NXOpen.INXObject@endlink) Prototype
    ##  Returns the prototype of this object if it is an occurrence.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @return NXOpen.INXObject
    @property
    def Prototype(self) -> NXOpen.INXObject:
        """
        Getter for property: (@link NXOpen.INXObject NXOpen.INXObject@endlink) Prototype
         Returns the prototype of this object if it is an occurrence.  
             
         
        """
        pass
    
    ##  Gets the user input hint. 
    ##  @return inputHint (List[str]): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetHint(self) -> List[str]:
        """
         Gets the user input hint. 
         @return inputHint (List[str]): .
        """
        pass
    
    ##  Sets the user input hint. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="inputHint"> (List[str]) </param>
    def SetHint(self, inputHint: List[str]) -> None:
        """
         Sets the user input hint. 
        """
        pass
    
##  Represents a user text item.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class UserTextItem(TextItem): 
    """ Represents a user text item. """
    pass


## @package NXOpen.Report
## Classes, Enums and Structs under NXOpen.Report namespace

##  @link AutomationLoggerMessageType NXOpen.Report.AutomationLoggerMessageType @endlink is an alias for @link AutomationLogger.MessageType NXOpen.Report.AutomationLogger.MessageType@endlink
AutomationLoggerMessageType = AutomationLogger.MessageType


##  @link BaseArgumentType NXOpen.Report.BaseArgumentType @endlink is an alias for @link BaseArgument.Type NXOpen.Report.BaseArgument.Type@endlink
BaseArgumentType = BaseArgument.Type


##  @link CommandBuilderUserInputLocation NXOpen.Report.CommandBuilderUserInputLocation @endlink is an alias for @link CommandBuilder.UserInputLocation NXOpen.Report.CommandBuilder.UserInputLocation@endlink
CommandBuilderUserInputLocation = CommandBuilder.UserInputLocation


##  @link CommandImporterOverrideOption NXOpen.Report.CommandImporterOverrideOption @endlink is an alias for @link CommandImporter.OverrideOption NXOpen.Report.CommandImporter.OverrideOption@endlink
CommandImporterOverrideOption = CommandImporter.OverrideOption


##  @link CommandLibraryMoveCommandLocation NXOpen.Report.CommandLibraryMoveCommandLocation @endlink is an alias for @link CommandLibrary.MoveCommandLocation NXOpen.Report.CommandLibrary.MoveCommandLocation@endlink
CommandLibraryMoveCommandLocation = CommandLibrary.MoveCommandLocation


##  @link ProgramInformationLanguageType NXOpen.Report.ProgramInformationLanguageType @endlink is an alias for @link ProgramInformation.LanguageType NXOpen.Report.ProgramInformation.LanguageType@endlink
ProgramInformationLanguageType = ProgramInformation.LanguageType


##  @link UserInputType NXOpen.Report.UserInputType @endlink is an alias for @link UserInput.Type NXOpen.Report.UserInput.Type@endlink
UserInputType = UserInput.Type


