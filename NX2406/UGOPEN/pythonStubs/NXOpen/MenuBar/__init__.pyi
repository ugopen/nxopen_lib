from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Implements the properties for the Addons 
## 
##   <br>  Created in NX2312.0.0  <br> 

class AddonProperties(NXOpen.TransientObject): 
    """ Implements the properties for the Addons """


    ##  Frees the object from memory.  After this method is
    ##         called, it is illegal to use the object.  In .NET and Java,
    ##         his method is automatically called when the object is
    ##         deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is
                called, it is illegal to use the object.  In .NET and Java,
                his method is automatically called when the object is
                deleted by the garbage collector.  
        """
        pass
    
    ##  This addon saves the setting of the add-on toggle button across sessions. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="save_toggle_state"> (bool)  This addon state will be saved across sessions </param>
    def SaveToggleState(self, save_toggle_state: bool) -> None:
        """
         This addon saves the setting of the add-on toggle button across sessions. 
        """
        pass
    
    ##  This addon sets the specified ribbon as the active tab when the add-on toggle is set 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="set_tab_active_on_toggle"> (bool)  This addon ribbon is set to the active tab when the toggle is set </param>
    def SetTabActiveOnToggle(self, set_tab_active_on_toggle: bool) -> None:
        """
         This addon sets the specified ribbon as the active tab when the add-on toggle is set 
        """
        pass
    
import NXOpen
##  Implements the properties for the Menu Applications 
## 
##   <br>  Created in NX1847.0.0  <br> 

class ApplicationProperties(NXOpen.TransientObject): 
    """ Implements the properties for the Menu Applications """


    ##  This application allows the display of multiple different parts in separate graphics windows at the same time. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="allows_multiple_window_designs"> (bool)  This application allows multiple different parts </param>
    def AllowsMultipleWindowDesigns(self, allows_multiple_window_designs: bool) -> None:
        """
         This application allows the display of multiple different parts in separate graphics windows at the same time. 
        """
        pass
    
    ##  This application allows more than one graphics window of the same displayed part (as in Windows->New Window). 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="allows_multiple_window_views"> (bool)  This application allows multiple window views </param>
    def AllowsMultipleWindowViews(self, allows_multiple_window_views: bool) -> None:
        """
         This application allows more than one graphics window of the same displayed part (as in Windows->New Window). 
        """
        pass
    
    ##  This application allows undo over an application. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="allows_undo_over_application_change"> (bool)  This application allows an undo over application change </param>
    def AllowsUndoOverApplicationChange(self, allows_undo_over_application_change: bool) -> None:
        """
         This application allows undo over an application. 
        """
        pass
    
    ##  Frees the object from memory.  After this method is
    ##         called, it is illegal to use the object.  In .NET and Java,
    ##         his method is automatically called when the object is
    ##         deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is
                called, it is illegal to use the object.  In .NET and Java,
                his method is automatically called when the object is
                deleted by the garbage collector.  
        """
        pass
    
    ##  Sets whether this application supports design-in-context.
    ##         
    ##             Applications supporting design-in-context allow the
    ##             work part to be set to one of the components of a displayed
    ##             assembly. For applications that do not support design-in-context,
    ##             the work part will always be the same as the displayed part. 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="supports_design_in_context"> (bool)  This application supports design-in-context </param>
    def SupportsDesignInContext(self, supports_design_in_context: bool) -> None:
        """
         Sets whether this application supports design-in-context.
                
                    Applications supporting design-in-context allow the
                    work part to be set to one of the components of a displayed
                    assembly. For applications that do not support design-in-context,
                    the work part will always be the same as the displayed part. 
        """
        pass
    
    ##  This application supports drawings. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="supports_drawings"> (bool)  This application support drawings </param>
    def SupportsDrawings(self, supports_drawings: bool) -> None:
        """
         This application supports drawings. 
        """
        pass
    
    ##  This application supports undo within in the application. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="supports_undo"> (bool)  This application support undo within in the application </param>
    def SupportsUndoWithinApplication(self, supports_undo: bool) -> None:
        """
         This application supports undo within in the application. 
        """
        pass
    
import NXOpen
##  Represents an entry on a context menu. 
## 
##   <br>  Created in NX8.5.0  <br> 

class ContextMenuEntry(NXOpen.TransientObject): 
    """ Represents an entry on a context menu. """


    ##  Specifies the type of the menu entry. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Submenu</term><description> 
    ##  Has an attached menu structure containing more entries. </description> </item><item><term> 
    ## PushButton</term><description> 
    ##  Has a command that is run when this entry is activated. </description> </item><item><term> 
    ## ToggleButton</term><description> 
    ##  Displays an On/Off state. </description> </item><item><term> 
    ## Separator</term><description> 
    ##  A visual divider between sections of the menu. </description> </item><item><term> 
    ## Label</term><description> 
    ##  A label often used to divide and provide context to sub-groups of commands. </description> </item></list>
    class Type(Enum):
        """
        Members Include: <Submenu> <PushButton> <ToggleButton> <Separator> <Label>
        """
        Submenu: int
        PushButton: int
        ToggleButton: int
        Separator: int
        Label: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ContextMenuEntry.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link ContextMenuEntry.Type NXOpen.MenuBar.ContextMenuEntry.Type@endlink) EntryType
    ##  Returns the type of this menu entry.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return ContextMenuEntry.Type
    @property
    def EntryType(self) -> ContextMenuEntry.Type:
        """
        Getter for property: (@link ContextMenuEntry.Type NXOpen.MenuBar.ContextMenuEntry.Type@endlink) EntryType
         Returns the type of this menu entry.  
             
         
        """
        pass
    
    ## Getter for property: (bool) IsDefault
    ##  Returns true if this entry is the default action for the menu.  
    ##    A menu entry is marked as
    ##             the default for the menu when it corresponds to the double-click 
    ##             action.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def IsDefault(self) -> bool:
        """
        Getter for property: (bool) IsDefault
         Returns true if this entry is the default action for the menu.  
           A menu entry is marked as
                    the default for the menu when it corresponds to the double-click 
                    action.
                  
         
        """
        pass
    
    ## Getter for property: (bool) IsHidden
    ##  Returns true if this entry is hidden on the menu.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def IsHidden(self) -> bool:
        """
        Getter for property: (bool) IsHidden
         Returns true if this entry is hidden on the menu.  
             
         
        """
        pass
    
    ## Getter for property: (bool) IsSensitive
    ##  Returns true if the command corresponding to this entry can be run.  
    ##    
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def IsSensitive(self) -> bool:
        """
        Getter for property: (bool) IsSensitive
         Returns true if the command corresponding to this entry can be run.  
           
                  
         
        """
        pass
    
    ## Getter for property: (str) Label
    ##  Returns the label of this menu entry.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Label(self) -> str:
        """
        Getter for property: (str) Label
         Returns the label of this menu entry.  
             
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the name of this menu entry.  
    ##    
    ##         
    ##             Some entries on the context menu may correspond to buttons on the menu bar.
    ##             For these entries, the name that is returned is the name of that 
    ##             @link MenuBar::MenuButton MenuBar::MenuButton@endlink  object.
    ##             
    ##             For all other entries which do not correspond to a menu bar button, the
    ##             name that is returned has no specific meaning. However, for any individual 
    ##             action within any specific context menu, the name that is assigned to
    ##             that action will not change.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name of this menu entry.  
           
                
                    Some entries on the context menu may correspond to buttons on the menu bar.
                    For these entries, the name that is returned is the name of that 
                    @link MenuBar::MenuButton MenuBar::MenuButton@endlink  object.
                    
                    For all other entries which do not correspond to a menu bar button, the
                    name that is returned has no specific meaning. However, for any individual 
                    action within any specific context menu, the name that is assigned to
                    that action will not change.
                  
         
        """
        pass
    
    ##  Frees the object from memory.  After this method is called,
    ##             it is illegal to use the object.  In .NET, this method is automatically
    ##             called when the object is deleted by the garbage collector. 
    ##         
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                    it is illegal to use the object.  In .NET, this method is automatically
                    called when the object is deleted by the garbage collector. 
                
        """
        pass
    
import NXOpen
##  Provides information about the MenuBar.ContextMenu object being customized. 
## 
##   <br>  Created in NX8.5.0  <br> 

class ContextMenuProperties(NXOpen.TransientObject): 
    """ Provides information about the MenuBar.ContextMenu object being customized. """


    ## Getter for property: (str) Context
    ##  Returns a description for the context for which the menu was created   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Context(self) -> str:
        """
        Getter for property: (str) Context
         Returns a description for the context for which the menu was created   
            
         
        """
        pass
    
    ## Getter for property: (str) Location
    ##  Returns the location where the context menu will be displayed   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Location(self) -> str:
        """
        Getter for property: (str) Location
         Returns the location where the context menu will be displayed   
            
         
        """
        pass
    
    ##  Frees the object from memory.  After this method is called,
    ##             it is illegal to use the object.  In .NET, this method is automatically
    ##             called when the object is deleted by the garbage collector. 
    ##         
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                    it is illegal to use the object.  In .NET, this method is automatically
                    called when the object is deleted by the garbage collector. 
                
        """
        pass
    
import NXOpen
##  Represents a Context Menu 
## 
##   <br>  Created in NX8.5.0  <br> 

class ContextMenu(NXOpen.TransientObject): 
    """ Represents a Context Menu """


    ## Getter for property: (int) NumberOfEntries
    ##  Returns the number of @link MenuBar::ContextMenuEntry MenuBar::ContextMenuEntry@endlink  objects in this menu.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def NumberOfEntries(self) -> int:
        """
        Getter for property: (int) NumberOfEntries
         Returns the number of @link MenuBar::ContextMenuEntry MenuBar::ContextMenuEntry@endlink  objects in this menu.  
             
         
        """
        pass
    
    ##  Adds a menu bar button to the context menu. Use 
    ##             @link MenuBar::MenuBarManager::GetButtonFromName MenuBar::MenuBarManager::GetButtonFromName@endlink  
    ##             to find the button to add to the menu.
    ##         
    ##  @return entry (@link ContextMenuEntry NXOpen.MenuBar.ContextMenuEntry@endlink):  the new menu entry .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="button"> (@link MenuButton NXOpen.MenuBar.MenuButton@endlink)  the menu bar button to add to the menu </param>
    ## <param name="index"> (int)  position at which to create the new button. Use -1 to add the button to the end of the menu. </param>
    def AddMenuButton(self, button: MenuButton, index: int) -> ContextMenuEntry:
        """
         Adds a menu bar button to the context menu. Use 
                    @link MenuBar::MenuBarManager::GetButtonFromName MenuBar::MenuBarManager::GetButtonFromName@endlink  
                    to find the button to add to the menu.
                
         @return entry (@link ContextMenuEntry NXOpen.MenuBar.ContextMenuEntry@endlink):  the new menu entry .
        """
        pass
    
    ##  Adds a label to the context menu. 
    ##  @return entry (@link ContextMenuEntry NXOpen.MenuBar.ContextMenuEntry@endlink):  the new menu entry .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="label"> (str)  label for the label entry </param>
    ## <param name="index"> (int)  position at which to create the label entry. Use -1 to add the label to the end of the menu. </param>
    def AddMenuLabel(self, label: str, index: int) -> ContextMenuEntry:
        """
         Adds a label to the context menu. 
         @return entry (@link ContextMenuEntry NXOpen.MenuBar.ContextMenuEntry@endlink):  the new menu entry .
        """
        pass
    
    ##  Adds a separator to the context menu. 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  position at which to create the separator. Use -1 to add the separator to the end of the menu. </param>
    def AddSeparator(self, index: int) -> None:
        """
         Adds a separator to the context menu. 
        """
        pass
    
    ##  Adds a submenu to the context menu. 
    ##  @return submenu (@link ContextMenu NXOpen.MenuBar.ContextMenu@endlink):  the new submenu .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="label"> (str)  label for the cascade menu </param>
    ## <param name="index"> (int)  position at which to create the sub-menu. Use -1 to add the sub-menu to the end of the menu. </param>
    def AddSubmenu(self, label: str, index: int) -> ContextMenu:
        """
         Adds a submenu to the context menu. 
         @return submenu (@link ContextMenu NXOpen.MenuBar.ContextMenu@endlink):  the new submenu .
        """
        pass
    
    ##  Frees the object from memory.  After this method is called,
    ##             it is illegal to use the object.  In .NET, this method is automatically
    ##             called when the object is deleted by the garbage collector. 
    ##         
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                    it is illegal to use the object.  In .NET, this method is automatically
                    called when the object is deleted by the garbage collector. 
                
        """
        pass
    
    ##  Returns the @link MenuBar::ContextMenuEntry MenuBar::ContextMenuEntry@endlink  at the specified index in the menu. 
    ##  @return entry (@link ContextMenuEntry NXOpen.MenuBar.ContextMenuEntry@endlink):  the menu entry at this position .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  index of menu entry to return </param>
    def GetEntry(self, index: int) -> ContextMenuEntry:
        """
         Returns the @link MenuBar::ContextMenuEntry MenuBar::ContextMenuEntry@endlink  at the specified index in the menu. 
         @return entry (@link ContextMenuEntry NXOpen.MenuBar.ContextMenuEntry@endlink):  the menu entry at this position .
        """
        pass
    
    ##  Given the name of a menu entry, returns the first
    ##             @link MenuBar::ContextMenuEntry MenuBar::ContextMenuEntry@endlink  in this menu which
    ##             matches. 
    ##         
    ##  @return entry (@link ContextMenuEntry NXOpen.MenuBar.ContextMenuEntry@endlink):  the menu entry with this name .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="name"> (str)  name of menu entry to search for </param>
    def GetEntryWithName(self, name: str) -> ContextMenuEntry:
        """
         Given the name of a menu entry, returns the first
                    @link MenuBar::ContextMenuEntry MenuBar::ContextMenuEntry@endlink  in this menu which
                    matches. 
                
         @return entry (@link ContextMenuEntry NXOpen.MenuBar.ContextMenuEntry@endlink):  the menu entry with this name .
        """
        pass
    
    ##  Returns the index of the @link MenuBar::ContextMenuEntry MenuBar::ContextMenuEntry@endlink 
    ##             object within this menu.
    ##         
    ##  @return index (int):  the index for that menu entry .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="entry"> (@link ContextMenuEntry NXOpen.MenuBar.ContextMenuEntry@endlink)  an entry in the menu </param>
    def GetIndexOfEntry(self, entry: ContextMenuEntry) -> int:
        """
         Returns the index of the @link MenuBar::ContextMenuEntry MenuBar::ContextMenuEntry@endlink 
                    object within this menu.
                
         @return index (int):  the index for that menu entry .
        """
        pass
    
    ##  Returns the submenu for the entry at the specified index in the menu. 
    ##             The menu entry at this index must be of type 
    ##             @link MenuBar::ContextMenuEntry::TypeSubmenu MenuBar::ContextMenuEntry::TypeSubmenu@endlink .
    ##          
    ##  @return submenu (@link ContextMenu NXOpen.MenuBar.ContextMenu@endlink):  the submenu at this position .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  index of submenu to return </param>
    def GetSubmenu(self, index: int) -> ContextMenu:
        """
         Returns the submenu for the entry at the specified index in the menu. 
                    The menu entry at this index must be of type 
                    @link MenuBar::ContextMenuEntry::TypeSubmenu MenuBar::ContextMenuEntry::TypeSubmenu@endlink .
                 
         @return submenu (@link ContextMenu NXOpen.MenuBar.ContextMenu@endlink):  the submenu at this position .
        """
        pass
    
    ##  Indicates whether or not this menu contains a 
    ##             @link MenuBar::ContextMenuEntry MenuBar::ContextMenuEntry@endlink  which 
    ##             has the given name.
    ##         
    ##  @return exists (bool):  the menu entry with this name .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="name"> (str)  name of menu entry to search for </param>
    def HasEntryWithName(self, name: str) -> bool:
        """
         Indicates whether or not this menu contains a 
                    @link MenuBar::ContextMenuEntry MenuBar::ContextMenuEntry@endlink  which 
                    has the given name.
                
         @return exists (bool):  the menu entry with this name .
        """
        pass
    
    ##  Prevents the indicated menu entry from being shown on the menu. 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="entry"> (@link ContextMenuEntry NXOpen.MenuBar.ContextMenuEntry@endlink)  the menu entry to hide </param>
    def HideEntry(self, entry: ContextMenuEntry) -> None:
        """
         Prevents the indicated menu entry from being shown on the menu. 
        """
        pass
    
    ##  Reorders the menu to move a menu entry to a new position in the list. 
    ##         
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="entry"> (@link ContextMenuEntry NXOpen.MenuBar.ContextMenuEntry@endlink)  the menu entry to be moved </param>
    ## <param name="index"> (int)  the new position </param>
    def MoveEntry(self, entry: ContextMenuEntry, index: int) -> None:
        """
         Reorders the menu to move a menu entry to a new position in the list. 
                
        """
        pass
    
    ##  Makes a specified menu entry the default for the menu. 
    ##         
    ##             This entry will be displayed in bold text on the menu. It will be the action
    ##             that is performed in response to a double-click event in the UI.
    ##             
    ##             The menu entry must have a type of @link MenuBar::ContextMenuEntry::TypePushButton MenuBar::ContextMenuEntry::TypePushButton@endlink 
    ##             or @link MenuBar::ContextMenuEntry::TypeToggleButton MenuBar::ContextMenuEntry::TypeToggleButton@endlink . 
    ##         
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="entry"> (@link ContextMenuEntry NXOpen.MenuBar.ContextMenuEntry@endlink)  the menu entry to become the default for the menu </param>
    def SetDefaultEntry(self, entry: ContextMenuEntry) -> None:
        """
         Makes a specified menu entry the default for the menu. 
                
                    This entry will be displayed in bold text on the menu. It will be the action
                    that is performed in response to a double-click event in the UI.
                    
                    The menu entry must have a type of @link MenuBar::ContextMenuEntry::TypePushButton MenuBar::ContextMenuEntry::TypePushButton@endlink 
                    or @link MenuBar::ContextMenuEntry::TypeToggleButton MenuBar::ContextMenuEntry::TypeToggleButton@endlink . 
                
        """
        pass
    
import NXOpen
##  Interface for the MenuBarManager object  <br> To obtain an instance of this class, refer to @link NXOpen::UI  NXOpen::UI @endlink  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class MenuBarManager(NXOpen.Object): 
    """ Interface for the MenuBarManager object """


    ##  Return values for action callbacks 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Continue</term><description> 
    ##  Continue performing the menu item's actions. </description> </item><item><term> 
    ## Cancel</term><description> 
    ##  User interaction requested inhibiting the 
    ##                                                                menu item's actions. </description> </item><item><term> 
    ## OverrideStandard</term><description> 
    ##  Inhibit further actions because a pre 
    ##                                                                           action took the place of the standard 
    ##                                                                           action for a standard NX menu item. </description> </item><item><term> 
    ## Warning</term><description> 
    ##  Inhibit further actions because a 
    ##                                                                 warning condition was raised. </description> </item><item><term> 
    ## Error</term><description> 
    ##  Inhibit further actions because a 
    ##                                                               error condition was raised. </description> </item></list>
    class CallbackStatus(Enum):
        """
        Members Include: <Continue> <Cancel> <OverrideStandard> <Warning> <Error>
        """
        Continue: int
        Cancel: int
        OverrideStandard: int
        Warning: int
        Error: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MenuBarManager.CallbackStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Return values for action callbacks 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Enter</term><description> 
    ##  An application has been entered. </description> </item><item><term> 
    ## TaskEnter</term><description> 
    ##  A task has been entered. </description> </item></list>
    class SwitchReason(Enum):
        """
        Members Include: <Enter> <TaskEnter>
        """
        Enter: int
        TaskEnter: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MenuBarManager.SwitchReason:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Prototype for the action callbacks 
    ## A callback definition with the following input arguments: 
    ##  - @link MenuButtonEvent NXOpen.MenuBar.MenuButtonEvent@endlink
    ##  and no return type
    ActionCallback = Callable[[MenuButtonEvent], None]
    
    
    ##  
    ##           Adds the action callback.
    ##          
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## <param name="name"> (str)  The name of the action.  This name must match the string used in the .men file. </param>
    ## <param name="action_callback"> (@link MenuBarManager.ActionCallback NXOpen.MenuBar.MenuBarManager.ActionCallback@endlink)  The method to execute for this action </param>
    def AddMenuAction(name: str, action_callback: MenuBarManager.ActionCallback) -> None:
        """
         
                  Adds the action callback.
                 
        """
        pass
    
    ##  Prototype for the add-on callback which is called when the registered application(s) for the add-on is initialized, entered and exited  
    ## A callback definition with the following input arguments: 
    ##  - str
    ##  and no return type
    AddOnCallback = Callable[[str], None]
    
    
    ##  Prototype for the add-on callback called when the add-on is toggled on or off 
    ## A callback definition with the following input arguments: 
    ##  - bool
    ##  and no return type
    AddOnToggleCallback = Callable[[bool], None]
    
    
    ##  Prototype for application switch callback 
    ## A callback definition with the following input arguments: 
    ##  - str
    ##  - @link MenuBarManager.SwitchReason NXOpen.MenuBar.MenuBarManager.SwitchReason@endlink
    ##  and no return type
    ApplicationSwitchNotify = Callable[[str, MenuBarManager.SwitchReason], None]
    
    
    ##  Prototype for the callback used to configure a context menu. 
    ##         
    ##             Return 0 to indicate successful processing of the menu. Any other value will
    ##             be treated as an error condition.
    ##         
    ## A callback definition with the following input arguments: 
    ##  - @link ContextMenu NXOpen.MenuBar.ContextMenu@endlink
    ##  - @link ContextMenuProperties NXOpen.MenuBar.ContextMenuProperties@endlink
    ##  and no return type
    ConfigureContextMenu = Callable[[ContextMenu, ContextMenuProperties], None]
    
    
    ##  Prototype for callback called whenever the application is entered 
    ## A callback definition with no input arguments and no return type
    EnterMenuApplication = Callable[[], None]
    
    
    ##  Prototype for callback called whenever the application is exited 
    ## A callback definition with no input arguments and no return type
    ExitMenuApplication = Callable[[], None]
    
    
    ##  
    ##           Returns the active toggle state of the add-on when a toggle button is utilized
    ##          
    ##  @return status (bool):  The toggle state of the add-on application.  .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## <param name="name"> (str)  The name of the add-on application.  </param>
    def GetAddOnToggleButton(name: str) -> bool:
        """
         
                  Returns the active toggle state of the add-on when a toggle button is utilized
                 
         @return status (bool):  The toggle state of the add-on application.  .
        """
        pass
    
    ##  Finds the MenuButton associated with the given name 
    ##  @return button (@link MenuButton NXOpen.MenuBar.MenuButton@endlink):  The button associated with the given name .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## <param name="name"> (str)  The name of the button.  This name must match the button name used in the .men file. </param>
    def GetButtonFromName(name: str) -> MenuButton:
        """
         Finds the MenuButton associated with the given name 
         @return button (@link MenuButton NXOpen.MenuBar.MenuButton@endlink):  The button associated with the given name .
        """
        pass
    
    ##  Prototype for application initialization callback 
    ## A callback definition with no input arguments and no return type
    InitializeMenuApplication = Callable[[], None]
    
    
    ##  Constructs a new AddonProperties object. 
    ##  @return data (@link AddonProperties NXOpen.MenuBar.AddonProperties@endlink):  .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    def NewAddOnProperties() -> AddonProperties:
        """
         Constructs a new AddonProperties object. 
         @return data (@link AddonProperties NXOpen.MenuBar.AddonProperties@endlink):  .
        """
        pass
    
    ##  Constructs a new ApplicationProperties object. 
    ##  @return data (@link ApplicationProperties NXOpen.MenuBar.ApplicationProperties@endlink):  .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def NewApplicationProperties() -> ApplicationProperties:
        """
         Constructs a new ApplicationProperties object. 
         @return data (@link ApplicationProperties NXOpen.MenuBar.ApplicationProperties@endlink):  .
        """
        pass
    
    ##  
    ##           Registers an add-on application
    ##          
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## <param name="name"> (str)  The name of the add-on application.  This name must match the toggle button used in the .men file if one exists. </param>
    ## <param name="application_name"> (List[str])  names of the applications to assign to the add-on </param>
    ## <param name="initialize_callback"> (@link MenuBarManager.AddOnCallback NXOpen.MenuBar.MenuBarManager.AddOnCallback@endlink)  The method called when initializing the add-on's registered application(s)</param>
    ## <param name="enter_callback"> (@link MenuBarManager.AddOnCallback NXOpen.MenuBar.MenuBarManager.AddOnCallback@endlink)  The method called when entering the add-on's registered application(s)</param>
    ## <param name="exit_callback"> (@link MenuBarManager.AddOnCallback NXOpen.MenuBar.MenuBarManager.AddOnCallback@endlink)  The method called when exiting the add-on's registered application(s)</param>
    ## <param name="toggle_callback"> (@link MenuBarManager.AddOnToggleCallback NXOpen.MenuBar.MenuBarManager.AddOnToggleCallback@endlink)  The method called when the add-on toggle has changed </param>
    ## <param name="add_on_properties"> (@link AddonProperties NXOpen.MenuBar.AddonProperties@endlink)  The add-on properties  </param>
    def RegisterAddOn(name: str, application_name: List[str], initialize_callback: MenuBarManager.AddOnCallback, enter_callback: MenuBarManager.AddOnCallback, exit_callback: MenuBarManager.AddOnCallback, toggle_callback: MenuBarManager.AddOnToggleCallback, add_on_properties: AddonProperties) -> None:
        """
         
                  Registers an add-on application
                 
        """
        pass
    
    ##  
    ##           Registers a menu to an add-on application
    ##          
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## <param name="name"> (str)  The name of the add-on application.  </param>
    ## <param name="menu_file"> (str)  The name of the add-on application.  </param>
    def RegisterAddOnMenuFile(name: str, menu_file: str) -> None:
        """
         
                  Registers a menu to an add-on application
                 
        """
        pass
    
    ##  
    ##           Registers a ribbon UI element to an add-on application
    ##          
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## <param name="name"> (str)  The name of the add-on application.  </param>
    ## <param name="ribbon_file"> (str)  The name of the add-on application.  </param>
    def RegisterAddOnRibbonFile(name: str, ribbon_file: str) -> None:
        """
         
                  Registers a ribbon UI element to an add-on application
                 
        """
        pass
    
    ##  
    ##           Registers the application
    ##          
    ##  @return application_id (int):  Unique identifier for the registered application .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## <param name="name"> (str)  The name of the application.  This name must match the string used in the .men file. </param>
    ## <param name="initialize_callback"> (@link MenuBarManager.InitializeMenuApplication NXOpen.MenuBar.MenuBarManager.InitializeMenuApplication@endlink)  The method used to initialize the application </param>
    ## <param name="enter_callback"> (@link MenuBarManager.EnterMenuApplication NXOpen.MenuBar.MenuBarManager.EnterMenuApplication@endlink)  The method called when entering the application </param>
    ## <param name="exit_callback"> (@link MenuBarManager.ExitMenuApplication NXOpen.MenuBar.MenuBarManager.ExitMenuApplication@endlink)  The method called when exiting the application </param>
    ## <param name="supports_drawings"> (bool)  Does this application support drawings? </param>
    ## <param name="supports_design_in_context"> (bool)  Does this application support design in context? </param>
    ## <param name="supports_undo"> (bool)  Does this application support undo? </param>
    @overload
    def RegisterApplication(name: str, initialize_callback: MenuBarManager.InitializeMenuApplication, enter_callback: MenuBarManager.EnterMenuApplication, exit_callback: MenuBarManager.ExitMenuApplication, supports_drawings: bool, supports_design_in_context: bool, supports_undo: bool) -> int:
        """
         
                  Registers the application
                 
         @return application_id (int):  Unique identifier for the registered application .
        """
        pass
    
    ##  Registers a callback for application switches.
    ##         
    ##  @return id (int):  Identifier of registered callback .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## <param name="switch_callback"> (@link MenuBarManager.ApplicationSwitchNotify NXOpen.MenuBar.MenuBarManager.ApplicationSwitchNotify@endlink)  The method to execute for this action </param>
    def RegisterApplicationSwitchCallback(switch_callback: MenuBarManager.ApplicationSwitchNotify) -> int:
        """
         Registers a callback for application switches.
                
         @return id (int):  Identifier of registered callback .
        """
        pass
    
    ##  
    ##           Registers the application
    ##          
    ##  @return application_id (int):  Unique identifier for the registered application .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## <param name="name"> (str)  The name of the application.  This name must match the string used in the .men file. </param>
    ## <param name="initialize_callback"> (@link MenuBarManager.InitializeMenuApplication NXOpen.MenuBar.MenuBarManager.InitializeMenuApplication@endlink)  The method used to initialize the application </param>
    ## <param name="enter_callback"> (@link MenuBarManager.EnterMenuApplication NXOpen.MenuBar.MenuBarManager.EnterMenuApplication@endlink)  The method called when entering the application </param>
    ## <param name="exit_callback"> (@link MenuBarManager.ExitMenuApplication NXOpen.MenuBar.MenuBarManager.ExitMenuApplication@endlink)  The method called when exiting the application </param>
    ## <param name="application"> (@link ApplicationProperties NXOpen.MenuBar.ApplicationProperties@endlink)  The application properties  </param>
    @overload
    def RegisterApplication(name: str, initialize_callback: MenuBarManager.InitializeMenuApplication, enter_callback: MenuBarManager.EnterMenuApplication, exit_callback: MenuBarManager.ExitMenuApplication, application: ApplicationProperties) -> int:
        """
         
                  Registers the application
                 
         @return application_id (int):  Unique identifier for the registered application .
        """
        pass
    
    ##  Registers a callback that is called whenever a customizable context
    ##             menu is about to be displayed. 
    ## 
    ##             Each callback is registered with a short name and a longer
    ##             description which is used to identify the callback for debugging
    ##             purposes.
    ##         
    ##  @return id (int):  Identifier of registered callback .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## <param name="name"> (str)  A short string identifying the callback </param>
    ## <param name="description"> (str)  A longer string describing the operation of the callback </param>
    ## <param name="configure_popup_menu"> (@link MenuBarManager.ConfigureContextMenu NXOpen.MenuBar.MenuBarManager.ConfigureContextMenu@endlink)  Callback to register </param>
    def RegisterConfigureContextMenuCallback(name: str, description: str, configure_popup_menu: MenuBarManager.ConfigureContextMenu) -> int:
        """
         Registers a callback that is called whenever a customizable context
                    menu is about to be displayed. 
        
                    Each callback is registered with a short name and a longer
                    description which is used to identify the callback for debugging
                    purposes.
                
         @return id (int):  Identifier of registered callback .
        """
        pass
    
    ##  
    ##           Sets the toggle value of the add-on when a toggle button is utilized
    ##          
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## <param name="name"> (str)  The name of the add-on application.  </param>
    ## <param name="status"> (bool)  The toggle state of the add-on application.  </param>
    def SetAddOnToggleButton(name: str, status: bool) -> None:
        """
         
                  Sets the toggle value of the add-on when a toggle button is utilized
                 
        """
        pass
    
    ##  Unregisters a callback for application switches.
    ##         
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## <param name="id"> (int)  Identifier for callback to unregister </param>
    def UnregisterApplicationSwitchCallback(id: int) -> None:
        """
         Unregisters a callback for application switches.
                
        """
        pass
    
    ##  Unregisters a callback for customizing context menus.
    ##         
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## <param name="id"> (int)  Identifier for callback to unregister </param>
    def UnregisterConfigureContextMenuCallback(id: int) -> None:
        """
         Unregisters a callback for customizing context menus.
                
        """
        pass
    
import NXOpen
##  Implements the Event Object for Menu Buttons 
## 
##   <br>  Created in NX6.0.0  <br> 

class MenuButtonEvent(NXOpen.TransientObject): 
    """ Implements the Event Object for Menu Buttons """


    ## Getter for property: (@link MenuButton NXOpen.MenuBar.MenuButton@endlink) ActiveButton
    ##  Returns the activated MenuButton.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return MenuButton
    @property
    def ActiveButton(self) -> MenuButton:
        """
        Getter for property: (@link MenuButton NXOpen.MenuBar.MenuButton@endlink) ActiveButton
         Returns the activated MenuButton.  
             
         
        """
        pass
    
    ## Getter for property: (int) ApplicationId
    ##  Returns the activated MenuButton's owning application identifier.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return int
    @property
    def ApplicationId(self) -> int:
        """
        Getter for property: (int) ApplicationId
         Returns the activated MenuButton's owning application identifier.  
             
         
        """
        pass
    
    ## Getter for property: (str) MenuBarName
    ##  Returns the name of the menu bar.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return str
    @property
    def MenuBarName(self) -> str:
        """
        Getter for property: (str) MenuBarName
         Returns the name of the menu bar.  
             
         
        """
        pass
    
    ##  Frees the object from memory.  After this method is
    ##             called, it is illegal to use the object.  In .NET and Java,
    ##             his method is automatically called when the object is
    ##             deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is
                    called, it is illegal to use the object.  In .NET and Java,
                    his method is automatically called when the object is
                    deleted by the garbage collector.  
        """
        pass
    
    ##  Get the ancestors of the active button. 
    ##  @return ancestors (List[str]):  The ancestors that caused the event to fire .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def GetMenuAncestors(self) -> List[str]:
        """
         Get the ancestors of the active button. 
         @return ancestors (List[str]):  The ancestors that caused the event to fire .
        """
        pass
    
import NXOpen
##  Implements the Object for Menu Buttons 
## 
##   <br>  Created in NX6.0.0  <br> 

class MenuButton(NXOpen.TransientObject): 
    """ Implements the Object for Menu Buttons """


    ##  Availability Status 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Available</term><description> 
    ##  The button is available. </description> </item><item><term> 
    ## Unavailable</term><description> 
    ##  The button is unavailable. </description> </item></list>
    class AvailabilityStatus(Enum):
        """
        Members Include: <Available> <Unavailable>
        """
        Available: int
        Unavailable: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MenuButton.AvailabilityStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Sensitivity Status 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Sensitive</term><description> 
    ##  The button is sensitive. </description> </item><item><term> 
    ## Insensitive</term><description> 
    ##  The button is insensitive. </description> </item></list>
    class SensitivityStatus(Enum):
        """
        Members Include: <Sensitive> <Insensitive>
        """
        Sensitive: int
        Insensitive: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MenuButton.SensitivityStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Toggle Status 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## On</term><description> 
    ##  The toggle is on. </description> </item><item><term> 
    ## Off</term><description> 
    ##  The toggle is off. </description> </item></list>
    class Toggle(Enum):
        """
        Members Include: <On> <Off>
        """
        On: int
        Off: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MenuButton.Toggle:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Available button types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## CascadeButton</term><description> 
    ##   </description> </item><item><term> 
    ## PushButton</term><description> 
    ##   </description> </item><item><term> 
    ## ToggleButton</term><description> 
    ##   </description> </item><item><term> 
    ## Separator</term><description> 
    ##   </description> </item><item><term> 
    ## ApplicationButton</term><description> 
    ##   </description> </item><item><term> 
    ## NullButton</term><description> 
    ##   </description> </item></list>
    class Type(Enum):
        """
        Members Include: <CascadeButton> <PushButton> <ToggleButton> <Separator> <ApplicationButton> <NullButton>
        """
        CascadeButton: int
        PushButton: int
        ToggleButton: int
        Separator: int
        ApplicationButton: int
        NullButton: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MenuButton.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link MenuButton.AvailabilityStatus NXOpen.MenuBar.MenuButton.AvailabilityStatus@endlink) ButtonAvailability
    ##  Returns  the availability of the NXOpen button.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return MenuButton.AvailabilityStatus
    @property
    def ButtonAvailability(self) -> MenuButton.AvailabilityStatus:
        """
        Getter for property: (@link MenuButton.AvailabilityStatus NXOpen.MenuBar.MenuButton.AvailabilityStatus@endlink) ButtonAvailability
         Returns  the availability of the NXOpen button.  
              
         
        """
        pass
    
    ## Setter for property: (@link MenuButton.AvailabilityStatus NXOpen.MenuBar.MenuButton.AvailabilityStatus@endlink) ButtonAvailability

    ##  Returns  the availability of the NXOpen button.  
    ##       
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ButtonAvailability.setter
    def ButtonAvailability(self, availability: MenuButton.AvailabilityStatus):
        """
        Setter for property: (@link MenuButton.AvailabilityStatus NXOpen.MenuBar.MenuButton.AvailabilityStatus@endlink) ButtonAvailability
         Returns  the availability of the NXOpen button.  
              
         
        """
        pass
    
    ## Getter for property: (int) ButtonId
    ##  Returns the identifier of the button.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return int
    @property
    def ButtonId(self) -> int:
        """
        Getter for property: (int) ButtonId
         Returns the identifier of the button.  
             
         
        """
        pass
    
    ## Getter for property: (str) ButtonName
    ##  Returns the name of the button.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return str
    @property
    def ButtonName(self) -> str:
        """
        Getter for property: (str) ButtonName
         Returns the name of the button.  
             
         
        """
        pass
    
    ## Getter for property: (@link MenuButton.SensitivityStatus NXOpen.MenuBar.MenuButton.SensitivityStatus@endlink) ButtonSensitivity
    ##  Returns the sensitivity of the button.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return MenuButton.SensitivityStatus
    @property
    def ButtonSensitivity(self) -> MenuButton.SensitivityStatus:
        """
        Getter for property: (@link MenuButton.SensitivityStatus NXOpen.MenuBar.MenuButton.SensitivityStatus@endlink) ButtonSensitivity
         Returns the sensitivity of the button.  
             
         
        """
        pass
    
    ## Setter for property: (@link MenuButton.SensitivityStatus NXOpen.MenuBar.MenuButton.SensitivityStatus@endlink) ButtonSensitivity

    ##  Returns the sensitivity of the button.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @ButtonSensitivity.setter
    def ButtonSensitivity(self, sensitivity: MenuButton.SensitivityStatus):
        """
        Setter for property: (@link MenuButton.SensitivityStatus NXOpen.MenuBar.MenuButton.SensitivityStatus@endlink) ButtonSensitivity
         Returns the sensitivity of the button.  
             
         
        """
        pass
    
    ## Getter for property: (@link MenuButton.Type NXOpen.MenuBar.MenuButton.Type@endlink) ButtonType
    ##  Returns the type of the button.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return MenuButton.Type
    @property
    def ButtonType(self) -> MenuButton.Type:
        """
        Getter for property: (@link MenuButton.Type NXOpen.MenuBar.MenuButton.Type@endlink) ButtonType
         Returns the type of the button.  
             
         
        """
        pass
    
    ## Getter for property: (str) ButtonTypeName
    ##  Returns the type name of the button.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return str
    @property
    def ButtonTypeName(self) -> str:
        """
        Getter for property: (str) ButtonTypeName
         Returns the type name of the button.  
             
         
        """
        pass
    
    ## Getter for property: (@link MenuButton.Toggle NXOpen.MenuBar.MenuButton.Toggle@endlink) ToggleStatus
    ##  Returns the toggle status of the button.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return MenuButton.Toggle
    @property
    def ToggleStatus(self) -> MenuButton.Toggle:
        """
        Getter for property: (@link MenuButton.Toggle NXOpen.MenuBar.MenuButton.Toggle@endlink) ToggleStatus
         Returns the toggle status of the button.  
             
         
        """
        pass
    
    ## Setter for property: (@link MenuButton.Toggle NXOpen.MenuBar.MenuButton.Toggle@endlink) ToggleStatus

    ##  Returns the toggle status of the button.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @ToggleStatus.setter
    def ToggleStatus(self, toggle_status: MenuButton.Toggle):
        """
        Setter for property: (@link MenuButton.Toggle NXOpen.MenuBar.MenuButton.Toggle@endlink) ToggleStatus
         Returns the toggle status of the button.  
             
         
        """
        pass
    
    ##  Frees the object from memory.  After this method is
    ##             called, it is illegal to use the object.  In .NET and Java,
    ##             his method is automatically called when the object is
    ##             deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is
                    called, it is illegal to use the object.  In .NET and Java,
                    his method is automatically called when the object is
                    deleted by the garbage collector.  
        """
        pass
    
## @package NXOpen.MenuBar
## Classes, Enums and Structs under NXOpen.MenuBar namespace

##  @link ContextMenuEntryType NXOpen.MenuBar.ContextMenuEntryType @endlink is an alias for @link ContextMenuEntry.Type NXOpen.MenuBar.ContextMenuEntry.Type@endlink
ContextMenuEntryType = ContextMenuEntry.Type


##  @link MenuBarManagerCallbackStatus NXOpen.MenuBar.MenuBarManagerCallbackStatus @endlink is an alias for @link MenuBarManager.CallbackStatus NXOpen.MenuBar.MenuBarManager.CallbackStatus@endlink
MenuBarManagerCallbackStatus = MenuBarManager.CallbackStatus


##  @link MenuBarManagerSwitchReason NXOpen.MenuBar.MenuBarManagerSwitchReason @endlink is an alias for @link MenuBarManager.SwitchReason NXOpen.MenuBar.MenuBarManager.SwitchReason@endlink
MenuBarManagerSwitchReason = MenuBarManager.SwitchReason


##  @link MenuButtonAvailabilityStatus NXOpen.MenuBar.MenuButtonAvailabilityStatus @endlink is an alias for @link MenuButton.AvailabilityStatus NXOpen.MenuBar.MenuButton.AvailabilityStatus@endlink
MenuButtonAvailabilityStatus = MenuButton.AvailabilityStatus


##  @link MenuButtonSensitivityStatus NXOpen.MenuBar.MenuButtonSensitivityStatus @endlink is an alias for @link MenuButton.SensitivityStatus NXOpen.MenuBar.MenuButton.SensitivityStatus@endlink
MenuButtonSensitivityStatus = MenuButton.SensitivityStatus


##  @link MenuButtonToggle NXOpen.MenuBar.MenuButtonToggle @endlink is an alias for @link MenuButton.Toggle NXOpen.MenuBar.MenuButton.Toggle@endlink
MenuButtonToggle = MenuButton.Toggle


##  @link MenuButtonType NXOpen.MenuBar.MenuButtonType @endlink is an alias for @link MenuButton.Type NXOpen.MenuBar.MenuButton.Type@endlink
MenuButtonType = MenuButton.Type


