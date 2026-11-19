from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
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
    ##  This application allows multiple different parts 
    def AllowsMultipleWindowDesigns(button: ApplicationProperties, allows_multiple_window_designs: bool) -> None:
        """
         This application allows the display of multiple different parts in separate graphics windows at the same time. 
        """
        pass
    
    ##  This application allows more than one graphics window of the same displayed part (as in Windows->New Window). 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  This application allows multiple window views 
    def AllowsMultipleWindowViews(button: ApplicationProperties, allows_multiple_window_views: bool) -> None:
        """
         This application allows more than one graphics window of the same displayed part (as in Windows->New Window). 
        """
        pass
    
    ##  This application allows undo over an application. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  This application allows an undo over application change 
    def AllowsUndoOverApplicationChange(button: ApplicationProperties, allows_undo_over_application_change: bool) -> None:
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
    @staticmethod
    def Dispose(application: ApplicationProperties) -> None:
        """
         Frees the object from memory.  After this method is
                called, it is illegal to use the object.  In .NET and Java,
                his method is automatically called when the object is
                deleted by the garbage collector.  
        """
        pass
    
    ##  This application supports drawings. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  This application support drawings 
    def SupportsDrawings(button: ApplicationProperties, supports_drawings: bool) -> None:
        """
         This application supports drawings. 
        """
        pass
    
    ##  This application supports undo within in the application. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  This application support undo within in the application 
    def SupportsUndoWithinApplication(button: ApplicationProperties, supports_undo: bool) -> None:
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
    ##  Has an attached menu structure containing more entries. 
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
    ##   the type of this menu entry.  
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
          the type of this menu entry.  
             
         
        """
        pass
    
    ## Getter for property: (bool) IsDefault
    ##   true if this entry is the default action for the menu.  
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
          true if this entry is the default action for the menu.  
           A menu entry is marked as
                    the default for the menu when it corresponds to the double-click 
                    action.
                  
         
        """
        pass
    
    ## Getter for property: (bool) IsHidden
    ##   true if this entry is hidden on the menu.  
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
          true if this entry is hidden on the menu.  
             
         
        """
        pass
    
    ## Getter for property: (bool) IsSensitive
    ##   true if the command corresponding to this entry can be run.  
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
          true if the command corresponding to this entry can be run.  
           
                  
         
        """
        pass
    
    ## Getter for property: (str) Label
    ##   the label of this menu entry.  
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
          the label of this menu entry.  
             
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##   the name of this menu entry.  
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
          the name of this menu entry.  
           
                
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
    @staticmethod
    def Dispose(menu_entry: ContextMenuEntry) -> None:
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
    ##   a description for the context for which the menu was created   
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
          a description for the context for which the menu was created   
            
         
        """
        pass
    
    ## Getter for property: (str) Location
    ##   the location where the context menu will be displayed   
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
          the location where the context menu will be displayed   
            
         
        """
        pass
    
    ##  Frees the object from memory.  After this method is called,
    ##             it is illegal to use the object.  In .NET, this method is automatically
    ##             called when the object is deleted by the garbage collector. 
    ##         
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(props: ContextMenuProperties) -> None:
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
    ##   the number of @link MenuBar::ContextMenuEntry MenuBar::ContextMenuEntry@endlink  objects in this menu.  
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
          the number of @link MenuBar::ContextMenuEntry MenuBar::ContextMenuEntry@endlink  objects in this menu.  
             
         
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
    ##  the menu bar button to add to the menu 
    def AddMenuButton(menu: ContextMenu, button: MenuButton, index: int) -> ContextMenuEntry:
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
    ##  label for the label entry 
    def AddMenuLabel(menu: ContextMenu, label: str, index: int) -> ContextMenuEntry:
        """
         Adds a label to the context menu. 
         @return entry (@link ContextMenuEntry NXOpen.MenuBar.ContextMenuEntry@endlink):  the new menu entry .
        """
        pass
    
    ##  Adds a separator to the context menu. 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ##  position at which to create the separator. Use -1 to add the separator to the end of the menu. 
    def AddSeparator(menu: ContextMenu, index: int) -> None:
        """
         Adds a separator to the context menu. 
        """
        pass
    
    ##  Adds a submenu to the context menu. 
    ##  @return submenu (@link ContextMenu NXOpen.MenuBar.ContextMenu@endlink):  the new submenu .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ##  label for the cascade menu 
    def AddSubmenu(menu: ContextMenu, label: str, index: int) -> ContextMenu:
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
    @staticmethod
    def Dispose(menu: ContextMenu) -> None:
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
    ##  index of menu entry to return 
    def GetEntry(menu: ContextMenu, index: int) -> ContextMenuEntry:
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
    ##  name of menu entry to search for 
    def GetEntryWithName(menu: ContextMenu, name: str) -> ContextMenuEntry:
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
    ##  an entry in the menu 
    def GetIndexOfEntry(menu: ContextMenu, entry: ContextMenuEntry) -> int:
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
    ##  index of submenu to return 
    def GetSubmenu(menu: ContextMenu, index: int) -> ContextMenu:
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
    ##  name of menu entry to search for 
    def HasEntryWithName(menu: ContextMenu, name: str) -> bool:
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
    ##  the menu entry to hide 
    def HideEntry(menu: ContextMenu, entry: ContextMenuEntry) -> None:
        """
         Prevents the indicated menu entry from being shown on the menu. 
        """
        pass
    
    ##  Reorders the menu to move a menu entry to a new position in the list. 
    ##         
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ##  the menu entry to be moved 
    def MoveEntry(menu: ContextMenu, entry: ContextMenuEntry, index: int) -> None:
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
    ##  the menu entry to become the default for the menu 
    def SetDefaultEntry(menu: ContextMenu, entry: ContextMenuEntry) -> None:
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
    ##  Continue performing the menu item's actions. 
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
    ##  An application has been entered. 
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
    ##  The name of the action.  This name must match the string used in the .men file. 
    def AddMenuAction(name: str, action_callback: MenuBarManager.ActionCallback) -> None:
        """
         
                  Adds the action callback.
                 
        """
        pass
    
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
    
    
    ##  Finds the MenuButton associated with the given name 
    ##  @return button (@link MenuButton NXOpen.MenuBar.MenuButton@endlink):  The button associated with the given name .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  The name of the button.  This name must match the button name used in the .men file. 
    @staticmethod
    def GetButtonFromName(name: str) -> MenuButton:
        """
         Finds the MenuButton associated with the given name 
         @return button (@link MenuButton NXOpen.MenuBar.MenuButton@endlink):  The button associated with the given name .
        """
        pass
    
    ##  Prototype for application initialization callback 
    ## A callback definition with no input arguments and no return type
    InitializeMenuApplication = Callable[[], None]
    
    
    ##  Constructs a new ApplicationProperties object. 
    ##  @return data (@link ApplicationProperties NXOpen.MenuBar.ApplicationProperties@endlink):  .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def NewApplicationProperties() -> ApplicationProperties:
        """
         Constructs a new ApplicationProperties object. 
         @return data (@link ApplicationProperties NXOpen.MenuBar.ApplicationProperties@endlink):  .
        """
        pass
    
    ##  
    ##           Registers the application
    ##          
    ##  @return application_id (int):  Unique identifier for the registered application .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  The name of the application.  This name must match the string used in the .men file. 
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
    ##  The method to execute for this action 
    @staticmethod
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
    ##  The name of the application.  This name must match the string used in the .men file. 
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
    ##  A short string identifying the callback 
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
    
    ##  Unregisters a callback for application switches.
    ##         
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ##  Identifier for callback to unregister 
    @staticmethod
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
    ##  Identifier for callback to unregister 
    @staticmethod
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
    ##   the activated MenuButton.  
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
          the activated MenuButton.  
             
         
        """
        pass
    
    ## Getter for property: (int) ApplicationId
    ##   the activated MenuButton's owning application identifier.  
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
          the activated MenuButton's owning application identifier.  
             
         
        """
        pass
    
    ## Getter for property: (str) MenuBarName
    ##   the name of the menu bar.  
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
          the name of the menu bar.  
             
         
        """
        pass
    
    ##  Frees the object from memory.  After this method is
    ##             called, it is illegal to use the object.  In .NET and Java,
    ##             his method is automatically called when the object is
    ##             deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(button_event: MenuButtonEvent) -> None:
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
    @staticmethod
    def GetMenuAncestors(button_event: MenuButtonEvent) -> List[str]:
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
    ##  The button is available. 
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
    ##  The button is sensitive. 
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
    ##  The toggle is on. 
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
    ##   
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
    ##    the availability of the NXOpen button.  
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
           the availability of the NXOpen button.  
              
         
        """
        pass
    
    ## Setter for property: (@link MenuButton.AvailabilityStatus NXOpen.MenuBar.MenuButton.AvailabilityStatus@endlink) ButtonAvailability

    ##    the availability of the NXOpen button.  
    ##       
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ButtonAvailability.setter
    def ButtonAvailability(self, availability: MenuButton.AvailabilityStatus):
        """
        Setter for property: (@link MenuButton.AvailabilityStatus NXOpen.MenuBar.MenuButton.AvailabilityStatus@endlink) ButtonAvailability
           the availability of the NXOpen button.  
              
         
        """
        pass
    
    ## Getter for property: (int) ButtonId
    ##   the identifier of the button.  
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
          the identifier of the button.  
             
         
        """
        pass
    
    ## Getter for property: (str) ButtonName
    ##   the name of the button.  
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
          the name of the button.  
             
         
        """
        pass
    
    ## Getter for property: (@link MenuButton.SensitivityStatus NXOpen.MenuBar.MenuButton.SensitivityStatus@endlink) ButtonSensitivity
    ##   the sensitivity of the button.  
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
          the sensitivity of the button.  
             
         
        """
        pass
    
    ## Setter for property: (@link MenuButton.SensitivityStatus NXOpen.MenuBar.MenuButton.SensitivityStatus@endlink) ButtonSensitivity

    ##   the sensitivity of the button.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @ButtonSensitivity.setter
    def ButtonSensitivity(self, sensitivity: MenuButton.SensitivityStatus):
        """
        Setter for property: (@link MenuButton.SensitivityStatus NXOpen.MenuBar.MenuButton.SensitivityStatus@endlink) ButtonSensitivity
          the sensitivity of the button.  
             
         
        """
        pass
    
    ## Getter for property: (@link MenuButton.Type NXOpen.MenuBar.MenuButton.Type@endlink) ButtonType
    ##   the type of the button.  
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
          the type of the button.  
             
         
        """
        pass
    
    ## Getter for property: (str) ButtonTypeName
    ##   the type name of the button.  
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
          the type name of the button.  
             
         
        """
        pass
    
    ## Getter for property: (@link MenuButton.Toggle NXOpen.MenuBar.MenuButton.Toggle@endlink) ToggleStatus
    ##   the toggle status of the button.  
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
          the toggle status of the button.  
             
         
        """
        pass
    
    ## Setter for property: (@link MenuButton.Toggle NXOpen.MenuBar.MenuButton.Toggle@endlink) ToggleStatus

    ##   the toggle status of the button.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @ToggleStatus.setter
    def ToggleStatus(self, toggle_status: MenuButton.Toggle):
        """
        Setter for property: (@link MenuButton.Toggle NXOpen.MenuBar.MenuButton.Toggle@endlink) ToggleStatus
          the toggle status of the button.  
             
         
        """
        pass
    
    ##  Frees the object from memory.  After this method is
    ##             called, it is illegal to use the object.  In .NET and Java,
    ##             his method is automatically called when the object is
    ##             deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(button: MenuButton) -> None:
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


