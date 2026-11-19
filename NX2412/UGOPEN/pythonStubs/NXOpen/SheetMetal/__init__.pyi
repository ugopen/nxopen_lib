from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class FlatPatternSettings(NXOpen.TaggedObject): 
    """ Provides access to object and callout properties for sheet-metal data in
        flat pattern views on drawings. The class is created upon a query to
        obtain the FlatPatternView object from either a view (style) or a 
        part (preferences). """
    class FlatPatternObjectType(Enum):
        """
        Members Include: 
         |BendCenterLine|  Deprecated 
         |BendUpCenterLine|  
         |BendDownCenterLine|  
         |BendTangentLine|  
         |OuterMoldLine|  
         |InnerMoldLine|  
         |ExteriorCurves|  
         |InteriorCurves|  Deprecated 
         |InteriorCutoutCurves|  
         |InteriorFeatureCurves|  
         |LighteningHoleCenter|  
         |JoggleLine|  
         |AddedTopGeometry|  
         |AddedBottomGeometry|  
         |ToolMarker|  
         |Hole|  
         |Centermark|  

        """
        BendCenterLine: int
        BendUpCenterLine: int
        BendDownCenterLine: int
        BendTangentLine: int
        OuterMoldLine: int
        InnerMoldLine: int
        ExteriorCurves: int
        InteriorCurves: int
        InteriorCutoutCurves: int
        InteriorFeatureCurves: int
        LighteningHoleCenter: int
        JoggleLine: int
        AddedTopGeometry: int
        AddedBottomGeometry: int
        ToolMarker: int
        Hole: int
        Centermark: int
        @staticmethod
        def ValueOf(value: int) -> FlatPatternSettings.FlatPatternObjectType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FlatPatternCalloutTypeDisplay:
        """
         The members of the following structure are the display data for a
                    callout in a flat pattern drawing member view. 
         FlatPatternSettingsFlatPatternCalloutTypeDisplay_Struct NXOpen.S is an alias for  FlatPatternSettings.FlatPatternCalloutTypeDisplay NXOpen.S.
        """
        @property
        def Type(self) -> str:
            """
            Getter for property Type
            The name of the callout type.

            """
            pass
        @Type.setter
        def Type(self, value: str):
            """
            Getter for property Type
            The name of the callout type.
            Setter for property Type
            The name of the callout type.

            """
            pass
        @property
        def IsEnabled(self) -> int:
            """
            Getter for property IsEnabled
            Enabled status for the callout type.

            """
            pass
        @IsEnabled.setter
        def IsEnabled(self, value: int):
            """
            Getter for property IsEnabled
            Enabled status for the callout type.
            Setter for property IsEnabled
            Enabled status for the callout type.

            """
            pass
        @property
        def Name(self) -> str:
            """
            Getter for property Name
            dialog name for the callout type.

            """
            pass
        @Name.setter
        def Name(self, value: str):
            """
            Getter for property Name
            dialog name for the callout type.
            Setter for property Name
            dialog name for the callout type.

            """
            pass
    class FlatPatternObjectTypeDisplay:
        """
         The members of the following structure are the display data for an
                    object in a flat pattern drawing member view. 
         FlatPatternSettingsFlatPatternObjectTypeDisplay_Struct NXOpen.S is an alias for  FlatPatternSettings.FlatPatternObjectTypeDisplay NXOpen.S.
        """
        @property
        def Type(self) -> FlatPatternSettings.FlatPatternObjectType:
            """
            Getter for property Type
            Object type

            """
            pass
        @Type.setter
        def Type(self, value: FlatPatternSettings.FlatPatternObjectType):
            """
            Getter for property Type
            Object type
            Setter for property Type
            Object type

            """
            pass
        @property
        def IsEnabled(self) -> int:
            """
            Getter for property IsEnabled
            Enabled status for the object type

            """
            pass
        @IsEnabled.setter
        def IsEnabled(self, value: int):
            """
            Getter for property IsEnabled
            Enabled status for the object type
            Setter for property IsEnabled
            Enabled status for the object type

            """
            pass
        @property
        def Color(self) -> int:
            """
            Getter for property Color
            Object color

            """
            pass
        @Color.setter
        def Color(self, value: int):
            """
            Getter for property Color
            Object color
            Setter for property Color
            Object color

            """
            pass
        @property
        def Font(self) -> NXOpen.ViewDependentDisplayManager.Font:
            """
            Getter for property Font
            Object font

            """
            pass
        @Font.setter
        def Font(self, value: NXOpen.ViewDependentDisplayManager.Font):
            """
            Getter for property Font
            Object font
            Setter for property Font
            Object font

            """
            pass
        @property
        def Width(self) -> NXOpen.ViewDependentDisplayManager.Width:
            """
            Getter for property Width
            Object width

            """
            pass
        @Width.setter
        def Width(self, value: NXOpen.ViewDependentDisplayManager.Width):
            """
            Getter for property Width
            Object width
            Setter for property Width
            Object width

            """
            pass
    def GetFlatPatternAllCalloutTypeDisplay(self) -> List[FlatPatternSettings.FlatPatternCalloutTypeDisplay]:
        """
         Returns the dialog names, identifiers, and enabled status for all the
                    available callout types. 
         Returns displayData ( FlatPatternSettings.FlatPatternCalloutTypeDisplay List[NXOpen):  Array of structures with the callout type display data. .
        """
        pass
    def GetFlatPatternAllObjectTypeDisplay(self) -> List[FlatPatternSettings.FlatPatternObjectTypeDisplay]:
        """
         Returns the types, colors, fonts, widths, and enabled status for all
                    the available object types. 
         Returns displayData ( FlatPatternSettings.FlatPatternObjectTypeDisplay List[NXOpen):  Array of structures with the object type display data. .
        """
        pass
    def GetFlatPatternCalloutTypeDisplay(self, calloutType: str) -> FlatPatternSettings.FlatPatternCalloutTypeDisplay:
        """
         Returns the display data for a callout type. The name member of the
                    NXOpen.SheetMetal.FlatPatternSettings.FlatPatternCalloutTypeDisplay
                    is separately allocated from the callout_type argument string. 
                    In some cases the new string will contain an
                    extended form of the callout_type passed in, and that form should
                    be used for subsequent calls, without modification. 
         Returns displayData ( FlatPatternSettings.FlatPatternCalloutTypeDisplay NXOpen.S):  The display data for the callout type. .
        """
        pass
    def GetFlatPatternObjectTypeDisplay(self, objectType: FlatPatternSettings.FlatPatternObjectType) -> FlatPatternSettings.FlatPatternObjectTypeDisplay:
        """
         Returns the display data for a flat pattern object type. 
         Returns displayData ( FlatPatternSettings.FlatPatternObjectTypeDisplay NXOpen.S):  The display data for the flat pattern object type. .
        """
        pass
    def SetFlatPatternCalloutTypeDisplay(self, calloutType: str, displayData: FlatPatternSettings.FlatPatternCalloutTypeDisplay) -> None:
        """
         Sets the display data for a callout type. 
        """
        pass
    def SetFlatPatternObjectTypeDisplay(self, objectType: FlatPatternSettings.FlatPatternObjectType, displayData: FlatPatternSettings.FlatPatternObjectTypeDisplay) -> None:
        """
         Sets the display data for a flat pattern object type. 
        """
        pass
