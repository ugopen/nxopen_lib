from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
## 
## Records changes to option values at the specified level.
## 
##  <br> 
## A ChangeList is created with a given level, and all of the edit operations apply to that
## level.  Each method for setting a value throws an error if the option value is locked at a
## higher level, or the specified value is not valid.
##  <br> 
##  <br> 
## All methods in this class use an option
## name as a unique identifier for accessing individual options and throw an error if an
## option with the given name is not found. All existing option names and their allowed
## values are described in the Online Documentation.
##  <br> 
##  <br> Use @link Options::OptionsManager::NewOptionsChangeList Options::OptionsManager::NewOptionsChangeList@endlink  to create a new instance of this class  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class ChangeList(NXOpen.TransientObject): 
    """
Records changes to option values at the specified level.

<para>
A ChangeList is created with a given level, and all of the edit operations apply to that
level.  Each method for setting a value throws an error if the option value is locked at a
higher level, or the specified value is not valid.
</para>
<para>
All methods in this class use an option
name as a unique identifier for accessing individual options and throw an error if an
option with the given name is not found. All existing option names and their allowed
values are described in the Online Documentation.
</para>
"""


    ## Getter for property: (@link LevelType NXOpen.Options.LevelType@endlink) CurrentLevel
    ##  Returns the current level of options    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## @return LevelType
    @property
    def CurrentLevel(self) -> LevelType:
        """
        Getter for property: (@link LevelType NXOpen.Options.LevelType@endlink) CurrentLevel
         Returns the current level of options    
            
         
        """
        pass
    
    ## Getter for property: (@link LevelLockedByDefault NXOpen.Options.LevelLockedByDefault@endlink) LockedByDefault
    ##  Returns the default lock status for the options level.  
    ##    Valid only for @link  Options::LevelTypeSite   Options::LevelTypeSite @endlink  and @link  Options::LevelTypeGroup   Options::LevelTypeGroup @endlink .    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## @return LevelLockedByDefault
    @property
    def LockedByDefault(self) -> LevelLockedByDefault:
        """
        Getter for property: (@link LevelLockedByDefault NXOpen.Options.LevelLockedByDefault@endlink) LockedByDefault
         Returns the default lock status for the options level.  
           Valid only for @link  Options::LevelTypeSite   Options::LevelTypeSite @endlink  and @link  Options::LevelTypeGroup   Options::LevelTypeGroup @endlink .    
         
        """
        pass
    
    ##  Delete an option value. Throws an error if the value does not exist at this level. 
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="name"> (str)  Option name. </param>
    def DeleteValue(self, name: str) -> None:
        """
         Delete an option value. Throws an error if the value does not exist at this level. 
        """
        pass
    
    ##  
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         
        """
        pass
    
    ##  Lock option value.  
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="name"> (str)  Option name </param>
    def LockValue(self, name: str) -> None:
        """
         Lock option value.  
        """
        pass
    
    ##  Saves options values at the current level. 
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    def Save(self) -> None:
        """
         Saves options values at the current level. 
        """
        pass
    
    ##  Sets the user comment. Throws an error if the value does not exist at this level. 
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="name"> (str)  Option name. </param>
    ## <param name="comment"> (str)  User comment text. </param>
    def SetUserComment(self, name: str, comment: str) -> None:
        """
         Sets the user comment. Throws an error if the value does not exist at this level. 
        """
        pass
    
    ##  Sets the value of a @link  Options::OptionTypeUtf8string   Options::OptionTypeUtf8string @endlink  option.
    ##         Throws an error if the option type is not @link  Options::OptionTypeUtf8string   Options::OptionTypeUtf8string @endlink .
    ##     
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## <param name="data"> (@link ChangeList NXOpen.Options.ChangeList@endlink) </param>
    ## <param name="name"> (str)  Option name. </param>
    ## <param name="value"> (str)  Option value </param>
    @overload
    def SetUtf8Value(self, name: str, value: str) -> None:
        """
         Sets the value of a @link  Options::OptionTypeUtf8string   Options::OptionTypeUtf8string @endlink  option.
                Throws an error if the option type is not @link  Options::OptionTypeUtf8string   Options::OptionTypeUtf8string @endlink .
            
        """
        pass
    
    ##  Sets the value of a @link  Options::OptionTypeUtf8stringList   Options::OptionTypeUtf8stringList @endlink  option.
    ##         Throws an error if the option type is not @link  Options::OptionTypeUtf8stringList   Options::OptionTypeUtf8stringList @endlink .
    ##      
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## <param name="data"> (@link ChangeList NXOpen.Options.ChangeList@endlink) </param>
    ## <param name="name"> (str)  Option name. </param>
    ## <param name="value"> (List[str])  Option value </param>
    @overload
    def SetUtf8Value(self, name: str, value: List[str]) -> None:
        """
         Sets the value of a @link  Options::OptionTypeUtf8stringList   Options::OptionTypeUtf8stringList @endlink  option.
                Throws an error if the option type is not @link  Options::OptionTypeUtf8stringList   Options::OptionTypeUtf8stringList @endlink .
             
        """
        pass
    
    ##  Sets the value of an @link  Options::OptionTypeInt   Options::OptionTypeInt @endlink  option.
    ##     If the option is of type @link  Options::OptionTypeReal   Options::OptionTypeReal @endlink  then the value parameter is converted to double.
    ##     Throws an error if the option type is not @link  Options::OptionTypeInt   Options::OptionTypeInt @endlink  or @link  Options::OptionTypeReal   Options::OptionTypeReal @endlink . 
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="data"> (@link ChangeList NXOpen.Options.ChangeList@endlink) </param>
    ## <param name="name"> (str)  Option name. </param>
    ## <param name="value"> (int)  Option value. </param>
    @overload
    def SetValue(self, name: str, value: int) -> None:
        """
         Sets the value of an @link  Options::OptionTypeInt   Options::OptionTypeInt @endlink  option.
            If the option is of type @link  Options::OptionTypeReal   Options::OptionTypeReal @endlink  then the value parameter is converted to double.
            Throws an error if the option type is not @link  Options::OptionTypeInt   Options::OptionTypeInt @endlink  or @link  Options::OptionTypeReal   Options::OptionTypeReal @endlink . 
        """
        pass
    
    ##  Sets the value of a @link  Options::OptionTypeReorderSelList   Options::OptionTypeReorderSelList @endlink  option for which the list entries can be reordered.
    ##         Throws an error if the option type is not @link  Options::OptionTypeReorderSelList   Options::OptionTypeReorderSelList @endlink .
    ##      
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="name"> (str)  Option name. </param>
    ## <param name="value"> (List[str])   </param>
    def SetValueOrder(self, name: str, value: List[str]) -> None:
        """
         Sets the value of a @link  Options::OptionTypeReorderSelList   Options::OptionTypeReorderSelList @endlink  option for which the list entries can be reordered.
                Throws an error if the option type is not @link  Options::OptionTypeReorderSelList   Options::OptionTypeReorderSelList @endlink .
             
        """
        pass
    
    ##  Sets the value of a @link  Options::OptionTypeReorderSelList   Options::OptionTypeReorderSelList @endlink  option for which the list entries can be reordered as well as selected.
    ##         Throws an error if the option type is not @link  Options::OptionTypeReorderSelList   Options::OptionTypeReorderSelList @endlink .
    ##      
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="name"> (str)  Option name. </param>
    ## <param name="selection"> (List[bool])  the selection bit </param>
    ## <param name="value"> (List[str])   </param>
    def SetValueSelection(self, name: str, selection: List[bool], value: List[str]) -> None:
        """
         Sets the value of a @link  Options::OptionTypeReorderSelList   Options::OptionTypeReorderSelList @endlink  option for which the list entries can be reordered as well as selected.
                Throws an error if the option type is not @link  Options::OptionTypeReorderSelList   Options::OptionTypeReorderSelList @endlink .
             
        """
        pass
    
    ##  Sets the value of a @link  Options::OptionTypeReal   Options::OptionTypeReal @endlink  option.
    ##         Throws an error if the option type is not @link  Options::OptionTypeReal   Options::OptionTypeReal @endlink .
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="data"> (@link ChangeList NXOpen.Options.ChangeList@endlink) </param>
    ## <param name="name"> (str)  Option name. </param>
    ## <param name="value"> (float)  Option value. </param>
    @overload
    def SetValue(self, name: str, value: float) -> None:
        """
         Sets the value of a @link  Options::OptionTypeReal   Options::OptionTypeReal @endlink  option.
                Throws an error if the option type is not @link  Options::OptionTypeReal   Options::OptionTypeReal @endlink .
            
        """
        pass
    
    ##  Sets the value of a @link  Options::OptionTypeString   Options::OptionTypeString @endlink  option.
    ##         Throws an error if the option type is not @link  Options::OptionTypeString   Options::OptionTypeString @endlink .
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="data"> (@link ChangeList NXOpen.Options.ChangeList@endlink) </param>
    ## <param name="name"> (str)  Option name. </param>
    ## <param name="value"> (str)  Option value </param>
    @overload
    def SetValue(self, name: str, value: str) -> None:
        """
         Sets the value of a @link  Options::OptionTypeString   Options::OptionTypeString @endlink  option.
                Throws an error if the option type is not @link  Options::OptionTypeString   Options::OptionTypeString @endlink .
            
        """
        pass
    
    ##  Sets the value of a @link  Options::OptionTypeStringList   Options::OptionTypeStringList @endlink  option.
    ##         Throws an error if the option type is not @link  Options::OptionTypeStringList   Options::OptionTypeStringList @endlink .
    ##      
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="data"> (@link ChangeList NXOpen.Options.ChangeList@endlink) </param>
    ## <param name="name"> (str)  Option name. </param>
    ## <param name="value"> (List[str])   </param>
    @overload
    def SetValue(self, name: str, value: List[str]) -> None:
        """
         Sets the value of a @link  Options::OptionTypeStringList   Options::OptionTypeStringList @endlink  option.
                Throws an error if the option type is not @link  Options::OptionTypeStringList   Options::OptionTypeStringList @endlink .
             
        """
        pass
    
    ##  Sets the value of a @link  Options::OptionTypeLogical   Options::OptionTypeLogical @endlink  option.
    ##         Throws an error if the option type is not @link  Options::OptionTypeLogical   Options::OptionTypeLogical @endlink .
    ##      
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="data"> (@link ChangeList NXOpen.Options.ChangeList@endlink) </param>
    ## <param name="name"> (str)  Option name. </param>
    ## <param name="value"> (bool)  Option value </param>
    @overload
    def SetValue(self, name: str, value: bool) -> None:
        """
         Sets the value of a @link  Options::OptionTypeLogical   Options::OptionTypeLogical @endlink  option.
                Throws an error if the option type is not @link  Options::OptionTypeLogical   Options::OptionTypeLogical @endlink .
             
        """
        pass
    
    ##  Unlock option value. 
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="name"> (str)  Option name </param>
    def UnlockValue(self, name: str) -> None:
        """
         Unlock option value. 
        """
        pass
    
import NXOpen
##  
## Records changes to option values at the specified level. 
## 
##  <br> 
## A DraftingStandardChangeList is created with a given level, and all of the edit operations apply to that
## level for drafting standard defaults.  Each method for setting a value throws an error if the option value 
## is locked at a higher level, or the specified value is not valid. 
##  <br> 
##  <br> 
## All methods in this class use an option
## name as a unique identifier for accessing individual options and throw an error if an
## option with the given name is not found. All existing option names and their allowed
## values are described in the Online Documentation. 
##  <br> 
##  <br> Use @link Options::OptionsManager::NewOptionsDraftingStandardChangeList Options::OptionsManager::NewOptionsDraftingStandardChangeList@endlink  to create a new instance of this class  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class DraftingStandardChangeList(NXOpen.TransientObject): 
    """ 
Records changes to option values at the specified level. 

<para>
A DraftingStandardChangeList is created with a given level, and all of the edit operations apply to that
level for drafting standard defaults.  Each method for setting a value throws an error if the option value 
is locked at a higher level, or the specified value is not valid. 
</para>
<para>
All methods in this class use an option
name as a unique identifier for accessing individual options and throw an error if an
option with the given name is not found. All existing option names and their allowed
values are described in the Online Documentation. 
</para>
"""


    ## Getter for property: (@link LevelType NXOpen.Options.LevelType@endlink) CurrentLevel
    ##  Returns the current level of options    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return LevelType
    @property
    def CurrentLevel(self) -> LevelType:
        """
        Getter for property: (@link LevelType NXOpen.Options.LevelType@endlink) CurrentLevel
         Returns the current level of options    
            
         
        """
        pass
    
    ##  Dispose the changes
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Dispose the changes
        """
        pass
    
    ##  Load the drafting standard defaults at the current level. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def Load(self) -> None:
        """
         Load the drafting standard defaults at the current level. 
        """
        pass
    
    ##  Lock option value.  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="name"> (str)  Option name </param>
    def LockValue(self, name: str) -> None:
        """
         Lock option value.  
        """
        pass
    
    ##  Saves the drafting standard defaults at the current level. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def Save(self) -> None:
        """
         Saves the drafting standard defaults at the current level. 
        """
        pass
    
    ##  Sets the user comment. Throws an error if the value does not exist at this level. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="name"> (str)  Option name. </param>
    ## <param name="comment"> (str)  User comment text. </param>
    def SetUserComment(self, name: str, comment: str) -> None:
        """
         Sets the user comment. Throws an error if the value does not exist at this level. 
        """
        pass
    
    ##  Sets the value of a @link  Options::OptionTypeUtf8string   Options::OptionTypeUtf8string @endlink  option. 
    ##         Throws an error if the option type is not @link  Options::OptionTypeUtf8string   Options::OptionTypeUtf8string @endlink . 
    ##     
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="name"> (str)  Option name. </param>
    ## <param name="value"> (str)  Option value </param>
    def SetUtf8Value(self, name: str, value: str) -> None:
        """
         Sets the value of a @link  Options::OptionTypeUtf8string   Options::OptionTypeUtf8string @endlink  option. 
                Throws an error if the option type is not @link  Options::OptionTypeUtf8string   Options::OptionTypeUtf8string @endlink . 
            
        """
        pass
    
    ##  Sets the value of an @link  Options::OptionTypeInt   Options::OptionTypeInt @endlink  option. 
    ##     If the option is of type @link  Options::OptionTypeReal   Options::OptionTypeReal @endlink  then the value parameter is converted to double.
    ##     Throws an error if the option type is not @link  Options::OptionTypeInt   Options::OptionTypeInt @endlink  or @link  Options::OptionTypeReal   Options::OptionTypeReal @endlink . 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="data"> (@link DraftingStandardChangeList NXOpen.Options.DraftingStandardChangeList@endlink) </param>
    ## <param name="name"> (str)  Option name. </param>
    ## <param name="value"> (int)  Option value. </param>
    @overload
    def SetValue(self, name: str, value: int) -> None:
        """
         Sets the value of an @link  Options::OptionTypeInt   Options::OptionTypeInt @endlink  option. 
            If the option is of type @link  Options::OptionTypeReal   Options::OptionTypeReal @endlink  then the value parameter is converted to double.
            Throws an error if the option type is not @link  Options::OptionTypeInt   Options::OptionTypeInt @endlink  or @link  Options::OptionTypeReal   Options::OptionTypeReal @endlink . 
        """
        pass
    
    ##  Sets the value of a @link  Options::OptionTypeReorderSelList   Options::OptionTypeReorderSelList @endlink  option for which the list entries can be reordered.
    ##         Throws an error if the option type is not @link  Options::OptionTypeReorderSelList   Options::OptionTypeReorderSelList @endlink .
    ##      
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="name"> (str)  Option name. </param>
    ## <param name="value"> (List[str])   </param>
    def SetValueOrder(self, name: str, value: List[str]) -> None:
        """
         Sets the value of a @link  Options::OptionTypeReorderSelList   Options::OptionTypeReorderSelList @endlink  option for which the list entries can be reordered.
                Throws an error if the option type is not @link  Options::OptionTypeReorderSelList   Options::OptionTypeReorderSelList @endlink .
             
        """
        pass
    
    ##  Sets the value of a @link  Options::OptionTypeReorderSelList   Options::OptionTypeReorderSelList @endlink  option for which the list entries can be reordered as well as selected.
    ##         Throws an error if the option type is not @link  Options::OptionTypeReorderSelList   Options::OptionTypeReorderSelList @endlink .
    ##      
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="name"> (str)  Option name. </param>
    ## <param name="selection"> (List[bool])  the selection bit </param>
    ## <param name="value"> (List[str])   </param>
    def SetValueSelection(self, name: str, selection: List[bool], value: List[str]) -> None:
        """
         Sets the value of a @link  Options::OptionTypeReorderSelList   Options::OptionTypeReorderSelList @endlink  option for which the list entries can be reordered as well as selected.
                Throws an error if the option type is not @link  Options::OptionTypeReorderSelList   Options::OptionTypeReorderSelList @endlink .
             
        """
        pass
    
    ##  Sets the value of a @link  Options::OptionTypeReal   Options::OptionTypeReal @endlink  option.
    ##         Throws an error if the option type is not @link  Options::OptionTypeReal   Options::OptionTypeReal @endlink . 
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="data"> (@link DraftingStandardChangeList NXOpen.Options.DraftingStandardChangeList@endlink) </param>
    ## <param name="name"> (str)  Option name. </param>
    ## <param name="value"> (float)  Option value. </param>
    @overload
    def SetValue(self, name: str, value: float) -> None:
        """
         Sets the value of a @link  Options::OptionTypeReal   Options::OptionTypeReal @endlink  option.
                Throws an error if the option type is not @link  Options::OptionTypeReal   Options::OptionTypeReal @endlink . 
            
        """
        pass
    
    ##  Sets the value of a @link  Options::OptionTypeString   Options::OptionTypeString @endlink  option. 
    ##         Throws an error if the option type is not @link  Options::OptionTypeString   Options::OptionTypeString @endlink . 
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="data"> (@link DraftingStandardChangeList NXOpen.Options.DraftingStandardChangeList@endlink) </param>
    ## <param name="name"> (str)  Option name. </param>
    ## <param name="value"> (str)  Option value </param>
    @overload
    def SetValue(self, name: str, value: str) -> None:
        """
         Sets the value of a @link  Options::OptionTypeString   Options::OptionTypeString @endlink  option. 
                Throws an error if the option type is not @link  Options::OptionTypeString   Options::OptionTypeString @endlink . 
            
        """
        pass
    
    ##  Sets the value of a @link  Options::OptionTypeStringList   Options::OptionTypeStringList @endlink  option.
    ##         Throws an error if the option type is not @link  Options::OptionTypeStringList   Options::OptionTypeStringList @endlink .     
    ##      
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="data"> (@link DraftingStandardChangeList NXOpen.Options.DraftingStandardChangeList@endlink) </param>
    ## <param name="name"> (str)  Option name. </param>
    ## <param name="value"> (List[str])   </param>
    @overload
    def SetValue(self, name: str, value: List[str]) -> None:
        """
         Sets the value of a @link  Options::OptionTypeStringList   Options::OptionTypeStringList @endlink  option.
                Throws an error if the option type is not @link  Options::OptionTypeStringList   Options::OptionTypeStringList @endlink .     
             
        """
        pass
    
    ##  Sets the value of a @link  Options::OptionTypeLogical   Options::OptionTypeLogical @endlink  option.
    ##         Throws an error if the option type is not @link  Options::OptionTypeLogical   Options::OptionTypeLogical @endlink .         
    ##      
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="data"> (@link DraftingStandardChangeList NXOpen.Options.DraftingStandardChangeList@endlink) </param>
    ## <param name="name"> (str)  Option name. </param>
    ## <param name="value"> (bool)  Option value </param>
    @overload
    def SetValue(self, name: str, value: bool) -> None:
        """
         Sets the value of a @link  Options::OptionTypeLogical   Options::OptionTypeLogical @endlink  option.
                Throws an error if the option type is not @link  Options::OptionTypeLogical   Options::OptionTypeLogical @endlink .         
             
        """
        pass
    
    ##  Unlock option value. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="name"> (str)  Option name </param>
    def UnlockValue(self, name: str) -> None:
        """
         Unlock option value. 
        """
        pass
    
##  Specifies default lock status for the options level. 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## FalseValue</term><description> 
##  Unlocked </description> </item><item><term> 
## TrueValue</term><description> 
##  Locked </description> </item></list>
class LevelLockedByDefault(Enum):
    """
    Members Include: <FalseValue> <TrueValue>
    """
    FalseValue: int
    TrueValue: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> LevelLockedByDefault:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Specifies level type. 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Shipped</term><description> 
##  Shipped level </description> </item><item><term> 
## Package</term><description> 
##  Package level </description> </item><item><term> 
## Site</term><description> 
##  Site level </description> </item><item><term> 
## Group</term><description> 
##  Group level </description> </item><item><term> 
## User</term><description> 
##  User level </description> </item></list>
class LevelType(Enum):
    """
    Members Include: <Shipped> <Package> <Site> <Group> <User>
    """
    Shipped: int
    Package: int
    Site: int
    Group: int
    User: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> LevelType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##  
##     Manages options. 
##      <br> 
##     OptionsManager methods use an option name as a unique identifier for
##     accessing individual options and throw an error if an option with a given name is not
##     found.  All existing option names are listed in the Online Documentation.
##      <br> 
##      <br> 
##     If a level parameter is not supplied to a query method then the option value effective in
##     current session is returned.  If a level parameter is supplied then then value
##     that is stored at the specified level is returned. This may not be the same as the value
##     effective in the current session and may take effect only after the session is restarted.
##      <br> 
##      <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class OptionsManager(NXOpen.Object): 
    """ 
    Manages options. 
    <para>
    OptionsManager methods use an option name as a unique identifier for
    accessing individual options and throw an error if an option with a given name is not
    found.  All existing option names are listed in the Online Documentation.
    </para>
    <para>
    If a level parameter is not supplied to a query method then the option value effective in
    current session is returned.  If a level parameter is supplied then then value
    that is stored at the specified level is returned. This may not be the same as the value
    effective in the current session and may take effect only after the session is restarted.
    </para>
    """


    ##  Gets the names of all available options. 
    ##  @return options (List[str]):  List of names of all available options. .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    def GetAllOptions() -> List[str]:
        """
         Gets the names of all available options. 
         @return options (List[str]):  List of names of all available options. .
        """
        pass
    
    ##  Gets the value of an @link  Options::OptionTypeInt   Options::OptionTypeInt @endlink  option. 
    ##             Throws an error if option type is not @link  Options::OptionTypeInt   Options::OptionTypeInt @endlink . 
    ##         
    ##  @return value (int):  Option value .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="name"> (str)  Option name. </param>
    @overload
    def GetIntValue(name: str) -> int:
        """
         Gets the value of an @link  Options::OptionTypeInt   Options::OptionTypeInt @endlink  option. 
                    Throws an error if option type is not @link  Options::OptionTypeInt   Options::OptionTypeInt @endlink . 
                
         @return value (int):  Option value .
        """
        pass
    
    ##  Gets the value of an @link  Options::OptionTypeInt   Options::OptionTypeInt @endlink  option at the specified level. 
    ##             Throws an error if the option is not of type @link  Options::OptionTypeInt   Options::OptionTypeInt @endlink .
    ##         
    ##  @return value (int):  Option value .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="name"> (str)  Option name. </param>
    ## <param name="level"> (@link LevelType NXOpen.Options.LevelType@endlink)  Options level. </param>
    @overload
    def GetIntValue(name: str, level: LevelType) -> int:
        """
         Gets the value of an @link  Options::OptionTypeInt   Options::OptionTypeInt @endlink  option at the specified level. 
                    Throws an error if the option is not of type @link  Options::OptionTypeInt   Options::OptionTypeInt @endlink .
                
         @return value (int):  Option value .
        """
        pass
    
    ##  Gets the value of a @link  Options::OptionTypeLogical   Options::OptionTypeLogical @endlink  option. 
    ##             Throws an error if the option is not of type @link  Options::OptionTypeLogical   Options::OptionTypeLogical @endlink . 
    ##  @return value (bool):  Option value. .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="name"> (str)  Option name. </param>
    @overload
    def GetLogicalValue(name: str) -> bool:
        """
         Gets the value of a @link  Options::OptionTypeLogical   Options::OptionTypeLogical @endlink  option. 
                    Throws an error if the option is not of type @link  Options::OptionTypeLogical   Options::OptionTypeLogical @endlink . 
         @return value (bool):  Option value. .
        """
        pass
    
    ##  Gets the value of a @link  Options::OptionTypeLogical   Options::OptionTypeLogical @endlink  option at the specified level.  
    ##             Throws an error if the option is not of type @link  Options::OptionTypeLogical   Options::OptionTypeLogical @endlink .
    ##         
    ##  @return value (bool):  Option value .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="name"> (str)  Option name. </param>
    ## <param name="level"> (@link LevelType NXOpen.Options.LevelType@endlink)  Options level. </param>
    @overload
    def GetLogicalValue(name: str, level: LevelType) -> bool:
        """
         Gets the value of a @link  Options::OptionTypeLogical   Options::OptionTypeLogical @endlink  option at the specified level.  
                    Throws an error if the option is not of type @link  Options::OptionTypeLogical   Options::OptionTypeLogical @endlink .
                
         @return value (bool):  Option value .
        """
        pass
    
    ##  Returns an option's type. 
    ##  @return type (@link OptionType NXOpen.Options.OptionType@endlink):  Option type .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="name"> (str)  Option name </param>
    def GetOptionType(name: str) -> OptionType:
        """
         Returns an option's type. 
         @return type (@link OptionType NXOpen.Options.OptionType@endlink):  Option type .
        """
        pass
    
    ##  Gets the value of a @link  Options::OptionTypeReal   Options::OptionTypeReal @endlink  option. 
    ##             Throws an error if the option is not of type @link  Options::OptionTypeReal   Options::OptionTypeReal @endlink .
    ##          
    ##  @return value (float):  Option value. .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="name"> (str)  Option name. </param>
    @overload
    def GetRealValue(name: str) -> float:
        """
         Gets the value of a @link  Options::OptionTypeReal   Options::OptionTypeReal @endlink  option. 
                    Throws an error if the option is not of type @link  Options::OptionTypeReal   Options::OptionTypeReal @endlink .
                 
         @return value (float):  Option value. .
        """
        pass
    
    ##  Gets the value of a @link  Options::OptionTypeReal   Options::OptionTypeReal @endlink  option at the specified level. 
    ##             Throws an error if the option is not of type @link  Options::OptionTypeReal   Options::OptionTypeReal @endlink .
    ##         
    ##  @return value (float):  Option value .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="name"> (str)  Option name. </param>
    ## <param name="level"> (@link LevelType NXOpen.Options.LevelType@endlink)  Options level. </param>
    @overload
    def GetRealValue(name: str, level: LevelType) -> float:
        """
         Gets the value of a @link  Options::OptionTypeReal   Options::OptionTypeReal @endlink  option at the specified level. 
                    Throws an error if the option is not of type @link  Options::OptionTypeReal   Options::OptionTypeReal @endlink .
                
         @return value (float):  Option value .
        """
        pass
    
    ##  Gets the value of a @link  Options::OptionTypeReorderSelList   Options::OptionTypeReorderSelList @endlink  option. 
    ##             Throws an error if the option is not of type @link  Options::OptionTypeReorderSelList   Options::OptionTypeReorderSelList @endlink .
    ##         
    ##  @return A tuple consisting of (value, selection). 
    ##  - value is: List[str]. Option value .
    ##  - selection is: List[bool]. the selection bit .

    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## <param name="name"> (str)  Option name. </param>
    @overload
    def GetReorderSelectableStringListValue(name: str) -> Tuple[List[str], List[bool]]:
        """
         Gets the value of a @link  Options::OptionTypeReorderSelList   Options::OptionTypeReorderSelList @endlink  option. 
                    Throws an error if the option is not of type @link  Options::OptionTypeReorderSelList   Options::OptionTypeReorderSelList @endlink .
                
         @return A tuple consisting of (value, selection). 
         - value is: List[str]. Option value .
         - selection is: List[bool]. the selection bit .

        """
        pass
    
    ##  Gets the value of a @link  Options::OptionTypeReorderSelList   Options::OptionTypeReorderSelList @endlink  option at the specified level. 
    ##             Throws an error if the option is not of type @link  Options::OptionTypeReorderSelList   Options::OptionTypeReorderSelList @endlink .
    ##         
    ##  @return A tuple consisting of (value, selection). 
    ##  - value is: List[str]. Option value .
    ##  - selection is: List[bool]. the selection bit .

    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## <param name="name"> (str)  Option name. </param>
    ## <param name="level"> (@link LevelType NXOpen.Options.LevelType@endlink)  Options level. </param>
    @overload
    def GetReorderSelectableStringListValue(name: str, level: LevelType) -> Tuple[List[str], List[bool]]:
        """
         Gets the value of a @link  Options::OptionTypeReorderSelList   Options::OptionTypeReorderSelList @endlink  option at the specified level. 
                    Throws an error if the option is not of type @link  Options::OptionTypeReorderSelList   Options::OptionTypeReorderSelList @endlink .
                
         @return A tuple consisting of (value, selection). 
         - value is: List[str]. Option value .
         - selection is: List[bool]. the selection bit .

        """
        pass
    
    ##  Returns scope of an option.
    ##         
    ##  @return scopeValue (@link OptionsScope NXOpen.Options.OptionsScope@endlink):  Option scope .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## <param name="name"> (str)  Option name </param>
    def GetScope(name: str) -> OptionsScope:
        """
         Returns scope of an option.
                
         @return scopeValue (@link OptionsScope NXOpen.Options.OptionsScope@endlink):  Option scope .
        """
        pass
    
    ##  Gets the value of a @link  Options::OptionTypeStringList   Options::OptionTypeStringList @endlink  option. 
    ##             Throws an error if the option is not of type @link  Options::OptionTypeStringList   Options::OptionTypeStringList @endlink .
    ##         
    ##  @return value (List[str]):  Option value. .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="name"> (str)  Option name. </param>
    @overload
    def GetStringListValue(name: str) -> List[str]:
        """
         Gets the value of a @link  Options::OptionTypeStringList   Options::OptionTypeStringList @endlink  option. 
                    Throws an error if the option is not of type @link  Options::OptionTypeStringList   Options::OptionTypeStringList @endlink .
                
         @return value (List[str]):  Option value. .
        """
        pass
    
    ##  Gets the value of a @link  Options::OptionTypeStringList   Options::OptionTypeStringList @endlink  option at the specified level. 
    ##             Throws an error if the option is not of type @link  Options::OptionTypeStringList   Options::OptionTypeStringList @endlink .
    ##         
    ##  @return value (List[str]):  Option value .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="name"> (str)  Option name. </param>
    ## <param name="level"> (@link LevelType NXOpen.Options.LevelType@endlink)  Options level. </param>
    @overload
    def GetStringListValue(name: str, level: LevelType) -> List[str]:
        """
         Gets the value of a @link  Options::OptionTypeStringList   Options::OptionTypeStringList @endlink  option at the specified level. 
                    Throws an error if the option is not of type @link  Options::OptionTypeStringList   Options::OptionTypeStringList @endlink .
                
         @return value (List[str]):  Option value .
        """
        pass
    
    ##  Gets the value of a @link  Options::OptionTypeString   Options::OptionTypeString @endlink  option. 
    ##             Throws an error if the option is not of type @link  Options::OptionTypeString   Options::OptionTypeString @endlink .
    ##         
    ##  @return value (str):  Option value. .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="name"> (str)  Option name. </param>
    @overload
    def GetStringValue(name: str) -> str:
        """
         Gets the value of a @link  Options::OptionTypeString   Options::OptionTypeString @endlink  option. 
                    Throws an error if the option is not of type @link  Options::OptionTypeString   Options::OptionTypeString @endlink .
                
         @return value (str):  Option value. .
        """
        pass
    
    ##  Gets the value of a @link  Options::OptionTypeString   Options::OptionTypeString @endlink  option at the specified level. 
    ##             Throws an error if the option is not of type @link  Options::OptionTypeString   Options::OptionTypeString @endlink .
    ##         
    ##  @return value (str):  Option value .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="name"> (str)  Option name. </param>
    ## <param name="level"> (@link LevelType NXOpen.Options.LevelType@endlink)  Options level. </param>
    @overload
    def GetStringValue(name: str, level: LevelType) -> str:
        """
         Gets the value of a @link  Options::OptionTypeString   Options::OptionTypeString @endlink  option at the specified level. 
                    Throws an error if the option is not of type @link  Options::OptionTypeString   Options::OptionTypeString @endlink .
                
         @return value (str):  Option value .
        """
        pass
    
    ##  Returns then user comment at the specified level. User comments are not supported at the @link  Options::LevelTypeShipped   Options::LevelTypeShipped @endlink  level. 
    ##  @return comment (str):  User comment text. .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="name"> (str)  Option name </param>
    ## <param name="level"> (@link LevelType NXOpen.Options.LevelType@endlink)  Options level. </param>
    def GetUserComment(name: str, level: LevelType) -> str:
        """
         Returns then user comment at the specified level. User comments are not supported at the @link  Options::LevelTypeShipped   Options::LevelTypeShipped @endlink  level. 
         @return comment (str):  User comment text. .
        """
        pass
    
    ##  Gets the value of a @link  Options::OptionTypeUtf8string   Options::OptionTypeUtf8string @endlink  option. 
    ##             Throws an error if the option is not of type @link  Options::OptionTypeUtf8string   Options::OptionTypeUtf8string @endlink .
    ##         
    ##  @return utf8_value (str):  Option utf8 value. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## <param name="name"> (str)  Option name. </param>
    @overload
    def GetUtf8stringValue(name: str) -> str:
        """
         Gets the value of a @link  Options::OptionTypeUtf8string   Options::OptionTypeUtf8string @endlink  option. 
                    Throws an error if the option is not of type @link  Options::OptionTypeUtf8string   Options::OptionTypeUtf8string @endlink .
                
         @return utf8_value (str):  Option utf8 value. .
        """
        pass
    
    ##  Gets the value of a @link  Options::OptionTypeUtf8string   Options::OptionTypeUtf8string @endlink  option at the specified level. 
    ##             Throws an error if the option is not of type @link  Options::OptionTypeString   Options::OptionTypeString @endlink .
    ##         
    ##  @return value (str):  Option value .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## <param name="name"> (str)  Option name. </param>
    ## <param name="level"> (@link LevelType NXOpen.Options.LevelType@endlink)  Options level. </param>
    @overload
    def GetUtf8stringValue(name: str, level: LevelType) -> str:
        """
         Gets the value of a @link  Options::OptionTypeUtf8string   Options::OptionTypeUtf8string @endlink  option at the specified level. 
                    Throws an error if the option is not of type @link  Options::OptionTypeString   Options::OptionTypeString @endlink .
                
         @return value (str):  Option value .
        """
        pass
    
    ##  Returns true if the option's values at the specified level are locked by default.
    ##             Locked by default means that if an option value does not exist at this level, 
    ##             then it is locked.
    ##         
    ##  @return status (bool):  True if options values are locked by default .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="level"> (@link LevelType NXOpen.Options.LevelType@endlink)  Options level. </param>
    def IsLevelLockedByDefault(level: LevelType) -> bool:
        """
         Returns true if the option's values at the specified level are locked by default.
                    Locked by default means that if an option value does not exist at this level, 
                    then it is locked.
                
         @return status (bool):  True if options values are locked by default .
        """
        pass
    
    ##  Returns true if the option value is locked at the specified level. 
    ##             Locks are not supported at @link  Options::LevelTypeUser   Options::LevelTypeUser @endlink  and @link  Options::LevelTypeShipped   Options::LevelTypeShipped @endlink  levels. 
    ##  @return status (bool):  Lock status .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="name"> (str)  Option name </param>
    ## <param name="level"> (@link LevelType NXOpen.Options.LevelType@endlink)  Options level. </param>
    def IsValueLocked(name: str, level: LevelType) -> bool:
        """
         Returns true if the option value is locked at the specified level. 
                    Locks are not supported at @link  Options::LevelTypeUser   Options::LevelTypeUser @endlink  and @link  Options::LevelTypeShipped   Options::LevelTypeShipped @endlink  levels. 
         @return status (bool):  Lock status .
        """
        pass
    
    ##  Returns true if the option value exists at the specified level. Always true for the @link  Options::LevelTypeShipped   Options::LevelTypeShipped @endlink  level. 
    ##  @return status (bool):  True if value is set .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="name"> (str)  Option name </param>
    ## <param name="level"> (@link LevelType NXOpen.Options.LevelType@endlink)  Options level. </param>
    def IsValueSet(name: str, level: LevelType) -> bool:
        """
         Returns true if the option value exists at the specified level. Always true for the @link  Options::LevelTypeShipped   Options::LevelTypeShipped @endlink  level. 
         @return status (bool):  True if value is set .
        """
        pass
    
    ##  Creates an instance of @link  NXOpen::Options::ChangeList   NXOpen::Options::ChangeList @endlink  class, in order to edit a set of options. 
    ##         It is not possible to create an instance of @link  NXOpen::Options::ChangeList   NXOpen::Options::ChangeList @endlink  for @link  Options::LevelTypeShipped   Options::LevelTypeShipped @endlink  level, 
    ##         or for a level that is not defined or is not writeable.  
    ##  @return data (@link ChangeList NXOpen.Options.ChangeList@endlink):  An instanse of @link  NXOpen::Options::ChangeList   NXOpen::Options::ChangeList @endlink  class .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="level"> (@link LevelType NXOpen.Options.LevelType@endlink)  Options level.  </param>
    ## <param name="locked_by_default"> (@link LevelLockedByDefault NXOpen.Options.LevelLockedByDefault@endlink)  Specifies whether Options level is locked by default. 
    ##             Ignored at @link  Options::LevelTypeUser   Options::LevelTypeUser @endlink  level as locks at @link  Options::LevelTypeUser   Options::LevelTypeUser @endlink  level are not supported. 
    ##             If specified default lock status is different from the current one, then all exisitng locks are cleared.  </param>
    def NewOptionsChangeList(level: LevelType, locked_by_default: LevelLockedByDefault) -> ChangeList:
        """
         Creates an instance of @link  NXOpen::Options::ChangeList   NXOpen::Options::ChangeList @endlink  class, in order to edit a set of options. 
                It is not possible to create an instance of @link  NXOpen::Options::ChangeList   NXOpen::Options::ChangeList @endlink  for @link  Options::LevelTypeShipped   Options::LevelTypeShipped @endlink  level, 
                or for a level that is not defined or is not writeable.  
         @return data (@link ChangeList NXOpen.Options.ChangeList@endlink):  An instanse of @link  NXOpen::Options::ChangeList   NXOpen::Options::ChangeList @endlink  class .
        """
        pass
    
    ##  Creates an instance of @link  NXOpen::Options::DraftingStandardChangeList   NXOpen::Options::DraftingStandardChangeList @endlink  class, in order to edit a set of options. 
    ##         It is not possible to create an instance of @link  NXOpen::Options::DraftingStandardChangeList   NXOpen::Options::DraftingStandardChangeList @endlink  for @link  Options::LevelTypeShipped   Options::LevelTypeShipped @endlink  level, 
    ##         or for a level that is not defined or is not writeable.  
    ##  @return data (@link DraftingStandardChangeList NXOpen.Options.DraftingStandardChangeList@endlink):  An instanse of @link  NXOpen::Options::DraftingStandardChangeList   NXOpen::Options::DraftingStandardChangeList @endlink  class .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="level"> (@link LevelType NXOpen.Options.LevelType@endlink)  Options level.  </param>
    ## <param name="filename"> (str)  Specifies the filename to save/save as.</param>
    def NewOptionsDraftingStandardChangeList(level: LevelType, filename: str) -> DraftingStandardChangeList:
        """
         Creates an instance of @link  NXOpen::Options::DraftingStandardChangeList   NXOpen::Options::DraftingStandardChangeList @endlink  class, in order to edit a set of options. 
                It is not possible to create an instance of @link  NXOpen::Options::DraftingStandardChangeList   NXOpen::Options::DraftingStandardChangeList @endlink  for @link  Options::LevelTypeShipped   Options::LevelTypeShipped @endlink  level, 
                or for a level that is not defined or is not writeable.  
         @return data (@link DraftingStandardChangeList NXOpen.Options.DraftingStandardChangeList@endlink):  An instanse of @link  NXOpen::Options::DraftingStandardChangeList   NXOpen::Options::DraftingStandardChangeList @endlink  class .
        """
        pass
    
##  Represents the scope of an option. 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Part</term><description> 
##  Option scope is part </description> </item><item><term> 
## Session</term><description> 
##  Option scope is session </description> </item></list>
class OptionsScope(Enum):
    """
    Members Include: <Part> <Session>
    """
    Part: int
    Session: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> OptionsScope:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Describes type of an option. 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Int</term><description> 
##  Option value is an integer number </description> </item><item><term> 
## Real</term><description> 
##  Option value is a real number </description> </item><item><term> 
## String</term><description> 
##  Option value is an ascii string </description> </item><item><term> 
## StringList</term><description> 
##  Option value is a list of ascii strings </description> </item><item><term> 
## Logical</term><description> 
##  Option value is logical </description> </item><item><term> 
## Utf8string</term><description> 
##  Option value is a utf8 string </description> </item><item><term> 
## Utf8stringList</term><description> 
##  Option value is a list of utf8 strings </description> </item><item><term> 
## ReorderSelList</term><description> 
##  Option value is a list which can be selected and re-ordered </description> </item></list>
class OptionType(Enum):
    """
    Members Include: <Int> <Real> <String> <StringList> <Logical> <Utf8string> <Utf8stringList> <ReorderSelList>
    """
    Int: int
    Real: int
    String: int
    StringList: int
    Logical: int
    Utf8string: int
    Utf8stringList: int
    ReorderSelList: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> OptionType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


## @package NXOpen.Options
## Classes, Enums and Structs under NXOpen.Options namespace

