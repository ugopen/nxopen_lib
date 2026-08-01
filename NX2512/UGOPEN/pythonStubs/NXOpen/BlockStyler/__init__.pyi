from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class AngularDimension(UIBlock): 
    """ Represents a Angular Dimension block"""
    @property
    def AdaptiveScaleLimits(self) -> bool:
        """
        Getter for property: (bool) AdaptiveScaleLimits
         Returnsthe AdaptiveScaleLimits.  
          
                If true, indicates that the scale should be adaptive. Only available when WithScale is set to true.  
         
        """
        pass
    @AdaptiveScaleLimits.setter
    def AdaptiveScaleLimits(self, scale_limits: bool):
        """
        Setter for property: (bool) AdaptiveScaleLimits
         Returnsthe AdaptiveScaleLimits.  
          
                If true, indicates that the scale should be adaptive. Only available when WithScale is set to true.  
         
        """
        pass
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @property
    def ExpressionObject(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) ExpressionObject
         Returns the ExpressionObject  
            
         
        """
        pass
    @ExpressionObject.setter
    def ExpressionObject(self, expression_obj: NXOpen.TaggedObject):
        """
        Setter for property: ( NXOpen.TaggedObject) ExpressionObject
         Returns the ExpressionObject  
            
         
        """
        pass
    @property
    def Formula(self) -> str:
        """
        Getter for property: (str) Formula
         Returns the Formula  
            
         
        """
        pass
    @Formula.setter
    def Formula(self, formula: str):
        """
        Setter for property: (str) Formula
         Returns the Formula  
            
         
        """
        pass
    @property
    def HandleFixedSizeFlag(self) -> bool:
        """
        Getter for property: (bool) HandleFixedSizeFlag
         Returns the HandleFixedSizeFlag  
            
         
        """
        pass
    @HandleFixedSizeFlag.setter
    def HandleFixedSizeFlag(self, handle_flag: bool):
        """
        Setter for property: (bool) HandleFixedSizeFlag
         Returns the HandleFixedSizeFlag  
            
         
        """
        pass
    @property
    def HandleOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) HandleOrigin
         Returns the HandleOrigin  
            
         
        """
        pass
    @HandleOrigin.setter
    def HandleOrigin(self, handle_orogin: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) HandleOrigin
         Returns the HandleOrigin  
            
         
        """
        pass
    @property
    def HandleRadius(self) -> float:
        """
        Getter for property: (float) HandleRadius
         Returns the HandleRadius  
            
         
        """
        pass
    @HandleRadius.setter
    def HandleRadius(self, handle_radius: float):
        """
        Setter for property: (float) HandleRadius
         Returns the HandleRadius  
            
         
        """
        pass
    @property
    def HandleRadiusOffset(self) -> float:
        """
        Getter for property: (float) HandleRadiusOffset
         Returns the HandleRadiusOffset  
            
         
        """
        pass
    @HandleRadiusOffset.setter
    def HandleRadiusOffset(self, radius_offset: float):
        """
        Setter for property: (float) HandleRadiusOffset
         Returns the HandleRadiusOffset  
            
         
        """
        pass
    @property
    def HandleXAxis(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) HandleXAxis
         Returns the HandleXAxis  
            
         
        """
        pass
    @HandleXAxis.setter
    def HandleXAxis(self, handle_x_axis: NXOpen.Vector3d):
        """
        Setter for property: ( NXOpen.Vector3d) HandleXAxis
         Returns the HandleXAxis  
            
         
        """
        pass
    @property
    def HandleZAxis(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) HandleZAxis
         Returns the HandleZAxis  
            
         
        """
        pass
    @HandleZAxis.setter
    def HandleZAxis(self, handle_z_axis: NXOpen.Vector3d):
        """
        Setter for property: ( NXOpen.Vector3d) HandleZAxis
         Returns the HandleZAxis  
            
         
        """
        pass
    @property
    def LineIncrement(self) -> float:
        """
        Getter for property: (float) LineIncrement
         Returnsthe LineIncrement value.  
          
                Specifies the incrementdecrement when the user presses the arrow keys on the keyboard.
                Only available when WithScale is set to true.  
         
        """
        pass
    @LineIncrement.setter
    def LineIncrement(self, line_increment: float):
        """
        Setter for property: (float) LineIncrement
         Returnsthe LineIncrement value.  
          
                Specifies the incrementdecrement when the user presses the arrow keys on the keyboard.
                Only available when WithScale is set to true.  
         
        """
        pass
    @property
    def MaxInclusive(self) -> bool:
        """
        Getter for property: (bool) MaxInclusive
         Returns the MaxInclusive  
            
         
        """
        pass
    @MaxInclusive.setter
    def MaxInclusive(self, max_inclusive: bool):
        """
        Setter for property: (bool) MaxInclusive
         Returns the MaxInclusive  
            
         
        """
        pass
    @property
    def MaximumValue(self) -> float:
        """
        Getter for property: (float) MaximumValue
         Returns the MaximumValue  
            
         
        """
        pass
    @MaximumValue.setter
    def MaximumValue(self, max_value: float):
        """
        Setter for property: (float) MaximumValue
         Returns the MaximumValue  
            
         
        """
        pass
    @property
    def MinInclusive(self) -> bool:
        """
        Getter for property: (bool) MinInclusive
         Returns the MinInclusive  
            
         
        """
        pass
    @MinInclusive.setter
    def MinInclusive(self, min_inclusive: bool):
        """
        Setter for property: (bool) MinInclusive
         Returns the MinInclusive  
            
         
        """
        pass
    @property
    def MinRadius(self) -> float:
        """
        Getter for property: (float) MinRadius
         Returns the MinRadius  
            
         
        """
        pass
    @MinRadius.setter
    def MinRadius(self, min_radius: float):
        """
        Setter for property: (float) MinRadius
         Returns the MinRadius  
            
         
        """
        pass
    @property
    def MinimumValue(self) -> float:
        """
        Getter for property: (float) MinimumValue
         Returns the MinimumValue  
            
         
        """
        pass
    @MinimumValue.setter
    def MinimumValue(self, min_value: float):
        """
        Setter for property: (float) MinimumValue
         Returns the MinimumValue  
            
         
        """
        pass
    @property
    def PageIncrement(self) -> float:
        """
        Getter for property: (float) PageIncrement
         Returnsthe PageIncrement value.  
          
                Specifies the incrementdecrement when the user presses the Page Up or Page Down keys on the keyboard.
                Only available when WithScale is set to true.  
         
        """
        pass
    @PageIncrement.setter
    def PageIncrement(self, page_increment: float):
        """
        Setter for property: (float) PageIncrement
         Returnsthe PageIncrement value.  
          
                Specifies the incrementdecrement when the user presses the Page Up or Page Down keys on the keyboard.
                Only available when WithScale is set to true.  
         
        """
        pass
    @property
    def ShowFocusHandle(self) -> bool:
        """
        Getter for property: (bool) ShowFocusHandle
         Returns the ShowFocusHandle  
            
         
        """
        pass
    @ShowFocusHandle.setter
    def ShowFocusHandle(self, show_focus: bool):
        """
        Setter for property: (bool) ShowFocusHandle
         Returns the ShowFocusHandle  
            
         
        """
        pass
    @property
    def ShowHandle(self) -> bool:
        """
        Getter for property: (bool) ShowHandle
         Returns the ShowHandle  
            
         
        """
        pass
    @ShowHandle.setter
    def ShowHandle(self, show_handle: bool):
        """
        Setter for property: (bool) ShowHandle
         Returns the ShowHandle  
            
         
        """
        pass
    @property
    def SnapPointTypesOnByDefault(self) -> int:
        """
        Getter for property: (int) SnapPointTypesOnByDefault
         Returns the SnapPointTypesOnByDefault  
            
         
        """
        pass
    @SnapPointTypesOnByDefault.setter
    def SnapPointTypesOnByDefault(self, point_type: int):
        """
        Setter for property: (int) SnapPointTypesOnByDefault
         Returns the SnapPointTypesOnByDefault  
            
         
        """
        pass
    @property
    def Units(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) Units
         Returns the Units  
            
         
        """
        pass
    @Units.setter
    def Units(self, units: NXOpen.TaggedObject):
        """
        Setter for property: ( NXOpen.TaggedObject) Units
         Returns the Units  
            
         
        """
        pass
    @property
    def Value(self) -> float:
        """
        Getter for property: (float) Value
         Returns the Value.  
            
         
        """
        pass
    @Value.setter
    def Value(self, dimension_value: float):
        """
        Setter for property: (float) Value
         Returns the Value.  
            
         
        """
        pass
    @property
    def WithScale(self) -> bool:
        """
        Getter for property: (bool) WithScale
         Returns the WithScale  
            
         
        """
        pass
    @WithScale.setter
    def WithScale(self, with_scale: bool):
        """
        Setter for property: (bool) WithScale
         Returns the WithScale  
            
         
        """
        pass
    def GetBalloonTooltipLayoutMembers(self) -> List[str]:
        """
         Gets the BalloonTooltipLayout member 
         Returns layout_strings (List[str]): Value to get from the. .
        """
        pass
    def TestValueChanged(self, dimension_value: float) -> None:
        """
        Tests dimension changed event workflow mapped to this AngularDimension block.
        """
        pass
import NXOpen
class BlockDialog(NXOpen.TransientObject): 
    """ Represents a Dialog """
    class DialogMode(Enum):
        """
        Members Include: 
         |Create|  When the user presses Ok or Apply on the
                    dialog, the user's inputs are saved in dialog memory and the next time that the dialog
                    is shown in Create mode, the dialog is initialized using the user's previous
                    inputs.  
         |Edit|  The Apply button is not shown.  
                    The user's inputs are not saved in dialog memory and the dialog is not initialized 
                    with the user's previous inputs. 

        """
        Create: int
        Edit: int
        @staticmethod
        def ValueOf(value: int) -> BlockDialog.DialogMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DialogResponse(Enum):
        """
        Members Include: 
         |Invalid|  Invalid response. 
         |Ok|  OK button was pressed. 
         |Cancel|  Cancel button was pressed. 
         |Back|  Back button was pressed. 
         |Apply|  Apply button was pressed. 

        """
        Invalid: int
        Ok: int
        Cancel: int
        Back: int
        Apply: int
        @staticmethod
        def ValueOf(value: int) -> BlockDialog.DialogResponse:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def TopBlock(self) -> CompositeBlock:
        """
        Getter for property: ( CompositeBlock NXOpen.B) TopBlock
         Returns a composite block that contains all the blocks in the dialog   
            
         
        """
        pass
    Apply = Callable[[], None]
    def AddApplyHandler(self, apply_cb: BlockDialog.Apply) -> None:
        """
        Adds Apply callback handler to the dialog. 
        """
        pass
    Cancel = Callable[[], None]
    def AddCancelHandler(self, cancel_cb: BlockDialog.Cancel) -> None:
        """
        Adds Cancel callback handler to the dialog.
        """
        pass
    Close = Callable[[], None]
    def AddCloseHandler(self, close_cb: BlockDialog.Close) -> None:
        """
        Adds Close callback handler to the dialog.
        """
        pass
    DialogShown = Callable[[], None]
    def AddDialogShownHandler(self, cb: BlockDialog.DialogShown) -> None:
        """
         Adds Dialog Shown callback handler to the dialog. The callback function is called before the dialog is shown.  The callback can be used to overwrite 
                changes that are made during dialog initialization when user inputs saved in dialog memory are applied to the dialog.
        """
        pass
    EnableOKButton = Callable[[], None]
    def AddEnableOKButtonHandler(self, cb: BlockDialog.EnableOKButton) -> None:
        """
         Adds enable-ok-button callback handler to the dialog. 
        """
        pass
    Filter = Callable[[UIBlock, NXOpen.TaggedObject], None]
    def AddFilterHandler(self, cb: BlockDialog.Filter) -> None:
        """
         Adds Filter callback handler to the dialog. 
        """
        pass
    FocusNotify = Callable[[UIBlock, bool], None]
    def AddFocusNotifyHandler(self, cb: BlockDialog.FocusNotify) -> None:
        """
         Adds focus notify callback handler to the dialog. 
        """
        pass
    Initialize = Callable[[], None]
    def AddInitializeHandler(self, cb: BlockDialog.Initialize) -> None:
        """
         Adds Initialize callback handler to the dialog. The callback function is called while the dialog is being initialized.  The callback is called before applying any user inputs saved in dialog memory.
        """
        pass
    KeyboardFocusNotify = Callable[[UIBlock, bool], None]
    def AddKeyboardFocusNotifyHandler(self, cb: BlockDialog.KeyboardFocusNotify) -> None:
        """
         Adds keyboard focus notify callback handler to the dialog. 
        """
        pass
    Ok = Callable[[], None]
    def AddOkHandler(self, ok_cb: BlockDialog.Ok) -> None:
        """
        Adds Ok callback handler to the dialog. 
        """
        pass
    Update = Callable[[UIBlock], None]
    def AddUpdateHandler(self, cb: BlockDialog.Update) -> None:
        """
         Adds Update callback handler to the dialog. 
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                 it is illegal to use the object.  In .NET, this method is automatically
                 called when the object is deleted by the garbage collector. 
                
        """
        pass
    def GetBlockProperties(self, blockName: str) -> PropertyList:
        """
         Gets the properties of a block 
         Returns propertyList ( PropertyList NXOpen.B): .
        """
        pass
    def Launch(self) -> BlockDialog.DialogResponse:
        """
         Shows the dialog in BlockStyler.BlockDialog.DialogMode.Create mode.  This method will not return until the dialog is closed, 
            which typically is when the dialog's navigation buttons are pressed.
         Returns dialogResponse ( BlockDialog.DialogResponse NXOpen.B): .
        """
        pass
    def LaunchInDialogMode(self, dialogMode: BlockDialog.DialogMode) -> BlockDialog.DialogResponse:
        """
         Shows the dialog based upon the mode specified in 
            BlockStyler.BlockDialog.DialogMode.
            This method will not return until the dialog is closed, which typically is when the dialog's navigation buttons are pressed. 
         Returns dialogResponse ( BlockDialog.DialogResponse NXOpen.B): Returns 1: When Ok is pressed. 2: When Cancel is pressed. 3: When Back is pressed. 4: When Apply is pressed.
        """
        pass
    def PerformApply(self) -> None:
        """
         Performs an Apply and restarts the dialog. This invokes the apply callback on the dialog.  This method is meant to be called
            when the dialog is shown and while inside the update callback.
        """
        pass
    def RegisterUserDefinedUIBlock(self, blockDialog: BlockDialog, blockId: str) -> None:
        """
         Registers the reusable block with the dialog 
        """
        pass
    @overload
    def Show(self) -> NXOpen.Selection.Response:
        """
         Shows the dialog in BlockStyler.BlockDialog.DialogMode.Create mode.  This method will not return until the dialog is closed, 
            which typically is when the dialog's OK or Cancel button is pressed.
         Returns response ( NXOpen.Selection.Response): .
        """
        pass
    @overload
    def Show(self, dialogMode: BlockDialog.DialogMode) -> NXOpen.Selection.Response:
        """
         Shows the dialog based upon the mode specified in 
            BlockStyler.BlockDialog.DialogMode.
            This method will not return until the dialog is closed, which typically is when the dialog's OK or Cancel button is pressed. 
         Returns response ( NXOpen.Selection.Response): Returns 1: When Back is pressed. 2: When Cancel is pressed. 3: When Ok or Apply is pressed.
        """
        pass
import NXOpen
class BodyCollector(UIBlock): 
    """ Represents a Body Collector block"""
    @property
    def AllowConvergentObject(self) -> bool:
        """
        Getter for property: (bool) AllowConvergentObject
         Returns the AllowConvergentObject  
            
         
        """
        pass
    @AllowConvergentObject.setter
    def AllowConvergentObject(self, allowConvergentObject: bool):
        """
        Setter for property: (bool) AllowConvergentObject
         Returns the AllowConvergentObject  
            
         
        """
        pass
    @property
    def AllowConvergentObjectWithMixedGeometries(self) -> bool:
        """
        Getter for property: (bool) AllowConvergentObjectWithMixedGeometries
         Returns the AllowConvergentObjectWithMixedGeometries  
            
         
        """
        pass
    @AllowConvergentObjectWithMixedGeometries.setter
    def AllowConvergentObjectWithMixedGeometries(self, allowConvergentObjectWithMixedGeometries: bool):
        """
        Setter for property: (bool) AllowConvergentObjectWithMixedGeometries
         Returns the AllowConvergentObjectWithMixedGeometries  
            
         
        """
        pass
    @property
    def AutomaticProgression(self) -> bool:
        """
        Getter for property: (bool) AutomaticProgression
         Returns the AutomaticProgression  
            
         
        """
        pass
    @AutomaticProgression.setter
    def AutomaticProgression(self, automaticProgression: bool):
        """
        Setter for property: (bool) AutomaticProgression
         Returns the AutomaticProgression  
            
         
        """
        pass
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @property
    def Bitmap(self) -> str:
        """
        Getter for property: (str) Bitmap
         Returns the Bitmap  
            
         
        """
        pass
    @Bitmap.setter
    def Bitmap(self, bitmap_string: str):
        """
        Setter for property: (str) Bitmap
         Returns the Bitmap  
            
         
        """
        pass
    @property
    def BlendVirtualCurveOverlay(self) -> bool:
        """
        Getter for property: (bool) BlendVirtualCurveOverlay
         Returns the BlendVirtualCurveOverlay  
            
         
        """
        pass
    @BlendVirtualCurveOverlay.setter
    def BlendVirtualCurveOverlay(self, blendCurve: bool):
        """
        Setter for property: (bool) BlendVirtualCurveOverlay
         Returns the BlendVirtualCurveOverlay  
            
         
        """
        pass
    @property
    def BodyRules(self) -> int:
        """
        Getter for property: (int) BodyRules
         Returns the BodyRules  
            
         
        """
        pass
    @BodyRules.setter
    def BodyRules(self, bodyRules: int):
        """
        Setter for property: (int) BodyRules
         Returns the BodyRules  
            
         
        """
        pass
    @property
    def CreateInterpartLink(self) -> bool:
        """
        Getter for property: (bool) CreateInterpartLink
         Returns the CreateInterpartLink  
            
         
        """
        pass
    @CreateInterpartLink.setter
    def CreateInterpartLink(self, createLink: bool):
        """
        Setter for property: (bool) CreateInterpartLink
         Returns the CreateInterpartLink  
            
         
        """
        pass
    @property
    def Cue(self) -> str:
        """
        Getter for property: (str) Cue
         Returns the Cue  
            
         
        """
        pass
    @Cue.setter
    def Cue(self, cue: str):
        """
        Setter for property: (str) Cue
         Returns the Cue  
            
         
        """
        pass
    @property
    def DefaultBodyRulesAsString(self) -> str:
        """
        Getter for property: (str) DefaultBodyRulesAsString
         Returns the DefaultBodyRules as string  
            
         
        """
        pass
    @DefaultBodyRulesAsString.setter
    def DefaultBodyRulesAsString(self, enumString: str):
        """
        Setter for property: (str) DefaultBodyRulesAsString
         Returns the DefaultBodyRules as string  
            
         
        """
        pass
    @property
    def EntityType(self) -> int:
        """
        Getter for property: (int) EntityType
         Returns the EntityType  
            
         
        """
        pass
    @EntityType.setter
    def EntityType(self, entityType: int):
        """
        Setter for property: (int) EntityType
         Returns the EntityType  
            
         
        """
        pass
    @property
    def IncludeSheetBodies(self) -> bool:
        """
        Getter for property: (bool) IncludeSheetBodies
         Returns the IncludeSheetBodies  
            
         
        """
        pass
    @IncludeSheetBodies.setter
    def IncludeSheetBodies(self, includeSheetBodies: bool):
        """
        Setter for property: (bool) IncludeSheetBodies
         Returns the IncludeSheetBodies  
            
         
        """
        pass
    @property
    def InterpartSelectionAsString(self) -> str:
        """
        Getter for property: (str) InterpartSelectionAsString
         Returns the InterpartSelection as string  
            
         
        """
        pass
    @InterpartSelectionAsString.setter
    def InterpartSelectionAsString(self, enumString: str):
        """
        Setter for property: (str) InterpartSelectionAsString
         Returns the InterpartSelection as string  
            
         
        """
        pass
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
         Returns the LabelString  
            
         
        """
        pass
    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
         Returns the LabelString  
            
         
        """
        pass
    @property
    def MaximumScopeAsString(self) -> str:
        """
        Getter for property: (str) MaximumScopeAsString
         Returns the MaximumScope  
            
         
        """
        pass
    @MaximumScopeAsString.setter
    def MaximumScopeAsString(self, enumString: str):
        """
        Setter for property: (str) MaximumScopeAsString
         Returns the MaximumScope  
            
         
        """
        pass
    @property
    def PopupMenuEnabled(self) -> bool:
        """
        Getter for property: (bool) PopupMenuEnabled
         Returns the PopupMenuEnabled.  
          
                If true, displays the popup menu for the body.  
         
        """
        pass
    @PopupMenuEnabled.setter
    def PopupMenuEnabled(self, enabled: bool):
        """
        Setter for property: (bool) PopupMenuEnabled
         Returns the PopupMenuEnabled.  
          
                If true, displays the popup menu for the body.  
         
        """
        pass
    @property
    def SelectModeAsString(self) -> str:
        """
        Getter for property: (str) SelectModeAsString
         Returns the SelectMode as string  
            
         
        """
        pass
    @SelectModeAsString.setter
    def SelectModeAsString(self, enumString: str):
        """
        Setter for property: (str) SelectModeAsString
         Returns the SelectMode as string  
            
         
        """
        pass
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
         Returns the StepStatus as string  
            
         
        """
        pass
    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
         Returns the StepStatus as string  
            
         
        """
        pass
    @property
    def ToolTip(self) -> str:
        """
        Getter for property: (str) ToolTip
         Returns the ToolTip  
            
         
        """
        pass
    @ToolTip.setter
    def ToolTip(self, toolTip: str):
        """
        Setter for property: (str) ToolTip
         Returns the ToolTip  
            
         
        """
        pass
    def GetBalloonTooltipLayoutMembers(self) -> List[str]:
        """
         Gets the BalloonTooltipLayout member 
         Returns layout_strings (List[str]): Value to get from the property. .
        """
        pass
    def GetCollectorObjectOfBodyCollector(self) -> NXOpen.ScCollector:
        """
         Get the collector object
         Returns collectorObject ( NXOpen.ScCollector): .
        """
        pass
    def GetDefaultBodyRulesMembers(self) -> List[str]:
        """
         Gets the DefaultBodyRules members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def GetInterpartSelectionMembers(self) -> List[str]:
        """
         Gets the InterpartSelection members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def GetSelectModeMembers(self) -> List[str]:
        """
         Gets the SelectMode members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def GetSelectedObjects(self) -> List[NXOpen.TaggedObject]:
        """
         Gets the SelectedObjects
         Returns objectVector ( NXOpen.TaggedObject Li): Value to get from the property.
        """
        pass
    def GetStepStatusMembers(self) -> List[str]:
        """
         Gets the StepStatus members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def SetCollectorObjectOfBodyCollector(self, collectorObject: NXOpen.ScCollector) -> None:
        """
         Sets the collector object
        """
        pass
    def SetSelectedObjects(self, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the SelectedObjects
        """
        pass
    def TestSelection(self, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Tests the selection for this block. The block must be in focus to call this API
        """
        pass
class Button(UIBlock): 
    """ Represents a button"""
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @property
    def Bitmap(self) -> str:
        """
        Getter for property: (str) Bitmap
         Returns the Bitmap  
            
         
        """
        pass
    @Bitmap.setter
    def Bitmap(self, bitmap_string: str):
        """
        Setter for property: (str) Bitmap
         Returns the Bitmap  
            
         
        """
        pass
    @property
    def HighQualityBitmap(self) -> bool:
        """
        Getter for property: (bool) HighQualityBitmap
         Returns the HighQualityBitmap  
            
         
        """
        pass
    @HighQualityBitmap.setter
    def HighQualityBitmap(self, high_quality: bool):
        """
        Setter for property: (bool) HighQualityBitmap
         Returns the HighQualityBitmap  
            
         
        """
        pass
    @property
    def Localize(self) -> bool:
        """
        Getter for property: (bool) Localize
         Returns the Localize  
            
         
        """
        pass
    @Localize.setter
    def Localize(self, localize: bool):
        """
        Setter for property: (bool) Localize
         Returns the Localize  
            
         
        """
        pass
    @property
    def Tooltip(self) -> str:
        """
        Getter for property: (str) Tooltip
         Returns the Tooltip  
            
         
        """
        pass
    @Tooltip.setter
    def Tooltip(self, tooltip_string: str):
        """
        Setter for property: (str) Tooltip
         Returns the Tooltip  
            
         
        """
        pass
    def GetBalloonTooltipLayoutMembers(self) -> List[str]:
        """
         Gets the BalloonTooltipLayout member 
         Returns layout_strings (List[str]): Value to get for given name. .
        """
        pass
    def TestAction(self) -> None:
        """
        Tests action event workflow mapped to this Button block.
        """
        pass
import NXOpen
class ChooseExpression(UIBlock): 
    """ Represents Choose Expression block"""
    @property
    def ExpressionSortTypeAsString(self) -> str:
        """
        Getter for property: (str) ExpressionSortTypeAsString
         Returns the ExpressionSortType as string  
            
         
        """
        pass
    @ExpressionSortTypeAsString.setter
    def ExpressionSortTypeAsString(self, enumString: str):
        """
        Setter for property: (str) ExpressionSortTypeAsString
         Returns the ExpressionSortType as string  
            
         
        """
        pass
    @property
    def ExpressionTypeIndexAsString(self) -> str:
        """
        Getter for property: (str) ExpressionTypeIndexAsString
         Returns the ExpressionTypeIndex as string  
            
         
        """
        pass
    @ExpressionTypeIndexAsString.setter
    def ExpressionTypeIndexAsString(self, enumString: str):
        """
        Setter for property: (str) ExpressionTypeIndexAsString
         Returns the ExpressionTypeIndex as string  
            
         
        """
        pass
    @property
    def SelectedExpression(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) SelectedExpression
         Returns the SelectedExpression  
            
         
        """
        pass
    @SelectedExpression.setter
    def SelectedExpression(self, selectedExpression: NXOpen.TaggedObject):
        """
        Setter for property: ( NXOpen.TaggedObject) SelectedExpression
         Returns the SelectedExpression  
            
         
        """
        pass
    def GetExpressionSortTypeMembers(self) -> List[str]:
        """
         Gets the ExpressionSortType members
         Returns member_strings (List[str]): .
        """
        pass
    def GetExpressionTypeIndexMembers(self) -> List[str]:
        """
         Gets the ExpressionTypeIndex members
         Returns member_strings (List[str]): .
        """
        pass
    def TestExpressionSelected(self, selectedExpression: NXOpen.TaggedObject) -> None:
        """
        Tests expression selected.
        """
        pass
import NXOpen
class CompositeBlock(UIBlock): 
    """ A composite block is a block that contains other blocks """
    @property
    def Cue(self) -> str:
        """
        Getter for property: (str) Cue
         Returns the Cue  
            
         
        """
        pass
    @Cue.setter
    def Cue(self, cue: str):
        """
        Setter for property: (str) Cue
         Returns the Cue  
            
         
        """
        pass
    @property
    def DialogSizing(self) -> int:
        """
        Getter for property: (int) DialogSizing
         Returns the Dialog Sizing  
            
         
        """
        pass
    @DialogSizing.setter
    def DialogSizing(self, enumIndex: int):
        """
        Setter for property: (int) DialogSizing
         Returns the Dialog Sizing  
            
         
        """
        pass
    @property
    def DialogSizingAsString(self) -> str:
        """
        Getter for property: (str) DialogSizingAsString
         Returns the Dialog Sizing as string  
            
         
        """
        pass
    @DialogSizingAsString.setter
    def DialogSizingAsString(self, enumString: str):
        """
        Setter for property: (str) DialogSizingAsString
         Returns the Dialog Sizing as string  
            
         
        """
        pass
    @property
    def LastUpdated(self) -> UIBlock:
        """
        Getter for property: ( UIBlock NXOpen.B) LastUpdated
         Returns the block contained in the composite block that was last updated.  
          
            For example, if the CompositeBlock is an item contained in a SetList and
            your update handler is notified that the CompositeBlock has been updated,
            this method returns which block inside the CompositeBlock has been updated.   
         
        """
        pass
    @property
    def NavigationStyle(self) -> int:
        """
        Getter for property: (int) NavigationStyle
         Returns the Navigation Style  
            
         
        """
        pass
    @property
    def NavigationStyleAsString(self) -> str:
        """
        Getter for property: (str) NavigationStyleAsString
         Returns the Navigation Style as string  
            
         
        """
        pass
    def FindBlock(self, block_name: str) -> UIBlock:
        """
         Finds a block contained in the composite block. Returns  if block not present
         Returns block ( UIBlock NXOpen.B):  .
        """
        pass
    def GetBlocks(self) -> List[UIBlock]:
        """
         Gets all the blocks available in the composite block 
         Returns block ( UIBlock List[NXOpen):  .
        """
        pass
    def GetDialogSizingMembers(self) -> List[str]:
        """
         Gets the Dialog Sizing members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def GetNavigationStyleMembers(self) -> List[str]:
        """
         Gets the Navigation Style members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def SetDialogNavigationResponse(self, response: NXOpen.Selection.DialogResponse) -> None:
        """
         Sets the dialog navigation response for testing
        """
        pass
import NXOpen
class CurveCollector(UIBlock): 
    """ Represents a Curve Collector"""
    @property
    def AllowConvergentObject(self) -> bool:
        """
        Getter for property: (bool) AllowConvergentObject
         Returns the AllowConvergentObject  
            
         
        """
        pass
    @AllowConvergentObject.setter
    def AllowConvergentObject(self, allowConvergentObject: bool):
        """
        Setter for property: (bool) AllowConvergentObject
         Returns the AllowConvergentObject  
            
         
        """
        pass
    @property
    def AllowConvergentObjectWithMixedGeometries(self) -> bool:
        """
        Getter for property: (bool) AllowConvergentObjectWithMixedGeometries
         Returns the AllowConvergentObjectWithMixedGeometries  
            
         
        """
        pass
    @AllowConvergentObjectWithMixedGeometries.setter
    def AllowConvergentObjectWithMixedGeometries(self, allowConvergentObjectWithMixedGeometries: bool):
        """
        Setter for property: (bool) AllowConvergentObjectWithMixedGeometries
         Returns the AllowConvergentObjectWithMixedGeometries  
            
         
        """
        pass
    @property
    def AllowInferredCurveSelection(self) -> bool:
        """
        Getter for property: (bool) AllowInferredCurveSelection
         Returns the AllowInferredCurveSelection  
            
         
        """
        pass
    @AllowInferredCurveSelection.setter
    def AllowInferredCurveSelection(self, allow: bool):
        """
        Setter for property: (bool) AllowInferredCurveSelection
         Returns the AllowInferredCurveSelection  
            
         
        """
        pass
    @property
    def AutomaticProgression(self) -> bool:
        """
        Getter for property: (bool) AutomaticProgression
         Returns the AutomaticProgression  
            
         
        """
        pass
    @AutomaticProgression.setter
    def AutomaticProgression(self, automaticProgression: bool):
        """
        Setter for property: (bool) AutomaticProgression
         Returns the AutomaticProgression  
            
         
        """
        pass
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @property
    def Bitmap(self) -> str:
        """
        Getter for property: (str) Bitmap
         Returns the Bitmap  
            
         
        """
        pass
    @Bitmap.setter
    def Bitmap(self, bitmap_string: str):
        """
        Setter for property: (str) Bitmap
         Returns the Bitmap  
            
         
        """
        pass
    @property
    def BlendVirtualCurveOverlay(self) -> bool:
        """
        Getter for property: (bool) BlendVirtualCurveOverlay
         Returns the BlendVirtualCurveOverlay  
            
         
        """
        pass
    @BlendVirtualCurveOverlay.setter
    def BlendVirtualCurveOverlay(self, blendCurve: bool):
        """
        Setter for property: (bool) BlendVirtualCurveOverlay
         Returns the BlendVirtualCurveOverlay  
            
         
        """
        pass
    @property
    def CreateInterpartLink(self) -> bool:
        """
        Getter for property: (bool) CreateInterpartLink
         Returns the CreateInterpartLink  
            
         
        """
        pass
    @CreateInterpartLink.setter
    def CreateInterpartLink(self, createLink: bool):
        """
        Setter for property: (bool) CreateInterpartLink
         Returns the CreateInterpartLink  
            
         
        """
        pass
    @property
    def Cue(self) -> str:
        """
        Getter for property: (str) Cue
         Returns the Cue  
            
         
        """
        pass
    @Cue.setter
    def Cue(self, cue: str):
        """
        Setter for property: (str) Cue
         Returns the Cue  
            
         
        """
        pass
    @property
    def CurveRules(self) -> int:
        """
        Getter for property: (int) CurveRules
         Returns the CurveRules  
            
         
        """
        pass
    @CurveRules.setter
    def CurveRules(self, curveRules: int):
        """
        Setter for property: (int) CurveRules
         Returns the CurveRules  
            
         
        """
        pass
    @property
    def DefaultCurveRulesAsString(self) -> str:
        """
        Getter for property: (str) DefaultCurveRulesAsString
         Returns the DefaultCurveRules as string  
            
         
        """
        pass
    @DefaultCurveRulesAsString.setter
    def DefaultCurveRulesAsString(self, enumString: str):
        """
        Setter for property: (str) DefaultCurveRulesAsString
         Returns the DefaultCurveRules as string  
            
         
        """
        pass
    @property
    def EntityType(self) -> int:
        """
        Getter for property: (int) EntityType
         Returns the EntityType  
            
         
        """
        pass
    @EntityType.setter
    def EntityType(self, entityType: int):
        """
        Setter for property: (int) EntityType
         Returns the EntityType  
            
         
        """
        pass
    @property
    def InferredCurveSelection(self) -> bool:
        """
        Getter for property: (bool) InferredCurveSelection
         Returns the InferredCurveSelection  
            
         
        """
        pass
    @InferredCurveSelection.setter
    def InferredCurveSelection(self, selectInferredCurve: bool):
        """
        Setter for property: (bool) InferredCurveSelection
         Returns the InferredCurveSelection  
            
         
        """
        pass
    @property
    def InterpartSelectionAsString(self) -> str:
        """
        Getter for property: (str) InterpartSelectionAsString
         Returns the InterpartSelection as string  
            
         
        """
        pass
    @InterpartSelectionAsString.setter
    def InterpartSelectionAsString(self, enumString: str):
        """
        Setter for property: (str) InterpartSelectionAsString
         Returns the InterpartSelection as string  
            
         
        """
        pass
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
         Returns the LabelString  
            
         
        """
        pass
    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
         Returns the LabelString  
            
         
        """
        pass
    @property
    def MaximumScopeAsString(self) -> str:
        """
        Getter for property: (str) MaximumScopeAsString
         Returns the MaximumScope  
            
         
        """
        pass
    @MaximumScopeAsString.setter
    def MaximumScopeAsString(self, enumString: str):
        """
        Setter for property: (str) MaximumScopeAsString
         Returns the MaximumScope  
            
         
        """
        pass
    @property
    def PopupMenuEnabled(self) -> bool:
        """
        Getter for property: (bool) PopupMenuEnabled
         Returns the PopupMenuEnabled  
            
         
        """
        pass
    @PopupMenuEnabled.setter
    def PopupMenuEnabled(self, enabled: bool):
        """
        Setter for property: (bool) PopupMenuEnabled
         Returns the PopupMenuEnabled  
            
         
        """
        pass
    @property
    def SelectModeAsString(self) -> str:
        """
        Getter for property: (str) SelectModeAsString
         Returns the SelectMode as string  
            
         
        """
        pass
    @SelectModeAsString.setter
    def SelectModeAsString(self, enumString: str):
        """
        Setter for property: (str) SelectModeAsString
         Returns the SelectMode as string  
            
         
        """
        pass
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
         Returns the StepStatus as string  
            
         
        """
        pass
    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
         Returns the StepStatus as string  
            
         
        """
        pass
    @property
    def ToolTip(self) -> str:
        """
        Getter for property: (str) ToolTip
         Returns the ToolTip  
            
         
        """
        pass
    @ToolTip.setter
    def ToolTip(self, toolTip: str):
        """
        Setter for property: (str) ToolTip
         Returns the ToolTip  
            
         
        """
        pass
    def GetBalloonTooltipLayoutMembers(self) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         Returns layout_strings (List[str]): Value to get from the property. .
        """
        pass
    def GetCollectorObjectOfCurveCollector(self) -> NXOpen.ScCollector:
        """
         Get the collector object
         Returns collectorObject ( NXOpen.ScCollector): .
        """
        pass
    def GetDefaultCurveRulesMembers(self) -> List[str]:
        """
         Gets the DefaultCurveRules members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def GetInterpartSelectionMembers(self) -> List[str]:
        """
         Gets the InterpartSelection members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def GetSelectModeMembers(self) -> List[str]:
        """
         Gets the SelectMode members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def GetSelectedObjects(self) -> List[NXOpen.TaggedObject]:
        """
         Gets the SelectedObjects
         Returns objectVector ( NXOpen.TaggedObject Li): Value to get from the property.
        """
        pass
    def GetStepStatusMembers(self) -> List[str]:
        """
         Gets the StepStatus members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def SetCollectorObjectOfCurveCollector(self, collectorObject: NXOpen.ScCollector) -> None:
        """
         Set collector object
        """
        pass
    def SetSelectedObjects(self, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the SelectedObjects
        """
        pass
    def TestSelection(self, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Tests the selection for this block. The block must be in focus to call this API
        """
        pass
import NXOpen
import NXOpen.MenuBar
class DialogTester(NXOpen.Object): 
    """ Represents Block Styler Dialog tester class that contains testing tools for Block Styler Dialogs """
    def GetMessageBoxTester() -> MessageBoxTester:
        """
         Returns an object of BlockStyler.MessageBoxTester class for testing NX Message Boxes. 
         Returns message_box_tester ( MessageBoxTester NXOpen.B): Object of BlockStyler.MessageBoxTester class.
        """
        pass
    def GetTestStepSequence(dialog_name: str) -> TestStepSequence:
        """
         Returns a test step sequence object for a dialog mapped to a dlx file.
         Returns test_sequence ( TestStepSequence NXOpen.B): Object of BlockStyler.TestStepSequence class .
        """
        pass
    def InvokeMenuButtonAction(button: NXOpen.MenuBar.MenuButton) -> bool:
        """
         Invokes a menu button action. Could be used for launching a dialog for testing using a menu button.
         Returns action_status (bool): .
        """
        pass
class DoubleBlock(UIBlock): 
    """ Represents a Double block"""
    @property
    def AdaptiveScaleLimits(self) -> bool:
        """
        Getter for property: (bool) AdaptiveScaleLimits
         Returns the AdaptiveScaleLimits  
            
         
        """
        pass
    @AdaptiveScaleLimits.setter
    def AdaptiveScaleLimits(self, scale_limits: bool):
        """
        Setter for property: (bool) AdaptiveScaleLimits
         Returns the AdaptiveScaleLimits  
            
         
        """
        pass
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @property
    def Bitmap(self) -> str:
        """
        Getter for property: (str) Bitmap
         Returns the Bitmap  
            
         
        """
        pass
    @Bitmap.setter
    def Bitmap(self, bitmap_string: str):
        """
        Setter for property: (str) Bitmap
         Returns the Bitmap  
            
         
        """
        pass
    @property
    def Increment(self) -> float:
        """
        Getter for property: (float) Increment
         Returns the Increment  
            
         
        """
        pass
    @Increment.setter
    def Increment(self, increment: float):
        """
        Setter for property: (float) Increment
         Returns the Increment  
            
         
        """
        pass
    @property
    def LineIncrement(self) -> float:
        """
        Getter for property: (float) LineIncrement
         Returns the LineIncrement  
            
         
        """
        pass
    @LineIncrement.setter
    def LineIncrement(self, line_increment: float):
        """
        Setter for property: (float) LineIncrement
         Returns the LineIncrement  
            
         
        """
        pass
    @property
    def Localize(self) -> bool:
        """
        Getter for property: (bool) Localize
         Returns the Localize  
            
         
        """
        pass
    @Localize.setter
    def Localize(self, localize: bool):
        """
        Setter for property: (bool) Localize
         Returns the Localize  
            
         
        """
        pass
    @property
    def MaxInclusive(self) -> bool:
        """
        Getter for property: (bool) MaxInclusive
         Returns the MaxInclusive  
            
         
        """
        pass
    @MaxInclusive.setter
    def MaxInclusive(self, max_inclusive: bool):
        """
        Setter for property: (bool) MaxInclusive
         Returns the MaxInclusive  
            
         
        """
        pass
    @property
    def MaximumValue(self) -> float:
        """
        Getter for property: (float) MaximumValue
         Returns the MaximumValue  
            
         
        """
        pass
    @MaximumValue.setter
    def MaximumValue(self, max_value: float):
        """
        Setter for property: (float) MaximumValue
         Returns the MaximumValue  
            
         
        """
        pass
    @property
    def MinInclusive(self) -> bool:
        """
        Getter for property: (bool) MinInclusive
         Returns the MinInclusive  
            
         
        """
        pass
    @MinInclusive.setter
    def MinInclusive(self, min_inclusive: bool):
        """
        Setter for property: (bool) MinInclusive
         Returns the MinInclusive  
            
         
        """
        pass
    @property
    def MinimumValue(self) -> float:
        """
        Getter for property: (float) MinimumValue
         Returns the MinimumValue  
            
         
        """
        pass
    @MinimumValue.setter
    def MinimumValue(self, min_value: float):
        """
        Setter for property: (float) MinimumValue
         Returns the MinimumValue  
            
         
        """
        pass
    @property
    def PageIncrement(self) -> float:
        """
        Getter for property: (float) PageIncrement
         Returns the PageIncrement  
            
         
        """
        pass
    @PageIncrement.setter
    def PageIncrement(self, page_increment: float):
        """
        Setter for property: (float) PageIncrement
         Returns the PageIncrement  
            
         
        """
        pass
    @property
    def PresentationStyleAsString(self) -> str:
        """
        Getter for property: (str) PresentationStyleAsString
         Returns the PresentationStyle as string  
            
         
        """
        pass
    @PresentationStyleAsString.setter
    def PresentationStyleAsString(self, enumString: str):
        """
        Setter for property: (str) PresentationStyleAsString
         Returns the PresentationStyle as string  
            
         
        """
        pass
    @property
    def ReadOnlyValue(self) -> bool:
        """
        Getter for property: (bool) ReadOnlyValue
         Returns the ReadOnlyValue  
            
         
        """
        pass
    @ReadOnlyValue.setter
    def ReadOnlyValue(self, read_only: bool):
        """
        Setter for property: (bool) ReadOnlyValue
         Returns the ReadOnlyValue  
            
         
        """
        pass
    @property
    def RetainValue(self) -> bool:
        """
        Getter for property: (bool) RetainValue
         Returns the RetainValue  
            
         
        """
        pass
    @RetainValue.setter
    def RetainValue(self, retain: bool):
        """
        Setter for property: (bool) RetainValue
         Returns the RetainValue  
            
         
        """
        pass
    @property
    def ScaleLimits(self) -> bool:
        """
        Getter for property: (bool) ScaleLimits
         Returns the ScaleLimits  
            
         
        """
        pass
    @ScaleLimits.setter
    def ScaleLimits(self, scale_limits: bool):
        """
        Setter for property: (bool) ScaleLimits
         Returns the ScaleLimits  
            
         
        """
        pass
    @property
    def ScaleMaxLimitLabel(self) -> str:
        """
        Getter for property: (str) ScaleMaxLimitLabel
         Returns the ScaleMaxLimitLabel  
            
         
        """
        pass
    @ScaleMaxLimitLabel.setter
    def ScaleMaxLimitLabel(self, max_limit_label: str):
        """
        Setter for property: (str) ScaleMaxLimitLabel
         Returns the ScaleMaxLimitLabel  
            
         
        """
        pass
    @property
    def ScaleMinLimitLabel(self) -> str:
        """
        Getter for property: (str) ScaleMinLimitLabel
         Returns the ScaleMinLimitLabel  
            
         
        """
        pass
    @ScaleMinLimitLabel.setter
    def ScaleMinLimitLabel(self, min_limit_label: str):
        """
        Setter for property: (str) ScaleMinLimitLabel
         Returns the ScaleMinLimitLabel  
            
         
        """
        pass
    @property
    def ShowScaleValue(self) -> bool:
        """
        Getter for property: (bool) ShowScaleValue
         Returns the ShowScaleValue  
            
         
        """
        pass
    @ShowScaleValue.setter
    def ShowScaleValue(self, show_value: bool):
        """
        Setter for property: (bool) ShowScaleValue
         Returns the ShowScaleValue  
            
         
        """
        pass
    @property
    def TitleVisibility(self) -> bool:
        """
        Getter for property: (bool) TitleVisibility
         Returns the TitleVisibility  
            
         
        """
        pass
    @TitleVisibility.setter
    def TitleVisibility(self, visibility: bool):
        """
        Setter for property: (bool) TitleVisibility
         Returns the TitleVisibility  
            
         
        """
        pass
    @property
    def Value(self) -> float:
        """
        Getter for property: (float) Value
         Returns the Value  
            
         
        """
        pass
    @Value.setter
    def Value(self, double_value: float):
        """
        Setter for property: (float) Value
         Returns the Value  
            
         
        """
        pass
    @property
    def WrapSpin(self) -> bool:
        """
        Getter for property: (bool) WrapSpin
         Returns the WrapSpin  
            
         
        """
        pass
    @WrapSpin.setter
    def WrapSpin(self, wrap_spin: bool):
        """
        Setter for property: (bool) WrapSpin
         Returns the WrapSpin  
            
         
        """
        pass
    def GetBalloonTooltipLayoutMembers(self) -> List[str]:
        """
         Gets the BalloonTooltipLayout member 
         Returns layout_strings (List[str]): Value to get from the proprty. .
        """
        pass
    def GetComboOptions(self) -> List[float]:
        """
         Gets the ComboOptions
         Returns option_value (List[float]): .
        """
        pass
    def GetPresentationStyleMembers(self) -> List[str]:
        """
         Gets the PresentationStyle members 
         Returns member_strings (List[str]): Value to get for the property. .
        """
        pass
    def SetComboOptions(self, option_value: List[float]) -> None:
        """
         Sets the ComboOptions
        """
        pass
    def TestValueChanged(self, double_value: float) -> None:
        """
        Tests value changed event workflow mapped to this DoubleBlock block.
        """
        pass
class DoubleTable(UIBlock): 
    """ Represents a Double Table block"""
    @property
    def CellWidth(self) -> int:
        """
        Getter for property: (int) CellWidth
         Returns the CellWidth  
            
         
        """
        pass
    @CellWidth.setter
    def CellWidth(self, cell_width: int):
        """
        Setter for property: (int) CellWidth
         Returns the CellWidth  
            
         
        """
        pass
    @property
    def Increment(self) -> float:
        """
        Getter for property: (float) Increment
         Returns the Increment.  
           Use this property only when Spin is true  
         
        """
        pass
    @Increment.setter
    def Increment(self, increment: float):
        """
        Setter for property: (float) Increment
         Returns the Increment.  
           Use this property only when Spin is true  
         
        """
        pass
    @property
    def RetainValue(self) -> bool:
        """
        Getter for property: (bool) RetainValue
         Returns the RetainValue.  
           If true, indicates that the values in the block would be stored in dialog memory upon OK, Apply or Close.   
         
        """
        pass
    @RetainValue.setter
    def RetainValue(self, retain: bool):
        """
        Setter for property: (bool) RetainValue
         Returns the RetainValue.  
           If true, indicates that the values in the block would be stored in dialog memory upon OK, Apply or Close.   
         
        """
        pass
    @property
    def Spin(self) -> bool:
        """
        Getter for property: (bool) Spin
         Returns the Spin  
            
         
        """
        pass
    @Spin.setter
    def Spin(self, spin: bool):
        """
        Setter for property: (bool) Spin
         Returns the Spin  
            
         
        """
        pass
    @property
    def WrapSpin(self) -> bool:
        """
        Getter for property: (bool) WrapSpin
         Returns the WrapSpin.  
           Use this property only when Spin is true  
         
        """
        pass
    @WrapSpin.setter
    def WrapSpin(self, wrap_spin: bool):
        """
        Setter for property: (bool) WrapSpin
         Returns the WrapSpin.  
           Use this property only when Spin is true  
         
        """
        pass
    def GetColumnTitles(self) -> List[str]:
        """
         Gets the Column Titles
         Returns column_titles (List[str]): Column Title values to get from the property. .
        """
        pass
    def GetMaximumValues(self) -> Tuple[List[float], int, int]:
        """
         Gets the MaximumValues
         Returns A tuple consisting of (matrixValue, nRows, nColumns). 
         - matrixValue is: List[float].Value to get from the property. .
         - nRows is: int. Number of Rows in the 2D matrix .
         - nColumns is: int. Number of Columns in the 2D matrix .

        """
        pass
    def GetMinimumValues(self) -> Tuple[List[float], int, int]:
        """
         Gets the MinimumValues
         Returns A tuple consisting of (matrixValue, nRows, nColumns). 
         - matrixValue is: List[float].Value to get from the property .
         - nRows is: int. Number of Rows in the 2D matrix .
         - nColumns is: int. Number of Columns in the 2D matrix .

        """
        pass
    def GetRowTitles(self) -> List[str]:
        """
         Gets the titles of rows in table
         Returns row_title (List[str]): Value to get from the property. .
        """
        pass
    def GetValues(self) -> Tuple[List[float], int, int]:
        """
         Gets the Values in table
         Returns A tuple consisting of (matrixValue, nRows, nColumns). 
         - matrixValue is: List[float].Value to get from the property. .
         - nRows is: int. Number of Rows in the 2D matrix .
         - nColumns is: int. Number of Columns in the 2D matrix .

        """
        pass
    def SetColumnTitles(self, column_titles: List[str]) -> None:
        """
         Sets the Column Titles
        """
        pass
    def SetMaximumValues(self, nRows: int, nColumns: int, matrixValue: List[float]) -> None:
        """
         Sets the MaximumValues
        """
        pass
    def SetMinimumValues(self, nRows: int, nColumns: int, matrixValue: List[float]) -> None:
        """
         Sets the MinimumValues
        """
        pass
    def SetRowTitles(self, row_title: List[str]) -> None:
        """
         Sets the titles of rows in table
        """
        pass
    def SetValues(self, nRows: int, nColumns: int, matrixValue: List[float]) -> None:
        """
         Sets the Values in table
        """
        pass
    def TestValueChanged(self, nRows: int, nColumns: int, matrixValue: List[float]) -> None:
        """
        Tests value changed event workflow mapped to this DoubleTable block.
        """
        pass
class DrawingArea(UIBlock): 
    """ Represents a Drawing Area block"""
    @property
    def Height(self) -> int:
        """
        Getter for property: (int) Height
         Returns the Height  
            
         
        """
        pass
    @Height.setter
    def Height(self, height: int):
        """
        Setter for property: (int) Height
         Returns the Height  
            
         
        """
        pass
    @property
    def Image(self) -> str:
        """
        Getter for property: (str) Image
         Returns the Image  
            
         
        """
        pass
    @Image.setter
    def Image(self, image_string: str):
        """
        Setter for property: (str) Image
         Returns the Image  
            
         
        """
        pass
    @property
    def Width(self) -> int:
        """
        Getter for property: (int) Width
         Returns the Width  
            
         
        """
        pass
    @Width.setter
    def Width(self, width: int):
        """
        Setter for property: (int) Width
         Returns the Width  
            
         
        """
        pass
class Enumeration(UIBlock): 
    """ Represents an Enumeration block"""
    @property
    def AllowShortcuts(self) -> bool:
        """
        Getter for property: (bool) AllowShortcuts
         Returns the AllowShortcuts.  
          
                If true, the 'Show Shortcuts' option is available.  
         
        """
        pass
    @AllowShortcuts.setter
    def AllowShortcuts(self, allow: bool):
        """
        Setter for property: (bool) AllowShortcuts
         Returns the AllowShortcuts.  
          
                If true, the 'Show Shortcuts' option is available.  
         
        """
        pass
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @property
    def BorderVisibility(self) -> bool:
        """
        Getter for property: (bool) BorderVisibility
         Returns the BorderVisibility  
            
         
        """
        pass
    @BorderVisibility.setter
    def BorderVisibility(self, visibility: bool):
        """
        Setter for property: (bool) BorderVisibility
         Returns the BorderVisibility  
            
         
        """
        pass
    @property
    def HighQualityBitmap(self) -> bool:
        """
        Getter for property: (bool) HighQualityBitmap
         Returns the HighQualityBitmap  
            
         
        """
        pass
    @HighQualityBitmap.setter
    def HighQualityBitmap(self, high_quality: bool):
        """
        Setter for property: (bool) HighQualityBitmap
         Returns the HighQualityBitmap  
            
         
        """
        pass
    @property
    def IconsOnly(self) -> bool:
        """
        Getter for property: (bool) IconsOnly
         Returns the IconsOnly.  
          
                If true, the enumeration options are shown as bitmaps only   
         
        """
        pass
    @IconsOnly.setter
    def IconsOnly(self, icons_only: bool):
        """
        Setter for property: (bool) IconsOnly
         Returns the IconsOnly.  
          
                If true, the enumeration options are shown as bitmaps only   
         
        """
        pass
    @property
    def LabelVisibility(self) -> bool:
        """
        Getter for property: (bool) LabelVisibility
         Returns the LabelVisibility  
            
         
        """
        pass
    @LabelVisibility.setter
    def LabelVisibility(self, visibility: bool):
        """
        Setter for property: (bool) LabelVisibility
         Returns the LabelVisibility  
            
         
        """
        pass
    @property
    def LayoutAsString(self) -> str:
        """
        Getter for property: (str) LayoutAsString
         Returns the Layout as string  
            
         
        """
        pass
    @LayoutAsString.setter
    def LayoutAsString(self, enumString: str):
        """
        Setter for property: (str) LayoutAsString
         Returns the Layout as string  
            
         
        """
        pass
    @property
    def Localize(self) -> bool:
        """
        Getter for property: (bool) Localize
         Returns the Localize.  
          
                If true, the Label is translated to current locale language.  
         
        """
        pass
    @Localize.setter
    def Localize(self, localize: bool):
        """
        Setter for property: (bool) Localize
         Returns the Localize.  
          
                If true, the Label is translated to current locale language.  
         
        """
        pass
    @property
    def NumberOfColumns(self) -> int:
        """
        Getter for property: (int) NumberOfColumns
         Returns the NumberOfColumns  
            
         
        """
        pass
    @NumberOfColumns.setter
    def NumberOfColumns(self, num_column: int):
        """
        Setter for property: (int) NumberOfColumns
         Returns the NumberOfColumns  
            
         
        """
        pass
    @property
    def PackedColumns(self) -> bool:
        """
        Getter for property: (bool) PackedColumns
         Returns the PackedColumns.  
          
                If true, each column takes up as much space as required for labels in that column. If false,
                the longest label amongst all options dictates the width of all columns.  
         
        """
        pass
    @PackedColumns.setter
    def PackedColumns(self, packed_columns: bool):
        """
        Setter for property: (bool) PackedColumns
         Returns the PackedColumns.  
          
                If true, each column takes up as much space as required for labels in that column. If false,
                the longest label amongst all options dictates the width of all columns.  
         
        """
        pass
    @property
    def PresentationStyleAsString(self) -> str:
        """
        Getter for property: (str) PresentationStyleAsString
         Returns the PresentationStyle as string  
            
         
        """
        pass
    @PresentationStyleAsString.setter
    def PresentationStyleAsString(self, enumString: str):
        """
        Setter for property: (str) PresentationStyleAsString
         Returns the PresentationStyle as string  
            
         
        """
        pass
    @property
    def RetainValue(self) -> bool:
        """
        Getter for property: (bool) RetainValue
         Returns the RetainValue  
            
         
        """
        pass
    @RetainValue.setter
    def RetainValue(self, retain: bool):
        """
        Setter for property: (bool) RetainValue
         Returns the RetainValue  
            
         
        """
        pass
    @property
    def ValueAsString(self) -> str:
        """
        Getter for property: (str) ValueAsString
         Returns the Value as string.  
          
                Represents the currently selected option of enum.  
         
        """
        pass
    @ValueAsString.setter
    def ValueAsString(self, enumString: str):
        """
        Setter for property: (str) ValueAsString
         Returns the Value as string.  
          
                Represents the currently selected option of enum.  
         
        """
        pass
    def GetBalloonTooltipImages(self) -> List[str]:
        """
         Gets the BalloonTooltipImages
         Returns image_strings (List[str]): .
        """
        pass
    def GetBalloonTooltipLayoutMembers(self) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         Returns layout_strings (List[str]): Value to get from the property.
        """
        pass
    def GetBalloonTooltipTexts(self) -> List[str]:
        """
         Gets the BalloonTooltipTexts
         Returns tooltip_text_array (List[str]): Value to get from the property .
        """
        pass
    def GetBitmaps(self) -> List[str]:
        """
         Gets the Bitmaps
         Returns bitmaps_strings (List[str]): Value to get for the property. .
        """
        pass
    def GetEnumMembers(self) -> List[str]:
        """
        Gets the Enum members.
         Returns member_strings (List[str]): Array of member names.
        """
        pass
    def GetEnumSensitivity(self) -> List[int]:
        """
         Gets EnumSensitivity
         Returns value_vector (List[int]):  Array of integers with the value 0 or 1. If 1 then the corresponding enum member is sensitive otherwise it is insensitive. .
        """
        pass
    def GetEnumVisibility(self) -> List[int]:
        """
         Gets EnumVisibility
         Returns value_vector (List[int]):  Array of integers with the value 0 or 1. If 1 then the corresponding enum member is visible otherwise it is hidden. .
        """
        pass
    def GetInitialShortcuts(self) -> List[int]:
        """
         Gets InitialShortcuts.
                Specifies the set of shortcuts that are displayed when the dialog is initially shown. Valid only if AllowShortcuts property is true. 
         Returns value_vector (List[int]):  Array of integers with length between 0 and N-1, where N is the number of enumeration options .
        """
        pass
    def GetLayoutMembers(self) -> List[str]:
        """
         Gets the Layout members 
         Returns layout_strings (List[str]): Value to get from the property .
        """
        pass
    def GetPresentationStyleMembers(self) -> List[str]:
        """
         Gets the PresentationStyle members 
         Returns member_strings (List[str]): Value to get from the property.
        """
        pass
    def SetBalloonTooltipImages(self, image_strings: List[str]) -> None:
        """
         Sets the BalloonTooltipImages
        """
        pass
    def SetBalloonTooltipTexts(self, tooltip_text_array: List[str]) -> None:
        """
         Sets the BalloonTooltipTexts
        """
        pass
    def SetBitmaps(self, bitmaps_strings: List[str]) -> None:
        """
         Sets the Bitmaps
        """
        pass
    def SetEnumMembers(self, member_strings: List[str]) -> None:
        """
        Sets the Enum members.
        """
        pass
    def SetEnumSensitivity(self, value_vector: List[int]) -> None:
        """
         Sets EnumSensitivity
        """
        pass
    def SetEnumVisibility(self, value_vector: List[int]) -> None:
        """
         Sets EnumVisibility
        """
        pass
    def SetInitialShortcuts(self, value_vector: List[int]) -> None:
        """
         Sets InitialShortcuts.
                Specifies the set of shortcuts that are displayed when the dialog is initially shown. Valid only if AllowShortcuts property is true.
        """
        pass
    def TestValueChanged(self, enumString: str) -> None:
        """
        Tests value changed event workflow mapped to this Enumeration block.
        """
        pass
class Explorer(UIBlock): 
    """ Represents an Explorer block.  The Explorer block allows for collecting a large number of inputs into a single dialog.
    The inputs are organized into nodes and sub-nodes on a tree to allow for quick and easy navigation.  The Explorer
    block provides the ability to have up to 5 levels of nodes in the Navigation Tree.  Each node contains groups and
    individual inputs that are laid out like standard NX dialogs.  When selecting level 1 and level 2 nodes that do not
    contain any groups and only contain sub-nodes the first sub-node containing groups is highlighted and its content shown.
 """
    @property
    def CurrentNode(self) -> int:
        """
        Getter for property: (int) CurrentNode
         Returns the CurrentNode selected in the Navigation Tree.  
             
         
        """
        pass
    @CurrentNode.setter
    def CurrentNode(self, currentNode: int):
        """
        Setter for property: (int) CurrentNode
         Returns the CurrentNode selected in the Navigation Tree.  
             
         
        """
        pass
    @property
    def Localize(self) -> bool:
        """
        Getter for property: (bool) Localize
         Returns the localization of the block label.  
           If the label matches an English string in the NX string
                localization databse and the Localize property is set to true, then the Label is translated
                to the current locale language.   
         
        """
        pass
    @Localize.setter
    def Localize(self, localize: bool):
        """
        Setter for property: (bool) Localize
         Returns the localization of the block label.  
           If the label matches an English string in the NX string
                localization databse and the Localize property is set to true, then the Label is translated
                to the current locale language.   
         
        """
        pass
    @property
    def Members(self) -> PropertyList:
        """
        Getter for property: ( PropertyList NXOpen.B) Members
         Returns the members.  
             
         
        """
        pass
    @property
    def TreeWidth(self) -> int:
        """
        Getter for property: (int) TreeWidth
         Returns the TreeWidth for the Navigation Tree.  
             
         
        """
        pass
    @TreeWidth.setter
    def TreeWidth(self, treeWidth: int):
        """
        Setter for property: (int) TreeWidth
         Returns the TreeWidth for the Navigation Tree.  
             
         
        """
        pass
    NotifyNodeSelectedPostCallback = Callable[[Explorer, int], None]
    NotifyNodeSelectedPreCallback = Callable[[Explorer, int], None]
    def SetChildMembers(self, parentMember: UIBlock, childMembers: List[UIBlock]) -> None:
        """
         Sets the parent member for the child members in the Explorer Navigation Tree.  The maximum
                Navigation Tree depth is 5 levels.  An exception is thrown if the parent member depth is
                already at the maximum allowed depth. 
        """
        pass
    def SetNotifyNodeSelectedPostHandler(self, cb: Explorer.NotifyNodeSelectedPostCallback) -> None:
        """
         Sets the NotifyNodeSelectedPost handler. 
        """
        pass
    def SetNotifyNodeSelectedPreHandler(self, cb: Explorer.NotifyNodeSelectedPreCallback) -> None:
        """
         Sets the NotifyNodeSelectedPre handler. 
        """
        pass
    def TestCurrentNodeChanged(self, currentNode: int) -> None:
        """
        Tests current node changed.
        """
        pass
import NXOpen
class ExpressionBlock(UIBlock): 
    """ Represents an Expression block"""
    @property
    def AdaptiveScaleLimits(self) -> bool:
        """
        Getter for property: (bool) AdaptiveScaleLimits
         Returnsthe AdaptiveScaleLimits.  
          
                If true, indicates that the scale should be adaptive.  
         
        """
        pass
    @AdaptiveScaleLimits.setter
    def AdaptiveScaleLimits(self, scale_limits: bool):
        """
        Setter for property: (bool) AdaptiveScaleLimits
         Returnsthe AdaptiveScaleLimits.  
          
                If true, indicates that the scale should be adaptive.  
         
        """
        pass
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @property
    def DimensionalityAsString(self) -> str:
        """
        Getter for property: (str) DimensionalityAsString
         Returns the  Dimensionality as string.  
           It specifies the type of quantity that the expression represents.  
         
        """
        pass
    @DimensionalityAsString.setter
    def DimensionalityAsString(self, enum_string: str):
        """
        Setter for property: (str) DimensionalityAsString
         Returns the  Dimensionality as string.  
           It specifies the type of quantity that the expression represents.  
         
        """
        pass
    @property
    def ExpressionObject(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) ExpressionObject
         Returns the ExpressionObject  
            
         
        """
        pass
    @ExpressionObject.setter
    def ExpressionObject(self, expression_object: NXOpen.TaggedObject):
        """
        Setter for property: ( NXOpen.TaggedObject) ExpressionObject
         Returns the ExpressionObject  
            
         
        """
        pass
    @property
    def Formula(self) -> str:
        """
        Getter for property: (str) Formula
         Returns the Formula for the expression  
            
         
        """
        pass
    @Formula.setter
    def Formula(self, formula_string: str):
        """
        Setter for property: (str) Formula
         Returns the Formula for the expression  
            
         
        """
        pass
    @property
    def HasUnitsMenu(self) -> bool:
        """
        Getter for property: (bool) HasUnitsMenu
         Returns the HasUnitsMenu.  
           If true, indicates that a menu will be displayed allowing the user to change units.
                This property is relevant only when the Dimensionality property is set to a value that is not without units.  
         
        """
        pass
    @HasUnitsMenu.setter
    def HasUnitsMenu(self, has_menu: bool):
        """
        Setter for property: (bool) HasUnitsMenu
         Returns the HasUnitsMenu.  
           If true, indicates that a menu will be displayed allowing the user to change units.
                This property is relevant only when the Dimensionality property is set to a value that is not without units.  
         
        """
        pass
    @property
    def LineIncrement(self) -> float:
        """
        Getter for property: (float) LineIncrement
         Returnsthe LineIncrement value.  
          
                Specifies the incrementdecrement when the user presses the arrow keys on the keyboard.
                Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
         
        """
        pass
    @LineIncrement.setter
    def LineIncrement(self, line_increment: float):
        """
        Setter for property: (float) LineIncrement
         Returnsthe LineIncrement value.  
          
                Specifies the incrementdecrement when the user presses the arrow keys on the keyboard.
                Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
         
        """
        pass
    @property
    def MaxInclusive(self) -> bool:
        """
        Getter for property: (bool) MaxInclusive
         Returns the MaxInclusive  
            
         
        """
        pass
    @MaxInclusive.setter
    def MaxInclusive(self, max_inclusive: bool):
        """
        Setter for property: (bool) MaxInclusive
         Returns the MaxInclusive  
            
         
        """
        pass
    @property
    def MaximumValue(self) -> float:
        """
        Getter for property: (float) MaximumValue
         Returns the MaximumValue  
            
         
        """
        pass
    @MaximumValue.setter
    def MaximumValue(self, max_value: float):
        """
        Setter for property: (float) MaximumValue
         Returns the MaximumValue  
            
         
        """
        pass
    @property
    def MinInclusive(self) -> bool:
        """
        Getter for property: (bool) MinInclusive
         Returns the MinInclusive  
            
         
        """
        pass
    @MinInclusive.setter
    def MinInclusive(self, min_inclusive: bool):
        """
        Setter for property: (bool) MinInclusive
         Returns the MinInclusive  
            
         
        """
        pass
    @property
    def MinimumValue(self) -> float:
        """
        Getter for property: (float) MinimumValue
         Returns the MinimumValue  
            
         
        """
        pass
    @MinimumValue.setter
    def MinimumValue(self, min_value: float):
        """
        Setter for property: (float) MinimumValue
         Returns the MinimumValue  
            
         
        """
        pass
    @property
    def PageIncrement(self) -> float:
        """
        Getter for property: (float) PageIncrement
         Returnsthe PageIncrement value.  
          
                Specifies the incrementdecrement when the user presses the Page Up or Page Down keys on the keyboard.
                Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
         
        """
        pass
    @PageIncrement.setter
    def PageIncrement(self, page_increment: float):
        """
        Setter for property: (float) PageIncrement
         Returnsthe PageIncrement value.  
          
                Specifies the incrementdecrement when the user presses the Page Up or Page Down keys on the keyboard.
                Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
         
        """
        pass
    @property
    def RetainUnits(self) -> bool:
        """
        Getter for property: (bool) RetainUnits
         Returns the RetainUnits.  
           If true, indicates that the units in the block would be stored in dialog memory upon OK, Apply or Close.   
         
        """
        pass
    @RetainUnits.setter
    def RetainUnits(self, retain: bool):
        """
        Setter for property: (bool) RetainUnits
         Returns the RetainUnits.  
           If true, indicates that the units in the block would be stored in dialog memory upon OK, Apply or Close.   
         
        """
        pass
    @property
    def RetainValue(self) -> bool:
        """
        Getter for property: (bool) RetainValue
         Returns the RetainValue.  
           If true, indicates that the values in the block would be stored in dialog memory upon OK, Apply or Close.   
         
        """
        pass
    @RetainValue.setter
    def RetainValue(self, retain: bool):
        """
        Setter for property: (bool) RetainValue
         Returns the RetainValue.  
           If true, indicates that the values in the block would be stored in dialog memory upon OK, Apply or Close.   
         
        """
        pass
    @property
    def Units(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) Units
         Returns the Units for the expression   
            
         
        """
        pass
    @Units.setter
    def Units(self, units: NXOpen.TaggedObject):
        """
        Setter for property: ( NXOpen.TaggedObject) Units
         Returns the Units for the expression   
            
         
        """
        pass
    @property
    def Value(self) -> float:
        """
        Getter for property: (float) Value
         Returns the Value.  
            
         
        """
        pass
    @Value.setter
    def Value(self, expression_value: float):
        """
        Setter for property: (float) Value
         Returns the Value.  
            
         
        """
        pass
    @property
    def WithScale(self) -> bool:
        """
        Getter for property: (bool) WithScale
         Returns the WithScale.  
           If true, the slider bar is shown.  
         
        """
        pass
    @WithScale.setter
    def WithScale(self, with_scale: bool):
        """
        Setter for property: (bool) WithScale
         Returns the WithScale.  
           If true, the slider bar is shown.  
         
        """
        pass
    def GetBalloonTooltipLayoutMembers(self) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         Returns layout_strings (List[str]): Value to get from the property.
        """
        pass
    def GetDimensionalityMembers(self) -> List[str]:
        """
        Gets the members of Dimensionality enum.
         Returns dimension_strings (List[str]): Value to get from the property. .
        """
        pass
    def TestValueChanged(self, dimension_value: float) -> None:
        """
        Tests value changed event workflow mapped to this ExpressionBlock block.
        """
        pass
import NXOpen
class FaceCollector(UIBlock): 
    """ Represents a Face Collector"""
    @property
    def AllowConvergentObject(self) -> bool:
        """
        Getter for property: (bool) AllowConvergentObject
         Returns the AllowConvergentObject  
            
         
        """
        pass
    @AllowConvergentObject.setter
    def AllowConvergentObject(self, allowConvergentObject: bool):
        """
        Setter for property: (bool) AllowConvergentObject
         Returns the AllowConvergentObject  
            
         
        """
        pass
    @property
    def AllowConvergentObjectWithMixedGeometries(self) -> bool:
        """
        Getter for property: (bool) AllowConvergentObjectWithMixedGeometries
         Returns the AllowConvergentObjectWithMixedGeometries  
            
         
        """
        pass
    @AllowConvergentObjectWithMixedGeometries.setter
    def AllowConvergentObjectWithMixedGeometries(self, allowConvergentObjectWithMixedGeometries: bool):
        """
        Setter for property: (bool) AllowConvergentObjectWithMixedGeometries
         Returns the AllowConvergentObjectWithMixedGeometries  
            
         
        """
        pass
    @property
    def AutomaticProgression(self) -> bool:
        """
        Getter for property: (bool) AutomaticProgression
         Returns the AutomaticProgression.  
           If true, focus automatically progresses to the next selection block.  
         
        """
        pass
    @AutomaticProgression.setter
    def AutomaticProgression(self, automaticProgression: bool):
        """
        Setter for property: (bool) AutomaticProgression
         Returns the AutomaticProgression.  
           If true, focus automatically progresses to the next selection block.  
         
        """
        pass
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @property
    def Bitmap(self) -> str:
        """
        Getter for property: (str) Bitmap
         Returns the Bitmap  
            
         
        """
        pass
    @Bitmap.setter
    def Bitmap(self, bitmap_string: str):
        """
        Setter for property: (str) Bitmap
         Returns the Bitmap  
            
         
        """
        pass
    @property
    def BlendVirtualCurveOverlay(self) -> bool:
        """
        Getter for property: (bool) BlendVirtualCurveOverlay
         Returns the BlendVirtualCurveOverlay  
            
         
        """
        pass
    @BlendVirtualCurveOverlay.setter
    def BlendVirtualCurveOverlay(self, blendCurve: bool):
        """
        Setter for property: (bool) BlendVirtualCurveOverlay
         Returns the BlendVirtualCurveOverlay  
            
         
        """
        pass
    @property
    def CreateInterpartLink(self) -> bool:
        """
        Getter for property: (bool) CreateInterpartLink
         Returns the CreateInterpartLink  
            
         
        """
        pass
    @CreateInterpartLink.setter
    def CreateInterpartLink(self, createLink: bool):
        """
        Setter for property: (bool) CreateInterpartLink
         Returns the CreateInterpartLink  
            
         
        """
        pass
    @property
    def Cue(self) -> str:
        """
        Getter for property: (str) Cue
         Returns the Cue  
            
         
        """
        pass
    @Cue.setter
    def Cue(self, cue: str):
        """
        Setter for property: (str) Cue
         Returns the Cue  
            
         
        """
        pass
    @property
    def DefaultFaceRulesAsString(self) -> str:
        """
        Getter for property: (str) DefaultFaceRulesAsString
         Returns the DefaultFaceRules as string  
            
         
        """
        pass
    @DefaultFaceRulesAsString.setter
    def DefaultFaceRulesAsString(self, enumString: str):
        """
        Setter for property: (str) DefaultFaceRulesAsString
         Returns the DefaultFaceRules as string  
            
         
        """
        pass
    @property
    def EntityType(self) -> int:
        """
        Getter for property: (int) EntityType
         Returns the EntityType  
            
         
        """
        pass
    @EntityType.setter
    def EntityType(self, entityType: int):
        """
        Setter for property: (int) EntityType
         Returns the EntityType  
            
         
        """
        pass
    @property
    def FaceRules(self) -> int:
        """
        Getter for property: (int) FaceRules
         Returns the FaceRules  
            
         
        """
        pass
    @FaceRules.setter
    def FaceRules(self, faceRules: int):
        """
        Setter for property: (int) FaceRules
         Returns the FaceRules  
            
         
        """
        pass
    @property
    def InterpartSelectionAsString(self) -> str:
        """
        Getter for property: (str) InterpartSelectionAsString
         Returns the InterpartSelection as string  
            
         
        """
        pass
    @InterpartSelectionAsString.setter
    def InterpartSelectionAsString(self, enumString: str):
        """
        Setter for property: (str) InterpartSelectionAsString
         Returns the InterpartSelection as string  
            
         
        """
        pass
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
         Returns the LabelString  
            
         
        """
        pass
    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
         Returns the LabelString  
            
         
        """
        pass
    @property
    def MaximumScopeAsString(self) -> str:
        """
        Getter for property: (str) MaximumScopeAsString
         Returns the MaximumScope  
            
         
        """
        pass
    @MaximumScopeAsString.setter
    def MaximumScopeAsString(self, enumString: str):
        """
        Setter for property: (str) MaximumScopeAsString
         Returns the MaximumScope  
            
         
        """
        pass
    @property
    def PopupMenuEnabled(self) -> bool:
        """
        Getter for property: (bool) PopupMenuEnabled
         Returns the PopupMenuEnabled  
            
         
        """
        pass
    @PopupMenuEnabled.setter
    def PopupMenuEnabled(self, enabled: bool):
        """
        Setter for property: (bool) PopupMenuEnabled
         Returns the PopupMenuEnabled  
            
         
        """
        pass
    @property
    def SelectModeAsString(self) -> str:
        """
        Getter for property: (str) SelectModeAsString
         Returns the SelectMode as string  
            
         
        """
        pass
    @SelectModeAsString.setter
    def SelectModeAsString(self, enumString: str):
        """
        Setter for property: (str) SelectModeAsString
         Returns the SelectMode as string  
            
         
        """
        pass
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
         Returns the StepStatus as string  
            
         
        """
        pass
    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
         Returns the StepStatus as string  
            
         
        """
        pass
    @property
    def ToolTip(self) -> str:
        """
        Getter for property: (str) ToolTip
         Returns the ToolTip  
            
         
        """
        pass
    @ToolTip.setter
    def ToolTip(self, toolTip: str):
        """
        Setter for property: (str) ToolTip
         Returns the ToolTip  
            
         
        """
        pass
    def GetBalloonTooltipLayoutMembers(self) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         Returns layout_strings (List[str]): Value to get from the property. .
        """
        pass
    def GetCollectorObjectOfFaceCollector(self) -> NXOpen.ScCollector:
        """
         Get collector objects
         Returns collectorObject ( NXOpen.ScCollector): .
        """
        pass
    def GetDefaultFaceRulesMembers(self) -> List[str]:
        """
         Gets the DefaultFaceRules members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def GetInterpartSelectionMembers(self) -> List[str]:
        """
         Gets the InterpartSelection members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def GetSelectModeMembers(self) -> List[str]:
        """
         Gets the SelectMode members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def GetSelectedObjects(self) -> List[NXOpen.TaggedObject]:
        """
         Gets the SelectedObjects
         Returns objectVector ( NXOpen.TaggedObject Li): Value to get from the property.
        """
        pass
    def GetStepStatusMembers(self) -> List[str]:
        """
         Gets the StepStatus members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def SetCollectorObjectOfFaceCollector(self, collectorObject: NXOpen.ScCollector) -> None:
        """
         Set collector objects
        """
        pass
    def SetSelectedObjects(self, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the SelectedObjects
        """
        pass
    def TestSelection(self, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Tests the selection for this block. The block must be in focus to call this API
        """
        pass
class FileSelection(UIBlock): 
    """ Represents File Selection With Browse block"""
    @property
    def Filter(self) -> str:
        """
        Getter for property: (str) Filter
         Returns the Filter
                Format of the filter string, for a group of related filter extensions will be "Group 1(.  
          xxx;.yyy;.zzz),Group 2(.aaa;.bbb)" e.g."EPLAN files(.emp;.ema;.ems),Simulation Files(.sim;.fem)".
                For the individual filter extensions ".xxx,.yyy,.zzz" e.g. ".prt,.fem,.sim" will appear as "prt File (.prt)","sim File (.sim)" and "fem File (.fem)" respectively in the "Files of type" of file open dialog.
                  
         
        """
        pass
    @Filter.setter
    def Filter(self, filterString: str):
        """
        Setter for property: (str) Filter
         Returns the Filter
                Format of the filter string, for a group of related filter extensions will be "Group 1(.  
          xxx;.yyy;.zzz),Group 2(.aaa;.bbb)" e.g."EPLAN files(.emp;.ema;.ems),Simulation Files(.sim;.fem)".
                For the individual filter extensions ".xxx,.yyy,.zzz" e.g. ".prt,.fem,.sim" will appear as "prt File (.prt)","sim File (.sim)" and "fem File (.fem)" respectively in the "Files of type" of file open dialog.
                  
         
        """
        pass
    @property
    def Path(self) -> str:
        """
        Getter for property: (str) Path
         Returns the Path  
            
         
        """
        pass
    @Path.setter
    def Path(self, path: str):
        """
        Setter for property: (str) Path
         Returns the Path  
            
         
        """
        pass
    @property
    def RetainStringValue(self) -> bool:
        """
        Getter for property: (bool) RetainStringValue
         Returns the RetainStringValue  
            
         
        """
        pass
    @RetainStringValue.setter
    def RetainStringValue(self, retain_string_value: bool):
        """
        Setter for property: (bool) RetainStringValue
         Returns the RetainStringValue  
            
         
        """
        pass
    def TestPathSelected(self, path: str) -> None:
        """
        Tests file selected.
        """
        pass
class FolderSelection(UIBlock): 
    """ Represents Folder Selection With Browse block"""
    @property
    def Path(self) -> str:
        """
        Getter for property: (str) Path
         Returns the Path  
            
         
        """
        pass
    @Path.setter
    def Path(self, path: str):
        """
        Setter for property: (str) Path
         Returns the Path  
            
         
        """
        pass
    @property
    def RetainStringValue(self) -> bool:
        """
        Getter for property: (bool) RetainStringValue
         Returns the RetainStringValue  
            
         
        """
        pass
    @RetainStringValue.setter
    def RetainStringValue(self, retain_string_value: bool):
        """
        Setter for property: (bool) RetainStringValue
         Returns the RetainStringValue  
            
         
        """
        pass
    def TestPathSelected(self, path: str) -> None:
        """
        Tests folder selected.
        """
        pass
class Group(UIBlock): 
    """ Represents a Group Block"""
    @property
    def Column(self) -> int:
        """
        Getter for property: (int) Column
         Returns the Column  
            
         
        """
        pass
    @Column.setter
    def Column(self, num_column: int):
        """
        Setter for property: (int) Column
         Returns the Column  
            
         
        """
        pass
    @property
    def Localize(self) -> bool:
        """
        Getter for property: (bool) Localize
         Returns the Localize  
            
         
        """
        pass
    @Localize.setter
    def Localize(self, localize: bool):
        """
        Setter for property: (bool) Localize
         Returns the Localize  
            
         
        """
        pass
    @property
    def Members(self) -> PropertyList:
        """
        Getter for property: ( PropertyList NXOpen.B) Members
         Returns the Members  
            
         
        """
        pass
class IntegerBlock(UIBlock): 
    """ Represents a Integer block"""
    @property
    def AdaptiveScaleLimits(self) -> bool:
        """
        Getter for property: (bool) AdaptiveScaleLimits
         Returns the AdaptiveScaleLimits  
            
         
        """
        pass
    @AdaptiveScaleLimits.setter
    def AdaptiveScaleLimits(self, scale_limits: bool):
        """
        Setter for property: (bool) AdaptiveScaleLimits
         Returns the AdaptiveScaleLimits  
            
         
        """
        pass
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @property
    def Bitmap(self) -> str:
        """
        Getter for property: (str) Bitmap
         Returns the Bitmap  
            
         
        """
        pass
    @Bitmap.setter
    def Bitmap(self, bitmap_string: str):
        """
        Setter for property: (str) Bitmap
         Returns the Bitmap  
            
         
        """
        pass
    @property
    def Increment(self) -> float:
        """
        Getter for property: (float) Increment
         Returns the Increment  
            
         
        """
        pass
    @Increment.setter
    def Increment(self, increment: float):
        """
        Setter for property: (float) Increment
         Returns the Increment  
            
         
        """
        pass
    @property
    def LineIncrement(self) -> float:
        """
        Getter for property: (float) LineIncrement
         Returns the LineIncrement  
            
         
        """
        pass
    @LineIncrement.setter
    def LineIncrement(self, line_increment: float):
        """
        Setter for property: (float) LineIncrement
         Returns the LineIncrement  
            
         
        """
        pass
    @property
    def Localize(self) -> bool:
        """
        Getter for property: (bool) Localize
         Returns the Localize  
            
         
        """
        pass
    @Localize.setter
    def Localize(self, localize: bool):
        """
        Setter for property: (bool) Localize
         Returns the Localize  
            
         
        """
        pass
    @property
    def MaxInclusive(self) -> bool:
        """
        Getter for property: (bool) MaxInclusive
         Returns the MaxInclusive  
            
         
        """
        pass
    @MaxInclusive.setter
    def MaxInclusive(self, max_inclusive: bool):
        """
        Setter for property: (bool) MaxInclusive
         Returns the MaxInclusive  
            
         
        """
        pass
    @property
    def MaximumValue(self) -> int:
        """
        Getter for property: (int) MaximumValue
         Returns the MaximumValue  
            
         
        """
        pass
    @MaximumValue.setter
    def MaximumValue(self, max_value: int):
        """
        Setter for property: (int) MaximumValue
         Returns the MaximumValue  
            
         
        """
        pass
    @property
    def MinInclusive(self) -> bool:
        """
        Getter for property: (bool) MinInclusive
         Returns the MinInclusive  
            
         
        """
        pass
    @MinInclusive.setter
    def MinInclusive(self, min_inclusive: bool):
        """
        Setter for property: (bool) MinInclusive
         Returns the MinInclusive  
            
         
        """
        pass
    @property
    def MinimumValue(self) -> int:
        """
        Getter for property: (int) MinimumValue
         Returns the MinimumValue  
            
         
        """
        pass
    @MinimumValue.setter
    def MinimumValue(self, min_value: int):
        """
        Setter for property: (int) MinimumValue
         Returns the MinimumValue  
            
         
        """
        pass
    @property
    def PageIncrement(self) -> float:
        """
        Getter for property: (float) PageIncrement
         Returns the PageIncrement  
            
         
        """
        pass
    @PageIncrement.setter
    def PageIncrement(self, page_increment: float):
        """
        Setter for property: (float) PageIncrement
         Returns the PageIncrement  
            
         
        """
        pass
    @property
    def PresentationStyleAsString(self) -> str:
        """
        Getter for property: (str) PresentationStyleAsString
         Returns the PresentationStyle as string  
            
         
        """
        pass
    @PresentationStyleAsString.setter
    def PresentationStyleAsString(self, enumString: str):
        """
        Setter for property: (str) PresentationStyleAsString
         Returns the PresentationStyle as string  
            
         
        """
        pass
    @property
    def ReadOnlyValue(self) -> bool:
        """
        Getter for property: (bool) ReadOnlyValue
         Returns the ReadOnlyValue  
            
         
        """
        pass
    @ReadOnlyValue.setter
    def ReadOnlyValue(self, read_only: bool):
        """
        Setter for property: (bool) ReadOnlyValue
         Returns the ReadOnlyValue  
            
         
        """
        pass
    @property
    def RetainValue(self) -> bool:
        """
        Getter for property: (bool) RetainValue
         Returns the RetainValue  
            
         
        """
        pass
    @RetainValue.setter
    def RetainValue(self, retain: bool):
        """
        Setter for property: (bool) RetainValue
         Returns the RetainValue  
            
         
        """
        pass
    @property
    def ScaleLimits(self) -> bool:
        """
        Getter for property: (bool) ScaleLimits
         Returns the ScaleLimits  
            
         
        """
        pass
    @ScaleLimits.setter
    def ScaleLimits(self, scale_limits: bool):
        """
        Setter for property: (bool) ScaleLimits
         Returns the ScaleLimits  
            
         
        """
        pass
    @property
    def ScaleMaxLimitLabel(self) -> str:
        """
        Getter for property: (str) ScaleMaxLimitLabel
         Returns the ScaleMaxLimitLabel  
            
         
        """
        pass
    @ScaleMaxLimitLabel.setter
    def ScaleMaxLimitLabel(self, max_limit_label: str):
        """
        Setter for property: (str) ScaleMaxLimitLabel
         Returns the ScaleMaxLimitLabel  
            
         
        """
        pass
    @property
    def ScaleMinLimitLabel(self) -> str:
        """
        Getter for property: (str) ScaleMinLimitLabel
         Returns the ScaleMinLimitLabel  
            
         
        """
        pass
    @ScaleMinLimitLabel.setter
    def ScaleMinLimitLabel(self, min_limit_label: str):
        """
        Setter for property: (str) ScaleMinLimitLabel
         Returns the ScaleMinLimitLabel  
            
         
        """
        pass
    @property
    def ShowScaleValue(self) -> bool:
        """
        Getter for property: (bool) ShowScaleValue
         Returns the ShowScaleValue  
            
         
        """
        pass
    @ShowScaleValue.setter
    def ShowScaleValue(self, show_value: bool):
        """
        Setter for property: (bool) ShowScaleValue
         Returns the ShowScaleValue  
            
         
        """
        pass
    @property
    def TitleVisibility(self) -> bool:
        """
        Getter for property: (bool) TitleVisibility
         Returns the TitleVisibility  
            
         
        """
        pass
    @TitleVisibility.setter
    def TitleVisibility(self, visibility: bool):
        """
        Setter for property: (bool) TitleVisibility
         Returns the TitleVisibility  
            
         
        """
        pass
    @property
    def Value(self) -> int:
        """
        Getter for property: (int) Value
         Returns the Value  
            
         
        """
        pass
    @Value.setter
    def Value(self, integer_value: int):
        """
        Setter for property: (int) Value
         Returns the Value  
            
         
        """
        pass
    @property
    def WrapSpin(self) -> bool:
        """
        Getter for property: (bool) WrapSpin
         Returns the WrapSpin  
            
         
        """
        pass
    @WrapSpin.setter
    def WrapSpin(self, wrap_spin: bool):
        """
        Setter for property: (bool) WrapSpin
         Returns the WrapSpin  
            
         
        """
        pass
    def GetBalloonTooltipLayoutMembers(self) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         Returns layout_strings (List[str]): Value to get from the property. .
        """
        pass
    def GetComboOptions(self) -> List[int]:
        """
         Gets the ComboOptions
         Returns option_value (List[int]): .
        """
        pass
    def GetPresentationStyleMembers(self) -> List[str]:
        """
         Gets the PresentationStyle member 
         Returns member_strings (List[str]): Value to get for the property. .
        """
        pass
    def SetComboOptions(self, option_value: List[int]) -> None:
        """
         Sets the ComboOptions
        """
        pass
    def TestValueChanged(self, ineteger_value: int) -> None:
        """
        Tests value changed event workflow mapped to this IntegerBlock block.
        """
        pass
class IntegerTable(UIBlock): 
    """ Represents a Integer Table block"""
    @property
    def ColumnTitles(self) -> str:
        """
        Getter for property: (str) ColumnTitles
         Returns the ColumnTitles  
            
         
        """
        pass
    @ColumnTitles.setter
    def ColumnTitles(self, title: str):
        """
        Setter for property: (str) ColumnTitles
         Returns the ColumnTitles  
            
         
        """
        pass
    @property
    def Increment(self) -> float:
        """
        Getter for property: (float) Increment
         Returns the Increment.  
           Use this property only when Spin is true  
         
        """
        pass
    @Increment.setter
    def Increment(self, increment: float):
        """
        Setter for property: (float) Increment
         Returns the Increment.  
           Use this property only when Spin is true  
         
        """
        pass
    @property
    def RetainValue(self) -> bool:
        """
        Getter for property: (bool) RetainValue
         Returns the RetainValue.  
           If true, indicates that the values in the block would be stored in dialog memory upon OK, Apply or Close.   
         
        """
        pass
    @RetainValue.setter
    def RetainValue(self, retain: bool):
        """
        Setter for property: (bool) RetainValue
         Returns the RetainValue.  
           If true, indicates that the values in the block would be stored in dialog memory upon OK, Apply or Close.   
         
        """
        pass
    @property
    def Spin(self) -> bool:
        """
        Getter for property: (bool) Spin
         Returns the Spin  
            
         
        """
        pass
    @Spin.setter
    def Spin(self, spin: bool):
        """
        Setter for property: (bool) Spin
         Returns the Spin  
            
         
        """
        pass
    @property
    def WrapSpin(self) -> bool:
        """
        Getter for property: (bool) WrapSpin
         Returns the WrapSpin.  
           Use this property only when Spin is true  
         
        """
        pass
    @WrapSpin.setter
    def WrapSpin(self, wrap_spin: bool):
        """
        Setter for property: (bool) WrapSpin
         Returns the WrapSpin.  
           Use this property only when Spin is true  
         
        """
        pass
    @overload
    def GetColumnTitles(self) -> List[str]:
        """
         Gets the Column Tiltles
         Returns column_titles (List[str]): Column Title values to get from the property. .
        """
        pass
    def GetMaximumValues(self) -> Tuple[List[int], int, int]:
        """
         Gets the MaximumValues
         Returns A tuple consisting of (matrixValue, nRows, nColumns). 
         - matrixValue is: List[int].Values to get from the property .
         - nRows is: int. Number of Rows in the 2D matrix .
         - nColumns is: int. Number of Columns in the 2D matrix .

        """
        pass
    def GetMinimumValues(self) -> Tuple[List[int], int, int]:
        """
         Gets the MinimumValues
         Returns A tuple consisting of (matrixValue, nRows, nColumns). 
         - matrixValue is: List[int].Value to get for given property name. .
         - nRows is: int. Number of Rows in the 2D matrix .
         - nColumns is: int. Number of Columns in the 2D matrix .

        """
        pass
    def GetRowTitles(self) -> List[str]:
        """
         Gets the RowTitles
         Returns row_title (List[str]): Values to get from the property. .
        """
        pass
    def GetValues(self) -> Tuple[List[int], int, int]:
        """
         Gets the Values
         Returns A tuple consisting of (matrixValue, nRows, nColumns). 
         - matrixValue is: List[int].Values to get from the property. .
         - nRows is: int. Number of Rows in the 2D matrix .
         - nColumns is: int. Number of Columns in the 2D matrix .

        """
        pass
    @overload
    def SetColumnTitles(self, column_titles: List[str]) -> None:
        """
         Sets the Column Titles
        """
        pass
    def SetMaximumValues(self, nRows: int, nColumns: int, matrixValue: List[int]) -> None:
        """
         Sets the MaximumValues
        """
        pass
    def SetMinimumValues(self, nRows: int, nColumns: int, matrixValue: List[int]) -> None:
        """
         Sets the MinimumValues
        """
        pass
    def SetRowTitles(self, row_title: List[str]) -> None:
        """
         Sets the RowTitles
        """
        pass
    def SetValues(self, nRows: int, nColumns: int, matrixValue: List[int]) -> None:
        """
         Sets the Values
        """
        pass
    def TestValueChanged(self, nRows: int, nColumns: int, matrixValue: List[int]) -> None:
        """
        Tests value changed event workflow mapped to this IntegerTable block.
        """
        pass
class Label(UIBlock): 
    """ Represents a Label"""
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @BalloonTooltipText.setter
    def BalloonTooltipText(self, tooltipText: str):
        """
        Setter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @property
    def Bitmap(self) -> str:
        """
        Getter for property: (str) Bitmap
         Returns the Bitmap  
            
         
        """
        pass
    @Bitmap.setter
    def Bitmap(self, bitmap_string: str):
        """
        Setter for property: (str) Bitmap
         Returns the Bitmap  
            
         
        """
        pass
    @property
    def DisplayBitmapLabel(self) -> bool:
        """
        Getter for property: (bool) DisplayBitmapLabel
         Returns the DisplayBitmapLabel  
            
         
        """
        pass
    @DisplayBitmapLabel.setter
    def DisplayBitmapLabel(self, display: bool):
        """
        Setter for property: (bool) DisplayBitmapLabel
         Returns the DisplayBitmapLabel  
            
         
        """
        pass
    @property
    def HighQualityBitmap(self) -> bool:
        """
        Getter for property: (bool) HighQualityBitmap
         Returns the HighQualityBitmap  
            
         
        """
        pass
    @HighQualityBitmap.setter
    def HighQualityBitmap(self, high_quality: bool):
        """
        Setter for property: (bool) HighQualityBitmap
         Returns the HighQualityBitmap  
            
         
        """
        pass
    @property
    def Localize(self) -> bool:
        """
        Getter for property: (bool) Localize
         Returns the Localize.  
           If true, translates the Label string into the current locale language.  
         
        """
        pass
    @Localize.setter
    def Localize(self, localize: bool):
        """
        Setter for property: (bool) Localize
         Returns the Localize.  
           If true, translates the Label string into the current locale language.  
         
        """
        pass
    @property
    def Tooltip(self) -> str:
        """
        Getter for property: (str) Tooltip
         Returns the Tooltip  
            
         
        """
        pass
    @Tooltip.setter
    def Tooltip(self, tooltip_string: str):
        """
        Setter for property: (str) Tooltip
         Returns the Tooltip  
            
         
        """
        pass
    @property
    def WordWrap(self) -> bool:
        """
        Getter for property: (bool) WordWrap
         Returns the WordWrap  
            
         
        """
        pass
    @WordWrap.setter
    def WordWrap(self, wordwrap: bool):
        """
        Setter for property: (bool) WordWrap
         Returns the WordWrap  
            
         
        """
        pass
    def GetBalloonTooltipLayoutMembers(self) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         Returns layout_strings (List[str]): Values to get from the property .
        """
        pass
class LayerBlock(UIBlock): 
    """ Represents a Layer block"""
    @property
    def LayerOption(self) -> int:
        """
        Getter for property: (int) LayerOption
         Returns the Layer Option  
            
         
        """
        pass
    @LayerOption.setter
    def LayerOption(self, integer_layer_option: int):
        """
        Setter for property: (int) LayerOption
         Returns the Layer Option  
            
         
        """
        pass
    @property
    def LayerValue(self) -> int:
        """
        Getter for property: (int) LayerValue
         Returns the Layer Value  
            
         
        """
        pass
    @LayerValue.setter
    def LayerValue(self, integer_layer_value: int):
        """
        Setter for property: (int) LayerValue
         Returns the Layer Value  
            
         
        """
        pass
    @property
    def ShowMaintainLayerOption(self) -> bool:
        """
        Getter for property: (bool) ShowMaintainLayerOption
         Returns the Show Maintain Layer Option
                If set to true, Maintain option is displayed in layer options  
            
         
        """
        pass
    @ShowMaintainLayerOption.setter
    def ShowMaintainLayerOption(self, show_maintain_layer_option: bool):
        """
        Setter for property: (bool) ShowMaintainLayerOption
         Returns the Show Maintain Layer Option
                If set to true, Maintain option is displayed in layer options  
            
         
        """
        pass
    @property
    def ShowOriginalLayerOption(self) -> bool:
        """
        Getter for property: (bool) ShowOriginalLayerOption
         Returns the Show Original Layer Option
                If set to true, Original option is displayed in layer options  
            
         
        """
        pass
    @ShowOriginalLayerOption.setter
    def ShowOriginalLayerOption(self, show_original_layer_option: bool):
        """
        Setter for property: (bool) ShowOriginalLayerOption
         Returns the Show Original Layer Option
                If set to true, Original option is displayed in layer options  
            
         
        """
        pass
    @property
    def ShowUserDefinedLayerOption(self) -> bool:
        """
        Getter for property: (bool) ShowUserDefinedLayerOption
         Returns the Show User Defined Layer Option
                If set to true, User Defined option is displayed in layer options  
            
         
        """
        pass
    @ShowUserDefinedLayerOption.setter
    def ShowUserDefinedLayerOption(self, show_user_defined_layer_option: bool):
        """
        Setter for property: (bool) ShowUserDefinedLayerOption
         Returns the Show User Defined Layer Option
                If set to true, User Defined option is displayed in layer options  
            
         
        """
        pass
    @property
    def ShowWorkLayerOption(self) -> bool:
        """
        Getter for property: (bool) ShowWorkLayerOption
         Returns the Show Work Layer Option
                If set to true, Work option is displayed in layer options  
            
         
        """
        pass
    @ShowWorkLayerOption.setter
    def ShowWorkLayerOption(self, show_work_layer_option: bool):
        """
        Setter for property: (bool) ShowWorkLayerOption
         Returns the Show Work Layer Option
                If set to true, Work option is displayed in layer options  
            
         
        """
        pass
    def TestOptionChanged(self, integer_layer_option: int) -> None:
        """
        Tests option changed event workflow mapped to this layer block.
        """
        pass
    def TestValueChanged(self, ineteger_layer_value: int) -> None:
        """
        Tests value changed event workflow mapped to this LayerBlock block.
        """
        pass
import NXOpen
class LinearDimension(UIBlock): 
    """ Represents a Linear Dimension block"""
    @property
    def AdaptiveScaleLimits(self) -> bool:
        """
        Getter for property: (bool) AdaptiveScaleLimits
         Returnsthe AdaptiveScaleLimits.  
          
                If true, indicates that the scale should be adaptive.  
         
        """
        pass
    @AdaptiveScaleLimits.setter
    def AdaptiveScaleLimits(self, scale_limits: bool):
        """
        Setter for property: (bool) AdaptiveScaleLimits
         Returnsthe AdaptiveScaleLimits.  
          
                If true, indicates that the scale should be adaptive.  
         
        """
        pass
    @property
    def AutoReverseDuringDrag(self) -> bool:
        """
        Getter for property: (bool) AutoReverseDuringDrag
         Returns the AutoReverseDuringDrag.  
           If true, the linear dimension handle reverses its direction when it is dragged through the 0 value.  
         
        """
        pass
    @AutoReverseDuringDrag.setter
    def AutoReverseDuringDrag(self, auto_reverse: bool):
        """
        Setter for property: (bool) AutoReverseDuringDrag
         Returns the AutoReverseDuringDrag.  
           If true, the linear dimension handle reverses its direction when it is dragged through the 0 value.  
         
        """
        pass
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @property
    def ExpressionObject(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) ExpressionObject
         Returns the ExpressionObject  
            
         
        """
        pass
    @ExpressionObject.setter
    def ExpressionObject(self, expression_obj: NXOpen.TaggedObject):
        """
        Setter for property: ( NXOpen.TaggedObject) ExpressionObject
         Returns the ExpressionObject  
            
         
        """
        pass
    @property
    def Formula(self) -> str:
        """
        Getter for property: (str) Formula
         Returns the Formula  
            
         
        """
        pass
    @Formula.setter
    def Formula(self, formula: str):
        """
        Setter for property: (str) Formula
         Returns the Formula  
            
         
        """
        pass
    @property
    def HandleOrientation(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) HandleOrientation
         Returns the HandleOrientation  
            
         
        """
        pass
    @HandleOrientation.setter
    def HandleOrientation(self, orientation: NXOpen.Vector3d):
        """
        Setter for property: ( NXOpen.Vector3d) HandleOrientation
         Returns the HandleOrientation  
            
         
        """
        pass
    @property
    def HandleOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) HandleOrigin
         Returns the HandleOrigin  
            
         
        """
        pass
    @HandleOrigin.setter
    def HandleOrigin(self, handle_orogin: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) HandleOrigin
         Returns the HandleOrigin  
            
         
        """
        pass
    @property
    def LineIncrement(self) -> float:
        """
        Getter for property: (float) LineIncrement
         Returnsthe LineIncrement value.  
          
                Specifies the incrementdecrement when the user presses the arrow keys on the keyboard.
                Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
         
        """
        pass
    @LineIncrement.setter
    def LineIncrement(self, line_increment: float):
        """
        Setter for property: (float) LineIncrement
         Returnsthe LineIncrement value.  
          
                Specifies the incrementdecrement when the user presses the arrow keys on the keyboard.
                Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
         
        """
        pass
    @property
    def MaxInclusive(self) -> bool:
        """
        Getter for property: (bool) MaxInclusive
         Returns the MaxInclusive  
            
         
        """
        pass
    @MaxInclusive.setter
    def MaxInclusive(self, max_inclusive: bool):
        """
        Setter for property: (bool) MaxInclusive
         Returns the MaxInclusive  
            
         
        """
        pass
    @property
    def MaximumValue(self) -> float:
        """
        Getter for property: (float) MaximumValue
         Returns the MaximumValue  
            
         
        """
        pass
    @MaximumValue.setter
    def MaximumValue(self, max_value: float):
        """
        Setter for property: (float) MaximumValue
         Returns the MaximumValue  
            
         
        """
        pass
    @property
    def MinInclusive(self) -> bool:
        """
        Getter for property: (bool) MinInclusive
         Returns the MinInclusive  
            
         
        """
        pass
    @MinInclusive.setter
    def MinInclusive(self, min_inclusive: bool):
        """
        Setter for property: (bool) MinInclusive
         Returns the MinInclusive  
            
         
        """
        pass
    @property
    def MinimumValue(self) -> float:
        """
        Getter for property: (float) MinimumValue
         Returns the MinimumValue  
            
         
        """
        pass
    @MinimumValue.setter
    def MinimumValue(self, min_value: float):
        """
        Setter for property: (float) MinimumValue
         Returns the MinimumValue  
            
         
        """
        pass
    @property
    def PageIncrement(self) -> float:
        """
        Getter for property: (float) PageIncrement
         Returnsthe PageIncrement value.  
          
                Specifies the incrementdecrement when the user presses the Page Up or Page Down keys on the keyboard.
                Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
         
        """
        pass
    @PageIncrement.setter
    def PageIncrement(self, page_increment: float):
        """
        Setter for property: (float) PageIncrement
         Returnsthe PageIncrement value.  
          
                Specifies the incrementdecrement when the user presses the Page Up or Page Down keys on the keyboard.
                Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
         
        """
        pass
    @property
    def ShowFocusHandle(self) -> bool:
        """
        Getter for property: (bool) ShowFocusHandle
         Returns the ShowFocusHandle  
            
         
        """
        pass
    @ShowFocusHandle.setter
    def ShowFocusHandle(self, show_focus: bool):
        """
        Setter for property: (bool) ShowFocusHandle
         Returns the ShowFocusHandle  
            
         
        """
        pass
    @property
    def ShowHandle(self) -> bool:
        """
        Getter for property: (bool) ShowHandle
         Returns the ShowHandle.  
           If true, linear dimension handle is visible  
         
        """
        pass
    @ShowHandle.setter
    def ShowHandle(self, show_handle: bool):
        """
        Setter for property: (bool) ShowHandle
         Returns the ShowHandle.  
           If true, linear dimension handle is visible  
         
        """
        pass
    @property
    def SnapPointTypesOnByDefault(self) -> int:
        """
        Getter for property: (int) SnapPointTypesOnByDefault
         Returns the SnapPointTypesOnByDefault  
            
         
        """
        pass
    @SnapPointTypesOnByDefault.setter
    def SnapPointTypesOnByDefault(self, point_type: int):
        """
        Setter for property: (int) SnapPointTypesOnByDefault
         Returns the SnapPointTypesOnByDefault  
            
         
        """
        pass
    @property
    def Units(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) Units
         Returns the Units  
            
         
        """
        pass
    @Units.setter
    def Units(self, units: NXOpen.TaggedObject):
        """
        Setter for property: ( NXOpen.TaggedObject) Units
         Returns the Units  
            
         
        """
        pass
    @property
    def Value(self) -> float:
        """
        Getter for property: (float) Value
         Returns the Value.  
            
         
        """
        pass
    @Value.setter
    def Value(self, dimension_value: float):
        """
        Setter for property: (float) Value
         Returns the Value.  
            
         
        """
        pass
    @property
    def WithScale(self) -> bool:
        """
        Getter for property: (bool) WithScale
         Returns the WithScale.  
           If true, the slider bar is shown.  
         
        """
        pass
    @WithScale.setter
    def WithScale(self, with_scale: bool):
        """
        Setter for property: (bool) WithScale
         Returns the WithScale.  
           If true, the slider bar is shown.  
         
        """
        pass
    def GetBalloonTooltipLayoutMembers(self) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         Returns layout_strings (List[str]): Values to get from the property. .
        """
        pass
    def TestValueChanged(self, dimension_value: float) -> None:
        """
        Tests value changed event workflow mapped to this LinearDimension block.
        """
        pass
class LineColorFontWidth(UIBlock): 
    """ Represents a Line Width block"""
    @property
    def HideSubBlocksAsString(self) -> str:
        """
        Getter for property: (str) HideSubBlocksAsString
         Returns the hide sub block.  
            
         
        """
        pass
    @HideSubBlocksAsString.setter
    def HideSubBlocksAsString(self, hideSubBlocksString: str):
        """
        Setter for property: (str) HideSubBlocksAsString
         Returns the hide sub block.  
            
         
        """
        pass
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
         Returns the Label String in horizontal layout.  
            
         
        """
        pass
    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
         Returns the Label String in horizontal layout.  
            
         
        """
        pass
    @property
    def LayoutAsString(self) -> str:
        """
        Getter for property: (str) LayoutAsString
         Returns the layout.  
            
         
        """
        pass
    @LayoutAsString.setter
    def LayoutAsString(self, layoutString: str):
        """
        Setter for property: (str) LayoutAsString
         Returns the layout.  
            
         
        """
        pass
    @property
    def LineFontAvailableOptions(self) -> int:
        """
        Getter for property: (int) LineFontAvailableOptions
         Returns the Line Font Available Options  
            
         
        """
        pass
    @LineFontAvailableOptions.setter
    def LineFontAvailableOptions(self, lineFontAvailableOptions: int):
        """
        Setter for property: (int) LineFontAvailableOptions
         Returns the Line Font Available Options  
            
         
        """
        pass
    @property
    def LineFontValueAsString(self) -> str:
        """
        Getter for property: (str) LineFontValueAsString
         Returns the Line Font Value.  
            
         
        """
        pass
    @LineFontValueAsString.setter
    def LineFontValueAsString(self, fontValueString: str):
        """
        Setter for property: (str) LineFontValueAsString
         Returns the Line Font Value.  
            
         
        """
        pass
    @property
    def LineWidthShowDefault(self) -> bool:
        """
        Getter for property: (bool) LineWidthShowDefault
         Returns the Line width Show Default  
            
         
        """
        pass
    @LineWidthShowDefault.setter
    def LineWidthShowDefault(self, lineWidthShowDefault: bool):
        """
        Setter for property: (bool) LineWidthShowDefault
         Returns the Line width Show Default  
            
         
        """
        pass
    @property
    def LineWidthShowDefaultAsOriginal(self) -> bool:
        """
        Getter for property: (bool) LineWidthShowDefaultAsOriginal
         Returns the Line Width Show Default as Original  
            
         
        """
        pass
    @LineWidthShowDefaultAsOriginal.setter
    def LineWidthShowDefaultAsOriginal(self, lineWidthShowDefaultAsOriginal: bool):
        """
        Setter for property: (bool) LineWidthShowDefaultAsOriginal
         Returns the Line Width Show Default as Original  
            
         
        """
        pass
    @property
    def LineWidthShowNoChange(self) -> bool:
        """
        Getter for property: (bool) LineWidthShowNoChange
         Returns the Line Width Show No Change  
            
         
        """
        pass
    @LineWidthShowNoChange.setter
    def LineWidthShowNoChange(self, lineWidthShowNoChange: bool):
        """
        Setter for property: (bool) LineWidthShowNoChange
         Returns the Line Width Show No Change  
            
         
        """
        pass
    @property
    def LineWidthUseWideLines(self) -> bool:
        """
        Getter for property: (bool) LineWidthUseWideLines
         Returns the Line Width Use Wide Lines  
            
         
        """
        pass
    @LineWidthUseWideLines.setter
    def LineWidthUseWideLines(self, lineWidthUseWideLines: bool):
        """
        Setter for property: (bool) LineWidthUseWideLines
         Returns the Line Width Use Wide Lines  
            
         
        """
        pass
    @property
    def LineWidthValue(self) -> int:
        """
        Getter for property: (int) LineWidthValue
         Returnsthe LineWidthValue  
            
         
        """
        pass
    @LineWidthValue.setter
    def LineWidthValue(self, width_value: int):
        """
        Setter for property: (int) LineWidthValue
         Returnsthe LineWidthValue  
            
         
        """
        pass
    @property
    def ShowLabel(self) -> bool:
        """
        Getter for property: (bool) ShowLabel
         Returns the Show Label flag.  
          
                If true, the block label is shown in horizontal layout.  
         
        """
        pass
    @ShowLabel.setter
    def ShowLabel(self, showLabel: bool):
        """
        Setter for property: (bool) ShowLabel
         Returns the Show Label flag.  
          
                If true, the block label is shown in horizontal layout.  
         
        """
        pass
    def GetColorValue(self) -> List[int]:
        """
         Gets line color values
         Returns colorValueVector (List[int]): color values to get from the property.
        """
        pass
    def SetColorValue(self, colorValueVector: List[int]) -> None:
        """
         Sets line color values
        """
        pass
    def TestColorValueChanged(self, colorValueVector: List[int]) -> None:
        """
        Tests color value changed event workflow mapped to this LineColorFontWidth block. Invokes the client notifiers to simulate UI like event.
        """
        pass
    def TestFontValueChanged(self, fontValueString: str) -> None:
        """
        Tests font value changed event workflow mapped to this LineColorFontWidth block.
        """
        pass
    def TestWidthValueChanged(self, width_value: int) -> None:
        """
        Tests width value changed event workflow mapped to this LineColorFontWidth block.
        """
        pass
class LineFont(UIBlock): 
    """ Represents a Line Width block"""
    @property
    def AvailableOptions(self) -> int:
        """
        Getter for property: (int) AvailableOptions
         Returns the Available Options  
            
         
        """
        pass
    @AvailableOptions.setter
    def AvailableOptions(self, availableOptions: int):
        """
        Setter for property: (int) AvailableOptions
         Returns the Available Options  
            
         
        """
        pass
    @property
    def ShowOptionLabels(self) -> bool:
        """
        Getter for property: (bool) ShowOptionLabels
         Returns the show option labels  
            
         
        """
        pass
    @ShowOptionLabels.setter
    def ShowOptionLabels(self, showOptionLabels: bool):
        """
        Setter for property: (bool) ShowOptionLabels
         Returns the show option labels  
            
         
        """
        pass
    @property
    def ValueAsString(self) -> str:
        """
        Getter for property: (str) ValueAsString
         Returns the value  
            
         
        """
        pass
    @ValueAsString.setter
    def ValueAsString(self, fontValueString: str):
        """
        Setter for property: (str) ValueAsString
         Returns the value  
            
         
        """
        pass
    def TestValueChanged(self, fontValueString: str) -> None:
        """
        Tests value changed event workflow mapped to this LineFont block.
        """
        pass
class LineWidth(UIBlock): 
    """ Represents a Line Width block"""
    @property
    def AllowDefaultWidth(self) -> bool:
        """
        Getter for property: (bool) AllowDefaultWidth
         Returns the AllowDefaultWidth  
            
         
        """
        pass
    @property
    def AllowNoChangeWidth(self) -> bool:
        """
        Getter for property: (bool) AllowNoChangeWidth
         Returns the AllowNoChangeWidth.  
           If true, no change in width is allowed.  
         
        """
        pass
    @property
    def LabelVisibility(self) -> bool:
        """
        Getter for property: (bool) LabelVisibility
         Returns the LabelVisibility  
            
         
        """
        pass
    @LabelVisibility.setter
    def LabelVisibility(self, visible: bool):
        """
        Setter for property: (bool) LabelVisibility
         Returns the LabelVisibility  
            
         
        """
        pass
    @property
    def LineWidthValue(self) -> int:
        """
        Getter for property: (int) LineWidthValue
         Returns the LineWidthValue  
            
         
        """
        pass
    @LineWidthValue.setter
    def LineWidthValue(self, width_value: int):
        """
        Setter for property: (int) LineWidthValue
         Returns the LineWidthValue  
            
         
        """
        pass
    @property
    def ShowDefaultAsOriginal(self) -> bool:
        """
        Getter for property: (bool) ShowDefaultAsOriginal
         Returns the ShowDefaultAsOriginal.  
           If true, default entry is shown as original.  
         
        """
        pass
    def TestValueChanged(self, width_value: int) -> None:
        """
        Tests value changed event workflow mapped to this LineWidth block.
        """
        pass
class ListBox(UIBlock): 
    """ Represents a ListBox block """
    @property
    def AllowDeselectForSingleSelect(self) -> bool:
        """
        Getter for property: (bool) AllowDeselectForSingleSelect
         Returns the AllowDeselectForSingleSelect.  
           Allows deselection of item using Ctrl+MB1 when single select is true.  
         
        """
        pass
    @AllowDeselectForSingleSelect.setter
    def AllowDeselectForSingleSelect(self, allow: bool):
        """
        Setter for property: (bool) AllowDeselectForSingleSelect
         Returns the AllowDeselectForSingleSelect.  
           Allows deselection of item using Ctrl+MB1 when single select is true.  
         
        """
        pass
    @property
    def Height(self) -> int:
        """
        Getter for property: (int) Height
         Returns the Height  
            
         
        """
        pass
    @Height.setter
    def Height(self, height: int):
        """
        Setter for property: (int) Height
         Returns the Height  
            
         
        """
        pass
    @property
    def IsAddButtonSensitive(self) -> bool:
        """
        Getter for property: (bool) IsAddButtonSensitive
         Returns the IsAddButtonSensitive  
            
         
        """
        pass
    @IsAddButtonSensitive.setter
    def IsAddButtonSensitive(self, sensitive: bool):
        """
        Setter for property: (bool) IsAddButtonSensitive
         Returns the IsAddButtonSensitive  
            
         
        """
        pass
    @property
    def IsDeleteButtonSensitive(self) -> bool:
        """
        Getter for property: (bool) IsDeleteButtonSensitive
         Returns the IsDeleteButtonSensitive  
            
         
        """
        pass
    @IsDeleteButtonSensitive.setter
    def IsDeleteButtonSensitive(self, sesitive: bool):
        """
        Setter for property: (bool) IsDeleteButtonSensitive
         Returns the IsDeleteButtonSensitive  
            
         
        """
        pass
    @property
    def Localize(self) -> bool:
        """
        Getter for property: (bool) Localize
         Returns the Localize.  
           If true, translates the Label string into the language of the current locale.  
         
        """
        pass
    @Localize.setter
    def Localize(self, localize: bool):
        """
        Setter for property: (bool) Localize
         Returns the Localize.  
           If true, translates the Label string into the language of the current locale.  
         
        """
        pass
    @property
    def MaximumHeight(self) -> int:
        """
        Getter for property: (int) MaximumHeight
         Returns the MaximumHeight  
            
         
        """
        pass
    @MaximumHeight.setter
    def MaximumHeight(self, max_height: int):
        """
        Setter for property: (int) MaximumHeight
         Returns the MaximumHeight  
            
         
        """
        pass
    @property
    def MaximumStringLength(self) -> int:
        """
        Getter for property: (int) MaximumStringLength
         Returns the MaximumStringLength  
            
         
        """
        pass
    @MaximumStringLength.setter
    def MaximumStringLength(self, max_length: int):
        """
        Setter for property: (int) MaximumStringLength
         Returns the MaximumStringLength  
            
         
        """
        pass
    @property
    def MinimumHeight(self) -> int:
        """
        Getter for property: (int) MinimumHeight
         Returns the MinimumHeight  
            
         
        """
        pass
    @MinimumHeight.setter
    def MinimumHeight(self, min_height: int):
        """
        Setter for property: (int) MinimumHeight
         Returns the MinimumHeight  
            
         
        """
        pass
    @property
    def ResizeHeightWithDialog(self) -> bool:
        """
        Getter for property: (bool) ResizeHeightWithDialog
         Returns the ResizeHeightWithDialog  
            
         
        """
        pass
    @ResizeHeightWithDialog.setter
    def ResizeHeightWithDialog(self, resize: bool):
        """
        Setter for property: (bool) ResizeHeightWithDialog
         Returns the ResizeHeightWithDialog  
            
         
        """
        pass
    @property
    def SelectedItemIndex(self) -> int:
        """
        Getter for property: (int) SelectedItemIndex
         Returns the SelectedItemIndex.  
           Valid only if SingleSelect is true. Otherwise -1 is returned.  
         
        """
        pass
    @SelectedItemIndex.setter
    def SelectedItemIndex(self, index: int):
        """
        Setter for property: (int) SelectedItemIndex
         Returns the SelectedItemIndex.  
           Valid only if SingleSelect is true. Otherwise -1 is returned.  
         
        """
        pass
    @property
    def SelectedItemString(self) -> str:
        """
        Getter for property: (str) SelectedItemString
         Returns the SelectedItemString.  
           Valid only if SingleSelect is true. Otherwise empty string is returned.  
         
        """
        pass
    @SelectedItemString.setter
    def SelectedItemString(self, string: str):
        """
        Setter for property: (str) SelectedItemString
         Returns the SelectedItemString.  
           Valid only if SingleSelect is true. Otherwise empty string is returned.  
         
        """
        pass
    @property
    def ShowAddButton(self) -> bool:
        """
        Getter for property: (bool) ShowAddButton
         Returns the ShowAddButton.  
           If true, Add button is shown.  
         
        """
        pass
    @ShowAddButton.setter
    def ShowAddButton(self, show: bool):
        """
        Setter for property: (bool) ShowAddButton
         Returns the ShowAddButton.  
           If true, Add button is shown.  
         
        """
        pass
    @property
    def ShowDeleteButton(self) -> bool:
        """
        Getter for property: (bool) ShowDeleteButton
         Returns the ShowDeleteButton.  
           If true, Delete button is shown.  
         
        """
        pass
    @ShowDeleteButton.setter
    def ShowDeleteButton(self, show: bool):
        """
        Setter for property: (bool) ShowDeleteButton
         Returns the ShowDeleteButton.  
           If true, Delete button is shown.  
         
        """
        pass
    @property
    def ShowMoveUpDownButtons(self) -> bool:
        """
        Getter for property: (bool) ShowMoveUpDownButtons
         Returns the ShowMoveUpDownButtons.  
           If true, MoveUp and MoveDown buttons are shown.  
         
        """
        pass
    @ShowMoveUpDownButtons.setter
    def ShowMoveUpDownButtons(self, show: bool):
        """
        Setter for property: (bool) ShowMoveUpDownButtons
         Returns the ShowMoveUpDownButtons.  
           If true, MoveUp and MoveDown buttons are shown.  
         
        """
        pass
    @property
    def SingleSelect(self) -> bool:
        """
        Getter for property: (bool) SingleSelect
         Returns the SingleSelect.  
           If true, only single item can be selected.  
         
        """
        pass
    @SingleSelect.setter
    def SingleSelect(self, sinle_select: bool):
        """
        Setter for property: (bool) SingleSelect
         Returns the SingleSelect.  
           If true, only single item can be selected.  
         
        """
        pass
    AddCallback = Callable[[ListBox], None]
    DeleteCallback = Callable[[ListBox], None]
    def GetListItems(self) -> List[str]:
        """
         Gets the ListItems
         Returns items (List[str]): .
        """
        pass
    def GetSelectedItemBooleans(self) -> List[int]:
        """
         Gets the SelectedItemBooleans. This method returns an integer array of boolen values populated with 0 and 1
         Returns items (List[int]): .
        """
        pass
    def GetSelectedItemStrings(self) -> List[str]:
        """
         Gets the SelectedItemStrings
         Returns strings (List[str]): .
        """
        pass
    def GetSelectedItems(self) -> List[int]:
        """
         Gets SelectedItems
         Returns selected_items (List[int]):  selected items.
        """
        pass
    def SetAddHandler(self, cb: ListBox.AddCallback) -> None:
        """
         Sets the Add handler.  This handler is called when the Add button is pressed.
            The handler is responsible for adding an item to the list.  Nothing will be added to the list unless the handler
            adds it. 
        """
        pass
    def SetDeleteHandler(self, cb: ListBox.DeleteCallback) -> None:
        """
         Sets the Delete handler.  If you set this handler, the handler will be
            called when the Delete button is pressed.  The handler does not need to implement code
            to delete the item.  The list will delete the selected items if and only if the handler returns 0. 
        """
        pass
    def SetListItems(self, items: List[str]) -> None:
        """
         Sets the ListItems
        """
        pass
    def SetSelectedItemBooleans(self, items: List[int]) -> None:
        """
         Sets the SelectedItemStrings. Selects the list items based on input boolean array. Item is deselcted if value is 0 and selected otherwise.
        """
        pass
    def SetSelectedItemStrings(self, strings: List[str]) -> None:
        """
         Sets the SelectedItemStrings. Selects the list items based on input array of strings.
        """
        pass
    def SetSelectedItems(self, selected_items: List[int]) -> None:
        """
         Sets SelectedItems
        """
        pass
    def TestAddItem(self) -> None:
        """
        Tests item added event mapped to this ListBox block.
        """
        pass
    def TestDeleteItem(self) -> None:
        """
        Tests item delete event mapped to this ListBox block.
        """
        pass
import NXOpen
class MessageBoxTester(NXOpen.TransientObject): 
    """ Class for validating NXMessageBox. Helpful for writing test cases on UI code. By default all message boxes are suppressed during Automated Testing except Question message boxes.
    The class provides interface to validate message boxes that user is expecting to hit. It also provides interface to set choices for question message box."""
    class Response(Enum):
        """
        Members Include: 
         |NotQuestion|  Not a question message box.
         |Yes|  NXMessageBox.Show will return 1 for yes for NXMessageBox.DialogType.Question type message box
         |No|  NXMessageBox.Show will return 2 for yes for NXMessageBox.DialogType.Question type message box

        """
        NotQuestion: int
        Yes: int
        No: int
        @staticmethod
        def ValueOf(value: int) -> MessageBoxTester.Response:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def SequenceCheck(self) -> bool:
        """
        Getter for property: (bool) SequenceCheck
         Returns the strict sequence checking flag for message validation.  
           The sequence works in LIFO manner. When set to true, messages will be popped back from the input sequence.
                By default, the messages are picked by searching from input sequence.  
         
        """
        pass
    @SequenceCheck.setter
    def SequenceCheck(self, check: bool):
        """
        Setter for property: (bool) SequenceCheck
         Returns the strict sequence checking flag for message validation.  
           The sequence works in LIFO manner. When set to true, messages will be popped back from the input sequence.
                By default, the messages are picked by searching from input sequence.  
         
        """
        pass
    def Dispose(self) -> None:
        """
         Disposes the object.
        """
        pass
    def SuppressAllQuestionMessageBox(self, choice: MessageBoxTester.Response) -> None:
        """
         Suppress all NXMessageBox.DialogType.Question messages with a default choice
        """
        pass
    def Validate(self, title: str, msgbox_type: NXOpen.NXMessageBox.DialogType, messages: List[str], choice: MessageBoxTester.Response) -> None:
        """
         Adds a specific message for validation with given details. This method matches both message title and body.
        """
        pass
    def ValidateIgnoreBody(self, title: str, msgbox_type: NXOpen.NXMessageBox.DialogType, choice: MessageBoxTester.Response) -> None:
        """
         Adds a specific message for validation with given details. Use this method when matching message body is not required
        """
        pass
class Microposition(UIBlock): 
    """ Represents a Microposition block"""
    pass
class MultilineString(UIBlock): 
    """ Represents a Multiline String block """
    @property
    def Height(self) -> int:
        """
        Getter for property: (int) Height
         Returns the Height  
            
         
        """
        pass
    @Height.setter
    def Height(self, height: int):
        """
        Setter for property: (int) Height
         Returns the Height  
            
         
        """
        pass
    @property
    def Localize(self) -> bool:
        """
        Getter for property: (bool) Localize
         Returns the Localize.  
           If true, the Label is translated to current locale language  
         
        """
        pass
    @Localize.setter
    def Localize(self, localize: bool):
        """
        Setter for property: (bool) Localize
         Returns the Localize.  
           If true, the Label is translated to current locale language  
         
        """
        pass
    @property
    def MaximumCharactersAccepted(self) -> int:
        """
        Getter for property: (int) MaximumCharactersAccepted
         Returns the MaximumCharactersAccepted  
            
         
        """
        pass
    @MaximumCharactersAccepted.setter
    def MaximumCharactersAccepted(self, max_char: int):
        """
        Setter for property: (int) MaximumCharactersAccepted
         Returns the MaximumCharactersAccepted  
            
         
        """
        pass
    @property
    def MaximumHeight(self) -> int:
        """
        Getter for property: (int) MaximumHeight
         Returns the MaximumHeight  
            
         
        """
        pass
    @MaximumHeight.setter
    def MaximumHeight(self, max_height: int):
        """
        Setter for property: (int) MaximumHeight
         Returns the MaximumHeight  
            
         
        """
        pass
    @property
    def MinimumHeight(self) -> int:
        """
        Getter for property: (int) MinimumHeight
         Returns the MinimumHeight  
            
         
        """
        pass
    @MinimumHeight.setter
    def MinimumHeight(self, min_height: int):
        """
        Setter for property: (int) MinimumHeight
         Returns the MinimumHeight  
            
         
        """
        pass
    @property
    def ResizeHeightWithDialog(self) -> bool:
        """
        Getter for property: (bool) ResizeHeightWithDialog
         Returns the ResizeHeightWithDialog.  
           If true, height of block will dynamically change when the dialog is resized.  
         
        """
        pass
    @ResizeHeightWithDialog.setter
    def ResizeHeightWithDialog(self, resize: bool):
        """
        Setter for property: (bool) ResizeHeightWithDialog
         Returns the ResizeHeightWithDialog.  
           If true, height of block will dynamically change when the dialog is resized.  
         
        """
        pass
    @property
    def RetainValue(self) -> bool:
        """
        Getter for property: (bool) RetainValue
         Returns the RetainValue  
            
         
        """
        pass
    @RetainValue.setter
    def RetainValue(self, retain: bool):
        """
        Setter for property: (bool) RetainValue
         Returns the RetainValue  
            
         
        """
        pass
    @property
    def ValuesConcatenated(self) -> str:
        """
        Getter for property: (str) ValuesConcatenated
         Returns the ValuesConcatenated.  
           Represents single string with values in block concatenated with new-line characters.  
         
        """
        pass
    @ValuesConcatenated.setter
    def ValuesConcatenated(self, value_string: str):
        """
        Setter for property: (str) ValuesConcatenated
         Returns the ValuesConcatenated.  
           Represents single string with values in block concatenated with new-line characters.  
         
        """
        pass
    @property
    def Width(self) -> int:
        """
        Getter for property: (int) Width
         Returns the Width  
            
         
        """
        pass
    @Width.setter
    def Width(self, width: int):
        """
        Setter for property: (int) Width
         Returns the Width  
            
         
        """
        pass
    def GetUncommittedValue(self) -> List[str]:
        """
         The Uncommitted Value. Represents the actual value user inputs in. 
         Returns uncommittedvalue_string (List[str]): .
        """
        pass
    def GetValue(self) -> List[str]:
        """
         Gets the Value
         Returns value_string (List[str]): .
        """
        pass
    def SetValue(self, value_string: List[str]) -> None:
        """
         Sets the Value
        """
        pass
    def TestValueChanged(self, value_string: List[str]) -> None:
        """
        Tests value changed event workflow mapped to this MultilineString block.
        """
        pass
import NXOpen
class Node(NXOpen.TaggedObject): 
    """Represents the node created and utilized by BlockStyler.Tree.
    The node represents the single row of the tree."""
    class DragType(Enum):
        """
        Members Include: 
         |NotSet| No drag
         |All| Drag allowed to any level in the same tree

        """
        NotSet: int
        All: int
        @staticmethod
        def ValueOf(value: int) -> Node.DragType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DropType(Enum):
        """
        Members Include: 
         |NotSet| Drop not permitted
         |On| Drop permitted on the target node
         |Before| Drop permitted before the target node
         |After| Drop permitted after the target node
         |BeforeAndAfter| Drop permitted before and after the target node

        """
        NotSet: int
        On: int
        Before: int
        After: int
        BeforeAndAfter: int
        @staticmethod
        def ValueOf(value: int) -> Node.DropType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ExpandOption(Enum):
        """
        Members Include: 
         |Collapse| Use this option to collapse the node.
         |Expand| Use this option to expand the node. The child node state is unaltered.
         |Toggle| Use this option to collapse the expanded node or expand the collapsed node.

        """
        Collapse: int
        Expand: int
        Toggle: int
        @staticmethod
        def ValueOf(value: int) -> Node.ExpandOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Scroll(Enum):
        """
        Members Include: 
         |Center| Scrolls the tree to bring the node at the center of the tree window
         |LeastScroll| Scrolls the tree to minimal to make the node appear in tree window
         |MostScroll| Scrolls the tree to maximum to make the node appear in tree window

        """
        Center: int
        LeastScroll: int
        MostScroll: int
        @staticmethod
        def ValueOf(value: int) -> Node.Scroll:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CrossSelection(self) -> bool:
        """
        Getter for property: (bool) CrossSelection
         Returnsthe flag indicating whether cross section is allowed.  
           
               It is useful when the node contains  NXOpen::DisplayableObject  as 
               data. If the flag is true then the  NXOpen::DisplayableObject  is 
               highlighted, else not. The default value is True  
         
        """
        pass
    @CrossSelection.setter
    def CrossSelection(self, crossSelection: bool):
        """
        Setter for property: (bool) CrossSelection
         Returnsthe flag indicating whether cross section is allowed.  
           
               It is useful when the node contains  NXOpen::DisplayableObject  as 
               data. If the flag is true then the  NXOpen::DisplayableObject  is 
               highlighted, else not. The default value is True  
         
        """
        pass
    @property
    def DisplayIcon(self) -> str:
        """
        Getter for property: (str) DisplayIcon
         Returnsthe display icon.  
           This is normal icon positioned before the node text and is 
               displayed when the node is in unselected state.  
         
        """
        pass
    @DisplayIcon.setter
    def DisplayIcon(self, icon: str):
        """
        Setter for property: (str) DisplayIcon
         Returnsthe display icon.  
           This is normal icon positioned before the node text and is 
               displayed when the node is in unselected state.  
         
        """
        pass
    @property
    def DisplayText(self) -> str:
        """
        Getter for property: (str) DisplayText
         Returns the display text of node.  
           This is same as 0th column text of this node. 
               Use  BlockStyler::Node::SetColumnDisplayText  to fetch the text of other column of the same node.   
         
        """
        pass
    @DisplayText.setter
    def DisplayText(self, displayText: str):
        """
        Setter for property: (str) DisplayText
         Returns the display text of node.  
           This is same as 0th column text of this node. 
               Use  BlockStyler::Node::SetColumnDisplayText  to fetch the text of other column of the same node.   
         
        """
        pass
    @property
    def FirstChildNode(self) -> Node:
        """
        Getter for property: ( Node NXOpen.B) FirstChildNode
         Returnsthe first child node.  
           Returns NULL if child node is not present.  
         
        """
        pass
    @property
    def ForegroundColor(self) -> int:
        """
        Getter for property: (int) ForegroundColor
         Returnsthe text color of the node.  
           The color is applicable for whole row.  
         
        """
        pass
    @ForegroundColor.setter
    def ForegroundColor(self, nodeForgroundColor: int):
        """
        Setter for property: (int) ForegroundColor
         Returnsthe text color of the node.  
           The color is applicable for whole row.  
         
        """
        pass
    @property
    def IsExpanded(self) -> bool:
        """
        Getter for property: (bool) IsExpanded
         Returns the flag indicating whether the node is in expanded state  
            
         
        """
        pass
    @property
    def IsInserted(self) -> bool:
        """
        Getter for property: (bool) IsInserted
         Returns the flag indicating whether the node is inserted in  BlockStyler::Tree   
            
         
        """
        pass
    @property
    def IsSelected(self) -> bool:
        """
        Getter for property: (bool) IsSelected
         Returns the flag indicating whether the node is in selected state  
            
         
        """
        pass
    @property
    def NextNode(self) -> Node:
        """
        Getter for property: ( Node NXOpen.B) NextNode
         Returnsthe next node which might not belong to the same hierarchy.  
           
               The next node either is a sibling node or belongs to other root node. 
               Returns NULL if next node is not present  
         
        """
        pass
    @property
    def NextSelectedNode(self) -> Node:
        """
        Getter for property: ( Node NXOpen.B) NextSelectedNode
         Returnsthe next selected node in the whole tree hierarchy.  
           The node on which this method is called does not have to be selected. Returns NULL if none of the next nodes are selected.  
         
        """
        pass
    @property
    def NextSiblingNode(self) -> Node:
        """
        Getter for property: ( Node NXOpen.B) NextSiblingNode
         Returns the next node which belongs to the same hierarchy.  
           
               Returns NULL null if next sibling node is not present.  
         
        """
        pass
    @property
    def ParentNode(self) -> Node:
        """
        Getter for property: ( Node NXOpen.B) ParentNode
         Returnsthe parent node.  
           Returns NULL if parent node is not present  
         
        """
        pass
    @property
    def PreviousNode(self) -> Node:
        """
        Getter for property: ( Node NXOpen.B) PreviousNode
         Returnsthe previous node which might not belong to the same hierarchy.  
           
               Returns NULL null if previous node is not present  
         
        """
        pass
    @property
    def PreviousSelectedNode(self) -> Node:
        """
        Getter for property: ( Node NXOpen.B) PreviousSelectedNode
         Returnsthe previous selected node in the whole tree hierarchy.  
           The node on which this method is called does not have to be selected.
               Returns NULL if none of the previous nodes are selected.  
         
        """
        pass
    @property
    def PreviousSiblingNode(self) -> Node:
        """
        Getter for property: ( Node NXOpen.B) PreviousSiblingNode
         Returnsthe previous node which belongs to the same hierarchy.  
           
               Returns NULL if previous sibling node is not present.  
         
        """
        pass
    @property
    def SelectedIcon(self) -> str:
        """
        Getter for property: (str) SelectedIcon
         Returnsthe selected icon.  
           This icon appears on node selection and is positioned before the node text
               replacing the  BlockStyler::Node::DisplayIcon .  
         
        """
        pass
    @SelectedIcon.setter
    def SelectedIcon(self, icon: str):
        """
        Setter for property: (str) SelectedIcon
         Returnsthe selected icon.  
           This icon appears on node selection and is positioned before the node text
               replacing the  BlockStyler::Node::DisplayIcon .  
         
        """
        pass
    def Expand(self, expandOption: Node.ExpandOption) -> None:
        """
        Expandscollapses the node
        """
        pass
    def GetColumnDisplayText(self, columnID: int) -> str:
        """
        Gets the column text for the given columnId. 
               The text is interpreted as icon if the column display type is  
               BlockStyler.Tree.ColumnDisplay.Icon.
         Returns columnDisplayText (str): Text associated with column.
        """
        pass
    def GetNodeData(self) -> NXOpen.DataContainer:
        """
          Gets node data which contains the data in the form of unique name-value pairs. 
                In this context unique name is termed as property name. There 
                could me more than one such property name - value pair, but the property name of the primary data 
                should be named "Data" (case-sensitive). For instance, if a BlockStyler.Node represents a 
                feature object then property name should be "Data" and the value should be feature object. The primary data is used by NX 
                for some operations such cross selection.
                
                Initialy the container or list is empty and it is expected that data 
                would be added to it. Additional property name - value pair can be added to the container or list, but it should be made sure that
                there is no dublicate property name exists in the container or list. The additional data can be seen as 
                book keeping information for node. At any point the node data can be fetched and value can be extracted
                using the corresponding property name. Refer to NXOpen.DataContainer on how property name-value pair is added
                to the container or list.
                
               
         Returns nodeData ( NXOpen.DataContainer): Node data which is list of property name - value pair. New property name - value pair can be added to it and existing value can be fetched using corresponding property name.
        """
        pass
    def GetState(self) -> int:
        """
        Gets the node state associated with node state icon. Node state is an iconic 
               representation, e.g., checkedunchecked icons for corresponding state. Node state 
               value 1 and 2 represents the standard checked and unchecked state respectively.
         Returns state (int): Node state.
        """
        pass
    def ScrollTo(self, columnID: int, visibleOption: Node.Scroll) -> None:
        """
        Scrolls horizontally and vertically to make the specific column of 
                node appear on the tree window.
        """
        pass
    def SetColumnDisplayText(self, columnID: int, columnDisplayText: str) -> None:
        """
        Sets the text in the column which corresponds to given columnId. 
               The text is interpreted as icon if the column display type is  
               BlockStyler.Tree.ColumnDisplay.Icon.
        """
        pass
    def SetState(self, state: int) -> None:
        """
        Sets the node state which is associated with node state icon. Node state is an iconic 
               representation, e.g., checkedunchecked state. Setting node state to value other 
               than 1 and 2 calls BlockStyler.Tree.StateIconName callback to fetch
               the icon name. Node state can be set only after the node has been added to TreeList.
        """
        pass
class ObjectColorPicker(UIBlock): 
    """ Represents an Object Color Picker Block"""
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @BalloonTooltipText.setter
    def BalloonTooltipText(self, tooltipText: str):
        """
        Setter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @property
    def Localize(self) -> bool:
        """
        Getter for property: (bool) Localize
         Returns the Localize.  
           If true, translates the Label string into the language of the current locale.  
         
        """
        pass
    @Localize.setter
    def Localize(self, localize: bool):
        """
        Setter for property: (bool) Localize
         Returns the Localize.  
           If true, translates the Label string into the language of the current locale.  
         
        """
        pass
    @property
    def NumberSelectable(self) -> int:
        """
        Getter for property: (int) NumberSelectable
         Returns the NumberSelectable.  
           Represents number of colors that can be selected  
         
        """
        pass
    @NumberSelectable.setter
    def NumberSelectable(self, number: int):
        """
        Setter for property: (int) NumberSelectable
         Returns the NumberSelectable.  
           Represents number of colors that can be selected  
         
        """
        pass
    @property
    def RetainValue(self) -> bool:
        """
        Getter for property: (bool) RetainValue
         Returns the RetainValue.  
           If true, block's value will be stored in dialog memory upon OK, Apply or Close.  
         
        """
        pass
    @RetainValue.setter
    def RetainValue(self, retain: bool):
        """
        Setter for property: (bool) RetainValue
         Returns the RetainValue.  
           If true, block's value will be stored in dialog memory upon OK, Apply or Close.  
         
        """
        pass
    def GetBalloonTooltipLayoutMembers(self) -> List[str]:
        """
         Gets theBalloonTooltipLayout members 
         Returns layout_strings (List[str]): Values to get from the property .
        """
        pass
    def GetValue(self) -> List[int]:
        """
         Gets the Value
         Returns value_vector (List[int]): Values to get from the property.
        """
        pass
    def SetValue(self, value_vector: List[int]) -> None:
        """
         Sets the Value
        """
        pass
    def TestValueChanged(self, value_vector: List[int]) -> None:
        """
        Tests value changed event workflow mapped to this object ObjectColorPicker block.
        """
        pass
import NXOpen
class OnPathDimension(UIBlock): 
    """ Represents a On Path Dimension block"""
    @property
    def AdaptiveScaleLimits(self) -> bool:
        """
        Getter for property: (bool) AdaptiveScaleLimits
         Returnsthe AdaptiveScaleLimits.  
          
                If true, indicates that the scale should be adaptive.  
         
        """
        pass
    @AdaptiveScaleLimits.setter
    def AdaptiveScaleLimits(self, scale_limits: bool):
        """
        Setter for property: (bool) AdaptiveScaleLimits
         Returnsthe AdaptiveScaleLimits.  
          
                If true, indicates that the scale should be adaptive.  
         
        """
        pass
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @property
    def ExpressionObject(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) ExpressionObject
         Returns the ExpressionObject  
            
         
        """
        pass
    @ExpressionObject.setter
    def ExpressionObject(self, expression_obj: NXOpen.TaggedObject):
        """
        Setter for property: ( NXOpen.TaggedObject) ExpressionObject
         Returns the ExpressionObject  
            
         
        """
        pass
    @property
    def Formula(self) -> str:
        """
        Getter for property: (str) Formula
         Returns the Formula  
            
         
        """
        pass
    @Formula.setter
    def Formula(self, formula: str):
        """
        Setter for property: (str) Formula
         Returns the Formula  
            
         
        """
        pass
    @property
    def LineIncrement(self) -> float:
        """
        Getter for property: (float) LineIncrement
         Returnsthe LineIncrement value.  
          
                Specifies the incrementdecrement when the user presses the arrow keys on the keyboard.
                Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
         
        """
        pass
    @LineIncrement.setter
    def LineIncrement(self, line_increment: float):
        """
        Setter for property: (float) LineIncrement
         Returnsthe LineIncrement value.  
          
                Specifies the incrementdecrement when the user presses the arrow keys on the keyboard.
                Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
         
        """
        pass
    @property
    def LocationOptionAsString(self) -> str:
        """
        Getter for property: (str) LocationOptionAsString
         Returns the LocationOption as string  
            
         
        """
        pass
    @LocationOptionAsString.setter
    def LocationOptionAsString(self, enumString: str):
        """
        Setter for property: (str) LocationOptionAsString
         Returns the LocationOption as string  
            
         
        """
        pass
    @property
    def MaxInclusive(self) -> bool:
        """
        Getter for property: (bool) MaxInclusive
         Returns the MaxInclusive  
            
         
        """
        pass
    @MaxInclusive.setter
    def MaxInclusive(self, max_inclusive: bool):
        """
        Setter for property: (bool) MaxInclusive
         Returns the MaxInclusive  
            
         
        """
        pass
    @property
    def MaximumValue(self) -> float:
        """
        Getter for property: (float) MaximumValue
         Returns the MaximumValue  
            
         
        """
        pass
    @MaximumValue.setter
    def MaximumValue(self, max_value: float):
        """
        Setter for property: (float) MaximumValue
         Returns the MaximumValue  
            
         
        """
        pass
    @property
    def MinInclusive(self) -> bool:
        """
        Getter for property: (bool) MinInclusive
         Returns the MinInclusive  
            
         
        """
        pass
    @MinInclusive.setter
    def MinInclusive(self, min_inclusive: bool):
        """
        Setter for property: (bool) MinInclusive
         Returns the MinInclusive  
            
         
        """
        pass
    @property
    def MinimumValue(self) -> float:
        """
        Getter for property: (float) MinimumValue
         Returns the MinimumValue  
            
         
        """
        pass
    @MinimumValue.setter
    def MinimumValue(self, min_value: float):
        """
        Setter for property: (float) MinimumValue
         Returns the MinimumValue  
            
         
        """
        pass
    @property
    def OptionMask(self) -> int:
        """
        Getter for property: (int) OptionMask
         Returns the OptionMask  
            
         
        """
        pass
    @OptionMask.setter
    def OptionMask(self, maskVal: int):
        """
        Setter for property: (int) OptionMask
         Returns the OptionMask  
            
         
        """
        pass
    @property
    def OptionMenuTitle(self) -> str:
        """
        Getter for property: (str) OptionMenuTitle
         Returns the OptionMenuTitle  
            
         
        """
        pass
    @OptionMenuTitle.setter
    def OptionMenuTitle(self, menuTitleText: str):
        """
        Setter for property: (str) OptionMenuTitle
         Returns the OptionMenuTitle  
            
         
        """
        pass
    @property
    def PageIncrement(self) -> float:
        """
        Getter for property: (float) PageIncrement
         Returnsthe PageIncrement value.  
          
                Specifies the incrementdecrement when the user presses the Page Up or Page Down keys on the keyboard.
                Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
         
        """
        pass
    @PageIncrement.setter
    def PageIncrement(self, page_increment: float):
        """
        Setter for property: (float) PageIncrement
         Returnsthe PageIncrement value.  
          
                Specifies the incrementdecrement when the user presses the Page Up or Page Down keys on the keyboard.
                Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
         
        """
        pass
    @property
    def Path(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) Path
         Returns the Path  
            
         
        """
        pass
    @Path.setter
    def Path(self, path: NXOpen.TaggedObject):
        """
        Setter for property: ( NXOpen.TaggedObject) Path
         Returns the Path  
            
         
        """
        pass
    @property
    def ShowFocusHandle(self) -> bool:
        """
        Getter for property: (bool) ShowFocusHandle
         Returns the ShowFocusHandle  
            
         
        """
        pass
    @ShowFocusHandle.setter
    def ShowFocusHandle(self, show_focus: bool):
        """
        Setter for property: (bool) ShowFocusHandle
         Returns the ShowFocusHandle  
            
         
        """
        pass
    @property
    def SnapPointTypesOnByDefault(self) -> int:
        """
        Getter for property: (int) SnapPointTypesOnByDefault
         Returns the SnapPointTypesOnByDefault  
            
         
        """
        pass
    @SnapPointTypesOnByDefault.setter
    def SnapPointTypesOnByDefault(self, point_type: int):
        """
        Setter for property: (int) SnapPointTypesOnByDefault
         Returns the SnapPointTypesOnByDefault  
            
         
        """
        pass
    @property
    def Units(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) Units
         Returns the Units  
            
         
        """
        pass
    @Units.setter
    def Units(self, units: NXOpen.TaggedObject):
        """
        Setter for property: ( NXOpen.TaggedObject) Units
         Returns the Units  
            
         
        """
        pass
    @property
    def Value(self) -> float:
        """
        Getter for property: (float) Value
         Returns the Value.  
            
         
        """
        pass
    @Value.setter
    def Value(self, dimension_value: float):
        """
        Setter for property: (float) Value
         Returns the Value.  
            
         
        """
        pass
    @property
    def WithScale(self) -> bool:
        """
        Getter for property: (bool) WithScale
         Returns the WithScale.  
           If true,the slider bar is shown.  
         
        """
        pass
    @WithScale.setter
    def WithScale(self, with_scale: bool):
        """
        Setter for property: (bool) WithScale
         Returns the WithScale.  
           If true,the slider bar is shown.  
         
        """
        pass
    def GetBalloonTooltipLayoutMembers(self) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         Returns layout_strings (List[str]): Values to get from the property. .
        """
        pass
    def GetLocationOptionMembers(self) -> List[str]:
        """
         Gets the LocationOption members
         Returns locationOptionMembers (List[str]):  Values to get from the property.
        """
        pass
    def TestValueChanged(self, dimension_value: float) -> None:
        """
        Tests dimension changed event workflow mapped to this OnPathDimension block.
        """
        pass
import NXOpen
class OrientXpress(UIBlock): 
    """ Represents OrientXpress Block"""
    @property
    def DirectionAsString(self) -> str:
        """
        Getter for property: (str) DirectionAsString
         Returns the Direction as string  
            
         
        """
        pass
    @DirectionAsString.setter
    def DirectionAsString(self, enumString: str):
        """
        Setter for property: (str) DirectionAsString
         Returns the Direction as string  
            
         
        """
        pass
    @property
    def PlaneAsString(self) -> str:
        """
        Getter for property: (str) PlaneAsString
         Returns the Plane as string  
            
         
        """
        pass
    @PlaneAsString.setter
    def PlaneAsString(self, enumString: str):
        """
        Setter for property: (str) PlaneAsString
         Returns the Plane as string  
            
         
        """
        pass
    @property
    def ReferenceAsString(self) -> str:
        """
        Getter for property: (str) ReferenceAsString
         Returns the Reference as string  
            
         
        """
        pass
    @ReferenceAsString.setter
    def ReferenceAsString(self, enumString: str):
        """
        Setter for property: (str) ReferenceAsString
         Returns the Reference as string  
            
         
        """
        pass
    @property
    def ReferenceCsys(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) ReferenceCsys
         Returns the ReferenceCsys  
            
         
        """
        pass
    @ReferenceCsys.setter
    def ReferenceCsys(self, referenceCsys: NXOpen.TaggedObject):
        """
        Setter for property: ( NXOpen.TaggedObject) ReferenceCsys
         Returns the ReferenceCsys  
            
         
        """
        pass
    @property
    def ShowAxisSubBlock(self) -> bool:
        """
        Getter for property: (bool) ShowAxisSubBlock
         Returns the ShowAxisSubBlock  
            
         
        """
        pass
    @ShowAxisSubBlock.setter
    def ShowAxisSubBlock(self, show: bool):
        """
        Setter for property: (bool) ShowAxisSubBlock
         Returns the ShowAxisSubBlock  
            
         
        """
        pass
    @property
    def ShowPlaneSubBlock(self) -> bool:
        """
        Getter for property: (bool) ShowPlaneSubBlock
         Returns the ShowPlaneSubBlock  
            
         
        """
        pass
    @ShowPlaneSubBlock.setter
    def ShowPlaneSubBlock(self, show: bool):
        """
        Setter for property: (bool) ShowPlaneSubBlock
         Returns the ShowPlaneSubBlock  
            
         
        """
        pass
    @property
    def ShowReferenceSubBlock(self) -> bool:
        """
        Getter for property: (bool) ShowReferenceSubBlock
         Returns the ShowReferenceSubBlock  
            
         
        """
        pass
    @ShowReferenceSubBlock.setter
    def ShowReferenceSubBlock(self, show: bool):
        """
        Setter for property: (bool) ShowReferenceSubBlock
         Returns the ShowReferenceSubBlock  
            
         
        """
        pass
    @property
    def ShowSceneControl(self) -> bool:
        """
        Getter for property: (bool) ShowSceneControl
         Returns the ShowSceneControl  
            
         
        """
        pass
    @ShowSceneControl.setter
    def ShowSceneControl(self, show: bool):
        """
        Setter for property: (bool) ShowSceneControl
         Returns the ShowSceneControl  
            
         
        """
        pass
    @property
    def ShowXAxis(self) -> bool:
        """
        Getter for property: (bool) ShowXAxis
         Returns the ShowXAxis  
            
         
        """
        pass
    @ShowXAxis.setter
    def ShowXAxis(self, show: bool):
        """
        Setter for property: (bool) ShowXAxis
         Returns the ShowXAxis  
            
         
        """
        pass
    @property
    def ShowXYPlane(self) -> bool:
        """
        Getter for property: (bool) ShowXYPlane
         Returns the ShowXYPlane  
            
         
        """
        pass
    @ShowXYPlane.setter
    def ShowXYPlane(self, show: bool):
        """
        Setter for property: (bool) ShowXYPlane
         Returns the ShowXYPlane  
            
         
        """
        pass
    @property
    def ShowXZPlane(self) -> bool:
        """
        Getter for property: (bool) ShowXZPlane
         Returns the ShowXZPlane  
            
         
        """
        pass
    @ShowXZPlane.setter
    def ShowXZPlane(self, show: bool):
        """
        Setter for property: (bool) ShowXZPlane
         Returns the ShowXZPlane  
            
         
        """
        pass
    @property
    def ShowYAxis(self) -> bool:
        """
        Getter for property: (bool) ShowYAxis
         Returns the ShowYAxis  
            
         
        """
        pass
    @ShowYAxis.setter
    def ShowYAxis(self, show: bool):
        """
        Setter for property: (bool) ShowYAxis
         Returns the ShowYAxis  
            
         
        """
        pass
    @property
    def ShowYZPlane(self) -> bool:
        """
        Getter for property: (bool) ShowYZPlane
         Returns the ShowYZPlane  
            
         
        """
        pass
    @ShowYZPlane.setter
    def ShowYZPlane(self, show: bool):
        """
        Setter for property: (bool) ShowYZPlane
         Returns the ShowYZPlane  
            
         
        """
        pass
    @property
    def ShowZAxis(self) -> bool:
        """
        Getter for property: (bool) ShowZAxis
         Returns the ShowZAxis  
            
         
        """
        pass
    @ShowZAxis.setter
    def ShowZAxis(self, show: bool):
        """
        Setter for property: (bool) ShowZAxis
         Returns the ShowZAxis  
            
         
        """
        pass
    def GetDirectionMembers(self) -> List[str]:
        """
         Gets Direction members
         Returns member_strings (List[str]): .
        """
        pass
    def GetPlaneMembers(self) -> List[str]:
        """
         Gets Plane members
         Returns member_strings (List[str]): .
        """
        pass
    def GetReferenceMembers(self) -> List[str]:
        """
         Gets Reference members
         Returns member_strings (List[str]): .
        """
        pass
    def TestDirectionSpecified(self, enumString: str) -> None:
        """
        Tests direction specified.
        """
        pass
    def TestPlaneSpecified(self, enumString: str) -> None:
        """
        Tests plane specified.
        """
        pass
    def TestReferenceCsysSpecified(self, referenceCsys: NXOpen.TaggedObject) -> None:
        """
        Tests referenceCsys specified.
        """
        pass
    def TestReferenceSpecified(self, enumString: str) -> None:
        """
        Tests reference specified.
        """
        pass
class PostSelectElement(UIBlock): 
    """
    Represents a Post Select Element block
    """
    class SmartMethodType(Enum):
        """
        Members Include: 
         |NoMethod|  
         |RelatedElements|  
         |FeatureAngleElements|  
         |ByResultRange|  
         |NumberOfMaxValues|  
         |NumberOfMinValues|  

        """
        NoMethod: int
        RelatedElements: int
        FeatureAngleElements: int
        ByResultRange: int
        NumberOfMaxValues: int
        NumberOfMinValues: int
        @staticmethod
        def ValueOf(value: int) -> PostSelectElement.SmartMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AutomaticProgression(self) -> bool:
        """
        Getter for property: (bool) AutomaticProgression
         Returnsthe automatic progression  
            
         
        """
        pass
    @AutomaticProgression.setter
    def AutomaticProgression(self, automaticProgression: bool):
        """
        Setter for property: (bool) AutomaticProgression
         Returnsthe automatic progression  
            
         
        """
        pass
    @property
    def Bitmap(self) -> str:
        """
        Getter for property: (str) Bitmap
         Returns the selection component bitmap   
            
         
        """
        pass
    @Bitmap.setter
    def Bitmap(self, bitmapString: str):
        """
        Setter for property: (str) Bitmap
         Returns the selection component bitmap   
            
         
        """
        pass
    @property
    def Cue(self) -> str:
        """
        Getter for property: (str) Cue
         Returns the cue massage   
            
         
        """
        pass
    @Cue.setter
    def Cue(self, cue: str):
        """
        Setter for property: (str) Cue
         Returns the cue massage   
            
         
        """
        pass
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
         Returns the selection component label   
            
         
        """
        pass
    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
         Returns the selection component label   
            
         
        """
        pass
    @property
    def PostViewId(self) -> int:
        """
        Getter for property: (int) PostViewId
         Returns the post view ID   
            
         
        """
        pass
    @PostViewId.setter
    def PostViewId(self, pvid: int):
        """
        Setter for property: (int) PostViewId
         Returns the post view ID   
            
         
        """
        pass
    @property
    def SelectionMode(self) -> str:
        """
        Getter for property: (str) SelectionMode
         Returns the selection mode types   
            
         
        """
        pass
    @SelectionMode.setter
    def SelectionMode(self, enumString: str):
        """
        Setter for property: (str) SelectionMode
         Returns the selection mode types   
            
         
        """
        pass
    @property
    def ShowSelection(self) -> bool:
        """
        Getter for property: (bool) ShowSelection
         Returns the value whether or not to show selection component.  
             
         
        """
        pass
    @ShowSelection.setter
    def ShowSelection(self, showSelection: bool):
        """
        Setter for property: (bool) ShowSelection
         Returns the value whether or not to show selection component.  
             
         
        """
        pass
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
         Returnsthe step status   
            
         
        """
        pass
    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
         Returnsthe step status   
            
         
        """
        pass
    def DisableSmartMethod(self, methodType: PostSelectElement.SmartMethodType) -> None:
        """
        Disables the smart method option
                  The NoMethod can not be disabled. Error will be raised up if NoMethod is disabled.
                
        """
        pass
    def GetAllSelectModes(self) -> List[str]:
        """
         Gets all of the selection modes 
         Returns stringMembers (List[str]): .
        """
        pass
    def GetSelectedElementIndices(self) -> List[int]:
        """
         Gets the selected element indices 
         Returns elemIndices (List[int]): Value to get from the property.
        """
        pass
    def GetSelectedElementLabels(self) -> List[int]:
        """
         Gets the selected element labels 
         Returns elemLabels (List[int]): Value to get from the property.
        """
        pass
    def GetStepStatusMembers(self) -> List[str]:
        """
         Gets the StepStatus members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def SetSelectedElementIndices(self, elemIndices: List[int]) -> None:
        """
         Sets the selected element indices 
        """
        pass
    def SetSelectedElementLabels(self, elemLabels: List[int]) -> None:
        """
         Sets the selected element labels 
        """
        pass
class PostSelectNode(UIBlock): 
    """
    Represents a Post Select Node block
    """
    class SmartMethodType(Enum):
        """
        Members Include: 
         |NoMethod|  
         |RelatedNodes|  
         |UnobstructedNodes|  
         |FeatureAngleNodes|  
         |FeatureEdgeNodes|  
         |ByResultRange|  
         |NumberOfMaxValues|  
         |NumberOfMinValues|  

        """
        NoMethod: int
        RelatedNodes: int
        UnobstructedNodes: int
        FeatureAngleNodes: int
        FeatureEdgeNodes: int
        ByResultRange: int
        NumberOfMaxValues: int
        NumberOfMinValues: int
        @staticmethod
        def ValueOf(value: int) -> PostSelectNode.SmartMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AutomaticProgression(self) -> bool:
        """
        Getter for property: (bool) AutomaticProgression
         Returnsthe automatic progression  
            
         
        """
        pass
    @AutomaticProgression.setter
    def AutomaticProgression(self, automaticProgression: bool):
        """
        Setter for property: (bool) AutomaticProgression
         Returnsthe automatic progression  
            
         
        """
        pass
    @property
    def Bitmap(self) -> str:
        """
        Getter for property: (str) Bitmap
         Returns the selection component bitmap   
            
         
        """
        pass
    @Bitmap.setter
    def Bitmap(self, bitmapString: str):
        """
        Setter for property: (str) Bitmap
         Returns the selection component bitmap   
            
         
        """
        pass
    @property
    def Cue(self) -> str:
        """
        Getter for property: (str) Cue
         Returns the cue massage   
            
         
        """
        pass
    @Cue.setter
    def Cue(self, cue: str):
        """
        Setter for property: (str) Cue
         Returns the cue massage   
            
         
        """
        pass
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
         Returns the selection component label   
            
         
        """
        pass
    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
         Returns the selection component label   
            
         
        """
        pass
    @property
    def PostViewId(self) -> int:
        """
        Getter for property: (int) PostViewId
         Returns the post view ID   
            
         
        """
        pass
    @PostViewId.setter
    def PostViewId(self, pvid: int):
        """
        Setter for property: (int) PostViewId
         Returns the post view ID   
            
         
        """
        pass
    @property
    def SelectionMode(self) -> str:
        """
        Getter for property: (str) SelectionMode
         Returns the selection mode types   
            
         
        """
        pass
    @SelectionMode.setter
    def SelectionMode(self, enumString: str):
        """
        Setter for property: (str) SelectionMode
         Returns the selection mode types   
            
         
        """
        pass
    @property
    def ShowSelection(self) -> bool:
        """
        Getter for property: (bool) ShowSelection
         Returns the value whether or not to show selection component.  
             
         
        """
        pass
    @ShowSelection.setter
    def ShowSelection(self, showSelection: bool):
        """
        Setter for property: (bool) ShowSelection
         Returns the value whether or not to show selection component.  
             
         
        """
        pass
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
         Returnsthe step status   
            
         
        """
        pass
    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
         Returnsthe step status   
            
         
        """
        pass
    def DisableSmartMethod(self, methodType: PostSelectNode.SmartMethodType) -> None:
        """
        Disables the smart method option
                The NoMethod can not be disabled. Error will be raised up if NoMethod is disabled.
                
        """
        pass
    def GetAllSelectModes(self) -> List[str]:
        """
         Gets all of the selection modes 
         Returns stringMembers (List[str]): .
        """
        pass
    def GetSelectedNodeIndices(self) -> List[int]:
        """
         Gets the selected node indices 
         Returns nodesIndices (List[int]): Value to get from the property.
        """
        pass
    def GetSelectedNodeLabels(self) -> List[int]:
        """
         Gets the selected node labels 
         Returns nodeLabels (List[int]): Value to get from the property.
        """
        pass
    def GetStepStatusMembers(self) -> List[str]:
        """
         Gets the StepStatus members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def SetSelectedNodeIndices(self, nodesIndices: List[int]) -> None:
        """
         Sets the selected node indices 
        """
        pass
    def SetSelectedNodeLabels(self, nodeLabels: List[int]) -> None:
        """
         Sets the selected node labels 
        """
        pass
import NXOpen
import NXOpen.Select
class PropertyList(NXOpen.TransientObject): 
    """ Represents a list of properties """
    class ListMode(Enum):
        """
        Members Include: 
         |Indexed|  The properties are not named and
                       must be indexed through an integer index 
         |Named|  The properties are named 

        """
        Indexed: int
        Named: int
        @staticmethod
        def ValueOf(value: int) -> PropertyList.ListMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PropertyType(Enum):
        """
        Members Include: 
         |String| String
         |Double| Double
         |Logical| Logical
         |Integer| Integer
         |Enum| Enum
         |Strings| Strings
         |UIBlock| UIBlock
         |Point| Point
         |Vector| Vector
         |Bits| Bits
         |TaggedObject| Tagged Object
         |Array| Array
         |IntegerMatrix2d| Integer 2d-Matrix
         |DoubleMatrix2d| Double 2d-Matrix
         |TaggedObjectMatrix2d| Tagged Object 2d-Matrix
         |IntegerVector| Integer Vector
         |DoubleVector| Double Vector
         |TaggedObjectVector| Tagged Object Vector
         |File| File
         |SelectionFilter| Selection Filter
         |Undefined| Undefined 

        """
        String: int
        Double: int
        Logical: int
        Integer: int
        Enum: int
        Strings: int
        UIBlock: int
        Point: int
        Vector: int
        Bits: int
        TaggedObject: int
        Array: int
        IntegerMatrix2d: int
        DoubleMatrix2d: int
        TaggedObjectMatrix2d: int
        IntegerVector: int
        DoubleVector: int
        TaggedObjectVector: int
        File: int
        SelectionFilter: int
        Undefined: int
        @staticmethod
        def ValueOf(value: int) -> PropertyList.PropertyType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @property
    def Mode(self) -> PropertyList.ListMode:
        """
        Getter for property: ( PropertyList.ListMode NXOpen.B) Mode
         Returns the mode of the list.  
            
         
        """
        pass
    def AddFilterMembers(self, propertyName: str, members: List[NXOpen.Select.FilterMember]) -> None:
        """
        Adds the filter members for the given property name. 
        """
        pass
    def ClearFilter(self, propertyName: str) -> None:
        """
        Clears the filter for the given property name. 
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                    it is illegal to use the object.  In .NET, this method is automatically
                    called when the object is deleted by the garbage collector. 
        """
        pass
    @overload
    def GetArray(self, propertyName: str) -> PropertyList:
        """
        Gets the value for the given property name. Exception will be raised if invalid property name is used. 
         Returns value ( PropertyList NXOpen.B): Value to get for given property name. .
        """
        pass
    @overload
    def GetArray(self, propertyIndex: int) -> PropertyList:
        """
        Gets the value for the given index. Exception will be raised if invalid index is used. 
         Returns value ( PropertyList NXOpen.B): Value to get for given index. .
        """
        pass
    @overload
    def GetBits(self, propertyName: str) -> int:
        """
         Gets the bits value for the given property name. Exception will be raised if invalid property name is used. 
         Returns bits_sc (int): Value to get for given property name.  .
        """
        pass
    @overload
    def GetBits(self, propertyIndex: int) -> int:
        """
         Gets the bits value for the given index. Exception will be raised if invalid index is used. 
         Returns bits_sc (int): Value to get for given index.  .
        """
        pass
    @overload
    def GetDouble(self, propertyName: str) -> float:
        """
         Gets the double value for the given property name. Exception will be raised if invalid property name is used. 
         Returns value (float): Value to get for given property name.
        """
        pass
    @overload
    def GetDoubleMatrix(self, propertyName: str) -> Tuple[List[float], int, int]:
        """
        Gets the double matrix for the given property name. Exception will be raised if invalid property name is used.
                    This is a two dimensional array encoded into a single array. 
         Returns A tuple consisting of (matrixValue, nRows, nColumns). 
         - matrixValue is: List[float].Value to get for given property name. .
         - nRows is: int. Number of Rows in the 2D matrix .
         - nColumns is: int. Number of Columns in the 2D matrix .

        """
        pass
    @overload
    def GetDoubleMatrix(self, propertyIndex: int) -> Tuple[List[float], int, int]:
        """
        Gets the double matrix for the given index. Exception will be raised if invalid index is used.
                    This is a two dimensional array encoded into a single array. 
         Returns A tuple consisting of (matrixValue, nRows, nColumns). 
         - matrixValue is: List[float].Value to get for given index. .
         - nRows is: int. Number of Rows in the 2D matrix .
         - nColumns is: int. Number of Columns in the 2D matrix .

        """
        pass
    @overload
    def GetDoubleVector(self, propertyName: str) -> List[float]:
        """
        Gets the double vector for the given property name. Exception will be raised if invalid property name is used. 
         Returns doubleVector (List[float]): Value to get for given property name. .
        """
        pass
    @overload
    def GetDoubleVector(self, propertyIndex: int) -> List[float]:
        """
        Gets the double vector for the given index. Exception will be raised if invalid index is used. 
         Returns doubleVector (List[float]): Value to get for given index. .
        """
        pass
    @overload
    def GetDouble(self, propertyIndex: int) -> float:
        """
         Gets the double value for the given index. Exception will be raised if invalid index is used. 
         Returns value (float): Value to get for given index.
        """
        pass
    @overload
    def GetEnum(self, propertyName: str) -> int:
        """
        Gets the value for the given property name. Exception will be raised if invalid property name is used. 
         Returns value (int): Value to get for given property name. .
        """
        pass
    @overload
    def GetEnumAsString(self, propertyName: str) -> str:
        """
        Gets the value for the given property name. Exception will be raised if invalid property name is used. 
         Returns value (str): Value to get for given property name. .
        """
        pass
    @overload
    def GetEnumAsString(self, propertyIndex: int) -> str:
        """
        Gets the value for the given index. Exception will be raised if invalid index is used. 
         Returns value (str): Value to get for given index. .
        """
        pass
    @overload
    def GetEnumMembers(self, propertyName: str) -> List[str]:
        """
        Gets the enum members for the given property of type enum. Exception will be raised if invalid property name is used. 
         Returns strings (List[str]): Value to get for given property name. .
        """
        pass
    @overload
    def GetEnumMembers(self, propertyIndex: int) -> List[str]:
        """
        Gets the enum members for the given property index. Exception will be raised if invalid property name is used. 
         Returns strings (List[str]): Value to get for given property index. .
        """
        pass
    @overload
    def GetEnum(self, propertyIndex: int) -> int:
        """
        Gets the value for the given index. Exception will be raised if invalid index is used. 
         Returns value (int): Value to get for given index. .
        """
        pass
    @overload
    def GetFile(self, propertyName: str) -> str:
        """
        Gets the value for the given property name. Exception will be raised if invalid property name is used. 
         Returns value (str): Value to get for given property name. .
        """
        pass
    @overload
    def GetFile(self, propertyIndex: int) -> str:
        """
        Gets the value for the given index. Exception will be raised if invalid index is used. 
         Returns value (str): Value to get for given index. .
        """
        pass
    @overload
    def GetInteger(self, propertyName: str) -> int:
        """
         Gets the integer value for the given property name. Exception will be raised if invalid property name is used 
         Returns value (int): Value to get for given property name .
        """
        pass
    @overload
    def GetIntegerMatrix(self, propertyName: str) -> Tuple[List[int], int, int]:
        """
        Gets the integer matrix for the given property name. Exception will be raised if invalid property name is used.
                  This is a two dimensional array encoded into a single array. 
         Returns A tuple consisting of (matrixValue, nRows, nColumns). 
         - matrixValue is: List[int].Value to get for given property name. .
         - nRows is: int. Number of Rows in the 2D matrix .
         - nColumns is: int. Number of Columns in the 2D matrix .

        """
        pass
    @overload
    def GetIntegerMatrix(self, propertyIndex: int) -> Tuple[List[int], int, int]:
        """
        Gets the integer matrix for the given index. Exception will be raised if invalid index is used.
                  This is a two dimensional array encoded into a single array. 
         Returns A tuple consisting of (matrixValue, nRows, nColumns). 
         - matrixValue is: List[int].Value to get for given index. .
         - nRows is: int. Number of Rows in the 2D matrix .
         - nColumns is: int. Number of Columns in the 2D matrix .

        """
        pass
    @overload
    def GetIntegerVector(self, propertyName: str) -> List[int]:
        """
        Gets the integer vector for the given property name. Exception will be raised if invalid property name is used. 
         Returns intVector (List[int]): Value to get for given property name. .
        """
        pass
    @overload
    def GetIntegerVector(self, propertyIndex: int) -> List[int]:
        """
        Gets the integer vector for the given index. Exception will be raised if invalid index is used. 
         Returns intVector (List[int]): Value to get for given index. .
        """
        pass
    @overload
    def GetInteger(self, propertyIndex: int) -> int:
        """
         Gets the integer value for the given index. Exception will be raised if invalid index is used 
         Returns value (int): Value to get for given index .
        """
        pass
    @overload
    def GetLogical(self, propertyName: str) -> bool:
        """
         Gets the logical value for the given property name. Exception will be raised if invalid property name is used. 
         Returns value (bool): Value to get for given property name.
        """
        pass
    @overload
    def GetLogical(self, propertyIndex: int) -> bool:
        """
         Gets the logical value for the given index. Exception will be raised if invalid index is used. 
         Returns value (bool): Value to get for given index.
        """
        pass
    @overload
    def GetPoint(self, propertyName: str) -> NXOpen.Point3d:
        """
        Gets the point value for the given property name. Exception will be raised if invalid property name is used. 
         Returns point_sc ( NXOpen.Point3d): Value to get for given property name. .
        """
        pass
    @overload
    def GetPoint(self, propertyIndex: int) -> NXOpen.Point3d:
        """
        Gets the point value for the given index. Exception will be raised if invalid index is used. 
         Returns point_sc ( NXOpen.Point3d): Value to get for given index. .
        """
        pass
    def GetPropertyNames(self) -> List[str]:
        """
         Returns a list of all the property names 
         Returns strings (List[str]): Property names .
        """
        pass
    @overload
    def GetPropertyType(self, propertyName: str) -> PropertyList.PropertyType:
        """
         Returns the property type for given property name 
         Returns value ( PropertyList.PropertyType NXOpen.B): Property type. .
        """
        pass
    @overload
    def GetPropertyType(self, propertyIndex: int) -> PropertyList.PropertyType:
        """
         Returns the property type for the Indexed property list. Don't use this method on Named property list 
         Returns value ( PropertyList.PropertyType NXOpen.B): Property type. .
        """
        pass
    @overload
    def GetString(self, propertyName: str) -> str:
        """
         Gets the string value for the given property name. Exception will be raised if invalid property name is used. 
         Returns value (str): Value to get for given property name. .
        """
        pass
    @overload
    def GetString(self, propertyIndex: int) -> str:
        """
         Gets the string value for the given index. Exception will be raised if invalid index is used. 
         Returns value (str): Value to get for given index. .
        """
        pass
    @overload
    def GetStrings(self, propertyName: str) -> List[str]:
        """
        Gets the strings value for the given property name. Exception will be raised if invalid property name is used. 
         Returns strings (List[str]): Value to get for given property name. .
        """
        pass
    @overload
    def GetStrings(self, propertyIndex: int) -> List[str]:
        """
        Gets the strings value for the given index. Exception will be raised if invalid index is used. 
         Returns strings (List[str]): Value to get for given index. .
        """
        pass
    @overload
    def GetTaggedObject(self, propertyName: str) -> NXOpen.TaggedObject:
        """
        Gets the tagged object for the given property name. Exception will be raised if invalid property name is used. 
         Returns tagged_sc ( NXOpen.TaggedObject): Value to get for given property name. .
        """
        pass
    @overload
    def GetTaggedObjectVector(self, propertyName: str) -> List[NXOpen.TaggedObject]:
        """
        Gets the tagged object vector for the given property name. Exception will be raised if invalid property name is used. 
         Returns tagVector ( NXOpen.TaggedObject Li): Value to get for given property name. .
        """
        pass
    @overload
    def GetTaggedObjectVector(self, propertyIndex: int) -> List[NXOpen.TaggedObject]:
        """
        Gets the tagged object vector for the given index. Exception will be raised if invalid index is used. 
         Returns tagVector ( NXOpen.TaggedObject Li): Value to get for given property name. .
        """
        pass
    @overload
    def GetTaggedObject(self, propertyIndex: int) -> NXOpen.TaggedObject:
        """
        Gets the tagged object for the given index. Exception will be raised if invalid index is used. 
         Returns tagged_sc ( NXOpen.TaggedObject): Value to get for given index. .
        """
        pass
    @overload
    def GetUIBlock(self, propertyName: str) -> UIBlock:
        """
        Gets the UI Block for the given property name. Exception will be raised if invalid property name is used. 
         Returns uiblocks ( UIBlock NXOpen.B): Value to get for given property name. .
        """
        pass
    @overload
    def GetUIBlock(self, propertyIndex: int) -> UIBlock:
        """
        Gets the UI Block for the given index. Exception will be raised if invalid index is used. 
         Returns uiblocks ( UIBlock NXOpen.B): Value to get for given index. .
        """
        pass
    @overload
    def GetVector(self, propertyName: str) -> NXOpen.Vector3d:
        """
        Gets the vector value for the given property name. Exception will be raised if invalid property name is used. 
         Returns vector ( NXOpen.Vector3d): Value to get for given property name. .
        """
        pass
    @overload
    def GetVector(self, propertyIndex: int) -> NXOpen.Vector3d:
        """
        Gets the vector value for the given index. Exception will be raised if invalid index is used. 
         Returns vector ( NXOpen.Vector3d): Value to get for given index. .
        """
        pass
    def RemoveFilterMembers(self, propertyName: str, members: List[NXOpen.Select.FilterMember]) -> None:
        """
        Removes the filter members for the given property name. 
        """
        pass
    def SetBits(self, propertyName: str, bits_sc: int) -> None:
        """
        Sets the bits value for the given property name. Exception will be raised if invalid property name is used. 
        """
        pass
    def SetDouble(self, propertyName: str, value: float) -> None:
        """
        Sets the double value for the given property name. Exception will be raised if invalid property name is used. 
        """
        pass
    def SetDoubleMatrix(self, propertyName: str, nRows: int, nColumns: int, matrixValue: List[float]) -> None:
        """
        Sets the double matrix for the given property name. Exception will be raised if invalid property name is used.
                  This is a two dimensional array encoded into a single array. 
        """
        pass
    def SetDoubleVector(self, propertyName: str, doubleVector: List[float]) -> None:
        """
        Sets the double vector for the given property name. Exception will be raised if invalid property name is used. 
        """
        pass
    def SetEnum(self, propertyName: str, value: int) -> None:
        """
        Sets the value for the given property name. Exception will be raised if invalid property name is used. 
        """
        pass
    def SetEnumAsString(self, propertyName: str, value: str) -> None:
        """
         Sets the value for the given property name. Exception will be raised if invalid property name is used. 
        """
        pass
    def SetEnumMembers(self, propertyName: str, stringArray: List[str]) -> None:
        """
        Sets the enum members for the given property of type enum. Exception will be raised if invalid property name is used. 
        """
        pass
    def SetFile(self, propertyName: str, value: str) -> None:
        """
        Sets the value for the given property name. Exception will be raised if invalid property name is used. 
        """
        pass
    def SetInteger(self, propertyName: str, value: int) -> None:
        """
         Sets the integer value for the given property name. 
                    Exception will be raised if invalid property name is used.
        """
        pass
    def SetIntegerMatrix(self, propertyName: str, nRows: int, nColumns: int, matrixValue: List[int]) -> None:
        """
        Sets the integer matrix for the given property name. Exception will be raised if invalid property name is used.
                  This is a two dimensional array encoded into a single array. 
        """
        pass
    def SetIntegerVector(self, propertyName: str, intVector: List[int]) -> None:
        """
        Sets the integer vector for the given property name. Exception will be raised if invalid property name is used. 
        """
        pass
    def SetLogical(self, propertyName: str, value: bool) -> None:
        """
        Sets the logical value for the given property name. Exception will be raised if invalid property name is used.
        """
        pass
    def SetPoint(self, propertyName: str, point_sc: NXOpen.Point3d) -> None:
        """
        Sets the point value for the given property name. Exception will be raised if invalid property name is used. 
        """
        pass
    def SetSelectionFilter(self, propertyName: str, maskAction: NXOpen.Selection.SelectionAction, maskTriples: List[NXOpen.Selection.MaskTriple]) -> None:
        """
        Sets the filter for the given property name. 
        """
        pass
    def SetString(self, propertyName: str, value: str) -> None:
        """
        Sets the string value for the given property name. Exception will be raised if invalid property name is used. 
        """
        pass
    def SetStrings(self, propertyName: str, stringArray: List[str]) -> None:
        """
        Sets the strings value for the given property name. Exception will be raised if invalid property name is used. 
        """
        pass
    def SetTaggedObject(self, propertyName: str, tagged_sc: NXOpen.TaggedObject) -> None:
        """
        Sets the tagged object for the given property name. Exception will be raised if invalid property name is used. 
        """
        pass
    def SetTaggedObjectVector(self, propertyName: str, tagVector: List[NXOpen.TaggedObject]) -> None:
        """
        Sets the tagged object vector for the given property name. Exception will be raised if invalid property name is used. 
        """
        pass
    def SetVector(self, propertyName: str, vector: NXOpen.Vector3d) -> None:
        """
        Sets the vector value for the given property name. Exception will be raised if invalid property name is used. 
        """
        pass
import NXOpen
class RadiusDimension(UIBlock): 
    """ Represents a Radius Dimension block"""
    @property
    def AdaptiveScaleLimits(self) -> bool:
        """
        Getter for property: (bool) AdaptiveScaleLimits
         Returnsthe AdaptiveScaleLimits.  
          
                If true, indicates that the scale should be adaptive.  
         
        """
        pass
    @AdaptiveScaleLimits.setter
    def AdaptiveScaleLimits(self, scale_limits: bool):
        """
        Setter for property: (bool) AdaptiveScaleLimits
         Returnsthe AdaptiveScaleLimits.  
          
                If true, indicates that the scale should be adaptive.  
         
        """
        pass
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @property
    def ExpressionObject(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) ExpressionObject
         Returns the ExpressionObject  
            
         
        """
        pass
    @ExpressionObject.setter
    def ExpressionObject(self, expression_obj: NXOpen.TaggedObject):
        """
        Setter for property: ( NXOpen.TaggedObject) ExpressionObject
         Returns the ExpressionObject  
            
         
        """
        pass
    @property
    def Formula(self) -> str:
        """
        Getter for property: (str) Formula
         Returns the Formula  
            
         
        """
        pass
    @Formula.setter
    def Formula(self, formula: str):
        """
        Setter for property: (str) Formula
         Returns the Formula  
            
         
        """
        pass
    @property
    def HandleOrientation(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) HandleOrientation
         Returns the HandleOrientation  
            
         
        """
        pass
    @HandleOrientation.setter
    def HandleOrientation(self, orientation: NXOpen.Vector3d):
        """
        Setter for property: ( NXOpen.Vector3d) HandleOrientation
         Returns the HandleOrientation  
            
         
        """
        pass
    @property
    def HandleOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) HandleOrigin
         Returns the HandleOrigin  
            
         
        """
        pass
    @HandleOrigin.setter
    def HandleOrigin(self, handle_orogin: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) HandleOrigin
         Returns the HandleOrigin  
            
         
        """
        pass
    @property
    def LineIncrement(self) -> float:
        """
        Getter for property: (float) LineIncrement
         Returnsthe LineIncrement value.  
          
                Specifies the incrementdecrement when the user presses the arrow keys on the keyboard.
                Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
         
        """
        pass
    @LineIncrement.setter
    def LineIncrement(self, line_increment: float):
        """
        Setter for property: (float) LineIncrement
         Returnsthe LineIncrement value.  
          
                Specifies the incrementdecrement when the user presses the arrow keys on the keyboard.
                Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
         
        """
        pass
    @property
    def MaxInclusive(self) -> bool:
        """
        Getter for property: (bool) MaxInclusive
         Returns the MaxInclusive  
            
         
        """
        pass
    @MaxInclusive.setter
    def MaxInclusive(self, max_inclusive: bool):
        """
        Setter for property: (bool) MaxInclusive
         Returns the MaxInclusive  
            
         
        """
        pass
    @property
    def MaximumValue(self) -> float:
        """
        Getter for property: (float) MaximumValue
         Returns the MaximumValue  
            
         
        """
        pass
    @MaximumValue.setter
    def MaximumValue(self, max_value: float):
        """
        Setter for property: (float) MaximumValue
         Returns the MaximumValue  
            
         
        """
        pass
    @property
    def MinInclusive(self) -> bool:
        """
        Getter for property: (bool) MinInclusive
         Returns the MinInclusive  
            
         
        """
        pass
    @MinInclusive.setter
    def MinInclusive(self, min_inclusive: bool):
        """
        Setter for property: (bool) MinInclusive
         Returns the MinInclusive  
            
         
        """
        pass
    @property
    def MinimumValue(self) -> float:
        """
        Getter for property: (float) MinimumValue
         Returns the MinimumValue  
            
         
        """
        pass
    @MinimumValue.setter
    def MinimumValue(self, min_value: float):
        """
        Setter for property: (float) MinimumValue
         Returns the MinimumValue  
            
         
        """
        pass
    @property
    def PageIncrement(self) -> float:
        """
        Getter for property: (float) PageIncrement
         Returnsthe PageIncrement value.  
          
                Specifies the incrementdecrement when the user presses the Page Up or Page Down keys on the keyboard.
                Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
         
        """
        pass
    @PageIncrement.setter
    def PageIncrement(self, page_increment: float):
        """
        Setter for property: (float) PageIncrement
         Returnsthe PageIncrement value.  
          
                Specifies the incrementdecrement when the user presses the Page Up or Page Down keys on the keyboard.
                Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
         
        """
        pass
    @property
    def ShowFocusHandle(self) -> bool:
        """
        Getter for property: (bool) ShowFocusHandle
         Returns the ShowFocusHandle  
            
         
        """
        pass
    @ShowFocusHandle.setter
    def ShowFocusHandle(self, show_focus: bool):
        """
        Setter for property: (bool) ShowFocusHandle
         Returns the ShowFocusHandle  
            
         
        """
        pass
    @property
    def ShowHandle(self) -> bool:
        """
        Getter for property: (bool) ShowHandle
         Returns the ShowHandle  
            
         
        """
        pass
    @ShowHandle.setter
    def ShowHandle(self, show_handle: bool):
        """
        Setter for property: (bool) ShowHandle
         Returns the ShowHandle  
            
         
        """
        pass
    @property
    def SnapPointTypesOnByDefault(self) -> int:
        """
        Getter for property: (int) SnapPointTypesOnByDefault
         Returns the SnapPointTypesOnByDefault  
            
         
        """
        pass
    @SnapPointTypesOnByDefault.setter
    def SnapPointTypesOnByDefault(self, point_type: int):
        """
        Setter for property: (int) SnapPointTypesOnByDefault
         Returns the SnapPointTypesOnByDefault  
            
         
        """
        pass
    @property
    def Units(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) Units
         Returns the Units  
            
         
        """
        pass
    @Units.setter
    def Units(self, units: NXOpen.TaggedObject):
        """
        Setter for property: ( NXOpen.TaggedObject) Units
         Returns the Units  
            
         
        """
        pass
    @property
    def Value(self) -> float:
        """
        Getter for property: (float) Value
         Returns the Value.  
            
         
        """
        pass
    @Value.setter
    def Value(self, dimension_value: float):
        """
        Setter for property: (float) Value
         Returns the Value.  
            
         
        """
        pass
    @property
    def WithScale(self) -> bool:
        """
        Getter for property: (bool) WithScale
         Returns the WithScale  
            
         
        """
        pass
    @WithScale.setter
    def WithScale(self, with_scale: bool):
        """
        Setter for property: (bool) WithScale
         Returns the WithScale  
            
         
        """
        pass
    def GetBalloonTooltipLayoutMembers(self) -> List[str]:
        """
         Gets the BalloonTooltipLayout member 
         Returns layout_strings (List[str]): Values to get from the property. .
        """
        pass
    def TestValueChanged(self, dimension_value: float) -> None:
        """
        Tests dimension changed event workflow mapped to this RadiusDimension block.
        """
        pass
import NXOpen
class ReverseDirection(UIBlock): 
    """ Represents Reverse Direction block"""
    @property
    def Direction(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) Direction
         Returns the Direction.  
           It specifies the orientation of direction handle.  
         
        """
        pass
    @Direction.setter
    def Direction(self, direction: NXOpen.Vector3d):
        """
        Setter for property: ( NXOpen.Vector3d) Direction
         Returns the Direction.  
           It specifies the orientation of direction handle.  
         
        """
        pass
    @property
    def Flip(self) -> bool:
        """
        Getter for property: (bool) Flip
         Returns the Flip.  
           If true, the handle is flipped opposite of the direction.  
         
        """
        pass
    @Flip.setter
    def Flip(self, flip: bool):
        """
        Setter for property: (bool) Flip
         Returns the Flip.  
           If true, the handle is flipped opposite of the direction.  
         
        """
        pass
    @property
    def Origin(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) Origin
         Returns the Origin.  
           It specifies the origin of direction handle.  
         
        """
        pass
    @Origin.setter
    def Origin(self, origin: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) Origin
         Returns the Origin.  
           It specifies the origin of direction handle.  
         
        """
        pass
    def TestFlip(self, flip: bool) -> None:
        """
        Tests the handle flipped.
        """
        pass
class RGBColorPicker(UIBlock): 
    """ Represents a RGB Color Picker block"""
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @BalloonTooltipText.setter
    def BalloonTooltipText(self, tooltipText: str):
        """
        Setter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @property
    def Localize(self) -> bool:
        """
        Getter for property: (bool) Localize
         Returns the Localize.  
           If true, the Label is translated to current locale language.  
         
        """
        pass
    @Localize.setter
    def Localize(self, localize: bool):
        """
        Setter for property: (bool) Localize
         Returns the Localize.  
           If true, the Label is translated to current locale language.  
         
        """
        pass
    @property
    def RetainValue(self) -> bool:
        """
        Getter for property: (bool) RetainValue
         Returns the RetainValue.  
           If true, the block's value will be saved in dialog memory upon OK, Apply or Close.  
         
        """
        pass
    @RetainValue.setter
    def RetainValue(self, retain: bool):
        """
        Setter for property: (bool) RetainValue
         Returns the RetainValue.  
           If true, the block's value will be saved in dialog memory upon OK, Apply or Close.  
         
        """
        pass
    @property
    def Value(self) -> int:
        """
        Getter for property: (int) Value
         Returns the Value  
            
         
        """
        pass
    @Value.setter
    def Value(self, rgb_value: int):
        """
        Setter for property: (int) Value
         Returns the Value  
            
         
        """
        pass
    def GetBalloonTooltipLayoutMembers(self) -> List[str]:
        """
         Gets the BalloonTooltipLayout member 
         Returns layout_strings (List[str]): Values to get from the property. .
        """
        pass
    def TestValueChanged(self, rgb_value: int) -> None:
        """
        Tests value changed event workflow mapped to this RGB ColorPicker block.
        """
        pass
class ScrolledWindow(UIBlock): 
    """ Represents a Scrolled Window block"""
    @property
    def Height(self) -> int:
        """
        Getter for property: (int) Height
         Returns the Height  
            
         
        """
        pass
    @Height.setter
    def Height(self, height: int):
        """
        Setter for property: (int) Height
         Returns the Height  
            
         
        """
        pass
    @property
    def Members(self) -> PropertyList:
        """
        Getter for property: ( PropertyList NXOpen.B) Members
         Returns the Members  
            
         
        """
        pass
    @property
    def ResizeHeightWithDialog(self) -> bool:
        """
        Getter for property: (bool) ResizeHeightWithDialog
         Returns the ResizeHeightWithDialog.  
           If true, the height of block will dynamically change when the dialog is resized.  
         
        """
        pass
    @ResizeHeightWithDialog.setter
    def ResizeHeightWithDialog(self, resize: bool):
        """
        Setter for property: (bool) ResizeHeightWithDialog
         Returns the ResizeHeightWithDialog.  
           If true, the height of block will dynamically change when the dialog is resized.  
         
        """
        pass
    @property
    def Width(self) -> int:
        """
        Getter for property: (int) Width
         Returns the Width  
            
         
        """
        pass
    @Width.setter
    def Width(self, width: int):
        """
        Setter for property: (int) Width
         Returns the Width  
            
         
        """
        pass
import NXOpen
class SectionBuilder(UIBlock): 
    """ Represents a Section Builder"""
    @property
    def AllowConvergentObject(self) -> bool:
        """
        Getter for property: (bool) AllowConvergentObject
         Returns the AllowConvergentObject  
            
         
        """
        pass
    @AllowConvergentObject.setter
    def AllowConvergentObject(self, allowConvergentObject: bool):
        """
        Setter for property: (bool) AllowConvergentObject
         Returns the AllowConvergentObject  
            
         
        """
        pass
    @property
    def AllowConvergentObjectWithMixedGeometries(self) -> bool:
        """
        Getter for property: (bool) AllowConvergentObjectWithMixedGeometries
         Returns the AllowConvergentObjectWithMixedGeometries  
            
         
        """
        pass
    @AllowConvergentObjectWithMixedGeometries.setter
    def AllowConvergentObjectWithMixedGeometries(self, allowConvergentObjectWithMixedGeometries: bool):
        """
        Setter for property: (bool) AllowConvergentObjectWithMixedGeometries
         Returns the AllowConvergentObjectWithMixedGeometries  
            
         
        """
        pass
    @property
    def AllowInferredCurveSelection(self) -> bool:
        """
        Getter for property: (bool) AllowInferredCurveSelection
         Returns the AllowInferredCurveSelection  
            
         
        """
        pass
    @AllowInferredCurveSelection.setter
    def AllowInferredCurveSelection(self, allow: bool):
        """
        Setter for property: (bool) AllowInferredCurveSelection
         Returns the AllowInferredCurveSelection  
            
         
        """
        pass
    @property
    def AllowStopAtIntersectionFollowFillet(self) -> bool:
        """
        Getter for property: (bool) AllowStopAtIntersectionFollowFillet
         Returns the AllowStopAtIntersectionFollowFillet  
            
         
        """
        pass
    @AllowStopAtIntersectionFollowFillet.setter
    def AllowStopAtIntersectionFollowFillet(self, allow: bool):
        """
        Setter for property: (bool) AllowStopAtIntersectionFollowFillet
         Returns the AllowStopAtIntersectionFollowFillet  
            
         
        """
        pass
    @property
    def AngularTolerance(self) -> float:
        """
        Getter for property: (float) AngularTolerance
         Returns the AngularTolerance  
            
         
        """
        pass
    @AngularTolerance.setter
    def AngularTolerance(self, tolerance: float):
        """
        Setter for property: (float) AngularTolerance
         Returns the AngularTolerance  
            
         
        """
        pass
    @property
    def AutomaticProgression(self) -> bool:
        """
        Getter for property: (bool) AutomaticProgression
         Returns the AutomaticProgression.  
           If true, focus automatically progresses to the next selection block.  
         
        """
        pass
    @AutomaticProgression.setter
    def AutomaticProgression(self, automaticProgression: bool):
        """
        Setter for property: (bool) AutomaticProgression
         Returns the AutomaticProgression.  
           If true, focus automatically progresses to the next selection block.  
         
        """
        pass
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @property
    def Bitmap(self) -> str:
        """
        Getter for property: (str) Bitmap
         Returns the Bitmap  
            
         
        """
        pass
    @Bitmap.setter
    def Bitmap(self, bitmap_string: str):
        """
        Setter for property: (str) Bitmap
         Returns the Bitmap  
            
         
        """
        pass
    @property
    def BlendVirtualCurveOverlay(self) -> bool:
        """
        Getter for property: (bool) BlendVirtualCurveOverlay
         Returns the BlendVirtualCurveOverlay  
            
         
        """
        pass
    @BlendVirtualCurveOverlay.setter
    def BlendVirtualCurveOverlay(self, blendCurve: bool):
        """
        Setter for property: (bool) BlendVirtualCurveOverlay
         Returns the BlendVirtualCurveOverlay  
            
         
        """
        pass
    @property
    def ChainWithinFeature(self) -> bool:
        """
        Getter for property: (bool) ChainWithinFeature
         Returns the ChainWithinFeature  
            
         
        """
        pass
    @ChainWithinFeature.setter
    def ChainWithinFeature(self, chainWithinFeature: bool):
        """
        Setter for property: (bool) ChainWithinFeature
         Returns the ChainWithinFeature  
            
         
        """
        pass
    @property
    def CreateInterpartLink(self) -> bool:
        """
        Getter for property: (bool) CreateInterpartLink
         Returns the CreateInterpartLink  
            
         
        """
        pass
    @CreateInterpartLink.setter
    def CreateInterpartLink(self, createLink: bool):
        """
        Setter for property: (bool) CreateInterpartLink
         Returns the CreateInterpartLink  
            
         
        """
        pass
    @property
    def Cue(self) -> str:
        """
        Getter for property: (str) Cue
         Returns the Cue  
            
         
        """
        pass
    @Cue.setter
    def Cue(self, cue: str):
        """
        Setter for property: (str) Cue
         Returns the Cue  
            
         
        """
        pass
    @property
    def CurveRules(self) -> int:
        """
        Getter for property: (int) CurveRules
         Returns the CurveRules  
            
         
        """
        pass
    @CurveRules.setter
    def CurveRules(self, curveRules: int):
        """
        Setter for property: (int) CurveRules
         Returns the CurveRules  
            
         
        """
        pass
    @property
    def DefaultCurveRulesAsString(self) -> str:
        """
        Getter for property: (str) DefaultCurveRulesAsString
         Returns the DefaultCurveRules as string  
            
         
        """
        pass
    @DefaultCurveRulesAsString.setter
    def DefaultCurveRulesAsString(self, enumString: str):
        """
        Setter for property: (str) DefaultCurveRulesAsString
         Returns the DefaultCurveRules as string  
            
         
        """
        pass
    @property
    def EntityType(self) -> int:
        """
        Getter for property: (int) EntityType
         Returns the EntityType  
            
         
        """
        pass
    @EntityType.setter
    def EntityType(self, entityType: int):
        """
        Setter for property: (int) EntityType
         Returns the EntityType  
            
         
        """
        pass
    @property
    def FollowFillet(self) -> bool:
        """
        Getter for property: (bool) FollowFillet
         Returns the FollowFillet  
            
         
        """
        pass
    @FollowFillet.setter
    def FollowFillet(self, followFillet: bool):
        """
        Setter for property: (bool) FollowFillet
         Returns the FollowFillet  
            
         
        """
        pass
    @property
    def InferredCurveSelection(self) -> bool:
        """
        Getter for property: (bool) InferredCurveSelection
         Returns the InferredCurveSelection  
            
         
        """
        pass
    @InferredCurveSelection.setter
    def InferredCurveSelection(self, selectInferredCurve: bool):
        """
        Setter for property: (bool) InferredCurveSelection
         Returns the InferredCurveSelection  
            
         
        """
        pass
    @property
    def InterpartSelectionAsString(self) -> str:
        """
        Getter for property: (str) InterpartSelectionAsString
         Returns the InterpartSelection as string  
            
         
        """
        pass
    @InterpartSelectionAsString.setter
    def InterpartSelectionAsString(self, enumString: str):
        """
        Setter for property: (str) InterpartSelectionAsString
         Returns the InterpartSelection as string  
            
         
        """
        pass
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
         Returns the LabelString  
            
         
        """
        pass
    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
         Returns the LabelString  
            
         
        """
        pass
    @property
    def PointOverlay(self) -> bool:
        """
        Getter for property: (bool) PointOverlay
         Returns the PointOverlay  
            
         
        """
        pass
    @PointOverlay.setter
    def PointOverlay(self, overlay: bool):
        """
        Setter for property: (bool) PointOverlay
         Returns the PointOverlay  
            
         
        """
        pass
    @property
    def ShowFlowDirectionAndOriginCurve(self) -> bool:
        """
        Getter for property: (bool) ShowFlowDirectionAndOriginCurve
         Returns the ShowFlowDirectionAndOriginCurve  
            
         
        """
        pass
    @ShowFlowDirectionAndOriginCurve.setter
    def ShowFlowDirectionAndOriginCurve(self, show: bool):
        """
        Setter for property: (bool) ShowFlowDirectionAndOriginCurve
         Returns the ShowFlowDirectionAndOriginCurve  
            
         
        """
        pass
    @property
    def SmartUpdateOptionAsString(self) -> str:
        """
        Getter for property: (str) SmartUpdateOptionAsString
         Returns the update option for points created by the point overlay.  
          
                  
                Acceptable values are:
                
                 Within Modeling The smart object updates within Modeling in time stamp order. For example, if the smart object is referenced by Feature(i), the smart object will update after Feature (i-1) and right before Feature(i).
                 After Modeling The smart object updates after Modeling. Use for Drafting dimensions and other objects outside Modeling.
                 After Parent Body The smart object will always update after the last feature on the parent body.
                 Mixed The smart object will update after the last feature on the parent body when the parent body is in a different part; updates within Modeling in time-stamp order for parents in the same part.
                
                  
                  
         
        """
        pass
    @SmartUpdateOptionAsString.setter
    def SmartUpdateOptionAsString(self, enumString: str):
        """
        Setter for property: (str) SmartUpdateOptionAsString
         Returns the update option for points created by the point overlay.  
          
                  
                Acceptable values are:
                
                 Within Modeling The smart object updates within Modeling in time stamp order. For example, if the smart object is referenced by Feature(i), the smart object will update after Feature (i-1) and right before Feature(i).
                 After Modeling The smart object updates after Modeling. Use for Drafting dimensions and other objects outside Modeling.
                 After Parent Body The smart object will always update after the last feature on the parent body.
                 Mixed The smart object will update after the last feature on the parent body when the parent body is in a different part; updates within Modeling in time-stamp order for parents in the same part.
                
                  
                  
         
        """
        pass
    @property
    def SnapPointTypesEnabled(self) -> int:
        """
        Getter for property: (int) SnapPointTypesEnabled
         Returns the SnapPointTypesEnabled  
            
         
        """
        pass
    @SnapPointTypesEnabled.setter
    def SnapPointTypesEnabled(self, snapPointType: int):
        """
        Setter for property: (int) SnapPointTypesEnabled
         Returns the SnapPointTypesEnabled  
            
         
        """
        pass
    @property
    def SnapPointTypesOnByDefault(self) -> int:
        """
        Getter for property: (int) SnapPointTypesOnByDefault
         Returns the SnapPointTypesOnByDefault  
            
         
        """
        pass
    @SnapPointTypesOnByDefault.setter
    def SnapPointTypesOnByDefault(self, defaultSnapPointType: int):
        """
        Setter for property: (int) SnapPointTypesOnByDefault
         Returns the SnapPointTypesOnByDefault  
            
         
        """
        pass
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
         Returns the StepStatus as string  
            
         
        """
        pass
    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
         Returns the StepStatus as string  
            
         
        """
        pass
    @property
    def StopAtIntersection(self) -> bool:
        """
        Getter for property: (bool) StopAtIntersection
         Returns the StopAtIntersection  
            
         
        """
        pass
    @StopAtIntersection.setter
    def StopAtIntersection(self, stop: bool):
        """
        Setter for property: (bool) StopAtIntersection
         Returns the StopAtIntersection  
            
         
        """
        pass
    @property
    def ToolTip(self) -> str:
        """
        Getter for property: (str) ToolTip
         Returns the ToolTip  
            
         
        """
        pass
    @ToolTip.setter
    def ToolTip(self, toolTip: str):
        """
        Setter for property: (str) ToolTip
         Returns the ToolTip  
            
         
        """
        pass
    def GetBalloonTooltipLayoutMembers(self) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         Returns layout_strings (List[str]): Value to get from the property. .
        """
        pass
    def GetDefaultCurveRulesMembers(self) -> List[str]:
        """
         Gets the DefaultCurveRules members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def GetInterpartSelectionMembers(self) -> List[str]:
        """
         Gets the InterpartSelection members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def GetSelectedObjects(self) -> List[NXOpen.TaggedObject]:
        """
         Gets the SelectedObjects
         Returns objectVector ( NXOpen.TaggedObject Li): Value to get from the property.
        """
        pass
    def GetStepStatusMembers(self) -> List[str]:
        """
         Gets the StepStatus members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def SetSelectedObjects(self, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the SelectedObjects
        """
        pass
    def TestSelection(self, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Tests the selection for this block. The block must be in focus to call this API
        """
        pass
import NXOpen
class SelectElement(UIBlock): 
    """ Represents a Select Elements block"""
    @property
    def AutomaticProgression(self) -> bool:
        """
        Getter for property: (bool) AutomaticProgression
         Returns the AutomaticProgression.  
           If true, focus automatically progresses to next selection block.  
         
        """
        pass
    @AutomaticProgression.setter
    def AutomaticProgression(self, automaticProgression: bool):
        """
        Setter for property: (bool) AutomaticProgression
         Returns the AutomaticProgression.  
           If true, focus automatically progresses to next selection block.  
         
        """
        pass
    @property
    def Bitmap(self) -> str:
        """
        Getter for property: (str) Bitmap
         Returns the Bitmap  
            
         
        """
        pass
    @Bitmap.setter
    def Bitmap(self, bitmap_string: str):
        """
        Setter for property: (str) Bitmap
         Returns the Bitmap  
            
         
        """
        pass
    @property
    def Cue(self) -> str:
        """
        Getter for property: (str) Cue
         Returns the Cue  
            
         
        """
        pass
    @Cue.setter
    def Cue(self, cue: str):
        """
        Setter for property: (str) Cue
         Returns the Cue  
            
         
        """
        pass
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
         Returns the LabelString  
            
         
        """
        pass
    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
         Returns the LabelString  
            
         
        """
        pass
    @property
    def SelectModeAsString(self) -> str:
        """
        Getter for property: (str) SelectModeAsString
         Returns the SelectMode as string  
            
         
        """
        pass
    @SelectModeAsString.setter
    def SelectModeAsString(self, enumString: str):
        """
        Setter for property: (str) SelectModeAsString
         Returns the SelectMode as string  
            
         
        """
        pass
    @property
    def SelectSubTypeAsString(self) -> str:
        """
        Getter for property: (str) SelectSubTypeAsString
         Returns the SelectSubType as string  
            
         
        """
        pass
    @SelectSubTypeAsString.setter
    def SelectSubTypeAsString(self, enumString: str):
        """
        Setter for property: (str) SelectSubTypeAsString
         Returns the SelectSubType as string  
            
         
        """
        pass
    @property
    def ShowSelection(self) -> bool:
        """
        Getter for property: (bool) ShowSelection
         Returns the Show Selection.  
           If true, the graphical selection part of this block is shown.  
         
        """
        pass
    @ShowSelection.setter
    def ShowSelection(self, showSelection: bool):
        """
        Setter for property: (bool) ShowSelection
         Returns the Show Selection.  
           If true, the graphical selection part of this block is shown.  
         
        """
        pass
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
         Returns the StepStatus as string  
            
         
        """
        pass
    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
         Returns the StepStatus as string  
            
         
        """
        pass
    def GetSelectModeMembers(self) -> List[str]:
        """
         Gets the SelectMode members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def GetSelectSubTypeMembers(self) -> List[str]:
        """
         Gets the SelectSubType members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def GetSelectedObjects(self) -> List[NXOpen.TaggedObject]:
        """
         Gets the SelectedObjects
         Returns objectVector ( NXOpen.TaggedObject Li): Value to get from the property.
        """
        pass
    def GetSelectedObjectsSubIDs(self) -> List[int]:
        """
         Gets the SelectedObjectSubIDs
         Returns idVector (List[int]): Value to get from the property.
        """
        pass
    def GetStepStatusMembers(self) -> List[str]:
        """
         Gets the StepStatus members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def SetSelectedObjects(self, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the SelectedObjects
        """
        pass
    def SetSelectedObjectsSubIDs(self, idVector: List[int]) -> None:
        """
         Sets the SelectedObjectSubIDs
        """
        pass
    def TestSelection(self, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Tests the selection for this block. The block must be in focus to call this API
        """
        pass
import NXOpen
class SelectFacetRegion(UIBlock): 
    """ Represents a Select Region Selection block"""
    @property
    def AutomaticProgression(self) -> bool:
        """
        Getter for property: (bool) AutomaticProgression
         Returns the AutomaticProgression  
            
         
        """
        pass
    @AutomaticProgression.setter
    def AutomaticProgression(self, automaticProgression: bool):
        """
        Setter for property: (bool) AutomaticProgression
         Returns the AutomaticProgression  
            
         
        """
        pass
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @property
    def Bitmap(self) -> str:
        """
        Getter for property: (str) Bitmap
         Returns the Bitmap  
            
         
        """
        pass
    @Bitmap.setter
    def Bitmap(self, bitmap_string: str):
        """
        Setter for property: (str) Bitmap
         Returns the Bitmap  
            
         
        """
        pass
    @property
    def Cue(self) -> str:
        """
        Getter for property: (str) Cue
         Returns the Cue  
            
         
        """
        pass
    @Cue.setter
    def Cue(self, cue: str):
        """
        Setter for property: (str) Cue
         Returns the Cue  
            
         
        """
        pass
    @property
    def EnabledFacetCollectionRules(self) -> int:
        """
        Getter for property: (int) EnabledFacetCollectionRules
         Returns the FacetCollectionRules.  
          
                  
                These are the selection intent rules enabled for the facet selection region block 
                 
         
                
                It returns the following bit values,
                
                 0x1 if only Single Facet rule is enabled,
                 0x2 if only Face Facets rule is enabled,
                 0x3 if only Flood Fill rule is enabled,
                 0x4 if only Color Region rule is enabled
                
                
                  
         
        """
        pass
    @EnabledFacetCollectionRules.setter
    def EnabledFacetCollectionRules(self, rulesEnabled: int):
        """
        Setter for property: (int) EnabledFacetCollectionRules
         Returns the FacetCollectionRules.  
          
                  
                These are the selection intent rules enabled for the facet selection region block 
                 
         
                
                It returns the following bit values,
                
                 0x1 if only Single Facet rule is enabled,
                 0x2 if only Face Facets rule is enabled,
                 0x3 if only Flood Fill rule is enabled,
                 0x4 if only Color Region rule is enabled
                
                
                  
         
        """
        pass
    @property
    def FacetCollector(self) -> NXOpen.FacetCollector:
        """
        Getter for property: ( NXOpen.FacetCollector) FacetCollector
         Returns the OwningFacetCollector.  
          
                  
                The owning facet collector is an object of class  FacetCollector  that holds collected facets of the block
                 
         
                  
         
        """
        pass
    @FacetCollector.setter
    def FacetCollector(self, facetCollector: NXOpen.FacetCollector):
        """
        Setter for property: ( NXOpen.FacetCollector) FacetCollector
         Returns the OwningFacetCollector.  
          
                  
                The owning facet collector is an object of class  FacetCollector  that holds collected facets of the block
                 
         
                  
         
        """
        pass
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
         Returns the LabelString  
            
         
        """
        pass
    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
         Returns the LabelString  
            
         
        """
        pass
    @property
    def SelectedFacetCollectionRule(self) -> int:
        """
        Getter for property: (int) SelectedFacetCollectionRule
         Returns the active facet collection rule  
            
         
        """
        pass
    @SelectedFacetCollectionRule.setter
    def SelectedFacetCollectionRule(self, selectedRule: int):
        """
        Setter for property: (int) SelectedFacetCollectionRule
         Returns the active facet collection rule  
            
         
        """
        pass
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
         Returns the StepStatus as string  
            
         
        """
        pass
    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
         Returns the StepStatus as string  
            
         
        """
        pass
    @property
    def SupportedFacetTypes(self) -> int:
        """
        Getter for property: (int) SupportedFacetTypes
         Returns the SupportedFacetTypes.  
          
                  
                These are type of facets enabled in filters for select facet region block 
                 
         
                
                It returns following bits,
                
                 0x1 if only convergent facets are enabled,
                 0x2 if only NX facets are enabled,
                 0x3 if both convergent as well as NX facets are enabled.
                
                
                  
         
        """
        pass
    @SupportedFacetTypes.setter
    def SupportedFacetTypes(self, typesEnabled: int):
        """
        Setter for property: (int) SupportedFacetTypes
         Returns the SupportedFacetTypes.  
          
                  
                These are type of facets enabled in filters for select facet region block 
                 
         
                
                It returns following bits,
                
                 0x1 if only convergent facets are enabled,
                 0x2 if only NX facets are enabled,
                 0x3 if both convergent as well as NX facets are enabled.
                
                
                  
         
        """
        pass
    @property
    def ToolTip(self) -> str:
        """
        Getter for property: (str) ToolTip
         Returns the ToolTip  
            
         
        """
        pass
    @ToolTip.setter
    def ToolTip(self, toolTip: str):
        """
        Setter for property: (str) ToolTip
         Returns the ToolTip  
            
         
        """
        pass
    def GetBalloonTooltipLayoutMembers(self) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         Returns layout_strings (List[str]): Value to get from the property. .
        """
        pass
    def GetLastDeselectedObjects(self) -> List[NXOpen.TaggedObject]:
        """
         Gets the LastDeselectedFacetRegions
         Returns objectVector ( NXOpen.TaggedObject Li): Value to get from the property.
        """
        pass
    def GetLastSelectedObjects(self) -> List[NXOpen.TaggedObject]:
        """
         Gets the LastSelectedFacetRegions
         Returns objectVector ( NXOpen.TaggedObject Li): Value to get from the property.
        """
        pass
    def GetSelectedObjects(self) -> List[NXOpen.TaggedObject]:
        """
         Gets the SelectedFacetRegions
         Returns objectVector ( NXOpen.TaggedObject Li): Value to get from the property.
        """
        pass
    def GetStepStatusMembers(self) -> List[str]:
        """
         Gets the StepStatus members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def SetSelectedObjects(self, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the SelectedFacetRegions
        """
        pass
    def TestSelection(self, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Tests the selection for this block. The block must be in focus to call this API
        """
        pass
import NXOpen
class SelectFeature(UIBlock): 
    """ Represents a Select Feature block"""
    @property
    def AutomaticProgression(self) -> bool:
        """
        Getter for property: (bool) AutomaticProgression
         Returns the AutomaticProgression  
            
         
        """
        pass
    @AutomaticProgression.setter
    def AutomaticProgression(self, automaticProgression: bool):
        """
        Setter for property: (bool) AutomaticProgression
         Returns the AutomaticProgression  
            
         
        """
        pass
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @property
    def BlendVirtualCurveOverlay(self) -> bool:
        """
        Getter for property: (bool) BlendVirtualCurveOverlay
         Returns the BlendVirtualCurveOverlay.  
           If true, virtual curve is displayed during pre-selection.  
         
        """
        pass
    @BlendVirtualCurveOverlay.setter
    def BlendVirtualCurveOverlay(self, blendCurve: bool):
        """
        Setter for property: (bool) BlendVirtualCurveOverlay
         Returns the BlendVirtualCurveOverlay.  
           If true, virtual curve is displayed during pre-selection.  
         
        """
        pass
    @property
    def Cue(self) -> str:
        """
        Getter for property: (str) Cue
         Returns the Cue  
            
         
        """
        pass
    @Cue.setter
    def Cue(self, cue: str):
        """
        Setter for property: (str) Cue
         Returns the Cue  
            
         
        """
        pass
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
         Returns the LabelString  
            
         
        """
        pass
    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
         Returns the LabelString  
            
         
        """
        pass
    @property
    def SelectModeAsString(self) -> str:
        """
        Getter for property: (str) SelectModeAsString
         Returns the SelectMode as string  
            
         
        """
        pass
    @SelectModeAsString.setter
    def SelectModeAsString(self, enumString: str):
        """
        Setter for property: (str) SelectModeAsString
         Returns the SelectMode as string  
            
         
        """
        pass
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
         Returns the StepStatus as string  
            
         
        """
        pass
    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
         Returns the StepStatus as string  
            
         
        """
        pass
    @property
    def ToolTip(self) -> str:
        """
        Getter for property: (str) ToolTip
         Returns the ToolTip  
            
         
        """
        pass
    @ToolTip.setter
    def ToolTip(self, toolTip: str):
        """
        Setter for property: (str) ToolTip
         Returns the ToolTip  
            
         
        """
        pass
    def GetBalloonTooltipLayoutMembers(self) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         Returns layout_strings (List[str]): Value to get from the property. .
        """
        pass
    def GetSelectModeMembers(self) -> List[str]:
        """
         Gets the SelectMode members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def GetSelectedObjects(self) -> List[NXOpen.TaggedObject]:
        """
         Gets the SelectedObjects
         Returns objectVector ( NXOpen.TaggedObject Li): Value to get from the property.
        """
        pass
    def GetStepStatusMembers(self) -> List[str]:
        """
         Gets the StepStatus members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def SetSelectedObjects(self, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the SelectedObjects
        """
        pass
    def TestSelection(self, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Tests the selection for this block. The block must be in focus to call this API
        """
        pass
import NXOpen
class SelectNode(UIBlock): 
    """ Represents a Select Node block"""
    @property
    def AutomaticProgression(self) -> bool:
        """
        Getter for property: (bool) AutomaticProgression
         Returns the AutomaticProgression  
            
         
        """
        pass
    @AutomaticProgression.setter
    def AutomaticProgression(self, automaticProgression: bool):
        """
        Setter for property: (bool) AutomaticProgression
         Returns the AutomaticProgression  
            
         
        """
        pass
    @property
    def Bitmap(self) -> str:
        """
        Getter for property: (str) Bitmap
         Returns the Bitmap  
            
         
        """
        pass
    @Bitmap.setter
    def Bitmap(self, bitmap_string: str):
        """
        Setter for property: (str) Bitmap
         Returns the Bitmap  
            
         
        """
        pass
    @property
    def Cue(self) -> str:
        """
        Getter for property: (str) Cue
         Returns the Cue  
            
         
        """
        pass
    @Cue.setter
    def Cue(self, cue: str):
        """
        Setter for property: (str) Cue
         Returns the Cue  
            
         
        """
        pass
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
         Returns the LabelString  
            
         
        """
        pass
    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
         Returns the LabelString  
            
         
        """
        pass
    @property
    def SelectModeAsString(self) -> str:
        """
        Getter for property: (str) SelectModeAsString
         Returns the SelectMode as string  
            
         
        """
        pass
    @SelectModeAsString.setter
    def SelectModeAsString(self, enumString: str):
        """
        Setter for property: (str) SelectModeAsString
         Returns the SelectMode as string  
            
         
        """
        pass
    @property
    def ShowSelection(self) -> bool:
        """
        Getter for property: (bool) ShowSelection
         Returns the Show Selection.  
           If true,the graphical selection part of this block is shown.  
         
        """
        pass
    @ShowSelection.setter
    def ShowSelection(self, showSelection: bool):
        """
        Setter for property: (bool) ShowSelection
         Returns the Show Selection.  
           If true,the graphical selection part of this block is shown.  
         
        """
        pass
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
         Returns the StepStatus as string  
            
         
        """
        pass
    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
         Returns the StepStatus as string  
            
         
        """
        pass
    def GetSelectModeMembers(self) -> List[str]:
        """
         Gets the SelectMode members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def GetSelectedObjects(self) -> List[NXOpen.TaggedObject]:
        """
         Gets the SelectedObjects
         Returns objectVector ( NXOpen.TaggedObject Li): Value to get from the property.
        """
        pass
    def GetStepStatusMembers(self) -> List[str]:
        """
         Gets the StepStatus members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def SetSelectedObjects(self, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the SelectedObjects
        """
        pass
    def TestSelection(self, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Tests the selection for this block. The block must be in focus to call this API
        """
        pass
import NXOpen
import NXOpen.Select
class SelectObject(UIBlock): 
    """ Represents a Select Object block"""
    class FilterType(Enum):
        """
        Members Include: 
         |Features|  Filter to select all feature types 
         |Faces|  Filter to select all face types 
         |Edges|  Filter to select all edge types 
         |CurvesAndEdges|  Filter to select all curve and edge types 
         |Components|  Filter to select all components 
         |SolidBodies|  Filter to select all solid bodies 
         |SheetBodies|  Filter to select all sheet bodies 

        """
        Features: int
        Faces: int
        Edges: int
        CurvesAndEdges: int
        Components: int
        SolidBodies: int
        SheetBodies: int
        @staticmethod
        def ValueOf(value: int) -> SelectObject.FilterType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AllowConvergentObject(self) -> bool:
        """
        Getter for property: (bool) AllowConvergentObject
         Returns the AllowConvergentObject  
            
         
        """
        pass
    @AllowConvergentObject.setter
    def AllowConvergentObject(self, allowConvergentObject: bool):
        """
        Setter for property: (bool) AllowConvergentObject
         Returns the AllowConvergentObject  
            
         
        """
        pass
    @property
    def AllowConvergentObjectWithMixedGeometries(self) -> bool:
        """
        Getter for property: (bool) AllowConvergentObjectWithMixedGeometries
         Returns the AllowConvergentObjectWithMixedGeometries  
            
         
        """
        pass
    @AllowConvergentObjectWithMixedGeometries.setter
    def AllowConvergentObjectWithMixedGeometries(self, allowConvergentObjectWithMixedGeometries: bool):
        """
        Setter for property: (bool) AllowConvergentObjectWithMixedGeometries
         Returns the AllowConvergentObjectWithMixedGeometries  
            
         
        """
        pass
    @property
    def AutomaticProgression(self) -> bool:
        """
        Getter for property: (bool) AutomaticProgression
         Returns the AutomaticProgression  
            
         
        """
        pass
    @AutomaticProgression.setter
    def AutomaticProgression(self, automaticProgression: bool):
        """
        Setter for property: (bool) AutomaticProgression
         Returns the AutomaticProgression  
            
         
        """
        pass
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @property
    def Bitmap(self) -> str:
        """
        Getter for property: (str) Bitmap
         Returns the Bitmap  
            
         
        """
        pass
    @Bitmap.setter
    def Bitmap(self, bitmap_string: str):
        """
        Setter for property: (str) Bitmap
         Returns the Bitmap  
            
         
        """
        pass
    @property
    def BlendVirtualCurveOverlay(self) -> bool:
        """
        Getter for property: (bool) BlendVirtualCurveOverlay
         Returns the BlendVirtualCurveOverlay.  
           If true, virtual curve is displayed during preselection.  
         
        """
        pass
    @BlendVirtualCurveOverlay.setter
    def BlendVirtualCurveOverlay(self, blendCurve: bool):
        """
        Setter for property: (bool) BlendVirtualCurveOverlay
         Returns the BlendVirtualCurveOverlay.  
           If true, virtual curve is displayed during preselection.  
         
        """
        pass
    @property
    def CreateInterpartLink(self) -> bool:
        """
        Getter for property: (bool) CreateInterpartLink
         Returns the CreateInterpartLink  
            
         
        """
        pass
    @CreateInterpartLink.setter
    def CreateInterpartLink(self, createLink: bool):
        """
        Setter for property: (bool) CreateInterpartLink
         Returns the CreateInterpartLink  
            
         
        """
        pass
    @property
    def Cue(self) -> str:
        """
        Getter for property: (str) Cue
         Returns the Cue  
            
         
        """
        pass
    @Cue.setter
    def Cue(self, cue: str):
        """
        Setter for property: (str) Cue
         Returns the Cue  
            
         
        """
        pass
    @property
    def InterpartSelectionAsString(self) -> str:
        """
        Getter for property: (str) InterpartSelectionAsString
         Returns the InterpartSelection as string  
            
         
        """
        pass
    @InterpartSelectionAsString.setter
    def InterpartSelectionAsString(self, enumString: str):
        """
        Setter for property: (str) InterpartSelectionAsString
         Returns the InterpartSelection as string  
            
         
        """
        pass
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
         Returns the LabelString  
            
         
        """
        pass
    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
         Returns the LabelString  
            
         
        """
        pass
    @property
    def MaximumScopeAsString(self) -> str:
        """
        Getter for property: (str) MaximumScopeAsString
         Returns the MaximumScope as string  
            
         
        """
        pass
    @MaximumScopeAsString.setter
    def MaximumScopeAsString(self, enumString: str):
        """
        Setter for property: (str) MaximumScopeAsString
         Returns the MaximumScope as string  
            
         
        """
        pass
    @property
    def PickPoint(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) PickPoint
         Returns the PickPoint  
            
         
        """
        pass
    @property
    def PointOverlay(self) -> bool:
        """
        Getter for property: (bool) PointOverlay
         Returns the PointOverlay.  
           If true,on the fly point creation is allowed.  
         
        """
        pass
    @PointOverlay.setter
    def PointOverlay(self, pointOverlay: bool):
        """
        Setter for property: (bool) PointOverlay
         Returns the PointOverlay.  
           If true,on the fly point creation is allowed.  
         
        """
        pass
    @property
    def SelectModeAsString(self) -> str:
        """
        Getter for property: (str) SelectModeAsString
         Returns the SelectMode as string  
            
         
        """
        pass
    @SelectModeAsString.setter
    def SelectModeAsString(self, enumString: str):
        """
        Setter for property: (str) SelectModeAsString
         Returns the SelectMode as string  
            
         
        """
        pass
    @property
    def SmartUpdateOptionAsString(self) -> str:
        """
        Getter for property: (str) SmartUpdateOptionAsString
         Returns the update option for points created by the point overlay.  
          
                  
                Acceptable values are:
                
                 Within Modeling The smart object updates within Modeling in time stamp order. For example, if the smart object is referenced by Feature(i), the smart object will update after Feature (i-1) and right before Feature(i).
                 After Modeling The smart object updates after Modeling. Use for Drafting dimensions and other objects outside Modeling.
                 After Parent Body The smart object will always update after the last feature on the parent body.
                 Mixed The smart object will update after the last feature on the parent body when the parent body is in a different part; updates within Modeling in time-stamp order for parents in the same part.
                
                  
                  
         
        """
        pass
    @SmartUpdateOptionAsString.setter
    def SmartUpdateOptionAsString(self, enumString: str):
        """
        Setter for property: (str) SmartUpdateOptionAsString
         Returns the update option for points created by the point overlay.  
          
                  
                Acceptable values are:
                
                 Within Modeling The smart object updates within Modeling in time stamp order. For example, if the smart object is referenced by Feature(i), the smart object will update after Feature (i-1) and right before Feature(i).
                 After Modeling The smart object updates after Modeling. Use for Drafting dimensions and other objects outside Modeling.
                 After Parent Body The smart object will always update after the last feature on the parent body.
                 Mixed The smart object will update after the last feature on the parent body when the parent body is in a different part; updates within Modeling in time-stamp order for parents in the same part.
                
                  
                  
         
        """
        pass
    @property
    def SnapPointTypesEnabled(self) -> int:
        """
        Getter for property: (int) SnapPointTypesEnabled
         Returns the SnapPointTypesEnabled  
            
         
        """
        pass
    @SnapPointTypesEnabled.setter
    def SnapPointTypesEnabled(self, typesEnabled: int):
        """
        Setter for property: (int) SnapPointTypesEnabled
         Returns the SnapPointTypesEnabled  
            
         
        """
        pass
    @property
    def SnapPointTypesOnByDefault(self) -> int:
        """
        Getter for property: (int) SnapPointTypesOnByDefault
         Returns the SnapPointTypesOnByDefault  
            
         
        """
        pass
    @SnapPointTypesOnByDefault.setter
    def SnapPointTypesOnByDefault(self, typesByDefault: int):
        """
        Setter for property: (int) SnapPointTypesOnByDefault
         Returns the SnapPointTypesOnByDefault  
            
         
        """
        pass
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
         Returns the StepStatus as string  
            
         
        """
        pass
    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
         Returns the StepStatus as string  
            
         
        """
        pass
    @property
    def ToolTip(self) -> str:
        """
        Getter for property: (str) ToolTip
         Returns the ToolTip  
            
         
        """
        pass
    @ToolTip.setter
    def ToolTip(self, toolTip: str):
        """
        Setter for property: (str) ToolTip
         Returns the ToolTip  
            
         
        """
        pass
    @overload
    def AddFilter(self, filterTypes: int) -> None:
        """
                
                Adds the filters for select object block
                
                
                This method takes the integer value of the desired enum values from 
                NXOpen.BlockStyler.SelectObject.FilterType.
                
                 
        """
        pass
    def AddFilterMember(self, member: NXOpen.Select.FilterMember) -> None:
        """
                
                Adds a single filter member for select object block without clearing the filter
                
                
                This method takes the desired enumeration value from
                NXOpen.Select.FilterMember.
                
                 
        """
        pass
    def AddFilterMembers(self, members: List[NXOpen.Select.FilterMember]) -> None:
        """
                
                Adds specific filter members for select object block without clearing the filter
                
                
                This method takes the desired enumeration values from
                NXOpen.Select.FilterMember.
                
                 
        """
        pass
    @overload
    def AddFilter(self, filterTypes: SelectObject.FilterType) -> None:
        """
                
                Adds the filters for select object block 
                
                
                This method takes the desired enumeration value from
                NXOpen.BlockStyler.SelectObject.FilterType.
                
                
        """
        pass
    @overload
    def AddFilter(self, type: int, subType: int, solidBodyType: int) -> None:
        """
        Adds the filter for select object block using type, subtype and solidBodyType 
        """
        pass
    def ClearFilter(self) -> None:
        """
         Clears the filter for select object block  
        """
        pass
    def GetBalloonTooltipLayoutMembers(self) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         Returns layout_strings (List[str]): Value to get from the property. .
        """
        pass
    def GetInterpartSelectionMembers(self) -> List[str]:
        """
         Gets the InterpartSelection members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def GetLastDeselectedObjects(self) -> List[NXOpen.TaggedObject]:
        """
         Gets the LastDeselectedObjects
         Returns objectVector ( NXOpen.TaggedObject Li): Value to get from the property.
        """
        pass
    def GetLastSelectedObjects(self) -> List[NXOpen.TaggedObject]:
        """
         Gets the LastSelectedObjects
         Returns objectVector ( NXOpen.TaggedObject Li): Value to get from the property.
        """
        pass
    def GetMaximumScopeMembers(self) -> List[str]:
        """
         Gets the MaximumScope members 
         Returns scope_strings (List[str]): Value to get from the property. .
        """
        pass
    def GetSelectModeMembers(self) -> List[str]:
        """
         Gets the SelectMode members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def GetSelectedObjects(self) -> List[NXOpen.TaggedObject]:
        """
         Gets the SelectedObjects
         Returns objectVector ( NXOpen.TaggedObject Li): Value to get from the property.
        """
        pass
    def GetStepStatusMembers(self) -> List[str]:
        """
         Gets the StepStatus members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def RemoveFilterMember(self, member: NXOpen.Select.FilterMember) -> None:
        """
                
                Removes a single filter member from select object block
                
                
                This method takes the desired enumeration value from
                NXOpen.Select.FilterMember.
                
                 
        """
        pass
    def RemoveFilterMembers(self, members: List[NXOpen.Select.FilterMember]) -> None:
        """
                
                Removes specific filter members from select object block
                
                
                This method takes the desired enumeration values from
                NXOpen.Select.FilterMember.
                
                 
        """
        pass
    def ResetFilter(self) -> None:
        """
        Resets the filter for select object block 
        """
        pass
    def SetSelectedObjects(self, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the SelectedObjects
        """
        pass
    def SetSelectionFilter(self, maskAction: NXOpen.Selection.SelectionAction, maskTriples: List[NXOpen.Selection.MaskTriple]) -> None:
        """
         Sets the SelectionFilter
        """
        pass
    def TestSelection(self, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Tests the selection for this block. The block must be in focus to call this API
        """
        pass
import NXOpen
class SelectPartFromList(UIBlock): 
    """ Represents a Select Part From List block"""
    def GetSelectedObjects(self) -> List[NXOpen.TaggedObject]:
        """
         Gets the SelectedObjects
         Returns objectVector ( NXOpen.TaggedObject Li): Value to get from the property.
        """
        pass
    def SetSelectedObjects(self, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the SelectedObjects
        """
        pass
    def TestSelection(self, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Tests the selection for this block. The block must be in focus to call this API
        """
        pass
class Separator(UIBlock): 
    """ Represents a Separator block"""
    pass
class SetList(UIBlock): 
    """ Represents a SetList block """
    class InsertionLocation(Enum):
        """
        Members Include: 
         |Before|  
         |After|  

        """
        Before: int
        After: int
        @staticmethod
        def ValueOf(value: int) -> SetList.InsertionLocation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AddNewSetLabel(self) -> str:
        """
        Getter for property: (str) AddNewSetLabel
         Returns the AddNewSetLabel.  
           Specifies the label for AddNewSet button.  
         
        """
        pass
    @AddNewSetLabel.setter
    def AddNewSetLabel(self, label: str):
        """
        Setter for property: (str) AddNewSetLabel
         Returns the AddNewSetLabel.  
           Specifies the label for AddNewSet button.  
         
        """
        pass
    @property
    def DefaultColumnWidth(self) -> int:
        """
        Getter for property: (int) DefaultColumnWidth
         Returns the DefaultColumnWidth  
            
         
        """
        pass
    @DefaultColumnWidth.setter
    def DefaultColumnWidth(self, defaultWidth: int):
        """
        Setter for property: (int) DefaultColumnWidth
         Returns the DefaultColumnWidth  
            
         
        """
        pass
    @property
    def IsAddButtonSensitive(self) -> bool:
        """
        Getter for property: (bool) IsAddButtonSensitive
         Returns the IsAddButtonSensitive  
            
         
        """
        pass
    @IsAddButtonSensitive.setter
    def IsAddButtonSensitive(self, addButton: bool):
        """
        Setter for property: (bool) IsAddButtonSensitive
         Returns the IsAddButtonSensitive  
            
         
        """
        pass
    @property
    def LayoutAsString(self) -> str:
        """
        Getter for property: (str) LayoutAsString
         Returns the Layout as string  
            
         
        """
        pass
    @LayoutAsString.setter
    def LayoutAsString(self, enumString: str):
        """
        Setter for property: (str) LayoutAsString
         Returns the Layout as string  
            
         
        """
        pass
    @property
    def ListExpanded(self) -> bool:
        """
        Getter for property: (bool) ListExpanded
         Returns the ListExpanded.  
           If true, the list is expanded.  
         
        """
        pass
    @ListExpanded.setter
    def ListExpanded(self, expanded: bool):
        """
        Setter for property: (bool) ListExpanded
         Returns the ListExpanded.  
           If true, the list is expanded.  
         
        """
        pass
    @property
    def ListHideGroup(self) -> bool:
        """
        Getter for property: (bool) ListHideGroup
         Returns the ListHideGroup  
            
         
        """
        pass
    @ListHideGroup.setter
    def ListHideGroup(self, listHideGroup: bool):
        """
        Setter for property: (bool) ListHideGroup
         Returns the ListHideGroup  
            
         
        """
        pass
    @property
    def MaximumHeight(self) -> int:
        """
        Getter for property: (int) MaximumHeight
         Returns the MaximumHeight  
            
         
        """
        pass
    @MaximumHeight.setter
    def MaximumHeight(self, maxHeight: int):
        """
        Setter for property: (int) MaximumHeight
         Returns the MaximumHeight  
            
         
        """
        pass
    @property
    def MinimumHeight(self) -> int:
        """
        Getter for property: (int) MinimumHeight
         Returns the MinimumHeight  
            
         
        """
        pass
    @MinimumHeight.setter
    def MinimumHeight(self, minHeight: int):
        """
        Setter for property: (int) MinimumHeight
         Returns the MinimumHeight  
            
         
        """
        pass
    @property
    def MultipleEdit(self) -> bool:
        """
        Getter for property: (bool) MultipleEdit
         Returns the MultipleEdit  
            
         
        """
        pass
    @MultipleEdit.setter
    def MultipleEdit(self, multipleEdit: bool):
        """
        Setter for property: (bool) MultipleEdit
         Returns the MultipleEdit  
            
         
        """
        pass
    @property
    def NumberColumnString(self) -> str:
        """
        Getter for property: (str) NumberColumnString
         Returns the NumberColumnString as string  
            
         
        """
        pass
    @NumberColumnString.setter
    def NumberColumnString(self, columnString: str):
        """
        Setter for property: (str) NumberColumnString
         Returns the NumberColumnString as string  
            
         
        """
        pass
    @property
    def NumberOfColumns(self) -> int:
        """
        Getter for property: (int) NumberOfColumns
         Returns the NumberOfColumns  
            
         
        """
        pass
    @NumberOfColumns.setter
    def NumberOfColumns(self, numColumns: int):
        """
        Setter for property: (int) NumberOfColumns
         Returns the NumberOfColumns  
            
         
        """
        pass
    @property
    def ResizeHeightWithDialog(self) -> bool:
        """
        Getter for property: (bool) ResizeHeightWithDialog
         Returns the ResizeHeightWithDialog.  
           If true, height of the block changes dynamically with dialog.  
         
        """
        pass
    @ResizeHeightWithDialog.setter
    def ResizeHeightWithDialog(self, resize: bool):
        """
        Setter for property: (bool) ResizeHeightWithDialog
         Returns the ResizeHeightWithDialog.  
           If true, height of the block changes dynamically with dialog.  
         
        """
        pass
    @property
    def SeedDlxFile(self) -> str:
        """
        Getter for property: (str) SeedDlxFile
         Returns the SeedDlxFile as string  
            
         
        """
        pass
    @SeedDlxFile.setter
    def SeedDlxFile(self, dlxName: str):
        """
        Setter for property: (str) SeedDlxFile
         Returns the SeedDlxFile as string  
            
         
        """
        pass
    @property
    def ShowAddNewSet(self) -> bool:
        """
        Getter for property: (bool) ShowAddNewSet
         Returns the ShowAddNewSet.  
           If true, "Add New Set" button is shown.  
         
        """
        pass
    @ShowAddNewSet.setter
    def ShowAddNewSet(self, show: bool):
        """
        Setter for property: (bool) ShowAddNewSet
         Returns the ShowAddNewSet.  
           If true, "Add New Set" button is shown.  
         
        """
        pass
    @property
    def ShowColumnHeadings(self) -> bool:
        """
        Getter for property: (bool) ShowColumnHeadings
         Returns the ShowColumnHeadings  
            
         
        """
        pass
    @ShowColumnHeadings.setter
    def ShowColumnHeadings(self, show: bool):
        """
        Setter for property: (bool) ShowColumnHeadings
         Returns the ShowColumnHeadings  
            
         
        """
        pass
    @property
    def ShowRemove(self) -> bool:
        """
        Getter for property: (bool) ShowRemove
         Returns the ShowRemove.  
           If true, "Remove" button is shown.  
         
        """
        pass
    @ShowRemove.setter
    def ShowRemove(self, show: bool):
        """
        Setter for property: (bool) ShowRemove
         Returns the ShowRemove.  
           If true, "Remove" button is shown.  
         
        """
        pass
    @property
    def ShowReorderControls(self) -> bool:
        """
        Getter for property: (bool) ShowReorderControls
         Returns the ShowReorderControls  
            
         
        """
        pass
    @ShowReorderControls.setter
    def ShowReorderControls(self, show: bool):
        """
        Setter for property: (bool) ShowReorderControls
         Returns the ShowReorderControls  
            
         
        """
        pass
    AddCallback = Callable[[SetList], None]
    def AddNewSet(self, copyPropertiesAndSelect: bool) -> UIBlock:
        """
         Adds an item to the end of the list 
         Returns uicomp ( UIBlock NXOpen.B):  The added item .
        """
        pass
    def Delete(self, uicomp: UIBlock) -> None:
        """
         Deletes an item from the list 
        """
        pass
    DeleteCallback = Callable[[SetList, UIBlock], None]
    def FindUpdated(self) -> UIBlock:
        """
         When an update event occurs on the list, this method finds the
            item in the list that was updated 
         Returns item ( UIBlock NXOpen.B): .
        """
        pass
    def GetColumnLabels(self) -> List[str]:
        """
         Gets the ColumnLabels
         Returns labels (List[str]):  Values to get from the property.
        """
        pass
    def GetColumnWidths(self) -> List[int]:
        """
         Gets the ColumnWidths
         Returns width (List[int]):  Values to get from the property.
        """
        pass
    def GetItemText(self, item: UIBlock) -> List[str]:
        """
         Gets the text for the specified item.
                If the list has a title column, the title column is not included in the item text. 
         Returns strings (List[str]):  The text .
        """
        pass
    def GetItems(self) -> List[UIBlock]:
        """
         Gets all the items in the list 
         Returns items ( UIBlock List[NXOpen): .
        """
        pass
    def GetLayoutMembers(self) -> List[str]:
        """
         Gets the Layout members
         Returns member_strings (List[str]): .
        """
        pass
    def GetSelected(self) -> List[UIBlock]:
        """
         Gets the selected items 
         Returns items ( UIBlock List[NXOpen): .
        """
        pass
    def InsertNewSet(self, location: UIBlock, insertBeforeOrAfter: SetList.InsertionLocation, copyPropertiesAndSelect: bool) -> UIBlock:
        """
         Inserts an item before or after a specified item 
         Returns uicomp ( UIBlock NXOpen.B):  The inserted item .
        """
        pass
    ReorderCallback = Callable[[SetList, UIBlock, int, int], None]
    def SetAddHandler(self, cb: SetList.AddCallback) -> None:
        """
         Sets the AddNewSet handler.  If you set this handler, the handler will be
            called when the Add New Set button is pressed, and the handler will be responsible
            for adding an item to the list.  Nothing will be added to the list unless the handler
            adds it. 
        """
        pass
    def SetColumnLabels(self, labels: List[str]) -> None:
        """
         Sets the ColumnLabels
        """
        pass
    def SetColumnWidths(self, width: List[int]) -> None:
        """
         Sets the ColumnWidths
        """
        pass
    def SetDeleteHandler(self, cb: SetList.DeleteCallback) -> None:
        """
         Sets the Delete handler.  If you set this handler, the handler will be
            called when the Delete button is pressed.  The handler does not need to implement code
            to delete the item.  The list will delete the item if and only if the handler returns 0. 
        """
        pass
    def SetItemText(self, item: UIBlock, strings: List[str]) -> None:
        """
         Sets the text for the specified item.
                If the list has a title column, the title column is not included in the item text. 
        """
        pass
    def SetReorderObserver(self, cb: SetList.ReorderCallback) -> None:
        """
         Sets the Reorder observer.  If you set this observer, the observer will
            be called after an item is moved by pressing the Move Up and Down buttons.
            The observer does not need to implement the move up and down behavior and is called
            after the item has already been moved. 
        """
        pass
    def SetSeed(self, dlxFile: str) -> None:
        """
         Sets the seed using a dlx file.  The seed must be set during initialization.
            Setting the seed will also reset any Add and Delete handlers that has been registered,
            so SetSeed should be called prior to calling SetAddHandler or SetDeleteHandler. 
        """
        pass
    def SetSelected(self, items: List[UIBlock]) -> None:
        """
         Sets the selected items.  If the "Multiple Edit" property is false,
            no more than one item can be selected 
        """
        pass
    def Swap(self, uicomp1: UIBlock, uicomp2: UIBlock) -> None:
        """
         Swaps the location of two items 
        """
        pass
    def TestItemAdded(self) -> None:
        """
        Tests add event mapped to this SetList block.
        """
        pass
    def TestItemDeleted(self) -> None:
        """
        Tests delete event mapped to this SetList block.
        """
        pass
    def TestItemMovedDown(self) -> None:
        """
        Tests move down event mapped to this SetList block.
        """
        pass
    def TestItemMovedUp(self) -> None:
        """
        Tests move up event mapped to this SetList block.
        """
        pass
import NXOpen
class SpecifyAxis(UIBlock): 
    """ Represents a Specify Axis block"""
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @property
    def BalloonTooltipPointImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipPointImage
         Returns the BalloonTooltipPointImage  
            
         
        """
        pass
    @BalloonTooltipPointImage.setter
    def BalloonTooltipPointImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipPointImage
         Returns the BalloonTooltipPointImage  
            
         
        """
        pass
    @property
    def BalloonTooltipPointText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipPointText
         Returns the BalloonTooltipPointText  
            
         
        """
        pass
    @BalloonTooltipPointText.setter
    def BalloonTooltipPointText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipPointText
         Returns the BalloonTooltipPointText  
            
         
        """
        pass
    @property
    def BalloonTooltipVectorImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipVectorImage
         Returns the BalloonTooltipVectorImage  
            
         
        """
        pass
    @BalloonTooltipVectorImage.setter
    def BalloonTooltipVectorImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipVectorImage
         Returns the BalloonTooltipVectorImage  
            
         
        """
        pass
    @property
    def BalloonTooltipVectorText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipVectorText
         Returns the BalloonTooltipVectorText  
            
         
        """
        pass
    @BalloonTooltipVectorText.setter
    def BalloonTooltipVectorText(self, tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipVectorText
         Returns the BalloonTooltipVectorText  
            
         
        """
        pass
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
         Returns the StepStatus as string  
            
         
        """
        pass
    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
         Returns the StepStatus as string  
            
         
        """
        pass
    def GetBalloonTooltipLayoutMembers(self) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         Returns layout_strings (List[str]): Value to get from the property. .
        """
        pass
    def GetSelectedObjects(self) -> List[NXOpen.TaggedObject]:
        """
         Gets the SelectedObjects
         Returns objectVector ( NXOpen.TaggedObject Li): Value to get from the property.
        """
        pass
    def GetStepStatusMembers(self) -> List[str]:
        """
         Gets the StepStatus members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def SetSelectedObjects(self, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the SelectedObjects
        """
        pass
    def TestSelection(self, objectVector: NXOpen.TaggedObject) -> None:
        """
         Tests the selection for this block. The block must be in focus to call this API
        """
        pass
import NXOpen
class SpecifyCSYS(UIBlock): 
    """ Represents a Specify CSYS block"""
    @property
    def AutomaticProgression(self) -> bool:
        """
        Getter for property: (bool) AutomaticProgression
         Returns the AutomaticProgression  
            
         
        """
        pass
    @AutomaticProgression.setter
    def AutomaticProgression(self, automaticProgression: bool):
        """
        Setter for property: (bool) AutomaticProgression
         Returns the AutomaticProgression  
            
         
        """
        pass
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @property
    def CreateInterpartLink(self) -> bool:
        """
        Getter for property: (bool) CreateInterpartLink
         Returns the CreateInterpartLink  
            
         
        """
        pass
    @CreateInterpartLink.setter
    def CreateInterpartLink(self, createLink: bool):
        """
        Setter for property: (bool) CreateInterpartLink
         Returns the CreateInterpartLink  
            
         
        """
        pass
    @property
    def InterpartSelectionAsString(self) -> str:
        """
        Getter for property: (str) InterpartSelectionAsString
         Returns the InterpartSelection as string  
            
         
        """
        pass
    @InterpartSelectionAsString.setter
    def InterpartSelectionAsString(self, enumString: str):
        """
        Setter for property: (str) InterpartSelectionAsString
         Returns the InterpartSelection as string  
            
         
        """
        pass
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
         Returns the LabelString  
            
         
        """
        pass
    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
         Returns the LabelString  
            
         
        """
        pass
    @property
    def OutputTypeAsString(self) -> str:
        """
        Getter for property: (str) OutputTypeAsString
         Returns the OutputType as string  
            
         
        """
        pass
    @OutputTypeAsString.setter
    def OutputTypeAsString(self, enumString: str):
        """
        Setter for property: (str) OutputTypeAsString
         Returns the OutputType as string  
            
         
        """
        pass
    @property
    def ShowShortcuts(self) -> bool:
        """
        Getter for property: (bool) ShowShortcuts
         Returns the ShowShortcuts  
            
         
        """
        pass
    @ShowShortcuts.setter
    def ShowShortcuts(self, show: bool):
        """
        Setter for property: (bool) ShowShortcuts
         Returns the ShowShortcuts  
            
         
        """
        pass
    @property
    def SmartUpdateOptionAsString(self) -> str:
        """
        Getter for property: (str) SmartUpdateOptionAsString
         Returns the SmartUpdateOption as string  
            
         
        """
        pass
    @SmartUpdateOptionAsString.setter
    def SmartUpdateOptionAsString(self, enumString: str):
        """
        Setter for property: (str) SmartUpdateOptionAsString
         Returns the SmartUpdateOption as string  
            
         
        """
        pass
    @property
    def SmartUpdteOptionAsString(self) -> str:
        """
        Getter for property: (str) SmartUpdteOptionAsString
         Returns the SmartUpdateOption as string  
            
         
        """
        pass
    @SmartUpdteOptionAsString.setter
    def SmartUpdteOptionAsString(self, enumString: str):
        """
        Setter for property: (str) SmartUpdteOptionAsString
         Returns the SmartUpdateOption as string  
            
         
        """
        pass
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
         Returns the StepStatus as string  
            
         
        """
        pass
    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
         Returns the StepStatus as string  
            
         
        """
        pass
    def GetBalloonTooltipLayoutMembers(self) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         Returns layout_strings (List[str]): Value to get from the property. .
        """
        pass
    def GetInterpartSelectionMembers(self) -> List[str]:
        """
         Gets the InterpartSelection members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def GetOutputTypeMembers(self) -> List[str]:
        """
         Gets the OutputType members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def GetSelectedObjects(self) -> List[NXOpen.TaggedObject]:
        """
         Gets the SelectedObjects
         Returns objectVector ( NXOpen.TaggedObject Li): Value to get from the property.
        """
        pass
    def GetSmartUpdateOptionMembers(self) -> List[str]:
        """
         Gets the SmartUpdateOption members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def GetSmartUpdteOptionMembers(self) -> List[str]:
        """
         Gets the SmartUpdateOption members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def GetStepStatusMembers(self) -> List[str]:
        """
         Gets the StepStatus members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def SetSelectedObjects(self, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the SelectedObjects
        """
        pass
    def TestSelection(self, objectVector: NXOpen.TaggedObject) -> None:
        """
         Tests the selection for this block. The block must be in focus to call this API
        """
        pass
import NXOpen
class SpecifyLocation(UIBlock): 
    """ Represents a Specify Location block"""
    @property
    def AutomaticProgression(self) -> bool:
        """
        Getter for property: (bool) AutomaticProgression
         Returns the AutomaticProgression  
            
         
        """
        pass
    @AutomaticProgression.setter
    def AutomaticProgression(self, automaticProgression: bool):
        """
        Setter for property: (bool) AutomaticProgression
         Returns the AutomaticProgression  
            
         
        """
        pass
    @property
    def CursorLocation(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) CursorLocation
         Returns the CursorLocation  
            
         
        """
        pass
    @CursorLocation.setter
    def CursorLocation(self, cursorLocation: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) CursorLocation
         Returns the CursorLocation  
            
         
        """
        pass
    @property
    def DisplayTemporaryPoint(self) -> bool:
        """
        Getter for property: (bool) DisplayTemporaryPoint
         Returns the DisplayTemporaryPoint  
            
         
        """
        pass
    @DisplayTemporaryPoint.setter
    def DisplayTemporaryPoint(self, display: bool):
        """
        Setter for property: (bool) DisplayTemporaryPoint
         Returns the DisplayTemporaryPoint  
            
         
        """
        pass
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
         Returns the LabelString  
            
         
        """
        pass
    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
         Returns the LabelString  
            
         
        """
        pass
    @property
    def LocationSpecified(self) -> bool:
        """
        Getter for property: (bool) LocationSpecified
         Returns whether the cursor location has been set or not.  
           Initially, this will return false, 
                    but will return true after the user has specified a location interactively, 
                    or if   SetCursorLocation  is set programmatically. 
                    Calling  ResetCursorLocation  will also reset this property back to false. 
                    If this property is false, then the value of  CursorLocation  is meaningless  
         
        """
        pass
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
         Returns the StepStatus as string  
            
         
        """
        pass
    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
         Returns the StepStatus as string  
            
         
        """
        pass
    def GetStepStatusMembers(self) -> List[str]:
        """
         Gets the StepStatus members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def ResetCursorLocation(self) -> None:
        """
         Reset the cursor location
        """
        pass
    def TestCursorLocationSpecified(self, cursorLocation: NXOpen.Point3d) -> None:
        """
         Tests the cursor location specified for this block. The block must be in focus to call this API
        """
        pass
import NXOpen
class SpecifyOrientation(UIBlock): 
    """ Represents Specify Orientation block"""
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @property
    def EnableDoubleClickFlip(self) -> bool:
        """
        Getter for property: (bool) EnableDoubleClickFlip
         Returns the EnableDoubleClickFlip.  
           If true, flipping is allowed when direction handle is double clicked.  
         
        """
        pass
    @EnableDoubleClickFlip.setter
    def EnableDoubleClickFlip(self, enableFlip: bool):
        """
        Setter for property: (bool) EnableDoubleClickFlip
         Returns the EnableDoubleClickFlip.  
           If true, flipping is allowed when direction handle is double clicked.  
         
        """
        pass
    @property
    def EnableFacetSelection(self) -> bool:
        """
        Getter for property: (bool) EnableFacetSelection
         Returns the EnableFacetSelection  
            
         
        """
        pass
    @EnableFacetSelection.setter
    def EnableFacetSelection(self, enableSelection: bool):
        """
        Setter for property: (bool) EnableFacetSelection
         Returns the EnableFacetSelection  
            
         
        """
        pass
    @property
    def HasOriginGwif(self) -> bool:
        """
        Getter for property: (bool) HasOriginGwif
         Returns the HasOriginGwif  
            
         
        """
        pass
    @HasOriginGwif.setter
    def HasOriginGwif(self, originGwif: bool):
        """
        Setter for property: (bool) HasOriginGwif
         Returns the HasOriginGwif  
            
         
        """
        pass
    @property
    def IsOriginSpecified(self) -> bool:
        """
        Getter for property: (bool) IsOriginSpecified
         Returns the IsOriginSpecified  
            
         
        """
        pass
    @IsOriginSpecified.setter
    def IsOriginSpecified(self, originSpecified: bool):
        """
        Setter for property: (bool) IsOriginSpecified
         Returns the IsOriginSpecified  
            
         
        """
        pass
    @property
    def IsWCSCoordinates(self) -> bool:
        """
        Getter for property: (bool) IsWCSCoordinates
         Returns the IsWCSCoordinates  
            
         
        """
        pass
    @IsWCSCoordinates.setter
    def IsWCSCoordinates(self, wcsCoordinates: bool):
        """
        Setter for property: (bool) IsWCSCoordinates
         Returns the IsWCSCoordinates  
            
         
        """
        pass
    @property
    def Origin(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) Origin
         Returns the Origin  
            
         
        """
        pass
    @Origin.setter
    def Origin(self, origin: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) Origin
         Returns the Origin  
            
         
        """
        pass
    @property
    def SnapPointTypesOnByDefault(self) -> int:
        """
        Getter for property: (int) SnapPointTypesOnByDefault
         Returns the SnapPointTypesOnByDefault  
            
         
        """
        pass
    @SnapPointTypesOnByDefault.setter
    def SnapPointTypesOnByDefault(self, snapPointTypes: int):
        """
        Setter for property: (int) SnapPointTypesOnByDefault
         Returns the SnapPointTypesOnByDefault  
            
         
        """
        pass
    @property
    def VisibleManipulatorHandles(self) -> int:
        """
        Getter for property: (int) VisibleManipulatorHandles
         Returns the VisibleManipulatorHandles.  
           It specifies the options to display the handles available on triad. The translation, rotation and origin handles are available.  
         
        """
        pass
    @VisibleManipulatorHandles.setter
    def VisibleManipulatorHandles(self, handles: int):
        """
        Setter for property: (int) VisibleManipulatorHandles
         Returns the VisibleManipulatorHandles.  
           It specifies the options to display the handles available on triad. The translation, rotation and origin handles are available.  
         
        """
        pass
    @property
    def XAxis(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) XAxis
         Returns the XAxis  
            
         
        """
        pass
    @XAxis.setter
    def XAxis(self, xAxis: NXOpen.Vector3d):
        """
        Setter for property: ( NXOpen.Vector3d) XAxis
         Returns the XAxis  
            
         
        """
        pass
    @property
    def YAxis(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) YAxis
         Returns the YAxis  
            
         
        """
        pass
    @YAxis.setter
    def YAxis(self, yAxis: NXOpen.Vector3d):
        """
        Setter for property: ( NXOpen.Vector3d) YAxis
         Returns the YAxis  
            
         
        """
        pass
    def GetBalloonTooltipLayoutMembers(self) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         Returns layout_strings (List[str]): Value to get from the property. .
        """
        pass
    def TestOriginSpecified(self, origin: NXOpen.Point3d) -> None:
        """
         Tests the origin of orientation specified for this block. The block must be in focus to call this API
        """
        pass
    def TestXAxisSpecified(self, xAxis: NXOpen.Vector3d) -> None:
        """
         Tests the X-Axis of orientation specified for this block. The block must be in focus to call this API
        """
        pass
    def TestYAxisSpecified(self, yAxis: NXOpen.Vector3d) -> None:
        """
         Tests the Y-Axis of orientation specified for this block. The block must be in focus to call this API
        """
        pass
import NXOpen
class SpecifyPlane(UIBlock): 
    """ Represents a Specify Plane block"""
    @property
    def AutomaticProgression(self) -> bool:
        """
        Getter for property: (bool) AutomaticProgression
         Returns the AutomaticProgression  
            
         
        """
        pass
    @AutomaticProgression.setter
    def AutomaticProgression(self, automaticProgression: bool):
        """
        Setter for property: (bool) AutomaticProgression
         Returns the AutomaticProgression  
            
         
        """
        pass
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @property
    def CreateInterpartLink(self) -> bool:
        """
        Getter for property: (bool) CreateInterpartLink
         Returns the CreateInterpartLink  
            
         
        """
        pass
    @CreateInterpartLink.setter
    def CreateInterpartLink(self, createLink: bool):
        """
        Setter for property: (bool) CreateInterpartLink
         Returns the CreateInterpartLink  
            
         
        """
        pass
    @property
    def CurrentStepStatusAsString(self) -> str:
        """
        Getter for property: (str) CurrentStepStatusAsString
         Returns the string specifying current StepStatus   
            
         
        """
        pass
    @property
    def InterpartSelectionAsString(self) -> str:
        """
        Getter for property: (str) InterpartSelectionAsString
         Returns the InterpartSelection as string  
            
         
        """
        pass
    @InterpartSelectionAsString.setter
    def InterpartSelectionAsString(self, enumString: str):
        """
        Setter for property: (str) InterpartSelectionAsString
         Returns the InterpartSelection as string  
            
         
        """
        pass
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
         Returns the LabelString  
            
         
        """
        pass
    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
         Returns the LabelString  
            
         
        """
        pass
    @property
    def ShowShortcuts(self) -> bool:
        """
        Getter for property: (bool) ShowShortcuts
         Returns the ShowShortcuts  
            
         
        """
        pass
    @ShowShortcuts.setter
    def ShowShortcuts(self, show: bool):
        """
        Setter for property: (bool) ShowShortcuts
         Returns the ShowShortcuts  
            
         
        """
        pass
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
         Returns the string specifying the default StepStatus   
            
         
        """
        pass
    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
         Returns the string specifying the default StepStatus   
            
         
        """
        pass
    def GetBalloonTooltipLayoutMembers(self) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         Returns layout_strings (List[str]): Value to get from the property. .
        """
        pass
    def GetInterpartSelectionMembers(self) -> List[str]:
        """
         Gets the InterpartSelection members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def GetSelectedObjects(self) -> List[NXOpen.TaggedObject]:
        """
         Gets the SelectedObjects
         Returns objectVector ( NXOpen.TaggedObject Li): Value to get from the property.
        """
        pass
    def GetStepStatusMembers(self) -> List[str]:
        """
         Gets the StepStatus members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def SetSelectedObjects(self, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the SelectedObjects
        """
        pass
    def TestSelection(self, objectVector: NXOpen.TaggedObject) -> None:
        """
         Tests the selection for this block. The block must be in focus to call this API
        """
        pass
import NXOpen
class SpecifyPoint(UIBlock): 
    """ Represents a Specify Point block"""
    @property
    def AutomaticProgression(self) -> bool:
        """
        Getter for property: (bool) AutomaticProgression
         Returns the AutomaticProgression  
            
         
        """
        pass
    @AutomaticProgression.setter
    def AutomaticProgression(self, automaticProgression: bool):
        """
        Setter for property: (bool) AutomaticProgression
         Returns the AutomaticProgression  
            
         
        """
        pass
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @property
    def CreateInterpartLink(self) -> bool:
        """
        Getter for property: (bool) CreateInterpartLink
         Returns the CreateInterpartLink  
            
         
        """
        pass
    @CreateInterpartLink.setter
    def CreateInterpartLink(self, createLink: bool):
        """
        Setter for property: (bool) CreateInterpartLink
         Returns the CreateInterpartLink  
            
         
        """
        pass
    @property
    def EnableFacetSelection(self) -> bool:
        """
        Getter for property: (bool) EnableFacetSelection
         Returns the EnableFacetSelection  
            
         
        """
        pass
    @EnableFacetSelection.setter
    def EnableFacetSelection(self, enableSelection: bool):
        """
        Setter for property: (bool) EnableFacetSelection
         Returns the EnableFacetSelection  
            
         
        """
        pass
    @property
    def InterpartSelectionAsString(self) -> str:
        """
        Getter for property: (str) InterpartSelectionAsString
         Returns the InterpartSelection as string  
            
         
        """
        pass
    @InterpartSelectionAsString.setter
    def InterpartSelectionAsString(self, enumString: str):
        """
        Setter for property: (str) InterpartSelectionAsString
         Returns the InterpartSelection as string  
            
         
        """
        pass
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
         Returns the LabelString  
            
         
        """
        pass
    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
         Returns the LabelString  
            
         
        """
        pass
    @property
    def Point(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) Point
         Returns the Point  
            
         
        """
        pass
    @Point.setter
    def Point(self, point: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) Point
         Returns the Point  
            
         
        """
        pass
    @property
    def SelectionView(self) -> NXOpen.View:
        """
        Getter for property: ( NXOpen.View) SelectionView
         Returns the SelectionView  
            
         
        """
        pass
    @property
    def ShowShortcuts(self) -> bool:
        """
        Getter for property: (bool) ShowShortcuts
         Returns the ShowShortcuts  
            
         
        """
        pass
    @ShowShortcuts.setter
    def ShowShortcuts(self, show: bool):
        """
        Setter for property: (bool) ShowShortcuts
         Returns the ShowShortcuts  
            
         
        """
        pass
    @property
    def SnapPointTypesEnabled(self) -> int:
        """
        Getter for property: (int) SnapPointTypesEnabled
         Returns the SnapPointTypesEnabled  
            
         
        """
        pass
    @SnapPointTypesEnabled.setter
    def SnapPointTypesEnabled(self, snapTypes: int):
        """
        Setter for property: (int) SnapPointTypesEnabled
         Returns the SnapPointTypesEnabled  
            
         
        """
        pass
    @property
    def SnapPointTypesOnByDefault(self) -> int:
        """
        Getter for property: (int) SnapPointTypesOnByDefault
         Returns the SnapPointTypesOnByDefault  
            
         
        """
        pass
    @SnapPointTypesOnByDefault.setter
    def SnapPointTypesOnByDefault(self, snapTypesByDefault: int):
        """
        Setter for property: (int) SnapPointTypesOnByDefault
         Returns the SnapPointTypesOnByDefault  
            
         
        """
        pass
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
         Returns the StepStatus as string  
            
         
        """
        pass
    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
         Returns the StepStatus as string  
            
         
        """
        pass
    def GetBalloonTooltipLayoutMembers(self) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         Returns layout_strings (List[str]): Value to get from the property. .
        """
        pass
    def GetInterpartSelectionMembers(self) -> List[str]:
        """
         Gets the InterpartSelection members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def GetSelectedObjects(self) -> List[NXOpen.TaggedObject]:
        """
         Gets the SelectedObjects
         Returns objectVector ( NXOpen.TaggedObject Li): Value to get from the property.
        """
        pass
    def GetStepStatusMembers(self) -> List[str]:
        """
         Gets the StepStatus members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def SetSelectedObjects(self, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the SelectedObjects
        """
        pass
    def TestPointSpecified(self, point: NXOpen.Point3d) -> None:
        """
         Tests the point specified for this block. The block must be in focus to call this API
        """
        pass
    def TestSelection(self, objectVector: NXOpen.TaggedObject) -> None:
        """
         Tests the selection for this block. The block must be in focus to call this API
        """
        pass
import NXOpen
class SpecifyVector(UIBlock): 
    """ Represents Specify Vector block"""
    @property
    def AutomaticProgression(self) -> bool:
        """
        Getter for property: (bool) AutomaticProgression
         Returns the AutomaticProgression  
            
         
        """
        pass
    @AutomaticProgression.setter
    def AutomaticProgression(self, automaticProgression: bool):
        """
        Setter for property: (bool) AutomaticProgression
         Returns the AutomaticProgression  
            
         
        """
        pass
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @property
    def CreateInterpartLink(self) -> bool:
        """
        Getter for property: (bool) CreateInterpartLink
         Returns the CreateInterpartLink  
            
         
        """
        pass
    @CreateInterpartLink.setter
    def CreateInterpartLink(self, createLink: bool):
        """
        Setter for property: (bool) CreateInterpartLink
         Returns the CreateInterpartLink  
            
         
        """
        pass
    @property
    def DoubleSide(self) -> bool:
        """
        Getter for property: (bool) DoubleSide
         Returns the DoubleSide  
            
         
        """
        pass
    @DoubleSide.setter
    def DoubleSide(self, doubleSide: bool):
        """
        Setter for property: (bool) DoubleSide
         Returns the DoubleSide  
            
         
        """
        pass
    @property
    def EnableFacetSelection(self) -> bool:
        """
        Getter for property: (bool) EnableFacetSelection
         Returns the EnableFacetSelection  
            
         
        """
        pass
    @EnableFacetSelection.setter
    def EnableFacetSelection(self, enableSelection: bool):
        """
        Setter for property: (bool) EnableFacetSelection
         Returns the EnableFacetSelection  
            
         
        """
        pass
    @property
    def EnableReverseDirection(self) -> bool:
        """
        Getter for property: (bool) EnableReverseDirection
         Returns the EnableReverseDirection  
            
         
        """
        pass
    @EnableReverseDirection.setter
    def EnableReverseDirection(self, enableReverse: bool):
        """
        Setter for property: (bool) EnableReverseDirection
         Returns the EnableReverseDirection  
            
         
        """
        pass
    @property
    def InterpartSelectionAsString(self) -> str:
        """
        Getter for property: (str) InterpartSelectionAsString
         Returns the InterpartSelection as string  
            
         
        """
        pass
    @InterpartSelectionAsString.setter
    def InterpartSelectionAsString(self, enumString: str):
        """
        Setter for property: (str) InterpartSelectionAsString
         Returns the InterpartSelection as string  
            
         
        """
        pass
    @property
    def Is2DMode(self) -> bool:
        """
        Getter for property: (bool) Is2DMode
         Returns the Is2DMode.  
           If true, vector is created in 2D space.  
         
        """
        pass
    @Is2DMode.setter
    def Is2DMode(self, is2DMode: bool):
        """
        Setter for property: (bool) Is2DMode
         Returns the Is2DMode.  
           If true, vector is created in 2D space.  
         
        """
        pass
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
         Returns the LabelString  
            
         
        """
        pass
    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
         Returns the LabelString  
            
         
        """
        pass
    @property
    def Point(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) Point
         Returns the Point  
            
         
        """
        pass
    @Point.setter
    def Point(self, point: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) Point
         Returns the Point  
            
         
        """
        pass
    @property
    def ShowShortcuts(self) -> bool:
        """
        Getter for property: (bool) ShowShortcuts
         Returns the ShowShortcuts  
            
         
        """
        pass
    @ShowShortcuts.setter
    def ShowShortcuts(self, show: bool):
        """
        Setter for property: (bool) ShowShortcuts
         Returns the ShowShortcuts  
            
         
        """
        pass
    @property
    def SnapPointTypesOnByDefault(self) -> int:
        """
        Getter for property: (int) SnapPointTypesOnByDefault
         Returns the SnapPointTypesOnByDefault  
            
         
        """
        pass
    @SnapPointTypesOnByDefault.setter
    def SnapPointTypesOnByDefault(self, snapTypesByDefault: int):
        """
        Setter for property: (int) SnapPointTypesOnByDefault
         Returns the SnapPointTypesOnByDefault  
            
         
        """
        pass
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
         Returns the StepStatus as string  
            
         
        """
        pass
    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
         Returns the StepStatus as string  
            
         
        """
        pass
    @property
    def Vector(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) Vector
         Returns the Vector  
            
         
        """
        pass
    @Vector.setter
    def Vector(self, vector: NXOpen.Vector3d):
        """
        Setter for property: ( NXOpen.Vector3d) Vector
         Returns the Vector  
            
         
        """
        pass
    def GetBalloonTooltipLayoutMembers(self) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         Returns layout_strings (List[str]): Value to get from the property. .
        """
        pass
    def GetInterpartSelectionMembers(self) -> List[str]:
        """
         Gets the InterpartSelection members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def GetSelectedObjects(self) -> List[NXOpen.TaggedObject]:
        """
         Gets the SelectedObjects
         Returns objectVector ( NXOpen.TaggedObject Li): Value to get from the property.
        """
        pass
    def GetStepStatusMembers(self) -> List[str]:
        """
         Gets the StepStatus
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def SetSelectedObjects(self, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the SelectedObjects
        """
        pass
    def TestPointSpecified(self, point: NXOpen.Point3d) -> None:
        """
         Tests the point specified for this block. The block must be in focus to call this API
        """
        pass
    def TestSelection(self, objectVector: NXOpen.TaggedObject) -> None:
        """
         Tests the selection for this block. The block must be in focus to call this API
        """
        pass
    def TestVectorSpecified(self, vector: NXOpen.Vector3d) -> None:
        """
         Tests the vector specified for this block. The block must be in focus to call this API
        """
        pass
class StringBlock(UIBlock): 
    """ Represents a String block"""
    @property
    def AllowInternationalTextInput(self) -> bool:
        """
        Getter for property: (bool) AllowInternationalTextInput
         Returns the AllowInternationalTextInput  
            
         
        """
        pass
    @AllowInternationalTextInput.setter
    def AllowInternationalTextInput(self, allow: bool):
        """
        Setter for property: (bool) AllowInternationalTextInput
         Returns the AllowInternationalTextInput  
            
         
        """
        pass
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @property
    def Bitmap(self) -> str:
        """
        Getter for property: (str) Bitmap
         Returns the Bitmap  
            
         
        """
        pass
    @Bitmap.setter
    def Bitmap(self, bitmap_string: str):
        """
        Setter for property: (str) Bitmap
         Returns the Bitmap  
            
         
        """
        pass
    @property
    def IsPassword(self) -> bool:
        """
        Getter for property: (bool) IsPassword
         Returns the IsPassword.  
           If true, characters will not be readable. They will be displayed as .  
         
        """
        pass
    @IsPassword.setter
    def IsPassword(self, passwrod: bool):
        """
        Setter for property: (bool) IsPassword
         Returns the IsPassword.  
           If true, characters will not be readable. They will be displayed as .  
         
        """
        pass
    @property
    def Localize(self) -> bool:
        """
        Getter for property: (bool) Localize
         Returns the Localize  
            
         
        """
        pass
    @Localize.setter
    def Localize(self, localize: bool):
        """
        Setter for property: (bool) Localize
         Returns the Localize  
            
         
        """
        pass
    @property
    def MaxTextLength(self) -> int:
        """
        Getter for property: (int) MaxTextLength
         Returns the MaxTextLength  
            
         
        """
        pass
    @MaxTextLength.setter
    def MaxTextLength(self, text_length: int):
        """
        Setter for property: (int) MaxTextLength
         Returns the MaxTextLength  
            
         
        """
        pass
    @property
    def PresentationStyleAsString(self) -> str:
        """
        Getter for property: (str) PresentationStyleAsString
         Returns the PresentationStyle as string  
            
         
        """
        pass
    @PresentationStyleAsString.setter
    def PresentationStyleAsString(self, enumString: str):
        """
        Setter for property: (str) PresentationStyleAsString
         Returns the PresentationStyle as string  
            
         
        """
        pass
    @property
    def ReadOnlyString(self) -> bool:
        """
        Getter for property: (bool) ReadOnlyString
         Returns the ReadOnlyString  
            
         
        """
        pass
    @ReadOnlyString.setter
    def ReadOnlyString(self, readonly: bool):
        """
        Setter for property: (bool) ReadOnlyString
         Returns the ReadOnlyString  
            
         
        """
        pass
    @property
    def RetainValue(self) -> bool:
        """
        Getter for property: (bool) RetainValue
         Returns the RetainValue  
            
         
        """
        pass
    @RetainValue.setter
    def RetainValue(self, retain: bool):
        """
        Setter for property: (bool) RetainValue
         Returns the RetainValue  
            
         
        """
        pass
    @property
    def Tooltip(self) -> str:
        """
        Getter for property: (str) Tooltip
         Returns the Tooltip  
            
         
        """
        pass
    @Tooltip.setter
    def Tooltip(self, tooltip_string: str):
        """
        Setter for property: (str) Tooltip
         Returns the Tooltip  
            
         
        """
        pass
    @property
    def UncommittedValue(self) -> str:
        """
        Getter for property: (str) UncommittedValue
         Returns the Uncommitted Value of string block.  
            
         
        """
        pass
    @UncommittedValue.setter
    def UncommittedValue(self, value_string: str):
        """
        Setter for property: (str) UncommittedValue
         Returns the Uncommitted Value of string block.  
            
         
        """
        pass
    @property
    def Value(self) -> str:
        """
        Getter for property: (str) Value
         Returns the Value  
            
         
        """
        pass
    @Value.setter
    def Value(self, value_string: str):
        """
        Setter for property: (str) Value
         Returns the Value  
            
         
        """
        pass
    @property
    def WideValue(self) -> str:
        """
        Getter for property: (str) WideValue
         Returns the WideValue.  
           Specifies the International text. This property accepts international characters supported by NX.  
         
        """
        pass
    @WideValue.setter
    def WideValue(self, wide_value_string: str):
        """
        Setter for property: (str) WideValue
         Returns the WideValue.  
           Specifies the International text. This property accepts international characters supported by NX.  
         
        """
        pass
    @property
    def WidthAsString(self) -> str:
        """
        Getter for property: (str) WidthAsString
         Returns the Width as string  
            
         
        """
        pass
    @WidthAsString.setter
    def WidthAsString(self, enumString: str):
        """
        Setter for property: (str) WidthAsString
         Returns the Width as string  
            
         
        """
        pass
    def GetBalloonTooltipImages(self) -> List[str]:
        """
         Gets the BalloonTooltipImages
         Returns image_strings (List[str]): .
        """
        pass
    def GetBalloonTooltipLayoutMembers(self) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         Returns layout_strings (List[str]): Values to get from the property.
        """
        pass
    def GetBalloonTooltipTexts(self) -> List[str]:
        """
         Gets the BalloonTooltipTexts
         Returns tooltip_text_array (List[str]): Values to get from the property. .
        """
        pass
    def GetListItems(self) -> List[str]:
        """
         Gets the ListItems
         Returns item_strings (List[str]): Values to get from the property.
        """
        pass
    def GetPresentationStyleMembers(self) -> List[str]:
        """
         Gets the PresentationStyle members 
         Returns member_strings (List[str]): Values to get from the property. .
        """
        pass
    def GetWidthMembers(self) -> List[str]:
        """
         Gets the Width members 
         Returns member_strings (List[str]): Values to get from the property. .
        """
        pass
    KeystrokeCallback = Callable[[StringBlock, str], None]
    KeystrokeCallbackHandler = Callable[[StringBlock, str], None]
    def SetBalloonTooltipImages(self, image_strings: List[str]) -> None:
        """
         Sets the BalloonTooltipImages
        """
        pass
    def SetBalloonTooltipTexts(self, tooltip_text_array: List[str]) -> None:
        """
         Sets the BalloonTooltipTexts
        """
        pass
    def SetKeystrokeCallback(self, cb: StringBlock.KeystrokeCallback) -> None:
        """
         Sets the keystroke callback for Block Styler String Block. 
        """
        pass
    def SetKeystrokeCallbackHandler(self, cb: StringBlock.KeystrokeCallbackHandler) -> None:
        """
         Sets the keystroke callback for Block Styler String Block. 
        """
        pass
    def SetListItems(self, item_strings: List[str]) -> None:
        """
         Sets the ListItems
        """
        pass
    def TestKeystrokeObserver(self) -> None:
        """
        Tests key stroke observer of this block. It also sets the passed value to the block.
                To mock the event, set necessary value before calling this method 
        """
        pass
    def TestValueChanged(self, value_string: str) -> None:
        """
        Tests value changed event workflow mapped to this string block.
        """
        pass
    def TestWideValueChanged(self, value_string: str) -> None:
        """
        Tests value changed event workflow mapped to this StringBlock block.
        """
        pass
import NXOpen
class SuperPoint(UIBlock): 
    """ Represents a Super Point block"""
    @property
    def AllowConvergentObject(self) -> bool:
        """
        Getter for property: (bool) AllowConvergentObject
         Returns the AllowConvergentObject  
            
         
        """
        pass
    @AllowConvergentObject.setter
    def AllowConvergentObject(self, allowConvergentObject: bool):
        """
        Setter for property: (bool) AllowConvergentObject
         Returns the AllowConvergentObject  
            
         
        """
        pass
    @property
    def AllowConvergentObjectWithMixedGeometries(self) -> bool:
        """
        Getter for property: (bool) AllowConvergentObjectWithMixedGeometries
         Returns the AllowConvergentObjectWithMixedGeometries  
            
         
        """
        pass
    @AllowConvergentObjectWithMixedGeometries.setter
    def AllowConvergentObjectWithMixedGeometries(self, allowConvergentObjectWithMixedGeometries: bool):
        """
        Setter for property: (bool) AllowConvergentObjectWithMixedGeometries
         Returns the AllowConvergentObjectWithMixedGeometries  
            
         
        """
        pass
    @property
    def AutomaticProgression(self) -> bool:
        """
        Getter for property: (bool) AutomaticProgression
         Returns the AutomaticProgression  
            
         
        """
        pass
    @AutomaticProgression.setter
    def AutomaticProgression(self, automaticProgression: bool):
        """
        Setter for property: (bool) AutomaticProgression
         Returns the AutomaticProgression  
            
         
        """
        pass
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @property
    def Bitmap(self) -> str:
        """
        Getter for property: (str) Bitmap
         Returns the Bitmap  
            
         
        """
        pass
    @Bitmap.setter
    def Bitmap(self, bitmap_string: str):
        """
        Setter for property: (str) Bitmap
         Returns the Bitmap  
            
         
        """
        pass
    @property
    def BlendVirtualCurveOverlay(self) -> bool:
        """
        Getter for property: (bool) BlendVirtualCurveOverlay
         Returns the BlendVirtualCurveOverlay.  
           If true, virtual curve is displayed during preselection.  
         
        """
        pass
    @BlendVirtualCurveOverlay.setter
    def BlendVirtualCurveOverlay(self, blendCurve: bool):
        """
        Setter for property: (bool) BlendVirtualCurveOverlay
         Returns the BlendVirtualCurveOverlay.  
           If true, virtual curve is displayed during preselection.  
         
        """
        pass
    @property
    def CreateInterpartLink(self) -> bool:
        """
        Getter for property: (bool) CreateInterpartLink
         Returns the CreateInterpartLink  
            
         
        """
        pass
    @CreateInterpartLink.setter
    def CreateInterpartLink(self, createLink: bool):
        """
        Setter for property: (bool) CreateInterpartLink
         Returns the CreateInterpartLink  
            
         
        """
        pass
    @property
    def Cue(self) -> str:
        """
        Getter for property: (str) Cue
         Returns the Cue  
            
         
        """
        pass
    @Cue.setter
    def Cue(self, cue: str):
        """
        Setter for property: (str) Cue
         Returns the Cue  
            
         
        """
        pass
    @property
    def CurveRules(self) -> int:
        """
        Getter for property: (int) CurveRules
         Returns the CurveRules  
            
         
        """
        pass
    @CurveRules.setter
    def CurveRules(self, curveRules: int):
        """
        Setter for property: (int) CurveRules
         Returns the CurveRules  
            
         
        """
        pass
    @property
    def DefaultCurveRulesAsString(self) -> str:
        """
        Getter for property: (str) DefaultCurveRulesAsString
         Returns the DefaultCurveRules as string  
            
         
        """
        pass
    @DefaultCurveRulesAsString.setter
    def DefaultCurveRulesAsString(self, enumString: str):
        """
        Setter for property: (str) DefaultCurveRulesAsString
         Returns the DefaultCurveRules as string  
            
         
        """
        pass
    @property
    def EntityType(self) -> int:
        """
        Getter for property: (int) EntityType
         Returns the EntityType  
            
         
        """
        pass
    @EntityType.setter
    def EntityType(self, entityType: int):
        """
        Setter for property: (int) EntityType
         Returns the EntityType  
            
         
        """
        pass
    @property
    def InterpartSelectionAsString(self) -> str:
        """
        Getter for property: (str) InterpartSelectionAsString
         Returns the InterpartSelection as string  
            
         
        """
        pass
    @InterpartSelectionAsString.setter
    def InterpartSelectionAsString(self, enumString: str):
        """
        Setter for property: (str) InterpartSelectionAsString
         Returns the InterpartSelection as string  
            
         
        """
        pass
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
         Returns the LabelString  
            
         
        """
        pass
    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
         Returns the LabelString  
            
         
        """
        pass
    @property
    def PointOverlay(self) -> bool:
        """
        Getter for property: (bool) PointOverlay
         Returns the PointOverlay  
            
         
        """
        pass
    @PointOverlay.setter
    def PointOverlay(self, overlay: bool):
        """
        Setter for property: (bool) PointOverlay
         Returns the PointOverlay  
            
         
        """
        pass
    @property
    def ShowFlowDirectionAndOriginCurve(self) -> bool:
        """
        Getter for property: (bool) ShowFlowDirectionAndOriginCurve
         Returns the ShowFlowDirectionAndOriginCurve  
            
         
        """
        pass
    @ShowFlowDirectionAndOriginCurve.setter
    def ShowFlowDirectionAndOriginCurve(self, show: bool):
        """
        Setter for property: (bool) ShowFlowDirectionAndOriginCurve
         Returns the ShowFlowDirectionAndOriginCurve  
            
         
        """
        pass
    @property
    def SketchOnPath(self) -> bool:
        """
        Getter for property: (bool) SketchOnPath
         Returns the SketchOnPath  
            
         
        """
        pass
    @SketchOnPath.setter
    def SketchOnPath(self, sketchOnPath: bool):
        """
        Setter for property: (bool) SketchOnPath
         Returns the SketchOnPath  
            
         
        """
        pass
    @property
    def SnapPointTypesEnabled(self) -> int:
        """
        Getter for property: (int) SnapPointTypesEnabled
         Returns the SnapPointTypesEnabled  
            
         
        """
        pass
    @SnapPointTypesEnabled.setter
    def SnapPointTypesEnabled(self, snapPointType: int):
        """
        Setter for property: (int) SnapPointTypesEnabled
         Returns the SnapPointTypesEnabled  
            
         
        """
        pass
    @property
    def SnapPointTypesOnByDefault(self) -> int:
        """
        Getter for property: (int) SnapPointTypesOnByDefault
         Returns the SnapPointTypesOnByDefault  
            
         
        """
        pass
    @SnapPointTypesOnByDefault.setter
    def SnapPointTypesOnByDefault(self, defaultSnapPointType: int):
        """
        Setter for property: (int) SnapPointTypesOnByDefault
         Returns the SnapPointTypesOnByDefault  
            
         
        """
        pass
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
         Returns the StepStatus as string  
            
         
        """
        pass
    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
         Returns the StepStatus as string  
            
         
        """
        pass
    @property
    def ToolTip(self) -> str:
        """
        Getter for property: (str) ToolTip
         Returns the ToolTip  
            
         
        """
        pass
    @ToolTip.setter
    def ToolTip(self, toolTip: str):
        """
        Setter for property: (str) ToolTip
         Returns the ToolTip  
            
         
        """
        pass
    def GetBalloonTooltipLayoutMembers(self) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         Returns layout_strings (List[str]): Value to get from the property. .
        """
        pass
    def GetDefaultCurveRulesMembers(self) -> List[str]:
        """
         Gets the DefaultCurveRules members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def GetInterpartSelectionMembers(self) -> List[str]:
        """
         Gets the InterpartSelection members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def GetSelectedObjects(self) -> List[NXOpen.TaggedObject]:
        """
         Gets the SelectedObjects
         Returns objectVector ( NXOpen.TaggedObject Li): Value to get from the property.
        """
        pass
    def GetStepStatusMembers(self) -> List[str]:
        """
         Gets the StepStatus members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def SetSelectedObjects(self, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the SelectedObjects
        """
        pass
    def TestSelection(self, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Tests the selection for this block. The block must be in focus to call this API
        """
        pass
import NXOpen
class SuperSection(UIBlock): 
    """ Represents a Super Section block"""
    @property
    def AllowConvergentObject(self) -> bool:
        """
        Getter for property: (bool) AllowConvergentObject
         Returns the AllowConvergentObject  
            
         
        """
        pass
    @AllowConvergentObject.setter
    def AllowConvergentObject(self, allowConvergentObject: bool):
        """
        Setter for property: (bool) AllowConvergentObject
         Returns the AllowConvergentObject  
            
         
        """
        pass
    @property
    def AllowConvergentObjectWithMixedGeometries(self) -> bool:
        """
        Getter for property: (bool) AllowConvergentObjectWithMixedGeometries
         Returns the AllowConvergentObjectWithMixedGeometries  
            
         
        """
        pass
    @AllowConvergentObjectWithMixedGeometries.setter
    def AllowConvergentObjectWithMixedGeometries(self, allowConvergentObjectWithMixedGeometries: bool):
        """
        Setter for property: (bool) AllowConvergentObjectWithMixedGeometries
         Returns the AllowConvergentObjectWithMixedGeometries  
            
         
        """
        pass
    @property
    def AllowInferredCurveSelection(self) -> bool:
        """
        Getter for property: (bool) AllowInferredCurveSelection
         Returns the AllowInferredCurveSelection  
            
         
        """
        pass
    @AllowInferredCurveSelection.setter
    def AllowInferredCurveSelection(self, allow: bool):
        """
        Setter for property: (bool) AllowInferredCurveSelection
         Returns the AllowInferredCurveSelection  
            
         
        """
        pass
    @property
    def AllowStopAtIntersectionFollowFillet(self) -> bool:
        """
        Getter for property: (bool) AllowStopAtIntersectionFollowFillet
         Returns the AllowStopAtIntersectionFollowFillet  
            
         
        """
        pass
    @AllowStopAtIntersectionFollowFillet.setter
    def AllowStopAtIntersectionFollowFillet(self, allow: bool):
        """
        Setter for property: (bool) AllowStopAtIntersectionFollowFillet
         Returns the AllowStopAtIntersectionFollowFillet  
            
         
        """
        pass
    @property
    def AngularTolerance(self) -> float:
        """
        Getter for property: (float) AngularTolerance
         Returns the AngularTolerance  
            
         
        """
        pass
    @AngularTolerance.setter
    def AngularTolerance(self, tolerance: float):
        """
        Setter for property: (float) AngularTolerance
         Returns the AngularTolerance  
            
         
        """
        pass
    @property
    def AutomaticProgression(self) -> bool:
        """
        Getter for property: (bool) AutomaticProgression
         Returns the AutomaticProgression  
            
         
        """
        pass
    @AutomaticProgression.setter
    def AutomaticProgression(self, automaticProgression: bool):
        """
        Setter for property: (bool) AutomaticProgression
         Returns the AutomaticProgression  
            
         
        """
        pass
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
         Returns the BalloonTooltipImage  
            
         
        """
        pass
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
         Returns the BalloonTooltipText  
            
         
        """
        pass
    @property
    def Bitmap(self) -> str:
        """
        Getter for property: (str) Bitmap
         Returns the Bitmap  
            
         
        """
        pass
    @Bitmap.setter
    def Bitmap(self, bitmap_string: str):
        """
        Setter for property: (str) Bitmap
         Returns the Bitmap  
            
         
        """
        pass
    @property
    def BlendVirtualCurveOverlay(self) -> bool:
        """
        Getter for property: (bool) BlendVirtualCurveOverlay
         Returns the BlendVirtualCurveOverlay.  
           If true, virtual curve is displayed during preselection.  
         
        """
        pass
    @BlendVirtualCurveOverlay.setter
    def BlendVirtualCurveOverlay(self, blendCurve: bool):
        """
        Setter for property: (bool) BlendVirtualCurveOverlay
         Returns the BlendVirtualCurveOverlay.  
           If true, virtual curve is displayed during preselection.  
         
        """
        pass
    @property
    def ChainWithinFeature(self) -> bool:
        """
        Getter for property: (bool) ChainWithinFeature
         Returns the ChainWithinFeature  
            
         
        """
        pass
    @ChainWithinFeature.setter
    def ChainWithinFeature(self, chainWithinFeature: bool):
        """
        Setter for property: (bool) ChainWithinFeature
         Returns the ChainWithinFeature  
            
         
        """
        pass
    @property
    def CreateInterpartLink(self) -> bool:
        """
        Getter for property: (bool) CreateInterpartLink
         Returns the CreateInterpartLink  
            
         
        """
        pass
    @CreateInterpartLink.setter
    def CreateInterpartLink(self, createLink: bool):
        """
        Setter for property: (bool) CreateInterpartLink
         Returns the CreateInterpartLink  
            
         
        """
        pass
    @property
    def Cue(self) -> str:
        """
        Getter for property: (str) Cue
         Returns the Cue  
            
         
        """
        pass
    @Cue.setter
    def Cue(self, cue: str):
        """
        Setter for property: (str) Cue
         Returns the Cue  
            
         
        """
        pass
    @property
    def CurveRules(self) -> int:
        """
        Getter for property: (int) CurveRules
         Returns the CurveRules  
            
         
        """
        pass
    @CurveRules.setter
    def CurveRules(self, curveRules: int):
        """
        Setter for property: (int) CurveRules
         Returns the CurveRules  
            
         
        """
        pass
    @property
    def DefaultCurveRulesAsString(self) -> str:
        """
        Getter for property: (str) DefaultCurveRulesAsString
         Returns the DefaultCurveRules as string  
            
         
        """
        pass
    @DefaultCurveRulesAsString.setter
    def DefaultCurveRulesAsString(self, enumString: str):
        """
        Setter for property: (str) DefaultCurveRulesAsString
         Returns the DefaultCurveRules as string  
            
         
        """
        pass
    @property
    def EntityType(self) -> int:
        """
        Getter for property: (int) EntityType
         Returns the EntityType  
            
         
        """
        pass
    @EntityType.setter
    def EntityType(self, entityType: int):
        """
        Setter for property: (int) EntityType
         Returns the EntityType  
            
         
        """
        pass
    @property
    def FollowFillet(self) -> bool:
        """
        Getter for property: (bool) FollowFillet
         Returns the FollowFillet  
            
         
        """
        pass
    @FollowFillet.setter
    def FollowFillet(self, followFillet: bool):
        """
        Setter for property: (bool) FollowFillet
         Returns the FollowFillet  
            
         
        """
        pass
    @property
    def InferredCurveSelection(self) -> bool:
        """
        Getter for property: (bool) InferredCurveSelection
         Returns the InferredCurveSelection  
            
         
        """
        pass
    @InferredCurveSelection.setter
    def InferredCurveSelection(self, selectInferredCurve: bool):
        """
        Setter for property: (bool) InferredCurveSelection
         Returns the InferredCurveSelection  
            
         
        """
        pass
    @property
    def InterpartSelectionAsString(self) -> str:
        """
        Getter for property: (str) InterpartSelectionAsString
         Returns the InterpartSelection as string  
            
         
        """
        pass
    @InterpartSelectionAsString.setter
    def InterpartSelectionAsString(self, enumString: str):
        """
        Setter for property: (str) InterpartSelectionAsString
         Returns the InterpartSelection as string  
            
         
        """
        pass
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
         Returns the LabelString  
            
         
        """
        pass
    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
         Returns the LabelString  
            
         
        """
        pass
    @property
    def PointOverlay(self) -> bool:
        """
        Getter for property: (bool) PointOverlay
         Returns the PointOverlay  
            
         
        """
        pass
    @PointOverlay.setter
    def PointOverlay(self, overlay: bool):
        """
        Setter for property: (bool) PointOverlay
         Returns the PointOverlay  
            
         
        """
        pass
    @property
    def ShowFlowDirectionAndOriginCurve(self) -> bool:
        """
        Getter for property: (bool) ShowFlowDirectionAndOriginCurve
         Returns the ShowFlowDirectionAndOriginCurve  
            
         
        """
        pass
    @ShowFlowDirectionAndOriginCurve.setter
    def ShowFlowDirectionAndOriginCurve(self, show: bool):
        """
        Setter for property: (bool) ShowFlowDirectionAndOriginCurve
         Returns the ShowFlowDirectionAndOriginCurve  
            
         
        """
        pass
    @property
    def SketchOnPath(self) -> bool:
        """
        Getter for property: (bool) SketchOnPath
         Returns the SketchOnPath  
            
         
        """
        pass
    @SketchOnPath.setter
    def SketchOnPath(self, sketchOnPath: bool):
        """
        Setter for property: (bool) SketchOnPath
         Returns the SketchOnPath  
            
         
        """
        pass
    @property
    def SmartUpdateOptionAsString(self) -> str:
        """
        Getter for property: (str) SmartUpdateOptionAsString
         Returns the update option for points created by the point overlay.  
          
                  
                Acceptable values are:
                
                 Within Modeling The smart object updates within Modeling in time stamp order. For example, if the smart object is referenced by Feature(i), the smart object will update after Feature (i-1) and right before Feature(i).
                 After Modeling The smart object updates after Modeling. Use for Drafting dimensions and other objects outside Modeling.
                 After Parent Body The smart object will always update after the last feature on the parent body.
                 Mixed The smart object will update after the last feature on the parent body when the parent body is in a different part; updates within Modeling in time-stamp order for parents in the same part.
                
                  
                  
         
        """
        pass
    @SmartUpdateOptionAsString.setter
    def SmartUpdateOptionAsString(self, enumString: str):
        """
        Setter for property: (str) SmartUpdateOptionAsString
         Returns the update option for points created by the point overlay.  
          
                  
                Acceptable values are:
                
                 Within Modeling The smart object updates within Modeling in time stamp order. For example, if the smart object is referenced by Feature(i), the smart object will update after Feature (i-1) and right before Feature(i).
                 After Modeling The smart object updates after Modeling. Use for Drafting dimensions and other objects outside Modeling.
                 After Parent Body The smart object will always update after the last feature on the parent body.
                 Mixed The smart object will update after the last feature on the parent body when the parent body is in a different part; updates within Modeling in time-stamp order for parents in the same part.
                
                  
                  
         
        """
        pass
    @property
    def SnapPointTypesEnabled(self) -> int:
        """
        Getter for property: (int) SnapPointTypesEnabled
         Returns the SnapPointTypesEnabled  
            
         
        """
        pass
    @SnapPointTypesEnabled.setter
    def SnapPointTypesEnabled(self, snapPointType: int):
        """
        Setter for property: (int) SnapPointTypesEnabled
         Returns the SnapPointTypesEnabled  
            
         
        """
        pass
    @property
    def SnapPointTypesOnByDefault(self) -> int:
        """
        Getter for property: (int) SnapPointTypesOnByDefault
         Returns the SnapPointTypesOnByDefault  
            
         
        """
        pass
    @SnapPointTypesOnByDefault.setter
    def SnapPointTypesOnByDefault(self, defaultSnapPointType: int):
        """
        Setter for property: (int) SnapPointTypesOnByDefault
         Returns the SnapPointTypesOnByDefault  
            
         
        """
        pass
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
         Returns the StepStatus as string  
            
         
        """
        pass
    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
         Returns the StepStatus as string  
            
         
        """
        pass
    @property
    def StopAtIntersection(self) -> bool:
        """
        Getter for property: (bool) StopAtIntersection
         Returns the StopAtIntersection  
            
         
        """
        pass
    @StopAtIntersection.setter
    def StopAtIntersection(self, stop: bool):
        """
        Setter for property: (bool) StopAtIntersection
         Returns the StopAtIntersection  
            
         
        """
        pass
    @property
    def ToolTip(self) -> str:
        """
        Getter for property: (str) ToolTip
         Returns the ToolTip  
            
         
        """
        pass
    @ToolTip.setter
    def ToolTip(self, toolTip: str):
        """
        Setter for property: (str) ToolTip
         Returns the ToolTip  
            
         
        """
        pass
    def GetBalloonTooltipLayoutMembers(self) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         Returns layout_strings (List[str]): Value to get from the property. .
        """
        pass
    def GetDefaultCurveRulesMembers(self) -> List[str]:
        """
         Gets the DefaultCurveRules members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def GetInterpartSelectionMembers(self) -> List[str]:
        """
         Gets the InterpartSelection members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def GetSelectedObjects(self) -> List[NXOpen.TaggedObject]:
        """
         Gets the SelectedObjects
         Returns objectVector ( NXOpen.TaggedObject Li): Value to get from the property.
        """
        pass
    def GetStepStatusMembers(self) -> List[str]:
        """
         Gets the StepStatus members
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def SetSelectedObjects(self, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the SelectedObjects
        """
        pass
    def TestSelection(self, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Tests the selection for this block. The block must be in focus to call this API
        """
        pass
class TabControl(UIBlock): 
    """ Represents a Tab Control layout"""
    @property
    def ActivePage(self) -> int:
        """
        Getter for property: (int) ActivePage
         Returns the ActivePage  
            
         
        """
        pass
    @ActivePage.setter
    def ActivePage(self, pageIndex: int):
        """
        Setter for property: (int) ActivePage
         Returns the ActivePage  
            
         
        """
        pass
    @property
    def HighQualityBitmap(self) -> bool:
        """
        Getter for property: (bool) HighQualityBitmap
         Returns the HighQualityBitmap  
            
         
        """
        pass
    @HighQualityBitmap.setter
    def HighQualityBitmap(self, highQuality: bool):
        """
        Setter for property: (bool) HighQualityBitmap
         Returns the HighQualityBitmap  
            
         
        """
        pass
    @property
    def Localize(self) -> bool:
        """
        Getter for property: (bool) Localize
         Returns the Localize  
            
         
        """
        pass
    @Localize.setter
    def Localize(self, localize: bool):
        """
        Setter for property: (bool) Localize
         Returns the Localize  
            
         
        """
        pass
    @property
    def Members(self) -> PropertyList:
        """
        Getter for property: ( PropertyList NXOpen.B) Members
         Returns the Members  
            
         
        """
        pass
    @property
    def RetainValue(self) -> bool:
        """
        Getter for property: (bool) RetainValue
         Returns the RetainValue  
            
         
        """
        pass
    @RetainValue.setter
    def RetainValue(self, retain: bool):
        """
        Setter for property: (bool) RetainValue
         Returns the RetainValue  
            
         
        """
        pass
    @property
    def TabsPerRow(self) -> int:
        """
        Getter for property: (int) TabsPerRow
         Returns the TabsPerRow  
            
         
        """
        pass
    @TabsPerRow.setter
    def TabsPerRow(self, numTabs: int):
        """
        Setter for property: (int) TabsPerRow
         Returns the TabsPerRow  
            
         
        """
        pass
    def GetHiddenTabPages(self) -> List[int]:
        """
         Gets the HiddenTabPages. This method returns an integer array of the HiddenTabPages.
                If the number of Tab Pages defined is 5 for a Tab Control, they will be indexed 0 to 4. If the first
                and third Tab Pages are hidden, the result returned will be [ 0, -1, 2, -1, -1 ]. Any negative integer
                value will show the Tab Page, using -1 simply to demonstrate.
         Returns hiddenTabs (List[int]): .
        """
        pass
    def SetHiddenTabPages(self, hiddenTabs: List[int]) -> None:
        """
         Sets the HiddenTabPages entered. If the number of Tab Pages defined is 5 for a Tab Control,
                they will be indexed 0 to 4. Entering an array of [ 0, -1, 2, -1, -1 ] will result in the first and third
                Tab Pages being hidden. Any negative integer value will show the Tab Page, using -1 simply to demonstrate.
        """
        pass
    def TestActivePageChanged(self, pageIndex: int) -> None:
        """
        Tests active tab changed.
        """
        pass
class Table(UIBlock): 
    """ Represents a Table layout"""
    @property
    def HasColumnLabels(self) -> bool:
        """
        Getter for property: (bool) HasColumnLabels
         Returns the HasColumnLabels  
            
         
        """
        pass
    @HasColumnLabels.setter
    def HasColumnLabels(self, hasLables: bool):
        """
        Setter for property: (bool) HasColumnLabels
         Returns the HasColumnLabels  
            
         
        """
        pass
    @property
    def HighQualityBitmap(self) -> bool:
        """
        Getter for property: (bool) HighQualityBitmap
         Returns the HighQualityBitmap  
            
         
        """
        pass
    @HighQualityBitmap.setter
    def HighQualityBitmap(self, highQuality: bool):
        """
        Setter for property: (bool) HighQualityBitmap
         Returns the HighQualityBitmap  
            
         
        """
        pass
    @property
    def Localize(self) -> bool:
        """
        Getter for property: (bool) Localize
         Returns the Localize  
            
         
        """
        pass
    @Localize.setter
    def Localize(self, localize: bool):
        """
        Setter for property: (bool) Localize
         Returns the Localize  
            
         
        """
        pass
    @property
    def Members(self) -> PropertyList:
        """
        Getter for property: ( PropertyList NXOpen.B) Members
         Returns the Members  
            
         
        """
        pass
    @property
    def NumberOfColumns(self) -> int:
        """
        Getter for property: (int) NumberOfColumns
         Returns the NumberOfColumns  
            
         
        """
        pass
    @NumberOfColumns.setter
    def NumberOfColumns(self, num_column: int):
        """
        Setter for property: (int) NumberOfColumns
         Returns the NumberOfColumns  
            
         
        """
        pass
    @property
    def RetainValue(self) -> bool:
        """
        Getter for property: (bool) RetainValue
         Returns the RetainValue.  
          If true, the block's value will be saved in dialog memory upon OK, Apply or Close.  
         
        """
        pass
    @RetainValue.setter
    def RetainValue(self, retain: bool):
        """
        Setter for property: (bool) RetainValue
         Returns the RetainValue.  
          If true, the block's value will be saved in dialog memory upon OK, Apply or Close.  
         
        """
        pass
import NXOpen
class TestStepSequence(NXOpen.TransientObject): 
    """ Class for registering test steps in a sequential manner. Steps registered with this class will be executed sequentially one after another as they appear in sequence."""
    TestStepFunction = Callable[[UIBlock], None]
    TestStepValidationNotifier = Callable[[UIBlock], None]
    def AddStep(self, step_fn: TestStepSequence.TestStepFunction, step_val_fn: TestStepSequence.TestStepValidationNotifier, step_identifier: str) -> None:
        """
        Adds a test step to a step sequence. The registered steps will be executed sequentially as they are registered.
        """
        pass
    def AddStepWithoutValidation(self, step_fn: TestStepSequence.TestStepFunction, step_identifier: str) -> None:
        """
        Adds a test step to a step sequence without validation function. The registered steps will be executed sequentially as they are registered.
        """
        pass
    def Dispose(self) -> None:
        """
        Disposes the object.
        """
        pass
class TextColorFontWidth(UIBlock): 
    """ Represents a Line Width block"""
    @property
    def AvailableFontTypesAsString(self) -> str:
        """
        Getter for property: (str) AvailableFontTypesAsString
         Returns the available font types.  
            
         
        """
        pass
    @AvailableFontTypesAsString.setter
    def AvailableFontTypesAsString(self, availableFontTypes: str):
        """
        Setter for property: (str) AvailableFontTypesAsString
         Returns the available font types.  
            
         
        """
        pass
    @property
    def FontValue(self) -> str:
        """
        Getter for property: (str) FontValue
         Returns the font value  
            
         
        """
        pass
    @FontValue.setter
    def FontValue(self, fontValue: str):
        """
        Setter for property: (str) FontValue
         Returns the font value  
            
         
        """
        pass
    @property
    def LayoutAsString(self) -> str:
        """
        Getter for property: (str) LayoutAsString
         Returns the layout.  
            
         
        """
        pass
    @LayoutAsString.setter
    def LayoutAsString(self, layoutString: str):
        """
        Setter for property: (str) LayoutAsString
         Returns the layout.  
            
         
        """
        pass
    @property
    def StandardFontStyle(self) -> str:
        """
        Getter for property: (str) StandardFontStyle
         Returns the standard font style.  
            
         
        """
        pass
    @StandardFontStyle.setter
    def StandardFontStyle(self, fontStyle: str):
        """
        Setter for property: (str) StandardFontStyle
         Returns the standard font style.  
            
         
        """
        pass
    @property
    def WidthValueAsString(self) -> str:
        """
        Getter for property: (str) WidthValueAsString
         Returns the width value.  
            
         
        """
        pass
    @WidthValueAsString.setter
    def WidthValueAsString(self, widthValueString: str):
        """
        Setter for property: (str) WidthValueAsString
         Returns the width value.  
            
         
        """
        pass
    def GetColorValue(self) -> List[int]:
        """
         Gets text color values
         Returns colorValueVector (List[int]): color values to get from the property.
        """
        pass
    def IsNxFont(self) -> bool:
        """
         Returns the whether selected font is nx font or standard font.
         Returns isNxFont (bool): .
        """
        pass
    def SetColorValue(self, colorValueVector: List[int]) -> None:
        """
         Sets text color values
        """
        pass
    def TestColorValueChanged(self, colorValueVector: List[int]) -> None:
        """
        Tests color value changed event workflow mapped to this TextColorFontWidth block. Invokes the client notifiers to simulate UI like event.
        """
        pass
    def TestFontValueChanged(self, fontValue: str) -> None:
        """
        Tests font value changed event workflow mapped to this TextColorFontWidth block. Invokes the client notifiers to simulate UI like event.
        """
        pass
    def TestWidthValueChanged(self, widthValueString: str) -> None:
        """
        Tests width value changed event workflow mapped to this TextColorFontWidth block.
        """
        pass
class Toggle(UIBlock): 
    """ Represents a Toggle block"""
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
         Returns the BalloonTooltipLayout as string  
            
         
        """
        pass
    @property
    def BalloonTooltipOffImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipOffImage
         Returns the BalloonTooltipOffImage  
            
         
        """
        pass
    @BalloonTooltipOffImage.setter
    def BalloonTooltipOffImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipOffImage
         Returns the BalloonTooltipOffImage  
            
         
        """
        pass
    @property
    def BalloonTooltipOffText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipOffText
         Returns the BalloonTooltipOffText  
            
         
        """
        pass
    @BalloonTooltipOffText.setter
    def BalloonTooltipOffText(self, tooltip_string: str):
        """
        Setter for property: (str) BalloonTooltipOffText
         Returns the BalloonTooltipOffText  
            
         
        """
        pass
    @property
    def BalloonTooltipOnImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipOnImage
         Returns the BalloonTooltipOnImage  
            
         
        """
        pass
    @BalloonTooltipOnImage.setter
    def BalloonTooltipOnImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipOnImage
         Returns the BalloonTooltipOnImage  
            
         
        """
        pass
    @property
    def BalloonTooltipOnText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipOnText
         Returns the BalloonTooltipOnText  
            
         
        """
        pass
    @BalloonTooltipOnText.setter
    def BalloonTooltipOnText(self, tooltip_string: str):
        """
        Setter for property: (str) BalloonTooltipOnText
         Returns the BalloonTooltipOnText  
            
         
        """
        pass
    @property
    def Bitmap(self) -> str:
        """
        Getter for property: (str) Bitmap
         Returns the Bitmap  
            
         
        """
        pass
    @Bitmap.setter
    def Bitmap(self, bitmap_string: str):
        """
        Setter for property: (str) Bitmap
         Returns the Bitmap  
            
         
        """
        pass
    @property
    def BitmapOnly(self) -> bool:
        """
        Getter for property: (bool) BitmapOnly
         Returns the BitmapOnly  
            
         
        """
        pass
    @BitmapOnly.setter
    def BitmapOnly(self, bitmap_only: bool):
        """
        Setter for property: (bool) BitmapOnly
         Returns the BitmapOnly  
            
         
        """
        pass
    @property
    def Localize(self) -> bool:
        """
        Getter for property: (bool) Localize
         Returns the Localize  
            
         
        """
        pass
    @Localize.setter
    def Localize(self, localize: bool):
        """
        Setter for property: (bool) Localize
         Returns the Localize  
            
         
        """
        pass
    @property
    def RetainValue(self) -> bool:
        """
        Getter for property: (bool) RetainValue
         Returns the RetainValue  
            
         
        """
        pass
    @RetainValue.setter
    def RetainValue(self, retain: bool):
        """
        Setter for property: (bool) RetainValue
         Returns the RetainValue  
            
         
        """
        pass
    @property
    def Value(self) -> bool:
        """
        Getter for property: (bool) Value
         Returns the Value  
            
         
        """
        pass
    @Value.setter
    def Value(self, value_property: bool):
        """
        Setter for property: (bool) Value
         Returns the Value  
            
         
        """
        pass
    def GetBalloonTooltipLayoutMembers(self) -> List[str]:
        """
         Gets the BalloonTooltipLayout member
         Returns layout_strings (List[str]): Value to get from the property. .
        """
        pass
    def TestValueChanged(self, value_property: bool) -> None:
        """
        Tests value changed event workflow mapped to this Toggle block.
        """
        pass
import NXOpen
class TreeListMenu(NXOpen.TransientObject): 
    """ Represents a menu class utilized by BlockStyler.Tree.
Refer to BlockStyler.Tree.CreateMenu to create the menu.
"""
    @overload
    def AddMenuItem(self, menuItemID: int, menuItemText: str) -> None:
        """
         Adds single menu item 
        """
        pass
    @overload
    def AddMenuItem(self, menuItemID: int, menuItemText: str, icon: str) -> None:
        """
         Adds single menu item 
        """
        pass
    def AddSeparator(self) -> None:
        """
         Adds a separator 
        """
        pass
    def AddSeperator(self) -> None:
        """
         Adds a separator 
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.
        """
        pass
    def GetItemChecked(self, menuItemID: int) -> bool:
        """
        Gets the checked status for given menu item 
         Returns checkedStatus (bool):  Status .
        """
        pass
    def GetItemDefault(self, menuItemID: int) -> bool:
        """
        Gets the flag indicating whether the given menu item is default 
         Returns defaultStatus (bool):  Status .
        """
        pass
    def GetItemDialogLaunching(self, menuItemID: int) -> bool:
        """
        Gets the flag indicating whether the given menu item is dialog lanching 
         Returns dialogLaunchingStaus (bool):  Status .
        """
        pass
    def GetItemDisable(self, menuItemID: int) -> bool:
        """
        Gets the flag indicating whether the given menu item is disabled 
         Returns disableStatus (bool):  Status .
        """
        pass
    def GetItemHidden(self, menuItemID: int) -> bool:
        """
        Gets the flag indicating whether the given menu item is hidden 
         Returns hiddenStatus (bool):  Status .
        """
        pass
    def GetItemIcon(self, menuItemID: int) -> str:
        """
         Gets the icon for given menu item 
         Returns icon (str):  Display text .
        """
        pass
    def GetItemText(self, menuItemID: int) -> str:
        """
         Gets the display text for given menu item 
         Returns text (str):  Display text .
        """
        pass
    def SetItemChecked(self, menuItemID: int, checkedStatusStatus: bool) -> None:
        """
        Sets the checked status for given menu item 
        """
        pass
    def SetItemDefault(self, menuItemID: int, defaultStatus: bool) -> None:
        """
        Sets the flag indicating whether the given menu item is default 
        """
        pass
    def SetItemDialogLaunching(self, menuItemID: int, dialogLaunchingStaus: bool) -> None:
        """
        Sets the flag indicating whether the given menu item is dialog lanching 
        """
        pass
    def SetItemDisable(self, menuItemID: int, disableStatus: bool) -> None:
        """
        Sets the flag indicating whether the given menu item is disabled 
        """
        pass
    def SetItemHidden(self, menuItemID: int, hiddenStatus: bool) -> None:
        """
        Sets the flag indicating whether the given menu item is hidden 
        """
        pass
    def SetItemIcon(self, menuItemID: int, icon: str) -> None:
        """
         Sets the icon for given menu item 
        """
        pass
    def SetItemText(self, menuItemID: int, text: str) -> None:
        """
         Sets the display text for given menu item 
        """
        pass
    def SetSubMenu(self, menuItemID: int, sub_menu: TreeListMenu) -> None:
        """
         Sets a submenu. 
                Submenu can be created using BlockStyler.Tree.CreateMenu method
        """
        pass
class Tree(UIBlock): 
    """Represents the Tree block in block styler automation. To start utilizing the tree use
   methods such as BlockStyler.Tree.InsertColumn, BlockStyler.Tree.CreateNode, BlockStyler.Tree.InsertNode etc.
   It is must to insert the column on the tree before inserting any node. Node can be created but cannot be inserted without the column available on the tree. 
   Note that some of the methods of this class such as BlockStyler.Tree.InsertColumn must be used in or after the BlockStyler.BlockDialog.DialogShown callback after 
   which tree is fully constructed and ready for use."""
    class BeginLabelEditState(Enum):
        """
        Members Include: 
         |Allow| Use this option to allow label edit.
         |Disallow| Use this option to disallow label edit.

        """
        Allow: int
        Disallow: int
        @staticmethod
        def ValueOf(value: int) -> Tree.BeginLabelEditState:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ColumnDisplay(Enum):
        """
        Members Include: 
         |Text| Text
         |Icon| Icon

        """
        Text: int
        Icon: int
        @staticmethod
        def ValueOf(value: int) -> Tree.ColumnDisplay:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ColumnResizePolicy(Enum):
        """
        Members Include: 
         |ConstantWidth|  Constant width
         |ResizeWithContents| Width resized with contents.
         |ResizeWithTree| Width resize with tree window resize.

        """
        ConstantWidth: int
        ResizeWithContents: int
        ResizeWithTree: int
        @staticmethod
        def ValueOf(value: int) -> Tree.ColumnResizePolicy:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ColumnSortOption(Enum):
        """
        Members Include: 
         |Unsorted| Unsorted
         |Ascending| Ascending
         |Descending| Descending

        """
        Unsorted: int
        Ascending: int
        Descending: int
        @staticmethod
        def ValueOf(value: int) -> Tree.ColumnSortOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ControlType(Enum):
        """
        Members Include: 
         |NotSet| None
         |ComboBox| Combo box.
         |ListBox| List box.

        """
        NotSet: int
        ComboBox: int
        ListBox: int
        @staticmethod
        def ValueOf(value: int) -> Tree.ControlType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class EditControlOption(Enum):
        """
        Members Include: 
         |Accept| Use this option to allow edit.
         |Reject| Use this option to disallow edit.

        """
        Accept: int
        Reject: int
        @staticmethod
        def ValueOf(value: int) -> Tree.EditControlOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class EndLabelEditState(Enum):
        """
        Members Include: 
         |AcceptText| Use this option to accept the edited text.
         |RejectText| Use this option to reject the edited text and retain the previous one.

        """
        AcceptText: int
        RejectText: int
        @staticmethod
        def ValueOf(value: int) -> Tree.EndLabelEditState:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class NodeInsertOption(Enum):
        """
        Members Include: 
         |First| Node is placed first in the hierarchy in which it is inserted.
         |Last| Node is placed last in the hierarchy in which it is inserted.
         |Sort| Node is sorted according to display text and placed accordingly in the hierarchy in which it is inserted
         |AlwaysFirst| Node is placed first in the hierarchy in which it is inserted. This is same as 
                                                        BlockStyler.Tree.NodeInsertOption.First, except that it 
                                                        remains first after a column sort. If there is more than one node beneath a single parent 
                                                        with this option then they will be sorted relative to each other.
                                                        
         |AlwaysLast| Node is placed last in the hierarchy in which it is inserted. This is same as 
                                                        BlockStyler.Tree.NodeInsertOption.Last, except that it 
                                                        remains last after a column sort. If there is more than one node beneath a single parent 
                                                        with this option then they will be sorted relative to each other.
                                                        

        """
        First: int
        Last: int
        Sort: int
        AlwaysFirst: int
        AlwaysLast: int
        @staticmethod
        def ValueOf(value: int) -> Tree.NodeInsertOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CanStretchHeight(self) -> bool:
        """
        Getter for property: (bool) CanStretchHeight
         Returns the CanStretchHeight.  
           If true, height of list box will change.  
         
        """
        pass
    @CanStretchHeight.setter
    def CanStretchHeight(self, stretchHeight: bool):
        """
        Setter for property: (bool) CanStretchHeight
         Returns the CanStretchHeight.  
           If true, height of list box will change.  
         
        """
        pass
    @property
    def CanStretchWidth(self) -> bool:
        """
        Getter for property: (bool) CanStretchWidth
         Returns the CanStretchWidth.  
           If true, width of TreeList block will change.  
         
        """
        pass
    @CanStretchWidth.setter
    def CanStretchWidth(self, stretchWidth: bool):
        """
        Setter for property: (bool) CanStretchWidth
         Returns the CanStretchWidth.  
           If true, width of TreeList block will change.  
         
        """
        pass
    @property
    def FirstSelectedNode(self) -> Node:
        """
        Getter for property: ( Node NXOpen.B) FirstSelectedNode
         Returns the first selected node among the available selected nodes.  
           
               Returns NULL if no node is selected.  
         
        """
        pass
    @property
    def Height(self) -> int:
        """
        Getter for property: (int) Height
         Returns the Height  
            
         
        """
        pass
    @Height.setter
    def Height(self, height: int):
        """
        Setter for property: (int) Height
         Returns the Height  
            
         
        """
        pass
    @property
    def Localize(self) -> bool:
        """
        Getter for property: (bool) Localize
         Returns the Localize  
            
         
        """
        pass
    @Localize.setter
    def Localize(self, localize: bool):
        """
        Setter for property: (bool) Localize
         Returns the Localize  
            
         
        """
        pass
    @property
    def MaximumHeight(self) -> int:
        """
        Getter for property: (int) MaximumHeight
         Returns the MaximumHeight  
            
         
        """
        pass
    @MaximumHeight.setter
    def MaximumHeight(self, maxHeight: int):
        """
        Setter for property: (int) MaximumHeight
         Returns the MaximumHeight  
            
         
        """
        pass
    @property
    def MaximumWidth(self) -> int:
        """
        Getter for property: (int) MaximumWidth
         Returns the MaximumWidth  
            
         
        """
        pass
    @MaximumWidth.setter
    def MaximumWidth(self, maxWidth: int):
        """
        Setter for property: (int) MaximumWidth
         Returns the MaximumWidth  
            
         
        """
        pass
    @property
    def MinimumHeight(self) -> int:
        """
        Getter for property: (int) MinimumHeight
         Returns the MinimumHeight  
            
         
        """
        pass
    @MinimumHeight.setter
    def MinimumHeight(self, minHeight: int):
        """
        Setter for property: (int) MinimumHeight
         Returns the MinimumHeight  
            
         
        """
        pass
    @property
    def MinimumWidth(self) -> int:
        """
        Getter for property: (int) MinimumWidth
         Returns the MinimumWidth  
            
         
        """
        pass
    @MinimumWidth.setter
    def MinimumWidth(self, minWidth: int):
        """
        Setter for property: (int) MinimumWidth
         Returns the MinimumWidth  
            
         
        """
        pass
    @property
    def NumberOfColumns(self) -> int:
        """
        Getter for property: (int) NumberOfColumns
         Returns the number of column inserted in the tree.  
            
         
        """
        pass
    @property
    def RootNode(self) -> Node:
        """
        Getter for property: ( Node NXOpen.B) RootNode
         Returns the root node.  
           If more than one root node is available in top hierarchy 
              then the first root node is returned.  
         
        """
        pass
    @property
    def ScrollFrozenColumn(self) -> int:
        """
        Getter for property: (int) ScrollFrozenColumn
         Returns the ScrollFrozenColumn.  
           It specifies the number of columns to freeze while scrolling.  
         
        """
        pass
    @ScrollFrozenColumn.setter
    def ScrollFrozenColumn(self, scrollFrozenColumn: int):
        """
        Setter for property: (int) ScrollFrozenColumn
         Returns the ScrollFrozenColumn.  
           It specifies the number of columns to freeze while scrolling.  
         
        """
        pass
    @property
    def ScrollLineNumber(self) -> int:
        """
        Getter for property: (int) ScrollLineNumber
         Returns the ScrollLineNumber.  
           It specifies the number of lines to scroll when the mouse wheel rotates.  
         
        """
        pass
    @ScrollLineNumber.setter
    def ScrollLineNumber(self, scrollLineNumber: int):
        """
        Setter for property: (int) ScrollLineNumber
         Returns the ScrollLineNumber.  
           It specifies the number of lines to scroll when the mouse wheel rotates.  
         
        """
        pass
    @property
    def SelectionModeAsString(self) -> str:
        """
        Getter for property: (str) SelectionModeAsString
         Returns the SelectionMode  
            
         
        """
        pass
    @SelectionModeAsString.setter
    def SelectionModeAsString(self, enumString: str):
        """
        Setter for property: (str) SelectionModeAsString
         Returns the SelectionMode  
            
         
        """
        pass
    @property
    def ShowExpandCollapseMarker(self) -> bool:
        """
        Getter for property: (bool) ShowExpandCollapseMarker
         Returns the ShowExpandCollapseMarker.  
           If true, displays a sign as a marker alongside first node of the tree indicating if it is expanded or collapsed.  
         
        """
        pass
    @ShowExpandCollapseMarker.setter
    def ShowExpandCollapseMarker(self, show: bool):
        """
        Setter for property: (bool) ShowExpandCollapseMarker
         Returns the ShowExpandCollapseMarker.  
           If true, displays a sign as a marker alongside first node of the tree indicating if it is expanded or collapsed.  
         
        """
        pass
    @property
    def ShowHeader(self) -> bool:
        """
        Getter for property: (bool) ShowHeader
         Returns the ShowHeader  
            
         
        """
        pass
    @ShowHeader.setter
    def ShowHeader(self, show: bool):
        """
        Setter for property: (bool) ShowHeader
         Returns the ShowHeader  
            
         
        """
        pass
    @property
    def ShowMultipleColumns(self) -> bool:
        """
        Getter for property: (bool) ShowMultipleColumns
         Returns the ShowMultipleColumns  
            
         
        """
        pass
    @ShowMultipleColumns.setter
    def ShowMultipleColumns(self, show: bool):
        """
        Setter for property: (bool) ShowMultipleColumns
         Returns the ShowMultipleColumns  
            
         
        """
        pass
    @property
    def ShowToolTips(self) -> bool:
        """
        Getter for property: (bool) ShowToolTips
         Returns the ShowToolTips  
            
         
        """
        pass
    @ShowToolTips.setter
    def ShowToolTips(self, show: bool):
        """
        Setter for property: (bool) ShowToolTips
         Returns the ShowToolTips  
            
         
        """
        pass
    @property
    def SortRootNodes(self) -> bool:
        """
        Getter for property: (bool) SortRootNodes
         Returns the SortRootNodes.  
           If true, sorting of root nodes is allowed.  
         
        """
        pass
    @SortRootNodes.setter
    def SortRootNodes(self, sort: bool):
        """
        Setter for property: (bool) SortRootNodes
         Returns the SortRootNodes.  
           If true, sorting of root nodes is allowed.  
         
        """
        pass
    @property
    def Width(self) -> int:
        """
        Getter for property: (int) Width
         Returns the Width  
            
         
        """
        pass
    @Width.setter
    def Width(self, width: int):
        """
        Setter for property: (int) Width
         Returns the Width  
            
         
        """
        pass
    AskEditControlCallback = Callable[[Tree, Node, int], None]
    ColumnSortCallback = Callable[[Tree, int, Node, Node], None]
    def CopyNode(self, sourceNode: Node) -> Node:
        """
        Copies the existing BlockStyler.Node. The tree can copy either its own node or the node of another tree. 
               The copied node can only be inserted into the tree which has copied that node. The column texts are not passed to the copied node. 
            
         Returns copiedNode ( Node NXOpen.B): Copied node.
        """
        pass
    def CreateMenu(self) -> TreeListMenu:
        """
         Creates the menu. Use BlockStyler.Tree.SetMenu to set the created menu.
         Returns menu ( TreeListMenu NXOpen.B):  .
        """
        pass
    def CreateNode(self, displayText: str) -> Node:
        """
        Creates the node but does not insert it. Use BlockStyler.Tree.InsertNode to insert 
                the node.
         Returns node ( Node NXOpen.B): Node.
        """
        pass
    def DeleteNode(self, node: Node) -> None:
        """
        Deletes the node from tree. Further usage of deleted node is illegal. The last place where node can be used is in 
              BlockStyler.Tree.OnDeleteNodeCallaback callback which gets called when node is deleted.
        """
        pass
    def GetColumnDisplayType(self, columnID: int) -> Tree.ColumnDisplay:
        """
        Gets the display type of the column.
         Returns displayType ( Tree.ColumnDisplay NXOpen.B): Display type.
        """
        pass
    def GetColumnId(self, columnPosition: int) -> int:
        """
        Gets the column Id for the provided column position.
         Returns columnID (int): Unique column Id associated with the column.
        """
        pass
    def GetColumnPosition(self, columnID: int) -> int:
        """
        Gets column position. Returns -1 if no column is associated with the provided column Id.
         Returns columnPosition (int): Column position.
        """
        pass
    def GetColumnResizePolicy(self, columnID: int) -> Tree.ColumnResizePolicy:
        """
        Gets the column resize policy.
         Returns resizePolicy ( Tree.ColumnResizePolicy NXOpen.B): Resize policy.
        """
        pass
    def GetColumnSortOption(self, columnID: int) -> Tree.ColumnSortOption:
        """
        Gets the column sort option.
         Returns sortOption ( Tree.ColumnSortOption NXOpen.B): Column sort option.
        """
        pass
    def GetColumnSortable(self, columnID: int) -> bool:
        """
        Gets the flag indicating whether the column is sortable.
         Returns isSortable (bool): Flag indicating whether the column is sortable.
        """
        pass
    def GetColumnTitle(self, columnID: int) -> str:
        """
        Gets the column title.
         Returns columnHeaderTitle (str): Column header title.
        """
        pass
    def GetColumnVisible(self, columnID: int) -> bool:
        """
        Gets the flag indicating whether the column is visible.
         Returns isVisible (bool): Flag indicating whether the column is visible.
        """
        pass
    def GetColumnWidth(self, columnID: int) -> int:
        """
        Gets column width
         Returns columnWidth (int): Column width.
        """
        pass
    def GetSelectedNodes(self) -> List[Node]:
        """
        Gets the selected nodes.
         Returns nodes ( Node List[NXOpen): Selected nodes.
        """
        pass
    def GetSelectionModeMembers(self) -> List[str]:
        """
         Gets the SelectionMode
         Returns members_strings (List[str]): Value to get from the property.
        """
        pass
    def InsertColumn(self, columnID: int, columnTitle: str, columnWidth: int) -> int:
        """
         Inserts a column.
               
               Inserts a column with following defaults: 
               
               BlockStyler.Tree.ColumnSortOption as BlockStyler.Tree.ColumnSortOption.Ascending
               Column sortable as True
               Column visible as True
               BlockStyler.Tree.ColumnDisplay as BlockStyler.Tree.ColumnDisplay.Text
               BlockStyler.Tree.ColumnResizePolicy as BlockStyler.Tree.ColumnResizePolicy.ConstantWidth
               
               The new column is placed after the last available column. If no column is available then the inserted one becomes the first column of the tree.
            
         Returns columnPosition (int): Absolute column position.
        """
        pass
    def InsertNode(self, newNode: Node, parentNode: Node, afterNode: Node, nodeInsertOption: Tree.NodeInsertOption) -> None:
        """
        Inserts the node. Subsequently BlockStyler.Tree.OnInsertNodeCallback is called. 
               Reinserting the node in same or different tree is not allowed.
        """
        pass
    IsDragAllowedCallback = Callable[[Tree, Node, int], None]
    IsDropAllowedCallback = Callable[[Tree, Node, int, Node, int], None]
    OnBeginLabelEditCallback = Callable[[Tree, Node, int], None]
    OnDefaultActionCallback = Callable[[Tree, Node, int], None]
    OnDeleteNodeCallback = Callable[[Tree, Node], None]
    OnDropCallback = Callable[[Tree, List[Node], int, Node, int, Node.DropType, int], None]
    OnDropMenuCallback = Callable[[Tree, Node, int, Node, int], None]
    OnEditOptionSelectedCallback = Callable[[Tree, Node, int, int, str, Tree.ControlType], None]
    OnEndLabelEditCallback = Callable[[Tree, Node, int, str], None]
    OnExpandCallback = Callable[[Tree, Node], None]
    OnInsertColumnCallback = Callable[[Tree, Node, int], None]
    OnInsertNodeCallback = Callable[[Tree, Node], None]
    OnMenuCallback = Callable[[Tree, Node, int], None]
    OnMenuSelectionCallback = Callable[[Tree, Node, int], None]
    OnPreSelectCallback = Callable[[Tree, Node, int, bool], None]
    OnSelectCallback = Callable[[Tree, Node, int, bool], None]
    OnStateChangeCallback = Callable[[Tree, Node, int], None]
    def Redraw(self, redraw: bool) -> None:
        """
        Freezes the tree if the value is set to False which implies that no changes would occur 
               in the tree after this point. The tree remains in that state until the value is set to True, 
               after which the tree completely updates itself with the changes performed on it in between 
               the two calls. Use this method to efficiently utilize the tree when it is subjected to enourmous changes.
        """
        pass
    def SelectNode(self, node: Node, isSelect: bool, isOtherNodeAffected: bool) -> None:
        """
        Selects the provided node.
        """
        pass
    def SelectNodes(self, node: List[Node], isSelect: bool, isOtherNodeAffected: bool) -> None:
        """
        Selects the provided nodes.
        """
        pass
    def SetAskEditControlHandler(self, cb: Tree.AskEditControlCallback) -> None:
        """
        Sets the node-edit-control callback
        """
        pass
    def SetColumnDisplayType(self, columnID: int, displayType: Tree.ColumnDisplay) -> None:
        """
        Sets the display type of the column.
        """
        pass
    def SetColumnResizePolicy(self, columnID: int, resizePolicy: Tree.ColumnResizePolicy) -> None:
        """
        Sets the column resize policy.
        """
        pass
    def SetColumnSortHandler(self, cb: Tree.ColumnSortCallback) -> None:
        """
        Sets the column sort callback.
        """
        pass
    def SetColumnSortOption(self, columnID: int, sortOption: Tree.ColumnSortOption) -> None:
        """
        Sets the column sort option.
        """
        pass
    def SetColumnSortable(self, columnID: int, isSortable: bool) -> None:
        """
        Sets the flag indicating whether the column is sortable.
        """
        pass
    def SetColumnTitle(self, columnID: int, columnHeaderTitle: str) -> None:
        """
        Sets the column title.
        """
        pass
    def SetColumnVisible(self, columnID: int, isVisible: bool) -> None:
        """
        Sets the flag indicating whether the column is visible
        """
        pass
    def SetColumnWidth(self, columnID: int, columnWidth: int) -> None:
        """
        Sets the column width
        """
        pass
    def SetEditOptions(self, stringArray: List[str], defaultIndex: int) -> None:
        """
        Sets the options in edit-control. This method must be used
               in BlockStyler.Tree.AskEditControlCallback to make available the options in edit-control.
               
              
        """
        pass
    def SetIsDragAllowedHandler(self, cb: Tree.IsDragAllowedCallback) -> None:
        """
        Sets the callback handler for node drag
        """
        pass
    def SetIsDropAllowedHandler(self, cb: Tree.IsDropAllowedCallback) -> None:
        """
        Sets the callback handler for node drop
        """
        pass
    def SetMenu(self, menu: TreeListMenu) -> None:
        """
         Sets the menu, resulting the menu to appear on the screen. This method must be used in callback which is intended to create
                menu, such as BlockStyler.Tree.OnMenuCallback
        """
        pass
    def SetOnBeginLabelEditHandler(self, cb: Tree.OnBeginLabelEditCallback) -> None:
        """
        Sets the on-begin-label-edit callback
        """
        pass
    def SetOnDefaultActionHandler(self, cb: Tree.OnDefaultActionCallback) -> None:
        """
         Sets the on select node callback 
        """
        pass
    def SetOnDeleteNodeHandler(self, cb: Tree.OnDeleteNodeCallback) -> None:
        """
         Sets on delete node callback 
        """
        pass
    def SetOnDropHandler(self, cb: Tree.OnDropCallback) -> None:
        """
        Sets the callback handler for node drop
        """
        pass
    def SetOnDropMenuHandler(self, cb: Tree.OnDropMenuCallback) -> None:
        """
        Sets the callback handler for on drop menu.
        """
        pass
    def SetOnEditOptionSelectedHandler(self, cb: Tree.OnEditOptionSelectedCallback) -> None:
        """
        Sets the on-end-label-edit callback
        """
        pass
    def SetOnEndLabelEditHandler(self, cb: Tree.OnEndLabelEditCallback) -> None:
        """
        Sets the on-end-label-edit callback
        """
        pass
    def SetOnExpandHandler(self, cb: Tree.OnExpandCallback) -> None:
        """
        Sets the on expand callback to the tree.
        """
        pass
    def SetOnInsertColumnHandler(self, cb: Tree.OnInsertColumnCallback) -> None:
        """
        Sets the on insert column callback to the tree.
        """
        pass
    def SetOnInsertNodeHandler(self, cb: Tree.OnInsertNodeCallback) -> None:
        """
         Sets the on insert node callback. 
        """
        pass
    def SetOnMenuHandler(self, cb: Tree.OnMenuCallback) -> None:
        """
         Sets the on menu callback 
        """
        pass
    def SetOnMenuSelectionHandler(self, cb: Tree.OnMenuSelectionCallback) -> None:
        """
         Sets the on menu selection callback 
        """
        pass
    def SetOnPreSelectHandler(self, cb: Tree.OnPreSelectCallback) -> None:
        """
         Sets on pre select callback 
        """
        pass
    def SetOnSelectHandler(self, cb: Tree.OnSelectCallback) -> None:
        """
         Sets the on select node callback 
        """
        pass
    def SetOnStateChangeHandler(self, cb: Tree.OnStateChangeCallback) -> None:
        """
        Sets the on state change callback.
        """
        pass
    def SetPreSelectionTimeOut(self, timeOut: float) -> None:
        """
        Sets the pre selection time out. BlockStyler.Tree.OnPreSelectCallback is called based on this value.
        """
        pass
    StateIconNameCallback = Callable[[Tree, Node, int], None]
    def SetStateIconNameHandler(self, cb: Tree.StateIconNameCallback) -> None:
        """
        Sets the state icon name callback.
        """
        pass
    ToolTipTextCallback = Callable[[Tree, Node, int], None]
    def SetToolTipTextHandler(self, cb: Tree.ToolTipTextCallback) -> None:
        """
        Sets the tool tip callback.
        """
        pass
    def TestColumnInserted(self, columnID: int, columnTitle: str, columnWidth: int) -> int:
        """
        Test the action to insert the column. 
         Returns columnPosition (int): .
        """
        pass
    def TestColumnSort(self, columnID: int, node1: Node, node2: Node, sortOption: Tree.ColumnSortOption) -> None:
        """
        Test the action to sort the column. 
        """
        pass
    def TestContextMenu(self, node: Node, columnID: int) -> None:
        """
        Test the action to show context menu. 
        """
        pass
    def TestDefaultAction(self, node: Node, columnID: int) -> None:
        """
        Test the default action. 
        """
        pass
    def TestDropMenu(self, node: Node, columnID: int, targetNode: Node, targetColumnID: int) -> None:
        """
        Test the action to show the drop menu. 
        """
        pass
    def TestLabelEdit(self, node: Node, columnID: int, editedText: str) -> None:
        """
        Test the action to edit the label of the node. 
        """
        pass
    def TestMenuAction(self, node: Node, command: int) -> None:
        """
        Test the action to click the command of the context menu. 
        """
        pass
    def TestNodeDeleted(self, node: Node) -> None:
        """
        Test the action to delete the node. 
        """
        pass
    def TestNodeDrop(self, node: Node, columnID: int, targetNode: Node, targetColumnID: int, command: int) -> None:
        """
        Test the action to click the command of the drop menu. 
        """
        pass
    def TestNodeExpanded(self, node: Node, expandOption: Node.ExpandOption) -> None:
        """
        Test the action to expand the node. 
        """
        pass
    def TestNodeInserted(self, newNode: Node, parentNode: Node, afterNode: Node, nodeInsertOption: Tree.NodeInsertOption) -> None:
        """
        Test the action to insert a node. 
        """
        pass
    def TestNodePreselection(self, node: Node, columnID: int) -> None:
        """
        Test the action to preselect the node. 
        """
        pass
    def TestNodeSelected(self, node: Node, isSelect: bool, isOtherNodeAffected: bool) -> None:
        """
        Test the action to select the node. 
        """
        pass
    def TestStateChanged(self, node: Node, state: int) -> None:
        """
        Test the action to preselect the node. 
        """
        pass
import NXOpen
class UIBlock(NXOpen.TaggedObject): 
    """ Represents a UI Block"""
    @property
    def Enable(self) -> bool:
        """
        Getter for property: (bool) Enable
         Returns the Enable.  
           If true, the block is sensitive.  
         
        """
        pass
    @Enable.setter
    def Enable(self, enable: bool):
        """
        Setter for property: (bool) Enable
         Returns the Enable.  
           If true, the block is sensitive.  
         
        """
        pass
    @property
    def Expanded(self) -> bool:
        """
        Getter for property: (bool) Expanded
         Returns the Expanded  
            
         
        """
        pass
    @Expanded.setter
    def Expanded(self, expanded: bool):
        """
        Setter for property: (bool) Expanded
         Returns the Expanded  
            
         
        """
        pass
    @property
    def Group(self) -> bool:
        """
        Getter for property: (bool) Group
         Returns the Group  
            
         
        """
        pass
    @Group.setter
    def Group(self, group: bool):
        """
        Setter for property: (bool) Group
         Returns the Group  
            
         
        """
        pass
    @property
    def Label(self) -> str:
        """
        Getter for property: (str) Label
         Returns the Label  
            
         
        """
        pass
    @Label.setter
    def Label(self, label: str):
        """
        Setter for property: (str) Label
         Returns the Label  
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name of the block or BlockID  
            
         
        """
        pass
    @property
    def Show(self) -> bool:
        """
        Getter for property: (bool) Show
         Returns the Visibility of block.  
           If true, the block is visible. Otherwise invisible.
            This is readonly property for dialog and will be always true for dialog.  
         
        """
        pass
    @Show.setter
    def Show(self, show: bool):
        """
        Setter for property: (bool) Show
         Returns the Visibility of block.  
           If true, the block is visible. Otherwise invisible.
            This is readonly property for dialog and will be always true for dialog.  
         
        """
        pass
    @property
    def Type(self) -> str:
        """
        Getter for property: (str) Type
         Returns the type of block   
            
         
        """
        pass
    def Focus(self) -> None:
        """
        Focuses on the block. Use this method for both focus and keyboard focus.
        """
        pass
    def GetProperties(self) -> PropertyList:
        """
         Returns the properties of the block 
         Returns propertyList ( PropertyList NXOpen.B): .
        """
        pass
    def TestFocusChange(self) -> None:
        """
        Tests the focus change callbacks. Use this method for both focus and keyboard focus.
        """
        pass
class Wizard(UIBlock): 
    """ Represents a Wizard block """
    class DialogResponse(Enum):
        """
        Members Include: 
         |Back|  Back button was pressed.. 
         |Next|  Next button was pressed. 
         |Finish|  Finish button was pressed. 
         |Apply|  Apply button was pressed. 
         |Cancel|  Cancel button was pressed. 

        """
        Back: int
        Next: int
        Finish: int
        Apply: int
        Cancel: int
        @staticmethod
        def ValueOf(value: int) -> Wizard.DialogResponse:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SubNodeAction(Enum):
        """
        Members Include: 
         |Select|  Sub-node has been selected. 
         |Deselect|  Sub-node has been deselected. 
         |Check|  Sub-node has been checked if a checkbox was specified. 
         |Uncheck|  Sub-node has been unchecked if a checkbox was specified. 

        """
        Select: int
        Deselect: int
        Check: int
        Uncheck: int
        @staticmethod
        def ValueOf(value: int) -> Wizard.SubNodeAction:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TaskNavigatorItem(Enum):
        """
        Members Include: 
         |Step|   
         |SubNode|   
         |Background|   

        """
        Step: int
        SubNode: int
        Background: int
        @staticmethod
        def ValueOf(value: int) -> Wizard.TaskNavigatorItem:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CurrentStep(self) -> int:
        """
        Getter for property: (int) CurrentStep
         Returns the CurrentStep.  
             
         
        """
        pass
    @CurrentStep.setter
    def CurrentStep(self, currentStep: int):
        """
        Setter for property: (int) CurrentStep
         Returns the CurrentStep.  
             
         
        """
        pass
    @property
    def HighQualityBitmap(self) -> bool:
        """
        Getter for property: (bool) HighQualityBitmap
         Returns the HighQualityBitmap.  
             
         
        """
        pass
    @HighQualityBitmap.setter
    def HighQualityBitmap(self, highQuality: bool):
        """
        Setter for property: (bool) HighQualityBitmap
         Returns the HighQualityBitmap.  
             
         
        """
        pass
    @property
    def Localize(self) -> bool:
        """
        Getter for property: (bool) Localize
         Returns the Localize.  
             
         
        """
        pass
    @Localize.setter
    def Localize(self, localize: bool):
        """
        Setter for property: (bool) Localize
         Returns the Localize.  
             
         
        """
        pass
    @property
    def Members(self) -> PropertyList:
        """
        Getter for property: ( PropertyList NXOpen.B) Members
         Returns the Members  
            
         
        """
        pass
    @property
    def ShowTaskNavigator(self) -> bool:
        """
        Getter for property: (bool) ShowTaskNavigator
         Returns the ShowTaskNavigator.  
             
         
        """
        pass
    @ShowTaskNavigator.setter
    def ShowTaskNavigator(self, show: bool):
        """
        Setter for property: (bool) ShowTaskNavigator
         Returns the ShowTaskNavigator.  
             
         
        """
        pass
    def CreateMenu(self) -> TreeListMenu:
        """
         Creates a popup menu. Use BlockStyler.Wizard.SetMenu to set
                 the created menu.  See the BlockStyler.TreeListMenu for
                 information on creating a menu.  
         Returns menu ( TreeListMenu NXOpen.B):  .
        """
        pass
    def CreateStepSubNode(self, step: int, text: str, bitmap: str, showCheckBox: bool, checkBoxChecked: bool) -> int:
        """
         Create a sub-node for a step in the Task Navigator. 
         Returns subNodeId (int):  Unique id for the sub-node. .
        """
        pass
    def GetStepBannerBitmaps(self) -> List[str]:
        """
         Gets the StepBannerBitmaps. Gets the list of bitmaps for the step bitmaps in the banner area.
         Returns bitmaps (List[str]): .
        """
        pass
    def GetStepBitmaps(self) -> List[str]:
        """
         Gets the StepBitmaps. Gets the list of bitmaps for the node bitmaps in the Task Navigator.
         Returns bitmaps (List[str]): .
        """
        pass
    def GetStepCues(self) -> List[str]:
        """
         Gets the StepCues. Gets the list of cue lines for the wizard steps.
         Returns cues (List[str]): .
        """
        pass
    def GetStepText(self) -> List[str]:
        """
         Gets the StepText. Gets the list of step descriptions for the banner area.
         Returns text (List[str]): .
        """
        pass
    IsStepOkayCallback = Callable[[Wizard, int], None]
    OnMenuCallback = Callable[[Wizard, Wizard.TaskNavigatorItem, int, int], None]
    OnMenuSelectionCallback = Callable[[Wizard, Wizard.TaskNavigatorItem, int, int, int], None]
    OnSubNodeCallback = Callable[[Wizard, int, int, Wizard.SubNodeAction], None]
    def RemoveStepSubNode(self, subNodeId: int) -> None:
        """
         Remove a sub-node in the Task Navigator. 
        """
        pass
    def SetDialogNavigationResponse(self, response: Wizard.DialogResponse) -> None:
        """
         Sets the dialog navigation response for testing
        """
        pass
    def SetIsStepOkayHandler(self, cb: Wizard.IsStepOkayCallback) -> None:
        """
         Sets the IsStepOkay handler. 
        """
        pass
    def SetMenu(self, menu: TreeListMenu) -> None:
        """
         Set the menu items for the popup menu for a step, sub-node or the background
                in the Task Navigator.  See the BlockStyler.TreeListMenu for
                information on creating a menu.
        """
        pass
    def SetOnMenuHandler(self, cb: Wizard.OnMenuCallback) -> None:
        """
         Sets the OnMenu handler. 
        """
        pass
    def SetOnMenuSelectionHandler(self, cb: Wizard.OnMenuSelectionCallback) -> None:
        """
         Sets the OnMenuSelection handler. 
        """
        pass
    def SetOnSubNodeHandler(self, cb: Wizard.OnSubNodeCallback) -> None:
        """
         Sets the OnSubNode handler. 
        """
        pass
    def SetStepBannerBitmaps(self, bitmaps: List[str]) -> None:
        """
         Sets the StepBannerBitmaps. Sets the list of bitmaps for the step bitmaps in the banner area.
        """
        pass
    def SetStepBitmaps(self, bitmaps: List[str]) -> None:
        """
         Sets the StepBitmaps. Sets the list of bitmaps for the node bitmaps in the Task Navigator.
        """
        pass
    def SetStepCues(self, cues: List[str]) -> None:
        """
         Sets the StepCues. Sets the list of cue lines for the wizard steps.
        """
        pass
    StepNotifyPostCallback = Callable[[Wizard, int], None]
    def SetStepNotifyPostHandler(self, cb: Wizard.StepNotifyPostCallback) -> None:
        """
         Sets the StepNotifyPost handler. 
        """
        pass
    StepNotifyPreCallback = Callable[[Wizard, int], None]
    def SetStepNotifyPreHandler(self, cb: Wizard.StepNotifyPreCallback) -> None:
        """
         Sets the StepNotifyPre handler. 
        """
        pass
    def SetStepText(self, text: List[str]) -> None:
        """
         Sets the StepText. Sets the list of step descriptions for the banner area.
        """
        pass
    def TestCurrentStepChanged(self, currentStep: int) -> None:
        """
        Tests set current step.
        """
        pass
    def TestMenuAction(self, item: Wizard.TaskNavigatorItem, stepNo: int, subNodeId: int) -> None:
        """
        Tests the menu action mapped to this block.
        """
        pass
    def TestMenuSelection(self, item: Wizard.TaskNavigatorItem, stepNo: int, subNodeId: int, menuItemIndex: int) -> None:
        """
        Tests the menu selection mapped to this block.
        """
        pass
    def TestSubnodeAction(self, stepNo: int, subNodeId: int, item: Wizard.SubNodeAction) -> None:
        """
        Tests the subnode action mapped to this block.
        """
        pass
