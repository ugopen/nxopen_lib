from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Provides access to object and callout properties for sheet-metal data in
##         flat pattern views on drawings. The class is created upon a query to
##         obtain the FlatPatternView object from either a view (style) or a 
##         part (preferences).  <br> This class is not created directly by the user.  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class FlatPatternSettings(NXOpen.TaggedObject): 
    """ Provides access to object and callout properties for sheet-metal data in
        flat pattern views on drawings. The class is created upon a query to
        obtain the FlatPatternView object from either a view (style) or a 
        part (preferences). """


    ##  The members of the following enumerated type are used to identify
    ##             object types to the FlatPatternView API. These are not the usual
    ##             NX object types; they are ordinary NX objects that are known to
    ##             the flat pattern feature for the type of outline they provide to
    ##             a bend region, joggle region, or lightening hole. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## BendCenterLine</term><description> 
    ##  Deprecated </description> </item><item><term> 
    ## BendUpCenterLine</term><description> 
    ##  </description> </item><item><term> 
    ## BendDownCenterLine</term><description> 
    ##  </description> </item><item><term> 
    ## BendTangentLine</term><description> 
    ##  </description> </item><item><term> 
    ## OuterMoldLine</term><description> 
    ##  </description> </item><item><term> 
    ## InnerMoldLine</term><description> 
    ##  </description> </item><item><term> 
    ## ExteriorCurves</term><description> 
    ##  </description> </item><item><term> 
    ## InteriorCurves</term><description> 
    ##  Deprecated </description> </item><item><term> 
    ## InteriorCutoutCurves</term><description> 
    ##  </description> </item><item><term> 
    ## InteriorFeatureCurves</term><description> 
    ##  </description> </item><item><term> 
    ## LighteningHoleCenter</term><description> 
    ##  </description> </item><item><term> 
    ## JoggleLine</term><description> 
    ##  </description> </item><item><term> 
    ## AddedTopGeometry</term><description> 
    ##  </description> </item><item><term> 
    ## AddedBottomGeometry</term><description> 
    ##  </description> </item><item><term> 
    ## ToolMarker</term><description> 
    ##  </description> </item><item><term> 
    ## Hole</term><description> 
    ##  </description> </item><item><term> 
    ## Centermark</term><description> 
    ##  </description> </item></list>
    class FlatPatternObjectType(Enum):
        """
        Members Include: <BendCenterLine> <BendUpCenterLine> <BendDownCenterLine> <BendTangentLine> <OuterMoldLine> <InnerMoldLine> <ExteriorCurves> <InteriorCurves> <InteriorCutoutCurves> <InteriorFeatureCurves> <LighteningHoleCenter> <JoggleLine> <AddedTopGeometry> <AddedBottomGeometry> <ToolMarker> <Hole> <Centermark>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FlatPatternSettings.FlatPatternObjectType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The members of the following structure are the display data for a
    ##             callout in a flat pattern drawing member view. 
    ## @link FlatPatternSettingsFlatPatternCalloutTypeDisplay_Struct NXOpen.SheetMetal.FlatPatternSettingsFlatPatternCalloutTypeDisplay_Struct@endlink is an alias for @link FlatPatternSettings.FlatPatternCalloutTypeDisplay NXOpen.SheetMetal.FlatPatternSettings.FlatPatternCalloutTypeDisplay@endlink.
    class FlatPatternCalloutTypeDisplay:
        """
         The members of the following structure are the display data for a
                    callout in a flat pattern drawing member view. 
        @link FlatPatternSettingsFlatPatternCalloutTypeDisplay_Struct NXOpen.SheetMetal.FlatPatternSettingsFlatPatternCalloutTypeDisplay_Struct@endlink is an alias for @link FlatPatternSettings.FlatPatternCalloutTypeDisplay NXOpen.SheetMetal.FlatPatternSettings.FlatPatternCalloutTypeDisplay@endlink.
        """
        ## Getter for property :(str) Type
        ## The name of the callout type.
        ## @return str
        @property
        def Type(self) -> str:
            """
            Getter for property Type
            The name of the callout type.

            """
            pass
        
        ## Setter for property :(str) Type
        @Type.setter
        def Type(self, value: str):
            """
            Getter for property Type
            The name of the callout type.
            Setter for property Type
            The name of the callout type.

            """
            pass
        
        ## Getter for property :(int) IsEnabled
        ## Enabled status for the callout type.
        ## @return int
        @property
        def IsEnabled(self) -> int:
            """
            Getter for property IsEnabled
            Enabled status for the callout type.

            """
            pass
        
        ## Setter for property :(int) IsEnabled
        @IsEnabled.setter
        def IsEnabled(self, value: int):
            """
            Getter for property IsEnabled
            Enabled status for the callout type.
            Setter for property IsEnabled
            Enabled status for the callout type.

            """
            pass
        
        ## Getter for property :(str) Name
        ## dialog name for the callout type.
        ## @return str
        @property
        def Name(self) -> str:
            """
            Getter for property Name
            dialog name for the callout type.

            """
            pass
        
        ## Setter for property :(str) Name
        @Name.setter
        def Name(self, value: str):
            """
            Getter for property Name
            dialog name for the callout type.
            Setter for property Name
            dialog name for the callout type.

            """
            pass
        
    
    
    ##  The members of the following structure are the display data for an
    ##             object in a flat pattern drawing member view. 
    ## @link FlatPatternSettingsFlatPatternObjectTypeDisplay_Struct NXOpen.SheetMetal.FlatPatternSettingsFlatPatternObjectTypeDisplay_Struct@endlink is an alias for @link FlatPatternSettings.FlatPatternObjectTypeDisplay NXOpen.SheetMetal.FlatPatternSettings.FlatPatternObjectTypeDisplay@endlink.
    class FlatPatternObjectTypeDisplay:
        """
         The members of the following structure are the display data for an
                    object in a flat pattern drawing member view. 
        @link FlatPatternSettingsFlatPatternObjectTypeDisplay_Struct NXOpen.SheetMetal.FlatPatternSettingsFlatPatternObjectTypeDisplay_Struct@endlink is an alias for @link FlatPatternSettings.FlatPatternObjectTypeDisplay NXOpen.SheetMetal.FlatPatternSettings.FlatPatternObjectTypeDisplay@endlink.
        """
        ## Getter for property :(@link FlatPatternSettings.FlatPatternObjectType NXOpen.SheetMetal.FlatPatternSettings.FlatPatternObjectType@endlink) Type
        ## Object type
        ## @return @link FlatPatternSettings.FlatPatternObjectType NXOpen.SheetMetal.FlatPatternSettings.FlatPatternObjectType@endlink
        @property
        def Type(self) -> FlatPatternSettings.FlatPatternObjectType:
            """
            Getter for property Type
            Object type

            """
            pass
        
        ## Setter for property :(@link FlatPatternSettings.FlatPatternObjectType NXOpen.SheetMetal.FlatPatternSettings.FlatPatternObjectType@endlink) Type
        @Type.setter
        def Type(self, value: FlatPatternSettings.FlatPatternObjectType):
            """
            Getter for property Type
            Object type
            Setter for property Type
            Object type

            """
            pass
        
        ## Getter for property :(int) IsEnabled
        ## Enabled status for the object type
        ## @return int
        @property
        def IsEnabled(self) -> int:
            """
            Getter for property IsEnabled
            Enabled status for the object type

            """
            pass
        
        ## Setter for property :(int) IsEnabled
        @IsEnabled.setter
        def IsEnabled(self, value: int):
            """
            Getter for property IsEnabled
            Enabled status for the object type
            Setter for property IsEnabled
            Enabled status for the object type

            """
            pass
        
        ## Getter for property :(int) Color
        ## Object color
        ## @return int
        @property
        def Color(self) -> int:
            """
            Getter for property Color
            Object color

            """
            pass
        
        ## Setter for property :(int) Color
        @Color.setter
        def Color(self, value: int):
            """
            Getter for property Color
            Object color
            Setter for property Color
            Object color

            """
            pass
        
        ## Getter for property :(@link NXOpen.ViewDependentDisplayManager.Font NXOpen.ViewDependentDisplayManager.Font@endlink) Font
        ## Object font
        ## @return @link NXOpen.ViewDependentDisplayManager.Font NXOpen.ViewDependentDisplayManager.Font@endlink
        @property
        def Font(self) -> NXOpen.ViewDependentDisplayManager.Font:
            """
            Getter for property Font
            Object font

            """
            pass
        
        ## Setter for property :(@link NXOpen.ViewDependentDisplayManager.Font NXOpen.ViewDependentDisplayManager.Font@endlink) Font
        @Font.setter
        def Font(self, value: NXOpen.ViewDependentDisplayManager.Font):
            """
            Getter for property Font
            Object font
            Setter for property Font
            Object font

            """
            pass
        
        ## Getter for property :(@link NXOpen.ViewDependentDisplayManager.Width NXOpen.ViewDependentDisplayManager.Width@endlink) Width
        ## Object width
        ## @return @link NXOpen.ViewDependentDisplayManager.Width NXOpen.ViewDependentDisplayManager.Width@endlink
        @property
        def Width(self) -> NXOpen.ViewDependentDisplayManager.Width:
            """
            Getter for property Width
            Object width

            """
            pass
        
        ## Setter for property :(@link NXOpen.ViewDependentDisplayManager.Width NXOpen.ViewDependentDisplayManager.Width@endlink) Width
        @Width.setter
        def Width(self, value: NXOpen.ViewDependentDisplayManager.Width):
            """
            Getter for property Width
            Object width
            Setter for property Width
            Object width

            """
            pass
        
    
    
    ##  Returns the dialog names, identifiers, and enabled status for all the
    ##             available callout types. 
    ##  @return displayData (@link FlatPatternSettings.FlatPatternCalloutTypeDisplay List[NXOpen.SheetMetal.FlatPatternSettings.FlatPatternCalloutTypeDisplay]@endlink):  Array of structures with the callout type display data. .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_sheet_metal ("NX Sheet Metal")
    def GetFlatPatternAllCalloutTypeDisplay(self) -> List[FlatPatternSettings.FlatPatternCalloutTypeDisplay]:
        """
         Returns the dialog names, identifiers, and enabled status for all the
                    available callout types. 
         @return displayData (@link FlatPatternSettings.FlatPatternCalloutTypeDisplay List[NXOpen.SheetMetal.FlatPatternSettings.FlatPatternCalloutTypeDisplay]@endlink):  Array of structures with the callout type display data. .
        """
        pass
    
    ##  Returns the types, colors, fonts, widths, and enabled status for all
    ##             the available object types. 
    ##  @return displayData (@link FlatPatternSettings.FlatPatternObjectTypeDisplay List[NXOpen.SheetMetal.FlatPatternSettings.FlatPatternObjectTypeDisplay]@endlink):  Array of structures with the object type display data. .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_sheet_metal ("NX Sheet Metal")
    def GetFlatPatternAllObjectTypeDisplay(self) -> List[FlatPatternSettings.FlatPatternObjectTypeDisplay]:
        """
         Returns the types, colors, fonts, widths, and enabled status for all
                    the available object types. 
         @return displayData (@link FlatPatternSettings.FlatPatternObjectTypeDisplay List[NXOpen.SheetMetal.FlatPatternSettings.FlatPatternObjectTypeDisplay]@endlink):  Array of structures with the object type display data. .
        """
        pass
    
    ##  Returns the display data for a callout type. The name member of the
    ##             @link NXOpen::SheetMetal::FlatPatternSettings::FlatPatternCalloutTypeDisplay NXOpen::SheetMetal::FlatPatternSettings::FlatPatternCalloutTypeDisplay@endlink 
    ##             is separately allocated from the callout_type argument string. 
    ##             In some cases the new string will contain an
    ##             extended form of the callout_type passed in, and that form should
    ##             be used for subsequent calls, without modification. 
    ##  @return displayData (@link FlatPatternSettings.FlatPatternCalloutTypeDisplay NXOpen.SheetMetal.FlatPatternSettings.FlatPatternCalloutTypeDisplay@endlink):  The display data for the callout type. .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_sheet_metal ("NX Sheet Metal")
    ## 
    ## <param name="calloutType"> (str)  The name of the callout type for which to get the display data. </param>
    def GetFlatPatternCalloutTypeDisplay(self, calloutType: str) -> FlatPatternSettings.FlatPatternCalloutTypeDisplay:
        """
         Returns the display data for a callout type. The name member of the
                    @link NXOpen::SheetMetal::FlatPatternSettings::FlatPatternCalloutTypeDisplay NXOpen::SheetMetal::FlatPatternSettings::FlatPatternCalloutTypeDisplay@endlink 
                    is separately allocated from the callout_type argument string. 
                    In some cases the new string will contain an
                    extended form of the callout_type passed in, and that form should
                    be used for subsequent calls, without modification. 
         @return displayData (@link FlatPatternSettings.FlatPatternCalloutTypeDisplay NXOpen.SheetMetal.FlatPatternSettings.FlatPatternCalloutTypeDisplay@endlink):  The display data for the callout type. .
        """
        pass
    
    ##  Returns the display data for a flat pattern object type. 
    ##  @return displayData (@link FlatPatternSettings.FlatPatternObjectTypeDisplay NXOpen.SheetMetal.FlatPatternSettings.FlatPatternObjectTypeDisplay@endlink):  The display data for the flat pattern object type. .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_sheet_metal ("NX Sheet Metal")
    ## 
    ## <param name="objectType"> (@link FlatPatternSettings.FlatPatternObjectType NXOpen.SheetMetal.FlatPatternSettings.FlatPatternObjectType@endlink)  The object type for which to return the display data. </param>
    def GetFlatPatternObjectTypeDisplay(self, objectType: FlatPatternSettings.FlatPatternObjectType) -> FlatPatternSettings.FlatPatternObjectTypeDisplay:
        """
         Returns the display data for a flat pattern object type. 
         @return displayData (@link FlatPatternSettings.FlatPatternObjectTypeDisplay NXOpen.SheetMetal.FlatPatternSettings.FlatPatternObjectTypeDisplay@endlink):  The display data for the flat pattern object type. .
        """
        pass
    
    ##  Sets the display data for a callout type. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_sheet_metal ("NX Sheet Metal")
    ## 
    ## <param name="calloutType"> (str)  The name of the callout type for which to set the display data. </param>
    ## <param name="displayData"> (@link FlatPatternSettings.FlatPatternCalloutTypeDisplay NXOpen.SheetMetal.FlatPatternSettings.FlatPatternCalloutTypeDisplay@endlink)  The display data for the callout type. </param>
    def SetFlatPatternCalloutTypeDisplay(self, calloutType: str, displayData: FlatPatternSettings.FlatPatternCalloutTypeDisplay) -> None:
        """
         Sets the display data for a callout type. 
        """
        pass
    
    ##  Sets the display data for a flat pattern object type. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_sheet_metal ("NX Sheet Metal")
    ## 
    ## <param name="objectType"> (@link FlatPatternSettings.FlatPatternObjectType NXOpen.SheetMetal.FlatPatternSettings.FlatPatternObjectType@endlink)  The object type for which to get the display data. </param>
    ## <param name="displayData"> (@link FlatPatternSettings.FlatPatternObjectTypeDisplay NXOpen.SheetMetal.FlatPatternSettings.FlatPatternObjectTypeDisplay@endlink)  The display data for the flat pattern object type. </param>
    def SetFlatPatternObjectTypeDisplay(self, objectType: FlatPatternSettings.FlatPatternObjectType, displayData: FlatPatternSettings.FlatPatternObjectTypeDisplay) -> None:
        """
         Sets the display data for a flat pattern object type. 
        """
        pass
    
## @package NXOpen.SheetMetal
## Classes, Enums and Structs under NXOpen.SheetMetal namespace

## @link FlatPatternSettingsFlatPatternCalloutTypeDisplay_Struct NXOpen.SheetMetal.FlatPatternSettingsFlatPatternCalloutTypeDisplay_Struct@endlink is an alias for @link FlatPatternSettings.FlatPatternCalloutTypeDisplay NXOpen.SheetMetal.FlatPatternSettings.FlatPatternCalloutTypeDisplay@endlink.
FlatPatternSettingsFlatPatternCalloutTypeDisplay_Struct = FlatPatternSettings.FlatPatternCalloutTypeDisplay


## @link FlatPatternSettingsFlatPatternObjectTypeDisplay_Struct NXOpen.SheetMetal.FlatPatternSettingsFlatPatternObjectTypeDisplay_Struct@endlink is an alias for @link FlatPatternSettings.FlatPatternObjectTypeDisplay NXOpen.SheetMetal.FlatPatternSettings.FlatPatternObjectTypeDisplay@endlink.
FlatPatternSettingsFlatPatternObjectTypeDisplay_Struct = FlatPatternSettings.FlatPatternObjectTypeDisplay


##  @link FlatPatternSettingsFlatPatternObjectType NXOpen.SheetMetal.FlatPatternSettingsFlatPatternObjectType @endlink is an alias for @link FlatPatternSettings.FlatPatternObjectType NXOpen.SheetMetal.FlatPatternSettings.FlatPatternObjectType@endlink
FlatPatternSettingsFlatPatternObjectType = FlatPatternSettings.FlatPatternObjectType


