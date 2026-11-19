from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class ChangeList(NXOpen.TransientObject): 
    """
Records changes to option values at the specified level.


A ChangeList is created with a given level, and all of the edit operations apply to that
level.  Each method for setting a value throws an error if the option value is locked at a
higher level, or the specified value is not valid.


All methods in this class use an option
name as a unique identifier for accessing individual options and throw an error if an
option with the given name is not found. All existing option names and their allowed
values are described in the Online Documentation.

"""
    @property
    def CurrentLevel(self) -> LevelType:
        """
        Getter for property: ( LevelType NXOpen) CurrentLevel
         Returns the current level of options    
            
         
        """
        pass
    @property
    def LockedByDefault(self) -> LevelLockedByDefault:
        """
        Getter for property: ( LevelLockedByDefault NXOpen) LockedByDefault
         Returns the default lock status for the options level.  
           Valid only for   Options::LevelTypeSite   and   Options::LevelTypeGroup  .    
         
        """
        pass
    def DeleteValue(self, name: str) -> None:
        """
         Delete an option value. Throws an error if the value does not exist at this level. 
        """
        pass
    def Dispose(self) -> None:
        """
         
        """
        pass
    def LockValue(self, name: str) -> None:
        """
         Lock option value.  
        """
        pass
    def Save(self) -> None:
        """
         Saves options values at the current level. 
        """
        pass
    def SetUserComment(self, name: str, comment: str) -> None:
        """
         Sets the user comment. Throws an error if the value does not exist at this level. 
        """
        pass
    @overload
    def SetUtf8Value(self, name: str, value: str) -> None:
        """
         Sets the value of a  Options.OptionType.Utf8string  option.
                Throws an error if the option type is not  Options.OptionType.Utf8string .
            
        """
        pass
    @overload
    def SetUtf8Value(self, name: str, value: List[str]) -> None:
        """
         Sets the value of a  Options.OptionType.Utf8stringList  option.
                Throws an error if the option type is not  Options.OptionType.Utf8stringList .
             
        """
        pass
    @overload
    def SetValue(self, name: str, value: int) -> None:
        """
         Sets the value of an  Options.OptionType.Int  option.
            If the option is of type  Options.OptionType.Real  then the value parameter is converted to double.
            Throws an error if the option type is not  Options.OptionType.Int  or  Options.OptionType.Real . 
        """
        pass
    def SetValueOrder(self, name: str, value: List[str]) -> None:
        """
         Sets the value of a  Options.OptionType.ReorderSelList  option for which the list entries can be reordered.
                Throws an error if the option type is not  Options.OptionType.ReorderSelList .
             
        """
        pass
    def SetValueSelection(self, name: str, selection: List[bool], value: List[str]) -> None:
        """
         Sets the value of a  Options.OptionType.ReorderSelList  option for which the list entries can be reordered as well as selected.
                Throws an error if the option type is not  Options.OptionType.ReorderSelList .
             
        """
        pass
    @overload
    def SetValue(self, name: str, value: float) -> None:
        """
         Sets the value of a  Options.OptionType.Real  option.
                Throws an error if the option type is not  Options.OptionType.Real .
            
        """
        pass
    @overload
    def SetValue(self, name: str, value: str) -> None:
        """
         Sets the value of a  Options.OptionType.String  option.
                Throws an error if the option type is not  Options.OptionType.String .
            
        """
        pass
    @overload
    def SetValue(self, name: str, value: List[str]) -> None:
        """
         Sets the value of a  Options.OptionType.StringList  option.
                Throws an error if the option type is not  Options.OptionType.StringList .
             
        """
        pass
    @overload
    def SetValue(self, name: str, value: bool) -> None:
        """
         Sets the value of a  Options.OptionType.Logical  option.
                Throws an error if the option type is not  Options.OptionType.Logical .
             
        """
        pass
    def UnlockValue(self, name: str) -> None:
        """
         Unlock option value. 
        """
        pass
import NXOpen
class DraftingStandardChangeList(NXOpen.TransientObject): 
    """ 
Records changes to option values at the specified level. 


A DraftingStandardChangeList is created with a given level, and all of the edit operations apply to that
level for drafting standard defaults.  Each method for setting a value throws an error if the option value 
is locked at a higher level, or the specified value is not valid. 


All methods in this class use an option
name as a unique identifier for accessing individual options and throw an error if an
option with the given name is not found. All existing option names and their allowed
values are described in the Online Documentation. 

"""
    @property
    def CurrentLevel(self) -> LevelType:
        """
        Getter for property: ( LevelType NXOpen) CurrentLevel
         Returns the current level of options    
            
         
        """
        pass
    def Dispose(self) -> None:
        """
         Dispose the changes
        """
        pass
    def Load(self) -> None:
        """
         Load the drafting standard defaults at the current level. 
        """
        pass
    def LockValue(self, name: str) -> None:
        """
         Lock option value.  
        """
        pass
    def Save(self) -> None:
        """
         Saves the drafting standard defaults at the current level. 
        """
        pass
    def SetUserComment(self, name: str, comment: str) -> None:
        """
         Sets the user comment. Throws an error if the value does not exist at this level. 
        """
        pass
    def SetUtf8Value(self, name: str, value: str) -> None:
        """
         Sets the value of a  Options.OptionType.Utf8string  option. 
                Throws an error if the option type is not  Options.OptionType.Utf8string . 
            
        """
        pass
    @overload
    def SetValue(self, name: str, value: int) -> None:
        """
         Sets the value of an  Options.OptionType.Int  option. 
            If the option is of type  Options.OptionType.Real  then the value parameter is converted to double.
            Throws an error if the option type is not  Options.OptionType.Int  or  Options.OptionType.Real . 
        """
        pass
    def SetValueOrder(self, name: str, value: List[str]) -> None:
        """
         Sets the value of a  Options.OptionType.ReorderSelList  option for which the list entries can be reordered.
                Throws an error if the option type is not  Options.OptionType.ReorderSelList .
             
        """
        pass
    def SetValueSelection(self, name: str, selection: List[bool], value: List[str]) -> None:
        """
         Sets the value of a  Options.OptionType.ReorderSelList  option for which the list entries can be reordered as well as selected.
                Throws an error if the option type is not  Options.OptionType.ReorderSelList .
             
        """
        pass
    @overload
    def SetValue(self, name: str, value: float) -> None:
        """
         Sets the value of a  Options.OptionType.Real  option.
                Throws an error if the option type is not  Options.OptionType.Real . 
            
        """
        pass
    @overload
    def SetValue(self, name: str, value: str) -> None:
        """
         Sets the value of a  Options.OptionType.String  option. 
                Throws an error if the option type is not  Options.OptionType.String . 
            
        """
        pass
    @overload
    def SetValue(self, name: str, value: List[str]) -> None:
        """
         Sets the value of a  Options.OptionType.StringList  option.
                Throws an error if the option type is not  Options.OptionType.StringList .     
             
        """
        pass
    @overload
    def SetValue(self, name: str, value: bool) -> None:
        """
         Sets the value of a  Options.OptionType.Logical  option.
                Throws an error if the option type is not  Options.OptionType.Logical .         
             
        """
        pass
    def UnlockValue(self, name: str) -> None:
        """
         Unlock option value. 
        """
        pass
class LevelLockedByDefault(Enum):
    """
    Members Include: 
     |FalseValue|  Unlocked 
     |TrueValue|  Locked 

    """
    FalseValue: int
    TrueValue: int
    @staticmethod
    def ValueOf(value: int) -> LevelLockedByDefault:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class LevelType(Enum):
    """
    Members Include: 
     |Shipped|  Shipped level 
     |Package|  Package level 
     |Site|  Site level 
     |Group|  Group level 
     |User|  User level 

    """
    Shipped: int
    Package: int
    Site: int
    Group: int
    User: int
    @staticmethod
    def ValueOf(value: int) -> LevelType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class OptionsManager(NXOpen.Object): 
    """ 
    Manages options. 
    
    OptionsManager methods use an option name as a unique identifier for
    accessing individual options and throw an error if an option with a given name is not
    found.  All existing option names are listed in the Online Documentation.
    
    
    If a level parameter is not supplied to a query method then the option value effective in
    current session is returned.  If a level parameter is supplied then then value
    that is stored at the specified level is returned. This may not be the same as the value
    effective in the current session and may take effect only after the session is restarted.
    
    """
    def GetAllOptions() -> List[str]:
        """
         Gets the names of all available options. 
         Returns options (List[str]):  List of names of all available options. .
        """
        pass
    @overload
    def GetIntValue(name: str) -> int:
        """
         Gets the value of an  Options.OptionType.Int  option. 
                    Throws an error if option type is not  Options.OptionType.Int . 
                
         Returns value (int):  Option value .
        """
        pass
    @overload
    def GetIntValue(name: str, level: LevelType) -> int:
        """
         Gets the value of an  Options.OptionType.Int  option at the specified level. 
                    Throws an error if the option is not of type  Options.OptionType.Int .
                
         Returns value (int):  Option value .
        """
        pass
    @overload
    def GetLogicalValue(name: str) -> bool:
        """
         Gets the value of a  Options.OptionType.Logical  option. 
                    Throws an error if the option is not of type  Options.OptionType.Logical . 
         Returns value (bool):  Option value. .
        """
        pass
    @overload
    def GetLogicalValue(name: str, level: LevelType) -> bool:
        """
         Gets the value of a  Options.OptionType.Logical  option at the specified level.  
                    Throws an error if the option is not of type  Options.OptionType.Logical .
                
         Returns value (bool):  Option value .
        """
        pass
    def GetOptionType(name: str) -> OptionType:
        """
         Returns an option's type. 
         Returns type ( OptionType NXOpen):  Option type .
        """
        pass
    @overload
    def GetRealValue(name: str) -> float:
        """
         Gets the value of a  Options.OptionType.Real  option. 
                    Throws an error if the option is not of type  Options.OptionType.Real .
                 
         Returns value (float):  Option value. .
        """
        pass
    @overload
    def GetRealValue(name: str, level: LevelType) -> float:
        """
         Gets the value of a  Options.OptionType.Real  option at the specified level. 
                    Throws an error if the option is not of type  Options.OptionType.Real .
                
         Returns value (float):  Option value .
        """
        pass
    @overload
    def GetReorderSelectableStringListValue(name: str) -> Tuple[List[str], List[bool]]:
        """
         Gets the value of a  Options.OptionType.ReorderSelList  option. 
                    Throws an error if the option is not of type  Options.OptionType.ReorderSelList .
                
         Returns A tuple consisting of (value, selection). 
         - value is: List[str]. Option value .
         - selection is: List[bool]. the selection bit .

        """
        pass
    @overload
    def GetReorderSelectableStringListValue(name: str, level: LevelType) -> Tuple[List[str], List[bool]]:
        """
         Gets the value of a  Options.OptionType.ReorderSelList  option at the specified level. 
                    Throws an error if the option is not of type  Options.OptionType.ReorderSelList .
                
         Returns A tuple consisting of (value, selection). 
         - value is: List[str]. Option value .
         - selection is: List[bool]. the selection bit .

        """
        pass
    def GetScope(name: str) -> OptionsScope:
        """
         Returns scope of an option.
                
         Returns scopeValue ( OptionsScope NXOpen):  Option scope .
        """
        pass
    @overload
    def GetStringListValue(name: str) -> List[str]:
        """
         Gets the value of a  Options.OptionType.StringList  option. 
                    Throws an error if the option is not of type  Options.OptionType.StringList .
                
         Returns value (List[str]):  Option value. .
        """
        pass
    @overload
    def GetStringListValue(name: str, level: LevelType) -> List[str]:
        """
         Gets the value of a  Options.OptionType.StringList  option at the specified level. 
                    Throws an error if the option is not of type  Options.OptionType.StringList .
                
         Returns value (List[str]):  Option value .
        """
        pass
    @overload
    def GetStringValue(name: str) -> str:
        """
         Gets the value of a  Options.OptionType.String  option. 
                    Throws an error if the option is not of type  Options.OptionType.String .
                
         Returns value (str):  Option value. .
        """
        pass
    @overload
    def GetStringValue(name: str, level: LevelType) -> str:
        """
         Gets the value of a  Options.OptionType.String  option at the specified level. 
                    Throws an error if the option is not of type  Options.OptionType.String .
                
         Returns value (str):  Option value .
        """
        pass
    def GetUserComment(name: str, level: LevelType) -> str:
        """
         Returns then user comment at the specified level. User comments are not supported at the  Options.LevelType.Shipped  level. 
         Returns comment (str):  User comment text. .
        """
        pass
    @overload
    def GetUtf8stringValue(name: str) -> str:
        """
         Gets the value of a  Options.OptionType.Utf8string  option. 
                    Throws an error if the option is not of type  Options.OptionType.Utf8string .
                
         Returns utf8_value (str):  Option utf8 value. .
        """
        pass
    @overload
    def GetUtf8stringValue(name: str, level: LevelType) -> str:
        """
         Gets the value of a  Options.OptionType.Utf8string  option at the specified level. 
                    Throws an error if the option is not of type  Options.OptionType.String .
                
         Returns value (str):  Option value .
        """
        pass
    def IsLevelLockedByDefault(level: LevelType) -> bool:
        """
         Returns true if the option's values at the specified level are locked by default.
                    Locked by default means that if an option value does not exist at this level, 
                    then it is locked.
                
         Returns status (bool):  True if options values are locked by default .
        """
        pass
    def IsValueLocked(name: str, level: LevelType) -> bool:
        """
         Returns true if the option value is locked at the specified level. 
                    Locks are not supported at  Options.LevelType.User  and  Options.LevelType.Shipped  levels. 
         Returns status (bool):  Lock status .
        """
        pass
    def IsValueSet(name: str, level: LevelType) -> bool:
        """
         Returns true if the option value exists at the specified level. Always true for the  Options.LevelType.Shipped  level. 
         Returns status (bool):  True if value is set .
        """
        pass
    def NewOptionsChangeList(level: LevelType, locked_by_default: LevelLockedByDefault) -> ChangeList:
        """
         Creates an instance of  NXOpen.Options.ChangeList  class, in order to edit a set of options. 
                It is not possible to create an instance of  NXOpen.Options.ChangeList  for  Options.LevelType.Shipped  level, 
                or for a level that is not defined or is not writeable.  
         Returns data ( ChangeList NXOpen):  An instanse of  NXOpen.Options.ChangeList  class .
        """
        pass
    def NewOptionsDraftingStandardChangeList(level: LevelType, filename: str) -> DraftingStandardChangeList:
        """
         Creates an instance of  NXOpen.Options.DraftingStandardChangeList  class, in order to edit a set of options. 
                It is not possible to create an instance of  NXOpen.Options.DraftingStandardChangeList  for  Options.LevelType.Shipped  level, 
                or for a level that is not defined or is not writeable.  
         Returns data ( DraftingStandardChangeList NXOpen):  An instanse of  NXOpen.Options.DraftingStandardChangeList  class .
        """
        pass
class OptionsScope(Enum):
    """
    Members Include: 
     |Part|  Option scope is part 
     |Session|  Option scope is session 

    """
    Part: int
    Session: int
    @staticmethod
    def ValueOf(value: int) -> OptionsScope:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class OptionType(Enum):
    """
    Members Include: 
     |Int|  Option value is an integer number 
     |Real|  Option value is a real number 
     |String|  Option value is an ascii string 
     |StringList|  Option value is a list of ascii strings 
     |Logical|  Option value is logical 
     |Utf8string|  Option value is a utf8 string 
     |Utf8stringList|  Option value is a list of utf8 strings 
     |ReorderSelList|  Option value is a list which can be selected and re-ordered 

    """
    Int: int
    Real: int
    String: int
    StringList: int
    Logical: int
    Utf8string: int
    Utf8stringList: int
    ReorderSelList: int
    @staticmethod
    def ValueOf(value: int) -> OptionType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
