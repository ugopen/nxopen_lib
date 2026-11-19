from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents an Attachment for UI Styler 
## 
##   <br>  Created in NX5.0.0  <br> 

class Attachment(NXOpen.TransientObject): 
    """ Represents an Attachment for UI Styler """


    ##  Represents alignment option for Styler Item 
    ##  Dialog type 
    class AttachType(Enum):
        """
        Members Include: <Dialog> <Default> <NotSet> <NoChange> <Item>
        """
        Dialog: int
        Default: int
        NotSet: int
        NoChange: int
        Item: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Attachment.AttachType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Free resources associated with the instance. 
    ##      After this method is called, it is illegal to use the object.  
    ##      In .NET or Java, this method is automatically called when 
    ##      the object is deleted by the garbage collector. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(item_attachment: Attachment) -> None:
        """
         Free resources associated with the instance. 
             After this method is called, it is illegal to use the object.  
             In .NET or Java, this method is automatically called when 
             the object is deleted by the garbage collector. 
        """
        pass
    
    ##  Sets the attach type left
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetAttachTypeLeft(item_attachment: Attachment, attach_type_left: Attachment.AttachType) -> None:
        """
         Sets the attach type left
        """
        pass
    
    ##  Sets the attach type right
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetAttachTypeRight(item_attachment: Attachment, attach_type_right: Attachment.AttachType) -> None:
        """
         Sets the attach type right
        """
        pass
    
    ##  Sets the attach type top
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  attach_type_top 
    def SetAttachTypeTop(item_attachment: Attachment, attach_type_top: Attachment.AttachType) -> None:
        """
         Sets the attach type top
        """
        pass
    
    ##  Sets whether the dialog item is at the center
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  center
    def SetCenter(item_attachment: Attachment, is_center: bool) -> None:
        """
         Sets whether the dialog item is at the center
        """
        pass
    
    ##  Sets the left dialog item
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Left item identifier 
    def SetLeftDialogItem(item_attachment: Attachment, left_item_identifire: str) -> None:
        """
         Sets the left dialog item
        """
        pass
    
    ##  Sets the left offset
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetLeftOffset(item_attachment: Attachment, offset_left: int) -> None:
        """
         Sets the left offset
        """
        pass
    
    ##  Sets the right dialog item
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Right item identifier 
    def SetRightDialogItem(item_attachment: Attachment, right_item_identifire: str) -> None:
        """
         Sets the right dialog item
        """
        pass
    
    ##  Sets the right offset
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetRightOffset(item_attachment: Attachment, offset_right: int) -> None:
        """
         Sets the right offset
        """
        pass
    
    ##  Sets the top dialog item
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Top item identifier 
    def SetTopDialogItem(item_attachment: Attachment, top_item_identifire: str) -> None:
        """
         Sets the top dialog item
        """
        pass
    
    ##  Sets the top offset
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetTopOffset(item_attachment: Attachment, offset_top: int) -> None:
        """
         Sets the top offset
        """
        pass
    
##  Represents a Bit Map for UI Styler. 
## 
##   <br>  Created in NX5.0.0  <br> 

class BitMap(StylerItem): 
    """ Represents a Bit Map for UI Styler. """


    ##  Sets the bitmap filename. The filename extension must be: .UBM, .XPM, or .BMP.
    ##     The bitmap can be of any size.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  filename with .ubm, .xpm, or .bmp extension that contains bitmap definition 
    def SetBitmap(styler_item: BitMap, bitmap: str) -> None:
        """
         Sets the bitmap filename. The filename extension must be: .UBM, .XPM, or .BMP.
            The bitmap can be of any size.
        """
        pass
    
##  Represents a Button Layout for UI Styler. 
## 
##   <br>  Created in NX5.0.0  <br> 

class ButtonLayout(StylerItem): 
    """ Represents a Button Layout for UI Styler. """


    ## Getter for property: (bool) Visibility
    ##   the visibility   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
          the visibility   
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##   the visibility   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
          the visibility   
            
         
        """
        pass
    
    ## Called when a dialog user clicks on a push button or presses the spacebar when a push 
    ##     button has keyboard focus. 
    ## A callback definition with the following input arguments: 
    ##  - @link StylerEvent NXOpen.UIStyler.StylerEvent@endlink
    ##  and no return type
    Activate = Callable[[StylerEvent], None]
    
    
    ## Registers activate callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Callback for activate event 
    def AddActivateHandler(styler_item: ButtonLayout, activateevent: ButtonLayout.Activate, is_dialog_launching_event: bool) -> None:
        """
        Registers activate callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ##  Gets selected index 
    ##  @return value (int):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectedIndexValue(styler_item: ButtonLayout) -> int:
        """
         Gets selected index 
         @return value (int):  .
        """
        pass
    
    ##  Gets the sensitivity 
    ##  @return type (bool):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSensitivity(styler_item: ButtonLayout) -> bool:
        """
         Gets the sensitivity 
         @return type (bool):  .
        """
        pass
    
    ##  Sets default action 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def SetDefaultAction(styler_item: ButtonLayout) -> None:
        """
         Sets default action 
        """
        pass
    
    ##  Sets the sensitivity 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  If the entire dialog item should change to the new sensitivity state, 
    ##         set this field to UF_STYLER_NO_SUB_INDEX. If only one subitem should change to the new sensitivity 
    ##         state, set this field to its zero-based index. 
    def SetSensitivity(styler_item: ButtonLayout, subitem_index: int, type: bool) -> None:
        """
         Sets the sensitivity 
        """
        pass
    
##  Represents a Collapsible Group for UI Styler 
## 
##   <br>  Created in NX5.0.0  <br> 

class CollapsibleGroup(StylerItem): 
    """ Represents a Collapsible Group for UI Styler """


    ## Getter for property: (bool) CollapseState
    ##  the collapse-state  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.5  <br> 

    ## @return bool
    @property
    def CollapseState(self) -> bool:
        """
        Getter for property: (bool) CollapseState
         the collapse-state  
            
         
        """
        pass
    
    ## Setter for property: (bool) CollapseState

    ##  the collapse-state  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.5  <br> 

    @CollapseState.setter
    def CollapseState(self, item_val: bool):
        """
        Setter for property: (bool) CollapseState
         the collapse-state  
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##  the visibility  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.5  <br> 

    ## @return bool
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         the visibility  
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##  the visibility  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.5  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         the visibility  
            
         
        """
        pass
    
    ## Sets label of collapsible group
    ## 
    ##   <br>  Created in NX6.0.5  <br> 

    ## License requirements: None.
    ##  Text to be set as label 
    def SetLabel(styler_item: CollapsibleGroup, str_label: str) -> None:
        """
        Sets label of collapsible group
        """
        pass
    
##  Represents a ColorTool for UI Styler. 
## 
##   <br>  Created in NX5.0.0  <br> 

class ColorTool(StylerItem): 
    """ Represents a ColorTool for UI Styler. """


    ## Getter for property: (int) ItemValue
    ##   the item value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def ItemValue(self) -> int:
        """
        Getter for property: (int) ItemValue
          the item value   
            
         
        """
        pass
    
    ## Setter for property: (int) ItemValue

    ##   the item value   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ItemValue.setter
    def ItemValue(self, item_val: int):
        """
        Setter for property: (int) ItemValue
          the item value   
            
         
        """
        pass
    
    ## Getter for property: (bool) Sensitivity
    ##   the sensitivity   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Sensitivity(self) -> bool:
        """
        Getter for property: (bool) Sensitivity
          the sensitivity   
            
         
        """
        pass
    
    ## Setter for property: (bool) Sensitivity

    ##   the sensitivity   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
          the sensitivity   
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##   the visibility   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
          the visibility   
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##   the visibility   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
          the visibility   
            
         
        """
        pass
    
    ## Called when a dialog user enters a valid color value. 
    ## A callback definition with the following input arguments: 
    ##  - @link StylerEvent NXOpen.UIStyler.StylerEvent@endlink
    ##  and no return type
    ValueChanged = Callable[[StylerEvent], None]
    
    
    ## Registers value change callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Callback for value changed event 
    def AddValueChangedHandler(styler_item: ColorTool, valuechangedevent: ColorTool.ValueChanged, is_dialog_launching_event: bool) -> None:
        """
        Registers value change callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
##  Represents indexes 
##  All sub items are selected.
class DialogIndex(Enum):
    """
    Members Include: <NoSubIndex>
    """
    NoSubIndex: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> DialogIndex:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##  Represents a DialogItem for UI Styler. 
## 
##   <br>  Created in NX5.0.0  <br> 

class DialogItem(StylerItem): 
    """ Represents a DialogItem for UI Styler. """


    ##  Describes dialog item index 
    ##  Ok index 
    class DialogItemIndex(Enum):
        """
        Members Include: <Ok> <Apply> <Back> <Cancel>
        """
        Ok: int
        Apply: int
        Back: int
        Cancel: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DialogItem.DialogItemIndex:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link FileOperationData NXOpen.UIStyler.FileOperationData@endlink) FileOperationData
    ##   the file operation data   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return FileOperationData
    @property
    def FileOperationData(self) -> FileOperationData:
        """
        Getter for property: (@link FileOperationData NXOpen.UIStyler.FileOperationData@endlink) FileOperationData
          the file operation data   
            
         
        """
        pass
    
    ## Called when a dialog user clicks Apply or \<Ctrl\>MB2 anywhere in NX or presses the Apply's 
    ##     keyboard accelerator as defined in the resource file. Apply callbacks should not terminate 
    ##     the dialog and always return UF_UI_CB_CONTINUE_DIALOG. 
    ## A callback definition with the following input arguments: 
    ##  - @link StylerEvent NXOpen.UIStyler.StylerEvent@endlink
    ##  and no return type
    Apply = Callable[[StylerEvent], None]
    
    
    ## Registers apply callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddApplyHandler(styler_item: DialogItem, applyevent: DialogItem.Apply, is_dialog_launching_event: bool) -> None:
        """
        Registers apply callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ## Called when a dialog user clicks Back \<Shift\>MB2 anywhere in NX or presses Back's keyboard accelerator 
    ##     as defined in the resource file. Back callbacks should terminate the dialog and always return 
    ##     UF_UI_CB_EXIT_DIALOG. 
    ## A callback definition with the following input arguments: 
    ##  - @link StylerEvent NXOpen.UIStyler.StylerEvent@endlink
    ##  and no return type
    Back = Callable[[StylerEvent], None]
    
    
    ## Registers back callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddBackHandler(styler_item: DialogItem, backevent: DialogItem.Back, is_dialog_launching_event: bool) -> None:
        """
        Registers back callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ## Called when a dialog user clicks Cancel or \<Alt\>MB2 anywhere in NX or presses Cancel's keyboard accelerator 
    ##     as defined in the resource file.Cancel callbacks should terminate the dialog and always return UF_UI_CB_EXIT_DIALOG. 
    ## A callback definition with the following input arguments: 
    ##  - @link StylerEvent NXOpen.UIStyler.StylerEvent@endlink
    ##  and no return type
    Cancel = Callable[[StylerEvent], None]
    
    
    ## Registers cancel callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddCancelHandler(styler_item: DialogItem, cancelevent: DialogItem.Cancel, is_dialog_launching_event: bool) -> None:
        """
        Registers cancel callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ## Called when the dialog displays. You can use the Constructor callback to set up dialog item attributes 
    ##     such as populating a list or setting the sensitivity of a dialog item. 
    ## A callback definition with the following input arguments: 
    ##  - @link StylerEvent NXOpen.UIStyler.StylerEvent@endlink
    ##  and no return type
    Construct = Callable[[StylerEvent], None]
    
    
    ## Registers construct callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddConstructHandler(styler_item: DialogItem, constructevent: DialogItem.Construct, is_dialog_launching_event: bool) -> None:
        """
        Registers construct callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ## Called when the dialog closes. Use the Destructor callback to perform cleanup. 
    ## A callback definition with the following input arguments: 
    ##  - @link StylerEvent NXOpen.UIStyler.StylerEvent@endlink
    ##  and no return type
    Destruct = Callable[[StylerEvent], None]
    
    
    ## Registers destruct callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddDestructHandler(styler_item: DialogItem, destructevent: DialogItem.Destruct, is_dialog_launching_event: bool) -> None:
        """
        Registers destruct callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ## Called just before a dialog user selects a file operation, such as in File?New, and again after a file
    ##     operation completes.
    ##     A typical use for a file operation callback would be to make sure that the system updates cached part data 
    ##     in a part before a dialog user executes a File?Save. The callback can determine from the callback data 
    ##     structure whether the file operation is about to begin or has just completed. It can also determine 
    ##     which operation is being executed. This callback is only used on DA1 dialogs because the DA2 dialogs 
    ##     are usually cancelled (automatically through the quick access menus) when a dialog user selects any of 
    ##     the File menu options. 
    ## A callback definition with the following input arguments: 
    ##  - @link StylerEvent NXOpen.UIStyler.StylerEvent@endlink
    ##  and no return type
    FileOperation = Callable[[StylerEvent], None]
    
    
    ## Registers file operation callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddFileOperationHandler(styler_item: DialogItem, fileoperationevent: DialogItem.FileOperation, is_dialog_launching_event: bool) -> None:
        """
        Registers file operation callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ## Called when a dialog user clicks OK or MB2 anywhere in NX or presses the OK's keyboard accelerator 
    ##     as defined in the resource file. OK callbacks should terminate the dialog and always return 
    ##     UF_UI_CB_EXIT_DIALOG. 
    ##     
    ## A callback definition with the following input arguments: 
    ##  - @link StylerEvent NXOpen.UIStyler.StylerEvent@endlink
    ##  and no return type
    Okay = Callable[[StylerEvent], None]
    
    
    ## Registers ok callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddOkayHandler(styler_item: DialogItem, okayevent: DialogItem.Okay, is_dialog_launching_event: bool) -> None:
        """
        Registers ok callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ## Called when a user switches tabs. 
    ## A callback definition with the following input arguments: 
    ##  - @link StylerEvent NXOpen.UIStyler.StylerEvent@endlink
    ##  and no return type
    PageSwitch = Callable[[StylerEvent], None]
    
    
    ## Registers switch callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
    ## 
    ##   <br>  Created in NX8.5.3  <br> 

    ## License requirements: None.
    ##  
    def AddPageSwitchHandler(styler_item: DialogItem, switchevent: DialogItem.PageSwitch, is_dialog_launching_event: bool) -> None:
        """
        Registers switch callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ##  Gets the selection handle for a given dialog item
    ##  @return select (@link NXOpen.SelectionHandle NXOpen.SelectionHandle@endlink): Selection handle .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectionHandle(styler_item: DialogItem) -> NXOpen.SelectionHandle:
        """
         Gets the selection handle for a given dialog item
         @return select (@link NXOpen.SelectionHandle NXOpen.SelectionHandle@endlink): Selection handle .
        """
        pass
    
    ##  Specifies the sensitivity of the navigation buttons at the bottom of the dialog. If you set the 
    ##     UF_STYLER_BACK_INDEX button to insensitive at creation time, the system does not show the BACK button; 
    ##     Changing the button's sensitivity while the dialog displays does not show the Back button. 
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Sub item index 
    def SetNavigationSensitivity(styler_item: DialogItem, sub_item_index: DialogItem.DialogItemIndex, type: bool) -> None:
        """
         Specifies the sensitivity of the navigation buttons at the bottom of the dialog. If you set the 
            UF_STYLER_BACK_INDEX button to insensitive at creation time, the system does not show the BACK button; 
            Changing the button's sensitivity while the dialog displays does not show the Back button. 
            
        """
        pass
    
    ## Specifies wether dialog is allowed to resize 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## TRUE to allow dialog to resize; FALSE to freeze the dialog size
    def SetResize(styler_item: DialogItem, type: bool) -> None:
        """
        Specifies wether dialog is allowed to resize 
        """
        pass
    
    ## Specifies the sensitivity of the dialog. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## TRUE if sensitive, FALSE if insensitive 
    def SetSensitivity(styler_item: DialogItem, type: bool) -> None:
        """
        Specifies the sensitivity of the dialog. 
        """
        pass
    
    ## Specifies a string to display on the top border of the dialog 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetTitle(styler_item: DialogItem, str_label: str) -> None:
        """
        Specifies a string to display on the top border of the dialog 
        """
        pass
    
    ## Specifies the pixel width for the dialog. You can only set this attribute when the 
    ##     Dialog Resize attribute is set to TRUE. You cannot enter a negative number. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetWidth(styler_item: DialogItem, width: int) -> None:
        """
        Specifies the pixel width for the dialog. You can only set this attribute when the 
            Dialog Resize attribute is set to TRUE. You cannot enter a negative number. 
        """
        pass
    
##  Represents dialog response 
##  User response was a selection of objects.
class DialogResponse(Enum):
    """
    Members Include: <PickResponse> <Ok> <Cancel> <Back> <Apply> <Help> <ObjectSelected> <ObjectSelectedByName> <CbTerminate>
    """
    PickResponse: int
    Ok: int
    Cancel: int
    Back: int
    Apply: int
    Help: int
    ObjectSelected: int
    ObjectSelectedByName: int
    CbTerminate: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> DialogResponse:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the dialog state 
##  Continue the dialog 
class DialogState(Enum):
    """
    Members Include: <ContinueDialog> <ExitDialog>
    """
    ContinueDialog: int
    ExitDialog: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> DialogState:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##  Represents a DialogItem for UI Styler. 
## 
##   <br>  Created in NX5.0.0  <br> 

class Dialog(NXOpen.TransientObject): 
    """ Represents a DialogItem for UI Styler. """


    ##  Represents dialog item type 
    ##   
    class ItemType(Enum):
        """
        Members Include: <PushButton> <DialogItem> <RadioBox> <RealItem> <RealScale> <Bitmap> <RowColumn> <ButtonLayout> <ScrolledWindow> <ColorTool> <SelectionBox> <Separator> <SingleSelectList> <StringItem> <GroupBox> <IntegerItem> <IntegerScale> <MultiSelectList> <LabelItem> <MultiTextBox> <TabControl> <OptionMenu> <Toggle> <OptionToggle> <ToolPalette> <WideString> <PropertyPage> <CollapsibleGroup>
        """
        PushButton: int
        DialogItem: int
        RadioBox: int
        RealItem: int
        RealScale: int
        Bitmap: int
        RowColumn: int
        ButtonLayout: int
        ScrolledWindow: int
        ColorTool: int
        SelectionBox: int
        Separator: int
        SingleSelectList: int
        StringItem: int
        GroupBox: int
        IntegerItem: int
        IntegerScale: int
        MultiSelectList: int
        LabelItem: int
        MultiTextBox: int
        TabControl: int
        OptionMenu: int
        Toggle: int
        OptionToggle: int
        ToolPalette: int
        WideString: int
        PropertyPage: int
        CollapsibleGroup: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Dialog.ItemType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Free resources associated with the instance. After this method
    ##     is called, it is illegal to use the object.  In .NET or Java, this 
    ##     method is automatically called when the object is deleted by the 
    ##     garbage collector. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(dialog: Dialog) -> None:
        """
         Free resources associated with the instance. After this method
            is called, it is illegal to use the object.  In .NET or Java, this 
            method is automatically called when the object is deleted by the 
            garbage collector. 
        """
        pass
    
    ##  Gets the dialog item with specified item identifier 
    ##  @return item (@link BitMap NXOpen.UIStyler.BitMap@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Dialog name 
    def GetBitmap(dialog_data: Dialog, item_identifier: str) -> BitMap:
        """
         Gets the dialog item with specified item identifier 
         @return item (@link BitMap NXOpen.UIStyler.BitMap@endlink):  .
        """
        pass
    
    ##  Gets the dialog item with specified item identifier 
    ##  @return item (@link ButtonLayout NXOpen.UIStyler.ButtonLayout@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Dialog name 
    def GetButtonLayout(dialog_data: Dialog, item_identifier: str) -> ButtonLayout:
        """
         Gets the dialog item with specified item identifier 
         @return item (@link ButtonLayout NXOpen.UIStyler.ButtonLayout@endlink):  .
        """
        pass
    
    ##  Gets the dialog item with specified item identifier 
    ##  @return item (@link CollapsibleGroup NXOpen.UIStyler.CollapsibleGroup@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Dialog name 
    def GetCollapsibleGroup(dialog_data: Dialog, item_identifier: str) -> CollapsibleGroup:
        """
         Gets the dialog item with specified item identifier 
         @return item (@link CollapsibleGroup NXOpen.UIStyler.CollapsibleGroup@endlink):  .
        """
        pass
    
    ##  Gets the dialog item with specified item identifier 
    ##  @return item (@link ColorTool NXOpen.UIStyler.ColorTool@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Dialog name 
    def GetColorTool(dialog_data: Dialog, item_identifier: str) -> ColorTool:
        """
         Gets the dialog item with specified item identifier 
         @return item (@link ColorTool NXOpen.UIStyler.ColorTool@endlink):  .
        """
        pass
    
    ##  Gets the dialog item with specified item identifier 
    ##  @return item (@link DialogItem NXOpen.UIStyler.DialogItem@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Dialog name 
    def GetDialogIndex(dialog_data: Dialog, item_identifier: str) -> DialogItem:
        """
         Gets the dialog item with specified item identifier 
         @return item (@link DialogItem NXOpen.UIStyler.DialogItem@endlink):  .
        """
        pass
    
    ##  Gets the dialog item for a selection handle 
    ##  @return item (@link StylerItem NXOpen.UIStyler.StylerItem@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## Selection handle 
    def GetDialogItemUsingSelectionHandle(dialog_data: Dialog, select: NXOpen.SelectionHandle) -> StylerItem:
        """
         Gets the dialog item for a selection handle 
         @return item (@link StylerItem NXOpen.UIStyler.StylerItem@endlink):  .
        """
        pass
    
    ##  Gets the dialog item with specified item identifier 
    ##  @return item (@link GroupBox NXOpen.UIStyler.GroupBox@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Dialog name 
    def GetGroupBox(dialog_data: Dialog, item_identifier: str) -> GroupBox:
        """
         Gets the dialog item with specified item identifier 
         @return item (@link GroupBox NXOpen.UIStyler.GroupBox@endlink):  .
        """
        pass
    
    ##  Gets the dialog item with specified item identifier 
    ##  @return item (@link IntegerItem NXOpen.UIStyler.IntegerItem@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Dialog name 
    def GetIntegerItem(dialog_data: Dialog, item_identifier: str) -> IntegerItem:
        """
         Gets the dialog item with specified item identifier 
         @return item (@link IntegerItem NXOpen.UIStyler.IntegerItem@endlink):  .
        """
        pass
    
    ##  Gets the dialog item with specified item identifier 
    ##  @return item (@link IntegerScale NXOpen.UIStyler.IntegerScale@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Dialog name 
    def GetIntegerScale(dialog_data: Dialog, item_identifier: str) -> IntegerScale:
        """
         Gets the dialog item with specified item identifier 
         @return item (@link IntegerScale NXOpen.UIStyler.IntegerScale@endlink):  .
        """
        pass
    
    ##  Gets the dialog item with specified item identifier 
    ##  @return item (@link LabelItem NXOpen.UIStyler.LabelItem@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Dialog name 
    def GetLabelItem(dialog_data: Dialog, item_identifier: str) -> LabelItem:
        """
         Gets the dialog item with specified item identifier 
         @return item (@link LabelItem NXOpen.UIStyler.LabelItem@endlink):  .
        """
        pass
    
    ##  Gets the dialog item with specified item identifier 
    ##  @return item (@link MultiSelectList NXOpen.UIStyler.MultiSelectList@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Dialog name 
    def GetMultiSelectList(dialog_data: Dialog, item_identifier: str) -> MultiSelectList:
        """
         Gets the dialog item with specified item identifier 
         @return item (@link MultiSelectList NXOpen.UIStyler.MultiSelectList@endlink):  .
        """
        pass
    
    ##  Gets the dialog item with specified item identifier 
    ##  @return item (@link MultiTextBox NXOpen.UIStyler.MultiTextBox@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Dialog name 
    def GetMultiTextBox(dialog_data: Dialog, item_identifier: str) -> MultiTextBox:
        """
         Gets the dialog item with specified item identifier 
         @return item (@link MultiTextBox NXOpen.UIStyler.MultiTextBox@endlink):  .
        """
        pass
    
    ##  Gets the dialog item with specified item identifier 
    ##  @return item (@link OptionMenu NXOpen.UIStyler.OptionMenu@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Dialog name 
    def GetOptionMenu(dialog_data: Dialog, item_identifier: str) -> OptionMenu:
        """
         Gets the dialog item with specified item identifier 
         @return item (@link OptionMenu NXOpen.UIStyler.OptionMenu@endlink):  .
        """
        pass
    
    ##  Gets the dialog item with specified item identifier 
    ##  @return item (@link OptionToggle NXOpen.UIStyler.OptionToggle@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Dialog name 
    def GetOptionToggle(dialog_data: Dialog, item_identifier: str) -> OptionToggle:
        """
         Gets the dialog item with specified item identifier 
         @return item (@link OptionToggle NXOpen.UIStyler.OptionToggle@endlink):  .
        """
        pass
    
    ##  Gets the dialog item with specified item identifier 
    ##  @return item (@link PropertyPage NXOpen.UIStyler.PropertyPage@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Dialog name 
    def GetPropertyPage(dialog_data: Dialog, item_identifier: str) -> PropertyPage:
        """
         Gets the dialog item with specified item identifier 
         @return item (@link PropertyPage NXOpen.UIStyler.PropertyPage@endlink):  .
        """
        pass
    
    ##  Gets the dialog item with specified item identifier 
    ##  @return item (@link PushButton NXOpen.UIStyler.PushButton@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Dialog name 
    def GetPushButton(dialog_data: Dialog, item_identifier: str) -> PushButton:
        """
         Gets the dialog item with specified item identifier 
         @return item (@link PushButton NXOpen.UIStyler.PushButton@endlink):  .
        """
        pass
    
    ##  Gets the dialog item with specified item identifier 
    ##  @return item (@link RadioBox NXOpen.UIStyler.RadioBox@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Dialog name 
    def GetRadioBox(dialog_data: Dialog, item_identifier: str) -> RadioBox:
        """
         Gets the dialog item with specified item identifier 
         @return item (@link RadioBox NXOpen.UIStyler.RadioBox@endlink):  .
        """
        pass
    
    ##  Gets the dialog item with specified item identifier 
    ##  @return item (@link RealItem NXOpen.UIStyler.RealItem@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Dialog name 
    def GetRealItem(dialog_data: Dialog, item_identifier: str) -> RealItem:
        """
         Gets the dialog item with specified item identifier 
         @return item (@link RealItem NXOpen.UIStyler.RealItem@endlink):  .
        """
        pass
    
    ##  Gets the dialog item with specified item identifier 
    ##  @return item (@link RealScale NXOpen.UIStyler.RealScale@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Dialog name 
    def GetRealScale(dialog_data: Dialog, item_identifier: str) -> RealScale:
        """
         Gets the dialog item with specified item identifier 
         @return item (@link RealScale NXOpen.UIStyler.RealScale@endlink):  .
        """
        pass
    
    ##  Gets the dialog item with specified item identifier 
    ##  @return item (@link RowColumn NXOpen.UIStyler.RowColumn@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Dialog name 
    def GetRowColumn(dialog_data: Dialog, item_identifier: str) -> RowColumn:
        """
         Gets the dialog item with specified item identifier 
         @return item (@link RowColumn NXOpen.UIStyler.RowColumn@endlink):  .
        """
        pass
    
    ##  Gets the dialog item with specified item identifier 
    ##  @return item (@link ScrolledWindow NXOpen.UIStyler.ScrolledWindow@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Dialog name 
    def GetScrolledWindow(dialog_data: Dialog, item_identifier: str) -> ScrolledWindow:
        """
         Gets the dialog item with specified item identifier 
         @return item (@link ScrolledWindow NXOpen.UIStyler.ScrolledWindow@endlink):  .
        """
        pass
    
    ##  Gets the dialog item with specified item identifier 
    ##  @return item (@link SelectionBox NXOpen.UIStyler.SelectionBox@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Dialog name 
    def GetSelectionBox(dialog_data: Dialog, item_identifier: str) -> SelectionBox:
        """
         Gets the dialog item with specified item identifier 
         @return item (@link SelectionBox NXOpen.UIStyler.SelectionBox@endlink):  .
        """
        pass
    
    ##  Gets the dialog item with specified item identifier 
    ##  @return item (@link Separator NXOpen.UIStyler.Separator@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Dialog name 
    def GetSeparator(dialog_data: Dialog, item_identifier: str) -> Separator:
        """
         Gets the dialog item with specified item identifier 
         @return item (@link Separator NXOpen.UIStyler.Separator@endlink):  .
        """
        pass
    
    ##  Gets the dialog item with specified item identifier 
    ##  @return item (@link SingleSelectList NXOpen.UIStyler.SingleSelectList@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Dialog name 
    def GetSingleSelectList(dialog_data: Dialog, item_identifier: str) -> SingleSelectList:
        """
         Gets the dialog item with specified item identifier 
         @return item (@link SingleSelectList NXOpen.UIStyler.SingleSelectList@endlink):  .
        """
        pass
    
    ##  Gets the dialog item with specified item identifier 
    ##  @return item (@link StringItem NXOpen.UIStyler.StringItem@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Dialog name 
    def GetStringItem(dialog_data: Dialog, item_identifier: str) -> StringItem:
        """
         Gets the dialog item with specified item identifier 
         @return item (@link StringItem NXOpen.UIStyler.StringItem@endlink):  .
        """
        pass
    
    ##  Gets the dialog item with specified item identifier 
    ##  @return item (@link StylerItem NXOpen.UIStyler.StylerItem@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Dialog name 
    def GetStylerItem(dialog_data: Dialog, item_identifier: str, type: Dialog.ItemType) -> StylerItem:
        """
         Gets the dialog item with specified item identifier 
         @return item (@link StylerItem NXOpen.UIStyler.StylerItem@endlink):  .
        """
        pass
    
    ##  Gets the dialog item with specified item identifier 
    ##  @return item (@link TabControl NXOpen.UIStyler.TabControl@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Dialog name 
    def GetTabControl(dialog_data: Dialog, item_identifier: str) -> TabControl:
        """
         Gets the dialog item with specified item identifier 
         @return item (@link TabControl NXOpen.UIStyler.TabControl@endlink):  .
        """
        pass
    
    ##  Gets the dialog item with specified item identifier 
    ##  @return item (@link Toggle NXOpen.UIStyler.Toggle@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Dialog name 
    def GetToggle(dialog_data: Dialog, item_identifier: str) -> Toggle:
        """
         Gets the dialog item with specified item identifier 
         @return item (@link Toggle NXOpen.UIStyler.Toggle@endlink):  .
        """
        pass
    
    ##  Gets the dialog item with specified item identifier 
    ##  @return item (@link ToolPalette NXOpen.UIStyler.ToolPalette@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Dialog name 
    def GetToolPalette(dialog_data: Dialog, item_identifier: str) -> ToolPalette:
        """
         Gets the dialog item with specified item identifier 
         @return item (@link ToolPalette NXOpen.UIStyler.ToolPalette@endlink):  .
        """
        pass
    
    ##  Gets the dialog item with specified item identifier 
    ##  @return item (@link WideString NXOpen.UIStyler.WideString@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Dialog name 
    def GetWideString(dialog_data: Dialog, item_identifier: str) -> WideString:
        """
         Gets the dialog item with specified item identifier 
         @return item (@link WideString NXOpen.UIStyler.WideString@endlink):  .
        """
        pass
    
    ##  Registers the dialog with a menu item.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def RegisterWithUiMenu(dialog_data: Dialog, is_top_dialog: bool) -> None:
        """
         Registers the dialog with a menu item.
        """
        pass
    
    ##  Displays an NX (UIStyler generated) "bottom" dialog.  This dialog 
    ##         is displayed to NX. Show Method can only be called once for the 
    ##         dialog object.Once show method is called @link UIStyler::Dialog::GetStylerItem UIStyler::Dialog::GetStylerItem@endlink  
    ##         will create any item
    ##     
    ##  @return response (@link DialogResponse NXOpen.UIStyler.DialogResponse@endlink): .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Show(dialog_data: Dialog) -> DialogResponse:
        """
         Displays an NX (UIStyler generated) "bottom" dialog.  This dialog 
                is displayed to NX. Show Method can only be called once for the 
                dialog object.Once show method is called @link UIStyler::Dialog::GetStylerItem UIStyler::Dialog::GetStylerItem@endlink  
                will create any item
            
         @return response (@link DialogResponse NXOpen.UIStyler.DialogResponse@endlink): .
        """
        pass
    
import NXOpen
##  Represents a FileOperationData for UI Styler 
## 
##   <br>  Created in NX5.0.0  <br> 

class FileOperationData(NXOpen.TransientObject): 
    """ Represents a FileOperationData for UI Styler """


    ##  Describes file state 
    ##  Enter file state 
    class FileOperationState(Enum):
        """
        Members Include: <Enter> <Exit>
        """
        Enter: int
        Exit: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FileOperationData.FileOperationState:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Describes file operation 
    ##  New file operation 
    class FileOperationType(Enum):
        """
        Members Include: <New> <Open> <Save> <SaveAs> <SaveAll> <Close> <Quit> <SaveAndExit> <ChangePart> <Execute> <Reopen> <SaveAllAndClose> <SaveAndClose> <SaveAsAndClose>
        """
        New: int
        Open: int
        Save: int
        SaveAs: int
        SaveAll: int
        Close: int
        Quit: int
        SaveAndExit: int
        ChangePart: int
        Execute: int
        Reopen: int
        SaveAllAndClose: int
        SaveAndClose: int
        SaveAsAndClose: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FileOperationData.FileOperationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link FileOperationData.FileOperationState NXOpen.UIStyler.FileOperationData.FileOperationState@endlink) State
    ##   the state   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return FileOperationData.FileOperationState
    @property
    def State(self) -> FileOperationData.FileOperationState:
        """
        Getter for property: (@link FileOperationData.FileOperationState NXOpen.UIStyler.FileOperationData.FileOperationState@endlink) State
          the state   
            
         
        """
        pass
    
    ## Getter for property: (@link FileOperationData.FileOperationType NXOpen.UIStyler.FileOperationData.FileOperationType@endlink) Type
    ##   the file operation type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return FileOperationData.FileOperationType
    @property
    def Type(self) -> FileOperationData.FileOperationType:
        """
        Getter for property: (@link FileOperationData.FileOperationType NXOpen.UIStyler.FileOperationData.FileOperationType@endlink) Type
          the file operation type   
            
         
        """
        pass
    
    ##  Free resources associated with the instance. After this method
    ##     is called, it is illegal to use the object.  In .NET or Java, this 
    ##     method is automatically called when the object is deleted by the 
    ##     garbage collector. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(file_op_data: FileOperationData) -> None:
        """
         Free resources associated with the instance. After this method
            is called, it is illegal to use the object.  In .NET or Java, this 
            method is automatically called when the object is deleted by the 
            garbage collector. 
        """
        pass
    
##  Represents a GroupBox for UI Styler. 
## 
##   <br>  Created in NX5.0.0  <br> 

class GroupBox(StylerItem): 
    """ Represents a GroupBox for UI Styler. """


    ## Getter for property: (bool) Sensitivity
    ##   the sensitivity   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Sensitivity(self) -> bool:
        """
        Getter for property: (bool) Sensitivity
          the sensitivity   
            
         
        """
        pass
    
    ## Setter for property: (bool) Sensitivity

    ##   the sensitivity   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
          the sensitivity   
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##   the visibility   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
          the visibility   
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##   the visibility   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
          the visibility   
            
         
        """
        pass
    
    ##  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Text label to display in the top line of the group box frame 
    def SetLabel(styler_item: GroupBox, str_label: str) -> None:
        """
         
        """
        pass
    
##  Represents a Integer for UI Styler. 
## 
##   <br>  Created in NX5.0.0  <br> 

class IntegerItem(StylerItem): 
    """ Represents a Integer for UI Styler. """


    ## Getter for property: (int) ItemValue
    ##  the value obtained from the text field.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def ItemValue(self) -> int:
        """
        Getter for property: (int) ItemValue
         the value obtained from the text field.  
            
         
        """
        pass
    
    ## Setter for property: (int) ItemValue

    ##  the value obtained from the text field.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ItemValue.setter
    def ItemValue(self, item_val: int):
        """
        Setter for property: (int) ItemValue
         the value obtained from the text field.  
            
         
        """
        pass
    
    ## Getter for property: (bool) Sensitivity
    ##   the sensitivity of Integer item   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Sensitivity(self) -> bool:
        """
        Getter for property: (bool) Sensitivity
          the sensitivity of Integer item   
            
         
        """
        pass
    
    ## Setter for property: (bool) Sensitivity

    ##   the sensitivity of Integer item   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
          the sensitivity of Integer item   
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##   the visibility of the dialog item.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
          the visibility of the dialog item.  
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##   the visibility of the dialog item.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
          the visibility of the dialog item.  
            
         
        """
        pass
    
    ## Called when a dialog user enters a valid integer value and presses Return 
    ## A callback definition with the following input arguments: 
    ##  - @link StylerEvent NXOpen.UIStyler.StylerEvent@endlink
    ##  and no return type
    Activate = Callable[[StylerEvent], None]
    
    
    ## Registers activate callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddActivateHandler(styler_item: IntegerItem, activateevent: IntegerItem.Activate, is_dialog_launching_event: bool) -> None:
        """
        Registers activate callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ## Specifies a filename that contains a bitmap definition. The filename must contain a UBM, XPM, or BMP 
    ##     extension. When you use this field, the system displays a bitmap for this dialog item instead of a text 
    ##     label. When a bitmap is present, the system uses the text label as tooltip text when a user places the 
    ##     mouse cursor over the bitmap. We recommend that you use a 16x16 bitmap for this dialog item. 
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## Filename with .ubm, .xpm, or .bmp extension that contains bitmap definition
    def SetBitmap(styler_item: IntegerItem, bitmap: str) -> None:
        """
        Specifies a filename that contains a bitmap definition. The filename must contain a UBM, XPM, or BMP 
            extension. When you use this field, the system displays a bitmap for this dialog item instead of a text 
            label. When a bitmap is present, the system uses the text label as tooltip text when a user places the 
            mouse cursor over the bitmap. We recommend that you use a 16x16 bitmap for this dialog item. 
            
        """
        pass
    
    ##  Sets focus 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def SetFocus(styler_item: IntegerItem) -> None:
        """
         Sets focus 
        """
        pass
    
    ## Specifies descriptive text to display for the dialog item. It should describe the dialog 
    ##     item's intended use. If you specify a bitmap for this dialog item, it uses this text as tooltip text. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  String to display on the left side of the text field.
    def SetLabel(styler_item: IntegerItem, str_label: str) -> None:
        """
        Specifies descriptive text to display for the dialog item. It should describe the dialog 
            item's intended use. If you specify a bitmap for this dialog item, it uses this text as tooltip text. 
        """
        pass
    
##  Represents a IntegerScale for UI Styler 
## 
##   <br>  Created in NX5.0.0  <br> 

class IntegerScale(StylerItem): 
    """ Represents a IntegerScale for UI Styler """


    ## Getter for property: (int) ItemValue
    ##     
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def ItemValue(self) -> int:
        """
        Getter for property: (int) ItemValue
            
            
         
        """
        pass
    
    ## Setter for property: (int) ItemValue

    ##     
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ItemValue.setter
    def ItemValue(self, item_val: int):
        """
        Setter for property: (int) ItemValue
            
            
         
        """
        pass
    
    ## Getter for property: (bool) Sensitivity
    ##   the sensitivity of the dialog item.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Sensitivity(self) -> bool:
        """
        Getter for property: (bool) Sensitivity
          the sensitivity of the dialog item.  
             
         
        """
        pass
    
    ## Setter for property: (bool) Sensitivity

    ##   the sensitivity of the dialog item.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
          the sensitivity of the dialog item.  
             
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##  the visibility of the dialog item.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         the visibility of the dialog item.  
             
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##  the visibility of the dialog item.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         the visibility of the dialog item.  
             
         
        """
        pass
    
    ## Called when a dialog user moves the slider up and down the scale. For example, if a user moves the 
    ##     slider from 0 to 100, the dialog calls the drag callback 100 times, one for each value that the 
    ##     slider moves across. 
    ##     Do not terminate the dialog with a drag callback. The dialog should always return 
    ##     UF_UI_CB_CONTINUE_DIALOG. 
    ## A callback definition with the following input arguments: 
    ##  - @link StylerEvent NXOpen.UIStyler.StylerEvent@endlink
    ##  and no return type
    Drag = Callable[[StylerEvent], None]
    
    
    ## Registers drag callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddDragHandler(styler_item: IntegerScale, dragevent: IntegerScale.Drag, is_dialog_launching_event: bool) -> None:
        """
        Registers drag callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ## Called when a dialog user moves the slider to a new position. 
    ##     Do not terminate the dialog with a value-changed callback. The dialog should always return 
    ##     UF_UI_CB_CONTINUE_DIALOG. 
    ## A callback definition with the following input arguments: 
    ##  - @link StylerEvent NXOpen.UIStyler.StylerEvent@endlink
    ##  and no return type
    ValueChanged = Callable[[StylerEvent], None]
    
    
    ## Registers value change callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Value changed event 
    def AddValueChangedHandler(styler_item: IntegerScale, valuechangedevent: IntegerScale.ValueChanged, is_dialog_launching_event: bool) -> None:
        """
        Registers value change callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ## Specifies the text for the minimum and maximum label. By default, the system uses the maximum/minimum 
    ##     value as a text label.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## minimum limit for label 
    def SetLabels(styler_item: IntegerScale, minimum_label: str, maximum_label: str) -> None:
        """
        Specifies the text for the minimum and maximum label. By default, the system uses the maximum/minimum 
            value as a text label.
        """
        pass
    
    ## Specifies the scale's maximum and minimum value.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## to set minimum 
    def SetLimits(styler_item: IntegerScale, minimum_value: int, maximum_value: int) -> None:
        """
        Specifies the scale's maximum and minimum value.
        """
        pass
    
##  Represents a Label for UI Styler. 
## 
##   <br>  Created in NX5.0.0  <br> 

class LabelItem(StylerItem): 
    """ Represents a Label for UI Styler. """


    ## Getter for property: (bool) Sensitivity
    ##   the seisitivity of the dialog item  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Sensitivity(self) -> bool:
        """
        Getter for property: (bool) Sensitivity
          the seisitivity of the dialog item  
            
         
        """
        pass
    
    ## Setter for property: (bool) Sensitivity

    ##   the seisitivity of the dialog item  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
          the seisitivity of the dialog item  
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##   the visibility of the dialog item  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
          the visibility of the dialog item  
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##   the visibility of the dialog item  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
          the visibility of the dialog item  
            
         
        """
        pass
    
    ##  Specifies a filename that contains a bitmap definition. 
    ##     The filename must contain a UBM, XPM, or BMP extension. 
    ##     When you use this field, the system displays a bitmap for this dialog item 
    ##     instead of a text label. When a bitmap is present, the system uses 
    ##     the text label as tooltip text when a user places the mouse cursor over the bitmap. 
    ##     We recommend that you use a 16x16 bitmap for this dialog item. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetBitmap(styler_item: LabelItem, bitmap_file: str) -> None:
        """
         Specifies a filename that contains a bitmap definition. 
            The filename must contain a UBM, XPM, or BMP extension. 
            When you use this field, the system displays a bitmap for this dialog item 
            instead of a text label. When a bitmap is present, the system uses 
            the text label as tooltip text when a user places the mouse cursor over the bitmap. 
            We recommend that you use a 16x16 bitmap for this dialog item. 
        """
        pass
    
    ##  Specifies descriptive text to display for the dialog item. It should describe the dialog item's intended use.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetLabel(styler_item: LabelItem, str_label: str) -> None:
        """
         Specifies descriptive text to display for the dialog item. It should describe the dialog item's intended use.
        """
        pass
    
##  Represents a MultiSelectList for UI Styler 
## 
##   <br>  Created in NX5.0.0  <br> 

class MultiSelectList(StylerItem): 
    """ Represents a MultiSelectList for UI Styler """


    ## Getter for property: (bool) Sensitivity
    ##   the senstivity   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Sensitivity(self) -> bool:
        """
        Getter for property: (bool) Sensitivity
          the senstivity   
            
         
        """
        pass
    
    ## Setter for property: (bool) Sensitivity

    ##   the senstivity   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
          the senstivity   
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##  the visibility  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         the visibility  
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##  the visibility  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         the visibility  
            
         
        """
        pass
    
    ##  
    ## A callback definition with the following input arguments: 
    ##  - @link StylerEvent NXOpen.UIStyler.StylerEvent@endlink
    ##  and no return type
    Activate = Callable[[StylerEvent], None]
    
    
    ## Called when a dialog user selects an entry with a double mouse click or presses Return on 
    ##     a selected item. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddActivateHandler(styler_item: MultiSelectList, activateevent: MultiSelectList.Activate, is_dialog_launching_event: bool) -> None:
        """
        Called when a dialog user selects an entry with a double mouse click or presses Return on 
            a selected item. 
        """
        pass
    
    ## Called when a dialog user selects an entry with a single mouse click or presses the spacebar 
    ##     on a selected item.  
    ## A callback definition with the following input arguments: 
    ##  - @link StylerEvent NXOpen.UIStyler.StylerEvent@endlink
    ##  and no return type
    DoubleClick = Callable[[StylerEvent], None]
    
    
    ## Registers double click callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddDoubleClickHandler(styler_item: MultiSelectList, doubleclickevent: MultiSelectList.DoubleClick, is_dialog_launching_event: bool) -> None:
        """
        Registers double click callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ##  Appends one or more entries to be inserted into the list 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## An array of entry names to be inserted into the list. This field is used only when more than one entry are to be inserted into the list.
    def Append(styler_item: MultiSelectList, multi_entries: List[str]) -> None:
        """
         Appends one or more entries to be inserted into the list 
        """
        pass
    
    ##  Deletes sub item 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Zero-based index of a list entry to be deleted 
    def DeleteSubitem(styler_item: MultiSelectList, subItemIndex: int) -> None:
        """
         Deletes sub item 
        """
        pass
    
    ## Requests a list entry to be deselected.
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Index of the list entry to be deselected.
    def Deselect(styler_item: MultiSelectList, subItemIndex: int) -> None:
        """
        Requests a list entry to be deselected.
            
        """
        pass
    
    ##  Indicates that this dialog item is receiving keyboard focus.
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Focus(styler_item: MultiSelectList) -> None:
        """
         Indicates that this dialog item is receiving keyboard focus.
            
        """
        pass
    
    ## Gets the indices of all selected list entries. 
    ##  @return indices (List[int]):  An array of integers for item indices of selected items .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetAllIndicesSelected(styler_item: MultiSelectList) -> List[int]:
        """
        Gets the indices of all selected list entries. 
         @return indices (List[int]):  An array of integers for item indices of selected items .
        """
        pass
    
    ## Gets the names of all selected list entries. 
    ##  @return names (List[str]):  An array of character strings of selected items.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetAllNameSelected(styler_item: MultiSelectList) -> List[str]:
        """
        Gets the names of all selected list entries. 
         @return names (List[str]):  An array of character strings of selected items.
        """
        pass
    
    ##  Gets an array of character strings for item names that are used as selectable choices for this 
    ##     dialog item.
    ##  @return item_val (List[str]):  An array of character strings for item names.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetListItems(styler_item: MultiSelectList) -> List[str]:
        """
         Gets an array of character strings for item names that are used as selectable choices for this 
            dialog item.
         @return item_val (List[str]):  An array of character strings for item names.
        """
        pass
    
    ##  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Sub item index 
    def InsertSubitems(styler_item: MultiSelectList, subitem_index: int, multi_entries: List[str]) -> None:
        """
         
        """
        pass
    
    ## Specifies all list entry to be selected.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def SetAllSelected(styler_item: MultiSelectList) -> None:
        """
        Specifies all list entry to be selected.
        """
        pass
    
    ## Specifies an array of character strings for item names that are used as selectable choices for this 
    ##     dialog item.
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## array of character strings for item names
    def SetListItems(styler_item: MultiSelectList, item_val: List[str]) -> None:
        """
        Specifies an array of character strings for item names that are used as selectable choices for this 
            dialog item.
            
        """
        pass
    
    ## Specifies particular list items to be selected.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  An index of particular list items to be selected 
    def SetSelected(styler_item: MultiSelectList, subIndex: int) -> None:
        """
        Specifies particular list items to be selected.
        """
        pass
    
    ##  Requests a list entry to be scrolled up to the first line in the list 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Zero-based index of a list entry to be scrolled up 
    ##                                 to the first line of the list.
    def ShowSubItem(styler_item: MultiSelectList, subItemIndex: int) -> None:
        """
         Requests a list entry to be scrolled up to the first line in the list 
        """
        pass
    
##  Represents a MultiTextBox for UI Styler. 
## 
##   <br>  Created in NX5.0.0  <br> 

class MultiTextBox(StylerItem): 
    """ Represents a MultiTextBox for UI Styler. """


    ## Getter for property: (bool) Sensitivity
    ##  the sensitivity of the dialog item.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Sensitivity(self) -> bool:
        """
        Getter for property: (bool) Sensitivity
         the sensitivity of the dialog item.  
             
         
        """
        pass
    
    ## Setter for property: (bool) Sensitivity

    ##  the sensitivity of the dialog item.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
         the sensitivity of the dialog item.  
             
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##   the visibility of the dialog item   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
          the visibility of the dialog item   
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##   the visibility of the dialog item   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
          the visibility of the dialog item   
            
         
        """
        pass
    
    ## Specifies the text for this dialog item. It can be programmatically get by APIs. 
    ##  @return item_val (List[str]):  to get array of strings.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetItemValues(styler_item: MultiTextBox) -> List[str]:
        """
        Specifies the text for this dialog item. It can be programmatically get by APIs. 
         @return item_val (List[str]):  to get array of strings.
        """
        pass
    
    ## Indicates that this dialog item is receiving keyboard focus.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def SetFocus(styler_item: MultiTextBox) -> None:
        """
        Indicates that this dialog item is receiving keyboard focus.
        """
        pass
    
    ## Specifies the text for this dialog item. It can be programmatically set by APIs supported in 
    ##     different laguages,or interactively entered by the user. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## array of strings to set the values in multi 
    ##                                 select List
    def SetItemValues(styler_item: MultiTextBox, values: List[str]) -> None:
        """
        Specifies the text for this dialog item. It can be programmatically set by APIs supported in 
            different laguages,or interactively entered by the user. 
        """
        pass
    
    ## Specifies descriptive text to display for the dialog item. It should describe the dialog item's 
    ##     intended use.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## new label string 
    def SetLabel(styler_item: MultiTextBox, str_label: str) -> None:
        """
        Specifies descriptive text to display for the dialog item. It should describe the dialog item's 
            intended use.
        """
        pass
    
##  Represents a OptionMenu for UI Styler. 
## 
##   <br>  Created in NX5.0.0  <br> 

class OptionMenu(StylerItem): 
    """ Represents a OptionMenu for UI Styler. """


    ## Getter for property: (int) ItemValue
    ##   the item value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def ItemValue(self) -> int:
        """
        Getter for property: (int) ItemValue
          the item value   
            
         
        """
        pass
    
    ## Setter for property: (int) ItemValue

    ##   the item value   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ItemValue.setter
    def ItemValue(self, item_val: int):
        """
        Setter for property: (int) ItemValue
          the item value   
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##   the visibility   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
          the visibility   
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##   the visibility   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
          the visibility   
            
         
        """
        pass
    
    ##  Called when a dialog user selects an option from the menu.  
    ## A callback definition with the following input arguments: 
    ##  - @link StylerEvent NXOpen.UIStyler.StylerEvent@endlink
    ##  and no return type
    Activate = Callable[[StylerEvent], None]
    
    
    ## Registers activate callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Callback for activate event 
    def AddActivateHandler(styler_item: OptionMenu, activateevent: OptionMenu.Activate, is_dialog_launching_event: bool) -> None:
        """
        Registers activate callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ##  Returns an array of bitmaps 
    ##  @return bitmaps (List[str]):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBitmap(styler_item: OptionMenu) -> List[str]:
        """
         Returns an array of bitmaps 
         @return bitmaps (List[str]):  .
        """
        pass
    
    ##  Returns an array if items 
    ##  @return list_entries (List[str]): .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetItems(styler_item: OptionMenu) -> List[str]:
        """
         Returns an array if items 
         @return list_entries (List[str]): .
        """
        pass
    
    ##  Gets the sensitivity 
    ##  @return type (bool):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSensitivity(styler_item: OptionMenu) -> bool:
        """
         Gets the sensitivity 
         @return type (bool):  .
        """
        pass
    
    ##  Set an array of bitmap filenames 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  An array of one or more bitmap filenames. 
    ##         If all bitmaps for the option menu reside in the same file, specify an array of just one entry, 
    ##         which contains the bitmap filename for this attribute. All existing choices for the option menu 
    ##         remains intact when this attribute is set. Only the bitmaps are changed. Note that the number of 
    ##         bitmaps must match the number of existing choices. 
    def SetBitmap(styler_item: OptionMenu, bitmaps: List[str]) -> None:
        """
         Set an array of bitmap filenames 
        """
        pass
    
    ##  Set an array of items 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  An array of new choices to be used for the 
    ##         dialog item. Note that this removes all existing choices (both text and bitmaps) 
    def SetItems(styler_item: OptionMenu, str_list_array: List[str]) -> None:
        """
         Set an array of items 
        """
        pass
    
    ##  Sets label 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Text to be set for the descriptive label. 
    def SetLabel(styler_item: OptionMenu, str_label: str) -> None:
        """
         Sets label 
        """
        pass
    
    ##  Sets the sensitivity 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  If the entire dialog item should change to the new Sensitivity state, 
    ##         set this field to UF_STYLER_NO_SUB_INDEX. If only one subitem should change to the new sensitivity state,
    ##         set this field to its zero-based index. 
    def SetSensitivity(styler_item: OptionMenu, subitem_index: int, type: bool) -> None:
        """
         Sets the sensitivity 
        """
        pass
    
##  Represents a OptionToggle for UI Styler 
## 
##   <br>  Created in NX5.0.0  <br> 

class OptionToggle(StylerItem): 
    """ Represents a OptionToggle for UI Styler """


    ## Getter for property: (bool) Visibility
    ##   the visibility   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
          the visibility   
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##   the visibility   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
          the visibility   
            
         
        """
        pass
    
    ##  Called when a dialog user selects an option from the menu  
    ## A callback definition with the following input arguments: 
    ##  - @link StylerEvent NXOpen.UIStyler.StylerEvent@endlink
    ##  and no return type
    Activate = Callable[[StylerEvent], None]
    
    
    ## Registers activate callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Callback for activate event 
    def AddActivateHandler(styler_item: OptionToggle, activateevent: OptionToggle.Activate, is_dialog_launching_event: bool) -> None:
        """
        Registers activate callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ## Called when a dialog user clicks on the button or presses the spacebar when the button has keyboard focus. 
    ##     Do not terminate the dialog with a value-changed callback. The dialog should always return UF_UI_CB_CONTINUE_DIALOG. 
    ## A callback definition with the following input arguments: 
    ##  - @link StylerEvent NXOpen.UIStyler.StylerEvent@endlink
    ##  and no return type
    ValueChanged = Callable[[StylerEvent], None]
    
    
    ## Registers value change callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Callback for value changed event 
    def AddValueChangedHandler(styler_item: OptionToggle, valuechangedevent: OptionToggle.ValueChanged, is_dialog_launching_event: bool) -> None:
        """
        Registers value change callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ##  Returns item value 
    ##  @return A tuple consisting of (item_val, set_check). 
    ##  - item_val is: int. Item value .
    ##  - set_check is: bool. .

    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetItemValue(styler_item: OptionToggle) -> Tuple[int, bool]:
        """
         Returns item value 
         @return A tuple consisting of (item_val, set_check). 
         - item_val is: int. Item value .
         - set_check is: bool. .

        """
        pass
    
    ##  Returns the items 
    ##  @return list_entries (List[str]):  An array of items .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetItems(styler_item: OptionToggle) -> List[str]:
        """
         Returns the items 
         @return list_entries (List[str]):  An array of items .
        """
        pass
    
    ##  Returns the sesitivity 
    ##  @return type (bool):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSensitivity(styler_item: OptionToggle) -> bool:
        """
         Returns the sesitivity 
         @return type (bool):  .
        """
        pass
    
    ##  Set bitmaps 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  An array of one or more bitmap filenames. 
    ##         If all bitmaps for the option menu reside in the same file, specify an array of just one entry, 
    ##         which contains the bitmap filename for this attribute. All existing choices for the option menu 
    ##         remain intact when this attribute is set. Only the bitmaps are changed. Note that the number of 
    ##         bitmaps must match the number of existing choices. 
    def SetBitmaps(styler_item: OptionToggle, bitmaps: List[str]) -> None:
        """
         Set bitmaps 
        """
        pass
    
    ##  Sets default action 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def SetDefaultAction(styler_item: OptionToggle) -> None:
        """
         Sets default action 
        """
        pass
    
    ##  Sets item value 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Zero-based index indicating the choice to be selected. 
    ##         It must be in the range of existing choices.
    def SetItemValue(styler_item: OptionToggle, subitem_index: int, set_check: bool) -> None:
        """
         Sets item value 
        """
        pass
    
    ##  Sets items in the array 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  An array of new choices to be used for the dialog item. 
    ##         Note that this removes all existing choices (both text and bitmaps). 
    def SetItems(styler_item: OptionToggle, str_list_array: List[str]) -> None:
        """
         Sets items in the array 
        """
        pass
    
    ##  Sets label 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Text to be set for the tool tip. 
    def SetLabel(styler_item: OptionToggle, str_label: str) -> None:
        """
         Sets label 
        """
        pass
    
    ##  Set the sesitivity 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  If the entire dialog item should change to the new Sensitivity state, 
    ##         set this field to UF_STYLER_NO_SUB_INDEX. If only one sub-item should change to the new sensitivity 
    ##         state, set this field to its zero-based index. 
    def SetSensitivity(styler_item: OptionToggle, subitem_index: int, type: bool) -> None:
        """
         Set the sesitivity 
        """
        pass
    
import NXOpen
##  Represents a PageSwitchData for UI Styler 
## 
##   <br>  Created in NX5.0.0  <br> 

class PageSwitchData(NXOpen.TransientObject): 
    """ Represents a PageSwitchData for UI Styler """


    ## Getter for property: (int) ActivatedPage
    ##   the activated page   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def ActivatedPage(self) -> int:
        """
        Getter for property: (int) ActivatedPage
          the activated page   
            
         
        """
        pass
    
    ## Getter for property: (int) DeactivatedPage
    ##   the deactivated page   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def DeactivatedPage(self) -> int:
        """
        Getter for property: (int) DeactivatedPage
          the deactivated page   
            
         
        """
        pass
    
    ##  Free resources associated with the instance. After this method
    ##     is called, it is illegal to use the object.  In .NET or Java, this 
    ##     method is automatically called when the object is deleted by the 
    ##     garbage collector. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(page_switch_data: PageSwitchData) -> None:
        """
         Free resources associated with the instance. After this method
            is called, it is illegal to use the object.  In .NET or Java, this 
            method is automatically called when the object is deleted by the 
            garbage collector. 
        """
        pass
    
##  Represents a PropertyPage for UI Styler 
## 
##   <br>  Created in NX5.0.0  <br> 

class PropertyPage(StylerItem): 
    """ Represents a PropertyPage for UI Styler """


    ## Getter for property: (bool) Sensitivity
    ##   the sensitivity of property page.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Sensitivity(self) -> bool:
        """
        Getter for property: (bool) Sensitivity
          the sensitivity of property page.  
             
         
        """
        pass
    
    ## Setter for property: (bool) Sensitivity

    ##   the sensitivity of property page.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
          the sensitivity of property page.  
             
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##  the visibility of the dialog item.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         the visibility of the dialog item.  
             
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##  the visibility of the dialog item.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         the visibility of the dialog item.  
             
         
        """
        pass
    
    ##  Sets focus 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def SetFocus(styler_item: PropertyPage) -> None:
        """
         Sets focus 
        """
        pass
    
    ## Specifies descriptive text to display for the dialog item. It should describe the dialog item's intended use. 
    ##     If you specify a bitmap for this dialog item, it uses this text as tooltip text. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## new label
    def SetLabel(styler_item: PropertyPage, str_label: str) -> None:
        """
        Specifies descriptive text to display for the dialog item. It should describe the dialog item's intended use. 
            If you specify a bitmap for this dialog item, it uses this text as tooltip text. 
        """
        pass
    
##  Represents a PushButton for UI Styler 
## 
##   <br>  Created in NX5.0.0  <br> 

class PushButton(StylerItem): 
    """ Represents a PushButton for UI Styler """


    ## Getter for property: (bool) Sensitivity
    ##   the senstivity of dialog.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Sensitivity(self) -> bool:
        """
        Getter for property: (bool) Sensitivity
          the senstivity of dialog.  
            
         
        """
        pass
    
    ## Setter for property: (bool) Sensitivity

    ##   the senstivity of dialog.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
          the senstivity of dialog.  
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##   the visibility of dialog.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
          the visibility of dialog.  
              
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##   the visibility of dialog.  
    ##       
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
          the visibility of dialog.  
              
         
        """
        pass
    
    ## Called when a dialog user clicks on the push button or presses the spacebar when the push button has 
    ##     keyboard focus. 
    ## A callback definition with the following input arguments: 
    ##  - @link StylerEvent NXOpen.UIStyler.StylerEvent@endlink
    ##  and no return type
    Activate = Callable[[StylerEvent], None]
    
    
    ## Registers activate callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddActivateHandler(styler_item: PushButton, activateevent: PushButton.Activate, is_dialog_launching_event: bool) -> None:
        """
        Registers activate callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ## Specifies a filename that contains a bitmap definition. The filename must contain a UBM, XPM, or BMP 
    ##     extension. When you use this field, the system displays a bitmap for this dialog item instead of a text 
    ##     label. When a bitmap is present, the system uses the text label as a popup hint when a user places the 
    ##     mouse cursor over the bitmap.  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## the bitmap extension 
    def SetBitmap(styler_item: PushButton, bitmap: str) -> None:
        """
        Specifies a filename that contains a bitmap definition. The filename must contain a UBM, XPM, or BMP 
            extension. When you use this field, the system displays a bitmap for this dialog item instead of a text 
            label. When a bitmap is present, the system uses the text label as a popup hint when a user places the 
            mouse cursor over the bitmap.  
        """
        pass
    
    ##  Sets default action 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def SetDefaultAction(styler_item: PushButton) -> None:
        """
         Sets default action 
        """
        pass
    
    ## Indicates that this dialog item is receiving keyboard focus. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def SetFocus(styler_item: PushButton) -> None:
        """
        Indicates that this dialog item is receiving keyboard focus. 
        """
        pass
    
    ## Specifies descriptive text to display for the dialog item. It should describe the dialog item's intended 
    ##     use. If you specify a bitmap for this dialog item, it uses this text as tooltip text.  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## the label string 
    def SetLabel(styler_item: PushButton, str_label: str) -> None:
        """
        Specifies descriptive text to display for the dialog item. It should describe the dialog item's intended 
            use. If you specify a bitmap for this dialog item, it uses this text as tooltip text.  
        """
        pass
    
##  Represents a RadioBox for UI Styler 
## 
##   <br>  Created in NX5.0.0  <br> 

class RadioBox(StylerItem): 
    """ Represents a RadioBox for UI Styler """


    ## Getter for property: (int) ItemValue
    ##   the item value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def ItemValue(self) -> int:
        """
        Getter for property: (int) ItemValue
          the item value   
            
         
        """
        pass
    
    ## Setter for property: (int) ItemValue

    ##   the item value   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ItemValue.setter
    def ItemValue(self, item_val: int):
        """
        Setter for property: (int) ItemValue
          the item value   
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##   the visibility   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
          the visibility   
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##   the visibility   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
          the visibility   
            
         
        """
        pass
    
    ## Called when a dialog user click on a button in the radio box.
    ##     Do not terminate the dialog with a value-changed callback. 
    ##     The dialog should always return UF_UI_CB_CONTINUE_DIALOG.  
    ## A callback definition with the following input arguments: 
    ##  - @link StylerEvent NXOpen.UIStyler.StylerEvent@endlink
    ##  and no return type
    ValueChanged = Callable[[StylerEvent], None]
    
    
    ## Registers value change callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Callback for value changed event 
    def AddValueChangedHandler(styler_item: RadioBox, valuechangedevent: RadioBox.ValueChanged, is_dialog_launching_event: bool) -> None:
        """
        Registers value change callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ##  Gets the sensitivity 
    ##  @return type (bool):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSensitivity(styler_item: RadioBox) -> bool:
        """
         Gets the sensitivity 
         @return type (bool):  .
        """
        pass
    
    ##  Set default action 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def SetDefaultAction(styler_item: RadioBox) -> None:
        """
         Set default action 
        """
        pass
    
    ##  Sets label 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Text to be set for the descriptive label 
    def SetLabel(styler_item: RadioBox, str_label: str) -> None:
        """
         Sets label 
        """
        pass
    
    ##  Sets the sensitivity 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetSensitivity(styler_item: RadioBox, subitem_index: int, type: bool) -> None:
        """
         Sets the sensitivity 
        """
        pass
    
##  Represents a Real for UI Styler 
## 
##   <br>  Created in NX5.0.0  <br> 

class RealItem(StylerItem): 
    """ Represents a Real for UI Styler """


    ## Getter for property: (float) ItemValue
    ##   the item value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def ItemValue(self) -> float:
        """
        Getter for property: (float) ItemValue
          the item value   
            
         
        """
        pass
    
    ## Setter for property: (float) ItemValue

    ##   the item value   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ItemValue.setter
    def ItemValue(self, item_val: float):
        """
        Setter for property: (float) ItemValue
          the item value   
            
         
        """
        pass
    
    ## Getter for property: (bool) Sensitivity
    ##   the sensitivity   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Sensitivity(self) -> bool:
        """
        Getter for property: (bool) Sensitivity
          the sensitivity   
            
         
        """
        pass
    
    ## Setter for property: (bool) Sensitivity

    ##   the sensitivity   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
          the sensitivity   
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##   the visibility   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
          the visibility   
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##   the visibility   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
          the visibility   
            
         
        """
        pass
    
    ##  Called when a dialog user enters a valid real value and presses Return.  
    ## A callback definition with the following input arguments: 
    ##  - @link StylerEvent NXOpen.UIStyler.StylerEvent@endlink
    ##  and no return type
    Activate = Callable[[StylerEvent], None]
    
    
    ## Registers activate callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Callback for activate event 
    def AddActivateHandler(styler_item: RealItem, activateevent: RealItem.Activate, is_dialog_launching_event: bool) -> None:
        """
        Registers activate callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ##  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Filename with .ubm, .xpm, or .bmp extension that contains a bitmap definition 
    def SetBitmap(styler_item: RealItem, str_bitmap: str) -> None:
        """
         
        """
        pass
    
    ##  Sets focus 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def SetFocus(styler_item: RealItem) -> None:
        """
         Sets focus 
        """
        pass
    
    ##  Set the label 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Text label to display on the left side of the text field. 
    def SetLabel(styler_item: RealItem, str_label: str) -> None:
        """
         Set the label 
        """
        pass
    
##  Represents a RealScale for UI Styler 
## 
##   <br>  Created in NX5.0.0  <br> 

class RealScale(StylerItem): 
    """ Represents a RealScale for UI Styler """


    ## Getter for property: (float) ItemValue
    ##   the item value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def ItemValue(self) -> float:
        """
        Getter for property: (float) ItemValue
          the item value   
            
         
        """
        pass
    
    ## Setter for property: (float) ItemValue

    ##   the item value   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ItemValue.setter
    def ItemValue(self, item_val: float):
        """
        Setter for property: (float) ItemValue
          the item value   
            
         
        """
        pass
    
    ## Getter for property: (bool) Sensitivity
    ##   the sensitivity   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Sensitivity(self) -> bool:
        """
        Getter for property: (bool) Sensitivity
          the sensitivity   
            
         
        """
        pass
    
    ## Setter for property: (bool) Sensitivity

    ##   the sensitivity   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
          the sensitivity   
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##   the visibility   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
          the visibility   
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##   the visibility   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
          the visibility   
            
         
        """
        pass
    
    ## Called when a dialog user moves the slider to a new position. 
    ##     Do not terminate the dialog with a value-changed callback. 
    ##     The dialog should always return UF_UI_CB_CONTINUE_DIALOG. 
    ## A callback definition with the following input arguments: 
    ##  - @link StylerEvent NXOpen.UIStyler.StylerEvent@endlink
    ##  and no return type
    Drag = Callable[[StylerEvent], None]
    
    
    ## Registers dtag callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Callback for add drag event 
    def AddDragHandler(styler_item: RealScale, dragevent: RealScale.Drag, is_dialog_launching_event: bool) -> None:
        """
        Registers dtag callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ##  
    ## A callback definition with the following input arguments: 
    ##  - @link StylerEvent NXOpen.UIStyler.StylerEvent@endlink
    ##  and no return type
    ValueChanged = Callable[[StylerEvent], None]
    
    
    ## Called when a dialog user moves the slider up and down the scale. 
    ##     For example, if a user moves the slider from 0.0 to 10.0, 
    ##     the dialog calls the drag callback 100 times, one for each value that the slider moves across. 
    ##     Do not terminate the dialog with a drag callback. The dialog should always return UF_UI_CB_CONTINUE_DIALOG.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Callback for value changed event 
    def AddValueChangedHandler(styler_item: RealScale, valuechangedevent: RealScale.ValueChanged, is_dialog_launching_event: bool) -> None:
        """
        Called when a dialog user moves the slider up and down the scale. 
            For example, if a user moves the slider from 0.0 to 10.0, 
            the dialog calls the drag callback 100 times, one for each value that the slider moves across. 
            Do not terminate the dialog with a drag callback. The dialog should always return UF_UI_CB_CONTINUE_DIALOG.
        """
        pass
    
    ##  Sets decimal precision 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  The number significant digits 
    def SetDecimalPrecision(styler_item: RealScale, digits: int) -> None:
        """
         Sets decimal precision 
        """
        pass
    
    ##  Sets labels 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  String minimum label 
    def SetLabels(styler_item: RealScale, minimum_label: str, maximum_label: str) -> None:
        """
         Sets labels 
        """
        pass
    
    ##  Sets limits 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Real minimum value 
    def SetLimits(styler_item: RealScale, minimum_value: float, maximum_value: float) -> None:
        """
         Sets limits 
        """
        pass
    
##  Represents a RowColumn for UI Styler 
## 
##   <br>  Created in NX5.0.0  <br> 

class RowColumn(StylerItem): 
    """ Represents a RowColumn for UI Styler """


    ## Getter for property: (bool) Sensitivity
    ##   the sensitivity   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Sensitivity(self) -> bool:
        """
        Getter for property: (bool) Sensitivity
          the sensitivity   
            
         
        """
        pass
    
    ## Setter for property: (bool) Sensitivity

    ##   the sensitivity   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
          the sensitivity   
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##   the visibility   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
          the visibility   
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##   the visibility   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
          the visibility   
            
         
        """
        pass
    
##  Represents a ScrolledWindow for UI Styler 
## 
##   <br>  Created in NX5.0.0  <br> 

class ScrolledWindow(StylerItem): 
    """ Represents a ScrolledWindow for UI Styler """


    ## Getter for property: (bool) Sensitivity
    ##     
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Sensitivity(self) -> bool:
        """
        Getter for property: (bool) Sensitivity
            
            
         
        """
        pass
    
    ## Setter for property: (bool) Sensitivity

    ##     
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
            
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##     
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
            
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##     
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
            
            
         
        """
        pass
    
##  Represents a SelectionBox for UI Styler 
## 
##   <br>  Created in NX5.0.0  <br> 

class SelectionBox(StylerItem): 
    """ Represents a SelectionBox for UI Styler """


    ## Getter for property: (bool) Sensitivity
    ##   the sensitivity of the selection box  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Sensitivity(self) -> bool:
        """
        Getter for property: (bool) Sensitivity
          the sensitivity of the selection box  
            
         
        """
        pass
    
    ## Setter for property: (bool) Sensitivity

    ##   the sensitivity of the selection box  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
          the sensitivity of the selection box  
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##   the visibility of the selection box  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
          the visibility of the selection box  
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##   the visibility of the selection box  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
          the visibility of the selection box  
            
         
        """
        pass
    
    ## Called when a dialog user selects a list entry with a single mouse click, presses the spacebar on a selected list entry, or presses Return when the cursor is in the text field.
    ## A callback definition with the following input arguments: 
    ##  - @link StylerEvent NXOpen.UIStyler.StylerEvent@endlink
    ##  and no return type
    Activate = Callable[[StylerEvent], None]
    
    
    ## Registers activate callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Activate event 
    def AddActivateHandler(styler_item: SelectionBox, activateevent: SelectionBox.Activate, is_dialog_launching_event: bool) -> None:
        """
        Registers activate callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ## Called when a dialog user double-clicks on an option in the selection box or presses Return when an item is already selected. 
    ## A callback definition with the following input arguments: 
    ##  - @link StylerEvent NXOpen.UIStyler.StylerEvent@endlink
    ##  and no return type
    DoubleClick = Callable[[StylerEvent], None]
    
    
    ## Registers double click callback. This method should be called before calling @link UIStyler::Dialog::Show  UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Double click event 
    def AddDoubleClickHandler(styler_item: SelectionBox, doubleclickevent: SelectionBox.DoubleClick, is_dialog_launching_event: bool) -> None:
        """
        Registers double click callback. This method should be called before calling @link UIStyler::Dialog::Show  UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ##  Appends one or more entries to be inserted into the list 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## An array of entry names to be inserted into the list. This field is used only when more than one entry are to be inserted into the list.
    def Append(styler_item: SelectionBox, multi_entries: List[str]) -> None:
        """
         Appends one or more entries to be inserted into the list 
        """
        pass
    
    ##  Deletes sub item 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def DeleteSubItem(styler_item: SelectionBox, subItemIndex: int) -> None:
        """
         Deletes sub item 
        """
        pass
    
    ##  Requests a list entry to be deselected.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def DeselectSubItem(styler_item: SelectionBox, subItemIndex: int) -> None:
        """
         Requests a list entry to be deselected.
        """
        pass
    
    ##  Gets an array of character strings for item names that are used as selectable choices for this dialog item.
    ##  @return values (List[str]):  List of items .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetListItems(styler_item: SelectionBox) -> List[str]:
        """
         Gets an array of character strings for item names that are used as selectable choices for this dialog item.
         @return values (List[str]):  List of items .
        """
        pass
    
    ##  Gets selected index value 
    ##  @return value (int):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectedIndexValue(styler_item: SelectionBox) -> int:
        """
         Gets selected index value 
         @return value (int):  .
        """
        pass
    
    ##  Gets selected string 
    ##  @return value (str):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectedString(styler_item: SelectionBox) -> str:
        """
         Gets selected string 
         @return value (str):  .
        """
        pass
    
    ##  Requests that one or more entries be inserted into the list. You can insert entries at the bottom of the list or at any position within the list.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Position index where the insertion should be made. If subitem_index equals UF_STYLER_NO_SUB_INDEX, then the new list entries are added to the bottom of the list. 
    def InsertSubItem(styler_item: SelectionBox, subitem_index: int, multi_entries: List[str]) -> None:
        """
         Requests that one or more entries be inserted into the list. You can insert entries at the bottom of the list or at any position within the list.
        """
        pass
    
    ##  Indicates that this dialog item is receiving keyboard focus. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def SetFocus(styler_item: SelectionBox) -> None:
        """
         Indicates that this dialog item is receiving keyboard focus. 
        """
        pass
    
    ##  Specifies the descriptive text string to display below the scrolled list and above the text field. It describes the dialog item's usage.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Label string 
    def SetLabel(styler_item: SelectionBox, str_label: str) -> None:
        """
         Specifies the descriptive text string to display below the scrolled list and above the text field. It describes the dialog item's usage.
        """
        pass
    
    ##  Specifies an array of character strings for item names that are used as selectable choices for this dialog item.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  List of items 
    def SetListItems(styler_item: SelectionBox, values: List[str]) -> None:
        """
         Specifies an array of character strings for item names that are used as selectable choices for this dialog item.
        """
        pass
    
    ##  Sets the value 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetValue(styler_item: SelectionBox, value: int) -> None:
        """
         Sets the value 
        """
        pass
    
    ##  Requests that a list entry be scrolled up to the first line in the list. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def ShowSubItem(styler_item: SelectionBox, subItemIndex: int) -> None:
        """
         Requests that a list entry be scrolled up to the first line in the list. 
        """
        pass
    
##  Represents a Separator for UI Styler 
## 
##   <br>  Created in NX5.0.0  <br> 

class Separator(StylerItem): 
    """ Represents a Separator for UI Styler """


    ## Getter for property: (bool) Visibility
    ##   the visibility of the separator  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
          the visibility of the separator  
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##   the visibility of the separator  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
          the visibility of the separator  
            
         
        """
        pass
    
##  Represents a SingleSelectList for UI Styler 
## 
##   <br>  Created in NX5.0.0  <br> 

class SingleSelectList(StylerItem): 
    """ Represents a SingleSelectList for UI Styler """


    ## Getter for property: (bool) Sensitivity
    ##   the sensitivity of the single select list  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Sensitivity(self) -> bool:
        """
        Getter for property: (bool) Sensitivity
          the sensitivity of the single select list  
            
         
        """
        pass
    
    ## Setter for property: (bool) Sensitivity

    ##   the sensitivity of the single select list  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
          the sensitivity of the single select list  
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##   the visibility of the single select list  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
          the visibility of the single select list  
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##   the visibility of the single select list  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
          the visibility of the single select list  
            
         
        """
        pass
    
    ##  Called when a dialog user selects an entry with a single mouse click 
    ##         or presses the spacebar on an already selected item. 
    ## A callback definition with the following input arguments: 
    ##  - @link StylerEvent NXOpen.UIStyler.StylerEvent@endlink
    ##  and no return type
    Activate = Callable[[StylerEvent], None]
    
    
    ## Registers activate callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddActivateHandler(styler_item: SingleSelectList, activateevent: SingleSelectList.Activate, is_dialog_launching_event: bool) -> None:
        """
        Registers activate callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ##  Called when a dialog user double-clicks on an option or presses Return when an item is already selected. 
    ## A callback definition with the following input arguments: 
    ##  - @link StylerEvent NXOpen.UIStyler.StylerEvent@endlink
    ##  and no return type
    DoubleClick = Callable[[StylerEvent], None]
    
    
    ## Registers double click callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddDoubleClickHandler(styler_item: SingleSelectList, doubleclickevent: SingleSelectList.DoubleClick, is_dialog_launching_event: bool) -> None:
        """
        Registers double click callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ##  Appends one or more entries to be inserted into the list 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## An array of entry names to be inserted into the list. This field is used only when more than one entry are to be inserted into the list.
    def Append(styler_item: SingleSelectList, multi_entries: List[str]) -> None:
        """
         Appends one or more entries to be inserted into the list 
        """
        pass
    
    ##  Requests a list entry to be deleted. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## Zero-based index of a list entry to be deleted. If subitem_index equals UF_STYLER_NO_SUB_INDEX, then all list entries are deleted. 
    def DeleteSubItem(styler_item: SingleSelectList, subItemIndex: int) -> None:
        """
         Requests a list entry to be deleted. 
        """
        pass
    
    ##  Requests a list entry to be deselected.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def DeselectSubItem(styler_item: SingleSelectList, subItemIndex: int) -> None:
        """
         Requests a list entry to be deselected.
        """
        pass
    
    ##  Gets an array of character strings that are used as entries in the list.
    ##  @return item_val (List[str]):  An array of string items .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetListItems(styler_item: SingleSelectList) -> List[str]:
        """
         Gets an array of character strings that are used as entries in the list.
         @return item_val (List[str]):  An array of string items .
        """
        pass
    
    ##  Gets selected index 
    ##  @return value (int):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectedIndexValue(styler_item: SingleSelectList) -> int:
        """
         Gets selected index 
         @return value (int):  .
        """
        pass
    
    ##  Gets selected string 
    ##  @return value (str):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectedString(styler_item: SingleSelectList) -> str:
        """
         Gets selected string 
         @return value (str):  .
        """
        pass
    
    ##  Returns whether or not an item has been selected 
    ##  @return selected (bool):  .
    ## 
    ##   <br>  Created in NX7.5.1  <br> 

    ## License requirements: None.
    @staticmethod
    def HasSelected(styler_item: SingleSelectList) -> bool:
        """
         Returns whether or not an item has been selected 
         @return selected (bool):  .
        """
        pass
    
    ##  Requests one or more entries to be inserted into the list. You can insert entries at the bottom of the list or at any position within the list. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Position index where the insertion should be made. If subitem_index equals UF_STYLER_NO_SUB_INDEX, then the new list entries are added to the bottom of the list.
    def InsertSubItem(styler_item: SingleSelectList, subitem_index: int, multi_entries: List[str]) -> None:
        """
         Requests one or more entries to be inserted into the list. You can insert entries at the bottom of the list or at any position within the list. 
        """
        pass
    
    ##  Indicates that this dialog item is receiving keyboard focus. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def SetFocus(styler_item: SingleSelectList) -> None:
        """
         Indicates that this dialog item is receiving keyboard focus. 
        """
        pass
    
    ##  Specifies an array of character strings that are used as entries in the list 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  An array of string items 
    def SetListItems(styler_item: SingleSelectList, item_val: List[str]) -> None:
        """
         Specifies an array of character strings that are used as entries in the list 
        """
        pass
    
    ##  Specifies particular list items to be selected 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Inndex of particular list items to be selected
    def SetSelected(styler_item: SingleSelectList, subIndex: int) -> None:
        """
         Specifies particular list items to be selected 
        """
        pass
    
    ## Requests that a list entry be scrolled up to the first line in the list 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Zero-based index of a list entry to be scrolled up to the first line of the list.
    def ShowSubItem(styler_item: SingleSelectList, subItemIndex: int) -> None:
        """
        Requests that a list entry be scrolled up to the first line in the list 
        """
        pass
    
##  Represents a StringItem for UI Styler. 
## 
##   <br>  Created in NX5.0.0  <br> 

class StringItem(StylerItem): 
    """ Represents a StringItem for UI Styler. """


    ## Getter for property: (str) ItemValue
    ##   the string value for this dialog item.  
    ##    It can be the initial value that is programmatically 
    ##     defined, or interactively entered by the user.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return str
    @property
    def ItemValue(self) -> str:
        """
        Getter for property: (str) ItemValue
          the string value for this dialog item.  
           It can be the initial value that is programmatically 
            defined, or interactively entered by the user.  
         
        """
        pass
    
    ## Setter for property: (str) ItemValue

    ##   the string value for this dialog item.  
    ##    It can be the initial value that is programmatically 
    ##     defined, or interactively entered by the user.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ItemValue.setter
    def ItemValue(self, item_val: str):
        """
        Setter for property: (str) ItemValue
          the string value for this dialog item.  
           It can be the initial value that is programmatically 
            defined, or interactively entered by the user.  
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##   the visibility of the dialog item   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
          the visibility of the dialog item   
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##   the visibility of the dialog item   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
          the visibility of the dialog item   
            
         
        """
        pass
    
    ## Called when a dialog user enters a character string and presses Return. 
    ## A callback definition with the following input arguments: 
    ##  - @link StylerEvent NXOpen.UIStyler.StylerEvent@endlink
    ##  and no return type
    Activate = Callable[[StylerEvent], None]
    
    
    ## Registers activate callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddActivateHandler(styler_item: StringItem, activateevent: StringItem.Activate, is_dialog_launching_event: bool) -> None:
        """
        Registers activate callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ##  To get senstivity of string control
    ##  @return type (bool):  TRUE if sensitive, FALSE if insensitive .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSensitivity(styler_item: StringItem) -> bool:
        """
         To get senstivity of string control
         @return type (bool):  TRUE if sensitive, FALSE if insensitive .
        """
        pass
    
    ## Specifies a filename that contains a bitmap definition. The filename must contain a UBM, XPM, or BMP 
    ##     extension. When you use this field, the system displays a bitmap for this dialog item instead of a text 
    ##     label. When a bitmap is present, the system uses the text label as tooltip text when a user places the 
    ##     mouse cursor over the bitmap. We recommend that you use a 16x16 bitmap for this dialog item.  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Filename with .ubm, .xpm, or .bmp extension that contains bitmap definition 
    def SetBitmap(styler_item: StringItem, str_bitmap: str) -> None:
        """
        Specifies a filename that contains a bitmap definition. The filename must contain a UBM, XPM, or BMP 
            extension. When you use this field, the system displays a bitmap for this dialog item instead of a text 
            label. When a bitmap is present, the system uses the text label as tooltip text when a user places the 
            mouse cursor over the bitmap. We recommend that you use a 16x16 bitmap for this dialog item.  
        """
        pass
    
    ##  Indicates that this dialog item is receiving keyboard focus 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def SetFocus(styler_item: StringItem) -> None:
        """
         Indicates that this dialog item is receiving keyboard focus 
        """
        pass
    
    ## Specifies descriptive text to display for the dialog item. 
    ##     It should describe the dialog item's intended use. If you specify a bitmap for this dialog item, 
    ##         it uses this text as tooltip text.
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  String label to display on the left side of the text field 
    def SetLabel(styler_item: StringItem, str_label: str) -> None:
        """
        Specifies descriptive text to display for the dialog item. 
            It should describe the dialog item's intended use. If you specify a bitmap for this dialog item, 
                it uses this text as tooltip text.
            
        """
        pass
    
    ## Specifies the sensitivity of the dialog item. When you set sensitivity to False, it grays out the 
    ##     dialog item. This indicates that the dialog item exists but is not active.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  TRUE if sensitive, FALSE if insensitive 
    def SetSensitivity(styler_item: StringItem, type: bool) -> None:
        """
        Specifies the sensitivity of the dialog item. When you set sensitivity to False, it grays out the 
            dialog item. This indicates that the dialog item exists but is not active.
        """
        pass
    
import NXOpen
##  Represents a StylerEvent 
## 
##   <br>  Created in NX5.0.0  <br> 

class StylerEvent(NXOpen.TransientObject): 
    """ Represents a StylerEvent """


    ##  Describes indicator value 
    ##  No value 
    class Indicator(Enum):
        """
        Members Include: <NoValue> <StringValue> <StringPointerValue> <IntegerValue> <IntegerPointerValue> <RealValue> <RealPointerValue> <SelectionValue> <OptionToggleValue>
        """
        NoValue: int
        StringValue: int
        StringPointerValue: int
        IntegerValue: int
        IntegerPointerValue: int
        RealValue: int
        RealPointerValue: int
        SelectionValue: int
        OptionToggleValue: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> StylerEvent.Indicator:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Describes event index 
    ##  No sub index 
    class Miscellaneous(Enum):
        """
        Members Include: <NoSubIndex> <OkIndex> <ApplyIndex> <BackIndex> <CancelIndex>
        """
        NoSubIndex: int
        OkIndex: int
        ApplyIndex: int
        BackIndex: int
        CancelIndex: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> StylerEvent.Miscellaneous:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Describes callback reason 
    ##  No reason 
    class Reason(Enum):
        """
        Members Include: <NoReason> <ActivateReason> <ValueChangedReason> <DragReason> <DoubleClickReason> <OkReason> <ApplyReason> <BackReason> <CancelReason> <ConstructReason> <DestructReason> <FileopReason> <SwitchReason> <FileOperationReason> <ExitFileOperationReason>
        """
        NoReason: int
        ActivateReason: int
        ValueChangedReason: int
        DragReason: int
        DoubleClickReason: int
        OkReason: int
        ApplyReason: int
        BackReason: int
        CancelReason: int
        ConstructReason: int
        DestructReason: int
        FileopReason: int
        SwitchReason: int
        FileOperationReason: int
        ExitFileOperationReason: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> StylerEvent.Reason:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Free resources associated with the instance. After this method
    ##     is called, it is illegal to use the object.  In .NET or Java, this 
    ##     method is automatically called when the object is deleted by the 
    ##     garbage collector. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(styler_event: StylerEvent) -> None:
        """
         Free resources associated with the instance. After this method
            is called, it is illegal to use the object.  In .NET or Java, this 
            method is automatically called when the object is deleted by the 
            garbage collector. 
        """
        pass
    
    ## Gets the reason for the event
    ##  @return reason (@link StylerEvent.Reason NXOpen.UIStyler.StylerEvent.Reason@endlink):  Reason .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetReason(styler_item: StylerEvent) -> StylerEvent.Reason:
        """
        Gets the reason for the event
         @return reason (@link StylerEvent.Reason NXOpen.UIStyler.StylerEvent.Reason@endlink):  Reason .
        """
        pass
    
    ##  Gets the dialog item
    ##  @return item (@link StylerItem NXOpen.UIStyler.StylerItem@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStylerItem(styler_item: StylerEvent) -> StylerItem:
        """
         Gets the dialog item
         @return item (@link StylerItem NXOpen.UIStyler.StylerItem@endlink):  .
        """
        pass
    
import NXOpen
##  Represents a Styler Item 
## 
##   <br>  Created in NX5.0.0  <br> 

class StylerItem(NXOpen.TransientObject): 
    """ Represents a Styler Item """


    ##  Describes kind of action to be taken from callbac. 
    ##  Invalid item 
    class ItemType(Enum):
        """
        Members Include: <InvalidType> <ActionButton> <Dialog> <RadioBox> <Real> <ScaleReal> <Bitmap> <RowColumn> <ButtonLayout> <ScrolledWindow> <ColorTool> <SelectionBox> <Separator> <SingleSelectionList> <String> <BeginGroup> <Integer> <ScaleInteger> <MultiList> <Label> <MultiLineText> <TabControl> <OptionMenu> <Toggle> <OptionToggle> <ToolPalette> <WideString> <PropertyPage> <CollapsibleGroup>
        """
        InvalidType: int
        ActionButton: int
        Dialog: int
        RadioBox: int
        Real: int
        ScaleReal: int
        Bitmap: int
        RowColumn: int
        ButtonLayout: int
        ScrolledWindow: int
        ColorTool: int
        SelectionBox: int
        Separator: int
        SingleSelectionList: int
        String: int
        BeginGroup: int
        Integer: int
        ScaleInteger: int
        MultiList: int
        Label: int
        MultiLineText: int
        TabControl: int
        OptionMenu: int
        Toggle: int
        OptionToggle: int
        ToolPalette: int
        WideString: int
        PropertyPage: int
        CollapsibleGroup: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> StylerItem.ItemType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Free resources associated with the instance. After this method
    ##     is called, it is illegal to use the object.  In .NET or Java, this 
    ##     method is automatically called when the object is deleted by the 
    ##     garbage collector. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(styler_item: StylerItem) -> None:
        """
         Free resources associated with the instance. After this method
            is called, it is illegal to use the object.  In .NET or Java, this 
            method is automatically called when the object is deleted by the 
            garbage collector. 
        """
        pass
    
    ##  Gets the dialog item type. User can write programs to query this attribute and determine the 
    ##     type of a dialog item in order to determine what further actions should be taken.
    ##  @return item_type (@link StylerItem.ItemType NXOpen.UIStyler.StylerItem.ItemType@endlink): .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetItemType(styler_item: StylerItem) -> StylerItem.ItemType:
        """
         Gets the dialog item type. User can write programs to query this attribute and determine the 
            type of a dialog item in order to determine what further actions should be taken.
         @return item_type (@link StylerItem.ItemType NXOpen.UIStyler.StylerItem.ItemType@endlink): .
        """
        pass
    
    ##  Returns initialized dialog item attachment information 
    ##  @return attachment (@link Attachment NXOpen.UIStyler.Attachment@endlink): attachment object.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def InitializeAttachment(styler_item: StylerItem) -> Attachment:
        """
         Returns initialized dialog item attachment information 
         @return attachment (@link Attachment NXOpen.UIStyler.Attachment@endlink): attachment object.
        """
        pass
    
    ##  Equates two styler items 
    ##  @return is_equal (bool): .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  styler item to compare
    def IsEqualTo(styler_item: StylerItem, item_to_compare: StylerItem) -> bool:
        """
         Equates two styler items 
         @return is_equal (bool): .
        """
        pass
    
    ## Specifies the updated dialog item attachment information 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## attachment object
    def SetAttachment(styler_item: StylerItem, attachment: Attachment) -> None:
        """
        Specifies the updated dialog item attachment information 
        """
        pass
    
import NXOpen
##  Represents a Uistyler for UI Styler  <br> To obtain an instance of this class, refer to @link NXOpen::UI  NXOpen::UI @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class Styler(NXOpen.Object): 
    """ Represents a Uistyler for UI Styler """


    ## Creates an NX (UIStyler generated) "bottom" dialog. The ".dlg" file can only be generated from the 
    ##     Open UIStyler. 
    ##  @return dialog (@link Dialog NXOpen.UIStyler.Dialog@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Dialog name 
    def CreateStylerDialog(dialog_name: str) -> Dialog:
        """
        Creates an NX (UIStyler generated) "bottom" dialog. The ".dlg" file can only be generated from the 
            Open UIStyler. 
         @return dialog (@link Dialog NXOpen.UIStyler.Dialog@endlink):  .
        """
        pass
    
##  Represents a Tab Control for UI Styler. 
## 
##   <br>  Created in NX5.0.0  <br> 

class TabControl(StylerItem): 
    """ Represents a Tab Control for UI Styler. """


    ## Getter for property: (@link PageSwitchData NXOpen.UIStyler.PageSwitchData@endlink) PageSwitchData
    ##   the page switch data  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return PageSwitchData
    @property
    def PageSwitchData(self) -> PageSwitchData:
        """
        Getter for property: (@link PageSwitchData NXOpen.UIStyler.PageSwitchData@endlink) PageSwitchData
          the page switch data  
            
         
        """
        pass
    
    ## Getter for property: (bool) Sensitivity
    ##   the sensitivity of the dialog item   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Sensitivity(self) -> bool:
        """
        Getter for property: (bool) Sensitivity
          the sensitivity of the dialog item   
            
         
        """
        pass
    
    ## Setter for property: (bool) Sensitivity

    ##   the sensitivity of the dialog item   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
          the sensitivity of the dialog item   
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##   the visibility of the dialog item  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
          the visibility of the dialog item  
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##   the visibility of the dialog item  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
          the visibility of the dialog item  
            
         
        """
        pass
    
    ## Called when a user switches tabs. 
    ## A callback definition with the following input arguments: 
    ##  - @link StylerEvent NXOpen.UIStyler.StylerEvent@endlink
    ##  and no return type
    SwitchHandler = Callable[[StylerEvent], None]
    
    
    ## Registers switch callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddSwitchHandler(styler_item: TabControl, switchevent: TabControl.SwitchHandler, is_dialog_launching_event: bool) -> None:
        """
        Registers switch callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ##  Sets focus 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def SetFocus(styler_item: TabControl) -> None:
        """
         Sets focus 
        """
        pass
    
##  Represents a Toggle for UI Styler. 
## 
##   <br>  Created in NX5.0.0  <br> 

class Toggle(StylerItem): 
    """ Represents a Toggle for UI Styler. """


    ## Getter for property: (bool) ItemValue
    ##   an item value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def ItemValue(self) -> bool:
        """
        Getter for property: (bool) ItemValue
          an item value   
            
         
        """
        pass
    
    ## Setter for property: (bool) ItemValue

    ##   an item value   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ItemValue.setter
    def ItemValue(self, item_val: bool):
        """
        Setter for property: (bool) ItemValue
          an item value   
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##   the visibility of the toggle  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
          the visibility of the toggle  
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##   the visibility of the toggle  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
          the visibility of the toggle  
            
         
        """
        pass
    
    ##  Called when a dialog user clicks on the button or presses the spacebar when the button has keyboard focus. 
    ##         Do not terminate the dialog with a value-changed callback. The dialog should always return UF_UI_CB_CONTINUE_DIALOG 
    ## A callback definition with the following input arguments: 
    ##  - @link StylerEvent NXOpen.UIStyler.StylerEvent@endlink
    ##  and no return type
    ValueChanged = Callable[[StylerEvent], None]
    
    
    ## Registers value change callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Value changed event 
    def AddValueChangedHandler(styler_item: Toggle, valuechangedevent: Toggle.ValueChanged, is_dialog_launching_event: bool) -> None:
        """
        Registers value change callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ##  Gets the sensitivity 
    ##  @return type (bool):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSensitivity(styler_item: Toggle) -> bool:
        """
         Gets the sensitivity 
         @return type (bool):  .
        """
        pass
    
    ##  Indicates that this dialog item should override the accelerator 
    ##     on the second mouse button, which normally accelerates to the OK button. 
    ##     When you set this attribute, a click on the second mouse button triggers 
    ##     this dialog item's ON/OFF state and calls the Value Changed callback 
    ##     instead of the action of the OK button.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def SetDefaultAction(styler_item: Toggle) -> None:
        """
         Indicates that this dialog item should override the accelerator 
            on the second mouse button, which normally accelerates to the OK button. 
            When you set this attribute, a click on the second mouse button triggers 
            this dialog item's ON/OFF state and calls the Value Changed callback 
            instead of the action of the OK button.
        """
        pass
    
    ##  Indicates that this dialog item is receiving keyboard focus. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def SetFocus(styler_item: Toggle) -> None:
        """
         Indicates that this dialog item is receiving keyboard focus. 
        """
        pass
    
    ##  Sets the label to display on the right side of the toggle button. 
    ##     If the toggle button displays a bitmap, then this text label is used as a popup hint instead
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetLabel(styler_item: Toggle, str_label: str) -> None:
        """
         Sets the label to display on the right side of the toggle button. 
            If the toggle button displays a bitmap, then this text label is used as a popup hint instead
        """
        pass
    
    ##  Sets the sensitivity of the toggle button 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetSensitivity(styler_item: Toggle, subitem_index: int, type: bool) -> None:
        """
         Sets the sensitivity of the toggle button 
        """
        pass
    
##  Represents a ToolPalette for UI Styler 
## 
##   <br>  Created in NX5.0.0  <br> 

class ToolPalette(StylerItem): 
    """ Represents a ToolPalette for UI Styler """


    ## Getter for property: (int) ItemValue
    ##   the currently selected choice for this dialog item.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def ItemValue(self) -> int:
        """
        Getter for property: (int) ItemValue
          the currently selected choice for this dialog item.  
            
         
        """
        pass
    
    ## Setter for property: (int) ItemValue

    ##   the currently selected choice for this dialog item.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ItemValue.setter
    def ItemValue(self, item_val: int):
        """
        Setter for property: (int) ItemValue
          the currently selected choice for this dialog item.  
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##   the visibility of the dialog item  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
          the visibility of the dialog item  
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##   the visibility of the dialog item  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
          the visibility of the dialog item  
            
         
        """
        pass
    
    ##  Called when a dialog user selects a button in the tool palette.
    ## A callback definition with the following input arguments: 
    ##  - @link StylerEvent NXOpen.UIStyler.StylerEvent@endlink
    ##  and no return type
    Activate = Callable[[StylerEvent], None]
    
    
    ## Registers activate callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddActivateHandler(styler_item: ToolPalette, activateevent: ToolPalette.Activate, is_dialog_launching_event: bool) -> None:
        """
        Registers activate callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ##  Gets the sensitivity of the dialog item
    ##  @return type (bool):  True if sensitivity is set otherwise False .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSensitivity(styler_item: ToolPalette) -> bool:
        """
         Gets the sensitivity of the dialog item
         @return type (bool):  True if sensitivity is set otherwise False .
        """
        pass
    
    ##  Indicates that this dialog item should override the accelerator 
    ##     on the second mouse button, which normally accelerates to the OK button. 
    ##     When you set this attribute, a click on the second mouse button triggers
    ##     this dialog item's Activate callback instead of the action of the OK button.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetDefault(styler_item: ToolPalette, dialog_id: int) -> None:
        """
         Indicates that this dialog item should override the accelerator 
            on the second mouse button, which normally accelerates to the OK button. 
            When you set this attribute, a click on the second mouse button triggers
            this dialog item's Activate callback instead of the action of the OK button.
        """
        pass
    
    ##  Specifies descriptive text to display for the dialog item. 
    ##     It should describe the dialog item's intended use. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  String label 
    def SetLabel(styler_item: ToolPalette, str_label: str) -> None:
        """
         Specifies descriptive text to display for the dialog item. 
            It should describe the dialog item's intended use. 
        """
        pass
    
    ##  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Sub item index 
    def SetSensitivity(styler_item: ToolPalette, subitem_index: int, type: bool) -> None:
        """
         
        """
        pass
    
##  Represents a WideString for UI Styler 
## 
##   <br>  Created in NX5.0.0  <br> 

class WideString(StylerItem): 
    """ Represents a WideString for UI Styler """


    ## Getter for property: (str) ItemValue
    ##   the string value for this dialog item.  
    ##   
    ##      It can be the initial value that is programmatically defined, or interactively entered by the user.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return str
    @property
    def ItemValue(self) -> str:
        """
        Getter for property: (str) ItemValue
          the string value for this dialog item.  
          
             It can be the initial value that is programmatically defined, or interactively entered by the user.   
         
        """
        pass
    
    ## Setter for property: (str) ItemValue

    ##   the string value for this dialog item.  
    ##   
    ##      It can be the initial value that is programmatically defined, or interactively entered by the user.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ItemValue.setter
    def ItemValue(self, item_val: str):
        """
        Setter for property: (str) ItemValue
          the string value for this dialog item.  
          
             It can be the initial value that is programmatically defined, or interactively entered by the user.   
         
        """
        pass
    
    ## Getter for property: (bool) Sensitivity
    ##   the sensitivity of the wide string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Sensitivity(self) -> bool:
        """
        Getter for property: (bool) Sensitivity
          the sensitivity of the wide string  
            
         
        """
        pass
    
    ## Setter for property: (bool) Sensitivity

    ##   the sensitivity of the wide string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
          the sensitivity of the wide string  
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##   the visibility of the wide string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
          the visibility of the wide string  
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##   the visibility of the wide string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
          the visibility of the wide string  
            
         
        """
        pass
    
    ##  Called when a dialog user enters a character string and presses Return.
    ## A callback definition with the following input arguments: 
    ##  - @link StylerEvent NXOpen.UIStyler.StylerEvent@endlink
    ##  and no return type
    Activate = Callable[[StylerEvent], None]
    
    
    ## Registers activate callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddActivateHandler(styler_item: WideString, activateevent: WideString.Activate, is_dialog_launching_event: bool) -> None:
        """
        Registers activate callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ##  Indicates that this dialog item is receiving keyboard focus.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def SetFocus(styler_item: WideString) -> None:
        """
         Indicates that this dialog item is receiving keyboard focus.
        """
        pass
    
    ##  Specifies descriptive text to display for the dialog item. 
    ##     It should describe the dialog item's intended use
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Label string 
    def SetLabel(styler_item: WideString, str_label: str) -> None:
        """
         Specifies descriptive text to display for the dialog item. 
            It should describe the dialog item's intended use
        """
        pass
    
## @package NXOpen.UIStyler
## Classes, Enums and Structs under NXOpen.UIStyler namespace

##  @link AttachmentAttachType NXOpen.UIStyler.AttachmentAttachType @endlink is an alias for @link Attachment.AttachType NXOpen.UIStyler.Attachment.AttachType@endlink
AttachmentAttachType = Attachment.AttachType


##  @link DialogItemDialogItemIndex NXOpen.UIStyler.DialogItemDialogItemIndex @endlink is an alias for @link DialogItem.DialogItemIndex NXOpen.UIStyler.DialogItem.DialogItemIndex@endlink
DialogItemDialogItemIndex = DialogItem.DialogItemIndex


##  @link DialogItemType NXOpen.UIStyler.DialogItemType @endlink is an alias for @link Dialog.ItemType NXOpen.UIStyler.Dialog.ItemType@endlink
DialogItemType = Dialog.ItemType


##  @link FileOperationDataFileOperationState NXOpen.UIStyler.FileOperationDataFileOperationState @endlink is an alias for @link FileOperationData.FileOperationState NXOpen.UIStyler.FileOperationData.FileOperationState@endlink
FileOperationDataFileOperationState = FileOperationData.FileOperationState


##  @link FileOperationDataFileOperationType NXOpen.UIStyler.FileOperationDataFileOperationType @endlink is an alias for @link FileOperationData.FileOperationType NXOpen.UIStyler.FileOperationData.FileOperationType@endlink
FileOperationDataFileOperationType = FileOperationData.FileOperationType


##  @link StylerEventIndicator NXOpen.UIStyler.StylerEventIndicator @endlink is an alias for @link StylerEvent.Indicator NXOpen.UIStyler.StylerEvent.Indicator@endlink
StylerEventIndicator = StylerEvent.Indicator


##  @link StylerEventMiscellaneous NXOpen.UIStyler.StylerEventMiscellaneous @endlink is an alias for @link StylerEvent.Miscellaneous NXOpen.UIStyler.StylerEvent.Miscellaneous@endlink
StylerEventMiscellaneous = StylerEvent.Miscellaneous


##  @link StylerEventReason NXOpen.UIStyler.StylerEventReason @endlink is an alias for @link StylerEvent.Reason NXOpen.UIStyler.StylerEvent.Reason@endlink
StylerEventReason = StylerEvent.Reason


##  @link StylerItemItemType NXOpen.UIStyler.StylerItemItemType @endlink is an alias for @link StylerItem.ItemType NXOpen.UIStyler.StylerItem.ItemType@endlink
StylerItemItemType = StylerItem.ItemType


