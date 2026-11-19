from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class Attachment(NXOpen.TransientObject): 
    """ Represents an Attachment for UI Styler """
    class AttachType(Enum):
        """
        Members Include: 
         |Dialog|  Dialog type 
         |Default|  Default type  
         |NotSet|  None type 
         |NoChange|  No change type 
         |Item|  Item type 

        """
        Dialog: int
        Default: int
        NotSet: int
        NoChange: int
        Item: int
        @staticmethod
        def ValueOf(value: int) -> Attachment.AttachType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. 
             After this method is called, it is illegal to use the object.  
             In .NET or Java, this method is automatically called when 
             the object is deleted by the garbage collector. 
        """
        pass
    def SetAttachTypeLeft(self, attach_type_left: Attachment.AttachType) -> None:
        """
         Sets the attach type left
        """
        pass
    def SetAttachTypeRight(self, attach_type_right: Attachment.AttachType) -> None:
        """
         Sets the attach type right
        """
        pass
    def SetAttachTypeTop(self, attach_type_top: Attachment.AttachType) -> None:
        """
         Sets the attach type top
        """
        pass
    def SetCenter(self, is_center: bool) -> None:
        """
         Sets whether the dialog item is at the center
        """
        pass
    def SetLeftDialogItem(self, left_item_identifire: str) -> None:
        """
         Sets the left dialog item
        """
        pass
    def SetLeftOffset(self, offset_left: int) -> None:
        """
         Sets the left offset
        """
        pass
    def SetRightDialogItem(self, right_item_identifire: str) -> None:
        """
         Sets the right dialog item
        """
        pass
    def SetRightOffset(self, offset_right: int) -> None:
        """
         Sets the right offset
        """
        pass
    def SetTopDialogItem(self, top_item_identifire: str) -> None:
        """
         Sets the top dialog item
        """
        pass
    def SetTopOffset(self, offset_top: int) -> None:
        """
         Sets the top offset
        """
        pass
class BitMap(StylerItem): 
    """ Represents a Bit Map for UI Styler. """
    def SetBitmap(self, bitmap: str) -> None:
        """
         Sets the bitmap filename. The filename extension must be: .UBM, .XPM, or .BMP.
            The bitmap can be of any size.
        """
        pass
class ButtonLayout(StylerItem): 
    """ Represents a Button Layout for UI Styler. """
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         Returns the visibility   
            
         
        """
        pass
    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility   
            
         
        """
        pass
    Activate = Callable[[StylerEvent], None]
    def AddActivateHandler(self, activateevent: ButtonLayout.Activate, is_dialog_launching_event: bool) -> None:
        """
        Registers activate callback. This method should be called before calling  UIStyler.Dialog.Show  or  UIStyler.Dialog.RegisterWithUiMenu  
        """
        pass
    def GetSelectedIndexValue(self) -> int:
        """
         Gets selected index 
         Returns value (int):  .
        """
        pass
    def GetSensitivity(self) -> bool:
        """
         Gets the sensitivity 
         Returns type (bool):  .
        """
        pass
    def SetDefaultAction(self) -> None:
        """
         Sets default action 
        """
        pass
    def SetSensitivity(self, subitem_index: int, type: bool) -> None:
        """
         Sets the sensitivity 
        """
        pass
class CollapsibleGroup(StylerItem): 
    """ Represents a Collapsible Group for UI Styler """
    @property
    def CollapseState(self) -> bool:
        """
        Getter for property: (bool) CollapseState
         Returnsthe collapse-state  
            
         
        """
        pass
    @CollapseState.setter
    def CollapseState(self, item_val: bool):
        """
        Setter for property: (bool) CollapseState
         Returnsthe collapse-state  
            
         
        """
        pass
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         Returnsthe visibility  
            
         
        """
        pass
    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returnsthe visibility  
            
         
        """
        pass
    def SetLabel(self, str_label: str) -> None:
        """
        Sets label of collapsible group
        """
        pass
class ColorTool(StylerItem): 
    """ Represents a ColorTool for UI Styler. """
    @property
    def ItemValue(self) -> int:
        """
        Getter for property: (int) ItemValue
         Returns the item value   
            
         
        """
        pass
    @ItemValue.setter
    def ItemValue(self, item_val: int):
        """
        Setter for property: (int) ItemValue
         Returns the item value   
            
         
        """
        pass
    @property
    def Sensitivity(self) -> bool:
        """
        Getter for property: (bool) Sensitivity
         Returns the sensitivity   
            
         
        """
        pass
    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
         Returns the sensitivity   
            
         
        """
        pass
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         Returns the visibility   
            
         
        """
        pass
    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility   
            
         
        """
        pass
    ValueChanged = Callable[[StylerEvent], None]
    def AddValueChangedHandler(self, valuechangedevent: ColorTool.ValueChanged, is_dialog_launching_event: bool) -> None:
        """
        Registers value change callback. This method should be called before calling  UIStyler.Dialog.Show  or  UIStyler.Dialog.RegisterWithUiMenu  
        """
        pass
class DialogIndex(Enum):
    """
    Members Include: 
     |NoSubIndex|  All sub items are selected.

    """
    NoSubIndex: int
    @staticmethod
    def ValueOf(value: int) -> DialogIndex:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class DialogItem(StylerItem): 
    """ Represents a DialogItem for UI Styler. """
    class DialogItemIndex(Enum):
        """
        Members Include: 
         |Ok|  Ok index 
         |Apply|  Apply index 
         |Back|  Back index 
         |Cancel|  Cancel index 

        """
        Ok: int
        Apply: int
        Back: int
        Cancel: int
        @staticmethod
        def ValueOf(value: int) -> DialogItem.DialogItemIndex:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FileOperationData(self) -> FileOperationData:
        """
        Getter for property: ( FileOperationData NXOpen.) FileOperationData
         Returns the file operation data   
            
         
        """
        pass
    Apply = Callable[[StylerEvent], None]
    def AddApplyHandler(self, applyevent: DialogItem.Apply, is_dialog_launching_event: bool) -> None:
        """
        Registers apply callback. This method should be called before calling  UIStyler.Dialog.Show  or  UIStyler.Dialog.RegisterWithUiMenu  
        """
        pass
    Back = Callable[[StylerEvent], None]
    def AddBackHandler(self, backevent: DialogItem.Back, is_dialog_launching_event: bool) -> None:
        """
        Registers back callback. This method should be called before calling  UIStyler.Dialog.Show  or  UIStyler.Dialog.RegisterWithUiMenu  
        """
        pass
    Cancel = Callable[[StylerEvent], None]
    def AddCancelHandler(self, cancelevent: DialogItem.Cancel, is_dialog_launching_event: bool) -> None:
        """
        Registers cancel callback. This method should be called before calling  UIStyler.Dialog.Show  or  UIStyler.Dialog.RegisterWithUiMenu  
        """
        pass
    Construct = Callable[[StylerEvent], None]
    def AddConstructHandler(self, constructevent: DialogItem.Construct, is_dialog_launching_event: bool) -> None:
        """
        Registers construct callback. This method should be called before calling  UIStyler.Dialog.Show  or  UIStyler.Dialog.RegisterWithUiMenu  
        """
        pass
    Destruct = Callable[[StylerEvent], None]
    def AddDestructHandler(self, destructevent: DialogItem.Destruct, is_dialog_launching_event: bool) -> None:
        """
        Registers destruct callback. This method should be called before calling  UIStyler.Dialog.Show  or  UIStyler.Dialog.RegisterWithUiMenu  
        """
        pass
    FileOperation = Callable[[StylerEvent], None]
    def AddFileOperationHandler(self, fileoperationevent: DialogItem.FileOperation, is_dialog_launching_event: bool) -> None:
        """
        Registers file operation callback. This method should be called before calling  UIStyler.Dialog.Show  or  UIStyler.Dialog.RegisterWithUiMenu  
        """
        pass
    Okay = Callable[[StylerEvent], None]
    def AddOkayHandler(self, okayevent: DialogItem.Okay, is_dialog_launching_event: bool) -> None:
        """
        Registers ok callback. This method should be called before calling  UIStyler.Dialog.Show  or  UIStyler.Dialog.RegisterWithUiMenu  
        """
        pass
    PageSwitch = Callable[[StylerEvent], None]
    def AddPageSwitchHandler(self, switchevent: DialogItem.PageSwitch, is_dialog_launching_event: bool) -> None:
        """
        Registers switch callback. This method should be called before calling  UIStyler.Dialog.Show  or  UIStyler.Dialog.RegisterWithUiMenu  
        """
        pass
    def GetSelectionHandle(self) -> NXOpen.SelectionHandle:
        """
         Gets the selection handle for a given dialog item
         Returns select ( NXOpen.SelectionHandle): Selection handle .
        """
        pass
    def SetNavigationSensitivity(self, sub_item_index: DialogItem.DialogItemIndex, type: bool) -> None:
        """
         Specifies the sensitivity of the navigation buttons at the bottom of the dialog. If you set the 
            UF_STYLER_BACK_INDEX button to insensitive at creation time, the system does not show the BACK button; 
            Changing the button's sensitivity while the dialog displays does not show the Back button. 
            
        """
        pass
    def SetResize(self, type: bool) -> None:
        """
        Specifies wether dialog is allowed to resize 
        """
        pass
    def SetSensitivity(self, type: bool) -> None:
        """
        Specifies the sensitivity of the dialog. 
        """
        pass
    def SetTitle(self, str_label: str) -> None:
        """
        Specifies a string to display on the top border of the dialog 
        """
        pass
    def SetWidth(self, width: int) -> None:
        """
        Specifies the pixel width for the dialog. You can only set this attribute when the 
            Dialog Resize attribute is set to TRUE. You cannot enter a negative number. 
        """
        pass
class DialogResponse(Enum):
    """
    Members Include: 
     |PickResponse|  User response was a selection of objects.
     |Ok|  OK button was selected. 
     |Cancel|  Cancel button was selected. 
     |Back|  Back button was selected. 
     |Apply|  Apply button was selected. 
     |Help|  Help button was selected. 
     |ObjectSelected|  Object was selected. 
     |ObjectSelectedByName|  Object was selected by name. 
     |CbTerminate|  Callback routine has terminated. 

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
    @staticmethod
    def ValueOf(value: int) -> DialogResponse:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class DialogState(Enum):
    """
    Members Include: 
     |ContinueDialog|  Continue the dialog 
     |ExitDialog|  Exit from the dialog 

    """
    ContinueDialog: int
    ExitDialog: int
    @staticmethod
    def ValueOf(value: int) -> DialogState:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class Dialog(NXOpen.TransientObject): 
    """ Represents a DialogItem for UI Styler. """
    class ItemType(Enum):
        """
        Members Include: 
         |PushButton|   
         |DialogItem|   
         |RadioBox|   
         |RealItem|   
         |RealScale|   
         |Bitmap|   
         |RowColumn|   
         |ButtonLayout|   
         |ScrolledWindow|   
         |ColorTool|   
         |SelectionBox|   
         |Separator|   
         |SingleSelectList|   
         |StringItem|   
         |GroupBox|   
         |IntegerItem|   
         |IntegerScale|   
         |MultiSelectList|   
         |LabelItem|   
         |MultiTextBox|   
         |TabControl|   
         |OptionMenu|   
         |Toggle|   
         |OptionToggle|   
         |ToolPalette|   
         |WideString|   
         |PropertyPage|   
         |CollapsibleGroup|   

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
        @staticmethod
        def ValueOf(value: int) -> Dialog.ItemType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
            is called, it is illegal to use the object.  In .NET or Java, this 
            method is automatically called when the object is deleted by the 
            garbage collector. 
        """
        pass
    def GetBitmap(self, item_identifier: str) -> BitMap:
        """
         Gets the dialog item with specified item identifier 
         Returns item ( BitMap NXOpen.):  .
        """
        pass
    def GetButtonLayout(self, item_identifier: str) -> ButtonLayout:
        """
         Gets the dialog item with specified item identifier 
         Returns item ( ButtonLayout NXOpen.):  .
        """
        pass
    def GetCollapsibleGroup(self, item_identifier: str) -> CollapsibleGroup:
        """
         Gets the dialog item with specified item identifier 
         Returns item ( CollapsibleGroup NXOpen.):  .
        """
        pass
    def GetColorTool(self, item_identifier: str) -> ColorTool:
        """
         Gets the dialog item with specified item identifier 
         Returns item ( ColorTool NXOpen.):  .
        """
        pass
    def GetDialogIndex(self, item_identifier: str) -> DialogItem:
        """
         Gets the dialog item with specified item identifier 
         Returns item ( DialogItem NXOpen.):  .
        """
        pass
    def GetDialogItemUsingSelectionHandle(self, select: NXOpen.SelectionHandle) -> StylerItem:
        """
         Gets the dialog item for a selection handle 
         Returns item ( StylerItem NXOpen.):  .
        """
        pass
    def GetGroupBox(self, item_identifier: str) -> GroupBox:
        """
         Gets the dialog item with specified item identifier 
         Returns item ( GroupBox NXOpen.):  .
        """
        pass
    def GetIntegerItem(self, item_identifier: str) -> IntegerItem:
        """
         Gets the dialog item with specified item identifier 
         Returns item ( IntegerItem NXOpen.):  .
        """
        pass
    def GetIntegerScale(self, item_identifier: str) -> IntegerScale:
        """
         Gets the dialog item with specified item identifier 
         Returns item ( IntegerScale NXOpen.):  .
        """
        pass
    def GetLabelItem(self, item_identifier: str) -> LabelItem:
        """
         Gets the dialog item with specified item identifier 
         Returns item ( LabelItem NXOpen.):  .
        """
        pass
    def GetMultiSelectList(self, item_identifier: str) -> MultiSelectList:
        """
         Gets the dialog item with specified item identifier 
         Returns item ( MultiSelectList NXOpen.):  .
        """
        pass
    def GetMultiTextBox(self, item_identifier: str) -> MultiTextBox:
        """
         Gets the dialog item with specified item identifier 
         Returns item ( MultiTextBox NXOpen.):  .
        """
        pass
    def GetOptionMenu(self, item_identifier: str) -> OptionMenu:
        """
         Gets the dialog item with specified item identifier 
         Returns item ( OptionMenu NXOpen.):  .
        """
        pass
    def GetOptionToggle(self, item_identifier: str) -> OptionToggle:
        """
         Gets the dialog item with specified item identifier 
         Returns item ( OptionToggle NXOpen.):  .
        """
        pass
    def GetPropertyPage(self, item_identifier: str) -> PropertyPage:
        """
         Gets the dialog item with specified item identifier 
         Returns item ( PropertyPage NXOpen.):  .
        """
        pass
    def GetPushButton(self, item_identifier: str) -> PushButton:
        """
         Gets the dialog item with specified item identifier 
         Returns item ( PushButton NXOpen.):  .
        """
        pass
    def GetRadioBox(self, item_identifier: str) -> RadioBox:
        """
         Gets the dialog item with specified item identifier 
         Returns item ( RadioBox NXOpen.):  .
        """
        pass
    def GetRealItem(self, item_identifier: str) -> RealItem:
        """
         Gets the dialog item with specified item identifier 
         Returns item ( RealItem NXOpen.):  .
        """
        pass
    def GetRealScale(self, item_identifier: str) -> RealScale:
        """
         Gets the dialog item with specified item identifier 
         Returns item ( RealScale NXOpen.):  .
        """
        pass
    def GetRowColumn(self, item_identifier: str) -> RowColumn:
        """
         Gets the dialog item with specified item identifier 
         Returns item ( RowColumn NXOpen.):  .
        """
        pass
    def GetScrolledWindow(self, item_identifier: str) -> ScrolledWindow:
        """
         Gets the dialog item with specified item identifier 
         Returns item ( ScrolledWindow NXOpen.):  .
        """
        pass
    def GetSelectionBox(self, item_identifier: str) -> SelectionBox:
        """
         Gets the dialog item with specified item identifier 
         Returns item ( SelectionBox NXOpen.):  .
        """
        pass
    def GetSeparator(self, item_identifier: str) -> Separator:
        """
         Gets the dialog item with specified item identifier 
         Returns item ( Separator NXOpen.):  .
        """
        pass
    def GetSingleSelectList(self, item_identifier: str) -> SingleSelectList:
        """
         Gets the dialog item with specified item identifier 
         Returns item ( SingleSelectList NXOpen.):  .
        """
        pass
    def GetStringItem(self, item_identifier: str) -> StringItem:
        """
         Gets the dialog item with specified item identifier 
         Returns item ( StringItem NXOpen.):  .
        """
        pass
    def GetStylerItem(self, item_identifier: str, type: Dialog.ItemType) -> StylerItem:
        """
         Gets the dialog item with specified item identifier 
         Returns item ( StylerItem NXOpen.):  .
        """
        pass
    def GetTabControl(self, item_identifier: str) -> TabControl:
        """
         Gets the dialog item with specified item identifier 
         Returns item ( TabControl NXOpen.):  .
        """
        pass
    def GetToggle(self, item_identifier: str) -> Toggle:
        """
         Gets the dialog item with specified item identifier 
         Returns item ( Toggle NXOpen.):  .
        """
        pass
    def GetToolPalette(self, item_identifier: str) -> ToolPalette:
        """
         Gets the dialog item with specified item identifier 
         Returns item ( ToolPalette NXOpen.):  .
        """
        pass
    def GetWideString(self, item_identifier: str) -> WideString:
        """
         Gets the dialog item with specified item identifier 
         Returns item ( WideString NXOpen.):  .
        """
        pass
    def RegisterWithUiMenu(self, is_top_dialog: bool) -> None:
        """
         Registers the dialog with a menu item.
        """
        pass
    def Show(self) -> DialogResponse:
        """
         Displays an NX (UIStyler generated) "bottom" dialog.  This dialog 
                is displayed to NX. Show Method can only be called once for the 
                dialog object.Once show method is called UIStyler.Dialog.GetStylerItem 
                will create any item
            
         Returns response ( DialogResponse NXOpen.): .
        """
        pass
import NXOpen
class FileOperationData(NXOpen.TransientObject): 
    """ Represents a FileOperationData for UI Styler """
    class FileOperationState(Enum):
        """
        Members Include: 
         |Enter|  Enter file state 
         |Exit|  Exit file state 

        """
        Enter: int
        Exit: int
        @staticmethod
        def ValueOf(value: int) -> FileOperationData.FileOperationState:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FileOperationType(Enum):
        """
        Members Include: 
         |New|  New file operation 
         |Open|  Open file operation 
         |Save|  Save file operation 
         |SaveAs|  Save as file operation 
         |SaveAll|  Save all file operation 
         |Close|  Close file operation 
         |Quit|  Quit file operation 
         |SaveAndExit|  Save and Exit file operation 
         |ChangePart|  Chaneg part file operation 
         |Execute|  Execute file operation 
         |Reopen|  Reopen file operation 
         |SaveAllAndClose|  Save all and close file operation 
         |SaveAndClose|  Save and close file operation 
         |SaveAsAndClose|  Save as and close file operation 

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
        @staticmethod
        def ValueOf(value: int) -> FileOperationData.FileOperationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def State(self) -> FileOperationData.FileOperationState:
        """
        Getter for property: ( FileOperationData.FileOperationState NXOpen.) State
         Returns the state   
            
         
        """
        pass
    @property
    def Type(self) -> FileOperationData.FileOperationType:
        """
        Getter for property: ( FileOperationData.FileOperationType NXOpen.) Type
         Returns the file operation type   
            
         
        """
        pass
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
            is called, it is illegal to use the object.  In .NET or Java, this 
            method is automatically called when the object is deleted by the 
            garbage collector. 
        """
        pass
class GroupBox(StylerItem): 
    """ Represents a GroupBox for UI Styler. """
    @property
    def Sensitivity(self) -> bool:
        """
        Getter for property: (bool) Sensitivity
         Returns the sensitivity   
            
         
        """
        pass
    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
         Returns the sensitivity   
            
         
        """
        pass
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         Returns the visibility   
            
         
        """
        pass
    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility   
            
         
        """
        pass
    def SetLabel(self, str_label: str) -> None:
        """
         
        """
        pass
class IntegerItem(StylerItem): 
    """ Represents a Integer for UI Styler. """
    @property
    def ItemValue(self) -> int:
        """
        Getter for property: (int) ItemValue
         Returnsthe value obtained from the text field.  
            
         
        """
        pass
    @ItemValue.setter
    def ItemValue(self, item_val: int):
        """
        Setter for property: (int) ItemValue
         Returnsthe value obtained from the text field.  
            
         
        """
        pass
    @property
    def Sensitivity(self) -> bool:
        """
        Getter for property: (bool) Sensitivity
         Returns the sensitivity of Integer item   
            
         
        """
        pass
    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
         Returns the sensitivity of Integer item   
            
         
        """
        pass
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         Returns the visibility of the dialog item.  
            
         
        """
        pass
    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility of the dialog item.  
            
         
        """
        pass
    Activate = Callable[[StylerEvent], None]
    def AddActivateHandler(self, activateevent: IntegerItem.Activate, is_dialog_launching_event: bool) -> None:
        """
        Registers activate callback. This method should be called before calling  UIStyler.Dialog.Show  or  UIStyler.Dialog.RegisterWithUiMenu  
        """
        pass
    def SetBitmap(self, bitmap: str) -> None:
        """
        Specifies a filename that contains a bitmap definition. The filename must contain a UBM, XPM, or BMP 
            extension. When you use this field, the system displays a bitmap for this dialog item instead of a text 
            label. When a bitmap is present, the system uses the text label as tooltip text when a user places the 
            mouse cursor over the bitmap. We recommend that you use a 16x16 bitmap for this dialog item. 
            
        """
        pass
    def SetFocus(self) -> None:
        """
         Sets focus 
        """
        pass
    def SetLabel(self, str_label: str) -> None:
        """
        Specifies descriptive text to display for the dialog item. It should describe the dialog 
            item's intended use. If you specify a bitmap for this dialog item, it uses this text as tooltip text. 
        """
        pass
class IntegerScale(StylerItem): 
    """ Represents a IntegerScale for UI Styler """
    @property
    def ItemValue(self) -> int:
        """
        Getter for property: (int) ItemValue
         Returns   
            
         
        """
        pass
    @ItemValue.setter
    def ItemValue(self, item_val: int):
        """
        Setter for property: (int) ItemValue
         Returns   
            
         
        """
        pass
    @property
    def Sensitivity(self) -> bool:
        """
        Getter for property: (bool) Sensitivity
         Returns the sensitivity of the dialog item.  
             
         
        """
        pass
    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
         Returns the sensitivity of the dialog item.  
             
         
        """
        pass
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         Returnsthe visibility of the dialog item.  
             
         
        """
        pass
    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returnsthe visibility of the dialog item.  
             
         
        """
        pass
    Drag = Callable[[StylerEvent], None]
    def AddDragHandler(self, dragevent: IntegerScale.Drag, is_dialog_launching_event: bool) -> None:
        """
        Registers drag callback. This method should be called before calling  UIStyler.Dialog.Show  or  UIStyler.Dialog.RegisterWithUiMenu  
        """
        pass
    ValueChanged = Callable[[StylerEvent], None]
    def AddValueChangedHandler(self, valuechangedevent: IntegerScale.ValueChanged, is_dialog_launching_event: bool) -> None:
        """
        Registers value change callback. This method should be called before calling  UIStyler.Dialog.Show  or  UIStyler.Dialog.RegisterWithUiMenu  
        """
        pass
    def SetLabels(self, minimum_label: str, maximum_label: str) -> None:
        """
        Specifies the text for the minimum and maximum label. By default, the system uses the maximumminimum 
            value as a text label.
        """
        pass
    def SetLimits(self, minimum_value: int, maximum_value: int) -> None:
        """
        Specifies the scale's maximum and minimum value.
        """
        pass
class LabelItem(StylerItem): 
    """ Represents a Label for UI Styler. """
    @property
    def Sensitivity(self) -> bool:
        """
        Getter for property: (bool) Sensitivity
         Returns the seisitivity of the dialog item  
            
         
        """
        pass
    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
         Returns the seisitivity of the dialog item  
            
         
        """
        pass
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         Returns the visibility of the dialog item  
            
         
        """
        pass
    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility of the dialog item  
            
         
        """
        pass
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
    def SetLabel(self, str_label: str) -> None:
        """
         Specifies descriptive text to display for the dialog item. It should describe the dialog item's intended use.
        """
        pass
class MultiSelectList(StylerItem): 
    """ Represents a MultiSelectList for UI Styler """
    @property
    def Sensitivity(self) -> bool:
        """
        Getter for property: (bool) Sensitivity
         Returns the senstivity   
            
         
        """
        pass
    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
         Returns the senstivity   
            
         
        """
        pass
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         Returnsthe visibility  
            
         
        """
        pass
    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returnsthe visibility  
            
         
        """
        pass
    Activate = Callable[[StylerEvent], None]
    def AddActivateHandler(self, activateevent: MultiSelectList.Activate, is_dialog_launching_event: bool) -> None:
        """
        Called when a dialog user selects an entry with a double mouse click or presses Return on 
            a selected item. 
        """
        pass
    DoubleClick = Callable[[StylerEvent], None]
    def AddDoubleClickHandler(self, doubleclickevent: MultiSelectList.DoubleClick, is_dialog_launching_event: bool) -> None:
        """
        Registers double click callback. This method should be called before calling  UIStyler.Dialog.Show  or  UIStyler.Dialog.RegisterWithUiMenu  
        """
        pass
    def Append(self, multi_entries: List[str]) -> None:
        """
         Appends one or more entries to be inserted into the list 
        """
        pass
    def DeleteSubitem(self, subItemIndex: int) -> None:
        """
         Deletes sub item 
        """
        pass
    def Deselect(self, subItemIndex: int) -> None:
        """
        Requests a list entry to be deselected.
            
        """
        pass
    def Focus(self) -> None:
        """
         Indicates that this dialog item is receiving keyboard focus.
            
        """
        pass
    def GetAllIndicesSelected(self) -> List[int]:
        """
        Gets the indices of all selected list entries. 
         Returns indices (List[int]):  An array of integers for item indices of selected items .
        """
        pass
    def GetAllNameSelected(self) -> List[str]:
        """
        Gets the names of all selected list entries. 
         Returns names (List[str]):  An array of character strings of selected items.
        """
        pass
    def GetListItems(self) -> List[str]:
        """
         Gets an array of character strings for item names that are used as selectable choices for this 
            dialog item.
         Returns item_val (List[str]):  An array of character strings for item names.
        """
        pass
    def InsertSubitems(self, subitem_index: int, multi_entries: List[str]) -> None:
        """
         
        """
        pass
    def SetAllSelected(self) -> None:
        """
        Specifies all list entry to be selected.
        """
        pass
    def SetListItems(self, item_val: List[str]) -> None:
        """
        Specifies an array of character strings for item names that are used as selectable choices for this 
            dialog item.
            
        """
        pass
    def SetSelected(self, subIndex: int) -> None:
        """
        Specifies particular list items to be selected.
        """
        pass
    def ShowSubItem(self, subItemIndex: int) -> None:
        """
         Requests a list entry to be scrolled up to the first line in the list 
        """
        pass
class MultiTextBox(StylerItem): 
    """ Represents a MultiTextBox for UI Styler. """
    @property
    def Sensitivity(self) -> bool:
        """
        Getter for property: (bool) Sensitivity
         Returnsthe sensitivity of the dialog item.  
             
         
        """
        pass
    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
         Returnsthe sensitivity of the dialog item.  
             
         
        """
        pass
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         Returns the visibility of the dialog item   
            
         
        """
        pass
    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility of the dialog item   
            
         
        """
        pass
    def GetItemValues(self) -> List[str]:
        """
        Specifies the text for this dialog item. It can be programmatically get by APIs. 
         Returns item_val (List[str]):  to get array of strings.
        """
        pass
    def SetFocus(self) -> None:
        """
        Indicates that this dialog item is receiving keyboard focus.
        """
        pass
    def SetItemValues(self, values: List[str]) -> None:
        """
        Specifies the text for this dialog item. It can be programmatically set by APIs supported in 
            different laguages,or interactively entered by the user. 
        """
        pass
    def SetLabel(self, str_label: str) -> None:
        """
        Specifies descriptive text to display for the dialog item. It should describe the dialog item's 
            intended use.
        """
        pass
class OptionMenu(StylerItem): 
    """ Represents a OptionMenu for UI Styler. """
    @property
    def ItemValue(self) -> int:
        """
        Getter for property: (int) ItemValue
         Returns the item value   
            
         
        """
        pass
    @ItemValue.setter
    def ItemValue(self, item_val: int):
        """
        Setter for property: (int) ItemValue
         Returns the item value   
            
         
        """
        pass
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         Returns the visibility   
            
         
        """
        pass
    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility   
            
         
        """
        pass
    Activate = Callable[[StylerEvent], None]
    def AddActivateHandler(self, activateevent: OptionMenu.Activate, is_dialog_launching_event: bool) -> None:
        """
        Registers activate callback. This method should be called before calling  UIStyler.Dialog.Show  or  UIStyler.Dialog.RegisterWithUiMenu  
        """
        pass
    def GetBitmap(self) -> List[str]:
        """
         Returns an array of bitmaps 
         Returns bitmaps (List[str]):  .
        """
        pass
    def GetItems(self) -> List[str]:
        """
         Returns an array if items 
         Returns list_entries (List[str]): .
        """
        pass
    def GetSensitivity(self) -> bool:
        """
         Gets the sensitivity 
         Returns type (bool):  .
        """
        pass
    def SetBitmap(self, bitmaps: List[str]) -> None:
        """
         Set an array of bitmap filenames 
        """
        pass
    def SetItems(self, str_list_array: List[str]) -> None:
        """
         Set an array of items 
        """
        pass
    def SetLabel(self, str_label: str) -> None:
        """
         Sets label 
        """
        pass
    def SetSensitivity(self, subitem_index: int, type: bool) -> None:
        """
         Sets the sensitivity 
        """
        pass
class OptionToggle(StylerItem): 
    """ Represents a OptionToggle for UI Styler """
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         Returns the visibility   
            
         
        """
        pass
    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility   
            
         
        """
        pass
    Activate = Callable[[StylerEvent], None]
    def AddActivateHandler(self, activateevent: OptionToggle.Activate, is_dialog_launching_event: bool) -> None:
        """
        Registers activate callback. This method should be called before calling  UIStyler.Dialog.Show  or  UIStyler.Dialog.RegisterWithUiMenu  
        """
        pass
    ValueChanged = Callable[[StylerEvent], None]
    def AddValueChangedHandler(self, valuechangedevent: OptionToggle.ValueChanged, is_dialog_launching_event: bool) -> None:
        """
        Registers value change callback. This method should be called before calling  UIStyler.Dialog.Show  or  UIStyler.Dialog.RegisterWithUiMenu  
        """
        pass
    def GetItemValue(self) -> Tuple[int, bool]:
        """
         Returns item value 
         Returns A tuple consisting of (item_val, set_check). 
         - item_val is: int. Item value .
         - set_check is: bool. .

        """
        pass
    def GetItems(self) -> List[str]:
        """
         Returns the items 
         Returns list_entries (List[str]):  An array of items .
        """
        pass
    def GetSensitivity(self) -> bool:
        """
         Returns the sesitivity 
         Returns type (bool):  .
        """
        pass
    def SetBitmaps(self, bitmaps: List[str]) -> None:
        """
         Set bitmaps 
        """
        pass
    def SetDefaultAction(self) -> None:
        """
         Sets default action 
        """
        pass
    def SetItemValue(self, subitem_index: int, set_check: bool) -> None:
        """
         Sets item value 
        """
        pass
    def SetItems(self, str_list_array: List[str]) -> None:
        """
         Sets items in the array 
        """
        pass
    def SetLabel(self, str_label: str) -> None:
        """
         Sets label 
        """
        pass
    def SetSensitivity(self, subitem_index: int, type: bool) -> None:
        """
         Set the sesitivity 
        """
        pass
import NXOpen
class PageSwitchData(NXOpen.TransientObject): 
    """ Represents a PageSwitchData for UI Styler """
    @property
    def ActivatedPage(self) -> int:
        """
        Getter for property: (int) ActivatedPage
         Returns the activated page   
            
         
        """
        pass
    @property
    def DeactivatedPage(self) -> int:
        """
        Getter for property: (int) DeactivatedPage
         Returns the deactivated page   
            
         
        """
        pass
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
            is called, it is illegal to use the object.  In .NET or Java, this 
            method is automatically called when the object is deleted by the 
            garbage collector. 
        """
        pass
class PropertyPage(StylerItem): 
    """ Represents a PropertyPage for UI Styler """
    @property
    def Sensitivity(self) -> bool:
        """
        Getter for property: (bool) Sensitivity
         Returns the sensitivity of property page.  
             
         
        """
        pass
    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
         Returns the sensitivity of property page.  
             
         
        """
        pass
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         Returnsthe visibility of the dialog item.  
             
         
        """
        pass
    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returnsthe visibility of the dialog item.  
             
         
        """
        pass
    def SetFocus(self) -> None:
        """
         Sets focus 
        """
        pass
    def SetLabel(self, str_label: str) -> None:
        """
        Specifies descriptive text to display for the dialog item. It should describe the dialog item's intended use. 
            If you specify a bitmap for this dialog item, it uses this text as tooltip text. 
        """
        pass
class PushButton(StylerItem): 
    """ Represents a PushButton for UI Styler """
    @property
    def Sensitivity(self) -> bool:
        """
        Getter for property: (bool) Sensitivity
         Returns the senstivity of dialog.  
            
         
        """
        pass
    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
         Returns the senstivity of dialog.  
            
         
        """
        pass
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         Returns the visibility of dialog.  
              
         
        """
        pass
    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility of dialog.  
              
         
        """
        pass
    Activate = Callable[[StylerEvent], None]
    def AddActivateHandler(self, activateevent: PushButton.Activate, is_dialog_launching_event: bool) -> None:
        """
        Registers activate callback. This method should be called before calling  UIStyler.Dialog.Show  or  UIStyler.Dialog.RegisterWithUiMenu  
        """
        pass
    def SetBitmap(self, bitmap: str) -> None:
        """
        Specifies a filename that contains a bitmap definition. The filename must contain a UBM, XPM, or BMP 
            extension. When you use this field, the system displays a bitmap for this dialog item instead of a text 
            label. When a bitmap is present, the system uses the text label as a popup hint when a user places the 
            mouse cursor over the bitmap.  
        """
        pass
    def SetDefaultAction(self) -> None:
        """
         Sets default action 
        """
        pass
    def SetFocus(self) -> None:
        """
        Indicates that this dialog item is receiving keyboard focus. 
        """
        pass
    def SetLabel(self, str_label: str) -> None:
        """
        Specifies descriptive text to display for the dialog item. It should describe the dialog item's intended 
            use. If you specify a bitmap for this dialog item, it uses this text as tooltip text.  
        """
        pass
class RadioBox(StylerItem): 
    """ Represents a RadioBox for UI Styler """
    @property
    def ItemValue(self) -> int:
        """
        Getter for property: (int) ItemValue
         Returns the item value   
            
         
        """
        pass
    @ItemValue.setter
    def ItemValue(self, item_val: int):
        """
        Setter for property: (int) ItemValue
         Returns the item value   
            
         
        """
        pass
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         Returns the visibility   
            
         
        """
        pass
    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility   
            
         
        """
        pass
    ValueChanged = Callable[[StylerEvent], None]
    def AddValueChangedHandler(self, valuechangedevent: RadioBox.ValueChanged, is_dialog_launching_event: bool) -> None:
        """
        Registers value change callback. This method should be called before calling  UIStyler.Dialog.Show  or  UIStyler.Dialog.RegisterWithUiMenu  
        """
        pass
    def GetSensitivity(self) -> bool:
        """
         Gets the sensitivity 
         Returns type (bool):  .
        """
        pass
    def SetDefaultAction(self) -> None:
        """
         Set default action 
        """
        pass
    def SetLabel(self, str_label: str) -> None:
        """
         Sets label 
        """
        pass
    def SetSensitivity(self, subitem_index: int, type: bool) -> None:
        """
         Sets the sensitivity 
        """
        pass
class RealItem(StylerItem): 
    """ Represents a Real for UI Styler """
    @property
    def ItemValue(self) -> float:
        """
        Getter for property: (float) ItemValue
         Returns the item value   
            
         
        """
        pass
    @ItemValue.setter
    def ItemValue(self, item_val: float):
        """
        Setter for property: (float) ItemValue
         Returns the item value   
            
         
        """
        pass
    @property
    def Sensitivity(self) -> bool:
        """
        Getter for property: (bool) Sensitivity
         Returns the sensitivity   
            
         
        """
        pass
    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
         Returns the sensitivity   
            
         
        """
        pass
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         Returns the visibility   
            
         
        """
        pass
    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility   
            
         
        """
        pass
    Activate = Callable[[StylerEvent], None]
    def AddActivateHandler(self, activateevent: RealItem.Activate, is_dialog_launching_event: bool) -> None:
        """
        Registers activate callback. This method should be called before calling  UIStyler.Dialog.Show  or  UIStyler.Dialog.RegisterWithUiMenu  
        """
        pass
    def SetBitmap(self, str_bitmap: str) -> None:
        """
         
        """
        pass
    def SetFocus(self) -> None:
        """
         Sets focus 
        """
        pass
    def SetLabel(self, str_label: str) -> None:
        """
         Set the label 
        """
        pass
class RealScale(StylerItem): 
    """ Represents a RealScale for UI Styler """
    @property
    def ItemValue(self) -> float:
        """
        Getter for property: (float) ItemValue
         Returns the item value   
            
         
        """
        pass
    @ItemValue.setter
    def ItemValue(self, item_val: float):
        """
        Setter for property: (float) ItemValue
         Returns the item value   
            
         
        """
        pass
    @property
    def Sensitivity(self) -> bool:
        """
        Getter for property: (bool) Sensitivity
         Returns the sensitivity   
            
         
        """
        pass
    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
         Returns the sensitivity   
            
         
        """
        pass
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         Returns the visibility   
            
         
        """
        pass
    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility   
            
         
        """
        pass
    Drag = Callable[[StylerEvent], None]
    def AddDragHandler(self, dragevent: RealScale.Drag, is_dialog_launching_event: bool) -> None:
        """
        Registers dtag callback. This method should be called before calling  UIStyler.Dialog.Show  or  UIStyler.Dialog.RegisterWithUiMenu  
        """
        pass
    ValueChanged = Callable[[StylerEvent], None]
    def AddValueChangedHandler(self, valuechangedevent: RealScale.ValueChanged, is_dialog_launching_event: bool) -> None:
        """
        Called when a dialog user moves the slider up and down the scale. 
            For example, if a user moves the slider from 0.0 to 10.0, 
            the dialog calls the drag callback 100 times, one for each value that the slider moves across. 
            Do not terminate the dialog with a drag callback. The dialog should always return UF_UI_CB_CONTINUE_DIALOG.
        """
        pass
    def SetDecimalPrecision(self, digits: int) -> None:
        """
         Sets decimal precision 
        """
        pass
    def SetLabels(self, minimum_label: str, maximum_label: str) -> None:
        """
         Sets labels 
        """
        pass
    def SetLimits(self, minimum_value: float, maximum_value: float) -> None:
        """
         Sets limits 
        """
        pass
class RowColumn(StylerItem): 
    """ Represents a RowColumn for UI Styler """
    @property
    def Sensitivity(self) -> bool:
        """
        Getter for property: (bool) Sensitivity
         Returns the sensitivity   
            
         
        """
        pass
    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
         Returns the sensitivity   
            
         
        """
        pass
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         Returns the visibility   
            
         
        """
        pass
    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility   
            
         
        """
        pass
class ScrolledWindow(StylerItem): 
    """ Represents a ScrolledWindow for UI Styler """
    @property
    def Sensitivity(self) -> bool:
        """
        Getter for property: (bool) Sensitivity
         Returns   
            
         
        """
        pass
    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
         Returns   
            
         
        """
        pass
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         Returns   
            
         
        """
        pass
    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns   
            
         
        """
        pass
class SelectionBox(StylerItem): 
    """ Represents a SelectionBox for UI Styler """
    @property
    def Sensitivity(self) -> bool:
        """
        Getter for property: (bool) Sensitivity
         Returns the sensitivity of the selection box  
            
         
        """
        pass
    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
         Returns the sensitivity of the selection box  
            
         
        """
        pass
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         Returns the visibility of the selection box  
            
         
        """
        pass
    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility of the selection box  
            
         
        """
        pass
    Activate = Callable[[StylerEvent], None]
    def AddActivateHandler(self, activateevent: SelectionBox.Activate, is_dialog_launching_event: bool) -> None:
        """
        Registers activate callback. This method should be called before calling  UIStyler.Dialog.Show  or  UIStyler.Dialog.RegisterWithUiMenu  
        """
        pass
    DoubleClick = Callable[[StylerEvent], None]
    def AddDoubleClickHandler(self, doubleclickevent: SelectionBox.DoubleClick, is_dialog_launching_event: bool) -> None:
        """
        Registers double click callback. This method should be called before calling UIStyler.Dialog.Show  or  UIStyler.Dialog.RegisterWithUiMenu  
        """
        pass
    def Append(self, multi_entries: List[str]) -> None:
        """
         Appends one or more entries to be inserted into the list 
        """
        pass
    def DeleteSubItem(self, subItemIndex: int) -> None:
        """
         Deletes sub item 
        """
        pass
    def DeselectSubItem(self, subItemIndex: int) -> None:
        """
         Requests a list entry to be deselected.
        """
        pass
    def GetListItems(self) -> List[str]:
        """
         Gets an array of character strings for item names that are used as selectable choices for this dialog item.
         Returns values (List[str]):  List of items .
        """
        pass
    def GetSelectedIndexValue(self) -> int:
        """
         Gets selected index value 
         Returns value (int):  .
        """
        pass
    def GetSelectedString(self) -> str:
        """
         Gets selected string 
         Returns value (str):  .
        """
        pass
    def InsertSubItem(self, subitem_index: int, multi_entries: List[str]) -> None:
        """
         Requests that one or more entries be inserted into the list. You can insert entries at the bottom of the list or at any position within the list.
        """
        pass
    def SetFocus(self) -> None:
        """
         Indicates that this dialog item is receiving keyboard focus. 
        """
        pass
    def SetLabel(self, str_label: str) -> None:
        """
         Specifies the descriptive text string to display below the scrolled list and above the text field. It describes the dialog item's usage.
        """
        pass
    def SetListItems(self, values: List[str]) -> None:
        """
         Specifies an array of character strings for item names that are used as selectable choices for this dialog item.
        """
        pass
    def SetValue(self, value: int) -> None:
        """
         Sets the value 
        """
        pass
    def ShowSubItem(self, subItemIndex: int) -> None:
        """
         Requests that a list entry be scrolled up to the first line in the list. 
        """
        pass
class Separator(StylerItem): 
    """ Represents a Separator for UI Styler """
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         Returns the visibility of the separator  
            
         
        """
        pass
    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility of the separator  
            
         
        """
        pass
class SingleSelectList(StylerItem): 
    """ Represents a SingleSelectList for UI Styler """
    @property
    def Sensitivity(self) -> bool:
        """
        Getter for property: (bool) Sensitivity
         Returns the sensitivity of the single select list  
            
         
        """
        pass
    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
         Returns the sensitivity of the single select list  
            
         
        """
        pass
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         Returns the visibility of the single select list  
            
         
        """
        pass
    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility of the single select list  
            
         
        """
        pass
    Activate = Callable[[StylerEvent], None]
    def AddActivateHandler(self, activateevent: SingleSelectList.Activate, is_dialog_launching_event: bool) -> None:
        """
        Registers activate callback. This method should be called before calling  UIStyler.Dialog.Show  or  UIStyler.Dialog.RegisterWithUiMenu  
        """
        pass
    DoubleClick = Callable[[StylerEvent], None]
    def AddDoubleClickHandler(self, doubleclickevent: SingleSelectList.DoubleClick, is_dialog_launching_event: bool) -> None:
        """
        Registers double click callback. This method should be called before calling  UIStyler.Dialog.Show  or  UIStyler.Dialog.RegisterWithUiMenu  
        """
        pass
    def Append(self, multi_entries: List[str]) -> None:
        """
         Appends one or more entries to be inserted into the list 
        """
        pass
    def DeleteSubItem(self, subItemIndex: int) -> None:
        """
         Requests a list entry to be deleted. 
        """
        pass
    def DeselectSubItem(self, subItemIndex: int) -> None:
        """
         Requests a list entry to be deselected.
        """
        pass
    def GetListItems(self) -> List[str]:
        """
         Gets an array of character strings that are used as entries in the list.
         Returns item_val (List[str]):  An array of string items .
        """
        pass
    def GetSelectedIndexValue(self) -> int:
        """
         Gets selected index 
         Returns value (int):  .
        """
        pass
    def GetSelectedString(self) -> str:
        """
         Gets selected string 
         Returns value (str):  .
        """
        pass
    def HasSelected(self) -> bool:
        """
         Returns whether or not an item has been selected 
         Returns selected (bool):  .
        """
        pass
    def InsertSubItem(self, subitem_index: int, multi_entries: List[str]) -> None:
        """
         Requests one or more entries to be inserted into the list. You can insert entries at the bottom of the list or at any position within the list. 
        """
        pass
    def SetFocus(self) -> None:
        """
         Indicates that this dialog item is receiving keyboard focus. 
        """
        pass
    def SetListItems(self, item_val: List[str]) -> None:
        """
         Specifies an array of character strings that are used as entries in the list 
        """
        pass
    def SetSelected(self, subIndex: int) -> None:
        """
         Specifies particular list items to be selected 
        """
        pass
    def ShowSubItem(self, subItemIndex: int) -> None:
        """
        Requests that a list entry be scrolled up to the first line in the list 
        """
        pass
class StringItem(StylerItem): 
    """ Represents a StringItem for UI Styler. """
    @property
    def ItemValue(self) -> str:
        """
        Getter for property: (str) ItemValue
         Returns the string value for this dialog item.  
           It can be the initial value that is programmatically 
            defined, or interactively entered by the user.  
         
        """
        pass
    @ItemValue.setter
    def ItemValue(self, item_val: str):
        """
        Setter for property: (str) ItemValue
         Returns the string value for this dialog item.  
           It can be the initial value that is programmatically 
            defined, or interactively entered by the user.  
         
        """
        pass
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         Returns the visibility of the dialog item   
            
         
        """
        pass
    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility of the dialog item   
            
         
        """
        pass
    Activate = Callable[[StylerEvent], None]
    def AddActivateHandler(self, activateevent: StringItem.Activate, is_dialog_launching_event: bool) -> None:
        """
        Registers activate callback. This method should be called before calling  UIStyler.Dialog.Show  or  UIStyler.Dialog.RegisterWithUiMenu  
        """
        pass
    def GetSensitivity(self) -> bool:
        """
         To get senstivity of string control
         Returns type (bool):  TRUE if sensitive, FALSE if insensitive .
        """
        pass
    def SetBitmap(self, str_bitmap: str) -> None:
        """
        Specifies a filename that contains a bitmap definition. The filename must contain a UBM, XPM, or BMP 
            extension. When you use this field, the system displays a bitmap for this dialog item instead of a text 
            label. When a bitmap is present, the system uses the text label as tooltip text when a user places the 
            mouse cursor over the bitmap. We recommend that you use a 16x16 bitmap for this dialog item.  
        """
        pass
    def SetFocus(self) -> None:
        """
         Indicates that this dialog item is receiving keyboard focus 
        """
        pass
    def SetLabel(self, str_label: str) -> None:
        """
        Specifies descriptive text to display for the dialog item. 
            It should describe the dialog item's intended use. If you specify a bitmap for this dialog item, 
                it uses this text as tooltip text.
            
        """
        pass
    def SetSensitivity(self, type: bool) -> None:
        """
        Specifies the sensitivity of the dialog item. When you set sensitivity to False, it grays out the 
            dialog item. This indicates that the dialog item exists but is not active.
        """
        pass
import NXOpen
class StylerEvent(NXOpen.TransientObject): 
    """ Represents a StylerEvent """
    class Indicator(Enum):
        """
        Members Include: 
         |NoValue|  No value 
         |StringValue|  String value 
         |StringPointerValue|  String pointer value 
         |IntegerValue|  Integer value 
         |IntegerPointerValue|  Integer pointer value 
         |RealValue|  Real value 
         |RealPointerValue|  Real pointer value 
         |SelectionValue|  Selection value 
         |OptionToggleValue|  Option toggle value 

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
        @staticmethod
        def ValueOf(value: int) -> StylerEvent.Indicator:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Miscellaneous(Enum):
        """
        Members Include: 
         |NoSubIndex|  No sub index 
         |OkIndex|  Ok index 
         |ApplyIndex|  Apply index 
         |BackIndex|  Back index 
         |CancelIndex|  Cancel index 

        """
        NoSubIndex: int
        OkIndex: int
        ApplyIndex: int
        BackIndex: int
        CancelIndex: int
        @staticmethod
        def ValueOf(value: int) -> StylerEvent.Miscellaneous:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Reason(Enum):
        """
        Members Include: 
         |NoReason|  No reason 
         |ActivateReason|  Activate reason 
         |ValueChangedReason|  Value changed reason 
         |DragReason|  Drag reason 
         |DoubleClickReason|  Double click reason 
         |OkReason|  Ok reason 
         |ApplyReason|  Apply reason 
         |BackReason|  BAck reason 
         |CancelReason|  Cancel reason 
         |ConstructReason|  Construct reason 
         |DestructReason|  Destruct reason 
         |FileopReason|  File operation reason 
         |SwitchReason|  Switch reason 
         |FileOperationReason|  File operation reason 
         |ExitFileOperationReason|  Exit file operation reason 

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
        @staticmethod
        def ValueOf(value: int) -> StylerEvent.Reason:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
            is called, it is illegal to use the object.  In .NET or Java, this 
            method is automatically called when the object is deleted by the 
            garbage collector. 
        """
        pass
    def GetReason(self) -> StylerEvent.Reason:
        """
        Gets the reason for the event
         Returns reason ( StylerEvent.Reason NXOpen.):  Reason .
        """
        pass
    def GetStylerItem(self) -> StylerItem:
        """
         Gets the dialog item
         Returns item ( StylerItem NXOpen.):  .
        """
        pass
import NXOpen
class StylerItem(NXOpen.TransientObject): 
    """ Represents a Styler Item """
    class ItemType(Enum):
        """
        Members Include: 
         |InvalidType|  Invalid item 
         |ActionButton|  Action Button item 
         |Dialog|  Dialog item 
         |RadioBox|  Radio Box item 
         |Real|  Real item 
         |ScaleReal|  Real Scale item 
         |Bitmap|  Bitmap item 
         |RowColumn|  Row Column item 
         |ButtonLayout|  Button Layout item 
         |ScrolledWindow|  Scrolled Window item 
         |ColorTool|  Color Item 
         |SelectionBox|  Section Box item 
         |Separator|  Separator item 
         |SingleSelectionList|  Single Selection List item 
         |String|  String item 
         |BeginGroup|  Begin Group item 
         |Integer|  Integer item 
         |ScaleInteger|  Scale item 
         |MultiList|  Multi List item 
         |Label|  Label item 
         |MultiLineText|  Multi-line text item 
         |TabControl|  Tab Control item 
         |OptionMenu|  Option Menu item 
         |Toggle|  Toggle item 
         |OptionToggle|  Option Toggle item 
         |ToolPalette|  Tool Palette item 
         |WideString|  Wide String item 
         |PropertyPage|  Property Page item 
         |CollapsibleGroup|  Callapsible Group item 

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
        @staticmethod
        def ValueOf(value: int) -> StylerItem.ItemType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
            is called, it is illegal to use the object.  In .NET or Java, this 
            method is automatically called when the object is deleted by the 
            garbage collector. 
        """
        pass
    def GetItemType(self) -> StylerItem.ItemType:
        """
         Gets the dialog item type. User can write programs to query this attribute and determine the 
            type of a dialog item in order to determine what further actions should be taken.
         Returns item_type ( StylerItem.ItemType NXOpen.): .
        """
        pass
    def InitializeAttachment(self) -> Attachment:
        """
         Returns initialized dialog item attachment information 
         Returns attachment ( Attachment NXOpen.): attachment object.
        """
        pass
    def IsEqualTo(self, item_to_compare: StylerItem) -> bool:
        """
         Equates two styler items 
         Returns is_equal (bool): .
        """
        pass
    def SetAttachment(self, attachment: Attachment) -> None:
        """
        Specifies the updated dialog item attachment information 
        """
        pass
import NXOpen
class Styler(NXOpen.Object): 
    """ Represents a Uistyler for UI Styler """
    def CreateStylerDialog(dialog_name: str) -> Dialog:
        """
        Creates an NX (UIStyler generated) "bottom" dialog. The ".dlg" file can only be generated from the 
            Open UIStyler. 
         Returns dialog ( Dialog NXOpen.):  .
        """
        pass
class TabControl(StylerItem): 
    """ Represents a Tab Control for UI Styler. """
    @property
    def PageSwitchData(self) -> PageSwitchData:
        """
        Getter for property: ( PageSwitchData NXOpen.) PageSwitchData
         Returns the page switch data  
            
         
        """
        pass
    @property
    def Sensitivity(self) -> bool:
        """
        Getter for property: (bool) Sensitivity
         Returns the sensitivity of the dialog item   
            
         
        """
        pass
    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
         Returns the sensitivity of the dialog item   
            
         
        """
        pass
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         Returns the visibility of the dialog item  
            
         
        """
        pass
    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility of the dialog item  
            
         
        """
        pass
    SwitchHandler = Callable[[StylerEvent], None]
    def AddSwitchHandler(self, switchevent: TabControl.SwitchHandler, is_dialog_launching_event: bool) -> None:
        """
        Registers switch callback. This method should be called before calling  UIStyler.Dialog.Show  or  UIStyler.Dialog.RegisterWithUiMenu  
        """
        pass
    def SetFocus(self) -> None:
        """
         Sets focus 
        """
        pass
class Toggle(StylerItem): 
    """ Represents a Toggle for UI Styler. """
    @property
    def ItemValue(self) -> bool:
        """
        Getter for property: (bool) ItemValue
         Returns an item value   
            
         
        """
        pass
    @ItemValue.setter
    def ItemValue(self, item_val: bool):
        """
        Setter for property: (bool) ItemValue
         Returns an item value   
            
         
        """
        pass
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         Returns the visibility of the toggle  
            
         
        """
        pass
    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility of the toggle  
            
         
        """
        pass
    ValueChanged = Callable[[StylerEvent], None]
    def AddValueChangedHandler(self, valuechangedevent: Toggle.ValueChanged, is_dialog_launching_event: bool) -> None:
        """
        Registers value change callback. This method should be called before calling  UIStyler.Dialog.Show  or  UIStyler.Dialog.RegisterWithUiMenu  
        """
        pass
    def GetSensitivity(self) -> bool:
        """
         Gets the sensitivity 
         Returns type (bool):  .
        """
        pass
    def SetDefaultAction(self) -> None:
        """
         Indicates that this dialog item should override the accelerator 
            on the second mouse button, which normally accelerates to the OK button. 
            When you set this attribute, a click on the second mouse button triggers 
            this dialog item's ONOFF state and calls the Value Changed callback 
            instead of the action of the OK button.
        """
        pass
    def SetFocus(self) -> None:
        """
         Indicates that this dialog item is receiving keyboard focus. 
        """
        pass
    def SetLabel(self, str_label: str) -> None:
        """
         Sets the label to display on the right side of the toggle button. 
            If the toggle button displays a bitmap, then this text label is used as a popup hint instead
        """
        pass
    def SetSensitivity(self, subitem_index: int, type: bool) -> None:
        """
         Sets the sensitivity of the toggle button 
        """
        pass
class ToolPalette(StylerItem): 
    """ Represents a ToolPalette for UI Styler """
    @property
    def ItemValue(self) -> int:
        """
        Getter for property: (int) ItemValue
         Returns the currently selected choice for this dialog item.  
            
         
        """
        pass
    @ItemValue.setter
    def ItemValue(self, item_val: int):
        """
        Setter for property: (int) ItemValue
         Returns the currently selected choice for this dialog item.  
            
         
        """
        pass
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         Returns the visibility of the dialog item  
            
         
        """
        pass
    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility of the dialog item  
            
         
        """
        pass
    Activate = Callable[[StylerEvent], None]
    def AddActivateHandler(self, activateevent: ToolPalette.Activate, is_dialog_launching_event: bool) -> None:
        """
        Registers activate callback. This method should be called before calling  UIStyler.Dialog.Show  or  UIStyler.Dialog.RegisterWithUiMenu  
        """
        pass
    def GetSensitivity(self) -> bool:
        """
         Gets the sensitivity of the dialog item
         Returns type (bool):  True if sensitivity is set otherwise False .
        """
        pass
    def SetDefault(self, dialog_id: int) -> None:
        """
         Indicates that this dialog item should override the accelerator 
            on the second mouse button, which normally accelerates to the OK button. 
            When you set this attribute, a click on the second mouse button triggers
            this dialog item's Activate callback instead of the action of the OK button.
        """
        pass
    def SetLabel(self, str_label: str) -> None:
        """
         Specifies descriptive text to display for the dialog item. 
            It should describe the dialog item's intended use. 
        """
        pass
    def SetSensitivity(self, subitem_index: int, type: bool) -> None:
        """
         
        """
        pass
class WideString(StylerItem): 
    """ Represents a WideString for UI Styler """
    @property
    def ItemValue(self) -> str:
        """
        Getter for property: (str) ItemValue
         Returns the string value for this dialog item.  
          
             It can be the initial value that is programmatically defined, or interactively entered by the user.   
         
        """
        pass
    @ItemValue.setter
    def ItemValue(self, item_val: str):
        """
        Setter for property: (str) ItemValue
         Returns the string value for this dialog item.  
          
             It can be the initial value that is programmatically defined, or interactively entered by the user.   
         
        """
        pass
    @property
    def Sensitivity(self) -> bool:
        """
        Getter for property: (bool) Sensitivity
         Returns the sensitivity of the wide string  
            
         
        """
        pass
    @Sensitivity.setter
    def Sensitivity(self, type: bool):
        """
        Setter for property: (bool) Sensitivity
         Returns the sensitivity of the wide string  
            
         
        """
        pass
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         Returns the visibility of the wide string  
            
         
        """
        pass
    @Visibility.setter
    def Visibility(self, type: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility of the wide string  
            
         
        """
        pass
    Activate = Callable[[StylerEvent], None]
    def AddActivateHandler(self, activateevent: WideString.Activate, is_dialog_launching_event: bool) -> None:
        """
        Registers activate callback. This method should be called before calling  UIStyler.Dialog.Show  or  UIStyler.Dialog.RegisterWithUiMenu  
        """
        pass
    def SetFocus(self) -> None:
        """
         Indicates that this dialog item is receiving keyboard focus.
        """
        pass
    def SetLabel(self, str_label: str) -> None:
        """
         Specifies descriptive text to display for the dialog item. 
            It should describe the dialog item's intended use
        """
        pass
