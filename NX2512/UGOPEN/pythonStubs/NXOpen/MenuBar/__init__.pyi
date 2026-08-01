from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class AddonProperties(NXOpen.TransientObject): 
    """ Implements the properties for the Addons """
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is
                called, it is illegal to use the object.  In .NET and Java,
                his method is automatically called when the object is
                deleted by the garbage collector.  
        """
        pass
    def SaveToggleState(self, save_toggle_state: bool) -> None:
        """
         This addon saves the setting of the add-on toggle button across sessions. 
        """
        pass
    def SetTabActiveOnToggle(self, set_tab_active_on_toggle: bool) -> None:
        """
         This addon sets the specified ribbon as the active tab when the add-on toggle is set 
        """
        pass
import NXOpen
class ApplicationProperties(NXOpen.TransientObject): 
    """ Implements the properties for the Menu Applications """
    def AllowsMultipleWindowDesigns(self, allows_multiple_window_designs: bool) -> None:
        """
         This application allows the display of multiple different parts in separate graphics windows at the same time. 
        """
        pass
    def AllowsMultipleWindowViews(self, allows_multiple_window_views: bool) -> None:
        """
         This application allows more than one graphics window of the same displayed part (as in Windows-New Window). 
        """
        pass
    def AllowsUndoOverApplicationChange(self, allows_undo_over_application_change: bool) -> None:
        """
         This application allows undo over an application. 
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is
                called, it is illegal to use the object.  In .NET and Java,
                his method is automatically called when the object is
                deleted by the garbage collector.  
        """
        pass
    def SupportsDesignInContext(self, supports_design_in_context: bool) -> None:
        """
         Sets whether this application supports design-in-context.
                
                    Applications supporting design-in-context allow the
                    work part to be set to one of the components of a displayed
                    assembly. For applications that do not support design-in-context,
                    the work part will always be the same as the displayed part. 
        """
        pass
    def SupportsDrawings(self, supports_drawings: bool) -> None:
        """
         This application supports drawings. 
        """
        pass
    def SupportsUndoWithinApplication(self, supports_undo: bool) -> None:
        """
         This application supports undo within in the application. 
        """
        pass
import NXOpen
class ContextMenuEntry(NXOpen.TransientObject): 
    """ Represents an entry on a context menu. """
    class Type(Enum):
        """
        Members Include: 
         |Submenu|  Has an attached menu structure containing more entries. 
         |PushButton|  Has a command that is run when this entry is activated. 
         |ToggleButton|  Displays an OnOff state. 
         |Separator|  A visual divider between sections of the menu. 
         |Label|  A label often used to divide and provide context to sub-groups of commands. 

        """
        Submenu: int
        PushButton: int
        ToggleButton: int
        Separator: int
        Label: int
        @staticmethod
        def ValueOf(value: int) -> ContextMenuEntry.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def EntryType(self) -> ContextMenuEntry.Type:
        """
        Getter for property: ( ContextMenuEntry.Type NXOpen) EntryType
         Returns the type of this menu entry.  
             
         
        """
        pass
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
    @property
    def IsHidden(self) -> bool:
        """
        Getter for property: (bool) IsHidden
         Returns true if this entry is hidden on the menu.  
             
         
        """
        pass
    @property
    def IsSensitive(self) -> bool:
        """
        Getter for property: (bool) IsSensitive
         Returns true if the command corresponding to this entry can be run.  
           
                  
         
        """
        pass
    @property
    def Label(self) -> str:
        """
        Getter for property: (str) Label
         Returns the label of this menu entry.  
             
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name of this menu entry.  
           
                
                    Some entries on the context menu may correspond to buttons on the menu bar.
                    For these entries, the name that is returned is the name of that 
                     MenuBar::MenuButton  object.
                    
                    For all other entries which do not correspond to a menu bar button, the
                    name that is returned has no specific meaning. However, for any individual 
                    action within any specific context menu, the name that is assigned to
                    that action will not change.
                  
         
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                    it is illegal to use the object.  In .NET, this method is automatically
                    called when the object is deleted by the garbage collector. 
                
        """
        pass
import NXOpen
class ContextMenuProperties(NXOpen.TransientObject): 
    """ Provides information about the MenuBar.ContextMenu object being customized. """
    @property
    def Context(self) -> str:
        """
        Getter for property: (str) Context
         Returns a description for the context for which the menu was created   
            
         
        """
        pass
    @property
    def Location(self) -> str:
        """
        Getter for property: (str) Location
         Returns the location where the context menu will be displayed   
            
         
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                    it is illegal to use the object.  In .NET, this method is automatically
                    called when the object is deleted by the garbage collector. 
                
        """
        pass
import NXOpen
class ContextMenu(NXOpen.TransientObject): 
    """ Represents a Context Menu """
    @property
    def NumberOfEntries(self) -> int:
        """
        Getter for property: (int) NumberOfEntries
         Returns the number of  MenuBar::ContextMenuEntry  objects in this menu.  
             
         
        """
        pass
    def AddMenuButton(self, button: MenuButton, index: int) -> ContextMenuEntry:
        """
         Adds a menu bar button to the context menu. Use 
                    MenuBar.MenuBarManager.GetButtonFromName 
                    to find the button to add to the menu.
                
         Returns entry ( ContextMenuEntry NXOpen):  the new menu entry .
        """
        pass
    def AddMenuLabel(self, label: str, index: int) -> ContextMenuEntry:
        """
         Adds a label to the context menu. 
         Returns entry ( ContextMenuEntry NXOpen):  the new menu entry .
        """
        pass
    def AddSeparator(self, index: int) -> None:
        """
         Adds a separator to the context menu. 
        """
        pass
    def AddSubmenu(self, label: str, index: int) -> ContextMenu:
        """
         Adds a submenu to the context menu. 
         Returns submenu ( ContextMenu NXOpen):  the new submenu .
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                    it is illegal to use the object.  In .NET, this method is automatically
                    called when the object is deleted by the garbage collector. 
                
        """
        pass
    def GetEntry(self, index: int) -> ContextMenuEntry:
        """
         Returns the MenuBar.ContextMenuEntry at the specified index in the menu. 
         Returns entry ( ContextMenuEntry NXOpen):  the menu entry at this position .
        """
        pass
    def GetEntryWithName(self, name: str) -> ContextMenuEntry:
        """
         Given the name of a menu entry, returns the first
                    MenuBar.ContextMenuEntry in this menu which
                    matches. 
                
         Returns entry ( ContextMenuEntry NXOpen):  the menu entry with this name .
        """
        pass
    def GetIndexOfEntry(self, entry: ContextMenuEntry) -> int:
        """
         Returns the index of the MenuBar.ContextMenuEntry
                    object within this menu.
                
         Returns index (int):  the index for that menu entry .
        """
        pass
    def GetSubmenu(self, index: int) -> ContextMenu:
        """
         Returns the submenu for the entry at the specified index in the menu. 
                    The menu entry at this index must be of type 
                    MenuBar.ContextMenuEntry.Type.Submenu.
                 
         Returns submenu ( ContextMenu NXOpen):  the submenu at this position .
        """
        pass
    def HasEntryWithName(self, name: str) -> bool:
        """
         Indicates whether or not this menu contains a 
                    MenuBar.ContextMenuEntry which 
                    has the given name.
                
         Returns exists (bool):  the menu entry with this name .
        """
        pass
    def HideEntry(self, entry: ContextMenuEntry) -> None:
        """
         Prevents the indicated menu entry from being shown on the menu. 
        """
        pass
    def MoveEntry(self, entry: ContextMenuEntry, index: int) -> None:
        """
         Reorders the menu to move a menu entry to a new position in the list. 
                
        """
        pass
    def SetDefaultEntry(self, entry: ContextMenuEntry) -> None:
        """
         Makes a specified menu entry the default for the menu. 
                
                    This entry will be displayed in bold text on the menu. It will be the action
                    that is performed in response to a double-click event in the UI.
                    
                    The menu entry must have a type of MenuBar.ContextMenuEntry.Type.PushButton
                    or MenuBar.ContextMenuEntry.Type.ToggleButton. 
                
        """
        pass
import NXOpen
class MenuBarManager(NXOpen.Object): 
    """ Interface for the MenuBarManager object """
    class CallbackStatus(Enum):
        """
        Members Include: 
         |Continue|  Continue performing the menu item's actions. 
         |Cancel|  User interaction requested inhibiting the 
                                                                       menu item's actions. 
         |OverrideStandard|  Inhibit further actions because a pre 
                                                                                  action took the place of the standard 
                                                                                  action for a standard NX menu item. 
         |Warning|  Inhibit further actions because a 
                                                                        warning condition was raised. 
         |Error|  Inhibit further actions because a 
                                                                      error condition was raised. 

        """
        Continue: int
        Cancel: int
        OverrideStandard: int
        Warning: int
        Error: int
        @staticmethod
        def ValueOf(value: int) -> MenuBarManager.CallbackStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SwitchReason(Enum):
        """
        Members Include: 
         |Enter|  An application has been entered. 
         |TaskEnter|  A task has been entered. 

        """
        Enter: int
        TaskEnter: int
        @staticmethod
        def ValueOf(value: int) -> MenuBarManager.SwitchReason:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    ActionCallback = Callable[[MenuButtonEvent], None]
    def AddMenuAction(name: str, action_callback: MenuBarManager.ActionCallback) -> None:
        """
         
                  Adds the action callback.
                 
        """
        pass
    AddOnCallback = Callable[[str], None]
    AddOnToggleCallback = Callable[[bool], None]
    ApplicationSwitchNotify = Callable[[str, MenuBarManager.SwitchReason], None]
    ConfigureContextMenu = Callable[[ContextMenu, ContextMenuProperties], None]
    EnterMenuApplication = Callable[[], None]
    ExitMenuApplication = Callable[[], None]
    def GetAddOnToggleButton(name: str) -> bool:
        """
         
                  Returns the active toggle state of the add-on when a toggle button is utilized
                 
         Returns status (bool):  The toggle state of the add-on application.  .
        """
        pass
    def GetButtonFromName(name: str) -> MenuButton:
        """
         Finds the MenuButton associated with the given name 
         Returns button ( MenuButton NXOpen):  The button associated with the given name .
        """
        pass
    InitializeMenuApplication = Callable[[], None]
    def NewAddOnProperties() -> AddonProperties:
        """
         Constructs a new AddonProperties object. 
         Returns data ( AddonProperties NXOpen):  .
        """
        pass
    def NewApplicationProperties() -> ApplicationProperties:
        """
         Constructs a new ApplicationProperties object. 
         Returns data ( ApplicationProperties NXOpen):  .
        """
        pass
    def RegisterAddOn(name: str, application_name: List[str], initialize_callback: MenuBarManager.AddOnCallback, enter_callback: MenuBarManager.AddOnCallback, exit_callback: MenuBarManager.AddOnCallback, toggle_callback: MenuBarManager.AddOnToggleCallback, add_on_properties: AddonProperties) -> None:
        """
         
                  Registers an add-on application
                 
        """
        pass
    def RegisterAddOnMenuFile(name: str, menu_file: str) -> None:
        """
         
                  Registers a menu to an add-on application
                 
        """
        pass
    def RegisterAddOnRibbonFile(name: str, ribbon_file: str) -> None:
        """
         
                  Registers a ribbon UI element to an add-on application
                 
        """
        pass
    @overload
    def RegisterApplication(name: str, initialize_callback: MenuBarManager.InitializeMenuApplication, enter_callback: MenuBarManager.EnterMenuApplication, exit_callback: MenuBarManager.ExitMenuApplication, supports_drawings: bool, supports_design_in_context: bool, supports_undo: bool) -> int:
        """
         
                  Registers the application
                 
         Returns application_id (int):  Unique identifier for the registered application .
        """
        pass
    def RegisterApplicationSwitchCallback(switch_callback: MenuBarManager.ApplicationSwitchNotify) -> int:
        """
         Registers a callback for application switches.
                
         Returns id (int):  Identifier of registered callback .
        """
        pass
    @overload
    def RegisterApplication(name: str, initialize_callback: MenuBarManager.InitializeMenuApplication, enter_callback: MenuBarManager.EnterMenuApplication, exit_callback: MenuBarManager.ExitMenuApplication, application: ApplicationProperties) -> int:
        """
         
                  Registers the application
                 
         Returns application_id (int):  Unique identifier for the registered application .
        """
        pass
    def RegisterConfigureContextMenuCallback(name: str, description: str, configure_popup_menu: MenuBarManager.ConfigureContextMenu) -> int:
        """
         Registers a callback that is called whenever a customizable context
                    menu is about to be displayed. 
                    Each callback is registered with a short name and a longer
                    description which is used to identify the callback for debugging
                    purposes.
                
         Returns id (int):  Identifier of registered callback .
        """
        pass
    def SetAddOnToggleButton(name: str, status: bool) -> None:
        """
         
                  Sets the toggle value of the add-on when a toggle button is utilized
                 
        """
        pass
    def UnregisterApplicationSwitchCallback(id: int) -> None:
        """
         Unregisters a callback for application switches.
                
        """
        pass
    def UnregisterConfigureContextMenuCallback(id: int) -> None:
        """
         Unregisters a callback for customizing context menus.
                
        """
        pass
import NXOpen
class MenuButtonEvent(NXOpen.TransientObject): 
    """ Implements the Event Object for Menu Buttons """
    @property
    def ActiveButton(self) -> MenuButton:
        """
        Getter for property: ( MenuButton NXOpen) ActiveButton
         Returns the activated MenuButton.  
             
         
        """
        pass
    @property
    def ApplicationId(self) -> int:
        """
        Getter for property: (int) ApplicationId
         Returns the activated MenuButton's owning application identifier.  
             
         
        """
        pass
    @property
    def MenuBarName(self) -> str:
        """
        Getter for property: (str) MenuBarName
         Returns the name of the menu bar.  
             
         
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is
                    called, it is illegal to use the object.  In .NET and Java,
                    his method is automatically called when the object is
                    deleted by the garbage collector.  
        """
        pass
    def GetMenuAncestors(self) -> List[str]:
        """
         Get the ancestors of the active button. 
         Returns ancestors (List[str]):  The ancestors that caused the event to fire .
        """
        pass
import NXOpen
class MenuButton(NXOpen.TransientObject): 
    """ Implements the Object for Menu Buttons """
    class AvailabilityStatus(Enum):
        """
        Members Include: 
         |Available|  The button is available. 
         |Unavailable|  The button is unavailable. 

        """
        Available: int
        Unavailable: int
        @staticmethod
        def ValueOf(value: int) -> MenuButton.AvailabilityStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SensitivityStatus(Enum):
        """
        Members Include: 
         |Sensitive|  The button is sensitive. 
         |Insensitive|  The button is insensitive. 

        """
        Sensitive: int
        Insensitive: int
        @staticmethod
        def ValueOf(value: int) -> MenuButton.SensitivityStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Toggle(Enum):
        """
        Members Include: 
         |On|  The toggle is on. 
         |Off|  The toggle is off. 

        """
        On: int
        Off: int
        @staticmethod
        def ValueOf(value: int) -> MenuButton.Toggle:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Type(Enum):
        """
        Members Include: 
         |CascadeButton|   
         |PushButton|   
         |ToggleButton|   
         |Separator|   
         |ApplicationButton|   
         |NullButton|   

        """
        CascadeButton: int
        PushButton: int
        ToggleButton: int
        Separator: int
        ApplicationButton: int
        NullButton: int
        @staticmethod
        def ValueOf(value: int) -> MenuButton.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ButtonAvailability(self) -> MenuButton.AvailabilityStatus:
        """
        Getter for property: ( MenuButton.AvailabilityStatus NXOpen) ButtonAvailability
         Returns  the availability of the NXOpen button.  
              
         
        """
        pass
    @ButtonAvailability.setter
    def ButtonAvailability(self, availability: MenuButton.AvailabilityStatus):
        """
        Setter for property: ( MenuButton.AvailabilityStatus NXOpen) ButtonAvailability
         Returns  the availability of the NXOpen button.  
              
         
        """
        pass
    @property
    def ButtonId(self) -> int:
        """
        Getter for property: (int) ButtonId
         Returns the identifier of the button.  
             
         
        """
        pass
    @property
    def ButtonName(self) -> str:
        """
        Getter for property: (str) ButtonName
         Returns the name of the button.  
             
         
        """
        pass
    @property
    def ButtonSensitivity(self) -> MenuButton.SensitivityStatus:
        """
        Getter for property: ( MenuButton.SensitivityStatus NXOpen) ButtonSensitivity
         Returns the sensitivity of the button.  
             
         
        """
        pass
    @ButtonSensitivity.setter
    def ButtonSensitivity(self, sensitivity: MenuButton.SensitivityStatus):
        """
        Setter for property: ( MenuButton.SensitivityStatus NXOpen) ButtonSensitivity
         Returns the sensitivity of the button.  
             
         
        """
        pass
    @property
    def ButtonType(self) -> MenuButton.Type:
        """
        Getter for property: ( MenuButton.Type NXOpen) ButtonType
         Returns the type of the button.  
             
         
        """
        pass
    @property
    def ButtonTypeName(self) -> str:
        """
        Getter for property: (str) ButtonTypeName
         Returns the type name of the button.  
             
         
        """
        pass
    @property
    def ToggleStatus(self) -> MenuButton.Toggle:
        """
        Getter for property: ( MenuButton.Toggle NXOpen) ToggleStatus
         Returns the toggle status of the button.  
             
         
        """
        pass
    @ToggleStatus.setter
    def ToggleStatus(self, toggle_status: MenuButton.Toggle):
        """
        Setter for property: ( MenuButton.Toggle NXOpen) ToggleStatus
         Returns the toggle status of the button.  
             
         
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is
                    called, it is illegal to use the object.  In .NET and Java,
                    his method is automatically called when the object is
                    deleted by the garbage collector.  
        """
        pass
