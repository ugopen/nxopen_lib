from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents a Angular Dimension block
## 
##   <br>  Created in NX8.5.0  <br> 

class AngularDimension(UIBlock): 
    """ Represents a Angular Dimension block"""


    ## Getter for property: (bool) AdaptiveScaleLimits
    ##  the AdaptiveScaleLimits.  
    ##   
    ##         If true, indicates that the scale should be adaptive. Only available when WithScale is set to true.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def AdaptiveScaleLimits(self) -> bool:
        """
        Getter for property: (bool) AdaptiveScaleLimits
         the AdaptiveScaleLimits.  
          
                If true, indicates that the scale should be adaptive. Only available when WithScale is set to true.  
         
        """
        pass
    
    ## Setter for property: (bool) AdaptiveScaleLimits

    ##  the AdaptiveScaleLimits.  
    ##   
    ##         If true, indicates that the scale should be adaptive. Only available when WithScale is set to true.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @AdaptiveScaleLimits.setter
    def AdaptiveScaleLimits(self, scale_limits: bool):
        """
        Setter for property: (bool) AdaptiveScaleLimits
         the AdaptiveScaleLimits.  
          
                If true, indicates that the scale should be adaptive. Only available when WithScale is set to true.  
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipImage
    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipImage

    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipLayoutAsString
    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipLayoutAsString

    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipText
    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipText

    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ExpressionObject
    ##   the ExpressionObject  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def ExpressionObject(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ExpressionObject
          the ExpressionObject  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ExpressionObject

    ##   the ExpressionObject  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ExpressionObject.setter
    def ExpressionObject(self, expression_obj: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ExpressionObject
          the ExpressionObject  
            
         
        """
        pass
    
    ## Getter for property: (str) Formula
    ##   the Formula  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Formula(self) -> str:
        """
        Getter for property: (str) Formula
          the Formula  
            
         
        """
        pass
    
    ## Setter for property: (str) Formula

    ##   the Formula  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Formula.setter
    def Formula(self, formula: str):
        """
        Setter for property: (str) Formula
          the Formula  
            
         
        """
        pass
    
    ## Getter for property: (bool) HandleFixedSizeFlag
    ##   the HandleFixedSizeFlag  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def HandleFixedSizeFlag(self) -> bool:
        """
        Getter for property: (bool) HandleFixedSizeFlag
          the HandleFixedSizeFlag  
            
         
        """
        pass
    
    ## Setter for property: (bool) HandleFixedSizeFlag

    ##   the HandleFixedSizeFlag  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @HandleFixedSizeFlag.setter
    def HandleFixedSizeFlag(self, handle_flag: bool):
        """
        Setter for property: (bool) HandleFixedSizeFlag
          the HandleFixedSizeFlag  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) HandleOrigin
    ##   the HandleOrigin  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def HandleOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) HandleOrigin
          the HandleOrigin  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) HandleOrigin

    ##   the HandleOrigin  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @HandleOrigin.setter
    def HandleOrigin(self, handle_orogin: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) HandleOrigin
          the HandleOrigin  
            
         
        """
        pass
    
    ## Getter for property: (float) HandleRadius
    ##   the HandleRadius  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return float
    @property
    def HandleRadius(self) -> float:
        """
        Getter for property: (float) HandleRadius
          the HandleRadius  
            
         
        """
        pass
    
    ## Setter for property: (float) HandleRadius

    ##   the HandleRadius  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @HandleRadius.setter
    def HandleRadius(self, handle_radius: float):
        """
        Setter for property: (float) HandleRadius
          the HandleRadius  
            
         
        """
        pass
    
    ## Getter for property: (float) HandleRadiusOffset
    ##   the HandleRadiusOffset  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return float
    @property
    def HandleRadiusOffset(self) -> float:
        """
        Getter for property: (float) HandleRadiusOffset
          the HandleRadiusOffset  
            
         
        """
        pass
    
    ## Setter for property: (float) HandleRadiusOffset

    ##   the HandleRadiusOffset  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @HandleRadiusOffset.setter
    def HandleRadiusOffset(self, radius_offset: float):
        """
        Setter for property: (float) HandleRadiusOffset
          the HandleRadiusOffset  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) HandleXAxis
    ##   the HandleXAxis  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.Vector3d
    @property
    def HandleXAxis(self) -> NXOpen.Vector3d:
        """
        Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) HandleXAxis
          the HandleXAxis  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) HandleXAxis

    ##   the HandleXAxis  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @HandleXAxis.setter
    def HandleXAxis(self, handle_x_axis: NXOpen.Vector3d):
        """
        Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) HandleXAxis
          the HandleXAxis  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) HandleZAxis
    ##   the HandleZAxis  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.Vector3d
    @property
    def HandleZAxis(self) -> NXOpen.Vector3d:
        """
        Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) HandleZAxis
          the HandleZAxis  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) HandleZAxis

    ##   the HandleZAxis  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @HandleZAxis.setter
    def HandleZAxis(self, handle_z_axis: NXOpen.Vector3d):
        """
        Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) HandleZAxis
          the HandleZAxis  
            
         
        """
        pass
    
    ## Getter for property: (float) LineIncrement
    ##  the LineIncrement value.  
    ##   
    ##         Specifies the increment/decrement when the user presses the arrow keys on the keyboard.
    ##         Only available when WithScale is set to true.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def LineIncrement(self) -> float:
        """
        Getter for property: (float) LineIncrement
         the LineIncrement value.  
          
                Specifies the increment/decrement when the user presses the arrow keys on the keyboard.
                Only available when WithScale is set to true.  
         
        """
        pass
    
    ## Setter for property: (float) LineIncrement

    ##  the LineIncrement value.  
    ##   
    ##         Specifies the increment/decrement when the user presses the arrow keys on the keyboard.
    ##         Only available when WithScale is set to true.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @LineIncrement.setter
    def LineIncrement(self, line_increment: float):
        """
        Setter for property: (float) LineIncrement
         the LineIncrement value.  
          
                Specifies the increment/decrement when the user presses the arrow keys on the keyboard.
                Only available when WithScale is set to true.  
         
        """
        pass
    
    ## Getter for property: (bool) MaxInclusive
    ##   the MaxInclusive  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def MaxInclusive(self) -> bool:
        """
        Getter for property: (bool) MaxInclusive
          the MaxInclusive  
            
         
        """
        pass
    
    ## Setter for property: (bool) MaxInclusive

    ##   the MaxInclusive  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MaxInclusive.setter
    def MaxInclusive(self, max_inclusive: bool):
        """
        Setter for property: (bool) MaxInclusive
          the MaxInclusive  
            
         
        """
        pass
    
    ## Getter for property: (float) MaximumValue
    ##   the MaximumValue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return float
    @property
    def MaximumValue(self) -> float:
        """
        Getter for property: (float) MaximumValue
          the MaximumValue  
            
         
        """
        pass
    
    ## Setter for property: (float) MaximumValue

    ##   the MaximumValue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MaximumValue.setter
    def MaximumValue(self, max_value: float):
        """
        Setter for property: (float) MaximumValue
          the MaximumValue  
            
         
        """
        pass
    
    ## Getter for property: (bool) MinInclusive
    ##   the MinInclusive  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def MinInclusive(self) -> bool:
        """
        Getter for property: (bool) MinInclusive
          the MinInclusive  
            
         
        """
        pass
    
    ## Setter for property: (bool) MinInclusive

    ##   the MinInclusive  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MinInclusive.setter
    def MinInclusive(self, min_inclusive: bool):
        """
        Setter for property: (bool) MinInclusive
          the MinInclusive  
            
         
        """
        pass
    
    ## Getter for property: (float) MinRadius
    ##   the MinRadius  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return float
    @property
    def MinRadius(self) -> float:
        """
        Getter for property: (float) MinRadius
          the MinRadius  
            
         
        """
        pass
    
    ## Setter for property: (float) MinRadius

    ##   the MinRadius  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @MinRadius.setter
    def MinRadius(self, min_radius: float):
        """
        Setter for property: (float) MinRadius
          the MinRadius  
            
         
        """
        pass
    
    ## Getter for property: (float) MinimumValue
    ##   the MinimumValue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return float
    @property
    def MinimumValue(self) -> float:
        """
        Getter for property: (float) MinimumValue
          the MinimumValue  
            
         
        """
        pass
    
    ## Setter for property: (float) MinimumValue

    ##   the MinimumValue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MinimumValue.setter
    def MinimumValue(self, min_value: float):
        """
        Setter for property: (float) MinimumValue
          the MinimumValue  
            
         
        """
        pass
    
    ## Getter for property: (float) PageIncrement
    ##  the PageIncrement value.  
    ##   
    ##         Specifies the increment/decrement when the user presses the Page Up or Page Down keys on the keyboard.
    ##         Only available when WithScale is set to true.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def PageIncrement(self) -> float:
        """
        Getter for property: (float) PageIncrement
         the PageIncrement value.  
          
                Specifies the increment/decrement when the user presses the Page Up or Page Down keys on the keyboard.
                Only available when WithScale is set to true.  
         
        """
        pass
    
    ## Setter for property: (float) PageIncrement

    ##  the PageIncrement value.  
    ##   
    ##         Specifies the increment/decrement when the user presses the Page Up or Page Down keys on the keyboard.
    ##         Only available when WithScale is set to true.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @PageIncrement.setter
    def PageIncrement(self, page_increment: float):
        """
        Setter for property: (float) PageIncrement
         the PageIncrement value.  
          
                Specifies the increment/decrement when the user presses the Page Up or Page Down keys on the keyboard.
                Only available when WithScale is set to true.  
         
        """
        pass
    
    ## Getter for property: (bool) ShowFocusHandle
    ##   the ShowFocusHandle  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowFocusHandle(self) -> bool:
        """
        Getter for property: (bool) ShowFocusHandle
          the ShowFocusHandle  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowFocusHandle

    ##   the ShowFocusHandle  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowFocusHandle.setter
    def ShowFocusHandle(self, show_focus: bool):
        """
        Setter for property: (bool) ShowFocusHandle
          the ShowFocusHandle  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowHandle
    ##   the ShowHandle  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowHandle(self) -> bool:
        """
        Getter for property: (bool) ShowHandle
          the ShowHandle  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowHandle

    ##   the ShowHandle  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowHandle.setter
    def ShowHandle(self, show_handle: bool):
        """
        Setter for property: (bool) ShowHandle
          the ShowHandle  
            
         
        """
        pass
    
    ## Getter for property: (int) SnapPointTypesOnByDefault
    ##   the SnapPointTypesOnByDefault  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX9.0.0.  This call can be safely removed as this is now a no-op.  <br> 

    ## @return int
    @property
    def SnapPointTypesOnByDefault(self) -> int:
        """
        Getter for property: (int) SnapPointTypesOnByDefault
          the SnapPointTypesOnByDefault  
            
         
        """
        pass
    
    ## Setter for property: (int) SnapPointTypesOnByDefault

    ##   the SnapPointTypesOnByDefault  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX9.0.0.  This call can be safely removed as this is now a no-op.  <br> 

    @SnapPointTypesOnByDefault.setter
    def SnapPointTypesOnByDefault(self, point_type: int):
        """
        Setter for property: (int) SnapPointTypesOnByDefault
          the SnapPointTypesOnByDefault  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Units
    ##   the Units  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def Units(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Units
          the Units  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Units

    ##   the Units  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Units.setter
    def Units(self, units: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Units
          the Units  
            
         
        """
        pass
    
    ## Getter for property: (float) Value
    ##   the Value.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return float
    @property
    def Value(self) -> float:
        """
        Getter for property: (float) Value
          the Value.  
            
         
        """
        pass
    
    ## Setter for property: (float) Value

    ##   the Value.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Value.setter
    def Value(self, dimension_value: float):
        """
        Setter for property: (float) Value
          the Value.  
            
         
        """
        pass
    
    ## Getter for property: (bool) WithScale
    ##   the WithScale  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def WithScale(self) -> bool:
        """
        Getter for property: (bool) WithScale
          the WithScale  
            
         
        """
        pass
    
    ## Setter for property: (bool) WithScale

    ##   the WithScale  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @WithScale.setter
    def WithScale(self, with_scale: bool):
        """
        Setter for property: (bool) WithScale
          the WithScale  
            
         
        """
        pass
    
    ##  Gets the BalloonTooltipLayout member 
    ##  @return layout_strings (List[str]): Value to get from the. .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBalloonTooltipLayoutMembers(angular_dim: AngularDimension) -> List[str]:
        """
         Gets the BalloonTooltipLayout member 
         @return layout_strings (List[str]): Value to get from the. .
        """
        pass
    
    ## Tests dimension changed event workflow mapped to this AngularDimension block.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="dimension_value"> (float) </param>
    def TestValueChanged(angular_dim: AngularDimension, dimension_value: float) -> None:
        """
        Tests dimension changed event workflow mapped to this AngularDimension block.
        """
        pass
    
import NXOpen
##  Represents a Dialog 
## 
##   <br>  Created in NX6.0.0  <br> 

class BlockDialog(NXOpen.TransientObject): 
    """ Represents a Dialog """


    ##  Datatype containing options for showing the dialog 
    ##  When the user presses Ok or Apply on the
    ##             dialog, the user's inputs are saved in dialog memory and the next time that the dialog
    ##             is shown in Create mode, the dialog is initialized using the user's previous
    ##             inputs.  
    class DialogMode(Enum):
        """
        Members Include: <Create> <Edit>
        """
        Create: int
        Edit: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> BlockDialog.DialogMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents dialog response values based on navigation button pressed 
    ##  Invalid response. 
    class DialogResponse(Enum):
        """
        Members Include: <Invalid> <Ok> <Cancel> <Back> <Apply>
        """
        Invalid: int
        Ok: int
        Cancel: int
        Back: int
        Apply: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> BlockDialog.DialogResponse:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link CompositeBlock NXOpen.BlockStyler.CompositeBlock@endlink) TopBlock
    ##   a composite block that contains all the blocks in the dialog   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return CompositeBlock
    @property
    def TopBlock(self) -> CompositeBlock:
        """
        Getter for property: (@link CompositeBlock NXOpen.BlockStyler.CompositeBlock@endlink) TopBlock
          a composite block that contains all the blocks in the dialog   
            
         
        """
        pass
    
    ## Apply callback
    ## A callback definition with no input arguments and no return type
    Apply = Callable[[], None]
    
    
    ## Adds Apply callback handler to the dialog. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddApplyHandler(dialog: BlockDialog, apply_cb: BlockDialog.Apply) -> None:
        """
        Adds Apply callback handler to the dialog. 
        """
        pass
    
    ##  Cancel callback 
    ## A callback definition with no input arguments and no return type
    Cancel = Callable[[], None]
    
    
    ## Adds Cancel callback handler to the dialog.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddCancelHandler(dialog: BlockDialog, cancel_cb: BlockDialog.Cancel) -> None:
        """
        Adds Cancel callback handler to the dialog.
        """
        pass
    
    ##  Close callback 
    ## A callback definition with no input arguments and no return type
    Close = Callable[[], None]
    
    
    ## Adds Close callback handler to the dialog.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ##  
    def AddCloseHandler(dialog: BlockDialog, close_cb: BlockDialog.Close) -> None:
        """
        Adds Close callback handler to the dialog.
        """
        pass
    
    ##  Dialog Shown callback 
    ## A callback definition with no input arguments and no return type
    DialogShown = Callable[[], None]
    
    
    ##  Adds Dialog Shown callback handler to the dialog. The callback function is called before the dialog is shown.  The callback can be used to overwrite 
    ##         changes that are made during dialog initialization when user inputs saved in dialog memory are applied to the dialog.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddDialogShownHandler(dialog: BlockDialog, cb: BlockDialog.DialogShown) -> None:
        """
         Adds Dialog Shown callback handler to the dialog. The callback function is called before the dialog is shown.  The callback can be used to overwrite 
                changes that are made during dialog initialization when user inputs saved in dialog memory are applied to the dialog.
        """
        pass
    
    ##  Callback to enable OK and Apply buttons of the dialog. 
    ##         Return True or False to enable or disable the buttons respectively.
    ## A callback definition with no input arguments and no return type
    EnableOKButton = Callable[[], None]
    
    
    ##  Adds enable-ok-button callback handler to the dialog. 
    ## 
    ##   <br>  Created in NX7.5.3  <br> 

    ## License requirements: None.
    ##  
    def AddEnableOKButtonHandler(dialog: BlockDialog, cb: BlockDialog.EnableOKButton) -> None:
        """
         Adds enable-ok-button callback handler to the dialog. 
        """
        pass
    
    ## Filter callback 
    ## A callback definition with the following input arguments: 
    ##  - @link UIBlock NXOpen.BlockStyler.UIBlock@endlink
    ##  - @link NXOpen.TaggedObject NXOpen.TaggedObject@endlink
    ##  and no return type
    Filter = Callable[[UIBlock, NXOpen.TaggedObject], None]
    
    
    ##  Adds Filter callback handler to the dialog. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddFilterHandler(dialog: BlockDialog, cb: BlockDialog.Filter) -> None:
        """
         Adds Filter callback handler to the dialog. 
        """
        pass
    
    ##  @brief Focus notify callback. This is invoked when any selection block on the dialog receives focus. 
    ## 
    ##  
    ## A callback definition with the following input arguments: 
    ##  - @link UIBlock NXOpen.BlockStyler.UIBlock@endlink
    ##  - bool
    ##  and no return type
    FocusNotify = Callable[[UIBlock, bool], None]
    
    
    ##  Adds focus notify callback handler to the dialog. 
    ## 
    ##   <br>  Created in NX6.0.2  <br> 

    ## License requirements: None.
    ##  
    def AddFocusNotifyHandler(dialog: BlockDialog, cb: BlockDialog.FocusNotify) -> None:
        """
         Adds focus notify callback handler to the dialog. 
        """
        pass
    
    ##  Initialize callback 
    ## A callback definition with no input arguments and no return type
    Initialize = Callable[[], None]
    
    
    ##  Adds Initialize callback handler to the dialog. The callback function is called while the dialog is being initialized.  The callback is called before applying any user inputs saved in dialog memory.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddInitializeHandler(dialog: BlockDialog, cb: BlockDialog.Initialize) -> None:
        """
         Adds Initialize callback handler to the dialog. The callback function is called while the dialog is being initialized.  The callback is called before applying any user inputs saved in dialog memory.
        """
        pass
    
    ##  @brief Keyboard focus notify callback. This is invoked when any block having keyboard input such as Integer block receives focus. 
    ## 
    ##   
    ##       
    ## A callback definition with the following input arguments: 
    ##  - @link UIBlock NXOpen.BlockStyler.UIBlock@endlink
    ##  - bool
    ##  and no return type
    KeyboardFocusNotify = Callable[[UIBlock, bool], None]
    
    
    ##  Adds keyboard focus notify callback handler to the dialog. 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  
    def AddKeyboardFocusNotifyHandler(dialog: BlockDialog, cb: BlockDialog.KeyboardFocusNotify) -> None:
        """
         Adds keyboard focus notify callback handler to the dialog. 
        """
        pass
    
    ##  Ok callback
    ## A callback definition with no input arguments and no return type
    Ok = Callable[[], None]
    
    
    ## Adds Ok callback handler to the dialog. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddOkHandler(dialog: BlockDialog, ok_cb: BlockDialog.Ok) -> None:
        """
        Adds Ok callback handler to the dialog. 
        """
        pass
    
    ##  Update callback
    ## A callback definition with the following input arguments: 
    ##  - @link UIBlock NXOpen.BlockStyler.UIBlock@endlink
    ##  and no return type
    Update = Callable[[UIBlock], None]
    
    
    ##  Adds Update callback handler to the dialog. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddUpdateHandler(dialog: BlockDialog, cb: BlockDialog.Update) -> None:
        """
         Adds Update callback handler to the dialog. 
        """
        pass
    
    ##  Frees the object from memory.  After this method is called,
    ##          it is illegal to use the object.  In .NET, this method is automatically
    ##          called when the object is deleted by the garbage collector. 
    ##         
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                 it is illegal to use the object.  In .NET, this method is automatically
                 called when the object is deleted by the garbage collector. 
                
        """
        pass
    
    ##  Gets the properties of a block 
    ##  @return propertyList (@link PropertyList NXOpen.BlockStyler.PropertyList@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## BlockID of the block
    def GetBlockProperties(dialog: BlockDialog, blockName: str) -> PropertyList:
        """
         Gets the properties of a block 
         @return propertyList (@link PropertyList NXOpen.BlockStyler.PropertyList@endlink): .
        """
        pass
    
    ##  Shows the dialog in @link BlockStyler::BlockDialog::DialogModeCreate BlockStyler::BlockDialog::DialogModeCreate@endlink  mode.  This method will not return until the dialog is closed, 
    ##     which typically is when the dialog's navigation buttons are pressed.
    ##  @return dialogResponse (@link BlockDialog.DialogResponse NXOpen.BlockStyler.BlockDialog.DialogResponse@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Launch(dialog: BlockDialog) -> BlockDialog.DialogResponse:
        """
         Shows the dialog in @link BlockStyler::BlockDialog::DialogModeCreate BlockStyler::BlockDialog::DialogModeCreate@endlink  mode.  This method will not return until the dialog is closed, 
            which typically is when the dialog's navigation buttons are pressed.
         @return dialogResponse (@link BlockDialog.DialogResponse NXOpen.BlockStyler.BlockDialog.DialogResponse@endlink): .
        """
        pass
    
    ##  Shows the dialog based upon the mode specified in 
    ##     @link BlockStyler::BlockDialog::DialogMode BlockStyler::BlockDialog::DialogMode@endlink .
    ##     This method will not return until the dialog is closed, which typically is when the dialog's navigation buttons are pressed. 
    ##  @return dialogResponse (@link BlockDialog.DialogResponse NXOpen.BlockStyler.BlockDialog.DialogResponse@endlink): Returns 1: When Ok is pressed. 2: When Cancel is pressed. 3: When Back is pressed. 4: When Apply is pressed.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## Dialog mode as Create or Edit. @link BlockStyler::BlockDialog::DialogMode  BlockStyler::BlockDialog::DialogMode @endlink  
    def LaunchInDialogMode(dialog: BlockDialog, dialogMode: BlockDialog.DialogMode) -> BlockDialog.DialogResponse:
        """
         Shows the dialog based upon the mode specified in 
            @link BlockStyler::BlockDialog::DialogMode BlockStyler::BlockDialog::DialogMode@endlink .
            This method will not return until the dialog is closed, which typically is when the dialog's navigation buttons are pressed. 
         @return dialogResponse (@link BlockDialog.DialogResponse NXOpen.BlockStyler.BlockDialog.DialogResponse@endlink): Returns 1: When Ok is pressed. 2: When Cancel is pressed. 3: When Back is pressed. 4: When Apply is pressed.
        """
        pass
    
    ##  Performs an Apply and restarts the dialog. This invokes the apply callback on the dialog.  This method is meant to be called
    ##     when the dialog is shown and while inside the update callback.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def PerformApply(dialog: BlockDialog) -> None:
        """
         Performs an Apply and restarts the dialog. This invokes the apply callback on the dialog.  This method is meant to be called
            when the dialog is shown and while inside the update callback.
        """
        pass
    
    ##  Registers the reusable block with the dialog 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  Dialog which contains the reusable block  
    def RegisterUserDefinedUIBlock(dialog: BlockDialog, blockDialog: BlockDialog, blockId: str) -> None:
        """
         Registers the reusable block with the dialog 
        """
        pass
    
    ##  Shows the dialog in @link BlockStyler::BlockDialog::DialogModeCreate BlockStyler::BlockDialog::DialogModeCreate@endlink  mode.  This method will not return until the dialog is closed, 
    ##     which typically is when the dialog's OK or Cancel button is pressed.
    ##  @return response (@link NXOpen.Selection.Response NXOpen.Selection.Response@endlink): .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2206.0.0.  Use @link BlockStyler::BlockDialog::Launch BlockStyler::BlockDialog::Launch@endlink  instead  <br> 

    ## License requirements: None.
    ## <param name="dialog"> (@link BlockDialog NXOpen.BlockStyler.BlockDialog@endlink) </param>
    @staticmethod
    @overload
    def Show(self, dialog: BlockDialog) -> NXOpen.Selection.Response:
        """
         Shows the dialog in @link BlockStyler::BlockDialog::DialogModeCreate BlockStyler::BlockDialog::DialogModeCreate@endlink  mode.  This method will not return until the dialog is closed, 
            which typically is when the dialog's OK or Cancel button is pressed.
         @return response (@link NXOpen.Selection.Response NXOpen.Selection.Response@endlink): .
        """
        pass
    
    ##  Shows the dialog based upon the mode specified in 
    ##     @link BlockStyler::BlockDialog::DialogMode BlockStyler::BlockDialog::DialogMode@endlink .
    ##     This method will not return until the dialog is closed, which typically is when the dialog's OK or Cancel button is pressed. 
    ##  @return response (@link NXOpen.Selection.Response NXOpen.Selection.Response@endlink): Returns 1: When Back is pressed. 2: When Cancel is pressed. 3: When Ok or Apply is pressed.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2206.0.0.  Use @link BlockStyler::BlockDialog::LaunchInDialogMode BlockStyler::BlockDialog::LaunchInDialogMode@endlink  instead  <br> 

    ## License requirements: None.
    ## Dialog mode as Create or Edit. @link BlockStyler::BlockDialog::DialogMode  BlockStyler::BlockDialog::DialogMode @endlink  
    @overload
    def Show(self, dialog: BlockDialog, dialogMode: BlockDialog.DialogMode) -> NXOpen.Selection.Response:
        """
         Shows the dialog based upon the mode specified in 
            @link BlockStyler::BlockDialog::DialogMode BlockStyler::BlockDialog::DialogMode@endlink .
            This method will not return until the dialog is closed, which typically is when the dialog's OK or Cancel button is pressed. 
         @return response (@link NXOpen.Selection.Response NXOpen.Selection.Response@endlink): Returns 1: When Back is pressed. 2: When Cancel is pressed. 3: When Ok or Apply is pressed.
        """
        pass
    
import NXOpen
##  Represents a Body Collector block
## 
##   <br>  Created in NX8.5.0  <br> 

class BodyCollector(UIBlock): 
    """ Represents a Body Collector block"""


    ## Getter for property: (bool) AllowConvergentObject
    ##   the AllowConvergentObject  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def AllowConvergentObject(self) -> bool:
        """
        Getter for property: (bool) AllowConvergentObject
          the AllowConvergentObject  
            
         
        """
        pass
    
    ## Setter for property: (bool) AllowConvergentObject

    ##   the AllowConvergentObject  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @AllowConvergentObject.setter
    def AllowConvergentObject(self, allowConvergentObject: bool):
        """
        Setter for property: (bool) AllowConvergentObject
          the AllowConvergentObject  
            
         
        """
        pass
    
    ## Getter for property: (bool) AllowConvergentObjectWithMixedGeometries
    ##   the AllowConvergentObjectWithMixedGeometries  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2007.0.0.  This property is no longer relevant as hybrid selection is default ON now.  <br> 

    ## @return bool
    @property
    def AllowConvergentObjectWithMixedGeometries(self) -> bool:
        """
        Getter for property: (bool) AllowConvergentObjectWithMixedGeometries
          the AllowConvergentObjectWithMixedGeometries  
            
         
        """
        pass
    
    ## Setter for property: (bool) AllowConvergentObjectWithMixedGeometries

    ##   the AllowConvergentObjectWithMixedGeometries  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2007.0.0.  This property is no longer relevant as hybrid selection is default ON now.  <br> 

    @AllowConvergentObjectWithMixedGeometries.setter
    def AllowConvergentObjectWithMixedGeometries(self, allowConvergentObjectWithMixedGeometries: bool):
        """
        Setter for property: (bool) AllowConvergentObjectWithMixedGeometries
          the AllowConvergentObjectWithMixedGeometries  
            
         
        """
        pass
    
    ## Getter for property: (bool) AutomaticProgression
    ##   the AutomaticProgression  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def AutomaticProgression(self) -> bool:
        """
        Getter for property: (bool) AutomaticProgression
          the AutomaticProgression  
            
         
        """
        pass
    
    ## Setter for property: (bool) AutomaticProgression

    ##   the AutomaticProgression  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @AutomaticProgression.setter
    def AutomaticProgression(self, automaticProgression: bool):
        """
        Setter for property: (bool) AutomaticProgression
          the AutomaticProgression  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipImage
    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipImage

    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipLayoutAsString
    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipLayoutAsString

    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipText
    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipText

    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Getter for property: (str) Bitmap
    ##   the Bitmap  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Bitmap(self) -> str:
        """
        Getter for property: (str) Bitmap
          the Bitmap  
            
         
        """
        pass
    
    ## Setter for property: (str) Bitmap

    ##   the Bitmap  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Bitmap.setter
    def Bitmap(self, bitmap_string: str):
        """
        Setter for property: (str) Bitmap
          the Bitmap  
            
         
        """
        pass
    
    ## Getter for property: (bool) BlendVirtualCurveOverlay
    ##   the BlendVirtualCurveOverlay  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def BlendVirtualCurveOverlay(self) -> bool:
        """
        Getter for property: (bool) BlendVirtualCurveOverlay
          the BlendVirtualCurveOverlay  
            
         
        """
        pass
    
    ## Setter for property: (bool) BlendVirtualCurveOverlay

    ##   the BlendVirtualCurveOverlay  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BlendVirtualCurveOverlay.setter
    def BlendVirtualCurveOverlay(self, blendCurve: bool):
        """
        Setter for property: (bool) BlendVirtualCurveOverlay
          the BlendVirtualCurveOverlay  
            
         
        """
        pass
    
    ## Getter for property: (int) BodyRules
    ##   the BodyRules  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def BodyRules(self) -> int:
        """
        Getter for property: (int) BodyRules
          the BodyRules  
            
         
        """
        pass
    
    ## Setter for property: (int) BodyRules

    ##   the BodyRules  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BodyRules.setter
    def BodyRules(self, bodyRules: int):
        """
        Setter for property: (int) BodyRules
          the BodyRules  
            
         
        """
        pass
    
    ## Getter for property: (bool) CreateInterpartLink
    ##   the CreateInterpartLink  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def CreateInterpartLink(self) -> bool:
        """
        Getter for property: (bool) CreateInterpartLink
          the CreateInterpartLink  
            
         
        """
        pass
    
    ## Setter for property: (bool) CreateInterpartLink

    ##   the CreateInterpartLink  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @CreateInterpartLink.setter
    def CreateInterpartLink(self, createLink: bool):
        """
        Setter for property: (bool) CreateInterpartLink
          the CreateInterpartLink  
            
         
        """
        pass
    
    ## Getter for property: (str) Cue
    ##   the Cue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Cue(self) -> str:
        """
        Getter for property: (str) Cue
          the Cue  
            
         
        """
        pass
    
    ## Setter for property: (str) Cue

    ##   the Cue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Cue.setter
    def Cue(self, cue: str):
        """
        Setter for property: (str) Cue
          the Cue  
            
         
        """
        pass
    
    ## Getter for property: (str) DefaultBodyRulesAsString
    ##   the DefaultBodyRules as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def DefaultBodyRulesAsString(self) -> str:
        """
        Getter for property: (str) DefaultBodyRulesAsString
          the DefaultBodyRules as string  
            
         
        """
        pass
    
    ## Setter for property: (str) DefaultBodyRulesAsString

    ##   the DefaultBodyRules as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @DefaultBodyRulesAsString.setter
    def DefaultBodyRulesAsString(self, enumString: str):
        """
        Setter for property: (str) DefaultBodyRulesAsString
          the DefaultBodyRules as string  
            
         
        """
        pass
    
    ## Getter for property: (int) EntityType
    ##   the EntityType  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def EntityType(self) -> int:
        """
        Getter for property: (int) EntityType
          the EntityType  
            
         
        """
        pass
    
    ## Setter for property: (int) EntityType

    ##   the EntityType  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @EntityType.setter
    def EntityType(self, entityType: int):
        """
        Setter for property: (int) EntityType
          the EntityType  
            
         
        """
        pass
    
    ## Getter for property: (bool) IncludeSheetBodies
    ##   the IncludeSheetBodies  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def IncludeSheetBodies(self) -> bool:
        """
        Getter for property: (bool) IncludeSheetBodies
          the IncludeSheetBodies  
            
         
        """
        pass
    
    ## Setter for property: (bool) IncludeSheetBodies

    ##   the IncludeSheetBodies  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @IncludeSheetBodies.setter
    def IncludeSheetBodies(self, includeSheetBodies: bool):
        """
        Setter for property: (bool) IncludeSheetBodies
          the IncludeSheetBodies  
            
         
        """
        pass
    
    ## Getter for property: (str) InterpartSelectionAsString
    ##   the InterpartSelection as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def InterpartSelectionAsString(self) -> str:
        """
        Getter for property: (str) InterpartSelectionAsString
          the InterpartSelection as string  
            
         
        """
        pass
    
    ## Setter for property: (str) InterpartSelectionAsString

    ##   the InterpartSelection as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @InterpartSelectionAsString.setter
    def InterpartSelectionAsString(self, enumString: str):
        """
        Setter for property: (str) InterpartSelectionAsString
          the InterpartSelection as string  
            
         
        """
        pass
    
    ## Getter for property: (str) LabelString
    ##   the LabelString  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
          the LabelString  
            
         
        """
        pass
    
    ## Setter for property: (str) LabelString

    ##   the LabelString  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
          the LabelString  
            
         
        """
        pass
    
    ## Getter for property: (str) MaximumScopeAsString
    ##   the MaximumScope  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return str
    @property
    def MaximumScopeAsString(self) -> str:
        """
        Getter for property: (str) MaximumScopeAsString
          the MaximumScope  
            
         
        """
        pass
    
    ## Setter for property: (str) MaximumScopeAsString

    ##   the MaximumScope  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @MaximumScopeAsString.setter
    def MaximumScopeAsString(self, enumString: str):
        """
        Setter for property: (str) MaximumScopeAsString
          the MaximumScope  
            
         
        """
        pass
    
    ## Getter for property: (bool) PopupMenuEnabled
    ##   the PopupMenuEnabled.  
    ##   
    ##         If true, displays the popup menu for the body.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def PopupMenuEnabled(self) -> bool:
        """
        Getter for property: (bool) PopupMenuEnabled
          the PopupMenuEnabled.  
          
                If true, displays the popup menu for the body.  
         
        """
        pass
    
    ## Setter for property: (bool) PopupMenuEnabled

    ##   the PopupMenuEnabled.  
    ##   
    ##         If true, displays the popup menu for the body.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @PopupMenuEnabled.setter
    def PopupMenuEnabled(self, enabled: bool):
        """
        Setter for property: (bool) PopupMenuEnabled
          the PopupMenuEnabled.  
          
                If true, displays the popup menu for the body.  
         
        """
        pass
    
    ## Getter for property: (str) SelectModeAsString
    ##   the SelectMode as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def SelectModeAsString(self) -> str:
        """
        Getter for property: (str) SelectModeAsString
          the SelectMode as string  
            
         
        """
        pass
    
    ## Setter for property: (str) SelectModeAsString

    ##   the SelectMode as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @SelectModeAsString.setter
    def SelectModeAsString(self, enumString: str):
        """
        Setter for property: (str) SelectModeAsString
          the SelectMode as string  
            
         
        """
        pass
    
    ## Getter for property: (str) StepStatusAsString
    ##   the StepStatus as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
          the StepStatus as string  
            
         
        """
        pass
    
    ## Setter for property: (str) StepStatusAsString

    ##   the StepStatus as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
          the StepStatus as string  
            
         
        """
        pass
    
    ## Getter for property: (str) ToolTip
    ##   the ToolTip  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def ToolTip(self) -> str:
        """
        Getter for property: (str) ToolTip
          the ToolTip  
            
         
        """
        pass
    
    ## Setter for property: (str) ToolTip

    ##   the ToolTip  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ToolTip.setter
    def ToolTip(self, toolTip: str):
        """
        Setter for property: (str) ToolTip
          the ToolTip  
            
         
        """
        pass
    
    ##  Gets the BalloonTooltipLayout member 
    ##  @return layout_strings (List[str]): Value to get from the property. .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBalloonTooltipLayoutMembers(bodyCollector: BodyCollector) -> List[str]:
        """
         Gets the BalloonTooltipLayout member 
         @return layout_strings (List[str]): Value to get from the property. .
        """
        pass
    
    ##  Get the collector object
    ##  @return collectorObject (@link NXOpen.ScCollector NXOpen.ScCollector@endlink): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetCollectorObjectOfBodyCollector(bodyCollector: BodyCollector) -> NXOpen.ScCollector:
        """
         Get the collector object
         @return collectorObject (@link NXOpen.ScCollector NXOpen.ScCollector@endlink): .
        """
        pass
    
    ##  Gets the DefaultBodyRules members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetDefaultBodyRulesMembers(bodyCollector: BodyCollector) -> List[str]:
        """
         Gets the DefaultBodyRules members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Gets the InterpartSelection members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetInterpartSelectionMembers(bodyCollector: BodyCollector) -> List[str]:
        """
         Gets the InterpartSelection members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Gets the SelectMode members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectModeMembers(bodyCollector: BodyCollector) -> List[str]:
        """
         Gets the SelectMode members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Gets the SelectedObjects
    ##  @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectedObjects(bodyCollector: BodyCollector) -> List[NXOpen.TaggedObject]:
        """
         Gets the SelectedObjects
         @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
        """
        pass
    
    ##  Gets the StepStatus members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStepStatusMembers(bodyCollector: BodyCollector) -> List[str]:
        """
         Gets the StepStatus members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Sets the collector object
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="collectorObject"> (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) </param>
    def SetCollectorObjectOfBodyCollector(bodyCollector: BodyCollector, collectorObject: NXOpen.ScCollector) -> None:
        """
         Sets the collector object
        """
        pass
    
    ##  Sets the SelectedObjects
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## Value to set for the property
    def SetSelectedObjects(bodyCollector: BodyCollector, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the SelectedObjects
        """
        pass
    
    ##  Tests the selection for this block. The block must be in focus to call this API
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ##  
    def TestSelection(bodyCollector: BodyCollector, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Tests the selection for this block. The block must be in focus to call this API
        """
        pass
    
##  Represents a button
## 
##   <br>  Created in NX8.5.0  <br> 

class Button(UIBlock): 
    """ Represents a button"""


    ## Getter for property: (str) BalloonTooltipImage
    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipImage

    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipLayoutAsString
    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipLayoutAsString

    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipText
    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipText

    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Getter for property: (str) Bitmap
    ##   the Bitmap  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Bitmap(self) -> str:
        """
        Getter for property: (str) Bitmap
          the Bitmap  
            
         
        """
        pass
    
    ## Setter for property: (str) Bitmap

    ##   the Bitmap  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Bitmap.setter
    def Bitmap(self, bitmap_string: str):
        """
        Setter for property: (str) Bitmap
          the Bitmap  
            
         
        """
        pass
    
    ## Getter for property: (bool) HighQualityBitmap
    ##   the HighQualityBitmap  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def HighQualityBitmap(self) -> bool:
        """
        Getter for property: (bool) HighQualityBitmap
          the HighQualityBitmap  
            
         
        """
        pass
    
    ## Setter for property: (bool) HighQualityBitmap

    ##   the HighQualityBitmap  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @HighQualityBitmap.setter
    def HighQualityBitmap(self, high_quality: bool):
        """
        Setter for property: (bool) HighQualityBitmap
          the HighQualityBitmap  
            
         
        """
        pass
    
    ## Getter for property: (bool) Localize
    ##   the Localize  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def Localize(self) -> bool:
        """
        Getter for property: (bool) Localize
          the Localize  
            
         
        """
        pass
    
    ## Setter for property: (bool) Localize

    ##   the Localize  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Localize.setter
    def Localize(self, localize: bool):
        """
        Setter for property: (bool) Localize
          the Localize  
            
         
        """
        pass
    
    ## Getter for property: (str) Tooltip
    ##   the Tooltip  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Tooltip(self) -> str:
        """
        Getter for property: (str) Tooltip
          the Tooltip  
            
         
        """
        pass
    
    ## Setter for property: (str) Tooltip

    ##   the Tooltip  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Tooltip.setter
    def Tooltip(self, tooltip_string: str):
        """
        Setter for property: (str) Tooltip
          the Tooltip  
            
         
        """
        pass
    
    ##  Gets the BalloonTooltipLayout member 
    ##  @return layout_strings (List[str]): Value to get for given name. .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBalloonTooltipLayoutMembers(button: Button) -> List[str]:
        """
         Gets the BalloonTooltipLayout member 
         @return layout_strings (List[str]): Value to get for given name. .
        """
        pass
    
    ## Tests action event workflow mapped to this Button block.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    @staticmethod
    def TestAction(button: Button) -> None:
        """
        Tests action event workflow mapped to this Button block.
        """
        pass
    
import NXOpen
##  Represents Choose Expression block
## 
##   <br>  Created in NX8.5.0  <br> 

class ChooseExpression(UIBlock): 
    """ Represents Choose Expression block"""


    ## Getter for property: (str) ExpressionSortTypeAsString
    ##   the ExpressionSortType as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def ExpressionSortTypeAsString(self) -> str:
        """
        Getter for property: (str) ExpressionSortTypeAsString
          the ExpressionSortType as string  
            
         
        """
        pass
    
    ## Setter for property: (str) ExpressionSortTypeAsString

    ##   the ExpressionSortType as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ExpressionSortTypeAsString.setter
    def ExpressionSortTypeAsString(self, enumString: str):
        """
        Setter for property: (str) ExpressionSortTypeAsString
          the ExpressionSortType as string  
            
         
        """
        pass
    
    ## Getter for property: (str) ExpressionTypeIndexAsString
    ##   the ExpressionTypeIndex as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def ExpressionTypeIndexAsString(self) -> str:
        """
        Getter for property: (str) ExpressionTypeIndexAsString
          the ExpressionTypeIndex as string  
            
         
        """
        pass
    
    ## Setter for property: (str) ExpressionTypeIndexAsString

    ##   the ExpressionTypeIndex as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ExpressionTypeIndexAsString.setter
    def ExpressionTypeIndexAsString(self, enumString: str):
        """
        Setter for property: (str) ExpressionTypeIndexAsString
          the ExpressionTypeIndex as string  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) SelectedExpression
    ##   the SelectedExpression  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def SelectedExpression(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) SelectedExpression
          the SelectedExpression  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) SelectedExpression

    ##   the SelectedExpression  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @SelectedExpression.setter
    def SelectedExpression(self, selectedExpression: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) SelectedExpression
          the SelectedExpression  
            
         
        """
        pass
    
    ##  Gets the ExpressionSortType members
    ##  @return member_strings (List[str]): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetExpressionSortTypeMembers(chooseExpression: ChooseExpression) -> List[str]:
        """
         Gets the ExpressionSortType members
         @return member_strings (List[str]): .
        """
        pass
    
    ##  Gets the ExpressionTypeIndex members
    ##  @return member_strings (List[str]): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetExpressionTypeIndexMembers(chooseExpression: ChooseExpression) -> List[str]:
        """
         Gets the ExpressionTypeIndex members
         @return member_strings (List[str]): .
        """
        pass
    
    ## Tests expression selected.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="selectedExpression"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def TestExpressionSelected(chooseExpression: ChooseExpression, selectedExpression: NXOpen.TaggedObject) -> None:
        """
        Tests expression selected.
        """
        pass
    
import NXOpen
##  A composite block is a block that contains other blocks 
## 
##   <br>  Created in NX6.0.0  <br> 

class CompositeBlock(UIBlock): 
    """ A composite block is a block that contains other blocks """


    ## Getter for property: (str) Cue
    ##   the Cue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Cue(self) -> str:
        """
        Getter for property: (str) Cue
          the Cue  
            
         
        """
        pass
    
    ## Setter for property: (str) Cue

    ##   the Cue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Cue.setter
    def Cue(self, cue: str):
        """
        Setter for property: (str) Cue
          the Cue  
            
         
        """
        pass
    
    ## Getter for property: (int) DialogSizing
    ##   the Dialog Sizing  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def DialogSizing(self) -> int:
        """
        Getter for property: (int) DialogSizing
          the Dialog Sizing  
            
         
        """
        pass
    
    ## Setter for property: (int) DialogSizing

    ##   the Dialog Sizing  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @DialogSizing.setter
    def DialogSizing(self, enumIndex: int):
        """
        Setter for property: (int) DialogSizing
          the Dialog Sizing  
            
         
        """
        pass
    
    ## Getter for property: (str) DialogSizingAsString
    ##   the Dialog Sizing as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def DialogSizingAsString(self) -> str:
        """
        Getter for property: (str) DialogSizingAsString
          the Dialog Sizing as string  
            
         
        """
        pass
    
    ## Setter for property: (str) DialogSizingAsString

    ##   the Dialog Sizing as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @DialogSizingAsString.setter
    def DialogSizingAsString(self, enumString: str):
        """
        Setter for property: (str) DialogSizingAsString
          the Dialog Sizing as string  
            
         
        """
        pass
    
    ## Getter for property: (@link UIBlock NXOpen.BlockStyler.UIBlock@endlink) LastUpdated
    ##   the block contained in the composite block that was last updated.  
    ##   
    ##     For example, if the CompositeBlock is an item contained in a SetList and
    ##     your update handler is notified that the CompositeBlock has been updated,
    ##     this method returns which block inside the CompositeBlock has been updated.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return UIBlock
    @property
    def LastUpdated(self) -> UIBlock:
        """
        Getter for property: (@link UIBlock NXOpen.BlockStyler.UIBlock@endlink) LastUpdated
          the block contained in the composite block that was last updated.  
          
            For example, if the CompositeBlock is an item contained in a SetList and
            your update handler is notified that the CompositeBlock has been updated,
            this method returns which block inside the CompositeBlock has been updated.   
         
        """
        pass
    
    ## Getter for property: (int) NavigationStyle
    ##   the Navigation Style  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def NavigationStyle(self) -> int:
        """
        Getter for property: (int) NavigationStyle
          the Navigation Style  
            
         
        """
        pass
    
    ## Getter for property: (str) NavigationStyleAsString
    ##   the Navigation Style as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def NavigationStyleAsString(self) -> str:
        """
        Getter for property: (str) NavigationStyleAsString
          the Navigation Style as string  
            
         
        """
        pass
    
    ##  Finds a block contained in the composite block. Returns NULL if block not present
    ##  @return block (@link UIBlock NXOpen.BlockStyler.UIBlock@endlink):  .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  Block name 
    def FindBlock(dialog: CompositeBlock, block_name: str) -> UIBlock:
        """
         Finds a block contained in the composite block. Returns NULL if block not present
         @return block (@link UIBlock NXOpen.BlockStyler.UIBlock@endlink):  .
        """
        pass
    
    ##  Gets all the blocks available in the composite block 
    ##  @return block (@link UIBlock List[NXOpen.BlockStyler.UIBlock]@endlink):  .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBlocks(dialog: CompositeBlock) -> List[UIBlock]:
        """
         Gets all the blocks available in the composite block 
         @return block (@link UIBlock List[NXOpen.BlockStyler.UIBlock]@endlink):  .
        """
        pass
    
    ##  Gets the Dialog Sizing members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetDialogSizingMembers(dialog: CompositeBlock) -> List[str]:
        """
         Gets the Dialog Sizing members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Gets the Navigation Style members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetNavigationStyleMembers(dialog: CompositeBlock) -> List[str]:
        """
         Gets the Navigation Style members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Sets the dialog navigation response for testing
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="response"> (@link NXOpen.Selection.DialogResponse NXOpen.Selection.DialogResponse@endlink) </param>
    def SetDialogNavigationResponse(dialog: CompositeBlock, response: NXOpen.Selection.DialogResponse) -> None:
        """
         Sets the dialog navigation response for testing
        """
        pass
    
import NXOpen
##  Represents a Curve Collector
## 
##   <br>  Created in NX8.5.0  <br> 

class CurveCollector(UIBlock): 
    """ Represents a Curve Collector"""


    ## Getter for property: (bool) AllowConvergentObject
    ##   the AllowConvergentObject  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def AllowConvergentObject(self) -> bool:
        """
        Getter for property: (bool) AllowConvergentObject
          the AllowConvergentObject  
            
         
        """
        pass
    
    ## Setter for property: (bool) AllowConvergentObject

    ##   the AllowConvergentObject  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @AllowConvergentObject.setter
    def AllowConvergentObject(self, allowConvergentObject: bool):
        """
        Setter for property: (bool) AllowConvergentObject
          the AllowConvergentObject  
            
         
        """
        pass
    
    ## Getter for property: (bool) AllowConvergentObjectWithMixedGeometries
    ##   the AllowConvergentObjectWithMixedGeometries  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2007.0.0.  This property is no longer relevant as hybrid selection is default ON now.  <br> 

    ## @return bool
    @property
    def AllowConvergentObjectWithMixedGeometries(self) -> bool:
        """
        Getter for property: (bool) AllowConvergentObjectWithMixedGeometries
          the AllowConvergentObjectWithMixedGeometries  
            
         
        """
        pass
    
    ## Setter for property: (bool) AllowConvergentObjectWithMixedGeometries

    ##   the AllowConvergentObjectWithMixedGeometries  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2007.0.0.  This property is no longer relevant as hybrid selection is default ON now.  <br> 

    @AllowConvergentObjectWithMixedGeometries.setter
    def AllowConvergentObjectWithMixedGeometries(self, allowConvergentObjectWithMixedGeometries: bool):
        """
        Setter for property: (bool) AllowConvergentObjectWithMixedGeometries
          the AllowConvergentObjectWithMixedGeometries  
            
         
        """
        pass
    
    ## Getter for property: (bool) AllowInferredCurveSelection
    ##   the AllowInferredCurveSelection  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def AllowInferredCurveSelection(self) -> bool:
        """
        Getter for property: (bool) AllowInferredCurveSelection
          the AllowInferredCurveSelection  
            
         
        """
        pass
    
    ## Setter for property: (bool) AllowInferredCurveSelection

    ##   the AllowInferredCurveSelection  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @AllowInferredCurveSelection.setter
    def AllowInferredCurveSelection(self, allow: bool):
        """
        Setter for property: (bool) AllowInferredCurveSelection
          the AllowInferredCurveSelection  
            
         
        """
        pass
    
    ## Getter for property: (bool) AutomaticProgression
    ##   the AutomaticProgression  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def AutomaticProgression(self) -> bool:
        """
        Getter for property: (bool) AutomaticProgression
          the AutomaticProgression  
            
         
        """
        pass
    
    ## Setter for property: (bool) AutomaticProgression

    ##   the AutomaticProgression  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @AutomaticProgression.setter
    def AutomaticProgression(self, automaticProgression: bool):
        """
        Setter for property: (bool) AutomaticProgression
          the AutomaticProgression  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipImage
    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipImage

    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipLayoutAsString
    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipLayoutAsString

    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipText
    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipText

    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Getter for property: (str) Bitmap
    ##   the Bitmap  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Bitmap(self) -> str:
        """
        Getter for property: (str) Bitmap
          the Bitmap  
            
         
        """
        pass
    
    ## Setter for property: (str) Bitmap

    ##   the Bitmap  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Bitmap.setter
    def Bitmap(self, bitmap_string: str):
        """
        Setter for property: (str) Bitmap
          the Bitmap  
            
         
        """
        pass
    
    ## Getter for property: (bool) BlendVirtualCurveOverlay
    ##   the BlendVirtualCurveOverlay  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def BlendVirtualCurveOverlay(self) -> bool:
        """
        Getter for property: (bool) BlendVirtualCurveOverlay
          the BlendVirtualCurveOverlay  
            
         
        """
        pass
    
    ## Setter for property: (bool) BlendVirtualCurveOverlay

    ##   the BlendVirtualCurveOverlay  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BlendVirtualCurveOverlay.setter
    def BlendVirtualCurveOverlay(self, blendCurve: bool):
        """
        Setter for property: (bool) BlendVirtualCurveOverlay
          the BlendVirtualCurveOverlay  
            
         
        """
        pass
    
    ## Getter for property: (bool) CreateInterpartLink
    ##   the CreateInterpartLink  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def CreateInterpartLink(self) -> bool:
        """
        Getter for property: (bool) CreateInterpartLink
          the CreateInterpartLink  
            
         
        """
        pass
    
    ## Setter for property: (bool) CreateInterpartLink

    ##   the CreateInterpartLink  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @CreateInterpartLink.setter
    def CreateInterpartLink(self, createLink: bool):
        """
        Setter for property: (bool) CreateInterpartLink
          the CreateInterpartLink  
            
         
        """
        pass
    
    ## Getter for property: (str) Cue
    ##   the Cue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Cue(self) -> str:
        """
        Getter for property: (str) Cue
          the Cue  
            
         
        """
        pass
    
    ## Setter for property: (str) Cue

    ##   the Cue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Cue.setter
    def Cue(self, cue: str):
        """
        Setter for property: (str) Cue
          the Cue  
            
         
        """
        pass
    
    ## Getter for property: (int) CurveRules
    ##   the CurveRules  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def CurveRules(self) -> int:
        """
        Getter for property: (int) CurveRules
          the CurveRules  
            
         
        """
        pass
    
    ## Setter for property: (int) CurveRules

    ##   the CurveRules  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @CurveRules.setter
    def CurveRules(self, curveRules: int):
        """
        Setter for property: (int) CurveRules
          the CurveRules  
            
         
        """
        pass
    
    ## Getter for property: (str) DefaultCurveRulesAsString
    ##   the DefaultCurveRules as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def DefaultCurveRulesAsString(self) -> str:
        """
        Getter for property: (str) DefaultCurveRulesAsString
          the DefaultCurveRules as string  
            
         
        """
        pass
    
    ## Setter for property: (str) DefaultCurveRulesAsString

    ##   the DefaultCurveRules as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @DefaultCurveRulesAsString.setter
    def DefaultCurveRulesAsString(self, enumString: str):
        """
        Setter for property: (str) DefaultCurveRulesAsString
          the DefaultCurveRules as string  
            
         
        """
        pass
    
    ## Getter for property: (int) EntityType
    ##   the EntityType  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def EntityType(self) -> int:
        """
        Getter for property: (int) EntityType
          the EntityType  
            
         
        """
        pass
    
    ## Setter for property: (int) EntityType

    ##   the EntityType  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @EntityType.setter
    def EntityType(self, entityType: int):
        """
        Setter for property: (int) EntityType
          the EntityType  
            
         
        """
        pass
    
    ## Getter for property: (bool) InferredCurveSelection
    ##   the InferredCurveSelection  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def InferredCurveSelection(self) -> bool:
        """
        Getter for property: (bool) InferredCurveSelection
          the InferredCurveSelection  
            
         
        """
        pass
    
    ## Setter for property: (bool) InferredCurveSelection

    ##   the InferredCurveSelection  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @InferredCurveSelection.setter
    def InferredCurveSelection(self, selectInferredCurve: bool):
        """
        Setter for property: (bool) InferredCurveSelection
          the InferredCurveSelection  
            
         
        """
        pass
    
    ## Getter for property: (str) InterpartSelectionAsString
    ##   the InterpartSelection as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def InterpartSelectionAsString(self) -> str:
        """
        Getter for property: (str) InterpartSelectionAsString
          the InterpartSelection as string  
            
         
        """
        pass
    
    ## Setter for property: (str) InterpartSelectionAsString

    ##   the InterpartSelection as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @InterpartSelectionAsString.setter
    def InterpartSelectionAsString(self, enumString: str):
        """
        Setter for property: (str) InterpartSelectionAsString
          the InterpartSelection as string  
            
         
        """
        pass
    
    ## Getter for property: (str) LabelString
    ##   the LabelString  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
          the LabelString  
            
         
        """
        pass
    
    ## Setter for property: (str) LabelString

    ##   the LabelString  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
          the LabelString  
            
         
        """
        pass
    
    ## Getter for property: (str) MaximumScopeAsString
    ##   the MaximumScope  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return str
    @property
    def MaximumScopeAsString(self) -> str:
        """
        Getter for property: (str) MaximumScopeAsString
          the MaximumScope  
            
         
        """
        pass
    
    ## Setter for property: (str) MaximumScopeAsString

    ##   the MaximumScope  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @MaximumScopeAsString.setter
    def MaximumScopeAsString(self, enumString: str):
        """
        Setter for property: (str) MaximumScopeAsString
          the MaximumScope  
            
         
        """
        pass
    
    ## Getter for property: (bool) PopupMenuEnabled
    ##   the PopupMenuEnabled  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def PopupMenuEnabled(self) -> bool:
        """
        Getter for property: (bool) PopupMenuEnabled
          the PopupMenuEnabled  
            
         
        """
        pass
    
    ## Setter for property: (bool) PopupMenuEnabled

    ##   the PopupMenuEnabled  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @PopupMenuEnabled.setter
    def PopupMenuEnabled(self, enabled: bool):
        """
        Setter for property: (bool) PopupMenuEnabled
          the PopupMenuEnabled  
            
         
        """
        pass
    
    ## Getter for property: (str) SelectModeAsString
    ##   the SelectMode as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def SelectModeAsString(self) -> str:
        """
        Getter for property: (str) SelectModeAsString
          the SelectMode as string  
            
         
        """
        pass
    
    ## Setter for property: (str) SelectModeAsString

    ##   the SelectMode as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @SelectModeAsString.setter
    def SelectModeAsString(self, enumString: str):
        """
        Setter for property: (str) SelectModeAsString
          the SelectMode as string  
            
         
        """
        pass
    
    ## Getter for property: (str) StepStatusAsString
    ##   the StepStatus as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
          the StepStatus as string  
            
         
        """
        pass
    
    ## Setter for property: (str) StepStatusAsString

    ##   the StepStatus as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
          the StepStatus as string  
            
         
        """
        pass
    
    ## Getter for property: (str) ToolTip
    ##   the ToolTip  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def ToolTip(self) -> str:
        """
        Getter for property: (str) ToolTip
          the ToolTip  
            
         
        """
        pass
    
    ## Setter for property: (str) ToolTip

    ##   the ToolTip  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ToolTip.setter
    def ToolTip(self, toolTip: str):
        """
        Setter for property: (str) ToolTip
          the ToolTip  
            
         
        """
        pass
    
    ##  Gets the BalloonTooltipLayout members 
    ##  @return layout_strings (List[str]): Value to get from the property. .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBalloonTooltipLayoutMembers(curveCollector: CurveCollector) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         @return layout_strings (List[str]): Value to get from the property. .
        """
        pass
    
    ##  Get the collector object
    ##  @return collectorObject (@link NXOpen.ScCollector NXOpen.ScCollector@endlink): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetCollectorObjectOfCurveCollector(curveCollector: CurveCollector) -> NXOpen.ScCollector:
        """
         Get the collector object
         @return collectorObject (@link NXOpen.ScCollector NXOpen.ScCollector@endlink): .
        """
        pass
    
    ##  Gets the DefaultCurveRules members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetDefaultCurveRulesMembers(curveCollector: CurveCollector) -> List[str]:
        """
         Gets the DefaultCurveRules members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Gets the InterpartSelection members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetInterpartSelectionMembers(curveCollector: CurveCollector) -> List[str]:
        """
         Gets the InterpartSelection members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Gets the SelectMode members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectModeMembers(curveCollector: CurveCollector) -> List[str]:
        """
         Gets the SelectMode members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Gets the SelectedObjects
    ##  @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectedObjects(curveCollector: CurveCollector) -> List[NXOpen.TaggedObject]:
        """
         Gets the SelectedObjects
         @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
        """
        pass
    
    ##  Gets the StepStatus members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStepStatusMembers(curveCollector: CurveCollector) -> List[str]:
        """
         Gets the StepStatus members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Set collector object
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="collectorObject"> (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) </param>
    def SetCollectorObjectOfCurveCollector(curveCollector: CurveCollector, collectorObject: NXOpen.ScCollector) -> None:
        """
         Set collector object
        """
        pass
    
    ##  Sets the SelectedObjects
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## Value to set for the property
    def SetSelectedObjects(curveCollector: CurveCollector, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the SelectedObjects
        """
        pass
    
    ##  Tests the selection for this block. The block must be in focus to call this API
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ##  
    def TestSelection(curveCollector: CurveCollector, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Tests the selection for this block. The block must be in focus to call this API
        """
        pass
    
import NXOpen
import NXOpen.MenuBar
##  Represents Block Styler Dialog tester class that contains testing tools for Block Styler Dialogs  <br> To obtain an instance of this class, refer to @link NXOpen::UI  NXOpen::UI @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class DialogTester(NXOpen.Object): 
    """ Represents Block Styler Dialog tester class that contains testing tools for Block Styler Dialogs """


    ##  Returns an object of @link BlockStyler::MessageBoxTester BlockStyler::MessageBoxTester@endlink  class for testing NX Message Boxes. 
    ##  @return message_box_tester (@link MessageBoxTester NXOpen.BlockStyler.MessageBoxTester@endlink): Object of @link BlockStyler::MessageBoxTester BlockStyler::MessageBoxTester@endlink  class.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    @staticmethod
    def GetMessageBoxTester() -> MessageBoxTester:
        """
         Returns an object of @link BlockStyler::MessageBoxTester BlockStyler::MessageBoxTester@endlink  class for testing NX Message Boxes. 
         @return message_box_tester (@link MessageBoxTester NXOpen.BlockStyler.MessageBoxTester@endlink): Object of @link BlockStyler::MessageBoxTester BlockStyler::MessageBoxTester@endlink  class.
        """
        pass
    
    ##  Returns a test step sequence object for a dialog mapped to a dlx file.
    ##  @return test_sequence (@link TestStepSequence NXOpen.BlockStyler.TestStepSequence@endlink): Object of @link BlockStyler::TestStepSequence BlockStyler::TestStepSequence@endlink  class .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ##  Unique dlx file name
    @staticmethod
    def GetTestStepSequence(dialog_name: str) -> TestStepSequence:
        """
         Returns a test step sequence object for a dialog mapped to a dlx file.
         @return test_sequence (@link TestStepSequence NXOpen.BlockStyler.TestStepSequence@endlink): Object of @link BlockStyler::TestStepSequence BlockStyler::TestStepSequence@endlink  class .
        """
        pass
    
    ##  Invokes a menu button action. Could be used for launching a dialog for testing using a menu button.
    ##  @return action_status (bool): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## Object of @link MenuBar::MenuButton MenuBar::MenuButton@endlink  class
    @staticmethod
    def InvokeMenuButtonAction(button: NXOpen.MenuBar.MenuButton) -> bool:
        """
         Invokes a menu button action. Could be used for launching a dialog for testing using a menu button.
         @return action_status (bool): .
        """
        pass
    
##  Represents a Double block
## 
##   <br>  Created in NX8.5.0  <br> 

class DoubleBlock(UIBlock): 
    """ Represents a Double block"""


    ## Getter for property: (bool) AdaptiveScaleLimits
    ##   the AdaptiveScaleLimits  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def AdaptiveScaleLimits(self) -> bool:
        """
        Getter for property: (bool) AdaptiveScaleLimits
          the AdaptiveScaleLimits  
            
         
        """
        pass
    
    ## Setter for property: (bool) AdaptiveScaleLimits

    ##   the AdaptiveScaleLimits  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @AdaptiveScaleLimits.setter
    def AdaptiveScaleLimits(self, scale_limits: bool):
        """
        Setter for property: (bool) AdaptiveScaleLimits
          the AdaptiveScaleLimits  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipImage
    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipImage

    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipLayoutAsString
    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipLayoutAsString

    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipText
    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipText

    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Getter for property: (str) Bitmap
    ##   the Bitmap  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Bitmap(self) -> str:
        """
        Getter for property: (str) Bitmap
          the Bitmap  
            
         
        """
        pass
    
    ## Setter for property: (str) Bitmap

    ##   the Bitmap  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Bitmap.setter
    def Bitmap(self, bitmap_string: str):
        """
        Setter for property: (str) Bitmap
          the Bitmap  
            
         
        """
        pass
    
    ## Getter for property: (float) Increment
    ##   the Increment  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return float
    @property
    def Increment(self) -> float:
        """
        Getter for property: (float) Increment
          the Increment  
            
         
        """
        pass
    
    ## Setter for property: (float) Increment

    ##   the Increment  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Increment.setter
    def Increment(self, increment: float):
        """
        Setter for property: (float) Increment
          the Increment  
            
         
        """
        pass
    
    ## Getter for property: (float) LineIncrement
    ##   the LineIncrement  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return float
    @property
    def LineIncrement(self) -> float:
        """
        Getter for property: (float) LineIncrement
          the LineIncrement  
            
         
        """
        pass
    
    ## Setter for property: (float) LineIncrement

    ##   the LineIncrement  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @LineIncrement.setter
    def LineIncrement(self, line_increment: float):
        """
        Setter for property: (float) LineIncrement
          the LineIncrement  
            
         
        """
        pass
    
    ## Getter for property: (bool) Localize
    ##   the Localize  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def Localize(self) -> bool:
        """
        Getter for property: (bool) Localize
          the Localize  
            
         
        """
        pass
    
    ## Setter for property: (bool) Localize

    ##   the Localize  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Localize.setter
    def Localize(self, localize: bool):
        """
        Setter for property: (bool) Localize
          the Localize  
            
         
        """
        pass
    
    ## Getter for property: (bool) MaxInclusive
    ##   the MaxInclusive  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def MaxInclusive(self) -> bool:
        """
        Getter for property: (bool) MaxInclusive
          the MaxInclusive  
            
         
        """
        pass
    
    ## Setter for property: (bool) MaxInclusive

    ##   the MaxInclusive  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MaxInclusive.setter
    def MaxInclusive(self, max_inclusive: bool):
        """
        Setter for property: (bool) MaxInclusive
          the MaxInclusive  
            
         
        """
        pass
    
    ## Getter for property: (float) MaximumValue
    ##   the MaximumValue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return float
    @property
    def MaximumValue(self) -> float:
        """
        Getter for property: (float) MaximumValue
          the MaximumValue  
            
         
        """
        pass
    
    ## Setter for property: (float) MaximumValue

    ##   the MaximumValue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MaximumValue.setter
    def MaximumValue(self, max_value: float):
        """
        Setter for property: (float) MaximumValue
          the MaximumValue  
            
         
        """
        pass
    
    ## Getter for property: (bool) MinInclusive
    ##   the MinInclusive  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def MinInclusive(self) -> bool:
        """
        Getter for property: (bool) MinInclusive
          the MinInclusive  
            
         
        """
        pass
    
    ## Setter for property: (bool) MinInclusive

    ##   the MinInclusive  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MinInclusive.setter
    def MinInclusive(self, min_inclusive: bool):
        """
        Setter for property: (bool) MinInclusive
          the MinInclusive  
            
         
        """
        pass
    
    ## Getter for property: (float) MinimumValue
    ##   the MinimumValue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return float
    @property
    def MinimumValue(self) -> float:
        """
        Getter for property: (float) MinimumValue
          the MinimumValue  
            
         
        """
        pass
    
    ## Setter for property: (float) MinimumValue

    ##   the MinimumValue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MinimumValue.setter
    def MinimumValue(self, min_value: float):
        """
        Setter for property: (float) MinimumValue
          the MinimumValue  
            
         
        """
        pass
    
    ## Getter for property: (float) PageIncrement
    ##   the PageIncrement  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return float
    @property
    def PageIncrement(self) -> float:
        """
        Getter for property: (float) PageIncrement
          the PageIncrement  
            
         
        """
        pass
    
    ## Setter for property: (float) PageIncrement

    ##   the PageIncrement  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @PageIncrement.setter
    def PageIncrement(self, page_increment: float):
        """
        Setter for property: (float) PageIncrement
          the PageIncrement  
            
         
        """
        pass
    
    ## Getter for property: (str) PresentationStyleAsString
    ##   the PresentationStyle as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def PresentationStyleAsString(self) -> str:
        """
        Getter for property: (str) PresentationStyleAsString
          the PresentationStyle as string  
            
         
        """
        pass
    
    ## Setter for property: (str) PresentationStyleAsString

    ##   the PresentationStyle as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @PresentationStyleAsString.setter
    def PresentationStyleAsString(self, enumString: str):
        """
        Setter for property: (str) PresentationStyleAsString
          the PresentationStyle as string  
            
         
        """
        pass
    
    ## Getter for property: (bool) ReadOnlyValue
    ##   the ReadOnlyValue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ReadOnlyValue(self) -> bool:
        """
        Getter for property: (bool) ReadOnlyValue
          the ReadOnlyValue  
            
         
        """
        pass
    
    ## Setter for property: (bool) ReadOnlyValue

    ##   the ReadOnlyValue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ReadOnlyValue.setter
    def ReadOnlyValue(self, read_only: bool):
        """
        Setter for property: (bool) ReadOnlyValue
          the ReadOnlyValue  
            
         
        """
        pass
    
    ## Getter for property: (bool) RetainValue
    ##   the RetainValue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def RetainValue(self) -> bool:
        """
        Getter for property: (bool) RetainValue
          the RetainValue  
            
         
        """
        pass
    
    ## Setter for property: (bool) RetainValue

    ##   the RetainValue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @RetainValue.setter
    def RetainValue(self, retain: bool):
        """
        Setter for property: (bool) RetainValue
          the RetainValue  
            
         
        """
        pass
    
    ## Getter for property: (bool) ScaleLimits
    ##   the ScaleLimits  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ScaleLimits(self) -> bool:
        """
        Getter for property: (bool) ScaleLimits
          the ScaleLimits  
            
         
        """
        pass
    
    ## Setter for property: (bool) ScaleLimits

    ##   the ScaleLimits  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ScaleLimits.setter
    def ScaleLimits(self, scale_limits: bool):
        """
        Setter for property: (bool) ScaleLimits
          the ScaleLimits  
            
         
        """
        pass
    
    ## Getter for property: (str) ScaleMaxLimitLabel
    ##   the ScaleMaxLimitLabel  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def ScaleMaxLimitLabel(self) -> str:
        """
        Getter for property: (str) ScaleMaxLimitLabel
          the ScaleMaxLimitLabel  
            
         
        """
        pass
    
    ## Setter for property: (str) ScaleMaxLimitLabel

    ##   the ScaleMaxLimitLabel  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ScaleMaxLimitLabel.setter
    def ScaleMaxLimitLabel(self, max_limit_label: str):
        """
        Setter for property: (str) ScaleMaxLimitLabel
          the ScaleMaxLimitLabel  
            
         
        """
        pass
    
    ## Getter for property: (str) ScaleMinLimitLabel
    ##   the ScaleMinLimitLabel  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def ScaleMinLimitLabel(self) -> str:
        """
        Getter for property: (str) ScaleMinLimitLabel
          the ScaleMinLimitLabel  
            
         
        """
        pass
    
    ## Setter for property: (str) ScaleMinLimitLabel

    ##   the ScaleMinLimitLabel  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ScaleMinLimitLabel.setter
    def ScaleMinLimitLabel(self, min_limit_label: str):
        """
        Setter for property: (str) ScaleMinLimitLabel
          the ScaleMinLimitLabel  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowScaleValue
    ##   the ShowScaleValue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowScaleValue(self) -> bool:
        """
        Getter for property: (bool) ShowScaleValue
          the ShowScaleValue  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowScaleValue

    ##   the ShowScaleValue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowScaleValue.setter
    def ShowScaleValue(self, show_value: bool):
        """
        Setter for property: (bool) ShowScaleValue
          the ShowScaleValue  
            
         
        """
        pass
    
    ## Getter for property: (bool) TitleVisibility
    ##   the TitleVisibility  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def TitleVisibility(self) -> bool:
        """
        Getter for property: (bool) TitleVisibility
          the TitleVisibility  
            
         
        """
        pass
    
    ## Setter for property: (bool) TitleVisibility

    ##   the TitleVisibility  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @TitleVisibility.setter
    def TitleVisibility(self, visibility: bool):
        """
        Setter for property: (bool) TitleVisibility
          the TitleVisibility  
            
         
        """
        pass
    
    ## Getter for property: (float) Value
    ##   the Value  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return float
    @property
    def Value(self) -> float:
        """
        Getter for property: (float) Value
          the Value  
            
         
        """
        pass
    
    ## Setter for property: (float) Value

    ##   the Value  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Value.setter
    def Value(self, double_value: float):
        """
        Setter for property: (float) Value
          the Value  
            
         
        """
        pass
    
    ## Getter for property: (bool) WrapSpin
    ##   the WrapSpin  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def WrapSpin(self) -> bool:
        """
        Getter for property: (bool) WrapSpin
          the WrapSpin  
            
         
        """
        pass
    
    ## Setter for property: (bool) WrapSpin

    ##   the WrapSpin  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @WrapSpin.setter
    def WrapSpin(self, wrap_spin: bool):
        """
        Setter for property: (bool) WrapSpin
          the WrapSpin  
            
         
        """
        pass
    
    ##  Gets the BalloonTooltipLayout member 
    ##  @return layout_strings (List[str]): Value to get from the proprty. .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBalloonTooltipLayoutMembers(double_block: DoubleBlock) -> List[str]:
        """
         Gets the BalloonTooltipLayout member 
         @return layout_strings (List[str]): Value to get from the proprty. .
        """
        pass
    
    ##  Gets the ComboOptions
    ##  @return option_value (List[float]): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetComboOptions(double_block: DoubleBlock) -> List[float]:
        """
         Gets the ComboOptions
         @return option_value (List[float]): .
        """
        pass
    
    ##  Gets the PresentationStyle members 
    ##  @return member_strings (List[str]): Value to get for the property. .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPresentationStyleMembers(double_block: DoubleBlock) -> List[str]:
        """
         Gets the PresentationStyle members 
         @return member_strings (List[str]): Value to get for the property. .
        """
        pass
    
    ##  Sets the ComboOptions
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="option_value"> (List[float]) </param>
    def SetComboOptions(double_block: DoubleBlock, option_value: List[float]) -> None:
        """
         Sets the ComboOptions
        """
        pass
    
    ## Tests value changed event workflow mapped to this DoubleBlock block.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="double_value"> (float) </param>
    def TestValueChanged(double_block: DoubleBlock, double_value: float) -> None:
        """
        Tests value changed event workflow mapped to this DoubleBlock block.
        """
        pass
    
##  Represents a Double Table block
## 
##   <br>  Created in NX8.5.0  <br> 

class DoubleTable(UIBlock): 
    """ Represents a Double Table block"""


    ## Getter for property: (int) CellWidth
    ##   the CellWidth  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def CellWidth(self) -> int:
        """
        Getter for property: (int) CellWidth
          the CellWidth  
            
         
        """
        pass
    
    ## Setter for property: (int) CellWidth

    ##   the CellWidth  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @CellWidth.setter
    def CellWidth(self, cell_width: int):
        """
        Setter for property: (int) CellWidth
          the CellWidth  
            
         
        """
        pass
    
    ## Getter for property: (float) Increment
    ##   the Increment.  
    ##    Use this property only when Spin is true  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return float
    @property
    def Increment(self) -> float:
        """
        Getter for property: (float) Increment
          the Increment.  
           Use this property only when Spin is true  
         
        """
        pass
    
    ## Setter for property: (float) Increment

    ##   the Increment.  
    ##    Use this property only when Spin is true  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Increment.setter
    def Increment(self, increment: float):
        """
        Setter for property: (float) Increment
          the Increment.  
           Use this property only when Spin is true  
         
        """
        pass
    
    ## Getter for property: (bool) RetainValue
    ##   the RetainValue.  
    ##    If true, indicates that the values in the block would be stored in dialog memory upon OK, Apply or Close.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def RetainValue(self) -> bool:
        """
        Getter for property: (bool) RetainValue
          the RetainValue.  
           If true, indicates that the values in the block would be stored in dialog memory upon OK, Apply or Close.   
         
        """
        pass
    
    ## Setter for property: (bool) RetainValue

    ##   the RetainValue.  
    ##    If true, indicates that the values in the block would be stored in dialog memory upon OK, Apply or Close.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @RetainValue.setter
    def RetainValue(self, retain: bool):
        """
        Setter for property: (bool) RetainValue
          the RetainValue.  
           If true, indicates that the values in the block would be stored in dialog memory upon OK, Apply or Close.   
         
        """
        pass
    
    ## Getter for property: (bool) Spin
    ##   the Spin  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def Spin(self) -> bool:
        """
        Getter for property: (bool) Spin
          the Spin  
            
         
        """
        pass
    
    ## Setter for property: (bool) Spin

    ##   the Spin  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Spin.setter
    def Spin(self, spin: bool):
        """
        Setter for property: (bool) Spin
          the Spin  
            
         
        """
        pass
    
    ## Getter for property: (bool) WrapSpin
    ##   the WrapSpin.  
    ##    Use this property only when Spin is true  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def WrapSpin(self) -> bool:
        """
        Getter for property: (bool) WrapSpin
          the WrapSpin.  
           Use this property only when Spin is true  
         
        """
        pass
    
    ## Setter for property: (bool) WrapSpin

    ##   the WrapSpin.  
    ##    Use this property only when Spin is true  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @WrapSpin.setter
    def WrapSpin(self, wrap_spin: bool):
        """
        Setter for property: (bool) WrapSpin
          the WrapSpin.  
           Use this property only when Spin is true  
         
        """
        pass
    
    ##  Gets the Column Titles
    ##  @return column_titles (List[str]): Column Title values to get from the property. .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetColumnTitles(double_table: DoubleTable) -> List[str]:
        """
         Gets the Column Titles
         @return column_titles (List[str]): Column Title values to get from the property. .
        """
        pass
    
    ##  Gets the MaximumValues
    ##  @return A tuple consisting of (matrixValue, nRows, nColumns). 
    ##  - matrixValue is: List[float].Value to get from the property. .
    ##  - nRows is: int. Number of Rows in the 2D matrix .
    ##  - nColumns is: int. Number of Columns in the 2D matrix .

    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetMaximumValues(double_table: DoubleTable) -> Tuple[List[float], int, int]:
        """
         Gets the MaximumValues
         @return A tuple consisting of (matrixValue, nRows, nColumns). 
         - matrixValue is: List[float].Value to get from the property. .
         - nRows is: int. Number of Rows in the 2D matrix .
         - nColumns is: int. Number of Columns in the 2D matrix .

        """
        pass
    
    ##  Gets the MinimumValues
    ##  @return A tuple consisting of (matrixValue, nRows, nColumns). 
    ##  - matrixValue is: List[float].Value to get from the property .
    ##  - nRows is: int. Number of Rows in the 2D matrix .
    ##  - nColumns is: int. Number of Columns in the 2D matrix .

    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetMinimumValues(double_table: DoubleTable) -> Tuple[List[float], int, int]:
        """
         Gets the MinimumValues
         @return A tuple consisting of (matrixValue, nRows, nColumns). 
         - matrixValue is: List[float].Value to get from the property .
         - nRows is: int. Number of Rows in the 2D matrix .
         - nColumns is: int. Number of Columns in the 2D matrix .

        """
        pass
    
    ##  Gets the titles of rows in table
    ##  @return row_title (List[str]): Value to get from the property. .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetRowTitles(double_table: DoubleTable) -> List[str]:
        """
         Gets the titles of rows in table
         @return row_title (List[str]): Value to get from the property. .
        """
        pass
    
    ##  Gets the Values in table
    ##  @return A tuple consisting of (matrixValue, nRows, nColumns). 
    ##  - matrixValue is: List[float].Value to get from the property. .
    ##  - nRows is: int. Number of Rows in the 2D matrix .
    ##  - nColumns is: int. Number of Columns in the 2D matrix .

    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetValues(double_table: DoubleTable) -> Tuple[List[float], int, int]:
        """
         Gets the Values in table
         @return A tuple consisting of (matrixValue, nRows, nColumns). 
         - matrixValue is: List[float].Value to get from the property. .
         - nRows is: int. Number of Rows in the 2D matrix .
         - nColumns is: int. Number of Columns in the 2D matrix .

        """
        pass
    
    ##  Sets the Column Titles
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ## Column Title values to set for the property. 
    def SetColumnTitles(double_table: DoubleTable, column_titles: List[str]) -> None:
        """
         Sets the Column Titles
        """
        pass
    
    ##  Sets the MaximumValues
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ##  Number of Rows in the 2D matrix 
    def SetMaximumValues(double_table: DoubleTable, nRows: int, nColumns: int, matrixValue: List[float]) -> None:
        """
         Sets the MaximumValues
        """
        pass
    
    ##  Sets the MinimumValues
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ##  Number of Rows in the 2D matrix 
    def SetMinimumValues(double_table: DoubleTable, nRows: int, nColumns: int, matrixValue: List[float]) -> None:
        """
         Sets the MinimumValues
        """
        pass
    
    ##  Sets the titles of rows in table
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## Value to set for the property. 
    def SetRowTitles(double_table: DoubleTable, row_title: List[str]) -> None:
        """
         Sets the titles of rows in table
        """
        pass
    
    ##  Sets the Values in table
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ##  Number of Rows in the 2D matrix 
    def SetValues(double_table: DoubleTable, nRows: int, nColumns: int, matrixValue: List[float]) -> None:
        """
         Sets the Values in table
        """
        pass
    
    ## Tests value changed event workflow mapped to this DoubleTable block.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ##  Number of Rows in the 2D matrix 
    def TestValueChanged(double_table: DoubleTable, nRows: int, nColumns: int, matrixValue: List[float]) -> None:
        """
        Tests value changed event workflow mapped to this DoubleTable block.
        """
        pass
    
##  Represents a Drawing Area block
## 
##   <br>  Created in NX8.5.0  <br> 

class DrawingArea(UIBlock): 
    """ Represents a Drawing Area block"""


    ## Getter for property: (int) Height
    ##   the Height  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def Height(self) -> int:
        """
        Getter for property: (int) Height
          the Height  
            
         
        """
        pass
    
    ## Setter for property: (int) Height

    ##   the Height  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Height.setter
    def Height(self, height: int):
        """
        Setter for property: (int) Height
          the Height  
            
         
        """
        pass
    
    ## Getter for property: (str) Image
    ##   the Image  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Image(self) -> str:
        """
        Getter for property: (str) Image
          the Image  
            
         
        """
        pass
    
    ## Setter for property: (str) Image

    ##   the Image  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Image.setter
    def Image(self, image_string: str):
        """
        Setter for property: (str) Image
          the Image  
            
         
        """
        pass
    
    ## Getter for property: (int) Width
    ##   the Width  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def Width(self) -> int:
        """
        Getter for property: (int) Width
          the Width  
            
         
        """
        pass
    
    ## Setter for property: (int) Width

    ##   the Width  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Width.setter
    def Width(self, width: int):
        """
        Setter for property: (int) Width
          the Width  
            
         
        """
        pass
    
##  Represents an Enumeration block
## 
##   <br>  Created in NX8.5.0  <br> 

class Enumeration(UIBlock): 
    """ Represents an Enumeration block"""


    ## Getter for property: (bool) AllowShortcuts
    ##   the AllowShortcuts.  
    ##   
    ##         If true, the 'Show Shortcuts' option is available.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def AllowShortcuts(self) -> bool:
        """
        Getter for property: (bool) AllowShortcuts
          the AllowShortcuts.  
          
                If true, the 'Show Shortcuts' option is available.  
         
        """
        pass
    
    ## Setter for property: (bool) AllowShortcuts

    ##   the AllowShortcuts.  
    ##   
    ##         If true, the 'Show Shortcuts' option is available.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @AllowShortcuts.setter
    def AllowShortcuts(self, allow: bool):
        """
        Setter for property: (bool) AllowShortcuts
          the AllowShortcuts.  
          
                If true, the 'Show Shortcuts' option is available.  
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipLayoutAsString
    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipLayoutAsString

    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipText
    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return str
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipText

    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Getter for property: (bool) BorderVisibility
    ##   the BorderVisibility  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def BorderVisibility(self) -> bool:
        """
        Getter for property: (bool) BorderVisibility
          the BorderVisibility  
            
         
        """
        pass
    
    ## Setter for property: (bool) BorderVisibility

    ##   the BorderVisibility  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BorderVisibility.setter
    def BorderVisibility(self, visibility: bool):
        """
        Setter for property: (bool) BorderVisibility
          the BorderVisibility  
            
         
        """
        pass
    
    ## Getter for property: (bool) HighQualityBitmap
    ##   the HighQualityBitmap  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def HighQualityBitmap(self) -> bool:
        """
        Getter for property: (bool) HighQualityBitmap
          the HighQualityBitmap  
            
         
        """
        pass
    
    ## Setter for property: (bool) HighQualityBitmap

    ##   the HighQualityBitmap  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @HighQualityBitmap.setter
    def HighQualityBitmap(self, high_quality: bool):
        """
        Setter for property: (bool) HighQualityBitmap
          the HighQualityBitmap  
            
         
        """
        pass
    
    ## Getter for property: (bool) IconsOnly
    ##   the IconsOnly.  
    ##   
    ##         If true, the enumeration options are shown as bitmaps only   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def IconsOnly(self) -> bool:
        """
        Getter for property: (bool) IconsOnly
          the IconsOnly.  
          
                If true, the enumeration options are shown as bitmaps only   
         
        """
        pass
    
    ## Setter for property: (bool) IconsOnly

    ##   the IconsOnly.  
    ##   
    ##         If true, the enumeration options are shown as bitmaps only   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @IconsOnly.setter
    def IconsOnly(self, icons_only: bool):
        """
        Setter for property: (bool) IconsOnly
          the IconsOnly.  
          
                If true, the enumeration options are shown as bitmaps only   
         
        """
        pass
    
    ## Getter for property: (bool) LabelVisibility
    ##   the LabelVisibility  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def LabelVisibility(self) -> bool:
        """
        Getter for property: (bool) LabelVisibility
          the LabelVisibility  
            
         
        """
        pass
    
    ## Setter for property: (bool) LabelVisibility

    ##   the LabelVisibility  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @LabelVisibility.setter
    def LabelVisibility(self, visibility: bool):
        """
        Setter for property: (bool) LabelVisibility
          the LabelVisibility  
            
         
        """
        pass
    
    ## Getter for property: (str) LayoutAsString
    ##   the Layout as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def LayoutAsString(self) -> str:
        """
        Getter for property: (str) LayoutAsString
          the Layout as string  
            
         
        """
        pass
    
    ## Setter for property: (str) LayoutAsString

    ##   the Layout as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @LayoutAsString.setter
    def LayoutAsString(self, enumString: str):
        """
        Setter for property: (str) LayoutAsString
          the Layout as string  
            
         
        """
        pass
    
    ## Getter for property: (bool) Localize
    ##   the Localize.  
    ##   
    ##         If true, the Label is translated to current locale language.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def Localize(self) -> bool:
        """
        Getter for property: (bool) Localize
          the Localize.  
          
                If true, the Label is translated to current locale language.  
         
        """
        pass
    
    ## Setter for property: (bool) Localize

    ##   the Localize.  
    ##   
    ##         If true, the Label is translated to current locale language.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Localize.setter
    def Localize(self, localize: bool):
        """
        Setter for property: (bool) Localize
          the Localize.  
          
                If true, the Label is translated to current locale language.  
         
        """
        pass
    
    ## Getter for property: (int) NumberOfColumns
    ##   the NumberOfColumns  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def NumberOfColumns(self) -> int:
        """
        Getter for property: (int) NumberOfColumns
          the NumberOfColumns  
            
         
        """
        pass
    
    ## Setter for property: (int) NumberOfColumns

    ##   the NumberOfColumns  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @NumberOfColumns.setter
    def NumberOfColumns(self, num_column: int):
        """
        Setter for property: (int) NumberOfColumns
          the NumberOfColumns  
            
         
        """
        pass
    
    ## Getter for property: (bool) PackedColumns
    ##   the PackedColumns.  
    ##   
    ##         If true, each column takes up as much space as required for labels in that column. If false,
    ##         the longest label amongst all options dictates the width of all columns.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def PackedColumns(self) -> bool:
        """
        Getter for property: (bool) PackedColumns
          the PackedColumns.  
          
                If true, each column takes up as much space as required for labels in that column. If false,
                the longest label amongst all options dictates the width of all columns.  
         
        """
        pass
    
    ## Setter for property: (bool) PackedColumns

    ##   the PackedColumns.  
    ##   
    ##         If true, each column takes up as much space as required for labels in that column. If false,
    ##         the longest label amongst all options dictates the width of all columns.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @PackedColumns.setter
    def PackedColumns(self, packed_columns: bool):
        """
        Setter for property: (bool) PackedColumns
          the PackedColumns.  
          
                If true, each column takes up as much space as required for labels in that column. If false,
                the longest label amongst all options dictates the width of all columns.  
         
        """
        pass
    
    ## Getter for property: (str) PresentationStyleAsString
    ##   the PresentationStyle as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def PresentationStyleAsString(self) -> str:
        """
        Getter for property: (str) PresentationStyleAsString
          the PresentationStyle as string  
            
         
        """
        pass
    
    ## Setter for property: (str) PresentationStyleAsString

    ##   the PresentationStyle as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @PresentationStyleAsString.setter
    def PresentationStyleAsString(self, enumString: str):
        """
        Setter for property: (str) PresentationStyleAsString
          the PresentationStyle as string  
            
         
        """
        pass
    
    ## Getter for property: (bool) RetainValue
    ##   the RetainValue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def RetainValue(self) -> bool:
        """
        Getter for property: (bool) RetainValue
          the RetainValue  
            
         
        """
        pass
    
    ## Setter for property: (bool) RetainValue

    ##   the RetainValue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @RetainValue.setter
    def RetainValue(self, retain: bool):
        """
        Setter for property: (bool) RetainValue
          the RetainValue  
            
         
        """
        pass
    
    ## Getter for property: (str) ValueAsString
    ##   the Value as string.  
    ##   
    ##         Represents the currently selected option of enum.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def ValueAsString(self) -> str:
        """
        Getter for property: (str) ValueAsString
          the Value as string.  
          
                Represents the currently selected option of enum.  
         
        """
        pass
    
    ## Setter for property: (str) ValueAsString

    ##   the Value as string.  
    ##   
    ##         Represents the currently selected option of enum.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ValueAsString.setter
    def ValueAsString(self, enumString: str):
        """
        Setter for property: (str) ValueAsString
          the Value as string.  
          
                Represents the currently selected option of enum.  
         
        """
        pass
    
    ##  Gets the BalloonTooltipImages
    ##  @return image_strings (List[str]): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBalloonTooltipImages(enumeration: Enumeration) -> List[str]:
        """
         Gets the BalloonTooltipImages
         @return image_strings (List[str]): .
        """
        pass
    
    ##  Gets the BalloonTooltipLayout members 
    ##  @return layout_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBalloonTooltipLayoutMembers(enumeration: Enumeration) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         @return layout_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Gets the BalloonTooltipTexts
    ##  @return tooltip_text_array (List[str]): Value to get from the property .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBalloonTooltipTexts(enumeration: Enumeration) -> List[str]:
        """
         Gets the BalloonTooltipTexts
         @return tooltip_text_array (List[str]): Value to get from the property .
        """
        pass
    
    ##  Gets the Bitmaps
    ##  @return bitmaps_strings (List[str]): Value to get for the property. .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBitmaps(enumeration: Enumeration) -> List[str]:
        """
         Gets the Bitmaps
         @return bitmaps_strings (List[str]): Value to get for the property. .
        """
        pass
    
    ## Gets the Enum members.
    ##  @return member_strings (List[str]): Array of member names.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetEnumMembers(enumeration: Enumeration) -> List[str]:
        """
        Gets the Enum members.
         @return member_strings (List[str]): Array of member names.
        """
        pass
    
    ##  Gets EnumSensitivity
    ##  @return value_vector (List[int]):  Array of integers with the value 0 or 1. If 1 then the corresponding enum member is sensitive otherwise it is insensitive. .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetEnumSensitivity(enumeration: Enumeration) -> List[int]:
        """
         Gets EnumSensitivity
         @return value_vector (List[int]):  Array of integers with the value 0 or 1. If 1 then the corresponding enum member is sensitive otherwise it is insensitive. .
        """
        pass
    
    ##  Gets EnumVisibility
    ##  @return value_vector (List[int]):  Array of integers with the value 0 or 1. If 1 then the corresponding enum member is visible otherwise it is hidden. .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetEnumVisibility(enumeration: Enumeration) -> List[int]:
        """
         Gets EnumVisibility
         @return value_vector (List[int]):  Array of integers with the value 0 or 1. If 1 then the corresponding enum member is visible otherwise it is hidden. .
        """
        pass
    
    ##  Gets InitialShortcuts.
    ##         Specifies the set of shortcuts that are displayed when the dialog is initially shown. Valid only if AllowShortcuts property is true. 
    ##  @return value_vector (List[int]):  Array of integers with length between 0 and N-1, where N is the number of enumeration options .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetInitialShortcuts(enumeration: Enumeration) -> List[int]:
        """
         Gets InitialShortcuts.
                Specifies the set of shortcuts that are displayed when the dialog is initially shown. Valid only if AllowShortcuts property is true. 
         @return value_vector (List[int]):  Array of integers with length between 0 and N-1, where N is the number of enumeration options .
        """
        pass
    
    ##  Gets the Layout members 
    ##  @return layout_strings (List[str]): Value to get from the property .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetLayoutMembers(enumeration: Enumeration) -> List[str]:
        """
         Gets the Layout members 
         @return layout_strings (List[str]): Value to get from the property .
        """
        pass
    
    ##  Gets the PresentationStyle members 
    ##  @return member_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPresentationStyleMembers(enumeration: Enumeration) -> List[str]:
        """
         Gets the PresentationStyle members 
         @return member_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Sets the BalloonTooltipImages
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="image_strings"> (List[str]) </param>
    def SetBalloonTooltipImages(enumeration: Enumeration, image_strings: List[str]) -> None:
        """
         Sets the BalloonTooltipImages
        """
        pass
    
    ##  Sets the BalloonTooltipTexts
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## Value to set for the property. 
    def SetBalloonTooltipTexts(enumeration: Enumeration, tooltip_text_array: List[str]) -> None:
        """
         Sets the BalloonTooltipTexts
        """
        pass
    
    ##  Sets the Bitmaps
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## Value to set for the property. 
    def SetBitmaps(enumeration: Enumeration, bitmaps_strings: List[str]) -> None:
        """
         Sets the Bitmaps
        """
        pass
    
    ## Sets the Enum members.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## Array of member names
    def SetEnumMembers(enumeration: Enumeration, member_strings: List[str]) -> None:
        """
        Sets the Enum members.
        """
        pass
    
    ##  Sets EnumSensitivity
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ##  Array of integers with the value 0 or 1. If 1 then the corresponding enum member is sensitive otherwise it is insensitive. 
    def SetEnumSensitivity(enumeration: Enumeration, value_vector: List[int]) -> None:
        """
         Sets EnumSensitivity
        """
        pass
    
    ##  Sets EnumVisibility
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ##  Array of integers with the value 0 or 1. If 1 then the corresponding enum member is visible otherwise it is hidden. 
    def SetEnumVisibility(enumeration: Enumeration, value_vector: List[int]) -> None:
        """
         Sets EnumVisibility
        """
        pass
    
    ##  Sets InitialShortcuts.
    ##         Specifies the set of shortcuts that are displayed when the dialog is initially shown. Valid only if AllowShortcuts property is true.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ##  Array of integers with length between 0 and N-1, where N is the number of enumeration options 
    def SetInitialShortcuts(enumeration: Enumeration, value_vector: List[int]) -> None:
        """
         Sets InitialShortcuts.
                Specifies the set of shortcuts that are displayed when the dialog is initially shown. Valid only if AllowShortcuts property is true.
        """
        pass
    
    ## Tests value changed event workflow mapped to this Enumeration block.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="enumString"> (str) </param>
    def TestValueChanged(enumeration: Enumeration, enumString: str) -> None:
        """
        Tests value changed event workflow mapped to this Enumeration block.
        """
        pass
    
##  Represents an Explorer block.  The Explorer block allows for collecting a large number of inputs into a single dialog.
##     The inputs are organized into nodes and sub-nodes on a tree to allow for quick and easy navigation.  The Explorer
##     block provides the ability to have up to 5 levels of nodes in the Navigation Tree.  Each node contains groups and
##     individual inputs that are laid out like standard NX dialogs.  When selecting level 1 and level 2 nodes that do not
##     contain any groups and only contain sub-nodes the first sub-node containing groups is highlighted and its content shown.
##  
## 
##   <br>  Created in NX9.0.0  <br> 

class Explorer(UIBlock): 
    """ Represents an Explorer block.  The Explorer block allows for collecting a large number of inputs into a single dialog.
    The inputs are organized into nodes and sub-nodes on a tree to allow for quick and easy navigation.  The Explorer
    block provides the ability to have up to 5 levels of nodes in the Navigation Tree.  Each node contains groups and
    individual inputs that are laid out like standard NX dialogs.  When selecting level 1 and level 2 nodes that do not
    contain any groups and only contain sub-nodes the first sub-node containing groups is highlighted and its content shown.
 """


    ## Getter for property: (int) CurrentNode
    ##   the CurrentNode selected in the Navigation Tree.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def CurrentNode(self) -> int:
        """
        Getter for property: (int) CurrentNode
          the CurrentNode selected in the Navigation Tree.  
             
         
        """
        pass
    
    ## Setter for property: (int) CurrentNode

    ##   the CurrentNode selected in the Navigation Tree.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @CurrentNode.setter
    def CurrentNode(self, currentNode: int):
        """
        Setter for property: (int) CurrentNode
          the CurrentNode selected in the Navigation Tree.  
             
         
        """
        pass
    
    ## Getter for property: (bool) Localize
    ##   the localization of the block label.  
    ##    If the label matches an English string in the NX string
    ##         localization databse and the Localize property is set to true, then the Label is translated
    ##         to the current locale language.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def Localize(self) -> bool:
        """
        Getter for property: (bool) Localize
          the localization of the block label.  
           If the label matches an English string in the NX string
                localization databse and the Localize property is set to true, then the Label is translated
                to the current locale language.   
         
        """
        pass
    
    ## Setter for property: (bool) Localize

    ##   the localization of the block label.  
    ##    If the label matches an English string in the NX string
    ##         localization databse and the Localize property is set to true, then the Label is translated
    ##         to the current locale language.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Localize.setter
    def Localize(self, localize: bool):
        """
        Setter for property: (bool) Localize
          the localization of the block label.  
           If the label matches an English string in the NX string
                localization databse and the Localize property is set to true, then the Label is translated
                to the current locale language.   
         
        """
        pass
    
    ## Getter for property: (@link PropertyList NXOpen.BlockStyler.PropertyList@endlink) Members
    ##   the members.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return PropertyList
    @property
    def Members(self) -> PropertyList:
        """
        Getter for property: (@link PropertyList NXOpen.BlockStyler.PropertyList@endlink) Members
          the members.  
             
         
        """
        pass
    
    ## Getter for property: (int) TreeWidth
    ##   the TreeWidth for the Navigation Tree.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return int
    @property
    def TreeWidth(self) -> int:
        """
        Getter for property: (int) TreeWidth
          the TreeWidth for the Navigation Tree.  
             
         
        """
        pass
    
    ## Setter for property: (int) TreeWidth

    ##   the TreeWidth for the Navigation Tree.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @TreeWidth.setter
    def TreeWidth(self, treeWidth: int):
        """
        Setter for property: (int) TreeWidth
          the TreeWidth for the Navigation Tree.  
             
         
        """
        pass
    
    ##  The NotifyNodeSelectedPost callback notifies a client after navigating to the next node
    ##         in the Explorer.  The nextNode parameter for the callback is zero based and represents
    ##         the nodes in the Explorer. 
    ## A callback definition with the following input arguments: 
    ##  - @link Explorer NXOpen.BlockStyler.Explorer@endlink
    ##  - int
    ##  and no return type
    NotifyNodeSelectedPostCallback = Callable[[Explorer, int], None]
    
    
    ##  The NotifyNodeSelectedPre callback notifies a client before navigating to the next node
    ##         in the Explorer.  The nextNode parameter for the callback is zero based and represents
    ##         the nodes in the Explorer. 
    ## A callback definition with the following input arguments: 
    ##  - @link Explorer NXOpen.BlockStyler.Explorer@endlink
    ##  - int
    ##  and no return type
    NotifyNodeSelectedPreCallback = Callable[[Explorer, int], None]
    
    
    ##  Sets the parent member for the child members in the Explorer Navigation Tree.  The maximum
    ##         Navigation Tree depth is 5 levels.  An exception is thrown if the parent member depth is
    ##         already at the maximum allowed depth. 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ##  Parent member for the child members. 
    def SetChildMembers(explorer: Explorer, parentMember: UIBlock, childMembers: List[UIBlock]) -> None:
        """
         Sets the parent member for the child members in the Explorer Navigation Tree.  The maximum
                Navigation Tree depth is 5 levels.  An exception is thrown if the parent member depth is
                already at the maximum allowed depth. 
        """
        pass
    
    ##  Sets the NotifyNodeSelectedPost handler. 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetNotifyNodeSelectedPostHandler(explorer: Explorer, cb: Explorer.NotifyNodeSelectedPostCallback) -> None:
        """
         Sets the NotifyNodeSelectedPost handler. 
        """
        pass
    
    ##  Sets the NotifyNodeSelectedPre handler. 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetNotifyNodeSelectedPreHandler(explorer: Explorer, cb: Explorer.NotifyNodeSelectedPreCallback) -> None:
        """
         Sets the NotifyNodeSelectedPre handler. 
        """
        pass
    
    ## Tests current node changed.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="currentNode"> (int) </param>
    def TestCurrentNodeChanged(explorer: Explorer, currentNode: int) -> None:
        """
        Tests current node changed.
        """
        pass
    
import NXOpen
##  Represents an Expression block
## 
##   <br>  Created in NX8.5.0  <br> 

class ExpressionBlock(UIBlock): 
    """ Represents an Expression block"""


    ## Getter for property: (bool) AdaptiveScaleLimits
    ##  the AdaptiveScaleLimits.  
    ##   
    ##         If true, indicates that the scale should be adaptive.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def AdaptiveScaleLimits(self) -> bool:
        """
        Getter for property: (bool) AdaptiveScaleLimits
         the AdaptiveScaleLimits.  
          
                If true, indicates that the scale should be adaptive.  
         
        """
        pass
    
    ## Setter for property: (bool) AdaptiveScaleLimits

    ##  the AdaptiveScaleLimits.  
    ##   
    ##         If true, indicates that the scale should be adaptive.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @AdaptiveScaleLimits.setter
    def AdaptiveScaleLimits(self, scale_limits: bool):
        """
        Setter for property: (bool) AdaptiveScaleLimits
         the AdaptiveScaleLimits.  
          
                If true, indicates that the scale should be adaptive.  
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipImage
    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipImage

    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipLayoutAsString
    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipLayoutAsString

    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipText
    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipText

    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Getter for property: (str) DimensionalityAsString
    ##   the  Dimensionality as string.  
    ##    It specifies the type of quantity that the expression represents.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def DimensionalityAsString(self) -> str:
        """
        Getter for property: (str) DimensionalityAsString
          the  Dimensionality as string.  
           It specifies the type of quantity that the expression represents.  
         
        """
        pass
    
    ## Setter for property: (str) DimensionalityAsString

    ##   the  Dimensionality as string.  
    ##    It specifies the type of quantity that the expression represents.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @DimensionalityAsString.setter
    def DimensionalityAsString(self, enum_string: str):
        """
        Setter for property: (str) DimensionalityAsString
          the  Dimensionality as string.  
           It specifies the type of quantity that the expression represents.  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ExpressionObject
    ##   the ExpressionObject  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def ExpressionObject(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ExpressionObject
          the ExpressionObject  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ExpressionObject

    ##   the ExpressionObject  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ExpressionObject.setter
    def ExpressionObject(self, expression_object: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ExpressionObject
          the ExpressionObject  
            
         
        """
        pass
    
    ## Getter for property: (str) Formula
    ##   the Formula for the expression  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Formula(self) -> str:
        """
        Getter for property: (str) Formula
          the Formula for the expression  
            
         
        """
        pass
    
    ## Setter for property: (str) Formula

    ##   the Formula for the expression  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Formula.setter
    def Formula(self, formula_string: str):
        """
        Setter for property: (str) Formula
          the Formula for the expression  
            
         
        """
        pass
    
    ## Getter for property: (bool) HasUnitsMenu
    ##   the HasUnitsMenu.  
    ##    If true, indicates that a menu will be displayed allowing the user to change units.
    ##         This property is relevant only when the Dimensionality property is set to a value that is not without units.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def HasUnitsMenu(self) -> bool:
        """
        Getter for property: (bool) HasUnitsMenu
          the HasUnitsMenu.  
           If true, indicates that a menu will be displayed allowing the user to change units.
                This property is relevant only when the Dimensionality property is set to a value that is not without units.  
         
        """
        pass
    
    ## Setter for property: (bool) HasUnitsMenu

    ##   the HasUnitsMenu.  
    ##    If true, indicates that a menu will be displayed allowing the user to change units.
    ##         This property is relevant only when the Dimensionality property is set to a value that is not without units.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @HasUnitsMenu.setter
    def HasUnitsMenu(self, has_menu: bool):
        """
        Setter for property: (bool) HasUnitsMenu
          the HasUnitsMenu.  
           If true, indicates that a menu will be displayed allowing the user to change units.
                This property is relevant only when the Dimensionality property is set to a value that is not without units.  
         
        """
        pass
    
    ## Getter for property: (float) LineIncrement
    ##  the LineIncrement value.  
    ##   
    ##         Specifies the increment/decrement when the user presses the arrow keys on the keyboard.
    ##         Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def LineIncrement(self) -> float:
        """
        Getter for property: (float) LineIncrement
         the LineIncrement value.  
          
                Specifies the increment/decrement when the user presses the arrow keys on the keyboard.
                Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
         
        """
        pass
    
    ## Setter for property: (float) LineIncrement

    ##  the LineIncrement value.  
    ##   
    ##         Specifies the increment/decrement when the user presses the arrow keys on the keyboard.
    ##         Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @LineIncrement.setter
    def LineIncrement(self, line_increment: float):
        """
        Setter for property: (float) LineIncrement
         the LineIncrement value.  
          
                Specifies the increment/decrement when the user presses the arrow keys on the keyboard.
                Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
         
        """
        pass
    
    ## Getter for property: (bool) MaxInclusive
    ##   the MaxInclusive  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def MaxInclusive(self) -> bool:
        """
        Getter for property: (bool) MaxInclusive
          the MaxInclusive  
            
         
        """
        pass
    
    ## Setter for property: (bool) MaxInclusive

    ##   the MaxInclusive  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MaxInclusive.setter
    def MaxInclusive(self, max_inclusive: bool):
        """
        Setter for property: (bool) MaxInclusive
          the MaxInclusive  
            
         
        """
        pass
    
    ## Getter for property: (float) MaximumValue
    ##   the MaximumValue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return float
    @property
    def MaximumValue(self) -> float:
        """
        Getter for property: (float) MaximumValue
          the MaximumValue  
            
         
        """
        pass
    
    ## Setter for property: (float) MaximumValue

    ##   the MaximumValue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MaximumValue.setter
    def MaximumValue(self, max_value: float):
        """
        Setter for property: (float) MaximumValue
          the MaximumValue  
            
         
        """
        pass
    
    ## Getter for property: (bool) MinInclusive
    ##   the MinInclusive  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def MinInclusive(self) -> bool:
        """
        Getter for property: (bool) MinInclusive
          the MinInclusive  
            
         
        """
        pass
    
    ## Setter for property: (bool) MinInclusive

    ##   the MinInclusive  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MinInclusive.setter
    def MinInclusive(self, min_inclusive: bool):
        """
        Setter for property: (bool) MinInclusive
          the MinInclusive  
            
         
        """
        pass
    
    ## Getter for property: (float) MinimumValue
    ##   the MinimumValue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return float
    @property
    def MinimumValue(self) -> float:
        """
        Getter for property: (float) MinimumValue
          the MinimumValue  
            
         
        """
        pass
    
    ## Setter for property: (float) MinimumValue

    ##   the MinimumValue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MinimumValue.setter
    def MinimumValue(self, min_value: float):
        """
        Setter for property: (float) MinimumValue
          the MinimumValue  
            
         
        """
        pass
    
    ## Getter for property: (float) PageIncrement
    ##  the PageIncrement value.  
    ##   
    ##         Specifies the increment/decrement when the user presses the Page Up or Page Down keys on the keyboard.
    ##         Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def PageIncrement(self) -> float:
        """
        Getter for property: (float) PageIncrement
         the PageIncrement value.  
          
                Specifies the increment/decrement when the user presses the Page Up or Page Down keys on the keyboard.
                Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
         
        """
        pass
    
    ## Setter for property: (float) PageIncrement

    ##  the PageIncrement value.  
    ##   
    ##         Specifies the increment/decrement when the user presses the Page Up or Page Down keys on the keyboard.
    ##         Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @PageIncrement.setter
    def PageIncrement(self, page_increment: float):
        """
        Setter for property: (float) PageIncrement
         the PageIncrement value.  
          
                Specifies the increment/decrement when the user presses the Page Up or Page Down keys on the keyboard.
                Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
         
        """
        pass
    
    ## Getter for property: (bool) RetainUnits
    ##   the RetainUnits.  
    ##    If true, indicates that the units in the block would be stored in dialog memory upon OK, Apply or Close.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def RetainUnits(self) -> bool:
        """
        Getter for property: (bool) RetainUnits
          the RetainUnits.  
           If true, indicates that the units in the block would be stored in dialog memory upon OK, Apply or Close.   
         
        """
        pass
    
    ## Setter for property: (bool) RetainUnits

    ##   the RetainUnits.  
    ##    If true, indicates that the units in the block would be stored in dialog memory upon OK, Apply or Close.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @RetainUnits.setter
    def RetainUnits(self, retain: bool):
        """
        Setter for property: (bool) RetainUnits
          the RetainUnits.  
           If true, indicates that the units in the block would be stored in dialog memory upon OK, Apply or Close.   
         
        """
        pass
    
    ## Getter for property: (bool) RetainValue
    ##   the RetainValue.  
    ##    If true, indicates that the values in the block would be stored in dialog memory upon OK, Apply or Close.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def RetainValue(self) -> bool:
        """
        Getter for property: (bool) RetainValue
          the RetainValue.  
           If true, indicates that the values in the block would be stored in dialog memory upon OK, Apply or Close.   
         
        """
        pass
    
    ## Setter for property: (bool) RetainValue

    ##   the RetainValue.  
    ##    If true, indicates that the values in the block would be stored in dialog memory upon OK, Apply or Close.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @RetainValue.setter
    def RetainValue(self, retain: bool):
        """
        Setter for property: (bool) RetainValue
          the RetainValue.  
           If true, indicates that the values in the block would be stored in dialog memory upon OK, Apply or Close.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Units
    ##   the Units for the expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def Units(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Units
          the Units for the expression   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Units

    ##   the Units for the expression   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Units.setter
    def Units(self, units: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Units
          the Units for the expression   
            
         
        """
        pass
    
    ## Getter for property: (float) Value
    ##   the Value.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return float
    @property
    def Value(self) -> float:
        """
        Getter for property: (float) Value
          the Value.  
            
         
        """
        pass
    
    ## Setter for property: (float) Value

    ##   the Value.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Value.setter
    def Value(self, expression_value: float):
        """
        Setter for property: (float) Value
          the Value.  
            
         
        """
        pass
    
    ## Getter for property: (bool) WithScale
    ##   the WithScale.  
    ##    If true, the slider bar is shown.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def WithScale(self) -> bool:
        """
        Getter for property: (bool) WithScale
          the WithScale.  
           If true, the slider bar is shown.  
         
        """
        pass
    
    ## Setter for property: (bool) WithScale

    ##   the WithScale.  
    ##    If true, the slider bar is shown.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @WithScale.setter
    def WithScale(self, with_scale: bool):
        """
        Setter for property: (bool) WithScale
          the WithScale.  
           If true, the slider bar is shown.  
         
        """
        pass
    
    ##  Gets the BalloonTooltipLayout members 
    ##  @return layout_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBalloonTooltipLayoutMembers(expression: ExpressionBlock) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         @return layout_strings (List[str]): Value to get from the property.
        """
        pass
    
    ## Gets the members of Dimensionality enum.
    ##  @return dimension_strings (List[str]): Value to get from the property. .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetDimensionalityMembers(expression: ExpressionBlock) -> List[str]:
        """
        Gets the members of Dimensionality enum.
         @return dimension_strings (List[str]): Value to get from the property. .
        """
        pass
    
    ## Tests value changed event workflow mapped to this ExpressionBlock block.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="dimension_value"> (float) </param>
    def TestValueChanged(expression: ExpressionBlock, dimension_value: float) -> None:
        """
        Tests value changed event workflow mapped to this ExpressionBlock block.
        """
        pass
    
import NXOpen
##  Represents a Face Collector
## 
##   <br>  Created in NX8.5.0  <br> 

class FaceCollector(UIBlock): 
    """ Represents a Face Collector"""


    ## Getter for property: (bool) AllowConvergentObject
    ##   the AllowConvergentObject  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def AllowConvergentObject(self) -> bool:
        """
        Getter for property: (bool) AllowConvergentObject
          the AllowConvergentObject  
            
         
        """
        pass
    
    ## Setter for property: (bool) AllowConvergentObject

    ##   the AllowConvergentObject  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @AllowConvergentObject.setter
    def AllowConvergentObject(self, allowConvergentObject: bool):
        """
        Setter for property: (bool) AllowConvergentObject
          the AllowConvergentObject  
            
         
        """
        pass
    
    ## Getter for property: (bool) AllowConvergentObjectWithMixedGeometries
    ##   the AllowConvergentObjectWithMixedGeometries  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2007.0.0.  This property is no longer relevant as hybrid selection is default ON now.  <br> 

    ## @return bool
    @property
    def AllowConvergentObjectWithMixedGeometries(self) -> bool:
        """
        Getter for property: (bool) AllowConvergentObjectWithMixedGeometries
          the AllowConvergentObjectWithMixedGeometries  
            
         
        """
        pass
    
    ## Setter for property: (bool) AllowConvergentObjectWithMixedGeometries

    ##   the AllowConvergentObjectWithMixedGeometries  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2007.0.0.  This property is no longer relevant as hybrid selection is default ON now.  <br> 

    @AllowConvergentObjectWithMixedGeometries.setter
    def AllowConvergentObjectWithMixedGeometries(self, allowConvergentObjectWithMixedGeometries: bool):
        """
        Setter for property: (bool) AllowConvergentObjectWithMixedGeometries
          the AllowConvergentObjectWithMixedGeometries  
            
         
        """
        pass
    
    ## Getter for property: (bool) AutomaticProgression
    ##   the AutomaticProgression.  
    ##    If true, focus automatically progresses to the next selection block.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def AutomaticProgression(self) -> bool:
        """
        Getter for property: (bool) AutomaticProgression
          the AutomaticProgression.  
           If true, focus automatically progresses to the next selection block.  
         
        """
        pass
    
    ## Setter for property: (bool) AutomaticProgression

    ##   the AutomaticProgression.  
    ##    If true, focus automatically progresses to the next selection block.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @AutomaticProgression.setter
    def AutomaticProgression(self, automaticProgression: bool):
        """
        Setter for property: (bool) AutomaticProgression
          the AutomaticProgression.  
           If true, focus automatically progresses to the next selection block.  
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipImage
    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipImage

    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipLayoutAsString
    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipLayoutAsString

    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipText
    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipText

    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Getter for property: (str) Bitmap
    ##   the Bitmap  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Bitmap(self) -> str:
        """
        Getter for property: (str) Bitmap
          the Bitmap  
            
         
        """
        pass
    
    ## Setter for property: (str) Bitmap

    ##   the Bitmap  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Bitmap.setter
    def Bitmap(self, bitmap_string: str):
        """
        Setter for property: (str) Bitmap
          the Bitmap  
            
         
        """
        pass
    
    ## Getter for property: (bool) BlendVirtualCurveOverlay
    ##   the BlendVirtualCurveOverlay  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def BlendVirtualCurveOverlay(self) -> bool:
        """
        Getter for property: (bool) BlendVirtualCurveOverlay
          the BlendVirtualCurveOverlay  
            
         
        """
        pass
    
    ## Setter for property: (bool) BlendVirtualCurveOverlay

    ##   the BlendVirtualCurveOverlay  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BlendVirtualCurveOverlay.setter
    def BlendVirtualCurveOverlay(self, blendCurve: bool):
        """
        Setter for property: (bool) BlendVirtualCurveOverlay
          the BlendVirtualCurveOverlay  
            
         
        """
        pass
    
    ## Getter for property: (bool) CreateInterpartLink
    ##   the CreateInterpartLink  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def CreateInterpartLink(self) -> bool:
        """
        Getter for property: (bool) CreateInterpartLink
          the CreateInterpartLink  
            
         
        """
        pass
    
    ## Setter for property: (bool) CreateInterpartLink

    ##   the CreateInterpartLink  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @CreateInterpartLink.setter
    def CreateInterpartLink(self, createLink: bool):
        """
        Setter for property: (bool) CreateInterpartLink
          the CreateInterpartLink  
            
         
        """
        pass
    
    ## Getter for property: (str) Cue
    ##   the Cue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Cue(self) -> str:
        """
        Getter for property: (str) Cue
          the Cue  
            
         
        """
        pass
    
    ## Setter for property: (str) Cue

    ##   the Cue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Cue.setter
    def Cue(self, cue: str):
        """
        Setter for property: (str) Cue
          the Cue  
            
         
        """
        pass
    
    ## Getter for property: (str) DefaultFaceRulesAsString
    ##   the DefaultFaceRules as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def DefaultFaceRulesAsString(self) -> str:
        """
        Getter for property: (str) DefaultFaceRulesAsString
          the DefaultFaceRules as string  
            
         
        """
        pass
    
    ## Setter for property: (str) DefaultFaceRulesAsString

    ##   the DefaultFaceRules as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @DefaultFaceRulesAsString.setter
    def DefaultFaceRulesAsString(self, enumString: str):
        """
        Setter for property: (str) DefaultFaceRulesAsString
          the DefaultFaceRules as string  
            
         
        """
        pass
    
    ## Getter for property: (int) EntityType
    ##   the EntityType  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def EntityType(self) -> int:
        """
        Getter for property: (int) EntityType
          the EntityType  
            
         
        """
        pass
    
    ## Setter for property: (int) EntityType

    ##   the EntityType  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @EntityType.setter
    def EntityType(self, entityType: int):
        """
        Setter for property: (int) EntityType
          the EntityType  
            
         
        """
        pass
    
    ## Getter for property: (int) FaceRules
    ##   the FaceRules  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def FaceRules(self) -> int:
        """
        Getter for property: (int) FaceRules
          the FaceRules  
            
         
        """
        pass
    
    ## Setter for property: (int) FaceRules

    ##   the FaceRules  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @FaceRules.setter
    def FaceRules(self, faceRules: int):
        """
        Setter for property: (int) FaceRules
          the FaceRules  
            
         
        """
        pass
    
    ## Getter for property: (str) InterpartSelectionAsString
    ##   the InterpartSelection as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def InterpartSelectionAsString(self) -> str:
        """
        Getter for property: (str) InterpartSelectionAsString
          the InterpartSelection as string  
            
         
        """
        pass
    
    ## Setter for property: (str) InterpartSelectionAsString

    ##   the InterpartSelection as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @InterpartSelectionAsString.setter
    def InterpartSelectionAsString(self, enumString: str):
        """
        Setter for property: (str) InterpartSelectionAsString
          the InterpartSelection as string  
            
         
        """
        pass
    
    ## Getter for property: (str) LabelString
    ##   the LabelString  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
          the LabelString  
            
         
        """
        pass
    
    ## Setter for property: (str) LabelString

    ##   the LabelString  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
          the LabelString  
            
         
        """
        pass
    
    ## Getter for property: (str) MaximumScopeAsString
    ##   the MaximumScope  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return str
    @property
    def MaximumScopeAsString(self) -> str:
        """
        Getter for property: (str) MaximumScopeAsString
          the MaximumScope  
            
         
        """
        pass
    
    ## Setter for property: (str) MaximumScopeAsString

    ##   the MaximumScope  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @MaximumScopeAsString.setter
    def MaximumScopeAsString(self, enumString: str):
        """
        Setter for property: (str) MaximumScopeAsString
          the MaximumScope  
            
         
        """
        pass
    
    ## Getter for property: (bool) PopupMenuEnabled
    ##   the PopupMenuEnabled  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def PopupMenuEnabled(self) -> bool:
        """
        Getter for property: (bool) PopupMenuEnabled
          the PopupMenuEnabled  
            
         
        """
        pass
    
    ## Setter for property: (bool) PopupMenuEnabled

    ##   the PopupMenuEnabled  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @PopupMenuEnabled.setter
    def PopupMenuEnabled(self, enabled: bool):
        """
        Setter for property: (bool) PopupMenuEnabled
          the PopupMenuEnabled  
            
         
        """
        pass
    
    ## Getter for property: (str) SelectModeAsString
    ##   the SelectMode as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def SelectModeAsString(self) -> str:
        """
        Getter for property: (str) SelectModeAsString
          the SelectMode as string  
            
         
        """
        pass
    
    ## Setter for property: (str) SelectModeAsString

    ##   the SelectMode as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @SelectModeAsString.setter
    def SelectModeAsString(self, enumString: str):
        """
        Setter for property: (str) SelectModeAsString
          the SelectMode as string  
            
         
        """
        pass
    
    ## Getter for property: (str) StepStatusAsString
    ##   the StepStatus as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
          the StepStatus as string  
            
         
        """
        pass
    
    ## Setter for property: (str) StepStatusAsString

    ##   the StepStatus as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
          the StepStatus as string  
            
         
        """
        pass
    
    ## Getter for property: (str) ToolTip
    ##   the ToolTip  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def ToolTip(self) -> str:
        """
        Getter for property: (str) ToolTip
          the ToolTip  
            
         
        """
        pass
    
    ## Setter for property: (str) ToolTip

    ##   the ToolTip  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ToolTip.setter
    def ToolTip(self, toolTip: str):
        """
        Setter for property: (str) ToolTip
          the ToolTip  
            
         
        """
        pass
    
    ##  Gets the BalloonTooltipLayout members 
    ##  @return layout_strings (List[str]): Value to get from the property. .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBalloonTooltipLayoutMembers(faceCollector: FaceCollector) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         @return layout_strings (List[str]): Value to get from the property. .
        """
        pass
    
    ##  Get collector objects
    ##  @return collectorObject (@link NXOpen.ScCollector NXOpen.ScCollector@endlink): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetCollectorObjectOfFaceCollector(faceCollector: FaceCollector) -> NXOpen.ScCollector:
        """
         Get collector objects
         @return collectorObject (@link NXOpen.ScCollector NXOpen.ScCollector@endlink): .
        """
        pass
    
    ##  Gets the DefaultFaceRules members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetDefaultFaceRulesMembers(faceCollector: FaceCollector) -> List[str]:
        """
         Gets the DefaultFaceRules members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Gets the InterpartSelection members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetInterpartSelectionMembers(faceCollector: FaceCollector) -> List[str]:
        """
         Gets the InterpartSelection members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Gets the SelectMode members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectModeMembers(faceCollector: FaceCollector) -> List[str]:
        """
         Gets the SelectMode members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Gets the SelectedObjects
    ##  @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectedObjects(faceCollector: FaceCollector) -> List[NXOpen.TaggedObject]:
        """
         Gets the SelectedObjects
         @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
        """
        pass
    
    ##  Gets the StepStatus members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStepStatusMembers(faceCollector: FaceCollector) -> List[str]:
        """
         Gets the StepStatus members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Set collector objects
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="collectorObject"> (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) </param>
    def SetCollectorObjectOfFaceCollector(faceCollector: FaceCollector, collectorObject: NXOpen.ScCollector) -> None:
        """
         Set collector objects
        """
        pass
    
    ##  Sets the SelectedObjects
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## Value to set for the property
    def SetSelectedObjects(faceCollector: FaceCollector, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the SelectedObjects
        """
        pass
    
    ##  Tests the selection for this block. The block must be in focus to call this API
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ##  
    def TestSelection(faceCollector: FaceCollector, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Tests the selection for this block. The block must be in focus to call this API
        """
        pass
    
##  Represents File Selection With Browse block
## 
##   <br>  Created in NX8.5.0  <br> 

class FileSelection(UIBlock): 
    """ Represents File Selection With Browse block"""


    ## Getter for property: (str) Filter
    ##   the Filter
    ##         Format of the filter string, for a group of related filter extensions will be "Group 1(*.  
    ##   xxx;*.yyy;*.zzz),Group 2(*.aaa;*.bbb)" e.g."EPLAN files(*.emp;*.ema;*.ems),Simulation Files(*.sim;*.fem)".
    ##         For the individual filter extensions ".xxx,.yyy,.zzz" e.g. ".prt,.fem,.sim" will appear as "prt File (*.prt)","sim File (*.sim)" and "fem File (*.fem)" respectively in the "Files of type" of file open dialog.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Filter(self) -> str:
        """
        Getter for property: (str) Filter
          the Filter
                Format of the filter string, for a group of related filter extensions will be "Group 1(*.  
          xxx;*.yyy;*.zzz),Group 2(*.aaa;*.bbb)" e.g."EPLAN files(*.emp;*.ema;*.ems),Simulation Files(*.sim;*.fem)".
                For the individual filter extensions ".xxx,.yyy,.zzz" e.g. ".prt,.fem,.sim" will appear as "prt File (*.prt)","sim File (*.sim)" and "fem File (*.fem)" respectively in the "Files of type" of file open dialog.
                  
         
        """
        pass
    
    ## Setter for property: (str) Filter

    ##   the Filter
    ##         Format of the filter string, for a group of related filter extensions will be "Group 1(*.  
    ##   xxx;*.yyy;*.zzz),Group 2(*.aaa;*.bbb)" e.g."EPLAN files(*.emp;*.ema;*.ems),Simulation Files(*.sim;*.fem)".
    ##         For the individual filter extensions ".xxx,.yyy,.zzz" e.g. ".prt,.fem,.sim" will appear as "prt File (*.prt)","sim File (*.sim)" and "fem File (*.fem)" respectively in the "Files of type" of file open dialog.
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Filter.setter
    def Filter(self, filterString: str):
        """
        Setter for property: (str) Filter
          the Filter
                Format of the filter string, for a group of related filter extensions will be "Group 1(*.  
          xxx;*.yyy;*.zzz),Group 2(*.aaa;*.bbb)" e.g."EPLAN files(*.emp;*.ema;*.ems),Simulation Files(*.sim;*.fem)".
                For the individual filter extensions ".xxx,.yyy,.zzz" e.g. ".prt,.fem,.sim" will appear as "prt File (*.prt)","sim File (*.sim)" and "fem File (*.fem)" respectively in the "Files of type" of file open dialog.
                  
         
        """
        pass
    
    ## Getter for property: (str) Path
    ##   the Path  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Path(self) -> str:
        """
        Getter for property: (str) Path
          the Path  
            
         
        """
        pass
    
    ## Setter for property: (str) Path

    ##   the Path  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Path.setter
    def Path(self, path: str):
        """
        Setter for property: (str) Path
          the Path  
            
         
        """
        pass
    
    ## Getter for property: (bool) RetainStringValue
    ##   the RetainStringValue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def RetainStringValue(self) -> bool:
        """
        Getter for property: (bool) RetainStringValue
          the RetainStringValue  
            
         
        """
        pass
    
    ## Setter for property: (bool) RetainStringValue

    ##   the RetainStringValue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @RetainStringValue.setter
    def RetainStringValue(self, retain_string_value: bool):
        """
        Setter for property: (bool) RetainStringValue
          the RetainStringValue  
            
         
        """
        pass
    
    ## Tests file selected.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="path"> (str) </param>
    def TestPathSelected(fileBrowser: FileSelection, path: str) -> None:
        """
        Tests file selected.
        """
        pass
    
##  Represents Folder Selection With Browse block
## 
##   <br>  Created in NX8.5.0  <br> 

class FolderSelection(UIBlock): 
    """ Represents Folder Selection With Browse block"""


    ## Getter for property: (str) Path
    ##   the Path  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Path(self) -> str:
        """
        Getter for property: (str) Path
          the Path  
            
         
        """
        pass
    
    ## Setter for property: (str) Path

    ##   the Path  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Path.setter
    def Path(self, path: str):
        """
        Setter for property: (str) Path
          the Path  
            
         
        """
        pass
    
    ## Getter for property: (bool) RetainStringValue
    ##   the RetainStringValue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def RetainStringValue(self) -> bool:
        """
        Getter for property: (bool) RetainStringValue
          the RetainStringValue  
            
         
        """
        pass
    
    ## Setter for property: (bool) RetainStringValue

    ##   the RetainStringValue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @RetainStringValue.setter
    def RetainStringValue(self, retain_string_value: bool):
        """
        Setter for property: (bool) RetainStringValue
          the RetainStringValue  
            
         
        """
        pass
    
    ## Tests folder selected.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="path"> (str) </param>
    def TestPathSelected(folderBrowser: FolderSelection, path: str) -> None:
        """
        Tests folder selected.
        """
        pass
    
##  Represents a Group Block
## 
##   <br>  Created in NX8.5.0  <br> 

class Group(UIBlock): 
    """ Represents a Group Block"""


    ## Getter for property: (int) Column
    ##   the Column  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def Column(self) -> int:
        """
        Getter for property: (int) Column
          the Column  
            
         
        """
        pass
    
    ## Setter for property: (int) Column

    ##   the Column  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Column.setter
    def Column(self, num_column: int):
        """
        Setter for property: (int) Column
          the Column  
            
         
        """
        pass
    
    ## Getter for property: (bool) Localize
    ##   the Localize  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def Localize(self) -> bool:
        """
        Getter for property: (bool) Localize
          the Localize  
            
         
        """
        pass
    
    ## Setter for property: (bool) Localize

    ##   the Localize  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Localize.setter
    def Localize(self, localize: bool):
        """
        Setter for property: (bool) Localize
          the Localize  
            
         
        """
        pass
    
    ## Getter for property: (@link PropertyList NXOpen.BlockStyler.PropertyList@endlink) Members
    ##   the Members  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return PropertyList
    @property
    def Members(self) -> PropertyList:
        """
        Getter for property: (@link PropertyList NXOpen.BlockStyler.PropertyList@endlink) Members
          the Members  
            
         
        """
        pass
    
##  Represents a Integer block
## 
##   <br>  Created in NX8.5.0  <br> 

class IntegerBlock(UIBlock): 
    """ Represents a Integer block"""


    ## Getter for property: (bool) AdaptiveScaleLimits
    ##   the AdaptiveScaleLimits  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def AdaptiveScaleLimits(self) -> bool:
        """
        Getter for property: (bool) AdaptiveScaleLimits
          the AdaptiveScaleLimits  
            
         
        """
        pass
    
    ## Setter for property: (bool) AdaptiveScaleLimits

    ##   the AdaptiveScaleLimits  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @AdaptiveScaleLimits.setter
    def AdaptiveScaleLimits(self, scale_limits: bool):
        """
        Setter for property: (bool) AdaptiveScaleLimits
          the AdaptiveScaleLimits  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipImage
    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipImage

    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipLayoutAsString
    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipLayoutAsString

    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipText
    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipText

    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Getter for property: (str) Bitmap
    ##   the Bitmap  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Bitmap(self) -> str:
        """
        Getter for property: (str) Bitmap
          the Bitmap  
            
         
        """
        pass
    
    ## Setter for property: (str) Bitmap

    ##   the Bitmap  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Bitmap.setter
    def Bitmap(self, bitmap_string: str):
        """
        Setter for property: (str) Bitmap
          the Bitmap  
            
         
        """
        pass
    
    ## Getter for property: (float) Increment
    ##   the Increment  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return float
    @property
    def Increment(self) -> float:
        """
        Getter for property: (float) Increment
          the Increment  
            
         
        """
        pass
    
    ## Setter for property: (float) Increment

    ##   the Increment  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Increment.setter
    def Increment(self, increment: float):
        """
        Setter for property: (float) Increment
          the Increment  
            
         
        """
        pass
    
    ## Getter for property: (float) LineIncrement
    ##   the LineIncrement  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return float
    @property
    def LineIncrement(self) -> float:
        """
        Getter for property: (float) LineIncrement
          the LineIncrement  
            
         
        """
        pass
    
    ## Setter for property: (float) LineIncrement

    ##   the LineIncrement  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @LineIncrement.setter
    def LineIncrement(self, line_increment: float):
        """
        Setter for property: (float) LineIncrement
          the LineIncrement  
            
         
        """
        pass
    
    ## Getter for property: (bool) Localize
    ##   the Localize  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def Localize(self) -> bool:
        """
        Getter for property: (bool) Localize
          the Localize  
            
         
        """
        pass
    
    ## Setter for property: (bool) Localize

    ##   the Localize  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Localize.setter
    def Localize(self, localize: bool):
        """
        Setter for property: (bool) Localize
          the Localize  
            
         
        """
        pass
    
    ## Getter for property: (bool) MaxInclusive
    ##   the MaxInclusive  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def MaxInclusive(self) -> bool:
        """
        Getter for property: (bool) MaxInclusive
          the MaxInclusive  
            
         
        """
        pass
    
    ## Setter for property: (bool) MaxInclusive

    ##   the MaxInclusive  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MaxInclusive.setter
    def MaxInclusive(self, max_inclusive: bool):
        """
        Setter for property: (bool) MaxInclusive
          the MaxInclusive  
            
         
        """
        pass
    
    ## Getter for property: (int) MaximumValue
    ##   the MaximumValue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def MaximumValue(self) -> int:
        """
        Getter for property: (int) MaximumValue
          the MaximumValue  
            
         
        """
        pass
    
    ## Setter for property: (int) MaximumValue

    ##   the MaximumValue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MaximumValue.setter
    def MaximumValue(self, max_value: int):
        """
        Setter for property: (int) MaximumValue
          the MaximumValue  
            
         
        """
        pass
    
    ## Getter for property: (bool) MinInclusive
    ##   the MinInclusive  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def MinInclusive(self) -> bool:
        """
        Getter for property: (bool) MinInclusive
          the MinInclusive  
            
         
        """
        pass
    
    ## Setter for property: (bool) MinInclusive

    ##   the MinInclusive  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MinInclusive.setter
    def MinInclusive(self, min_inclusive: bool):
        """
        Setter for property: (bool) MinInclusive
          the MinInclusive  
            
         
        """
        pass
    
    ## Getter for property: (int) MinimumValue
    ##   the MinimumValue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def MinimumValue(self) -> int:
        """
        Getter for property: (int) MinimumValue
          the MinimumValue  
            
         
        """
        pass
    
    ## Setter for property: (int) MinimumValue

    ##   the MinimumValue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MinimumValue.setter
    def MinimumValue(self, min_value: int):
        """
        Setter for property: (int) MinimumValue
          the MinimumValue  
            
         
        """
        pass
    
    ## Getter for property: (float) PageIncrement
    ##   the PageIncrement  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return float
    @property
    def PageIncrement(self) -> float:
        """
        Getter for property: (float) PageIncrement
          the PageIncrement  
            
         
        """
        pass
    
    ## Setter for property: (float) PageIncrement

    ##   the PageIncrement  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @PageIncrement.setter
    def PageIncrement(self, page_increment: float):
        """
        Setter for property: (float) PageIncrement
          the PageIncrement  
            
         
        """
        pass
    
    ## Getter for property: (str) PresentationStyleAsString
    ##   the PresentationStyle as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def PresentationStyleAsString(self) -> str:
        """
        Getter for property: (str) PresentationStyleAsString
          the PresentationStyle as string  
            
         
        """
        pass
    
    ## Setter for property: (str) PresentationStyleAsString

    ##   the PresentationStyle as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @PresentationStyleAsString.setter
    def PresentationStyleAsString(self, enumString: str):
        """
        Setter for property: (str) PresentationStyleAsString
          the PresentationStyle as string  
            
         
        """
        pass
    
    ## Getter for property: (bool) ReadOnlyValue
    ##   the ReadOnlyValue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ReadOnlyValue(self) -> bool:
        """
        Getter for property: (bool) ReadOnlyValue
          the ReadOnlyValue  
            
         
        """
        pass
    
    ## Setter for property: (bool) ReadOnlyValue

    ##   the ReadOnlyValue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ReadOnlyValue.setter
    def ReadOnlyValue(self, read_only: bool):
        """
        Setter for property: (bool) ReadOnlyValue
          the ReadOnlyValue  
            
         
        """
        pass
    
    ## Getter for property: (bool) RetainValue
    ##   the RetainValue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def RetainValue(self) -> bool:
        """
        Getter for property: (bool) RetainValue
          the RetainValue  
            
         
        """
        pass
    
    ## Setter for property: (bool) RetainValue

    ##   the RetainValue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @RetainValue.setter
    def RetainValue(self, retain: bool):
        """
        Setter for property: (bool) RetainValue
          the RetainValue  
            
         
        """
        pass
    
    ## Getter for property: (bool) ScaleLimits
    ##   the ScaleLimits  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ScaleLimits(self) -> bool:
        """
        Getter for property: (bool) ScaleLimits
          the ScaleLimits  
            
         
        """
        pass
    
    ## Setter for property: (bool) ScaleLimits

    ##   the ScaleLimits  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ScaleLimits.setter
    def ScaleLimits(self, scale_limits: bool):
        """
        Setter for property: (bool) ScaleLimits
          the ScaleLimits  
            
         
        """
        pass
    
    ## Getter for property: (str) ScaleMaxLimitLabel
    ##   the ScaleMaxLimitLabel  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def ScaleMaxLimitLabel(self) -> str:
        """
        Getter for property: (str) ScaleMaxLimitLabel
          the ScaleMaxLimitLabel  
            
         
        """
        pass
    
    ## Setter for property: (str) ScaleMaxLimitLabel

    ##   the ScaleMaxLimitLabel  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ScaleMaxLimitLabel.setter
    def ScaleMaxLimitLabel(self, max_limit_label: str):
        """
        Setter for property: (str) ScaleMaxLimitLabel
          the ScaleMaxLimitLabel  
            
         
        """
        pass
    
    ## Getter for property: (str) ScaleMinLimitLabel
    ##   the ScaleMinLimitLabel  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def ScaleMinLimitLabel(self) -> str:
        """
        Getter for property: (str) ScaleMinLimitLabel
          the ScaleMinLimitLabel  
            
         
        """
        pass
    
    ## Setter for property: (str) ScaleMinLimitLabel

    ##   the ScaleMinLimitLabel  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ScaleMinLimitLabel.setter
    def ScaleMinLimitLabel(self, min_limit_label: str):
        """
        Setter for property: (str) ScaleMinLimitLabel
          the ScaleMinLimitLabel  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowScaleValue
    ##   the ShowScaleValue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowScaleValue(self) -> bool:
        """
        Getter for property: (bool) ShowScaleValue
          the ShowScaleValue  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowScaleValue

    ##   the ShowScaleValue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowScaleValue.setter
    def ShowScaleValue(self, show_value: bool):
        """
        Setter for property: (bool) ShowScaleValue
          the ShowScaleValue  
            
         
        """
        pass
    
    ## Getter for property: (bool) TitleVisibility
    ##   the TitleVisibility  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def TitleVisibility(self) -> bool:
        """
        Getter for property: (bool) TitleVisibility
          the TitleVisibility  
            
         
        """
        pass
    
    ## Setter for property: (bool) TitleVisibility

    ##   the TitleVisibility  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @TitleVisibility.setter
    def TitleVisibility(self, visibility: bool):
        """
        Setter for property: (bool) TitleVisibility
          the TitleVisibility  
            
         
        """
        pass
    
    ## Getter for property: (int) Value
    ##   the Value  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def Value(self) -> int:
        """
        Getter for property: (int) Value
          the Value  
            
         
        """
        pass
    
    ## Setter for property: (int) Value

    ##   the Value  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Value.setter
    def Value(self, integer_value: int):
        """
        Setter for property: (int) Value
          the Value  
            
         
        """
        pass
    
    ## Getter for property: (bool) WrapSpin
    ##   the WrapSpin  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def WrapSpin(self) -> bool:
        """
        Getter for property: (bool) WrapSpin
          the WrapSpin  
            
         
        """
        pass
    
    ## Setter for property: (bool) WrapSpin

    ##   the WrapSpin  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @WrapSpin.setter
    def WrapSpin(self, wrap_spin: bool):
        """
        Setter for property: (bool) WrapSpin
          the WrapSpin  
            
         
        """
        pass
    
    ##  Gets the BalloonTooltipLayout members 
    ##  @return layout_strings (List[str]): Value to get from the property. .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBalloonTooltipLayoutMembers(integer_block: IntegerBlock) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         @return layout_strings (List[str]): Value to get from the property. .
        """
        pass
    
    ##  Gets the ComboOptions
    ##  @return option_value (List[int]): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetComboOptions(integer_block: IntegerBlock) -> List[int]:
        """
         Gets the ComboOptions
         @return option_value (List[int]): .
        """
        pass
    
    ##  Gets the PresentationStyle member 
    ##  @return member_strings (List[str]): Value to get for the property. .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPresentationStyleMembers(integer_block: IntegerBlock) -> List[str]:
        """
         Gets the PresentationStyle member 
         @return member_strings (List[str]): Value to get for the property. .
        """
        pass
    
    ##  Sets the ComboOptions
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="option_value"> (List[int]) </param>
    def SetComboOptions(integer_block: IntegerBlock, option_value: List[int]) -> None:
        """
         Sets the ComboOptions
        """
        pass
    
    ## Tests value changed event workflow mapped to this IntegerBlock block.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="ineteger_value"> (int) </param>
    def TestValueChanged(integer_block: IntegerBlock, ineteger_value: int) -> None:
        """
        Tests value changed event workflow mapped to this IntegerBlock block.
        """
        pass
    
##  Represents a Integer Table block
## 
##   <br>  Created in NX8.5.0  <br> 

class IntegerTable(UIBlock): 
    """ Represents a Integer Table block"""


    ## Getter for property: (str) ColumnTitles
    ##   the ColumnTitles  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1847.0.0.  Use @link NXOpen::BlockStyler::IntegerTable::JA_BLOCK_STYLER_INTEGER_TABLE_get_column_titles NXOpen::BlockStyler::IntegerTable::JA_BLOCK_STYLER_INTEGER_TABLE_get_column_titles@endlink  instead.  <br> 

    ## @return str
    @property
    def ColumnTitles(self) -> str:
        """
        Getter for property: (str) ColumnTitles
          the ColumnTitles  
            
         
        """
        pass
    
    ## Setter for property: (str) ColumnTitles

    ##   the ColumnTitles  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1847.0.0.  Use @link NXOpen::BlockStyler::IntegerTable::JA_BLOCK_STYLER_INTEGER_TABLE_set_column_titles NXOpen::BlockStyler::IntegerTable::JA_BLOCK_STYLER_INTEGER_TABLE_set_column_titles@endlink  instead.  <br> 

    @ColumnTitles.setter
    def ColumnTitles(self, title: str):
        """
        Setter for property: (str) ColumnTitles
          the ColumnTitles  
            
         
        """
        pass
    
    ## Getter for property: (float) Increment
    ##   the Increment.  
    ##    Use this property only when Spin is true  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return float
    @property
    def Increment(self) -> float:
        """
        Getter for property: (float) Increment
          the Increment.  
           Use this property only when Spin is true  
         
        """
        pass
    
    ## Setter for property: (float) Increment

    ##   the Increment.  
    ##    Use this property only when Spin is true  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Increment.setter
    def Increment(self, increment: float):
        """
        Setter for property: (float) Increment
          the Increment.  
           Use this property only when Spin is true  
         
        """
        pass
    
    ## Getter for property: (bool) RetainValue
    ##   the RetainValue.  
    ##    If true, indicates that the values in the block would be stored in dialog memory upon OK, Apply or Close.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def RetainValue(self) -> bool:
        """
        Getter for property: (bool) RetainValue
          the RetainValue.  
           If true, indicates that the values in the block would be stored in dialog memory upon OK, Apply or Close.   
         
        """
        pass
    
    ## Setter for property: (bool) RetainValue

    ##   the RetainValue.  
    ##    If true, indicates that the values in the block would be stored in dialog memory upon OK, Apply or Close.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @RetainValue.setter
    def RetainValue(self, retain: bool):
        """
        Setter for property: (bool) RetainValue
          the RetainValue.  
           If true, indicates that the values in the block would be stored in dialog memory upon OK, Apply or Close.   
         
        """
        pass
    
    ## Getter for property: (bool) Spin
    ##   the Spin  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def Spin(self) -> bool:
        """
        Getter for property: (bool) Spin
          the Spin  
            
         
        """
        pass
    
    ## Setter for property: (bool) Spin

    ##   the Spin  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Spin.setter
    def Spin(self, spin: bool):
        """
        Setter for property: (bool) Spin
          the Spin  
            
         
        """
        pass
    
    ## Getter for property: (bool) WrapSpin
    ##   the WrapSpin.  
    ##    Use this property only when Spin is true  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def WrapSpin(self) -> bool:
        """
        Getter for property: (bool) WrapSpin
          the WrapSpin.  
           Use this property only when Spin is true  
         
        """
        pass
    
    ## Setter for property: (bool) WrapSpin

    ##   the WrapSpin.  
    ##    Use this property only when Spin is true  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @WrapSpin.setter
    def WrapSpin(self, wrap_spin: bool):
        """
        Setter for property: (bool) WrapSpin
          the WrapSpin.  
           Use this property only when Spin is true  
         
        """
        pass
    
    ##  Gets the Column Tiltles
    ##  @return column_titles (List[str]): Column Title values to get from the property. .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## <param name="integer_table"> (@link IntegerTable NXOpen.BlockStyler.IntegerTable@endlink) </param>
    @staticmethod
    @overload
    def GetColumnTitles(self, integer_table: IntegerTable) -> List[str]:
        """
         Gets the Column Tiltles
         @return column_titles (List[str]): Column Title values to get from the property. .
        """
        pass
    
    ##  Gets the MaximumValues
    ##  @return A tuple consisting of (matrixValue, nRows, nColumns). 
    ##  - matrixValue is: List[int].Values to get from the property .
    ##  - nRows is: int. Number of Rows in the 2D matrix .
    ##  - nColumns is: int. Number of Columns in the 2D matrix .

    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetMaximumValues(integer_table: IntegerTable) -> Tuple[List[int], int, int]:
        """
         Gets the MaximumValues
         @return A tuple consisting of (matrixValue, nRows, nColumns). 
         - matrixValue is: List[int].Values to get from the property .
         - nRows is: int. Number of Rows in the 2D matrix .
         - nColumns is: int. Number of Columns in the 2D matrix .

        """
        pass
    
    ##  Gets the MinimumValues
    ##  @return A tuple consisting of (matrixValue, nRows, nColumns). 
    ##  - matrixValue is: List[int].Value to get for given property name. .
    ##  - nRows is: int. Number of Rows in the 2D matrix .
    ##  - nColumns is: int. Number of Columns in the 2D matrix .

    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetMinimumValues(integer_table: IntegerTable) -> Tuple[List[int], int, int]:
        """
         Gets the MinimumValues
         @return A tuple consisting of (matrixValue, nRows, nColumns). 
         - matrixValue is: List[int].Value to get for given property name. .
         - nRows is: int. Number of Rows in the 2D matrix .
         - nColumns is: int. Number of Columns in the 2D matrix .

        """
        pass
    
    ##  Gets the RowTitles
    ##  @return row_title (List[str]): Values to get from the property. .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetRowTitles(integer_table: IntegerTable) -> List[str]:
        """
         Gets the RowTitles
         @return row_title (List[str]): Values to get from the property. .
        """
        pass
    
    ##  Gets the Values
    ##  @return A tuple consisting of (matrixValue, nRows, nColumns). 
    ##  - matrixValue is: List[int].Values to get from the property. .
    ##  - nRows is: int. Number of Rows in the 2D matrix .
    ##  - nColumns is: int. Number of Columns in the 2D matrix .

    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetValues(integer_table: IntegerTable) -> Tuple[List[int], int, int]:
        """
         Gets the Values
         @return A tuple consisting of (matrixValue, nRows, nColumns). 
         - matrixValue is: List[int].Values to get from the property. .
         - nRows is: int. Number of Rows in the 2D matrix .
         - nColumns is: int. Number of Columns in the 2D matrix .

        """
        pass
    
    ##  Sets the Column Titles
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## Column Title values to set for the property. 
    @overload
    def SetColumnTitles(self, integer_table: IntegerTable, column_titles: List[str]) -> None:
        """
         Sets the Column Titles
        """
        pass
    
    ##  Sets the MaximumValues
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ##  Number of Rows in the 2D matrix 
    def SetMaximumValues(integer_table: IntegerTable, nRows: int, nColumns: int, matrixValue: List[int]) -> None:
        """
         Sets the MaximumValues
        """
        pass
    
    ##  Sets the MinimumValues
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ##  Number of Rows in the 2D matrix 
    def SetMinimumValues(integer_table: IntegerTable, nRows: int, nColumns: int, matrixValue: List[int]) -> None:
        """
         Sets the MinimumValues
        """
        pass
    
    ##  Sets the RowTitles
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## Value to set for the property. 
    def SetRowTitles(integer_table: IntegerTable, row_title: List[str]) -> None:
        """
         Sets the RowTitles
        """
        pass
    
    ##  Sets the Values
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ##  Number of Rows in the 2D matrix 
    def SetValues(integer_table: IntegerTable, nRows: int, nColumns: int, matrixValue: List[int]) -> None:
        """
         Sets the Values
        """
        pass
    
    ## Tests value changed event workflow mapped to this IntegerTable block.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ##  Number of Rows in the 2D matrix 
    def TestValueChanged(integer_table: IntegerTable, nRows: int, nColumns: int, matrixValue: List[int]) -> None:
        """
        Tests value changed event workflow mapped to this IntegerTable block.
        """
        pass
    
##  Represents a Label
## 
##   <br>  Created in NX8.5.0  <br> 

class Label(UIBlock): 
    """ Represents a Label"""


    ## Getter for property: (str) BalloonTooltipImage
    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipImage

    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipLayoutAsString
    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipLayoutAsString

    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipText
    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipText

    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipText.setter
    def BalloonTooltipText(self, tooltipText: str):
        """
        Setter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Getter for property: (str) Bitmap
    ##   the Bitmap  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Bitmap(self) -> str:
        """
        Getter for property: (str) Bitmap
          the Bitmap  
            
         
        """
        pass
    
    ## Setter for property: (str) Bitmap

    ##   the Bitmap  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Bitmap.setter
    def Bitmap(self, bitmap_string: str):
        """
        Setter for property: (str) Bitmap
          the Bitmap  
            
         
        """
        pass
    
    ## Getter for property: (bool) DisplayBitmapLabel
    ##   the DisplayBitmapLabel  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def DisplayBitmapLabel(self) -> bool:
        """
        Getter for property: (bool) DisplayBitmapLabel
          the DisplayBitmapLabel  
            
         
        """
        pass
    
    ## Setter for property: (bool) DisplayBitmapLabel

    ##   the DisplayBitmapLabel  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @DisplayBitmapLabel.setter
    def DisplayBitmapLabel(self, display: bool):
        """
        Setter for property: (bool) DisplayBitmapLabel
          the DisplayBitmapLabel  
            
         
        """
        pass
    
    ## Getter for property: (bool) HighQualityBitmap
    ##   the HighQualityBitmap  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def HighQualityBitmap(self) -> bool:
        """
        Getter for property: (bool) HighQualityBitmap
          the HighQualityBitmap  
            
         
        """
        pass
    
    ## Setter for property: (bool) HighQualityBitmap

    ##   the HighQualityBitmap  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @HighQualityBitmap.setter
    def HighQualityBitmap(self, high_quality: bool):
        """
        Setter for property: (bool) HighQualityBitmap
          the HighQualityBitmap  
            
         
        """
        pass
    
    ## Getter for property: (bool) Localize
    ##   the Localize.  
    ##    If true, translates the Label string into the current locale language.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def Localize(self) -> bool:
        """
        Getter for property: (bool) Localize
          the Localize.  
           If true, translates the Label string into the current locale language.  
         
        """
        pass
    
    ## Setter for property: (bool) Localize

    ##   the Localize.  
    ##    If true, translates the Label string into the current locale language.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Localize.setter
    def Localize(self, localize: bool):
        """
        Setter for property: (bool) Localize
          the Localize.  
           If true, translates the Label string into the current locale language.  
         
        """
        pass
    
    ## Getter for property: (str) Tooltip
    ##   the Tooltip  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Tooltip(self) -> str:
        """
        Getter for property: (str) Tooltip
          the Tooltip  
            
         
        """
        pass
    
    ## Setter for property: (str) Tooltip

    ##   the Tooltip  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Tooltip.setter
    def Tooltip(self, tooltip_string: str):
        """
        Setter for property: (str) Tooltip
          the Tooltip  
            
         
        """
        pass
    
    ## Getter for property: (bool) WordWrap
    ##   the WordWrap  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def WordWrap(self) -> bool:
        """
        Getter for property: (bool) WordWrap
          the WordWrap  
            
         
        """
        pass
    
    ## Setter for property: (bool) WordWrap

    ##   the WordWrap  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @WordWrap.setter
    def WordWrap(self, wordwrap: bool):
        """
        Setter for property: (bool) WordWrap
          the WordWrap  
            
         
        """
        pass
    
    ##  Gets the BalloonTooltipLayout members 
    ##  @return layout_strings (List[str]): Values to get from the property .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBalloonTooltipLayoutMembers(label: Label) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         @return layout_strings (List[str]): Values to get from the property .
        """
        pass
    
##  Represents a Layer block
## 
##   <br>  Created in NX10.0.0  <br> 

class LayerBlock(UIBlock): 
    """ Represents a Layer block"""


    ## Getter for property: (int) LayerOption
    ##   the Layer Option  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return int
    @property
    def LayerOption(self) -> int:
        """
        Getter for property: (int) LayerOption
          the Layer Option  
            
         
        """
        pass
    
    ## Setter for property: (int) LayerOption

    ##   the Layer Option  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @LayerOption.setter
    def LayerOption(self, integer_layer_option: int):
        """
        Setter for property: (int) LayerOption
          the Layer Option  
            
         
        """
        pass
    
    ## Getter for property: (int) LayerValue
    ##   the Layer Value  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return int
    @property
    def LayerValue(self) -> int:
        """
        Getter for property: (int) LayerValue
          the Layer Value  
            
         
        """
        pass
    
    ## Setter for property: (int) LayerValue

    ##   the Layer Value  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @LayerValue.setter
    def LayerValue(self, integer_layer_value: int):
        """
        Setter for property: (int) LayerValue
          the Layer Value  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowMaintainLayerOption
    ##   the Show Maintain Layer Option
    ##         If set to true, Maintain option is displayed in layer options  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def ShowMaintainLayerOption(self) -> bool:
        """
        Getter for property: (bool) ShowMaintainLayerOption
          the Show Maintain Layer Option
                If set to true, Maintain option is displayed in layer options  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowMaintainLayerOption

    ##   the Show Maintain Layer Option
    ##         If set to true, Maintain option is displayed in layer options  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ShowMaintainLayerOption.setter
    def ShowMaintainLayerOption(self, show_maintain_layer_option: bool):
        """
        Setter for property: (bool) ShowMaintainLayerOption
          the Show Maintain Layer Option
                If set to true, Maintain option is displayed in layer options  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowOriginalLayerOption
    ##   the Show Original Layer Option
    ##         If set to true, Original option is displayed in layer options  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def ShowOriginalLayerOption(self) -> bool:
        """
        Getter for property: (bool) ShowOriginalLayerOption
          the Show Original Layer Option
                If set to true, Original option is displayed in layer options  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowOriginalLayerOption

    ##   the Show Original Layer Option
    ##         If set to true, Original option is displayed in layer options  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ShowOriginalLayerOption.setter
    def ShowOriginalLayerOption(self, show_original_layer_option: bool):
        """
        Setter for property: (bool) ShowOriginalLayerOption
          the Show Original Layer Option
                If set to true, Original option is displayed in layer options  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowUserDefinedLayerOption
    ##   the Show User Defined Layer Option
    ##         If set to true, User Defined option is displayed in layer options  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def ShowUserDefinedLayerOption(self) -> bool:
        """
        Getter for property: (bool) ShowUserDefinedLayerOption
          the Show User Defined Layer Option
                If set to true, User Defined option is displayed in layer options  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowUserDefinedLayerOption

    ##   the Show User Defined Layer Option
    ##         If set to true, User Defined option is displayed in layer options  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ShowUserDefinedLayerOption.setter
    def ShowUserDefinedLayerOption(self, show_user_defined_layer_option: bool):
        """
        Setter for property: (bool) ShowUserDefinedLayerOption
          the Show User Defined Layer Option
                If set to true, User Defined option is displayed in layer options  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowWorkLayerOption
    ##   the Show Work Layer Option
    ##         If set to true, Work option is displayed in layer options  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def ShowWorkLayerOption(self) -> bool:
        """
        Getter for property: (bool) ShowWorkLayerOption
          the Show Work Layer Option
                If set to true, Work option is displayed in layer options  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowWorkLayerOption

    ##   the Show Work Layer Option
    ##         If set to true, Work option is displayed in layer options  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ShowWorkLayerOption.setter
    def ShowWorkLayerOption(self, show_work_layer_option: bool):
        """
        Setter for property: (bool) ShowWorkLayerOption
          the Show Work Layer Option
                If set to true, Work option is displayed in layer options  
            
         
        """
        pass
    
    ## Tests option changed event workflow mapped to this layer block.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="integer_layer_option"> (int) </param>
    def TestOptionChanged(layer_block: LayerBlock, integer_layer_option: int) -> None:
        """
        Tests option changed event workflow mapped to this layer block.
        """
        pass
    
    ## Tests value changed event workflow mapped to this LayerBlock block.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="ineteger_layer_value"> (int) </param>
    def TestValueChanged(layer_block: LayerBlock, ineteger_layer_value: int) -> None:
        """
        Tests value changed event workflow mapped to this LayerBlock block.
        """
        pass
    
import NXOpen
##  Represents a Linear Dimension block
## 
##   <br>  Created in NX8.5.0  <br> 

class LinearDimension(UIBlock): 
    """ Represents a Linear Dimension block"""


    ## Getter for property: (bool) AdaptiveScaleLimits
    ##  the AdaptiveScaleLimits.  
    ##   
    ##         If true, indicates that the scale should be adaptive.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def AdaptiveScaleLimits(self) -> bool:
        """
        Getter for property: (bool) AdaptiveScaleLimits
         the AdaptiveScaleLimits.  
          
                If true, indicates that the scale should be adaptive.  
         
        """
        pass
    
    ## Setter for property: (bool) AdaptiveScaleLimits

    ##  the AdaptiveScaleLimits.  
    ##   
    ##         If true, indicates that the scale should be adaptive.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @AdaptiveScaleLimits.setter
    def AdaptiveScaleLimits(self, scale_limits: bool):
        """
        Setter for property: (bool) AdaptiveScaleLimits
         the AdaptiveScaleLimits.  
          
                If true, indicates that the scale should be adaptive.  
         
        """
        pass
    
    ## Getter for property: (bool) AutoReverseDuringDrag
    ##   the AutoReverseDuringDrag.  
    ##    If true, the linear dimension handle reverses its direction when it is dragged through the 0 value.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def AutoReverseDuringDrag(self) -> bool:
        """
        Getter for property: (bool) AutoReverseDuringDrag
          the AutoReverseDuringDrag.  
           If true, the linear dimension handle reverses its direction when it is dragged through the 0 value.  
         
        """
        pass
    
    ## Setter for property: (bool) AutoReverseDuringDrag

    ##   the AutoReverseDuringDrag.  
    ##    If true, the linear dimension handle reverses its direction when it is dragged through the 0 value.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @AutoReverseDuringDrag.setter
    def AutoReverseDuringDrag(self, auto_reverse: bool):
        """
        Setter for property: (bool) AutoReverseDuringDrag
          the AutoReverseDuringDrag.  
           If true, the linear dimension handle reverses its direction when it is dragged through the 0 value.  
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipImage
    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipImage

    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipLayoutAsString
    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipLayoutAsString

    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipText
    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipText

    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ExpressionObject
    ##   the ExpressionObject  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def ExpressionObject(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ExpressionObject
          the ExpressionObject  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ExpressionObject

    ##   the ExpressionObject  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ExpressionObject.setter
    def ExpressionObject(self, expression_obj: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ExpressionObject
          the ExpressionObject  
            
         
        """
        pass
    
    ## Getter for property: (str) Formula
    ##   the Formula  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Formula(self) -> str:
        """
        Getter for property: (str) Formula
          the Formula  
            
         
        """
        pass
    
    ## Setter for property: (str) Formula

    ##   the Formula  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Formula.setter
    def Formula(self, formula: str):
        """
        Setter for property: (str) Formula
          the Formula  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) HandleOrientation
    ##   the HandleOrientation  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.Vector3d
    @property
    def HandleOrientation(self) -> NXOpen.Vector3d:
        """
        Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) HandleOrientation
          the HandleOrientation  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) HandleOrientation

    ##   the HandleOrientation  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @HandleOrientation.setter
    def HandleOrientation(self, orientation: NXOpen.Vector3d):
        """
        Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) HandleOrientation
          the HandleOrientation  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) HandleOrigin
    ##   the HandleOrigin  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def HandleOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) HandleOrigin
          the HandleOrigin  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) HandleOrigin

    ##   the HandleOrigin  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @HandleOrigin.setter
    def HandleOrigin(self, handle_orogin: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) HandleOrigin
          the HandleOrigin  
            
         
        """
        pass
    
    ## Getter for property: (float) LineIncrement
    ##  the LineIncrement value.  
    ##   
    ##         Specifies the increment/decrement when the user presses the arrow keys on the keyboard.
    ##         Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def LineIncrement(self) -> float:
        """
        Getter for property: (float) LineIncrement
         the LineIncrement value.  
          
                Specifies the increment/decrement when the user presses the arrow keys on the keyboard.
                Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
         
        """
        pass
    
    ## Setter for property: (float) LineIncrement

    ##  the LineIncrement value.  
    ##   
    ##         Specifies the increment/decrement when the user presses the arrow keys on the keyboard.
    ##         Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @LineIncrement.setter
    def LineIncrement(self, line_increment: float):
        """
        Setter for property: (float) LineIncrement
         the LineIncrement value.  
          
                Specifies the increment/decrement when the user presses the arrow keys on the keyboard.
                Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
         
        """
        pass
    
    ## Getter for property: (bool) MaxInclusive
    ##   the MaxInclusive  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def MaxInclusive(self) -> bool:
        """
        Getter for property: (bool) MaxInclusive
          the MaxInclusive  
            
         
        """
        pass
    
    ## Setter for property: (bool) MaxInclusive

    ##   the MaxInclusive  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MaxInclusive.setter
    def MaxInclusive(self, max_inclusive: bool):
        """
        Setter for property: (bool) MaxInclusive
          the MaxInclusive  
            
         
        """
        pass
    
    ## Getter for property: (float) MaximumValue
    ##   the MaximumValue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return float
    @property
    def MaximumValue(self) -> float:
        """
        Getter for property: (float) MaximumValue
          the MaximumValue  
            
         
        """
        pass
    
    ## Setter for property: (float) MaximumValue

    ##   the MaximumValue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MaximumValue.setter
    def MaximumValue(self, max_value: float):
        """
        Setter for property: (float) MaximumValue
          the MaximumValue  
            
         
        """
        pass
    
    ## Getter for property: (bool) MinInclusive
    ##   the MinInclusive  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def MinInclusive(self) -> bool:
        """
        Getter for property: (bool) MinInclusive
          the MinInclusive  
            
         
        """
        pass
    
    ## Setter for property: (bool) MinInclusive

    ##   the MinInclusive  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MinInclusive.setter
    def MinInclusive(self, min_inclusive: bool):
        """
        Setter for property: (bool) MinInclusive
          the MinInclusive  
            
         
        """
        pass
    
    ## Getter for property: (float) MinimumValue
    ##   the MinimumValue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return float
    @property
    def MinimumValue(self) -> float:
        """
        Getter for property: (float) MinimumValue
          the MinimumValue  
            
         
        """
        pass
    
    ## Setter for property: (float) MinimumValue

    ##   the MinimumValue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MinimumValue.setter
    def MinimumValue(self, min_value: float):
        """
        Setter for property: (float) MinimumValue
          the MinimumValue  
            
         
        """
        pass
    
    ## Getter for property: (float) PageIncrement
    ##  the PageIncrement value.  
    ##   
    ##         Specifies the increment/decrement when the user presses the Page Up or Page Down keys on the keyboard.
    ##         Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def PageIncrement(self) -> float:
        """
        Getter for property: (float) PageIncrement
         the PageIncrement value.  
          
                Specifies the increment/decrement when the user presses the Page Up or Page Down keys on the keyboard.
                Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
         
        """
        pass
    
    ## Setter for property: (float) PageIncrement

    ##  the PageIncrement value.  
    ##   
    ##         Specifies the increment/decrement when the user presses the Page Up or Page Down keys on the keyboard.
    ##         Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @PageIncrement.setter
    def PageIncrement(self, page_increment: float):
        """
        Setter for property: (float) PageIncrement
         the PageIncrement value.  
          
                Specifies the increment/decrement when the user presses the Page Up or Page Down keys on the keyboard.
                Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
         
        """
        pass
    
    ## Getter for property: (bool) ShowFocusHandle
    ##   the ShowFocusHandle  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowFocusHandle(self) -> bool:
        """
        Getter for property: (bool) ShowFocusHandle
          the ShowFocusHandle  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowFocusHandle

    ##   the ShowFocusHandle  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowFocusHandle.setter
    def ShowFocusHandle(self, show_focus: bool):
        """
        Setter for property: (bool) ShowFocusHandle
          the ShowFocusHandle  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowHandle
    ##   the ShowHandle.  
    ##    If true, linear dimension handle is visible  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowHandle(self) -> bool:
        """
        Getter for property: (bool) ShowHandle
          the ShowHandle.  
           If true, linear dimension handle is visible  
         
        """
        pass
    
    ## Setter for property: (bool) ShowHandle

    ##   the ShowHandle.  
    ##    If true, linear dimension handle is visible  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowHandle.setter
    def ShowHandle(self, show_handle: bool):
        """
        Setter for property: (bool) ShowHandle
          the ShowHandle.  
           If true, linear dimension handle is visible  
         
        """
        pass
    
    ## Getter for property: (int) SnapPointTypesOnByDefault
    ##   the SnapPointTypesOnByDefault  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX9.0.0.  This call can be safely removed as this is now a no-op.  <br> 

    ## @return int
    @property
    def SnapPointTypesOnByDefault(self) -> int:
        """
        Getter for property: (int) SnapPointTypesOnByDefault
          the SnapPointTypesOnByDefault  
            
         
        """
        pass
    
    ## Setter for property: (int) SnapPointTypesOnByDefault

    ##   the SnapPointTypesOnByDefault  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX9.0.0.  This call can be safely removed as this is now a no-op.  <br> 

    @SnapPointTypesOnByDefault.setter
    def SnapPointTypesOnByDefault(self, point_type: int):
        """
        Setter for property: (int) SnapPointTypesOnByDefault
          the SnapPointTypesOnByDefault  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Units
    ##   the Units  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def Units(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Units
          the Units  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Units

    ##   the Units  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Units.setter
    def Units(self, units: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Units
          the Units  
            
         
        """
        pass
    
    ## Getter for property: (float) Value
    ##   the Value.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return float
    @property
    def Value(self) -> float:
        """
        Getter for property: (float) Value
          the Value.  
            
         
        """
        pass
    
    ## Setter for property: (float) Value

    ##   the Value.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Value.setter
    def Value(self, dimension_value: float):
        """
        Setter for property: (float) Value
          the Value.  
            
         
        """
        pass
    
    ## Getter for property: (bool) WithScale
    ##   the WithScale.  
    ##    If true, the slider bar is shown.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def WithScale(self) -> bool:
        """
        Getter for property: (bool) WithScale
          the WithScale.  
           If true, the slider bar is shown.  
         
        """
        pass
    
    ## Setter for property: (bool) WithScale

    ##   the WithScale.  
    ##    If true, the slider bar is shown.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @WithScale.setter
    def WithScale(self, with_scale: bool):
        """
        Setter for property: (bool) WithScale
          the WithScale.  
           If true, the slider bar is shown.  
         
        """
        pass
    
    ##  Gets the BalloonTooltipLayout members 
    ##  @return layout_strings (List[str]): Values to get from the property. .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBalloonTooltipLayoutMembers(linear_dim: LinearDimension) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         @return layout_strings (List[str]): Values to get from the property. .
        """
        pass
    
    ## Tests value changed event workflow mapped to this LinearDimension block.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="dimension_value"> (float) </param>
    def TestValueChanged(linear_dim: LinearDimension, dimension_value: float) -> None:
        """
        Tests value changed event workflow mapped to this LinearDimension block.
        """
        pass
    
##  Represents a Line Width block
## 
##   <br>  Created in NX9.0.0  <br> 

class LineColorFontWidth(UIBlock): 
    """ Represents a Line Width block"""


    ## Getter for property: (str) HideSubBlocksAsString
    ##   the hide sub block.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def HideSubBlocksAsString(self) -> str:
        """
        Getter for property: (str) HideSubBlocksAsString
          the hide sub block.  
            
         
        """
        pass
    
    ## Setter for property: (str) HideSubBlocksAsString

    ##   the hide sub block.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @HideSubBlocksAsString.setter
    def HideSubBlocksAsString(self, hideSubBlocksString: str):
        """
        Setter for property: (str) HideSubBlocksAsString
          the hide sub block.  
            
         
        """
        pass
    
    ## Getter for property: (str) LabelString
    ##   the Label String in horizontal layout.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return str
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
          the Label String in horizontal layout.  
            
         
        """
        pass
    
    ## Setter for property: (str) LabelString

    ##   the Label String in horizontal layout.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
          the Label String in horizontal layout.  
            
         
        """
        pass
    
    ## Getter for property: (str) LayoutAsString
    ##   the layout.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def LayoutAsString(self) -> str:
        """
        Getter for property: (str) LayoutAsString
          the layout.  
            
         
        """
        pass
    
    ## Setter for property: (str) LayoutAsString

    ##   the layout.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @LayoutAsString.setter
    def LayoutAsString(self, layoutString: str):
        """
        Setter for property: (str) LayoutAsString
          the layout.  
            
         
        """
        pass
    
    ## Getter for property: (int) LineFontAvailableOptions
    ##   the Line Font Available Options  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def LineFontAvailableOptions(self) -> int:
        """
        Getter for property: (int) LineFontAvailableOptions
          the Line Font Available Options  
            
         
        """
        pass
    
    ## Setter for property: (int) LineFontAvailableOptions

    ##   the Line Font Available Options  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @LineFontAvailableOptions.setter
    def LineFontAvailableOptions(self, lineFontAvailableOptions: int):
        """
        Setter for property: (int) LineFontAvailableOptions
          the Line Font Available Options  
            
         
        """
        pass
    
    ## Getter for property: (str) LineFontValueAsString
    ##   the Line Font Value.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def LineFontValueAsString(self) -> str:
        """
        Getter for property: (str) LineFontValueAsString
          the Line Font Value.  
            
         
        """
        pass
    
    ## Setter for property: (str) LineFontValueAsString

    ##   the Line Font Value.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @LineFontValueAsString.setter
    def LineFontValueAsString(self, fontValueString: str):
        """
        Setter for property: (str) LineFontValueAsString
          the Line Font Value.  
            
         
        """
        pass
    
    ## Getter for property: (bool) LineWidthShowDefault
    ##   the Line width Show Default  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def LineWidthShowDefault(self) -> bool:
        """
        Getter for property: (bool) LineWidthShowDefault
          the Line width Show Default  
            
         
        """
        pass
    
    ## Setter for property: (bool) LineWidthShowDefault

    ##   the Line width Show Default  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @LineWidthShowDefault.setter
    def LineWidthShowDefault(self, lineWidthShowDefault: bool):
        """
        Setter for property: (bool) LineWidthShowDefault
          the Line width Show Default  
            
         
        """
        pass
    
    ## Getter for property: (bool) LineWidthShowDefaultAsOriginal
    ##   the Line Width Show Default as Original  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def LineWidthShowDefaultAsOriginal(self) -> bool:
        """
        Getter for property: (bool) LineWidthShowDefaultAsOriginal
          the Line Width Show Default as Original  
            
         
        """
        pass
    
    ## Setter for property: (bool) LineWidthShowDefaultAsOriginal

    ##   the Line Width Show Default as Original  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @LineWidthShowDefaultAsOriginal.setter
    def LineWidthShowDefaultAsOriginal(self, lineWidthShowDefaultAsOriginal: bool):
        """
        Setter for property: (bool) LineWidthShowDefaultAsOriginal
          the Line Width Show Default as Original  
            
         
        """
        pass
    
    ## Getter for property: (bool) LineWidthShowNoChange
    ##   the Line Width Show No Change  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def LineWidthShowNoChange(self) -> bool:
        """
        Getter for property: (bool) LineWidthShowNoChange
          the Line Width Show No Change  
            
         
        """
        pass
    
    ## Setter for property: (bool) LineWidthShowNoChange

    ##   the Line Width Show No Change  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @LineWidthShowNoChange.setter
    def LineWidthShowNoChange(self, lineWidthShowNoChange: bool):
        """
        Setter for property: (bool) LineWidthShowNoChange
          the Line Width Show No Change  
            
         
        """
        pass
    
    ## Getter for property: (bool) LineWidthUseWideLines
    ##   the Line Width Use Wide Lines  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def LineWidthUseWideLines(self) -> bool:
        """
        Getter for property: (bool) LineWidthUseWideLines
          the Line Width Use Wide Lines  
            
         
        """
        pass
    
    ## Setter for property: (bool) LineWidthUseWideLines

    ##   the Line Width Use Wide Lines  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @LineWidthUseWideLines.setter
    def LineWidthUseWideLines(self, lineWidthUseWideLines: bool):
        """
        Setter for property: (bool) LineWidthUseWideLines
          the Line Width Use Wide Lines  
            
         
        """
        pass
    
    ## Getter for property: (int) LineWidthValue
    ##  the LineWidthValue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return int
    @property
    def LineWidthValue(self) -> int:
        """
        Getter for property: (int) LineWidthValue
         the LineWidthValue  
            
         
        """
        pass
    
    ## Setter for property: (int) LineWidthValue

    ##  the LineWidthValue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @LineWidthValue.setter
    def LineWidthValue(self, width_value: int):
        """
        Setter for property: (int) LineWidthValue
         the LineWidthValue  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowLabel
    ##   the Show Label flag.  
    ##   
    ##         If true, the block label is shown in horizontal layout.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def ShowLabel(self) -> bool:
        """
        Getter for property: (bool) ShowLabel
          the Show Label flag.  
          
                If true, the block label is shown in horizontal layout.  
         
        """
        pass
    
    ## Setter for property: (bool) ShowLabel

    ##   the Show Label flag.  
    ##   
    ##         If true, the block label is shown in horizontal layout.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @ShowLabel.setter
    def ShowLabel(self, showLabel: bool):
        """
        Setter for property: (bool) ShowLabel
          the Show Label flag.  
          
                If true, the block label is shown in horizontal layout.  
         
        """
        pass
    
    ##  Gets line color values
    ##  @return colorValueVector (List[int]): color values to get from the property.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetColorValue(lineColorFontWidth: LineColorFontWidth) -> List[int]:
        """
         Gets line color values
         @return colorValueVector (List[int]): color values to get from the property.
        """
        pass
    
    ##  Sets line color values
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ## color values to set for the property. 
    def SetColorValue(lineColorFontWidth: LineColorFontWidth, colorValueVector: List[int]) -> None:
        """
         Sets line color values
        """
        pass
    
    ## Tests color value changed event workflow mapped to this LineColorFontWidth block. Invokes the client notifiers to simulate UI like event.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## color values to set for the property. 
    def TestColorValueChanged(lineColorFontWidth: LineColorFontWidth, colorValueVector: List[int]) -> None:
        """
        Tests color value changed event workflow mapped to this LineColorFontWidth block. Invokes the client notifiers to simulate UI like event.
        """
        pass
    
    ## Tests font value changed event workflow mapped to this LineColorFontWidth block.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="fontValueString"> (str) </param>
    def TestFontValueChanged(lineColorFontWidth: LineColorFontWidth, fontValueString: str) -> None:
        """
        Tests font value changed event workflow mapped to this LineColorFontWidth block.
        """
        pass
    
    ## Tests width value changed event workflow mapped to this LineColorFontWidth block.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="width_value"> (int) </param>
    def TestWidthValueChanged(lineColorFontWidth: LineColorFontWidth, width_value: int) -> None:
        """
        Tests width value changed event workflow mapped to this LineColorFontWidth block.
        """
        pass
    
##  Represents a Line Width block
## 
##   <br>  Created in NX9.0.0  <br> 

class LineFont(UIBlock): 
    """ Represents a Line Width block"""


    ## Getter for property: (int) AvailableOptions
    ##   the Available Options  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def AvailableOptions(self) -> int:
        """
        Getter for property: (int) AvailableOptions
          the Available Options  
            
         
        """
        pass
    
    ## Setter for property: (int) AvailableOptions

    ##   the Available Options  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @AvailableOptions.setter
    def AvailableOptions(self, availableOptions: int):
        """
        Setter for property: (int) AvailableOptions
          the Available Options  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowOptionLabels
    ##   the show option labels  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def ShowOptionLabels(self) -> bool:
        """
        Getter for property: (bool) ShowOptionLabels
          the show option labels  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowOptionLabels

    ##   the show option labels  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ShowOptionLabels.setter
    def ShowOptionLabels(self, showOptionLabels: bool):
        """
        Setter for property: (bool) ShowOptionLabels
          the show option labels  
            
         
        """
        pass
    
    ## Getter for property: (str) ValueAsString
    ##   the value  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def ValueAsString(self) -> str:
        """
        Getter for property: (str) ValueAsString
          the value  
            
         
        """
        pass
    
    ## Setter for property: (str) ValueAsString

    ##   the value  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ValueAsString.setter
    def ValueAsString(self, fontValueString: str):
        """
        Setter for property: (str) ValueAsString
          the value  
            
         
        """
        pass
    
    ## Tests value changed event workflow mapped to this LineFont block.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="fontValueString"> (str) </param>
    def TestValueChanged(lineFont: LineFont, fontValueString: str) -> None:
        """
        Tests value changed event workflow mapped to this LineFont block.
        """
        pass
    
##  Represents a Line Width block
## 
##   <br>  Created in NX8.5.0  <br> 

class LineWidth(UIBlock): 
    """ Represents a Line Width block"""


    ## Getter for property: (bool) AllowDefaultWidth
    ##   the AllowDefaultWidth  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def AllowDefaultWidth(self) -> bool:
        """
        Getter for property: (bool) AllowDefaultWidth
          the AllowDefaultWidth  
            
         
        """
        pass
    
    ## Getter for property: (bool) AllowNoChangeWidth
    ##   the AllowNoChangeWidth.  
    ##    If true, no change in width is allowed.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def AllowNoChangeWidth(self) -> bool:
        """
        Getter for property: (bool) AllowNoChangeWidth
          the AllowNoChangeWidth.  
           If true, no change in width is allowed.  
         
        """
        pass
    
    ## Getter for property: (bool) LabelVisibility
    ##   the LabelVisibility  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def LabelVisibility(self) -> bool:
        """
        Getter for property: (bool) LabelVisibility
          the LabelVisibility  
            
         
        """
        pass
    
    ## Setter for property: (bool) LabelVisibility

    ##   the LabelVisibility  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @LabelVisibility.setter
    def LabelVisibility(self, visible: bool):
        """
        Setter for property: (bool) LabelVisibility
          the LabelVisibility  
            
         
        """
        pass
    
    ## Getter for property: (int) LineWidthValue
    ##   the LineWidthValue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def LineWidthValue(self) -> int:
        """
        Getter for property: (int) LineWidthValue
          the LineWidthValue  
            
         
        """
        pass
    
    ## Setter for property: (int) LineWidthValue

    ##   the LineWidthValue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @LineWidthValue.setter
    def LineWidthValue(self, width_value: int):
        """
        Setter for property: (int) LineWidthValue
          the LineWidthValue  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowDefaultAsOriginal
    ##   the ShowDefaultAsOriginal.  
    ##    If true, default entry is shown as original.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowDefaultAsOriginal(self) -> bool:
        """
        Getter for property: (bool) ShowDefaultAsOriginal
          the ShowDefaultAsOriginal.  
           If true, default entry is shown as original.  
         
        """
        pass
    
    ## Tests value changed event workflow mapped to this LineWidth block.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="width_value"> (int) </param>
    def TestValueChanged(lineWidth: LineWidth, width_value: int) -> None:
        """
        Tests value changed event workflow mapped to this LineWidth block.
        """
        pass
    
##  Represents a ListBox block 
## 
##   <br>  Created in NX6.0.0  <br> 

class ListBox(UIBlock): 
    """ Represents a ListBox block """


    ## Getter for property: (bool) AllowDeselectForSingleSelect
    ##   the AllowDeselectForSingleSelect.  
    ##    Allows deselection of item using Ctrl+MB1 when single select is true.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def AllowDeselectForSingleSelect(self) -> bool:
        """
        Getter for property: (bool) AllowDeselectForSingleSelect
          the AllowDeselectForSingleSelect.  
           Allows deselection of item using Ctrl+MB1 when single select is true.  
         
        """
        pass
    
    ## Setter for property: (bool) AllowDeselectForSingleSelect

    ##   the AllowDeselectForSingleSelect.  
    ##    Allows deselection of item using Ctrl+MB1 when single select is true.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @AllowDeselectForSingleSelect.setter
    def AllowDeselectForSingleSelect(self, allow: bool):
        """
        Setter for property: (bool) AllowDeselectForSingleSelect
          the AllowDeselectForSingleSelect.  
           Allows deselection of item using Ctrl+MB1 when single select is true.  
         
        """
        pass
    
    ## Getter for property: (int) Height
    ##   the Height  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def Height(self) -> int:
        """
        Getter for property: (int) Height
          the Height  
            
         
        """
        pass
    
    ## Setter for property: (int) Height

    ##   the Height  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Height.setter
    def Height(self, height: int):
        """
        Setter for property: (int) Height
          the Height  
            
         
        """
        pass
    
    ## Getter for property: (bool) IsAddButtonSensitive
    ##   the IsAddButtonSensitive  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def IsAddButtonSensitive(self) -> bool:
        """
        Getter for property: (bool) IsAddButtonSensitive
          the IsAddButtonSensitive  
            
         
        """
        pass
    
    ## Setter for property: (bool) IsAddButtonSensitive

    ##   the IsAddButtonSensitive  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @IsAddButtonSensitive.setter
    def IsAddButtonSensitive(self, sensitive: bool):
        """
        Setter for property: (bool) IsAddButtonSensitive
          the IsAddButtonSensitive  
            
         
        """
        pass
    
    ## Getter for property: (bool) IsDeleteButtonSensitive
    ##   the IsDeleteButtonSensitive  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def IsDeleteButtonSensitive(self) -> bool:
        """
        Getter for property: (bool) IsDeleteButtonSensitive
          the IsDeleteButtonSensitive  
            
         
        """
        pass
    
    ## Setter for property: (bool) IsDeleteButtonSensitive

    ##   the IsDeleteButtonSensitive  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @IsDeleteButtonSensitive.setter
    def IsDeleteButtonSensitive(self, sesitive: bool):
        """
        Setter for property: (bool) IsDeleteButtonSensitive
          the IsDeleteButtonSensitive  
            
         
        """
        pass
    
    ## Getter for property: (bool) Localize
    ##   the Localize.  
    ##    If true, translates the Label string into the language of the current locale.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def Localize(self) -> bool:
        """
        Getter for property: (bool) Localize
          the Localize.  
           If true, translates the Label string into the language of the current locale.  
         
        """
        pass
    
    ## Setter for property: (bool) Localize

    ##   the Localize.  
    ##    If true, translates the Label string into the language of the current locale.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Localize.setter
    def Localize(self, localize: bool):
        """
        Setter for property: (bool) Localize
          the Localize.  
           If true, translates the Label string into the language of the current locale.  
         
        """
        pass
    
    ## Getter for property: (int) MaximumHeight
    ##   the MaximumHeight  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def MaximumHeight(self) -> int:
        """
        Getter for property: (int) MaximumHeight
          the MaximumHeight  
            
         
        """
        pass
    
    ## Setter for property: (int) MaximumHeight

    ##   the MaximumHeight  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MaximumHeight.setter
    def MaximumHeight(self, max_height: int):
        """
        Setter for property: (int) MaximumHeight
          the MaximumHeight  
            
         
        """
        pass
    
    ## Getter for property: (int) MaximumStringLength
    ##   the MaximumStringLength  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def MaximumStringLength(self) -> int:
        """
        Getter for property: (int) MaximumStringLength
          the MaximumStringLength  
            
         
        """
        pass
    
    ## Setter for property: (int) MaximumStringLength

    ##   the MaximumStringLength  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MaximumStringLength.setter
    def MaximumStringLength(self, max_length: int):
        """
        Setter for property: (int) MaximumStringLength
          the MaximumStringLength  
            
         
        """
        pass
    
    ## Getter for property: (int) MinimumHeight
    ##   the MinimumHeight  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def MinimumHeight(self) -> int:
        """
        Getter for property: (int) MinimumHeight
          the MinimumHeight  
            
         
        """
        pass
    
    ## Setter for property: (int) MinimumHeight

    ##   the MinimumHeight  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MinimumHeight.setter
    def MinimumHeight(self, min_height: int):
        """
        Setter for property: (int) MinimumHeight
          the MinimumHeight  
            
         
        """
        pass
    
    ## Getter for property: (bool) ResizeHeightWithDialog
    ##   the ResizeHeightWithDialog  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ResizeHeightWithDialog(self) -> bool:
        """
        Getter for property: (bool) ResizeHeightWithDialog
          the ResizeHeightWithDialog  
            
         
        """
        pass
    
    ## Setter for property: (bool) ResizeHeightWithDialog

    ##   the ResizeHeightWithDialog  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ResizeHeightWithDialog.setter
    def ResizeHeightWithDialog(self, resize: bool):
        """
        Setter for property: (bool) ResizeHeightWithDialog
          the ResizeHeightWithDialog  
            
         
        """
        pass
    
    ## Getter for property: (int) SelectedItemIndex
    ##   the SelectedItemIndex.  
    ##    Valid only if SingleSelect is true. Otherwise -1 is returned.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def SelectedItemIndex(self) -> int:
        """
        Getter for property: (int) SelectedItemIndex
          the SelectedItemIndex.  
           Valid only if SingleSelect is true. Otherwise -1 is returned.  
         
        """
        pass
    
    ## Setter for property: (int) SelectedItemIndex

    ##   the SelectedItemIndex.  
    ##    Valid only if SingleSelect is true. Otherwise -1 is returned.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @SelectedItemIndex.setter
    def SelectedItemIndex(self, index: int):
        """
        Setter for property: (int) SelectedItemIndex
          the SelectedItemIndex.  
           Valid only if SingleSelect is true. Otherwise -1 is returned.  
         
        """
        pass
    
    ## Getter for property: (str) SelectedItemString
    ##   the SelectedItemString.  
    ##    Valid only if SingleSelect is true. Otherwise empty string is returned.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def SelectedItemString(self) -> str:
        """
        Getter for property: (str) SelectedItemString
          the SelectedItemString.  
           Valid only if SingleSelect is true. Otherwise empty string is returned.  
         
        """
        pass
    
    ## Setter for property: (str) SelectedItemString

    ##   the SelectedItemString.  
    ##    Valid only if SingleSelect is true. Otherwise empty string is returned.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @SelectedItemString.setter
    def SelectedItemString(self, string: str):
        """
        Setter for property: (str) SelectedItemString
          the SelectedItemString.  
           Valid only if SingleSelect is true. Otherwise empty string is returned.  
         
        """
        pass
    
    ## Getter for property: (bool) ShowAddButton
    ##   the ShowAddButton.  
    ##    If true, Add button is shown.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowAddButton(self) -> bool:
        """
        Getter for property: (bool) ShowAddButton
          the ShowAddButton.  
           If true, Add button is shown.  
         
        """
        pass
    
    ## Setter for property: (bool) ShowAddButton

    ##   the ShowAddButton.  
    ##    If true, Add button is shown.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowAddButton.setter
    def ShowAddButton(self, show: bool):
        """
        Setter for property: (bool) ShowAddButton
          the ShowAddButton.  
           If true, Add button is shown.  
         
        """
        pass
    
    ## Getter for property: (bool) ShowDeleteButton
    ##   the ShowDeleteButton.  
    ##    If true, Delete button is shown.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowDeleteButton(self) -> bool:
        """
        Getter for property: (bool) ShowDeleteButton
          the ShowDeleteButton.  
           If true, Delete button is shown.  
         
        """
        pass
    
    ## Setter for property: (bool) ShowDeleteButton

    ##   the ShowDeleteButton.  
    ##    If true, Delete button is shown.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowDeleteButton.setter
    def ShowDeleteButton(self, show: bool):
        """
        Setter for property: (bool) ShowDeleteButton
          the ShowDeleteButton.  
           If true, Delete button is shown.  
         
        """
        pass
    
    ## Getter for property: (bool) ShowMoveUpDownButtons
    ##   the ShowMoveUpDownButtons.  
    ##    If true, MoveUp and MoveDown buttons are shown.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowMoveUpDownButtons(self) -> bool:
        """
        Getter for property: (bool) ShowMoveUpDownButtons
          the ShowMoveUpDownButtons.  
           If true, MoveUp and MoveDown buttons are shown.  
         
        """
        pass
    
    ## Setter for property: (bool) ShowMoveUpDownButtons

    ##   the ShowMoveUpDownButtons.  
    ##    If true, MoveUp and MoveDown buttons are shown.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowMoveUpDownButtons.setter
    def ShowMoveUpDownButtons(self, show: bool):
        """
        Setter for property: (bool) ShowMoveUpDownButtons
          the ShowMoveUpDownButtons.  
           If true, MoveUp and MoveDown buttons are shown.  
         
        """
        pass
    
    ## Getter for property: (bool) SingleSelect
    ##   the SingleSelect.  
    ##    If true, only single item can be selected.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def SingleSelect(self) -> bool:
        """
        Getter for property: (bool) SingleSelect
          the SingleSelect.  
           If true, only single item can be selected.  
         
        """
        pass
    
    ## Setter for property: (bool) SingleSelect

    ##   the SingleSelect.  
    ##    If true, only single item can be selected.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @SingleSelect.setter
    def SingleSelect(self, sinle_select: bool):
        """
        Setter for property: (bool) SingleSelect
          the SingleSelect.  
           If true, only single item can be selected.  
         
        """
        pass
    
    ##  Add callback 
    ## A callback definition with the following input arguments: 
    ##  - @link ListBox NXOpen.BlockStyler.ListBox@endlink
    ##  and no return type
    AddCallback = Callable[[ListBox], None]
    
    
    ##  Delete callback.  Return a non-zero value in order to veto the deletion. 
    ## A callback definition with the following input arguments: 
    ##  - @link ListBox NXOpen.BlockStyler.ListBox@endlink
    ##  and no return type
    DeleteCallback = Callable[[ListBox], None]
    
    
    ##  Gets the ListItems
    ##  @return items (List[str]): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetListItems(list: ListBox) -> List[str]:
        """
         Gets the ListItems
         @return items (List[str]): .
        """
        pass
    
    ##  Gets the SelectedItemBooleans. This method returns an integer array of boolen values populated with 0 and 1
    ##  @return items (List[int]): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectedItemBooleans(list: ListBox) -> List[int]:
        """
         Gets the SelectedItemBooleans. This method returns an integer array of boolen values populated with 0 and 1
         @return items (List[int]): .
        """
        pass
    
    ##  Gets the SelectedItemStrings
    ##  @return strings (List[str]): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectedItemStrings(list: ListBox) -> List[str]:
        """
         Gets the SelectedItemStrings
         @return strings (List[str]): .
        """
        pass
    
    ##  Gets SelectedItems
    ##  @return selected_items (List[int]):  selected items.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectedItems(list: ListBox) -> List[int]:
        """
         Gets SelectedItems
         @return selected_items (List[int]):  selected items.
        """
        pass
    
    ##  Sets the Add handler.  This handler is called when the Add button is pressed.
    ##     The handler is responsible for adding an item to the list.  Nothing will be added to the list unless the handler
    ##     adds it. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetAddHandler(list: ListBox, cb: ListBox.AddCallback) -> None:
        """
         Sets the Add handler.  This handler is called when the Add button is pressed.
            The handler is responsible for adding an item to the list.  Nothing will be added to the list unless the handler
            adds it. 
        """
        pass
    
    ##  Sets the Delete handler.  If you set this handler, the handler will be
    ##     called when the Delete button is pressed.  The handler does not need to implement code
    ##     to delete the item.  The list will delete the selected items if and only if the handler returns 0. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetDeleteHandler(list: ListBox, cb: ListBox.DeleteCallback) -> None:
        """
         Sets the Delete handler.  If you set this handler, the handler will be
            called when the Delete button is pressed.  The handler does not need to implement code
            to delete the item.  The list will delete the selected items if and only if the handler returns 0. 
        """
        pass
    
    ##  Sets the ListItems
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="items"> (List[str]) </param>
    def SetListItems(list: ListBox, items: List[str]) -> None:
        """
         Sets the ListItems
        """
        pass
    
    ##  Sets the SelectedItemStrings. Selects the list items based on input boolean array. Item is deselcted if value is 0 and selected otherwise.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="items"> (List[int]) </param>
    def SetSelectedItemBooleans(list: ListBox, items: List[int]) -> None:
        """
         Sets the SelectedItemStrings. Selects the list items based on input boolean array. Item is deselcted if value is 0 and selected otherwise.
        """
        pass
    
    ##  Sets the SelectedItemStrings. Selects the list items based on input array of strings.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="strings"> (List[str]) </param>
    def SetSelectedItemStrings(list: ListBox, strings: List[str]) -> None:
        """
         Sets the SelectedItemStrings. Selects the list items based on input array of strings.
        """
        pass
    
    ##  Sets SelectedItems
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ##  selected items
    def SetSelectedItems(list: ListBox, selected_items: List[int]) -> None:
        """
         Sets SelectedItems
        """
        pass
    
    ## Tests item added event mapped to this ListBox block.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    @staticmethod
    def TestAddItem(list: ListBox) -> None:
        """
        Tests item added event mapped to this ListBox block.
        """
        pass
    
    ## Tests item delete event mapped to this ListBox block.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    @staticmethod
    def TestDeleteItem(list: ListBox) -> None:
        """
        Tests item delete event mapped to this ListBox block.
        """
        pass
    
import NXOpen
##  Class for validating NXMessageBox. Helpful for writing test cases on UI code. By default all message boxes are suppressed during Automated Testing except Question message boxes.
##     The class provides interface to validate message boxes that user is expecting to hit. It also provides interface to set choices for question message box.
## 
##   <br>  Created in NX2206.0.0  <br> 

class MessageBoxTester(NXOpen.TransientObject): 
    """ Class for validating NXMessageBox. Helpful for writing test cases on UI code. By default all message boxes are suppressed during Automated Testing except Question message boxes.
    The class provides interface to validate message boxes that user is expecting to hit. It also provides interface to set choices for question message box."""


    ##  Types of @link MessageBoxTester MessageBoxTester@endlink  choices when they are suppressed by automation program
    ##  Not a question message box.
    class Response(Enum):
        """
        Members Include: <NotQuestion> <Yes> <No>
        """
        NotQuestion: int
        Yes: int
        No: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MessageBoxTester.Response:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) SequenceCheck
    ##   the strict sequence checking flag for message validation.  
    ##    The sequence works in LIFO manner. When set to true, messages will be popped back from the input sequence.
    ##         By default, the messages are picked by searching from input sequence.  
    ##  
    ## Getter License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def SequenceCheck(self) -> bool:
        """
        Getter for property: (bool) SequenceCheck
          the strict sequence checking flag for message validation.  
           The sequence works in LIFO manner. When set to true, messages will be popped back from the input sequence.
                By default, the messages are picked by searching from input sequence.  
         
        """
        pass
    
    ## Setter for property: (bool) SequenceCheck

    ##   the strict sequence checking flag for message validation.  
    ##    The sequence works in LIFO manner. When set to true, messages will be popped back from the input sequence.
    ##         By default, the messages are picked by searching from input sequence.  
    ##  
    ## Setter License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @SequenceCheck.setter
    def SequenceCheck(self, check: bool):
        """
        Setter for property: (bool) SequenceCheck
          the strict sequence checking flag for message validation.  
           The sequence works in LIFO manner. When set to true, messages will be popped back from the input sequence.
                By default, the messages are picked by searching from input sequence.  
         
        """
        pass
    
    ##  Disposes the object.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(message_tester: MessageBoxTester) -> None:
        """
         Disposes the object.
        """
        pass
    
    ##  Suppress all @link NXMessageBox::DialogTypeQuestion NXMessageBox::DialogTypeQuestion@endlink  messages with a default choice
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ##  default choice for all question type message
    def SuppressAllQuestionMessageBox(message_tester: MessageBoxTester, choice: MessageBoxTester.Response) -> None:
        """
         Suppress all @link NXMessageBox::DialogTypeQuestion NXMessageBox::DialogTypeQuestion@endlink  messages with a default choice
        """
        pass
    
    ##  Adds a specific message for validation with given details. This method matches both message title and body.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ##  Title 
    def Validate(message_tester: MessageBoxTester, title: str, msgbox_type: NXOpen.NXMessageBox.DialogType, messages: List[str], choice: MessageBoxTester.Response) -> None:
        """
         Adds a specific message for validation with given details. This method matches both message title and body.
        """
        pass
    
    ##  Adds a specific message for validation with given details. Use this method when matching message body is not required
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ##  Title 
    def ValidateIgnoreBody(message_tester: MessageBoxTester, title: str, msgbox_type: NXOpen.NXMessageBox.DialogType, choice: MessageBoxTester.Response) -> None:
        """
         Adds a specific message for validation with given details. Use this method when matching message body is not required
        """
        pass
    
##  Represents a Microposition block
## 
##   <br>  Created in NX8.5.0  <br> 

class Microposition(UIBlock): 
    """ Represents a Microposition block"""
    pass


##  Represents a Multiline String block 
## 
##   <br>  Created in NX6.0.0  <br> 

class MultilineString(UIBlock): 
    """ Represents a Multiline String block """


    ## Getter for property: (int) Height
    ##   the Height  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def Height(self) -> int:
        """
        Getter for property: (int) Height
          the Height  
            
         
        """
        pass
    
    ## Setter for property: (int) Height

    ##   the Height  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Height.setter
    def Height(self, height: int):
        """
        Setter for property: (int) Height
          the Height  
            
         
        """
        pass
    
    ## Getter for property: (bool) Localize
    ##   the Localize.  
    ##    If true, the Label is translated to current locale language  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def Localize(self) -> bool:
        """
        Getter for property: (bool) Localize
          the Localize.  
           If true, the Label is translated to current locale language  
         
        """
        pass
    
    ## Setter for property: (bool) Localize

    ##   the Localize.  
    ##    If true, the Label is translated to current locale language  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Localize.setter
    def Localize(self, localize: bool):
        """
        Setter for property: (bool) Localize
          the Localize.  
           If true, the Label is translated to current locale language  
         
        """
        pass
    
    ## Getter for property: (int) MaximumCharactersAccepted
    ##   the MaximumCharactersAccepted  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def MaximumCharactersAccepted(self) -> int:
        """
        Getter for property: (int) MaximumCharactersAccepted
          the MaximumCharactersAccepted  
            
         
        """
        pass
    
    ## Setter for property: (int) MaximumCharactersAccepted

    ##   the MaximumCharactersAccepted  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MaximumCharactersAccepted.setter
    def MaximumCharactersAccepted(self, max_char: int):
        """
        Setter for property: (int) MaximumCharactersAccepted
          the MaximumCharactersAccepted  
            
         
        """
        pass
    
    ## Getter for property: (int) MaximumHeight
    ##   the MaximumHeight  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def MaximumHeight(self) -> int:
        """
        Getter for property: (int) MaximumHeight
          the MaximumHeight  
            
         
        """
        pass
    
    ## Setter for property: (int) MaximumHeight

    ##   the MaximumHeight  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MaximumHeight.setter
    def MaximumHeight(self, max_height: int):
        """
        Setter for property: (int) MaximumHeight
          the MaximumHeight  
            
         
        """
        pass
    
    ## Getter for property: (int) MinimumHeight
    ##   the MinimumHeight  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def MinimumHeight(self) -> int:
        """
        Getter for property: (int) MinimumHeight
          the MinimumHeight  
            
         
        """
        pass
    
    ## Setter for property: (int) MinimumHeight

    ##   the MinimumHeight  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MinimumHeight.setter
    def MinimumHeight(self, min_height: int):
        """
        Setter for property: (int) MinimumHeight
          the MinimumHeight  
            
         
        """
        pass
    
    ## Getter for property: (bool) ResizeHeightWithDialog
    ##   the ResizeHeightWithDialog.  
    ##    If true, height of block will dynamically change when the dialog is resized.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ResizeHeightWithDialog(self) -> bool:
        """
        Getter for property: (bool) ResizeHeightWithDialog
          the ResizeHeightWithDialog.  
           If true, height of block will dynamically change when the dialog is resized.  
         
        """
        pass
    
    ## Setter for property: (bool) ResizeHeightWithDialog

    ##   the ResizeHeightWithDialog.  
    ##    If true, height of block will dynamically change when the dialog is resized.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ResizeHeightWithDialog.setter
    def ResizeHeightWithDialog(self, resize: bool):
        """
        Setter for property: (bool) ResizeHeightWithDialog
          the ResizeHeightWithDialog.  
           If true, height of block will dynamically change when the dialog is resized.  
         
        """
        pass
    
    ## Getter for property: (bool) RetainValue
    ##   the RetainValue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def RetainValue(self) -> bool:
        """
        Getter for property: (bool) RetainValue
          the RetainValue  
            
         
        """
        pass
    
    ## Setter for property: (bool) RetainValue

    ##   the RetainValue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @RetainValue.setter
    def RetainValue(self, retain: bool):
        """
        Setter for property: (bool) RetainValue
          the RetainValue  
            
         
        """
        pass
    
    ## Getter for property: (str) ValuesConcatenated
    ##   the ValuesConcatenated.  
    ##    Represents single string with values in block concatenated with new-line characters.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def ValuesConcatenated(self) -> str:
        """
        Getter for property: (str) ValuesConcatenated
          the ValuesConcatenated.  
           Represents single string with values in block concatenated with new-line characters.  
         
        """
        pass
    
    ## Setter for property: (str) ValuesConcatenated

    ##   the ValuesConcatenated.  
    ##    Represents single string with values in block concatenated with new-line characters.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ValuesConcatenated.setter
    def ValuesConcatenated(self, value_string: str):
        """
        Setter for property: (str) ValuesConcatenated
          the ValuesConcatenated.  
           Represents single string with values in block concatenated with new-line characters.  
         
        """
        pass
    
    ## Getter for property: (int) Width
    ##   the Width  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def Width(self) -> int:
        """
        Getter for property: (int) Width
          the Width  
            
         
        """
        pass
    
    ## Setter for property: (int) Width

    ##   the Width  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Width.setter
    def Width(self, width: int):
        """
        Setter for property: (int) Width
          the Width  
            
         
        """
        pass
    
    ##  The Uncommitted Value. Represents the actual value user inputs in. 
    ##  @return uncommittedvalue_string (List[str]): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetUncommittedValue(multiline_string: MultilineString) -> List[str]:
        """
         The Uncommitted Value. Represents the actual value user inputs in. 
         @return uncommittedvalue_string (List[str]): .
        """
        pass
    
    ##  Gets the Value
    ##  @return value_string (List[str]): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetValue(multiline_string: MultilineString) -> List[str]:
        """
         Gets the Value
         @return value_string (List[str]): .
        """
        pass
    
    ##  Sets the Value
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="value_string"> (List[str]) </param>
    def SetValue(multiline_string: MultilineString, value_string: List[str]) -> None:
        """
         Sets the Value
        """
        pass
    
    ## Tests value changed event workflow mapped to this MultilineString block.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="value_string"> (List[str]) </param>
    def TestValueChanged(multiline_string: MultilineString, value_string: List[str]) -> None:
        """
        Tests value changed event workflow mapped to this MultilineString block.
        """
        pass
    
import NXOpen
## Represents the node created and utilized by @link BlockStyler::Tree BlockStyler::Tree@endlink .
##     The node represents the single row of the tree.
## 
##   <br>  Created in NX7.5.0  <br> 

class Node(NXOpen.TaggedObject): 
    """Represents the node created and utilized by <ja_class>BlockStyler.Tree</ja_class>.
    The node represents the single row of the tree."""


    ## Represents the drag type
    ## No drag
    class DragType(Enum):
        """
        Members Include: <NotSet> <All>
        """
        NotSet: int
        All: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Node.DragType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Represents the drop type
    ## Drop not permitted
    class DropType(Enum):
        """
        Members Include: <NotSet> <On> <Before> <After> <BeforeAndAfter>
        """
        NotSet: int
        On: int
        Before: int
        After: int
        BeforeAndAfter: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Node.DropType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Represents the Expand/Collapse option
    ## Use this option to collapse the node.
    class ExpandOption(Enum):
        """
        Members Include: <Collapse> <Expand> <Toggle>
        """
        Collapse: int
        Expand: int
        Toggle: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Node.ExpandOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Represents the scroll position to be applied on node. 
    ##         Use one of these options to make the node appear in tree window.
    ## Scrolls the tree to bring the node at the center of the tree window
    class Scroll(Enum):
        """
        Members Include: <Center> <LeastScroll> <MostScroll>
        """
        Center: int
        LeastScroll: int
        MostScroll: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Node.Scroll:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) CrossSelection
    ##  the flag indicating whether cross section is allowed.  
    ##    
    ##        It is useful when the node contains @link NXOpen::DisplayableObject NXOpen::DisplayableObject@endlink  as 
    ##        data. If the flag is true then the @link NXOpen::DisplayableObject NXOpen::DisplayableObject@endlink  is 
    ##        highlighted, else not. The default value is True  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return bool
    @property
    def CrossSelection(self) -> bool:
        """
        Getter for property: (bool) CrossSelection
         the flag indicating whether cross section is allowed.  
           
               It is useful when the node contains @link NXOpen::DisplayableObject NXOpen::DisplayableObject@endlink  as 
               data. If the flag is true then the @link NXOpen::DisplayableObject NXOpen::DisplayableObject@endlink  is 
               highlighted, else not. The default value is True  
         
        """
        pass
    
    ## Setter for property: (bool) CrossSelection

    ##  the flag indicating whether cross section is allowed.  
    ##    
    ##        It is useful when the node contains @link NXOpen::DisplayableObject NXOpen::DisplayableObject@endlink  as 
    ##        data. If the flag is true then the @link NXOpen::DisplayableObject NXOpen::DisplayableObject@endlink  is 
    ##        highlighted, else not. The default value is True  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @CrossSelection.setter
    def CrossSelection(self, crossSelection: bool):
        """
        Setter for property: (bool) CrossSelection
         the flag indicating whether cross section is allowed.  
           
               It is useful when the node contains @link NXOpen::DisplayableObject NXOpen::DisplayableObject@endlink  as 
               data. If the flag is true then the @link NXOpen::DisplayableObject NXOpen::DisplayableObject@endlink  is 
               highlighted, else not. The default value is True  
         
        """
        pass
    
    ## Getter for property: (str) DisplayIcon
    ##  the display icon.  
    ##    This is normal icon positioned before the node text and is 
    ##        displayed when the node is in unselected state.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return str
    @property
    def DisplayIcon(self) -> str:
        """
        Getter for property: (str) DisplayIcon
         the display icon.  
           This is normal icon positioned before the node text and is 
               displayed when the node is in unselected state.  
         
        """
        pass
    
    ## Setter for property: (str) DisplayIcon

    ##  the display icon.  
    ##    This is normal icon positioned before the node text and is 
    ##        displayed when the node is in unselected state.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @DisplayIcon.setter
    def DisplayIcon(self, icon: str):
        """
        Setter for property: (str) DisplayIcon
         the display icon.  
           This is normal icon positioned before the node text and is 
               displayed when the node is in unselected state.  
         
        """
        pass
    
    ## Getter for property: (str) DisplayText
    ##   the display text of node.  
    ##    This is same as 0th column text of this node. 
    ##        Use @link BlockStyler::Node::SetColumnDisplayText BlockStyler::Node::SetColumnDisplayText@endlink  to fetch the text of other column of the same node.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return str
    @property
    def DisplayText(self) -> str:
        """
        Getter for property: (str) DisplayText
          the display text of node.  
           This is same as 0th column text of this node. 
               Use @link BlockStyler::Node::SetColumnDisplayText BlockStyler::Node::SetColumnDisplayText@endlink  to fetch the text of other column of the same node.   
         
        """
        pass
    
    ## Setter for property: (str) DisplayText

    ##   the display text of node.  
    ##    This is same as 0th column text of this node. 
    ##        Use @link BlockStyler::Node::SetColumnDisplayText BlockStyler::Node::SetColumnDisplayText@endlink  to fetch the text of other column of the same node.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @DisplayText.setter
    def DisplayText(self, displayText: str):
        """
        Setter for property: (str) DisplayText
          the display text of node.  
           This is same as 0th column text of this node. 
               Use @link BlockStyler::Node::SetColumnDisplayText BlockStyler::Node::SetColumnDisplayText@endlink  to fetch the text of other column of the same node.   
         
        """
        pass
    
    ## Getter for property: (@link Node NXOpen.BlockStyler.Node@endlink) FirstChildNode
    ##  the first child node.  
    ##    Returns NULL if child node is not present.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return Node
    @property
    def FirstChildNode(self) -> Node:
        """
        Getter for property: (@link Node NXOpen.BlockStyler.Node@endlink) FirstChildNode
         the first child node.  
           Returns NULL if child node is not present.  
         
        """
        pass
    
    ## Getter for property: (int) ForegroundColor
    ##  the text color of the node.  
    ##    The color is applicable for whole row.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return int
    @property
    def ForegroundColor(self) -> int:
        """
        Getter for property: (int) ForegroundColor
         the text color of the node.  
           The color is applicable for whole row.  
         
        """
        pass
    
    ## Setter for property: (int) ForegroundColor

    ##  the text color of the node.  
    ##    The color is applicable for whole row.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @ForegroundColor.setter
    def ForegroundColor(self, nodeForgroundColor: int):
        """
        Setter for property: (int) ForegroundColor
         the text color of the node.  
           The color is applicable for whole row.  
         
        """
        pass
    
    ## Getter for property: (bool) IsExpanded
    ##   the flag indicating whether the node is in expanded state  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.3  <br> 

    ## @return bool
    @property
    def IsExpanded(self) -> bool:
        """
        Getter for property: (bool) IsExpanded
          the flag indicating whether the node is in expanded state  
            
         
        """
        pass
    
    ## Getter for property: (bool) IsInserted
    ##   the flag indicating whether the node is inserted in @link BlockStyler::Tree BlockStyler::Tree@endlink   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return bool
    @property
    def IsInserted(self) -> bool:
        """
        Getter for property: (bool) IsInserted
          the flag indicating whether the node is inserted in @link BlockStyler::Tree BlockStyler::Tree@endlink   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsSelected
    ##   the flag indicating whether the node is in selected state  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.3  <br> 

    ## @return bool
    @property
    def IsSelected(self) -> bool:
        """
        Getter for property: (bool) IsSelected
          the flag indicating whether the node is in selected state  
            
         
        """
        pass
    
    ## Getter for property: (@link Node NXOpen.BlockStyler.Node@endlink) NextNode
    ##  the next node which might not belong to the same hierarchy.  
    ##    
    ##        The next node either is a sibling node or belongs to other root node. 
    ##        Returns NULL if next node is not present  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return Node
    @property
    def NextNode(self) -> Node:
        """
        Getter for property: (@link Node NXOpen.BlockStyler.Node@endlink) NextNode
         the next node which might not belong to the same hierarchy.  
           
               The next node either is a sibling node or belongs to other root node. 
               Returns NULL if next node is not present  
         
        """
        pass
    
    ## Getter for property: (@link Node NXOpen.BlockStyler.Node@endlink) NextSelectedNode
    ##  the next selected node in the whole tree hierarchy.  
    ##    The node on which this method is called does not have to be selected. Returns NULL if none of the next nodes are selected.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return Node
    @property
    def NextSelectedNode(self) -> Node:
        """
        Getter for property: (@link Node NXOpen.BlockStyler.Node@endlink) NextSelectedNode
         the next selected node in the whole tree hierarchy.  
           The node on which this method is called does not have to be selected. Returns NULL if none of the next nodes are selected.  
         
        """
        pass
    
    ## Getter for property: (@link Node NXOpen.BlockStyler.Node@endlink) NextSiblingNode
    ##   the next node which belongs to the same hierarchy.  
    ##    
    ##        Returns NULL null if next sibling node is not present.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return Node
    @property
    def NextSiblingNode(self) -> Node:
        """
        Getter for property: (@link Node NXOpen.BlockStyler.Node@endlink) NextSiblingNode
          the next node which belongs to the same hierarchy.  
           
               Returns NULL null if next sibling node is not present.  
         
        """
        pass
    
    ## Getter for property: (@link Node NXOpen.BlockStyler.Node@endlink) ParentNode
    ##  the parent node.  
    ##    Returns NULL if parent node is not present  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return Node
    @property
    def ParentNode(self) -> Node:
        """
        Getter for property: (@link Node NXOpen.BlockStyler.Node@endlink) ParentNode
         the parent node.  
           Returns NULL if parent node is not present  
         
        """
        pass
    
    ## Getter for property: (@link Node NXOpen.BlockStyler.Node@endlink) PreviousNode
    ##  the previous node which might not belong to the same hierarchy.  
    ##    
    ##        Returns NULL null if previous node is not present  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return Node
    @property
    def PreviousNode(self) -> Node:
        """
        Getter for property: (@link Node NXOpen.BlockStyler.Node@endlink) PreviousNode
         the previous node which might not belong to the same hierarchy.  
           
               Returns NULL null if previous node is not present  
         
        """
        pass
    
    ## Getter for property: (@link Node NXOpen.BlockStyler.Node@endlink) PreviousSelectedNode
    ##  the previous selected node in the whole tree hierarchy.  
    ##    The node on which this method is called does not have to be selected.
    ##        Returns NULL if none of the previous nodes are selected.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return Node
    @property
    def PreviousSelectedNode(self) -> Node:
        """
        Getter for property: (@link Node NXOpen.BlockStyler.Node@endlink) PreviousSelectedNode
         the previous selected node in the whole tree hierarchy.  
           The node on which this method is called does not have to be selected.
               Returns NULL if none of the previous nodes are selected.  
         
        """
        pass
    
    ## Getter for property: (@link Node NXOpen.BlockStyler.Node@endlink) PreviousSiblingNode
    ##  the previous node which belongs to the same hierarchy.  
    ##    
    ##        Returns NULL if previous sibling node is not present.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return Node
    @property
    def PreviousSiblingNode(self) -> Node:
        """
        Getter for property: (@link Node NXOpen.BlockStyler.Node@endlink) PreviousSiblingNode
         the previous node which belongs to the same hierarchy.  
           
               Returns NULL if previous sibling node is not present.  
         
        """
        pass
    
    ## Getter for property: (str) SelectedIcon
    ##  the selected icon.  
    ##    This icon appears on node selection and is positioned before the node text
    ##        replacing the @link BlockStyler::Node::DisplayIcon BlockStyler::Node::DisplayIcon@endlink .  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return str
    @property
    def SelectedIcon(self) -> str:
        """
        Getter for property: (str) SelectedIcon
         the selected icon.  
           This icon appears on node selection and is positioned before the node text
               replacing the @link BlockStyler::Node::DisplayIcon BlockStyler::Node::DisplayIcon@endlink .  
         
        """
        pass
    
    ## Setter for property: (str) SelectedIcon

    ##  the selected icon.  
    ##    This icon appears on node selection and is positioned before the node text
    ##        replacing the @link BlockStyler::Node::DisplayIcon BlockStyler::Node::DisplayIcon@endlink .  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @SelectedIcon.setter
    def SelectedIcon(self, icon: str):
        """
        Setter for property: (str) SelectedIcon
         the selected icon.  
           This icon appears on node selection and is positioned before the node text
               replacing the @link BlockStyler::Node::DisplayIcon BlockStyler::Node::DisplayIcon@endlink .  
         
        """
        pass
    
    ## Expands/collapses the node
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Expand option
    def Expand(self, expandOption: Node.ExpandOption) -> None:
        """
        Expands/collapses the node
        """
        pass
    
    ## Gets the column text for the given columnId. 
    ##        The text is interpreted as icon if the column display type is  
    ##        @link BlockStyler::Tree::ColumnDisplayIcon BlockStyler::Tree::ColumnDisplayIcon@endlink .
    ##  @return columnDisplayText (str): Text associated with column.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Unique column id of the column.
    def GetColumnDisplayText(self, columnID: int) -> str:
        """
        Gets the column text for the given columnId. 
               The text is interpreted as icon if the column display type is  
               @link BlockStyler::Tree::ColumnDisplayIcon BlockStyler::Tree::ColumnDisplayIcon@endlink .
         @return columnDisplayText (str): Text associated with column.
        """
        pass
    
    ##   @brief  Gets node data which contains the data in the form of unique name-value pairs. 
    ##         In this context unique name is termed as property name. There 
    ##         could me more than one such property name - value pair, but the property name of the primary data 
    ##         should be named "Data" (case-sensitive). For instance, if a @link BlockStyler::Node BlockStyler::Node@endlink  represents a 
    ##         feature object then property name should be "Data" and the value should be feature object. The primary data is used by NX 
    ##         for some operations such cross selection. 
    ## 
    ##  
    ##          <br> 
    ##         Initialy the container or list is empty and it is expected that data 
    ##         would be added to it. Additional property name - value pair can be added to the container or list, but it should be made sure that
    ##         there is no dublicate property name exists in the container or list. The additional data can be seen as 
    ##         book keeping information for node. At any point the node data can be fetched and value can be extracted
    ##         using the corresponding property name. Refer to @link NXOpen::DataContainer NXOpen::DataContainer@endlink  on how property name-value pair is added
    ##         to the container or list.
    ##          <br> 
    ##        
    ##  @return nodeData (@link NXOpen.DataContainer NXOpen.DataContainer@endlink): Node data which is list of property name - value pair. New property name - value pair can be added to it and existing value can be fetched using corresponding property name.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    def GetNodeData(self) -> NXOpen.DataContainer:
        """
          @brief  Gets node data which contains the data in the form of unique name-value pairs. 
                In this context unique name is termed as property name. There 
                could me more than one such property name - value pair, but the property name of the primary data 
                should be named "Data" (case-sensitive). For instance, if a @link BlockStyler::Node BlockStyler::Node@endlink  represents a 
                feature object then property name should be "Data" and the value should be feature object. The primary data is used by NX 
                for some operations such cross selection. 
        
         
                 <br> 
                Initialy the container or list is empty and it is expected that data 
                would be added to it. Additional property name - value pair can be added to the container or list, but it should be made sure that
                there is no dublicate property name exists in the container or list. The additional data can be seen as 
                book keeping information for node. At any point the node data can be fetched and value can be extracted
                using the corresponding property name. Refer to @link NXOpen::DataContainer NXOpen::DataContainer@endlink  on how property name-value pair is added
                to the container or list.
                 <br> 
               
         @return nodeData (@link NXOpen.DataContainer NXOpen.DataContainer@endlink): Node data which is list of property name - value pair. New property name - value pair can be added to it and existing value can be fetched using corresponding property name.
        """
        pass
    
    ## Gets the node state associated with node state icon. Node state is an iconic 
    ##        representation, e.g., checked/unchecked icons for corresponding state. Node state 
    ##        value 1 and 2 represents the standard checked and unchecked state respectively.
    ##  @return state (int): Node state.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    def GetState(self) -> int:
        """
        Gets the node state associated with node state icon. Node state is an iconic 
               representation, e.g., checked/unchecked icons for corresponding state. Node state 
               value 1 and 2 represents the standard checked and unchecked state respectively.
         @return state (int): Node state.
        """
        pass
    
    ## Scrolls horizontally and vertically to make the specific column of 
    ##         node appear on the tree window.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## ColumnId of the column to which tree window scrolls horizontally.
    def ScrollTo(self, columnID: int, visibleOption: Node.Scroll) -> None:
        """
        Scrolls horizontally and vertically to make the specific column of 
                node appear on the tree window.
        """
        pass
    
    ## Sets the text in the column which corresponds to given columnId. 
    ##        The text is interpreted as icon if the column display type is  
    ##        @link BlockStyler::Tree::ColumnDisplayIcon BlockStyler::Tree::ColumnDisplayIcon@endlink .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Unique coulmn id of the column.
    def SetColumnDisplayText(self, columnID: int, columnDisplayText: str) -> None:
        """
        Sets the text in the column which corresponds to given columnId. 
               The text is interpreted as icon if the column display type is  
               @link BlockStyler::Tree::ColumnDisplayIcon BlockStyler::Tree::ColumnDisplayIcon@endlink .
        """
        pass
    
    ## Sets the node state which is associated with node state icon. Node state is an iconic 
    ##        representation, e.g., checked/unchecked state. Setting node state to value other 
    ##        than 1 and 2 calls BlockStyler.Tree.StateIconName callback to fetch
    ##        the icon name. Node state can be set only after the node has been added to TreeList.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Node state
    def SetState(self, state: int) -> None:
        """
        Sets the node state which is associated with node state icon. Node state is an iconic 
               representation, e.g., checked/unchecked state. Setting node state to value other 
               than 1 and 2 calls BlockStyler.Tree.StateIconName callback to fetch
               the icon name. Node state can be set only after the node has been added to TreeList.
        """
        pass
    
##  Represents an Object Color Picker Block
## 
##   <br>  Created in NX8.5.0  <br> 

class ObjectColorPicker(UIBlock): 
    """ Represents an Object Color Picker Block"""


    ## Getter for property: (str) BalloonTooltipImage
    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipImage

    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipLayoutAsString
    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipLayoutAsString

    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipText
    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipText

    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipText.setter
    def BalloonTooltipText(self, tooltipText: str):
        """
        Setter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Getter for property: (bool) Localize
    ##   the Localize.  
    ##    If true, translates the Label string into the language of the current locale.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def Localize(self) -> bool:
        """
        Getter for property: (bool) Localize
          the Localize.  
           If true, translates the Label string into the language of the current locale.  
         
        """
        pass
    
    ## Setter for property: (bool) Localize

    ##   the Localize.  
    ##    If true, translates the Label string into the language of the current locale.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Localize.setter
    def Localize(self, localize: bool):
        """
        Setter for property: (bool) Localize
          the Localize.  
           If true, translates the Label string into the language of the current locale.  
         
        """
        pass
    
    ## Getter for property: (int) NumberSelectable
    ##   the NumberSelectable.  
    ##    Represents number of colors that can be selected  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def NumberSelectable(self) -> int:
        """
        Getter for property: (int) NumberSelectable
          the NumberSelectable.  
           Represents number of colors that can be selected  
         
        """
        pass
    
    ## Setter for property: (int) NumberSelectable

    ##   the NumberSelectable.  
    ##    Represents number of colors that can be selected  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @NumberSelectable.setter
    def NumberSelectable(self, number: int):
        """
        Setter for property: (int) NumberSelectable
          the NumberSelectable.  
           Represents number of colors that can be selected  
         
        """
        pass
    
    ## Getter for property: (bool) RetainValue
    ##   the RetainValue.  
    ##    If true, block's value will be stored in dialog memory upon OK, Apply or Close.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def RetainValue(self) -> bool:
        """
        Getter for property: (bool) RetainValue
          the RetainValue.  
           If true, block's value will be stored in dialog memory upon OK, Apply or Close.  
         
        """
        pass
    
    ## Setter for property: (bool) RetainValue

    ##   the RetainValue.  
    ##    If true, block's value will be stored in dialog memory upon OK, Apply or Close.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @RetainValue.setter
    def RetainValue(self, retain: bool):
        """
        Setter for property: (bool) RetainValue
          the RetainValue.  
           If true, block's value will be stored in dialog memory upon OK, Apply or Close.  
         
        """
        pass
    
    ##  Gets theBalloonTooltipLayout members 
    ##  @return layout_strings (List[str]): Values to get from the property .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBalloonTooltipLayoutMembers(color_picker: ObjectColorPicker) -> List[str]:
        """
         Gets theBalloonTooltipLayout members 
         @return layout_strings (List[str]): Values to get from the property .
        """
        pass
    
    ##  Gets the Value
    ##  @return value_vector (List[int]): Values to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetValue(color_picker: ObjectColorPicker) -> List[int]:
        """
         Gets the Value
         @return value_vector (List[int]): Values to get from the property.
        """
        pass
    
    ##  Sets the Value
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## Values to set for the property. 
    def SetValue(color_picker: ObjectColorPicker, value_vector: List[int]) -> None:
        """
         Sets the Value
        """
        pass
    
    ## Tests value changed event workflow mapped to this object ObjectColorPicker block.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## Values to set for the property. 
    def TestValueChanged(color_picker: ObjectColorPicker, value_vector: List[int]) -> None:
        """
        Tests value changed event workflow mapped to this object ObjectColorPicker block.
        """
        pass
    
import NXOpen
##  Represents a On Path Dimension block
## 
##   <br>  Created in NX8.5.0  <br> 

class OnPathDimension(UIBlock): 
    """ Represents a On Path Dimension block"""


    ## Getter for property: (bool) AdaptiveScaleLimits
    ##  the AdaptiveScaleLimits.  
    ##   
    ##         If true, indicates that the scale should be adaptive.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def AdaptiveScaleLimits(self) -> bool:
        """
        Getter for property: (bool) AdaptiveScaleLimits
         the AdaptiveScaleLimits.  
          
                If true, indicates that the scale should be adaptive.  
         
        """
        pass
    
    ## Setter for property: (bool) AdaptiveScaleLimits

    ##  the AdaptiveScaleLimits.  
    ##   
    ##         If true, indicates that the scale should be adaptive.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @AdaptiveScaleLimits.setter
    def AdaptiveScaleLimits(self, scale_limits: bool):
        """
        Setter for property: (bool) AdaptiveScaleLimits
         the AdaptiveScaleLimits.  
          
                If true, indicates that the scale should be adaptive.  
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipImage
    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipImage

    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipLayoutAsString
    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipLayoutAsString

    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipText
    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipText

    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ExpressionObject
    ##   the ExpressionObject  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def ExpressionObject(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ExpressionObject
          the ExpressionObject  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ExpressionObject

    ##   the ExpressionObject  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ExpressionObject.setter
    def ExpressionObject(self, expression_obj: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ExpressionObject
          the ExpressionObject  
            
         
        """
        pass
    
    ## Getter for property: (str) Formula
    ##   the Formula  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Formula(self) -> str:
        """
        Getter for property: (str) Formula
          the Formula  
            
         
        """
        pass
    
    ## Setter for property: (str) Formula

    ##   the Formula  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Formula.setter
    def Formula(self, formula: str):
        """
        Setter for property: (str) Formula
          the Formula  
            
         
        """
        pass
    
    ## Getter for property: (float) LineIncrement
    ##  the LineIncrement value.  
    ##   
    ##         Specifies the increment/decrement when the user presses the arrow keys on the keyboard.
    ##         Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def LineIncrement(self) -> float:
        """
        Getter for property: (float) LineIncrement
         the LineIncrement value.  
          
                Specifies the increment/decrement when the user presses the arrow keys on the keyboard.
                Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
         
        """
        pass
    
    ## Setter for property: (float) LineIncrement

    ##  the LineIncrement value.  
    ##   
    ##         Specifies the increment/decrement when the user presses the arrow keys on the keyboard.
    ##         Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @LineIncrement.setter
    def LineIncrement(self, line_increment: float):
        """
        Setter for property: (float) LineIncrement
         the LineIncrement value.  
          
                Specifies the increment/decrement when the user presses the arrow keys on the keyboard.
                Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
         
        """
        pass
    
    ## Getter for property: (str) LocationOptionAsString
    ##   the LocationOption as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def LocationOptionAsString(self) -> str:
        """
        Getter for property: (str) LocationOptionAsString
          the LocationOption as string  
            
         
        """
        pass
    
    ## Setter for property: (str) LocationOptionAsString

    ##   the LocationOption as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @LocationOptionAsString.setter
    def LocationOptionAsString(self, enumString: str):
        """
        Setter for property: (str) LocationOptionAsString
          the LocationOption as string  
            
         
        """
        pass
    
    ## Getter for property: (bool) MaxInclusive
    ##   the MaxInclusive  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def MaxInclusive(self) -> bool:
        """
        Getter for property: (bool) MaxInclusive
          the MaxInclusive  
            
         
        """
        pass
    
    ## Setter for property: (bool) MaxInclusive

    ##   the MaxInclusive  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MaxInclusive.setter
    def MaxInclusive(self, max_inclusive: bool):
        """
        Setter for property: (bool) MaxInclusive
          the MaxInclusive  
            
         
        """
        pass
    
    ## Getter for property: (float) MaximumValue
    ##   the MaximumValue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return float
    @property
    def MaximumValue(self) -> float:
        """
        Getter for property: (float) MaximumValue
          the MaximumValue  
            
         
        """
        pass
    
    ## Setter for property: (float) MaximumValue

    ##   the MaximumValue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MaximumValue.setter
    def MaximumValue(self, max_value: float):
        """
        Setter for property: (float) MaximumValue
          the MaximumValue  
            
         
        """
        pass
    
    ## Getter for property: (bool) MinInclusive
    ##   the MinInclusive  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def MinInclusive(self) -> bool:
        """
        Getter for property: (bool) MinInclusive
          the MinInclusive  
            
         
        """
        pass
    
    ## Setter for property: (bool) MinInclusive

    ##   the MinInclusive  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MinInclusive.setter
    def MinInclusive(self, min_inclusive: bool):
        """
        Setter for property: (bool) MinInclusive
          the MinInclusive  
            
         
        """
        pass
    
    ## Getter for property: (float) MinimumValue
    ##   the MinimumValue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return float
    @property
    def MinimumValue(self) -> float:
        """
        Getter for property: (float) MinimumValue
          the MinimumValue  
            
         
        """
        pass
    
    ## Setter for property: (float) MinimumValue

    ##   the MinimumValue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MinimumValue.setter
    def MinimumValue(self, min_value: float):
        """
        Setter for property: (float) MinimumValue
          the MinimumValue  
            
         
        """
        pass
    
    ## Getter for property: (int) OptionMask
    ##   the OptionMask  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def OptionMask(self) -> int:
        """
        Getter for property: (int) OptionMask
          the OptionMask  
            
         
        """
        pass
    
    ## Setter for property: (int) OptionMask

    ##   the OptionMask  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @OptionMask.setter
    def OptionMask(self, maskVal: int):
        """
        Setter for property: (int) OptionMask
          the OptionMask  
            
         
        """
        pass
    
    ## Getter for property: (str) OptionMenuTitle
    ##   the OptionMenuTitle  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def OptionMenuTitle(self) -> str:
        """
        Getter for property: (str) OptionMenuTitle
          the OptionMenuTitle  
            
         
        """
        pass
    
    ## Setter for property: (str) OptionMenuTitle

    ##   the OptionMenuTitle  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @OptionMenuTitle.setter
    def OptionMenuTitle(self, menuTitleText: str):
        """
        Setter for property: (str) OptionMenuTitle
          the OptionMenuTitle  
            
         
        """
        pass
    
    ## Getter for property: (float) PageIncrement
    ##  the PageIncrement value.  
    ##   
    ##         Specifies the increment/decrement when the user presses the Page Up or Page Down keys on the keyboard.
    ##         Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def PageIncrement(self) -> float:
        """
        Getter for property: (float) PageIncrement
         the PageIncrement value.  
          
                Specifies the increment/decrement when the user presses the Page Up or Page Down keys on the keyboard.
                Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
         
        """
        pass
    
    ## Setter for property: (float) PageIncrement

    ##  the PageIncrement value.  
    ##   
    ##         Specifies the increment/decrement when the user presses the Page Up or Page Down keys on the keyboard.
    ##         Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @PageIncrement.setter
    def PageIncrement(self, page_increment: float):
        """
        Setter for property: (float) PageIncrement
         the PageIncrement value.  
          
                Specifies the increment/decrement when the user presses the Page Up or Page Down keys on the keyboard.
                Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Path
    ##   the Path  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def Path(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Path
          the Path  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Path

    ##   the Path  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Path.setter
    def Path(self, path: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Path
          the Path  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowFocusHandle
    ##   the ShowFocusHandle  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowFocusHandle(self) -> bool:
        """
        Getter for property: (bool) ShowFocusHandle
          the ShowFocusHandle  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowFocusHandle

    ##   the ShowFocusHandle  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowFocusHandle.setter
    def ShowFocusHandle(self, show_focus: bool):
        """
        Setter for property: (bool) ShowFocusHandle
          the ShowFocusHandle  
            
         
        """
        pass
    
    ## Getter for property: (int) SnapPointTypesOnByDefault
    ##   the SnapPointTypesOnByDefault  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX9.0.0.  This call can be safely removed as this is now a no-op.  <br> 

    ## @return int
    @property
    def SnapPointTypesOnByDefault(self) -> int:
        """
        Getter for property: (int) SnapPointTypesOnByDefault
          the SnapPointTypesOnByDefault  
            
         
        """
        pass
    
    ## Setter for property: (int) SnapPointTypesOnByDefault

    ##   the SnapPointTypesOnByDefault  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX9.0.0.  This call can be safely removed as this is now a no-op.  <br> 

    @SnapPointTypesOnByDefault.setter
    def SnapPointTypesOnByDefault(self, point_type: int):
        """
        Setter for property: (int) SnapPointTypesOnByDefault
          the SnapPointTypesOnByDefault  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Units
    ##   the Units  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def Units(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Units
          the Units  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Units

    ##   the Units  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Units.setter
    def Units(self, units: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Units
          the Units  
            
         
        """
        pass
    
    ## Getter for property: (float) Value
    ##   the Value.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return float
    @property
    def Value(self) -> float:
        """
        Getter for property: (float) Value
          the Value.  
            
         
        """
        pass
    
    ## Setter for property: (float) Value

    ##   the Value.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Value.setter
    def Value(self, dimension_value: float):
        """
        Setter for property: (float) Value
          the Value.  
            
         
        """
        pass
    
    ## Getter for property: (bool) WithScale
    ##   the WithScale.  
    ##    If true,the slider bar is shown.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def WithScale(self) -> bool:
        """
        Getter for property: (bool) WithScale
          the WithScale.  
           If true,the slider bar is shown.  
         
        """
        pass
    
    ## Setter for property: (bool) WithScale

    ##   the WithScale.  
    ##    If true,the slider bar is shown.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @WithScale.setter
    def WithScale(self, with_scale: bool):
        """
        Setter for property: (bool) WithScale
          the WithScale.  
           If true,the slider bar is shown.  
         
        """
        pass
    
    ##  Gets the BalloonTooltipLayout members 
    ##  @return layout_strings (List[str]): Values to get from the property. .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBalloonTooltipLayoutMembers(onPathDimension: OnPathDimension) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         @return layout_strings (List[str]): Values to get from the property. .
        """
        pass
    
    ##  Gets the LocationOption members
    ##  @return locationOptionMembers (List[str]):  Values to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetLocationOptionMembers(onPathDimension: OnPathDimension) -> List[str]:
        """
         Gets the LocationOption members
         @return locationOptionMembers (List[str]):  Values to get from the property.
        """
        pass
    
    ## Tests dimension changed event workflow mapped to this OnPathDimension block.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="dimension_value"> (float) </param>
    def TestValueChanged(onPathDimension: OnPathDimension, dimension_value: float) -> None:
        """
        Tests dimension changed event workflow mapped to this OnPathDimension block.
        """
        pass
    
import NXOpen
##  Represents OrientXpress Block
## 
##   <br>  Created in NX8.5.0  <br> 

class OrientXpress(UIBlock): 
    """ Represents OrientXpress Block"""


    ## Getter for property: (str) DirectionAsString
    ##   the Direction as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def DirectionAsString(self) -> str:
        """
        Getter for property: (str) DirectionAsString
          the Direction as string  
            
         
        """
        pass
    
    ## Setter for property: (str) DirectionAsString

    ##   the Direction as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @DirectionAsString.setter
    def DirectionAsString(self, enumString: str):
        """
        Setter for property: (str) DirectionAsString
          the Direction as string  
            
         
        """
        pass
    
    ## Getter for property: (str) PlaneAsString
    ##   the Plane as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def PlaneAsString(self) -> str:
        """
        Getter for property: (str) PlaneAsString
          the Plane as string  
            
         
        """
        pass
    
    ## Setter for property: (str) PlaneAsString

    ##   the Plane as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @PlaneAsString.setter
    def PlaneAsString(self, enumString: str):
        """
        Setter for property: (str) PlaneAsString
          the Plane as string  
            
         
        """
        pass
    
    ## Getter for property: (str) ReferenceAsString
    ##   the Reference as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def ReferenceAsString(self) -> str:
        """
        Getter for property: (str) ReferenceAsString
          the Reference as string  
            
         
        """
        pass
    
    ## Setter for property: (str) ReferenceAsString

    ##   the Reference as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ReferenceAsString.setter
    def ReferenceAsString(self, enumString: str):
        """
        Setter for property: (str) ReferenceAsString
          the Reference as string  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ReferenceCsys
    ##   the ReferenceCsys  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def ReferenceCsys(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ReferenceCsys
          the ReferenceCsys  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ReferenceCsys

    ##   the ReferenceCsys  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ReferenceCsys.setter
    def ReferenceCsys(self, referenceCsys: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ReferenceCsys
          the ReferenceCsys  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowAxisSubBlock
    ##   the ShowAxisSubBlock  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowAxisSubBlock(self) -> bool:
        """
        Getter for property: (bool) ShowAxisSubBlock
          the ShowAxisSubBlock  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowAxisSubBlock

    ##   the ShowAxisSubBlock  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowAxisSubBlock.setter
    def ShowAxisSubBlock(self, show: bool):
        """
        Setter for property: (bool) ShowAxisSubBlock
          the ShowAxisSubBlock  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowPlaneSubBlock
    ##   the ShowPlaneSubBlock  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowPlaneSubBlock(self) -> bool:
        """
        Getter for property: (bool) ShowPlaneSubBlock
          the ShowPlaneSubBlock  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowPlaneSubBlock

    ##   the ShowPlaneSubBlock  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowPlaneSubBlock.setter
    def ShowPlaneSubBlock(self, show: bool):
        """
        Setter for property: (bool) ShowPlaneSubBlock
          the ShowPlaneSubBlock  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowReferenceSubBlock
    ##   the ShowReferenceSubBlock  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowReferenceSubBlock(self) -> bool:
        """
        Getter for property: (bool) ShowReferenceSubBlock
          the ShowReferenceSubBlock  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowReferenceSubBlock

    ##   the ShowReferenceSubBlock  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowReferenceSubBlock.setter
    def ShowReferenceSubBlock(self, show: bool):
        """
        Setter for property: (bool) ShowReferenceSubBlock
          the ShowReferenceSubBlock  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowSceneControl
    ##   the ShowSceneControl  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowSceneControl(self) -> bool:
        """
        Getter for property: (bool) ShowSceneControl
          the ShowSceneControl  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowSceneControl

    ##   the ShowSceneControl  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowSceneControl.setter
    def ShowSceneControl(self, show: bool):
        """
        Setter for property: (bool) ShowSceneControl
          the ShowSceneControl  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowXAxis
    ##   the ShowXAxis  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowXAxis(self) -> bool:
        """
        Getter for property: (bool) ShowXAxis
          the ShowXAxis  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowXAxis

    ##   the ShowXAxis  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowXAxis.setter
    def ShowXAxis(self, show: bool):
        """
        Setter for property: (bool) ShowXAxis
          the ShowXAxis  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowXYPlane
    ##   the ShowXYPlane  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowXYPlane(self) -> bool:
        """
        Getter for property: (bool) ShowXYPlane
          the ShowXYPlane  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowXYPlane

    ##   the ShowXYPlane  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowXYPlane.setter
    def ShowXYPlane(self, show: bool):
        """
        Setter for property: (bool) ShowXYPlane
          the ShowXYPlane  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowXZPlane
    ##   the ShowXZPlane  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowXZPlane(self) -> bool:
        """
        Getter for property: (bool) ShowXZPlane
          the ShowXZPlane  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowXZPlane

    ##   the ShowXZPlane  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowXZPlane.setter
    def ShowXZPlane(self, show: bool):
        """
        Setter for property: (bool) ShowXZPlane
          the ShowXZPlane  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowYAxis
    ##   the ShowYAxis  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowYAxis(self) -> bool:
        """
        Getter for property: (bool) ShowYAxis
          the ShowYAxis  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowYAxis

    ##   the ShowYAxis  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowYAxis.setter
    def ShowYAxis(self, show: bool):
        """
        Setter for property: (bool) ShowYAxis
          the ShowYAxis  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowYZPlane
    ##   the ShowYZPlane  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowYZPlane(self) -> bool:
        """
        Getter for property: (bool) ShowYZPlane
          the ShowYZPlane  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowYZPlane

    ##   the ShowYZPlane  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowYZPlane.setter
    def ShowYZPlane(self, show: bool):
        """
        Setter for property: (bool) ShowYZPlane
          the ShowYZPlane  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowZAxis
    ##   the ShowZAxis  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowZAxis(self) -> bool:
        """
        Getter for property: (bool) ShowZAxis
          the ShowZAxis  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowZAxis

    ##   the ShowZAxis  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowZAxis.setter
    def ShowZAxis(self, show: bool):
        """
        Setter for property: (bool) ShowZAxis
          the ShowZAxis  
            
         
        """
        pass
    
    ##  Gets Direction members
    ##  @return member_strings (List[str]): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetDirectionMembers(orientXpress: OrientXpress) -> List[str]:
        """
         Gets Direction members
         @return member_strings (List[str]): .
        """
        pass
    
    ##  Gets Plane members
    ##  @return member_strings (List[str]): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPlaneMembers(orientXpress: OrientXpress) -> List[str]:
        """
         Gets Plane members
         @return member_strings (List[str]): .
        """
        pass
    
    ##  Gets Reference members
    ##  @return member_strings (List[str]): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetReferenceMembers(orientXpress: OrientXpress) -> List[str]:
        """
         Gets Reference members
         @return member_strings (List[str]): .
        """
        pass
    
    ## Tests direction specified.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="enumString"> (str) </param>
    def TestDirectionSpecified(orientXpress: OrientXpress, enumString: str) -> None:
        """
        Tests direction specified.
        """
        pass
    
    ## Tests plane specified.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="enumString"> (str) </param>
    def TestPlaneSpecified(orientXpress: OrientXpress, enumString: str) -> None:
        """
        Tests plane specified.
        """
        pass
    
    ## Tests referenceCsys specified.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="referenceCsys"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def TestReferenceCsysSpecified(orientXpress: OrientXpress, referenceCsys: NXOpen.TaggedObject) -> None:
        """
        Tests referenceCsys specified.
        """
        pass
    
    ## Tests reference specified.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="enumString"> (str) </param>
    def TestReferenceSpecified(orientXpress: OrientXpress, enumString: str) -> None:
        """
        Tests reference specified.
        """
        pass
    
import NXOpen
import NXOpen.Select
##  Represents a list of properties 
## 
##   <br>  Created in NX6.0.0  <br> 

class PropertyList(NXOpen.TransientObject): 
    """ Represents a list of properties """


    ##  Indicates whether the properties in the list are named.
    ##  The properties are not named and
    ##                must be indexed through an integer index 
    class ListMode(Enum):
        """
        Members Include: <Indexed> <Named>
        """
        Indexed: int
        Named: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PropertyList.ListMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the property types.
    ## String
    class PropertyType(Enum):
        """
        Members Include: <String> <Double> <Logical> <Integer> <Enum> <Strings> <UIBlock> <Point> <Vector> <Bits> <TaggedObject> <Array> <IntegerMatrix2d> <DoubleMatrix2d> <TaggedObjectMatrix2d> <IntegerVector> <DoubleVector> <TaggedObjectVector> <File> <SelectionFilter> <Undefined>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PropertyList.PropertyType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (int) Length
    ##   the length of the list   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return int
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
          the length of the list   
            
         
        """
        pass
    
    ## Getter for property: (@link PropertyList.ListMode NXOpen.BlockStyler.PropertyList.ListMode@endlink) Mode
    ##   the mode of the list.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return PropertyList.ListMode
    @property
    def Mode(self) -> PropertyList.ListMode:
        """
        Getter for property: (@link PropertyList.ListMode NXOpen.BlockStyler.PropertyList.ListMode@endlink) Mode
          the mode of the list.  
            
         
        """
        pass
    
    ## Adds the filter members for the given property name. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    def AddFilterMembers(list: PropertyList, propertyName: str, members: List[NXOpen.Select.FilterMember]) -> None:
        """
        Adds the filter members for the given property name. 
        """
        pass
    
    ## Clears the filter for the given property name. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    def ClearFilter(list: PropertyList, propertyName: str) -> None:
        """
        Clears the filter for the given property name. 
        """
        pass
    
    ##  Frees the object from memory.  After this method is called,
    ##             it is illegal to use the object.  In .NET, this method is automatically
    ##             called when the object is deleted by the garbage collector. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                    it is illegal to use the object.  In .NET, this method is automatically
                    called when the object is deleted by the garbage collector. 
        """
        pass
    
    ## Gets the value for the given property name. Exception will be raised if invalid property name is used. 
    ##  @return value (@link PropertyList NXOpen.BlockStyler.PropertyList@endlink): Value to get for given property name. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    @overload
    def GetArray(self, list: PropertyList, propertyName: str) -> PropertyList:
        """
        Gets the value for the given property name. Exception will be raised if invalid property name is used. 
         @return value (@link PropertyList NXOpen.BlockStyler.PropertyList@endlink): Value to get for given property name. .
        """
        pass
    
    ## Gets the value for the given index. Exception will be raised if invalid index is used. 
    ##  @return value (@link PropertyList NXOpen.BlockStyler.PropertyList@endlink): Value to get for given index. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  Index 
    @overload
    def GetArray(self, list: PropertyList, propertyIndex: int) -> PropertyList:
        """
        Gets the value for the given index. Exception will be raised if invalid index is used. 
         @return value (@link PropertyList NXOpen.BlockStyler.PropertyList@endlink): Value to get for given index. .
        """
        pass
    
    ##  Gets the bits value for the given property name. Exception will be raised if invalid property name is used. 
    ##  @return bits_sc (int): Value to get for given property name.  .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    @overload
    def GetBits(self, list: PropertyList, propertyName: str) -> int:
        """
         Gets the bits value for the given property name. Exception will be raised if invalid property name is used. 
         @return bits_sc (int): Value to get for given property name.  .
        """
        pass
    
    ##  Gets the bits value for the given index. Exception will be raised if invalid index is used. 
    ##  @return bits_sc (int): Value to get for given index.  .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## index 
    @overload
    def GetBits(self, list: PropertyList, propertyIndex: int) -> int:
        """
         Gets the bits value for the given index. Exception will be raised if invalid index is used. 
         @return bits_sc (int): Value to get for given index.  .
        """
        pass
    
    ##  Gets the double value for the given property name. Exception will be raised if invalid property name is used. 
    ##  @return value (float): Value to get for given property name.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    def GetDouble(list: PropertyList, propertyName: str) -> float:
        """
         Gets the double value for the given property name. Exception will be raised if invalid property name is used. 
         @return value (float): Value to get for given property name.
        """
        pass
    
    ## Gets the double matrix for the given property name. Exception will be raised if invalid property name is used.
    ##             This is a two dimensional array encoded into a single array. 
    ##  @return A tuple consisting of (matrixValue, nRows, nColumns). 
    ##  - matrixValue is: List[float].Value to get for given property name. .
    ##  - nRows is: int. Number of Rows in the 2D matrix .
    ##  - nColumns is: int. Number of Columns in the 2D matrix .

    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    @staticmethod
    @overload
    def GetDoubleMatrix(self, list: PropertyList, propertyName: str) -> Tuple[List[float], int, int]:
        """
        Gets the double matrix for the given property name. Exception will be raised if invalid property name is used.
                    This is a two dimensional array encoded into a single array. 
         @return A tuple consisting of (matrixValue, nRows, nColumns). 
         - matrixValue is: List[float].Value to get for given property name. .
         - nRows is: int. Number of Rows in the 2D matrix .
         - nColumns is: int. Number of Columns in the 2D matrix .

        """
        pass
    
    ## Gets the double matrix for the given index. Exception will be raised if invalid index is used.
    ##             This is a two dimensional array encoded into a single array. 
    ##  @return A tuple consisting of (matrixValue, nRows, nColumns). 
    ##  - matrixValue is: List[float].Value to get for given index. .
    ##  - nRows is: int. Number of Rows in the 2D matrix .
    ##  - nColumns is: int. Number of Columns in the 2D matrix .

    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  Index 
    @staticmethod
    @overload
    def GetDoubleMatrix(self, list: PropertyList, propertyIndex: int) -> Tuple[List[float], int, int]:
        """
        Gets the double matrix for the given index. Exception will be raised if invalid index is used.
                    This is a two dimensional array encoded into a single array. 
         @return A tuple consisting of (matrixValue, nRows, nColumns). 
         - matrixValue is: List[float].Value to get for given index. .
         - nRows is: int. Number of Rows in the 2D matrix .
         - nColumns is: int. Number of Columns in the 2D matrix .

        """
        pass
    
    ## Gets the double vector for the given property name. Exception will be raised if invalid property name is used. 
    ##  @return doubleVector (List[float]): Value to get for given property name. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    @overload
    def GetDoubleVector(self, list: PropertyList, propertyName: str) -> List[float]:
        """
        Gets the double vector for the given property name. Exception will be raised if invalid property name is used. 
         @return doubleVector (List[float]): Value to get for given property name. .
        """
        pass
    
    ## Gets the double vector for the given index. Exception will be raised if invalid index is used. 
    ##  @return doubleVector (List[float]): Value to get for given index. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  Index
    @overload
    def GetDoubleVector(self, list: PropertyList, propertyIndex: int) -> List[float]:
        """
        Gets the double vector for the given index. Exception will be raised if invalid index is used. 
         @return doubleVector (List[float]): Value to get for given index. .
        """
        pass
    
    ##  Gets the double value for the given index. Exception will be raised if invalid index is used. 
    ##  @return value (float): Value to get for given index.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  Index
    def GetDouble(list: PropertyList, propertyIndex: int) -> float:
        """
         Gets the double value for the given index. Exception will be raised if invalid index is used. 
         @return value (float): Value to get for given index.
        """
        pass
    
    ## Gets the value for the given property name. Exception will be raised if invalid property name is used. 
    ##  @return value (int): Value to get for given property name. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    def GetEnum(list: PropertyList, propertyName: str) -> int:
        """
        Gets the value for the given property name. Exception will be raised if invalid property name is used. 
         @return value (int): Value to get for given property name. .
        """
        pass
    
    ## Gets the value for the given property name. Exception will be raised if invalid property name is used. 
    ##  @return value (str): Value to get for given property name. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    @overload
    def GetEnumAsString(self, styler_item: PropertyList, propertyName: str) -> str:
        """
        Gets the value for the given property name. Exception will be raised if invalid property name is used. 
         @return value (str): Value to get for given property name. .
        """
        pass
    
    ## Gets the value for the given index. Exception will be raised if invalid index is used. 
    ##  @return value (str): Value to get for given index. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  index 
    @overload
    def GetEnumAsString(self, styler_item: PropertyList, propertyIndex: int) -> str:
        """
        Gets the value for the given index. Exception will be raised if invalid index is used. 
         @return value (str): Value to get for given index. .
        """
        pass
    
    ## Gets the enum members for the given property of type enum. Exception will be raised if invalid property name is used. 
    ##  @return strings (List[str]): Value to get for given property name. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    @overload
    def GetEnumMembers(self, list: PropertyList, propertyName: str) -> List[str]:
        """
        Gets the enum members for the given property of type enum. Exception will be raised if invalid property name is used. 
         @return strings (List[str]): Value to get for given property name. .
        """
        pass
    
    ## Gets the enum members for the given property index. Exception will be raised if invalid property name is used. 
    ##  @return strings (List[str]): Value to get for given property index. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  Index 
    @overload
    def GetEnumMembers(self, list: PropertyList, propertyIndex: int) -> List[str]:
        """
        Gets the enum members for the given property index. Exception will be raised if invalid property name is used. 
         @return strings (List[str]): Value to get for given property index. .
        """
        pass
    
    ## Gets the value for the given index. Exception will be raised if invalid index is used. 
    ##  @return value (int): Value to get for given index. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  Index 
    def GetEnum(list: PropertyList, propertyIndex: int) -> int:
        """
        Gets the value for the given index. Exception will be raised if invalid index is used. 
         @return value (int): Value to get for given index. .
        """
        pass
    
    ## Gets the value for the given property name. Exception will be raised if invalid property name is used. 
    ##  @return value (str): Value to get for given property name. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    @overload
    def GetFile(self, list: PropertyList, propertyName: str) -> str:
        """
        Gets the value for the given property name. Exception will be raised if invalid property name is used. 
         @return value (str): Value to get for given property name. .
        """
        pass
    
    ## Gets the value for the given index. Exception will be raised if invalid index is used. 
    ##  @return value (str): Value to get for given index. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  Index 
    @overload
    def GetFile(self, list: PropertyList, propertyIndex: int) -> str:
        """
        Gets the value for the given index. Exception will be raised if invalid index is used. 
         @return value (str): Value to get for given index. .
        """
        pass
    
    ##  Gets the integer value for the given property name. Exception will be raised if invalid property name is used 
    ##  @return value (int): Value to get for given property name .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    def GetInteger(list: PropertyList, propertyName: str) -> int:
        """
         Gets the integer value for the given property name. Exception will be raised if invalid property name is used 
         @return value (int): Value to get for given property name .
        """
        pass
    
    ## Gets the integer matrix for the given property name. Exception will be raised if invalid property name is used.
    ##           This is a two dimensional array encoded into a single array. 
    ##  @return A tuple consisting of (matrixValue, nRows, nColumns). 
    ##  - matrixValue is: List[int].Value to get for given property name. .
    ##  - nRows is: int. Number of Rows in the 2D matrix .
    ##  - nColumns is: int. Number of Columns in the 2D matrix .

    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    @staticmethod
    @overload
    def GetIntegerMatrix(self, list: PropertyList, propertyName: str) -> Tuple[List[int], int, int]:
        """
        Gets the integer matrix for the given property name. Exception will be raised if invalid property name is used.
                  This is a two dimensional array encoded into a single array. 
         @return A tuple consisting of (matrixValue, nRows, nColumns). 
         - matrixValue is: List[int].Value to get for given property name. .
         - nRows is: int. Number of Rows in the 2D matrix .
         - nColumns is: int. Number of Columns in the 2D matrix .

        """
        pass
    
    ## Gets the integer matrix for the given index. Exception will be raised if invalid index is used.
    ##           This is a two dimensional array encoded into a single array. 
    ##  @return A tuple consisting of (matrixValue, nRows, nColumns). 
    ##  - matrixValue is: List[int].Value to get for given index. .
    ##  - nRows is: int. Number of Rows in the 2D matrix .
    ##  - nColumns is: int. Number of Columns in the 2D matrix .

    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  Index 
    @staticmethod
    @overload
    def GetIntegerMatrix(self, list: PropertyList, propertyIndex: int) -> Tuple[List[int], int, int]:
        """
        Gets the integer matrix for the given index. Exception will be raised if invalid index is used.
                  This is a two dimensional array encoded into a single array. 
         @return A tuple consisting of (matrixValue, nRows, nColumns). 
         - matrixValue is: List[int].Value to get for given index. .
         - nRows is: int. Number of Rows in the 2D matrix .
         - nColumns is: int. Number of Columns in the 2D matrix .

        """
        pass
    
    ## Gets the integer vector for the given property name. Exception will be raised if invalid property name is used. 
    ##  @return intVector (List[int]): Value to get for given property name. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    @overload
    def GetIntegerVector(self, list: PropertyList, propertyName: str) -> List[int]:
        """
        Gets the integer vector for the given property name. Exception will be raised if invalid property name is used. 
         @return intVector (List[int]): Value to get for given property name. .
        """
        pass
    
    ## Gets the integer vector for the given index. Exception will be raised if invalid index is used. 
    ##  @return intVector (List[int]): Value to get for given index. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Index
    @overload
    def GetIntegerVector(self, list: PropertyList, propertyIndex: int) -> List[int]:
        """
        Gets the integer vector for the given index. Exception will be raised if invalid index is used. 
         @return intVector (List[int]): Value to get for given index. .
        """
        pass
    
    ##  Gets the integer value for the given index. Exception will be raised if invalid index is used 
    ##  @return value (int): Value to get for given index .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Index
    def GetInteger(list: PropertyList, propertyIndex: int) -> int:
        """
         Gets the integer value for the given index. Exception will be raised if invalid index is used 
         @return value (int): Value to get for given index .
        """
        pass
    
    ##  Gets the logical value for the given property name. Exception will be raised if invalid property name is used. 
    ##  @return value (bool): Value to get for given property name.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    @overload
    def GetLogical(self, list: PropertyList, propertyName: str) -> bool:
        """
         Gets the logical value for the given property name. Exception will be raised if invalid property name is used. 
         @return value (bool): Value to get for given property name.
        """
        pass
    
    ##  Gets the logical value for the given index. Exception will be raised if invalid index is used. 
    ##  @return value (bool): Value to get for given index.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  Index 
    @overload
    def GetLogical(self, list: PropertyList, propertyIndex: int) -> bool:
        """
         Gets the logical value for the given index. Exception will be raised if invalid index is used. 
         @return value (bool): Value to get for given index.
        """
        pass
    
    ## Gets the point value for the given property name. Exception will be raised if invalid property name is used. 
    ##  @return point_sc (@link NXOpen.Point3d NXOpen.Point3d@endlink): Value to get for given property name. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    @overload
    def GetPoint(self, list: PropertyList, propertyName: str) -> NXOpen.Point3d:
        """
        Gets the point value for the given property name. Exception will be raised if invalid property name is used. 
         @return point_sc (@link NXOpen.Point3d NXOpen.Point3d@endlink): Value to get for given property name. .
        """
        pass
    
    ## Gets the point value for the given index. Exception will be raised if invalid index is used. 
    ##  @return point_sc (@link NXOpen.Point3d NXOpen.Point3d@endlink): Value to get for given index. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Index 
    @overload
    def GetPoint(self, list: PropertyList, propertyIndex: int) -> NXOpen.Point3d:
        """
        Gets the point value for the given index. Exception will be raised if invalid index is used. 
         @return point_sc (@link NXOpen.Point3d NXOpen.Point3d@endlink): Value to get for given index. .
        """
        pass
    
    ##  Returns a list of all the property names 
    ##  @return strings (List[str]): Property names .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPropertyNames(list: PropertyList) -> List[str]:
        """
         Returns a list of all the property names 
         @return strings (List[str]): Property names .
        """
        pass
    
    ##  Returns the property type for given property name 
    ##  @return value (@link PropertyList.PropertyType NXOpen.BlockStyler.PropertyList.PropertyType@endlink): Property type. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    @overload
    def GetPropertyType(self, list: PropertyList, propertyName: str) -> PropertyList.PropertyType:
        """
         Returns the property type for given property name 
         @return value (@link PropertyList.PropertyType NXOpen.BlockStyler.PropertyList.PropertyType@endlink): Property type. .
        """
        pass
    
    ##  Returns the property type for the Indexed property list. Don't use this method on Named property list 
    ##  @return value (@link PropertyList.PropertyType NXOpen.BlockStyler.PropertyList.PropertyType@endlink): Property type. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Index
    @overload
    def GetPropertyType(self, list: PropertyList, propertyIndex: int) -> PropertyList.PropertyType:
        """
         Returns the property type for the Indexed property list. Don't use this method on Named property list 
         @return value (@link PropertyList.PropertyType NXOpen.BlockStyler.PropertyList.PropertyType@endlink): Property type. .
        """
        pass
    
    ##  Gets the string value for the given property name. Exception will be raised if invalid property name is used. 
    ##  @return value (str): Value to get for given property name. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    @overload
    def GetString(self, styler_item: PropertyList, propertyName: str) -> str:
        """
         Gets the string value for the given property name. Exception will be raised if invalid property name is used. 
         @return value (str): Value to get for given property name. .
        """
        pass
    
    ##  Gets the string value for the given index. Exception will be raised if invalid index is used. 
    ##  @return value (str): Value to get for given index. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  Index
    @overload
    def GetString(self, styler_item: PropertyList, propertyIndex: int) -> str:
        """
         Gets the string value for the given index. Exception will be raised if invalid index is used. 
         @return value (str): Value to get for given index. .
        """
        pass
    
    ## Gets the strings value for the given property name. Exception will be raised if invalid property name is used. 
    ##  @return strings (List[str]): Value to get for given property name. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    @overload
    def GetStrings(self, list: PropertyList, propertyName: str) -> List[str]:
        """
        Gets the strings value for the given property name. Exception will be raised if invalid property name is used. 
         @return strings (List[str]): Value to get for given property name. .
        """
        pass
    
    ## Gets the strings value for the given index. Exception will be raised if invalid index is used. 
    ##  @return strings (List[str]): Value to get for given index. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  Index 
    @overload
    def GetStrings(self, list: PropertyList, propertyIndex: int) -> List[str]:
        """
        Gets the strings value for the given index. Exception will be raised if invalid index is used. 
         @return strings (List[str]): Value to get for given index. .
        """
        pass
    
    ## Gets the tagged object for the given property name. Exception will be raised if invalid property name is used. 
    ##  @return tagged_sc (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink): Value to get for given property name. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    def GetTaggedObject(list: PropertyList, propertyName: str) -> NXOpen.TaggedObject:
        """
        Gets the tagged object for the given property name. Exception will be raised if invalid property name is used. 
         @return tagged_sc (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink): Value to get for given property name. .
        """
        pass
    
    ## Gets the tagged object vector for the given property name. Exception will be raised if invalid property name is used. 
    ##  @return tagVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get for given property name. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    @overload
    def GetTaggedObjectVector(self, list: PropertyList, propertyName: str) -> List[NXOpen.TaggedObject]:
        """
        Gets the tagged object vector for the given property name. Exception will be raised if invalid property name is used. 
         @return tagVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get for given property name. .
        """
        pass
    
    ## Gets the tagged object vector for the given index. Exception will be raised if invalid index is used. 
    ##  @return tagVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get for given property name. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  Index
    @overload
    def GetTaggedObjectVector(self, list: PropertyList, propertyIndex: int) -> List[NXOpen.TaggedObject]:
        """
        Gets the tagged object vector for the given index. Exception will be raised if invalid index is used. 
         @return tagVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get for given property name. .
        """
        pass
    
    ## Gets the tagged object for the given index. Exception will be raised if invalid index is used. 
    ##  @return tagged_sc (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink): Value to get for given index. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Index
    def GetTaggedObject(list: PropertyList, propertyIndex: int) -> NXOpen.TaggedObject:
        """
        Gets the tagged object for the given index. Exception will be raised if invalid index is used. 
         @return tagged_sc (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink): Value to get for given index. .
        """
        pass
    
    ## Gets the UI Block for the given property name. Exception will be raised if invalid property name is used. 
    ##  @return uiblocks (@link UIBlock NXOpen.BlockStyler.UIBlock@endlink): Value to get for given property name. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    @overload
    def GetUIBlock(self, list: PropertyList, propertyName: str) -> UIBlock:
        """
        Gets the UI Block for the given property name. Exception will be raised if invalid property name is used. 
         @return uiblocks (@link UIBlock NXOpen.BlockStyler.UIBlock@endlink): Value to get for given property name. .
        """
        pass
    
    ## Gets the UI Block for the given index. Exception will be raised if invalid index is used. 
    ##  @return uiblocks (@link UIBlock NXOpen.BlockStyler.UIBlock@endlink): Value to get for given index. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  Index 
    @overload
    def GetUIBlock(self, list: PropertyList, propertyIndex: int) -> UIBlock:
        """
        Gets the UI Block for the given index. Exception will be raised if invalid index is used. 
         @return uiblocks (@link UIBlock NXOpen.BlockStyler.UIBlock@endlink): Value to get for given index. .
        """
        pass
    
    ## Gets the vector value for the given property name. Exception will be raised if invalid property name is used. 
    ##  @return vector (@link NXOpen.Vector3d NXOpen.Vector3d@endlink): Value to get for given property name. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    @overload
    def GetVector(self, list: PropertyList, propertyName: str) -> NXOpen.Vector3d:
        """
        Gets the vector value for the given property name. Exception will be raised if invalid property name is used. 
         @return vector (@link NXOpen.Vector3d NXOpen.Vector3d@endlink): Value to get for given property name. .
        """
        pass
    
    ## Gets the vector value for the given index. Exception will be raised if invalid index is used. 
    ##  @return vector (@link NXOpen.Vector3d NXOpen.Vector3d@endlink): Value to get for given index. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Index 
    @overload
    def GetVector(self, list: PropertyList, propertyIndex: int) -> NXOpen.Vector3d:
        """
        Gets the vector value for the given index. Exception will be raised if invalid index is used. 
         @return vector (@link NXOpen.Vector3d NXOpen.Vector3d@endlink): Value to get for given index. .
        """
        pass
    
    ## Removes the filter members for the given property name. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    def RemoveFilterMembers(list: PropertyList, propertyName: str, members: List[NXOpen.Select.FilterMember]) -> None:
        """
        Removes the filter members for the given property name. 
        """
        pass
    
    ## Sets the bits value for the given property name. Exception will be raised if invalid property name is used. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    def SetBits(list: PropertyList, propertyName: str, bits_sc: int) -> None:
        """
        Sets the bits value for the given property name. Exception will be raised if invalid property name is used. 
        """
        pass
    
    ## Sets the double value for the given property name. Exception will be raised if invalid property name is used. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    def SetDouble(list: PropertyList, propertyName: str, value: float) -> None:
        """
        Sets the double value for the given property name. Exception will be raised if invalid property name is used. 
        """
        pass
    
    ## Sets the double matrix for the given property name. Exception will be raised if invalid property name is used.
    ##           This is a two dimensional array encoded into a single array. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    def SetDoubleMatrix(list: PropertyList, propertyName: str, nRows: int, nColumns: int, matrixValue: List[float]) -> None:
        """
        Sets the double matrix for the given property name. Exception will be raised if invalid property name is used.
                  This is a two dimensional array encoded into a single array. 
        """
        pass
    
    ## Sets the double vector for the given property name. Exception will be raised if invalid property name is used. 
    ## 
    ##   <br>  Created in NX7.5.3  <br> 

    ## License requirements: None.
    ## Name of the property 
    def SetDoubleVector(list: PropertyList, propertyName: str, doubleVector: List[float]) -> None:
        """
        Sets the double vector for the given property name. Exception will be raised if invalid property name is used. 
        """
        pass
    
    ## Sets the value for the given property name. Exception will be raised if invalid property name is used. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    def SetEnum(list: PropertyList, propertyName: str, value: int) -> None:
        """
        Sets the value for the given property name. Exception will be raised if invalid property name is used. 
        """
        pass
    
    ##  Sets the value for the given property name. Exception will be raised if invalid property name is used. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    def SetEnumAsString(styler_item: PropertyList, propertyName: str, value: str) -> None:
        """
         Sets the value for the given property name. Exception will be raised if invalid property name is used. 
        """
        pass
    
    ## Sets the enum members for the given property of type enum. Exception will be raised if invalid property name is used. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    def SetEnumMembers(list: PropertyList, propertyName: str, stringArray: List[str]) -> None:
        """
        Sets the enum members for the given property of type enum. Exception will be raised if invalid property name is used. 
        """
        pass
    
    ## Sets the value for the given property name. Exception will be raised if invalid property name is used. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  Name of the property 
    def SetFile(list: PropertyList, propertyName: str, value: str) -> None:
        """
        Sets the value for the given property name. Exception will be raised if invalid property name is used. 
        """
        pass
    
    ##  Sets the integer value for the given property name. 
    ##             Exception will be raised if invalid property name is used.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    def SetInteger(list: PropertyList, propertyName: str, value: int) -> None:
        """
         Sets the integer value for the given property name. 
                    Exception will be raised if invalid property name is used.
        """
        pass
    
    ## Sets the integer matrix for the given property name. Exception will be raised if invalid property name is used.
    ##           This is a two dimensional array encoded into a single array. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    def SetIntegerMatrix(list: PropertyList, propertyName: str, nRows: int, nColumns: int, matrixValue: List[int]) -> None:
        """
        Sets the integer matrix for the given property name. Exception will be raised if invalid property name is used.
                  This is a two dimensional array encoded into a single array. 
        """
        pass
    
    ## Sets the integer vector for the given property name. Exception will be raised if invalid property name is used. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    def SetIntegerVector(list: PropertyList, propertyName: str, intVector: List[int]) -> None:
        """
        Sets the integer vector for the given property name. Exception will be raised if invalid property name is used. 
        """
        pass
    
    ## Sets the logical value for the given property name. Exception will be raised if invalid property name is used.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    def SetLogical(list: PropertyList, propertyName: str, value: bool) -> None:
        """
        Sets the logical value for the given property name. Exception will be raised if invalid property name is used.
        """
        pass
    
    ## Sets the point value for the given property name. Exception will be raised if invalid property name is used. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    def SetPoint(list: PropertyList, propertyName: str, point_sc: NXOpen.Point3d) -> None:
        """
        Sets the point value for the given property name. Exception will be raised if invalid property name is used. 
        """
        pass
    
    ## Sets the filter for the given property name. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    def SetSelectionFilter(list: PropertyList, propertyName: str, maskAction: NXOpen.Selection.SelectionAction, maskTriples: List[NXOpen.Selection.MaskTriple]) -> None:
        """
        Sets the filter for the given property name. 
        """
        pass
    
    ## Sets the string value for the given property name. Exception will be raised if invalid property name is used. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    def SetString(styler_item: PropertyList, propertyName: str, value: str) -> None:
        """
        Sets the string value for the given property name. Exception will be raised if invalid property name is used. 
        """
        pass
    
    ## Sets the strings value for the given property name. Exception will be raised if invalid property name is used. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    def SetStrings(list: PropertyList, propertyName: str, stringArray: List[str]) -> None:
        """
        Sets the strings value for the given property name. Exception will be raised if invalid property name is used. 
        """
        pass
    
    ## Sets the tagged object for the given property name. Exception will be raised if invalid property name is used. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    def SetTaggedObject(list: PropertyList, propertyName: str, tagged_sc: NXOpen.TaggedObject) -> None:
        """
        Sets the tagged object for the given property name. Exception will be raised if invalid property name is used. 
        """
        pass
    
    ## Sets the tagged object vector for the given property name. Exception will be raised if invalid property name is used. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property 
    def SetTaggedObjectVector(list: PropertyList, propertyName: str, tagVector: List[NXOpen.TaggedObject]) -> None:
        """
        Sets the tagged object vector for the given property name. Exception will be raised if invalid property name is used. 
        """
        pass
    
    ## Sets the vector value for the given property name. Exception will be raised if invalid property name is used. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Name of the property
    def SetVector(list: PropertyList, propertyName: str, vector: NXOpen.Vector3d) -> None:
        """
        Sets the vector value for the given property name. Exception will be raised if invalid property name is used. 
        """
        pass
    
import NXOpen
##  Represents a Radius Dimension block
## 
##   <br>  Created in NX8.5.0  <br> 

class RadiusDimension(UIBlock): 
    """ Represents a Radius Dimension block"""


    ## Getter for property: (bool) AdaptiveScaleLimits
    ##  the AdaptiveScaleLimits.  
    ##   
    ##         If true, indicates that the scale should be adaptive.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def AdaptiveScaleLimits(self) -> bool:
        """
        Getter for property: (bool) AdaptiveScaleLimits
         the AdaptiveScaleLimits.  
          
                If true, indicates that the scale should be adaptive.  
         
        """
        pass
    
    ## Setter for property: (bool) AdaptiveScaleLimits

    ##  the AdaptiveScaleLimits.  
    ##   
    ##         If true, indicates that the scale should be adaptive.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @AdaptiveScaleLimits.setter
    def AdaptiveScaleLimits(self, scale_limits: bool):
        """
        Setter for property: (bool) AdaptiveScaleLimits
         the AdaptiveScaleLimits.  
          
                If true, indicates that the scale should be adaptive.  
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipImage
    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipImage

    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipLayoutAsString
    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipLayoutAsString

    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipText
    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipText

    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ExpressionObject
    ##   the ExpressionObject  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def ExpressionObject(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ExpressionObject
          the ExpressionObject  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ExpressionObject

    ##   the ExpressionObject  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ExpressionObject.setter
    def ExpressionObject(self, expression_obj: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ExpressionObject
          the ExpressionObject  
            
         
        """
        pass
    
    ## Getter for property: (str) Formula
    ##   the Formula  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Formula(self) -> str:
        """
        Getter for property: (str) Formula
          the Formula  
            
         
        """
        pass
    
    ## Setter for property: (str) Formula

    ##   the Formula  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Formula.setter
    def Formula(self, formula: str):
        """
        Setter for property: (str) Formula
          the Formula  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) HandleOrientation
    ##   the HandleOrientation  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.Vector3d
    @property
    def HandleOrientation(self) -> NXOpen.Vector3d:
        """
        Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) HandleOrientation
          the HandleOrientation  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) HandleOrientation

    ##   the HandleOrientation  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @HandleOrientation.setter
    def HandleOrientation(self, orientation: NXOpen.Vector3d):
        """
        Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) HandleOrientation
          the HandleOrientation  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) HandleOrigin
    ##   the HandleOrigin  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def HandleOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) HandleOrigin
          the HandleOrigin  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) HandleOrigin

    ##   the HandleOrigin  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @HandleOrigin.setter
    def HandleOrigin(self, handle_orogin: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) HandleOrigin
          the HandleOrigin  
            
         
        """
        pass
    
    ## Getter for property: (float) LineIncrement
    ##  the LineIncrement value.  
    ##   
    ##         Specifies the increment/decrement when the user presses the arrow keys on the keyboard.
    ##         Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def LineIncrement(self) -> float:
        """
        Getter for property: (float) LineIncrement
         the LineIncrement value.  
          
                Specifies the increment/decrement when the user presses the arrow keys on the keyboard.
                Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
         
        """
        pass
    
    ## Setter for property: (float) LineIncrement

    ##  the LineIncrement value.  
    ##   
    ##         Specifies the increment/decrement when the user presses the arrow keys on the keyboard.
    ##         Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @LineIncrement.setter
    def LineIncrement(self, line_increment: float):
        """
        Setter for property: (float) LineIncrement
         the LineIncrement value.  
          
                Specifies the increment/decrement when the user presses the arrow keys on the keyboard.
                Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
         
        """
        pass
    
    ## Getter for property: (bool) MaxInclusive
    ##   the MaxInclusive  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def MaxInclusive(self) -> bool:
        """
        Getter for property: (bool) MaxInclusive
          the MaxInclusive  
            
         
        """
        pass
    
    ## Setter for property: (bool) MaxInclusive

    ##   the MaxInclusive  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MaxInclusive.setter
    def MaxInclusive(self, max_inclusive: bool):
        """
        Setter for property: (bool) MaxInclusive
          the MaxInclusive  
            
         
        """
        pass
    
    ## Getter for property: (float) MaximumValue
    ##   the MaximumValue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return float
    @property
    def MaximumValue(self) -> float:
        """
        Getter for property: (float) MaximumValue
          the MaximumValue  
            
         
        """
        pass
    
    ## Setter for property: (float) MaximumValue

    ##   the MaximumValue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MaximumValue.setter
    def MaximumValue(self, max_value: float):
        """
        Setter for property: (float) MaximumValue
          the MaximumValue  
            
         
        """
        pass
    
    ## Getter for property: (bool) MinInclusive
    ##   the MinInclusive  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def MinInclusive(self) -> bool:
        """
        Getter for property: (bool) MinInclusive
          the MinInclusive  
            
         
        """
        pass
    
    ## Setter for property: (bool) MinInclusive

    ##   the MinInclusive  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MinInclusive.setter
    def MinInclusive(self, min_inclusive: bool):
        """
        Setter for property: (bool) MinInclusive
          the MinInclusive  
            
         
        """
        pass
    
    ## Getter for property: (float) MinimumValue
    ##   the MinimumValue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return float
    @property
    def MinimumValue(self) -> float:
        """
        Getter for property: (float) MinimumValue
          the MinimumValue  
            
         
        """
        pass
    
    ## Setter for property: (float) MinimumValue

    ##   the MinimumValue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MinimumValue.setter
    def MinimumValue(self, min_value: float):
        """
        Setter for property: (float) MinimumValue
          the MinimumValue  
            
         
        """
        pass
    
    ## Getter for property: (float) PageIncrement
    ##  the PageIncrement value.  
    ##   
    ##         Specifies the increment/decrement when the user presses the Page Up or Page Down keys on the keyboard.
    ##         Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def PageIncrement(self) -> float:
        """
        Getter for property: (float) PageIncrement
         the PageIncrement value.  
          
                Specifies the increment/decrement when the user presses the Page Up or Page Down keys on the keyboard.
                Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
         
        """
        pass
    
    ## Setter for property: (float) PageIncrement

    ##  the PageIncrement value.  
    ##   
    ##         Specifies the increment/decrement when the user presses the Page Up or Page Down keys on the keyboard.
    ##         Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @PageIncrement.setter
    def PageIncrement(self, page_increment: float):
        """
        Setter for property: (float) PageIncrement
         the PageIncrement value.  
          
                Specifies the increment/decrement when the user presses the Page Up or Page Down keys on the keyboard.
                Only available when PresentationStyle  is set to Scale or ScaleKeyin.  
         
        """
        pass
    
    ## Getter for property: (bool) ShowFocusHandle
    ##   the ShowFocusHandle  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowFocusHandle(self) -> bool:
        """
        Getter for property: (bool) ShowFocusHandle
          the ShowFocusHandle  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowFocusHandle

    ##   the ShowFocusHandle  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowFocusHandle.setter
    def ShowFocusHandle(self, show_focus: bool):
        """
        Setter for property: (bool) ShowFocusHandle
          the ShowFocusHandle  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowHandle
    ##   the ShowHandle  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowHandle(self) -> bool:
        """
        Getter for property: (bool) ShowHandle
          the ShowHandle  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowHandle

    ##   the ShowHandle  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowHandle.setter
    def ShowHandle(self, show_handle: bool):
        """
        Setter for property: (bool) ShowHandle
          the ShowHandle  
            
         
        """
        pass
    
    ## Getter for property: (int) SnapPointTypesOnByDefault
    ##   the SnapPointTypesOnByDefault  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX9.0.0.  This call can be safely removed as this is now a no-op.  <br> 

    ## @return int
    @property
    def SnapPointTypesOnByDefault(self) -> int:
        """
        Getter for property: (int) SnapPointTypesOnByDefault
          the SnapPointTypesOnByDefault  
            
         
        """
        pass
    
    ## Setter for property: (int) SnapPointTypesOnByDefault

    ##   the SnapPointTypesOnByDefault  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX9.0.0.  This call can be safely removed as this is now a no-op.  <br> 

    @SnapPointTypesOnByDefault.setter
    def SnapPointTypesOnByDefault(self, point_type: int):
        """
        Setter for property: (int) SnapPointTypesOnByDefault
          the SnapPointTypesOnByDefault  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Units
    ##   the Units  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def Units(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Units
          the Units  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Units

    ##   the Units  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Units.setter
    def Units(self, units: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Units
          the Units  
            
         
        """
        pass
    
    ## Getter for property: (float) Value
    ##   the Value.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return float
    @property
    def Value(self) -> float:
        """
        Getter for property: (float) Value
          the Value.  
            
         
        """
        pass
    
    ## Setter for property: (float) Value

    ##   the Value.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Value.setter
    def Value(self, dimension_value: float):
        """
        Setter for property: (float) Value
          the Value.  
            
         
        """
        pass
    
    ## Getter for property: (bool) WithScale
    ##   the WithScale  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def WithScale(self) -> bool:
        """
        Getter for property: (bool) WithScale
          the WithScale  
            
         
        """
        pass
    
    ## Setter for property: (bool) WithScale

    ##   the WithScale  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @WithScale.setter
    def WithScale(self, with_scale: bool):
        """
        Setter for property: (bool) WithScale
          the WithScale  
            
         
        """
        pass
    
    ##  Gets the BalloonTooltipLayout member 
    ##  @return layout_strings (List[str]): Values to get from the property. .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBalloonTooltipLayoutMembers(radiusDim: RadiusDimension) -> List[str]:
        """
         Gets the BalloonTooltipLayout member 
         @return layout_strings (List[str]): Values to get from the property. .
        """
        pass
    
    ## Tests dimension changed event workflow mapped to this RadiusDimension block.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="dimension_value"> (float) </param>
    def TestValueChanged(radiusDim: RadiusDimension, dimension_value: float) -> None:
        """
        Tests dimension changed event workflow mapped to this RadiusDimension block.
        """
        pass
    
import NXOpen
##  Represents Reverse Direction block
## 
##   <br>  Created in NX8.5.0  <br> 

class ReverseDirection(UIBlock): 
    """ Represents Reverse Direction block"""


    ## Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) Direction
    ##   the Direction.  
    ##    It specifies the orientation of direction handle.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.Vector3d
    @property
    def Direction(self) -> NXOpen.Vector3d:
        """
        Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) Direction
          the Direction.  
           It specifies the orientation of direction handle.  
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) Direction

    ##   the Direction.  
    ##    It specifies the orientation of direction handle.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Direction.setter
    def Direction(self, direction: NXOpen.Vector3d):
        """
        Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) Direction
          the Direction.  
           It specifies the orientation of direction handle.  
         
        """
        pass
    
    ## Getter for property: (bool) Flip
    ##   the Flip.  
    ##    If true, the handle is flipped opposite of the direction.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def Flip(self) -> bool:
        """
        Getter for property: (bool) Flip
          the Flip.  
           If true, the handle is flipped opposite of the direction.  
         
        """
        pass
    
    ## Setter for property: (bool) Flip

    ##   the Flip.  
    ##    If true, the handle is flipped opposite of the direction.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Flip.setter
    def Flip(self, flip: bool):
        """
        Setter for property: (bool) Flip
          the Flip.  
           If true, the handle is flipped opposite of the direction.  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Origin
    ##   the Origin.  
    ##    It specifies the origin of direction handle.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def Origin(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Origin
          the Origin.  
           It specifies the origin of direction handle.  
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Origin

    ##   the Origin.  
    ##    It specifies the origin of direction handle.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Origin.setter
    def Origin(self, origin: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Origin
          the Origin.  
           It specifies the origin of direction handle.  
         
        """
        pass
    
    ## Tests the handle flipped.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="flip"> (bool) </param>
    def TestFlip(reverseDirection: ReverseDirection, flip: bool) -> None:
        """
        Tests the handle flipped.
        """
        pass
    
##  Represents a RGB Color Picker block
## 
##   <br>  Created in NX8.5.0  <br> 

class RGBColorPicker(UIBlock): 
    """ Represents a RGB Color Picker block"""


    ## Getter for property: (str) BalloonTooltipImage
    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipImage

    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipLayoutAsString
    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipLayoutAsString

    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipText
    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipText

    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipText.setter
    def BalloonTooltipText(self, tooltipText: str):
        """
        Setter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Getter for property: (bool) Localize
    ##   the Localize.  
    ##    If true, the Label is translated to current locale language.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def Localize(self) -> bool:
        """
        Getter for property: (bool) Localize
          the Localize.  
           If true, the Label is translated to current locale language.  
         
        """
        pass
    
    ## Setter for property: (bool) Localize

    ##   the Localize.  
    ##    If true, the Label is translated to current locale language.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Localize.setter
    def Localize(self, localize: bool):
        """
        Setter for property: (bool) Localize
          the Localize.  
           If true, the Label is translated to current locale language.  
         
        """
        pass
    
    ## Getter for property: (bool) RetainValue
    ##   the RetainValue.  
    ##    If true, the block's value will be saved in dialog memory upon OK, Apply or Close.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def RetainValue(self) -> bool:
        """
        Getter for property: (bool) RetainValue
          the RetainValue.  
           If true, the block's value will be saved in dialog memory upon OK, Apply or Close.  
         
        """
        pass
    
    ## Setter for property: (bool) RetainValue

    ##   the RetainValue.  
    ##    If true, the block's value will be saved in dialog memory upon OK, Apply or Close.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @RetainValue.setter
    def RetainValue(self, retain: bool):
        """
        Setter for property: (bool) RetainValue
          the RetainValue.  
           If true, the block's value will be saved in dialog memory upon OK, Apply or Close.  
         
        """
        pass
    
    ## Getter for property: (int) Value
    ##   the Value  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def Value(self) -> int:
        """
        Getter for property: (int) Value
          the Value  
            
         
        """
        pass
    
    ## Setter for property: (int) Value

    ##   the Value  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Value.setter
    def Value(self, rgb_value: int):
        """
        Setter for property: (int) Value
          the Value  
            
         
        """
        pass
    
    ##  Gets the BalloonTooltipLayout member 
    ##  @return layout_strings (List[str]): Values to get from the property. .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBalloonTooltipLayoutMembers(rgb_color_picker: RGBColorPicker) -> List[str]:
        """
         Gets the BalloonTooltipLayout member 
         @return layout_strings (List[str]): Values to get from the property. .
        """
        pass
    
    ## Tests value changed event workflow mapped to this RGB ColorPicker block.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="rgb_value"> (int) </param>
    def TestValueChanged(rgb_color_picker: RGBColorPicker, rgb_value: int) -> None:
        """
        Tests value changed event workflow mapped to this RGB ColorPicker block.
        """
        pass
    
##  Represents a Scrolled Window block
## 
##   <br>  Created in NX8.5.0  <br> 

class ScrolledWindow(UIBlock): 
    """ Represents a Scrolled Window block"""


    ## Getter for property: (int) Height
    ##   the Height  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def Height(self) -> int:
        """
        Getter for property: (int) Height
          the Height  
            
         
        """
        pass
    
    ## Setter for property: (int) Height

    ##   the Height  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Height.setter
    def Height(self, height: int):
        """
        Setter for property: (int) Height
          the Height  
            
         
        """
        pass
    
    ## Getter for property: (@link PropertyList NXOpen.BlockStyler.PropertyList@endlink) Members
    ##   the Members  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return PropertyList
    @property
    def Members(self) -> PropertyList:
        """
        Getter for property: (@link PropertyList NXOpen.BlockStyler.PropertyList@endlink) Members
          the Members  
            
         
        """
        pass
    
    ## Getter for property: (bool) ResizeHeightWithDialog
    ##   the ResizeHeightWithDialog.  
    ##    If true, the height of block will dynamically change when the dialog is resized.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ResizeHeightWithDialog(self) -> bool:
        """
        Getter for property: (bool) ResizeHeightWithDialog
          the ResizeHeightWithDialog.  
           If true, the height of block will dynamically change when the dialog is resized.  
         
        """
        pass
    
    ## Setter for property: (bool) ResizeHeightWithDialog

    ##   the ResizeHeightWithDialog.  
    ##    If true, the height of block will dynamically change when the dialog is resized.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ResizeHeightWithDialog.setter
    def ResizeHeightWithDialog(self, resize: bool):
        """
        Setter for property: (bool) ResizeHeightWithDialog
          the ResizeHeightWithDialog.  
           If true, the height of block will dynamically change when the dialog is resized.  
         
        """
        pass
    
    ## Getter for property: (int) Width
    ##   the Width  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def Width(self) -> int:
        """
        Getter for property: (int) Width
          the Width  
            
         
        """
        pass
    
    ## Setter for property: (int) Width

    ##   the Width  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Width.setter
    def Width(self, width: int):
        """
        Setter for property: (int) Width
          the Width  
            
         
        """
        pass
    
import NXOpen
##  Represents a Section Builder
## 
##   <br>  Created in NX8.5.0  <br> 

class SectionBuilder(UIBlock): 
    """ Represents a Section Builder"""


    ## Getter for property: (bool) AllowConvergentObject
    ##   the AllowConvergentObject  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def AllowConvergentObject(self) -> bool:
        """
        Getter for property: (bool) AllowConvergentObject
          the AllowConvergentObject  
            
         
        """
        pass
    
    ## Setter for property: (bool) AllowConvergentObject

    ##   the AllowConvergentObject  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @AllowConvergentObject.setter
    def AllowConvergentObject(self, allowConvergentObject: bool):
        """
        Setter for property: (bool) AllowConvergentObject
          the AllowConvergentObject  
            
         
        """
        pass
    
    ## Getter for property: (bool) AllowConvergentObjectWithMixedGeometries
    ##   the AllowConvergentObjectWithMixedGeometries  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2007.0.0.  This property is no longer relevant as hybrid selection is default ON now.  <br> 

    ## @return bool
    @property
    def AllowConvergentObjectWithMixedGeometries(self) -> bool:
        """
        Getter for property: (bool) AllowConvergentObjectWithMixedGeometries
          the AllowConvergentObjectWithMixedGeometries  
            
         
        """
        pass
    
    ## Setter for property: (bool) AllowConvergentObjectWithMixedGeometries

    ##   the AllowConvergentObjectWithMixedGeometries  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2007.0.0.  This property is no longer relevant as hybrid selection is default ON now.  <br> 

    @AllowConvergentObjectWithMixedGeometries.setter
    def AllowConvergentObjectWithMixedGeometries(self, allowConvergentObjectWithMixedGeometries: bool):
        """
        Setter for property: (bool) AllowConvergentObjectWithMixedGeometries
          the AllowConvergentObjectWithMixedGeometries  
            
         
        """
        pass
    
    ## Getter for property: (bool) AllowInferredCurveSelection
    ##   the AllowInferredCurveSelection  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def AllowInferredCurveSelection(self) -> bool:
        """
        Getter for property: (bool) AllowInferredCurveSelection
          the AllowInferredCurveSelection  
            
         
        """
        pass
    
    ## Setter for property: (bool) AllowInferredCurveSelection

    ##   the AllowInferredCurveSelection  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @AllowInferredCurveSelection.setter
    def AllowInferredCurveSelection(self, allow: bool):
        """
        Setter for property: (bool) AllowInferredCurveSelection
          the AllowInferredCurveSelection  
            
         
        """
        pass
    
    ## Getter for property: (bool) AllowStopAtIntersectionFollowFillet
    ##   the AllowStopAtIntersectionFollowFillet  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def AllowStopAtIntersectionFollowFillet(self) -> bool:
        """
        Getter for property: (bool) AllowStopAtIntersectionFollowFillet
          the AllowStopAtIntersectionFollowFillet  
            
         
        """
        pass
    
    ## Setter for property: (bool) AllowStopAtIntersectionFollowFillet

    ##   the AllowStopAtIntersectionFollowFillet  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @AllowStopAtIntersectionFollowFillet.setter
    def AllowStopAtIntersectionFollowFillet(self, allow: bool):
        """
        Setter for property: (bool) AllowStopAtIntersectionFollowFillet
          the AllowStopAtIntersectionFollowFillet  
            
         
        """
        pass
    
    ## Getter for property: (float) AngularTolerance
    ##   the AngularTolerance  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return float
    @property
    def AngularTolerance(self) -> float:
        """
        Getter for property: (float) AngularTolerance
          the AngularTolerance  
            
         
        """
        pass
    
    ## Setter for property: (float) AngularTolerance

    ##   the AngularTolerance  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @AngularTolerance.setter
    def AngularTolerance(self, tolerance: float):
        """
        Setter for property: (float) AngularTolerance
          the AngularTolerance  
            
         
        """
        pass
    
    ## Getter for property: (bool) AutomaticProgression
    ##   the AutomaticProgression.  
    ##    If true, focus automatically progresses to the next selection block.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def AutomaticProgression(self) -> bool:
        """
        Getter for property: (bool) AutomaticProgression
          the AutomaticProgression.  
           If true, focus automatically progresses to the next selection block.  
         
        """
        pass
    
    ## Setter for property: (bool) AutomaticProgression

    ##   the AutomaticProgression.  
    ##    If true, focus automatically progresses to the next selection block.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @AutomaticProgression.setter
    def AutomaticProgression(self, automaticProgression: bool):
        """
        Setter for property: (bool) AutomaticProgression
          the AutomaticProgression.  
           If true, focus automatically progresses to the next selection block.  
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipImage
    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipImage

    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipLayoutAsString
    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipLayoutAsString

    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipText
    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipText

    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Getter for property: (str) Bitmap
    ##   the Bitmap  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Bitmap(self) -> str:
        """
        Getter for property: (str) Bitmap
          the Bitmap  
            
         
        """
        pass
    
    ## Setter for property: (str) Bitmap

    ##   the Bitmap  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Bitmap.setter
    def Bitmap(self, bitmap_string: str):
        """
        Setter for property: (str) Bitmap
          the Bitmap  
            
         
        """
        pass
    
    ## Getter for property: (bool) BlendVirtualCurveOverlay
    ##   the BlendVirtualCurveOverlay  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def BlendVirtualCurveOverlay(self) -> bool:
        """
        Getter for property: (bool) BlendVirtualCurveOverlay
          the BlendVirtualCurveOverlay  
            
         
        """
        pass
    
    ## Setter for property: (bool) BlendVirtualCurveOverlay

    ##   the BlendVirtualCurveOverlay  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BlendVirtualCurveOverlay.setter
    def BlendVirtualCurveOverlay(self, blendCurve: bool):
        """
        Setter for property: (bool) BlendVirtualCurveOverlay
          the BlendVirtualCurveOverlay  
            
         
        """
        pass
    
    ## Getter for property: (bool) ChainWithinFeature
    ##   the ChainWithinFeature  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ChainWithinFeature(self) -> bool:
        """
        Getter for property: (bool) ChainWithinFeature
          the ChainWithinFeature  
            
         
        """
        pass
    
    ## Setter for property: (bool) ChainWithinFeature

    ##   the ChainWithinFeature  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ChainWithinFeature.setter
    def ChainWithinFeature(self, chainWithinFeature: bool):
        """
        Setter for property: (bool) ChainWithinFeature
          the ChainWithinFeature  
            
         
        """
        pass
    
    ## Getter for property: (bool) CreateInterpartLink
    ##   the CreateInterpartLink  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def CreateInterpartLink(self) -> bool:
        """
        Getter for property: (bool) CreateInterpartLink
          the CreateInterpartLink  
            
         
        """
        pass
    
    ## Setter for property: (bool) CreateInterpartLink

    ##   the CreateInterpartLink  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @CreateInterpartLink.setter
    def CreateInterpartLink(self, createLink: bool):
        """
        Setter for property: (bool) CreateInterpartLink
          the CreateInterpartLink  
            
         
        """
        pass
    
    ## Getter for property: (str) Cue
    ##   the Cue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Cue(self) -> str:
        """
        Getter for property: (str) Cue
          the Cue  
            
         
        """
        pass
    
    ## Setter for property: (str) Cue

    ##   the Cue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Cue.setter
    def Cue(self, cue: str):
        """
        Setter for property: (str) Cue
          the Cue  
            
         
        """
        pass
    
    ## Getter for property: (int) CurveRules
    ##   the CurveRules  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def CurveRules(self) -> int:
        """
        Getter for property: (int) CurveRules
          the CurveRules  
            
         
        """
        pass
    
    ## Setter for property: (int) CurveRules

    ##   the CurveRules  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @CurveRules.setter
    def CurveRules(self, curveRules: int):
        """
        Setter for property: (int) CurveRules
          the CurveRules  
            
         
        """
        pass
    
    ## Getter for property: (str) DefaultCurveRulesAsString
    ##   the DefaultCurveRules as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def DefaultCurveRulesAsString(self) -> str:
        """
        Getter for property: (str) DefaultCurveRulesAsString
          the DefaultCurveRules as string  
            
         
        """
        pass
    
    ## Setter for property: (str) DefaultCurveRulesAsString

    ##   the DefaultCurveRules as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @DefaultCurveRulesAsString.setter
    def DefaultCurveRulesAsString(self, enumString: str):
        """
        Setter for property: (str) DefaultCurveRulesAsString
          the DefaultCurveRules as string  
            
         
        """
        pass
    
    ## Getter for property: (int) EntityType
    ##   the EntityType  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def EntityType(self) -> int:
        """
        Getter for property: (int) EntityType
          the EntityType  
            
         
        """
        pass
    
    ## Setter for property: (int) EntityType

    ##   the EntityType  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @EntityType.setter
    def EntityType(self, entityType: int):
        """
        Setter for property: (int) EntityType
          the EntityType  
            
         
        """
        pass
    
    ## Getter for property: (bool) FollowFillet
    ##   the FollowFillet  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def FollowFillet(self) -> bool:
        """
        Getter for property: (bool) FollowFillet
          the FollowFillet  
            
         
        """
        pass
    
    ## Setter for property: (bool) FollowFillet

    ##   the FollowFillet  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @FollowFillet.setter
    def FollowFillet(self, followFillet: bool):
        """
        Setter for property: (bool) FollowFillet
          the FollowFillet  
            
         
        """
        pass
    
    ## Getter for property: (bool) InferredCurveSelection
    ##   the InferredCurveSelection  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def InferredCurveSelection(self) -> bool:
        """
        Getter for property: (bool) InferredCurveSelection
          the InferredCurveSelection  
            
         
        """
        pass
    
    ## Setter for property: (bool) InferredCurveSelection

    ##   the InferredCurveSelection  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @InferredCurveSelection.setter
    def InferredCurveSelection(self, selectInferredCurve: bool):
        """
        Setter for property: (bool) InferredCurveSelection
          the InferredCurveSelection  
            
         
        """
        pass
    
    ## Getter for property: (str) InterpartSelectionAsString
    ##   the InterpartSelection as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def InterpartSelectionAsString(self) -> str:
        """
        Getter for property: (str) InterpartSelectionAsString
          the InterpartSelection as string  
            
         
        """
        pass
    
    ## Setter for property: (str) InterpartSelectionAsString

    ##   the InterpartSelection as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @InterpartSelectionAsString.setter
    def InterpartSelectionAsString(self, enumString: str):
        """
        Setter for property: (str) InterpartSelectionAsString
          the InterpartSelection as string  
            
         
        """
        pass
    
    ## Getter for property: (str) LabelString
    ##   the LabelString  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
          the LabelString  
            
         
        """
        pass
    
    ## Setter for property: (str) LabelString

    ##   the LabelString  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
          the LabelString  
            
         
        """
        pass
    
    ## Getter for property: (bool) PointOverlay
    ##   the PointOverlay  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def PointOverlay(self) -> bool:
        """
        Getter for property: (bool) PointOverlay
          the PointOverlay  
            
         
        """
        pass
    
    ## Setter for property: (bool) PointOverlay

    ##   the PointOverlay  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @PointOverlay.setter
    def PointOverlay(self, overlay: bool):
        """
        Setter for property: (bool) PointOverlay
          the PointOverlay  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowFlowDirectionAndOriginCurve
    ##   the ShowFlowDirectionAndOriginCurve  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowFlowDirectionAndOriginCurve(self) -> bool:
        """
        Getter for property: (bool) ShowFlowDirectionAndOriginCurve
          the ShowFlowDirectionAndOriginCurve  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowFlowDirectionAndOriginCurve

    ##   the ShowFlowDirectionAndOriginCurve  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowFlowDirectionAndOriginCurve.setter
    def ShowFlowDirectionAndOriginCurve(self, show: bool):
        """
        Setter for property: (bool) ShowFlowDirectionAndOriginCurve
          the ShowFlowDirectionAndOriginCurve  
            
         
        """
        pass
    
    ## Getter for property: (str) SmartUpdateOptionAsString
    ##   the update option for points created by the point overlay.  
    ##   
    ##          <br> 
    ##         Acceptable values are:
    ##         <ul>
    ##         <li> <b>Within Modeling</b> The smart object updates within Modeling in time stamp order. For example, if the smart object is referenced by Feature(i), the smart object will update after Feature (i-1) and right before Feature(i).</li>
    ##         <li> <b>After Modeling</b> The smart object updates after Modeling. Use for Drafting dimensions and other objects outside Modeling.</li>
    ##         <li> <b>After Parent Body</b> The smart object will always update after the last feature on the parent body.</li>
    ##         <li> <b>Mixed</b> The smart object will update after the last feature on the parent body when the parent body is in a different part; updates within Modeling in time-stamp order for parents in the same part.</li>
    ##         </ul>
    ##          <br> 
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.1  <br> 

    ## @return str
    @property
    def SmartUpdateOptionAsString(self) -> str:
        """
        Getter for property: (str) SmartUpdateOptionAsString
          the update option for points created by the point overlay.  
          
                 <br> 
                Acceptable values are:
                <ul>
                <li> <b>Within Modeling</b> The smart object updates within Modeling in time stamp order. For example, if the smart object is referenced by Feature(i), the smart object will update after Feature (i-1) and right before Feature(i).</li>
                <li> <b>After Modeling</b> The smart object updates after Modeling. Use for Drafting dimensions and other objects outside Modeling.</li>
                <li> <b>After Parent Body</b> The smart object will always update after the last feature on the parent body.</li>
                <li> <b>Mixed</b> The smart object will update after the last feature on the parent body when the parent body is in a different part; updates within Modeling in time-stamp order for parents in the same part.</li>
                </ul>
                 <br> 
                  
         
        """
        pass
    
    ## Setter for property: (str) SmartUpdateOptionAsString

    ##   the update option for points created by the point overlay.  
    ##   
    ##          <br> 
    ##         Acceptable values are:
    ##         <ul>
    ##         <li> <b>Within Modeling</b> The smart object updates within Modeling in time stamp order. For example, if the smart object is referenced by Feature(i), the smart object will update after Feature (i-1) and right before Feature(i).</li>
    ##         <li> <b>After Modeling</b> The smart object updates after Modeling. Use for Drafting dimensions and other objects outside Modeling.</li>
    ##         <li> <b>After Parent Body</b> The smart object will always update after the last feature on the parent body.</li>
    ##         <li> <b>Mixed</b> The smart object will update after the last feature on the parent body when the parent body is in a different part; updates within Modeling in time-stamp order for parents in the same part.</li>
    ##         </ul>
    ##          <br> 
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.1  <br> 

    @SmartUpdateOptionAsString.setter
    def SmartUpdateOptionAsString(self, enumString: str):
        """
        Setter for property: (str) SmartUpdateOptionAsString
          the update option for points created by the point overlay.  
          
                 <br> 
                Acceptable values are:
                <ul>
                <li> <b>Within Modeling</b> The smart object updates within Modeling in time stamp order. For example, if the smart object is referenced by Feature(i), the smart object will update after Feature (i-1) and right before Feature(i).</li>
                <li> <b>After Modeling</b> The smart object updates after Modeling. Use for Drafting dimensions and other objects outside Modeling.</li>
                <li> <b>After Parent Body</b> The smart object will always update after the last feature on the parent body.</li>
                <li> <b>Mixed</b> The smart object will update after the last feature on the parent body when the parent body is in a different part; updates within Modeling in time-stamp order for parents in the same part.</li>
                </ul>
                 <br> 
                  
         
        """
        pass
    
    ## Getter for property: (int) SnapPointTypesEnabled
    ##   the SnapPointTypesEnabled  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def SnapPointTypesEnabled(self) -> int:
        """
        Getter for property: (int) SnapPointTypesEnabled
          the SnapPointTypesEnabled  
            
         
        """
        pass
    
    ## Setter for property: (int) SnapPointTypesEnabled

    ##   the SnapPointTypesEnabled  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @SnapPointTypesEnabled.setter
    def SnapPointTypesEnabled(self, snapPointType: int):
        """
        Setter for property: (int) SnapPointTypesEnabled
          the SnapPointTypesEnabled  
            
         
        """
        pass
    
    ## Getter for property: (int) SnapPointTypesOnByDefault
    ##   the SnapPointTypesOnByDefault  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def SnapPointTypesOnByDefault(self) -> int:
        """
        Getter for property: (int) SnapPointTypesOnByDefault
          the SnapPointTypesOnByDefault  
            
         
        """
        pass
    
    ## Setter for property: (int) SnapPointTypesOnByDefault

    ##   the SnapPointTypesOnByDefault  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @SnapPointTypesOnByDefault.setter
    def SnapPointTypesOnByDefault(self, defaultSnapPointType: int):
        """
        Setter for property: (int) SnapPointTypesOnByDefault
          the SnapPointTypesOnByDefault  
            
         
        """
        pass
    
    ## Getter for property: (str) StepStatusAsString
    ##   the StepStatus as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
          the StepStatus as string  
            
         
        """
        pass
    
    ## Setter for property: (str) StepStatusAsString

    ##   the StepStatus as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
          the StepStatus as string  
            
         
        """
        pass
    
    ## Getter for property: (bool) StopAtIntersection
    ##   the StopAtIntersection  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def StopAtIntersection(self) -> bool:
        """
        Getter for property: (bool) StopAtIntersection
          the StopAtIntersection  
            
         
        """
        pass
    
    ## Setter for property: (bool) StopAtIntersection

    ##   the StopAtIntersection  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @StopAtIntersection.setter
    def StopAtIntersection(self, stop: bool):
        """
        Setter for property: (bool) StopAtIntersection
          the StopAtIntersection  
            
         
        """
        pass
    
    ## Getter for property: (str) ToolTip
    ##   the ToolTip  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def ToolTip(self) -> str:
        """
        Getter for property: (str) ToolTip
          the ToolTip  
            
         
        """
        pass
    
    ## Setter for property: (str) ToolTip

    ##   the ToolTip  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ToolTip.setter
    def ToolTip(self, toolTip: str):
        """
        Setter for property: (str) ToolTip
          the ToolTip  
            
         
        """
        pass
    
    ##  Gets the BalloonTooltipLayout members 
    ##  @return layout_strings (List[str]): Value to get from the property. .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBalloonTooltipLayoutMembers(sectionBuilder: SectionBuilder) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         @return layout_strings (List[str]): Value to get from the property. .
        """
        pass
    
    ##  Gets the DefaultCurveRules members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetDefaultCurveRulesMembers(sectionBuilder: SectionBuilder) -> List[str]:
        """
         Gets the DefaultCurveRules members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Gets the InterpartSelection members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetInterpartSelectionMembers(sectionBuilder: SectionBuilder) -> List[str]:
        """
         Gets the InterpartSelection members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Gets the SelectedObjects
    ##  @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectedObjects(sectionBuilder: SectionBuilder) -> List[NXOpen.TaggedObject]:
        """
         Gets the SelectedObjects
         @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
        """
        pass
    
    ##  Gets the StepStatus members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStepStatusMembers(sectionBuilder: SectionBuilder) -> List[str]:
        """
         Gets the StepStatus members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Sets the SelectedObjects
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## Value to set for the property
    def SetSelectedObjects(sectionBuilder: SectionBuilder, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the SelectedObjects
        """
        pass
    
    ##  Tests the selection for this block. The block must be in focus to call this API
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## Value to set for the property
    def TestSelection(sectionBuilder: SectionBuilder, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Tests the selection for this block. The block must be in focus to call this API
        """
        pass
    
import NXOpen
##  Represents a Select Elements block
## 
##   <br>  Created in NX8.5.0  <br> 

class SelectElement(UIBlock): 
    """ Represents a Select Elements block"""


    ## Getter for property: (bool) AutomaticProgression
    ##   the AutomaticProgression.  
    ##    If true, focus automatically progresses to next selection block.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def AutomaticProgression(self) -> bool:
        """
        Getter for property: (bool) AutomaticProgression
          the AutomaticProgression.  
           If true, focus automatically progresses to next selection block.  
         
        """
        pass
    
    ## Setter for property: (bool) AutomaticProgression

    ##   the AutomaticProgression.  
    ##    If true, focus automatically progresses to next selection block.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @AutomaticProgression.setter
    def AutomaticProgression(self, automaticProgression: bool):
        """
        Setter for property: (bool) AutomaticProgression
          the AutomaticProgression.  
           If true, focus automatically progresses to next selection block.  
         
        """
        pass
    
    ## Getter for property: (str) Bitmap
    ##   the Bitmap  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Bitmap(self) -> str:
        """
        Getter for property: (str) Bitmap
          the Bitmap  
            
         
        """
        pass
    
    ## Setter for property: (str) Bitmap

    ##   the Bitmap  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Bitmap.setter
    def Bitmap(self, bitmap_string: str):
        """
        Setter for property: (str) Bitmap
          the Bitmap  
            
         
        """
        pass
    
    ## Getter for property: (str) Cue
    ##   the Cue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Cue(self) -> str:
        """
        Getter for property: (str) Cue
          the Cue  
            
         
        """
        pass
    
    ## Setter for property: (str) Cue

    ##   the Cue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Cue.setter
    def Cue(self, cue: str):
        """
        Setter for property: (str) Cue
          the Cue  
            
         
        """
        pass
    
    ## Getter for property: (str) LabelString
    ##   the LabelString  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
          the LabelString  
            
         
        """
        pass
    
    ## Setter for property: (str) LabelString

    ##   the LabelString  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
          the LabelString  
            
         
        """
        pass
    
    ## Getter for property: (str) SelectModeAsString
    ##   the SelectMode as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def SelectModeAsString(self) -> str:
        """
        Getter for property: (str) SelectModeAsString
          the SelectMode as string  
            
         
        """
        pass
    
    ## Setter for property: (str) SelectModeAsString

    ##   the SelectMode as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @SelectModeAsString.setter
    def SelectModeAsString(self, enumString: str):
        """
        Setter for property: (str) SelectModeAsString
          the SelectMode as string  
            
         
        """
        pass
    
    ## Getter for property: (str) SelectSubTypeAsString
    ##   the SelectSubType as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def SelectSubTypeAsString(self) -> str:
        """
        Getter for property: (str) SelectSubTypeAsString
          the SelectSubType as string  
            
         
        """
        pass
    
    ## Setter for property: (str) SelectSubTypeAsString

    ##   the SelectSubType as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @SelectSubTypeAsString.setter
    def SelectSubTypeAsString(self, enumString: str):
        """
        Setter for property: (str) SelectSubTypeAsString
          the SelectSubType as string  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowSelection
    ##   the Show Selection.  
    ##    If true, the graphical selection part of this block is shown.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  no replacement for this api  <br> 

    ## @return bool
    @property
    def ShowSelection(self) -> bool:
        """
        Getter for property: (bool) ShowSelection
          the Show Selection.  
           If true, the graphical selection part of this block is shown.  
         
        """
        pass
    
    ## Setter for property: (bool) ShowSelection

    ##   the Show Selection.  
    ##    If true, the graphical selection part of this block is shown.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  no replacement for this api  <br> 

    @ShowSelection.setter
    def ShowSelection(self, showSelection: bool):
        """
        Setter for property: (bool) ShowSelection
          the Show Selection.  
           If true, the graphical selection part of this block is shown.  
         
        """
        pass
    
    ## Getter for property: (str) StepStatusAsString
    ##   the StepStatus as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
          the StepStatus as string  
            
         
        """
        pass
    
    ## Setter for property: (str) StepStatusAsString

    ##   the StepStatus as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
          the StepStatus as string  
            
         
        """
        pass
    
    ##  Gets the SelectMode members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectModeMembers(selectElement: SelectElement) -> List[str]:
        """
         Gets the SelectMode members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Gets the SelectSubType members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectSubTypeMembers(selectElement: SelectElement) -> List[str]:
        """
         Gets the SelectSubType members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Gets the SelectedObjects
    ##  @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectedObjects(selectElement: SelectElement) -> List[NXOpen.TaggedObject]:
        """
         Gets the SelectedObjects
         @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
        """
        pass
    
    ##  Gets the SelectedObjectSubIDs
    ##  @return idVector (List[int]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectedObjectsSubIDs(selectElement: SelectElement) -> List[int]:
        """
         Gets the SelectedObjectSubIDs
         @return idVector (List[int]): Value to get from the property.
        """
        pass
    
    ##  Gets the StepStatus members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStepStatusMembers(selectElement: SelectElement) -> List[str]:
        """
         Gets the StepStatus members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Sets the SelectedObjects
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## Value to set for the property
    def SetSelectedObjects(selectElement: SelectElement, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the SelectedObjects
        """
        pass
    
    ##  Sets the SelectedObjectSubIDs
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## Value to set for the property
    def SetSelectedObjectsSubIDs(selectElement: SelectElement, idVector: List[int]) -> None:
        """
         Sets the SelectedObjectSubIDs
        """
        pass
    
    ##  Tests the selection for this block. The block must be in focus to call this API
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ##  
    def TestSelection(selectElement: SelectElement, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Tests the selection for this block. The block must be in focus to call this API
        """
        pass
    
import NXOpen
##  Represents a Select Region Selection block
## 
##   <br>  Created in NX12.0.0  <br> 

class SelectFacetRegion(UIBlock): 
    """ Represents a Select Region Selection block"""


    ## Getter for property: (bool) AutomaticProgression
    ##   the AutomaticProgression  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def AutomaticProgression(self) -> bool:
        """
        Getter for property: (bool) AutomaticProgression
          the AutomaticProgression  
            
         
        """
        pass
    
    ## Setter for property: (bool) AutomaticProgression

    ##   the AutomaticProgression  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @AutomaticProgression.setter
    def AutomaticProgression(self, automaticProgression: bool):
        """
        Setter for property: (bool) AutomaticProgression
          the AutomaticProgression  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipImage
    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipImage

    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipLayoutAsString
    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipLayoutAsString

    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipText
    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipText

    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Getter for property: (str) Bitmap
    ##   the Bitmap  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def Bitmap(self) -> str:
        """
        Getter for property: (str) Bitmap
          the Bitmap  
            
         
        """
        pass
    
    ## Setter for property: (str) Bitmap

    ##   the Bitmap  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Bitmap.setter
    def Bitmap(self, bitmap_string: str):
        """
        Setter for property: (str) Bitmap
          the Bitmap  
            
         
        """
        pass
    
    ## Getter for property: (str) Cue
    ##   the Cue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def Cue(self) -> str:
        """
        Getter for property: (str) Cue
          the Cue  
            
         
        """
        pass
    
    ## Setter for property: (str) Cue

    ##   the Cue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Cue.setter
    def Cue(self, cue: str):
        """
        Setter for property: (str) Cue
          the Cue  
            
         
        """
        pass
    
    ## Getter for property: (int) EnabledFacetCollectionRules
    ##   the FacetCollectionRules.  
    ##   
    ##          @brief 
    ##         These are the selection intent rules enabled for the facet selection region block 
    ##          
    ## 
    ##  
    ##         
    ##         It returns the following bit values,
    ##         <ol>
    ##         <li> 0x1 if only Single Facet rule is enabled,</li>
    ##         <li> 0x2 if only Face Facets rule is enabled,</li>
    ##         <li> 0x3 if only Flood Fill rule is enabled,</li>
    ##         <li> 0x4 if only Color Region rule is enabled</li>
    ##         </ol>
    ##         
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def EnabledFacetCollectionRules(self) -> int:
        """
        Getter for property: (int) EnabledFacetCollectionRules
          the FacetCollectionRules.  
          
                 @brief 
                These are the selection intent rules enabled for the facet selection region block 
                 
        
         
                
                It returns the following bit values,
                <ol>
                <li> 0x1 if only Single Facet rule is enabled,</li>
                <li> 0x2 if only Face Facets rule is enabled,</li>
                <li> 0x3 if only Flood Fill rule is enabled,</li>
                <li> 0x4 if only Color Region rule is enabled</li>
                </ol>
                
                  
         
        """
        pass
    
    ## Setter for property: (int) EnabledFacetCollectionRules

    ##   the FacetCollectionRules.  
    ##   
    ##          @brief 
    ##         These are the selection intent rules enabled for the facet selection region block 
    ##          
    ## 
    ##  
    ##         
    ##         It returns the following bit values,
    ##         <ol>
    ##         <li> 0x1 if only Single Facet rule is enabled,</li>
    ##         <li> 0x2 if only Face Facets rule is enabled,</li>
    ##         <li> 0x3 if only Flood Fill rule is enabled,</li>
    ##         <li> 0x4 if only Color Region rule is enabled</li>
    ##         </ol>
    ##         
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @EnabledFacetCollectionRules.setter
    def EnabledFacetCollectionRules(self, rulesEnabled: int):
        """
        Setter for property: (int) EnabledFacetCollectionRules
          the FacetCollectionRules.  
          
                 @brief 
                These are the selection intent rules enabled for the facet selection region block 
                 
        
         
                
                It returns the following bit values,
                <ol>
                <li> 0x1 if only Single Facet rule is enabled,</li>
                <li> 0x2 if only Face Facets rule is enabled,</li>
                <li> 0x3 if only Flood Fill rule is enabled,</li>
                <li> 0x4 if only Color Region rule is enabled</li>
                </ol>
                
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetCollector
    ##   the OwningFacetCollector.  
    ##   
    ##          @brief 
    ##         The owning facet collector is an object of class @link FacetCollector FacetCollector@endlink  that holds collected facets of the block
    ##          
    ## 
    ##  
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.FacetCollector
    @property
    def FacetCollector(self) -> NXOpen.FacetCollector:
        """
        Getter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetCollector
          the OwningFacetCollector.  
          
                 @brief 
                The owning facet collector is an object of class @link FacetCollector FacetCollector@endlink  that holds collected facets of the block
                 
        
         
                  
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetCollector

    ##   the OwningFacetCollector.  
    ##   
    ##          @brief 
    ##         The owning facet collector is an object of class @link FacetCollector FacetCollector@endlink  that holds collected facets of the block
    ##          
    ## 
    ##  
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @FacetCollector.setter
    def FacetCollector(self, facetCollector: NXOpen.FacetCollector):
        """
        Setter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetCollector
          the OwningFacetCollector.  
          
                 @brief 
                The owning facet collector is an object of class @link FacetCollector FacetCollector@endlink  that holds collected facets of the block
                 
        
         
                  
         
        """
        pass
    
    ## Getter for property: (str) LabelString
    ##   the LabelString  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
          the LabelString  
            
         
        """
        pass
    
    ## Setter for property: (str) LabelString

    ##   the LabelString  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
          the LabelString  
            
         
        """
        pass
    
    ## Getter for property: (int) SelectedFacetCollectionRule
    ##   the active facet collection rule  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def SelectedFacetCollectionRule(self) -> int:
        """
        Getter for property: (int) SelectedFacetCollectionRule
          the active facet collection rule  
            
         
        """
        pass
    
    ## Setter for property: (int) SelectedFacetCollectionRule

    ##   the active facet collection rule  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SelectedFacetCollectionRule.setter
    def SelectedFacetCollectionRule(self, selectedRule: int):
        """
        Setter for property: (int) SelectedFacetCollectionRule
          the active facet collection rule  
            
         
        """
        pass
    
    ## Getter for property: (str) StepStatusAsString
    ##   the StepStatus as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
          the StepStatus as string  
            
         
        """
        pass
    
    ## Setter for property: (str) StepStatusAsString

    ##   the StepStatus as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
          the StepStatus as string  
            
         
        """
        pass
    
    ## Getter for property: (int) SupportedFacetTypes
    ##   the SupportedFacetTypes.  
    ##   
    ##          @brief 
    ##         These are type of facets enabled in filters for select facet region block 
    ##          
    ## 
    ##  
    ##         
    ##         It returns following bits,
    ##         <ol>
    ##         <li> 0x1 if only convergent facets are enabled,</li>
    ##         <li> 0x2 if only NX facets are enabled,</li>
    ##         <li> 0x3 if both convergent as well as NX facets are enabled.</li>
    ##         </ol>
    ##         
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def SupportedFacetTypes(self) -> int:
        """
        Getter for property: (int) SupportedFacetTypes
          the SupportedFacetTypes.  
          
                 @brief 
                These are type of facets enabled in filters for select facet region block 
                 
        
         
                
                It returns following bits,
                <ol>
                <li> 0x1 if only convergent facets are enabled,</li>
                <li> 0x2 if only NX facets are enabled,</li>
                <li> 0x3 if both convergent as well as NX facets are enabled.</li>
                </ol>
                
                  
         
        """
        pass
    
    ## Setter for property: (int) SupportedFacetTypes

    ##   the SupportedFacetTypes.  
    ##   
    ##          @brief 
    ##         These are type of facets enabled in filters for select facet region block 
    ##          
    ## 
    ##  
    ##         
    ##         It returns following bits,
    ##         <ol>
    ##         <li> 0x1 if only convergent facets are enabled,</li>
    ##         <li> 0x2 if only NX facets are enabled,</li>
    ##         <li> 0x3 if both convergent as well as NX facets are enabled.</li>
    ##         </ol>
    ##         
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SupportedFacetTypes.setter
    def SupportedFacetTypes(self, typesEnabled: int):
        """
        Setter for property: (int) SupportedFacetTypes
          the SupportedFacetTypes.  
          
                 @brief 
                These are type of facets enabled in filters for select facet region block 
                 
        
         
                
                It returns following bits,
                <ol>
                <li> 0x1 if only convergent facets are enabled,</li>
                <li> 0x2 if only NX facets are enabled,</li>
                <li> 0x3 if both convergent as well as NX facets are enabled.</li>
                </ol>
                
                  
         
        """
        pass
    
    ## Getter for property: (str) ToolTip
    ##   the ToolTip  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def ToolTip(self) -> str:
        """
        Getter for property: (str) ToolTip
          the ToolTip  
            
         
        """
        pass
    
    ## Setter for property: (str) ToolTip

    ##   the ToolTip  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ToolTip.setter
    def ToolTip(self, toolTip: str):
        """
        Setter for property: (str) ToolTip
          the ToolTip  
            
         
        """
        pass
    
    ##  Gets the BalloonTooltipLayout members 
    ##  @return layout_strings (List[str]): Value to get from the property. .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBalloonTooltipLayoutMembers(selectFacetRegion: SelectFacetRegion) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         @return layout_strings (List[str]): Value to get from the property. .
        """
        pass
    
    ##  Gets the LastDeselectedFacetRegions
    ##  @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetLastDeselectedObjects(selectFacetRegion: SelectFacetRegion) -> List[NXOpen.TaggedObject]:
        """
         Gets the LastDeselectedFacetRegions
         @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
        """
        pass
    
    ##  Gets the LastSelectedFacetRegions
    ##  @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetLastSelectedObjects(selectFacetRegion: SelectFacetRegion) -> List[NXOpen.TaggedObject]:
        """
         Gets the LastSelectedFacetRegions
         @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
        """
        pass
    
    ##  Gets the SelectedFacetRegions
    ##  @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectedObjects(selectFacetRegion: SelectFacetRegion) -> List[NXOpen.TaggedObject]:
        """
         Gets the SelectedFacetRegions
         @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
        """
        pass
    
    ##  Gets the StepStatus members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStepStatusMembers(selectFacetRegion: SelectFacetRegion) -> List[str]:
        """
         Gets the StepStatus members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Sets the SelectedFacetRegions
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## Value to set for the property
    def SetSelectedObjects(selectFacetRegion: SelectFacetRegion, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the SelectedFacetRegions
        """
        pass
    
    ##  Tests the selection for this block. The block must be in focus to call this API
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## Value to set for the property
    def TestSelection(selectFacetRegion: SelectFacetRegion, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Tests the selection for this block. The block must be in focus to call this API
        """
        pass
    
import NXOpen
##  Represents a Select Feature block
## 
##   <br>  Created in NX8.5.0  <br> 

class SelectFeature(UIBlock): 
    """ Represents a Select Feature block"""


    ## Getter for property: (bool) AutomaticProgression
    ##   the AutomaticProgression  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def AutomaticProgression(self) -> bool:
        """
        Getter for property: (bool) AutomaticProgression
          the AutomaticProgression  
            
         
        """
        pass
    
    ## Setter for property: (bool) AutomaticProgression

    ##   the AutomaticProgression  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @AutomaticProgression.setter
    def AutomaticProgression(self, automaticProgression: bool):
        """
        Setter for property: (bool) AutomaticProgression
          the AutomaticProgression  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipImage
    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipImage

    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipLayoutAsString
    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipLayoutAsString

    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipText
    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipText

    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Getter for property: (bool) BlendVirtualCurveOverlay
    ##   the BlendVirtualCurveOverlay.  
    ##    If true, virtual curve is displayed during pre-selection.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def BlendVirtualCurveOverlay(self) -> bool:
        """
        Getter for property: (bool) BlendVirtualCurveOverlay
          the BlendVirtualCurveOverlay.  
           If true, virtual curve is displayed during pre-selection.  
         
        """
        pass
    
    ## Setter for property: (bool) BlendVirtualCurveOverlay

    ##   the BlendVirtualCurveOverlay.  
    ##    If true, virtual curve is displayed during pre-selection.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BlendVirtualCurveOverlay.setter
    def BlendVirtualCurveOverlay(self, blendCurve: bool):
        """
        Setter for property: (bool) BlendVirtualCurveOverlay
          the BlendVirtualCurveOverlay.  
           If true, virtual curve is displayed during pre-selection.  
         
        """
        pass
    
    ## Getter for property: (str) Cue
    ##   the Cue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Cue(self) -> str:
        """
        Getter for property: (str) Cue
          the Cue  
            
         
        """
        pass
    
    ## Setter for property: (str) Cue

    ##   the Cue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Cue.setter
    def Cue(self, cue: str):
        """
        Setter for property: (str) Cue
          the Cue  
            
         
        """
        pass
    
    ## Getter for property: (str) LabelString
    ##   the LabelString  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
          the LabelString  
            
         
        """
        pass
    
    ## Setter for property: (str) LabelString

    ##   the LabelString  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
          the LabelString  
            
         
        """
        pass
    
    ## Getter for property: (str) SelectModeAsString
    ##   the SelectMode as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def SelectModeAsString(self) -> str:
        """
        Getter for property: (str) SelectModeAsString
          the SelectMode as string  
            
         
        """
        pass
    
    ## Setter for property: (str) SelectModeAsString

    ##   the SelectMode as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @SelectModeAsString.setter
    def SelectModeAsString(self, enumString: str):
        """
        Setter for property: (str) SelectModeAsString
          the SelectMode as string  
            
         
        """
        pass
    
    ## Getter for property: (str) StepStatusAsString
    ##   the StepStatus as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
          the StepStatus as string  
            
         
        """
        pass
    
    ## Setter for property: (str) StepStatusAsString

    ##   the StepStatus as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
          the StepStatus as string  
            
         
        """
        pass
    
    ## Getter for property: (str) ToolTip
    ##   the ToolTip  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def ToolTip(self) -> str:
        """
        Getter for property: (str) ToolTip
          the ToolTip  
            
         
        """
        pass
    
    ## Setter for property: (str) ToolTip

    ##   the ToolTip  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ToolTip.setter
    def ToolTip(self, toolTip: str):
        """
        Setter for property: (str) ToolTip
          the ToolTip  
            
         
        """
        pass
    
    ##  Gets the BalloonTooltipLayout members 
    ##  @return layout_strings (List[str]): Value to get from the property. .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBalloonTooltipLayoutMembers(selectFeature: SelectFeature) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         @return layout_strings (List[str]): Value to get from the property. .
        """
        pass
    
    ##  Gets the SelectMode members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectModeMembers(selectFeature: SelectFeature) -> List[str]:
        """
         Gets the SelectMode members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Gets the SelectedObjects
    ##  @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectedObjects(selectFeature: SelectFeature) -> List[NXOpen.TaggedObject]:
        """
         Gets the SelectedObjects
         @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
        """
        pass
    
    ##  Gets the StepStatus members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStepStatusMembers(selectFeature: SelectFeature) -> List[str]:
        """
         Gets the StepStatus members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Sets the SelectedObjects
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## Value to set for the property
    def SetSelectedObjects(selectFeature: SelectFeature, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the SelectedObjects
        """
        pass
    
    ##  Tests the selection for this block. The block must be in focus to call this API
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## Value to set for the property
    def TestSelection(selectFeature: SelectFeature, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Tests the selection for this block. The block must be in focus to call this API
        """
        pass
    
import NXOpen
##  Represents a Select Node block
## 
##   <br>  Created in NX8.5.0  <br> 

class SelectNode(UIBlock): 
    """ Represents a Select Node block"""


    ## Getter for property: (bool) AutomaticProgression
    ##   the AutomaticProgression  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def AutomaticProgression(self) -> bool:
        """
        Getter for property: (bool) AutomaticProgression
          the AutomaticProgression  
            
         
        """
        pass
    
    ## Setter for property: (bool) AutomaticProgression

    ##   the AutomaticProgression  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @AutomaticProgression.setter
    def AutomaticProgression(self, automaticProgression: bool):
        """
        Setter for property: (bool) AutomaticProgression
          the AutomaticProgression  
            
         
        """
        pass
    
    ## Getter for property: (str) Bitmap
    ##   the Bitmap  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Bitmap(self) -> str:
        """
        Getter for property: (str) Bitmap
          the Bitmap  
            
         
        """
        pass
    
    ## Setter for property: (str) Bitmap

    ##   the Bitmap  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Bitmap.setter
    def Bitmap(self, bitmap_string: str):
        """
        Setter for property: (str) Bitmap
          the Bitmap  
            
         
        """
        pass
    
    ## Getter for property: (str) Cue
    ##   the Cue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Cue(self) -> str:
        """
        Getter for property: (str) Cue
          the Cue  
            
         
        """
        pass
    
    ## Setter for property: (str) Cue

    ##   the Cue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Cue.setter
    def Cue(self, cue: str):
        """
        Setter for property: (str) Cue
          the Cue  
            
         
        """
        pass
    
    ## Getter for property: (str) LabelString
    ##   the LabelString  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
          the LabelString  
            
         
        """
        pass
    
    ## Setter for property: (str) LabelString

    ##   the LabelString  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
          the LabelString  
            
         
        """
        pass
    
    ## Getter for property: (str) SelectModeAsString
    ##   the SelectMode as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def SelectModeAsString(self) -> str:
        """
        Getter for property: (str) SelectModeAsString
          the SelectMode as string  
            
         
        """
        pass
    
    ## Setter for property: (str) SelectModeAsString

    ##   the SelectMode as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @SelectModeAsString.setter
    def SelectModeAsString(self, enumString: str):
        """
        Setter for property: (str) SelectModeAsString
          the SelectMode as string  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowSelection
    ##   the Show Selection.  
    ##    If true,the graphical selection part of this block is shown.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  no replacement for this api  <br> 

    ## @return bool
    @property
    def ShowSelection(self) -> bool:
        """
        Getter for property: (bool) ShowSelection
          the Show Selection.  
           If true,the graphical selection part of this block is shown.  
         
        """
        pass
    
    ## Setter for property: (bool) ShowSelection

    ##   the Show Selection.  
    ##    If true,the graphical selection part of this block is shown.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  no replacement for this api  <br> 

    @ShowSelection.setter
    def ShowSelection(self, showSelection: bool):
        """
        Setter for property: (bool) ShowSelection
          the Show Selection.  
           If true,the graphical selection part of this block is shown.  
         
        """
        pass
    
    ## Getter for property: (str) StepStatusAsString
    ##   the StepStatus as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
          the StepStatus as string  
            
         
        """
        pass
    
    ## Setter for property: (str) StepStatusAsString

    ##   the StepStatus as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
          the StepStatus as string  
            
         
        """
        pass
    
    ##  Gets the SelectMode members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectModeMembers(selectNode: SelectNode) -> List[str]:
        """
         Gets the SelectMode members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Gets the SelectedObjects
    ##  @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectedObjects(selectNode: SelectNode) -> List[NXOpen.TaggedObject]:
        """
         Gets the SelectedObjects
         @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
        """
        pass
    
    ##  Gets the StepStatus members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStepStatusMembers(selectNode: SelectNode) -> List[str]:
        """
         Gets the StepStatus members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Sets the SelectedObjects
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## Value to set for the property
    def SetSelectedObjects(selectNode: SelectNode, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the SelectedObjects
        """
        pass
    
    ##  Tests the selection for this block. The block must be in focus to call this API
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ##  
    def TestSelection(selectNode: SelectNode, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Tests the selection for this block. The block must be in focus to call this API
        """
        pass
    
import NXOpen
import NXOpen.Select
##  Represents a Select Object block
## 
##   <br>  Created in NX8.5.0  <br> 

class SelectObject(UIBlock): 
    """ Represents a Select Object block"""


    ## Indicates the general filter type for selection. 
    ##  Filter to select all feature types 
    class FilterType(Enum):
        """
        Members Include: <Features> <Faces> <Edges> <CurvesAndEdges> <Components> <SolidBodies> <SheetBodies>
        """
        Features: int
        Faces: int
        Edges: int
        CurvesAndEdges: int
        Components: int
        SolidBodies: int
        SheetBodies: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SelectObject.FilterType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) AllowConvergentObject
    ##   the AllowConvergentObject  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def AllowConvergentObject(self) -> bool:
        """
        Getter for property: (bool) AllowConvergentObject
          the AllowConvergentObject  
            
         
        """
        pass
    
    ## Setter for property: (bool) AllowConvergentObject

    ##   the AllowConvergentObject  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @AllowConvergentObject.setter
    def AllowConvergentObject(self, allowConvergentObject: bool):
        """
        Setter for property: (bool) AllowConvergentObject
          the AllowConvergentObject  
            
         
        """
        pass
    
    ## Getter for property: (bool) AllowConvergentObjectWithMixedGeometries
    ##   the AllowConvergentObjectWithMixedGeometries  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2007.0.0.  This property is no longer relevant as hybrid selection is default ON now.  <br> 

    ## @return bool
    @property
    def AllowConvergentObjectWithMixedGeometries(self) -> bool:
        """
        Getter for property: (bool) AllowConvergentObjectWithMixedGeometries
          the AllowConvergentObjectWithMixedGeometries  
            
         
        """
        pass
    
    ## Setter for property: (bool) AllowConvergentObjectWithMixedGeometries

    ##   the AllowConvergentObjectWithMixedGeometries  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2007.0.0.  This property is no longer relevant as hybrid selection is default ON now.  <br> 

    @AllowConvergentObjectWithMixedGeometries.setter
    def AllowConvergentObjectWithMixedGeometries(self, allowConvergentObjectWithMixedGeometries: bool):
        """
        Setter for property: (bool) AllowConvergentObjectWithMixedGeometries
          the AllowConvergentObjectWithMixedGeometries  
            
         
        """
        pass
    
    ## Getter for property: (bool) AutomaticProgression
    ##   the AutomaticProgression  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def AutomaticProgression(self) -> bool:
        """
        Getter for property: (bool) AutomaticProgression
          the AutomaticProgression  
            
         
        """
        pass
    
    ## Setter for property: (bool) AutomaticProgression

    ##   the AutomaticProgression  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @AutomaticProgression.setter
    def AutomaticProgression(self, automaticProgression: bool):
        """
        Setter for property: (bool) AutomaticProgression
          the AutomaticProgression  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipImage
    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipImage

    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipLayoutAsString
    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipLayoutAsString

    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipText
    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipText

    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Getter for property: (str) Bitmap
    ##   the Bitmap  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Bitmap(self) -> str:
        """
        Getter for property: (str) Bitmap
          the Bitmap  
            
         
        """
        pass
    
    ## Setter for property: (str) Bitmap

    ##   the Bitmap  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Bitmap.setter
    def Bitmap(self, bitmap_string: str):
        """
        Setter for property: (str) Bitmap
          the Bitmap  
            
         
        """
        pass
    
    ## Getter for property: (bool) BlendVirtualCurveOverlay
    ##   the BlendVirtualCurveOverlay.  
    ##    If true, virtual curve is displayed during preselection.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def BlendVirtualCurveOverlay(self) -> bool:
        """
        Getter for property: (bool) BlendVirtualCurveOverlay
          the BlendVirtualCurveOverlay.  
           If true, virtual curve is displayed during preselection.  
         
        """
        pass
    
    ## Setter for property: (bool) BlendVirtualCurveOverlay

    ##   the BlendVirtualCurveOverlay.  
    ##    If true, virtual curve is displayed during preselection.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BlendVirtualCurveOverlay.setter
    def BlendVirtualCurveOverlay(self, blendCurve: bool):
        """
        Setter for property: (bool) BlendVirtualCurveOverlay
          the BlendVirtualCurveOverlay.  
           If true, virtual curve is displayed during preselection.  
         
        """
        pass
    
    ## Getter for property: (bool) CreateInterpartLink
    ##   the CreateInterpartLink  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def CreateInterpartLink(self) -> bool:
        """
        Getter for property: (bool) CreateInterpartLink
          the CreateInterpartLink  
            
         
        """
        pass
    
    ## Setter for property: (bool) CreateInterpartLink

    ##   the CreateInterpartLink  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @CreateInterpartLink.setter
    def CreateInterpartLink(self, createLink: bool):
        """
        Setter for property: (bool) CreateInterpartLink
          the CreateInterpartLink  
            
         
        """
        pass
    
    ## Getter for property: (str) Cue
    ##   the Cue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Cue(self) -> str:
        """
        Getter for property: (str) Cue
          the Cue  
            
         
        """
        pass
    
    ## Setter for property: (str) Cue

    ##   the Cue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Cue.setter
    def Cue(self, cue: str):
        """
        Setter for property: (str) Cue
          the Cue  
            
         
        """
        pass
    
    ## Getter for property: (str) InterpartSelectionAsString
    ##   the InterpartSelection as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def InterpartSelectionAsString(self) -> str:
        """
        Getter for property: (str) InterpartSelectionAsString
          the InterpartSelection as string  
            
         
        """
        pass
    
    ## Setter for property: (str) InterpartSelectionAsString

    ##   the InterpartSelection as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @InterpartSelectionAsString.setter
    def InterpartSelectionAsString(self, enumString: str):
        """
        Setter for property: (str) InterpartSelectionAsString
          the InterpartSelection as string  
            
         
        """
        pass
    
    ## Getter for property: (str) LabelString
    ##   the LabelString  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
          the LabelString  
            
         
        """
        pass
    
    ## Setter for property: (str) LabelString

    ##   the LabelString  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
          the LabelString  
            
         
        """
        pass
    
    ## Getter for property: (str) MaximumScopeAsString
    ##   the MaximumScope as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def MaximumScopeAsString(self) -> str:
        """
        Getter for property: (str) MaximumScopeAsString
          the MaximumScope as string  
            
         
        """
        pass
    
    ## Setter for property: (str) MaximumScopeAsString

    ##   the MaximumScope as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MaximumScopeAsString.setter
    def MaximumScopeAsString(self, enumString: str):
        """
        Setter for property: (str) MaximumScopeAsString
          the MaximumScope as string  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) PickPoint
    ##   the PickPoint  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def PickPoint(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) PickPoint
          the PickPoint  
            
         
        """
        pass
    
    ## Getter for property: (bool) PointOverlay
    ##   the PointOverlay.  
    ##    If true,on the fly point creation is allowed.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def PointOverlay(self) -> bool:
        """
        Getter for property: (bool) PointOverlay
          the PointOverlay.  
           If true,on the fly point creation is allowed.  
         
        """
        pass
    
    ## Setter for property: (bool) PointOverlay

    ##   the PointOverlay.  
    ##    If true,on the fly point creation is allowed.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @PointOverlay.setter
    def PointOverlay(self, pointOverlay: bool):
        """
        Setter for property: (bool) PointOverlay
          the PointOverlay.  
           If true,on the fly point creation is allowed.  
         
        """
        pass
    
    ## Getter for property: (str) SelectModeAsString
    ##   the SelectMode as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def SelectModeAsString(self) -> str:
        """
        Getter for property: (str) SelectModeAsString
          the SelectMode as string  
            
         
        """
        pass
    
    ## Setter for property: (str) SelectModeAsString

    ##   the SelectMode as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @SelectModeAsString.setter
    def SelectModeAsString(self, enumString: str):
        """
        Setter for property: (str) SelectModeAsString
          the SelectMode as string  
            
         
        """
        pass
    
    ## Getter for property: (str) SmartUpdateOptionAsString
    ##   the update option for points created by the point overlay.  
    ##   
    ##          <br> 
    ##         Acceptable values are:
    ##         <ul>
    ##         <li> <b>Within Modeling</b> The smart object updates within Modeling in time stamp order. For example, if the smart object is referenced by Feature(i), the smart object will update after Feature (i-1) and right before Feature(i).</li>
    ##         <li> <b>After Modeling</b> The smart object updates after Modeling. Use for Drafting dimensions and other objects outside Modeling.</li>
    ##         <li> <b>After Parent Body</b> The smart object will always update after the last feature on the parent body.</li>
    ##         <li> <b>Mixed</b> The smart object will update after the last feature on the parent body when the parent body is in a different part; updates within Modeling in time-stamp order for parents in the same part.</li>
    ##         </ul>
    ##          <br> 
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.1  <br> 

    ## @return str
    @property
    def SmartUpdateOptionAsString(self) -> str:
        """
        Getter for property: (str) SmartUpdateOptionAsString
          the update option for points created by the point overlay.  
          
                 <br> 
                Acceptable values are:
                <ul>
                <li> <b>Within Modeling</b> The smart object updates within Modeling in time stamp order. For example, if the smart object is referenced by Feature(i), the smart object will update after Feature (i-1) and right before Feature(i).</li>
                <li> <b>After Modeling</b> The smart object updates after Modeling. Use for Drafting dimensions and other objects outside Modeling.</li>
                <li> <b>After Parent Body</b> The smart object will always update after the last feature on the parent body.</li>
                <li> <b>Mixed</b> The smart object will update after the last feature on the parent body when the parent body is in a different part; updates within Modeling in time-stamp order for parents in the same part.</li>
                </ul>
                 <br> 
                  
         
        """
        pass
    
    ## Setter for property: (str) SmartUpdateOptionAsString

    ##   the update option for points created by the point overlay.  
    ##   
    ##          <br> 
    ##         Acceptable values are:
    ##         <ul>
    ##         <li> <b>Within Modeling</b> The smart object updates within Modeling in time stamp order. For example, if the smart object is referenced by Feature(i), the smart object will update after Feature (i-1) and right before Feature(i).</li>
    ##         <li> <b>After Modeling</b> The smart object updates after Modeling. Use for Drafting dimensions and other objects outside Modeling.</li>
    ##         <li> <b>After Parent Body</b> The smart object will always update after the last feature on the parent body.</li>
    ##         <li> <b>Mixed</b> The smart object will update after the last feature on the parent body when the parent body is in a different part; updates within Modeling in time-stamp order for parents in the same part.</li>
    ##         </ul>
    ##          <br> 
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.1  <br> 

    @SmartUpdateOptionAsString.setter
    def SmartUpdateOptionAsString(self, enumString: str):
        """
        Setter for property: (str) SmartUpdateOptionAsString
          the update option for points created by the point overlay.  
          
                 <br> 
                Acceptable values are:
                <ul>
                <li> <b>Within Modeling</b> The smart object updates within Modeling in time stamp order. For example, if the smart object is referenced by Feature(i), the smart object will update after Feature (i-1) and right before Feature(i).</li>
                <li> <b>After Modeling</b> The smart object updates after Modeling. Use for Drafting dimensions and other objects outside Modeling.</li>
                <li> <b>After Parent Body</b> The smart object will always update after the last feature on the parent body.</li>
                <li> <b>Mixed</b> The smart object will update after the last feature on the parent body when the parent body is in a different part; updates within Modeling in time-stamp order for parents in the same part.</li>
                </ul>
                 <br> 
                  
         
        """
        pass
    
    ## Getter for property: (int) SnapPointTypesEnabled
    ##   the SnapPointTypesEnabled  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def SnapPointTypesEnabled(self) -> int:
        """
        Getter for property: (int) SnapPointTypesEnabled
          the SnapPointTypesEnabled  
            
         
        """
        pass
    
    ## Setter for property: (int) SnapPointTypesEnabled

    ##   the SnapPointTypesEnabled  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @SnapPointTypesEnabled.setter
    def SnapPointTypesEnabled(self, typesEnabled: int):
        """
        Setter for property: (int) SnapPointTypesEnabled
          the SnapPointTypesEnabled  
            
         
        """
        pass
    
    ## Getter for property: (int) SnapPointTypesOnByDefault
    ##   the SnapPointTypesOnByDefault  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def SnapPointTypesOnByDefault(self) -> int:
        """
        Getter for property: (int) SnapPointTypesOnByDefault
          the SnapPointTypesOnByDefault  
            
         
        """
        pass
    
    ## Setter for property: (int) SnapPointTypesOnByDefault

    ##   the SnapPointTypesOnByDefault  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @SnapPointTypesOnByDefault.setter
    def SnapPointTypesOnByDefault(self, typesByDefault: int):
        """
        Setter for property: (int) SnapPointTypesOnByDefault
          the SnapPointTypesOnByDefault  
            
         
        """
        pass
    
    ## Getter for property: (str) StepStatusAsString
    ##   the StepStatus as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
          the StepStatus as string  
            
         
        """
        pass
    
    ## Setter for property: (str) StepStatusAsString

    ##   the StepStatus as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
          the StepStatus as string  
            
         
        """
        pass
    
    ## Getter for property: (str) ToolTip
    ##   the ToolTip  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def ToolTip(self) -> str:
        """
        Getter for property: (str) ToolTip
          the ToolTip  
            
         
        """
        pass
    
    ## Setter for property: (str) ToolTip

    ##   the ToolTip  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ToolTip.setter
    def ToolTip(self, toolTip: str):
        """
        Setter for property: (str) ToolTip
          the ToolTip  
            
         
        """
        pass
    
    ## 
    ##          @brief 
    ##         Adds the filters for select object block
    ##          
    ## 
    ##  
    ##         
    ##         This method takes the integer value of the desired enum values from 
    ##         @link NXOpen::BlockStyler::SelectObject::FilterType NXOpen::BlockStyler::SelectObject::FilterType@endlink .
    ##         
    ##          
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## Values from @link SelectObject::FilterType SelectObject::FilterType@endlink  for specifying filters 
    def AddFilter(selObject: SelectObject, filterTypes: int) -> None:
        """
        
                 @brief 
                Adds the filters for select object block
                 
        
         
                
                This method takes the integer value of the desired enum values from 
                @link NXOpen::BlockStyler::SelectObject::FilterType NXOpen::BlockStyler::SelectObject::FilterType@endlink .
                
                 
        """
        pass
    
    ## 
    ##          @brief 
    ##         Adds a single filter member for select object block without clearing the filter
    ##          
    ## 
    ##  
    ##         
    ##         This method takes the desired enumeration value from
    ##         @link NXOpen::Select::FilterMember NXOpen::Select::FilterMember@endlink .
    ##         
    ##          
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ##  Filter Member to add 
    def AddFilterMember(selObject: SelectObject, member: NXOpen.Select.FilterMember) -> None:
        """
        
                 @brief 
                Adds a single filter member for select object block without clearing the filter
                 
        
         
                
                This method takes the desired enumeration value from
                @link NXOpen::Select::FilterMember NXOpen::Select::FilterMember@endlink .
                
                 
        """
        pass
    
    ## 
    ##          @brief 
    ##         Adds specific filter members for select object block without clearing the filter
    ##          
    ## 
    ##  
    ##         
    ##         This method takes the desired enumeration values from
    ##         @link NXOpen::Select::FilterMember NXOpen::Select::FilterMember@endlink .
    ##         
    ##          
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ##  Filter Members to add 
    def AddFilterMembers(selObject: SelectObject, members: List[NXOpen.Select.FilterMember]) -> None:
        """
        
                 @brief 
                Adds specific filter members for select object block without clearing the filter
                 
        
         
                
                This method takes the desired enumeration values from
                @link NXOpen::Select::FilterMember NXOpen::Select::FilterMember@endlink .
                
                 
        """
        pass
    
    ## 
    ##          @brief 
    ##         Adds the filters for select object block 
    ##          
    ## 
    ##  
    ##         
    ##         This method takes the desired enumeration value from
    ##         @link NXOpen::BlockStyler::SelectObject::FilterType NXOpen::BlockStyler::SelectObject::FilterType@endlink .
    ##         
    ##         
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## Values from @link SelectObject::FilterType SelectObject::FilterType@endlink  for specifying filters 
    @overload
    def AddFilter(self, selObject: SelectObject, filterTypes: SelectObject.FilterType) -> None:
        """
        
                 @brief 
                Adds the filters for select object block 
                 
        
         
                
                This method takes the desired enumeration value from
                @link NXOpen::BlockStyler::SelectObject::FilterType NXOpen::BlockStyler::SelectObject::FilterType@endlink .
                
                
        """
        pass
    
    ## Adds the filter for select object block using type, subtype and solidBodyType 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ##  Object type. This can be one of the object types that are listed in 
    ##                                         uf_object_types.h. For example, for point, 
    ##                                         use UF_point_type in C++ and
    ##                                         NXOpen.UF.UFConstants.UF_point_type in .NET. 
    @overload
    def AddFilter(self, selObject: SelectObject, type: int, subType: int, solidBodyType: int) -> None:
        """
        Adds the filter for select object block using type, subtype and solidBodyType 
        """
        pass
    
    ##  Clears the filter for select object block  
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def ClearFilter(selObject: SelectObject) -> None:
        """
         Clears the filter for select object block  
        """
        pass
    
    ##  Gets the BalloonTooltipLayout members 
    ##  @return layout_strings (List[str]): Value to get from the property. .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBalloonTooltipLayoutMembers(selectObject: SelectObject) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         @return layout_strings (List[str]): Value to get from the property. .
        """
        pass
    
    ##  Gets the InterpartSelection members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetInterpartSelectionMembers(selectObject: SelectObject) -> List[str]:
        """
         Gets the InterpartSelection members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Gets the LastDeselectedObjects
    ##  @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetLastDeselectedObjects(selectObject: SelectObject) -> List[NXOpen.TaggedObject]:
        """
         Gets the LastDeselectedObjects
         @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
        """
        pass
    
    ##  Gets the LastSelectedObjects
    ##  @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetLastSelectedObjects(selectObject: SelectObject) -> List[NXOpen.TaggedObject]:
        """
         Gets the LastSelectedObjects
         @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
        """
        pass
    
    ##  Gets the MaximumScope members 
    ##  @return scope_strings (List[str]): Value to get from the property. .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetMaximumScopeMembers(selectObject: SelectObject) -> List[str]:
        """
         Gets the MaximumScope members 
         @return scope_strings (List[str]): Value to get from the property. .
        """
        pass
    
    ##  Gets the SelectMode members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectModeMembers(selectObject: SelectObject) -> List[str]:
        """
         Gets the SelectMode members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Gets the SelectedObjects
    ##  @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectedObjects(selectObject: SelectObject) -> List[NXOpen.TaggedObject]:
        """
         Gets the SelectedObjects
         @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
        """
        pass
    
    ##  Gets the StepStatus members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStepStatusMembers(selectObject: SelectObject) -> List[str]:
        """
         Gets the StepStatus members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ## 
    ##          @brief 
    ##         Removes a single filter member from select object block
    ##          
    ## 
    ##  
    ##         
    ##         This method takes the desired enumeration value from
    ##         @link NXOpen::Select::FilterMember NXOpen::Select::FilterMember@endlink .
    ##         
    ##          
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ##  Filter Member to remove 
    def RemoveFilterMember(selObject: SelectObject, member: NXOpen.Select.FilterMember) -> None:
        """
        
                 @brief 
                Removes a single filter member from select object block
                 
        
         
                
                This method takes the desired enumeration value from
                @link NXOpen::Select::FilterMember NXOpen::Select::FilterMember@endlink .
                
                 
        """
        pass
    
    ## 
    ##          @brief 
    ##         Removes specific filter members from select object block
    ##          
    ## 
    ##  
    ##         
    ##         This method takes the desired enumeration values from
    ##         @link NXOpen::Select::FilterMember NXOpen::Select::FilterMember@endlink .
    ##         
    ##          
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ##  Filter Members to remove 
    def RemoveFilterMembers(selObject: SelectObject, members: List[NXOpen.Select.FilterMember]) -> None:
        """
        
                 @brief 
                Removes specific filter members from select object block
                 
        
         
                
                This method takes the desired enumeration values from
                @link NXOpen::Select::FilterMember NXOpen::Select::FilterMember@endlink .
                
                 
        """
        pass
    
    ## Resets the filter for select object block 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def ResetFilter(selObject: SelectObject) -> None:
        """
        Resets the filter for select object block 
        """
        pass
    
    ##  Sets the SelectedObjects
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## Value to set for the property
    def SetSelectedObjects(selectObject: SelectObject, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the SelectedObjects
        """
        pass
    
    ##  Sets the SelectionFilter
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ##  Mask action 
    def SetSelectionFilter(selectObject: SelectObject, maskAction: NXOpen.Selection.SelectionAction, maskTriples: List[NXOpen.Selection.MaskTriple]) -> None:
        """
         Sets the SelectionFilter
        """
        pass
    
    ##  Tests the selection for this block. The block must be in focus to call this API
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ##  
    def TestSelection(selectObject: SelectObject, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Tests the selection for this block. The block must be in focus to call this API
        """
        pass
    
import NXOpen
##  Represents a Select Part From List block
## 
##   <br>  Created in NX8.5.0  <br> 

class SelectPartFromList(UIBlock): 
    """ Represents a Select Part From List block"""


    ##  Gets the SelectedObjects
    ##  @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectedObjects(selectPart: SelectPartFromList) -> List[NXOpen.TaggedObject]:
        """
         Gets the SelectedObjects
         @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
        """
        pass
    
    ##  Sets the SelectedObjects
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## Value to set for the property
    def SetSelectedObjects(selectPart: SelectPartFromList, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the SelectedObjects
        """
        pass
    
    ##  Tests the selection for this block. The block must be in focus to call this API
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## Value to set for the property
    def TestSelection(selectPart: SelectPartFromList, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Tests the selection for this block. The block must be in focus to call this API
        """
        pass
    
##  Represents a Separator block
## 
##   <br>  Created in NX8.5.0  <br> 

class Separator(UIBlock): 
    """ Represents a Separator block"""
    pass


##  Represents a SetList block 
## 
##   <br>  Created in NX6.0.0  <br> 

class SetList(UIBlock): 
    """ Represents a SetList block """


    ##  During Insert, indicates whether component should be
    ##     inserted before or after the insertion location 
    ##  
    class InsertionLocation(Enum):
        """
        Members Include: <Before> <After>
        """
        Before: int
        After: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SetList.InsertionLocation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) AddNewSetLabel
    ##   the AddNewSetLabel.  
    ##    Specifies the label for AddNewSet button.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def AddNewSetLabel(self) -> str:
        """
        Getter for property: (str) AddNewSetLabel
          the AddNewSetLabel.  
           Specifies the label for AddNewSet button.  
         
        """
        pass
    
    ## Setter for property: (str) AddNewSetLabel

    ##   the AddNewSetLabel.  
    ##    Specifies the label for AddNewSet button.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @AddNewSetLabel.setter
    def AddNewSetLabel(self, label: str):
        """
        Setter for property: (str) AddNewSetLabel
          the AddNewSetLabel.  
           Specifies the label for AddNewSet button.  
         
        """
        pass
    
    ## Getter for property: (int) DefaultColumnWidth
    ##   the DefaultColumnWidth  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def DefaultColumnWidth(self) -> int:
        """
        Getter for property: (int) DefaultColumnWidth
          the DefaultColumnWidth  
            
         
        """
        pass
    
    ## Setter for property: (int) DefaultColumnWidth

    ##   the DefaultColumnWidth  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @DefaultColumnWidth.setter
    def DefaultColumnWidth(self, defaultWidth: int):
        """
        Setter for property: (int) DefaultColumnWidth
          the DefaultColumnWidth  
            
         
        """
        pass
    
    ## Getter for property: (bool) IsAddButtonSensitive
    ##   the IsAddButtonSensitive  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def IsAddButtonSensitive(self) -> bool:
        """
        Getter for property: (bool) IsAddButtonSensitive
          the IsAddButtonSensitive  
            
         
        """
        pass
    
    ## Setter for property: (bool) IsAddButtonSensitive

    ##   the IsAddButtonSensitive  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @IsAddButtonSensitive.setter
    def IsAddButtonSensitive(self, addButton: bool):
        """
        Setter for property: (bool) IsAddButtonSensitive
          the IsAddButtonSensitive  
            
         
        """
        pass
    
    ## Getter for property: (str) LayoutAsString
    ##   the Layout as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def LayoutAsString(self) -> str:
        """
        Getter for property: (str) LayoutAsString
          the Layout as string  
            
         
        """
        pass
    
    ## Setter for property: (str) LayoutAsString

    ##   the Layout as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @LayoutAsString.setter
    def LayoutAsString(self, enumString: str):
        """
        Setter for property: (str) LayoutAsString
          the Layout as string  
            
         
        """
        pass
    
    ## Getter for property: (bool) ListExpanded
    ##   the ListExpanded.  
    ##    If true, the list is expanded.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ListExpanded(self) -> bool:
        """
        Getter for property: (bool) ListExpanded
          the ListExpanded.  
           If true, the list is expanded.  
         
        """
        pass
    
    ## Setter for property: (bool) ListExpanded

    ##   the ListExpanded.  
    ##    If true, the list is expanded.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ListExpanded.setter
    def ListExpanded(self, expanded: bool):
        """
        Setter for property: (bool) ListExpanded
          the ListExpanded.  
           If true, the list is expanded.  
         
        """
        pass
    
    ## Getter for property: (bool) ListHideGroup
    ##   the ListHideGroup  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ListHideGroup(self) -> bool:
        """
        Getter for property: (bool) ListHideGroup
          the ListHideGroup  
            
         
        """
        pass
    
    ## Setter for property: (bool) ListHideGroup

    ##   the ListHideGroup  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ListHideGroup.setter
    def ListHideGroup(self, listHideGroup: bool):
        """
        Setter for property: (bool) ListHideGroup
          the ListHideGroup  
            
         
        """
        pass
    
    ## Getter for property: (int) MaximumHeight
    ##   the MaximumHeight  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def MaximumHeight(self) -> int:
        """
        Getter for property: (int) MaximumHeight
          the MaximumHeight  
            
         
        """
        pass
    
    ## Setter for property: (int) MaximumHeight

    ##   the MaximumHeight  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MaximumHeight.setter
    def MaximumHeight(self, maxHeight: int):
        """
        Setter for property: (int) MaximumHeight
          the MaximumHeight  
            
         
        """
        pass
    
    ## Getter for property: (int) MinimumHeight
    ##   the MinimumHeight  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def MinimumHeight(self) -> int:
        """
        Getter for property: (int) MinimumHeight
          the MinimumHeight  
            
         
        """
        pass
    
    ## Setter for property: (int) MinimumHeight

    ##   the MinimumHeight  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MinimumHeight.setter
    def MinimumHeight(self, minHeight: int):
        """
        Setter for property: (int) MinimumHeight
          the MinimumHeight  
            
         
        """
        pass
    
    ## Getter for property: (bool) MultipleEdit
    ##   the MultipleEdit  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def MultipleEdit(self) -> bool:
        """
        Getter for property: (bool) MultipleEdit
          the MultipleEdit  
            
         
        """
        pass
    
    ## Setter for property: (bool) MultipleEdit

    ##   the MultipleEdit  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MultipleEdit.setter
    def MultipleEdit(self, multipleEdit: bool):
        """
        Setter for property: (bool) MultipleEdit
          the MultipleEdit  
            
         
        """
        pass
    
    ## Getter for property: (str) NumberColumnString
    ##   the NumberColumnString as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def NumberColumnString(self) -> str:
        """
        Getter for property: (str) NumberColumnString
          the NumberColumnString as string  
            
         
        """
        pass
    
    ## Setter for property: (str) NumberColumnString

    ##   the NumberColumnString as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @NumberColumnString.setter
    def NumberColumnString(self, columnString: str):
        """
        Setter for property: (str) NumberColumnString
          the NumberColumnString as string  
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfColumns
    ##   the NumberOfColumns  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def NumberOfColumns(self) -> int:
        """
        Getter for property: (int) NumberOfColumns
          the NumberOfColumns  
            
         
        """
        pass
    
    ## Setter for property: (int) NumberOfColumns

    ##   the NumberOfColumns  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @NumberOfColumns.setter
    def NumberOfColumns(self, numColumns: int):
        """
        Setter for property: (int) NumberOfColumns
          the NumberOfColumns  
            
         
        """
        pass
    
    ## Getter for property: (bool) ResizeHeightWithDialog
    ##   the ResizeHeightWithDialog.  
    ##    If true, height of the block changes dynamically with dialog.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ResizeHeightWithDialog(self) -> bool:
        """
        Getter for property: (bool) ResizeHeightWithDialog
          the ResizeHeightWithDialog.  
           If true, height of the block changes dynamically with dialog.  
         
        """
        pass
    
    ## Setter for property: (bool) ResizeHeightWithDialog

    ##   the ResizeHeightWithDialog.  
    ##    If true, height of the block changes dynamically with dialog.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ResizeHeightWithDialog.setter
    def ResizeHeightWithDialog(self, resize: bool):
        """
        Setter for property: (bool) ResizeHeightWithDialog
          the ResizeHeightWithDialog.  
           If true, height of the block changes dynamically with dialog.  
         
        """
        pass
    
    ## Getter for property: (str) SeedDlxFile
    ##   the SeedDlxFile as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def SeedDlxFile(self) -> str:
        """
        Getter for property: (str) SeedDlxFile
          the SeedDlxFile as string  
            
         
        """
        pass
    
    ## Setter for property: (str) SeedDlxFile

    ##   the SeedDlxFile as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @SeedDlxFile.setter
    def SeedDlxFile(self, dlxName: str):
        """
        Setter for property: (str) SeedDlxFile
          the SeedDlxFile as string  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowAddNewSet
    ##   the ShowAddNewSet.  
    ##    If true, "Add New Set" button is shown.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowAddNewSet(self) -> bool:
        """
        Getter for property: (bool) ShowAddNewSet
          the ShowAddNewSet.  
           If true, "Add New Set" button is shown.  
         
        """
        pass
    
    ## Setter for property: (bool) ShowAddNewSet

    ##   the ShowAddNewSet.  
    ##    If true, "Add New Set" button is shown.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowAddNewSet.setter
    def ShowAddNewSet(self, show: bool):
        """
        Setter for property: (bool) ShowAddNewSet
          the ShowAddNewSet.  
           If true, "Add New Set" button is shown.  
         
        """
        pass
    
    ## Getter for property: (bool) ShowColumnHeadings
    ##   the ShowColumnHeadings  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowColumnHeadings(self) -> bool:
        """
        Getter for property: (bool) ShowColumnHeadings
          the ShowColumnHeadings  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowColumnHeadings

    ##   the ShowColumnHeadings  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowColumnHeadings.setter
    def ShowColumnHeadings(self, show: bool):
        """
        Setter for property: (bool) ShowColumnHeadings
          the ShowColumnHeadings  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowRemove
    ##   the ShowRemove.  
    ##    If true, "Remove" button is shown.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowRemove(self) -> bool:
        """
        Getter for property: (bool) ShowRemove
          the ShowRemove.  
           If true, "Remove" button is shown.  
         
        """
        pass
    
    ## Setter for property: (bool) ShowRemove

    ##   the ShowRemove.  
    ##    If true, "Remove" button is shown.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowRemove.setter
    def ShowRemove(self, show: bool):
        """
        Setter for property: (bool) ShowRemove
          the ShowRemove.  
           If true, "Remove" button is shown.  
         
        """
        pass
    
    ## Getter for property: (bool) ShowReorderControls
    ##   the ShowReorderControls  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowReorderControls(self) -> bool:
        """
        Getter for property: (bool) ShowReorderControls
          the ShowReorderControls  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowReorderControls

    ##   the ShowReorderControls  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowReorderControls.setter
    def ShowReorderControls(self, show: bool):
        """
        Setter for property: (bool) ShowReorderControls
          the ShowReorderControls  
            
         
        """
        pass
    
    ##  Add callback 
    ## A callback definition with the following input arguments: 
    ##  - @link SetList NXOpen.BlockStyler.SetList@endlink
    ##  and no return type
    AddCallback = Callable[[SetList], None]
    
    
    ##  Adds an item to the end of the list 
    ##  @return uicomp (@link UIBlock NXOpen.BlockStyler.UIBlock@endlink):  The added item .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  Indicates whether to copy properties from the 
    ##                 currently selected component and set focus to the new set 
    def AddNewSet(block: SetList, copyPropertiesAndSelect: bool) -> UIBlock:
        """
         Adds an item to the end of the list 
         @return uicomp (@link UIBlock NXOpen.BlockStyler.UIBlock@endlink):  The added item .
        """
        pass
    
    ##  Deletes an item from the list 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  Item to delete 
    def Delete(block: SetList, uicomp: UIBlock) -> None:
        """
         Deletes an item from the list 
        """
        pass
    
    ##  Delete callback.  Return a non-zero value in order to veto the deletion. 
    ## A callback definition with the following input arguments: 
    ##  - @link SetList NXOpen.BlockStyler.SetList@endlink
    ##  - @link UIBlock NXOpen.BlockStyler.UIBlock@endlink
    ##  and no return type
    DeleteCallback = Callable[[SetList, UIBlock], None]
    
    
    ##  When an update event occurs on the list, this method finds the
    ##     item in the list that was updated 
    ##  @return item (@link UIBlock NXOpen.BlockStyler.UIBlock@endlink): .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def FindUpdated(block: SetList) -> UIBlock:
        """
         When an update event occurs on the list, this method finds the
            item in the list that was updated 
         @return item (@link UIBlock NXOpen.BlockStyler.UIBlock@endlink): .
        """
        pass
    
    ##  Gets the ColumnLabels
    ##  @return labels (List[str]):  Values to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetColumnLabels(block: SetList) -> List[str]:
        """
         Gets the ColumnLabels
         @return labels (List[str]):  Values to get from the property.
        """
        pass
    
    ##  Gets the ColumnWidths
    ##  @return width (List[int]):  Values to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetColumnWidths(block: SetList) -> List[int]:
        """
         Gets the ColumnWidths
         @return width (List[int]):  Values to get from the property.
        """
        pass
    
    ##  Gets the text for the specified item.
    ##         If the list has a title column, the title column is not included in the item text. 
    ##  @return strings (List[str]):  The text .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  
    def GetItemText(block: SetList, item: UIBlock) -> List[str]:
        """
         Gets the text for the specified item.
                If the list has a title column, the title column is not included in the item text. 
         @return strings (List[str]):  The text .
        """
        pass
    
    ##  Gets all the items in the list 
    ##  @return items (@link UIBlock List[NXOpen.BlockStyler.UIBlock]@endlink): .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetItems(block: SetList) -> List[UIBlock]:
        """
         Gets all the items in the list 
         @return items (@link UIBlock List[NXOpen.BlockStyler.UIBlock]@endlink): .
        """
        pass
    
    ##  Gets the Layout members
    ##  @return member_strings (List[str]): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetLayoutMembers(block: SetList) -> List[str]:
        """
         Gets the Layout members
         @return member_strings (List[str]): .
        """
        pass
    
    ##  Gets the selected items 
    ##  @return items (@link UIBlock List[NXOpen.BlockStyler.UIBlock]@endlink): .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelected(block: SetList) -> List[UIBlock]:
        """
         Gets the selected items 
         @return items (@link UIBlock List[NXOpen.BlockStyler.UIBlock]@endlink): .
        """
        pass
    
    ##  Inserts an item before or after a specified item 
    ##  @return uicomp (@link UIBlock NXOpen.BlockStyler.UIBlock@endlink):  The inserted item .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  Location to insert the new item 
    def InsertNewSet(block: SetList, location: UIBlock, insertBeforeOrAfter: SetList.InsertionLocation, copyPropertiesAndSelect: bool) -> UIBlock:
        """
         Inserts an item before or after a specified item 
         @return uicomp (@link UIBlock NXOpen.BlockStyler.UIBlock@endlink):  The inserted item .
        """
        pass
    
    ##  Reorder callback 
    ## A callback definition with the following input arguments: 
    ##  - @link SetList NXOpen.BlockStyler.SetList@endlink
    ##  - @link UIBlock NXOpen.BlockStyler.UIBlock@endlink
    ##  - int
    ##  - int
    ##  and no return type
    ReorderCallback = Callable[[SetList, UIBlock, int, int], None]
    
    
    ##  Sets the AddNewSet handler.  If you set this handler, the handler will be
    ##     called when the Add New Set button is pressed, and the handler will be responsible
    ##     for adding an item to the list.  Nothing will be added to the list unless the handler
    ##     adds it. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetAddHandler(dialog: SetList, cb: SetList.AddCallback) -> None:
        """
         Sets the AddNewSet handler.  If you set this handler, the handler will be
            called when the Add New Set button is pressed, and the handler will be responsible
            for adding an item to the list.  Nothing will be added to the list unless the handler
            adds it. 
        """
        pass
    
    ##  Sets the ColumnLabels
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ##  Values to set to the property
    def SetColumnLabels(block: SetList, labels: List[str]) -> None:
        """
         Sets the ColumnLabels
        """
        pass
    
    ##  Sets the ColumnWidths
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ##  Values to set to the property
    def SetColumnWidths(block: SetList, width: List[int]) -> None:
        """
         Sets the ColumnWidths
        """
        pass
    
    ##  Sets the Delete handler.  If you set this handler, the handler will be
    ##     called when the Delete button is pressed.  The handler does not need to implement code
    ##     to delete the item.  The list will delete the item if and only if the handler returns 0. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetDeleteHandler(dialog: SetList, cb: SetList.DeleteCallback) -> None:
        """
         Sets the Delete handler.  If you set this handler, the handler will be
            called when the Delete button is pressed.  The handler does not need to implement code
            to delete the item.  The list will delete the item if and only if the handler returns 0. 
        """
        pass
    
    ##  Sets the text for the specified item.
    ##         If the list has a title column, the title column is not included in the item text. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetItemText(block: SetList, item: UIBlock, strings: List[str]) -> None:
        """
         Sets the text for the specified item.
                If the list has a title column, the title column is not included in the item text. 
        """
        pass
    
    ##  Sets the Reorder observer.  If you set this observer, the observer will
    ##     be called after an item is moved by pressing the Move Up and Down buttons.
    ##     The observer does not need to implement the move up and down behavior and is called
    ##     after the item has already been moved. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetReorderObserver(dialog: SetList, cb: SetList.ReorderCallback) -> None:
        """
         Sets the Reorder observer.  If you set this observer, the observer will
            be called after an item is moved by pressing the Move Up and Down buttons.
            The observer does not need to implement the move up and down behavior and is called
            after the item has already been moved. 
        """
        pass
    
    ##  Sets the seed using a dlx file.  The seed must be set during initialization.
    ##     Setting the seed will also reset any Add and Delete handlers that has been registered,
    ##     so SetSeed should be called prior to calling SetAddHandler or SetDeleteHandler. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  The dlx file used to create the seed 
    def SetSeed(block: SetList, dlxFile: str) -> None:
        """
         Sets the seed using a dlx file.  The seed must be set during initialization.
            Setting the seed will also reset any Add and Delete handlers that has been registered,
            so SetSeed should be called prior to calling SetAddHandler or SetDeleteHandler. 
        """
        pass
    
    ##  Sets the selected items.  If the "Multiple Edit" property is false,
    ##     no more than one item can be selected 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetSelected(block: SetList, items: List[UIBlock]) -> None:
        """
         Sets the selected items.  If the "Multiple Edit" property is false,
            no more than one item can be selected 
        """
        pass
    
    ##  Swaps the location of two items 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  Item to swap 
    def Swap(block: SetList, uicomp1: UIBlock, uicomp2: UIBlock) -> None:
        """
         Swaps the location of two items 
        """
        pass
    
    ## Tests add event mapped to this SetList block.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    @staticmethod
    def TestItemAdded(block: SetList) -> None:
        """
        Tests add event mapped to this SetList block.
        """
        pass
    
    ## Tests delete event mapped to this SetList block.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    @staticmethod
    def TestItemDeleted(block: SetList) -> None:
        """
        Tests delete event mapped to this SetList block.
        """
        pass
    
    ## Tests move down event mapped to this SetList block.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    @staticmethod
    def TestItemMovedDown(block: SetList) -> None:
        """
        Tests move down event mapped to this SetList block.
        """
        pass
    
    ## Tests move up event mapped to this SetList block.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    @staticmethod
    def TestItemMovedUp(block: SetList) -> None:
        """
        Tests move up event mapped to this SetList block.
        """
        pass
    
import NXOpen
##  Represents a Specify Axis block
## 
##   <br>  Created in NX8.5.0  <br> 

class SpecifyAxis(UIBlock): 
    """ Represents a Specify Axis block"""


    ## Getter for property: (str) BalloonTooltipLayoutAsString
    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipLayoutAsString

    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipPointImage
    ##   the BalloonTooltipPointImage  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipPointImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipPointImage
          the BalloonTooltipPointImage  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipPointImage

    ##   the BalloonTooltipPointImage  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipPointImage.setter
    def BalloonTooltipPointImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipPointImage
          the BalloonTooltipPointImage  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipPointText
    ##   the BalloonTooltipPointText  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipPointText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipPointText
          the BalloonTooltipPointText  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipPointText

    ##   the BalloonTooltipPointText  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipPointText.setter
    def BalloonTooltipPointText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipPointText
          the BalloonTooltipPointText  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipVectorImage
    ##   the BalloonTooltipVectorImage  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipVectorImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipVectorImage
          the BalloonTooltipVectorImage  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipVectorImage

    ##   the BalloonTooltipVectorImage  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipVectorImage.setter
    def BalloonTooltipVectorImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipVectorImage
          the BalloonTooltipVectorImage  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipVectorText
    ##   the BalloonTooltipVectorText  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipVectorText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipVectorText
          the BalloonTooltipVectorText  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipVectorText

    ##   the BalloonTooltipVectorText  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipVectorText.setter
    def BalloonTooltipVectorText(self, tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipVectorText
          the BalloonTooltipVectorText  
            
         
        """
        pass
    
    ## Getter for property: (str) StepStatusAsString
    ##   the StepStatus as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
          the StepStatus as string  
            
         
        """
        pass
    
    ## Setter for property: (str) StepStatusAsString

    ##   the StepStatus as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
          the StepStatus as string  
            
         
        """
        pass
    
    ##  Gets the BalloonTooltipLayout members 
    ##  @return layout_strings (List[str]): Value to get from the property. .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBalloonTooltipLayoutMembers(specifyAxis: SpecifyAxis) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         @return layout_strings (List[str]): Value to get from the property. .
        """
        pass
    
    ##  Gets the SelectedObjects
    ##  @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectedObjects(specifyAxis: SpecifyAxis) -> List[NXOpen.TaggedObject]:
        """
         Gets the SelectedObjects
         @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
        """
        pass
    
    ##  Gets the StepStatus members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStepStatusMembers(specifyAxis: SpecifyAxis) -> List[str]:
        """
         Gets the StepStatus members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Sets the SelectedObjects
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## Value to set for the property
    def SetSelectedObjects(specifyAxis: SpecifyAxis, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the SelectedObjects
        """
        pass
    
    ##  Tests the selection for this block. The block must be in focus to call this API
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## Value to set for the property
    def TestSelection(specifyAxis: SpecifyAxis, objectVector: NXOpen.TaggedObject) -> None:
        """
         Tests the selection for this block. The block must be in focus to call this API
        """
        pass
    
import NXOpen
##  Represents a Specify CSYS block
## 
##   <br>  Created in NX8.5.0  <br> 

class SpecifyCSYS(UIBlock): 
    """ Represents a Specify CSYS block"""


    ## Getter for property: (bool) AutomaticProgression
    ##   the AutomaticProgression  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def AutomaticProgression(self) -> bool:
        """
        Getter for property: (bool) AutomaticProgression
          the AutomaticProgression  
            
         
        """
        pass
    
    ## Setter for property: (bool) AutomaticProgression

    ##   the AutomaticProgression  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @AutomaticProgression.setter
    def AutomaticProgression(self, automaticProgression: bool):
        """
        Setter for property: (bool) AutomaticProgression
          the AutomaticProgression  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipImage
    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipImage

    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipLayoutAsString
    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipLayoutAsString

    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipText
    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipText

    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Getter for property: (bool) CreateInterpartLink
    ##   the CreateInterpartLink  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def CreateInterpartLink(self) -> bool:
        """
        Getter for property: (bool) CreateInterpartLink
          the CreateInterpartLink  
            
         
        """
        pass
    
    ## Setter for property: (bool) CreateInterpartLink

    ##   the CreateInterpartLink  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @CreateInterpartLink.setter
    def CreateInterpartLink(self, createLink: bool):
        """
        Setter for property: (bool) CreateInterpartLink
          the CreateInterpartLink  
            
         
        """
        pass
    
    ## Getter for property: (str) InterpartSelectionAsString
    ##   the InterpartSelection as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def InterpartSelectionAsString(self) -> str:
        """
        Getter for property: (str) InterpartSelectionAsString
          the InterpartSelection as string  
            
         
        """
        pass
    
    ## Setter for property: (str) InterpartSelectionAsString

    ##   the InterpartSelection as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @InterpartSelectionAsString.setter
    def InterpartSelectionAsString(self, enumString: str):
        """
        Setter for property: (str) InterpartSelectionAsString
          the InterpartSelection as string  
            
         
        """
        pass
    
    ## Getter for property: (str) LabelString
    ##   the LabelString  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
          the LabelString  
            
         
        """
        pass
    
    ## Setter for property: (str) LabelString

    ##   the LabelString  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
          the LabelString  
            
         
        """
        pass
    
    ## Getter for property: (str) OutputTypeAsString
    ##   the OutputType as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def OutputTypeAsString(self) -> str:
        """
        Getter for property: (str) OutputTypeAsString
          the OutputType as string  
            
         
        """
        pass
    
    ## Setter for property: (str) OutputTypeAsString

    ##   the OutputType as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @OutputTypeAsString.setter
    def OutputTypeAsString(self, enumString: str):
        """
        Setter for property: (str) OutputTypeAsString
          the OutputType as string  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowShortcuts
    ##   the ShowShortcuts  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def ShowShortcuts(self) -> bool:
        """
        Getter for property: (bool) ShowShortcuts
          the ShowShortcuts  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowShortcuts

    ##   the ShowShortcuts  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ShowShortcuts.setter
    def ShowShortcuts(self, show: bool):
        """
        Setter for property: (bool) ShowShortcuts
          the ShowShortcuts  
            
         
        """
        pass
    
    ## Getter for property: (str) SmartUpdateOptionAsString
    ##   the SmartUpdateOption as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.1  <br> 

    ## @return str
    @property
    def SmartUpdateOptionAsString(self) -> str:
        """
        Getter for property: (str) SmartUpdateOptionAsString
          the SmartUpdateOption as string  
            
         
        """
        pass
    
    ## Setter for property: (str) SmartUpdateOptionAsString

    ##   the SmartUpdateOption as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.1  <br> 

    @SmartUpdateOptionAsString.setter
    def SmartUpdateOptionAsString(self, enumString: str):
        """
        Setter for property: (str) SmartUpdateOptionAsString
          the SmartUpdateOption as string  
            
         
        """
        pass
    
    ## Getter for property: (str) SmartUpdteOptionAsString
    ##   the SmartUpdateOption as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX9.0.1.  Use @link BlockStyler::SpecifyCSYS::SmartUpdateOptionAsString BlockStyler::SpecifyCSYS::SmartUpdateOptionAsString@endlink  instead  <br> 

    ## @return str
    @property
    def SmartUpdteOptionAsString(self) -> str:
        """
        Getter for property: (str) SmartUpdteOptionAsString
          the SmartUpdateOption as string  
            
         
        """
        pass
    
    ## Setter for property: (str) SmartUpdteOptionAsString

    ##   the SmartUpdateOption as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX9.0.1.  Use @link BlockStyler::SpecifyCSYS::SetSmartUpdateOptionAsString BlockStyler::SpecifyCSYS::SetSmartUpdateOptionAsString@endlink  instead  <br> 

    @SmartUpdteOptionAsString.setter
    def SmartUpdteOptionAsString(self, enumString: str):
        """
        Setter for property: (str) SmartUpdteOptionAsString
          the SmartUpdateOption as string  
            
         
        """
        pass
    
    ## Getter for property: (str) StepStatusAsString
    ##   the StepStatus as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
          the StepStatus as string  
            
         
        """
        pass
    
    ## Setter for property: (str) StepStatusAsString

    ##   the StepStatus as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
          the StepStatus as string  
            
         
        """
        pass
    
    ##  Gets the BalloonTooltipLayout members 
    ##  @return layout_strings (List[str]): Value to get from the property. .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBalloonTooltipLayoutMembers(specifyCSYS: SpecifyCSYS) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         @return layout_strings (List[str]): Value to get from the property. .
        """
        pass
    
    ##  Gets the InterpartSelection members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetInterpartSelectionMembers(specifyCSYS: SpecifyCSYS) -> List[str]:
        """
         Gets the InterpartSelection members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Gets the OutputType members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetOutputTypeMembers(specifyCSYS: SpecifyCSYS) -> List[str]:
        """
         Gets the OutputType members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Gets the SelectedObjects
    ##  @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectedObjects(specifyCSYS: SpecifyCSYS) -> List[NXOpen.TaggedObject]:
        """
         Gets the SelectedObjects
         @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
        """
        pass
    
    ##  Gets the SmartUpdateOption members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX9.0.1  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSmartUpdateOptionMembers(specifyCSYS: SpecifyCSYS) -> List[str]:
        """
         Gets the SmartUpdateOption members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Gets the SmartUpdateOption members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX9.0.1.  Use @link BlockStyler::SpecifyCSYS::GetSmartUpdateOptionMembers BlockStyler::SpecifyCSYS::GetSmartUpdateOptionMembers@endlink  instead  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSmartUpdteOptionMembers(specifyCSYS: SpecifyCSYS) -> List[str]:
        """
         Gets the SmartUpdateOption members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Gets the StepStatus members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStepStatusMembers(specifyCSYS: SpecifyCSYS) -> List[str]:
        """
         Gets the StepStatus members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Sets the SelectedObjects
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## Value to set for the property
    def SetSelectedObjects(specifyCSYS: SpecifyCSYS, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the SelectedObjects
        """
        pass
    
    ##  Tests the selection for this block. The block must be in focus to call this API
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## Value to set for the property
    def TestSelection(specifyCSYS: SpecifyCSYS, objectVector: NXOpen.TaggedObject) -> None:
        """
         Tests the selection for this block. The block must be in focus to call this API
        """
        pass
    
import NXOpen
##  Represents a Specify Location block
## 
##   <br>  Created in NX8.5.0  <br> 

class SpecifyLocation(UIBlock): 
    """ Represents a Specify Location block"""


    ## Getter for property: (bool) AutomaticProgression
    ##   the AutomaticProgression  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def AutomaticProgression(self) -> bool:
        """
        Getter for property: (bool) AutomaticProgression
          the AutomaticProgression  
            
         
        """
        pass
    
    ## Setter for property: (bool) AutomaticProgression

    ##   the AutomaticProgression  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @AutomaticProgression.setter
    def AutomaticProgression(self, automaticProgression: bool):
        """
        Setter for property: (bool) AutomaticProgression
          the AutomaticProgression  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) CursorLocation
    ##   the CursorLocation  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def CursorLocation(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) CursorLocation
          the CursorLocation  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) CursorLocation

    ##   the CursorLocation  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @CursorLocation.setter
    def CursorLocation(self, cursorLocation: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) CursorLocation
          the CursorLocation  
            
         
        """
        pass
    
    ## Getter for property: (bool) DisplayTemporaryPoint
    ##   the DisplayTemporaryPoint  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def DisplayTemporaryPoint(self) -> bool:
        """
        Getter for property: (bool) DisplayTemporaryPoint
          the DisplayTemporaryPoint  
            
         
        """
        pass
    
    ## Setter for property: (bool) DisplayTemporaryPoint

    ##   the DisplayTemporaryPoint  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @DisplayTemporaryPoint.setter
    def DisplayTemporaryPoint(self, display: bool):
        """
        Setter for property: (bool) DisplayTemporaryPoint
          the DisplayTemporaryPoint  
            
         
        """
        pass
    
    ## Getter for property: (str) LabelString
    ##   the LabelString  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
          the LabelString  
            
         
        """
        pass
    
    ## Setter for property: (str) LabelString

    ##   the LabelString  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
          the LabelString  
            
         
        """
        pass
    
    ## Getter for property: (bool) LocationSpecified
    ##   whether the cursor location has been set or not.  
    ##    Initially, this will return false, 
    ##             but will return true after the user has specified a location interactively, 
    ##             or if  @link SetCursorLocation SetCursorLocation@endlink  is set programmatically. 
    ##             Calling @link ResetCursorLocation ResetCursorLocation@endlink  will also reset this property back to false. 
    ##             If this property is false, then the value of @link CursorLocation CursorLocation@endlink  is meaningless  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def LocationSpecified(self) -> bool:
        """
        Getter for property: (bool) LocationSpecified
          whether the cursor location has been set or not.  
           Initially, this will return false, 
                    but will return true after the user has specified a location interactively, 
                    or if  @link SetCursorLocation SetCursorLocation@endlink  is set programmatically. 
                    Calling @link ResetCursorLocation ResetCursorLocation@endlink  will also reset this property back to false. 
                    If this property is false, then the value of @link CursorLocation CursorLocation@endlink  is meaningless  
         
        """
        pass
    
    ## Getter for property: (str) StepStatusAsString
    ##   the StepStatus as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
          the StepStatus as string  
            
         
        """
        pass
    
    ## Setter for property: (str) StepStatusAsString

    ##   the StepStatus as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
          the StepStatus as string  
            
         
        """
        pass
    
    ##  Gets the StepStatus members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStepStatusMembers(specifyLocation: SpecifyLocation) -> List[str]:
        """
         Gets the StepStatus members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Reset the cursor location
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def ResetCursorLocation(specifyLocation: SpecifyLocation) -> None:
        """
         Reset the cursor location
        """
        pass
    
    ##  Tests the cursor location specified for this block. The block must be in focus to call this API
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="cursorLocation"> (@link NXOpen.Point3d NXOpen.Point3d@endlink) </param>
    def TestCursorLocationSpecified(specifyLocation: SpecifyLocation, cursorLocation: NXOpen.Point3d) -> None:
        """
         Tests the cursor location specified for this block. The block must be in focus to call this API
        """
        pass
    
import NXOpen
##  Represents Specify Orientation block
## 
##   <br>  Created in NX8.5.0  <br> 

class SpecifyOrientation(UIBlock): 
    """ Represents Specify Orientation block"""


    ## Getter for property: (str) BalloonTooltipImage
    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipImage

    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipLayoutAsString
    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipLayoutAsString

    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipText
    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipText

    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Getter for property: (bool) EnableDoubleClickFlip
    ##   the EnableDoubleClickFlip.  
    ##    If true, flipping is allowed when direction handle is double clicked.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def EnableDoubleClickFlip(self) -> bool:
        """
        Getter for property: (bool) EnableDoubleClickFlip
          the EnableDoubleClickFlip.  
           If true, flipping is allowed when direction handle is double clicked.  
         
        """
        pass
    
    ## Setter for property: (bool) EnableDoubleClickFlip

    ##   the EnableDoubleClickFlip.  
    ##    If true, flipping is allowed when direction handle is double clicked.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @EnableDoubleClickFlip.setter
    def EnableDoubleClickFlip(self, enableFlip: bool):
        """
        Setter for property: (bool) EnableDoubleClickFlip
          the EnableDoubleClickFlip.  
           If true, flipping is allowed when direction handle is double clicked.  
         
        """
        pass
    
    ## Getter for property: (bool) EnableFacetSelection
    ##   the EnableFacetSelection  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def EnableFacetSelection(self) -> bool:
        """
        Getter for property: (bool) EnableFacetSelection
          the EnableFacetSelection  
            
         
        """
        pass
    
    ## Setter for property: (bool) EnableFacetSelection

    ##   the EnableFacetSelection  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @EnableFacetSelection.setter
    def EnableFacetSelection(self, enableSelection: bool):
        """
        Setter for property: (bool) EnableFacetSelection
          the EnableFacetSelection  
            
         
        """
        pass
    
    ## Getter for property: (bool) HasOriginGwif
    ##   the HasOriginGwif  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def HasOriginGwif(self) -> bool:
        """
        Getter for property: (bool) HasOriginGwif
          the HasOriginGwif  
            
         
        """
        pass
    
    ## Setter for property: (bool) HasOriginGwif

    ##   the HasOriginGwif  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @HasOriginGwif.setter
    def HasOriginGwif(self, originGwif: bool):
        """
        Setter for property: (bool) HasOriginGwif
          the HasOriginGwif  
            
         
        """
        pass
    
    ## Getter for property: (bool) IsOriginSpecified
    ##   the IsOriginSpecified  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def IsOriginSpecified(self) -> bool:
        """
        Getter for property: (bool) IsOriginSpecified
          the IsOriginSpecified  
            
         
        """
        pass
    
    ## Setter for property: (bool) IsOriginSpecified

    ##   the IsOriginSpecified  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @IsOriginSpecified.setter
    def IsOriginSpecified(self, originSpecified: bool):
        """
        Setter for property: (bool) IsOriginSpecified
          the IsOriginSpecified  
            
         
        """
        pass
    
    ## Getter for property: (bool) IsWCSCoordinates
    ##   the IsWCSCoordinates  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def IsWCSCoordinates(self) -> bool:
        """
        Getter for property: (bool) IsWCSCoordinates
          the IsWCSCoordinates  
            
         
        """
        pass
    
    ## Setter for property: (bool) IsWCSCoordinates

    ##   the IsWCSCoordinates  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @IsWCSCoordinates.setter
    def IsWCSCoordinates(self, wcsCoordinates: bool):
        """
        Setter for property: (bool) IsWCSCoordinates
          the IsWCSCoordinates  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Origin
    ##   the Origin  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def Origin(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Origin
          the Origin  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Origin

    ##   the Origin  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Origin.setter
    def Origin(self, origin: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Origin
          the Origin  
            
         
        """
        pass
    
    ## Getter for property: (int) SnapPointTypesOnByDefault
    ##   the SnapPointTypesOnByDefault  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def SnapPointTypesOnByDefault(self) -> int:
        """
        Getter for property: (int) SnapPointTypesOnByDefault
          the SnapPointTypesOnByDefault  
            
         
        """
        pass
    
    ## Setter for property: (int) SnapPointTypesOnByDefault

    ##   the SnapPointTypesOnByDefault  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @SnapPointTypesOnByDefault.setter
    def SnapPointTypesOnByDefault(self, snapPointTypes: int):
        """
        Setter for property: (int) SnapPointTypesOnByDefault
          the SnapPointTypesOnByDefault  
            
         
        """
        pass
    
    ## Getter for property: (int) VisibleManipulatorHandles
    ##   the VisibleManipulatorHandles.  
    ##    It specifies the options to display the handles available on triad. The translation, rotation and origin handles are available.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def VisibleManipulatorHandles(self) -> int:
        """
        Getter for property: (int) VisibleManipulatorHandles
          the VisibleManipulatorHandles.  
           It specifies the options to display the handles available on triad. The translation, rotation and origin handles are available.  
         
        """
        pass
    
    ## Setter for property: (int) VisibleManipulatorHandles

    ##   the VisibleManipulatorHandles.  
    ##    It specifies the options to display the handles available on triad. The translation, rotation and origin handles are available.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @VisibleManipulatorHandles.setter
    def VisibleManipulatorHandles(self, handles: int):
        """
        Setter for property: (int) VisibleManipulatorHandles
          the VisibleManipulatorHandles.  
           It specifies the options to display the handles available on triad. The translation, rotation and origin handles are available.  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) XAxis
    ##   the XAxis  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.Vector3d
    @property
    def XAxis(self) -> NXOpen.Vector3d:
        """
        Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) XAxis
          the XAxis  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) XAxis

    ##   the XAxis  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @XAxis.setter
    def XAxis(self, xAxis: NXOpen.Vector3d):
        """
        Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) XAxis
          the XAxis  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) YAxis
    ##   the YAxis  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.Vector3d
    @property
    def YAxis(self) -> NXOpen.Vector3d:
        """
        Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) YAxis
          the YAxis  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) YAxis

    ##   the YAxis  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @YAxis.setter
    def YAxis(self, yAxis: NXOpen.Vector3d):
        """
        Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) YAxis
          the YAxis  
            
         
        """
        pass
    
    ##  Gets the BalloonTooltipLayout members 
    ##  @return layout_strings (List[str]): Value to get from the property. .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBalloonTooltipLayoutMembers(specifyOrientation: SpecifyOrientation) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         @return layout_strings (List[str]): Value to get from the property. .
        """
        pass
    
    ##  Tests the origin of orientation specified for this block. The block must be in focus to call this API
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="origin"> (@link NXOpen.Point3d NXOpen.Point3d@endlink) </param>
    def TestOriginSpecified(specifyOrientation: SpecifyOrientation, origin: NXOpen.Point3d) -> None:
        """
         Tests the origin of orientation specified for this block. The block must be in focus to call this API
        """
        pass
    
    ##  Tests the X-Axis of orientation specified for this block. The block must be in focus to call this API
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="xAxis"> (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) </param>
    def TestXAxisSpecified(specifyOrientation: SpecifyOrientation, xAxis: NXOpen.Vector3d) -> None:
        """
         Tests the X-Axis of orientation specified for this block. The block must be in focus to call this API
        """
        pass
    
    ##  Tests the Y-Axis of orientation specified for this block. The block must be in focus to call this API
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="yAxis"> (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) </param>
    def TestYAxisSpecified(specifyOrientation: SpecifyOrientation, yAxis: NXOpen.Vector3d) -> None:
        """
         Tests the Y-Axis of orientation specified for this block. The block must be in focus to call this API
        """
        pass
    
import NXOpen
##  Represents a Specify Plane block
## 
##   <br>  Created in NX8.5.0  <br> 

class SpecifyPlane(UIBlock): 
    """ Represents a Specify Plane block"""


    ## Getter for property: (bool) AutomaticProgression
    ##   the AutomaticProgression  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def AutomaticProgression(self) -> bool:
        """
        Getter for property: (bool) AutomaticProgression
          the AutomaticProgression  
            
         
        """
        pass
    
    ## Setter for property: (bool) AutomaticProgression

    ##   the AutomaticProgression  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @AutomaticProgression.setter
    def AutomaticProgression(self, automaticProgression: bool):
        """
        Setter for property: (bool) AutomaticProgression
          the AutomaticProgression  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipImage
    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipImage

    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipLayoutAsString
    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipLayoutAsString

    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipText
    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipText

    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Getter for property: (bool) CreateInterpartLink
    ##   the CreateInterpartLink  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def CreateInterpartLink(self) -> bool:
        """
        Getter for property: (bool) CreateInterpartLink
          the CreateInterpartLink  
            
         
        """
        pass
    
    ## Setter for property: (bool) CreateInterpartLink

    ##   the CreateInterpartLink  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @CreateInterpartLink.setter
    def CreateInterpartLink(self, createLink: bool):
        """
        Setter for property: (bool) CreateInterpartLink
          the CreateInterpartLink  
            
         
        """
        pass
    
    ## Getter for property: (str) CurrentStepStatusAsString
    ##   the string specifying current StepStatus   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def CurrentStepStatusAsString(self) -> str:
        """
        Getter for property: (str) CurrentStepStatusAsString
          the string specifying current StepStatus   
            
         
        """
        pass
    
    ## Getter for property: (str) InterpartSelectionAsString
    ##   the InterpartSelection as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return str
    @property
    def InterpartSelectionAsString(self) -> str:
        """
        Getter for property: (str) InterpartSelectionAsString
          the InterpartSelection as string  
            
         
        """
        pass
    
    ## Setter for property: (str) InterpartSelectionAsString

    ##   the InterpartSelection as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @InterpartSelectionAsString.setter
    def InterpartSelectionAsString(self, enumString: str):
        """
        Setter for property: (str) InterpartSelectionAsString
          the InterpartSelection as string  
            
         
        """
        pass
    
    ## Getter for property: (str) LabelString
    ##   the LabelString  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
          the LabelString  
            
         
        """
        pass
    
    ## Setter for property: (str) LabelString

    ##   the LabelString  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
          the LabelString  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowShortcuts
    ##   the ShowShortcuts  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowShortcuts(self) -> bool:
        """
        Getter for property: (bool) ShowShortcuts
          the ShowShortcuts  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowShortcuts

    ##   the ShowShortcuts  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowShortcuts.setter
    def ShowShortcuts(self, show: bool):
        """
        Setter for property: (bool) ShowShortcuts
          the ShowShortcuts  
            
         
        """
        pass
    
    ## Getter for property: (str) StepStatusAsString
    ##   the string specifying the default StepStatus   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
          the string specifying the default StepStatus   
            
         
        """
        pass
    
    ## Setter for property: (str) StepStatusAsString

    ##   the string specifying the default StepStatus   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
          the string specifying the default StepStatus   
            
         
        """
        pass
    
    ##  Gets the BalloonTooltipLayout members 
    ##  @return layout_strings (List[str]): Value to get from the property. .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBalloonTooltipLayoutMembers(specifyPlane: SpecifyPlane) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         @return layout_strings (List[str]): Value to get from the property. .
        """
        pass
    
    ##  Gets the InterpartSelection members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetInterpartSelectionMembers(specifyPlane: SpecifyPlane) -> List[str]:
        """
         Gets the InterpartSelection members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Gets the SelectedObjects
    ##  @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectedObjects(specifyPlane: SpecifyPlane) -> List[NXOpen.TaggedObject]:
        """
         Gets the SelectedObjects
         @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
        """
        pass
    
    ##  Gets the StepStatus members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStepStatusMembers(specifyPlane: SpecifyPlane) -> List[str]:
        """
         Gets the StepStatus members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Sets the SelectedObjects
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## Value to set for the property
    def SetSelectedObjects(specifyPlane: SpecifyPlane, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the SelectedObjects
        """
        pass
    
    ##  Tests the selection for this block. The block must be in focus to call this API
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## Value to set for the property
    def TestSelection(specifyPlane: SpecifyPlane, objectVector: NXOpen.TaggedObject) -> None:
        """
         Tests the selection for this block. The block must be in focus to call this API
        """
        pass
    
import NXOpen
##  Represents a Specify Point block
## 
##   <br>  Created in NX8.5.0  <br> 

class SpecifyPoint(UIBlock): 
    """ Represents a Specify Point block"""


    ## Getter for property: (bool) AutomaticProgression
    ##   the AutomaticProgression  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def AutomaticProgression(self) -> bool:
        """
        Getter for property: (bool) AutomaticProgression
          the AutomaticProgression  
            
         
        """
        pass
    
    ## Setter for property: (bool) AutomaticProgression

    ##   the AutomaticProgression  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @AutomaticProgression.setter
    def AutomaticProgression(self, automaticProgression: bool):
        """
        Setter for property: (bool) AutomaticProgression
          the AutomaticProgression  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipImage
    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipImage

    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipLayoutAsString
    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipLayoutAsString

    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipText
    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipText

    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Getter for property: (bool) CreateInterpartLink
    ##   the CreateInterpartLink  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def CreateInterpartLink(self) -> bool:
        """
        Getter for property: (bool) CreateInterpartLink
          the CreateInterpartLink  
            
         
        """
        pass
    
    ## Setter for property: (bool) CreateInterpartLink

    ##   the CreateInterpartLink  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @CreateInterpartLink.setter
    def CreateInterpartLink(self, createLink: bool):
        """
        Setter for property: (bool) CreateInterpartLink
          the CreateInterpartLink  
            
         
        """
        pass
    
    ## Getter for property: (bool) EnableFacetSelection
    ##   the EnableFacetSelection  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def EnableFacetSelection(self) -> bool:
        """
        Getter for property: (bool) EnableFacetSelection
          the EnableFacetSelection  
            
         
        """
        pass
    
    ## Setter for property: (bool) EnableFacetSelection

    ##   the EnableFacetSelection  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @EnableFacetSelection.setter
    def EnableFacetSelection(self, enableSelection: bool):
        """
        Setter for property: (bool) EnableFacetSelection
          the EnableFacetSelection  
            
         
        """
        pass
    
    ## Getter for property: (str) InterpartSelectionAsString
    ##   the InterpartSelection as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def InterpartSelectionAsString(self) -> str:
        """
        Getter for property: (str) InterpartSelectionAsString
          the InterpartSelection as string  
            
         
        """
        pass
    
    ## Setter for property: (str) InterpartSelectionAsString

    ##   the InterpartSelection as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @InterpartSelectionAsString.setter
    def InterpartSelectionAsString(self, enumString: str):
        """
        Setter for property: (str) InterpartSelectionAsString
          the InterpartSelection as string  
            
         
        """
        pass
    
    ## Getter for property: (str) LabelString
    ##   the LabelString  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
          the LabelString  
            
         
        """
        pass
    
    ## Setter for property: (str) LabelString

    ##   the LabelString  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
          the LabelString  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Point
    ##   the Point  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def Point(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Point
          the Point  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Point

    ##   the Point  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Point.setter
    def Point(self, point: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Point
          the Point  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.View NXOpen.View@endlink) SelectionView
    ##   the SelectionView  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.View
    @property
    def SelectionView(self) -> NXOpen.View:
        """
        Getter for property: (@link NXOpen.View NXOpen.View@endlink) SelectionView
          the SelectionView  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowShortcuts
    ##   the ShowShortcuts  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowShortcuts(self) -> bool:
        """
        Getter for property: (bool) ShowShortcuts
          the ShowShortcuts  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowShortcuts

    ##   the ShowShortcuts  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowShortcuts.setter
    def ShowShortcuts(self, show: bool):
        """
        Setter for property: (bool) ShowShortcuts
          the ShowShortcuts  
            
         
        """
        pass
    
    ## Getter for property: (int) SnapPointTypesEnabled
    ##   the SnapPointTypesEnabled  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def SnapPointTypesEnabled(self) -> int:
        """
        Getter for property: (int) SnapPointTypesEnabled
          the SnapPointTypesEnabled  
            
         
        """
        pass
    
    ## Setter for property: (int) SnapPointTypesEnabled

    ##   the SnapPointTypesEnabled  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @SnapPointTypesEnabled.setter
    def SnapPointTypesEnabled(self, snapTypes: int):
        """
        Setter for property: (int) SnapPointTypesEnabled
          the SnapPointTypesEnabled  
            
         
        """
        pass
    
    ## Getter for property: (int) SnapPointTypesOnByDefault
    ##   the SnapPointTypesOnByDefault  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def SnapPointTypesOnByDefault(self) -> int:
        """
        Getter for property: (int) SnapPointTypesOnByDefault
          the SnapPointTypesOnByDefault  
            
         
        """
        pass
    
    ## Setter for property: (int) SnapPointTypesOnByDefault

    ##   the SnapPointTypesOnByDefault  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @SnapPointTypesOnByDefault.setter
    def SnapPointTypesOnByDefault(self, snapTypesByDefault: int):
        """
        Setter for property: (int) SnapPointTypesOnByDefault
          the SnapPointTypesOnByDefault  
            
         
        """
        pass
    
    ## Getter for property: (str) StepStatusAsString
    ##   the StepStatus as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
          the StepStatus as string  
            
         
        """
        pass
    
    ## Setter for property: (str) StepStatusAsString

    ##   the StepStatus as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
          the StepStatus as string  
            
         
        """
        pass
    
    ##  Gets the BalloonTooltipLayout members 
    ##  @return layout_strings (List[str]): Value to get from the property. .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBalloonTooltipLayoutMembers(specifyPoint: SpecifyPoint) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         @return layout_strings (List[str]): Value to get from the property. .
        """
        pass
    
    ##  Gets the InterpartSelection members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetInterpartSelectionMembers(specifyPoint: SpecifyPoint) -> List[str]:
        """
         Gets the InterpartSelection members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Gets the SelectedObjects
    ##  @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectedObjects(specifyPoint: SpecifyPoint) -> List[NXOpen.TaggedObject]:
        """
         Gets the SelectedObjects
         @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
        """
        pass
    
    ##  Gets the StepStatus members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStepStatusMembers(specifyPoint: SpecifyPoint) -> List[str]:
        """
         Gets the StepStatus members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Sets the SelectedObjects
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## Value to set for the property
    def SetSelectedObjects(specifyPoint: SpecifyPoint, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the SelectedObjects
        """
        pass
    
    ##  Tests the point specified for this block. The block must be in focus to call this API
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="point"> (@link NXOpen.Point3d NXOpen.Point3d@endlink) </param>
    def TestPointSpecified(specifyPoint: SpecifyPoint, point: NXOpen.Point3d) -> None:
        """
         Tests the point specified for this block. The block must be in focus to call this API
        """
        pass
    
    ##  Tests the selection for this block. The block must be in focus to call this API
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## Value to set for the property
    def TestSelection(specifyPoint: SpecifyPoint, objectVector: NXOpen.TaggedObject) -> None:
        """
         Tests the selection for this block. The block must be in focus to call this API
        """
        pass
    
import NXOpen
##  Represents Specify Vector block
## 
##   <br>  Created in NX8.5.0  <br> 

class SpecifyVector(UIBlock): 
    """ Represents Specify Vector block"""


    ## Getter for property: (bool) AutomaticProgression
    ##   the AutomaticProgression  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def AutomaticProgression(self) -> bool:
        """
        Getter for property: (bool) AutomaticProgression
          the AutomaticProgression  
            
         
        """
        pass
    
    ## Setter for property: (bool) AutomaticProgression

    ##   the AutomaticProgression  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @AutomaticProgression.setter
    def AutomaticProgression(self, automaticProgression: bool):
        """
        Setter for property: (bool) AutomaticProgression
          the AutomaticProgression  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipImage
    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipImage

    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipLayoutAsString
    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipLayoutAsString

    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipText
    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipText

    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Getter for property: (bool) CreateInterpartLink
    ##   the CreateInterpartLink  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def CreateInterpartLink(self) -> bool:
        """
        Getter for property: (bool) CreateInterpartLink
          the CreateInterpartLink  
            
         
        """
        pass
    
    ## Setter for property: (bool) CreateInterpartLink

    ##   the CreateInterpartLink  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @CreateInterpartLink.setter
    def CreateInterpartLink(self, createLink: bool):
        """
        Setter for property: (bool) CreateInterpartLink
          the CreateInterpartLink  
            
         
        """
        pass
    
    ## Getter for property: (bool) DoubleSide
    ##   the DoubleSide  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def DoubleSide(self) -> bool:
        """
        Getter for property: (bool) DoubleSide
          the DoubleSide  
            
         
        """
        pass
    
    ## Setter for property: (bool) DoubleSide

    ##   the DoubleSide  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @DoubleSide.setter
    def DoubleSide(self, doubleSide: bool):
        """
        Setter for property: (bool) DoubleSide
          the DoubleSide  
            
         
        """
        pass
    
    ## Getter for property: (bool) EnableFacetSelection
    ##   the EnableFacetSelection  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def EnableFacetSelection(self) -> bool:
        """
        Getter for property: (bool) EnableFacetSelection
          the EnableFacetSelection  
            
         
        """
        pass
    
    ## Setter for property: (bool) EnableFacetSelection

    ##   the EnableFacetSelection  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @EnableFacetSelection.setter
    def EnableFacetSelection(self, enableSelection: bool):
        """
        Setter for property: (bool) EnableFacetSelection
          the EnableFacetSelection  
            
         
        """
        pass
    
    ## Getter for property: (bool) EnableReverseDirection
    ##   the EnableReverseDirection  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def EnableReverseDirection(self) -> bool:
        """
        Getter for property: (bool) EnableReverseDirection
          the EnableReverseDirection  
            
         
        """
        pass
    
    ## Setter for property: (bool) EnableReverseDirection

    ##   the EnableReverseDirection  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @EnableReverseDirection.setter
    def EnableReverseDirection(self, enableReverse: bool):
        """
        Setter for property: (bool) EnableReverseDirection
          the EnableReverseDirection  
            
         
        """
        pass
    
    ## Getter for property: (str) InterpartSelectionAsString
    ##   the InterpartSelection as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def InterpartSelectionAsString(self) -> str:
        """
        Getter for property: (str) InterpartSelectionAsString
          the InterpartSelection as string  
            
         
        """
        pass
    
    ## Setter for property: (str) InterpartSelectionAsString

    ##   the InterpartSelection as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @InterpartSelectionAsString.setter
    def InterpartSelectionAsString(self, enumString: str):
        """
        Setter for property: (str) InterpartSelectionAsString
          the InterpartSelection as string  
            
         
        """
        pass
    
    ## Getter for property: (bool) Is2DMode
    ##   the Is2DMode.  
    ##    If true, vector is created in 2D space.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def Is2DMode(self) -> bool:
        """
        Getter for property: (bool) Is2DMode
          the Is2DMode.  
           If true, vector is created in 2D space.  
         
        """
        pass
    
    ## Setter for property: (bool) Is2DMode

    ##   the Is2DMode.  
    ##    If true, vector is created in 2D space.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Is2DMode.setter
    def Is2DMode(self, is2DMode: bool):
        """
        Setter for property: (bool) Is2DMode
          the Is2DMode.  
           If true, vector is created in 2D space.  
         
        """
        pass
    
    ## Getter for property: (str) LabelString
    ##   the LabelString  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
          the LabelString  
            
         
        """
        pass
    
    ## Setter for property: (str) LabelString

    ##   the LabelString  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
          the LabelString  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Point
    ##   the Point  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def Point(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Point
          the Point  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Point

    ##   the Point  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Point.setter
    def Point(self, point: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Point
          the Point  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowShortcuts
    ##   the ShowShortcuts  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowShortcuts(self) -> bool:
        """
        Getter for property: (bool) ShowShortcuts
          the ShowShortcuts  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowShortcuts

    ##   the ShowShortcuts  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowShortcuts.setter
    def ShowShortcuts(self, show: bool):
        """
        Setter for property: (bool) ShowShortcuts
          the ShowShortcuts  
            
         
        """
        pass
    
    ## Getter for property: (int) SnapPointTypesOnByDefault
    ##   the SnapPointTypesOnByDefault  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def SnapPointTypesOnByDefault(self) -> int:
        """
        Getter for property: (int) SnapPointTypesOnByDefault
          the SnapPointTypesOnByDefault  
            
         
        """
        pass
    
    ## Setter for property: (int) SnapPointTypesOnByDefault

    ##   the SnapPointTypesOnByDefault  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @SnapPointTypesOnByDefault.setter
    def SnapPointTypesOnByDefault(self, snapTypesByDefault: int):
        """
        Setter for property: (int) SnapPointTypesOnByDefault
          the SnapPointTypesOnByDefault  
            
         
        """
        pass
    
    ## Getter for property: (str) StepStatusAsString
    ##   the StepStatus as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
          the StepStatus as string  
            
         
        """
        pass
    
    ## Setter for property: (str) StepStatusAsString

    ##   the StepStatus as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
          the StepStatus as string  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) Vector
    ##   the Vector  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.Vector3d
    @property
    def Vector(self) -> NXOpen.Vector3d:
        """
        Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) Vector
          the Vector  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) Vector

    ##   the Vector  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Vector.setter
    def Vector(self, vector: NXOpen.Vector3d):
        """
        Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) Vector
          the Vector  
            
         
        """
        pass
    
    ##  Gets the BalloonTooltipLayout members 
    ##  @return layout_strings (List[str]): Value to get from the property. .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBalloonTooltipLayoutMembers(specifyVector: SpecifyVector) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         @return layout_strings (List[str]): Value to get from the property. .
        """
        pass
    
    ##  Gets the InterpartSelection members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetInterpartSelectionMembers(specifyVector: SpecifyVector) -> List[str]:
        """
         Gets the InterpartSelection members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Gets the SelectedObjects
    ##  @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectedObjects(specifyVector: SpecifyVector) -> List[NXOpen.TaggedObject]:
        """
         Gets the SelectedObjects
         @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
        """
        pass
    
    ##  Gets the StepStatus
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStepStatusMembers(specifyVector: SpecifyVector) -> List[str]:
        """
         Gets the StepStatus
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Sets the SelectedObjects
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## Value to set for the property
    def SetSelectedObjects(specifyVector: SpecifyVector, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the SelectedObjects
        """
        pass
    
    ##  Tests the point specified for this block. The block must be in focus to call this API
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="point"> (@link NXOpen.Point3d NXOpen.Point3d@endlink) </param>
    def TestPointSpecified(specifyVector: SpecifyVector, point: NXOpen.Point3d) -> None:
        """
         Tests the point specified for this block. The block must be in focus to call this API
        """
        pass
    
    ##  Tests the selection for this block. The block must be in focus to call this API
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## Value to set for the property
    def TestSelection(specifyVector: SpecifyVector, objectVector: NXOpen.TaggedObject) -> None:
        """
         Tests the selection for this block. The block must be in focus to call this API
        """
        pass
    
    ##  Tests the vector specified for this block. The block must be in focus to call this API
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="vector"> (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) </param>
    def TestVectorSpecified(specifyVector: SpecifyVector, vector: NXOpen.Vector3d) -> None:
        """
         Tests the vector specified for this block. The block must be in focus to call this API
        """
        pass
    
##  Represents a String block
## 
##   <br>  Created in NX8.5.0  <br> 

class StringBlock(UIBlock): 
    """ Represents a String block"""


    ## Getter for property: (bool) AllowInternationalTextInput
    ##   the AllowInternationalTextInput  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.0.  Not required from NX10 onwards. Internationalization is available by default.  <br> 

    ## @return bool
    @property
    def AllowInternationalTextInput(self) -> bool:
        """
        Getter for property: (bool) AllowInternationalTextInput
          the AllowInternationalTextInput  
            
         
        """
        pass
    
    ## Setter for property: (bool) AllowInternationalTextInput

    ##   the AllowInternationalTextInput  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.0.  Not required from NX10 onwards. Internationalization is available by default.  <br> 

    @AllowInternationalTextInput.setter
    def AllowInternationalTextInput(self, allow: bool):
        """
        Setter for property: (bool) AllowInternationalTextInput
          the AllowInternationalTextInput  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipLayoutAsString
    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipLayoutAsString

    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Getter for property: (str) Bitmap
    ##   the Bitmap  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Bitmap(self) -> str:
        """
        Getter for property: (str) Bitmap
          the Bitmap  
            
         
        """
        pass
    
    ## Setter for property: (str) Bitmap

    ##   the Bitmap  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Bitmap.setter
    def Bitmap(self, bitmap_string: str):
        """
        Setter for property: (str) Bitmap
          the Bitmap  
            
         
        """
        pass
    
    ## Getter for property: (bool) IsPassword
    ##   the IsPassword.  
    ##    If true, characters will not be readable. They will be displayed as *.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def IsPassword(self) -> bool:
        """
        Getter for property: (bool) IsPassword
          the IsPassword.  
           If true, characters will not be readable. They will be displayed as *.  
         
        """
        pass
    
    ## Setter for property: (bool) IsPassword

    ##   the IsPassword.  
    ##    If true, characters will not be readable. They will be displayed as *.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @IsPassword.setter
    def IsPassword(self, passwrod: bool):
        """
        Setter for property: (bool) IsPassword
          the IsPassword.  
           If true, characters will not be readable. They will be displayed as *.  
         
        """
        pass
    
    ## Getter for property: (bool) Localize
    ##   the Localize  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def Localize(self) -> bool:
        """
        Getter for property: (bool) Localize
          the Localize  
            
         
        """
        pass
    
    ## Setter for property: (bool) Localize

    ##   the Localize  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Localize.setter
    def Localize(self, localize: bool):
        """
        Setter for property: (bool) Localize
          the Localize  
            
         
        """
        pass
    
    ## Getter for property: (int) MaxTextLength
    ##   the MaxTextLength  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def MaxTextLength(self) -> int:
        """
        Getter for property: (int) MaxTextLength
          the MaxTextLength  
            
         
        """
        pass
    
    ## Setter for property: (int) MaxTextLength

    ##   the MaxTextLength  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MaxTextLength.setter
    def MaxTextLength(self, text_length: int):
        """
        Setter for property: (int) MaxTextLength
          the MaxTextLength  
            
         
        """
        pass
    
    ## Getter for property: (str) PresentationStyleAsString
    ##   the PresentationStyle as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def PresentationStyleAsString(self) -> str:
        """
        Getter for property: (str) PresentationStyleAsString
          the PresentationStyle as string  
            
         
        """
        pass
    
    ## Setter for property: (str) PresentationStyleAsString

    ##   the PresentationStyle as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @PresentationStyleAsString.setter
    def PresentationStyleAsString(self, enumString: str):
        """
        Setter for property: (str) PresentationStyleAsString
          the PresentationStyle as string  
            
         
        """
        pass
    
    ## Getter for property: (bool) ReadOnlyString
    ##   the ReadOnlyString  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ReadOnlyString(self) -> bool:
        """
        Getter for property: (bool) ReadOnlyString
          the ReadOnlyString  
            
         
        """
        pass
    
    ## Setter for property: (bool) ReadOnlyString

    ##   the ReadOnlyString  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ReadOnlyString.setter
    def ReadOnlyString(self, readonly: bool):
        """
        Setter for property: (bool) ReadOnlyString
          the ReadOnlyString  
            
         
        """
        pass
    
    ## Getter for property: (bool) RetainValue
    ##   the RetainValue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def RetainValue(self) -> bool:
        """
        Getter for property: (bool) RetainValue
          the RetainValue  
            
         
        """
        pass
    
    ## Setter for property: (bool) RetainValue

    ##   the RetainValue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @RetainValue.setter
    def RetainValue(self, retain: bool):
        """
        Setter for property: (bool) RetainValue
          the RetainValue  
            
         
        """
        pass
    
    ## Getter for property: (str) Tooltip
    ##   the Tooltip  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Tooltip(self) -> str:
        """
        Getter for property: (str) Tooltip
          the Tooltip  
            
         
        """
        pass
    
    ## Setter for property: (str) Tooltip

    ##   the Tooltip  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Tooltip.setter
    def Tooltip(self, tooltip_string: str):
        """
        Setter for property: (str) Tooltip
          the Tooltip  
            
         
        """
        pass
    
    ## Getter for property: (str) UncommittedValue
    ##   the Uncommitted Value of string block.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def UncommittedValue(self) -> str:
        """
        Getter for property: (str) UncommittedValue
          the Uncommitted Value of string block.  
            
         
        """
        pass
    
    ## Setter for property: (str) UncommittedValue

    ##   the Uncommitted Value of string block.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @UncommittedValue.setter
    def UncommittedValue(self, value_string: str):
        """
        Setter for property: (str) UncommittedValue
          the Uncommitted Value of string block.  
            
         
        """
        pass
    
    ## Getter for property: (str) Value
    ##   the Value  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Value(self) -> str:
        """
        Getter for property: (str) Value
          the Value  
            
         
        """
        pass
    
    ## Setter for property: (str) Value

    ##   the Value  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Value.setter
    def Value(self, value_string: str):
        """
        Setter for property: (str) Value
          the Value  
            
         
        """
        pass
    
    ## Getter for property: (str) WideValue
    ##   the WideValue.  
    ##    Specifies the International text. This property accepts international characters supported by NX.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.0.  Use 'Value' instead which supports Internationalization.  <br> 

    ## @return str
    @property
    def WideValue(self) -> str:
        """
        Getter for property: (str) WideValue
          the WideValue.  
           Specifies the International text. This property accepts international characters supported by NX.  
         
        """
        pass
    
    ## Setter for property: (str) WideValue

    ##   the WideValue.  
    ##    Specifies the International text. This property accepts international characters supported by NX.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.0.  Use 'Value' instead which supports Internationalization.  <br> 

    @WideValue.setter
    def WideValue(self, wide_value_string: str):
        """
        Setter for property: (str) WideValue
          the WideValue.  
           Specifies the International text. This property accepts international characters supported by NX.  
         
        """
        pass
    
    ## Getter for property: (str) WidthAsString
    ##   the Width as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def WidthAsString(self) -> str:
        """
        Getter for property: (str) WidthAsString
          the Width as string  
            
         
        """
        pass
    
    ## Setter for property: (str) WidthAsString

    ##   the Width as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @WidthAsString.setter
    def WidthAsString(self, enumString: str):
        """
        Setter for property: (str) WidthAsString
          the Width as string  
            
         
        """
        pass
    
    ##  Gets the BalloonTooltipImages
    ##  @return image_strings (List[str]): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBalloonTooltipImages(string_block: StringBlock) -> List[str]:
        """
         Gets the BalloonTooltipImages
         @return image_strings (List[str]): .
        """
        pass
    
    ##  Gets the BalloonTooltipLayout members 
    ##  @return layout_strings (List[str]): Values to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBalloonTooltipLayoutMembers(string_block: StringBlock) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         @return layout_strings (List[str]): Values to get from the property.
        """
        pass
    
    ##  Gets the BalloonTooltipTexts
    ##  @return tooltip_text_array (List[str]): Values to get from the property. .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBalloonTooltipTexts(string_block: StringBlock) -> List[str]:
        """
         Gets the BalloonTooltipTexts
         @return tooltip_text_array (List[str]): Values to get from the property. .
        """
        pass
    
    ##  Gets the ListItems
    ##  @return item_strings (List[str]): Values to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetListItems(string_block: StringBlock) -> List[str]:
        """
         Gets the ListItems
         @return item_strings (List[str]): Values to get from the property.
        """
        pass
    
    ##  Gets the PresentationStyle members 
    ##  @return member_strings (List[str]): Values to get from the property. .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPresentationStyleMembers(string_block: StringBlock) -> List[str]:
        """
         Gets the PresentationStyle members 
         @return member_strings (List[str]): Values to get from the property. .
        """
        pass
    
    ##  Gets the Width members 
    ##  @return member_strings (List[str]): Values to get from the property. .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetWidthMembers(string_block: StringBlock) -> List[str]:
        """
         Gets the Width members 
         @return member_strings (List[str]): Values to get from the property. .
        """
        pass
    
    ##  The keystroke callback that is registered by calling @link SetKeystrokeCallback SetKeystrokeCallback@endlink . 
    ##         It will get called for each key stroke the user makes in the String Block input field. 
    ## A callback definition with the following input arguments: 
    ##  - @link StringBlock NXOpen.BlockStyler.StringBlock@endlink
    ##  - str
    ##  and no return type
    KeystrokeCallback = Callable[[StringBlock, str], None]
    
    
    ##  Sets the BalloonTooltipImages
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="image_strings"> (List[str]) </param>
    def SetBalloonTooltipImages(string_block: StringBlock, image_strings: List[str]) -> None:
        """
         Sets the BalloonTooltipImages
        """
        pass
    
    ##  Sets the BalloonTooltipTexts
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## Value to set for the property. 
    def SetBalloonTooltipTexts(string_block: StringBlock, tooltip_text_array: List[str]) -> None:
        """
         Sets the BalloonTooltipTexts
        """
        pass
    
    ##  Sets the keystroke callback for Block Styler String Block. 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    ## Callback function for keystroke event. 
    def SetKeystrokeCallback(string_block: StringBlock, cb: StringBlock.KeystrokeCallback) -> None:
        """
         Sets the keystroke callback for Block Styler String Block. 
        """
        pass
    
    ##  Sets the ListItems
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## Value to set to the property
    def SetListItems(string_block: StringBlock, item_strings: List[str]) -> None:
        """
         Sets the ListItems
        """
        pass
    
    ## Tests key stroke observer of this block. It also sets the passed value to the block.
    ##         To mock the event, set necessary value before calling this method 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    @staticmethod
    def TestKeystrokeObserver(string_block: StringBlock) -> None:
        """
        Tests key stroke observer of this block. It also sets the passed value to the block.
                To mock the event, set necessary value before calling this method 
        """
        pass
    
    ## Tests value changed event workflow mapped to this string block.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="value_string"> (str) </param>
    def TestValueChanged(string_block: StringBlock, value_string: str) -> None:
        """
        Tests value changed event workflow mapped to this string block.
        """
        pass
    
    ## Tests value changed event workflow mapped to this StringBlock block.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="value_string"> (str) </param>
    def TestWideValueChanged(string_block: StringBlock, value_string: str) -> None:
        """
        Tests value changed event workflow mapped to this StringBlock block.
        """
        pass
    
import NXOpen
##  Represents a Super Point block
## 
##   <br>  Created in NX8.5.0  <br> 

class SuperPoint(UIBlock): 
    """ Represents a Super Point block"""


    ## Getter for property: (bool) AllowConvergentObject
    ##   the AllowConvergentObject  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def AllowConvergentObject(self) -> bool:
        """
        Getter for property: (bool) AllowConvergentObject
          the AllowConvergentObject  
            
         
        """
        pass
    
    ## Setter for property: (bool) AllowConvergentObject

    ##   the AllowConvergentObject  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @AllowConvergentObject.setter
    def AllowConvergentObject(self, allowConvergentObject: bool):
        """
        Setter for property: (bool) AllowConvergentObject
          the AllowConvergentObject  
            
         
        """
        pass
    
    ## Getter for property: (bool) AllowConvergentObjectWithMixedGeometries
    ##   the AllowConvergentObjectWithMixedGeometries  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2007.0.0.  This property is no longer relevant as hybrid selection is default ON now.  <br> 

    ## @return bool
    @property
    def AllowConvergentObjectWithMixedGeometries(self) -> bool:
        """
        Getter for property: (bool) AllowConvergentObjectWithMixedGeometries
          the AllowConvergentObjectWithMixedGeometries  
            
         
        """
        pass
    
    ## Setter for property: (bool) AllowConvergentObjectWithMixedGeometries

    ##   the AllowConvergentObjectWithMixedGeometries  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2007.0.0.  This property is no longer relevant as hybrid selection is default ON now.  <br> 

    @AllowConvergentObjectWithMixedGeometries.setter
    def AllowConvergentObjectWithMixedGeometries(self, allowConvergentObjectWithMixedGeometries: bool):
        """
        Setter for property: (bool) AllowConvergentObjectWithMixedGeometries
          the AllowConvergentObjectWithMixedGeometries  
            
         
        """
        pass
    
    ## Getter for property: (bool) AutomaticProgression
    ##   the AutomaticProgression  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def AutomaticProgression(self) -> bool:
        """
        Getter for property: (bool) AutomaticProgression
          the AutomaticProgression  
            
         
        """
        pass
    
    ## Setter for property: (bool) AutomaticProgression

    ##   the AutomaticProgression  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @AutomaticProgression.setter
    def AutomaticProgression(self, automaticProgression: bool):
        """
        Setter for property: (bool) AutomaticProgression
          the AutomaticProgression  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipImage
    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipImage

    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipLayoutAsString
    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipLayoutAsString

    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipText
    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipText

    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Getter for property: (str) Bitmap
    ##   the Bitmap  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def Bitmap(self) -> str:
        """
        Getter for property: (str) Bitmap
          the Bitmap  
            
         
        """
        pass
    
    ## Setter for property: (str) Bitmap

    ##   the Bitmap  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Bitmap.setter
    def Bitmap(self, bitmap_string: str):
        """
        Setter for property: (str) Bitmap
          the Bitmap  
            
         
        """
        pass
    
    ## Getter for property: (bool) BlendVirtualCurveOverlay
    ##   the BlendVirtualCurveOverlay.  
    ##    If true, virtual curve is displayed during preselection.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def BlendVirtualCurveOverlay(self) -> bool:
        """
        Getter for property: (bool) BlendVirtualCurveOverlay
          the BlendVirtualCurveOverlay.  
           If true, virtual curve is displayed during preselection.  
         
        """
        pass
    
    ## Setter for property: (bool) BlendVirtualCurveOverlay

    ##   the BlendVirtualCurveOverlay.  
    ##    If true, virtual curve is displayed during preselection.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @BlendVirtualCurveOverlay.setter
    def BlendVirtualCurveOverlay(self, blendCurve: bool):
        """
        Setter for property: (bool) BlendVirtualCurveOverlay
          the BlendVirtualCurveOverlay.  
           If true, virtual curve is displayed during preselection.  
         
        """
        pass
    
    ## Getter for property: (bool) CreateInterpartLink
    ##   the CreateInterpartLink  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def CreateInterpartLink(self) -> bool:
        """
        Getter for property: (bool) CreateInterpartLink
          the CreateInterpartLink  
            
         
        """
        pass
    
    ## Setter for property: (bool) CreateInterpartLink

    ##   the CreateInterpartLink  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @CreateInterpartLink.setter
    def CreateInterpartLink(self, createLink: bool):
        """
        Setter for property: (bool) CreateInterpartLink
          the CreateInterpartLink  
            
         
        """
        pass
    
    ## Getter for property: (str) Cue
    ##   the Cue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def Cue(self) -> str:
        """
        Getter for property: (str) Cue
          the Cue  
            
         
        """
        pass
    
    ## Setter for property: (str) Cue

    ##   the Cue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Cue.setter
    def Cue(self, cue: str):
        """
        Setter for property: (str) Cue
          the Cue  
            
         
        """
        pass
    
    ## Getter for property: (int) CurveRules
    ##   the CurveRules  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def CurveRules(self) -> int:
        """
        Getter for property: (int) CurveRules
          the CurveRules  
            
         
        """
        pass
    
    ## Setter for property: (int) CurveRules

    ##   the CurveRules  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @CurveRules.setter
    def CurveRules(self, curveRules: int):
        """
        Setter for property: (int) CurveRules
          the CurveRules  
            
         
        """
        pass
    
    ## Getter for property: (str) DefaultCurveRulesAsString
    ##   the DefaultCurveRules as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def DefaultCurveRulesAsString(self) -> str:
        """
        Getter for property: (str) DefaultCurveRulesAsString
          the DefaultCurveRules as string  
            
         
        """
        pass
    
    ## Setter for property: (str) DefaultCurveRulesAsString

    ##   the DefaultCurveRules as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @DefaultCurveRulesAsString.setter
    def DefaultCurveRulesAsString(self, enumString: str):
        """
        Setter for property: (str) DefaultCurveRulesAsString
          the DefaultCurveRules as string  
            
         
        """
        pass
    
    ## Getter for property: (int) EntityType
    ##   the EntityType  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def EntityType(self) -> int:
        """
        Getter for property: (int) EntityType
          the EntityType  
            
         
        """
        pass
    
    ## Setter for property: (int) EntityType

    ##   the EntityType  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @EntityType.setter
    def EntityType(self, entityType: int):
        """
        Setter for property: (int) EntityType
          the EntityType  
            
         
        """
        pass
    
    ## Getter for property: (str) InterpartSelectionAsString
    ##   the InterpartSelection as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def InterpartSelectionAsString(self) -> str:
        """
        Getter for property: (str) InterpartSelectionAsString
          the InterpartSelection as string  
            
         
        """
        pass
    
    ## Setter for property: (str) InterpartSelectionAsString

    ##   the InterpartSelection as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @InterpartSelectionAsString.setter
    def InterpartSelectionAsString(self, enumString: str):
        """
        Setter for property: (str) InterpartSelectionAsString
          the InterpartSelection as string  
            
         
        """
        pass
    
    ## Getter for property: (str) LabelString
    ##   the LabelString  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
          the LabelString  
            
         
        """
        pass
    
    ## Setter for property: (str) LabelString

    ##   the LabelString  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
          the LabelString  
            
         
        """
        pass
    
    ## Getter for property: (bool) PointOverlay
    ##   the PointOverlay  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def PointOverlay(self) -> bool:
        """
        Getter for property: (bool) PointOverlay
          the PointOverlay  
            
         
        """
        pass
    
    ## Setter for property: (bool) PointOverlay

    ##   the PointOverlay  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @PointOverlay.setter
    def PointOverlay(self, overlay: bool):
        """
        Setter for property: (bool) PointOverlay
          the PointOverlay  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowFlowDirectionAndOriginCurve
    ##   the ShowFlowDirectionAndOriginCurve  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def ShowFlowDirectionAndOriginCurve(self) -> bool:
        """
        Getter for property: (bool) ShowFlowDirectionAndOriginCurve
          the ShowFlowDirectionAndOriginCurve  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowFlowDirectionAndOriginCurve

    ##   the ShowFlowDirectionAndOriginCurve  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ShowFlowDirectionAndOriginCurve.setter
    def ShowFlowDirectionAndOriginCurve(self, show: bool):
        """
        Setter for property: (bool) ShowFlowDirectionAndOriginCurve
          the ShowFlowDirectionAndOriginCurve  
            
         
        """
        pass
    
    ## Getter for property: (bool) SketchOnPath
    ##   the SketchOnPath  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def SketchOnPath(self) -> bool:
        """
        Getter for property: (bool) SketchOnPath
          the SketchOnPath  
            
         
        """
        pass
    
    ## Setter for property: (bool) SketchOnPath

    ##   the SketchOnPath  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @SketchOnPath.setter
    def SketchOnPath(self, sketchOnPath: bool):
        """
        Setter for property: (bool) SketchOnPath
          the SketchOnPath  
            
         
        """
        pass
    
    ## Getter for property: (int) SnapPointTypesEnabled
    ##   the SnapPointTypesEnabled  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def SnapPointTypesEnabled(self) -> int:
        """
        Getter for property: (int) SnapPointTypesEnabled
          the SnapPointTypesEnabled  
            
         
        """
        pass
    
    ## Setter for property: (int) SnapPointTypesEnabled

    ##   the SnapPointTypesEnabled  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @SnapPointTypesEnabled.setter
    def SnapPointTypesEnabled(self, snapPointType: int):
        """
        Setter for property: (int) SnapPointTypesEnabled
          the SnapPointTypesEnabled  
            
         
        """
        pass
    
    ## Getter for property: (int) SnapPointTypesOnByDefault
    ##   the SnapPointTypesOnByDefault  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def SnapPointTypesOnByDefault(self) -> int:
        """
        Getter for property: (int) SnapPointTypesOnByDefault
          the SnapPointTypesOnByDefault  
            
         
        """
        pass
    
    ## Setter for property: (int) SnapPointTypesOnByDefault

    ##   the SnapPointTypesOnByDefault  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @SnapPointTypesOnByDefault.setter
    def SnapPointTypesOnByDefault(self, defaultSnapPointType: int):
        """
        Setter for property: (int) SnapPointTypesOnByDefault
          the SnapPointTypesOnByDefault  
            
         
        """
        pass
    
    ## Getter for property: (str) StepStatusAsString
    ##   the StepStatus as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
          the StepStatus as string  
            
         
        """
        pass
    
    ## Setter for property: (str) StepStatusAsString

    ##   the StepStatus as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
          the StepStatus as string  
            
         
        """
        pass
    
    ## Getter for property: (str) ToolTip
    ##   the ToolTip  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def ToolTip(self) -> str:
        """
        Getter for property: (str) ToolTip
          the ToolTip  
            
         
        """
        pass
    
    ## Setter for property: (str) ToolTip

    ##   the ToolTip  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ToolTip.setter
    def ToolTip(self, toolTip: str):
        """
        Setter for property: (str) ToolTip
          the ToolTip  
            
         
        """
        pass
    
    ##  Gets the BalloonTooltipLayout members 
    ##  @return layout_strings (List[str]): Value to get from the property. .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBalloonTooltipLayoutMembers(superPoint: SuperPoint) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         @return layout_strings (List[str]): Value to get from the property. .
        """
        pass
    
    ##  Gets the DefaultCurveRules members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetDefaultCurveRulesMembers(superPoint: SuperPoint) -> List[str]:
        """
         Gets the DefaultCurveRules members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Gets the InterpartSelection members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetInterpartSelectionMembers(superPoint: SuperPoint) -> List[str]:
        """
         Gets the InterpartSelection members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Gets the SelectedObjects
    ##  @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectedObjects(superPoint: SuperPoint) -> List[NXOpen.TaggedObject]:
        """
         Gets the SelectedObjects
         @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
        """
        pass
    
    ##  Gets the StepStatus members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStepStatusMembers(superPoint: SuperPoint) -> List[str]:
        """
         Gets the StepStatus members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Sets the SelectedObjects
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ## Value to set for the property
    def SetSelectedObjects(superPoint: SuperPoint, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the SelectedObjects
        """
        pass
    
    ##  Tests the selection for this block. The block must be in focus to call this API
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## Value to set for the property
    def TestSelection(superPoint: SuperPoint, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Tests the selection for this block. The block must be in focus to call this API
        """
        pass
    
import NXOpen
##  Represents a Super Section block
## 
##   <br>  Created in NX8.5.0  <br> 

class SuperSection(UIBlock): 
    """ Represents a Super Section block"""


    ## Getter for property: (bool) AllowConvergentObject
    ##   the AllowConvergentObject  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def AllowConvergentObject(self) -> bool:
        """
        Getter for property: (bool) AllowConvergentObject
          the AllowConvergentObject  
            
         
        """
        pass
    
    ## Setter for property: (bool) AllowConvergentObject

    ##   the AllowConvergentObject  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @AllowConvergentObject.setter
    def AllowConvergentObject(self, allowConvergentObject: bool):
        """
        Setter for property: (bool) AllowConvergentObject
          the AllowConvergentObject  
            
         
        """
        pass
    
    ## Getter for property: (bool) AllowConvergentObjectWithMixedGeometries
    ##   the AllowConvergentObjectWithMixedGeometries  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2007.0.0.  This property is no longer relevant as hybrid selection is default ON now.  <br> 

    ## @return bool
    @property
    def AllowConvergentObjectWithMixedGeometries(self) -> bool:
        """
        Getter for property: (bool) AllowConvergentObjectWithMixedGeometries
          the AllowConvergentObjectWithMixedGeometries  
            
         
        """
        pass
    
    ## Setter for property: (bool) AllowConvergentObjectWithMixedGeometries

    ##   the AllowConvergentObjectWithMixedGeometries  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2007.0.0.  This property is no longer relevant as hybrid selection is default ON now.  <br> 

    @AllowConvergentObjectWithMixedGeometries.setter
    def AllowConvergentObjectWithMixedGeometries(self, allowConvergentObjectWithMixedGeometries: bool):
        """
        Setter for property: (bool) AllowConvergentObjectWithMixedGeometries
          the AllowConvergentObjectWithMixedGeometries  
            
         
        """
        pass
    
    ## Getter for property: (bool) AllowInferredCurveSelection
    ##   the AllowInferredCurveSelection  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def AllowInferredCurveSelection(self) -> bool:
        """
        Getter for property: (bool) AllowInferredCurveSelection
          the AllowInferredCurveSelection  
            
         
        """
        pass
    
    ## Setter for property: (bool) AllowInferredCurveSelection

    ##   the AllowInferredCurveSelection  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @AllowInferredCurveSelection.setter
    def AllowInferredCurveSelection(self, allow: bool):
        """
        Setter for property: (bool) AllowInferredCurveSelection
          the AllowInferredCurveSelection  
            
         
        """
        pass
    
    ## Getter for property: (bool) AllowStopAtIntersectionFollowFillet
    ##   the AllowStopAtIntersectionFollowFillet  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def AllowStopAtIntersectionFollowFillet(self) -> bool:
        """
        Getter for property: (bool) AllowStopAtIntersectionFollowFillet
          the AllowStopAtIntersectionFollowFillet  
            
         
        """
        pass
    
    ## Setter for property: (bool) AllowStopAtIntersectionFollowFillet

    ##   the AllowStopAtIntersectionFollowFillet  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @AllowStopAtIntersectionFollowFillet.setter
    def AllowStopAtIntersectionFollowFillet(self, allow: bool):
        """
        Setter for property: (bool) AllowStopAtIntersectionFollowFillet
          the AllowStopAtIntersectionFollowFillet  
            
         
        """
        pass
    
    ## Getter for property: (float) AngularTolerance
    ##   the AngularTolerance  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return float
    @property
    def AngularTolerance(self) -> float:
        """
        Getter for property: (float) AngularTolerance
          the AngularTolerance  
            
         
        """
        pass
    
    ## Setter for property: (float) AngularTolerance

    ##   the AngularTolerance  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @AngularTolerance.setter
    def AngularTolerance(self, tolerance: float):
        """
        Setter for property: (float) AngularTolerance
          the AngularTolerance  
            
         
        """
        pass
    
    ## Getter for property: (bool) AutomaticProgression
    ##   the AutomaticProgression  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def AutomaticProgression(self) -> bool:
        """
        Getter for property: (bool) AutomaticProgression
          the AutomaticProgression  
            
         
        """
        pass
    
    ## Setter for property: (bool) AutomaticProgression

    ##   the AutomaticProgression  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @AutomaticProgression.setter
    def AutomaticProgression(self, automaticProgression: bool):
        """
        Setter for property: (bool) AutomaticProgression
          the AutomaticProgression  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipImage
    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipImage

    ##   the BalloonTooltipImage  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipImage.setter
    def BalloonTooltipImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipImage
          the BalloonTooltipImage  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipLayoutAsString
    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipLayoutAsString

    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipText
    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipText

    ##   the BalloonTooltipText  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipText.setter
    def BalloonTooltipText(self, balloon_tooltip_text: str):
        """
        Setter for property: (str) BalloonTooltipText
          the BalloonTooltipText  
            
         
        """
        pass
    
    ## Getter for property: (str) Bitmap
    ##   the Bitmap  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Bitmap(self) -> str:
        """
        Getter for property: (str) Bitmap
          the Bitmap  
            
         
        """
        pass
    
    ## Setter for property: (str) Bitmap

    ##   the Bitmap  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Bitmap.setter
    def Bitmap(self, bitmap_string: str):
        """
        Setter for property: (str) Bitmap
          the Bitmap  
            
         
        """
        pass
    
    ## Getter for property: (bool) BlendVirtualCurveOverlay
    ##   the BlendVirtualCurveOverlay.  
    ##    If true, virtual curve is displayed during preselection.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def BlendVirtualCurveOverlay(self) -> bool:
        """
        Getter for property: (bool) BlendVirtualCurveOverlay
          the BlendVirtualCurveOverlay.  
           If true, virtual curve is displayed during preselection.  
         
        """
        pass
    
    ## Setter for property: (bool) BlendVirtualCurveOverlay

    ##   the BlendVirtualCurveOverlay.  
    ##    If true, virtual curve is displayed during preselection.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BlendVirtualCurveOverlay.setter
    def BlendVirtualCurveOverlay(self, blendCurve: bool):
        """
        Setter for property: (bool) BlendVirtualCurveOverlay
          the BlendVirtualCurveOverlay.  
           If true, virtual curve is displayed during preselection.  
         
        """
        pass
    
    ## Getter for property: (bool) ChainWithinFeature
    ##   the ChainWithinFeature  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ChainWithinFeature(self) -> bool:
        """
        Getter for property: (bool) ChainWithinFeature
          the ChainWithinFeature  
            
         
        """
        pass
    
    ## Setter for property: (bool) ChainWithinFeature

    ##   the ChainWithinFeature  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ChainWithinFeature.setter
    def ChainWithinFeature(self, chainWithinFeature: bool):
        """
        Setter for property: (bool) ChainWithinFeature
          the ChainWithinFeature  
            
         
        """
        pass
    
    ## Getter for property: (bool) CreateInterpartLink
    ##   the CreateInterpartLink  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def CreateInterpartLink(self) -> bool:
        """
        Getter for property: (bool) CreateInterpartLink
          the CreateInterpartLink  
            
         
        """
        pass
    
    ## Setter for property: (bool) CreateInterpartLink

    ##   the CreateInterpartLink  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @CreateInterpartLink.setter
    def CreateInterpartLink(self, createLink: bool):
        """
        Setter for property: (bool) CreateInterpartLink
          the CreateInterpartLink  
            
         
        """
        pass
    
    ## Getter for property: (str) Cue
    ##   the Cue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Cue(self) -> str:
        """
        Getter for property: (str) Cue
          the Cue  
            
         
        """
        pass
    
    ## Setter for property: (str) Cue

    ##   the Cue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Cue.setter
    def Cue(self, cue: str):
        """
        Setter for property: (str) Cue
          the Cue  
            
         
        """
        pass
    
    ## Getter for property: (int) CurveRules
    ##   the CurveRules  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def CurveRules(self) -> int:
        """
        Getter for property: (int) CurveRules
          the CurveRules  
            
         
        """
        pass
    
    ## Setter for property: (int) CurveRules

    ##   the CurveRules  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @CurveRules.setter
    def CurveRules(self, curveRules: int):
        """
        Setter for property: (int) CurveRules
          the CurveRules  
            
         
        """
        pass
    
    ## Getter for property: (str) DefaultCurveRulesAsString
    ##   the DefaultCurveRules as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def DefaultCurveRulesAsString(self) -> str:
        """
        Getter for property: (str) DefaultCurveRulesAsString
          the DefaultCurveRules as string  
            
         
        """
        pass
    
    ## Setter for property: (str) DefaultCurveRulesAsString

    ##   the DefaultCurveRules as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @DefaultCurveRulesAsString.setter
    def DefaultCurveRulesAsString(self, enumString: str):
        """
        Setter for property: (str) DefaultCurveRulesAsString
          the DefaultCurveRules as string  
            
         
        """
        pass
    
    ## Getter for property: (int) EntityType
    ##   the EntityType  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def EntityType(self) -> int:
        """
        Getter for property: (int) EntityType
          the EntityType  
            
         
        """
        pass
    
    ## Setter for property: (int) EntityType

    ##   the EntityType  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @EntityType.setter
    def EntityType(self, entityType: int):
        """
        Setter for property: (int) EntityType
          the EntityType  
            
         
        """
        pass
    
    ## Getter for property: (bool) FollowFillet
    ##   the FollowFillet  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def FollowFillet(self) -> bool:
        """
        Getter for property: (bool) FollowFillet
          the FollowFillet  
            
         
        """
        pass
    
    ## Setter for property: (bool) FollowFillet

    ##   the FollowFillet  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @FollowFillet.setter
    def FollowFillet(self, followFillet: bool):
        """
        Setter for property: (bool) FollowFillet
          the FollowFillet  
            
         
        """
        pass
    
    ## Getter for property: (bool) InferredCurveSelection
    ##   the InferredCurveSelection  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def InferredCurveSelection(self) -> bool:
        """
        Getter for property: (bool) InferredCurveSelection
          the InferredCurveSelection  
            
         
        """
        pass
    
    ## Setter for property: (bool) InferredCurveSelection

    ##   the InferredCurveSelection  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @InferredCurveSelection.setter
    def InferredCurveSelection(self, selectInferredCurve: bool):
        """
        Setter for property: (bool) InferredCurveSelection
          the InferredCurveSelection  
            
         
        """
        pass
    
    ## Getter for property: (str) InterpartSelectionAsString
    ##   the InterpartSelection as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def InterpartSelectionAsString(self) -> str:
        """
        Getter for property: (str) InterpartSelectionAsString
          the InterpartSelection as string  
            
         
        """
        pass
    
    ## Setter for property: (str) InterpartSelectionAsString

    ##   the InterpartSelection as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @InterpartSelectionAsString.setter
    def InterpartSelectionAsString(self, enumString: str):
        """
        Setter for property: (str) InterpartSelectionAsString
          the InterpartSelection as string  
            
         
        """
        pass
    
    ## Getter for property: (str) LabelString
    ##   the LabelString  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def LabelString(self) -> str:
        """
        Getter for property: (str) LabelString
          the LabelString  
            
         
        """
        pass
    
    ## Setter for property: (str) LabelString

    ##   the LabelString  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @LabelString.setter
    def LabelString(self, labelString: str):
        """
        Setter for property: (str) LabelString
          the LabelString  
            
         
        """
        pass
    
    ## Getter for property: (bool) PointOverlay
    ##   the PointOverlay  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def PointOverlay(self) -> bool:
        """
        Getter for property: (bool) PointOverlay
          the PointOverlay  
            
         
        """
        pass
    
    ## Setter for property: (bool) PointOverlay

    ##   the PointOverlay  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @PointOverlay.setter
    def PointOverlay(self, overlay: bool):
        """
        Setter for property: (bool) PointOverlay
          the PointOverlay  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowFlowDirectionAndOriginCurve
    ##   the ShowFlowDirectionAndOriginCurve  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowFlowDirectionAndOriginCurve(self) -> bool:
        """
        Getter for property: (bool) ShowFlowDirectionAndOriginCurve
          the ShowFlowDirectionAndOriginCurve  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowFlowDirectionAndOriginCurve

    ##   the ShowFlowDirectionAndOriginCurve  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowFlowDirectionAndOriginCurve.setter
    def ShowFlowDirectionAndOriginCurve(self, show: bool):
        """
        Setter for property: (bool) ShowFlowDirectionAndOriginCurve
          the ShowFlowDirectionAndOriginCurve  
            
         
        """
        pass
    
    ## Getter for property: (bool) SketchOnPath
    ##   the SketchOnPath  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def SketchOnPath(self) -> bool:
        """
        Getter for property: (bool) SketchOnPath
          the SketchOnPath  
            
         
        """
        pass
    
    ## Setter for property: (bool) SketchOnPath

    ##   the SketchOnPath  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @SketchOnPath.setter
    def SketchOnPath(self, sketchOnPath: bool):
        """
        Setter for property: (bool) SketchOnPath
          the SketchOnPath  
            
         
        """
        pass
    
    ## Getter for property: (str) SmartUpdateOptionAsString
    ##   the update option for points created by the point overlay.  
    ##   
    ##          <br> 
    ##         Acceptable values are:
    ##         <ul>
    ##         <li> <b>Within Modeling</b> The smart object updates within Modeling in time stamp order. For example, if the smart object is referenced by Feature(i), the smart object will update after Feature (i-1) and right before Feature(i).</li>
    ##         <li> <b>After Modeling</b> The smart object updates after Modeling. Use for Drafting dimensions and other objects outside Modeling.</li>
    ##         <li> <b>After Parent Body</b> The smart object will always update after the last feature on the parent body.</li>
    ##         <li> <b>Mixed</b> The smart object will update after the last feature on the parent body when the parent body is in a different part; updates within Modeling in time-stamp order for parents in the same part.</li>
    ##         </ul>
    ##          <br> 
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.1  <br> 

    ## @return str
    @property
    def SmartUpdateOptionAsString(self) -> str:
        """
        Getter for property: (str) SmartUpdateOptionAsString
          the update option for points created by the point overlay.  
          
                 <br> 
                Acceptable values are:
                <ul>
                <li> <b>Within Modeling</b> The smart object updates within Modeling in time stamp order. For example, if the smart object is referenced by Feature(i), the smart object will update after Feature (i-1) and right before Feature(i).</li>
                <li> <b>After Modeling</b> The smart object updates after Modeling. Use for Drafting dimensions and other objects outside Modeling.</li>
                <li> <b>After Parent Body</b> The smart object will always update after the last feature on the parent body.</li>
                <li> <b>Mixed</b> The smart object will update after the last feature on the parent body when the parent body is in a different part; updates within Modeling in time-stamp order for parents in the same part.</li>
                </ul>
                 <br> 
                  
         
        """
        pass
    
    ## Setter for property: (str) SmartUpdateOptionAsString

    ##   the update option for points created by the point overlay.  
    ##   
    ##          <br> 
    ##         Acceptable values are:
    ##         <ul>
    ##         <li> <b>Within Modeling</b> The smart object updates within Modeling in time stamp order. For example, if the smart object is referenced by Feature(i), the smart object will update after Feature (i-1) and right before Feature(i).</li>
    ##         <li> <b>After Modeling</b> The smart object updates after Modeling. Use for Drafting dimensions and other objects outside Modeling.</li>
    ##         <li> <b>After Parent Body</b> The smart object will always update after the last feature on the parent body.</li>
    ##         <li> <b>Mixed</b> The smart object will update after the last feature on the parent body when the parent body is in a different part; updates within Modeling in time-stamp order for parents in the same part.</li>
    ##         </ul>
    ##          <br> 
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.1  <br> 

    @SmartUpdateOptionAsString.setter
    def SmartUpdateOptionAsString(self, enumString: str):
        """
        Setter for property: (str) SmartUpdateOptionAsString
          the update option for points created by the point overlay.  
          
                 <br> 
                Acceptable values are:
                <ul>
                <li> <b>Within Modeling</b> The smart object updates within Modeling in time stamp order. For example, if the smart object is referenced by Feature(i), the smart object will update after Feature (i-1) and right before Feature(i).</li>
                <li> <b>After Modeling</b> The smart object updates after Modeling. Use for Drafting dimensions and other objects outside Modeling.</li>
                <li> <b>After Parent Body</b> The smart object will always update after the last feature on the parent body.</li>
                <li> <b>Mixed</b> The smart object will update after the last feature on the parent body when the parent body is in a different part; updates within Modeling in time-stamp order for parents in the same part.</li>
                </ul>
                 <br> 
                  
         
        """
        pass
    
    ## Getter for property: (int) SnapPointTypesEnabled
    ##   the SnapPointTypesEnabled  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def SnapPointTypesEnabled(self) -> int:
        """
        Getter for property: (int) SnapPointTypesEnabled
          the SnapPointTypesEnabled  
            
         
        """
        pass
    
    ## Setter for property: (int) SnapPointTypesEnabled

    ##   the SnapPointTypesEnabled  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @SnapPointTypesEnabled.setter
    def SnapPointTypesEnabled(self, snapPointType: int):
        """
        Setter for property: (int) SnapPointTypesEnabled
          the SnapPointTypesEnabled  
            
         
        """
        pass
    
    ## Getter for property: (int) SnapPointTypesOnByDefault
    ##   the SnapPointTypesOnByDefault  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def SnapPointTypesOnByDefault(self) -> int:
        """
        Getter for property: (int) SnapPointTypesOnByDefault
          the SnapPointTypesOnByDefault  
            
         
        """
        pass
    
    ## Setter for property: (int) SnapPointTypesOnByDefault

    ##   the SnapPointTypesOnByDefault  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @SnapPointTypesOnByDefault.setter
    def SnapPointTypesOnByDefault(self, defaultSnapPointType: int):
        """
        Setter for property: (int) SnapPointTypesOnByDefault
          the SnapPointTypesOnByDefault  
            
         
        """
        pass
    
    ## Getter for property: (str) StepStatusAsString
    ##   the StepStatus as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def StepStatusAsString(self) -> str:
        """
        Getter for property: (str) StepStatusAsString
          the StepStatus as string  
            
         
        """
        pass
    
    ## Setter for property: (str) StepStatusAsString

    ##   the StepStatus as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @StepStatusAsString.setter
    def StepStatusAsString(self, enumString: str):
        """
        Setter for property: (str) StepStatusAsString
          the StepStatus as string  
            
         
        """
        pass
    
    ## Getter for property: (bool) StopAtIntersection
    ##   the StopAtIntersection  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def StopAtIntersection(self) -> bool:
        """
        Getter for property: (bool) StopAtIntersection
          the StopAtIntersection  
            
         
        """
        pass
    
    ## Setter for property: (bool) StopAtIntersection

    ##   the StopAtIntersection  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @StopAtIntersection.setter
    def StopAtIntersection(self, stop: bool):
        """
        Setter for property: (bool) StopAtIntersection
          the StopAtIntersection  
            
         
        """
        pass
    
    ## Getter for property: (str) ToolTip
    ##   the ToolTip  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def ToolTip(self) -> str:
        """
        Getter for property: (str) ToolTip
          the ToolTip  
            
         
        """
        pass
    
    ## Setter for property: (str) ToolTip

    ##   the ToolTip  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ToolTip.setter
    def ToolTip(self, toolTip: str):
        """
        Setter for property: (str) ToolTip
          the ToolTip  
            
         
        """
        pass
    
    ##  Gets the BalloonTooltipLayout members 
    ##  @return layout_strings (List[str]): Value to get from the property. .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBalloonTooltipLayoutMembers(superSection: SuperSection) -> List[str]:
        """
         Gets the BalloonTooltipLayout members 
         @return layout_strings (List[str]): Value to get from the property. .
        """
        pass
    
    ##  Gets the DefaultCurveRules members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetDefaultCurveRulesMembers(superSection: SuperSection) -> List[str]:
        """
         Gets the DefaultCurveRules members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Gets the InterpartSelection members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetInterpartSelectionMembers(superSection: SuperSection) -> List[str]:
        """
         Gets the InterpartSelection members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Gets the SelectedObjects
    ##  @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectedObjects(superSection: SuperSection) -> List[NXOpen.TaggedObject]:
        """
         Gets the SelectedObjects
         @return objectVector (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): Value to get from the property.
        """
        pass
    
    ##  Gets the StepStatus members
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStepStatusMembers(superSection: SuperSection) -> List[str]:
        """
         Gets the StepStatus members
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Sets the SelectedObjects
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## Value to set for the property
    def SetSelectedObjects(superSection: SuperSection, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the SelectedObjects
        """
        pass
    
    ##  Tests the selection for this block. The block must be in focus to call this API
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## Value to set for the property
    def TestSelection(superSection: SuperSection, objectVector: List[NXOpen.TaggedObject]) -> None:
        """
         Tests the selection for this block. The block must be in focus to call this API
        """
        pass
    
##  Represents a Tab Control layout
## 
##   <br>  Created in NX8.5.0  <br> 

class TabControl(UIBlock): 
    """ Represents a Tab Control layout"""


    ## Getter for property: (int) ActivePage
    ##   the ActivePage  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def ActivePage(self) -> int:
        """
        Getter for property: (int) ActivePage
          the ActivePage  
            
         
        """
        pass
    
    ## Setter for property: (int) ActivePage

    ##   the ActivePage  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ActivePage.setter
    def ActivePage(self, pageIndex: int):
        """
        Setter for property: (int) ActivePage
          the ActivePage  
            
         
        """
        pass
    
    ## Getter for property: (bool) HighQualityBitmap
    ##   the HighQualityBitmap  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def HighQualityBitmap(self) -> bool:
        """
        Getter for property: (bool) HighQualityBitmap
          the HighQualityBitmap  
            
         
        """
        pass
    
    ## Setter for property: (bool) HighQualityBitmap

    ##   the HighQualityBitmap  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @HighQualityBitmap.setter
    def HighQualityBitmap(self, highQuality: bool):
        """
        Setter for property: (bool) HighQualityBitmap
          the HighQualityBitmap  
            
         
        """
        pass
    
    ## Getter for property: (bool) Localize
    ##   the Localize  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def Localize(self) -> bool:
        """
        Getter for property: (bool) Localize
          the Localize  
            
         
        """
        pass
    
    ## Setter for property: (bool) Localize

    ##   the Localize  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Localize.setter
    def Localize(self, localize: bool):
        """
        Setter for property: (bool) Localize
          the Localize  
            
         
        """
        pass
    
    ## Getter for property: (@link PropertyList NXOpen.BlockStyler.PropertyList@endlink) Members
    ##   the Members  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return PropertyList
    @property
    def Members(self) -> PropertyList:
        """
        Getter for property: (@link PropertyList NXOpen.BlockStyler.PropertyList@endlink) Members
          the Members  
            
         
        """
        pass
    
    ## Getter for property: (bool) RetainValue
    ##   the RetainValue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def RetainValue(self) -> bool:
        """
        Getter for property: (bool) RetainValue
          the RetainValue  
            
         
        """
        pass
    
    ## Setter for property: (bool) RetainValue

    ##   the RetainValue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @RetainValue.setter
    def RetainValue(self, retain: bool):
        """
        Setter for property: (bool) RetainValue
          the RetainValue  
            
         
        """
        pass
    
    ## Getter for property: (int) TabsPerRow
    ##   the TabsPerRow  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def TabsPerRow(self) -> int:
        """
        Getter for property: (int) TabsPerRow
          the TabsPerRow  
            
         
        """
        pass
    
    ## Setter for property: (int) TabsPerRow

    ##   the TabsPerRow  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @TabsPerRow.setter
    def TabsPerRow(self, numTabs: int):
        """
        Setter for property: (int) TabsPerRow
          the TabsPerRow  
            
         
        """
        pass
    
    ##  Gets the HiddenTabPages. This method returns an integer array of the HiddenTabPages.
    ##         If the number of Tab Pages defined is 5 for a Tab Control, they will be indexed 0 to 4. If the first
    ##         and third Tab Pages are hidden, the result returned will be [ 0, -1, 2, -1, -1 ]. Any negative integer
    ##         value will show the Tab Page, using -1 simply to demonstrate.
    ##  @return hiddenTabs (List[int]): .
    ## 
    ##   <br>  Created in NX10.0.1  <br> 

    ## License requirements: None.
    @staticmethod
    def GetHiddenTabPages(tabControl: TabControl) -> List[int]:
        """
         Gets the HiddenTabPages. This method returns an integer array of the HiddenTabPages.
                If the number of Tab Pages defined is 5 for a Tab Control, they will be indexed 0 to 4. If the first
                and third Tab Pages are hidden, the result returned will be [ 0, -1, 2, -1, -1 ]. Any negative integer
                value will show the Tab Page, using -1 simply to demonstrate.
         @return hiddenTabs (List[int]): .
        """
        pass
    
    ##  Sets the HiddenTabPages entered. If the number of Tab Pages defined is 5 for a Tab Control,
    ##         they will be indexed 0 to 4. Entering an array of [ 0, -1, 2, -1, -1 ] will result in the first and third
    ##         Tab Pages being hidden. Any negative integer value will show the Tab Page, using -1 simply to demonstrate.
    ## 
    ##   <br>  Created in NX10.0.1  <br> 

    ## License requirements: None.
    ## Array of Tab Pages defined. To hide a Tab Page, value entered has to map directly to the index being set.
    def SetHiddenTabPages(tabControl: TabControl, hiddenTabs: List[int]) -> None:
        """
         Sets the HiddenTabPages entered. If the number of Tab Pages defined is 5 for a Tab Control,
                they will be indexed 0 to 4. Entering an array of [ 0, -1, 2, -1, -1 ] will result in the first and third
                Tab Pages being hidden. Any negative integer value will show the Tab Page, using -1 simply to demonstrate.
        """
        pass
    
    ## Tests active tab changed.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="pageIndex"> (int) </param>
    def TestActivePageChanged(tabControl: TabControl, pageIndex: int) -> None:
        """
        Tests active tab changed.
        """
        pass
    
##  Represents a Table layout
## 
##   <br>  Created in NX8.5.0  <br> 

class Table(UIBlock): 
    """ Represents a Table layout"""


    ## Getter for property: (bool) HasColumnLabels
    ##   the HasColumnLabels  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def HasColumnLabels(self) -> bool:
        """
        Getter for property: (bool) HasColumnLabels
          the HasColumnLabels  
            
         
        """
        pass
    
    ## Setter for property: (bool) HasColumnLabels

    ##   the HasColumnLabels  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @HasColumnLabels.setter
    def HasColumnLabels(self, hasLables: bool):
        """
        Setter for property: (bool) HasColumnLabels
          the HasColumnLabels  
            
         
        """
        pass
    
    ## Getter for property: (bool) HighQualityBitmap
    ##   the HighQualityBitmap  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  The HighQualityBitmap property is deprecated.  <br> 

    ## @return bool
    @property
    def HighQualityBitmap(self) -> bool:
        """
        Getter for property: (bool) HighQualityBitmap
          the HighQualityBitmap  
            
         
        """
        pass
    
    ## Setter for property: (bool) HighQualityBitmap

    ##   the HighQualityBitmap  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  The HighQualityBitmap property is deprecated.  <br> 

    @HighQualityBitmap.setter
    def HighQualityBitmap(self, highQuality: bool):
        """
        Setter for property: (bool) HighQualityBitmap
          the HighQualityBitmap  
            
         
        """
        pass
    
    ## Getter for property: (bool) Localize
    ##   the Localize  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  The Localize property is deprecated.  <br> 

    ## @return bool
    @property
    def Localize(self) -> bool:
        """
        Getter for property: (bool) Localize
          the Localize  
            
         
        """
        pass
    
    ## Setter for property: (bool) Localize

    ##   the Localize  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  The Localize property is deprecated.  <br> 

    @Localize.setter
    def Localize(self, localize: bool):
        """
        Setter for property: (bool) Localize
          the Localize  
            
         
        """
        pass
    
    ## Getter for property: (@link PropertyList NXOpen.BlockStyler.PropertyList@endlink) Members
    ##   the Members  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return PropertyList
    @property
    def Members(self) -> PropertyList:
        """
        Getter for property: (@link PropertyList NXOpen.BlockStyler.PropertyList@endlink) Members
          the Members  
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfColumns
    ##   the NumberOfColumns  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def NumberOfColumns(self) -> int:
        """
        Getter for property: (int) NumberOfColumns
          the NumberOfColumns  
            
         
        """
        pass
    
    ## Setter for property: (int) NumberOfColumns

    ##   the NumberOfColumns  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @NumberOfColumns.setter
    def NumberOfColumns(self, num_column: int):
        """
        Setter for property: (int) NumberOfColumns
          the NumberOfColumns  
            
         
        """
        pass
    
    ## Getter for property: (bool) RetainValue
    ##   the RetainValue.  
    ##   If true, the block's value will be saved in dialog memory upon OK, Apply or Close.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  The RetainValue property is deprecated.  <br> 

    ## @return bool
    @property
    def RetainValue(self) -> bool:
        """
        Getter for property: (bool) RetainValue
          the RetainValue.  
          If true, the block's value will be saved in dialog memory upon OK, Apply or Close.  
         
        """
        pass
    
    ## Setter for property: (bool) RetainValue

    ##   the RetainValue.  
    ##   If true, the block's value will be saved in dialog memory upon OK, Apply or Close.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  The RetainValue property is deprecated.  <br> 

    @RetainValue.setter
    def RetainValue(self, retain: bool):
        """
        Setter for property: (bool) RetainValue
          the RetainValue.  
          If true, the block's value will be saved in dialog memory upon OK, Apply or Close.  
         
        """
        pass
    
import NXOpen
##  Class for registering test steps in a sequential manner. Steps registered with this class will be executed sequentially one after another as they appear in sequence.
## 
##   <br>  Created in NX2206.0.0  <br> 

class TestStepSequence(NXOpen.TransientObject): 
    """ Class for registering test steps in a sequential manner. Steps registered with this class will be executed sequentially one after another as they appear in sequence."""


    ## Dialog test step function. This notifier will be invoked to set the desired values to a block.
    ##         User must register this function to step registration in order to test a block> 
    ## A callback definition with the following input arguments: 
    ##  - @link UIBlock NXOpen.BlockStyler.UIBlock@endlink
    ##  and no return type
    TestStepFunction = Callable[[UIBlock], None]
    
    
    ## Dialog test step validation notifier. This notifier will be invoked once the test API is called and the system is ready for validation.
    ##         If the notifier is NULL the system will not try to invoke the notifier. Return false if the validation fails 
    ## A callback definition with the following input arguments: 
    ##  - @link UIBlock NXOpen.BlockStyler.UIBlock@endlink
    ##  and no return type
    TestStepValidationNotifier = Callable[[UIBlock], None]
    
    
    ## Adds a test step to a step sequence. The registered steps will be executed sequentially as they are registered.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## Step function
    def AddStep(sequence: TestStepSequence, step_fn: TestStepSequence.TestStepFunction, step_val_fn: TestStepSequence.TestStepValidationNotifier, step_identifier: str) -> None:
        """
        Adds a test step to a step sequence. The registered steps will be executed sequentially as they are registered.
        """
        pass
    
    ## Adds a test step to a step sequence without validation function. The registered steps will be executed sequentially as they are registered.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## Step function
    def AddStepWithoutValidation(sequence: TestStepSequence, step_fn: TestStepSequence.TestStepFunction, step_identifier: str) -> None:
        """
        Adds a test step to a step sequence without validation function. The registered steps will be executed sequentially as they are registered.
        """
        pass
    
    ## Disposes the object.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(sequence: TestStepSequence) -> None:
        """
        Disposes the object.
        """
        pass
    
##  Represents a Line Width block
## 
##   <br>  Created in NX9.0.0  <br> 

class TextColorFontWidth(UIBlock): 
    """ Represents a Line Width block"""


    ## Getter for property: (str) AvailableFontTypesAsString
    ##   the available font types.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def AvailableFontTypesAsString(self) -> str:
        """
        Getter for property: (str) AvailableFontTypesAsString
          the available font types.  
            
         
        """
        pass
    
    ## Setter for property: (str) AvailableFontTypesAsString

    ##   the available font types.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @AvailableFontTypesAsString.setter
    def AvailableFontTypesAsString(self, availableFontTypes: str):
        """
        Setter for property: (str) AvailableFontTypesAsString
          the available font types.  
            
         
        """
        pass
    
    ## Getter for property: (str) FontValue
    ##   the font value  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def FontValue(self) -> str:
        """
        Getter for property: (str) FontValue
          the font value  
            
         
        """
        pass
    
    ## Setter for property: (str) FontValue

    ##   the font value  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @FontValue.setter
    def FontValue(self, fontValue: str):
        """
        Setter for property: (str) FontValue
          the font value  
            
         
        """
        pass
    
    ## Getter for property: (str) LayoutAsString
    ##   the layout.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def LayoutAsString(self) -> str:
        """
        Getter for property: (str) LayoutAsString
          the layout.  
            
         
        """
        pass
    
    ## Setter for property: (str) LayoutAsString

    ##   the layout.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @LayoutAsString.setter
    def LayoutAsString(self, layoutString: str):
        """
        Setter for property: (str) LayoutAsString
          the layout.  
            
         
        """
        pass
    
    ## Getter for property: (str) StandardFontStyle
    ##   the standard font style.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def StandardFontStyle(self) -> str:
        """
        Getter for property: (str) StandardFontStyle
          the standard font style.  
            
         
        """
        pass
    
    ## Setter for property: (str) StandardFontStyle

    ##   the standard font style.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @StandardFontStyle.setter
    def StandardFontStyle(self, fontStyle: str):
        """
        Setter for property: (str) StandardFontStyle
          the standard font style.  
            
         
        """
        pass
    
    ## Getter for property: (str) WidthValueAsString
    ##   the width value.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def WidthValueAsString(self) -> str:
        """
        Getter for property: (str) WidthValueAsString
          the width value.  
            
         
        """
        pass
    
    ## Setter for property: (str) WidthValueAsString

    ##   the width value.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @WidthValueAsString.setter
    def WidthValueAsString(self, widthValueString: str):
        """
        Setter for property: (str) WidthValueAsString
          the width value.  
            
         
        """
        pass
    
    ##  Gets text color values
    ##  @return colorValueVector (List[int]): color values to get from the property.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetColorValue(textColorFontWidth: TextColorFontWidth) -> List[int]:
        """
         Gets text color values
         @return colorValueVector (List[int]): color values to get from the property.
        """
        pass
    
    ##  Returns the whether selected font is nx font or standard font.
    ##  @return isNxFont (bool): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def IsNxFont(textColorFontWidth: TextColorFontWidth) -> bool:
        """
         Returns the whether selected font is nx font or standard font.
         @return isNxFont (bool): .
        """
        pass
    
    ##  Sets text color values
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ## color values to set for the property. 
    def SetColorValue(textColorFontWidth: TextColorFontWidth, colorValueVector: List[int]) -> None:
        """
         Sets text color values
        """
        pass
    
    ## Tests color value changed event workflow mapped to this TextColorFontWidth block. Invokes the client notifiers to simulate UI like event.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## color values to set for the property. 
    def TestColorValueChanged(textColorFontWidth: TextColorFontWidth, colorValueVector: List[int]) -> None:
        """
        Tests color value changed event workflow mapped to this TextColorFontWidth block. Invokes the client notifiers to simulate UI like event.
        """
        pass
    
    ## Tests font value changed event workflow mapped to this TextColorFontWidth block. Invokes the client notifiers to simulate UI like event.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="fontValue"> (str) </param>
    def TestFontValueChanged(textColorFontWidth: TextColorFontWidth, fontValue: str) -> None:
        """
        Tests font value changed event workflow mapped to this TextColorFontWidth block. Invokes the client notifiers to simulate UI like event.
        """
        pass
    
    ## Tests width value changed event workflow mapped to this TextColorFontWidth block.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="widthValueString"> (str) </param>
    def TestWidthValueChanged(textColorFontWidth: TextColorFontWidth, widthValueString: str) -> None:
        """
        Tests width value changed event workflow mapped to this TextColorFontWidth block.
        """
        pass
    
##  Represents a Toggle block
## 
##   <br>  Created in NX8.5.0  <br> 

class Toggle(UIBlock): 
    """ Represents a Toggle block"""


    ## Getter for property: (str) BalloonTooltipLayoutAsString
    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipLayoutAsString(self) -> str:
        """
        Getter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipLayoutAsString

    ##   the BalloonTooltipLayout as string  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipLayoutAsString.setter
    def BalloonTooltipLayoutAsString(self, enumString: str):
        """
        Setter for property: (str) BalloonTooltipLayoutAsString
          the BalloonTooltipLayout as string  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipOffImage
    ##   the BalloonTooltipOffImage  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipOffImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipOffImage
          the BalloonTooltipOffImage  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipOffImage

    ##   the BalloonTooltipOffImage  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipOffImage.setter
    def BalloonTooltipOffImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipOffImage
          the BalloonTooltipOffImage  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipOffText
    ##   the BalloonTooltipOffText  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipOffText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipOffText
          the BalloonTooltipOffText  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipOffText

    ##   the BalloonTooltipOffText  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipOffText.setter
    def BalloonTooltipOffText(self, tooltip_string: str):
        """
        Setter for property: (str) BalloonTooltipOffText
          the BalloonTooltipOffText  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipOnImage
    ##   the BalloonTooltipOnImage  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipOnImage(self) -> str:
        """
        Getter for property: (str) BalloonTooltipOnImage
          the BalloonTooltipOnImage  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipOnImage

    ##   the BalloonTooltipOnImage  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipOnImage.setter
    def BalloonTooltipOnImage(self, image_string: str):
        """
        Setter for property: (str) BalloonTooltipOnImage
          the BalloonTooltipOnImage  
            
         
        """
        pass
    
    ## Getter for property: (str) BalloonTooltipOnText
    ##   the BalloonTooltipOnText  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def BalloonTooltipOnText(self) -> str:
        """
        Getter for property: (str) BalloonTooltipOnText
          the BalloonTooltipOnText  
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonTooltipOnText

    ##   the BalloonTooltipOnText  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BalloonTooltipOnText.setter
    def BalloonTooltipOnText(self, tooltip_string: str):
        """
        Setter for property: (str) BalloonTooltipOnText
          the BalloonTooltipOnText  
            
         
        """
        pass
    
    ## Getter for property: (str) Bitmap
    ##   the Bitmap  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Bitmap(self) -> str:
        """
        Getter for property: (str) Bitmap
          the Bitmap  
            
         
        """
        pass
    
    ## Setter for property: (str) Bitmap

    ##   the Bitmap  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Bitmap.setter
    def Bitmap(self, bitmap_string: str):
        """
        Setter for property: (str) Bitmap
          the Bitmap  
            
         
        """
        pass
    
    ## Getter for property: (bool) BitmapOnly
    ##   the BitmapOnly  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def BitmapOnly(self) -> bool:
        """
        Getter for property: (bool) BitmapOnly
          the BitmapOnly  
            
         
        """
        pass
    
    ## Setter for property: (bool) BitmapOnly

    ##   the BitmapOnly  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @BitmapOnly.setter
    def BitmapOnly(self, bitmap_only: bool):
        """
        Setter for property: (bool) BitmapOnly
          the BitmapOnly  
            
         
        """
        pass
    
    ## Getter for property: (bool) Localize
    ##   the Localize  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def Localize(self) -> bool:
        """
        Getter for property: (bool) Localize
          the Localize  
            
         
        """
        pass
    
    ## Setter for property: (bool) Localize

    ##   the Localize  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Localize.setter
    def Localize(self, localize: bool):
        """
        Setter for property: (bool) Localize
          the Localize  
            
         
        """
        pass
    
    ## Getter for property: (bool) RetainValue
    ##   the RetainValue  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def RetainValue(self) -> bool:
        """
        Getter for property: (bool) RetainValue
          the RetainValue  
            
         
        """
        pass
    
    ## Setter for property: (bool) RetainValue

    ##   the RetainValue  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @RetainValue.setter
    def RetainValue(self, retain: bool):
        """
        Setter for property: (bool) RetainValue
          the RetainValue  
            
         
        """
        pass
    
    ## Getter for property: (bool) Value
    ##   the Value  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def Value(self) -> bool:
        """
        Getter for property: (bool) Value
          the Value  
            
         
        """
        pass
    
    ## Setter for property: (bool) Value

    ##   the Value  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Value.setter
    def Value(self, value_property: bool):
        """
        Setter for property: (bool) Value
          the Value  
            
         
        """
        pass
    
    ##  Gets the BalloonTooltipLayout member
    ##  @return layout_strings (List[str]): Value to get from the property. .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBalloonTooltipLayoutMembers(toggle: Toggle) -> List[str]:
        """
         Gets the BalloonTooltipLayout member
         @return layout_strings (List[str]): Value to get from the property. .
        """
        pass
    
    ## Tests value changed event workflow mapped to this Toggle block.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="value_property"> (bool) </param>
    def TestValueChanged(toggle: Toggle, value_property: bool) -> None:
        """
        Tests value changed event workflow mapped to this Toggle block.
        """
        pass
    
import NXOpen
##  Represents a menu class utilized by @link BlockStyler::Tree BlockStyler::Tree@endlink .
## Refer to @link BlockStyler::Tree::CreateMenu BlockStyler::Tree::CreateMenu@endlink  to create the menu.

## 
##   <br>  Created in NX7.5.0  <br> 

class TreeListMenu(NXOpen.TransientObject): 
    """ Represents a menu class utilized by <ja_class>BlockStyler.Tree</ja_class>.
Refer to <ja_method>BlockStyler.Tree.CreateMenu</ja_method> to create the menu.
"""


    ##  Adds single menu item 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Unique identifier for the menu item being added 
    @overload
    def AddMenuItem(self, menu: TreeListMenu, menuItemID: int, menuItemText: str) -> None:
        """
         Adds single menu item 
        """
        pass
    
    ##  Adds single menu item 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Unique identifier for the menu item being added 
    @overload
    def AddMenuItem(self, menu: TreeListMenu, menuItemID: int, menuItemText: str, icon: str) -> None:
        """
         Adds single menu item 
        """
        pass
    
    ##  Adds a separator 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def AddSeparator(menu: TreeListMenu) -> None:
        """
         Adds a separator 
        """
        pass
    
    ##  Adds a separator 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link BlockStyler::TreeListMenu::AddSeparator BlockStyler::TreeListMenu::AddSeparator@endlink  instead.  <br> 

    ## License requirements: None.
    @staticmethod
    def AddSeperator(menu: TreeListMenu) -> None:
        """
         Adds a separator 
        """
        pass
    
    ##  Frees the object from memory.  After this method is called,
    ##         it is illegal to use the object.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.
        """
        pass
    
    ## Gets the checked status for given menu item 
    ##  @return checkedStatus (bool):  Status .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Menu-item ID  
    def GetItemChecked(menu: TreeListMenu, menuItemID: int) -> bool:
        """
        Gets the checked status for given menu item 
         @return checkedStatus (bool):  Status .
        """
        pass
    
    ## Gets the flag indicating whether the given menu item is default 
    ##  @return defaultStatus (bool):  Status .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Menu-item ID  
    def GetItemDefault(menu: TreeListMenu, menuItemID: int) -> bool:
        """
        Gets the flag indicating whether the given menu item is default 
         @return defaultStatus (bool):  Status .
        """
        pass
    
    ## Gets the flag indicating whether the given menu item is dialog lanching 
    ##  @return dialogLaunchingStaus (bool):  Status .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Menu-item ID  
    def GetItemDialogLaunching(menu: TreeListMenu, menuItemID: int) -> bool:
        """
        Gets the flag indicating whether the given menu item is dialog lanching 
         @return dialogLaunchingStaus (bool):  Status .
        """
        pass
    
    ## Gets the flag indicating whether the given menu item is disabled 
    ##  @return disableStatus (bool):  Status .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Menu-item ID  
    def GetItemDisable(menu: TreeListMenu, menuItemID: int) -> bool:
        """
        Gets the flag indicating whether the given menu item is disabled 
         @return disableStatus (bool):  Status .
        """
        pass
    
    ## Gets the flag indicating whether the given menu item is hidden 
    ##  @return hiddenStatus (bool):  Status .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Menu-item ID  
    def GetItemHidden(menu: TreeListMenu, menuItemID: int) -> bool:
        """
        Gets the flag indicating whether the given menu item is hidden 
         @return hiddenStatus (bool):  Status .
        """
        pass
    
    ##  Gets the icon for given menu item 
    ##  @return icon (str):  Display text .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Menu-item ID 
    def GetItemIcon(menu: TreeListMenu, menuItemID: int) -> str:
        """
         Gets the icon for given menu item 
         @return icon (str):  Display text .
        """
        pass
    
    ##  Gets the display text for given menu item 
    ##  @return text (str):  Display text .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Menu-item ID 
    def GetItemText(menu: TreeListMenu, menuItemID: int) -> str:
        """
         Gets the display text for given menu item 
         @return text (str):  Display text .
        """
        pass
    
    ## Sets the checked status for given menu item 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Menu-item ID  
    def SetItemChecked(menu: TreeListMenu, menuItemID: int, checkedStatusStatus: bool) -> None:
        """
        Sets the checked status for given menu item 
        """
        pass
    
    ## Sets the flag indicating whether the given menu item is default 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Menu-item ID  
    def SetItemDefault(menu: TreeListMenu, menuItemID: int, defaultStatus: bool) -> None:
        """
        Sets the flag indicating whether the given menu item is default 
        """
        pass
    
    ## Sets the flag indicating whether the given menu item is dialog lanching 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Menu-item ID  
    def SetItemDialogLaunching(menu: TreeListMenu, menuItemID: int, dialogLaunchingStaus: bool) -> None:
        """
        Sets the flag indicating whether the given menu item is dialog lanching 
        """
        pass
    
    ## Sets the flag indicating whether the given menu item is disabled 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Menu-item ID  
    def SetItemDisable(menu: TreeListMenu, menuItemID: int, disableStatus: bool) -> None:
        """
        Sets the flag indicating whether the given menu item is disabled 
        """
        pass
    
    ## Sets the flag indicating whether the given menu item is hidden 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Menu-item ID  
    def SetItemHidden(menu: TreeListMenu, menuItemID: int, hiddenStatus: bool) -> None:
        """
        Sets the flag indicating whether the given menu item is hidden 
        """
        pass
    
    ##  Sets the icon for given menu item 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Menu-item ID 
    def SetItemIcon(menu: TreeListMenu, menuItemID: int, icon: str) -> None:
        """
         Sets the icon for given menu item 
        """
        pass
    
    ##  Sets the display text for given menu item 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Menu-item ID 
    def SetItemText(menu: TreeListMenu, menuItemID: int, text: str) -> None:
        """
         Sets the display text for given menu item 
        """
        pass
    
    ##  Sets a submenu. 
    ##         Submenu can be created using @link BlockStyler::Tree::CreateMenu BlockStyler::Tree::CreateMenu@endlink  method
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Menu Item ID of menu item on which submenu is supposed to be set.
    def SetSubMenu(menu: TreeListMenu, menuItemID: int, sub_menu: TreeListMenu) -> None:
        """
         Sets a submenu. 
                Submenu can be created using @link BlockStyler::Tree::CreateMenu BlockStyler::Tree::CreateMenu@endlink  method
        """
        pass
    
## Represents the Tree block in block styler automation. To start utilizing the tree use
##    methods such as @link BlockStyler::Tree::InsertColumn BlockStyler::Tree::InsertColumn@endlink , @link BlockStyler::Tree::CreateNode BlockStyler::Tree::CreateNode@endlink , @link BlockStyler::Tree::InsertNode BlockStyler::Tree::InsertNode@endlink  etc.
##    It is must to insert the column on the tree before inserting any node. Node can be created but cannot be inserted without the column available on the tree. 
##    Note that some of the methods of this class such as @link BlockStyler::Tree::InsertColumn BlockStyler::Tree::InsertColumn@endlink  must be used in or after the BlockStyler.BlockDialog.DialogShown callback after 
##    which tree is fully constructed and ready for use.
## 
##   <br>  Created in NX7.5.0  <br> 

class Tree(UIBlock): 
    """Represents the Tree block in block styler automation. To start utilizing the tree use
   methods such as <ja_method>BlockStyler.Tree.InsertColumn</ja_method>, <ja_method>BlockStyler.Tree.CreateNode</ja_method>, <ja_method>BlockStyler.Tree.InsertNode</ja_method> etc.
   It is must to insert the column on the tree before inserting any node. Node can be created but cannot be inserted without the column available on the tree. 
   Note that some of the methods of this class such as <ja_method>BlockStyler.Tree.InsertColumn</ja_method> must be used in or after the BlockStyler.BlockDialog.DialogShown callback after 
   which tree is fully constructed and ready for use."""


    ## Represents the state to allow/disallow the node label edit. Use these options in callback BlockStyler.Tree.OnBeginLabelEditCallback.
    ## Use this option to allow label edit.
    class BeginLabelEditState(Enum):
        """
        Members Include: <Allow> <Disallow>
        """
        Allow: int
        Disallow: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Tree.BeginLabelEditState:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Represents the column display type. If the type is @link BlockStyler::Tree::ColumnDisplayIcon  BlockStyler::Tree::ColumnDisplayIcon @endlink 
    ##       then the provided text is interpreted as icon.
    ## Text
    class ColumnDisplay(Enum):
        """
        Members Include: <Text> <Icon>
        """
        Text: int
        Icon: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Tree.ColumnDisplay:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Represents column resize policy.
    ##  Constant width
    class ColumnResizePolicy(Enum):
        """
        Members Include: <ConstantWidth> <ResizeWithContents> <ResizeWithTree>
        """
        ConstantWidth: int
        ResizeWithContents: int
        ResizeWithTree: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Tree.ColumnResizePolicy:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Represents the column sort option.
    ## Unsorted
    class ColumnSortOption(Enum):
        """
        Members Include: <Unsorted> <Ascending> <Descending>
        """
        Unsorted: int
        Ascending: int
        Descending: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Tree.ColumnSortOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Represents the type of edit options. Use these options in edit control callback
    ## None
    class ControlType(Enum):
        """
        Members Include: <NotSet> <ComboBox> <ListBox>
        """
        NotSet: int
        ComboBox: int
        ListBox: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Tree.ControlType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Represents the options to accept or reject the changed value.
    ## Use this option to allow edit.
    class EditControlOption(Enum):
        """
        Members Include: <Accept> <Reject>
        """
        Accept: int
        Reject: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Tree.EditControlOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Represents the state to accept/reject the edited label of node. Use these options in callback BlockStyler.Tree.OnEndLabelEditCallback.
    ## Use this option to accept the edited text.
    class EndLabelEditState(Enum):
        """
        Members Include: <AcceptText> <RejectText>
        """
        AcceptText: int
        RejectText: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Tree.EndLabelEditState:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Represents the node insert option which is used while inserting the node in tree.
    ## Node is placed first in the hierarchy in which it is inserted.
    class NodeInsertOption(Enum):
        """
        Members Include: <First> <Last> <Sort> <AlwaysFirst> <AlwaysLast>
        """
        First: int
        Last: int
        Sort: int
        AlwaysFirst: int
        AlwaysLast: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Tree.NodeInsertOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) CanStretchHeight
    ##   the CanStretchHeight.  
    ##    If true, height of list box will change.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def CanStretchHeight(self) -> bool:
        """
        Getter for property: (bool) CanStretchHeight
          the CanStretchHeight.  
           If true, height of list box will change.  
         
        """
        pass
    
    ## Setter for property: (bool) CanStretchHeight

    ##   the CanStretchHeight.  
    ##    If true, height of list box will change.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @CanStretchHeight.setter
    def CanStretchHeight(self, stretchHeight: bool):
        """
        Setter for property: (bool) CanStretchHeight
          the CanStretchHeight.  
           If true, height of list box will change.  
         
        """
        pass
    
    ## Getter for property: (bool) CanStretchWidth
    ##   the CanStretchWidth.  
    ##    If true, width of TreeList block will change.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def CanStretchWidth(self) -> bool:
        """
        Getter for property: (bool) CanStretchWidth
          the CanStretchWidth.  
           If true, width of TreeList block will change.  
         
        """
        pass
    
    ## Setter for property: (bool) CanStretchWidth

    ##   the CanStretchWidth.  
    ##    If true, width of TreeList block will change.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @CanStretchWidth.setter
    def CanStretchWidth(self, stretchWidth: bool):
        """
        Setter for property: (bool) CanStretchWidth
          the CanStretchWidth.  
           If true, width of TreeList block will change.  
         
        """
        pass
    
    ## Getter for property: (@link Node NXOpen.BlockStyler.Node@endlink) FirstSelectedNode
    ##   the first selected node among the available selected nodes.  
    ##    
    ##        Returns NULL if no node is selected.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return Node
    @property
    def FirstSelectedNode(self) -> Node:
        """
        Getter for property: (@link Node NXOpen.BlockStyler.Node@endlink) FirstSelectedNode
          the first selected node among the available selected nodes.  
           
               Returns NULL if no node is selected.  
         
        """
        pass
    
    ## Getter for property: (int) Height
    ##   the Height  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def Height(self) -> int:
        """
        Getter for property: (int) Height
          the Height  
            
         
        """
        pass
    
    ## Setter for property: (int) Height

    ##   the Height  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Height.setter
    def Height(self, height: int):
        """
        Setter for property: (int) Height
          the Height  
            
         
        """
        pass
    
    ## Getter for property: (bool) Localize
    ##   the Localize  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def Localize(self) -> bool:
        """
        Getter for property: (bool) Localize
          the Localize  
            
         
        """
        pass
    
    ## Setter for property: (bool) Localize

    ##   the Localize  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Localize.setter
    def Localize(self, localize: bool):
        """
        Setter for property: (bool) Localize
          the Localize  
            
         
        """
        pass
    
    ## Getter for property: (int) MaximumHeight
    ##   the MaximumHeight  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def MaximumHeight(self) -> int:
        """
        Getter for property: (int) MaximumHeight
          the MaximumHeight  
            
         
        """
        pass
    
    ## Setter for property: (int) MaximumHeight

    ##   the MaximumHeight  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MaximumHeight.setter
    def MaximumHeight(self, maxHeight: int):
        """
        Setter for property: (int) MaximumHeight
          the MaximumHeight  
            
         
        """
        pass
    
    ## Getter for property: (int) MaximumWidth
    ##   the MaximumWidth  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return int
    @property
    def MaximumWidth(self) -> int:
        """
        Getter for property: (int) MaximumWidth
          the MaximumWidth  
            
         
        """
        pass
    
    ## Setter for property: (int) MaximumWidth

    ##   the MaximumWidth  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @MaximumWidth.setter
    def MaximumWidth(self, maxWidth: int):
        """
        Setter for property: (int) MaximumWidth
          the MaximumWidth  
            
         
        """
        pass
    
    ## Getter for property: (int) MinimumHeight
    ##   the MinimumHeight  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def MinimumHeight(self) -> int:
        """
        Getter for property: (int) MinimumHeight
          the MinimumHeight  
            
         
        """
        pass
    
    ## Setter for property: (int) MinimumHeight

    ##   the MinimumHeight  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MinimumHeight.setter
    def MinimumHeight(self, minHeight: int):
        """
        Setter for property: (int) MinimumHeight
          the MinimumHeight  
            
         
        """
        pass
    
    ## Getter for property: (int) MinimumWidth
    ##   the MinimumWidth  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return int
    @property
    def MinimumWidth(self) -> int:
        """
        Getter for property: (int) MinimumWidth
          the MinimumWidth  
            
         
        """
        pass
    
    ## Setter for property: (int) MinimumWidth

    ##   the MinimumWidth  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @MinimumWidth.setter
    def MinimumWidth(self, minWidth: int):
        """
        Setter for property: (int) MinimumWidth
          the MinimumWidth  
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfColumns
    ##   the number of column inserted in the tree.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return int
    @property
    def NumberOfColumns(self) -> int:
        """
        Getter for property: (int) NumberOfColumns
          the number of column inserted in the tree.  
            
         
        """
        pass
    
    ## Getter for property: (@link Node NXOpen.BlockStyler.Node@endlink) RootNode
    ##   the root node.  
    ##    If more than one root node is available in top hierarchy 
    ##       then the first root node is returned.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return Node
    @property
    def RootNode(self) -> Node:
        """
        Getter for property: (@link Node NXOpen.BlockStyler.Node@endlink) RootNode
          the root node.  
           If more than one root node is available in top hierarchy 
              then the first root node is returned.  
         
        """
        pass
    
    ## Getter for property: (int) ScrollFrozenColumn
    ##   the ScrollFrozenColumn.  
    ##    It specifies the number of columns to freeze while scrolling.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def ScrollFrozenColumn(self) -> int:
        """
        Getter for property: (int) ScrollFrozenColumn
          the ScrollFrozenColumn.  
           It specifies the number of columns to freeze while scrolling.  
         
        """
        pass
    
    ## Setter for property: (int) ScrollFrozenColumn

    ##   the ScrollFrozenColumn.  
    ##    It specifies the number of columns to freeze while scrolling.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ScrollFrozenColumn.setter
    def ScrollFrozenColumn(self, scrollFrozenColumn: int):
        """
        Setter for property: (int) ScrollFrozenColumn
          the ScrollFrozenColumn.  
           It specifies the number of columns to freeze while scrolling.  
         
        """
        pass
    
    ## Getter for property: (int) ScrollLineNumber
    ##   the ScrollLineNumber.  
    ##    It specifies the number of lines to scroll when the mouse wheel rotates.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def ScrollLineNumber(self) -> int:
        """
        Getter for property: (int) ScrollLineNumber
          the ScrollLineNumber.  
           It specifies the number of lines to scroll when the mouse wheel rotates.  
         
        """
        pass
    
    ## Setter for property: (int) ScrollLineNumber

    ##   the ScrollLineNumber.  
    ##    It specifies the number of lines to scroll when the mouse wheel rotates.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ScrollLineNumber.setter
    def ScrollLineNumber(self, scrollLineNumber: int):
        """
        Setter for property: (int) ScrollLineNumber
          the ScrollLineNumber.  
           It specifies the number of lines to scroll when the mouse wheel rotates.  
         
        """
        pass
    
    ## Getter for property: (str) SelectionModeAsString
    ##   the SelectionMode  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def SelectionModeAsString(self) -> str:
        """
        Getter for property: (str) SelectionModeAsString
          the SelectionMode  
            
         
        """
        pass
    
    ## Setter for property: (str) SelectionModeAsString

    ##   the SelectionMode  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @SelectionModeAsString.setter
    def SelectionModeAsString(self, enumString: str):
        """
        Setter for property: (str) SelectionModeAsString
          the SelectionMode  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowExpandCollapseMarker
    ##   the ShowExpandCollapseMarker.  
    ##    If true, displays a sign as a marker alongside first node of the tree indicating if it is expanded or collapsed.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowExpandCollapseMarker(self) -> bool:
        """
        Getter for property: (bool) ShowExpandCollapseMarker
          the ShowExpandCollapseMarker.  
           If true, displays a sign as a marker alongside first node of the tree indicating if it is expanded or collapsed.  
         
        """
        pass
    
    ## Setter for property: (bool) ShowExpandCollapseMarker

    ##   the ShowExpandCollapseMarker.  
    ##    If true, displays a sign as a marker alongside first node of the tree indicating if it is expanded or collapsed.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowExpandCollapseMarker.setter
    def ShowExpandCollapseMarker(self, show: bool):
        """
        Setter for property: (bool) ShowExpandCollapseMarker
          the ShowExpandCollapseMarker.  
           If true, displays a sign as a marker alongside first node of the tree indicating if it is expanded or collapsed.  
         
        """
        pass
    
    ## Getter for property: (bool) ShowHeader
    ##   the ShowHeader  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowHeader(self) -> bool:
        """
        Getter for property: (bool) ShowHeader
          the ShowHeader  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowHeader

    ##   the ShowHeader  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowHeader.setter
    def ShowHeader(self, show: bool):
        """
        Setter for property: (bool) ShowHeader
          the ShowHeader  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowMultipleColumns
    ##   the ShowMultipleColumns  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowMultipleColumns(self) -> bool:
        """
        Getter for property: (bool) ShowMultipleColumns
          the ShowMultipleColumns  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowMultipleColumns

    ##   the ShowMultipleColumns  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowMultipleColumns.setter
    def ShowMultipleColumns(self, show: bool):
        """
        Setter for property: (bool) ShowMultipleColumns
          the ShowMultipleColumns  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowToolTips
    ##   the ShowToolTips  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowToolTips(self) -> bool:
        """
        Getter for property: (bool) ShowToolTips
          the ShowToolTips  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowToolTips

    ##   the ShowToolTips  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowToolTips.setter
    def ShowToolTips(self, show: bool):
        """
        Setter for property: (bool) ShowToolTips
          the ShowToolTips  
            
         
        """
        pass
    
    ## Getter for property: (bool) SortRootNodes
    ##   the SortRootNodes.  
    ##    If true, sorting of root nodes is allowed.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def SortRootNodes(self) -> bool:
        """
        Getter for property: (bool) SortRootNodes
          the SortRootNodes.  
           If true, sorting of root nodes is allowed.  
         
        """
        pass
    
    ## Setter for property: (bool) SortRootNodes

    ##   the SortRootNodes.  
    ##    If true, sorting of root nodes is allowed.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @SortRootNodes.setter
    def SortRootNodes(self, sort: bool):
        """
        Setter for property: (bool) SortRootNodes
          the SortRootNodes.  
           If true, sorting of root nodes is allowed.  
         
        """
        pass
    
    ## Getter for property: (int) Width
    ##   the Width  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return int
    @property
    def Width(self) -> int:
        """
        Getter for property: (int) Width
          the Width  
            
         
        """
        pass
    
    ## Setter for property: (int) Width

    ##   the Width  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @Width.setter
    def Width(self, width: int):
        """
        Setter for property: (int) Width
          the Width  
            
         
        """
        pass
    
    ##  @brief Represents the callback which gets called when edit is attempted on any cell. Edit-control is 
    ##        made available on the cell based on control type returned by this callback.
    ##         
    ## 
    ##  
    ##        Use @link BlockStyler::Tree::SetEditOptions BlockStyler::Tree::SetEditOptions@endlink  in this callback to show the options in the 
    ##        edit-control. Further BlockStyler.Tree.OnEditOptionSelectedCallback is called when option is selected.
    ##       
    ## A callback definition with the following input arguments: 
    ##  - @link Tree NXOpen.BlockStyler.Tree@endlink
    ##  - @link Node NXOpen.BlockStyler.Node@endlink
    ##  - int
    ##  and no return type
    AskEditControlCallback = Callable[[Tree, Node, int], None]
    
    
    ##  @brief Represents the callback which gets called when column sort is attempted. The possible return values are 0, positive and
    ##         negative value, suggesting respectively that both nodes are same, first node greater than second, and first node smaller than second.
    ##         
    ## 
    ##  
    ## A callback definition with the following input arguments: 
    ##  - @link Tree NXOpen.BlockStyler.Tree@endlink
    ##  - int
    ##  - @link Node NXOpen.BlockStyler.Node@endlink
    ##  - @link Node NXOpen.BlockStyler.Node@endlink
    ##  and no return type
    ColumnSortCallback = Callable[[Tree, int, Node, Node], None]
    
    
    ## Copies the existing @link BlockStyler::Node BlockStyler::Node@endlink . The tree can copy either its own node or the node of another tree. 
    ##        The copied node can only be inserted into the tree which has copied that node. The column texts are not passed to the copied node. 
    ##     
    ##  @return copiedNode (@link Node NXOpen.BlockStyler.Node@endlink): Copied node.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Source node. Can be node of other tree.
    def CopyNode(tree: Tree, sourceNode: Node) -> Node:
        """
        Copies the existing @link BlockStyler::Node BlockStyler::Node@endlink . The tree can copy either its own node or the node of another tree. 
               The copied node can only be inserted into the tree which has copied that node. The column texts are not passed to the copied node. 
            
         @return copiedNode (@link Node NXOpen.BlockStyler.Node@endlink): Copied node.
        """
        pass
    
    ##  Creates the menu. Use @link BlockStyler::Tree::SetMenu BlockStyler::Tree::SetMenu@endlink  to set the created menu.
    ##  @return menu (@link TreeListMenu NXOpen.BlockStyler.TreeListMenu@endlink):  .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    def CreateMenu(tree: Tree) -> TreeListMenu:
        """
         Creates the menu. Use @link BlockStyler::Tree::SetMenu BlockStyler::Tree::SetMenu@endlink  to set the created menu.
         @return menu (@link TreeListMenu NXOpen.BlockStyler.TreeListMenu@endlink):  .
        """
        pass
    
    ## Creates the node but does not insert it. Use @link BlockStyler::Tree::InsertNode BlockStyler::Tree::InsertNode@endlink  to insert 
    ##         the node.
    ##  @return node (@link Node NXOpen.BlockStyler.Node@endlink): Node.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Specifies the display text of the node.
    def CreateNode(tree: Tree, displayText: str) -> Node:
        """
        Creates the node but does not insert it. Use @link BlockStyler::Tree::InsertNode BlockStyler::Tree::InsertNode@endlink  to insert 
                the node.
         @return node (@link Node NXOpen.BlockStyler.Node@endlink): Node.
        """
        pass
    
    ## Deletes the node from tree. Further usage of deleted node is illegal. The last place where node can be used is in 
    ##       BlockStyler.Tree.OnDeleteNodeCallaback callback which gets called when node is deleted.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Node to delete
    def DeleteNode(tree: Tree, node: Node) -> None:
        """
        Deletes the node from tree. Further usage of deleted node is illegal. The last place where node can be used is in 
              BlockStyler.Tree.OnDeleteNodeCallaback callback which gets called when node is deleted.
        """
        pass
    
    ## Gets the display type of the column.
    ##  @return displayType (@link Tree.ColumnDisplay NXOpen.BlockStyler.Tree.ColumnDisplay@endlink): Display type.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Unique column Id associated with the column.
    def GetColumnDisplayType(tree: Tree, columnID: int) -> Tree.ColumnDisplay:
        """
        Gets the display type of the column.
         @return displayType (@link Tree.ColumnDisplay NXOpen.BlockStyler.Tree.ColumnDisplay@endlink): Display type.
        """
        pass
    
    ## Gets the column Id for the provided column position.
    ##  @return columnID (int): Unique column Id associated with the column.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Column position.
    def GetColumnId(tree: Tree, columnPosition: int) -> int:
        """
        Gets the column Id for the provided column position.
         @return columnID (int): Unique column Id associated with the column.
        """
        pass
    
    ## Gets column position. Returns -1 if no column is associated with the provided column Id.
    ##  @return columnPosition (int): Column position.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Unique column Id associated with the column.
    def GetColumnPosition(tree: Tree, columnID: int) -> int:
        """
        Gets column position. Returns -1 if no column is associated with the provided column Id.
         @return columnPosition (int): Column position.
        """
        pass
    
    ## Gets the column resize policy.
    ##  @return resizePolicy (@link Tree.ColumnResizePolicy NXOpen.BlockStyler.Tree.ColumnResizePolicy@endlink): Resize policy.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Unique column Id associated with the column.
    def GetColumnResizePolicy(tree: Tree, columnID: int) -> Tree.ColumnResizePolicy:
        """
        Gets the column resize policy.
         @return resizePolicy (@link Tree.ColumnResizePolicy NXOpen.BlockStyler.Tree.ColumnResizePolicy@endlink): Resize policy.
        """
        pass
    
    ## Gets the column sort option.
    ##  @return sortOption (@link Tree.ColumnSortOption NXOpen.BlockStyler.Tree.ColumnSortOption@endlink): Column sort option.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Unique column Id associated with the column.
    def GetColumnSortOption(tree: Tree, columnID: int) -> Tree.ColumnSortOption:
        """
        Gets the column sort option.
         @return sortOption (@link Tree.ColumnSortOption NXOpen.BlockStyler.Tree.ColumnSortOption@endlink): Column sort option.
        """
        pass
    
    ## Gets the flag indicating whether the column is sortable.
    ##  @return isSortable (bool): Flag indicating whether the column is sortable.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Unique column Id associated with the column.
    def GetColumnSortable(tree: Tree, columnID: int) -> bool:
        """
        Gets the flag indicating whether the column is sortable.
         @return isSortable (bool): Flag indicating whether the column is sortable.
        """
        pass
    
    ## Gets the column title.
    ##  @return columnHeaderTitle (str): Column header title.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Unique column Id associated with the column.
    def GetColumnTitle(tree: Tree, columnID: int) -> str:
        """
        Gets the column title.
         @return columnHeaderTitle (str): Column header title.
        """
        pass
    
    ## Gets the flag indicating whether the column is visible.
    ##  @return isVisible (bool): Flag indicating whether the column is visible.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Unique column Id associated with the column.
    def GetColumnVisible(tree: Tree, columnID: int) -> bool:
        """
        Gets the flag indicating whether the column is visible.
         @return isVisible (bool): Flag indicating whether the column is visible.
        """
        pass
    
    ## Gets column width
    ##  @return columnWidth (int): Column width.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Unique column Id associated with the column.
    def GetColumnWidth(tree: Tree, columnID: int) -> int:
        """
        Gets column width
         @return columnWidth (int): Column width.
        """
        pass
    
    ## Gets the selected nodes.
    ##  @return nodes (@link Node List[NXOpen.BlockStyler.Node]@endlink): Selected nodes.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectedNodes(tree: Tree) -> List[Node]:
        """
        Gets the selected nodes.
         @return nodes (@link Node List[NXOpen.BlockStyler.Node]@endlink): Selected nodes.
        """
        pass
    
    ##  Gets the SelectionMode
    ##  @return members_strings (List[str]): Value to get from the property.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectionModeMembers(tree: Tree) -> List[str]:
        """
         Gets the SelectionMode
         @return members_strings (List[str]): Value to get from the property.
        """
        pass
    
    ##  Inserts a column.
    ##        
    ##        Inserts a column with following defaults: 
    ##        <ul>
    ##        <li>@link BlockStyler::Tree::ColumnSortOption BlockStyler::Tree::ColumnSortOption@endlink  as @link BlockStyler::Tree::ColumnSortOptionAscending BlockStyler::Tree::ColumnSortOptionAscending@endlink </li>
    ##        <li>Column sortable as True</li>
    ##        <li>Column visible as True</li>
    ##        <li>@link BlockStyler::Tree::ColumnDisplay BlockStyler::Tree::ColumnDisplay@endlink  as @link BlockStyler::Tree::ColumnDisplayText BlockStyler::Tree::ColumnDisplayText@endlink </li>
    ##        <li>@link BlockStyler::Tree::ColumnResizePolicy BlockStyler::Tree::ColumnResizePolicy@endlink  as @link BlockStyler::Tree::ColumnResizePolicyConstantWidth BlockStyler::Tree::ColumnResizePolicyConstantWidth@endlink </li>
    ##        </ul>
    ##        The new column is placed after the last available column. If no column is available then the inserted one becomes the first column of the tree.
    ##     
    ##  @return columnPosition (int): Absolute column position.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Unique column Id associated with the column. Any further interaction with the column is done with this column Id.
    def InsertColumn(tree: Tree, columnID: int, columnTitle: str, columnWidth: int) -> int:
        """
         Inserts a column.
               
               Inserts a column with following defaults: 
               <ul>
               <li>@link BlockStyler::Tree::ColumnSortOption BlockStyler::Tree::ColumnSortOption@endlink  as @link BlockStyler::Tree::ColumnSortOptionAscending BlockStyler::Tree::ColumnSortOptionAscending@endlink </li>
               <li>Column sortable as True</li>
               <li>Column visible as True</li>
               <li>@link BlockStyler::Tree::ColumnDisplay BlockStyler::Tree::ColumnDisplay@endlink  as @link BlockStyler::Tree::ColumnDisplayText BlockStyler::Tree::ColumnDisplayText@endlink </li>
               <li>@link BlockStyler::Tree::ColumnResizePolicy BlockStyler::Tree::ColumnResizePolicy@endlink  as @link BlockStyler::Tree::ColumnResizePolicyConstantWidth BlockStyler::Tree::ColumnResizePolicyConstantWidth@endlink </li>
               </ul>
               The new column is placed after the last available column. If no column is available then the inserted one becomes the first column of the tree.
            
         @return columnPosition (int): Absolute column position.
        """
        pass
    
    ## Inserts the node. Subsequently BlockStyler.Tree.OnInsertNodeCallback is called. 
    ##        Reinserting the node in same or different tree is not allowed.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## New Node.
    def InsertNode(tree: Tree, newNode: Node, parentNode: Node, afterNode: Node, nodeInsertOption: Tree.NodeInsertOption) -> None:
        """
        Inserts the node. Subsequently BlockStyler.Tree.OnInsertNodeCallback is called. 
               Reinserting the node in same or different tree is not allowed.
        """
        pass
    
    ## Represents the callback which gets called when node is dragged.
    ## A callback definition with the following input arguments: 
    ##  - @link Tree NXOpen.BlockStyler.Tree@endlink
    ##  - @link Node NXOpen.BlockStyler.Node@endlink
    ##  - int
    ##  and no return type
    IsDragAllowedCallback = Callable[[Tree, Node, int], None]
    
    
    ##  @brief 
    ##        Represents the callback which gets called when an attempt is made to drop the node on any target node. If multiple nodes 
    ##        are selected and dragged then this callback is invoked for each of the selected nodes. 
    ##         
    ## 
    ##  
    ##        If node is dragged using MB3 then the callback BlockStyler.Tree.OnDropMenuCallback 
    ##        is invoked which is expected to provide and show the menu. Subsequently, BlockStyler.Tree.OnDropCallback
    ##        might get invoked.
    ##       
    ## A callback definition with the following input arguments: 
    ##  - @link Tree NXOpen.BlockStyler.Tree@endlink
    ##  - @link Node NXOpen.BlockStyler.Node@endlink
    ##  - int
    ##  - @link Node NXOpen.BlockStyler.Node@endlink
    ##  - int
    ##  and no return type
    IsDropAllowedCallback = Callable[[Tree, Node, int, Node, int], None]
    
    
    ## Represents the callback which gets called when label edit is attempted on any column. The label edit is allowed/disallowed 
    ##        based on return value of this callback.
    ## A callback definition with the following input arguments: 
    ##  - @link Tree NXOpen.BlockStyler.Tree@endlink
    ##  - @link Node NXOpen.BlockStyler.Node@endlink
    ##  - int
    ##  and no return type
    OnBeginLabelEditCallback = Callable[[Tree, Node, int], None]
    
    
    ## Represents the callback which gets called when double clicked is performed on the node.
    ## A callback definition with the following input arguments: 
    ##  - @link Tree NXOpen.BlockStyler.Tree@endlink
    ##  - @link Node NXOpen.BlockStyler.Node@endlink
    ##  - int
    ##  and no return type
    OnDefaultActionCallback = Callable[[Tree, Node, int], None]
    
    
    ##  @brief Represents the callback which gets called when the node is deleted from tree.
    ##       It is expected to perform only clean-up operation related to the deleted node such as clean-up of Node Data.
    ##        
    ## 
    ##  
    ##       Avoid operations such as node insert, node delete etc, and avoid calling any methods of tree. This is 
    ##       particularly severe when dialog is closed (through Ok, dialog-reset etc) because by then tree is unavailable and any usage of tree
    ##       method would raise exception. As the callback is called for each node, the exception would be raised number of times equaling number of nodes available on tree.
    ##       
    ## A callback definition with the following input arguments: 
    ##  - @link Tree NXOpen.BlockStyler.Tree@endlink
    ##  - @link Node NXOpen.BlockStyler.Node@endlink
    ##  and no return type
    OnDeleteNodeCallback = Callable[[Tree, Node], None]
    
    
    ## Represents the callback which gets called when nodes are dropped on any target node. This callback is invoked irrespective of case 
    ##        whether nodes are dragged using MB1 or MB3. If nodes are dragged using MB3 then BlockStyler.Tree.OnDropMenuCallback is called
    ##        prior to the invocation of this callback.
    ## A callback definition with the following input arguments: 
    ##  - @link Tree NXOpen.BlockStyler.Tree@endlink
    ##  - @link Node List[NXOpen.BlockStyler.Node]@endlink
    ##  - int
    ##  - @link Node NXOpen.BlockStyler.Node@endlink
    ##  - int
    ##  - @link Node.DropType NXOpen.BlockStyler.Node.DropType@endlink
    ##  - int
    ##  and no return type
    OnDropCallback = Callable[[Tree, List[Node], int, Node, int, Node.DropType, int], None]
    
    
    ## Represents the callback to show the menu when nodes are dragged using MB3 or right mouse click, and dropped on any target node. 
    ##       
    ##        <br> 
    ##        The menu can be made available using two methods @link BlockStyler::Tree::CreateMenu BlockStyler::Tree::CreateMenu@endlink  and 
    ##        @link BlockStyler::Tree::SetMenu BlockStyler::Tree::SetMenu@endlink . Subsequently, menu is shown and selected menu option is passed as paremeter in 
    ##        the callback BlockStyler.Tree.OnDropCallback       
    ##        <br>        
    ##        
    ## A callback definition with the following input arguments: 
    ##  - @link Tree NXOpen.BlockStyler.Tree@endlink
    ##  - @link Node NXOpen.BlockStyler.Node@endlink
    ##  - int
    ##  - @link Node NXOpen.BlockStyler.Node@endlink
    ##  - int
    ##  and no return type
    OnDropMenuCallback = Callable[[Tree, Node, int, Node, int], None]
    
    
    ## Represents the callback which gets called when user selects an option in edit-control set by 
    ##        BlockStyler.Tree.AskEditControlCallback. If returned @link BlockStyler::Tree::EditControlOptionAccept BlockStyler::Tree::EditControlOptionAccept@endlink  
    ##        then the edited option/text is accepted else it is rejected and old option/text remains.    
    ##       
    ## A callback definition with the following input arguments: 
    ##  - @link Tree NXOpen.BlockStyler.Tree@endlink
    ##  - @link Node NXOpen.BlockStyler.Node@endlink
    ##  - int
    ##  - int
    ##  - str
    ##  - @link Tree.ControlType NXOpen.BlockStyler.Tree.ControlType@endlink
    ##  and no return type
    OnEditOptionSelectedCallback = Callable[[Tree, Node, int, int, str, Tree.ControlType], None]
    
    
    ## Represents the callback which gets called when label edit is completed on any column. 
    ##        The edited label is accepted/rejected based on return value of this callback.
    ## A callback definition with the following input arguments: 
    ##  - @link Tree NXOpen.BlockStyler.Tree@endlink
    ##  - @link Node NXOpen.BlockStyler.Node@endlink
    ##  - int
    ##  - str
    ##  and no return type
    OnEndLabelEditCallback = Callable[[Tree, Node, int, str], None]
    
    
    ## Represents the callback which gets called when the node is expanded. This is called only once.
    ## A callback definition with the following input arguments: 
    ##  - @link Tree NXOpen.BlockStyler.Tree@endlink
    ##  - @link Node NXOpen.BlockStyler.Node@endlink
    ##  and no return type
    OnExpandCallback = Callable[[Tree, Node], None]
    
    
    ##  @brief 
    ##         Represents the callback which gets called for each node when the column is inserted using 
    ##         @link BlockStyler::Tree::InsertColumn BlockStyler::Tree::InsertColumn@endlink . This callback in not invoked if no node is 
    ##         available on the tree. 
    ##         
    ## 
    ##  
    ##        In this callback it is expected to provide column text for individual node.
    ## A callback definition with the following input arguments: 
    ##  - @link Tree NXOpen.BlockStyler.Tree@endlink
    ##  - @link Node NXOpen.BlockStyler.Node@endlink
    ##  - int
    ##  and no return type
    OnInsertColumnCallback = Callable[[Tree, Node, int], None]
    
    
    ## Represents the callback which gets called when the node is inserted.
    ## A callback definition with the following input arguments: 
    ##  - @link Tree NXOpen.BlockStyler.Tree@endlink
    ##  - @link Node NXOpen.BlockStyler.Node@endlink
    ##  and no return type
    OnInsertNodeCallback = Callable[[Tree, Node], None]
    
    
    ## Represents the callback which gets called when MB3 or right click is attempted on node or tree. Value of Node parameter is NULL if 
    ##        MB3 is attempted on area other than node. This distinction allows to have separate menu for node and tree.
    ##         <br> 
    ##        The menu can be made available using two methods @link BlockStyler::Tree::CreateMenu BlockStyler::Tree::CreateMenu@endlink  and 
    ##        @link BlockStyler::Tree::SetMenu BlockStyler::Tree::SetMenu@endlink . Subsequently BlockStyler.Tree.OnMenuSelectionCallback
    ##        is invoked after the menu item is selected.     
    ##         <br> 
    ##       
    ## A callback definition with the following input arguments: 
    ##  - @link Tree NXOpen.BlockStyler.Tree@endlink
    ##  - @link Node NXOpen.BlockStyler.Node@endlink
    ##  - int
    ##  and no return type
    OnMenuCallback = Callable[[Tree, Node, int], None]
    
    
    ## Represents the callback which gets called when one of the menu option is selected. 
    ##        Refer to callback BlockStyler.Tree.OnMenuCallback to make available the menu.
    ##        
    ## A callback definition with the following input arguments: 
    ##  - @link Tree NXOpen.BlockStyler.Tree@endlink
    ##  - @link Node NXOpen.BlockStyler.Node@endlink
    ##  - int
    ##  and no return type
    OnMenuSelectionCallback = Callable[[Tree, Node, int], None]
    
    
    ## Represents the callback which gets called when pre selection is attempted on node.
    ## A callback definition with the following input arguments: 
    ##  - @link Tree NXOpen.BlockStyler.Tree@endlink
    ##  - @link Node NXOpen.BlockStyler.Node@endlink
    ##  - int
    ##  - bool
    ##  and no return type
    OnPreSelectCallback = Callable[[Tree, Node, int, bool], None]
    
    
    ## Represents the callback which gets called when the node is selected.
    ## A callback definition with the following input arguments: 
    ##  - @link Tree NXOpen.BlockStyler.Tree@endlink
    ##  - @link Node NXOpen.BlockStyler.Node@endlink
    ##  - int
    ##  - bool
    ##  and no return type
    OnSelectCallback = Callable[[Tree, Node, int, bool], None]
    
    
    ## Represents the callback which gets called when the state icon is clicked. 
    ##        This callback does not get called when state is changed using the method 
    ##        @link BlockStyler::Node::SetState BlockStyler::Node::SetState@endlink . The node state can be 
    ##        changed in this callback using @link BlockStyler::Node::SetState BlockStyler::Node::SetState@endlink , 
    ##        e.g., node can be changed from checked state to unchecked state and vice-versa.
    ## A callback definition with the following input arguments: 
    ##  - @link Tree NXOpen.BlockStyler.Tree@endlink
    ##  - @link Node NXOpen.BlockStyler.Node@endlink
    ##  - int
    ##  and no return type
    OnStateChangeCallback = Callable[[Tree, Node, int], None]
    
    
    ## Freezes the tree if the value is set to False which implies that no changes would occur 
    ##        in the tree after this point. The tree remains in that state until the value is set to True, 
    ##        after which the tree completely updates itself with the changes performed on it in between 
    ##        the two calls. Use this method to efficiently utilize the tree when it is subjected to enourmous changes.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Flag corresponds to freeze/unfreeze of tree changes.
    def Redraw(tree: Tree, redraw: bool) -> None:
        """
        Freezes the tree if the value is set to False which implies that no changes would occur 
               in the tree after this point. The tree remains in that state until the value is set to True, 
               after which the tree completely updates itself with the changes performed on it in between 
               the two calls. Use this method to efficiently utilize the tree when it is subjected to enourmous changes.
        """
        pass
    
    ## Selects the provided node.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Node to be selected
    def SelectNode(tree: Tree, node: Node, isSelect: bool, isOtherNodeAffected: bool) -> None:
        """
        Selects the provided node.
        """
        pass
    
    ## Selects the provided nodes.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Nodes to be selected
    def SelectNodes(tree: Tree, node: List[Node], isSelect: bool, isOtherNodeAffected: bool) -> None:
        """
        Selects the provided nodes.
        """
        pass
    
    ## Sets the node-edit-control callback
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Callback
    def SetAskEditControlHandler(tree: Tree, cb: Tree.AskEditControlCallback) -> None:
        """
        Sets the node-edit-control callback
        """
        pass
    
    ## Sets the display type of the column.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Unique column Id associated with the column.
    def SetColumnDisplayType(tree: Tree, columnID: int, displayType: Tree.ColumnDisplay) -> None:
        """
        Sets the display type of the column.
        """
        pass
    
    ## Sets the column resize policy.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Unique column Id associated with the column
    def SetColumnResizePolicy(tree: Tree, columnID: int, resizePolicy: Tree.ColumnResizePolicy) -> None:
        """
        Sets the column resize policy.
        """
        pass
    
    ## Sets the column sort callback.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Callback
    def SetColumnSortHandler(tree: Tree, cb: Tree.ColumnSortCallback) -> None:
        """
        Sets the column sort callback.
        """
        pass
    
    ## Sets the column sort option.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Unique column Id associated with the column.
    def SetColumnSortOption(tree: Tree, columnID: int, sortOption: Tree.ColumnSortOption) -> None:
        """
        Sets the column sort option.
        """
        pass
    
    ## Sets the flag indicating whether the column is sortable.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Unique column Id associated with the column.
    def SetColumnSortable(tree: Tree, columnID: int, isSortable: bool) -> None:
        """
        Sets the flag indicating whether the column is sortable.
        """
        pass
    
    ## Sets the column title.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Unique column Id associated with the column.
    def SetColumnTitle(tree: Tree, columnID: int, columnHeaderTitle: str) -> None:
        """
        Sets the column title.
        """
        pass
    
    ## Sets the flag indicating whether the column is visible
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Unique column Id associated with the column
    def SetColumnVisible(tree: Tree, columnID: int, isVisible: bool) -> None:
        """
        Sets the flag indicating whether the column is visible
        """
        pass
    
    ## Sets the column width
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Unique column Id associated with the column.
    def SetColumnWidth(tree: Tree, columnID: int, columnWidth: int) -> None:
        """
        Sets the column width
        """
        pass
    
    ##  @brief Sets the options in edit-control. This method must be used
    ##        in BlockStyler.Tree.AskEditControlCallback to make available the options in edit-control.
    ##         
    ## 
    ##  
    ##       
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Options to be made availabe in edit-control
    def SetEditOptions(tree: Tree, stringArray: List[str], defaultIndex: int) -> None:
        """
         @brief Sets the options in edit-control. This method must be used
               in BlockStyler.Tree.AskEditControlCallback to make available the options in edit-control.
                
        
         
              
        """
        pass
    
    ## Sets the callback handler for node drag
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Callback
    def SetIsDragAllowedHandler(tree: Tree, cb: Tree.IsDragAllowedCallback) -> None:
        """
        Sets the callback handler for node drag
        """
        pass
    
    ## Sets the callback handler for node drop
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Callback
    def SetIsDropAllowedHandler(tree: Tree, cb: Tree.IsDropAllowedCallback) -> None:
        """
        Sets the callback handler for node drop
        """
        pass
    
    ##  Sets the menu, resulting the menu to appear on the screen. This method must be used in callback which is intended to create
    ##         menu, such as BlockStyler.Tree.OnMenuCallback
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Menu.
    def SetMenu(tree: Tree, menu: TreeListMenu) -> None:
        """
         Sets the menu, resulting the menu to appear on the screen. This method must be used in callback which is intended to create
                menu, such as BlockStyler.Tree.OnMenuCallback
        """
        pass
    
    ## Sets the on-begin-label-edit callback
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Callback
    def SetOnBeginLabelEditHandler(tree: Tree, cb: Tree.OnBeginLabelEditCallback) -> None:
        """
        Sets the on-begin-label-edit callback
        """
        pass
    
    ##  Sets the on select node callback 
    ## 
    ##   <br>  Created in NX7.5.2  <br> 

    ## License requirements: None.
    ## Callback.
    def SetOnDefaultActionHandler(tree: Tree, cb: Tree.OnDefaultActionCallback) -> None:
        """
         Sets the on select node callback 
        """
        pass
    
    ##  Sets on delete node callback 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Callback.
    def SetOnDeleteNodeHandler(tree: Tree, cb: Tree.OnDeleteNodeCallback) -> None:
        """
         Sets on delete node callback 
        """
        pass
    
    ## Sets the callback handler for node drop
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Callback
    def SetOnDropHandler(tree: Tree, cb: Tree.OnDropCallback) -> None:
        """
        Sets the callback handler for node drop
        """
        pass
    
    ## Sets the callback handler for on drop menu.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Callback
    def SetOnDropMenuHandler(tree: Tree, cb: Tree.OnDropMenuCallback) -> None:
        """
        Sets the callback handler for on drop menu.
        """
        pass
    
    ## Sets the on-end-label-edit callback
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Callback
    def SetOnEditOptionSelectedHandler(tree: Tree, cb: Tree.OnEditOptionSelectedCallback) -> None:
        """
        Sets the on-end-label-edit callback
        """
        pass
    
    ## Sets the on-end-label-edit callback
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Callback
    def SetOnEndLabelEditHandler(tree: Tree, cb: Tree.OnEndLabelEditCallback) -> None:
        """
        Sets the on-end-label-edit callback
        """
        pass
    
    ## Sets the on expand callback to the tree.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Callback
    def SetOnExpandHandler(tree: Tree, cb: Tree.OnExpandCallback) -> None:
        """
        Sets the on expand callback to the tree.
        """
        pass
    
    ## Sets the on insert column callback to the tree.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Callback.
    def SetOnInsertColumnHandler(tree: Tree, cb: Tree.OnInsertColumnCallback) -> None:
        """
        Sets the on insert column callback to the tree.
        """
        pass
    
    ##  Sets the on insert node callback. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## Callback
    def SetOnInsertNodeHandler(tree: Tree, cb: Tree.OnInsertNodeCallback) -> None:
        """
         Sets the on insert node callback. 
        """
        pass
    
    ##  Sets the on menu callback 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Callback.
    def SetOnMenuHandler(tree: Tree, cb: Tree.OnMenuCallback) -> None:
        """
         Sets the on menu callback 
        """
        pass
    
    ##  Sets the on menu selection callback 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Callback.
    def SetOnMenuSelectionHandler(tree: Tree, cb: Tree.OnMenuSelectionCallback) -> None:
        """
         Sets the on menu selection callback 
        """
        pass
    
    ##  Sets on pre select callback 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Callback
    def SetOnPreSelectHandler(tree: Tree, cb: Tree.OnPreSelectCallback) -> None:
        """
         Sets on pre select callback 
        """
        pass
    
    ##  Sets the on select node callback 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Callback.
    def SetOnSelectHandler(tree: Tree, cb: Tree.OnSelectCallback) -> None:
        """
         Sets the on select node callback 
        """
        pass
    
    ## Sets the on state change callback.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Callback
    def SetOnStateChangeHandler(tree: Tree, cb: Tree.OnStateChangeCallback) -> None:
        """
        Sets the on state change callback.
        """
        pass
    
    ## Sets the pre selection time out. BlockStyler.Tree.OnPreSelectCallback is called based on this value.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Time in millisecond
    def SetPreSelectionTimeOut(tree: Tree, timeOut: float) -> None:
        """
        Sets the pre selection time out. BlockStyler.Tree.OnPreSelectCallback is called based on this value.
        """
        pass
    
    ## Represents the callback which gets called when the node state is set 
    ##        by @link BlockStyler::Node::SetState BlockStyler::Node::SetState@endlink  and the corresponding 
    ##        state icon of node state is not known. This callback is expected to provide 
    ##        the icon name for the node state used in the application. This callback is 
    ##        called only once for any given node state.
    ## A callback definition with the following input arguments: 
    ##  - @link Tree NXOpen.BlockStyler.Tree@endlink
    ##  - @link Node NXOpen.BlockStyler.Node@endlink
    ##  - int
    ##  and no return type
    StateIconNameCallback = Callable[[Tree, Node, int], None]
    
    
    ## Sets the state icon name callback.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Callback.
    def SetStateIconNameHandler(tree: Tree, cb: Tree.StateIconNameCallback) -> None:
        """
        Sets the state icon name callback.
        """
        pass
    
    ## Represents the callback which gets called when tree seeks the tooltip.
    ## A callback definition with the following input arguments: 
    ##  - @link Tree NXOpen.BlockStyler.Tree@endlink
    ##  - @link Node NXOpen.BlockStyler.Node@endlink
    ##  - int
    ##  and no return type
    ToolTipTextCallback = Callable[[Tree, Node, int], None]
    
    
    ## Sets the tool tip callback.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## Callback.
    def SetToolTipTextHandler(tree: Tree, cb: Tree.ToolTipTextCallback) -> None:
        """
        Sets the tool tip callback.
        """
        pass
    
    ## Test the action to insert the column. 
    ##  @return columnPosition (int): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="columnID"> (int) </param>
    ## <param name="columnTitle"> (str) </param>
    ## <param name="columnWidth"> (int) </param>
    def TestColumnInserted(tree: Tree, columnID: int, columnTitle: str, columnWidth: int) -> int:
        """
        Test the action to insert the column. 
         @return columnPosition (int): .
        """
        pass
    
    ## Test the action to sort the column. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="columnID"> (int) </param>
    ## <param name="node1"> (@link Node NXOpen.BlockStyler.Node@endlink) </param>
    ## <param name="node2"> (@link Node NXOpen.BlockStyler.Node@endlink) </param>
    ## <param name="sortOption"> (@link Tree.ColumnSortOption NXOpen.BlockStyler.Tree.ColumnSortOption@endlink) </param>
    def TestColumnSort(tree: Tree, columnID: int, node1: Node, node2: Node, sortOption: Tree.ColumnSortOption) -> None:
        """
        Test the action to sort the column. 
        """
        pass
    
    ## Test the action to show context menu. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="node"> (@link Node NXOpen.BlockStyler.Node@endlink) </param>
    ## <param name="columnID"> (int) </param>
    def TestContextMenu(tree: Tree, node: Node, columnID: int) -> None:
        """
        Test the action to show context menu. 
        """
        pass
    
    ## Test the default action. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="node"> (@link Node NXOpen.BlockStyler.Node@endlink) </param>
    ## <param name="columnID"> (int) </param>
    def TestDefaultAction(tree: Tree, node: Node, columnID: int) -> None:
        """
        Test the default action. 
        """
        pass
    
    ## Test the action to show the drop menu. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="node"> (@link Node NXOpen.BlockStyler.Node@endlink) </param>
    ## <param name="columnID"> (int) </param>
    ## <param name="targetNode"> (@link Node NXOpen.BlockStyler.Node@endlink) </param>
    ## <param name="targetColumnID"> (int) </param>
    def TestDropMenu(tree: Tree, node: Node, columnID: int, targetNode: Node, targetColumnID: int) -> None:
        """
        Test the action to show the drop menu. 
        """
        pass
    
    ## Test the action to edit the label of the node. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="node"> (@link Node NXOpen.BlockStyler.Node@endlink) </param>
    ## <param name="columnID"> (int) </param>
    ## <param name="editedText"> (str) </param>
    def TestLabelEdit(tree: Tree, node: Node, columnID: int, editedText: str) -> None:
        """
        Test the action to edit the label of the node. 
        """
        pass
    
    ## Test the action to click the command of the context menu. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="node"> (@link Node NXOpen.BlockStyler.Node@endlink) </param>
    ## <param name="command"> (int) </param>
    def TestMenuAction(tree: Tree, node: Node, command: int) -> None:
        """
        Test the action to click the command of the context menu. 
        """
        pass
    
    ## Test the action to delete the node. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="node"> (@link Node NXOpen.BlockStyler.Node@endlink) </param>
    def TestNodeDeleted(tree: Tree, node: Node) -> None:
        """
        Test the action to delete the node. 
        """
        pass
    
    ## Test the action to click the command of the drop menu. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="node"> (@link Node NXOpen.BlockStyler.Node@endlink) </param>
    ## <param name="columnID"> (int) </param>
    ## <param name="targetNode"> (@link Node NXOpen.BlockStyler.Node@endlink) </param>
    ## <param name="targetColumnID"> (int) </param>
    ## <param name="command"> (int) </param>
    def TestNodeDrop(tree: Tree, node: Node, columnID: int, targetNode: Node, targetColumnID: int, command: int) -> None:
        """
        Test the action to click the command of the drop menu. 
        """
        pass
    
    ## Test the action to expand the node. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="node"> (@link Node NXOpen.BlockStyler.Node@endlink) </param>
    ## <param name="expandOption"> (@link Node.ExpandOption NXOpen.BlockStyler.Node.ExpandOption@endlink) </param>
    def TestNodeExpanded(tree: Tree, node: Node, expandOption: Node.ExpandOption) -> None:
        """
        Test the action to expand the node. 
        """
        pass
    
    ## Test the action to insert a node. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="newNode"> (@link Node NXOpen.BlockStyler.Node@endlink) </param>
    ## <param name="parentNode"> (@link Node NXOpen.BlockStyler.Node@endlink) </param>
    ## <param name="afterNode"> (@link Node NXOpen.BlockStyler.Node@endlink) </param>
    ## <param name="nodeInsertOption"> (@link Tree.NodeInsertOption NXOpen.BlockStyler.Tree.NodeInsertOption@endlink) </param>
    def TestNodeInserted(tree: Tree, newNode: Node, parentNode: Node, afterNode: Node, nodeInsertOption: Tree.NodeInsertOption) -> None:
        """
        Test the action to insert a node. 
        """
        pass
    
    ## Test the action to preselect the node. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="node"> (@link Node NXOpen.BlockStyler.Node@endlink) </param>
    ## <param name="columnID"> (int) </param>
    def TestNodePreselection(tree: Tree, node: Node, columnID: int) -> None:
        """
        Test the action to preselect the node. 
        """
        pass
    
    ## Test the action to select the node. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="node"> (@link Node NXOpen.BlockStyler.Node@endlink) </param>
    ## <param name="isSelect"> (bool) </param>
    ## <param name="isOtherNodeAffected"> (bool) </param>
    def TestNodeSelected(tree: Tree, node: Node, isSelect: bool, isOtherNodeAffected: bool) -> None:
        """
        Test the action to select the node. 
        """
        pass
    
    ## Test the action to preselect the node. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="node"> (@link Node NXOpen.BlockStyler.Node@endlink) </param>
    ## <param name="state"> (int) </param>
    def TestStateChanged(tree: Tree, node: Node, state: int) -> None:
        """
        Test the action to preselect the node. 
        """
        pass
    
import NXOpen
##  Represents a UI Block
## 
##   <br>  Created in NX6.0.0  <br> 

class UIBlock(NXOpen.TaggedObject): 
    """ Represents a UI Block"""


    ## Getter for property: (bool) Enable
    ##   the Enable.  
    ##    If true, the block is sensitive.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def Enable(self) -> bool:
        """
        Getter for property: (bool) Enable
          the Enable.  
           If true, the block is sensitive.  
         
        """
        pass
    
    ## Setter for property: (bool) Enable

    ##   the Enable.  
    ##    If true, the block is sensitive.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Enable.setter
    def Enable(self, enable: bool):
        """
        Setter for property: (bool) Enable
          the Enable.  
           If true, the block is sensitive.  
         
        """
        pass
    
    ## Getter for property: (bool) Expanded
    ##   the Expanded  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def Expanded(self) -> bool:
        """
        Getter for property: (bool) Expanded
          the Expanded  
            
         
        """
        pass
    
    ## Setter for property: (bool) Expanded

    ##   the Expanded  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Expanded.setter
    def Expanded(self, expanded: bool):
        """
        Setter for property: (bool) Expanded
          the Expanded  
            
         
        """
        pass
    
    ## Getter for property: (bool) Group
    ##   the Group  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def Group(self) -> bool:
        """
        Getter for property: (bool) Group
          the Group  
            
         
        """
        pass
    
    ## Setter for property: (bool) Group

    ##   the Group  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Group.setter
    def Group(self, group: bool):
        """
        Setter for property: (bool) Group
          the Group  
            
         
        """
        pass
    
    ## Getter for property: (str) Label
    ##   the Label  
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
          the Label  
            
         
        """
        pass
    
    ## Setter for property: (str) Label

    ##   the Label  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Label.setter
    def Label(self, label: str):
        """
        Setter for property: (str) Label
          the Label  
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##   the name of the block or BlockID  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
          the name of the block or BlockID  
            
         
        """
        pass
    
    ## Getter for property: (bool) Show
    ##   the Visibility of block.  
    ##    If true, the block is visible. Otherwise invisible.
    ##     This is readonly property for dialog and will be always true for dialog.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def Show(self) -> bool:
        """
        Getter for property: (bool) Show
          the Visibility of block.  
           If true, the block is visible. Otherwise invisible.
            This is readonly property for dialog and will be always true for dialog.  
         
        """
        pass
    
    ## Setter for property: (bool) Show

    ##   the Visibility of block.  
    ##    If true, the block is visible. Otherwise invisible.
    ##     This is readonly property for dialog and will be always true for dialog.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Show.setter
    def Show(self, show: bool):
        """
        Setter for property: (bool) Show
          the Visibility of block.  
           If true, the block is visible. Otherwise invisible.
            This is readonly property for dialog and will be always true for dialog.  
         
        """
        pass
    
    ## Getter for property: (str) Type
    ##   the type of block   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return str
    @property
    def Type(self) -> str:
        """
        Getter for property: (str) Type
          the type of block   
            
         
        """
        pass
    
    ## Focuses on the block. Use this method for both focus and keyboard focus.
    ## 
    ##   <br>  Created in NX6.0.2  <br> 

    ## License requirements: None.
    @staticmethod
    def Focus(block: UIBlock) -> None:
        """
        Focuses on the block. Use this method for both focus and keyboard focus.
        """
        pass
    
    ##  Returns the properties of the block 
    ##  @return propertyList (@link PropertyList NXOpen.BlockStyler.PropertyList@endlink): .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetProperties(block: UIBlock) -> PropertyList:
        """
         Returns the properties of the block 
         @return propertyList (@link PropertyList NXOpen.BlockStyler.PropertyList@endlink): .
        """
        pass
    
    ## Tests the focus change callbacks. Use this method for both focus and keyboard focus.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    @staticmethod
    def TestFocusChange(block: UIBlock) -> None:
        """
        Tests the focus change callbacks. Use this method for both focus and keyboard focus.
        """
        pass
    
##  Represents a Wizard block 
## 
##   <br>  Created in NX7.5.0  <br> 

class Wizard(UIBlock): 
    """ Represents a Wizard block """


    ##  Represents Wizard dialog response values based on navigation button pressed 
    ##  Back button was pressed.. 
    class DialogResponse(Enum):
        """
        Members Include: <Back> <Next> <Finish> <Apply> <Cancel>
        """
        Back: int
        Next: int
        Finish: int
        Apply: int
        Cancel: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Wizard.DialogResponse:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Specifies the type of action performed on a sub-node in the Wizard Task Navigator.
    ##         The action is passed into the callback BlockStyler.Wizard.OnSubNodeCallback. 
    ##  Sub-node has been selected. 
    class SubNodeAction(Enum):
        """
        Members Include: <Select> <Deselect> <Check> <Uncheck>
        """
        Select: int
        Deselect: int
        Check: int
        Uncheck: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Wizard.SubNodeAction:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Specifies an item in the Task Navigator.  
    ##   
    class TaskNavigatorItem(Enum):
        """
        Members Include: <Step> <SubNode> <Background>
        """
        Step: int
        SubNode: int
        Background: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Wizard.TaskNavigatorItem:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (int) CurrentStep
    ##   the CurrentStep.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def CurrentStep(self) -> int:
        """
        Getter for property: (int) CurrentStep
          the CurrentStep.  
             
         
        """
        pass
    
    ## Setter for property: (int) CurrentStep

    ##   the CurrentStep.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @CurrentStep.setter
    def CurrentStep(self, currentStep: int):
        """
        Setter for property: (int) CurrentStep
          the CurrentStep.  
             
         
        """
        pass
    
    ## Getter for property: (bool) HighQualityBitmap
    ##   the HighQualityBitmap.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def HighQualityBitmap(self) -> bool:
        """
        Getter for property: (bool) HighQualityBitmap
          the HighQualityBitmap.  
             
         
        """
        pass
    
    ## Setter for property: (bool) HighQualityBitmap

    ##   the HighQualityBitmap.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @HighQualityBitmap.setter
    def HighQualityBitmap(self, highQuality: bool):
        """
        Setter for property: (bool) HighQualityBitmap
          the HighQualityBitmap.  
             
         
        """
        pass
    
    ## Getter for property: (bool) Localize
    ##   the Localize.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def Localize(self) -> bool:
        """
        Getter for property: (bool) Localize
          the Localize.  
             
         
        """
        pass
    
    ## Setter for property: (bool) Localize

    ##   the Localize.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Localize.setter
    def Localize(self, localize: bool):
        """
        Setter for property: (bool) Localize
          the Localize.  
             
         
        """
        pass
    
    ## Getter for property: (@link PropertyList NXOpen.BlockStyler.PropertyList@endlink) Members
    ##   the Members  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return PropertyList
    @property
    def Members(self) -> PropertyList:
        """
        Getter for property: (@link PropertyList NXOpen.BlockStyler.PropertyList@endlink) Members
          the Members  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowTaskNavigator
    ##   the ShowTaskNavigator.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowTaskNavigator(self) -> bool:
        """
        Getter for property: (bool) ShowTaskNavigator
          the ShowTaskNavigator.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ShowTaskNavigator

    ##   the ShowTaskNavigator.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowTaskNavigator.setter
    def ShowTaskNavigator(self, show: bool):
        """
        Setter for property: (bool) ShowTaskNavigator
          the ShowTaskNavigator.  
             
         
        """
        pass
    
    ##  Creates a popup menu. Use @link BlockStyler::Wizard::SetMenu BlockStyler::Wizard::SetMenu@endlink  to set
    ##          the created menu.  See the @link BlockStyler::TreeListMenu BlockStyler::TreeListMenu@endlink  for
    ##          information on creating a menu.  
    ##  @return menu (@link TreeListMenu NXOpen.BlockStyler.TreeListMenu@endlink):  .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    def CreateMenu(wizard: Wizard) -> TreeListMenu:
        """
         Creates a popup menu. Use @link BlockStyler::Wizard::SetMenu BlockStyler::Wizard::SetMenu@endlink  to set
                 the created menu.  See the @link BlockStyler::TreeListMenu BlockStyler::TreeListMenu@endlink  for
                 information on creating a menu.  
         @return menu (@link TreeListMenu NXOpen.BlockStyler.TreeListMenu@endlink):  .
        """
        pass
    
    ##  Create a sub-node for a step in the Task Navigator. 
    ##  @return subNodeId (int):  Unique id for the sub-node. .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  The step to add a sub-node. 
    def CreateStepSubNode(wizard: Wizard, step: int, text: str, bitmap: str, showCheckBox: bool, checkBoxChecked: bool) -> int:
        """
         Create a sub-node for a step in the Task Navigator. 
         @return subNodeId (int):  Unique id for the sub-node. .
        """
        pass
    
    ##  Gets the StepBannerBitmaps. Gets the list of bitmaps for the step bitmaps in the banner area.
    ##  @return bitmaps (List[str]): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStepBannerBitmaps(wizard: Wizard) -> List[str]:
        """
         Gets the StepBannerBitmaps. Gets the list of bitmaps for the step bitmaps in the banner area.
         @return bitmaps (List[str]): .
        """
        pass
    
    ##  Gets the StepBitmaps. Gets the list of bitmaps for the node bitmaps in the Task Navigator.
    ##  @return bitmaps (List[str]): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStepBitmaps(wizard: Wizard) -> List[str]:
        """
         Gets the StepBitmaps. Gets the list of bitmaps for the node bitmaps in the Task Navigator.
         @return bitmaps (List[str]): .
        """
        pass
    
    ##  Gets the StepCues. Gets the list of cue lines for the wizard steps.
    ##  @return cues (List[str]): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStepCues(wizard: Wizard) -> List[str]:
        """
         Gets the StepCues. Gets the list of cue lines for the wizard steps.
         @return cues (List[str]): .
        """
        pass
    
    ##  Gets the StepText. Gets the list of step descriptions for the banner area.
    ##  @return text (List[str]): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStepText(wizard: Wizard) -> List[str]:
        """
         Gets the StepText. Gets the list of step descriptions for the banner area.
         @return text (List[str]): .
        """
        pass
    
    ##  The IsStepOkay callback allows the client to notify the Wizard that the step is okay
    ##         or not.  Returns true if the step is okay and false otherwise. The step parameter for the
    ##         callback is zero based and represents the steps in the Wizard.
    ## A callback definition with the following input arguments: 
    ##  - @link Wizard NXOpen.BlockStyler.Wizard@endlink
    ##  - int
    ##  and no return type
    IsStepOkayCallback = Callable[[Wizard, int], None]
    
    
    ##  The OnMenu callback notifies a client prior to creating the popup menu in the Task
    ##         Navigator.  The item parameter specifies the popup menu was activated on a step,
    ##         sub-node or the background. The step parameter for the callback is zero based and
    ##         represents the steps in the Wizard.  The subNodeId parameter is the unique id returned
    ##         by @link BlockStyler::Wizard::CreateStepSubNode BlockStyler::Wizard::CreateStepSubNode@endlink .
    ##         If the popup menu is invoked on the background of the Task Navigator the step and
    ##         subNodeId parameters will be -1.  
    ## A callback definition with the following input arguments: 
    ##  - @link Wizard NXOpen.BlockStyler.Wizard@endlink
    ##  - @link Wizard.TaskNavigatorItem NXOpen.BlockStyler.Wizard.TaskNavigatorItem@endlink
    ##  - int
    ##  - int
    ##  and no return type
    OnMenuCallback = Callable[[Wizard, Wizard.TaskNavigatorItem, int, int], None]
    
    
    ##  The OnMenuSelection callback notifies a client of the menu item selection on the popup menu
    ##         in the Task Navigator.  The item parameter specifies the popup menu was activated on a step,
    ##         sub-node or the background. The step parameter for the callback is zero based and
    ##         represents the steps in the Wizard.  The subNodeId parameter is the unique id returned
    ##         by @link BlockStyler::Wizard::CreateStepSubNode BlockStyler::Wizard::CreateStepSubNode@endlink .  The menuItemIndex parameter will
    ##         be the unique id specified when creating menu items for the BlockStyler.TreeListMenu.
    ##         If the popup menu is invoked on the background of the Task Navigator the step and
    ##         subNodeId parameters will be -1.  
    ## A callback definition with the following input arguments: 
    ##  - @link Wizard NXOpen.BlockStyler.Wizard@endlink
    ##  - @link Wizard.TaskNavigatorItem NXOpen.BlockStyler.Wizard.TaskNavigatorItem@endlink
    ##  - int
    ##  - int
    ##  - int
    ##  and no return type
    OnMenuSelectionCallback = Callable[[Wizard, Wizard.TaskNavigatorItem, int, int, int], None]
    
    
    ##  The OnSubNode callback notifies a client of an action performed
    ##         on a sub-node in the Wizard Task Navigator.  The step
    ##         parameter for the callback is zero based and represents the steps in the Wizard.
    ##         The subNodeId parameter is the unique id returned by @link BlockStyler::Wizard::CreateStepSubNode BlockStyler::Wizard::CreateStepSubNode@endlink .  
    ## A callback definition with the following input arguments: 
    ##  - @link Wizard NXOpen.BlockStyler.Wizard@endlink
    ##  - int
    ##  - int
    ##  - @link Wizard.SubNodeAction NXOpen.BlockStyler.Wizard.SubNodeAction@endlink
    ##  and no return type
    OnSubNodeCallback = Callable[[Wizard, int, int, Wizard.SubNodeAction], None]
    
    
    ##  Remove a sub-node in the Task Navigator. 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  The sub-node id. 
    def RemoveStepSubNode(wizard: Wizard, subNodeId: int) -> None:
        """
         Remove a sub-node in the Task Navigator. 
        """
        pass
    
    ##  Sets the dialog navigation response for testing
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ## 
    ## <param name="response"> (@link Wizard.DialogResponse NXOpen.BlockStyler.Wizard.DialogResponse@endlink) </param>
    def SetDialogNavigationResponse(wizard: Wizard, response: Wizard.DialogResponse) -> None:
        """
         Sets the dialog navigation response for testing
        """
        pass
    
    ##  Sets the IsStepOkay handler. 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  
    def SetIsStepOkayHandler(wizard: Wizard, cb: Wizard.IsStepOkayCallback) -> None:
        """
         Sets the IsStepOkay handler. 
        """
        pass
    
    ##  Set the menu items for the popup menu for a step, sub-node or the background
    ##         in the Task Navigator.  See the @link BlockStyler::TreeListMenu BlockStyler::TreeListMenu@endlink  for
    ##         information on creating a menu.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  
    def SetMenu(wizard: Wizard, menu: TreeListMenu) -> None:
        """
         Set the menu items for the popup menu for a step, sub-node or the background
                in the Task Navigator.  See the @link BlockStyler::TreeListMenu BlockStyler::TreeListMenu@endlink  for
                information on creating a menu.
        """
        pass
    
    ##  Sets the OnMenu handler. 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  
    def SetOnMenuHandler(wizard: Wizard, cb: Wizard.OnMenuCallback) -> None:
        """
         Sets the OnMenu handler. 
        """
        pass
    
    ##  Sets the OnMenuSelection handler. 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  
    def SetOnMenuSelectionHandler(wizard: Wizard, cb: Wizard.OnMenuSelectionCallback) -> None:
        """
         Sets the OnMenuSelection handler. 
        """
        pass
    
    ##  Sets the OnSubNode handler. 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  
    def SetOnSubNodeHandler(wizard: Wizard, cb: Wizard.OnSubNodeCallback) -> None:
        """
         Sets the OnSubNode handler. 
        """
        pass
    
    ##  Sets the StepBannerBitmaps. Sets the list of bitmaps for the step bitmaps in the banner area.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="bitmaps"> (List[str]) </param>
    def SetStepBannerBitmaps(wizard: Wizard, bitmaps: List[str]) -> None:
        """
         Sets the StepBannerBitmaps. Sets the list of bitmaps for the step bitmaps in the banner area.
        """
        pass
    
    ##  Sets the StepBitmaps. Sets the list of bitmaps for the node bitmaps in the Task Navigator.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="bitmaps"> (List[str]) </param>
    def SetStepBitmaps(wizard: Wizard, bitmaps: List[str]) -> None:
        """
         Sets the StepBitmaps. Sets the list of bitmaps for the node bitmaps in the Task Navigator.
        """
        pass
    
    ##  Sets the StepCues. Sets the list of cue lines for the wizard steps.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="cues"> (List[str]) </param>
    def SetStepCues(wizard: Wizard, cues: List[str]) -> None:
        """
         Sets the StepCues. Sets the list of cue lines for the wizard steps.
        """
        pass
    
    ##  The StepNotifyPost callback notifies a client after navigating to the next step 
    ##         in the Wizard.  The nextStep parameter for the callback is zero based and represents
    ##         the steps in the Wizard. 
    ## A callback definition with the following input arguments: 
    ##  - @link Wizard NXOpen.BlockStyler.Wizard@endlink
    ##  - int
    ##  and no return type
    StepNotifyPostCallback = Callable[[Wizard, int], None]
    
    
    ##  Sets the StepNotifyPost handler. 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  
    def SetStepNotifyPostHandler(wizard: Wizard, cb: Wizard.StepNotifyPostCallback) -> None:
        """
         Sets the StepNotifyPost handler. 
        """
        pass
    
    ##  The StepNotifyPre callback notifies a client before navigating to the next step 
    ##         in the Wizard.  The nextStep parameter for the callback is zero based and represents
    ##         the steps in the Wizard. 
    ## A callback definition with the following input arguments: 
    ##  - @link Wizard NXOpen.BlockStyler.Wizard@endlink
    ##  - int
    ##  and no return type
    StepNotifyPreCallback = Callable[[Wizard, int], None]
    
    
    ##  Sets the StepNotifyPre handler. 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  
    def SetStepNotifyPreHandler(wizard: Wizard, cb: Wizard.StepNotifyPreCallback) -> None:
        """
         Sets the StepNotifyPre handler. 
        """
        pass
    
    ##  Sets the StepText. Sets the list of step descriptions for the banner area.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="text"> (List[str]) </param>
    def SetStepText(wizard: Wizard, text: List[str]) -> None:
        """
         Sets the StepText. Sets the list of step descriptions for the banner area.
        """
        pass
    
    ## Tests set current step.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ##  
    def TestCurrentStepChanged(wizard: Wizard, currentStep: int) -> None:
        """
        Tests set current step.
        """
        pass
    
    ## Tests the menu action mapped to this block.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ##  
    def TestMenuAction(wizard: Wizard, item: Wizard.TaskNavigatorItem, stepNo: int, subNodeId: int) -> None:
        """
        Tests the menu action mapped to this block.
        """
        pass
    
    ## Tests the menu selection mapped to this block.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ##  
    def TestMenuSelection(wizard: Wizard, item: Wizard.TaskNavigatorItem, stepNo: int, subNodeId: int, menuItemIndex: int) -> None:
        """
        Tests the menu selection mapped to this block.
        """
        pass
    
    ## Tests the subnode action mapped to this block.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_auto_test_studio (" NX Automated Testing Studio")
    ##  
    def TestSubnodeAction(wizard: Wizard, stepNo: int, subNodeId: int, item: Wizard.SubNodeAction) -> None:
        """
        Tests the subnode action mapped to this block.
        """
        pass
    
## @package NXOpen.BlockStyler
## Classes, Enums and Structs under NXOpen.BlockStyler namespace

##  @link BlockDialogDialogMode NXOpen.BlockStyler.BlockDialogDialogMode @endlink is an alias for @link BlockDialog.DialogMode NXOpen.BlockStyler.BlockDialog.DialogMode@endlink
BlockDialogDialogMode = BlockDialog.DialogMode


##  @link BlockDialogDialogResponse NXOpen.BlockStyler.BlockDialogDialogResponse @endlink is an alias for @link BlockDialog.DialogResponse NXOpen.BlockStyler.BlockDialog.DialogResponse@endlink
BlockDialogDialogResponse = BlockDialog.DialogResponse


##  @link MessageBoxTesterResponse NXOpen.BlockStyler.MessageBoxTesterResponse @endlink is an alias for @link MessageBoxTester.Response NXOpen.BlockStyler.MessageBoxTester.Response@endlink
MessageBoxTesterResponse = MessageBoxTester.Response


##  @link NodeDragType NXOpen.BlockStyler.NodeDragType @endlink is an alias for @link Node.DragType NXOpen.BlockStyler.Node.DragType@endlink
NodeDragType = Node.DragType


##  @link NodeDropType NXOpen.BlockStyler.NodeDropType @endlink is an alias for @link Node.DropType NXOpen.BlockStyler.Node.DropType@endlink
NodeDropType = Node.DropType


##  @link NodeExpandOption NXOpen.BlockStyler.NodeExpandOption @endlink is an alias for @link Node.ExpandOption NXOpen.BlockStyler.Node.ExpandOption@endlink
NodeExpandOption = Node.ExpandOption


##  @link NodeScroll NXOpen.BlockStyler.NodeScroll @endlink is an alias for @link Node.Scroll NXOpen.BlockStyler.Node.Scroll@endlink
NodeScroll = Node.Scroll


##  @link PropertyListListMode NXOpen.BlockStyler.PropertyListListMode @endlink is an alias for @link PropertyList.ListMode NXOpen.BlockStyler.PropertyList.ListMode@endlink
PropertyListListMode = PropertyList.ListMode


##  @link PropertyListPropertyType NXOpen.BlockStyler.PropertyListPropertyType @endlink is an alias for @link PropertyList.PropertyType NXOpen.BlockStyler.PropertyList.PropertyType@endlink
PropertyListPropertyType = PropertyList.PropertyType


##  @link SelectObjectFilterType NXOpen.BlockStyler.SelectObjectFilterType @endlink is an alias for @link SelectObject.FilterType NXOpen.BlockStyler.SelectObject.FilterType@endlink
SelectObjectFilterType = SelectObject.FilterType


##  @link SetListInsertionLocation NXOpen.BlockStyler.SetListInsertionLocation @endlink is an alias for @link SetList.InsertionLocation NXOpen.BlockStyler.SetList.InsertionLocation@endlink
SetListInsertionLocation = SetList.InsertionLocation


##  @link TreeBeginLabelEditState NXOpen.BlockStyler.TreeBeginLabelEditState @endlink is an alias for @link Tree.BeginLabelEditState NXOpen.BlockStyler.Tree.BeginLabelEditState@endlink
TreeBeginLabelEditState = Tree.BeginLabelEditState


##  @link TreeColumnDisplay NXOpen.BlockStyler.TreeColumnDisplay @endlink is an alias for @link Tree.ColumnDisplay NXOpen.BlockStyler.Tree.ColumnDisplay@endlink
TreeColumnDisplay = Tree.ColumnDisplay


##  @link TreeColumnResizePolicy NXOpen.BlockStyler.TreeColumnResizePolicy @endlink is an alias for @link Tree.ColumnResizePolicy NXOpen.BlockStyler.Tree.ColumnResizePolicy@endlink
TreeColumnResizePolicy = Tree.ColumnResizePolicy


##  @link TreeColumnSortOption NXOpen.BlockStyler.TreeColumnSortOption @endlink is an alias for @link Tree.ColumnSortOption NXOpen.BlockStyler.Tree.ColumnSortOption@endlink
TreeColumnSortOption = Tree.ColumnSortOption


##  @link TreeControlType NXOpen.BlockStyler.TreeControlType @endlink is an alias for @link Tree.ControlType NXOpen.BlockStyler.Tree.ControlType@endlink
TreeControlType = Tree.ControlType


##  @link TreeEditControlOption NXOpen.BlockStyler.TreeEditControlOption @endlink is an alias for @link Tree.EditControlOption NXOpen.BlockStyler.Tree.EditControlOption@endlink
TreeEditControlOption = Tree.EditControlOption


##  @link TreeEndLabelEditState NXOpen.BlockStyler.TreeEndLabelEditState @endlink is an alias for @link Tree.EndLabelEditState NXOpen.BlockStyler.Tree.EndLabelEditState@endlink
TreeEndLabelEditState = Tree.EndLabelEditState


##  @link TreeNodeInsertOption NXOpen.BlockStyler.TreeNodeInsertOption @endlink is an alias for @link Tree.NodeInsertOption NXOpen.BlockStyler.Tree.NodeInsertOption@endlink
TreeNodeInsertOption = Tree.NodeInsertOption


##  @link WizardDialogResponse NXOpen.BlockStyler.WizardDialogResponse @endlink is an alias for @link Wizard.DialogResponse NXOpen.BlockStyler.Wizard.DialogResponse@endlink
WizardDialogResponse = Wizard.DialogResponse


##  @link WizardSubNodeAction NXOpen.BlockStyler.WizardSubNodeAction @endlink is an alias for @link Wizard.SubNodeAction NXOpen.BlockStyler.Wizard.SubNodeAction@endlink
WizardSubNodeAction = Wizard.SubNodeAction


##  @link WizardTaskNavigatorItem NXOpen.BlockStyler.WizardTaskNavigatorItem @endlink is an alias for @link Wizard.TaskNavigatorItem NXOpen.BlockStyler.Wizard.TaskNavigatorItem@endlink
WizardTaskNavigatorItem = Wizard.TaskNavigatorItem


