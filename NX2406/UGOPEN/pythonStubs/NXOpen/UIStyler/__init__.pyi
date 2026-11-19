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
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Dialog</term><description> 
    ##  Dialog type </description> </item><item><term> 
    ## Default</term><description> 
    ##  Default type  </description> </item><item><term> 
    ## NotSet</term><description> 
    ##  None type </description> </item><item><term> 
    ## NoChange</term><description> 
    ##  No change type </description> </item><item><term> 
    ## Item</term><description> 
    ##  Item type </description> </item></list>
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
    def Dispose(self) -> None:
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
    ## <param name="attach_type_left"> (@link Attachment.AttachType NXOpen.UIStyler.Attachment.AttachType@endlink)  </param>
    def SetAttachTypeLeft(self, attach_type_left: Attachment.AttachType) -> None:
        """
         Sets the attach type left
        """
        pass
    
    ##  Sets the attach type right
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="attach_type_right"> (@link Attachment.AttachType NXOpen.UIStyler.Attachment.AttachType@endlink)  </param>
    def SetAttachTypeRight(self, attach_type_right: Attachment.AttachType) -> None:
        """
         Sets the attach type right
        """
        pass
    
    ##  Sets the attach type top
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="attach_type_top"> (@link Attachment.AttachType NXOpen.UIStyler.Attachment.AttachType@endlink)  attach_type_top </param>
    def SetAttachTypeTop(self, attach_type_top: Attachment.AttachType) -> None:
        """
         Sets the attach type top
        """
        pass
    
    ##  Sets whether the dialog item is at the center
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="is_center"> (bool)  center</param>
    def SetCenter(self, is_center: bool) -> None:
        """
         Sets whether the dialog item is at the center
        """
        pass
    
    ##  Sets the left dialog item
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="left_item_identifire"> (str)  Left item identifier </param>
    def SetLeftDialogItem(self, left_item_identifire: str) -> None:
        """
         Sets the left dialog item
        """
        pass
    
    ##  Sets the left offset
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="offset_left"> (int)  </param>
    def SetLeftOffset(self, offset_left: int) -> None:
        """
         Sets the left offset
        """
        pass
    
    ##  Sets the right dialog item
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="right_item_identifire"> (str)  Right item identifier </param>
    def SetRightDialogItem(self, right_item_identifire: str) -> None:
        """
         Sets the right dialog item
        """
        pass
    
    ##  Sets the right offset
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="offset_right"> (int)  </param>
    def SetRightOffset(self, offset_right: int) -> None:
        """
         Sets the right offset
        """
        pass
    
    ##  Sets the top dialog item
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="top_item_identifire"> (str)  Top item identifier </param>
    def SetTopDialogItem(self, top_item_identifire: str) -> None:
        """
         Sets the top dialog item
        """
        pass
    
    ##  Sets the top offset
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="offset_top"> (int)  </param>
    def SetTopOffset(self, offset_top: int) -> None:
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
    ## 
    ## <param name="bitmap"> (str)  filename with .ubm, .xpm, or .bmp extension that contains bitmap definition </param>
    def SetBitmap(self, bitmap: str) -> None:
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
    ##  Returns the visibility   
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
         Returns the visibility   
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##  Returns the visibility   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility   
            
         
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
    ## 
    ## <param name="activateevent"> (@link ButtonLayout.Activate NXOpen.UIStyler.ButtonLayout.Activate@endlink)  Callback for activate event </param>
    ## <param name="is_dialog_launching_event"> (bool)  TRUE if dialog is going to launch, FALSE if not </param>
    def AddActivateHandler(self, activateevent: ButtonLayout.Activate, is_dialog_launching_event: bool) -> None:
        """
        Registers activate callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ##  Gets selected index 
    ##  @return value (int):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetSelectedIndexValue(self) -> int:
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
    def GetSensitivity(self) -> bool:
        """
         Gets the sensitivity 
         @return type (bool):  .
        """
        pass
    
    ##  Sets default action 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def SetDefaultAction(self) -> None:
        """
         Sets default action 
        """
        pass
    
    ##  Sets the sensitivity 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="subitem_index"> (int)  If the entire dialog item should change to the new sensitivity state, 
    ##         set this field to UF_STYLER_NO_SUB_INDEX. If only one subitem should change to the new sensitivity 
    ##         state, set this field to its zero-based index. </param>
    ## <param name="type"> (bool)  TRUE if sensitive, FALSE if insensitive </param>
    def SetSensitivity(self, subitem_index: int, type: bool) -> None:
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
    ##  Returnsthe collapse-state  
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
         Returnsthe collapse-state  
            
         
        """
        pass
    
    ## Setter for property: (bool) CollapseState

    ##  Returnsthe collapse-state  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.5  <br> 

    @CollapseState.setter
    def CollapseState(self, item_val: bool):
        """
        Setter for property: (bool) CollapseState
         Returnsthe collapse-state  
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##  Returnsthe visibility  
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
         Returnsthe visibility  
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##  Returnsthe visibility  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.5  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returnsthe visibility  
            
         
        """
        pass
    
    ## Sets label of collapsible group
    ## 
    ##   <br>  Created in NX6.0.5  <br> 

    ## License requirements: None.
    ## 
    ## <param name="str_label"> (str)  Text to be set as label </param>
    def SetLabel(self, str_label: str) -> None:
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
    ##  Returns the item value   
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
         Returns the item value   
            
         
        """
        pass
    
    ## Setter for property: (int) ItemValue

    ##  Returns the item value   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ItemValue.setter
    def ItemValue(self, item_val: int):
        """
        Setter for property: (int) ItemValue
         Returns the item value   
            
         
        """
        pass
    
    ## Getter for property: (bool) Sensitivity
    ##  Returns the sensitivity   
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
         Returns the sensitivity   
            
         
        """
        pass
    
    ## Setter for property: (bool) Sensitivity

    ##  Returns the sensitivity   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
         Returns the sensitivity   
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##  Returns the visibility   
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
         Returns the visibility   
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##  Returns the visibility   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility   
            
         
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
    ## 
    ## <param name="valuechangedevent"> (@link ColorTool.ValueChanged NXOpen.UIStyler.ColorTool.ValueChanged@endlink)  Callback for value changed event </param>
    ## <param name="is_dialog_launching_event"> (bool)  TRUE if dialog is going to launch, FALSE if not </param>
    def AddValueChangedHandler(self, valuechangedevent: ColorTool.ValueChanged, is_dialog_launching_event: bool) -> None:
        """
        Registers value change callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
##  Represents indexes 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## NoSubIndex</term><description> 
##  All sub items are selected.</description> </item></list>
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
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Ok</term><description> 
    ##  Ok index </description> </item><item><term> 
    ## Apply</term><description> 
    ##  Apply index </description> </item><item><term> 
    ## Back</term><description> 
    ##  Back index </description> </item><item><term> 
    ## Cancel</term><description> 
    ##  Cancel index </description> </item></list>
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
    ##  Returns the file operation data   
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
         Returns the file operation data   
            
         
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
    ## <param name="applyevent"> (@link DialogItem.Apply NXOpen.UIStyler.DialogItem.Apply@endlink)  </param>
    ## <param name="is_dialog_launching_event"> (bool)  </param>
    def AddApplyHandler(self, applyevent: DialogItem.Apply, is_dialog_launching_event: bool) -> None:
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
    ## <param name="backevent"> (@link DialogItem.Back NXOpen.UIStyler.DialogItem.Back@endlink)  </param>
    ## <param name="is_dialog_launching_event"> (bool)  </param>
    def AddBackHandler(self, backevent: DialogItem.Back, is_dialog_launching_event: bool) -> None:
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
    ## <param name="cancelevent"> (@link DialogItem.Cancel NXOpen.UIStyler.DialogItem.Cancel@endlink)  </param>
    ## <param name="is_dialog_launching_event"> (bool)  </param>
    def AddCancelHandler(self, cancelevent: DialogItem.Cancel, is_dialog_launching_event: bool) -> None:
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
    ## <param name="constructevent"> (@link DialogItem.Construct NXOpen.UIStyler.DialogItem.Construct@endlink)  </param>
    ## <param name="is_dialog_launching_event"> (bool)  </param>
    def AddConstructHandler(self, constructevent: DialogItem.Construct, is_dialog_launching_event: bool) -> None:
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
    ## <param name="destructevent"> (@link DialogItem.Destruct NXOpen.UIStyler.DialogItem.Destruct@endlink)  </param>
    ## <param name="is_dialog_launching_event"> (bool)  </param>
    def AddDestructHandler(self, destructevent: DialogItem.Destruct, is_dialog_launching_event: bool) -> None:
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
    ## <param name="fileoperationevent"> (@link DialogItem.FileOperation NXOpen.UIStyler.DialogItem.FileOperation@endlink)  </param>
    ## <param name="is_dialog_launching_event"> (bool)  </param>
    def AddFileOperationHandler(self, fileoperationevent: DialogItem.FileOperation, is_dialog_launching_event: bool) -> None:
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
    ## <param name="okayevent"> (@link DialogItem.Okay NXOpen.UIStyler.DialogItem.Okay@endlink)  </param>
    ## <param name="is_dialog_launching_event"> (bool)  </param>
    def AddOkayHandler(self, okayevent: DialogItem.Okay, is_dialog_launching_event: bool) -> None:
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
    ## <param name="switchevent"> (@link DialogItem.PageSwitch NXOpen.UIStyler.DialogItem.PageSwitch@endlink)  </param>
    ## <param name="is_dialog_launching_event"> (bool)  </param>
    def AddPageSwitchHandler(self, switchevent: DialogItem.PageSwitch, is_dialog_launching_event: bool) -> None:
        """
        Registers switch callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ##  Gets the selection handle for a given dialog item
    ##  @return select (@link NXOpen.SelectionHandle NXOpen.SelectionHandle@endlink): Selection handle .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetSelectionHandle(self) -> NXOpen.SelectionHandle:
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
    ## 
    ## <param name="sub_item_index"> (@link DialogItem.DialogItemIndex NXOpen.UIStyler.DialogItem.DialogItemIndex@endlink)  Sub item index </param>
    ## <param name="type"> (bool)  TRUE if sensitive, FALSE if insensitive </param>
    def SetNavigationSensitivity(self, sub_item_index: DialogItem.DialogItemIndex, type: bool) -> None:
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
    ## 
    ## <param name="type"> (bool) TRUE to allow dialog to resize; FALSE to freeze the dialog size</param>
    def SetResize(self, type: bool) -> None:
        """
        Specifies wether dialog is allowed to resize 
        """
        pass
    
    ## Specifies the sensitivity of the dialog. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="type"> (bool) TRUE if sensitive, FALSE if insensitive </param>
    def SetSensitivity(self, type: bool) -> None:
        """
        Specifies the sensitivity of the dialog. 
        """
        pass
    
    ## Specifies a string to display on the top border of the dialog 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="str_label"> (str)  </param>
    def SetTitle(self, str_label: str) -> None:
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
    ## <param name="width"> (int)  </param>
    def SetWidth(self, width: int) -> None:
        """
        Specifies the pixel width for the dialog. You can only set this attribute when the 
            Dialog Resize attribute is set to TRUE. You cannot enter a negative number. 
        """
        pass
    
##  Represents dialog response 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## PickResponse</term><description> 
##  User response was a selection of objects.</description> </item><item><term> 
## Ok</term><description> 
##  OK button was selected. </description> </item><item><term> 
## Cancel</term><description> 
##  Cancel button was selected. </description> </item><item><term> 
## Back</term><description> 
##  Back button was selected. </description> </item><item><term> 
## Apply</term><description> 
##  Apply button was selected. </description> </item><item><term> 
## Help</term><description> 
##  Help button was selected. </description> </item><item><term> 
## ObjectSelected</term><description> 
##  Object was selected. </description> </item><item><term> 
## ObjectSelectedByName</term><description> 
##  Object was selected by name. </description> </item><item><term> 
## CbTerminate</term><description> 
##  Callback routine has terminated. </description> </item></list>
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
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## ContinueDialog</term><description> 
##  Continue the dialog </description> </item><item><term> 
## ExitDialog</term><description> 
##  Exit from the dialog </description> </item></list>
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
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## PushButton</term><description> 
    ##   </description> </item><item><term> 
    ## DialogItem</term><description> 
    ##   </description> </item><item><term> 
    ## RadioBox</term><description> 
    ##   </description> </item><item><term> 
    ## RealItem</term><description> 
    ##   </description> </item><item><term> 
    ## RealScale</term><description> 
    ##   </description> </item><item><term> 
    ## Bitmap</term><description> 
    ##   </description> </item><item><term> 
    ## RowColumn</term><description> 
    ##   </description> </item><item><term> 
    ## ButtonLayout</term><description> 
    ##   </description> </item><item><term> 
    ## ScrolledWindow</term><description> 
    ##   </description> </item><item><term> 
    ## ColorTool</term><description> 
    ##   </description> </item><item><term> 
    ## SelectionBox</term><description> 
    ##   </description> </item><item><term> 
    ## Separator</term><description> 
    ##   </description> </item><item><term> 
    ## SingleSelectList</term><description> 
    ##   </description> </item><item><term> 
    ## StringItem</term><description> 
    ##   </description> </item><item><term> 
    ## GroupBox</term><description> 
    ##   </description> </item><item><term> 
    ## IntegerItem</term><description> 
    ##   </description> </item><item><term> 
    ## IntegerScale</term><description> 
    ##   </description> </item><item><term> 
    ## MultiSelectList</term><description> 
    ##   </description> </item><item><term> 
    ## LabelItem</term><description> 
    ##   </description> </item><item><term> 
    ## MultiTextBox</term><description> 
    ##   </description> </item><item><term> 
    ## TabControl</term><description> 
    ##   </description> </item><item><term> 
    ## OptionMenu</term><description> 
    ##   </description> </item><item><term> 
    ## Toggle</term><description> 
    ##   </description> </item><item><term> 
    ## OptionToggle</term><description> 
    ##   </description> </item><item><term> 
    ## ToolPalette</term><description> 
    ##   </description> </item><item><term> 
    ## WideString</term><description> 
    ##   </description> </item><item><term> 
    ## PropertyPage</term><description> 
    ##   </description> </item><item><term> 
    ## CollapsibleGroup</term><description> 
    ##   </description> </item></list>
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
    def Dispose(self) -> None:
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
    ## 
    ## <param name="item_identifier"> (str)  Dialog name </param>
    def GetBitmap(self, item_identifier: str) -> BitMap:
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
    ## 
    ## <param name="item_identifier"> (str)  Dialog name </param>
    def GetButtonLayout(self, item_identifier: str) -> ButtonLayout:
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
    ## 
    ## <param name="item_identifier"> (str)  Dialog name </param>
    def GetCollapsibleGroup(self, item_identifier: str) -> CollapsibleGroup:
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
    ## 
    ## <param name="item_identifier"> (str)  Dialog name </param>
    def GetColorTool(self, item_identifier: str) -> ColorTool:
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
    ## 
    ## <param name="item_identifier"> (str)  Dialog name </param>
    def GetDialogIndex(self, item_identifier: str) -> DialogItem:
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
    ## 
    ## <param name="select"> (@link NXOpen.SelectionHandle NXOpen.SelectionHandle@endlink) Selection handle </param>
    def GetDialogItemUsingSelectionHandle(self, select: NXOpen.SelectionHandle) -> StylerItem:
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
    ## 
    ## <param name="item_identifier"> (str)  Dialog name </param>
    def GetGroupBox(self, item_identifier: str) -> GroupBox:
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
    ## 
    ## <param name="item_identifier"> (str)  Dialog name </param>
    def GetIntegerItem(self, item_identifier: str) -> IntegerItem:
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
    ## 
    ## <param name="item_identifier"> (str)  Dialog name </param>
    def GetIntegerScale(self, item_identifier: str) -> IntegerScale:
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
    ## 
    ## <param name="item_identifier"> (str)  Dialog name </param>
    def GetLabelItem(self, item_identifier: str) -> LabelItem:
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
    ## 
    ## <param name="item_identifier"> (str)  Dialog name </param>
    def GetMultiSelectList(self, item_identifier: str) -> MultiSelectList:
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
    ## 
    ## <param name="item_identifier"> (str)  Dialog name </param>
    def GetMultiTextBox(self, item_identifier: str) -> MultiTextBox:
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
    ## 
    ## <param name="item_identifier"> (str)  Dialog name </param>
    def GetOptionMenu(self, item_identifier: str) -> OptionMenu:
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
    ## 
    ## <param name="item_identifier"> (str)  Dialog name </param>
    def GetOptionToggle(self, item_identifier: str) -> OptionToggle:
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
    ## 
    ## <param name="item_identifier"> (str)  Dialog name </param>
    def GetPropertyPage(self, item_identifier: str) -> PropertyPage:
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
    ## 
    ## <param name="item_identifier"> (str)  Dialog name </param>
    def GetPushButton(self, item_identifier: str) -> PushButton:
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
    ## 
    ## <param name="item_identifier"> (str)  Dialog name </param>
    def GetRadioBox(self, item_identifier: str) -> RadioBox:
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
    ## 
    ## <param name="item_identifier"> (str)  Dialog name </param>
    def GetRealItem(self, item_identifier: str) -> RealItem:
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
    ## 
    ## <param name="item_identifier"> (str)  Dialog name </param>
    def GetRealScale(self, item_identifier: str) -> RealScale:
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
    ## 
    ## <param name="item_identifier"> (str)  Dialog name </param>
    def GetRowColumn(self, item_identifier: str) -> RowColumn:
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
    ## 
    ## <param name="item_identifier"> (str)  Dialog name </param>
    def GetScrolledWindow(self, item_identifier: str) -> ScrolledWindow:
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
    ## 
    ## <param name="item_identifier"> (str)  Dialog name </param>
    def GetSelectionBox(self, item_identifier: str) -> SelectionBox:
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
    ## 
    ## <param name="item_identifier"> (str)  Dialog name </param>
    def GetSeparator(self, item_identifier: str) -> Separator:
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
    ## 
    ## <param name="item_identifier"> (str)  Dialog name </param>
    def GetSingleSelectList(self, item_identifier: str) -> SingleSelectList:
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
    ## 
    ## <param name="item_identifier"> (str)  Dialog name </param>
    def GetStringItem(self, item_identifier: str) -> StringItem:
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
    ## 
    ## <param name="item_identifier"> (str)  Dialog name </param>
    ## <param name="type"> (@link Dialog.ItemType NXOpen.UIStyler.Dialog.ItemType@endlink)  </param>
    def GetStylerItem(self, item_identifier: str, type: Dialog.ItemType) -> StylerItem:
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
    ## 
    ## <param name="item_identifier"> (str)  Dialog name </param>
    def GetTabControl(self, item_identifier: str) -> TabControl:
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
    ## 
    ## <param name="item_identifier"> (str)  Dialog name </param>
    def GetToggle(self, item_identifier: str) -> Toggle:
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
    ## 
    ## <param name="item_identifier"> (str)  Dialog name </param>
    def GetToolPalette(self, item_identifier: str) -> ToolPalette:
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
    ## 
    ## <param name="item_identifier"> (str)  Dialog name </param>
    def GetWideString(self, item_identifier: str) -> WideString:
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
    ## <param name="is_top_dialog"> (bool)  </param>
    def RegisterWithUiMenu(self, is_top_dialog: bool) -> None:
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
    def Show(self) -> DialogResponse:
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
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Enter</term><description> 
    ##  Enter file state </description> </item><item><term> 
    ## Exit</term><description> 
    ##  Exit file state </description> </item></list>
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
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## New</term><description> 
    ##  New file operation </description> </item><item><term> 
    ## Open</term><description> 
    ##  Open file operation </description> </item><item><term> 
    ## Save</term><description> 
    ##  Save file operation </description> </item><item><term> 
    ## SaveAs</term><description> 
    ##  Save as file operation </description> </item><item><term> 
    ## SaveAll</term><description> 
    ##  Save all file operation </description> </item><item><term> 
    ## Close</term><description> 
    ##  Close file operation </description> </item><item><term> 
    ## Quit</term><description> 
    ##  Quit file operation </description> </item><item><term> 
    ## SaveAndExit</term><description> 
    ##  Save and Exit file operation </description> </item><item><term> 
    ## ChangePart</term><description> 
    ##  Chaneg part file operation </description> </item><item><term> 
    ## Execute</term><description> 
    ##  Execute file operation </description> </item><item><term> 
    ## Reopen</term><description> 
    ##  Reopen file operation </description> </item><item><term> 
    ## SaveAllAndClose</term><description> 
    ##  Save all and close file operation </description> </item><item><term> 
    ## SaveAndClose</term><description> 
    ##  Save and close file operation </description> </item><item><term> 
    ## SaveAsAndClose</term><description> 
    ##  Save as and close file operation </description> </item></list>
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
    ##  Returns the state   
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
         Returns the state   
            
         
        """
        pass
    
    ## Getter for property: (@link FileOperationData.FileOperationType NXOpen.UIStyler.FileOperationData.FileOperationType@endlink) Type
    ##  Returns the file operation type   
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
         Returns the file operation type   
            
         
        """
        pass
    
    ##  Free resources associated with the instance. After this method
    ##     is called, it is illegal to use the object.  In .NET or Java, this 
    ##     method is automatically called when the object is deleted by the 
    ##     garbage collector. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
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
    ##  Returns the sensitivity   
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
         Returns the sensitivity   
            
         
        """
        pass
    
    ## Setter for property: (bool) Sensitivity

    ##  Returns the sensitivity   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
         Returns the sensitivity   
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##  Returns the visibility   
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
         Returns the visibility   
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##  Returns the visibility   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility   
            
         
        """
        pass
    
    ##  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="str_label"> (str)  Text label to display in the top line of the group box frame </param>
    def SetLabel(self, str_label: str) -> None:
        """
         
        """
        pass
    
##  Represents a Integer for UI Styler. 
## 
##   <br>  Created in NX5.0.0  <br> 

class IntegerItem(StylerItem): 
    """ Represents a Integer for UI Styler. """


    ## Getter for property: (int) ItemValue
    ##  Returnsthe value obtained from the text field.  
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
         Returnsthe value obtained from the text field.  
            
         
        """
        pass
    
    ## Setter for property: (int) ItemValue

    ##  Returnsthe value obtained from the text field.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ItemValue.setter
    def ItemValue(self, item_val: int):
        """
        Setter for property: (int) ItemValue
         Returnsthe value obtained from the text field.  
            
         
        """
        pass
    
    ## Getter for property: (bool) Sensitivity
    ##  Returns the sensitivity of Integer item   
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
         Returns the sensitivity of Integer item   
            
         
        """
        pass
    
    ## Setter for property: (bool) Sensitivity

    ##  Returns the sensitivity of Integer item   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
         Returns the sensitivity of Integer item   
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##  Returns the visibility of the dialog item.  
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
         Returns the visibility of the dialog item.  
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##  Returns the visibility of the dialog item.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility of the dialog item.  
            
         
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
    ## <param name="activateevent"> (@link IntegerItem.Activate NXOpen.UIStyler.IntegerItem.Activate@endlink)  </param>
    ## <param name="is_dialog_launching_event"> (bool)  </param>
    def AddActivateHandler(self, activateevent: IntegerItem.Activate, is_dialog_launching_event: bool) -> None:
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
    ## 
    ## <param name="bitmap"> (str) Filename with .ubm, .xpm, or .bmp extension that contains bitmap definition</param>
    def SetBitmap(self, bitmap: str) -> None:
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
    def SetFocus(self) -> None:
        """
         Sets focus 
        """
        pass
    
    ## Specifies descriptive text to display for the dialog item. It should describe the dialog 
    ##     item's intended use. If you specify a bitmap for this dialog item, it uses this text as tooltip text. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="str_label"> (str)  String to display on the left side of the text field.</param>
    def SetLabel(self, str_label: str) -> None:
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
    ##  Returns   
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
         Returns   
            
         
        """
        pass
    
    ## Setter for property: (int) ItemValue

    ##  Returns   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ItemValue.setter
    def ItemValue(self, item_val: int):
        """
        Setter for property: (int) ItemValue
         Returns   
            
         
        """
        pass
    
    ## Getter for property: (bool) Sensitivity
    ##  Returns the sensitivity of the dialog item.  
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
         Returns the sensitivity of the dialog item.  
             
         
        """
        pass
    
    ## Setter for property: (bool) Sensitivity

    ##  Returns the sensitivity of the dialog item.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
         Returns the sensitivity of the dialog item.  
             
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##  Returnsthe visibility of the dialog item.  
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
         Returnsthe visibility of the dialog item.  
             
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##  Returnsthe visibility of the dialog item.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returnsthe visibility of the dialog item.  
             
         
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
    ## <param name="dragevent"> (@link IntegerScale.Drag NXOpen.UIStyler.IntegerScale.Drag@endlink)  </param>
    ## <param name="is_dialog_launching_event"> (bool)  </param>
    def AddDragHandler(self, dragevent: IntegerScale.Drag, is_dialog_launching_event: bool) -> None:
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
    ## 
    ## <param name="valuechangedevent"> (@link IntegerScale.ValueChanged NXOpen.UIStyler.IntegerScale.ValueChanged@endlink)  Value changed event </param>
    ## <param name="is_dialog_launching_event"> (bool)  True if launch any dialog else False </param>
    def AddValueChangedHandler(self, valuechangedevent: IntegerScale.ValueChanged, is_dialog_launching_event: bool) -> None:
        """
        Registers value change callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ## Specifies the text for the minimum and maximum label. By default, the system uses the maximum/minimum 
    ##     value as a text label.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="minimum_label"> (str) minimum limit for label </param>
    ## <param name="maximum_label"> (str) maximum limit for label </param>
    def SetLabels(self, minimum_label: str, maximum_label: str) -> None:
        """
        Specifies the text for the minimum and maximum label. By default, the system uses the maximum/minimum 
            value as a text label.
        """
        pass
    
    ## Specifies the scale's maximum and minimum value.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="minimum_value"> (int) to set minimum </param>
    ## <param name="maximum_value"> (int) to set maximum </param>
    def SetLimits(self, minimum_value: int, maximum_value: int) -> None:
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
    ##  Returns the seisitivity of the dialog item  
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
         Returns the seisitivity of the dialog item  
            
         
        """
        pass
    
    ## Setter for property: (bool) Sensitivity

    ##  Returns the seisitivity of the dialog item  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
         Returns the seisitivity of the dialog item  
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##  Returns the visibility of the dialog item  
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
         Returns the visibility of the dialog item  
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##  Returns the visibility of the dialog item  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility of the dialog item  
            
         
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
    ## <param name="bitmap_file"> (str)  </param>
    def SetBitmap(self, bitmap_file: str) -> None:
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
    ## <param name="str_label"> (str)  </param>
    def SetLabel(self, str_label: str) -> None:
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
    ##  Returns the senstivity   
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
         Returns the senstivity   
            
         
        """
        pass
    
    ## Setter for property: (bool) Sensitivity

    ##  Returns the senstivity   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
         Returns the senstivity   
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##  Returnsthe visibility  
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
         Returnsthe visibility  
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##  Returnsthe visibility  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returnsthe visibility  
            
         
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
    ## <param name="activateevent"> (@link MultiSelectList.Activate NXOpen.UIStyler.MultiSelectList.Activate@endlink)  </param>
    ## <param name="is_dialog_launching_event"> (bool)  </param>
    def AddActivateHandler(self, activateevent: MultiSelectList.Activate, is_dialog_launching_event: bool) -> None:
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
    ## <param name="doubleclickevent"> (@link MultiSelectList.DoubleClick NXOpen.UIStyler.MultiSelectList.DoubleClick@endlink)  </param>
    ## <param name="is_dialog_launching_event"> (bool)  </param>
    def AddDoubleClickHandler(self, doubleclickevent: MultiSelectList.DoubleClick, is_dialog_launching_event: bool) -> None:
        """
        Registers double click callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ##  Appends one or more entries to be inserted into the list 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="multi_entries"> (List[str]) An array of entry names to be inserted into the list. This field is used only when more than one entry are to be inserted into the list.</param>
    def Append(self, multi_entries: List[str]) -> None:
        """
         Appends one or more entries to be inserted into the list 
        """
        pass
    
    ##  Deletes sub item 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="subItemIndex"> (int)  Zero-based index of a list entry to be deleted </param>
    def DeleteSubitem(self, subItemIndex: int) -> None:
        """
         Deletes sub item 
        """
        pass
    
    ## Requests a list entry to be deselected.
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="subItemIndex"> (int)  Index of the list entry to be deselected.</param>
    def Deselect(self, subItemIndex: int) -> None:
        """
        Requests a list entry to be deselected.
            
        """
        pass
    
    ##  Indicates that this dialog item is receiving keyboard focus.
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def Focus(self) -> None:
        """
         Indicates that this dialog item is receiving keyboard focus.
            
        """
        pass
    
    ## Gets the indices of all selected list entries. 
    ##  @return indices (List[int]):  An array of integers for item indices of selected items .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetAllIndicesSelected(self) -> List[int]:
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
    def GetAllNameSelected(self) -> List[str]:
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
    def GetListItems(self) -> List[str]:
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
    ## 
    ## <param name="subitem_index"> (int)  Sub item index </param>
    ## <param name="multi_entries"> (List[str])  An array of items to be inserted </param>
    def InsertSubitems(self, subitem_index: int, multi_entries: List[str]) -> None:
        """
         
        """
        pass
    
    ## Specifies all list entry to be selected.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def SetAllSelected(self) -> None:
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
    ## 
    ## <param name="item_val"> (List[str]) array of character strings for item names</param>
    def SetListItems(self, item_val: List[str]) -> None:
        """
        Specifies an array of character strings for item names that are used as selectable choices for this 
            dialog item.
            
        """
        pass
    
    ## Specifies particular list items to be selected.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="subIndex"> (int)  An index of particular list items to be selected </param>
    def SetSelected(self, subIndex: int) -> None:
        """
        Specifies particular list items to be selected.
        """
        pass
    
    ##  Requests a list entry to be scrolled up to the first line in the list 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="subItemIndex"> (int)  Zero-based index of a list entry to be scrolled up 
    ##                                 to the first line of the list.</param>
    def ShowSubItem(self, subItemIndex: int) -> None:
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
    ##  Returnsthe sensitivity of the dialog item.  
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
         Returnsthe sensitivity of the dialog item.  
             
         
        """
        pass
    
    ## Setter for property: (bool) Sensitivity

    ##  Returnsthe sensitivity of the dialog item.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
         Returnsthe sensitivity of the dialog item.  
             
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##  Returns the visibility of the dialog item   
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
         Returns the visibility of the dialog item   
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##  Returns the visibility of the dialog item   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility of the dialog item   
            
         
        """
        pass
    
    ## Specifies the text for this dialog item. It can be programmatically get by APIs. 
    ##  @return item_val (List[str]):  to get array of strings.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetItemValues(self) -> List[str]:
        """
        Specifies the text for this dialog item. It can be programmatically get by APIs. 
         @return item_val (List[str]):  to get array of strings.
        """
        pass
    
    ## Indicates that this dialog item is receiving keyboard focus.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def SetFocus(self) -> None:
        """
        Indicates that this dialog item is receiving keyboard focus.
        """
        pass
    
    ## Specifies the text for this dialog item. It can be programmatically set by APIs supported in 
    ##     different laguages,or interactively entered by the user. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="values"> (List[str]) array of strings to set the values in multi 
    ##                                 select List</param>
    def SetItemValues(self, values: List[str]) -> None:
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
    ## 
    ## <param name="str_label"> (str) new label string </param>
    def SetLabel(self, str_label: str) -> None:
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
    ##  Returns the item value   
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
         Returns the item value   
            
         
        """
        pass
    
    ## Setter for property: (int) ItemValue

    ##  Returns the item value   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ItemValue.setter
    def ItemValue(self, item_val: int):
        """
        Setter for property: (int) ItemValue
         Returns the item value   
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##  Returns the visibility   
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
         Returns the visibility   
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##  Returns the visibility   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility   
            
         
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
    ## 
    ## <param name="activateevent"> (@link OptionMenu.Activate NXOpen.UIStyler.OptionMenu.Activate@endlink)  Callback for activate event </param>
    ## <param name="is_dialog_launching_event"> (bool)  TRUE if dialog is going to launch, FALSE if not </param>
    def AddActivateHandler(self, activateevent: OptionMenu.Activate, is_dialog_launching_event: bool) -> None:
        """
        Registers activate callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ##  Returns an array of bitmaps 
    ##  @return bitmaps (List[str]):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetBitmap(self) -> List[str]:
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
    def GetItems(self) -> List[str]:
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
    def GetSensitivity(self) -> bool:
        """
         Gets the sensitivity 
         @return type (bool):  .
        """
        pass
    
    ##  Set an array of bitmap filenames 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="bitmaps"> (List[str])  An array of one or more bitmap filenames. 
    ##         If all bitmaps for the option menu reside in the same file, specify an array of just one entry, 
    ##         which contains the bitmap filename for this attribute. All existing choices for the option menu 
    ##         remains intact when this attribute is set. Only the bitmaps are changed. Note that the number of 
    ##         bitmaps must match the number of existing choices. </param>
    def SetBitmap(self, bitmaps: List[str]) -> None:
        """
         Set an array of bitmap filenames 
        """
        pass
    
    ##  Set an array of items 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="str_list_array"> (List[str])  An array of new choices to be used for the 
    ##         dialog item. Note that this removes all existing choices (both text and bitmaps) </param>
    def SetItems(self, str_list_array: List[str]) -> None:
        """
         Set an array of items 
        """
        pass
    
    ##  Sets label 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="str_label"> (str)  Text to be set for the descriptive label. </param>
    def SetLabel(self, str_label: str) -> None:
        """
         Sets label 
        """
        pass
    
    ##  Sets the sensitivity 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="subitem_index"> (int)  If the entire dialog item should change to the new Sensitivity state, 
    ##         set this field to UF_STYLER_NO_SUB_INDEX. If only one subitem should change to the new sensitivity state,
    ##         set this field to its zero-based index. </param>
    ## <param name="type"> (bool)  TRUE if sensitive, FALSE if insensitive </param>
    def SetSensitivity(self, subitem_index: int, type: bool) -> None:
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
    ##  Returns the visibility   
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
         Returns the visibility   
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##  Returns the visibility   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility   
            
         
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
    ## 
    ## <param name="activateevent"> (@link OptionToggle.Activate NXOpen.UIStyler.OptionToggle.Activate@endlink)  Callback for activate event </param>
    ## <param name="is_dialog_launching_event"> (bool)  TRUE if dialog is going to launch, FALSE if not </param>
    def AddActivateHandler(self, activateevent: OptionToggle.Activate, is_dialog_launching_event: bool) -> None:
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
    ## 
    ## <param name="valuechangedevent"> (@link OptionToggle.ValueChanged NXOpen.UIStyler.OptionToggle.ValueChanged@endlink)  Callback for value changed event </param>
    ## <param name="is_dialog_launching_event"> (bool)  TRUE if dialog is going to launch, FALSE if not </param>
    def AddValueChangedHandler(self, valuechangedevent: OptionToggle.ValueChanged, is_dialog_launching_event: bool) -> None:
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
    def GetItemValue(self) -> Tuple[int, bool]:
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
    def GetItems(self) -> List[str]:
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
    def GetSensitivity(self) -> bool:
        """
         Returns the sesitivity 
         @return type (bool):  .
        """
        pass
    
    ##  Set bitmaps 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="bitmaps"> (List[str])  An array of one or more bitmap filenames. 
    ##         If all bitmaps for the option menu reside in the same file, specify an array of just one entry, 
    ##         which contains the bitmap filename for this attribute. All existing choices for the option menu 
    ##         remain intact when this attribute is set. Only the bitmaps are changed. Note that the number of 
    ##         bitmaps must match the number of existing choices. </param>
    def SetBitmaps(self, bitmaps: List[str]) -> None:
        """
         Set bitmaps 
        """
        pass
    
    ##  Sets default action 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def SetDefaultAction(self) -> None:
        """
         Sets default action 
        """
        pass
    
    ##  Sets item value 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="subitem_index"> (int)  Zero-based index indicating the choice to be selected. 
    ##         It must be in the range of existing choices.</param>
    ## <param name="set_check"> (bool)  TRUE if set, FALSE if unset. </param>
    def SetItemValue(self, subitem_index: int, set_check: bool) -> None:
        """
         Sets item value 
        """
        pass
    
    ##  Sets items in the array 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="str_list_array"> (List[str])  An array of new choices to be used for the dialog item. 
    ##         Note that this removes all existing choices (both text and bitmaps). </param>
    def SetItems(self, str_list_array: List[str]) -> None:
        """
         Sets items in the array 
        """
        pass
    
    ##  Sets label 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="str_label"> (str)  Text to be set for the tool tip. </param>
    def SetLabel(self, str_label: str) -> None:
        """
         Sets label 
        """
        pass
    
    ##  Set the sesitivity 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="subitem_index"> (int)  If the entire dialog item should change to the new Sensitivity state, 
    ##         set this field to UF_STYLER_NO_SUB_INDEX. If only one sub-item should change to the new sensitivity 
    ##         state, set this field to its zero-based index. </param>
    ## <param name="type"> (bool)  TRUE if sensitive, FALSE if insensitive </param>
    def SetSensitivity(self, subitem_index: int, type: bool) -> None:
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
    ##  Returns the activated page   
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
         Returns the activated page   
            
         
        """
        pass
    
    ## Getter for property: (int) DeactivatedPage
    ##  Returns the deactivated page   
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
         Returns the deactivated page   
            
         
        """
        pass
    
    ##  Free resources associated with the instance. After this method
    ##     is called, it is illegal to use the object.  In .NET or Java, this 
    ##     method is automatically called when the object is deleted by the 
    ##     garbage collector. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
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
    ##  Returns the sensitivity of property page.  
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
         Returns the sensitivity of property page.  
             
         
        """
        pass
    
    ## Setter for property: (bool) Sensitivity

    ##  Returns the sensitivity of property page.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
         Returns the sensitivity of property page.  
             
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##  Returnsthe visibility of the dialog item.  
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
         Returnsthe visibility of the dialog item.  
             
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##  Returnsthe visibility of the dialog item.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returnsthe visibility of the dialog item.  
             
         
        """
        pass
    
    ##  Sets focus 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def SetFocus(self) -> None:
        """
         Sets focus 
        """
        pass
    
    ## Specifies descriptive text to display for the dialog item. It should describe the dialog item's intended use. 
    ##     If you specify a bitmap for this dialog item, it uses this text as tooltip text. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="str_label"> (str) new label</param>
    def SetLabel(self, str_label: str) -> None:
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
    ##  Returns the senstivity of dialog.  
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
         Returns the senstivity of dialog.  
            
         
        """
        pass
    
    ## Setter for property: (bool) Sensitivity

    ##  Returns the senstivity of dialog.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
         Returns the senstivity of dialog.  
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##  Returns the visibility of dialog.  
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
         Returns the visibility of dialog.  
              
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##  Returns the visibility of dialog.  
    ##       
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility of dialog.  
              
         
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
    ## <param name="activateevent"> (@link PushButton.Activate NXOpen.UIStyler.PushButton.Activate@endlink)  </param>
    ## <param name="is_dialog_launching_event"> (bool)  </param>
    def AddActivateHandler(self, activateevent: PushButton.Activate, is_dialog_launching_event: bool) -> None:
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
    ## 
    ## <param name="bitmap"> (str) the bitmap extension </param>
    def SetBitmap(self, bitmap: str) -> None:
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
    def SetDefaultAction(self) -> None:
        """
         Sets default action 
        """
        pass
    
    ## Indicates that this dialog item is receiving keyboard focus. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def SetFocus(self) -> None:
        """
        Indicates that this dialog item is receiving keyboard focus. 
        """
        pass
    
    ## Specifies descriptive text to display for the dialog item. It should describe the dialog item's intended 
    ##     use. If you specify a bitmap for this dialog item, it uses this text as tooltip text.  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="str_label"> (str) the label string </param>
    def SetLabel(self, str_label: str) -> None:
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
    ##  Returns the item value   
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
         Returns the item value   
            
         
        """
        pass
    
    ## Setter for property: (int) ItemValue

    ##  Returns the item value   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ItemValue.setter
    def ItemValue(self, item_val: int):
        """
        Setter for property: (int) ItemValue
         Returns the item value   
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##  Returns the visibility   
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
         Returns the visibility   
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##  Returns the visibility   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility   
            
         
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
    ## 
    ## <param name="valuechangedevent"> (@link RadioBox.ValueChanged NXOpen.UIStyler.RadioBox.ValueChanged@endlink)  Callback for value changed event </param>
    ## <param name="is_dialog_launching_event"> (bool)  TRUE if dialog is going to launch, FALSE if not </param>
    def AddValueChangedHandler(self, valuechangedevent: RadioBox.ValueChanged, is_dialog_launching_event: bool) -> None:
        """
        Registers value change callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ##  Gets the sensitivity 
    ##  @return type (bool):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetSensitivity(self) -> bool:
        """
         Gets the sensitivity 
         @return type (bool):  .
        """
        pass
    
    ##  Set default action 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def SetDefaultAction(self) -> None:
        """
         Set default action 
        """
        pass
    
    ##  Sets label 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="str_label"> (str)  Text to be set for the descriptive label </param>
    def SetLabel(self, str_label: str) -> None:
        """
         Sets label 
        """
        pass
    
    ##  Sets the sensitivity 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="subitem_index"> (int)  </param>
    ## <param name="type"> (bool)  TRUE if visible, FALSE if invisible </param>
    def SetSensitivity(self, subitem_index: int, type: bool) -> None:
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
    ##  Returns the item value   
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
         Returns the item value   
            
         
        """
        pass
    
    ## Setter for property: (float) ItemValue

    ##  Returns the item value   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ItemValue.setter
    def ItemValue(self, item_val: float):
        """
        Setter for property: (float) ItemValue
         Returns the item value   
            
         
        """
        pass
    
    ## Getter for property: (bool) Sensitivity
    ##  Returns the sensitivity   
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
         Returns the sensitivity   
            
         
        """
        pass
    
    ## Setter for property: (bool) Sensitivity

    ##  Returns the sensitivity   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
         Returns the sensitivity   
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##  Returns the visibility   
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
         Returns the visibility   
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##  Returns the visibility   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility   
            
         
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
    ## 
    ## <param name="activateevent"> (@link RealItem.Activate NXOpen.UIStyler.RealItem.Activate@endlink)  Callback for activate event </param>
    ## <param name="is_dialog_launching_event"> (bool)  TRUE if dialog is going to launch, FALSE if not </param>
    def AddActivateHandler(self, activateevent: RealItem.Activate, is_dialog_launching_event: bool) -> None:
        """
        Registers activate callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ##  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="str_bitmap"> (str)  Filename with .ubm, .xpm, or .bmp extension that contains a bitmap definition </param>
    def SetBitmap(self, str_bitmap: str) -> None:
        """
         
        """
        pass
    
    ##  Sets focus 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def SetFocus(self) -> None:
        """
         Sets focus 
        """
        pass
    
    ##  Set the label 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="str_label"> (str)  Text label to display on the left side of the text field. </param>
    def SetLabel(self, str_label: str) -> None:
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
    ##  Returns the item value   
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
         Returns the item value   
            
         
        """
        pass
    
    ## Setter for property: (float) ItemValue

    ##  Returns the item value   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ItemValue.setter
    def ItemValue(self, item_val: float):
        """
        Setter for property: (float) ItemValue
         Returns the item value   
            
         
        """
        pass
    
    ## Getter for property: (bool) Sensitivity
    ##  Returns the sensitivity   
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
         Returns the sensitivity   
            
         
        """
        pass
    
    ## Setter for property: (bool) Sensitivity

    ##  Returns the sensitivity   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
         Returns the sensitivity   
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##  Returns the visibility   
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
         Returns the visibility   
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##  Returns the visibility   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility   
            
         
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
    ## 
    ## <param name="dragevent"> (@link RealScale.Drag NXOpen.UIStyler.RealScale.Drag@endlink)  Callback for add drag event </param>
    ## <param name="is_dialog_launching_event"> (bool)  TRUE if dialog is going to launch, FALSE if not </param>
    def AddDragHandler(self, dragevent: RealScale.Drag, is_dialog_launching_event: bool) -> None:
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
    ## 
    ## <param name="valuechangedevent"> (@link RealScale.ValueChanged NXOpen.UIStyler.RealScale.ValueChanged@endlink)  Callback for value changed event </param>
    ## <param name="is_dialog_launching_event"> (bool)  TRUE if dialog is going to launch, FALSE if not </param>
    def AddValueChangedHandler(self, valuechangedevent: RealScale.ValueChanged, is_dialog_launching_event: bool) -> None:
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
    ## 
    ## <param name="digits"> (int)  The number significant digits </param>
    def SetDecimalPrecision(self, digits: int) -> None:
        """
         Sets decimal precision 
        """
        pass
    
    ##  Sets labels 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="minimum_label"> (str)  String minimum label </param>
    ## <param name="maximum_label"> (str)  String maximum label </param>
    def SetLabels(self, minimum_label: str, maximum_label: str) -> None:
        """
         Sets labels 
        """
        pass
    
    ##  Sets limits 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="minimum_value"> (float)  Real minimum value </param>
    ## <param name="maximum_value"> (float)  Real maximum value </param>
    def SetLimits(self, minimum_value: float, maximum_value: float) -> None:
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
    ##  Returns the sensitivity   
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
         Returns the sensitivity   
            
         
        """
        pass
    
    ## Setter for property: (bool) Sensitivity

    ##  Returns the sensitivity   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
         Returns the sensitivity   
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##  Returns the visibility   
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
         Returns the visibility   
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##  Returns the visibility   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility   
            
         
        """
        pass
    
##  Represents a ScrolledWindow for UI Styler 
## 
##   <br>  Created in NX5.0.0  <br> 

class ScrolledWindow(StylerItem): 
    """ Represents a ScrolledWindow for UI Styler """


    ## Getter for property: (bool) Sensitivity
    ##  Returns   
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
         Returns   
            
         
        """
        pass
    
    ## Setter for property: (bool) Sensitivity

    ##  Returns   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
         Returns   
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##  Returns   
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
         Returns   
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##  Returns   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns   
            
         
        """
        pass
    
##  Represents a SelectionBox for UI Styler 
## 
##   <br>  Created in NX5.0.0  <br> 

class SelectionBox(StylerItem): 
    """ Represents a SelectionBox for UI Styler """


    ## Getter for property: (bool) Sensitivity
    ##  Returns the sensitivity of the selection box  
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
         Returns the sensitivity of the selection box  
            
         
        """
        pass
    
    ## Setter for property: (bool) Sensitivity

    ##  Returns the sensitivity of the selection box  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
         Returns the sensitivity of the selection box  
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##  Returns the visibility of the selection box  
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
         Returns the visibility of the selection box  
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##  Returns the visibility of the selection box  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility of the selection box  
            
         
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
    ## 
    ## <param name="activateevent"> (@link SelectionBox.Activate NXOpen.UIStyler.SelectionBox.Activate@endlink)  Activate event </param>
    ## <param name="is_dialog_launching_event"> (bool)  TRUE if launch new dialog, FALSE if not </param>
    def AddActivateHandler(self, activateevent: SelectionBox.Activate, is_dialog_launching_event: bool) -> None:
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
    ## 
    ## <param name="doubleclickevent"> (@link SelectionBox.DoubleClick NXOpen.UIStyler.SelectionBox.DoubleClick@endlink)  Double click event </param>
    ## <param name="is_dialog_launching_event"> (bool)  TRUE if launch new dialog, FALSE if not </param>
    def AddDoubleClickHandler(self, doubleclickevent: SelectionBox.DoubleClick, is_dialog_launching_event: bool) -> None:
        """
        Registers double click callback. This method should be called before calling @link UIStyler::Dialog::Show  UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ##  Appends one or more entries to be inserted into the list 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="multi_entries"> (List[str]) An array of entry names to be inserted into the list. This field is used only when more than one entry are to be inserted into the list.</param>
    def Append(self, multi_entries: List[str]) -> None:
        """
         Appends one or more entries to be inserted into the list 
        """
        pass
    
    ##  Deletes sub item 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="subItemIndex"> (int)  </param>
    def DeleteSubItem(self, subItemIndex: int) -> None:
        """
         Deletes sub item 
        """
        pass
    
    ##  Requests a list entry to be deselected.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="subItemIndex"> (int)  </param>
    def DeselectSubItem(self, subItemIndex: int) -> None:
        """
         Requests a list entry to be deselected.
        """
        pass
    
    ##  Gets an array of character strings for item names that are used as selectable choices for this dialog item.
    ##  @return values (List[str]):  List of items .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetListItems(self) -> List[str]:
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
    def GetSelectedIndexValue(self) -> int:
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
    def GetSelectedString(self) -> str:
        """
         Gets selected string 
         @return value (str):  .
        """
        pass
    
    ##  Requests that one or more entries be inserted into the list. You can insert entries at the bottom of the list or at any position within the list.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="subitem_index"> (int)  Position index where the insertion should be made. If subitem_index equals UF_STYLER_NO_SUB_INDEX, then the new list entries are added to the bottom of the list. </param>
    ## <param name="multi_entries"> (List[str])  </param>
    def InsertSubItem(self, subitem_index: int, multi_entries: List[str]) -> None:
        """
         Requests that one or more entries be inserted into the list. You can insert entries at the bottom of the list or at any position within the list.
        """
        pass
    
    ##  Indicates that this dialog item is receiving keyboard focus. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def SetFocus(self) -> None:
        """
         Indicates that this dialog item is receiving keyboard focus. 
        """
        pass
    
    ##  Specifies the descriptive text string to display below the scrolled list and above the text field. It describes the dialog item's usage.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="str_label"> (str)  Label string </param>
    def SetLabel(self, str_label: str) -> None:
        """
         Specifies the descriptive text string to display below the scrolled list and above the text field. It describes the dialog item's usage.
        """
        pass
    
    ##  Specifies an array of character strings for item names that are used as selectable choices for this dialog item.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="values"> (List[str])  List of items </param>
    def SetListItems(self, values: List[str]) -> None:
        """
         Specifies an array of character strings for item names that are used as selectable choices for this dialog item.
        """
        pass
    
    ##  Sets the value 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="value"> (int)  </param>
    def SetValue(self, value: int) -> None:
        """
         Sets the value 
        """
        pass
    
    ##  Requests that a list entry be scrolled up to the first line in the list. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="subItemIndex"> (int)  </param>
    def ShowSubItem(self, subItemIndex: int) -> None:
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
    ##  Returns the visibility of the separator  
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
         Returns the visibility of the separator  
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##  Returns the visibility of the separator  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility of the separator  
            
         
        """
        pass
    
##  Represents a SingleSelectList for UI Styler 
## 
##   <br>  Created in NX5.0.0  <br> 

class SingleSelectList(StylerItem): 
    """ Represents a SingleSelectList for UI Styler """


    ## Getter for property: (bool) Sensitivity
    ##  Returns the sensitivity of the single select list  
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
         Returns the sensitivity of the single select list  
            
         
        """
        pass
    
    ## Setter for property: (bool) Sensitivity

    ##  Returns the sensitivity of the single select list  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
         Returns the sensitivity of the single select list  
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##  Returns the visibility of the single select list  
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
         Returns the visibility of the single select list  
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##  Returns the visibility of the single select list  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility of the single select list  
            
         
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
    ## <param name="activateevent"> (@link SingleSelectList.Activate NXOpen.UIStyler.SingleSelectList.Activate@endlink)  </param>
    ## <param name="is_dialog_launching_event"> (bool)  </param>
    def AddActivateHandler(self, activateevent: SingleSelectList.Activate, is_dialog_launching_event: bool) -> None:
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
    ## <param name="doubleclickevent"> (@link SingleSelectList.DoubleClick NXOpen.UIStyler.SingleSelectList.DoubleClick@endlink)  </param>
    ## <param name="is_dialog_launching_event"> (bool)  </param>
    def AddDoubleClickHandler(self, doubleclickevent: SingleSelectList.DoubleClick, is_dialog_launching_event: bool) -> None:
        """
        Registers double click callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ##  Appends one or more entries to be inserted into the list 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="multi_entries"> (List[str]) An array of entry names to be inserted into the list. This field is used only when more than one entry are to be inserted into the list.</param>
    def Append(self, multi_entries: List[str]) -> None:
        """
         Appends one or more entries to be inserted into the list 
        """
        pass
    
    ##  Requests a list entry to be deleted. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="subItemIndex"> (int) Zero-based index of a list entry to be deleted. If subitem_index equals UF_STYLER_NO_SUB_INDEX, then all list entries are deleted. </param>
    def DeleteSubItem(self, subItemIndex: int) -> None:
        """
         Requests a list entry to be deleted. 
        """
        pass
    
    ##  Requests a list entry to be deselected.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="subItemIndex"> (int)  </param>
    def DeselectSubItem(self, subItemIndex: int) -> None:
        """
         Requests a list entry to be deselected.
        """
        pass
    
    ##  Gets an array of character strings that are used as entries in the list.
    ##  @return item_val (List[str]):  An array of string items .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetListItems(self) -> List[str]:
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
    def GetSelectedIndexValue(self) -> int:
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
    def GetSelectedString(self) -> str:
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
    def HasSelected(self) -> bool:
        """
         Returns whether or not an item has been selected 
         @return selected (bool):  .
        """
        pass
    
    ##  Requests one or more entries to be inserted into the list. You can insert entries at the bottom of the list or at any position within the list. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="subitem_index"> (int)  Position index where the insertion should be made. If subitem_index equals UF_STYLER_NO_SUB_INDEX, then the new list entries are added to the bottom of the list.</param>
    ## <param name="multi_entries"> (List[str]) An array of entry names to be inserted into the list. This field is used only when more than one entry are to be inserted into the list.</param>
    def InsertSubItem(self, subitem_index: int, multi_entries: List[str]) -> None:
        """
         Requests one or more entries to be inserted into the list. You can insert entries at the bottom of the list or at any position within the list. 
        """
        pass
    
    ##  Indicates that this dialog item is receiving keyboard focus. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def SetFocus(self) -> None:
        """
         Indicates that this dialog item is receiving keyboard focus. 
        """
        pass
    
    ##  Specifies an array of character strings that are used as entries in the list 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="item_val"> (List[str])  An array of string items </param>
    def SetListItems(self, item_val: List[str]) -> None:
        """
         Specifies an array of character strings that are used as entries in the list 
        """
        pass
    
    ##  Specifies particular list items to be selected 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="subIndex"> (int)  Inndex of particular list items to be selected</param>
    def SetSelected(self, subIndex: int) -> None:
        """
         Specifies particular list items to be selected 
        """
        pass
    
    ## Requests that a list entry be scrolled up to the first line in the list 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="subItemIndex"> (int)  Zero-based index of a list entry to be scrolled up to the first line of the list.</param>
    def ShowSubItem(self, subItemIndex: int) -> None:
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
    ##  Returns the string value for this dialog item.  
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
         Returns the string value for this dialog item.  
           It can be the initial value that is programmatically 
            defined, or interactively entered by the user.  
         
        """
        pass
    
    ## Setter for property: (str) ItemValue

    ##  Returns the string value for this dialog item.  
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
         Returns the string value for this dialog item.  
           It can be the initial value that is programmatically 
            defined, or interactively entered by the user.  
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##  Returns the visibility of the dialog item   
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
         Returns the visibility of the dialog item   
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##  Returns the visibility of the dialog item   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility of the dialog item   
            
         
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
    ## <param name="activateevent"> (@link StringItem.Activate NXOpen.UIStyler.StringItem.Activate@endlink)  </param>
    ## <param name="is_dialog_launching_event"> (bool)  </param>
    def AddActivateHandler(self, activateevent: StringItem.Activate, is_dialog_launching_event: bool) -> None:
        """
        Registers activate callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ##  To get senstivity of string control
    ##  @return type (bool):  TRUE if sensitive, FALSE if insensitive .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetSensitivity(self) -> bool:
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
    ## 
    ## <param name="str_bitmap"> (str)  Filename with .ubm, .xpm, or .bmp extension that contains bitmap definition </param>
    def SetBitmap(self, str_bitmap: str) -> None:
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
    def SetFocus(self) -> None:
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
    ## 
    ## <param name="str_label"> (str)  String label to display on the left side of the text field </param>
    def SetLabel(self, str_label: str) -> None:
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
    ## 
    ## <param name="type"> (bool)  TRUE if sensitive, FALSE if insensitive </param>
    def SetSensitivity(self, type: bool) -> None:
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
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NoValue</term><description> 
    ##  No value </description> </item><item><term> 
    ## StringValue</term><description> 
    ##  String value </description> </item><item><term> 
    ## StringPointerValue</term><description> 
    ##  String pointer value </description> </item><item><term> 
    ## IntegerValue</term><description> 
    ##  Integer value </description> </item><item><term> 
    ## IntegerPointerValue</term><description> 
    ##  Integer pointer value </description> </item><item><term> 
    ## RealValue</term><description> 
    ##  Real value </description> </item><item><term> 
    ## RealPointerValue</term><description> 
    ##  Real pointer value </description> </item><item><term> 
    ## SelectionValue</term><description> 
    ##  Selection value </description> </item><item><term> 
    ## OptionToggleValue</term><description> 
    ##  Option toggle value </description> </item></list>
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
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NoSubIndex</term><description> 
    ##  No sub index </description> </item><item><term> 
    ## OkIndex</term><description> 
    ##  Ok index </description> </item><item><term> 
    ## ApplyIndex</term><description> 
    ##  Apply index </description> </item><item><term> 
    ## BackIndex</term><description> 
    ##  Back index </description> </item><item><term> 
    ## CancelIndex</term><description> 
    ##  Cancel index </description> </item></list>
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
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NoReason</term><description> 
    ##  No reason </description> </item><item><term> 
    ## ActivateReason</term><description> 
    ##  Activate reason </description> </item><item><term> 
    ## ValueChangedReason</term><description> 
    ##  Value changed reason </description> </item><item><term> 
    ## DragReason</term><description> 
    ##  Drag reason </description> </item><item><term> 
    ## DoubleClickReason</term><description> 
    ##  Double click reason </description> </item><item><term> 
    ## OkReason</term><description> 
    ##  Ok reason </description> </item><item><term> 
    ## ApplyReason</term><description> 
    ##  Apply reason </description> </item><item><term> 
    ## BackReason</term><description> 
    ##  BAck reason </description> </item><item><term> 
    ## CancelReason</term><description> 
    ##  Cancel reason </description> </item><item><term> 
    ## ConstructReason</term><description> 
    ##  Construct reason </description> </item><item><term> 
    ## DestructReason</term><description> 
    ##  Destruct reason </description> </item><item><term> 
    ## FileopReason</term><description> 
    ##  File operation reason </description> </item><item><term> 
    ## SwitchReason</term><description> 
    ##  Switch reason </description> </item><item><term> 
    ## FileOperationReason</term><description> 
    ##  File operation reason </description> </item><item><term> 
    ## ExitFileOperationReason</term><description> 
    ##  Exit file operation reason </description> </item></list>
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
    def Dispose(self) -> None:
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
    def GetReason(self) -> StylerEvent.Reason:
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
    def GetStylerItem(self) -> StylerItem:
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
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## InvalidType</term><description> 
    ##  Invalid item </description> </item><item><term> 
    ## ActionButton</term><description> 
    ##  Action Button item </description> </item><item><term> 
    ## Dialog</term><description> 
    ##  Dialog item </description> </item><item><term> 
    ## RadioBox</term><description> 
    ##  Radio Box item </description> </item><item><term> 
    ## Real</term><description> 
    ##  Real item </description> </item><item><term> 
    ## ScaleReal</term><description> 
    ##  Real Scale item </description> </item><item><term> 
    ## Bitmap</term><description> 
    ##  Bitmap item </description> </item><item><term> 
    ## RowColumn</term><description> 
    ##  Row Column item </description> </item><item><term> 
    ## ButtonLayout</term><description> 
    ##  Button Layout item </description> </item><item><term> 
    ## ScrolledWindow</term><description> 
    ##  Scrolled Window item </description> </item><item><term> 
    ## ColorTool</term><description> 
    ##  Color Item </description> </item><item><term> 
    ## SelectionBox</term><description> 
    ##  Section Box item </description> </item><item><term> 
    ## Separator</term><description> 
    ##  Separator item </description> </item><item><term> 
    ## SingleSelectionList</term><description> 
    ##  Single Selection List item </description> </item><item><term> 
    ## String</term><description> 
    ##  String item </description> </item><item><term> 
    ## BeginGroup</term><description> 
    ##  Begin Group item </description> </item><item><term> 
    ## Integer</term><description> 
    ##  Integer item </description> </item><item><term> 
    ## ScaleInteger</term><description> 
    ##  Scale item </description> </item><item><term> 
    ## MultiList</term><description> 
    ##  Multi List item </description> </item><item><term> 
    ## Label</term><description> 
    ##  Label item </description> </item><item><term> 
    ## MultiLineText</term><description> 
    ##  Multi-line text item </description> </item><item><term> 
    ## TabControl</term><description> 
    ##  Tab Control item </description> </item><item><term> 
    ## OptionMenu</term><description> 
    ##  Option Menu item </description> </item><item><term> 
    ## Toggle</term><description> 
    ##  Toggle item </description> </item><item><term> 
    ## OptionToggle</term><description> 
    ##  Option Toggle item </description> </item><item><term> 
    ## ToolPalette</term><description> 
    ##  Tool Palette item </description> </item><item><term> 
    ## WideString</term><description> 
    ##  Wide String item </description> </item><item><term> 
    ## PropertyPage</term><description> 
    ##  Property Page item </description> </item><item><term> 
    ## CollapsibleGroup</term><description> 
    ##  Callapsible Group item </description> </item></list>
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
    def Dispose(self) -> None:
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
    def GetItemType(self) -> StylerItem.ItemType:
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
    def InitializeAttachment(self) -> Attachment:
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
    ## 
    ## <param name="item_to_compare"> (@link StylerItem NXOpen.UIStyler.StylerItem@endlink)  styler item to compare</param>
    def IsEqualTo(self, item_to_compare: StylerItem) -> bool:
        """
         Equates two styler items 
         @return is_equal (bool): .
        """
        pass
    
    ## Specifies the updated dialog item attachment information 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="attachment"> (@link Attachment NXOpen.UIStyler.Attachment@endlink) attachment object</param>
    def SetAttachment(self, attachment: Attachment) -> None:
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
    ## <param name="dialog_name"> (str)  Dialog name </param>
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
    ##  Returns the page switch data  
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
         Returns the page switch data  
            
         
        """
        pass
    
    ## Getter for property: (bool) Sensitivity
    ##  Returns the sensitivity of the dialog item   
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
         Returns the sensitivity of the dialog item   
            
         
        """
        pass
    
    ## Setter for property: (bool) Sensitivity

    ##  Returns the sensitivity of the dialog item   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
         Returns the sensitivity of the dialog item   
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##  Returns the visibility of the dialog item  
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
         Returns the visibility of the dialog item  
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##  Returns the visibility of the dialog item  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility of the dialog item  
            
         
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
    ## <param name="switchevent"> (@link TabControl.SwitchHandler NXOpen.UIStyler.TabControl.SwitchHandler@endlink)  </param>
    ## <param name="is_dialog_launching_event"> (bool)  </param>
    def AddSwitchHandler(self, switchevent: TabControl.SwitchHandler, is_dialog_launching_event: bool) -> None:
        """
        Registers switch callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ##  Sets focus 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def SetFocus(self) -> None:
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
    ##  Returns an item value   
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
         Returns an item value   
            
         
        """
        pass
    
    ## Setter for property: (bool) ItemValue

    ##  Returns an item value   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ItemValue.setter
    def ItemValue(self, item_val: bool):
        """
        Setter for property: (bool) ItemValue
         Returns an item value   
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##  Returns the visibility of the toggle  
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
         Returns the visibility of the toggle  
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##  Returns the visibility of the toggle  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility of the toggle  
            
         
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
    ## 
    ## <param name="valuechangedevent"> (@link Toggle.ValueChanged NXOpen.UIStyler.Toggle.ValueChanged@endlink)  Value changed event </param>
    ## <param name="is_dialog_launching_event"> (bool)  True if launch any dialog else False </param>
    def AddValueChangedHandler(self, valuechangedevent: Toggle.ValueChanged, is_dialog_launching_event: bool) -> None:
        """
        Registers value change callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ##  Gets the sensitivity 
    ##  @return type (bool):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetSensitivity(self) -> bool:
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
    def SetDefaultAction(self) -> None:
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
    def SetFocus(self) -> None:
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
    ## <param name="str_label"> (str)  </param>
    def SetLabel(self, str_label: str) -> None:
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
    ## <param name="subitem_index"> (int)  </param>
    ## <param name="type"> (bool)  </param>
    def SetSensitivity(self, subitem_index: int, type: bool) -> None:
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
    ##  Returns the currently selected choice for this dialog item.  
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
         Returns the currently selected choice for this dialog item.  
            
         
        """
        pass
    
    ## Setter for property: (int) ItemValue

    ##  Returns the currently selected choice for this dialog item.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ItemValue.setter
    def ItemValue(self, item_val: int):
        """
        Setter for property: (int) ItemValue
         Returns the currently selected choice for this dialog item.  
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##  Returns the visibility of the dialog item  
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
         Returns the visibility of the dialog item  
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##  Returns the visibility of the dialog item  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility of the dialog item  
            
         
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
    ## <param name="activateevent"> (@link ToolPalette.Activate NXOpen.UIStyler.ToolPalette.Activate@endlink)  </param>
    ## <param name="is_dialog_launching_event"> (bool)  </param>
    def AddActivateHandler(self, activateevent: ToolPalette.Activate, is_dialog_launching_event: bool) -> None:
        """
        Registers activate callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ##  Gets the sensitivity of the dialog item
    ##  @return type (bool):  True if sensitivity is set otherwise False .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetSensitivity(self) -> bool:
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
    ## <param name="dialog_id"> (int)  </param>
    def SetDefault(self, dialog_id: int) -> None:
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
    ## 
    ## <param name="str_label"> (str)  String label </param>
    def SetLabel(self, str_label: str) -> None:
        """
         Specifies descriptive text to display for the dialog item. 
            It should describe the dialog item's intended use. 
        """
        pass
    
    ##  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="subitem_index"> (int)  Sub item index </param>
    ## <param name="type"> (bool)  True if sentivity is set otherwise False </param>
    def SetSensitivity(self, subitem_index: int, type: bool) -> None:
        """
         
        """
        pass
    
##  Represents a WideString for UI Styler 
## 
##   <br>  Created in NX5.0.0  <br> 

class WideString(StylerItem): 
    """ Represents a WideString for UI Styler """


    ## Getter for property: (str) ItemValue
    ##  Returns the string value for this dialog item.  
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
         Returns the string value for this dialog item.  
          
             It can be the initial value that is programmatically defined, or interactively entered by the user.   
         
        """
        pass
    
    ## Setter for property: (str) ItemValue

    ##  Returns the string value for this dialog item.  
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
         Returns the string value for this dialog item.  
          
             It can be the initial value that is programmatically defined, or interactively entered by the user.   
         
        """
        pass
    
    ## Getter for property: (bool) Sensitivity
    ##  Returns the sensitivity of the wide string  
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
         Returns the sensitivity of the wide string  
            
         
        """
        pass
    
    ## Setter for property: (bool) Sensitivity

    ##  Returns the sensitivity of the wide string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
         Returns the sensitivity of the wide string  
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##  Returns the visibility of the wide string  
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
         Returns the visibility of the wide string  
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##  Returns the visibility of the wide string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility of the wide string  
            
         
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
    ## <param name="activateevent"> (@link WideString.Activate NXOpen.UIStyler.WideString.Activate@endlink)  </param>
    ## <param name="is_dialog_launching_event"> (bool)  </param>
    def AddActivateHandler(self, activateevent: WideString.Activate, is_dialog_launching_event: bool) -> None:
        """
        Registers activate callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
        """
        pass
    
    ##  Indicates that this dialog item is receiving keyboard focus.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def SetFocus(self) -> None:
        """
         Indicates that this dialog item is receiving keyboard focus.
        """
        pass
    
    ##  Specifies descriptive text to display for the dialog item. 
    ##     It should describe the dialog item's intended use
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="str_label"> (str)  Label string </param>
    def SetLabel(self, str_label: str) -> None:
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


